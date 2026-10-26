---
id: ecs-instance-state-unexpected-reboot
intent: diagnose
environment: huawei-cloud-ecs
status: draft
---

# 意外重启或系统崩溃

## Overview

- **Issue：**实例非预期重启，或日志出现 panic/Oops 等崩溃线索。
- **Environment：**ECS；Linux 内核分支适用 Linux，平台事件适用对应实例。
- **Resolution：**建立事件时间线，区分操作、平台与 OS 线索。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 确认发生过什么

对齐用户感知中断、启动时间/启动标识、云事件与操作记录。业务进程重启不等于整机重启。先查[云故障](../../commands/fault/hcloud.md#ecs)与已有审计证据，保留时区和延迟差异。

[待补 ecs-instance-state-unexpected-reboot/DOC-01：平台重启/维护事件与 OS 重启记录语义]

### 保留前一次启动证据

寻找中断前日志、控制台 panic/Oops、已有 dump 与同期资源趋势。[内核日志](../../commands/fault/linux.md)默认覆盖当前启动，不能拿本次空结果排除上次崩溃。资源高只构成关联，需崩溃/操作证据支持归因。

[待补 ecs-instance-state-unexpected-reboot/TOOL-01：历史启动日志、审计事件与已有 dump 的读取契约]

### 交付可追溯时间线

有明确平台操作记录则标注执行者/事件及时间；有崩溃栈则记录版本、模块和首个错误，交给对应维护方。缺历史日志时说明无法判定，不主动诱发崩溃或重启重现。

[待补 ecs-instance-state-unexpected-reboot/CASE-01：正常操作重启与内核崩溃的对照时间线]
