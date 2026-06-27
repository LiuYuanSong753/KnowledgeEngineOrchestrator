# 更新日志 (Changelog)

本文档记录 Knowledge Engine Orchestrator 插件的所有版本变更历史。

---

## v2.8.0 (2026-06-27)

### 三核心 Skill 全面优化

#### 知识分析师（order:2）优化
- **ID 格式规范化**：知识点 ID 严格为 `{学科缩写}-{三位序号}`（如 `PYB-001`），JSON 中移除所有 `[[ ]]` Wiki 语法，缩写由学科独立生成（内置映射表 + 拼音首字母兜底）
- **知识点结构扩展**：新增风格相关可选字段 — `exam_weight`（面试星级 1-5）、`common_questions`（常见面试问题）、`application_scenarios`、`academic_refs`、`analogy`、`practice_code`（G3/G4 必填）
- **类型枚举升级**：`type` 从"独立知识点/联动知识点"升级为 5 类新枚举 — 核心概念 / 方法算法 / 工具实践 / 对比辨析 / 应用案例
- **subjects_covered 结构化**：从字符串数组改为对象数组 `{"subject": "学科名", "abbreviation": "PYB"}`
- **跨学科依赖支持**：新增 `cross_subject_dependencies` 数组记录跨学科前置关系
- **输入校验门**：阶段 0 增加 6 项严格校验（`SUBJECTS_EMPTY` / `MAX_POINTS_INVALID` / `GRANULARITY_INVALID` / `DEPTH_INVALID` / `STYLE_INVALID` / `LANGUAGE_INVALID`），返回结构化错误码
- **可行性估算**：阶段 1 增加点数上限与学科覆盖冲突的自动降级机制（深度降级 → 裁剪提示）
- **学科骨架支持**：支持从 `subjects_syllabus.json` 加载核心知识点骨架，确保多次运行产物稳定
- **断点续跑精确化**：基于 `content_hash`（SHA-256）判定上游是否变更

#### 项目专家（order:3）优化
- **需求分析驱动**：新增 `requirements_profile.json` 为可选输入（强烈建议），根据学习者画像与生成规格调整项目设计
- **情境驱动原则**：5 种风格深度映射 — 面试突击型（面试场景+模拟讲述）、学术研究型（论文复现+实验对比）、项目驱动型（生产环境+性能指标）、认证考试型（时间限制+标准对照）、科普故事型（通用教学场景）
- **JSON 结构扩展**：新增字段 — `direction`、`requirements_profile_version`、`estimated_hours`（2~8h）、`project_dependencies`、`learning_path_narrative`
- **多知识点关联**：`practice_steps[].related_knowledge_ids`（数组）、`deviations[].related_knowledge_ids`（数组，支持交叉偏差）、`acceptance_criteria[].knowledge_ids`（数组，支持组合验收）
- **映射增强**：`mappings` 新增 `merged_coverage` 字段标记合并覆盖
- **目标匹配度自检**：存在需求分析时校验项目背景是否呼应 `inferred_goal`，通报附匹配声明
- **负荷控制**：项目总时长 ≤40h 可配置

#### 知识教学专家（order:4）优化
- **可执行打包算法**：前置依赖聚类 + 项目步骤耦合聚类 + 跨学科联动判断 + 粒度边界（2~4 知识点/单元）+ 饱和检查
- **归属唯一性约束**：知识点默认只能归属一个单元的 `knowledge_ids`，新增 `review_knowledge_ids` 支持螺旋复习
- **联动单元规范**：跨 ≥2 学科且同 deviation/acceptance 共引时必生成为联动单元，`combination_logic` 必填
- **排序语义标准化**：`unit_ordering_strategy` 声明为 `topological_by_difficulty`（依赖→难度→项目连贯性）
- **数据结构精简**：移除 `linked_project_ids`（与 `hooks` 冗余），`hooks` 成为唯一项目关联来源
- **内容质量自动化**：标题纯文本检查、占位符检测、联动单元完整性校验、启发式问题答案泄露检测（不阻塞）
- **风格深度适配矩阵**：5 风格 × 4 维度（大白话/精讲/问题/钩子）定向调节
- **孤儿知识点处理**：未关联项目的知识点生成 `project_id: "NONE"` 特殊钩子
- **元数据扩充**：新增 `estimated_minutes`、`tags`、`review_knowledge_ids`、`upstream_graph_hash`、`upstream_project_hash`
- **断点续跑精确化**：基于 SHA-256 哈希比对上游文件内容

