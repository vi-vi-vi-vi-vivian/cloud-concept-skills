---
id: ecs-storage-disk-expand-failed
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 扩容后容量未增加

## Overview

- **Issue：**云盘扩容失败，或云盘已增大但 OS/应用仍见旧容量。
- **Environment：**Linux ECS；云盘、块设备、分区/卷与文件系统映射已知。
- **Resolution：**指出容量在哪一层尚未变化及下一处理前提。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 对齐盘身份和预期容量

按[Helper](../../helpers.md)映射云盘与主机设备；按[云配置](../../commands/configuration/hcloud.md#evs)核对扩容任务/容量。任务未成功时停在云侧证据，不执行主机扩容。

[待补 ecs-storage-disk-expand-failed/DOC-01：华为云扩容状态、系统与文件系统在线扩容条件]

### 逐层比较可见容量

按[块设备/分区/挂载](../../commands/configuration/linux.md)和[文件系统容量](../../commands/performance/linux.md)比较整盘、分区、LVM 等中间卷层及文件系统。整盘没更新、分区没增长、卷层未扩展和文件系统未增长分别交付；未分区或未使用 LVM 时跳过对应层。

[待补 ecs-storage-disk-expand-failed/TOOL-01：扩容任务及 LVM/分区/文件系统对应模式契约]

### 给出针对性处理条件

明确需要更新的层、文件系统类型、在线支持条件及保护方案；暂不生成未核验的 growpart/文件系统修改命令。所有层均已增长则回到应用实际挂载/配额核对，避免重复扩容。

[待补 ecs-storage-disk-expand-failed/CASE-01：不同层未生效及成功后应用可见容量验证]
