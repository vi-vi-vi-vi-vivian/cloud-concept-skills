---
id: ecs-network-dns-resolution-failed
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# DNS 解析失败或结果异常

## Overview

- **Issue：**名称解析超时、NXDOMAIN、SERVFAIL 或返回地址不符合预期。
- **Environment：**Linux ECS；名称、记录类型、实际解析器及公私网语境已知。
- **Resolution：**区分客户端解析链、解析器可达性和记录/转发范围。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 固定一次解析上下文

保留应用原始错误、完整名称、查询类型、实际解析器与响应码。只有部分名称失败时，与同语境成功名称对照；NXDOMAIN 与超时分开，返回空答案也不等于不存在。

[待补 ecs-network-dns-resolution-failed/DOC-01：华为云 DNS 区域关联、转发与缓存生效语义]

### 沿实际解析链检查

核对系统/应用缓存、搜索域和解析器配置的管理来源，再查私有区域关联、转发与记录范围。使用[DNS 查询契约](../../commands/fault/linux.md)时注意当前只定义 A 查询；AAAA、指定解析器或应用内解析需另补契约。通用查询成功不能证明应用解析链相同。

[待补 ecs-network-dns-resolution-failed/TOOL-01：实际解析器配置、指定类型/解析器查询契约]

### 交付故障范围

解析器请求超时需要路径证据，可转[出网检查](outbound-unreachable.sop.md)的路径段；记录回答异常需记录版本、TTL、关联范围及查询时间。避免直接替换 DNS 服务器或清缓存掩盖证据。

[待补 ecs-network-dns-resolution-failed/CASE-01：公有正常私有失败、NXDOMAIN 与超时对照]
