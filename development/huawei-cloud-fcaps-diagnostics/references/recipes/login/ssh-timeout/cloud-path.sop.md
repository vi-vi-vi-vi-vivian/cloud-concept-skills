---
id: ecs-login-ssh-timeout-cloud-path
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# SSH 超时：云侧路径检查

## Overview

- **Issue：**由 SSH 超时主篇调用，需要确认连接实际经过的云资源及有效规则。
- **Environment：**沿用父篇目标、时间窗、源地址、目标地址与端口。
- **Resolution：**返回匹配证据、可疑阻断点与仍未知的主机/数据面事实。

## Guidance

执行按[共同约束](../../../shared.md)，远程取证按[通道](../../../execution.md)；结果按[报告字段](../../../report.md)记录。

### 确认连的是哪台实例

按[云配置](../../../commands/configuration/hcloud.md#ecs)和[网络配置](../../../commands/configuration/hcloud-network.md)核对状态、网卡、私网地址及公网/NAT 绑定；通过[Helper](../../../helpers.md)关联标识。实例运行状态不证明 OS 或 SSH 就绪。状态异常转[启动诊断](../../instance-state/boot-failed.sop.md)。

[待补 ecs-login-ssh-timeout-cloud-path/DOC-01：华为云规则优先级、状态性、NAT 和回程语义]

### 沿实际方向解释配置

按实际路径查路由、关联的访问规则及回程条件。只有规则对象、优先级、地址转换和方向都明确时，才判断本连接是否匹配；单条允许规则或配置清单不足以证明有效放行。历史故障须区别当前配置与当时记录。

[待补 ecs-login-ssh-timeout-cloud-path/TOOL-01：内部路径查询的输入、有效规则输出和错误含义]

### 返回父篇

指出哪一跳的配置与期望冲突，或配置未发现解释但仍缺数据面证据。缺权限、无记录与不存在分别报告；不以查询失败当阻断。将结果返回[SSH 超时](../ssh-timeout.sop.md)。

[待补 ecs-login-ssh-timeout-cloud-path/CASE-01：实际命中规则与原路径复测证据]
