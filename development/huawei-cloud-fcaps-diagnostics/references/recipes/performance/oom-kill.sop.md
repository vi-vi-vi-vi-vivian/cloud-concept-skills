---
id: ecs-performance-oom-kill
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 确认与分析 OOM 终止事件

## Overview

- **Issue：**日志含 oom-killer/Killed process 或工作负载报告 OOMKilled。
- **Environment：**Linux ECS；事件时间、进程/容器身份及所属启动已知。
- **Resolution：**确认事件范围、受害进程与压力来源的区别。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 先确认终止机制

按[内核日志](../../commands/fault/linux.md)获取事件上下文，核对目标、启动与时间。退出码 137 或进程消失本身不能证明 OOM；当前日志未见记录也不能排除历史 OOM。

[待补 ecs-performance-oom-kill/DOC-01：内核/cgroup/容器 OOM 事件语义与版本差异]

### 还原事件时的限制

区分全局 OOM 与 cgroup 范围，提取内存限制、受害者和当时占用；被杀进程未必是压力来源。需要当前压力调查时引用[内存压力](memory-pressure.sop.md)，不以事件后的余量反推事件前正常。

[待补 ecs-performance-oom-kill/TOOL-01：历史启动日志、cgroup 事件与限制读取契约]

### 交付事件与候选原因

记录哪次事件、谁被终止、限制在哪层、是否重复及业务影响。缺限制或历史占用时只确认事件，不断言泄漏；修复建议需对应限制或增长证据。

[待补 ecs-performance-oom-kill/CASE-01：受害进程不是最大消耗者及限额 OOM 工单]
