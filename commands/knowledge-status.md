---
name: knowledge-status
description: 查询知识引擎当前领域的缓存状态与 Pipeline 进度。
version: 2.9.0
parameters:
  - name: domain
    type: string
    required: false
    description: 要查询的领域名称（不指定则列出所有领域）
---

# /knowledge-status

查看知识引擎 Pipeline 的执行状态和缓存信息。

## 用法

```
/knowledge-status [领域名称]
```

## 示例

```
/knowledge-status                    # 列出所有已生成的领域知识库
/knowledge-status Python数据分析     # 查看指定领域的详细缓存状态
```

## 输出信息

### 全局概览（无参数）
- 已生成的知识库领域列表
- 每个领域的生成时间
- 每个领域的 Pipeline 完成状态

### 领域详情（指定领域）
- 各 Skill 的缓存状态（已缓存 / 未生成）
- 上游 JSON 文件的 SHA-256 hash 及变更状态
- 断点续跑建议（哪些步骤可跳过、需重跑）
- 知识点覆盖率、死链数量
- 预估 Token 消耗（重跑所需步骤）

## 状态标记说明

| 标记 | 含义 |
|:---|:---|
| ✅ 已完成 | 对应 JSON 存在，上游 hash 未变更，可直接复用 |
| 🔄 需重跑 | 上游 JSON 已变更，缓存失效 |
| ⬜ 未生成 | 对应 JSON 不存在，需首次生成 |
| ❌ 异常 | 缓存文件存在但 Schema 校验失败 |
