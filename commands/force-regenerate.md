---
name: force-regenerate
description: 忽略所有缓存，强制全量重新执行知识引擎 Pipeline。
version: 2.9.0
parameters:
  - name: domain
    type: string
    required: true
    description: 要强制重跑的领域名称
  - name: confirm
    type: boolean
    required: false
    default: false
    description: 确认执行（防止误操作）
---

# /force-regenerate

忽略 `.shared/` 下的所有 JSON 缓存和断点续跑状态，从 order: 1 需求分析师开始全量重新执行 Pipeline。

## 用法

```
/force-regenerate <领域名称> --confirm
```

## 示例

```
/force-regenerate Python数据分析 --confirm
/force-regenerate 提示词工程 --confirm
```

## 执行流程

1. 清除 `领域知识库/[领域名称]/.shared/` 下的所有 JSON 缓存
2. 重置断点续跑状态
3. 按 order: 1 → 6 全量重新执行 Pipeline
4. 覆盖现有的全部 Markdown 文档

## 注意事项

- **此操作不可逆**：旧的知识库文档将被覆盖
- 需要 `--confirm` 参数确认，防止误操作
- 在覆盖前会自动备份旧产出到 `.shared/backup/` 目录
- 若有未提交的进度追踪数据，请先手动备份

## 替代方案

若只需重跑部分步骤：
- 手动删除 `领域知识库/[领域名称]/.shared/` 中对应的 JSON 文件
- 然后执行 `/analyze-knowledge <领域>` — 将自动从缺失的步骤开始续跑
