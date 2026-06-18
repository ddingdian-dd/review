#!/usr/bin/env bash
# detect-repeated-changes.sh - 检测反复修改（效率杀手）
#
# 检测标准：同一个文件被修改 ≥ 3 次，且 commit message 涉及"fix/修复/回滚/revert/改回/重构"等返工词
#
# 用法：
#   bash detect-repeated-changes.sh                      # 今天
#   bash detect-repeated-changes.sh 2026-04-22 2026-04-28
#   bash detect-repeated-changes.sh this-week --markdown
#
# Why：反复修改是效率损失的最大黑洞。
# 同一 bug 改 3 次 = 原本 1 次的工作量 × 3，外加心理成本。
# LLM 记忆会漏数，脚本扫 git log 不会漏。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REWORK_THRESHOLD=3

MARKDOWN=""
ARGS=()
for a in "$@"; do
  if [[ "$a" == "--markdown" ]]; then
    MARKDOWN="--markdown"
  else
    ARGS+=("$a")
  fi
done

# 日期兼容 BSD/GNU
bsd_date() { date -v"$1" +%Y-%m-%d 2>/dev/null; }
gnu_date() { date -d "$1" +%Y-%m-%d 2>/dev/null; }
d_yesterday() { bsd_date -1d || gnu_date "yesterday"; }
d_monday() { bsd_date -mon || gnu_date "last monday"; }

if [[ ${#ARGS[@]} -eq 0 ]]; then
  SINCE=$(date +%Y-%m-%d); UNTIL="$SINCE"
elif [[ ${#ARGS[@]} -eq 1 ]]; then
  case "${ARGS[0]}" in
    today)      SINCE=$(date +%Y-%m-%d); UNTIL="$SINCE" ;;
    yesterday)  SINCE=$(d_yesterday); UNTIL="$SINCE" ;;
    this-week)  SINCE=$(d_monday); UNTIL=$(date +%Y-%m-%d) ;;
    *)          SINCE="${ARGS[0]}"; UNTIL="${ARGS[0]}" ;;
  esac
else
  SINCE="${ARGS[0]}"; UNTIL="${ARGS[1]}"
fi

# 检查 git 仓库
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: 当前目录不是 git 仓库（请 cd 到项目目录再跑）" >&2
  exit 1
fi

# 提取数据传给 Python 分析
python3 "$SCRIPT_DIR/_detect_repeated_changes.py" \
  "$SINCE" "$UNTIL" "$REWORK_THRESHOLD" $MARKDOWN