### Schema 与模板同步更新
- **重写**：`schemas/knowledge_graph.schema.json` — v2.8 结构（direction、subjects_covered 对象数组、新 type 枚举、风格字段、cross_subject_dependencies）
- **重写**：`schemas/project_manifest.schema.json` — v2.8 结构（direction、estimated_hours、数组化 related_knowledge_ids/knowledge_ids、project_dependencies、merged_coverage、learning_path_narrative）
- **重写**：`schemas/teaching_outline.schema.json` — v2.8 结构（移除 linked_project_ids、新增 estimated_minutes/tags/review_knowledge_ids/unit_ordering_strategy/hashes、hooks 增强）
- **重写**：`templates/knowledge-checklist.template.md` — 新增 direction、style、学科覆盖表、跨学科依赖、面试高频考点区块
- **重写**：`templates/project-collection.template.md` — 新增 direction、预估学时、前置项目、目标匹配声明、步骤关联知识点
- **重写**：`templates/teaching-guide.template.md` — 新增方向、排序策略、预估学时、联动单元数、复习提示、孤儿项目处理

### 文档全量更新
- **更新**：`README.md` — v2.8 架构说明、6 Skill 表格、Mermaid 流程图、新参数表、产出物详解
- **更新**：`README-en.md` — 英文同步更新
- **更新**：`marketplace.json` — v2.8.0
- **更新**：`CHANGELOG.md` — 本条目

### 版本号
- 2.7.0 → 2.8.0

---

## v2.7.0 (2026-06-27)

### 职责分离：需求分析师 + 知识分析师 拆分
- **新增**：`skill/requirements-analyst/Skill.md` — 独立需求分析师 Skill（order:1，插件入口），实现完整三阶段交互（三拆→学习者画像→生成规格配置）
- **恢复**：`skill/knowledge-analyst/Skill.md` — 回归纯知识拆解角色（order:2），接收 requirements_profile.json
- **数据契约**：新增 `schemas/requirements_profile.schema.json` 定义上下游数据格式
- **Pipeline 重构**：新增 step-requirements（order:1），全部步骤 order 后移一位，总计 6 核心步骤，通报格式 [N/6]
- **全 Skill order 引用更新**：project-expert(2→3)、knowledge-educator(3→4)、verifier(4→5)、obsidian-doc-writer(5→6)

### 版本号
- 2.6.0 → 2.7.0

---

## v2.6.0 (2026-06-27)

### 架构革命：中央编排器 → 分布式自编排
- **入口迁移**：插件入口从根 `Skill.md`（中央编排器）变更为 `skill/knowledge-analyst`（需求分析师）
- **Skill.md 弱化**：原 242 行编排器降级为 46 行兼容性重定向入口
- **运行契约迁移**：原编排器的 8 条核心运行契约全部分解迁移至各对应 Skill 的"架构合约"章节
- **职责分离迁移**：层1/层2 职责定义迁移至各 Skill 角色定位中
- **扩展规范迁移**：模板/Schema 对照表迁移至 obsidian-doc-writer，中间件清单分布至各 Skill

### 新功能：三拆需求分析
- **基于设计文档**：`docs/领域知识分析师-设计文档.md` 的"三拆双层"方法论落地
- **第一拆**：领域拆分 — 自动分析用户学习内容所属领域
- **第二拆**：方向拆分 — 交互式引导用户明确学习方向
- **第三拆**：学科拆分 — 确定学科范围并征询扩展
- **知识分析师**（原）→ **需求分析师**（新）：继承知识拆解能力，新增需求澄清前置环节

### 独立状态通报机制
- 各 Skill 不再依赖中央编排器汇报，改为独立输出 `[N/5]` 格式的状态报告
- 每条状态报告包含：完成摘要 + 下一步提示 + 依赖文件路径
- 执行计划不再由编排器统一下发，改为各 Skill 按 order 独立感知

### Pipeline 新增 order 参数
- `schemas/pipeline.config.yml` 新增 `order` 字段（1-based），明确定义执行顺序
- `depends_on` 保留用于数据依赖声明，`order` 用于执行序列
- 支持通过 order 灵活调整 Skill 执行优先级

### 全量文件变更
- **重写**：`skill/knowledge-analyst/Skill.md` — 需求分析师（三拆 + 知识拆解 + 架构合约）
- **重写**：`skill/project-expert/Skill.md` — order: 2 + 独立通报 + 合约迁移
- **重写**：`skill/knowledge-educator/Skill.md` — order: 3 + 独立通报 + 合约迁移
- **重写**：`skill/verifier/Skill.md` — order: 4 + 独立通报 + 合约迁移
- **重写**：`skill/obsidian-doc-writer/Skill.md` — order: 5 + 模板/Schema 对照迁移 + 扩展规范
- **重写**：`schemas/pipeline.config.yml` — 新增 order 字段
- **弱化**：`Skill.md` — 242 行 → 46 行兼容性重定向
- **更新**：`marketplace.json`、`CHANGELOG.md`

