---
id: ecs-login-rdp-unavailable
intent: diagnose
environment: huawei-cloud-ecs-windows
status: draft
---

# RDP 远程桌面不可用

## Overview

- **Issue：**Windows ECS 的 RDP 超时、拒绝、认证或会话建立失败。
- **Environment：**Windows ECS；实际目标端口、访问路径、客户端报错和版本已知。
- **Resolution：**定位连接、认证或会话阶段的证据边界。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 按失败阶段选择证据

超时/拒绝先核对实例、网卡地址、云规则与实际路径，使用[云网络配置](../../commands/configuration/hcloud-network.md)。认证报错转身份策略调查；登录后黑屏或会话断开保留会话阶段，不当成端口不通。

[待补 ecs-login-rdp-unavailable/DOC-01：Windows 版本对应的 RDP/NLA/域身份与事件含义]

### 在 Windows 端核对

通过[独立通道](../../execution.md)，按[Windows 故障](../../commands/fault/windows.md)与[配置](../../commands/configuration/windows.md)取得服务、事件和连接事实。将监听、主机规则、远程登录资格与相同时段事件关联；Linux 命令和 SSH 子篇不直接套用。

[待补 ecs-login-rdp-unavailable/TOOL-01：RDP 有效监听、远程登录资格及事件查询契约]

### 交付阶段与缺口

明确已确认的连接/认证/会话阶段，以及仍需的事件证据。NLA、域身份、证书或会话限制只有证据匹配后才列为原因；不默认关闭安全机制或重启服务。

[待补 ecs-login-rdp-unavailable/CASE-01：超时、认证失败、会话失败分别对应的华为云工单]
