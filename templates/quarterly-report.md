# 季报 - {{YEAR}}年Q{{QUARTER}}

<!-- CHUNK-INDEX
本文件共 766 行。建议按需读取章节而非完整读取（节省 ~60% context）：
- `🎯 本季度关键结论` → offset=8 limit=53
- `📊 本季度核心数据` → offset=61 limit=31
- `🎯 季度 OKR 达成情况` → offset=92 limit=51
- `📊 季度 ROI 评估` → offset=143 limit=69
- `✅ 假设验证（预期 vs 实际）` → offset=212 limit=50
- `🔄 战略偏差分析` → offset=262 limit=30
- `📈 边际效益分析（下季度优先级）` → offset=292 limit=72
- `🎯 方向调整建议` → offset=364 limit=67
- `🔮 季度趋势预测` → offset=431 limit=75
- `🤖 自我进化分析（完整版）` → offset=506 limit=85
- `🎯 系统动力学分析（深度）` → offset=591 limit=52
- `📅 下季度战略规划` → offset=643 limit=52
- `📊 季度总结` → offset=695 limit=36
- `📚 附录：本季度产出文档索引` → offset=731 limit=22
- `🔧 生成说明` → offset=753 limit=13
使用方式：Read(file, offset=N, limit=M)
-->

**生成时间**：{{TIMESTAMP}}  
**覆盖周期**：{{START_DATE}} 至 {{END_DATE}}（{{MONTH_COUNT}} 个月）  
**Commits**：{{COMMIT_COUNT}} 次 | **工作时长**：约 {{WORK_HOURS}} 小时

---

## 🎯 本季度关键结论

### ✅ 主要成果（3-5 条）

#### 成果 #1：{{ACHIEVEMENT_1_TITLE}}
**具体产出**：
- {{ACHIEVEMENT_1_OUTPUT}}

**数据支撑**：
- {{ACHIEVEMENT_1_DATA}}

**价值评估**：
- {{ACHIEVEMENT_1_VALUE}}
- ROI：{{ACHIEVEMENT_1_ROI}}

**战略意义**：
- {{ACHIEVEMENT_1_STRATEGIC_VALUE}}

---

### ⚠️ 主要问题（2-3 条）

#### 问题 #1：{{ISSUE_1_TITLE}}
**表现**：
- {{ISSUE_1_DESC}}

**累计损失**（本季度）：
- {{ISSUE_1_TOTAL_COST}}

**根因**（第一性原理分解）：
- {{ISSUE_1_ROOT_CAUSE}}

**战略影响**：
- {{ISSUE_1_STRATEGIC_IMPACT}}

**系统性解决方案**：
- {{ISSUE_1_SOLUTION}}

---

### 💡 关键教训（3-5 条）

#### 教训 #1：{{LESSON_1_TITLE}}
**来源**：{{LESSON_1_SOURCE}}

**适用场景**：{{LESSON_1_SCENARIO}}

**预期收益**：{{LESSON_1_BENEFIT}}

**已推广情况**：{{LESSON_1_STATUS}}

---

## 📊 本季度核心数据

### Git 数据（基于月报汇总）
| 维度 | 数值 | 月均 | 趋势 |
|------|------|------|------|
| 工作月数 | {{MONTH_COUNT}} 月 | - | - |
| Git 提交 | {{COMMIT_COUNT}} 次 | {{MONTHLY_COMMITS}} 次 | {{COMMIT_TREND}} |
| 代码新增 | {{LINES_ADDED}} 行 | {{MONTHLY_ADDED}} 行 | {{ADDED_TREND}} |
| 代码删除 | {{LINES_DELETED}} 行 | {{MONTHLY_DELETED}} 行 | {{DELETED_TREND}} |
| 净变更 | {{NET_CHANGE}} 行 | {{MONTHLY_NET}} 行 | {{NET_TREND}} |
| 工作时长 | {{WORK_HOURS}} 小时 | {{MONTHLY_HOURS}} 小时 | {{HOURS_TREND}} |

