#!/usr/bin/env python3
"""反复修改检测：从 git log 识别同一文件被反复改动 + 返工关键词。

用法：python3 _detect_repeated_changes.py <since> <until> <threshold> [--markdown]
"""
import subprocess
import sys
import json
import re
from collections import defaultdict, Counter

if len(sys.argv) < 4:
    print("Usage: python3 _detect_repeated_changes.py <since> <until> <threshold> [--markdown]", file=sys.stderr)
    sys.exit(2)

since, until, threshold = sys.argv[1], sys.argv[2], int(sys.argv[3])
markdown = "--markdown" in sys.argv

# 返工关键词（中英混合）
REWORK_KEYWORDS = [
    "fix", "bug", "hotfix", "patch",
    "修复", "修正", "改回", "回滚", "还原",
    "revert", "undo", "rollback",
    "refactor", "rewrite", "redo",
    "重构", "重写", "重新",
    "再次", "再改", "又改", "再修", "又修",
]


def run_git(*args) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        return result.stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return ""


# 获取 commits（哈希 | 日期 | 作者 | 消息）
log_output = run_git(
    "log",
    f"--since={since} 00:00:00",
    f"--until={until} 23:59:59",
    "--format=%H|%ai|%an|%s",
    "--no-merges",
)

commits = []
for line in log_output.strip().split("\n"):
    if not line:
        continue
    parts = line.split("|", 3)
    if len(parts) == 4:
        commits.append({"hash": parts[0], "date": parts[1], "author": parts[2], "msg": parts[3]})

if not commits:
    if markdown:
        print(f"## 反复修改检测 {since} ~ {until}\n")
        print(f"> ✅ 无提交记录，无需检测。")
    else:
        print(json.dumps({"date_range": {"since": since, "until": until}, "repeated": [], "summary": {"total_commits": 0, "rework_commits": 0, "repeated_files": 0}}))
    sys.exit(0)

# 获取每个 commit 修改的文件
file_changes = defaultdict(list)  # filename -> [(commit_hash, msg, date)]
rework_commits = []

for c in commits:
    files_out = run_git("show", "--format=", "--name-only", c["hash"])
    files = [f.strip() for f in files_out.strip().split("\n") if f.strip()]

    msg_lower = c["msg"].lower()
    is_rework = any(kw.lower() in msg_lower for kw in REWORK_KEYWORDS)
    if is_rework:
        rework_commits.append(c)

    for f in files:
        file_changes[f].append({
            "hash": c["hash"][:8],
            "msg": c["msg"],
            "date": c["date"][:10],
            "rework": is_rework,
        })

# 找出被修改 ≥ threshold 的文件
repeated = []
for fname, changes in file_changes.items():
    if len(changes) >= threshold:
        rework_count = sum(1 for x in changes if x["rework"])
        repeated.append({
            "file": fname,
            "change_count": len(changes),
            "rework_count": rework_count,
            "is_rework_pattern": rework_count >= 2,  # 至少 2 次返工 = 模式
            "commits": changes,
        })

# 按返工严重度排序
repeated.sort(key=lambda x: (-x["rework_count"], -x["change_count"]))

if markdown:
    print(f"## 反复修改检测 {since} ~ {until}\n")
    print(f"**总 commit 数**：{len(commits)}")
    print(f"**返工类 commit**：{len(rework_commits)} 次（含 fix/修复/回滚/revert 等关键词）")
    print(f"**被改 ≥ {threshold} 次的文件**：{len(repeated)} 个\n")

    if not repeated:
        print("> ✅ 未发现反复修改，本期效率良好。")
    else:
        print(f"### Top 反复修改文件（排序：返工次数 > 总次数）\n")
        for item in repeated[:10]:
            flag = "🔴" if item["is_rework_pattern"] else "⚠️"
            print(f"{flag} **{item['file']}** — 改动 {item['change_count']} 次，其中返工 {item['rework_count']} 次")
            for c in item["commits"][:5]:
                rw = " 🔁" if c["rework"] else ""
                print(f"   - `{c['hash']}` {c['date']}: {c['msg']}{rw}")
            if len(item["commits"]) > 5:
                print(f"   - ...还有 {len(item['commits']) - 5} 次")
            print()

        print("### 损失估算\n")
        total_rework_commits = sum(x["rework_count"] for x in repeated)
        print(f"- 累计返工 commit：{total_rework_commits} 次")
        print(f"- 预估损失时间：{total_rework_commits * 30} 分钟（按每次 30min 算）")
        print(f"- 建议：针对 🔴 级别文件做根因分析（5 问法），形成规则避免再犯")
else:
    print(json.dumps({
        "date_range": {"since": since, "until": until},
        "summary": {
            "total_commits": len(commits),
            "rework_commits": len(rework_commits),
            "repeated_files": len(repeated),
            "threshold": threshold,
        },
        "repeated": repeated,
    }, ensure_ascii=False, indent=2))
