---
id: ecs-login-ssh-timeout-host-endpoint
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# SSH 超时：主机端点检查

## Overview

- **Issue：**由 SSH 超时主篇调用，需判断主机接收、监听或返回路径。
- **Environment：**Linux ECS；独立通道已就绪并已确认目标身份。
- **Resolution：**返回端点观测及其覆盖边界。

## Guidance

执行按[共同约束](../../../shared.md)，远程取证按[通道](../../../execution.md)；结果按[报告字段](../../../report.md)记录。

### 确认观察通道

按[执行通道](../../../execution.md)确认当前主机和权限。通道不可用时返回缺口，不能据此断言 OS 已宕机；不默认安装代理或重启。

[待补 ecs-login-ssh-timeout-host-endpoint/DOC-01：主机通道适用范围、SSH 服务与防火墙语义]

### 对照目标端口与服务

按[连接配置](../../../commands/configuration/linux.md)及[服务状态/日志](../../../commands/fault/linux.md)核对实际端口、绑定地址、服务状态和故障时间窗。服务进程存在不等于监听正确，日志缺失不等于没有请求。服务名以目标系统为准。

[待补 ecs-login-ssh-timeout-host-endpoint/TOOL-01：有效监听/防火墙查询及内部远程执行契约]

### 仅为剩余疑问补证据

核对主机地址、路由与策略规则；防火墙有效判定需专门契约。确需证明报文到达及返回时，按[有界抓包](../../../commands/performance/linux.md)限定接口、连接和时长；未捕获也可能是观察点或过滤范围错误。返回[父篇](../ssh-timeout.sop.md)已确认事实、时间及缺口。

[待补 ecs-login-ssh-timeout-host-endpoint/CASE-01：端点无监听、主机过滤与回程异常的对照工单]
