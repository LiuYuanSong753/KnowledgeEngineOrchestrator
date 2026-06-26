# 更新日志 (Changelog)

本文档记录 Knowledge Engine Orchestrator 插件的所有版本变更历史。

---

## v2.3.0 (2026-06-26)

### 多领域独立存储机制
- **修复**：`.shared/` 目录从全局扁平结构迁移为 `领域知识库/[领域名称]/.shared/`，每个领域的中间件 JSON 文件独立存储，彻底解决多领域知识库连续产出时 `.shared/` 被覆盖导致旧知识库无法更新的问题

### 知识库文档结构优化与精简
- **文档合并**：`3-知识点项目映射表.md` 的全部内容合并至 `0-体系总索引.md` 中的"知识点项目映射表"章节，由闭环校验器基于 `project_manifest.json` 统一生成
- **文档移除**：`7-Obsidian语法校验报告.md` 改为内部工作文件（`.shared/syntax_check_report.md`），不再出现在用户交付物列表中
- **文档重编号**：`4-领域知识教学指南.md` → `3-领域知识教学指南.md`，`6-进度追踪看板.md` → `4-进度追踪看板.md`
- **优化后交付物列表**：0-体系总索引 / 1-领域知识点清单 / 2-项目集 / 3-领域知识教学指南 / 4-进度追踪看板

### 全路径引用更新
- **更新**：`Skill.md` — 所有 `.shared/` 路径迁移至 `领域知识库/[领域名称]/.shared/`，Pipeline 步骤、前置校验门、断点续跑、扩展规范、质量红线全部同步
- **更新**：`_agents/knowledge-analyst.md` — `.shared/` 路径迁移
- **更新**：`_agents/project-expert.md` — 移除单独映射表输出职责，`.shared/` 路径迁移
- **更新**：`_agents/knowledge-educator.md` — `.shared/` 路径迁移，文档引用重编号（4→3）
- **更新**：`_agents/verifier.md` — 新增"知识点项目映射表"章节，校验源从扫描映射表文件改为直接解析 `project_manifest.json`，文档引用重编号
- **更新**：`_agents/obsidian-syntax-validator.md` — 校验报告输出路径改为内部文件

### 版本号同步
- `marketplace.json`、`Skill.md`、`README.md`、`README-en.md` 版本号统一更新为 2.3.0

---

## v2.2.0 (2026-06-26)

### 全新 Skill：Obsidian 语法校验器
- **新增**：`_agents/obsidian-syntax-validator.md` — 整合 `obsidian操作文档/` 下全部 15 篇 Obsidian 官方规范的专用语法校验 Skill
- **包含**：8 大规则组（A-H），覆盖 Wiki 链接、标题格式、YAML Frontmatter、Callout 标注、标签、表格、文本格式化、嵌入/图表等全部语法
- **包含**：4 阶段校验工作流（逐文件扫描 → 自动修正 → 内容丰富化建议 → 输出校验报告）
- **包含**：三级问题分级（严重 🔴 / 警告 🟡 / 建议 🟢），严重和警告级别自动修正

### 插件编排器集成
- **新增**：`Skill.md` Pipeline 新增 `step-syntax-check` 步骤，在全部文档生成后自动执行 Obsidian 语法校验
- **新增**：第 9 条核心执行规则"Obsidian 语法强制合规"，所有产出物必须在最终交付前通过语法校验
- **新增**：`7-Obsidian语法校验报告.md` 产出物，包含逐文件校验结果和修正记录

### 内容丰富化（全 Agent 升级）
- **增强**：`knowledge-analyst.md` — 新增 YAML Frontmatter 生成要求（tags/领域标签）
- **增强**：`project-expert.md` — 新增 YAML Frontmatter + Callout 标注应用（warning/success/danger/info）+ 标签推荐
- **增强**：`knowledge-educator.md` — 新增 YAML Frontmatter + Callout 标注应用（tip/note/question/info）+ 标签建议
- **增强**：`verifier.md` — 新增 Obsidian 语法预校验自检清单 + 内容丰富化要求（Frontmatter/Callout/cssclasses）

### 规则库
- **新增**：规则 A1-A7 — Wiki 链接完整格式规范（含表格内 pipe 转义）
- **新增**：规则 B1-B3 — 标题格式规范（纯文本禁止、`#` 后空格）
- **新增**：规则 C1-C5 — YAML Frontmatter 属性规范
- **新增**：规则 D1-D3 — Callout 标注规范（13 种类型 + 折叠）
- **新增**：规则 E1-E4 — 标签规范（嵌套、合法字符）
- **新增**：规则 F1-F2 — 表格规范（pipe 转义）
- **新增**：规则 G1-G8 — 文本格式化规范（粗/斜/高亮/删除/代码/注释/转义）
- **新增**：规则 H1-H10 — 其他高级语法规范（嵌入/Mermaid/数学公式/任务列表等）

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
