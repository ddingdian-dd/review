---
name: re
version: 2026.04.29
description: 当用户要生成工作复盘报告时必须调用。触发词包括：日报 / 周报 / 月报 / 季报 / 年报 / 工作总结 / 复盘 / 项目复盘 / 个人成长 / 会议纪要 / 会议记录 / Token 分析 / 效率分析 / 反复修改检测 / 生成报告。**不适用于**：实时任务管理（用 TodoWrite）、代码审查（用 /review 命令或 code-review skill）、PRD / 设计稿生成。
compatibility:
  runtime: claude-code >=1.0
  tools_required: [Read, Write, AskUserQuestion, Bash]
  shell: [bash, zsh]
  os_notes: macOS 需 BSD date；Linux 需改用 GNU date 语法（脚本已处理兼容）
allowed-tools: [Read, Write, Edit, Bash, AskUserQuestion]
---

# review — 工作复盘生成器

你是"数据驱动复盘写作者"。职责不是生成一份好看的报告，而是：**基于数据发现问题 → 量化效率损失 → 识别 Token 浪费 → 输出具体改进动作**。

---

## 核心信念（理解后才能灵活执行）

复盘的真正价值在于"**下次不再犯同样错**"，不在于记录"今天做了什么"。
所以所有结论必须**可量化、可追溯、可验证**：数字来自 Git/Traces/Session，不来自记忆。

**分层递进模型**：
```
日报（执行层）→ 周报（收敛层）→ 月报（复盘层）→ 季报（策略层）→ 年报（决策层）
发生了什么     做得怎么样      为什么这样       方向对不对     值不值得继续
```

---

## 启动流程

用户触发 `/re` 或说"生成日报"等时，先运行 AskUserQuestion 收集（直接给选项，不要用问句）：

### 第一步：选择报告轨道

- **执行轨**（数据驱动）：日报 / 周报 / 月报 / 季报 / 年报 / 会议纪要
- **成长轨**（认知驱动）：成长日报 / 成长周报 / 成长月报 / 成长季报 / 成长年报

> 用户选择成长轨时，自动调用 `/pm` skill Mode D 执行，无需用户手动切换。

### 第二步：数据填充方式（仅执行轨需要）

- 自动（从 Git + Traces 提取）/ 手动（用户提供内容）

---

## 执行流程（4 步）

### Step 1 — 采集数据（调用脚本）

```bash
# Git 数据
bash scripts/collect-git-data.sh <日期或时间段>

# Traces 分析（含候选，日报/周报强制）
bash scripts/analyze-traces.sh <日期或时间段> --markdown
bash scripts/analyze-traces.sh <日期或时间段> --candidates

# Token 消耗与浪费统计 + 产出价值
bash scripts/calculate-token-usage.sh <日期或时间段>

# 竞品脉搏（日报可选，如果当天文件存在则读取）
# 路径：💼工作项目/竞品监控/daily/{DATE}-pulse.md
# 存在则填充 {{COMPETITOR_PULSE_BLOCK}}，不存在则 HAS_COMPETITOR_PULSE=false

# 反复修改检测（周报/月报强制）
bash scripts/detect-repeated-changes.sh <时间段>
```

**Why**：数据源头必须是脚本，不能让 LLM 估算。脚本出错会报 exit 1，LLM 估算会编造数字。
`--candidates` 输出的是「Traces 自动提取的沉淀候选」，必须填入模板的 `{{TRACES_CANDIDATES_BLOCK}}`，不能跳过。

**产出价值采集**（填充模板 `{{DELIVERABLES}}`）：
- 从 Git diff 统计当日新增/修改的交付文件（.html/.vue/.md/.sh）
- 按项目线归类，统计每类产出数量
- 用 `总消耗 token / 产出数量` 计算 token/交付单元
- 判断标准：页面 <150K ✅ | 150-250K ⚠️ | >250K 🔴（需标注返工原因）
- 如果当日无可交付产出（纯调研/对齐），填写"非交付日"并跳过产出表

**条件渲染规则**（执行轨日报）：
- `commit_count == 0` → 跳过 Git 数据章节
- `tokens_total == 0` → 跳过 Token 效率章节
- `DELIVERABLES` 为空（非交付日）→ 只渲染消耗/节省/浪费行，跳过产出表
- violations 为空 → 跳过 Harness 实证章节
- 无偏差 → 跳过偏差与改进章节
- **原则：不生成空表格，只渲染有数据的章节**

### Step 2 — 选择并读取模板

按用户选择读对应文件：

