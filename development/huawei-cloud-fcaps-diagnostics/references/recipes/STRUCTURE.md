# Recipe 目标结构与维护规则

本文件供维护者使用。目标结构采用 ITSM 事件分类的分层与路由思路，以 ECS 症状/任务定义类目；条目按 KCS 组织信息，执行部分借用 Agent SOP。以下目录和字段是项目约定，不是行业标准规定的固定清单。

## 目标结构

```text
references/
├── triage.md                         # 描述不明确时先分诊
├── commands/                         # 既有 FCAPS 事实工具
└── recipes/
    ├── STRUCTURE.md                  # 本文件：分类边界、维护规则
    ├── template.md                   # KCS + Agent SOP 简版模板
    ├── index.md                      # 已有流程的检索索引
    ├── instance-state/               # 创建、启动、停止及异常状态
    │   ├── boot-failed.sop.md
    │   └── unexpected-reboot.sop.md
    ├── login/                        # SSH、RDP、VNC 管理登录
    │   ├── ssh-timeout.sop.md
    │   ├── ssh-auth-failed.sop.md
    │   └── rdp-unavailable.sop.md
    ├── network/                      # 通用网络、业务连接
    │   ├── outbound-unreachable.sop.md
    │   ├── dns-resolution-failed.sop.md
    │   └── packet-loss.sop.md
    ├── storage/
    │   ├── disk-full.sop.md
    │   ├── mount-failed.sop.md
    │   └── reclaim-disk-space.sop.md
    ├── performance/
    │   ├── high-cpu.sop.md
    │   └── high-io-latency.sop.md
    ├── configuration/                # 配置不生效、配置漂移
    ├── security/                     # 云权限、可疑安全行为
    └── cost/                         # 费用/计量异常，按需建设
```

只为实际内容建文件。当前已落地 [SSH 超时诊断](login/ssh-timeout.sop.md)、[登录分诊](login.md)、[索引](index.md)及[模板](template.md)；其余示例路径是规划，不能作为已可执行流程。原九项入口文件暂留，其中 login 已改为分诊，其余八项保留占位并逐步迁移；boot/crash 进入 instance-state，具体恢复流程回到相应场景。

## 分类边界

| 类别 | 收录入口 | 重叠时的规则 |
| --- | --- | --- |
| instance-state | 创建/启动/停止失败、意外重启、系统崩溃 | 运行中但登录失败优先 login |
| login | SSH、RDP、VNC 管理登录失败 | 即使最终原因是网络、安全规则或资源压力，也留在 login |
| network | DNS、出网、通用业务端口、丢包 | 管理登录协议的特定失败优先 login |
| storage | 空间不足、挂载失败、只读、读写失败 | 以容量/功能异常为入口；IO 延迟大归 performance |
| performance | CPU/内存占用高、延迟高、吞吐低 | 空间满归 storage；诊断出的根因不决定文件搬迁 |
| configuration | 明确以配置未生效、配置漂移为诉求 | 其他场景发现配置错误时保留原场景归属 |
| security | 云 API 权限被拒、可疑访问 | SSH 认证失败优先 login；结合上下文解释报错 |
| cost | 账单突增、异常计量、闲置成本 | 其他诊断发现欠费时按需引用，不改变主维护位置 |

“服务器连不上”等模糊描述先分诊。按用户入口现象归类，一条流程只有一个正文，通过链接提供其他入口。恢复是用途，例如 storage/reclaim-disk-space.sop.md 使用 intent: recover，不另建跨场景的 recovery 总目录。

## 条目结构

- **Overview**：KCS 的 Issue、Environment、Resolution、可选 Cause；随后写跨步骤 Constraints 和全局 Stop conditions。
- **Steps**：按 Agent SOP 分步描述动作；每步写 Constraints 和 Stop conditions。停止既包括完成，也包括转诊或证据受阻，均输出已有结论和缺口。
- **元数据**：id、intent、environment、status。当前保持最少字段；同义描述和匹配边界放 Issue。索引手工维护摘要，不宣称已自动生成。

Cause 记录已有依据的可复用原因知识；待确认的原因放 Steps 作为待验证假设。Overview 内的 Resolution 指向下面的流程，不再维护第二套步骤。

## 新增与维护

1. 先搜索已有问题、同义描述和环境。相同场景补充分支；目标或主体执行路径明显不同再拆新条目。
2. 按上表选唯一目录，采用描述症状或任务的 kebab-case 文件名和 .sop.md 扩展名；id 保持稳定。
3. 复制模板，按已有事实契约写取证步骤、证据解释边界和退出条件。未覆盖的命令模式先补 commands，或明确留为缺口。
4. Linux/Windows、在线/离线差异少时用分支，主体流程明显不同时才拆变体，并写清区分条件。不预建所有环境组合。
5. 更新 index.md 中的触发条件、环境、路径和状态；原入口若有引用，一并维护。具体命令只在 commands 定义一次。
6. status 使用 draft、reviewed 或 deprecated；reviewed 表示内容审阅，不代表真实环境实测通过。来源、维护责任和端到端验证情况在开发说明记录，执行结果使用 report.md。

## 第一条流程的来源与验证

本轮新增的是人工整理的诊断草稿，尚未指定长期维护组，尚未做真实 ECS 端到端验证。原命令分册的历史验证只覆盖其记录范围，不能转化为整条 recipe 已验证。

- [华为云：无法登录到 Linux 云服务器](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0105127983.html)：2026-10-22 阅读；借鉴状态、端点、网络规则、主机等排查范围，不照搬其中恢复操作或泛化结论。
- [KCS Article Structure](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health/Technique_5.1)：Issue、Environment、Resolution、可选 Cause 及内容维护思路。
- [BMC Operational catalogs](https://docs.helixops.ai/bin/Service-Management/IT-Service-Management/BMC-Helix-ITSM/itsm251/Administering/Setting-up-and-modifying-Foundation-data-by-using-Application-Administration-Console/Configuring-product-and-operational-catalogs/Configuring-operational-catalogs/)：症状/操作分类及路由思路。
- [Agent SOP Author](https://github.com/strands-agents/agent-sop/tree/main/skills/agent-sop-author)：借用 Overview、Steps、约束关键词及 .sop.md 命名。本项目按用户要求采用简版，将输入并入 Environment，不强制独立 Parameters、Examples、Troubleshooting 章节。
- 友商本地资料借鉴：Alibaba Linux SSH 排查的云侧/主机层次，以及 Microsoft SSH 症状分流；华为云契约、执行通道和证据限制以本仓为准。

本次只变更 recipes，顶层入口说明和 QA 保持原版本。本地检查仅核对目录内引用和内容结构，不调用云 API；旧 QA 仍要求九个占位条目，与新增流程不兼容，需后续调整。原云端门禁还绑定旧整套运行文档摘要，新增流程后需要新的真实证据才能重新签署；不修改历史记录来伪装通过。
