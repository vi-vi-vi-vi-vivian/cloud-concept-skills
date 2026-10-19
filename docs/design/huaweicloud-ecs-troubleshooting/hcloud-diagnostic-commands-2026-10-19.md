# hcloud 诊断命令全景清单：ECS 及相关服务

核查日期：2026-10-19（北京时间）。本机 KooCLI：7.2.12。

范围围绕 ECS 主机及其网络、磁盘、镜像、备份、监控、日志、审计、安全、账号权限和费用依赖。本报告核实命令是否存在、关键参数与行为；当前账号是否已开通某服务、是否具有相应权限、目标区域是否支持，需要在实际诊断时确认。此次只获取 CLI 帮助和华为云官方元数据，没有运行主机诊断、抓包、扫描或远程脚本。

## 快速入口

下表是常用入口，后文为按服务分组的完整相关清单。操作都在 `rtk proxy hcloud` 后使用；参数由各操作的 `--help` 提供。

| 要定位的问题 | 首先查看的命令 |
|---|---|
| CLI 失败、选错账号/区域/项目 | `version`、`configure test`、`configure list`、`log show`；原命令加 `--debug` / `--dryrun`；`IAM KeystoneListRegions/v3`、`IAM KeystoneListProjects/v3` |
| 主机异常、启动失败、实例消失 | `ECS ShowServer`、`ECS ShowServerConsoleOutput`、`ECS ListScheduledEvents`、`ECS ShowJob`、`ECS ListRecycleBinServers` |
| CPU、内存、磁盘或网络负载 | `CES ListMetrics`、`CES ShowMetricData`、`CES BatchListMetricData`、`CES ListAgentStatus`、`CES ListAlarmHistories/v2` |
| 主机/应用报错、日志缺失 | `LTS ListLogs`、`LTS ListLogContext`、`LTS ListStructuredLogsWithTimeRange`、`LTS ListHost`、`LTS ListAccessConfig` |
| 谁重启/删除/改配置 | `CTS ListTraces`、`Config ShowResourceHistory`、`Config ShowResourceRelations` |
| SSH 或网络不通 | `ECS ListServerInterfaces`、`ECS NovaListServerSecurityGroups`、`VPC ShowPort/v3`、`VPC ListSecurityGroupRules/v3`、`VPC ShowRouteTable/v2`、`VPC ShowFirewall/v3` |
| 公网不通、速度受限 | `EIP ShowPublicip/v3`、`EIP ShowBandwidth/v2`、`Anti-DDoS ShowDDosStatus/v1`；有云防火墙时查 `CFW ListAccessControlLogs` / `ListFlowLogs` |
| 网站/域名/负载均衡异常 | `DNS ShowDomainDetection`、`ELB ShowLoadBalancerStatus/v3`、`ELB ListMembers/v3`、`ELB ShowHealthMonitor/v3`；已用 WAF 时查 `WAF ListEvent` / `ShowCompositeHost` |
| 挂盘、扩盘、备份失败 | `ECS ListServerBlockDevices`、`EVS ShowVolume`、`EVS ShowJob`、`CBR ListOpLogs`、`CBR ShowOpLog` |
| 漏洞、挖矿、异常登录、防护拦截 | `HSS ListHostStatus`、`HSS ListSecurityEvents`、`HSS ListHostVuls`、`HSS ListPorts`、`HSS ListBlockedIp` |
| 已有诊断结果、远程运维失败 | `COC ListDiagnosisTasks`、`COC ShowDiagnosisSummary`、`COC ShowDiagnosisNode`、`COC ListScriptJobs` |
| 资源到期、冻结、订单未完成 | `BSS ListPayPerUseCustomerResources`、`BSS ShowCustomerAccountBalances`、`BSS ListCustomerOrders` |
| 403、资源不可见、策略不生效 | IAM 授权查询、EPS 企业项目查询、`IAMAccessAnalyzer ValidatePolicy` |
| 应用慢、调用链异常、统一安全关联 | 已接入时使用 AOM、APM、SecMaster 的指标/调用链/事件查询 |

### 专门的诊断能力及影响

| 能力 | 命令 | 执行性质 |
|---|---|---|
| ECS GuestOS 自动诊断 | `COC CreateDiagnosisTask` → `ShowDiagnosisTask` / `ShowDiagnosisSummary` / `ShowDiagnosisNode` | 会安装 Holmes 插件并采集系统数据，需要 UniAgent、授权与受支持环境 |
| 公网域名诊断 | `DNS ShowDomainDetection` | GET；按域名/zone 查询诊断，站点/区域有要求 |
| ELB 后端配置诊断 | `ELB CreateMemberHealthCheckJob/v3` → `ShowMemberHealthCheckJob/v3` | 创建检测任务；检查后端配置、安全组及 ACL，目标必须是 ELB 后端 |
| 云防火墙抓包 | `CFW CreateCaptureTask` → `ListCaptureTask` / `ListCaptureResult` | 创建并执行抓包，需已有 CFW 和相应流量路径 |
| HSS 漏洞/基线/病毒检查 | `CreateVulnerabilityScanTask` / `RunBaselineDetect` / `CreateAntiVirusTask` | 发起扫描；部分功能/版本涉及收费，和读取已有结果分开 |
| 权限策略静态检查 | `IAMAccessAnalyzer ValidatePolicy` / `CheckNoNewAccess` | 校验输入策略，不修改现有授权；不能代替完整运行时鉴权 |
| HCS 全链路路径查询 | `HCSCLOUDNETDEBUG ShowFullLinkPaths` | HCS 条件适用，未验证普通公有云账号可用 |

行为以 API 的实际业务效果为准：POST 可以只是查询，GET 也可能触发扫描。控制台访问 URL、内核 dump、重启/重部署、创建流日志、安装 Agent、远程脚本和安全处置在后文分别标明。

### 适用于已确认主机的只读起点

下面只是命令示例，此次没有执行。固定 profile 和区域以减少作用域歧义。

```bash
rtk proxy hcloud ECS ShowServer --cli-profile=kekelogin --cli-region=cn-north-4 --project_id=0c6f6730795446b5988cd6d6a499f204 --server_id=9d9a77f3-23af-4ab0-a373-e183af605e2a
rtk proxy hcloud ECS ShowServerConsoleOutput --cli-profile=kekelogin --cli-region=cn-north-4 --project_id=0c6f6730795446b5988cd6d6a499f204 --server_id=9d9a77f3-23af-4ab0-a373-e183af605e2a --length=200
rtk proxy hcloud ECS ListServerInterfaces --cli-profile=kekelogin --cli-region=cn-north-4 --project_id=0c6f6730795446b5988cd6d6a499f204 --server_id=9d9a77f3-23af-4ab0-a373-e183af605e2a
rtk proxy hcloud ECS ListServerBlockDevices --cli-profile=kekelogin --cli-region=cn-north-4 --project_id=0c6f6730795446b5988cd6d6a499f204 --server_id=9d9a77f3-23af-4ab0-a373-e183af605e2a
rtk proxy hcloud CTS ListTraces --cli-profile=kekelogin --cli-region=cn-north-4 --trace_type=system --service_type=ECS --resource_id=9d9a77f3-23af-4ab0-a373-e183af605e2a --limit=200
```

## 如何使用这份清单

- 本机官方 `apis_cn.json` 中的 `Name`、`Versions`、`Suggests` 用于核对 operation 与用途；重点接口另查 operation 帮助和官方 API。CLI API组版本与 HTTP URI 里的版本号可能不同。
- 按接口的分页参数遍历结果，并保留查询时间、区域、项目、资源ID、request_id及原始 error_code/error_msg。空列表、权限拒绝、网络错误与服务不支持是不同结论。不要只用 CLI 的退出码判断是否成功。
- CES/LTS/HSS/APM 等只能查询已有采集数据；云平台资源状态与主机内的进程、文件系统、内核及应用状态需要结合分析。
- 下文的“查询”指读取现有状态/结果，并不承诺所有查询免费；计量型日志/安全分析以当前服务规则为准。需要新建检测、扫描或运行脚本时，按具体目标和影响另行选择。

## 详细清单导航

