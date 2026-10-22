---
id: ecs-login-ssh-timeout
intent: diagnose
environment: huawei-cloud-ecs-linux
status: draft
---

# Linux ECS SSH 连接超时诊断

## Overview

### Issue

适用于 SSH 建立连接阶段出现 `Connection timed out`、连接目标端口持续无响应。端口以客户端实际配置为准。

`Connection refused`、`Permission denied`、主机密钥校验失败，以及 TCP 已建立后的 SSH 握手或认证超时，转[登录分诊](../login.md)；仅描述“服务器连不上”时先区分管理登录与业务访问。

### Environment

目标是华为云 Linux ECS。复用已有账号/区域、实例标识、故障时间窗、原始报错、连接源、目的地址和端口；区分直连、VPN、堡垒机或代理，来源有 NAT 时核对目标侧实际源地址。缺失信息只在影响当前检查时补齐。

云查询依赖可用的 hcloud 身份；主机检查依赖已就绪的独立通道，按[执行通道](../../execution.md)确认。缺云权限仍可分析已有主机证据，缺主机通道仍可完成云侧检查。

### Resolution

按下列步骤定位故障边界，区分已确认事实、候选原因和证据缺口，按[报告字段](../../report.md)输出。目标是诊断；恢复建议单列具体动作及验证条件。

### Cause

本流程不预设根因。端点/路径不符、实例不可用、访问规则不匹配、主机监听或回程异常都是待验证方向。只有目标、时间和匹配条件对应的证据充分时，才写入已确认原因。

### Constraints

- MUST 遵守[共同约束](../../shared.md)，从所链接的 commands 契约读取实际命令、输入和影响，不在本文件维护第二套命令。
- MUST 将当前配置与故障时间窗区分；快照和一次采样只能支持对应时刻的判断。
- SHOULD 优先复用已有错误与查询。主动探测和条件采集按当前授权及实际影响选择；重启、改规则、重置密码、安装 Agent、发起诊断任务不属于本诊断的默认步骤。

### Stop conditions

以下“停止”均先记录已有证据，再转步骤 6 输出：目标无法唯一确定；现象超出范围；证据足以回答问题；剩余区分检查缺权限、通道或契约；用户要求停止。局部受阻时继续其他可独立完成的已授权检查。已确认边界后仍保留其他未检查范围。

## Steps

### 1. 确认失败阶段和连接范围

读取报错及时间，确认连接源、实际端点、端口和路径。使用域名时核对该客户端当时解析结果；经过堡垒机/代理时确认哪一段超时。仅在授权的 Linux 连接源上，才按 [LINUX/dns-query](../../commands/fault/linux.md)补查 A 记录。

**Constraints:** MUST 用实际错误区分超时、拒绝连接和认证失败；管理机的解析结果不替代用户连接源。DNS 契约只覆盖 A 记录，IPv6 或代理端点证据不足时保留缺口。

**Stop conditions:** 属于其他失败阶段时转登录分诊；连接目标或失败链路仍有多个候选且影响查询时，暂停依赖它的检查。范围确定后进入步骤 2。

### 2. 核对实例状态和目标绑定

