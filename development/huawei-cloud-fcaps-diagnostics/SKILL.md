---
name: huawei-cloud-fcaps-diagnostics
description: 按 FCAPS 选择华为云 hcloud、Linux、Windows 及可选 Kubernetes 的事实查询，解析命令依赖。用于实例、网络、存储、日志、性能、权限和费用问题的证据定位。
---

# 华为云 FCAPS 诊断

目标：取得问题所需的观测，说明已确认的边界和证据缺口。

- 已知命令：直接搜索 `references/commands/` 中的完整 ID。已知场景：按 [Recipe 索引](references/recipes/index.md) 选择指导；未覆盖的问题按 [FCAPS 地图](references/commands/index.md) 选择类别和环境；目标不明时读[分诊](references/triage.md)。
- 需要解释观测、核对适用条件或补充依据时读[文档入口](references/documents/index.md)；按需取原文，已知命令不先加载文档。
- 首次执行读[共同约束](references/shared.md)。切换工具或环境时，只读对应工具入口；远程主机执行时读[通道](references/execution.md)。
- 已有标识和时间窗直接复用；缺输入才读 [Helper](references/helpers.md)。按所选契约执行，不把观测直接写成根因。
- 需要判断实测范围时按 ID 读[验证摘要](references/verification/index.md)。结果按[报告字段](references/report.md)记录。Recipe 为待内部适配与实测的 draft；缺口不视为已具备的工具能力。
