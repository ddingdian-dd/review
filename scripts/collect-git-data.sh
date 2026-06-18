#!/usr/bin/env bash

# Git 数据采集脚本
# 用途：为日报/周报/月报自动采集 Git 提交数据
# 使用：./collect-git-data.sh [日期范围] [输出格式]

set -e

# ============================================
# 参数解析
# ============================================

SINCE=""
UNTIL=""
FORMAT="json"  # 默认输出 json 格式，可选 "markdown"

# 解析日期范围参数
if [ $# -eq 0 ]; then
    # 无参数：采集今日数据
    SINCE="$(date +%Y-%m-%d) 00:00:00"
    UNTIL="$(date +%Y-%m-%d) 23:59:59"
elif [ $# -eq 1 ]; then
    # 1个参数：自动识别类型
    case "$1" in
        today)
            SINCE="$(date +%Y-%m-%d) 00:00:00"
            UNTIL="$(date +%Y-%m-%d) 23:59:59"
            ;;
        yesterday)
            SINCE="$(date -v-1d +%Y-%m-%d) 00:00:00"
            UNTIL="$(date -v-1d +%Y-%m-%d) 23:59:59"
            ;;
        this-week)
            # 本周一 00:00:00 到现在
            SINCE="$(date -v-mon +%Y-%m-%d) 00:00:00"
            UNTIL="$(date +%Y-%m-%d) 23:59:59"
            ;;
        last-week)
            # 上周一到上周日
            SINCE="$(date -v-2mon -v+mon +%Y-%m-%d) 00:00:00"
            UNTIL="$(date -v-mon -v+sun +%Y-%m-%d) 23:59:59"
            ;;
        this-month)
            # 本月1号到现在
            SINCE="$(date -v1d +%Y-%m)-01 00:00:00"
            UNTIL="$(date +%Y-%m-%d) 23:59:59"
            ;;
        *)
            # 假设是日期格式 YYYY-MM-DD
            SINCE="$1 00:00:00"
            UNTIL="$1 23:59:59"
            ;;
    esac
elif [ $# -eq 2 ]; then
    # 2个参数：开始和结束日期
    SINCE="$1 00:00:00"
    UNTIL="$2 23:59:59"
fi

# 第二个参数可能是输出格式
if [ $# -eq 2 ] && [[ "$2" == "markdown" || "$2" == "json" ]]; then
    FORMAT="$2"
fi

# ============================================
# 数据采集
# ============================================

# 检查是否在 git 仓库中
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "错误: 当前目录不是 git 仓库" >&2
    exit 1
fi

# 采集提交记录（带统计信息）
COMMITS=$(git log --since="$SINCE" --until="$UNTIL" --numstat --format="COMMIT:%H|%an|%ae|%at|%s" 2>/dev/null || true)

# 解析数据
COMMIT_COUNT=0
LINES_ADDED=0
LINES_DELETED=0
FILES_MODIFIED=0

if [ -n "$COMMITS" ]; then
    while IFS= read -r line; do
        if [[ "$line" == COMMIT:* ]]; then
            COMMIT_COUNT=$((COMMIT_COUNT + 1))
        elif [[ "$line" =~ ^[0-9]+[[:space:]]+[0-9]+[[:space:]] ]]; then
            read -r added deleted filename <<< "$line"
            if [[ "$added" != "-" && "$deleted" != "-" ]]; then
                LINES_ADDED=$((LINES_ADDED + added))
                LINES_DELETED=$((LINES_DELETED + deleted))
            fi
        fi
    done <<< "$COMMITS"
    FILES_MODIFIED=$(echo "$COMMITS" | grep -E '^[0-9]+[[:space:]]+[0-9]+[[:space:]]' | awk '{print $3}' | sort -u | wc -l | tr -d ' ')
fi

NET_CHANGE=$((LINES_ADDED - LINES_DELETED))

# 计算工作时长（基于提交时间戳）
TIMESTAMPS=$(git log --since="$SINCE" --until="$UNTIL" --format="%at" 2>/dev/null | sort -n)
WORK_HOURS=0.0

if [ -n "$TIMESTAMPS" ]; then
    # 计算首次提交到最后提交的时间跨度
    FIRST_COMMIT=$(echo "$TIMESTAMPS" | head -1)
    LAST_COMMIT=$(echo "$TIMESTAMPS" | tail -1)
    if [ "$FIRST_COMMIT" != "$LAST_COMMIT" ]; then
        TIME_SPAN=$((LAST_COMMIT - FIRST_COMMIT))
        WORK_HOURS=$(echo "scale=1; $TIME_SPAN / 3600" | bc)
    fi
fi

# 统计新增和修改的文件
NEW_FILES=$(git log --since="$SINCE" --until="$UNTIL" --diff-filter=A --name-only --format="" 2>/dev/null | sort -u | wc -l | tr -d ' ')
MODIFIED_FILES=$(git log --since="$SINCE" --until="$UNTIL" --diff-filter=M --name-only --format="" 2>/dev/null | sort -u | wc -l | tr -d ' ')

# ============================================
# 输出结果
# ============================================

if [ "$FORMAT" == "json" ]; then
    # JSON 格式输出
    cat <<EOF
{
  "date_range": {
    "since": "$SINCE",
    "until": "$UNTIL"
  },
  "summary": {
    "commit_count": $COMMIT_COUNT,
    "lines_added": $LINES_ADDED,
    "lines_deleted": $LINES_DELETED,
    "net_change": $NET_CHANGE,
    "files_modified": $FILES_MODIFIED,
    "new_files": $NEW_FILES,
    "modified_files": $MODIFIED_FILES,
    "work_hours": $WORK_HOURS
  }
}
EOF
else
    # Markdown 格式输出
    cat <<EOF
## Git 数据汇总

**时间范围**: $SINCE 至 $UNTIL

| 维度 | 数值 |
|------|------|
| Git 提交 | $COMMIT_COUNT 次 |
| 代码新增 | $LINES_ADDED 行 |
| 代码删除 | $LINES_DELETED 行 |
| 净变更 | $NET_CHANGE 行 |
| 新增文件 | $NEW_FILES 个 |
| 修改文件 | $MODIFIED_FILES 个 |
| 工作时长 | 约 $WORK_HOURS 小时 |
EOF
fi
