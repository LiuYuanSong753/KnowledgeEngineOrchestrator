---
name: knowledge-engine-orchestrator
description: >-
  知识体系构建引擎-分布式编排器 v2.9。
  入口为需求分析师(agents/requirements-analyst.md)，
  通过三阶段交互(三拆→学习者画像→生成规格)精准锁定需求。
  6 Agent 按 pipeline.config.yml 中 order 顺序独立执行并通报状态，
  最终产出 Obsidian 双链知识库(5个 Markdown 文档)。
version: 2.9.0
entry_skill: agents/requirements-analyst.md
---

# 🧠 知识引擎编排器 (Knowledge Engine Orchestrator) v2.9

## 插件概览

本插件是一个**知识体系构建引擎**，内置六类 AI Agent，按 Pipeline 顺序自动串联：

| order | Agent | 职责 | 产出 |
|:---:|:---|:---|:---|
| 1 | **需求分析师** | 三阶段交互锁定学习范围与规格 | `requirements_profile.json` |
| 2 | **知识分析师** | 体系化知识拆解 | `knowledge_graph.json` |
| 3 | **项目专家** | 情境驱动项目设计 | `project_manifest.json` |
| 4 | **知识教学专家** | 教学单元打包 | `teaching_outline.json` |
| 5 | **闭环校验器** | 覆盖率/双链/依赖闭环校验 | `verification_result.json` |
| 6 | **Obsidian文档编写助手** | 模板渲染全部 Markdown + 语法校验 | `0~4 全部 .md 文档` |

## 触发方式

### 方式一：自然语言触发

> "请使用需求分析师分析『提示词工程』"

### 方式二：斜杠命令

- `/analyze-knowledge <领域>` — 一键触发完整 Pipeline
- `/knowledge-status` — 查看当前领域缓存状态
- `/force-regenerate` — 强制全量重跑

### 带参数运行

> "分析『Python数据分析』，拆分粒度=G3，深度=D2，风格=面试突击型，知识点上限=20。"

| 参数 | 可选值 | 默认值 |
|:---|:---|:---|
| `granularity` | G1 / G2 / G3 / G4 | G3 |
| `depth` | D1 / D2 / D3 | D2 |
| `max_points` | 5~200 | 20 |
| `style` | 标准系统型 / 面试突击型 / 项目驱动型 / 学术严谨型 / 科普故事型 | 标准系统型 |

## 目录架构

```text
./
├── .claude-plugin/
│   ├── plugin.json              ← 插件清单（运行时）
│   └── marketplace.json         ← 市场描述
├── agents/                      ← 6 个独立 Agent 定义
│   ├── requirements-analyst.md
│   ├── knowledge-analyst.md
│   ├── project-expert.md
│   ├── knowledge-educator.md
│   ├── verifier.md
│   └── obsidian-doc-writer.md
├── skills/                      ← 可复用技能模块
│   └── schema-validator.md
├── resources/                   ← 共享资源
│   ├── schemas/                 ← Pipeline 配置 + JSON Schema
│   └── templates/               ← 5 个标准化文档模板
├── commands/                    ← 斜杠命令定义
│   ├── analyze-knowledge.md
│   ├── knowledge-status.md
│   └── force-regenerate.md
├── hooks/
│   └── hooks.json               ← 事件触发配置
├── .mcp.json                    ← MCP 服务定义
├── Skill.md                     ← 插件入口（本文件）
├── README.md
├── README-en.md
└── CHANGELOG.md
```

## Pipeline 架构

### 层1（order:1-5）：业务 Agent — 仅产出 JSON
各 Agent 按 resources/schemas/pipeline.config.yml 中定义的 order 顺序独立执行，通过 `.shared/` 目录下的 JSON 中间件传递数据。

### 层2（order:6）：Obsidian文档编写助手 — 统一文档渲染
读取全部 JSON + resources/templates/*.template.md 模板，渲染为最终 Markdown 知识库文档。

## 断点续跑

- 自动检测 `.shared/` 缓存，基于 SHA-256 hash 判定上游是否变更
- 已缓存且未变更的步骤自动跳过
- 支持强制全量重跑和局部更新

## 使用说明

1. 确保插件已安装到 Claude Code 插件目录
2. 推荐搭配 **Obsidian** 以获得最佳双链跳转体验
3. 初次使用时，需求分析师将通过三阶段交互引导您设定学习范围
4. 产出物位于 `领域知识库/[领域名称]/` 目录下

## 注意事项

- 所有产出物均由 LLM 自动生成，请根据专业背景审核
- 知识点 ID（如 `PYB-001`）一旦生成终身不得修改
- `.shared/` 目录下 JSON 由系统自动维护，请勿手动修改

---

> 完整文档请参阅 [README.md](./README.md) | 版本历史请参阅 [CHANGELOG.md](./CHANGELOG.md)
