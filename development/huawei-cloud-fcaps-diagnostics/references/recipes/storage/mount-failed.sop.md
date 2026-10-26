---
id: ecs-storage-mount-failed
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 文件系统挂载失败或挂载异常

## Overview

- **Issue：**目标盘未挂载、挂错路径或只读；启动挂载失败可由 boot 转入。
- **Environment：**Linux ECS；设备身份、期望挂载点与原始错误已知。
- **Resolution：**区分盘发现、分区/文件系统身份、配置与运行状态。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 先确认设备而非猜路径

按[块设备、稳定名称与文件系统身份](../../commands/configuration/linux.md)核对云盘映射。重启后设备名可能变化；UUID、分区标识与云盘 ID 分别处理。设备未出现时先查云侧挂载关系及主机识别。

[待补 ecs-storage-mount-failed/DOC-01：支持的文件系统、挂载依赖与故障恢复边界]

### 对照期望与实际

比较当前挂载关系、预期配置及同时间窗[服务/内核日志](../../commands/fault/linux.md)。区分找不到设备、类型/选项不匹配、依赖失败和文件系统报错；只读现象不能直接证明物理盘损坏。

[待补 ecs-storage-mount-failed/TOOL-01：挂载配置只读读取及文件系统检查模式契约]

### 交付可修正边界

给出错误、对应设备和配置差异。疑似损坏先保留证据及数据保护要求；格式化、fsck、强制挂载或改 fstab 不作为诊断动作。无法启动时把结论返回[启动诊断](../instance-state/boot-failed.sop.md)。

[待补 ecs-storage-mount-failed/CASE-01：设备名变化、配置错误与真实损坏对照工单]
