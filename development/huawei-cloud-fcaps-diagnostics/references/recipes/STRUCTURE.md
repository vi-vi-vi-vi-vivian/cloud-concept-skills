# Recipe 目标结构与维护规则

本文件供维护者使用。目标结构采用 ITSM 事件分类的分层与路由思路，以 ECS 症状/任务定义类目；条目按 KCS 组织信息，以判断目标、证据和分支提供指导，沿用 .sop.md 命名。以下目录和字段是项目约定，不是行业标准规定的固定清单。

## 目标结构

```text
references/
├── triage.md                         # 描述不明确时先分诊
├── commands/                         # 既有 FCAPS 事实工具
└── recipes/
    ├── STRUCTURE.md                  # 本文件：分类边界、维护规则
    ├── template.md                   # KCS Overview + Guidance 轻量模板
    ├── index.md                      # 已有流程的检索索引
    ├── instance-state/               # 创建、启动、停止及异常状态
    │   ├── boot-failed.sop.md
    │   ├── boot-failed/
    │   │   └── offline-inspection.sop.md
    │   └── unexpected-reboot.sop.md
    ├── login/                        # SSH、RDP、VNC 管理登录
    │   ├── ssh-timeout.sop.md
    │   ├── ssh-timeout/              # 条件读取的子 recipe
    │   │   ├── cloud-path.sop.md
    │   │   └── host-endpoint.sop.md
    │   ├── ssh-auth-failed.sop.md
    │   └── rdp-unavailable.sop.md
    ├── network/                      # 通用网络、业务连接
    │   ├── outbound-unreachable.sop.md
    │   ├── dns-resolution-failed.sop.md
    │   └── packet-loss.sop.md
    ├── storage/
    │   ├── disk-full.sop.md
    │   ├── disk-expand-failed.sop.md
    │   ├── mount-failed.sop.md
    │   └── reclaim-disk-space.sop.md
    ├── performance/
    │   ├── high-cpu.sop.md
    │   ├── high-load.sop.md
    │   ├── memory-pressure.sop.md
    │   ├── oom-kill.sop.md
    │   └── high-io-latency.sop.md
    ├── configuration/                # 配置不生效、配置漂移
    │   └── cloud-init-failed.sop.md
    ├── security/                     # 云权限；事件响应待建设
    │   └── api-permission-denied.sop.md
    └── cost/                         # 费用/计量异常，按需建设
```

当前已按本模板落地 19 篇场景草稿及 3 篇条件子篇，入口见 [index](index.md)。原九项入口文件保留为分诊/任务路由，boot/crash 指向 instance-state，恢复回到具体场景。cost 仍按需建设，尚无正文。

本轮提取依据为本地固定友商快照。来源及哈希、内部补充清单保存在仓库 qa/development/huawei-cloud-fcaps-diagnostics/recipe-sources.json 与 recipe-supplements.md，供维护者使用；运行时不必读取研究资料。所有正文仍为 draft，未进行真实 ECS 验证。

## 分类边界

| 类别 | 收录入口 | 重叠时的规则 |
| --- | --- | --- |
| instance-state | 创建/启动/停止失败、意外重启、系统崩溃 | 运行中但登录失败优先 login |
| login | SSH、RDP、VNC 管理登录失败 | 即使最终原因是网络、安全规则或资源压力，也留在 login |
| network | DNS、出网、通用业务端口、丢包 | 管理登录协议的特定失败优先 login |
| storage | 空间不足、挂载失败、只读、读写失败 | 以容量/功能异常为入口；IO 延迟大归 performance |
| performance | CPU/内存占用高、延迟高、吞吐低 | 空间满归 storage；诊断出的根因不决定文件搬迁 |
| configuration | 明确以配置未生效、配置漂移或初始化脚本失败为诉求 | 已进入初始化阶段的 cloud-init/user-data 失败优先此处；OS 未能启动仍按 instance-state 分诊 |
| security | 云 API 权限被拒、可疑访问 | SSH 认证失败优先 login；结合上下文解释报错 |
| cost | 账单突增、异常计量、闲置成本 | 其他诊断发现欠费时按需引用，不改变主维护位置 |

