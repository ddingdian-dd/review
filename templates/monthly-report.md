# 月报 - {{YEAR}}年{{MONTH}}月

**生成时间**：{{TIMESTAMP}}
**周期**：{{START_DATE}} 至 {{END_DATE}}（{{WEEK_COUNT}} 周）| {{COMMIT_COUNT}} commits | {{WORK_HOURS}} 小时

---

## 1. 月度结论

**✅ 成果**（3-5 条）
{{#each ACHIEVEMENTS}}
{{@index}}. {{this.title}} - {{this.output}}（价值：{{this.value}}）
{{/each}}

**⚠️ 问题**（2-3 条，仅列重复出现 ≥2 次）
{{#each ISSUES}}
{{@index}}. {{this.title}}（{{this.count}} 次，{{this.cost}}）
{{/each}}

**💡 教训**（3-5 条，可复用）
{{#each LESSONS}}
{{@index}}. {{this.lesson}}
{{/each}}

---

## 2. 核心指标

| 维度 | W1 | W2 | W3 | W4 | 月总 | 趋势 |
|------|----|----|----|----|------|------|
| Git 提交 | {{W1_COMMITS}} | {{W2_COMMITS}} | {{W3_COMMITS}} | {{W4_COMMITS}} | {{COMMIT_COUNT}} | {{COMMIT_TREND}} |
| 代码净变更 | {{W1_NET}} | {{W2_NET}} | {{W3_NET}} | {{W4_NET}} | {{NET_CHANGE}} | {{NET_TREND}} |
| Token 消耗 | {{W1_TOKENS}} | {{W2_TOKENS}} | {{W3_TOKENS}} | {{W4_TOKENS}} | {{TOTAL_TOKENS}} | {{TOKEN_TREND}} |
| 浪费率 | {{W1_WASTE}}% | {{W2_WASTE}}% | {{W3_WASTE}}% | {{W4_WASTE}}% | {{WASTE_RATE}}% | {{WASTE_TREND}} |
| 反复修改 | {{W1_REPEATED}} | {{W2_REPEATED}} | {{W3_REPEATED}} | {{W4_REPEATED}} | {{REPEATED_COUNT}} | {{REPEATED_TREND}} |
| AI 规范命中 | {{W1_STANDARD}}% | {{W2_STANDARD}}% | {{W3_STANDARD}}% | {{W4_STANDARD}}% | - | {{STANDARD_TREND}} |

**结论**：{{METRICS_CONCLUSION}}

---

## 3. 重点工作

**数据来源**：本月 {{WEEK_COUNT}} 份周报汇总

{{#each PROJECTS}}
### 项目 {{@index}}：{{this.name}}（完成度 {{this.progress}}% / {{this.status}}）

- 进度：{{this.weekly_breakdown}}
- 投入：{{this.code_change}} 代码 | {{this.tokens}} Token | {{this.commits}} 次提交
{{#if this.delayed}}
- ⚠️ 延迟原因：{{this.delay_reason}}
- 预期影响：{{this.delay_impact}}
{{/if}}

{{/each}}

---

## 4. 问题与改进

### 重复问题

{{#each REPEATED_PROBLEMS}}
**问题 {{@index}}：{{this.title}}**（{{this.count}} 次，{{this.total_cost}}）

- 根因（5 问法压缩）：{{this.root_cause}}
- 方案：{{this.solution}}
- 规则：{{this.rule_file}}

{{/each}}

### 改进验证

| 改进措施 | 实施时间 | 前 | 后 | 结论 |
|---------|---------|----|----|------|
{{#each IMPROVEMENTS}}
| {{this.name}} | {{this.date}} | {{this.before}} | {{this.after}} | {{this.result}} |
{{/each}}

---

## 5. 系统进化

**主要进化层**：{{MAIN_EVOLUTION_LAYER}}

**Harness 层**
{{#each HARNESS_CHANGES}}
- {{this.desc}}（{{this.date}}）
{{/each}}
→ 量化效果：{{HARNESS_EFFECT}}

**Context 层**
- 新增记忆 {{NEW_MEMORIES}} 条 / 规则 {{NEW_RULES}} 条 / 技能 {{NEW_SKILLS}} 个
→ 量化效果：{{CONTEXT_EFFECT}}

**下月关注**
- Token：目标 < {{NEXT_TOKEN_TARGET}}，浪费率 < {{NEXT_WASTE_TARGET}}%
- 项目：{{NEXT_PROJECT_FOCUS}}（风险：{{NEXT_PROJECT_RISK}}）

---

## 6. 下月计划

**P0 必做**
{{#each NEXT_MONTH_P0}}
- [ ] {{this.goal}}（~{{this.hours}}h，成功标准：{{this.success_criteria}}）
{{/each}}

**P1 重要**
{{#each NEXT_MONTH_P1}}
- [ ] {{this.goal}}（~{{this.hours}}h）
{{/each}}

**强制执行**（基于本月重复问题沉淀）
{{#each NEXT_MONTH_RULES}}
- [ ] {{this.rule}}（来源：{{this.source}}）
{{/each}}

---

**生成说明**：
1. 读取本月所有周报（强制）
2. 按需读取日报（周报不完整时）
3. 采集 Git 数据补充
4. 强调因果关系，只列 ≥2 次的重复问题
