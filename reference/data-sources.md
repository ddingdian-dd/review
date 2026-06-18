# review 数据源说明

> 所有复盘报告的数据必须来自以下 4 类源。不在这些源里的数据需要明确标注"来自回忆"。

---

## 数据源总表

| 数据源 | 脚本 | 覆盖内容 | 精度 | 覆盖粒度 |
|---|---|---|---|---|
| **Git log** | `collect-git-data.sh` | 代码变更、commit 消息、工作时间窗口 | 完全精确 | 每个 commit |
| **Traces** | `analyze-traces.sh` | AI 执行记录、skill 调用、耗时、成功率 | 完全精确（若有 trace） | 每次任务 |
| **Violations** | `analyze-traces.sh` + `calculate-token-usage.sh` | Token 节省、Hook 触发、规则违反 | 完全精确 | 每次触发 |
| **会议纪要** | 手动 Read | 决策、Action Items、线下讨论 | 依赖记录质量 | 每个议题 |

---

## 1. Git log —— 代码层真相

**存储位置**：每个项目的 `.git/` 目录

**获取方式**：
```bash
# 通用
git log --since="YYYY-MM-DD 00:00:00" --until="YYYY-MM-DD 23:59:59" \
  --all --numstat --no-merges --format="%H|%ai|%an|%s"

# 封装后
bash scripts/collect-git-data.sh 2026-04-29
bash scripts/collect-git-data.sh this-week --markdown
```

**能回答**：
- 今天/本周/本月提交了多少次？
- 改了哪些文件？增加/删除多少行？
- 工作时间窗口（首提交到末提交）？
- 谁改了什么（多人协作）？

**不能回答**：
- 未提交的工作（暂存区 / 未 add）
- 纯讨论类工作（无代码产出）
- AI 工具执行的具体细节

**注意**：
- `collect-git-data.sh` 默认统计**所有作者**。若需区分本人 vs 团队，加 `--author=本人名字`
- macOS 下需要 BSD date，脚本已兼容

---

## 2. Traces —— AI 执行层真相

**存储位置**：`~/.claude/traces/`

**目录结构**：
```
~/.claude/traces/
├── design/              # 设计稿生成
├── code-review/         # 代码审查
├── git-operations/      # Git 操作
├── skill-execution/     # Skill 调用
├── check/               # Check skill 产出
└── violations.jsonl     # 规则违反日志（按行追加）
```

**每个 trace.json 的标准结构**：
```json
{
  "trace_id": "...",
  "type": "design|code-review|git-operation|skill-execution",
  "timestamp": "2026-04-29T10:00:00Z",
  "scope": {"user": "...", "project": "...", "org": "..."},
  "task": {"description": "...", "input": "...", "context": {...}},
  "execution": {
    "steps": [...],
    "total_duration_ms": 11620,
    "final_status": "success|failed"
  },
  "output": {"artifacts": [...], "summary": "..."},
  "feedback": {"rating": "...", "comments": "..."},
  "metadata": {
    "model": "claude-sonnet-4.5",
    "skills_used": ["qxhy-design"],
    "tokens": {"input": 12000, "output": 3000}
  }
}
```

**能回答**：
- AI 今天执行了多少个任务？成功率？
- 每次任务耗时多少？
- 哪些 skill 被调用？
- 模型选型分布（Sonnet vs Haiku vs Opus）？

**缺口**：
- `metadata.tokens` 字段不是所有 trace 都填充（取决于 Hook 配置）
- 需要 Hook 主动写入 trace.json，目前部分类型（如 git-operation）由脚本生成

---

## 3. Violations —— 自动化规则触发

**存储位置**：`~/.claude/traces/violations.jsonl`

**格式**（每行一个 JSON）：
```json
{"ts": "2026-04-28T09:30:55Z", "rule": "daily-report-missing", "severity": "reminded", "context": {...}, "saved_minutes": 0, "saved_tokens": 0}
{"ts": "2026-04-28T09:36:12Z", "rule": "large-file-read", "severity": "warned", "context": {"file": "...", "lines": 3385}, "saved_tokens": 50325}
```

**字段说明**：
- `rule`：触发的规则名（由 Hook 决定）
- `severity`：`reminded` / `warned` / `blocked`
- `saved_minutes` / `saved_tokens`：本次避免的损失量（事前估算值）

**能回答**：
- 本周/本月触发了哪些规则？
- 哪个规则累计节省最多 token？
- 哪些是 blocked（必须改）vs reminded（提示即可）？

**使用**：
```bash
bash scripts/analyze-traces.sh this-week --markdown
bash scripts/calculate-token-usage.sh this-week --markdown
```

---

## 4. 会议纪要 —— 线下/讨论层真相

**存储位置**：`💼工作项目/总结报告/会议纪要/YYYY-MM-DD_会议主题.md`

**标准结构**（见 `templates/meeting-notes.md`）：
- 议题列表
- 每个议题：核心问题 / 决策 / 关键观点 / 数据
- Action Items（按人分组，标注 ✅ 已定 / ⚠️ 有条件 / 🔴 被否）
- 核心认知沉淀
- 待跟进

**能回答**：
- 今天开了什么会？决策了什么？
- Action Items 给谁？完成情况？
- 同一议题被讨论了多少次（反复讨论未落地 = 系统性卡点）？

**review 集成规则**：
- **日报深版**：当日会议决策 + Action Items 归入用户投入
- **周报**：汇总本周所有会议决策，检查 Action Items 完成率
- **月报**：做"同一议题出现次数"分析 —— 出现 ≥ 2 次意味着反复讨论没落地

---

## 数据源组合策略

### 日报（执行层）
```
Git log（代码） + Traces（AI 执行） + Violations（触发日志） + 当日会议纪要
```

### 周报（收敛层）
```
日报 5-7 篇（必读） + Git log（补充遗漏） + 本周会议纪要汇总
```

### 月报（复盘层）
```
周报 4 篇（必读） + 日报（选读） + 本月会议纪要（识别反复议题）
```

### 季报 / 年报
```
逐级向上聚合，不跳级读原始数据
```

---

## 数据补全原则

**所有报告里的数字必须可追溯**：
- ✅ `Token 消耗 105,000（来自 violations.jsonl 聚合）`
- ✅ `反复修改 3 个文件（detect-repeated-changes.sh 2026-04-28 输出）`
- ❌ `Token 消耗大约 10 万`
- ❌ `改了好几次`

**无法追溯的数据必须明确标注**：
- `来自回忆` / `来自手动估算` / `来自会议口头数字`
- 提醒自己下次要记录到可追溯的数据源

---

## 常见陷阱

1. **Git log 只统计 commit 作者 = 自己** → 不准，有时是在团队仓库里混了别人 commit。加 `--author=本人`
2. **trace.json 的 `metadata.tokens` 不是所有类型都有** → 以 violations.jsonl 为准做成本估算
3. **会议纪要文件名不规范** → 按 `YYYY-MM-DD_主题.md` 命名，否则脚本无法按日期遍历
4. **macOS date 命令和 Linux 不同** → 所有脚本已兼容 BSD / GNU date
