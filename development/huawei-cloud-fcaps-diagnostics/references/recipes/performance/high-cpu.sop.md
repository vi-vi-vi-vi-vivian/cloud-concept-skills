---
id: ecs-performance-high-cpu
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# CPU 使用率异常升高

## Overview

- **Issue：**CPU 升高并需要解释影响；单纯 load 高转负载诊断。
- **Environment：**Linux ECS；实例规格、指标口径及故障时间窗已知。
- **Resolution：**区分用户态、内核、中断、等待与资源分配线索。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 确认异常窗口和影响

对齐云指标与[CPU/进程采样](../../commands/performance/linux.md)，核对聚合周期、单核/整机口径及业务延迟。业务峰值或共享规格不能直接结束调查；当前正常也不能否定历史异常。

[待补 ecs-performance-high-cpu/DOC-01：华为云 CPU 指标、规格限制与 steal 解释]

### 按 CPU 类别选证据

用户态高关联对应进程/线程与负载；系统态或中断高关联内核/接口活动；等待线索结合[IO 延迟](high-io-latency.sop.md)而非当作计算繁忙。steal/平台事件需产品语义支持，不能仅凭一个值判断平台故障。

[待补 ecs-performance-high-cpu/TOOL-01：中断/进程线程历史观测及必要热点分析契约]

### 在足够区分时停止

记录主要消耗对象及持续区间，区分正常需求增长与异常行为。进程总和对不上先查采样时差、统计范围与短命线程，不能直接判断挖矿。确需进一步跟踪时按契约限定对象、权限和时长；缺证据交付候选与下一观察。

[待补 ecs-performance-high-cpu/CASE-01：业务峰值、异常计算与采样口径反例]
