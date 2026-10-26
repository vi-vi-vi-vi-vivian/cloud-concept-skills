---
id: ecs-performance-high-io-latency
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 磁盘 IO 延迟升高

## Overview

- **Issue：**业务读写变慢、await/队列升高或 IO 等待增加。
- **Environment：**Linux ECS；主机设备与云盘映射及故障时间窗已知。
- **Resolution：**区分负载变化、盘/实例限额及主机等待线索。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 关联同一设备和时间

用[Helper](../../helpers.md)关联设备与云盘，再对齐[主机 IO 采样](../../commands/performance/linux.md)和[云性能](../../commands/performance/hcloud.md)。比较操作数、吞吐、请求大小、延迟和队列，避免单位/聚合周期混用。

[待补 ecs-performance-high-io-latency/DOC-01：华为云盘/实例性能上限、聚合单位和突发机制]

### 区分需求与可用能力

结合进程 IO、读写模式、同期其他盘和实例/云盘能力。单一 util、iowait 或高延迟不能证明饱和；云限额、突发额度只能在华为云对应产品证据支持时使用，不能移植 AWS 数值。

[待补 ecs-performance-high-io-latency/TOOL-01：内部设备指标与进程/后端关联查询契约]

### 把剩余疑问落到观察点

如容量/文件系统错误明显，转[存储](../storage.md)；任务阻塞与本地设备不对应时查实际后端及等待点。交付最可能的瓶颈层与证据缺口；不默认压测、改调度器或关闭写入保护。

[待补 ecs-performance-high-io-latency/CASE-01：盘限额、实例共享上限与应用同步写对照工单]
