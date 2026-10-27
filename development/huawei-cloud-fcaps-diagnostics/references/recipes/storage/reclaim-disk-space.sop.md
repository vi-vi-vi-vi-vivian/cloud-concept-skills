---
id: ecs-storage-reclaim-disk-space
intent: recover
environment: huawei-cloud-ecs-linux
status: draft
---

# 回收已确认可释放的磁盘空间

## Overview

- **Issue：**磁盘满诊断已定位占用，用户要求释放空间。
- **Environment：**Linux ECS；目标文件系统、对象归属与保留要求已确认。
- **Resolution：**形成最小回收方案；执行条件齐备后用原写入验证恢复。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 把占用转换为候选对象

复用[磁盘满诊断](disk-full.sop.md)结果，逐项列出日志、缓存、历史部署或已删除仍打开文件的归属、预计可回收量和保留要求。文件大、旧或位于临时目录都不自动表示可删除。

[待补 ecs-storage-reclaim-disk-space/DOC-01：日志保留、业务数据清理及备份恢复规范]

### 准备并选择一项操作

选定应用支持的轮转/清理/句柄释放方式，说明准确目标、影响、保护与失败处置。删除不能假装有回滚，备份也需验证可恢复。缺正式操作契约或授权时交付方案；不运行泛化删除、截断或杀进程命令。

[待补 ecs-storage-reclaim-disk-space/TOOL-01：按对象限定的清理/轮转/释放操作、效果与失败契约]

### 按实际结果复测

如已获准且契约齐备，执行选定操作并核对释放的容量/inode，再复测原失败写入。未释放则查持有句柄/挂载范围，不叠加盲目清理；记录剩余增长趋势和后续轮转建议。

[待补 ecs-storage-reclaim-disk-space/CASE-01：实际回收量、原写入复测及复发记录]
