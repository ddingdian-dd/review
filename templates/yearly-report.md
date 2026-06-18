# 年报 - {{YEAR}}年

<!-- CHUNK-INDEX
本文件共 795 行。建议按需读取章节而非完整读取（节省 ~60% context）：
- `🎯 年度关键结论` → offset=8 limit=50
- `📊 年度核心数据` → offset=58 limit=31
- `📋 年度价值排序（ROI 排名）` → offset=89 limit=89
- `⏰ 年度时间分配分析` → offset=178 limit=37
- `🚀 年度能力提升分析` → offset=215 limit=76
- `🎯 能力矩阵分析（深度）` → offset=291 limit=95
- `🎯 年度 OKR 达成情况` → offset=386 limit=50
- `🤖 年度自我进化分析（完整版）` → offset=436 limit=113
- `🎯 系统动力学分析（年度总结）` → offset=549 limit=47
- `📅 明年战略规划（数据驱动）` → offset=596 limit=115
- `📊 年度总结` → offset=711 limit=49
- `📚 附录：年度产出文档索引` → offset=760 limit=22
- `🔧 生成说明` → offset=782 limit=13
使用方式：Read(file, offset=N, limit=M)
-->

**生成时间**：{{TIMESTAMP}}  
**覆盖周期**：{{START_DATE}} 至 {{END_DATE}}（全年）  
**Commits**：{{COMMIT_COUNT}} 次 | **工作时长**：约 {{WORK_HOURS}} 小时

---

## 🎯 年度关键结论

### ✅ 最有价值的事情（Top 3）

#### #1：{{TOP_VALUE_1_TITLE}}
**具体产出**：
- {{TOP_VALUE_1_OUTPUT}}

**价值评估**：
- 用户价值：{{TOP_VALUE_1_USER_VALUE}}
- 商业价值：{{TOP_VALUE_1_BUSINESS_VALUE}}
- 个人成长：{{TOP_VALUE_1_PERSONAL_GROWTH}}

**ROI**：{{TOP_VALUE_1_ROI}}%

**为什么排第一**：
- {{TOP_VALUE_1_REASON}}

---

### ⚠️ 最大的浪费（Top 3）

#### #1：{{WASTE_1_TITLE}}
**时间投入**：{{WASTE_1_HOURS}} 小时（{{WASTE_1_PERCENTAGE}}%）

**产出**：{{WASTE_1_OUTPUT}}

**为什么是浪费**：
- {{WASTE_1_REASON}}

**如果重来一次**：
- {{WASTE_1_ALTERNATIVE}}

**累计损失**：{{WASTE_1_LOSS}}

---

### 💡 关键教训（Top 5）

#### 教训 #1：{{LESSON_1_TITLE}}
**来源**：{{LESSON_1_SOURCE}}

**适用场景**：{{LESSON_1_SCENARIO}}

**预期收益**：{{LESSON_1_BENEFIT}}

**推广状态**：{{LESSON_1_STATUS}}

---

## 📊 年度核心数据

### Git 数据（基于季报汇总）
| 维度 | 数值 | 季均 | 月均 | 趋势 |
|------|------|------|------|------|
| 工作季度 | {{QUARTER_COUNT}} 季度 | - | - | - |
| Git 提交 | {{COMMIT_COUNT}} 次 | {{QUARTERLY_COMMITS}} 次 | {{MONTHLY_COMMITS}} 次 | {{COMMIT_TREND}} |
| 代码新增 | {{LINES_ADDED}} 行 | {{QUARTERLY_ADDED}} 行 | {{MONTHLY_ADDED}} 行 | {{ADDED_TREND}} |
| 代码删除 | {{LINES_DELETED}} 行 | {{QUARTERLY_DELETED}} 行 | {{MONTHLY_DELETED}} 行 | {{DELETED_TREND}} |
| 净变更 | {{NET_CHANGE}} 行 | {{QUARTERLY_NET}} 行 | {{MONTHLY_NET}} 行 | {{NET_TREND}} |
| 工作时长 | {{WORK_HOURS}} 小时 | {{QUARTERLY_HOURS}} 小时 | {{MONTHLY_HOURS}} 小时 | {{HOURS_TREND}} |

