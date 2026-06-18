# 周报 - {{YEAR}}年第{{WEEK_NUMBER}}周（{{START_DATE}} 至 {{END_DATE}}）

<!-- CHUNK-INDEX
本文件共 ~300 行。按需读取：
- `🎯 关键结论` → offset=8 limit=40
- `📊 核心数据` → offset=48 limit=35
- `📋 重点工作` → offset=83 limit=50
- `🌐 行业趋势` → offset=133 limit=50
- `⚠️ 问题与改进` → offset=183 limit=40
- `💡 经验与沉淀` → offset=223 limit=40
- `📅 下周计划` → offset=263 limit=25
- `📚 附录` → offset=288 limit=20
使用方式：Read(file, offset=N, limit=M)
-->

**生成时间**：{{TIMESTAMP}}  
**工作分支**：{{BRANCH}}  
**Commits**：{{MY_COMMITS}} 次（本人）/ {{TOTAL_COMMITS}} 次（全团队）| **工作时长**：用户 ~{{USER_HOURS}} 小时 / Claude ~{{CLAUDE_HOURS}} 小时

---

## 🎯 关键结论

> 30 秒读完本周全貌。成果证明方向对，问题指向下周动作。

### 成果（2-3 条）

#### {{ACHIEVEMENT_1_TITLE}}
- **产出**：{{ACHIEVEMENT_1_OUTPUT}}
- **数据**：{{ACHIEVEMENT_1_DATA}}
- **价值**：{{ACHIEVEMENT_1_VALUE}}

#### {{ACHIEVEMENT_2_TITLE}}
- **产出**：{{ACHIEVEMENT_2_OUTPUT}}
- **数据**：{{ACHIEVEMENT_2_DATA}}
- **价值**：{{ACHIEVEMENT_2_VALUE}}

### 问题（1-2 条）

#### {{ISSUE_1_TITLE}}
- **表现**：{{ISSUE_1_DESC}}
- **损失**：{{ISSUE_1_COST}}
- **根因**：{{ISSUE_1_ROOT_CAUSE}}
- **下周动作**：{{ISSUE_1_ACTION}}

---

## 📊 核心数据

### Git

| 维度 | 数值 | 说明 |
|------|------|------|
| 工作天数 | {{WORK_DAYS}} | {{START_DATE}} 至 {{END_DATE}} |
| 本人提交 | {{MY_COMMITS}} 次 | 日均 {{DAILY_COMMITS}} |
| 代码净变更 | +{{ADDED}} / -{{DELETED}}（净 {{NET}}） | {{MAIN_WORK}} |
| 文件变更 | {{FILES}} 个 | {{FILE_TYPES}} |

### Token & 成本

| 维度 | 数值 | 说明 |
|------|------|------|
| Hook 节省 | ~{{SAVED_TOKENS}} tokens | {{SAVE_SOURCE}} |
| 浪费量 | ~{{WASTED_TOKENS}} tokens | {{WASTE_SOURCE}} |
| 净节省 | ~{{NET_SAVED}} tokens（~${{NET_COST}}） | — |
| 浪费类型 TOP3 | {{WASTE_TYPE_1}} / {{WASTE_TYPE_2}} / {{WASTE_TYPE_3}} | 占比分布 |

### AI 协作质量

| 维度 | 数值 | 趋势 |
|------|------|------|
| AI 生成覆盖率 | {{AI_COVERAGE}}% | {{TREND_COVERAGE}} |
| 人工修改率 | {{MANUAL_RATE}}% | {{TREND_MANUAL}} |
| 规范命中率 | {{STANDARD_RATE}}% | {{TREND_STANDARD}} |
| Violations | {{VIOLATIONS}} 次 | {{VIOLATION_BREAKDOWN}} |

### 日均分布