“服务器连不上”等模糊描述先分诊。按用户入口现象归类，一条流程只有一个正文，通过链接提供其他入口。恢复是用途，例如 storage/reclaim-disk-space.sop.md 使用 intent: recover，不另建跨场景的 recovery 总目录。

## 最小单元与拆分

默认从一篇有明确现象/任务和交付目标的 recipe 开始。按判断任务和读取条件拆分，不机械按云侧/主机侧、FCAPS、工具或章节数量拆分。

| 形式 | 使用条件 | 例子 |
| --- | --- | --- |
| 篇内分支 | 共享同一目标和大部分前提，差异能简短表达 | 磁盘满先区分容量与 inode，按证据选择占用调查 |
| 并列 recipe | 可由不同现象/任务直接命中，或交付目标不同 | CPU 高与负载高；磁盘满诊断与空间回收；SSH 超时与认证失败 |
| 条件子 recipe | 只有部分路径需要，具有独立目标、输入和返回结果，展开会干扰主线 | 启动故障的离线调查；SSH 超时的云侧路径或主机端点检查 |

子篇沿用模板：父篇交代何时读取、哪些已知事实可传入；子篇交付判断、证据和缺口并返回。目标资源与时间窗沿用，缺失且影响当前检查时再补。子篇没有新增判断或只包装一条命令时，留在父篇或引用 commands/Helper。

诊断 recipe 可以组织多个待验证原因的分支；原因已明确且处理互不适用的恢复方法，按各自条件另写 recipe，避免把所有修复串成必做步骤。

专属子篇按需放在与主文件同名的目录中；跨场景复用已有 recipe 时直接链接其唯一正文。只有对象、输入、判断含义和交付结果确实一致时才共用，不因都涉及网络或主机就合并。独立可搜索的子篇可进入索引；仅被父篇调用的子篇从父篇可达即可，不必重复注册。

### 当前来源支持的拆分候选

以下是固定友商快照抽读后的拆分依据；本轮已据此落地候选草稿，不代表运行验证。依据与取舍保存在维护侧的《Recipe 场景拆分复核》（工作区 analysis/recipe-decomposition-review.md），不作为运行时必读材料。

| 场景 | 起步方式 | 何时再拆 |
| --- | --- | --- |
| SSH/RDP 连接失败 | 先按失败阶段分诊，超时与认证失败并列 | 云路径与主机调查展开较长且读取条件不同，再设条件子篇；不规定每篇都两段拆分 |
| 实例启动/不可用 | 主篇先区分管理状态、OS 启动和初始化阶段 | 离线调查有独立前提时拆子篇；已启动后的 cloud-init 失败按独立诉求建入口 |
| CPU 高、负载高 | 分别建入口，篇内解释 CPU 类别与运行/等待线索 | 特定组件调查有明确触发、足够独立内容时再拆；不因都有云/主机查询而拆 |
| 内存压力、OOM 事件 | 高占用与已发生的 OOM 按诉求区分，重合取证引用 | 持续压力与历史事件的调查确实展开成独立任务时拆；不能把高占用直接写成 OOM |
| 磁盘满 | 先一篇，区分容量、inode、占用及观测差异 | 清理回收、扩容是不同任务，另建 recipe；诊断中仅条件引用 |
| 扩容后容量未增加 | 一篇按云盘、OS 块设备、分区和文件系统定位边界 | 分区/文件系统差异或执行前提形成独立调查时拆；不预建四篇或所有文件系统变体 |
| IO 慢 | 一篇关联云盘、实例与主机同时间窗观测 | 某后端/组件有独立证据链时拆；厂商配额、阈值和调优不直接通用化 |
| 通用网络/DNS | 按连接目标和失败阶段路由；DNS 有独立诉求时独立入口 | 与 SSH 等场景需要相同路径判断时复用唯一正文，保留实际源与观测点差异 |

