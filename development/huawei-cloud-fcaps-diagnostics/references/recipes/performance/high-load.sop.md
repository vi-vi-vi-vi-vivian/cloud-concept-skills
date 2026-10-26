---
id: ecs-performance-high-load
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 系统负载升高

## Overview

- **Issue：**Linux load1/load5/load15 升高，CPU 使用率未必高。
- **Environment：**Linux ECS；可用 CPU 数、时间窗与业务影响已知。
- **Resolution：**区分可运行任务竞争与不可中断等待。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 对齐负载而非套 CPU 结论

按[运行队列与线程状态](../../commands/performance/linux.md)观察趋势，关联可用 CPU 数及实际受限范围。负载值是时间平均，线程快照是瞬时，两者不能要求逐项相等。

[待补 ecs-performance-high-load/DOC-01：CPU 配额/可用核数与 Linux 负载指标口径]

### 按任务状态定位

R 状态/队列持续增多时结合[CPU 诊断](high-cpu.sop.md)与短命任务线索；D 状态增多时查相同任务的等待点及设备/网络文件系统证据，必要时转[IO 延迟](high-io-latency.sop.md)。D 状态不唯一意味着本地磁盘慢。

[待补 ecs-performance-high-load/TOOL-01：任务等待栈及短命任务有界观测契约]

### 给出证据支持的范围

交付负载窗口、任务群、等待类型及业务关联；采样错过故障时保留历史缺口。未知等待栈或采样权限不足时不默认终止任务或升级规格。

[待补 ecs-performance-high-load/CASE-01：CPU 不高但负载高与短命任务工单]