### Token 数据（基于季报汇总）
| 维度 | 数值 | 季均 | 月均 | 趋势 |
|------|------|------|------|------|
| Token 总消耗 | ~{{TOTAL_TOKENS}} tokens | ~{{QUARTERLY_TOKENS}} tokens | ~{{MONTHLY_TOKENS}} tokens | {{TOKEN_TREND}} |
| Token 浪费量 | ~{{WASTED_TOKENS}} tokens | ~{{QUARTERLY_WASTED}} tokens | ~{{MONTHLY_WASTED}} tokens | {{WASTED_TREND}} |
| Token 浪费率 | {{WASTE_RATE}}% | - | - | {{WASTE_RATE_TREND}} |
| 成本估算 | ~${{COST}} | ~${{QUARTERLY_COST}} | ~${{MONTHLY_COST}} | {{COST_TREND}} |
| 浪费成本 | ~${{WASTED_COST}} | ~${{QUARTERLY_WASTED_COST}} | ~${{MONTHLY_WASTED_COST}} | {{WASTED_COST_TREND}} |

### 效率指标（基于季报汇总）
| 维度 | 数值 | 季均 | 月均 | 趋势 |
|------|------|------|------|------|
| 反复修改次数 | {{REPEATED_COUNT}} 次 | {{QUARTERLY_REPEATED}} 次 | {{MONTHLY_REPEATED}} 次 | {{REPEATED_TREND}} |
| 效率损失 | {{EFFICIENCY_LOSS}} 小时 | {{QUARTERLY_LOSS}} 小时 | {{MONTHLY_LOSS}} 小时 | {{LOSS_TREND}} |
| AI 生成覆盖率 | {{AI_COVERAGE}}% | - | - | {{COVERAGE_TREND}} |
| 规范命中率 | {{STANDARD_RATE}}% | - | - | {{STANDARD_TREND}} |

---

## 📋 年度价值排序（ROI 排名）

**数据来源**：基于全年所有项目的 ROI 评估

