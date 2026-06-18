#!/usr/bin/env bash
# calculate-token-usage.sh - 基于 Traces + Violations 估算 Token 消耗与成本
#
# 用法：
#   bash calculate-token-usage.sh 2026-04-29
#   bash calculate-token-usage.sh 2026-04-22 2026-04-28 --markdown
#
# 数据来源：
#   1. ~/.claude/traces/violations.jsonl 的 saved_tokens 字段（已节省的量）
#   2. trace.json 的 metadata.tokens（如有）
#
# Why：Token 成本计算是纯算术，交给脚本。
# 模型定价（2026-04 Claude）：
#   - Sonnet 4.5: $3/MTok 输入, $15/MTok 输出
#   - Haiku 4.5:  $1/MTok 输入, $5/MTok 输出
#   - Opus 4.7:   $15/MTok 输入, $75/MTok 输出
# 默认按 Sonnet 4.5 估算；若需精确，改 trace.json 里的 model 字段。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

MARKDOWN=""
ARGS=()
for a in "$@"; do
  if [[ "$a" == "--markdown" ]]; then
    MARKDOWN="--markdown"
  else
    ARGS+=("$a")
  fi
done

if [[ ${#ARGS[@]} -eq 0 ]]; then
  SINCE=$(date +%Y-%m-%d); UNTIL="$SINCE"
elif [[ ${#ARGS[@]} -eq 1 ]]; then
  SINCE="${ARGS[0]}"; UNTIL="${ARGS[0]}"
else
  SINCE="${ARGS[0]}"; UNTIL="${ARGS[1]}"
fi

python3 "$SCRIPT_DIR/_calculate_token_usage.py" "$SINCE" "$UNTIL" $MARKDOWN
