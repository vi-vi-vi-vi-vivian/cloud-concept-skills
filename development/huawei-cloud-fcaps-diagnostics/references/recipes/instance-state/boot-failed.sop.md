---
id: ecs-instance-state-boot-failed
intent: diagnose
environment: huawei-cloud-ecs
status: draft
---

# 实例启动失败或 OS 未就绪

## Overview

- **Issue：**启动任务失败、状态长期未完成，或实例显示运行但 OS 未正常启动。
- **Environment：**ECS；OS 启动链部分仅适用于 Linux，Windows 需补对应证据。
- **Resolution：**定位管理状态、引导、内核、挂载或系统服务阶段。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 分开平台状态与 OS 状态

按[云故障](../../commands/fault/hcloud.md#ecs)与[云配置](../../commands/configuration/hcloud.md#ecs)核对任务、实例、镜像和近期变更。没有主机代理响应不等于 OS 未启动。控制台证据已显示系统就绪时，登录问题转[登录](../login.md)，初始化脚本问题转[cloud-init](../configuration/cloud-init-failed.sop.md)。

[待补 ecs-instance-state-boot-failed/DOC-01：华为云启动状态、镜像/规格兼容性及控制台可用性]

### 让日志决定下一层

读取已有控制台或启动日志，定位最后成功阶段和首个具体错误：引导器、内核/initrd、根文件系统、挂载依赖或服务。结合镜像/规格/启动模式变更验证关联；泛化报错不能唯一确定原因。挂载证据明确时转[挂载失败](../storage/mount-failed.sop.md)。

[待补 ecs-instance-state-boot-failed/TOOL-01：启动任务、控制台日志和历史启动证据获取契约]

### 决定是否需要离线调查

在线证据不足且需检查系统盘时读[离线调查](boot-failed/offline-inspection.sop.md)，传入已确认启动阶段、磁盘身份及变更记录。离线前提不具备时交付现有证据与缺口；不把救援作为必做步骤。

[待补 ecs-instance-state-boot-failed/CASE-01：各启动阶段的具体报错及恢复复测]