### 版本号
- 2.5.0 → 2.6.0

---

## v2.5.0 (2026-06-27)

### 插件入口标准化
- **重构入口**：`Skill.md` 从混合型大文件重构为干净插件入口，YAML frontmatter 精简至仅含 `name`/`description`/`version`
- **Pipeline 规则抽离**：将 `config` 与 `pipeline` 定义从 `Skill.md` YAML frontmatter 中抽离至 `schemas/pipeline.config.yml`
- **启动流程**：编排器启动时解析 `schemas/pipeline.config.yml` 获取流水线定义，与编排器角色逻辑解耦

### 目录架构平级化
- **`schemas/`**、**`skill/`**、**`templates/`** 调整为项目根目录下的平级目录
- 全局路径引用更新：`skill/schemas/` → `schemas/`、`skill/templates/` → `templates/`
- 影响文件：Skill.md、knowledge-analyst/Skill.md、project-expert/Skill.md、knowledge-educator/Skill.md、obsidian-doc-writer/Skill.md、CHANGELOG.md

### 编排器文档精简
- Skill.md 从 420 行精简至 ~240 行，去除冗余内嵌 Pipeline YAML
- 执行流程精简为要点式指令，5个阶段统一为紧凑格式

### 版本号
- 2.4.0 → 2.5.0

---

## v2.4.0 (2026-06-27)

### 插件架构重构：两层分层设计
- **核心变革**：将原有单一Pipeline重构为「层1：数据生产」+「层2：文档渲染」两层架构
- **层1 — 业务Skill**：知识分析师、项目专家、教学专家、闭环校验器**仅产出结构化JSON数据**，不再负责任何Markdown文档生成
- **层2 — Obsidian文档编写助手**：新增统一文档生成模块，读取全部JSON + 标准化模板 → 渲染全部Markdown文档
- **职责分离原则**：业务逻辑与文档呈现完全解耦，层1专注数据质量，层2专注格式合规与内容丰富化

### 新Skill：Obsidian文档编写助手
- **新建**：`skill/obsidian-doc-writer/Skill.md` — 原 `obsidian-syntax-validator` 升级为统一文档生成模块
- **功能**：模板驱动文档生成 + Obsidian语法校验与自动修正（规则组A-H）+ 内容丰富化
- **输入**：全部4个JSON中间件 + 5个标准化模板
- **输出**：全部5个用户交付文档（0-体系总索引/1-领域知识点清单/2-项目集/3-领域知识教学指南/4-进度追踪看板）+ 语法校验报告

### 标准化模板系统
- **新建**：`skill/templates/` 目录，包含5个标准化文档模板
- `knowledge-checklist.template.md` — 知识点清单模板
- `project-collection.template.md` — 项目集模板
- `teaching-guide.template.md` — 教学指南模板
- `master-index.template.md` — 体系总索引模板
- `progress-tracker.template.md` — 进度追踪看板模板
- **占位符语法**：`{{VARIABLE}}` + `{{#EACH}}...{{/EACH}}` 迭代 + `{{#IF}}...{{/IF}}` 条件渲染

### 新增JSON Schema
- **新建**：`skill/schemas/verification_result.schema.json` — 闭环校验器输出数据结构定义

### 业务Skill重构（仅产出JSON）
- **重构**：`skill/knowledge-analyst/Skill.md` — 移除Markdown产出逻辑，仅输出 `knowledge_graph.json`
- **重构**：`skill/project-expert/Skill.md` — 移除Markdown产出逻辑，仅输出 `project_manifest.json`
- **重构**：`skill/knowledge-educator/Skill.md` — 移除Markdown产出逻辑，仅输出 `teaching_outline.json`
- **重构**：`skill/verifier/Skill.md` — 移除Markdown产出逻辑，仅输出 `verification_result.json`（含校验结果、Mermaid图谱、映射表、引用索引、学习路径、进度跟踪数据）

### 根入口优化
- **重构**：`Skill.md` — 插件化设计优化，明确两层架构、Pipeline路径更新为 `skill/` 目录、职责分离规范、模板/Schema对照表

### 清理
- **移除**：`skill/obsidian-syntax-validator/` 目录（功能已整合至 obsidian-doc-writer）
- **更新**：`marketplace.json`、`CHANGELOG.md` 版本号同步至 2.4.0

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
