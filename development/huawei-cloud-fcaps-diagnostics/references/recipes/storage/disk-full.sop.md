---
id: ecs-storage-disk-full
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 磁盘空间或 inode 不足

## Overview

- **Issue：**写入报 No space left on device，或文件系统容量/inode 接近耗尽。
- **Environment：**Linux ECS；实际失败路径及其挂载环境已知。
- **Resolution：**定位限制类型、占用来源并选择恢复方向。

## Guidance

执行按[共同约束](../../shared.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 从失败路径定位文件系统

按[容量/inode](../../commands/performance/linux.md)与[挂载关系](../../commands/configuration/linux.md)确定失败路径所在文件系统；容器和宿主观察范围分别标明。磁盘未满时继续核对配额、只读或应用限制，不强行归入空间满。

[待补 ecs-storage-disk-full/DOC-01：配额、文件系统和容器挂载范围的容量语义]

### 按限制类型追查占用

容量不足时有界调查目录占用；inode 不足时查小文件增长来源。df/du 差异先核对同挂载范围、权限和扫描完整性，再按[打开的已删除文件](../../commands/fault/linux.md)验证持有者；差异本身不能唯一证明文件未释放。

[待补 ecs-storage-disk-full/TOOL-01：配额/小文件分布的有界只读契约]

### 交付处理方向

确认可回收对象及业务归属后转[回收空间](reclaim-disk-space.sop.md)。已扩容仍无变化转[扩容未生效](disk-expand-failed.sop.md)。只给占用证据和候选操作，不把所有日志/临时文件当可删除。

[待补 ecs-storage-disk-full/CASE-01：容量满、inode 满及 df/du 差异工单]
