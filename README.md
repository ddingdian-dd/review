# review — 工作复盘生成器

数据驱动的工作复盘报告生成 skill。职责不是生成一份好看的报告，而是：**基于数据发现问题 → 量化效率损失 → 识别 Token 浪费 → 输出具体改进动作**。

核心信念：复盘的真正价值在于"下次不再犯同样错"，不在于记录"今天做了什么"。所有结论必须**可量化、可追溯、可验证**，数字来自 Git / Traces / Session，不来自记忆。

## 分层递进模型

```
日报（执行层）→ 周报（收敛层）→ 月报（复盘层）→ 季报（策略层）→ 年报（决策层）
发生了什么     做得怎么样      为什么这样       方向对不对     值不值得继续
```

## 支持的报告类型

| 类型 | 模板 | 核心模块 |
|---|---|---|
| 日报 | `templates/daily-report.md` | 结论 + 数据 + 工作 + 偏差 + 反思 + 沉淀候选 |
| 周报 | `templates/weekly-report.md` | 根因分析 + 动作分级 + 行业趋势 + 会议纪要摘要 |
| 月报 | `templates/monthly-report.md` | 结论 + 指标 + 重点工作 + 问题改进 + 系统进化 + 下月计划 |
| 季报 | `templates/quarterly-report.md` | OKR + ROI + 假设验证 |
| 年报 | `templates/yearly-report.md` | 价值排序 + 能力矩阵 + 战略 |
| 会议纪要 | `templates/meeting-notes.md` | 议题 + Action Items + 认知沉淀 |

## 执行流程

1. **采集数据**：通过脚本从 Git / Traces / Session 提取，禁止 LLM 估算
2. **选择模板**：按报告类型读取对应模板，用采集数据填充占位符
3. **前置读取**（周报及以上）：周报读本周日报 + AI 资讯 + 会议纪要，月报读本月周报，逐级递进
4. **写入归档**：按 `YYYYMM` 月份文件夹归档到标准路径

## 目录结构

```
re/
├── SKILL.md          # skill 主定义（触发词、流程、标准）
├── scripts/          # 数据采集脚本
│   ├── collect-git-data.sh        # Git 提交统计
│   ├── analyze-traces.sh          # Traces 聚合分析
│   ├── calculate-token-usage.sh   # Token 消耗 + 浪费估算
│   └── detect-repeated-changes.sh # 反复修改识别
├── templates/        # 各类报告模板
├── reference/        # 参考文档
│   ├── anti-patterns.md           # 5 大反模式 + Why/How
│   └── data-sources.md            # 数据源说明
└── .archive/         # v1 旧版本备份
```

## 质量标准

报告质量用 4 条断言衡量：

- 所有数字可追溯到 Git / Traces / 会议纪要
- 每个 ⚠️/🔴 问题都有对应改进动作
- 同一问题反复出现 ≥2 次被识别为模式
- 日报/周报必含「沉淀候选」章节（即使为空也要标注"本期无候选"）

不达标必须返工。

## 安装

作为 Claude Code skill 使用，将本仓库内容放到 `~/.claude/skills/re/` 目录下即可。
