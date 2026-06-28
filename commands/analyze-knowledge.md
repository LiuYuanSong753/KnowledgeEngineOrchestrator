---
name: analyze-knowledge
description: 触发知识引擎完整 Pipeline。输入学习领域/方向，需求分析师三阶段交互锁定范围后，自动串联全部 6 个 Skill 产出 Obsidian 知识库。
version: 2.9.0
parameters:
  - name: domain
    type: string
    required: true
    description: 要分析的学习领域或方向名称（如 "Python数据分析"）
  - name: granularity
    type: string
    required: false
    default: G3
    enum: [G1, G2, G3, G4]
    description: 知识拆分粒度
  - name: depth
    type: string
    required: false
    default: D2
    enum: [D1, D2, D3]
    description: 生成深度
  - name: max_points
    type: integer
    required: false
    default: 20
    minimum: 5
    maximum: 200
    description: 知识点数量上限
  - name: style
    type: string
    required: false
    default: 标准系统型
    enum: [标准系统型, 面试突击型, 项目驱动型, 学术严谨型, 科普故事型]
    description: 内容风格预设
---

# /analyze-knowledge

触发知识体系构建引擎的完整 Pipeline。

## 用法

```
/analyze-knowledge <领域名称> [参数...]
```

## 示例

```
/analyze-knowledge Python数据分析
/analyze-knowledge "机器学习基础" --granularity=G4 --depth=D3 --style=面试突击型
/analyze-knowledge 提示词工程 --max_points=30 --style=项目驱动型
```

## 工作流

1. **需求分析师** (order:1) — 三阶段交互锁定学习范围与生成规格
2. **知识分析师** (order:2) — 体系化知识拆解 → `knowledge_graph.json`
3. **项目专家** (order:3) — 情境驱动项目设计 → `project_manifest.json`
4. **知识教学专家** (order:4) — 教学单元打包 → `teaching_outline.json`
5. **闭环校验器** (order:5) — 覆盖率/双链/依赖闭环校验 → `verification_result.json`
6. **Obsidian文档编写助手** (order:6) — 模板渲染全部 Markdown 文档

## 产出

全部产出位于 `领域知识库/[领域名称]/` 目录：
- `0-体系总索引.md`
- `1-领域知识点清单.md`
- `2-项目集.md`
- `3-领域知识教学指南.md`
- `4-进度追踪看板.md`

## 注意事项

- 支持断点续跑：已缓存的步骤自动跳过
- 使用 `/force-regenerate` 可强制全量重跑
- 使用 `/knowledge-status` 查看当前缓存状态
