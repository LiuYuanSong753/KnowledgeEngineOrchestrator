---
tags:
  - {{DOMAIN}}
  - 体系索引
  - 知识图谱
aliases:
  - 体系总索引
cssclasses:
  - wide-page
---

# 体系总索引：{{DOMAIN}}

> [!info] 文档说明
> 本文档由 **闭环校验器** 对全部产出物执行完整性校验后，经 **Obsidian文档编写助手** 统一生成。包含校验报告摘要、Mermaid 知识图谱、知识点项目映射表、全量引用索引与学习路径建议。

---

## 校验报告摘要

{{#IF VERIFICATION_PASSED}}
> [!success] 全部校验通过
| 校验项 | 状态 | 详情 |
|:---|:---:|:---|
| 知识点项目覆盖率 | ✅ 通过 | 覆盖率 {{COVERAGE_RATE}} |
| 双链有效性 | ✅ 通过 | 死链 0 条 |
| 依赖链闭环 | ✅ 通过 | 无循环依赖、悬挂引用或跨级跳跃 |
{{/IF}}

{{#IF VERIFICATION_FAILED}}
> [!danger] 校验发现问题
| 校验项 | 状态 | 详情 |
|:---|:---:|:---|
| 知识点项目覆盖率 | ❌ 失败 | 覆盖率 {{COVERAGE_RATE}}，缺失 {{MISSING_COUNT}} 个知识点 |
| 双链有效性 | ❌ 失败 | 死链 {{DEAD_LINK_COUNT}} 条 |
| 依赖链闭环 | ⚠️ 警告 | {{DEPENDENCY_ISSUES}} |

### 缺失知识点

| 知识点ID | 知识点名称 | 状态 |
|:---|:---|:---|
{{#EACH MISSING_KP}}
| {{ID}} | {{NAME}} | ❌ 未映射到任何项目 |
{{/EACH}}

### 死链详情

| 死链目标 | 所在文档 | 所在行 |
|:---|:---|:---:|
{{#EACH DEAD_LINKS}}
| {{TARGET}} | {{SOURCE_FILE}} | 行{{LINE}} |
{{/EACH}}
{{/IF}}

---

## Mermaid 知识图谱

```mermaid
flowchart TD
{{MERMAID_GRAPH}}
```

> [!tip] 图谱说明
> 节点颜色：🟢 入门级 / 🟠 进阶级 / 🔴 高级。箭头方向：A → B 表示 A 依赖 B。

## 知识点项目映射表

基于 `project_manifest.json` 的完整知识点-项目映射：

| 知识点ID | 知识点名称 | 所属项目 | 项目名称 | 项目应用环节 | 掌握要求 |
|:---|:---|:---|:---|:---|:---|
{{#EACH MAPPINGS}}
| {{KP_ID}} | {{KP_NAME}} | [[2-项目集#{{PROJ_ID}} {{PROJ_NAME}}]] | {{PROJ_NAME}} | {{APPLICATION_STEP}} | {{PROFICIENCY}} |
{{/EACH}}

> [!warning] 映射表链接格式
> 映射表中的链接使用 `[[file#anchor]]` 格式（不含 `|` 分隔符），因为 `|` 会与表格列分隔符冲突。

---

## 全量知识点引用索引

| 知识点ID | 知识点名称 | 难度 | 出现在清单 | 映射至项目 | 教学单元 |
|:---|:---|:---|:---:|:---|:---|
{{#EACH REF_INDEX}}
| {{KP_ID}} | {{KP_NAME}} | {{DIFFICULTY}} | ✅ | {{PROJECT_LINKS}} | {{TEACHING_LINKS}} |
{{/EACH}}

> [!warning] 索引表链接格式
> 索引表中的所有链接使用 `[[file#anchor]]` 格式（不含 `|` 分隔符）。锚点文字必须与目标文档中的 `##`/`###` 标题文字完全一致。

---

## 学习路径建议

> [!tip] 推荐学习路径

### 第一阶段：入门基础

{{#EACH PHASE_1_ITEMS}}
- {{INDEX}}. 学习 [[3-领域知识教学指南#{{EDU_ID}} {{EDU_NAME}}\|{{EDU_ID}}]] → 实践 [[2-项目集#{{PROJ_ID}} {{PROJ_NAME}}\|{{PROJ_ID}}]]
{{/EACH}}

### 第二阶段：进阶级

{{#EACH PHASE_2_ITEMS}}
- {{INDEX}}. 学习 [[3-领域知识教学指南#{{EDU_ID}} {{EDU_NAME}}\|{{EDU_ID}}]] → 实践 [[2-项目集#{{PROJ_ID}} {{PROJ_NAME}}\|{{PROJ_ID}}]]
{{/EACH}}

### 第三阶段：高级

{{#EACH PHASE_3_ITEMS}}
- {{INDEX}}. 学习 [[3-领域知识教学指南#{{EDU_ID}} {{EDU_NAME}}\|{{EDU_ID}}]] → 实践 [[2-项目集#{{PROJ_ID}} {{PROJ_NAME}}\|{{PROJ_ID}}]]
{{/EACH}}

---

## 跨文件一致性说明

| 链接目标文件 | 标题格式规范 | 锚点示例 |
|:---|:---|:---|
| [[1-领域知识点清单]] | `### PCE-001 知识点名称` | `#PCE-001 知识点名称` |
| [[2-项目集]] | `### Proj-001 项目名称` | `#Proj-001 项目名称` |
| [[3-领域知识教学指南]] | `### EDU-001 教学单元名称` | `#EDU-001 教学单元名称` |
| 本文档 | 内部锚点 | — |

> [!note] 生成信息
> 本索引由知识体系构建引擎 v{{ENGINE_VERSION}} 自动生成。
