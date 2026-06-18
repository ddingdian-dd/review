# {{TITLE}}

---
date: {{DATE}}
title: {{TITLE}}
duration: {{DURATION}}
attendees:
  - {{ATTENDEE_1}}
  - {{ATTENDEE_2}}
type: {{MEETING_TYPE}}
source: {{SOURCE}}
---

## 会议议题

1. {{TOPIC_1}}
2. {{TOPIC_2}}

---

## 议题一：{{TOPIC_1}}

### 核心问题
- {{PROBLEM_1}}

### 决策
- ✅ {{DECISION_1}}
- ⚠️ {{DECISION_WITH_CONDITION}}
- 🔴 {{BLOCKED_OR_REJECTED}}

### 关键观点
> "{{KEY_QUOTE}}"（发言人）

### 数据 / 事实
- {{FACT_1}}

---

## 议题二：{{TOPIC_2}}

（同上结构）

---

## Action Items

按负责人分组，便于后续跟进和读取。

### {{OWNER_1}}
- [ ] {{ACTION_1}}（截止：{{DEADLINE}}）
- [ ] {{ACTION_2}}

### {{OWNER_2}}
- [ ] {{ACTION_3}}

---

## 核心认知沉淀（我的思考）

**方法论层面**
1. {{METHODOLOGY_INSIGHT}}

**产品层面**
1. {{PRODUCT_INSIGHT}}

**团队协作**
1. {{COLLABORATION_INSIGHT}}

---

## 待跟进（留给下次会议）

- [ ] {{FOLLOWUP_1}}
- [ ] {{FOLLOWUP_2}}

---

## 模板使用说明

**路径**：`💼工作项目/总结报告/会议纪要/YYYY-MM-DD_会议主题.md`

**字段规则**：
- `type`：周度对齐 / 项目评审 / 决策会 / 头脑风暴 / 客户反馈等
- `source`：豆包会议记录 / 飞书妙记 / 手写笔记
- **Action Items 必须按人分组**，方便周报/月报自动聚合待办
- **决策用 ✅⚠️🔴 三级标注**（已定 / 有条件 / 被否）
- **关键观点保留原话**（引号包裹 + 发言人）

**review 集成点**：
- 日报 v3：当日会议纪要的决策 + action items 归入"用户投入"段
- 周报 v2：汇总本周所有会议决策，识别"反复讨论但未落地"的议题
- 月报 v2：识别模式（同一问题是否多次出现在会议中）
