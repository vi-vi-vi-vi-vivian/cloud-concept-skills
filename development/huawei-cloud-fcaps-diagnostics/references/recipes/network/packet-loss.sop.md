---
id: ecs-network-packet-loss
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 网络丢包或间歇重传

## Overview

- **Issue：**业务报文丢失、间歇超时或重传增加；仅中间跳不回应不能确认丢包。
- **Environment：**Linux ECS；实际流量方向、协议、时间窗和观察点已知。
- **Resolution：**确认损失范围，关联主机、路径或负载证据。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 先验证观测口径

区别应用超时、TCP 重传、接口 drop 与 ICMP 探测损失。按[探测契约](../../commands/fault/linux.md)解释有限采样；中间跳限速/不回应不等于转发丢包。暂不可重现仍保留历史证据，不能宣布恢复。

[待补 ecs-network-packet-loss/DOC-01：各规格网络限制、驱动计数与云路径观测含义]

### 比较同时间窗增量

按[性能契约](../../commands/performance/linux.md)对齐接口/驱动计数增量、吞吐与 CPU 采样。结合相关内核日志和有效路径规则；累计 drop 值、共享规格或高软中断均不能单独确定根因。

[待补 ecs-network-packet-loss/TOOL-01：有界双端采集与计数时间对齐契约]

### 缩小丢失位置

需要报文证据时限定连接、接口、时长和数量，比较发送与接收观察点；抓包本身丢包、NAT 及非对称路径影响解释。交付损失出现在哪个范围、何时发生、仍缺哪一侧证据。

[待补 ecs-network-packet-loss/CASE-01：业务损失与 ICMP 限速反例、实际定位记录]
