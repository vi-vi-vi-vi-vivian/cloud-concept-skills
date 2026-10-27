---
id: ecs-login-ssh-auth-failed
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# SSH 认证失败

## Overview

- **Issue：**已到达 SSH 认证阶段，出现 Permission denied 等身份认证失败；主机密钥校验失败单独核对目标身份。
- **Environment：**Linux ECS；客户端用户名、认证方式与脱敏错误已知。
- **Resolution：**区分身份选择、服务端认证策略与账户状态问题。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 固定认证双方

核对实际目标、用户名和客户端选中的认证方式/公钥指纹；不采集私钥或密码。已进入认证阶段时不重复全套云网络调查。

[待补 ecs-login-ssh-auth-failed/DOC-01：镜像默认账户与 SSH/PAM 生效规则]

### 对照同一次认证日志

通过独立[执行通道](../../execution.md)按[服务日志](../../commands/fault/linux.md)查相同时段拒绝原因；区分未提供合适身份、身份被拒、账户/会话策略拒绝。核对有效配置及账户解析，配置文件片段未必是实际生效值。另一通道成功不能单独证明 PAM 故障。

[待补 ecs-login-ssh-auth-failed/TOOL-01：有效 SSH 配置、账户状态和密钥权限的只读契约]

### 输出最小修正条件

把客户端所用身份与服务端拒绝证据对应；无日志/无权限时保持候选原因。重置密码、替换密钥或改认证策略应形成具体恢复方案，不能用放宽认证来验证猜测。

[待补 ecs-login-ssh-auth-failed/CASE-01：认证拒绝原因与最小修正后复测]
