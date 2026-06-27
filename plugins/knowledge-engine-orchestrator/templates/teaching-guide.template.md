---
tags:
  - {{DOMAIN}}
  - 教学指南
  - 系统学习
aliases:
  - 领域教学指南
---

# 领域知识教学指南：{{DOMAIN}} — {{DIRECTION}}

> [!info] 文档说明
> 本文档由 **知识教学专家** 采用「单元打包教学」策略，经 **Obsidian文档编写助手** 统一生成。将关联知识点合并为教学单元，通过五维结构（价值锚点→专业精讲→大白话直通→启发式追问→实战钩子）输出系统化教学内容。

---

## 教学单元总览

- **风格模式**：{{STYLE_PROFILE}}
- **排序策略**：{{ORDERING_STRATEGY}}
- **教学单元总数**：{{TOTAL_UNITS}}
- **总预估学时**：{{TOTAL_MINUTES}} 分钟
- **联动单元**：{{COMBINED_UNITS_COUNT}} 个

| 单元ID | 单元名称 | 难度 | 预估时长 | 涵盖知识点数 | 关联项目 |
|:---|:---|:---:|:---:|:---:|:---|
{{#EACH UNITS}}
| [[#{{ID}} {{NAME}}\|{{ID}}]] | {{NAME}} | {{DIFFICULTY}} | {{ESTIMATED_MINUTES}}min | {{KP_COUNT}} | {{PROJECT_LINKS}} |
{{/EACH}}

---

## 入门级教学单元

{{#EACH BEGINNER_UNITS}}

---

### {{ID}} {{NAME}}

{{#TAGS}}
#教学单元 #{{DIFFICULTY_LEVEL}}
{{/TAGS}}

> [!tip] 为什么要学这个？
> **痛点**：{{PAIN_POINT}}
> **价值**：{{VALUE_PROPOSITION}}
> **预计学习时长**：{{ESTIMATED_MINUTES}} 分钟

#### 大白话直通车

{{PLAIN_LANGUAGE}}

#### 专业知识精讲

{{PROFESSIONAL_EXPLANATION}}

{{#IF COMBINATION_LOGIC}}
#### 联动组合逻辑

{{COMBINATION_LOGIC}}
{{/IF}}

> [!question] 思考一下
> 1. {{INQUIRY_1}}
> 2. {{INQUIRY_2}}

> [!note] 实战预埋
> {{#EACH HOOKS}}
> - 关联项目：{{#IF IS_NONE}}无项目覆盖 — 建议自主设计练习{{/IF}}{{#IF NOT_NONE}}[[2-项目集#{{PROJECT_ID}} {{PROJECT_NAME}}\|{{PROJECT_ID}}]]，应用环节：{{APPLICATION_STEP}}{{/IF}}
> - 预期挑战：{{CHALLENGE}}
> {{/EACH}}

**前置要求**：{{PREREQUISITES_TEXT}}

{{#IF REVIEW_KP}}
> [!tip] 复习提示
> 建议复习：{{REVIEW_KP}}
{{/IF}}

{{/EACH}}

---

## 进阶级教学单元

{{#EACH INTERMEDIATE_UNITS}}

---

### {{ID}} {{NAME}}

{{#TAGS}}
#教学单元 #{{DIFFICULTY_LEVEL}}
{{/TAGS}}

> [!tip] 为什么要学这个？
> **痛点**：{{PAIN_POINT}}
> **价值**：{{VALUE_PROPOSITION}}
> **预计学习时长**：{{ESTIMATED_MINUTES}} 分钟

#### 专业知识精讲

{{PROFESSIONAL_EXPLANATION}}

{{#IF COMBINATION_LOGIC}}
#### 联动组合逻辑

{{COMBINATION_LOGIC}}
{{/IF}}

#### 大白话直通车

{{PLAIN_LANGUAGE}}

> [!question] 思考一下
> 1. {{INQUIRY_1}}
> 2. {{INQUIRY_2}}

> [!note] 实战预埋
> {{#EACH HOOKS}}
> - 关联项目：{{#IF IS_NONE}}无项目覆盖 — 建议自主设计练习{{/IF}}{{#IF NOT_NONE}}[[2-项目集#{{PROJECT_ID}} {{PROJECT_NAME}}\|{{PROJECT_ID}}]]，应用环节：{{APPLICATION_STEP}}{{/IF}}
> - 预期挑战：{{CHALLENGE}}
> {{/EACH}}

**前置要求**：{{PREREQUISITES_TEXT}}

{{#IF REVIEW_KP}}
> [!tip] 复习提示
> 建议复习：{{REVIEW_KP}}
{{/IF}}

{{/EACH}}

---

## 高级教学单元

{{#EACH ADVANCED_UNITS}}

---

### {{ID}} {{NAME}}

{{#TAGS}}
#教学单元 #{{DIFFICULTY_LEVEL}}
{{/TAGS}}

> [!tip] 为什么要学这个？
> **痛点**：{{PAIN_POINT}}
> **价值**：{{VALUE_PROPOSITION}}
> **预计学习时长**：{{ESTIMATED_MINUTES}} 分钟

#### 专业知识精讲

{{PROFESSIONAL_EXPLANATION}}

{{#IF COMBINATION_LOGIC}}
#### 联动组合逻辑

{{COMBINATION_LOGIC}}
{{/IF}}

> [!question] 思考一下
> 1. {{INQUIRY_1}}
> 2. {{INQUIRY_2}}

> [!note] 实战预埋
> {{#EACH HOOKS}}
> - 关联项目：{{#IF IS_NONE}}无项目覆盖 — 建议自主设计练习{{/IF}}{{#IF NOT_NONE}}[[2-项目集#{{PROJECT_ID}} {{PROJECT_NAME}}\|{{PROJECT_ID}}]]，应用环节：{{APPLICATION_STEP}}{{/IF}}
> - 预期挑战：{{CHALLENGE}}
> {{/EACH}}

**前置要求**：{{PREREQUISITES_TEXT}}

{{#IF REVIEW_KP}}
> [!tip] 复习提示
> 建议复习：{{REVIEW_KP}}
{{/IF}}

{{/EACH}}

---

> [!note] 生成信息
> 本指南由知识体系构建引擎 v{{ENGINE_VERSION}} 自动生成，数据源：`teaching_outline.json` + `project_manifest.json`
