---
id: ecs-configuration-cloud-init-failed
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# cloud-init 或 user-data 初始化失败

## Overview

- **Issue：**OS 已进入初始化阶段，脚本未执行、部分失败或等待依赖超时。
- **Environment：**Linux ECS；镜像、cloud-init 版本、启动次数及目标配置已知。
- **Resolution：**定位数据下发、处理阶段、依赖或脚本失败。

## Guidance

执行按[入口规则](../../../SKILL.md)，远程取证按[通道](../../execution.md)；结果按[报告字段](../../report.md)记录。

### 区分没执行与执行失败

对照当前启动的状态、阶段日志和输出，确认预期执行频率。系统启动完成不代表初始化完成；后续启动未重跑可能符合模块频率。系统尚未启动则转[启动诊断](../instance-state/boot-failed.sop.md)。

[待补 ecs-configuration-cloud-init-failed/DOC-01：华为云镜像 datasource、内容格式/编码和模块执行频率]

### 沿失败阶段补证据

核对 user-data 是否下发、内容类型和解析结果，再定位首个失败模块/命令及退出原因。通过[服务日志](../../commands/fault/linux.md)保留上下文；元数据根路径响应不能证明 user-data 已交付。仅取必要脱敏片段，避免输出脚本中的凭据。

[待补 ecs-configuration-cloud-init-failed/TOOL-01：初始化状态/日志及安全读取下发证据的契约]

### 选择对应依赖调查

DNS/网络依赖失败转[网络](../network.md)，内存终止证据转[OOM](../performance/oom-kill.sop.md)。内容已部分执行时记录副作用和幂等性，交付具体失败边界；清状态或重跑需独立方案，不能用作默认验证。

[待补 ecs-configuration-cloud-init-failed/CASE-01：未下发、格式错误、依赖失败和重复执行工单]