### Token 数据（基于月报汇总）
| 维度 | 数值 | 月均 | 趋势 |
|------|------|------|------|
| Token 总消耗 | ~{{TOTAL_TOKENS}} tokens | ~{{MONTHLY_TOKENS}} tokens | {{TOKEN_TREND}} |
| Token 浪费量 | ~{{WASTED_TOKENS}} tokens | ~{{MONTHLY_WASTED}} tokens | {{WASTED_TREND}} |
| Token 浪费率 | {{WASTE_RATE}}% | - | {{WASTE_RATE_TREND}} |
| 成本估算 | ~${{COST}} | ~${{MONTHLY_COST}} | {{COST_TREND}} |
| 浪费成本 | ~${{WASTED_COST}} | ~${{MONTHLY_WASTED_COST}} | {{WASTED_COST_TREND}} |

### 效率指标（基于月报汇总）
| 维度 | 数值 | 月均 | 趋势 |
|------|------|------|------|
| 反复修改次数 | {{REPEATED_COUNT}} 次 | {{MONTHLY_REPEATED}} 次 | {{REPEATED_TREND}} |
| 效率损失 | {{EFFICIENCY_LOSS}} 小时 | {{MONTHLY_LOSS}} 小时 | {{LOSS_TREND}} |
| AI 生成覆盖率 | {{AI_COVERAGE}}% | - | {{COVERAGE_TREND}} |
| 规范命中率 | {{STANDARD_RATE}}% | - | {{STANDARD_TREND}} |

---

## 🎯 季度 OKR 达成情况

**数据来源**：基于本季度 {{MONTH_COUNT}} 份月报汇总

### O1：{{OBJECTIVE_1_TITLE}}

#### KR1：{{KR_1_1_TITLE}}
**目标值**：{{KR_1_1_TARGET}}  
**实际值**：{{KR_1_1_ACTUAL}}  
**达成率**：{{KR_1_1_ACHIEVEMENT_RATE}}%

