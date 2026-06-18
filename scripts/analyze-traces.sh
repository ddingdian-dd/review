#!/usr/bin/env bash
# analyze-traces.sh - 聚合 ~/.claude/traces/，为复盘报告提供 AI 执行数据
#
# 用法：
#   bash analyze-traces.sh                     # 今天（JSON）
#   bash analyze-traces.sh today --markdown    # 今天（Markdown）
#   bash analyze-traces.sh yesterday
#   bash analyze-traces.sh 2026-04-29
#   bash analyze-traces.sh 2026-04-22 2026-04-28       # 周范围
#   bash analyze-traces.sh this-week --markdown
#
# Why：Traces 是 Agent 执行日志的唯一真相来源。LLM 记忆会漂移，
# 但 trace.json 的执行耗时、步骤、状态永远精确。让脚本聚合，不让 LLM 数数。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HELPER="$SCRIPT_DIR/_analyze_traces.py"

MARKDOWN=""
CANDIDATES=""
ARGS=()
for a in "$@"; do
  if [[ "$a" == "--markdown" ]]; then
    MARKDOWN="--markdown"
  elif [[ "$a" == "--candidates" ]]; then
    CANDIDATES="--candidates"
  else
    ARGS+=("$a")
  fi
done

# 日期解析（macOS BSD date / Linux GNU date 兼容）
date_cmd() {
  if date -v-1d +%Y-%m-%d >/dev/null 2>&1; then
    # BSD
    case "$1" in
      yesterday) date -v-1d +%Y-%m-%d ;;
      mon-of-week) date -v-mon +%Y-%m-%d ;;
      mon-of-last-week) date -v-mon -v-7d +%Y-%m-%d ;;
      sun-of-last-week) date -v-sun -v-7d +%Y-%m-%d ;;
    esac
  else
    # GNU
    case "$1" in
      yesterday) date -d "yesterday" +%Y-%m-%d ;;
      mon-of-week) date -d "last monday" +%Y-%m-%d ;;
      mon-of-last-week) date -d "last monday -7 days" +%Y-%m-%d ;;
      sun-of-last-week) date -d "last sunday -7 days" +%Y-%m-%d ;;
    esac
  fi
}

if [[ ${#ARGS[@]} -eq 0 ]]; then
  SINCE=$(date +%Y-%m-%d); UNTIL="$SINCE"
elif [[ ${#ARGS[@]} -eq 1 ]]; then
  case "${ARGS[0]}" in
    today)      SINCE=$(date +%Y-%m-%d); UNTIL="$SINCE" ;;
    yesterday)  SINCE=$(date_cmd yesterday); UNTIL="$SINCE" ;;
    this-week)  SINCE=$(date_cmd mon-of-week); UNTIL=$(date +%Y-%m-%d) ;;
    last-week)  SINCE=$(date_cmd mon-of-last-week); UNTIL=$(date_cmd sun-of-last-week) ;;
    this-month) SINCE=$(date +%Y-%m-01); UNTIL=$(date +%Y-%m-%d) ;;
    *)          SINCE="${ARGS[0]}"; UNTIL="${ARGS[0]}" ;;
  esac
else
  SINCE="${ARGS[0]}"; UNTIL="${ARGS[1]}"
fi

python3 "$HELPER" "$SINCE" "$UNTIL" $MARKDOWN $CANDIDATES
