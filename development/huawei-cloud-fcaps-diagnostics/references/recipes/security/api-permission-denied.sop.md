---
id: ecs-security-api-permission-denied
intent: diagnose
environment: huawei-cloud-api
status: draft
---

# 云 API 权限被拒

## Overview

- **Issue：**云 API 返回鉴权/授权错误；SSH 认证失败使用登录入口。
- **Environment：**华为云 API 调用；身份来源、项目/区域、操作和资源范围已知。
- **Resolution：**定位身份/范围不匹配或待核实的授权条件。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 先固定失败请求

保留脱敏错误码、请求 ID、时间、服务/操作版本及执行身份来源，不记录凭据值。区分网络失败、凭据缺失/过期、签名错误和授权拒绝；HTTP 403 本身不足以判断缺哪条权限。

[待补 ecs-security-api-permission-denied/DOC-01：华为云错误码、IAM/委托及条件求值规则]

### 对照身份与作用范围

按[云安全查询](../../commands/security/hcloud.md#iam)可覆盖的契约核对身份、项目和已获策略证据。将操作、资源与条件逐项对照；AWS instance profile、SCP 或策略模拟器不能直接当成华为云同名能力。策略列表也不等于有效授权结论。

[待补 ecs-security-api-permission-denied/TOOL-01：内部实际身份、有效权限与审计拒绝原因查询契约]

### 交付最小授权差异

有明确拒绝证据则说明对应身份、作用范围和条件；无权读取策略时交付请求 ID 及缺口给有权限的维护方。提出精确权限需求，避免用管理员授权或停用安全控制试错。

[待补 ecs-security-api-permission-denied/CASE-01：身份正确但范围/条件不匹配的拒绝工单]