**关键里程碑**（基于月报汇总）：
{{#each KR_1_1_MILESTONES}}
- **{{this.month}}月**：{{this.milestone}}（完成度 {{this.progress}}%）
{{/each}}

**达成/未达成原因**：
- {{KR_1_1_REASON}}

**数据支撑**：
- {{KR_1_1_DATA}}

---

#### KR2：{{KR_1_2_TITLE}}
（同上结构）

---

### O2：{{OBJECTIVE_2_TITLE}}
（同上结构）

---

### 整体评估

**季度 OKR 达成率**：{{OVERALL_ACHIEVEMENT_RATE}}%（{{ACHIEVED_KR_COUNT}}/{{TOTAL_KR_COUNT}} 个 KR 达成）

**达成情况分布**：
- ✅ 超额达成（≥110%）：{{EXCEEDED_KR_COUNT}} 个
- ✅ 达成（90-110%）：{{ACHIEVED_KR_COUNT}} 个
- ⚠️ 基本达成（70-90%）：{{PARTIALLY_ACHIEVED_KR_COUNT}} 个
- ❌ 未达成（<70%）：{{NOT_ACHIEVED_KR_COUNT}} 个

**主要偏差分析**：
{{#each OKR_DEVIATIONS}}
- {{this.kr}}：{{this.deviation_desc}}（{{this.deviation_reason}}）
{{/each}}

---

## 📊 季度 ROI 评估

**数据来源**：基于月报数据汇总 + 业务价值评估

### 项目 #1：{{PROJECT_1_NAME}}

**投入统计**：
- 工作时长：{{PROJECT_1_HOURS}} 小时（{{PROJECT_1_HOUR_PERCENTAGE}}%）
- 人力成本：${{PROJECT_1_LABOR_COST}}（按 ${{HOURLY_RATE}}/小时）
- Token 成本：${{PROJECT_1_TOKEN_COST}}
- 其他成本：${{PROJECT_1_OTHER_COST}}
- **总成本**：${{PROJECT_1_TOTAL_COST}}

**产出统计**：
- 完成度：{{PROJECT_1_PROGRESS}}%
- 代码变更：+{{PROJECT_1_ADDED}} / -{{PROJECT_1_DELETED}}（净 {{PROJECT_1_NET}}）
- 功能交付：{{PROJECT_1_FEATURES_DELIVERED}} 个
- 上线状态：{{PROJECT_1_LAUNCH_STATUS}}

**价值评估**：
- 用户价值：{{PROJECT_1_USER_VALUE}}
- 商业价值：{{PROJECT_1_BUSINESS_VALUE}}
- 技术价值：{{PROJECT_1_TECH_VALUE}}
- **预期年度收益**：${{PROJECT_1_EXPECTED_ANNUAL_VALUE}}

**ROI 计算**：
```
ROI = (预期年度收益 - 总成本) / 总成本
    = (${{PROJECT_1_EXPECTED_ANNUAL_VALUE}} - ${{PROJECT_1_TOTAL_COST}}) / ${{PROJECT_1_TOTAL_COST}}
    = {{PROJECT_1_ROI}}%
```

**投资回收期**：{{PROJECT_1_PAYBACK_PERIOD}}

---

### 项目 #2：{{PROJECT_2_NAME}}
（同上结构）

---

### 整体 ROI 分析

**季度总投入**：${{TOTAL_COST}}（{{WORK_HOURS}} 小时）

**时间分配**：
| 项目 | 时长 | 占比 | ROI | 优先级 |
|------|------|------|-----|--------|
{{#each PROJECT_TIME_ALLOCATION}}
| {{this.project}} | {{this.hours}}h | {{this.percentage}}% | {{this.roi}}% | {{this.priority}} |
{{/each}}

**ROI 排序**（从高到低）：
{{#each PROJECTS_BY_ROI}}
{{@index}}. **{{this.project}}**：{{this.roi}}%（投入 {{this.hours}}h，预期年度收益 ${{this.value}}）
{{/each}}

**资源配置评估**：
- ✅ 高 ROI 项目（>300%）：{{HIGH_ROI_PROJECTS}}（占用 {{HIGH_ROI_TIME_PERCENTAGE}}% 时间）
- ⚠️ 中 ROI 项目（100-300%）：{{MID_ROI_PROJECTS}}（占用 {{MID_ROI_TIME_PERCENTAGE}}% 时间）
- ❌ 低 ROI 项目（<100%）：{{LOW_ROI_PROJECTS}}（占用 {{LOW_ROI_TIME_PERCENTAGE}}% 时间）

**优化建议**：
{{#each ROI_OPTIMIZATION_SUGGESTIONS}}
- {{this.suggestion}}
{{/each}}

---

## ✅ 假设验证（预期 vs 实际）

**数据来源**：对比季度初假设与实际数据

### 假设 #1：{{HYPOTHESIS_1_TITLE}}

**季度初假设**：
- {{HYPOTHESIS_1_DESC}}
- 预期结果：{{HYPOTHESIS_1_EXPECTED}}
- 验证标准：{{HYPOTHESIS_1_CRITERIA}}

**实际结果**：
- {{HYPOTHESIS_1_ACTUAL}}

**数据对比**：
| 维度 | 预期 | 实际 | 偏差 |
|------|------|------|------|
{{#each HYPOTHESIS_1_METRICS}}
| {{this.metric}} | {{this.expected}} | {{this.actual}} | {{this.deviation}} |
{{/each}}

**验证结论**：
{{#if HYPOTHESIS_1_VALIDATED}}
- ✅ **假设成立**：{{HYPOTHESIS_1_VALIDATION_DESC}}
- 原因分析：{{HYPOTHESIS_1_VALIDATION_REASON}}
- **下季度行动**：继续执行该策略
{{else}}
- ❌ **假设不成立**：{{HYPOTHESIS_1_INVALIDATION_DESC}}
- 原因分析：{{HYPOTHESIS_1_INVALIDATION_REASON}}
- **下季度行动**：调整策略 → {{HYPOTHESIS_1_ADJUSTMENT}}
{{/if}}

---

### 假设 #2：{{HYPOTHESIS_2_TITLE}}
（同上结构）

---

### 整体假设验证率

**验证成功**：{{VALIDATED_HYPOTHESES_COUNT}}/{{TOTAL_HYPOTHESES_COUNT}}（{{VALIDATION_RATE}}%）

**主要学习**：
{{#each KEY_LEARNINGS}}
- {{this.learning}}
{{/each}}

---

## 🔄 战略偏差分析

**数据来源**：对比季度战略目标与实际执行

### 偏差 #1：{{DEVIATION_1_TITLE}}

**战略目标**：{{DEVIATION_1_GOAL}}

**实际执行**：{{DEVIATION_1_ACTUAL}}

**偏差量化**：
- 目标达成率：{{DEVIATION_1_ACHIEVEMENT_RATE}}%
- 资源投入偏差：{{DEVIATION_1_RESOURCE_DEVIATION}}
- 时间进度偏差：{{DEVIATION_1_TIME_DEVIATION}}

**偏差原因**（5 问法）：
{{#each DEVIATION_1_ROOT_CAUSES}}
- {{this.why}}
{{/each}}

**影响评估**：
- {{DEVIATION_1_IMPACT}}

**调整方案**：
{{#each DEVIATION_1_ADJUSTMENTS}}
{{this.priority}}. {{this.adjustment}}
{{/each}}

---

## 📈 边际效益分析（下季度优先级）

**核心问题**：下季度的每一个小时，最应该投在哪里？

**分析方法**：基于本季度数据，计算每个项目/方向的边际效益

### 候选方向 #1：{{DIRECTION_1_NAME}}

**预计投入**：{{DIRECTION_1_HOURS}} 小时

**预期收益**：
- 用户价值：{{DIRECTION_1_USER_VALUE}}
- 商业价值：{{DIRECTION_1_BUSINESS_VALUE}}
- 技术价值：{{DIRECTION_1_TECH_VALUE}}
- 量化收益：{{DIRECTION_1_QUANTIFIED_VALUE}}

**边际效益**：
```
边际效益 = 预期收益 / 预计投入
         = {{DIRECTION_1_QUANTIFIED_VALUE}} / {{DIRECTION_1_HOURS}}h
         = {{DIRECTION_1_MARGINAL_BENEFIT}} / h
```

**风险评估**：
- 技术风险：{{DIRECTION_1_TECH_RISK}}
- 市场风险：{{DIRECTION_1_MARKET_RISK}}
- 资源风险：{{DIRECTION_1_RESOURCE_RISK}}

**前置依赖**：
- {{DIRECTION_1_DEPENDENCIES}}

---

### 候选方向 #2：{{DIRECTION_2_NAME}}
（同上结构）

---

### 边际效益排序

**按边际效益排序**（从高到低）：
| 排名 | 方向 | 边际效益 | 预计投入 | 预期收益 | 风险等级 | 建议优先级 |
|------|------|---------|---------|---------|---------|-----------|
{{#each DIRECTIONS_BY_MARGINAL_BENEFIT}}
| {{@index}} | {{this.direction}} | {{this.benefit}}/h | {{this.hours}}h | {{this.value}} | {{this.risk}} | {{this.priority}} |
{{/each}}

**资源配置建议**：
```
P0（必做，50% 时间）：
{{#each P0_DIRECTIONS}}
- {{this.direction}}（{{this.hours}}h）
{{/each}}

P1（重要，30% 时间）：
{{#each P1_DIRECTIONS}}
- {{this.direction}}（{{this.hours}}h）
{{/each}}

P2（可选，20% 时间）：
{{#each P2_DIRECTIONS}}
- {{this.direction}}（{{this.hours}}h）
{{/each}}
```

**时间分配优化**：
- 当前季度高 ROI 项目占比：{{CURRENT_HIGH_ROI_PERCENTAGE}}%
- 下季度目标占比：{{NEXT_HIGH_ROI_PERCENTAGE}}%
- 预期 ROI 提升：{{ROI_IMPROVEMENT}}%

---

## 🎯 方向调整建议

**数据来源**：基于 ROI、OKR 达成率、边际效益分析

### 项目/方向 #1：{{PROJECT_1_NAME}}

**本季度表现**：
- ROI：{{PROJECT_1_ROI}}%
- OKR 达成率：{{PROJECT_1_OKR_ACHIEVEMENT}}%
- 边际效益：{{PROJECT_1_MARGINAL_BENEFIT}}/h
- 时间占比：{{PROJECT_1_TIME_PERCENTAGE}}%

**评估结论**：
{{#if PROJECT_1_CONTINUE}}
✅ **继续执行**
- 理由：{{PROJECT_1_CONTINUE_REASON}}
- 下季度目标：{{PROJECT_1_NEXT_GOAL}}
- 资源配置：{{PROJECT_1_NEXT_RESOURCE}}
{{else if PROJECT_1_INCREASE}}
⬆️ **加大投入**
- 理由：{{PROJECT_1_INCREASE_REASON}}
- 当前投入：{{PROJECT_1_CURRENT_RESOURCE}}
- 建议投入：{{PROJECT_1_RECOMMENDED_RESOURCE}}（+{{PROJECT_1_RESOURCE_INCREASE}}）
{{else if PROJECT_1_DECREASE}}
⬇️ **减少投入**
- 理由：{{PROJECT_1_DECREASE_REASON}}
- 当前投入：{{PROJECT_1_CURRENT_RESOURCE}}
- 建议投入：{{PROJECT_1_RECOMMENDED_RESOURCE}}（-{{PROJECT_1_RESOURCE_DECREASE}}）
{{else}}
❌ **放弃/暂停**
- 理由：{{PROJECT_1_STOP_REASON}}
- 已投入成本：${{PROJECT_1_SUNK_COST}}
- 预期损失：{{PROJECT_1_EXPECTED_LOSS}}
- 放弃决策依据：{{PROJECT_1_STOP_CRITERIA}}
{{/if}}

---

### 项目/方向 #2：{{PROJECT_2_NAME}}
（同上结构）

---

### 整体方向调整总结

**继续执行**（{{CONTINUE_COUNT}} 个）：
{{#each CONTINUE_PROJECTS}}
- {{this.project}}：{{this.reason}}
{{/each}}

**加大投入**（{{INCREASE_COUNT}} 个）：
{{#each INCREASE_PROJECTS}}
- {{this.project}}：{{this.current}} → {{this.recommended}}（+{{this.increase}}）
{{/each}}

**减少投入**（{{DECREASE_COUNT}} 个）：
{{#each DECREASE_PROJECTS}}
- {{this.project}}：{{this.current}} → {{this.recommended}}（-{{this.decrease}}）
{{/each}}

**放弃/暂停**（{{STOP_COUNT}} 个）：
{{#each STOP_PROJECTS}}
- {{this.project}}：{{this.reason}}
{{/each}}

---

## 🔮 季度趋势预测

### 预测 #1：下季度 Token 消耗趋势

**历史数据**（本季度 {{MONTH_COUNT}} 个月）：
| 月 | Token 消耗 | 浪费率 | 成本 | 趋势 |
|----|-----------|--------|------|------|
{{#each QUARTERLY_TOKEN_HISTORY}}
| {{this.month}} | {{this.total}} | {{this.waste_rate}}% | ${{this.cost}} | {{this.trend}} |
{{/each}}

**趋势分析**：
- 季度趋势：{{TOKEN_QUARTERLY_TREND}}
- 平均月变化：{{TOKEN_MONTHLY_CHANGE}}
- 浪费率趋势：{{WASTE_RATE_QUARTERLY_TREND}}

**预测模型**：
```
线性回归预测（基于过去 {{MONTH_COUNT}} 个月数据）：
  下季度第 1 月预测：{{NEXT_Q_MONTH_1_PREDICTION}} tokens
  下季度第 2 月预测：{{NEXT_Q_MONTH_2_PREDICTION}} tokens
  下季度第 3 月预测：{{NEXT_Q_MONTH_3_PREDICTION}} tokens
  
  下季度总预测：{{NEXT_Q_PREDICTION}} tokens
  预测浪费率：{{NEXT_Q_WASTE_RATE}}%
  预测成本：${{NEXT_Q_COST}}
```

**置信度**：{{PREDICTION_CONFIDENCE}}

**建议**：
{{#each TOKEN_PREDICTION_SUGGESTIONS}}
- {{this.suggestion}}
{{/each}}

---

### 预测 #2：下季度 OKR 达成率

**历史数据**（本季度 OKR 进展）：
| 月 | OKR 平均达成率 | 月进度 | 趋势 |
|----|--------------|--------|------|
{{#each QUARTERLY_OKR_HISTORY}}
| {{this.month}} | {{this.achievement}}% | +{{this.delta}}% | {{this.trend}} |
{{/each}}

**趋势分析**：
- 季度平均进度：+{{QUARTERLY_AVERAGE_PROGRESS}}%/月
- 加速/减速：{{PROGRESS_ACCELERATION}}
- 存在风险：{{OKR_RISKS}}

**预测模型**：
```
保守预测（考虑风险）：
  下季度预计达成率 = {{NEXT_Q_CONSERVATIVE_ACHIEVEMENT}}%
  
最可能预测（基于历史平均）：
  下季度预计达成率 = {{NEXT_Q_REALISTIC_ACHIEVEMENT}}%
  
乐观预测（无阻碍）：
  下季度预计达成率 = {{NEXT_Q_OPTIMISTIC_ACHIEVEMENT}}%
```

**关键风险**：
{{#each OKR_KEY_RISKS}}
- {{this.risk}}（影响：-{{this.impact}}%）
{{/each}}

**建议**：
{{#each OKR_SUGGESTIONS}}
- {{this.suggestion}}
{{/each}}

---

## 🤖 自我进化分析（完整版）

### Model 层（底层模型）
**季度初版本**：{{MODEL_VERSION_START}}  
**季度末版本**：{{MODEL_VERSION_END}}  
**本季度变化**：{{MODEL_CHANGES}}  
**评估**：{{MODEL_EVALUATION}}

---

### Harness 层（执行框架）
**本季度变化**：
{{#each HARNESS_CHANGES}}
- {{this.month}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{HARNESS_EVALUATION}}

**量化效果**：
{{#each HARNESS_EFFECTS}}
- {{this.metric}}：{{this.effect}}
{{/each}}

**优化迭代**：
- 本季度迭代次数：{{HARNESS_ITERATION_COUNT}} 次
- 主要优化方向：{{HARNESS_OPTIMIZATION_FOCUS}}
- A/B 测试次数：{{HARNESS_AB_TEST_COUNT}} 次

---

### Context 层（可配置上下文）
**本季度变化**：
{{#each CONTEXT_CHANGES}}
- {{this.month}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{CONTEXT_EVALUATION}}

**量化效果**：
{{#each CONTEXT_EFFECTS}}
- {{this.metric}}：{{this.effect}}
{{/each}}

**知识库增长**：
- 新增经验：{{NEW_EXPERIENCES}} 条
- 新增规则：{{NEW_RULES}} 条
- 新增技能：{{NEW_SKILLS}} 个
- Skills 优化：{{SKILLS_OPTIMIZED}} 个

---

### Traces 层（执行日志）
**本季度变化**：
{{#each TRACES_CHANGES}}
- {{this.month}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{TRACES_EVALUATION}}

**Traces 积累**：
- 总 traces 数：{{TOTAL_TRACES}}
- 本季度新增：{{NEW_TRACES}}
- 分析次数：{{ANALYSIS_COUNT}}
- 转化为规则：{{TRACES_TO_RULES_COUNT}} 条

---

### 整体评估
{{EVOLUTION_SUMMARY}}

**本季度主要在 {{MAIN_EVOLUTION_LAYERS}} 层进化**。

**进化速度**：
- Model 层：{{MODEL_EVOLUTION_SPEED}}
- Harness 层：{{HARNESS_EVOLUTION_SPEED}}
- Context 层：{{CONTEXT_EVOLUTION_SPEED}}
- Traces 层：{{TRACES_EVOLUTION_SPEED}}

**下季度进化目标**：
{{#each NEXT_Q_EVOLUTION_GOALS}}
{{this.priority}}. {{this.goal}}（{{this.layer}} 层）
{{/each}}

---

## 🎯 系统动力学分析（深度）

### 正反馈循环识别

**循环 #1：{{POSITIVE_LOOP_1_NAME}}**

```
{{POSITIVE_LOOP_1_DIAGRAM}}
```

**循环机制**：
{{#each POSITIVE_LOOP_1_STEPS}}
{{@index}}. {{this.step}}
{{/each}}

**本季度表现**：
- 循环强度：{{POSITIVE_LOOP_1_STRENGTH}}
- 放大效果：{{POSITIVE_LOOP_1_AMPLIFICATION}}
- 量化收益：{{POSITIVE_LOOP_1_BENEFIT}}

**下季度放大策略**：
{{#each POSITIVE_LOOP_1_AMPLIFY}}
- {{this.strategy}}（预期效果：{{this.effect}}）
{{/each}}

---

### 负反馈循环识别

**循环 #1：{{NEGATIVE_LOOP_1_NAME}}**

```
{{NEGATIVE_LOOP_1_DIAGRAM}}
```

**循环机制**：
{{#each NEGATIVE_LOOP_1_STEPS}}
{{@index}}. {{this.step}}
{{/each}}

**本季度表现**：
- 循环强度：{{NEGATIVE_LOOP_1_STRENGTH}}
- 负面影响：{{NEGATIVE_LOOP_1_DAMAGE}}
- 量化损失：{{NEGATIVE_LOOP_1_LOSS}}

**打破策略**：
{{#each NEGATIVE_LOOP_1_BREAK}}
- {{this.strategy}}（已实施：{{this.status}}，效果：{{this.effect}}）
{{/each}}

---

## 📅 下季度战略规划

### 战略目标（基于本季度数据驱动）

**O1：{{NEXT_Q_OBJECTIVE_1}}**

**为什么这是优先级 P0**：
- 数据支撑：{{NEXT_Q_O1_DATA_SUPPORT}}
- 边际效益：{{NEXT_Q_O1_MARGINAL_BENEFIT}}/h
- ROI 预测：{{NEXT_Q_O1_PREDICTED_ROI}}%

**Key Results**：
{{#each NEXT_Q_O1_KRS}}
- KR{{@index}}: {{this.kr}}（验证标准：{{this.criteria}}）
{{/each}}

**资源配置**：
- 时间投入：{{NEXT_Q_O1_TIME}} 小时（{{NEXT_Q_O1_TIME_PERCENTAGE}}%）
- 预算：${{NEXT_Q_O1_BUDGET}}

---

### O2：{{NEXT_Q_OBJECTIVE_2}}
（同上结构）

---

### P0 必做（战略级）

{{#each NEXT_Q_P0}}
- [ ] **{{this.goal}}**（预计耗时 {{this.hours}}h）
  - 战略目标：{{this.objective}}
  - 成功标准：{{this.success_criteria}}
  - 预期产出：{{this.output}}
  - 边际效益：{{this.marginal_benefit}}/h
  - ROI 预测：{{this.predicted_roi}}%
{{/each}}

### P1 重要（战术级）

{{#each NEXT_Q_P1}}
- [ ] **{{this.goal}}**（预计耗时 {{this.hours}}h）
{{/each}}

### 强制执行（基于本季度反思）

{{#each NEXT_Q_RULES}}
- [ ] {{this.rule}}（来源：{{this.source}}）
{{/each}}

---

## 📊 季度总结

### 🎯 OKR 达成情况

| 目标 | 目标值 | 实际值 | 达成率 | 评估 |
|------|--------|--------|--------|------|
{{#each QUARTERLY_OKRS}}
| {{this.okr}} | {{this.target}} | {{this.actual}} | {{this.achievement_rate}}% | {{this.evaluation}} |
{{/each}}

### 🏆 关键成果（Top 3）

{{#each TOP_ACHIEVEMENTS}}
{{@index}}. **{{this.achievement}}**
   - 产出：{{this.output}}
   - 价值：{{this.value}}
   - ROI：{{this.roi}}%
{{/each}}

### ⚠️ 关键问题（Top 3）

{{#each TOP_ISSUES}}
{{@index}}. **{{this.issue}}**（累计损失 {{this.cost}}）
   - 根因：{{this.root_cause}}
   - 已建立规则：{{this.rules}}
   - 下季度调整：{{this.adjustment}}
{{/each}}

### 💡 关键教训（{{EXPERIENCE_COUNT}} 条）

{{#each KEY_EXPERIENCES}}
{{@index}}. {{this.experience}}（{{this.benefit}}）
{{/each}}

---

## 📚 附录：本季度产出文档索引

### 月报（{{MONTHLY_REPORT_COUNT}} 份）
{{#each MONTHLY_REPORTS}}
{{@index}}. [月报-{{this.month}}月]({{this.path}}) - {{this.summary}}
{{/each}}

### 周报（{{WEEKLY_REPORT_COUNT}} 份）
（略，详见各月报）

### 分析报告（{{ANALYSIS_REPORT_COUNT}} 份）
{{#each ANALYSIS_REPORTS}}
{{@index}}. [{{this.name}}]({{this.path}}) - {{this.summary}}
{{/each}}

---

**记录时间**：{{RECORD_TIME}}  
**填写耗时**：{{FILL_TIME}} 分钟（基于 {{MONTHLY_REPORT_COUNT}} 份月报内容生成）

---

## 🔧 生成说明

**强制流程**：
1. ✅ 第一步：读取本季度所有月报（绝对优先）
2. ✅ 第二步：选择性读取周报（如月报不完整）
3. ✅ 第三步：采集 Git 数据（补充）
4. ✅ 第四步：生成季报（强调战略因果关系，评估 ROI 和方向）

**数据来源**：
- 月报：{{MONTHLY_REPORT_LIST}}
- 周报：{{WEEKLY_REPORT_LIST}}（如需要）
- Git log：{{GIT_LOG_RANGE}}
- Traces：{{TRACES_RANGE}}