| 排名 | 项目/方向 | 时间投入 | 时间占比 | 总成本 | 预期年度价值 | ROI | 值不值得继续 |
|------|----------|---------|---------|--------|------------|-----|-------------|
{{#each PROJECTS_BY_ROI}}
| {{@index}} | {{this.project}} | {{this.hours}}h | {{this.percentage}}% | ${{this.cost}} | ${{this.value}} | {{this.roi}}% | {{this.worth_continue}} |
{{/each}}

---

### 项目 #1：{{PROJECT_1_NAME}}（ROI {{PROJECT_1_ROI}}%，排名第 {{PROJECT_1_RANK}}）

**年度投入**：
- 工作时长：{{PROJECT_1_HOURS}} 小时（{{PROJECT_1_HOUR_PERCENTAGE}}%）
- 人力成本：${{PROJECT_1_LABOR_COST}}
- Token 成本：${{PROJECT_1_TOKEN_COST}}
- 其他成本：${{PROJECT_1_OTHER_COST}}
- **总成本**：${{PROJECT_1_TOTAL_COST}}

**年度产出**：
- 完成度：{{PROJECT_1_PROGRESS}}%
- 代码变更：+{{PROJECT_1_ADDED}} / -{{PROJECT_1_DELETED}}（净 {{PROJECT_1_NET}}）
- 功能交付：{{PROJECT_1_FEATURES_DELIVERED}} 个
- 上线状态：{{PROJECT_1_LAUNCH_STATUS}}

**价值评估**：
- 用户价值：{{PROJECT_1_USER_VALUE}}
- 商业价值：{{PROJECT_1_BUSINESS_VALUE}}
- 技术价值：{{PROJECT_1_TECH_VALUE}}
- **实际年度收益**：${{PROJECT_1_ACTUAL_ANNUAL_VALUE}}

**ROI 分析**：
```
ROI = (实际年度收益 - 总成本) / 总成本
    = (${{PROJECT_1_ACTUAL_ANNUAL_VALUE}} - ${{PROJECT_1_TOTAL_COST}}) / ${{PROJECT_1_TOTAL_COST}}
    = {{PROJECT_1_ROI}}%
```

**投资回收期**：{{PROJECT_1_PAYBACK_PERIOD}}

**值不值得继续**：
{{#if PROJECT_1_WORTH_CONTINUE}}
✅ **值得继续**
- 理由：{{PROJECT_1_CONTINUE_REASON}}
- 明年目标：{{PROJECT_1_NEXT_YEAR_GOAL}}
- 建议投入：{{PROJECT_1_NEXT_YEAR_RESOURCE}}
{{else}}
❌ **不值得继续**
- 理由：{{PROJECT_1_STOP_REASON}}
- 沉没成本：${{PROJECT_1_SUNK_COST}}
- 明年替代方案：{{PROJECT_1_ALTERNATIVE}}
{{/if}}

---

### 项目 #2：{{PROJECT_2_NAME}}
（同上结构）

---

### 整体评估

**高 ROI 项目（>300%）**：
{{#each HIGH_ROI_PROJECTS}}
- {{this.project}}：{{this.roi}}%（占用 {{this.hours}}h，{{this.percentage}}%）
{{/each}}
- **总计**：{{HIGH_ROI_TIME_PERCENTAGE}}% 时间，创造 {{HIGH_ROI_VALUE_PERCENTAGE}}% 价值

**中 ROI 项目（100-300%）**：
{{#each MID_ROI_PROJECTS}}
- {{this.project}}：{{this.roi}}%（占用 {{this.hours}}h，{{this.percentage}}%）
{{/each}}
- **总计**：{{MID_ROI_TIME_PERCENTAGE}}% 时间，创造 {{MID_ROI_VALUE_PERCENTAGE}}% 价值

**低 ROI 项目（<100%）**：
{{#each LOW_ROI_PROJECTS}}
- {{this.project}}：{{this.roi}}%（占用 {{this.hours}}h，{{this.percentage}}%）
{{/each}}
- **总计**：{{LOW_ROI_TIME_PERCENTAGE}}% 时间，创造 {{LOW_ROI_VALUE_PERCENTAGE}}% 价值

**关键发现**：
- 帕累托定律验证：{{PARETO_TOP_PERCENTAGE}}% 的项目创造了 {{PARETO_VALUE_PERCENTAGE}}% 的价值
- 时间浪费：{{WASTED_TIME_PERCENTAGE}}% 的时间投入在低 ROI 项目（<100%）
- **优化潜力**：如果将低 ROI 项目时间重新分配到高 ROI 项目，预计可提升 {{OPTIMIZATION_POTENTIAL}}% 整体价值

---

## ⏰ 年度时间分配分析

**核心问题**：时间都花在哪里了？值不值得？

### 时间分配饼图

```
总工作时长：{{WORK_HOURS}} 小时

项目开发：{{PROJECT_HOURS}}h（{{PROJECT_PERCENTAGE}}%）
  ├─ 高 ROI 项目：{{HIGH_ROI_HOURS}}h（{{HIGH_ROI_PERCENTAGE}}%）
  ├─ 中 ROI 项目：{{MID_ROI_HOURS}}h（{{MID_ROI_PERCENTAGE}}%）
  └─ 低 ROI 项目：{{LOW_ROI_HOURS}}h（{{LOW_ROI_PERCENTAGE}}%）

技术债务清理：{{TECHDEBT_HOURS}}h（{{TECHDEBT_PERCENTAGE}}%）
效率损失（反复修改）：{{EFFICIENCY_LOSS_HOURS}}h（{{EFFICIENCY_LOSS_PERCENTAGE}}%）
学习成长：{{LEARNING_HOURS}}h（{{LEARNING_PERCENTAGE}}%）
会议协调：{{MEETING_HOURS}}h（{{MEETING_PERCENTAGE}}%）
其他：{{OTHER_HOURS}}h（{{OTHER_PERCENTAGE}}%）
```

### 时间价值分析

| 类型 | 时长 | 占比 | 价值 | 价值占比 | 单位时间价值 | 评估 |
|------|------|------|------|---------|------------|------|
{{#each TIME_ALLOCATION_VALUE}}
| {{this.type}} | {{this.hours}}h | {{this.percentage}}% | ${{this.value}} | {{this.value_percentage}}% | ${{this.value_per_hour}}/h | {{this.evaluation}} |
{{/each}}

**关键发现**：
- 最高价值时间：{{HIGHEST_VALUE_TIME_TYPE}}（${{HIGHEST_VALUE_PER_HOUR}}/h）
- 最低价值时间：{{LOWEST_VALUE_TIME_TYPE}}（${{LOWEST_VALUE_PER_HOUR}}/h）
- 效率损失：{{EFFICIENCY_LOSS_HOURS}}h（{{EFFICIENCY_LOSS_PERCENTAGE}}%），相当于浪费 {{EFFICIENCY_LOSS_WEEKS}} 周
- **优化建议**：如果将效率损失时间投入高价值项目，可额外创造 ${{EFFICIENCY_LOSS_OPPORTUNITY_VALUE}} 价值

---

## 🚀 年度能力提升分析

**核心问题**：这一年学到了什么？掌握了什么？

### 技能掌握清单

**年初掌握**：
{{#each SKILLS_AT_START}}
- {{this.skill}}：{{this.proficiency}}%
{{/each}}

**年末掌握**：
{{#each SKILLS_AT_END}}
- {{this.skill}}：{{this.proficiency}}%（+{{this.growth}}%）
{{/each}}

**新增技能**：
{{#each NEW_SKILLS}}
- {{this.skill}}：{{this.proficiency}}%（从 0 到 {{this.proficiency}}%）
{{/each}}

---

### 能力提升详情

#### 技能 #1：{{SKILL_1_NAME}}

**年初水平**：{{SKILL_1_START_PROFICIENCY}}%

**年末水平**：{{SKILL_1_END_PROFICIENCY}}%

**提升幅度**：+{{SKILL_1_GROWTH}}%

**学习路径**：
{{#each SKILL_1_LEARNING_PATH}}
- {{this.quarter}}：{{this.milestone}}（{{this.proficiency}}%）
{{/each}}

**关键突破**：
{{#each SKILL_1_BREAKTHROUGHS}}
- {{this.breakthrough}}（{{this.date}}）
{{/each}}

**应用场景**：
{{#each SKILL_1_APPLICATIONS}}
- {{this.project}}：{{this.application}}
{{/each}}

**价值评估**：
- 创造价值：${{SKILL_1_VALUE_CREATED}}
- 学习成本：{{SKILL_1_LEARNING_HOURS}}h（${{SKILL_1_LEARNING_COST}}）
- ROI：{{SKILL_1_ROI}}%

---

#### 技能 #2：{{SKILL_2_NAME}}
（同上结构）

---

### 学习效率分析

| 技能 | 学习时长 | 提升幅度 | 学习效率 | 价值创造 | 学习 ROI | 值不值得 |
|------|---------|---------|---------|---------|---------|---------|
{{#each LEARNING_EFFICIENCY}}
| {{this.skill}} | {{this.hours}}h | +{{this.growth}}% | {{this.efficiency}}%/h | ${{this.value}} | {{this.roi}}% | {{this.worth}} |
{{/each}}

**关键发现**：
- 最高效学习：{{HIGHEST_LEARNING_EFFICIENCY_SKILL}}（{{HIGHEST_LEARNING_EFFICIENCY}}%/h）
- 最低效学习：{{LOWEST_LEARNING_EFFICIENCY_SKILL}}（{{LOWEST_LEARNING_EFFICIENCY}}%/h）
- 最高 ROI 学习：{{HIGHEST_LEARNING_ROI_SKILL}}（{{HIGHEST_LEARNING_ROI}}%）
- **优化建议**：明年优先学习高 ROI 技能（{{HIGH_ROI_SKILLS}}）

---

## 🎯 能力矩阵分析（深度）

**核心问题**：我的能力短板在哪里？应该优先提升什么？

### 二维矩阵：重要性 vs 熟练度

```
                高重要性
                  ↑
   紧急提升区 | 保持优势区
   ----------|----------
   低优先级区 | 学习储备区
                  ↓
                低重要性
          ←─────────────→
      低熟练度      高熟练度
```

### 能力分布

**保持优势区**（高重要 + 高熟练）：
{{#each ADVANTAGE_SKILLS}}
- ✅ {{this.skill}}（重要性 {{this.importance}}/5，熟练度 {{this.proficiency}}%）
  - 应用场景：{{this.scenarios}}
  - 年度价值：${{this.value}}
  - 明年策略：{{this.next_year_strategy}}
{{/each}}

---

**紧急提升区**（高重要 + 低熟练）：
{{#each URGENT_SKILLS}}
- ⚠️ {{this.skill}}（重要性 {{this.importance}}/5，熟练度 {{this.proficiency}}%）
  - **影响**：{{this.impact}}
  - **年度损失**：{{this.loss}}
  - **学习难度**：{{this.difficulty}}
  - **预期学习时长**：{{this.learning_hours}}h
  - **预期收益**：${{this.expected_benefit}}
  - **学习 ROI**：{{this.learning_roi}}%
  - **优先级**：{{this.priority}}（{{this.priority_reason}}）
{{/each}}

---

**学习储备区**（低重要 + 高熟练）：
{{#each RESERVE_SKILLS}}
- 💡 {{this.skill}}（重要性 {{this.importance}}/5，熟练度 {{this.proficiency}}%）
  - 应用场景：{{this.scenarios}}
  - 明年策略：{{this.next_year_strategy}}
{{/each}}

---

**低优先级区**（低重要 + 低熟练）：
{{#each LOW_PRIORITY_SKILLS}}
- ⚪ {{this.skill}}（重要性 {{this.importance}}/5，熟练度 {{this.proficiency}}%）
  - 明年策略：{{this.next_year_strategy}}
{{/each}}

---

### 能力缺口分析

**最大能力缺口**（重要性 - 熟练度）：
{{#each CAPABILITY_GAPS}}
{{@index}}. **{{this.skill}}**（缺口 {{this.gap}} 分）
   - 重要性：{{this.importance}}/5（{{this.importance_reason}}）
   - 熟练度：{{this.proficiency}}%（{{this.proficiency_reason}}）
   - **影响**：{{this.impact}}
   - **年度损失**：{{this.loss}}
   - **弥补策略**：{{this.fill_strategy}}
   - **预期收益**：${{this.expected_benefit}}
{{/each}}

---

### 能力组合优化

**当前能力组合**：
- 高重要高熟练：{{ADVANTAGE_SKILLS_COUNT}} 个（{{ADVANTAGE_PERCENTAGE}}%）
- 高重要低熟练：{{URGENT_SKILLS_COUNT}} 个（{{URGENT_PERCENTAGE}}%）
- 低重要高熟练：{{RESERVE_SKILLS_COUNT}} 个（{{RESERVE_PERCENTAGE}}%）
- 低重要低熟练：{{LOW_PRIORITY_SKILLS_COUNT}} 个（{{LOW_PRIORITY_PERCENTAGE}}%）

**理想能力组合**（基于行业标准）：
- 高重要高熟练：应占 {{IDEAL_ADVANTAGE_PERCENTAGE}}%
- 高重要低熟练：应占 {{IDEAL_URGENT_PERCENTAGE}}%

**优化路径**：
{{#each CAPABILITY_OPTIMIZATION_PATH}}
{{this.priority}}. {{this.action}}（预计耗时 {{this.hours}}h，预期收益 ${{this.benefit}}）
{{/each}}

---

## 🎯 年度 OKR 达成情况

**数据来源**：基于 {{QUARTER_COUNT}} 个季度的 OKR 汇总

### 年度整体达成率

**O1：{{ANNUAL_OBJECTIVE_1}}**

| KR | 目标值 | 实际值 | 达成率 | 季度进展 |
|----|--------|--------|--------|---------|
{{#each ANNUAL_O1_KRS}}
| {{this.kr}} | {{this.target}} | {{this.actual}} | {{this.achievement_rate}}% | {{this.quarterly_progress}} |
{{/each}}

**整体达成率**：{{ANNUAL_O1_ACHIEVEMENT_RATE}}%

**达成/未达成原因**：
- {{ANNUAL_O1_REASON}}

---

### O2：{{ANNUAL_OBJECTIVE_2}}
（同上结构）

---

### 年度 OKR 总结

**整体达成率**：{{OVERALL_ANNUAL_ACHIEVEMENT_RATE}}%（{{ACHIEVED_ANNUAL_KR_COUNT}}/{{TOTAL_ANNUAL_KR_COUNT}} 个 KR 达成）

**达成情况分布**：
- ✅ 超额达成（≥110%）：{{EXCEEDED_ANNUAL_KR_COUNT}} 个
- ✅ 达成（90-110%）：{{ACHIEVED_ANNUAL_KR_COUNT}} 个
- ⚠️ 基本达成（70-90%）：{{PARTIALLY_ACHIEVED_ANNUAL_KR_COUNT}} 个
- ❌ 未达成（<70%）：{{NOT_ACHIEVED_ANNUAL_KR_COUNT}} 个

**年度 OKR vs ROI 对比**：
| OKR | 达成率 | 投入时间 | ROI | 评估 |
|-----|--------|---------|-----|------|
{{#each ANNUAL_OKR_VS_ROI}}
| {{this.okr}} | {{this.achievement}}% | {{this.hours}}h | {{this.roi}}% | {{this.evaluation}} |
{{/each}}

**关键洞察**：
{{#each ANNUAL_OKR_INSIGHTS}}
- {{this.insight}}
{{/each}}

---

## 🤖 年度自我进化分析（完整版）

### Model 层（底层模型）
**年初版本**：{{MODEL_VERSION_START}}  
**年末版本**：{{MODEL_VERSION_END}}  
**年度升级**：{{MODEL_UPGRADES}}  
**评估**：{{MODEL_EVALUATION}}

**主要能力提升**：
{{#each MODEL_CAPABILITY_IMPROVEMENTS}}
- {{this.capability}}：{{this.improvement}}
{{/each}}

---

### Harness 层（执行框架）
**年度变化**：
{{#each HARNESS_ANNUAL_CHANGES}}
- {{this.quarter}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{HARNESS_EVALUATION}}

**量化效果**：
{{#each HARNESS_ANNUAL_EFFECTS}}
- {{this.metric}}：{{this.effect}}
{{/each}}

**优化迭代**：
- 年度迭代次数：{{HARNESS_ANNUAL_ITERATION_COUNT}} 次
- 主要优化方向：{{HARNESS_ANNUAL_OPTIMIZATION_FOCUS}}
- A/B 测试次数：{{HARNESS_ANNUAL_AB_TEST_COUNT}} 次
- 成功率：{{HARNESS_OPTIMIZATION_SUCCESS_RATE}}%

**关键突破**：
{{#each HARNESS_BREAKTHROUGHS}}
- {{this.breakthrough}}（{{this.date}}，效果：{{this.effect}}）
{{/each}}

---

### Context 层（可配置上下文）
**年度变化**：
{{#each CONTEXT_ANNUAL_CHANGES}}
- {{this.quarter}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{CONTEXT_EVALUATION}}

**量化效果**：
{{#each CONTEXT_ANNUAL_EFFECTS}}
- {{this.metric}}：{{this.effect}}
{{/each}}

**知识库年度增长**：
- 年初规模：{{CONTEXT_START_SIZE}}
- 年末规模：{{CONTEXT_END_SIZE}}
- 增长率：+{{CONTEXT_GROWTH_RATE}}%
- 新增经验：{{NEW_EXPERIENCES_ANNUAL}} 条
- 新增规则：{{NEW_RULES_ANNUAL}} 条
- 新增技能：{{NEW_SKILLS_ANNUAL}} 个
- Skills 优化：{{SKILLS_OPTIMIZED_ANNUAL}} 个

**知识质量**：
- 知识复用率：{{KNOWLEDGE_REUSE_RATE}}%
- 知识准确率：{{KNOWLEDGE_ACCURACY_RATE}}%
- 知识时效性：{{KNOWLEDGE_TIMELINESS}}

---

### Traces 层（执行日志）
**年度变化**：
{{#each TRACES_ANNUAL_CHANGES}}
- {{this.quarter}}: {{this.change_type}} {{this.desc}}
{{/each}}

**评估**：{{TRACES_EVALUATION}}

**Traces 年度积累**：
- 总 traces 数：{{TOTAL_TRACES_ANNUAL}}
- 年度新增：{{NEW_TRACES_ANNUAL}}
- 分析次数：{{ANALYSIS_COUNT_ANNUAL}}
- 转化为规则：{{TRACES_TO_RULES_COUNT_ANNUAL}} 条
- 转化率：{{TRACES_TO_RULES_RATE}}%

**Traces 价值**：
- 基于 traces 优化次数：{{TRACES_OPTIMIZATION_COUNT}} 次
- 预计节省成本：${{TRACES_SAVED_COST}}
- ROI：{{TRACES_ROI}}%

---

### 整体评估
{{EVOLUTION_ANNUAL_SUMMARY}}

**年度进化速度**：
- Model 层：{{MODEL_EVOLUTION_SPEED_ANNUAL}}
- Harness 层：{{HARNESS_EVOLUTION_SPEED_ANNUAL}}
- Context 层：{{CONTEXT_EVOLUTION_SPEED_ANNUAL}}
- Traces 层：{{TRACES_EVOLUTION_SPEED_ANNUAL}}

**年度进化成果**：
{{#each EVOLUTION_ANNUAL_ACHIEVEMENTS}}
- {{this.achievement}}（{{this.layer}} 层，{{this.effect}}）
{{/each}}

**明年进化目标**：
{{#each NEXT_YEAR_EVOLUTION_GOALS}}
{{this.priority}}. {{this.goal}}（{{this.layer}} 层）
{{/each}}

---

## 🎯 系统动力学分析（年度总结）

### 正反馈循环年度表现

**循环 #1：{{POSITIVE_LOOP_1_NAME}}**

**年度强度变化**：
| 季度 | 循环强度 | 放大效果 | 量化收益 | 趋势 |
|------|---------|---------|---------|------|
{{#each POSITIVE_LOOP_1_ANNUAL}}
| {{this.quarter}} | {{this.strength}} | {{this.amplification}} | ${{this.benefit}} | {{this.trend}} |
{{/each}}

**年度总收益**：${{POSITIVE_LOOP_1_TOTAL_BENEFIT}}

**明年放大策略**：
{{#each POSITIVE_LOOP_1_NEXT_YEAR_AMPLIFY}}
- {{this.strategy}}（预期效果：{{this.effect}}，投入：{{this.hours}}h）
{{/each}}

---

### 负反馈循环年度表现

**循环 #1：{{NEGATIVE_LOOP_1_NAME}}**

**年度强度变化**：
| 季度 | 循环强度 | 负面影响 | 量化损失 | 趋势 |
|------|---------|---------|---------|------|
{{#each NEGATIVE_LOOP_1_ANNUAL}}
| {{this.quarter}} | {{this.strength}} | {{this.damage}} | ${{this.loss}} | {{this.trend}} |
{{/each}}

**年度总损失**：${{NEGATIVE_LOOP_1_TOTAL_LOSS}}

**打破效果评估**：
{{#each NEGATIVE_LOOP_1_BREAK_RESULTS}}
- {{this.strategy}}：{{this.status}}，效果 {{this.effect}}，节省 ${{this.saved}}
{{/each}}

**明年持续优化**：
{{#each NEGATIVE_LOOP_1_NEXT_YEAR_BREAK}}
- {{this.strategy}}（预期效果：{{this.effect}}，投入：{{this.hours}}h）
{{/each}}

---

## 📅 明年战略规划（数据驱动）

**核心问题**：明年最应该做什么？为什么？

### 战略选择框架

基于今年数据分析，明年战略方向应满足：
1. **高 ROI**（>300%）
2. **高边际效益**（>$100/h）
3. **能力匹配**（熟练度 >60% 或学习 ROI >500%）
4. **战略价值**（符合长期目标）

---

### 明年战略方向 #1：{{NEXT_YEAR_DIRECTION_1}}

**为什么选择这个方向**：
- 今年数据：{{NEXT_YEAR_D1_THIS_YEAR_DATA}}
- ROI：{{NEXT_YEAR_D1_ROI}}%（排名第 {{NEXT_YEAR_D1_ROI_RANK}}）
- 边际效益：${{NEXT_YEAR_D1_MARGINAL_BENEFIT}}/h
- 能力匹配度：{{NEXT_YEAR_D1_CAPABILITY_MATCH}}%
- 战略价值：{{NEXT_YEAR_D1_STRATEGIC_VALUE}}

**明年目标**（SMART）：
- Specific：{{NEXT_YEAR_D1_SPECIFIC}}
- Measurable：{{NEXT_YEAR_D1_MEASURABLE}}
- Achievable：{{NEXT_YEAR_D1_ACHIEVABLE}}
- Relevant：{{NEXT_YEAR_D1_RELEVANT}}
- Time-bound：{{NEXT_YEAR_D1_TIME_BOUND}}

**资源配置**：
- 时间投入：{{NEXT_YEAR_D1_TIME}} 小时（{{NEXT_YEAR_D1_TIME_PERCENTAGE}}%）
- 预算：${{NEXT_YEAR_D1_BUDGET}}
- 能力储备：{{NEXT_YEAR_D1_CAPABILITY_PREP}}

**预期产出**：
- {{NEXT_YEAR_D1_OUTPUT}}

**预期价值**：
- 用户价值：{{NEXT_YEAR_D1_USER_VALUE}}
- 商业价值：{{NEXT_YEAR_D1_BUSINESS_VALUE}}
- 个人成长：{{NEXT_YEAR_D1_PERSONAL_GROWTH}}
- 量化收益：${{NEXT_YEAR_D1_QUANTIFIED_VALUE}}

**关键里程碑**：
{{#each NEXT_YEAR_D1_MILESTONES}}
- {{this.quarter}}：{{this.milestone}}（验证标准：{{this.criteria}}）
{{/each}}

**风险与对策**：
{{#each NEXT_YEAR_D1_RISKS}}
- 风险：{{this.risk}}（概率 {{this.probability}}%，影响 {{this.impact}}）
  - 对策：{{this.mitigation}}
{{/each}}

---

### 明年战略方向 #2：{{NEXT_YEAR_DIRECTION_2}}
（同上结构）

---

### 明年战略方向 #3：{{NEXT_YEAR_DIRECTION_3}}
（同上结构）

---

### 明年资源配置总览

**时间分配**：
| 方向 | 时长 | 占比 | 预期 ROI | 预期价值 |
|------|------|------|---------|---------|
{{#each NEXT_YEAR_TIME_ALLOCATION}}
| {{this.direction}} | {{this.hours}}h | {{this.percentage}}% | {{this.roi}}% | ${{this.value}} |
{{/each}}

**对比今年**：
| 类型 | 今年时间占比 | 明年时间占比 | 变化 | 原因 |
|------|------------|------------|------|------|
{{#each NEXT_YEAR_VS_THIS_YEAR}}
| {{this.type}} | {{this.this_year}}% | {{this.next_year}}% | {{this.change}} | {{this.reason}} |
{{/each}}

**关键调整**：
{{#each NEXT_YEAR_KEY_ADJUSTMENTS}}
- {{this.adjustment}}（预期效果：{{this.effect}}）
{{/each}}

---

### 明年学习计划（能力缺口弥补）

**基于能力矩阵分析，明年优先学习：**

| 优先级 | 技能 | 当前熟练度 | 目标熟练度 | 学习时长 | 预期收益 | 学习 ROI |
|--------|------|-----------|-----------|---------|---------|---------|
{{#each NEXT_YEAR_LEARNING_PLAN}}
| {{this.priority}} | {{this.skill}} | {{this.current}}% | {{this.target}}% | {{this.hours}}h | ${{this.benefit}} | {{this.roi}}% |
{{/each}}

**学习策略**：
{{#each NEXT_YEAR_LEARNING_STRATEGIES}}
- {{this.skill}}：{{this.strategy}}
{{/each}}

---

### 明年强制执行规则（基于今年教训）

{{#each NEXT_YEAR_RULES}}
- [ ] {{this.rule}}（来源：{{this.source}}，预期节省：{{this.saving}}）
{{/each}}

---

## 📊 年度总结

### 🎯 年度 OKR 达成情况

| 目标 | 目标值 | 实际值 | 达成率 | 评估 |
|------|--------|--------|--------|------|
{{#each ANNUAL_OKRS}}
| {{this.okr}} | {{this.target}} | {{this.actual}} | {{this.achievement_rate}}% | {{this.evaluation}} |
{{/each}}

### 🏆 最有价值的事情（Top 3）

{{#each TOP_VALUES}}
{{@index}}. **{{this.thing}}**
   - 产出：{{this.output}}
   - 价值：{{this.value}}
   - ROI：{{this.roi}}%
   - 为什么排第 {{@index}}：{{this.reason}}
{{/each}}

### ⚠️ 最大的浪费（Top 3）

{{#each TOP_WASTES}}
{{@index}}. **{{this.waste}}**（占用 {{this.hours}}h，{{this.percentage}}%）
   - 为什么是浪费：{{this.reason}}
   - 累计损失：{{this.loss}}
   - 如果重来：{{this.alternative}}
{{/each}}

### 💡 关键教训（{{EXPERIENCE_COUNT_ANNUAL}} 条）

{{#each KEY_EXPERIENCES_ANNUAL}}
{{@index}}. {{this.experience}}（{{this.benefit}}）
{{/each}}

### 📈 能力提升总结

**新增技能**：{{NEW_SKILLS_COUNT}} 个  
**技能提升**：平均 +{{AVERAGE_SKILL_GROWTH}}%  
**最大突破**：{{BIGGEST_BREAKTHROUGH}}（+{{BIGGEST_BREAKTHROUGH_GROWTH}}%）

### 🎯 明年三大战略方向

1. **{{NEXT_YEAR_DIRECTION_1}}**（{{NEXT_YEAR_D1_TIME_PERCENTAGE}}% 时间，预期 ROI {{NEXT_YEAR_D1_ROI}}%）
2. **{{NEXT_YEAR_DIRECTION_2}}**（{{NEXT_YEAR_D2_TIME_PERCENTAGE}}% 时间，预期 ROI {{NEXT_YEAR_D2_ROI}}%）
3. **{{NEXT_YEAR_DIRECTION_3}}**（{{NEXT_YEAR_D3_TIME_PERCENTAGE}}% 时间，预期 ROI {{NEXT_YEAR_D3_ROI}}%）

---

## 📚 附录：年度产出文档索引

### 季报（{{QUARTERLY_REPORT_COUNT}} 份）
{{#each QUARTERLY_REPORTS}}
{{@index}}. [季报-{{this.quarter}}季度]({{this.path}}) - {{this.summary}}
{{/each}}

### 月报（{{MONTHLY_REPORT_COUNT}} 份）
（略，详见各季报）

### 分析报告（{{ANALYSIS_REPORT_COUNT}} 份）
{{#each ANALYSIS_REPORTS}}
{{@index}}. [{{this.name}}]({{this.path}}) - {{this.summary}}
{{/each}}

---

**记录时间**：{{RECORD_TIME}}  
**填写耗时**：{{FILL_TIME}} 分钟（基于 {{QUARTERLY_REPORT_COUNT}} 份季报内容生成）

---

## 🔧 生成说明

**强制流程**：
1. ✅ 第一步：读取全年所有季报（绝对优先）
2. ✅ 第二步：选择性读取月报（如季报不完整）
3. ✅ 第三步：采集 Git 数据（补充）
4. ✅ 第四步：生成年报（强调价值评估、ROI 排序、能力矩阵、战略规划）

**数据来源**：
- 季报：{{QUARTERLY_REPORT_LIST}}
- 月报：{{MONTHLY_REPORT_LIST}}（如需要）
- Git log：{{GIT_LOG_RANGE}}
- Traces：{{TRACES_RANGE}}