用 [ECS/ShowServer/v2](../../commands/configuration/hcloud.md#ecs)核对身份、状态和地址，用 [ECS/ListServerInterfaces/v2](../../commands/configuration/hcloud.md#ecs)核对连接对应的网卡。存在启动/系统异常线索时，读取 [ECS/ShowServerConsoleOutput/v2](../../commands/fault/hcloud.md#ecs)。

**Constraints:** MUST 将结果绑定到步骤 1 的目标。“运行中”不证明 GuestOS 或 SSH 正常；关机/异常状态可以解释当前不可用，不自动解释其形成原因。当前状态不替代故障时状态。

**Stop conditions:** 目标地址属于其他资源，或实例不可用已足以回答当前问题时转步骤 6；否则进入步骤 3。云查询受阻时保留缺口，已有网络绑定仍可供下一步使用。

### 3. 核对云侧路径与访问规则

按实际路径选择检查，内网访问不要求 EIP：

- 公网直连且依赖 EIP：按 [H-eip](../../helpers.md#h-eip)解析绑定，用 [EIP/ShowPublicip/v3](../../commands/configuration/hcloud-network.md#eip)核对地址和端口关联；代理/转发映射不在当前契约覆盖内时保留缺口。
- 目标网卡/子网：按 [H-port](../../helpers.md#h-port)、[H-subnet](../../helpers.md#h-subnet)解析，必要时用 [VPC/ShowPort/v3](../../commands/configuration/hcloud-network.md#vpc)、[VPC/ShowSubnet/v2](../../commands/configuration/hcloud-network.md#vpc)读取配置。
- 安全组：对目标端口实际关联的组调用 [VPC/ListSecurityGroupRules/v3](../../commands/configuration/hcloud-network.md#vpc)，核对实际源、协议、目的端口及规则条件；多组和优先级按[官方文档入口](../../documents/index.md)核对求值语义。
- 自定义路由、VPN、对等连接、ACL 确在路径中时，按 [VPC 配置契约](../../commands/configuration/hcloud-network.md#vpc)及相应服务分册核对绑定、方向、匹配条件及回程。关联关系无法确认时，不将任意规则套给目标。

**Constraints:** MUST 解释匹配实际流量的有效规则，单条“允许”记录不证明全路径放行；空结果、权限错误与规则不匹配分别记录。缺历史或流量证据时说明时间及因果边界。

**Stop conditions:** 证据足以确认路径/规则问题且无需继续区分时转步骤 6；仍有竞争假设或配置不足以解释时进入步骤 4。

### 4. 经可用通道核对主机

有独立通道时，用 [LINUX/os-release](../../commands/common/linux.md)、[LINUX/identity](../../commands/common/linux.md)确认目标环境和执行身份，再按现象选择：

- [LINUX/connections](../../commands/configuration/linux.md)：核对实际端口的监听、监听地址、协议族及可见进程。缺进程权限不等于不存在监听。
- 按 [H-unit](../../helpers.md#h-unit)发现服务后，用 [LINUX/service-status](../../commands/fault/linux.md)、[LINUX/unit-journal](../../commands/fault/linux.md)读取状态和故障时段事件。服务名、激活方式依系统而异，不能仅凭某个 unit 未运行判断 SSH 不可用。
- [LINUX/addresses](../../commands/configuration/linux.md)、[LINUX/routes](../../commands/configuration/linux.md)、[LINUX/rules](../../commands/configuration/linux.md)：结合实际源核对接口和回程。现有路由/规则模式覆盖 IPv4，IPv6 需补适用契约。
- 主机防火墙存在时，按 [LINUX/iptables-filter](../../commands/security/linux.md)或 [firewalld 查询](../../commands/security/linux.md)读取适用规则；结果仅覆盖对应后端和范围。
- 已有资源压力线索时，按[性能契约](../../commands/performance/linux.md)有限采样并结合故障时段日志；单次 CPU/内存数值不直接确认为超时原因。

**Constraints:** MUST 在目标内执行。缺独立通道时记录主机侧未采集，不经故障 SSH 反复尝试或默认安装 Agent。缺 sshd 有效配置、其他防火墙后端或协议族契约时，明确列为未覆盖检查。

**Stop conditions:** 主机证据足以解释问题时转步骤 6；缺通道或仍无法区分网络与主机问题时，带着已有证据进入步骤 5。

### 5. 对剩余假设做最小区分检查

先明确需要区分什么，例如“连接未到达目标”与“目标收到连接但未响应”。已有授权、主机通道及接口绑定时，可按 [LINUX/packet-capture](../../commands/performance/linux.md)做限定采集；先确定接口、过滤条件、秒数和包数上限，与已有或一次获授权的复现对应。

**Constraints:** MUST 说明结果将如何改变判断。抓到 SYN 只证明到达采集位置；未抓到包还需排除接口、过滤条件和时间不匹配；抓到发出的响应不证明客户端收到。当前没有客户端 SSH/TCP 探测契约，需新模式时先补契约或取得现有证据，不临时编造命令冒充已有工具。

**Stop conditions:** 有区分结果即转步骤 6；条件不满足或本次检查没有新增区分证据时也转步骤 6，记录最有价值的下一步，不无界重试。

### 6. 输出结论和下一步

按[报告字段](../../report.md)列出范围、命令 ID、时间、关键结果及未覆盖检查，区分事实与候选解释，给出一个区分假设的检查或具体恢复建议。

**Constraints:** MUST 将“已定位边界”和“已恢复登录”分别表述。恢复后验证应对应原连接源、端点、端口及预期 SSH 登录能力；端口可连接不证明认证/会话恢复，没有复测时标记未验证。

**Stop conditions:** 已交付证据支持的边界、缺口及下一步后结束；新证据到来时从受影响步骤继续。
