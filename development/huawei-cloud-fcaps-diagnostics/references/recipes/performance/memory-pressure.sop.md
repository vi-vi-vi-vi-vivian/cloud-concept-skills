---
id: ecs-performance-memory-pressure
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 内存压力或分配失败

## Overview

- **Issue：**可用内存下降、换页增加或分配失败；未确认 OOM 事件。
- **Environment：**Linux ECS；主机与进程/容器内存限制分别明确。
- **Resolution：**区分可回收缓存、持续压力及局部内存限制。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 核对统计口径

按[内存与 vm 采样](../../commands/performance/linux.md)对照 available、缓存、swap 活动和业务延迟；free 少或 used 高不单独证明压力。云内存指标缺失时确认是否具备采集来源，不解释为零。

[待补 ecs-performance-memory-pressure/DOC-01：内存监控采集条件及主机/容器限制口径]

### 关联占用与限制

对齐进程/工作负载增长、回收/换页趋势与限制范围。主机有余量但应用失败时查进程/容器限制；一次高占用不能证明泄漏，需要随时间和负载的增长证据。

[待补 ecs-performance-memory-pressure/TOOL-01：cgroup/进程限制与内存组成只读查询契约]

### 区分事件与当前状态

发现 OOM 证据时转[OOM 事件](oom-kill.sop.md)。其余交付压力范围、主要占用及未知限制；不把加 swap、重启或清缓存当诊断默认动作。

[待补 ecs-performance-memory-pressure/CASE-01：缓存高、泄漏、局部限制与真实压力对照]
