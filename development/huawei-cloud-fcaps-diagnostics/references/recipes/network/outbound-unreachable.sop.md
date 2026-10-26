---
id: ecs-network-outbound-unreachable
intent: diagnose
environment: huawei-cloud-ecs
status: draft
---

# 实例出网或业务目标不可达

## Overview

- **Issue：**从 ECS 访问明确业务目标超时、拒绝或无路由；管理登录走 login。
- **Environment：**ECS；主机取证以 Linux 为主，源进程/网络环境与目的协议已知。
- **Resolution：**缩小名称、主机、云路径或目标服务边界。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 明确连接从哪里发起

记录源实例/进程、容器或代理、目标域名/IP、端口、协议和失败阶段。解析失败转[DNS](dns-resolution-failed.sop.md)；使用 IP 测试时保留应用 Host/TLS 差异，不能把不同请求直接比较。

[待补 ecs-network-outbound-unreachable/DOC-01：华为云出网/NAT/规则及回程条件]

### 对照双向路径

按[主机配置](../../commands/configuration/linux.md)核对地址、路由和策略规则；按[云网络](../../commands/configuration/hcloud-network.md)核对网卡、路由、NAT/公网出口和有效规则。仅有公网地址或默认路由不足以证明业务可达，目标拒绝也需确认响应来源。

[待补 ecs-network-outbound-unreachable/TOOL-01：内部路径、目标端口探测和代理上下文契约]

### 用剩余疑问决定探测

按[网络探测](../../commands/fault/linux.md)及[有限抓包](../../commands/performance/linux.md)选择可区分假设的观察点与协议；ICMP 无响应不直接代表 TCP 失败。没有目标侧证据时明确边界，交付连接元组、路径、观察结果和下一检查点。

[待补 ecs-network-outbound-unreachable/CASE-01：同网段局部失败与多实例失败的对照工单]
