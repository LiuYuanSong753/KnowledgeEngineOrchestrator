---
tags:
  - {{DOMAIN}}
  - 知识图谱
  - 知识点清单
aliases:
  - 领域知识点清单
---

# 领域知识点清单：{{DOMAIN}}

> [!info] 文档说明
> 本文档由 **知识分析师** 对「{{DOMAIN}} - {{DIRECTION}}」领域进行体系化拆解后，经 **Obsidian文档编写助手** 统一生成。涵盖该领域从入门到高级的全量核心知识点清单。

---

## 知识点总览

- **领域名称**：{{DOMAIN}}
- **方向**：{{DIRECTION}}
- **知识图谱版本**：{{VERSION}}
- **知识点总数**：{{TOTAL_COUNT}}
- **拆分粒度**：{{GRANULARITY}}
- **覆盖深度**：{{DEPTH}}
- **生成风格**：{{STYLE}}
- **覆盖学科**：{{SUBJECTS_LIST}}

### 难度分布

| 难度层级 | 数量 | 占比 |
|:---|:---:|:---:|
| 入门级 | {{BEGINNER_COUNT}} | {{BEGINNER_PCT}} |
| 进阶级 | {{INTERMEDIATE_COUNT}} | {{INTERMEDIATE_PCT}} |
| 高级 | {{ADVANCED_COUNT}} | {{ADVANCED_PCT}} |

### 类型分布

| 知识点类型 | 数量 | 占比 |
|:---|:---:|:---:|
| 核心概念 | {{CORE_COUNT}} | {{CORE_PCT}} |
| 方法/算法 | {{METHOD_COUNT}} | {{METHOD_PCT}} |
| 工具实践 | {{TOOL_COUNT}} | {{TOOL_PCT}} |
| 对比辨析 | {{COMPARE_COUNT}} | {{COMPARE_PCT}} |
| 应用案例 | {{CASE_COUNT}} | {{CASE_PCT}} |

### 学科覆盖

| 学科 | 缩写 | 知识点数 |
|:---|:---:|:---:|
{{#EACH SUBJECTS_COVERED}}
| {{SUBJECT}} | {{ABBREVIATION}} | {{COUNT}} |
{{/EACH}}

{{#IF TRUNCATION_WARNING}}
> [!warning] 裁剪提示
> {{TRUNCATION_WARNING}}
{{/IF}}

---

## 跨学科依赖关系

{{#IF CROSS_DEPS}}
| 依赖方 | 被依赖方 | 原因 |
|:---|:---|:---|
{{#EACH CROSS_DEPS}}
| {{FROM}} {{FROM_NAME}} | {{TO}} {{TO_NAME}} | {{REASON}} |
{{/EACH}}
{{/IF}}
{{#IF NO_CROSS_DEPS}}
> 无跨学科依赖关系。
{{/IF}}

---

## 入门级知识点

| 知识点ID | 知识点名称 | 类型 | 学科 | 前置依赖 | 描述 |
|:---|:---|:---|:---|:---|:---|
{{#EACH BEGINNER_POINTS}}
| {{ID}} | {{NAME}} | {{TYPE}} | {{SUBJECT}} | {{PREREQUISITES}} | {{DESCRIPTION}} |
{{/EACH}}

---

## 进阶级知识点

| 知识点ID | 知识点名称 | 类型 | 学科 | 前置依赖 | 描述 |
|:---|:---|:---|:---|:---|:---|
{{#EACH INTERMEDIATE_POINTS}}
| {{ID}} | {{NAME}} | {{TYPE}} | {{SUBJECT}} | {{PREREQUISITES}} | {{DESCRIPTION}} |
{{/EACH}}

---

## 高级知识点

| 知识点ID | 知识点名称 | 类型 | 学科 | 前置依赖 | 描述 |
|:---|:---|:---|:---|:---|:---|
{{#EACH ADVANCED_POINTS}}
| {{ID}} | {{NAME}} | {{TYPE}} | {{SUBJECT}} | {{PREREQUISITES}} | {{DESCRIPTION}} |
{{/EACH}}

{{#IF SHOW_EXAM_WEIGHT}}
---

## 面试高频考点（星级标注）

| 知识点ID | 知识点名称 | 星级 | 常见面试问题 |
|:---|:---|:---:|:---|
{{#EACH EXAM_WEIGHTED}}
| {{ID}} | {{NAME}} | {{EXAM_WEIGHT}}⭐ | {{COMMON_QUESTIONS}} |
{{/EACH}}
{{/IF}}

---

## 前置依赖关系图

```mermaid
flowchart TD
{{MERMAID_GRAPH}}
```

> [!tip] 阅读提示
> 绿色节点 = 入门级 / 橙色节点 = 进阶级 / 红色节点 = 高级。箭头表示"依赖"关系（A → B 表示 A 依赖 B）。虚线表示跨学科依赖。

---

## 使用说明

1. **学习路径**：建议按「入门级 → 进阶级 → 高级」顺序学习。
2. **前置依赖**：标有前置依赖的知识点需先掌握依赖项。
3. **跨学科依赖**：标注了跨学科依赖的知识点需跨越学科边界学习前置内容。
4. **学科切换**：可按学科章节（见上方"学科覆盖"表）分科学习。
5. **项目实践**：每个知识点的实践对应关系请查阅 [[0-体系总索引#知识点项目映射表|映射表]]。
6. **教学指南**：系统化教学请查阅 [[3-领域知识教学指南]]。

---

> [!note] 生成信息
> 本清单由知识体系构建引擎 v{{ENGINE_VERSION}} 自动生成，数据源：`knowledge_graph.json`