1. [CLI、账号、权限、企业项目、资源历史、费用与通知](#hcloud-自身权限资源历史费用及告警通知)
2. [ECS、EVS、IMS、CBR](#计算存储镜像与备份)
3. [网络及网站访问依赖](#网络及网站访问依赖)
4. [监控、日志、审计、运维和安全](#监控日志审计运维和安全)

## hcloud 自身、权限、资源历史、费用及告警通知

### CLI 本身

以下命令已用本机 KooCLI 7.2.12 帮助核实。`configure test` 只校验配置文件格式，不能证明 AK/SK 有效；认证应选择低权限只读 API 验证。

| 命令或选项 | 用途 | 性质 |
|---|---|---|
| `rtk proxy hcloud version` | 查本机版本 | 本地查询 |
| `rtk proxy hcloud --help` | 查服务及全局选项 | 帮助；可能获取远程元数据 |
| `rtk proxy hcloud ECS --help` | 查服务操作全集 | 同上 |
| `rtk proxy hcloud ECS ShowServer --help` | 查具体参数及 HTTP 方法 | 同上 |
| `rtk proxy hcloud configure list` | 查已有 profile、当前 profile、region | 本地查询，输出应保留脱敏 |
| `rtk proxy hcloud configure show --cli-profile=<profile>` | 查一个 profile | 本地查询 |
| `rtk proxy hcloud configure test` | 检查配置文件格式 | 本地校验 |
| `rtk proxy hcloud log show` | 查 CLI 日志配置 | 本地查询 |
| `rtk proxy hcloud log set --level=info` | 提高本地调用日志级别 | 修改本地配置，不是云日志检索 |
| `--debug` | 打印调用调试信息；附加到原始命令 | 原命令仍会执行 |
| `--dryrun` | 校验参数、显示将发送的请求，跳过目标 API | 预览；仍可能获取元数据或项目资料 |
| `--skeleton` | 生成 JSON 入参骨架 | 参数准备 |
| `--cli-profile`、`--cli-region`、`--cli-project-id`、`--project_id` | 固定账号、区域、IAM 项目，排除查错位置 | 请求作用域；`project_id` 是否存在以操作帮助为准 |
| `--cli-domain-id`、`--cli-x-project-id` | 诊断全局账号、显式鉴权项目问题 | 是否需要以 API 为准 |
| `--cli-endpoint` | 明确目标端点，排除端点选择问题 | 仅使用官方公布端点 |
| `--cli-connect-timeout`、`--cli-read-timeout`、`--cli-retry-count` | 诊断连接/I/O超时、瞬时网络错误 | 取值范围见帮助；重试不能修复403 |
| `--cli-query`、`--cli-output=json/table/tsv` | 只取相关字段、区分业务错误对象与资源列表 | 展示选项，不会减少目标API返回的数据 |
| `--cli-waiter` | 轮询任务/资源状态 | 会持续调用原API，只宜配合只读操作 |
| `rtk proxy hcloud meta download` | 更新离线元数据包 | 下载并改变本地缓存 |
| `rtk proxy hcloud meta clear` | 排除过期/损坏元数据 | 清理本地缓存，后续需重新获取 |
| `rtk proxy hcloud update` | 升级CLI以排除旧版本兼容性问题 | 改变本机安装版本 |

本机默认日志位置是 `/Users/agentcodex7/.hcloud/log/`。共享 debug、console、日志或诊断报告前，去除令牌、密码、业务数据及无需公开的标识。没有必要通过关闭 TLS 校验来处理普通网络故障。

来源：[配置命令](https://support.huaweicloud.com/usermanual-hcli/hcli_03_001.html)、[dryrun](https://support.huaweicloud.com/usermanual-hcli/hcli_05_14.html)、[CLI日志](https://support.huaweicloud.com/intl/zh-cn/usermanual-hcli/hcli_04_006.html)及本机 `hcloud --help`。

### 账号、项目与权限

查不到实例或报403时，先确认 profile、区域、IAM项目、企业项目、策略范围。IAM v3 的用户组/角色策略与新版 v5 身份策略应按账号实际使用模式选择，不能只检查其中一种就断言权限完整。

### IAM：身份、区域、项目及授权

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `IAM KeystoneListRegions/v3` | 查询区域列表 |
| `IAM KeystoneListProjects/v3` | 查询指定条件下的项目列表 |
| `IAM KeystoneListAuthProjects/v3` | 查询IAM用户可以访问的项目列表 |
| `IAM KeystoneListAuthDomains/v3` | 查询IAM用户可以访问的账号详情 |
| `IAM KeystoneListProjectsForUser/v3` | 查询指定IAM用户的项目列表 |
| `IAM KeystoneShowProject/v3` | 查询项目详情 |
| `IAM ShowProjectDetailsAndStatus/v3` | 查询项目详情与状态 |
| `IAM KeystoneListGroupsForUser/v3` | 查询IAM用户所属用户组 |
| `IAM KeystoneListAllProjectPermissionsForGroup/v3` | 查询用户组的所有项目权限列表 |
| `IAM KeystoneListProjectPermissionsForGroup/v3` | 查询项目服务中的用户组权限 |
| `IAM KeystoneListDomainPermissionsForGroup/v3` | 查询全局服务中的用户组权限 |
| `IAM ShowDomainRoleAssignments/v3` | 查询指定账号中的授权记录 |
| `IAM ListCustomPolicies/v3` | 查询自定义策略列表 |
| `IAM ShowCustomPolicy/v3` | 查询自定义策略详情 |
| `IAM ListAgencies/v3` | 查询指定条件下的委托列表 |
| `IAM ShowAgency/v3` | 查询委托详情 |
| `IAM ListAllProjectsPermissionsForAgency/v3` | 查询委托下的所有项目服务权限列表 |
| `IAM ListProjectPermissionsForAgency/v3` | 查询项目服务中的委托权限 |
| `IAM ListDomainPermissionsForAgency/v3` | 查询全局服务中的委托权限 |
| `IAM ListEnterpriseProjectsForUser/v3` | 查询用户直接关联的企业项目 |
| `IAM ListRolesForUserOnEnterpriseProject/v3` | 查询企业项目直接关联用户的权限 |
| `IAM ShowDomainApiAclPolicy/v3` | 查询账号接口访问策略 |
| `IAM ShowDomainConsoleAclPolicy/v3` | 查询账号控制台访问策略 |
| `IAM ShowUser/v3` | 查询IAM用户详情(推荐) |
| `IAM ShowUserLoginProtect/v3` | 查询指定IAM用户的登录保护状态信息 |
| `IAM ListPermanentAccessKeys/v3` | 查询所有永久访问密钥 |
| `IAM ShowPermanentAccessKey/v3` | 查询指定永久访问密钥 |
| `IAM ShowDomainQuota/v3` | 查询账号配额 |
| `IAM ShowProjectQuota/v3` | 查询项目配额 |
| `IAM KeystoneListServices/v3` | 查询服务列表 |
| `IAM KeystoneListEndpoints/v3` | 查询终端节点列表 |
| `IAM KeystoneShowCatalog/v3` | 查询服务目录 |
| `IAM GetAccountSummaryV5/v5` | 获取此账号中IAM实体使用情况和IAM配额的摘要信息 |
| `IAM GetFeatureStatusV5/v5` | 获取此账号的功能状态 |
| `IAM ShowUserV5/v5` | 查询IAM用户详情 |
| `IAM ListAttachedUserPoliciesV5/v5` | 查询指定IAM用户附加的所有身份策略 |
| `IAM ListAttachedGroupPoliciesV5/v5` | 查询指定用户组附加的所有身份策略 |
| `IAM ListAttachedAgencyPoliciesV5/v5` | 查询指定委托或信任委托附加的所有身份策略 |
| `IAM GetPolicyV5/v5` | 通过身份策略ID获取身份策略 |
| `IAM GetPolicyVersionV5/v5` | 查询指定身份策略版本 |
| `IAM ShowAccessKeyLastUsedV5/v5` | 查询指定永久访问密钥最后使用时间 |

### IAMAccessAnalyzer：访问分析与策略静态校验

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `IAMAccessAnalyzer ListAnalyzers` | 检索分析器的列表 |
| `IAMAccessAnalyzer ShowAnalyzer` | 显示指定的分析器 |
| `IAMAccessAnalyzer ListFindings` | 检索指定分析器生成的访问分析结果列表 |
| `IAMAccessAnalyzer ShowFinding` | 检索有关指定结果的信息 |
| `IAMAccessAnalyzer ListAccessPreviews` | 获取所有访问预览 |
| `IAMAccessAnalyzer ShowAccessPreview` | 获取相关访问预览的信息 |
| `IAMAccessAnalyzer ListAccessPreviewFindings` | 获取相关预览生成的分析结果 |
| `IAMAccessAnalyzer ListArchiveRules` | 检索为指定分析器创建的存档规则的列表 |
| `IAMAccessAnalyzer ShowArchiveRule` | 检索有关存档规则的信息 |
| `IAMAccessAnalyzer ListResourceConfigurations` | 列举资源分析配置 |
| `IAMAccessAnalyzer ListNotificationSettings` | 获取消息通知配置列表 |
| `IAMAccessAnalyzer ShowNotificationSetting` | 获取消息通知配置 |
| `IAMAccessAnalyzer ValidatePolicy` | 校验策略 |
| `IAMAccessAnalyzer CheckNoNewAccess` | 校验策略是否有新访问权限 |

`ValidatePolicy` 和 `CheckNoNewAccess` 通过 POST 执行静态策略校验，不会修改用户策略；也不能替代对某个具体 API 请求的完整运行时鉴权判断。`CreateAccessPreview`、`StartResourceScan` 会创建分析活动/触发扫描，单独评估后再运行。来源：[官方策略校验 API](https://support.huaweicloud.com/intl/en-us/api-iam5/ValidatePolicy.html)、[策略校验目录](https://support.huaweicloud.com/api-iam5/topic_300000005.html)。

### EPS：企业项目与资源归属

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `EPS ListEnterpriseProject` | 查询企业项目列表 |
| `EPS ShowEnterpriseProject` | 查询企业项目详情 |
| `EPS ShowResourceBindEnterpriseProject` | 查询企业项目绑定的资源列表 |
| `EPS ShowAssociatedResources` | 查询关联资源 |
| `EPS ListMigrationRecord` | 查询资源迁移记录 |
| `EPS ShowEnterpriseProjectQuota` | 查询企业项目配额 |
| `EPS ListResourceMapping` | 查询资源类型映射 |
| `EPS ListProviders` | 查询企业项目支持的服务 |

### Config / RMS：资源历史、关系与合规

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `Config ListAllResources` | 列举所有资源 |
| `Config ListResources` | 列举指定类型的资源 |
| `Config ListRegions` | 查询用户可见的区域 |
| `Config ShowResourceById` | 查询单个资源 |
| `Config ShowResourceDetail` | 查询帐号下的单个资源 |
| `Config ShowResourceHistory` | 查询资源历史 |
| `Config ShowResourceRelations` | 列举资源关系 |
| `Config ShowResourceRelationsDetail` | 列举资源关系详情 |
| `Config ShowTrackerConfig` | 查询记录器 |
| `Config ListTrackedResources` | 列举资源记录器收集的全部资源 |
| `Config ShowTrackedResourceDetail` | 查询资源记录器收集的单个资源 |
| `Config ListPolicyAssignments` | 列出合规规则 |
| `Config ListPolicyStatesByResourceId` | 获取资源的合规结果 |
| `Config ShowEvaluationStateByAssignmentId` | 获取规则的评估状态 |
| `Config ShowConfigurationAggregatorSourcesStatus` | 查询指定资源聚合器聚合帐号的状态信息 |
| `Config ShowRemediationConfiguration` | 查询修正配置 |
| `Config ListRemediationExecutionStatuses` | 查询修正执行结果 |

本机 `RMS` 和 `Config` 同时提供上表多数基础资源查询；以各自 `--help` 为准。RMS 不具有上表中 `ListTrackedResources`、`ShowTrackedResourceDetail`、`ShowRemediationConfiguration`、`ListRemediationExecutionStatuses` 四项。资源历史需要已有记录器和实际采集记录，不能追溯采集前的数据。

### BSS：到期、冻结、订单、余额与消费

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `BSS ShowCustomerAccountBalances` | 查询账户余额 |
| `BSS ListCustomerOrders` | 查询订单列表 |
| `BSS ShowCustomerOrderDetails` | 查询订单详情 |
| `BSS ListPayPerUseCustomerResources` | 查询客户包年/包月资源列表 |
| `BSS ListCustomerOnDemandResources` | 查询客户按需资源列表 |
| `BSS ListCustomerBillsFeeRecords` | 查询流水账单 |
| `BSS ListCustomerBillsMonthlyBreakDown` | 查询月度成本 |
| `BSS ListCustomerselfResourceRecords` | 查询资源消费记录 |
| `BSS ListCustomerselfResourceRecordDetails` | 查询资源详单 |
| `BSS ShowCustomerMonthlySum` | 查询汇总账单 |
| `BSS ListCosts` | 查询成本数据 |
| `BSS ListFreeResourceInfos` | 查询资源包列表 |
| `BSS ListFreeResourceUsages` | 查询资源包使用量 |
| `BSS ListFreeResourcesUsageRecords` | 查询资源包使用明细 |
| `BSS ShowRealNameAuthStatus` | 查询实名认证状态 |

注意反直觉的命名：`ListPayPerUseCustomerResources` 在本机官方元数据中指“包年/包月资源列表”，可查过期时间/冻结状态；按需资源是 `ListCustomerOnDemandResources`。ECS ListServersDetails 本身不返回包年包月到期时间。`ShowRealNameAuthStatus` 仅与账号开通/购买限制有关。来源：[客户包年包月资源 API](https://support.huaweicloud.com/api-oce/api_order_00021.html)、[ECS查询约束](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0094148850.html)。

### SMN：告警通知未送达

| 操作（均在 `hcloud` 后） | 诊断用途 |
|---|---|
| `SMN ListTopics` | 查询主题列表 |
| `SMN ListTopicDetails` | 查询主题详情 |
| `SMN ListTopicAttributes` | 查询主题策略 |
| `SMN ListSubscriptions` | 查询订阅者列表 |
| `SMN ListSubscriptionsByTopic` | 查询指定Topic的订阅者列表 |
| `SMN ListTopicMessageStatistics` | 查询主题的发送详情 |
| `SMN ListTopicsWithAssociatedResources` | 查询主题列表及主题关联资源信息 |
| `SMN ShowNotifyPolicy` | 查询通知策略 |
| `SMN ListLogtank` | 查询云日志 |
| `SMN ShowHttpDetectResult` | 获取http探测结果 |

`ShowHttpDetectResult` 只读已有 HTTP 探测结果，需 topic_urn/task_id；`PublishHttpDetect` 会向终端发布实际探测消息，不是无副作用的读取。`PublishMessage` 是发送消息，也不应在普通巡检中自动运行。


## 计算、存储、镜像与备份


### 核实范围与来源

只运行了 service/operation 的 `--help`，读取 CLI 官方元数据缓存，以及查询华为云官方文档；未调用云资源 API、未读取凭据。操作名以本机 CLI 与缓存为准。参数示例已对照相应 operation 的帮助核实，未执行示例。

本机元数据目录为 `~/.hcloud/metaRepo/template/{ecs,evs,ims,cbr}/`。其中 `apis_cn.json` 给出真实 operation 名称、版本、中文说明；已获取帮助的 `<Operation>_cn.yaml` 实际为 JSON，给出 HTTP method、URI、参数。下文“CLI API组版本”是该元数据中的版本，ECS/EVS/IMS 为 v2，CBR 为 v1；它与 URI 中的 /v1、/v2.1、/v3 不应混为一谈。

官方交叉来源：[ECS CLI 命令参考](https://support.huaweicloud.com/clir-ecs/ecs_cli_02.html)、[CBR CLI 命令参考](https://support.huaweicloud.com/intl/en-us/clir-cbr/cbr_cli_02.html)。

### ECS：主机状态、启动失败、挂载与配置

下表全部 operation 存在于本机 `hcloud ECS --help`，CLI API组均为 v2。标为“查询”的用途来自本机官方说明，具体参数用 `rtk proxy hcloud ECS <Operation> --help` 查看；对 Nova 历史接口优先采用 ECS 同类接口。

| 场景 | 查询 operation | 作用与选用 |
|---|---|---|
| 实例清单、状态、冻结、计费 | `ListCloudServers`、`ListServersDetails`、`ShowServer` | 查状态、配置、地址、规格、镜像、磁盘等；ShowServer/ListServersDetails 明确支持计费方式和冻结信息 |
| 原生实例查询补充 | `NovaListServers`、`NovaListServersDetails`、`NovaShowServer` | OpenStack Nova 同类接口 |
| 启动失败、内核异常 | `ShowServerConsoleOutput` | GET /v1/{project_id}/cloudservers/{server_id}/console-output；默认 50 行，--length=-1 表示不限输出行数 |
| 最近操作行为 | `NovaListServerActions`、`NovaShowServerAction` | 列表取 request_id 后查单条行为；官方将其列入历史废弃 API，作为补充，操作者审计应结合 CTS |
| 底层维护与计划事件 | `ListScheduledEvents` | GET /v3/{project_id}/instance-scheduled-events；本机帮助说明支持查看过去 7 天；按 --instance_id.1 过滤 |
| 异步任务失败 | `ShowJob` | 按 --job_id 查创建、删除、批量操作及网卡操作等任务状态 |
| 网卡挂载 | `ListServerInterfaces`、`NovaListServerInterfaces`、`NovaShowServerInterface` | 关联 port_id、IP、MAC 等，再转 VPC 排查 |
| 主机安全组关联 | `NovaListServerSecurityGroups` | 确认主机绑定哪些安全组，规则本身转 VPC 查询 |
| 磁盘挂载 | `ListServerBlockDevices`、`ShowServerBlockDevice`、`ListServerVolumeAttachments`、`NovaListServerVolumes`、`NovaShowServerVolume` | 获取 volume_id、系统/数据盘挂载关系，再转 EVS 查盘状态 |
| 元数据、IMDS | `ShowMetadataOptions`、`NovaShowServerMetadata`、`NovaShowServerMetadataItem` | 前者查 IMDS 配置；后两者查用户元数据及指定 key |
| 密钥配置和重置能力 | `NovaListKeypairs`、`NovaShowKeypair`、`ShowResetPasswordFlag` | 查 SSH 密钥记录或是否支持一键重置；不返回/重置登录密码作为常规诊断 |
| 项目/实例配额 | `ShowServerLimits`、`ShowServerAttachableNicNum`、`ShowAppendableVolumeQuota` | 项目配额、还可挂载网卡、包周期主机可追加磁盘数 |
| 规格/AZ/资源容量 | `ListFlavors`、`ListFlavorSellPolicies`、`ListResizeFlavors`、`ShowFlavorCapacity`、`ListServerAzInfo`、`NovaListAvailabilityZones` | 调度失败、规格售罄、AZ 与变更规格可用性 |
| 原生规格查询 | `NovaListFlavors`、`NovaListFlavorsDetails`、`NovaShowFlavor`、`NovaShowFlavorExtraSpecs` | 规格与 extra_specs 补充 |
| 亲和/反亲和组 | `ListServerGroups`、`ShowServerGroup`、`NovaListServerGroups`、`NovaShowServerGroup` | 组成员/策略用于调度问题 |
| 模板差异 | `ListTemplates`、`ListLaunchTemplateVersions` | 批量部署配置排查 |
| 资源归属/筛选 | `ListServerTags`、`ShowServerTags` | 项目标签、实例标签 |
| 删除/回收站 | `ListRecycleBinServers`、`ShowRecycleBin` | 主机“消失”时确认回收站及其配置 |
| 服务版本 | `NovaListVersions`、`NovaShowVersion` | API endpoint 的版本支持信息 |

[ShowServer 官方 API](https://support.huaweicloud.com/api-ecs/ecs_02_0104.html) 确认详情查询包含计费/冻结信息；[计划事件 API](https://support.huaweicloud.com/api-ecs/ecs_02_2201.html) 确认 URI 为 /v3；[历史动作 API](https://support.huaweicloud.com/intl/zh-cn/api-ecs/ecs_03_1501.html) 明确标注废弃。

控制台日志可用于开机、关机、重启定位；官方用户指南说明 Windows 不支持此功能、系统最多保存 100 KB、管理控制台可获取一个小时内的日志。日志缺失也可能需要操作系统启动参数支持。[获取控制台日志](https://support.huaweicloud.com/usermanual-ecs/ecs_03_0154.html)

#### ECS 已核实参数示例（只读）

以下使用此前已确认主机所在区域 cn-north-4 与配置 kekelogin，ID 需替换成真实 UUID。所有涉及项目的命令可加 `--project_id='<PROJECT_ID>'` 消除项目推断歧义。

```bash
rtk proxy hcloud ECS ListServersDetails --cli-profile=kekelogin --cli-region=cn-north-4 --name=hcss_ecs_a68a
rtk proxy hcloud ECS ShowServer --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS ShowServerConsoleOutput --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>' --length=200
rtk proxy hcloud ECS NovaListServerActions --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS NovaShowServerAction --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>' --request_id='<REQUEST_ID>'
rtk proxy hcloud ECS ListScheduledEvents --cli-profile=kekelogin --cli-region=cn-north-4 --instance_id.1='<ECS_ID>'
rtk proxy hcloud ECS ShowJob --cli-profile=kekelogin --cli-region=cn-north-4 --job_id='<JOB_ID>'
rtk proxy hcloud ECS ListServerInterfaces --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS NovaListServerSecurityGroups --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS ListServerBlockDevices --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS ShowMetadataOptions --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS ShowResetPasswordFlag --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud ECS ShowServerLimits --cli-profile=kekelogin --cli-region=cn-north-4
```

`ListCloudServers` 默认 limit=10，最大100；`ListServersDetails` 默认25、最大1000，两者都有 marker，完整盘点应翻页。企业项目范围也影响可见性，后者支持 --enterprise_project_id=all_granted_eps。

#### ECS 中与诊断相关、但应单独执行的操作

| 类别 | operation | 核实结论 |
|---|---|---|
| 生成控制台访问链接 | `ShowServerRemoteConsole` | POST，需 --server_id、--remote_console.protocol=vnc、--remote_console.type=novnc；不是普通 GET 查询，返回可登录 URL，应按访问凭证保管 |
| 生成串口访问链接 | `ShowSerialConsoleActions` | POST，需 --server_id；获取串口登录地址，启用串口本身另有写操作 |
| 开启/关闭串口 | `UpdateSerialConsoleOptions` | 写入配置，不能混入只读体检 |
| 采集内核现场 | `ExecuteServerDump` | POST 触发内核 dump，官方权限是 write；具有中断风险，不能当成读取已有日志 |
| 注册监控采集 | `RegisterServerMonitor` | POST 加入监控表，参数 --server_id、--monitorMetrics；帮助说明会被周期采集平台版本、CPU、内存、网卡、磁盘等；不是读取 CES 指标 |
| 重部署 | `ExecuteServerRedeploy` | POST 写操作并返回 job_id，属于修复步骤 |
| 计划事件授权/调整 | `AcceptScheduledEvent`、`UpdateScheduledEvent` | 授权执行维护或修改计划事件时间，非查询 |
| 重启/启停/迁移/改规格 | `BatchRebootServers`、`BatchStartServers`、`BatchStopServers`、`NovaRebootServer`、`NovaStartServer`、`NovaStopServer`、`MigrateServer`、`ResizeServer`、`ResizePostPaidServer`、`BatchResizeServers` | 修复或变更，可能中断业务、改变费用 |
| 密码、系统与挂载修复 | `ResetServerPassword`、`BatchResetServersPassword`、`ReinstallServerWithCloudInit`、`ReinstallServerWithoutCloudInit`、`ChangeServerOsWithCloudInit`、`ChangeServerOsWithoutCloudInit`、挂载/卸载网卡和磁盘、修改安全组或元数据配置 | 都属于改变资源的操作 |
| 返回密码 | `ShowServerPassword` | 名称确实存在，但涉及敏感登录数据，不列为常规诊断步骤 |

官方约束：ExecuteServerDump 不支持鲲鹏 CPU，允许状态为 ACTIVE、PAUSED、RESCUED、RESIZED、ERROR。[内核 dump API](https://support.huaweicloud.com/api-ecs/ecs_02_2502.html)；[重部署 API](https://support.huaweicloud.com/api-ecs/ecs_02_2501.html)；[VNC URL API](https://support.huaweicloud.com/api-ecs/ecs_02_0208.html)；[串口 URL API](https://support.huaweicloud.com/api-ecs/ecs_02_2102.html)。

### EVS：盘异常、挂载失败、快照和容量（CLI API组 v2）

| 场景 | 查询 operation |
|---|---|
| 盘状态、大小、类型、加密和挂载关系 | `ListVolumes`、`ShowVolume` |
| 创建、扩容、删除异步失败 | `ShowJob` |
| 快照存在性、状态与源卷 | `ListSnapshots`、`ShowSnapshot` |
| 租户配额 | `CinderListQuotas` |
| AZ 与卷类型 | `CinderListAvailabilityZones`、`CinderListVolumeTypes` |
| 回收站 | `ListVolumesInRecycle`、`ShowVolumeInRecycle`、`ShowRecyclePolicy` |
| 盘归属、标签筛选 | `ListVolumesByTags`、`ListVolumeTags`、`ShowVolumeTags` |
| 过户记录 | `CinderListVolumeTransfers`、`CinderShowVolumeTransfer` |
| 服务 API 版本 | `ListVersions`、`ShowVersion` |

以上操作名、用途由本机 EVS --help 与官方缓存核实。重点示例的参数全部核实：

```bash
rtk proxy hcloud EVS ListVolumes --cli-profile=kekelogin --cli-region=cn-north-4 --server_id='<ECS_ID>'
rtk proxy hcloud EVS ShowVolume --cli-profile=kekelogin --cli-region=cn-north-4 --volume_id='<VOLUME_ID>'
rtk proxy hcloud EVS ListSnapshots --cli-profile=kekelogin --cli-region=cn-north-4 --volume_id='<VOLUME_ID>'
rtk proxy hcloud EVS ShowSnapshot --cli-profile=kekelogin --cli-region=cn-north-4 --snapshot_id='<SNAPSHOT_ID>'
rtk proxy hcloud EVS ShowJob --cli-profile=kekelogin --cli-region=cn-north-4 --job_id='<JOB_ID>'
rtk proxy hcloud EVS CinderListQuotas --cli-profile=kekelogin --cli-region=cn-north-4 --project_id='<PROJECT_ID>' --target_project_id='<PROJECT_ID>' --usage=true
```

`CinderListQuotas` 的 target_project_id 要与 project_id 一致，usage 当前只支持 true。ListVolumes 默认1000条，支持 limit、marker、offset，分页以帮助为准。盘查询只能看到云平台状态，不能代替操作系统内的文件系统、分区、挂载和 I/O 诊断；此为接口能力范围的推断。

`CreateSnapshot` 是创建新快照；`RollbackSnapshot` 会回滚数据；`ResizeVolume`、`BatchResizeVolumes`、`RetypeVolume`、`ModifyVolumeQoS`、删除/恢复回收站等均为资源变更，不能混入只读查询。云硬盘状态的官方取值见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。

### IMS：启动镜像、共享权限与镜像异步任务（CLI API组 v2）

| 场景 | 查询 operation |
|---|---|
| 镜像状态、架构、磁盘/内存最低要求与规格兼容 | `ListImages`、`GlanceShowImage`；原生列表补充 `GlanceListImages` |
| 支持操作系统 | `ListOsVersions` |
| 镜像导入、导出、复制、创建任务 | `ShowJob`、`ShowJobProgress` |
| 镜像配额 | `ShowImageQuota` |
| 共享和成员状态 | `ListImageMembers`、`ShowImageMember`、`GlanceListImageMembers`、`GlanceShowImageMember` |
| 标签及筛选 | `ListImageByTags`、`ListImagesTags`、`ListImageTags`、`ListTags` |
| Schema、版本补充 | `GlanceListImageMemberSchemas`、`GlanceListImageSchemas`、`GlanceShowImageMemberSchemas`、`GlanceShowImageSchemas`、`ListVersions`、`ShowVersion` |

来源：本机 IMS --help 与官方缓存。实际参数已核实：

```bash
rtk proxy hcloud IMS GlanceShowImage --cli-profile=kekelogin --cli-region=cn-north-4 --image_id='<IMAGE_ID>'
rtk proxy hcloud IMS ListImages --cli-profile=kekelogin --cli-region=cn-north-4 --id='<IMAGE_ID>'
rtk proxy hcloud IMS ListImages --cli-profile=kekelogin --cli-region=cn-north-4 --__imagetype=gold --flavor_id=t7.large.1 --status=active
rtk proxy hcloud IMS ShowJob --cli-profile=kekelogin --cli-region=cn-north-4 --job_id='<JOB_ID>'
rtk proxy hcloud IMS ShowJobProgress --cli-profile=kekelogin --cli-region=cn-north-4 --job_id='<JOB_ID>'
```

ListImages 支持 --architecture=x86/arm、--__os_type=Linux/Windows/Other、--visibility、--member_status、--status，默认 limit=500、以 marker 翻页。帮助解释状态 queued/saving/deleted/killed/active；镜像操作名称存在并不代表当前账号/区域有权限。

`CreateImage*`、`CreateWholeImage`、`CopyImage*`、`ExportImage*`、`ImportImageQuick*`、`RegisterImage`、`UpdateImage`、`GlanceUpdateImage`、成员接受/拒绝/添加/删除等是任务创建或配置变更；重装或切换 ECS 系统更不是只读诊断。

### CBR：备份失败、恢复能力、策略和存储库（CLI API组 v1）

| 场景 | 查询 operation |
|---|---|
| 主机/卷备份是否存在、备份状态 | `ListBackups`、`ShowBackup` |
| 备份/恢复/复制任务失败 | `ListOpLogs`、`ShowOpLog` |
| 还原点与备份元数据 | `ShowCheckpoint`、`ShowMetadata` |
| 存储库绑定、状态、容量 | `ListVault`、`ShowVault`、`ShowSummary`、`ShowStorageUsage` |
| 备份策略 | `ListPolicies`、`ShowPolicy` |
| 资源可保护性 | `ListProtectable`、`ShowProtectable` |
| 文件备份客户端 | `ListAgent`、`ShowAgent` |
| 备份共享成员 | `ShowMemberDetail`、`ShowMembersDetail` |
| 跨区域复制、服务特性 | `ListExternalVault`、`ShowReplicationCapabilities`、`ListFeatures`、`ShowFeature` |
| 组织策略部署 | `ListOrganizationPolicies`、`ListOrganizationPolicyDetail`、`ShowOrganizationPolicy` |
| 迁移与范围 | `ShowMigrateStatus`、`ListProjects`、`ListDomainProjects`、`ShowDomain`（后者为控制台内部接口，非首选） |
| 标签筛选 | `ShowVaultProjectTag`、`ShowVaultResourceInstances`、`ShowVaultTag` |

操作名与用途均由本机 CBR --help/元数据核实，官方对照可见[CBR CLI 参考](https://support.huaweicloud.com/intl/en-us/clir-cbr/cbr_cli_02.html)。重点参数示例核实：

```bash
rtk proxy hcloud CBR ListBackups --cli-profile=kekelogin --cli-region=cn-north-4 --resource_id='<ECS_ID>' --resource_type='OS::Nova::Server'
rtk proxy hcloud CBR ShowBackup --cli-profile=kekelogin --cli-region=cn-north-4 --backup_id='<BACKUP_ID>'
rtk proxy hcloud CBR ListOpLogs --cli-profile=kekelogin --cli-region=cn-north-4 --resource_id='<ECS_ID>' --status=failed
rtk proxy hcloud CBR ShowOpLog --cli-profile=kekelogin --cli-region=cn-north-4 --operation_log_id='<OPERATION_LOG_ID>'
rtk proxy hcloud CBR ListVault --cli-profile=kekelogin --cli-region=cn-north-4 --resource_ids='<ECS_ID>'
rtk proxy hcloud CBR ShowCheckpoint --cli-profile=kekelogin --cli-region=cn-north-4 --checkpoint_id='<CHECKPOINT_ID>'
rtk proxy hcloud CBR ListProtectable --cli-profile=kekelogin --cli-region=cn-north-4 --protectable_type=server --id='<ECS_ID>'
rtk proxy hcloud CBR ShowProtectable --cli-profile=kekelogin --cli-region=cn-north-4 --protectable_type=server --instance_id='<ECS_ID>'
rtk proxy hcloud CBR ShowSummary --cli-profile=kekelogin --cli-region=cn-north-4
rtk proxy hcloud CBR ShowStorageUsage --cli-profile=kekelogin --cli-region=cn-north-4 --resource_id='<ECS_ID>'
```

`ListBackups` 可按 --vault_id、--checkpoint_id、--status、--start_time/--end_time 过滤，支持 marker/offset/limit；`ListOpLogs` 可按 --operation_type=backup/copy/replication/delete/restore 等、--status=success/skipped/failed/running/timeout/waiting 过滤。

`CheckAgent` 是 **POST 主动检查应用一致性 Agent 状态**，不是 ListAgent/ShowAgent 的客户端 GET 查询。其参数已核实为 --agent_status.1.resource_id、--agent_status.1.resource_type='OS::Nova::Server'，不自动执行。

`CreateCheckpoint` 会创建备份还原点，`RestoreBackup` 会恢复数据，`CopyBackup`/`CopyCheckpoint` 创建复制任务，`RegisterAgent`/`UpdateAgent`/`UnregisterAgent`、策略/存储库修改都会改变服务状态。尤其 DeleteVault 会清除库中备份，不能作为诊断清理步骤。

### 执行与解释边界

1. 本文验证了命令与参数能力，没有证明用户当前 IAM 权限足以调用全部接口；地域、企业项目、服务开通范围都会影响结果。
2. CLI 官方元数据中的“v2/v1”只表明命令所属 API组，某些 ECS URI 实际为 /v1、/v2.1、/v3。不要靠名称或版本数字猜 HTTP 路径。
3. “Show/List”不等于普通只读 GET：VNC/串口 URL 为 POST，标签筛选也可能以 POST 承载查询。应依具体 method 和业务效果判断。
4. `--help` 可能联网到 API Explorer 获取帮助元数据。此次曾遇到 API Explorer 的 `APIGW.0308`（同 IP 5 次/5 秒）与沙箱 DNS 失败；这是帮助元数据访问问题，不能据此断言 ECS 资源异常。后续优先本地缓存。
5. 若要“完整诊断 ECS”，这些管理 API 仍需配合 CES 指标、CTS 审计、VPC/EIP 路由与规则、LTS/HSS，以及主机内 OS/应用日志；这是从各接口能力边界得出的排障组合建议。


## 网络及网站访问依赖


核查日期：2026-10-19。范围是 ECS 的网络及网站访问依赖组件；仅获取本机 CLI 帮助和官方元数据，未查询真实云资源、未读取凭据、未创建诊断任务。

### 核心结论

- 对普通 ECS 网络，最直接的是 `VPC` 的安全组/端口/子网/路由/网络 ACL，`EIP` 的公网绑定和带宽，以及 `Anti-DDoS ShowDDosStatus` 的清洗/黑洞状态。
- 真正的专用诊断 API 存在：`DNS ShowDomainDetection` 是 GET 查询域名诊断；`ELB CreateMemberHealthCheckJob` 是 POST 创建后端配置/安全组/ACL检查任务，之后用 `ShowMemberHealthCheckJob` 获取结果。后者需要 ELB 后端 member，不能直接对任意 ECS 使用。[DNS诊断](https://support.huaweicloud.com/api-dns/ShowDomainDetection.html)、[ELB CLI 参考](https://support.huaweicloud.com/clir-elb/elb-cli_v3.html)
- `CFW CreateCaptureTask` 会创建并执行抓包任务，不是只读查询；已存在任务可用 `ListCaptureTask`、`ListCaptureResult` 查询。[CFW抓包](https://support.huaweicloud.com/api-cfw/CreateCaptureTask.html)
- `HCSCLOUDNETDEBUG` 的确有 `ShowFullLinkPaths`（POST 全链路虚拟路径查询）、`ListFlowPaths`（GET 获取业务流监控的端到端路径）。不过 API Explorer 将网络诊断工具列在 HCS 产品类别；本次没有证据证明普通公有云 ECS 账户可用，不能把它当作公有云通用连通性分析 API。[API Explorer产品分类](https://console.huaweicloud.com/apiexplorer/?region=cn-north-4)
- 本次核实的 VPC/EIP/ER/NAT 等服务命令未发现通用 `ping`、`traceroute` 或面向任意 ECS 的自动路径分析 API。普通资源查询能检查控制面配置；并不证明操作系统端口、进程或实际数据面端到端可达。

### 使用与证据

以下每行是“诊断主题 → 可用操作”。命令用法为 `hcloud <服务> <操作> --cli-region=<区域> <参数>`，追加 `--help` 查看必填参数。多版本命令显式写为 `/v2`、`/v3`；其他操作也按元数据标出版本，避免默认版本歧义。

清单来自各服务实际 `hcloud <Service> --help` 与本机官方帮助缓存 `~/.hcloud/metaRepo/template/<service>/apis_cn.json` 的 `Name / Versions / Suggests`。对重要诊断命令另执行了 `<operation> --help`，核实 HTTP 方法与参数。下表不把建立流日志、改变规则、防护开关、重启等动作混入已有状态查询。

流日志部分：VPC/ER 的 `ListFlowLogs`、`ShowFlowLog` 查询流日志资源/配置；并非读取完整流量日志内容。日志内容应在其已配置的 LTS 日志流查询。CFW 的同名 `ListFlowLogs` 则是查询流日志内容（本机中文帮助已核实）。

### 按 ECS 依赖分类的查询清单

#### VPC

| 诊断主题 | 实际操作 |
|---|---|
| 安全组及地址组 | `ListSecurityGroups/v3`, `ListSecurityGroups/v2`, `ShowSecurityGroup/v3`, `ShowSecurityGroup/v2`, `ListSecurityGroupRules/v3`, `ListSecurityGroupRules/v2`, `ShowSecurityGroupRule/v3`, `ShowSecurityGroupRule/v2`, `ListAddressGroup/v3`, `ShowAddressGroup/v3`, `ListAddressGroupsDependency/v3` |
| 网卡、IP和子网 | `ListPorts/v3`, `ListPorts/v2`, `ShowPort/v3`, `ShowPort/v2`, `ListSubNetworkInterfaces/v3`, `ShowSubNetworkInterface/v3`, `ShowSubNetworkInterfacesQuantity/v3`, `ListPrivateips/v2`, `ShowPrivateip/v2`, `ListSubnets/v2`, `ShowSubnet/v2`, `ListVirsubnets/v3`, `ShowVirsubnet/v3`, `ListVirsubnetCidrReservations/v3`, `ShowVirsubnetCidrReservation/v3`, `ShowNetworkIpAvailabilities/v2` |
| VPC、路由与对等连接 | `ListVpcs/v3`, `ListVpcs/v2`, `ShowVpc/v3`, `ShowVpc/v2`, `ListRouteTables/v2`, `ShowRouteTable/v2`, `ListVpcRoutes/v2`, `ShowVpcRoute/v2`, `ListVpcPeerings/v2`, `ShowVpcPeering/v2` |
| 网络ACL | `ListFirewall/v3`, `ShowFirewall/v3`, `NeutronListFirewallGroups/v2`, `NeutronShowFirewallGroup/v2`, `NeutronListFirewallPolicies/v2`, `NeutronShowFirewallPolicy/v2`, `NeutronListFirewallRules/v2`, `NeutronShowFirewallRule/v2` |
| 已有流日志与流量镜像配置 | `ListFlowLogs/v2`, `ShowFlowLog/v2`, `ListTrafficMirrorSessions/v3`, `ShowTrafficMirrorSession/v3`, `ListTrafficMirrorFilters/v3`, `ShowTrafficMirrorFilter/v3`, `ListTrafficMirrorFilterRules/v3`, `ShowTrafficMirrorFilterRule/v3` |
| 兼容Neutron查询 | `NeutronListNetworks/v2`, `NeutronShowNetwork/v2`, `NeutronListPorts/v2`, `NeutronShowPort/v2`, `NeutronListRouters/v2`, `NeutronShowRouter/v2`, `NeutronListSubnets/v2`, `NeutronShowSubnet/v2`, `NeutronListSecurityGroups/v2`, `NeutronShowSecurityGroup/v2`, `NeutronListSecurityGroupRules/v2`, `NeutronShowSecurityGroupRule/v2` |
| 配额 | `ShowQuota/v3`, `ShowQuota/v2` |

#### EIP

| 诊断主题 | 实际操作 |
|---|---|
| 公网IP及绑定 | `ListPublicips/v3`, `ListPublicips/v2`, `ShowPublicip/v3`, `ShowPublicip/v2`, `NeutronListFloatingIps/v2`, `NeutronShowFloatingIp/v2`, `ListProjectGeipBindings/v3` |
| 带宽、限速与共享带宽规则 | `ListBandwidths/v2`, `ShowBandwidth/v2`, `ListBandwidth/v3`, `ListEipBandwidths/v3`, `ListBandwidthsLimit/v3`, `ListBandwidthRule/v3`, `ShowBandwidthRule/v3`, `ListBandwidthPkg/v2` |
| 网关、IP池、资源任务与配额 | `ListTenantVpcIgws/v3`, `ShowInternalVpcIgw/v3`, `ListPublicipPool/v3`, `ShowPublicipPool/v3`, `CountEipAvailableResources/v3`, `ShowResourcesJobDetail/v2`, `ListQuotas/v2` |

#### ER

| 诊断主题 | 实际操作 |
|---|---|
| 实例及连接 | `ListEnterpriseRouters/v3`, `ShowEnterpriseRouter/v3`, `ListAttachments/v3`, `ShowAttachment/v3`, `ListVpcAttachments/v3`, `ShowVpcAttachment/v3` |
| 路由表、优选有效路由、静态路由、传播、关联 | `ListRouteTables/v3`, `ShowRouteTable/v3`, `ListEffectiveRoutes/v3`, `ListStaticRoutes/v3`, `ShowStaticRoute/v3`, `ListAssociations/v3`, `ListPropagations/v3` |
| 已有流日志和配额 | `ListFlowLogs/v3`, `ShowFlowLog/v3`, `ShowQuotas/v3` |

#### ELB

| 诊断主题 | 实际操作 |
|---|---|
| 实例、拓扑及整体状态 | `ListLoadBalancers/v3`, `ListLoadBalancers/v2`, `ShowLoadBalancer/v3`, `ShowLoadBalancer/v2`, `ShowLoadBalancerStatus/v3`, `ShowLoadbalancersStatus/v2`, `ShowLoadBalancerTopology/v3`, `ShowLoadBalancerPorts/v3`, `ListDomainIPs/v3`, `ListLoadbalancerFeature/v3`, `ListFeatureConfigs/v3` |
| 监听器、后端组、后端、健康检查 | `ListListeners/v3`, `ListListeners/v2`, `ShowListener/v3`, `ShowListener/v2`, `ListPools/v3`, `ListPools/v2`, `ShowPool/v3`, `ShowPool/v2`, `ListMasterSlavePools/v3`, `ShowMasterSlavePool/v3`, `ListMembers/v3`, `ListMembers/v2`, `ListAllMembers/v3`, `ShowMember/v3`, `ShowMember/v2`, `ListHealthMonitors/v3`, `ListHealthMonitors/v2`, `ShowHealthMonitor/v3`, `ShowHealthmonitors/v2`, `ShowMemberHealthCheckJob/v3` |
| 七层转发、访问控制、TLS策略与证书清单 | `ListL7Policies/v3`, `ListL7Policies/v2`, `ShowL7Policy/v3`, `ShowL7Policy/v2`, `ListL7Rules/v3`, `ListL7Rules/v2`, `ListAllL7Rules/v3`, `ShowL7Rule/v3`, `ShowL7Rule/v2`, `ListIpGroups/v3`, `ShowIpGroup/v3`, `ShowIpGroupRelatedListeners/v3`, `ListWhitelists/v2`, `ShowWhitelist/v2`, `ListSecurityPolicies/v3`, `ShowSecurityPolicy/v3`, `ListSystemSecurityPolicies/v3`, `ListCertificates/v3`, `ListCertificates/v2` |
| 日志配置、任务、规格、配额 | `ListLogtanks/v3`, `ShowLogtank/v3`, `ListJobs/v3`, `ShowJob/v3`, `ListFlavors/v3`, `ShowFlavor/v3`, `ListQuotaDetails/v3`, `ShowQuota/v3` |

#### NAT

| 诊断主题 | 实际操作 |
|---|---|
| 公网NAT及SNAT/DNAT | `ListNatGateways/v2`, `ShowNatGateway/v2`, `ListNatGatewaySnatRules/v2`, `ShowNatGatewaySnatRule/v2`, `ListNatGatewayDnatRules/v2`, `ShowNatGatewayDnatRule/v2` |
| 私网NAT、中转IP、中转子网及规则 | `ListPrivateNats/v2`, `ShowPrivateNat/v2`, `ListPrivateSnats/v2`, `ShowPrivateSnat/v2`, `ListPrivateDnats/v2`, `ShowPrivateDnat/v2`, `ListTransitIps/v2`, `ShowTransitIp/v2`, `ListTransitSubnet/v2`, `ShowTransitSubnet/v2` |
| 网关规格 | `ListNatGatewaySpecs/v2`, `ListSpecs/v2` |

#### DNS

| 诊断主题 | 实际操作 |
|---|---|
| 域名与解析记录 | `ListPublicZones/v2`, `ShowPublicZone/v2`, `ListPrivateZones/v2`, `ShowPrivateZone/v2`, `ListRecordSets/v2`, `ListRecordSetsByZone/v2`, `ShowRecordSet/v2`, `ShowRecordSetByZone/v2`, `ListRecordSetsWithLine/v2`, `ShowRecordSetWithLine/v2`, `ListPtrRecords/v2`, `ListPtrs/v2`, `ShowPtr/v2`, `ShowPtrRecordSet/v2`, `ShowDnssecConfig/v2` |
| 公网域名专用诊断与权威服务器 | `ShowDomainDetection/v2`, `ShowWebsiteRecordSet/v2`, `ShowEmailRecordSet/v2`, `ShowZoneNameServer/v2`, `ListNameServers/v2`, `ShowPublicZoneNameServer/v2`, `ShowPrivateZoneNameServer/v2` |
| 内网解析端点、转发规则与已有解析日志配置 | `ListEndpoints/v2`, `ShowEndpoint/v2`, `ListEndpointIpaddresses/v2`, `ListEndpointVpcs/v2`, `ListResolverRules/v2`, `ShowResolverRule/v2`, `ListResolverQueryLogConfigs/v2`, `ShowResolverQueryLogConfig/v2` |
| 解析线路、统计资源、异步任务与配额 | `ListCustomLine/v2`, `ListLineGroups/v2`, `ShowLineGroup/v2`, `ListSystemLines/v2`, `ListPublicZoneLines/v2`, `ListInstances/v2`, `ListBatchOperationTasks/v2`, `ShowBatchOperationTask/v2`, `ShowBatchCreateRecordSetsTask/v2`, `ShowDomainQuota/v2` |

#### VPCEP

| 诊断主题 | 实际操作 |
|---|---|
| 终端节点、服务详情、连接状态和白名单 | `ListEndpoints/v1`, `ListEndpointInfoDetails/v1`, `ListEndpointService/v1`, `ListServiceConnections/v1`, `ListServiceDescribeDetails/v1`, `ListServiceDetails/v1`, `ListServicePermissionsDetails/v1`, `ListServicePublicDetails/v1`, `ListQuotaDetails/v1` |

#### CFW

| 诊断主题 | 实际操作 |
|---|---|
| 实例、防护路径及状态 | `ListFirewallList/v1`, `ListFirewallDetail/v1`, `ListEips/v1`, `ListEipCount/v1`, `ListEastWestFirewall/v1`, `ListProtectedVpcs/v1`, `ShowEwAssociatedEr/v1`, `ShowEwAssociatedVpc/v1`, `ShowSnFirewallProtectionStatus/v1`, `ShowAutoProtectStatus/v1`, `ListPrivateNetworkSegments/v1`, `ShowConfigQuota/v1` |
| 访问规则、命中情况、黑白名单、IPS | `ListAclRules/v1`, `ListAclRuleHitCount/v1`, `ListAclRuleHitStatus/v1`, `ListAddressSets/v1`, `ListAddressSetDetail/v1`, `ListAddressItems/v1`, `ListServiceSets/v1`, `ListServiceSetDetail/v1`, `ListServiceItems/v1`, `ListBlackWhiteLists/v1`, `ListIpBlacklist/v1`, `ListIpBlacklistSwitch/v1`, `ListIpsRules/v1`, `ListAdvancedIpsRules/v1`, `ListCustomerIps/v1`, `ShowCustomerIpsInfo/v1`, `ListIpsProtectMode/v1`, `ListIpsSwitchStatus/v1`, `ListIpsWhitelists/v1`, `ShowIpsUpdateTime/v1`, `ListSchedules/v1`, `ShowAntiVirusRule/v1`, `ShowAntiVirusSwitch/v1` |
| 访问、攻击、流量日志与统计 | `ListAccessControlLogs/v1`, `ListAttackLogs/v1`, `ListFlowLogs/v1`, `ListLogs/v1`, `ListFlowStatistic/v1`, `ListAttackStatistic/v1`, `ShowAccessDetail/v1`, `ShowAccessTop/v1`, `ShowAttackDetail/v1`, `ShowAttackTop/v1`, `ShowAttackTotal/v1`, `ShowAttackTrend/v1`, `ShowFlowDetail/v1`, `ShowFlowTop/v1`, `ShowFlowTrend/v1`, `ShowTrafficTrend/v1`, `ShowLogsCount/v1`, `ListLogConfig/v1`, `ShowAlarmConfig/v1`, `ListAlarmWhitelist/v1`, `ListJob/v1` |
| 域名解析、已有抓包任务与结果 | `ListDnsServers/v1`, `ListDomainParseDetail/v1`, `ListDomainParseIp/v1`, `ListDomainResolveIp/v1`, `ListDomainSets/v1`, `ShowDomainSetDetail/v1`, `ListDomains/v1`, `ListCaptureTask/v1`, `ListCaptureResult/v1` |

#### CC

| 诊断主题 | 实际操作 |
|---|---|
| 跨区域云连接与路由 | `ListCloudConnections/v3`, `ShowCloudConnection/v3`, `ListNetworkInstances/v3`, `ShowNetworkInstance/v3`, `ListCloudConnectionRoutes/v3`, `ShowCloudConnectionRoutes/v3`, `ListAuthorisations/v3`, `ListPermissions/v3` |
| 带宽资源、中心网络和连接 | `ListBandwidthPackages/v3`, `ShowBandwidthPackage/v3`, `ListInterRegionBandwidths/v3`, `ShowInterRegionBandwidth/v3`, `ListGlobalConnectionBandwidths/v3`, `ShowGlobalConnectionBandwidth/v3`, `ListGlobalConnectionBandwidthConfigs/v3`, `ListCentralNetworks/v3`, `ShowCentralNetwork/v3`, `ListCentralNetworkAttachments/v3`, `ListCentralNetworkConnections/v3`, `ListCentralNetworkErRouteTableAttachments/v3`, `ShowCentralNetworkErRouteTableAttachment/v3`, `ListCentralNetworkGdgwAttachments/v3`, `ShowCentralNetworkGdgwAttachment/v3`, `ListCentralNetworkPolicies/v3`, `ListCentralNetworkPolicyChangeSet/v3`, `ListSiteNetworks/v3`, `ShowSiteNetwork/v3`, `ListCentralNetworkQuotas/v3`, `ListCloudConnectionQuotas/v3`, `ListSiteNetworkQuotas/v3` |

#### VPN

| 诊断主题 | 实际操作 |
|---|---|
| 站点VPN网关、连接、协商、路由和日志 | `ListVgws/v5`, `ShowVgw/v5`, `ListCgws/v5`, `ShowCgw/v5`, `ListVpnConnections/v5`, `ShowVpnConnection/v5`, `ListConnectionIpsecSa/v5`, `ShowVpnGatewayRoutingTable/v5`, `ShowVpnConnectionLog/v5`, `ShowVpnConnectionsLogConfig/v5`, `ListConnectionMonitors/v5`, `ShowConnectionMonitor/v5`, `ListVpnGatewayJobs/v5`, `ShowQuotasInfo/v5` |
| 客户端VPN | `ListP2cVgws/v5`, `ShowP2cVgw/v5`, `ListP2cVgwConnections/v5`, `ListVpnServersByProject/v5`, `ListVpnServersByVgw/v5`, `ListVpnAccessPolicies/v5`, `ShowVpnAccessPolicy/v5`, `ListP2cVpnGatewayJobs/v5` |

#### Anti-DDoS

| 诊断主题 | 实际操作 |
|---|---|
| 基础防护、清洗、黑洞、异常事件与防护流量 | `ListDDosStatus/v2`, `ListDDosStatus/v1`, `ShowDDosStatus/v1`, `ShowDDos/v1`, `ShowDefaultConfig/v1`, `ListDailyLog/v1`, `ListDailyReport/v1`, `ListWeeklyReports/v1`, `ShowAlertConfig/v2`, `ShowLogConfig/v1`, `ShowNewTaskStatus/v2`, `ListQuota/v1` |

#### AAD

| 诊断主题 | 实际操作 |
|---|---|
| 已用高防/原生高级防护时：实例、封堵与攻击状态 | `ListInstance/v1`, `ShowInstanceByInstanceId/v2`, `ListPackage/v1`, `ListProtectedIp/v1`, `ListBlockIps/v1`, `ShowBlockStatistics/v1`, `ShowFlowBlock/v2`, `ShowUnblockRecord/v1`, `ListUnblockQuotaStatistics/v1`, `ListDDoSAttackEvent/v2`, `ListDDoSBlackHoleEvent/v2`, `ListDDoSFlow/v2`, `ListDDoSConnectionNumber/v2`, `ListPeak/v1`, `ShowDDoSPeak/v2` |
| 高防转发、源站和访问规则 | `ListDomain/v1`, `ListInstanceDomains/v2`, `ListInstanceId/v1`, `ShowDomainDetail/v2`, `ShowDomainNameConfig/v2`, `ListInstanceIpRule/v1`, `ListPolicy/v1`, `ShowPolicy/v1`, `ListSourceIp/v2`, `ListSourceIps/v1`, `ListFrequencyControlRule/v2`, `ListWhiteBlackIpRule/v2`, `ListWafCustomRule/v2`, `ListWafGeoIpRule/v2`, `ListWafWhiteIpRule/v2`, `ListWafAttackEvent/v2`, `ListWafBandwidth/v2`, `ListWafQps/v2`, `ShowWafQps/v2`, `ShowWafPolicy/v2`, `ShowLtsConfig/v1` |

#### WAF

| 诊断主题 | 实际操作 |
|---|---|
| 防护域名、源站、接入状态与引擎 | `ListCompositeHosts/v1`, `ShowCompositeHost/v1`, `ListHost/v1`, `ShowHost/v1`, `ShowHostStatus/v1`, `ListHostRoute/v1`, `ListPremiumHost/v1`, `ShowPremiumHost/v1`, `ShowSourceIp/v1`, `ListInstance/v1`, `ShowInstance/v1`, `ListInstanceStatus/v1`, `ListInstancePools/v1`, `ShowPool/v1`, `CheckAgency/v1`, `ConfirmDnsDomain/v1` |
| 访问拦截策略与规则 | `ListPolicy/v1`, `ShowPolicy/v1`, `ListPolicyProtectRules/v1`, `ListCcPolicyRules/v1`, `ListCcRules/v1`, `ShowCcRule/v1`, `ListCustomPolicyRules/v1`, `ListCustomRules/v1`, `ShowCustomRule/v1`, `ListGeoIpPolicyRules/v1`, `ListGeoipRule/v1`, `ShowGeoipRule/v1`, `ListWhiteblackipPolicyRules/v1`, `ListWhiteblackipRule/v1`, `ShowWhiteBlackIpRule/v1`, `ListIgnorePolicyRules/v1`, `ListIgnoreRule/v1`, `ShowIgnoreRule/v1`, `ListAnticrawlerRules/v1`, `ShowAnticrawlerRule/v1`, `ListIpReputationPolicyRules/v1`, `ListIpReputationRules/v1`, `ConfirmIpReputationRule/v1`, `ListPunishmentRules/v1`, `ShowPunishmentRule/v1`, `ListWebBasicProtectionRules/v1`, `ShowWebProtectionRule/v1`, `ListIpGroup/v1`, `ShowIpGroup/v1`, `ListValueList/v1`, `ShowValueList/v1`, `ListAntileakagePolicyRules/v1`, `ListAntileakageRules/v1`, `ShowAntileakageRule/v1`, `ListAntiTamperPolicyRules/v1`, `ListAntitamperRule/v1`, `ShowAntitamperRule/v1`, `ListPrivacyPolicyRules/v1`, `ListPrivacyRule/v1`, `ShowPrivacyRule/v1` |
| 异常、攻击事件、响应码、流量与日志 | `ListEvent/v1`, `ShowEvent/v1`, `ListEventLog/v1`, `ListStatistics/v1`, `ListTopAbnormal/v1`, `ListResponseCodeTimeline/v1`, `ListBandwidthTimeline/v1`, `ListQpsTimeline/v1`, `ListRequestTimeline/v1`, `ListThreats/v1`, `ListAttackActionTypes/v1`, `ListSourceIpTop5/v1`, `ListTopIp/v1`, `ListTopUrl/v1`, `ListUrl/v1`, `ListTopDomains/v1`, `ListOverviewsClassification/v1`, `ListOverviewsHostDomains/v1`, `ShowLtsInfoConfig/v1`, `ConfirmAsyncJob/v1`, `ListCertificates/v1`, `ShowConsoleConfig/v1`, `ShowSubscriptionInfo/v1`, `ConfirmUserBundle/v1` |

#### HCSCLOUDNETDEBUG

| 诊断主题 | 实际操作 |
|---|---|
| HCS条件适用的网络诊断查询 | `ListFlowMonitors/v1`, `ListFlowPaths/v1`, `Listinstances/v1`, `ListVmInfo/v1`, `ListCurSessionElbTask/v1`, `ListHistSessionElbTask/v1`, `ShowElbCurSessionElbTaskDetail/v1`, `ShowElbHistSessionElbTaskDetail/v1` |

### 专用诊断与会产生任务/配置的动作（单独区别）

| 命令 | 已核实行为 | 用法或限制 |
|---|---|---|
| `hcloud DNS ShowDomainDetection/v2` | GET 公网域名诊断 | 必填 `--zone_id`、`--domain_name`，`--type` 可选 MX/CNAME/TXT。国内站区域 `cn-north-4`；国际站文档写 `ap-southeast-3`，需按账号站点选择。 |
| `hcloud ELB CreateMemberHealthCheckJob/v3` | POST 创建后端服务器检测任务 | 必填 `--member_id`；`--member_check.subject` 支持 `securityGroup`、`networkAcl`、`config`、`all`；`--member_check.listener_id` 可选。这是配置检查任务，不能据此声称会探测整个网络路径。 |
| `hcloud ELB ShowMemberHealthCheckJob/v3` | GET 检测结果 | 必填 `--job_id`，来自创建任务返回值。 |
| `hcloud CFW CreateCaptureTask/v1` | POST 创建并执行一次抓包任务 | 防火墙ID、源/目的地址、协议、时长、最大报文数必填；仅适用已开通且流量经过 CFW 的情况。已有结果用 `ListCaptureTask/v1`、`ListCaptureResult/v1`。 |
| `hcloud VPN CreateConnectionMonitor/v5` | POST 创建 VPN 连接监控 | 必填 `--connection_monitor.vpn_connection_id`。已有监控用 `ListConnectionMonitors/v5`、`ShowConnectionMonitor/v5`。 |
| `hcloud VPC CreateFlowLog/v2` / `UpdateFlowLog/v2` | 创建/修改流日志资源 | 需要日志接收配置；不与只读诊断混用。日志存储/采集费用须按所用 LTS 等服务计费规则核对，本次未核价格。 |
| `hcloud ER CreateFlowLog/v3` / `EnableFlowLog/v3` | 创建/开启 ER 流日志 | 需要流日志接收配置；同样可能产生日志采集/存储费用，非只读。 |
| `hcloud VPC CreateTrafficMirrorSession/v3` 等 | 创建流量镜像和筛选规则 | 会复制流量并改变资源配置，需要接收端能力和资源；已有配置查询见清单。 |
| `hcloud HCSCLOUDNETDEBUG ShowFullLinkPaths/v1` | POST 全链路虚拟路径查询 | 必填源/目的ID、IP、类型及内外网标志；可选协议和端口。仅列 HCS 条件适用；未验证普通公有云可用。 |
| `hcloud HCSCLOUDNETDEBUG CreateCurSessionElbQuery/v1`、`CreateHistSessionElbQuery/v1`、`StartElbCurSessionElbTask/v1`、`StartElbHistSessionElbTask/v1` | 创建/启动 ELB 连接查询任务 | HCS 条件适用；创建和启动属于主动任务操作，非读取已有结果。 |

DNS 诊断的返回状态可区分未注册、未托管华为云、缺少网站/邮箱记录、缺少默认解析、权威服务器未生效等问题。[域名诊断响应](https://support.huaweicloud.com/api-dns/ShowDomainDetection.html)

`ER ListEffectiveRoutes/v3` 返回优选后的有效路由，可检查下一跳和黑洞路由，不只是看用户配置的静态路由。[有效路由API](https://support.huaweicloud.com/api-er/ListEffectiveRoutes.html)

`Anti-DDoS ShowDDosStatus/v1` 的 `packetcleaning` 表示清洗，`packetdropping` 表示黑洞，这两类能解释 EIP 突然不可达。[EIP防护状态](https://support.huaweicloud.com/intl/zh-cn/api-aad/ShowDDosStatus.html)

`WAF ShowCompositeHost/v1` 可以核对防护接入/运行状态、后端IP、回源协议和端口；`ShowSourceIp/v1` 查 WAF 回源 IP，结合 ECS 安全组检查源站是否放通。[WAF域名详情](https://support.huaweicloud.com/api-waf/ShowCompositeHost.html)、[WAF CLI参考](https://support.huaweicloud.com/intl/en-us/clir-waf/en-us_topic_0000002750566309.html)

### 重要区别与参数注意

- `VPC ShowFirewall/v3` 指网络 ACL；`CFW` 是云防火墙，产品不同。
- `ELB ShowLoadBalancerStatus/v3` 查询负载均衡及子资源的状态树，部分 `operating_status` 映射与单资源详情不完全一致（例如被禁用 Member 在状态树可为 `DISABLE`）。应与 `ShowMember/v3` 配合。
- `ELB ShowHealthMonitor/v3` 与 `ShowHealthmonitors/v2` 拼写不同，不能自行改名；健康检查配置查询不会主动新建健康探测。
- 本机支持 `WAF ListHostRoute/v1`，官方说明该接口在部分站点受限且将下线；优先用域名详情核对源站。[WAF CLI参考](https://support.huaweicloud.com/intl/en-us/clir-waf/en-us_topic_0000002750566309.html)
- 证书检查列清单和相关 TLS 策略即可开始；证书详情 API 可能含证书/密钥字段，需要只保留诊断所需字段。
- `List*` 可能有分页；空结果只说明当前区域、项目、权限与筛选条件下无返回，不能直接推断全账号没有该资源。
- 本清单排除纯标签、API版本查询、资源创建/删除、解除黑洞、改安全组/ACL、重置 VPN、改 DNS 记录等；这些对定位不是必需的只读动作。

### 最小示例（模板，未执行）

```bash
rtk proxy hcloud VPC ShowPort/v3 --cli-region=cn-north-4 --port_id='<网卡端口ID>'
rtk proxy hcloud VPC ListSecurityGroupRules/v3 --cli-region=cn-north-4 --security_group_id.1='<安全组ID>'
rtk proxy hcloud VPC ShowRouteTable/v2 --cli-region=cn-north-4 --routetable_id='<路由表ID>'
rtk proxy hcloud EIP ShowPublicip/v3 --cli-region=cn-north-4 --publicip_id='<EIP资源ID>'
rtk proxy hcloud Anti-DDoS ShowDDosStatus/v1 --cli-region=cn-north-4 --floating_ip_id='<EIP资源ID>'
rtk proxy hcloud DNS ShowDomainDetection/v2 --cli-region=cn-north-4 --zone_id='<域名ID>' --domain_name=www.example.com.
rtk proxy hcloud ELB ShowLoadBalancerStatus/v3 --cli-region=cn-north-4 --loadbalancer_id='<ELB_ID>'
```

### 补充官方来源

- [VPC安全组规则API](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0017.html)
- [EIP CLI V3](https://support.huaweicloud.com/intl/zh-cn/clir-eip/EIP-cli_v3.html)、[EIP CLI V2](https://support.huaweicloud.com/intl/zh-cn/clir-eip/EIP-cli_v2.html)
- [VPN站点入云CLI](https://support.huaweicloud.com/clir-vpn/vpn_cli_001.html)
- [各网络产品只读采集所需权限](https://support.huaweicloud.com/intl/en-us/productdesc-mgc/mgc_01_0017.html)

本地元数据校验通过：483 个含版本的候选查询命令。不是账号开通/接口授权/实际执行成功的证明。

## 监控、日志、审计、运维和安全


核查日期：2026-10-19。核查的是本机命令能力与官方前置条件，没有调用账号云资源 API、没有读取凭据、没有发起扫描或执行远程脚本。

命令名依据本机 `hcloud <service> --help` 和官方 CLI 缓存 `~/.hcloud/metaRepo/template/<service>/apis_cn.json`；关键参数通过 operation `--help` 验证。`CES`、`LTS`、`CTS`、`COC`、`HSS`、`AOM`、`APM`、`SecMaster` 均有可用 operation。单一版本 operation 可省略 `/vN`；多版本服务建议显式使用 `/vN`，例如 `ListAlarmHistories/v2`。本笔记中每个 operation 前均应加 `hcloud 服务名`。

### 结论与边界

- 排查普通 ECS 优先使用 CES（性能/告警/事件）、CTS（谁何时改过什么）、LTS（已采集的系统与应用日志）、HSS（已采集的漏洞/入侵/主机指纹）。
- COC 有真正的 ECS GuestOS 诊断，但会安装诊断插件、执行采集脚本和采集 OS 数据，需要前置授权和 Agent 条件，不能当作纯查询。
- AOM/APM/SecMaster 适用于已经接入这些服务的应用或安全平台；拥有 ECS 并不代表已有这些数据。
- `CMS` 当前可用命令属于“智能购买组”，不是主机故障诊断；本机没有 CMS 原生诊断 operation。
- HTTP 方法不能作为是否改变状态的唯一判断：CES/LTS/SecMaster 的某些 `POST` 是查询，而 HSS `RunBaselineDetect` 虽是 `GET` 却会发起检测。

### CES 云监控：性能、Agent、告警和事件

| 用途 | 已核实 operation |
|---|---|
| 指标发现与历史曲线 | `ListMetrics`、`ShowMetricData`、`BatchListMetricData`、`BatchListSpecifiedMetricData` |
| Agent 运行状态、监控维度与维护结果 | `ListAgentStatus`（v3）、`ListAgentDimensionInfo`、`ListAgentInvocations`（v3） |
| 告警记录、告警规则与触发条件 | `ListAlarmHistories/v2`（推荐）、`ListAlarmHistories/v1`、`ListAlarmRules`（推荐）、`ListAlarms`、`ShowAlarm`、`ListAlarmRulePolicies`、`ListAlarmRuleResources` |
| 告警为什么没通知：屏蔽、模板与一键告警 | `ListNotificationMasks`、`ListNotificationMaskResources`、`ListAlarmTemplates/v2`、`ListAlarmTemplates/v1`、`ShowAlarmTemplate`、`ListAlarmTemplateAssociationAlarms`、`ListOneClickAlarms`、`ListOneClickAlarmRules` |
| 系统运维/计划事件与自定义事件 | `ListEvents`、`ListEventDetail` |
| 已有监控看板、资源分组、配额 | `ListDashboardInfos`、`ListDashboardWidgets`、`ShowWidget`、`ListResourceGroup`、`ListResourceGroups`、`ShowResourceGroup/v1`、`ShowResourceGroup/v2`、`ListResourceGroupsServicesResources`、`ShowQuotas` |

`SYS.ECS` 是 ECS 基础监控命名空间，`AGT.ECS` 用于 OS 监控；EIP/带宽、EVS 还应分别查看 `SYS.VPC`、`SYS.EVS` 等对应资源的指标。先用 `ListMetrics` 发现实际存在的指标与维度，不应假定普通 ECS 未装 Agent 也有内存/文件系统指标。[官方指标接口](https://support.huaweicloud.com/intl/en-us/api-ces/ces_03_0023.html)、[支持监控的服务](https://support.huaweicloud.com/api-ces/ces_03_0059.html)

关键参数与模板（仅供后续选择运行）：

```sh
rtk proxy hcloud CES ListMetrics --cli-region=cn-north-4 --namespace=SYS.ECS --dim.0='instance_id,<ECS_ID>'
rtk proxy hcloud CES ShowMetricData --cli-region=cn-north-4 --namespace=SYS.ECS --metric_name=cpu_util --dim.0='instance_id,<ECS_ID>' --from='<毫秒时间戳>' --to='<毫秒时间戳>' --period=300 --filter=average
rtk proxy hcloud CES ListAgentStatus --cli-region=cn-north-4 --instance_ids.1='<ECS_ID>'
rtk proxy hcloud CES ListAlarmHistories/v2 --cli-region=cn-north-4 --resource_id='<ECS_ID>' --limit=100
rtk proxy hcloud CES ListEvents --cli-region=cn-north-4 --event_type=EVENT.SYS --from='<毫秒时间戳>' --to='<毫秒时间戳>'
```

`ShowMetricData` 的 `from/to` 使用毫秒 UTC 时间戳；`ListAlarmHistories/v2` 的 `from/to` 则使用 ISO 8601 时间字符串，不应复用指标的时间戳格式；`period` 可选 1、60、300、1200、3600、14400、86400，`filter` 支持 average/variance/min/max/sum。Agent 查询是 `POST` 只读，结果区分 UniAgent 未安装/在线/静默/失联及 telescope 未安装/运行/停止/故障/失联。[官方 Agent 状态](https://support.huaweicloud.com/api-ces/ListAgentStatus.html)、[CES CLI v3](https://support.huaweicloud.com/intl/en-us/clir-ces/CES-cli_v3_en.html)

主动改变主机的相关命令：`BatchCreateAgentInvocations`（v3，安装/升级/回滚/重试/远程安装监控 Agent）。创建或启停告警的 `CreateAlarmRules`、`CreateOneClickAlarm`、`UpdateAlarm*`、`BatchEnableAlarmRules` 等属于监控配置修改，不是查询。

特殊场景：`ShowEventData` 只服务于 SAP HANA 的 SAP Monitor 主机配置查询；不要将它作为普通 ECS 通用主机配置接口。[官方适用范围](https://support.huaweicloud.com/api-ces/ces_03_0035.html)

### LTS 云日志：错误、上下文、SQL 分析与采集状态

| 用途 | 已核实 operation |
|---|---|
| 找日志组/日志流 | `ListLogGroups`、`ListLogStream`、`ListLogStreams`、`ListLogStreamIndex` |
| 关键字检索、上下文与分布 | `ListLogs`、`ListLogContext`、`ListLogHistogram` |
| SQL/结构化日志分析 | `ListStructuredLogsWithTimeRange`（新版）、`ListQueryStructuredLogs`（旧版，官方 PDF 标注即将下线）、`ListStructTemplate`、`ListBreifStructTemplate`、`ShowStructTemplate` |
| 采集器/接入规则状态 | `ListHost`、`ListHostGroup`、`ListAccessConfig`、`ShowAomMappingRule`、`ShowAomMappingRules`、`ShowAdminConfig`、`ShowLogConvergeConfig`、`ShowMemberGroupAndStream` |
| 日志告警、通知规则 | `ListActiveOrHistoryAlarms`、`ListKeywordsAlarmRules`、`ListSqlAlarmRules`、`ListNotificationTemplates`、`ShowNotificationTemplate`、`ListNotificationTopics` |
| 已有快速查询、历史 SQL、图表 | `ListCriterias`、`ListQueryAllSearchCriterias`、`ListHistorySql`、`ListCharts` |
| 流量、日志丢失/成本排查和转储配置 | `ListTimeLineTrafficStatistics`、`ListTopnTrafficStatistics`、`ListTransfers` |

这些命令只能查询已接入的日志；ECS 的任意本地日志不会自动可查。`ListHost` 可查 running/offline/error/install-fail/authentication error 等采集状态。`ListLogs` 虽是 POST，权限分类为 List，读取指定流内容。[官方 LTS CLI](https://support.huaweicloud.com/clir-lts/LTS-cli.html)、[ListLogs](https://support.huaweicloud.com/api-lts/ListLogs.html)

```sh
rtk proxy hcloud LTS ListLogs --cli-region=cn-north-4 --log_group_id='<组ID>' --log_stream_id='<流ID>' --start_time='<毫秒时间戳>' --end_time='<毫秒时间戳>' --keywords=error --limit=100 --is_desc=true
rtk proxy hcloud LTS ListStructuredLogsWithTimeRange --cli-region=cn-north-4 --log_stream_id='<流ID>' --format=k-v --query='<只读SQL>' --time_range.start_time='<毫秒时间戳>' --time_range.end_time='<毫秒时间戳>'
```

`ListLogs` 分页使用返回值中的 line_num/scroll_id，并按接口要求带 search_type；已启用自定义时间时还需 `__time__`。`ListLogContext` 用上一轮结果的 `line_num`，可指定 backwards_size/forwards_size；自定义时间场景需共同传入 `__time__`。[上下文日志接口](https://support.huaweicloud.com/intl/zh-cn/api-lts/ListLogContext.html)

`EnableLogCollection` 是打开超额采集开关，会改变采集/费用条件；创建接入、安装采集器、转储、更新保留天数与索引也属于配置/费用动作。

### CTS 云审计：重启、删除、改安全组等操作追溯

| 用途 | 已核实 operation |
|---|---|
| 查询资源操作轨迹 | `ListTraces` |
| 确认是否有追踪器与关键操作通知 | `ListTrackers`、`ListNotifications` |
| 查支持审计的操作、资源类型、操作用户 | `ListOperations`、`ListTraceResources`、`ListUserResources` |
| 配额与转储问题 | `ListQuotas`、`CheckObsBuckets`（检查已有 OBS 桶能否成功转储；属于检查动作，非日志查询） |

`ListTraces` 查询最近 7 天资源操作，默认只返回 10 条，最大 200；可按 ECS 资源 ID、服务、操作名、用户和等级过滤。管理事件用 `--trace_type=system`，配合 `--service_type=ECS --resource_id=<ECS_ID>`；`from/to` 为毫秒时间戳。下一页用响应 marker 传给 `--next`，时间范围过滤与 next 取交集。超过 7 天需查已有转储文件/接入日志，不能靠调大时间参数扩展在线保留期。[官方 CTS API 范围](https://support.huaweicloud.com/intl/en-us/api-cts/cts_api_0002.html)

```sh
rtk proxy hcloud CTS ListTraces --cli-region=cn-north-4 --trace_type=system --service_type=ECS --resource_id='<ECS_ID>' --limit=200 --from='<毫秒时间戳>' --to='<毫秒时间戳>'
```

### COC 云运维中心：真正的 GuestOS 诊断、远程脚本、作业结果

| 类别 | 已核实 operation |
|---|---|
| 读取已有诊断结果 | `ListDiagnosisTasks`、`ShowDiagnosisTask`、`ShowDiagnosisSummary`、`ShowDiagnosisNode` |
| 主动发起/管理诊断 | `CreateDiagnosisTask`、`RetryDiagnosisTask`、`CancelDiagnosisTask` |
| 读取已有公共/自定义脚本及作业内容 | `ListPublicScripts`、`GetPublicScript`、`ListScripts`、`GetScript`、`ListDocuments`、`GetDocument`、`ListDocumentAtomics`、`GetDocumentAtomicInfo` |
| 读取远程脚本执行结果 | `ListScriptJobs`、`GetScriptJobInfo`、`GetScriptJobStatistics`、`ListScriptJobBatches`、`GetScriptJobBatch` |
| 读取作业/定时任务执行结果 | `ListExecutions`、`GetExecution`、`ListExecutionSteps`、`ListExecutionInstances`、`ListScheduledTaskHistory`、`ListScheduledTask`、`ShowScheduledTask`、`ShowJobDetail` |
| 补丁与合规报告 | `ListInstanceCompliant`、`ShowInstancePatchItems` |
| 已有告警、事件单、问题单和历史 | `ShowAlarm`、`ListAlarmHandleHistories`、`ListIncidents`、`ListIncidentsHistories`、`ShowCocIncidentDetail`、`ShowCocIssuesDetail`、`ShowIncidentTask`、`ListIncidentSimpleTickets`、`ListCocTicketOperationHistories` |
| 找 COC 纳管资源与容量/评估结果 | `ListResources`、`ListResourcesOfResourceView`、`ListResourceViews`、`ListAssessTask`、`ListCapacityOrder`、`ListCapacityView`、`ShowLastSyncStatus` |
| 运行远程脚本/作业（主机上执行） | `ExecutePublicScript`、`ExecuteScript`、`ExecuteDocument` |
| 影响执行任务状态 | `OperateScriptJob`、`OperateExecution`、`CreateScheduledTask`、`EnableScheduledTask`、`DisableScheduledTask` |

命令集依据[官方 COC CLI](https://support.huaweicloud.com/clir-coc/COC-cli.html)与本机 CLI 元数据。

**CreateDiagnosisTask 的实际参数**只有 `type`、`resource_ids`、`extra_properties`（供 RDS 等）；当前 v1 没有 `task_type`、treeId 或 nodeId。ECS 形态为 `--type=ECS --resource_ids.1=<ECS_ID>`。API 要求资源已存在于 COC 应用资源管理，返回诊断工单 `id` 后异步执行，身份策略权限是 `coc:job:action` Write。[提交诊断 API](https://support.huaweicloud.com/api-coc/CreateDiagnosisTask.html)

**ECS 前置条件**：UniAgent 必须运行，Linux >=1.1.5、Windows >=1.1.8，并且 OS 在官方支持列表内；要同意安装插件及 GuestOS 数据采集授权。安装/清理阶段分别可能需要 `aom:uniagentAgent:install`、`aom:uniagentAgent:uninstall`。诊断流程会安装 Holmes 插件、运行采集脚本、诊断、卸载/清理；会采集 GuestOS 数据，并做 CPU、网络延时、IO 性能等分析，因此不是纯读取已有数据。已读文档没有承诺所有区域都支持，不应假定该账号北京四 ECS 已满足条件。[ECS 诊断前提](https://support.huaweicloud.com/usermanual-coc/coc_um_06_08_01.html)、[诊断异常与权限](https://support.huaweicloud.com/coc_faq/coc_faq_05_004.html)

读取结果需要 `task_id`；`ShowDiagnosisTask` 本机 CLI 将 `instance_id` 也标记必填。`ShowDiagnosisNode` 需要 task_id、instance_id、code；ECS code 是 `holmesInstall`、`dataCollection`、`diagnosisFault`、`holmesUnInstall`。[步骤结果 API](https://support.huaweicloud.com/api-coc/ShowDiagnosisNode.html)

`ExecutePublicScript` 不是安全性质保证：需先读 GetPublicScript 中的脚本内容；参数包括脚本 UUID、目标实例及 region、执行用户（如 root）、超时和分批策略。`ListInstancesBatch` 仅计算自动分批结果，虽为 POST 但不执行脚本；`CheckScriptRisk` 评估脚本风险，也不能代替人工阅读其实际行为。不要把 ResetAccountPassword、SyncResourceAgent 或各类 Handle/Update 操作当作查询诊断命令。

### HSS 企业主机安全：入侵、漏洞、基线、主机指纹

以下均在本机 HSS v5 operation 清单内（可以显式加 `/v5`）。查询前确认主机是否有 HSS Agent、是否在线、已开通防护版本及对应功能；本次没有验证账号服务开通情况。

| 诊断目标 | 读取现有结果的 operation |
|---|---|
| 主机与 Agent、防护是否正常 | `ListHostStatus`、`ListAgentStatus`（历史状态）、`ShowHostProtectionStatus`、`ShowAgentStatistics`、`ShowAgentStatisticsStatus`、`ListHostProtectHistoryInfo`、`ListProtectionServers`、`ShowProtectStatistics`、`ShowHostsStatistics`、`ShowVersion` |
| 总体风险、报告、体检 | `ListHostsRisk`、`ListSecurityRisk`、`ShowRiskScore`、`ListSecurityReport`、`ShowSecurityCheckHostReport`、`ShowManualSecurityCheckStatus`、`ListMonthlyOperationReports`、`ShowMonthlyOperationReportDetail` |
| 入侵、挖矿、反弹 shell、Webshell、异常登录等告警 | `ListSecurityEvents`、`ListEventType`、`ListEventForensic`、`ListEventHandleHistory`、`ListEventOperates`、`ListRelatedEvents`、`ListSameEvents`、`ListSimilarHandledEvents`、`ListEventAttCk`、`ListEventTopRisk`、`ShowEventAttackTag`、`ShowEventSeverity` |
| 已拦截 IP/隔离文件、防护策略或白名单导致的行为 | `ListBlockedIp`、`ListLockedStatus`、`ListIsolatedFile`、`ListAlarmConfig`、`ListAlarmWhiteList`、`ListLoginWhiteList`、`ListLoginWhiteIp`、`ListLoginCommonIp`、`ListLoginCommonLocation`、`ListSystemUserWhiteList`、`ListPolicies`、`ListPolicyGroup`、`ShowPolicySwitchStatus`、`ShowSwitchesStatus` |
| 漏洞与影响主机/进程/应用 | `ListVulnerabilities`、`ListHostVuls`、`ListVulHostVuls`、`ListVulHosts`、`ListVulHostHosts`、`ListVulHostProcess`、`ListVulHostApps`、`ListVulnerabilityCve`、`ListUrgentVulnerabilities`、`ShowLinuxVulDetail`、`ShowWindowsVulDetail`、`ShowCmsVulDetail`、`ShowVulReportData`、`ShowVulStatics`、`ShowVulAffectedStatics` |
| 漏洞扫描/修复失败与历史 | `ListVulScanTask`、`ListVulScanTaskHost`、`ShowVulScanPolicy`、`ShowVulScanTaskEstimatedTime`、`ListVulHandleHistory`、`ListVulRepairFailedDetail`、`ListVulRepairCmds`（只查询修复命令，不执行）、`ShowVulTaskStatistics` |
| 安全配置、弱口令与基线 | `ListRiskConfigs`、`ShowRiskConfigDetail`、`ListRiskConfigCheckRules`、`ListRiskConfigHosts`、`ListHostCheckRules`、`ListCheckRuleHost`、`ListCheckRulesInfo`、`ShowCheckRuleDetail`、`ShowCheckRuleFixFailDetail`、`ListWeakPasswordUsers`、`ListPasswordComplexity`、`ListSecurityCheckPolicyGroup`、`ShowSecurityCheckConfig`、`ShowBaselineScanStatus`、`ShowBaselineOverview`、`ShowBaselineStatistic`、`ListBaselineWhiteLists` |
| 开放端口、进程、账号、软件、启动项 | `ListPorts`（单台主机）、`ListPortHost`、`ListPortStatistics`、`ShowPortTop`、`ListProcessesHost`、`ListProcessStatistics`、`ShowProcessTop`、`ListUsers`、`ListUserStatistics`、`ListAccounts`、`ShowAccountTop`、`ListApps`、`ListAppStatistics`、`ShowSoftwareTop`、`ListAutoLaunchs`、`ListAutoLaunchStatistics`、`ShowAutoLaunchTop` |
| Web站点/框架/中间件、系统配置与文件变更 | `ListWebAppAndServices`、`ListWebAppAndServiceStatistics`、`ListWebSiteInfo`、`ListWebSiteHostInfo`、`ListWebFrameworkInfo`、`ListWebFrameworkHostInfo`、`ListJarPackageInfo`、`ListJarPackageHostInfo`、`ListKernelModuleInfo`、`ListKernelModuleHostInfo`、`ListSystemConfigs`、`ListFileEvents`、`ListFileHostEventDetails`、`ShowFileStatistic` |
| 资产信息何时发生变化/采集状态 | `ListAppChangeHistories`、`ListAutoLaunchChangeHistories`、`ListUserChangeHistories`、`ShowHostAssetManualCollectStatus`、`ListGlobalAssetScanTask`、`ShowAssetStatistic`、`ShowOsStatisticsInfo` |
| 病毒扫描结果、扫描次数与收费开关 | `ListAntiVirusTask`、`ListAntiVirusResult`、`ListAntivirusHandleHistory`、`ShowAntivirusStatistic`、`ListAntiVirusHost`、`ListAntiVirusPaidHosts`、`ShowAntivirusFreeQuota`、`ShowAntivirusPayPerScanStatus`、`ListAntiVirusPolicy` |
| 网页防篡改、运行时应用防护 | `ListWebTamperEvent`、`ListWebTamperHost`、`ListWebTamperProtectionConfigs`、`ListWebTamperProtectionDirectory`、`ShowWebTamperHostPolicy`、`ListRaspEvents`、`ListRaspPolicies`、`ShowRaspServerDetail`、`ListHostRaspProtectHistoryInfo` |
| 任务执行结果 | `ListTasks`、`ListTaskResources`、`ShowTaskStatistics` |

`ListHostStatus` 可按 host_id、host_name、IP、agent_status、protect_status、has_vul/has_intrusion/has_baseline 等过滤；避免使用 `--refresh=true`，其语义是强制从 ECS 同步主机。`ListSecurityEvents` 至少给 `--category=host`；支持 host_id、severity、handle_status、last_days（1–30）或 begin_time/end_time（13 位毫秒）过滤。[官方 HSS CLI v5](https://support.huaweicloud.com/intl/en-us/clir-hss2.0/HSS-cli_v5_en.html)

HSS 主动检查与处置（均不是读取结果）：

- `CreateVulnerabilityScanTask`、`RecreateVulScanTask`：发起/重新发起漏洞扫描；specific_host 范围对应 agent_id_list，避免 all_host 无意扩大范围。
- `RunBaselineDetect`：对配置检测策略组中的主机发起配置/弱口令检测；虽然 HTTP GET，明确会运行任务，需要 group_id。[官方 RunBaselineDetect](https://support.huaweicloud.com/api-hss2.0/RunBaselineDetect.html)
- `StartManualSecurityCheck`、`SetManualDetect`：手动安全体检/检测；`RunHostAssetManualCollect`、`CreateGlobalAssetScanTask`：主动采集/扫描资产。
- `CreateAntiVirusTask`、`CreateAntiVirusPaidTask`：主动病毒扫描，后者明确按次收费；action=auto 还会自动处置，manual 则人工处置。`ChangeAntivirusPayPerScanStatus` 会改变按次计费开关。[付费病毒扫描 API](https://support.huaweicloud.com/api-hss2.0/CreateAntiVirusPaidTask.html)
- `ChangeCheckRuleAction`、`ChangeVulStatus`、`ChangeEvent`、`BatchChangeEvent`、`HandleAntiVirusResult`、`ChangeBlockedIp`、`ChangeIsolatedFile` 等是忽略/修复/处置/解封/恢复，不属于查询。
- `StartProtection`、`StartPlugin`、`UpgradeAgents`、`UninstallAgents`、开关防护/防火墙等会改变主机行为或防护；`CreateQuotasOrder` 属于购买，不应纳入只读诊断。

运行容器时另查：`ListContainers`、`ListContainerNodes`、`ListContainerLogs`、`ListContainerCmdLogs`、`ListContainerImageLogs`、`ListClusterEvents`、`ListClusterEventLogs`、`ListClusterAuditLogs`、`ListClusterRisks`、`ListCceClusterDetectRisk`、`ListClusterRiskAffectResources`、`ListImageLocal`、`ListRegistryImages`、`ListImageVulnerabilities`、`ListImageMalware`、`ListImageRiskConfigs`、`ListImageWeakPwdUsers`、`ListImageScanTask`、`ListK8sPods`、`ListK8sDeployments`、`ListK8sStatefulSets`、`ListK8sDaemonSets`、`ListK8sJobs`、`ListK8sCronJobs`。这些是已有容器/镜像安全结果；扫描镜像的 BatchScanLocalImage/CreateManualImageScanTask 等另属主动任务。

### AOM 应用运维：已有指标、Prometheus、Agent 与自动化结果

| 用途 | 已核实 operation |
|---|---|
| Agent 采集状态 | `ShowAgentInfos`（UniAgent 主机列表）、`ListAgents`（ICAgent）、`ListPermissions` |
| 时序指标/维度 | `ListSeries`、`ListSample`、`ListMetricItems`、`ShowMetricsData`、`ListLogItems` |
| Prometheus 查询 | `ListPromInstance`、`ListInstantQueryAomPromGet`、`ListInstantQueryAomPromPost`、`ListRangeQueryAomPromGet`、`ListRangeQueryAomPromPost`、`ListLabelsAomPromGet`、`ListLabelsAomPromPost`、`ListLabelValuesAomPromGet`、`ListMetadataAomPromGet` |
| 告警、事件、静默与通知历史 | `ListEvents`、`CountEvents`、`ListAlarmRule`、`ShowAlarmRule`、`ListMetricOrEventAlarmRule`、`ListEvent2alarmRule`、`ListAlarmRuleTemplate`、`ListActionRule`、`ShowActionRule`、`ListMuteRule`、`ListNotifiedHistories`、`ListNotificationTemplates`、`ListNotificationTemplateByName` |
| 自动化执行结果 | `ListWorkflow`、`ListWorkflowExecutions`、`SearchWorkflowExecutionDetail`、`ListAllJobByName`、`ListAllScriptByName`、`ListAllVersionByVersionId`、`ListTemplateByJobId`、`SearchTemplateById` |
| 已有应用/环境/组件和服务发现 | `ShowApp`、`ShowAppByName`、`ShowComponent`、`ShowComponentByName`、`ShowEnv`、`ShowEnvByName`、`ListResourceUnderNode`、`ListServiceDiscoveryRules` |
| 看板 | `ListDashBoards`、`ShowDashBoard`、`ListDashboardsFolder` |

依赖已有 Agent/指标或 Prometheus 接入；Get/Post 版本都可能只读。`ExecuteWorkflow`、`BatchImportAgent`、`BatchUpdateAgent` 是执行/安装/升级动作。`ListAccessCode` 返回访问凭据，不应作为日常诊断随手输出。[官方 AOM CLI](https://support.huaweicloud.com/clir-aom/AOM-cli.html)

### APM 应用性能：慢接口、调用链、火焰图、拓扑

若应用已接入 APM（探针/OTel/SkyWalking 等），以下可用于定位应用层故障。APM Agent 必须能与所在区域 APM 服务通信；本次未验证该 ECS 有应用探针或 APM 数据。[官方接入前置](https://support.huaweicloud.com/usermanual-apm2/apm_08_0047.html)

| 用途 | 已核实 operation |
|---|---|
| 找应用、环境、实例和探针 | `ListBusiness`、`ListApps`、`ListAppEnvs`、`ListBusinessEnv`、`ListEnvInstances`、`SearchApplication`、`SearchAgent`、`ShowBusinessDetail`、`ShowSubBusinessDetail`、`ShowTopologyTree`、`ListOpenRegion`、`ListSupportedRegion` |
| 拓扑与依赖链 | `SearchBusinessTopology`、`SearchEnvTopology`、`ShowTopology` |
| 调用链/span/异常事件/火焰图 | `ShowSpanSearch`、`ShowTraceEvents`、`ShowEventDetail`、`ShowClobDetail`、`ShowFlameLineTree` |
| 慢 URL/事务 | `SearchTransaction`、`SearchTransactionConfig`、`ShowTransactionDetail` |
| 指标/趋势/原始与汇总数据 | `ListEnvMonitorItem`、`ShowEnvMonitorItems`、`ShowMonitorItemDetail`、`ShowMonitorItemViewConfig`、`ShowRawTable`、`ShowSumTable`、`ShowTrend`、`ListEnvTags` |
| 告警与消息 | `ListAlarmData`、`ListAlarmNotify` |

`ShowSpanSearch` 是查询性质的 POST，但官方身份策略访问级别标为 Write；需要 `--x-business-id`、`--biz_id`、`--region` 等必填应用维度，不能仅传 ECS ID。是否改变状态与 IAM 的 Write 标签也应分别解释。[官方 span 查询](https://support.huaweicloud.com/api-apm/ShowSpanSearch.html)

不要常规输出 `ListAkSk`、`ShowAkSks`、`ShowToken`；这些读取密钥/令牌。ChangeAgentStatus/SaveMonitorItemConfig 等改变采集或配置。

### SecMaster 安全云脑：已有统一安全数据、关联事件与安全日志

已核实适合已有 SecMaster 工作空间的 operation：

- 空间、资产与漏洞：`ListWorkspaces`、`ShowWorkspace`、`ListResources`、`ShowResource`、`ListVulnerabilities`、`ShowVulnerability`。
- 告警、事件、情报与关系：`ListAlerts`、`ShowAlert`、`ListIncidents`、`ShowIncident`、`ListIndicators`、`ShowIndicatorDetail`、`ListDataobjectRelations`、`ListDataobjects`、`ShowDataobject`、`ListNotes`。
- 日志查询与直方图：`ListSearchLogs`、`ListSearchHistograms`、`ListTableLogs`、`ListTableHistograms`、`ShowAdhocResult`。
- 查询配置与接入是否正常：`ListDataspaces`、`ShowDataspace`、`ListTables`、`ShowTable`、`ListPipes/v1`、`ListPipes/v2`、`ShowPipe/v1`、`ShowPipe/v2`、`ListCollectConfig/v1`、`ListCollectConfig/v2`、`ListCollectorInstances`、`ListCollectorChannels`、`ListCollectorConnections`、`ListCollectorNode`、`ListSearchConditions`、`ShowSearchCondition`、`ListCloudLogResources`、`ListShippers`、`ShowShipper`、`ShowMonitorStats`、`ShowMoniterMetricStats`。
- 基线/合规与策略运行历史：`SearchBaseline`、`SearchCheckitems`、`ShowCheckitemDetail`、`SearchCompliancePackages`、`ShowCompliancePackageDetail`、`SearchPolicy`、`ShowPolicy`、`SearchPolicyRecord`、`SearchPolicyRecordByPolicyId`。
- 自动化处置调查：`ListPlaybooks`、`ShowPlaybook`、`ListPlaybookInstances`、`ShowPlaybookInstance`、`ListPlaybookAuditLogs`、`ShowPlaybookMonitors`、`ShowPlaybookStatistics`、`ShowPlaybookTopology`、`ListAopWorkflowInstance`、`ShowAopWorkflowInstance`、`ListTasks`、`ShowTask`、`ListReports`、`ShowReportInfo`。

`ListAlerts` 使用 project_id + workspace_id，即使是 POST 仍是搜索已有告警；`ListSearchLogs` 是已有采集日志检索。只有创建 ECS 而未开通工作空间、接入安全服务/日志时，这些查询不会凭空产生诊断结果。[告警查询](https://support.huaweicloud.com/api-secmaster/ListAlerts.html)、[日志检索](https://support.huaweicloud.com/intl/zh-cn/api-secmaster/ListSearchLogs.html)

主动但主要用于分析的命令：`CreateAdhocQuery`、`CreateSearchAnalysis`、`CreateTableAnalysis`、`CreateAlertRuleSimulation` 会启动查询/分析任务，应核对工作空间及查询计量。`CreateWorkflowInstance`/`ChangePlaybookInstance` 等可以执行安全自动化和处置；`CreateSubscriptionOrder` 是订阅购买，`ChangeAlert/ChangeIncident` 修改事件状态，均不要混入只读诊断链。
