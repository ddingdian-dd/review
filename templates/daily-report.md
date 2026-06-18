# 日报 - {{DATE}}

**生成时间**：{{TIMESTAMP}}
**数据来源**：Git log + violations.jsonl + Traces

---

## 关键结论

1. **{{CONCLUSION_1}}**
2. **{{CONCLUSION_2}}**

**当日主线**：（一句话）
**当日代价**：（一句话，无则写"无"）

---

{{#if HAS_GIT_DATA}}
## Git 数据

| 维度 | 数值 | 说明 |
|------|------|------|
| 提交 | {{COMMIT_COUNT}} 次 | {{COMMIT_TIME_RANGE}} |
| 净变更 | +{{LINES_ADDED}} / -{{LINES_DELETED}} | {{MAIN_FILES}} |
| 工作时长 | ~{{WORK_HOURS}} 小时 | {{WORK_PERIOD}} |

**Commit 列表**：
{{#each COMMITS}}
- `{{this.hash}}` {{this.time}} {{this.message}}（+{{this.added}}/-{{this.deleted}}）
{{/each}}

---
{{/if}}

{{#if HAS_TOKEN_DATA}}
## Token 效率

| 维度 | 数值 | 说明 |
|------|------|------|
| 总消耗 | ~{{TOTAL_TOKENS}} | {{TOKEN_SOURCE}} |
| 节省 | ~{{SAVED_TOKENS}} | {{SAVE_RULES}} |
| 浪费 | ~{{WASTED_TOKENS}}（{{WASTE_RATE}}%） | {{WASTE_SOURCE}} |

| 产出物 | 数量 | token/单元 | 判断 |
|--------|------|-----------|------|
{{#each DELIVERABLES}}
| {{this.name}} | {{this.count}} | {{this.token_per_unit}} | {{this.verdict}} |
{{/each}}

**效率基准**：页面 <150K/个 ✅ | 组件 <30K/个 ✅ | 脚本 <80K/个 ✅ | 超标需注明返工原因

---
{{/if}}

{{#if HAS_VIOLATIONS}}
## Harness 实证

| 规则 | 触发 | 效果 |
|------|------|------|
{{#each VIOLATIONS}}
| {{this.rule}} | {{this.count}} 次 | {{this.effect}} |
{{/each}}

---
{{/if}}

{{#if HAS_COMPETITOR_PULSE}}
## 竞品脉搏

{{COMPETITOR_PULSE_BLOCK}}

---
{{/if}}

## 重点工作

### P0：{{TASK_P0_NAME}}

- 背景：{{TASK_P0_CONTEXT}}
- 产出：{{TASK_P0_OUTPUT}}
- 关键决策：{{TASK_P0_DECISION}}

{{#if TASK_P1_NAME}}
### P1：{{TASK_P1_NAME}}

- 产出：{{TASK_P1_OUTPUT}}
{{/if}}

---

{{#if HAS_DEVIATIONS}}
## 偏差与改进

{{#each DEVIATIONS}}
### {{this.level}} {{this.title}}
- **表现**：{{this.desc}}
- **损失**：{{this.cost}}
- **改进**：{{this.action}}
{{/each}}

---
{{/if}}

## 下游反馈

- **前端/产品负责人反馈**：{{DOWNSTREAM_FEEDBACK}}
- **如未收到反馈**：明天第一件事对齐

---

## 今日反思

- 做对了什么：{{WHAT_WENT_WELL}}
- 做错了什么：{{WHAT_WENT_WRONG}}
- 明天改什么：{{TOMORROW_CHANGE}}

---

## 明日计划

- [ ] {{TOMORROW_P0}}
- [ ] {{TOMORROW_P1}}

---

## 沉淀候选（Traces 提取）

{{TRACES_CANDIDATES_BLOCK}}

---

**数据完整性**：Git 全天窗口 ✓ | Traces 已读取 ✓ | 生成方式：/review 触发