## 条目结构

- **Overview**：用简短条目保留 KCS 的 Issue、Environment、Resolution、可选 Cause，说明适用范围和交付目标。
- **Guidance**：围绕判断目标组织证据、解释边界和下一步；必要约束与退出条件写在相关判断附近，不强制每节重复固定栏目。
- **元数据**：id、intent、environment、status。当前保持最少字段；同义描述和匹配边界放 Issue。索引手工维护摘要，不宣称已自动生成。

Cause 记录已有依据的可复用原因知识；待确认的原因放 Guidance 作为待验证假设。Overview 内的 Resolution 指向下文，不再维护第二套步骤。

主、子 recipe 共用此结构；父篇说明读取条件，子篇有独立目标和返回条件。具体工具契约继续只在 commands 定义。工单、内部帮助文档和工具缺口使用模板规定的待补标记；详细补充记录留在维护资料中。SSH 超时已迁移为本模板，并通过父篇条件调用云侧路径与主机端点子篇。

## 新增与维护

1. 先搜索已有问题、同义描述和环境。相同场景补充分支；目标或主体执行路径明显不同再拆新条目。
2. 按上表选唯一目录，采用描述症状或任务的 kebab-case 文件名和 .sop.md 扩展名；id 保持稳定。
3. 复制模板，按已有事实契约写取证步骤、证据解释边界和退出条件。未覆盖的命令模式先补 commands，或明确留为缺口。
4. 按“最小单元与拆分”选择篇内分支、并列或条件子篇。Linux/Windows、在线/离线差异少时用分支，主体调查明显不同时再拆，并写清输入和返回条件。不预建所有环境组合。
5. 更新 index.md 中的触发条件、环境、路径和状态；原入口若有引用，一并维护。具体命令只在 commands 定义一次。
6. status 使用 draft、reviewed 或 deprecated；reviewed 表示内容审阅，不代表真实环境实测通过。来源、维护责任和端到端验证情况在开发说明记录，执行结果使用 report.md。

## 来源与验证边界

本轮正文是基于固定友商快照人工整理的诊断与恢复指导草稿，尚未指定长期维护组，尚未做真实 ECS 端到端验证。原命令分册的历史验证只覆盖其记录范围，不能转化为整条 recipe 已验证。

- [华为云：无法登录到 Linux 云服务器](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0105127983.html)：2026-10-22 阅读；借鉴状态、端点、网络规则、主机等排查范围，不照搬其中恢复操作或泛化结论。
- [KCS Article Structure](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health/Technique_5.1)：Issue、Environment、Resolution、可选 Cause 及内容维护思路。
- [BMC Operational catalogs](https://docs.helixops.ai/bin/Service-Management/IT-Service-Management/BMC-Helix-ITSM/itsm251/Administering/Setting-up-and-modifying-Foundation-data-by-using-Application-Administration-Console/Configuring-product-and-operational-catalogs/Configuring-operational-catalogs/)：症状/操作分类及路由思路。
- [Agent SOP Author](https://github.com/strands-agents/agent-sop/tree/main/skills/agent-sop-author)：原 SSH 草稿借鉴其 Overview、Steps 和 .sop.md 命名。当前轻量模板采用 Overview/Guidance，不宣称完整遵循 Agent SOP 规范。
- 友商本地资料借鉴：Alibaba Linux SSH 排查的云侧/主机层次，以及 Microsoft SSH 症状分流；华为云契约、执行通道和证据限制以本仓为准。

本轮同步了 recipes、分诊与技能入口，并将来源/待补清单保存在 QA 目录。本地检查只验证文档结构、引用和技能基础格式，不调用云 API。旧 QA 仍要求九个规划占位条目，与当前正文不兼容；所需历史证据目录亦未提供。云端门禁绑定旧运行文档摘要，重新签署需要新证据，不修改历史记录来宣称通过。