| 日期 | commits | 用户时长 | 主要事项 |
|------|---------|---------|---------|
{{#each DAILY_ROWS}}
| {{this.date}} | {{this.commits}} | {{this.user_hours}} | {{this.summary}} |
{{/each}}

---

## 📋 重点工作

**数据来源**：{{DAILY_REPORT_COUNT}} 份日报 + Git log + Traces

### P0：{{TASK_P0_1_NAME}}（完成度 {{TASK_P0_1_PROGRESS}}%）

{{#each TASK_P0_1_DAYS}}
**{{this.date}}**：
{{#each this.items}}
- ✅ {{this.desc}}（{{this.commit}}，{{this.stat}}）
{{/each}}
{{/each}}

**效率分析**：
- ✅ {{TASK_P0_1_EFFICIENT}}
- ⚠️ {{TASK_P0_1_INEFFICIENT}}（损失：{{TASK_P0_1_LOSS}}）

---

### P1：{{TASK_P1_1_NAME}}（完成度 {{TASK_P1_1_PROGRESS}}%）

{{TASK_P1_1_SUMMARY}}

---

## 🌐 行业趋势判断（基于本周 AI 资讯）

> 条件渲染：当周有 AI 资讯文件时渲染此章节，无则跳过。
> 数据来源：`💼工作项目/总结报告/日报/AI资讯-{{DATE}}.md`

本周 {{AI_NEWS_DAYS}} 天资讯共追踪 {{AI_NEWS_COUNT}} 条行业动态，提炼 2-3 个趋势判断：

{{#each TRENDS}}
### 趋势 {{@index}}：{{this.title}}

**信号集合**：
{{#each this.signals}}
- {{this.desc}}（{{this.date}}）
{{/each}}

**判断**：{{this.judgment}}

**对启信慧眼的动作**：
{{#each this.actions}}
- {{this.desc}}
{{/each}}

---
{{/each}}

## ⚠️ 问题与改进

> 问题和踩坑统一放这里。每条必须有：表现→量化损失→根因→改进动作→预计节省。

### #1：{{PROBLEM_1_TITLE}}

**表现**：
{{#each PROBLEM_1_INCIDENTS}}
- {{this.date}}：{{this.desc}}
{{/each}}

**累计损失**：{{PROBLEM_1_TOTAL_COST}}

**根因**（5 问法）：
- Q1：{{Q1}} → A1：{{A1}}
- Q2：{{Q2}} → A2：{{A2}}
- **根因**：{{ROOT_CAUSE}}

**改进动作**：
{{#each PROBLEM_1_ACTIONS}}
- [ ] {{this.action}}（落地位置：{{this.target}}）
{{/each}}

**预计节省**：{{PROBLEM_1_SAVING}}

---

### #2：{{PROBLEM_2_TITLE}}

（同上结构）

---

## 💡 经验与沉淀

> 高效动作 + 教训 + 是否落地，一个表搞定。

### 本周经验提炼

| # | 经验 | 来源 | ✅ 做法 | ❌ 反面 | 量化收益 |
|---|------|------|--------|--------|---------|
{{#each EXPERIENCES}}
| {{@index}} | {{this.title}} | {{this.source}} | {{this.good}} | {{this.bad}} | {{this.benefit}} |
{{/each}}

### 沉淀候选（Traces 提取 + 本周实践）

| # | 候选内容 | 落地位置 | 优先级 | 采纳？ |
|---|---------|---------|--------|-------|
{{#each CANDIDATES}}
| {{@index}} | {{this.content}} | {{this.target}} | {{this.priority}} | [ ] |
{{/each}}

---

## 🔄 自动改进建议（Agent 自诊断）

> 基于本周日报重复模式自动生成，待用户审批后落地。每条建议必须有：触发数据、改动内容、落地位置、预期收益。

{{#each IMPROVEMENT_PROPOSALS}}
### 建议 {{@index}}：{{this.title}}

**触发数据**：{{this.trigger}}（本周出现 {{this.frequency}} 次）

**诊断**：{{this.diagnosis}}

**具体改动**：
```
文件：{{this.target_file}}
改动：{{this.diff_preview}}
```

**预期收益**：{{this.expected_benefit}}

**审批**：[ ] 采纳 / [ ] 拒绝（原因：___）

---
{{/each}}

{{#if NO_IMPROVEMENTS}}
本周无重复模式达到自动改进阈值（≥3 天出现同一问题）。
{{/if}}

---

## 📅 下周计划

### P0 必做

{{#each NEXT_P0}}
- [ ] **{{this.task}}**（{{this.hours}}h）— 目标：{{this.goal}}
{{/each}}

### P1 重要

{{#each NEXT_P1}}
- [ ] {{this.task}}（{{this.hours}}h）
{{/each}}

### 强制执行（基于本周问题）

{{#each NEXT_RULES}}
- [ ] {{this.rule}}
{{/each}}

---

## 📚 附录

### 产出文档索引

**日报**（{{DAILY_COUNT}} 份）：
{{#each DAILY_REPORTS}}
- [日报-{{this.date}}.md]({{this.path}}) — {{this.summary}}
{{/each}}

**会议纪要**（{{MEETING_COUNT}} 份）：
{{#each MEETINGS}}
- [{{this.name}}]({{this.path}}) — {{this.summary}}
{{/each}}

**AI 资讯**（{{AI_NEWS_COUNT_FILES}} 份）：
{{#each AI_NEWS_FILES}}
- [AI资讯-{{this.date}}.md]({{this.path}}) — {{this.highlights}}
{{/each}}

### 生成说明

- 数据来源：{{DATA_SOURCES}}
- 日报完整性：{{DAILY_COMPLETENESS}}
- 生成方式：/review 触发，基于日报收敛（非原始数据重采）
