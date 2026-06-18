#!/usr/bin/env python3
"""Traces 聚合分析：扫描 ~/.claude/traces/ 下的 trace.json + violations.jsonl。

用法：python3 _analyze_traces.py <since> <until> [--markdown]
日期格式：YYYY-MM-DD

被 analyze-traces.sh 调用。
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from collections import Counter

if len(sys.argv) < 3:
    print("Usage: python3 _analyze_traces.py <since> <until> [--markdown|--candidates]", file=sys.stderr)
    sys.exit(2)

since_str, until_str = sys.argv[1], sys.argv[2]
markdown = "--markdown" in sys.argv
candidates_mode = "--candidates" in sys.argv

try:
    since = datetime.strptime(since_str, "%Y-%m-%d")
    until = datetime.strptime(until_str + " 23:59:59", "%Y-%m-%d %H:%M:%S")
except ValueError as e:
    print(f"Invalid date: {e}", file=sys.stderr)
    sys.exit(2)

TRACES_DIR = Path.home() / ".claude" / "traces"
VIOLATIONS_FILE = TRACES_DIR / "violations.jsonl"


def parse_iso(ts: str):
    """容错解析 trace 的 timestamp。"""
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d"):
        try:
            return datetime.strptime(ts, fmt)
        except ValueError:
            continue
    return None


# --- 扫描 trace.json ---
stats = {
    "total": 0,
    "success": 0,
    "failed": 0,
    "total_duration_ms": 0,
}
by_type = Counter()
by_skill = Counter()
# 候选维度：重复出现的 tool_input / description，可能提示新模式或高频场景
by_tool_input = Counter()
by_description = Counter()
failed_actions = Counter()

for trace_file in TRACES_DIR.rglob("trace.json"):
    try:
        data = json.loads(trace_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        continue

    ts = parse_iso(data.get("timestamp", ""))
    if ts is None or not (since <= ts <= until):
        continue

    stats["total"] += 1
    t = data.get("type", "unknown")
    by_type[t] += 1

    exe = data.get("execution", {})
    status = exe.get("final_status", "unknown")
    if status == "success":
        stats["success"] += 1
    elif status == "failed":
        stats["failed"] += 1

    dur = exe.get("total_duration_ms", 0)
    if isinstance(dur, (int, float)):
        stats["total_duration_ms"] += int(dur)

    for sk in data.get("metadata", {}).get("skills_used", []):
        by_skill[sk] += 1

    task = data.get("task", {})
    ti = task.get("tool_input", "")
    if ti:
        by_tool_input[ti] += 1
    desc = task.get("description", "")
    if desc:
        by_description[desc] += 1

    for step in exe.get("steps", []) or []:
        if isinstance(step, dict) and step.get("status") == "failed":
            failed_actions[step.get("action", "unknown")] += 1

# --- 扫描 violations.jsonl ---
violations = {
    "count": 0,
    "saved_tokens": 0,
    "saved_minutes": 0,
}
violation_rules = Counter()

if VIOLATIONS_FILE.exists():
    with VIOLATIONS_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                v = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = parse_iso(v.get("ts", ""))
            if ts is None or not (since <= ts <= until):
                continue
            violations["count"] += 1
            violations["saved_tokens"] += int(v.get("saved_tokens", 0) or 0)
            violations["saved_minutes"] += int(v.get("saved_minutes", 0) or 0)
            violation_rules[v.get("rule", "unknown")] += 1

# --- 输出 ---

def render_candidates():
    """输出「今日/本周可沉淀到 skill 的候选清单」。

    候选来源：
    1. 失败步骤（action 失败 ≥2 次 → 建议加 hook / 校验脚本）
    2. 高频 tool_input（同一文件/组件引用 ≥3 次 → 建议升级为 P0 组件或独立案例）
    3. 高频 description（相似任务重复出现 → 建议提炼 skill recipe）
    4. Top violations（违规规则高频 → 建议新增挡板）
    5. skill 使用频次（热门 skill → 进入 evals 优先级）
    """
    print(f"## 今日可沉淀候选（{since_str} ~ {until_str}）\n")
    lines = []

    if failed_actions:
        lines.append("### 🔴 失败模式（建议补挡板 / 校验脚本）")
        for action, c in failed_actions.most_common(5):
            if c >= 2:
                lines.append(f"- `{action}` 失败 {c} 次 → 提炼为 hook 或 pre-check 脚本")
        if lines and not lines[-1].startswith("-"):
            lines.pop()
        lines.append("")

    if by_tool_input:
        high_freq = [(x, c) for x, c in by_tool_input.most_common(10) if c >= 3]
        if high_freq:
            lines.append("### 📎 高频引用（建议升级为 skill 组件 / 独立案例）")
            for inp, c in high_freq[:5]:
                snippet = inp if len(inp) <= 80 else inp[:77] + "..."
                lines.append(f"- `{snippet}` 被引用 {c} 次")
            lines.append("")

    if by_description:
        high_freq_desc = [(x, c) for x, c in by_description.most_common(10) if c >= 3]
        if high_freq_desc:
            lines.append("### 🔁 重复任务（建议固化为 recipe / 模板）")
            for desc, c in high_freq_desc[:5]:
                snippet = desc if len(desc) <= 80 else desc[:77] + "..."
                lines.append(f"- `{snippet}` 共 {c} 次")
            lines.append("")

    if violation_rules:
        lines.append("### ⚠️ 高频违规（建议调整 harness 规则）")
        for rule, c in violation_rules.most_common(5):
            if c >= 2:
                lines.append(f"- `{rule}` 触发 {c} 次 → 考虑加强 / 放宽 / 加白名单")
        lines.append("")

    if by_skill:
        lines.append("### 🎯 高频 Skill（建议优先跑 evals）")
        for sk, c in by_skill.most_common(5):
            if c >= 2:
                lines.append(f"- `{sk}` 执行 {c} 次")
        lines.append("")

    if not lines:
        print("本周期内 traces 不足或无明显沉淀候选。继续积累数据 3-7 天后再查看。\n")
    else:
        print("\n".join(lines))


if candidates_mode:
    render_candidates()
    sys.exit(0)

if markdown:
    print(f"## Traces 分析 {since_str} ~ {until_str}\n")
    print("| 维度 | 数值 |")
    print("|---|---|")
    print(f"| Trace 总数 | {stats['total']} |")
    print(f"| 成功 / 失败 | {stats['success']} / {stats['failed']} |")
    print(f"| 总执行时长 | {stats['total_duration_ms'] // 1000}s |")
    print(f"| Violations 触发 | {violations['count']} 次 |")
    print(f"| Token 节省（累计） | {violations['saved_tokens']:,} |")
    print(f"| 时间节省（分钟） | {violations['saved_minutes']} |")
    print()
    if by_type:
        print("### Traces 按类型")
        for t, c in by_type.most_common():
            print(f"- {t}: {c}")
    if by_skill:
        print("\n### 使用的 Skills")
        for s, c in by_skill.most_common():
            print(f"- {s}: {c}")
    if violation_rules:
        print("\n### Top 违规规则")
        for r, c in violation_rules.most_common(5):
            print(f"- {r}: {c}")
else:
    output = {
        "date_range": {"since": since_str, "until": until_str},
        "traces": {
            **stats,
            "by_type": dict(by_type),
            "by_skill": dict(by_skill),
        },
        "violations": {
            **violations,
            "top_rules": dict(violation_rules.most_common(5)),
        },
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