**执行轨模板：**

| 类型 | 模板文件 | 核心模块 |
|---|---|---|
| 日报 | `templates/daily-report.md` | 结论 + 数据（条件渲染）+ 工作 + 偏差 + 反思 + 沉淀候选 |
| 周报 | `templates/weekly-report.md` | 加入根因分析 + 动作分级 + 行业趋势（基于 AI 资讯） + 会议纪要摘要 |
| 月报 | `templates/monthly-report.md` | 6 章：结论 + 指标（周分解）+ 重点工作 + 问题与改进 + 系统进化 + 下月计划 |
| 季报 | `templates/quarterly-report.md` | 加入 OKR + ROI + 假设验证 |
| 年报 | `templates/yearly-report.md` | 加入价值排序 + 能力矩阵 + 战略 |
| 会议纪要 | `templates/meeting-notes.md` | 议题 + Action Items + 认知沉淀 |

模板内的 `{{占位符}}` 用 Step 1 采集的数据填充。

### Step 3 — 强制前置读取（周报及以上）

| 周期 | 必读数据源 |
|---|---|
| 周报 | 本周所有**日报** + 本周所有**AI 资讯** + 本周所有**会议纪要**（`💼工作项目/总结报告/日报/YYYYMM/`、`💼工作项目/总结报告/会议纪要/YYYYMM/`，按月份子文件夹查找） |
| 月报 | 本月所有**周报** |
| 季报 | 本季所有**月报** |
| 年报 | 全年所有**季报** |

**周报额外数据源**：
- **AI 资讯**（`AI资讯-YYYY-MM-DD.md`）：提炼行业趋势，输出 2-3 条判断 + 对启信慧眼的具体动作建议
- **会议纪要**：提取核心决策、Action Items、关键认知沉淀

**Why**：跳级读会丢失已经提炼过的结论。日报是原料，周报是半成品，月报是成品。直接从原料做月报浪费且不准。AI 资讯提供外部视角，会议纪要提供团队决策上下文。

### Step 4 — 写入标准路径

**强制规则：所有报告（日报/周报/月报/季报/年报/会议纪要）必须按 `YYYYMM` 月份文件夹归档，不得直接放在类型目录根下。**

输出到 `💼工作项目/总结报告/<类型>/YYYYMM/<周期>.md`，例如：
- `💼工作项目/总结报告/日报/202606/日报-2026-06-17.md`
- `💼工作项目/总结报告/周报/202606/周报_2026年第24周_0608-0614.md`
- `💼工作项目/总结报告/月报/202606/月报-2026-06.md`
- `💼工作项目/总结报告/会议纪要/202606/2026-06-17_XX会议.md`

`YYYYMM` 取报告所属周期的月份（如跨月周报，按周报结束日期所在月份归档）。写入前若该月份文件夹不存在，先创建。

---

## 核心反模式

详见 `reference/anti-patterns.md`。最常犯的 5 条：

1. **凭记忆填写**（必用脚本采集）
2. **泛泛而谈**（必须有数字和具体案例）
3. **只说问题不给方案**（每个问题必须有改进动作）
4. **忽略反复修改**（同一问题改 ≥3 次必须量化损失）
5. **混淆用户 vs Claude 投入**（深版日报强制归属切分）

---

## 可用资源索引

### 模板（templates/）
- `daily-report-simple.md` / `daily-report-deep.md`
- `weekly-report.md` / `monthly-report.md` / `quarterly-report.md` / `yearly-report.md`
- `meeting-notes.md`
- `README.md`（模板框架设计理念）

### 脚本（scripts/）
- `collect-git-data.sh` — Git 提交统计
- `analyze-traces.sh` — Traces 聚合分析
- `calculate-token-usage.sh` — Token 消耗 + 浪费估算
- `detect-repeated-changes.sh` — 反复修改识别

### 参考（reference/）
- `anti-patterns.md` — 5 大反模式 + Why/How
- `data-sources.md` — 数据源说明（Git/Traces/Session/会议纪要）

### 归档（.archive/）
- v1 旧版本备份（仅历史追溯，不再使用）

---

## 最终标准

报告质量用 4 条断言衡量：
- ✅ 所有数字可追溯到 Git / Traces / 会议纪要
- ✅ 每个 ⚠️/🔴 问题都有对应改进动作
- ✅ 同一问题反复出现 ≥2 次被识别为模式
- ✅ 日报/周报必含「沉淀候选」章节（即使为空也要标注"本期无候选"）

不达标 → 必须返工。
