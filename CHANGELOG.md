# 更新日志 (Changelog)

本文档记录 Knowledge Engine Orchestrator 插件的所有版本变更历史。

---

## v2.1.0 (2026-06-26)

### 双向链接格式修复
- **修复**：`verifier.md` — 表格内链接从 `[[file#anchor|display]]` 改为 `[[file#anchor]]`，解决 pipe `|` 与 Markdown 表格列分隔符冲突导致 `]]` 缺失的问题
- **修复**：`verifier.md` — 新增"表格内链接格式规则"和"学习路径链接格式规则"两节
- **修复**：`verifier.md` — 新增"标题与锚点跨文件一致性规约"表，确保锚点与目标标题完全匹配
- **修复**：`knowledge-educator.md` — 新增标题格式规约，禁止 `###` 标题内嵌 `[[ ]]` wikilink
- **修复**：`project-expert.md` — 新增标题格式规约和映射表内链接格式规则
- **修复**：`knowledge-analyst.md` — 质量红线增加标题纯文本禁令

### 内容质量增强
- **增强**：`project-expert.md` — 项目背景与解决问题板块增加篇幅下限（≥3句）、场景真实感要求、禁止空泛表述

### 全局规范
- **新增**：`Skill.md` — 第7条"标题纯文本规约"（所有 `##`/`###` 标题禁止内嵌 wikilink）
- **新增**：`Skill.md` — 第8条"表格内链接格式规约"（表格内禁用 `[[...|...]]`，非表格可用）

---

## v2.0.0 (2026-06-26)

### 新增功能
- **新增**：闭环校验器 Agent (`_agents/verifier.md`)，替代未实现的 `system-calculation`，支持覆盖率检查、双链有效性校验、依赖闭环检测与 Mermaid 知识图谱生成
- **新增**：`teaching_outline.json` 中间件，由 `step-teach` 产出，供扩展 Skill 消费
- **新增**：`config` 参数化配置，支持 `granularity`（拆分粒度）、`depth_mode`（生成深度）、`max_knowledge_points`（知识点上限）、`style_profile`（风格预设）等7个配置项
- **新增**：断点续跑机制（`checkpoint` 标记 + 缓存一致性校验 + 时间戳比对）
- **新增**：前置校验门（每个步骤完成后自动校验输出完整性、格式有效性、覆盖率）
- **新增**：执行进度反馈（ASCII 艺术进度报告 + 每步完成摘要）
- **新增**：`schemas/` 目录，包含 `knowledge_graph.schema.json`、`project_manifest.schema.json`、`teaching_outline.schema.json` 三套 JSON Schema
- **新增**：`6-进度追踪看板.md` 产出物（可选，由 `config.enable_tracker` 控制）
- **新增**：`step-assessment` Pipeline 步骤框架（默认关闭，需扩展 `_agents/assessment-generator.md`）

### 修复
- **修复**：Agent 输入声明格式断层 — 三个 Agent 均明确声明 JSON 输入格式 + 数据契约说明
- **修复**：Pipeline 配置中 `input_source` 与实际 Agent 声明不匹配的问题
- **修复**：`step-verify` 的 `agent: system-calculation` 无实现体问题

### 文档
- 新增故障排查指南（6类常见问题）
- 新增 Token 消耗估算表（5档规模）
- 更新 README.md 和 README-en.md

### 架构改进
- 编排器职责拆分（配置参数独立 `config` 段）
- 扩展指南更新（新增可用中间件清单）
- `.gitignore` 文件（忽略自动生成文件）

---

## v1.0.0 (2026-06-25)

### 初始发布
- **知识分析师** (`knowledge-analyst.md`)：领域知识拆解，生成知识点清单与依赖图谱
- **项目专家** (`project-expert.md`)：5+2 框架项目设计，100% 知识点映射
- **知识教学专家** (`knowledge-educator.md`)：教学单元打包，精确锚定项目步骤
- **Pipeline 编排器** (`Skill.md`)：顺序调度 + 热插拔扩展机制
- **缓存中间层**：`.shared/knowledge_graph.json` + `.shared/project_manifest.json`
- **Obsidian 双链**：所有产出物支持 WikiLink 双向链接跳转
- **输出产物**：`1-领域知识点清单.md`、`2-项目集.md`、`3-知识点项目映射表.md`、`4-领域知识教学指南.md`、`0-体系总索引.md`
