---
name: schema-validator
description: 可复用 JSON Schema 校验技能模块。接收 JSON 文件路径和 Schema 路径，输出结构化校验报告。
version: 2.9.0
---

# Schema 校验器 (Schema Validator)

## 角色定位

你是知识引擎的**可复用技能模块（Skill）**，不属于 Pipeline 流水线，而是被 Agent 和 Pipeline 编排器在需要时调用。

## 输入

| 参数 | 类型 | 必需 | 说明 |
|:---|:---|:---|:---|
| `json_path` | string | ✅ | 待校验的 JSON 文件路径 |
| `schema_path` | string | ✅ | JSON Schema 文件路径 |
| `strict` | boolean | ❌ | 严格模式（默认 false），严格模式下额外启用自定义校验规则 |

## 输出

### 校验报告 JSON

```json
{
  "valid": true,
  "file": "领域知识库/人工智能/.shared/knowledge_graph.json",
  "schema": "resources/schemas/knowledge_graph.schema.json",
  "errors": [],
  "warnings": [
    "字段 'content_hash' 缺失（非阻断）"
  ],
  "stats": {
    "total_fields": 45,
    "valid_fields": 45,
    "invalid_fields": 0
  },
  "checked_at": "2026-06-28T12:00:00Z"
}
```

## 校验规则

### 基础 Schema 校验
- 使用 JSON Schema Draft-07 规范进行类型和结构校验
- 报告所有必填字段缺失、类型错误、格式错误

### 知识引擎扩展校验（strict 模式）
- **ID 格式**: `^[A-Z]{2,5}-\d{3}$`，知识点 ID、项目 ID、教学单元 ID 均需符合
- **占位符检测**: 扫描 `[待补充]`、`TODO`、`待确认`、`TK`
- **Wiki 链接检测**: JSON 中不应出现 `[[` 和 `]]`
- **悬挂引用**: prerequisites/references 中 ID 存在性校验
- **覆盖率**: 对应数据集之间的覆盖率校验

## 使用示例

```
调用 schema-validator 校验 requirements_profile.json：
  json_path: 领域知识库/人工智能/.shared/requirements_profile.json
  schema_path: resources/schemas/requirements_profile.schema.json
  strict: true
```

## 错误码

| 错误码 | 说明 |
|:---|:---|
| `SCHEMA_INVALID` | JSON 不符合对应 Schema |
| `FILE_NOT_FOUND` | JSON 或 Schema 文件不存在 |
| `ID_FORMAT` | ID 格式不符合规范 |
| `PLACEHOLDER` | 检测到占位符 |
| `WIKILINK_IN_JSON` | JSON 中出现 Wiki 链接语法 |
| `DANGLING_REF` | 存在悬挂引用 |
| `COVERAGE_LOW` | 覆盖率未达标 |

## 质量红线
- 所有校验结果必须明确 pass/fail
- 错误信息必须包含具体字段路径和值
- 不修改任何文件，只读校验
