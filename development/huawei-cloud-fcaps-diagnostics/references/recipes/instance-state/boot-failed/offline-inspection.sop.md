---
id: ecs-instance-state-boot-failed-offline-inspection
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# 启动故障：离线系统盘调查

## Overview

- **Issue：**启动主篇证据不足，且需要离线读取系统盘内容。
- **Environment：**Linux ECS；盘身份、保护副本/救援环境、停机影响和授权已明确。
- **Resolution：**返回磁盘内证据及对应启动阶段；不混淆救援机与原主机。

## Guidance

执行按[入口规则](../../../../SKILL.md)，远程取证按[通道](../../../execution.md)；结果按[报告字段](../../../report.md)记录。

### 先满足进入条件

由[启动主篇](../boot-failed.sop.md)传入对象与阶段。说明停机、拆挂盘和救援环境的具体影响；缺少保护方案、执行契约或相应授权时停在准备结果。优先使用已有副本，读取方式须确认是否会回放日志或写入。

[待补 ecs-instance-state-boot-failed-offline-inspection/DOC-01：救援方式、盘保护与离线读取写入影响]

### 限定调查对象

核对云盘到设备/分区/文件系统映射，原盘与救援系统盘分开。只围绕已知阶段查看引导配置、内核/initrd、挂载配置及留存日志；救援机当前服务状态不能代表原机。

[待补 ecs-instance-state-boot-failed-offline-inspection/TOOL-01：救援创建、盘映射、只读挂载及退出恢复的契约]

### 返回并交接恢复

返回读取位置、盘/副本版本、证据时间和支持的假设。修复、chroot 执行、文件系统修复和回挂启动须另有具体方案；缺少执行契约时不生成猜测命令。

[待补 ecs-instance-state-boot-failed-offline-inspection/CASE-01：离线证据如何确认原因及回挂后启动验证]
