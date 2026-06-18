#!/usr/bin/env python3
"""Token 消耗与成本估算 v2：基于 violations.jsonl + trace.json + user-prompts.jsonl。

v2 改进：当 trace.json 无 token 数据时，用 user-prompts.jsonl 估算总消耗。
估算公式：prompt 数 × (平均输入 800 + 平均输出 2000) = 总 token

用法：python3 _calculate_token_usage.py <since> <until> [--markdown]
"""
import json
import sys
from datetime import datetime
from pathlib import Path
from collections import Counter

AVG_INPUT_PER_PROMPT = 800
AVG_OUTPUT_PER_PROMPT = 2000

if len(sys.argv) < 3:
    print("Usage: python3 _calculate_token_usage.py <since> <until> [--markdown]", file=sys.stderr)
    sys.exit(2)

since_str, until_str = sys.argv[1], sys.argv[2]
markdown = "--markdown" in sys.argv

try:
    since = datetime.strptime(since_str, "%Y-%m-%d")
    until = datetime.strptime(until_str + " 23:59:59", "%Y-%m-%d %H:%M:%S")
except ValueError as e:
    print(f"Invalid date: {e}", file=sys.stderr)
    sys.exit(2)

TRACES_DIR = Path.home() / ".claude" / "traces"
VIOLATIONS = TRACES_DIR / "violations.jsonl"
PROMPTS = TRACES_DIR / "user-prompts.jsonl"

# 定价表（USD per million tokens，2026-04 Claude 定价）
PRICING = {
    "sonnet": {"input": 3.0, "output": 15.0},
    "haiku": {"input": 1.0, "output": 5.0},
    "opus": {"input": 15.0, "output": 75.0},
}


def parse_iso(ts: str):
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d"):
        try:
            return datetime.strptime(ts, fmt)
        except ValueError:
            continue
    return None


# --- 从 violations 累计节省量 ---
saved_tokens_total = 0
saved_by_rule = Counter()

if VIOLATIONS.exists():
    with VIOLATIONS.open(encoding="utf-8") as f:
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
            saved = int(v.get("saved_tokens", 0) or 0)
            saved_tokens_total += saved
            saved_by_rule[v.get("rule", "unknown")] += saved

# --- 从 traces 提取实际 token 使用 ---
tokens_input = 0
tokens_output = 0
trace_count = 0
model_usage = Counter()

for trace_file in TRACES_DIR.rglob("trace.json"):
    try:
        data = json.loads(trace_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        continue
    ts = parse_iso(data.get("timestamp", ""))
    if ts is None or not (since <= ts <= until):
        continue

    meta = data.get("metadata", {})
    tokens = meta.get("tokens", {})
    if tokens:
        tokens_input += int(tokens.get("input", 0) or 0)
        tokens_output += int(tokens.get("output", 0) or 0)
        trace_count += 1
    model_usage[meta.get("model", "unknown")] += 1


def price(model_name: str) -> dict:
    """根据模型名猜定价档位。"""
    m = model_name.lower()
    for key in PRICING:
        if key in m:
            return PRICING[key]
    return PRICING["sonnet"]  # 默认


# --- 从 user-prompts.jsonl 估算（当 trace.json 无数据时的 fallback）---
prompt_count = 0
if PROMPTS.exists():
    with PROMPTS.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = parse_iso(rec.get("timestamp", rec.get("ts", "")))
            if ts and since <= ts <= until:
                prompt_count += 1

estimated_input = prompt_count * AVG_INPUT_PER_PROMPT
estimated_output = prompt_count * AVG_OUTPUT_PER_PROMPT

# 按 Sonnet 4.5 估算成本（主力模型）
p = PRICING["sonnet"]

# 优先用 trace.json 实际数据，否则用 prompt 估算
if tokens_input > 0 or tokens_output > 0:
    final_input = tokens_input
    final_output = tokens_output
    data_source = "trace.json（精确）"
else:
    final_input = estimated_input
    final_output = estimated_output
    data_source = "user-prompts.jsonl（估算，~800 tok/prompt 输入 + ~2000 tok/prompt 输出）"

cost_usd = (final_input / 1_000_000) * p["input"] + (final_output / 1_000_000) * p["output"]

# 节省金额（按混合价估算）
saved_cost_usd = (saved_tokens_total / 1_000_000) * ((p["input"] + p["output"]) / 2)

total_tokens = final_input + final_output

# --- 输出 ---
if markdown:
    print(f"## Token 消耗分析 {since_str} ~ {until_str}\n")
    print("### 实际消耗（来自 trace.json）")
    print("| 维度 | 数值 |")
    print("|---|---|")
    print(f"| Trace 样本数 | {trace_count} |")
    print(f"| 输入 Token | {tokens_input:,} |")
    print(f"| 输出 Token | {tokens_output:,} |")
    print(f"| 合计 | {total_tokens:,} |")
    print(f"| 估算成本（按 Sonnet 4.5） | ${cost_usd:.4f} |")
    if trace_count == 0 and prompt_count > 0:
        print(f"\n> 📊 数据来源：{data_source}（{prompt_count} 条 prompt）")
    elif trace_count == 0:
        print("\n> ⚠️ 无任何 token 数据源（trace.json 未填充，user-prompts.jsonl 无记录）。")
    print()
    print("### Token 节省（来自 violations.jsonl）")
    print("| 维度 | 数值 |")
    print("|---|---|")
    print(f"| 节省总量 | {saved_tokens_total:,} |")
    print(f"| 折合节省成本 | ${saved_cost_usd:.4f} |")
    if saved_by_rule:
        print("\n### 节省 Top 规则")
        for r, c in saved_by_rule.most_common(5):
            print(f"- {r}: {c:,}")
    if model_usage:
        print("\n### 模型使用分布")
        for m, c in model_usage.most_common():
            print(f"- {m}: {c} 次")
else:
    output = {
        "date_range": {"since": since_str, "until": until_str},
        "usage": {
            "trace_count": trace_count,
            "tokens_input": tokens_input,
            "tokens_output": tokens_output,
            "tokens_total": total_tokens,
            "cost_usd": round(cost_usd, 4),
            "pricing_basis": "sonnet-4.5",
            "data_source": data_source,
            "prompt_count": prompt_count,
        },
        "saved": {
            "saved_tokens": saved_tokens_total,
            "saved_cost_usd": round(saved_cost_usd, 4),
            "by_rule": dict(saved_by_rule.most_common(10)),
        },
        "models": dict(model_usage),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
