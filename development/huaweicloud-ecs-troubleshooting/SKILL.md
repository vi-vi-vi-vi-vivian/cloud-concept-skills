---
name: huaweicloud-ecs-troubleshooting
description: 查询华为云 ECS 及关联资源，选择 hcloud 诊断命令，解析跨命令依赖。适用于实例、网络、存储、指标、日志、权限和费用异常的证据查询。场景配方目前仅为规划。
---

# ECS 诊断

目标：取得当前问题所需的证据，说明已确认的故障边界和缺口。

- 工作准则：歧义仅问改查证路径者；已述/已决不重问；可自证则推进；须裁断则一次一问。
- 目标或现象不明确时，读[分诊](references/triage.md)。复用已知账号、区域、实例和时间窗。
- 首次调用或访问失败时，读[Shared](references/shared.md)。服务或操作未知时，读[Service](references/services.md)。
- 按问题选择 [FCAPS 命令分册](references/commands/index.md)。按完整命令 ID 搜索命中行；详细参数查所选操作的 help。
- 缺少资源标识时，读[Helper](references/helpers.md)的对应条目。已有标识直接使用。
- 按契约的作用与约束执行。当前授权未覆盖的修改、扫描、主机执行和消息发送，先给出具体动作与影响。
- 需要核验证据范围时，按命令 ID 读[验证记录](references/verification.md)。
- 将权限拒绝、空结果和成功明细分别记录。单次接口成功不能证明整个系统正常。
- recipes 只提供规划指导。实际查询依照命令契约；结论使用[报告字段](references/report.md)。
