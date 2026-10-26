---
id: ecs-login-ssh-timeout
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# SSH 建立连接超时

## Overview

- **Issue：**SSH 建连超时或目标端口无响应；拒绝连接、认证失败、握手阶段超时先转[登录分诊](../login.md)。
- **Environment：**Linux ECS；已知实际连接源、目标、端口与路径。
- **Resolution：**定位阻断边界，交付证据与下一项可区分假设的检查。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 先固定一次失败连接

复用原始报错、时间窗及客户端实际配置，区分直连、代理、VPN、堡垒机。NAT 前后的源地址分别标注。确认超时发生在 TCP 建立之前；仅凭超时不能判断报文未到主机。

[待补 ecs-login-ssh-timeout/DOC-01：连接阶段及代理/NAT 场景边界]

### 按已有证据选择调查

需要核对资源绑定、访问规则和回程时读[云侧路径](ssh-timeout/cloud-path.sop.md)，传入连接元组与已知云资源。已有独立主机通道，或云查询仍不能解释失败时读[主机端点](ssh-timeout/host-endpoint.sop.md)，传入同一时间窗与已查结果。两条调查可独立推进；云配置表面正常不证明网络通畅。

[待补 ecs-login-ssh-timeout/TOOL-01：客户端失败阶段证据的采集方式]

### 合并结果

把实际源、目的、规则匹配、主机观测放回同一连接。目标不明或缺关键通道时交付缺口；证据足够时说明阻断点和反证。恢复建议单列，成功须由原连接路径复测。

[待补 ecs-login-ssh-timeout/CASE-01：同一症状的云侧与主机侧反例工单]
