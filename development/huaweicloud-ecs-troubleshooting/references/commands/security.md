# 安全 S

核对访问控制和安全结果。规则配置与实际命中证据分别判断。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[AAD](#aad) · [Anti-DDoS](#anti-ddos) · [BSS](#bss) · [CFW](#cfw) · [Config](#config) · [IAM](#iam) · [IAMAccessAnalyzer](#iamaccessanalyzer) · [RMS](#rms) · [SecMaster](#secmaster) · [WAF](#waf)

## AAD

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `AAD/ListBlockIps/v1` · 助 | 查询租户封堵列表 | 读取 | — |
| `AAD/ListDDoSAttackEvent/v2` · 助 | 查询DDoS攻击事件列表 | 读取 | 需 `instance_id`。 |
| `AAD/ListDDoSBlackHoleEvent/v2` · 助 | 黑洞事件列表 | 读取 | — |
| `AAD/ListDDoSConnectionNumber/v2` · 助 | 查询新建连接数和并发连接数 | 读取 | 需 `instance_id`。 |
| `AAD/ListDDoSFlow/v2` · 助 | 查询DDoS攻击防护BPS/PPS流量 | 读取 | 需 `instance_id`。 |
| `AAD/ListDomain/v1` · 助 | 查询域名列表 | 读取 | — |
| `AAD/ListFrequencyControlRule/v2` · 助 | 查询频率控制规则列表 | 读取 | — |
| `AAD/ListInstance/v1` · 助 | 查询高防实例列表 | 读取 | — |
| `AAD/ListInstanceDomains/v2` · 助 | 查询实例关联的域名信息 | 读取 | 需 `instance_id`。 |
| `AAD/ListInstanceId/v1` · 助 | 查询域名关联的实例ID | 读取 | — |
| `AAD/ListInstanceIpRule/v1` · 助 | 查询高防实例IP的转发规则列表 | 读取 | 需 `instance_id`、`ip`。 |
| `AAD/ListPackage/v1` · 助 | 查询实例列表 | 读取 | — |
| `AAD/ListPeak/v1` · 助 | 查询流量峰值、攻击计数 | 读取 | 需 `instance_id`、`ip`。 |
| `AAD/ListPolicy/v1` · 助 | 查询策略列表 | 读取 | — |
| `AAD/ListProtectedIp/v1` · 助 | 查询防护对象列表 | 读取 | — |
| `AAD/ListSourceIp/v2` · 助 | 查询回源ip列表 | 读取 | — |
| `AAD/ListSourceIps/v1` · 助 | 查询高防回源IP段列表 | 读取 | — |
| `AAD/ListUnblockQuotaStatistics/v1` · 助 | 查询解封配额 | 读取 | — |
| `AAD/ListWafAttackEvent/v2` · 助 | 查询攻击事件列表 | 读取 | — |
| `AAD/ListWafBandwidth/v2` · 助 | 带宽曲线 | 读取 | — |
| `AAD/ListWafCustomRule/v2` · 助 | 查询精准防护规则 | 读取 | — |
| `AAD/ListWafGeoIpRule/v2` · 助 | 查询区域封禁规则 | 读取 | — |
| `AAD/ListWafQps/v2` · 助 | 查询请求QPS | 读取 | — |
| `AAD/ListWafWhiteIpRule/v2` · 助 | 防护策略web-cc黑白名单-查询黑白名单规则 | 读取 | — |
| `AAD/ListWhiteBlackIpRule/v2` · 助 | 查询DDoS攻击防护的黑白名单列表 | 读取 | 需 `instance_id`。 |
| `AAD/ShowBlockStatistics/v1` · 助 | 查询封堵统计数据 | 读取 | — |
| `AAD/ShowDDoSPeak/v2` · 助 | 查询高防入流量峰值、攻击流量峰值、DDoS攻击次数 | 读取 | 需 `instance_id`。 |
| `AAD/ShowDomainDetail/v2` · 助 | 查询域名详情 | 读取 | — |
| `AAD/ShowDomainNameConfig/v2` · 助 | 查看域名配置 | 读取 | — |
| `AAD/ShowFlowBlock/v2` · 助 | 查询流量封禁信息 | 读取 | 需 `instance_id`。 |
| `AAD/ShowInstanceByInstanceId/v2` · 助 | 查询实例详情 | 读取 | 需 `instance_id`。 |
| `AAD/ShowLtsConfig/v1` · 助 | 查询日志配置 | 读取 | — |
| `AAD/ShowPolicy/v1` · 助 | 查询策略详情 | 读取 | 需 `policy_id`。 |
| `AAD/ShowUnblockRecord/v1` · 助 | 查询租户解封记录 | 读取 | — |
| `AAD/ShowWafPolicy/v2` · 助 | 查询WEB防护策略配置 | 读取 | — |
| `AAD/ShowWafQps/v2` · 助 | 查询CC攻击防护请求QPS | 读取 | — |

## Anti-DDoS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `Anti-DDoS/ListDDosStatus/v1` · 助 | 查询EIP防护状态列表 | 读取 | — |
| `Anti-DDoS/ListDDosStatus/v2` · 助 | 查询EIP防护状态列表 | 读取 | — |
| `Anti-DDoS/ListDailyLog/v1` · 助 | 查询指定EIP异常事件 | 读取 | 需 `floating_ip_id`。 |
| `Anti-DDoS/ListDailyReport/v1` · 助 | 查询指定EIP防护流量 | 读取 | 需 `floating_ip_id`。 |
| `Anti-DDoS/ListQuota/v1` · 助 | 查询配额 | 读取 | — |
| `Anti-DDoS/ListWeeklyReports/v1` · 助 | 查询周防护统计情况 | 读取 | — |
| `Anti-DDoS/ShowAlertConfig/v2` · 助 | 查询告警配置信息 | 读取 | — |
| `Anti-DDoS/ShowDDos/v1` · 助 | 查询Anti-DDoS服务 | 读取 | 需 `floating_ip_id`。 |
| `Anti-DDoS/ShowDDosStatus/v1` · 实 | 查询指定EIP防护状态 | 读取 | 需 `floating_ip_id`。 |
| `Anti-DDoS/ShowDefaultConfig/v1` · 助 | 查询Ani-DDoS默认防护策略 | 读取 | — |
| `Anti-DDoS/ShowLogConfig/v1` · 助 | 查询全量日志设置 | 读取 | 需 `enterprise_project_id`。 |
| `Anti-DDoS/ShowNewTaskStatus/v2` · 助 | 查询Anti-DDoS任务 | 读取 | 需 `task_id`。 复用已有任务标识。 |

## BSS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `BSS/ShowRealNameAuthStatus/v2` · 助 | 查询实名认证状态 | 读取 | — 帮助使用区域 cn-north-1。 |

## CFW

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CFW/CreateCaptureTask/v1` · 助 | 创建抓包任务 | 抓包任务 | 需 `fw_instance_id`。 |
| `CFW/ListAccessControlLogs/v1` · 助 | 查询访问控制日志 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListAclRuleHitCount/v1` · 助 | 获取规则击中次数 | 读取 | — |
| `CFW/ListAclRuleHitStatus/v1` · 助 | 获取规则的命中次数和最后一次命中时间 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListAclRules/v1` · 助 | 查询防护规则 | 读取 | 需 `object_id`。 |
| `CFW/ListAddressItems/v1` · 助 | 查询地址组成员 | 读取 | 需 `set_id`。 |
| `CFW/ListAddressSetDetail/v1` · 助 | 查询地址组详细信息 | 读取 | 需 `set_id`。 |
| `CFW/ListAddressSets/v1` · 助 | 查询地址组列表 | 读取 | 需 `object_id`。 |
| `CFW/ListAdvancedIpsRules/v1` · 助 | 查询频率IPS规则信息 | 读取 | 需 `object_id`。 |
| `CFW/ListAlarmWhitelist/v1` · 助 | 查看EIP告警白名单 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListAttackLogs/v1` · 助 | 查询攻击日志 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListAttackStatistic/v1` · 助 | 查询攻击统计 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListBlackWhiteLists/v1` · 助 | 查询黑白名单列表 | 读取 | 需 `object_id`。 |
| `CFW/ListCaptureResult/v1` · 助 | 获取抓包任务结果 | 读取 | 需 `fw_instance_id`、`task_id`。 复用已有任务标识。 |
| `CFW/ListCaptureTask/v1` · 助 | 查询抓包任务 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListCustomerIps/v1` · 助 | 查看自定义IPS规则列表 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListDnsServers/v1` · 助 | 查询DNS服务器列表 | 读取 | — |
| `CFW/ListDomainParseDetail/v1` · 助 | 查询域名解析IP地址 | 读取 | 需 `domain_name`。 |
| `CFW/ListDomainParseIp/v1` · 助 | 获取域名地址解析结果 | 读取 | 需 `domain_address_id`、`domain_set_id`、`fw_instance_id`。 |
| `CFW/ListDomainResolveIp/v1` · 助 | 获取域名解析结果 | 读取 | 需 `domain_address_id`、`fw_instance_id`。 |
| `CFW/ListDomainSets/v1` · 助 | 查询域名组列表 | 读取 | 需 `fw_instance_id`、`object_id`。 |
| `CFW/ListDomains/v1` · 助 | 获取域名组下域名列表 | 读取 | 需 `domain_set_id`、`fw_instance_id`。 |
| `CFW/ListEastWestFirewall/v1` · 助 | 获取东西向防火墙信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListEipCount/v1` · 助 | 查询EIP数量 | 读取 | 需 `object_id`。 |
| `CFW/ListEips/v1` · 助 | 弹性IP列表查询 | 读取；sync 可触发同步 | 只查询已有数据时用 sync=0；sync=1 会同步租户 EIP。 |
| `CFW/ListFirewallDetail/v1` · 助 | 查询防火墙详细信息 | 读取 | — |
| `CFW/ListFirewallList/v1` · 助 | 查询防火墙列表 | 读取 | — |
| `CFW/ListFlowLogs/v1` · 助 | 查询流日志 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListFlowStatistic/v1` · 助 | 查询流量日志统计 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListIpBlacklist/v1` · 助 | 获取导入的IP黑名单列表信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListIpBlacklistSwitch/v1` · 助 | 获取流量过滤功能的开关信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListIpsProtectMode/v1` · 助 | 查询防护模式 | 读取 | 需 `object_id`。 |
| `CFW/ListIpsRules/v1` · 助 | 获取IPS规则列表 | 读取 | 需 `object_id`。 |
| `CFW/ListIpsSwitchStatus/v1` · 助 | 查询IPS特性开关状态 | 读取 | 需 `object_id`。 |
| `CFW/ListIpsWhitelists/v1` · 助 | 查询IPS白名单列表详情 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListJob/v1` · 助 | 获取CFW任务执行状态 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `CFW/ListLogConfig/v1` · 助 | 获取日志配置 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListLogs/v1` · 助 | 查询防火墙日志 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListPrivateNetworkSegments/v1` · 助 | 获取私网网段的信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ListProtectedVpcs/v1` · 助 | 查询防护VPC数 | 读取 | 需 `object_id`。 |
| `CFW/ListSchedules/v1` · 助 | 查询时间表列表 | 读取 | 需 `object_id`。 |
| `CFW/ListServiceItems/v1` · 助 | 查询服务成员列表 | 读取 | 需 `set_id`。 |
| `CFW/ListServiceSetDetail/v1` · 助 | 查询服务组详情 | 读取 | 需 `set_id`。 |
| `CFW/ListServiceSets/v1` · 助 | 获取服务组列表 | 读取 | 需 `object_id`。 |
| `CFW/ShowAccessDetail/v1` · 助 | 查询访问控制统计详情 | 读取 | 需 `fw_instance_id`、`item_id`。 |
| `CFW/ShowAccessTop/v1` · 助 | 查询访问日志统计信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAlarmConfig/v1` · 助 | 获取告警配置信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAntiVirusRule/v1` · 助 | 获取防火墙反病毒规则信息 | 读取 | 需 `object_id`。 |
| `CFW/ShowAntiVirusSwitch/v1` · 助 | 查看反病毒开关 | 读取 | 需 `object_id`。 |
| `CFW/ShowAttackDetail/v1` · 助 | 查询攻击日志统计详情 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAttackTop/v1` · 助 | 查询攻击日志TOP统计 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAttackTotal/v1` · 助 | 查询攻击概览 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAttackTrend/v1` · 助 | 查询攻击趋势 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowAutoProtectStatus/v1` · 助 | 获取EIP自动防护状态信息 | 读取 | 需 `object_id`。 |
| `CFW/ShowConfigQuota/v1` · 助 | 查询防火墙配额信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowCustomerIpsInfo/v1` · 助 | 查询自定义IPS规则详情 | 读取 | 需 `ips_cfw_id`、`fw_instance_id`。 |
| `CFW/ShowDomainSetDetail/v1` · 助 | 查看域名组详情 | 读取 | 需 `domain_set_id`、`fw_instance_id`。 |
| `CFW/ShowEwAssociatedEr/v1` · 助 | 查询VPC间防火墙使用的企业路由器信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowEwAssociatedVpc/v1` · 助 | 查询VPC边界防火墙使用的引流VPC信息 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowFlowDetail/v1` · 助 | 查询流量日志统计详情 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowFlowTop/v1` · 助 | 查询流量TOP统计 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowFlowTrend/v1` · 助 | 查询会话趋势 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowIpsUpdateTime/v1` · 助 | 获取IPS规则细节 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowLogsCount/v1` · 助 | 查询日志数量 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowSnFirewallProtectionStatus/v1` · 助 | 查询南北向防火墙防护状态 | 读取 | 需 `fw_instance_id`。 |
| `CFW/ShowTrafficTrend/v1` · 助 | 查询流量趋势 | 读取 | 需 `fw_instance_id`。 |

## Config

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `Config/ListPolicyAssignments/v1` · 助 | 列出合规规则 | 读取 | — |
| `Config/ListPolicyStatesByResourceId/v1` · 助 | 获取资源的合规结果 | 读取 | 需 `resource_id`。 |
| `Config/ListRemediationExecutionStatuses/v1` · 助 | 查询修正执行结果 | 读取 | 需 `policy_assignment_id`。 |
| `Config/ShowEvaluationStateByAssignmentId/v1` · 助 | 获取规则的评估状态 | 读取 | 需 `policy_assignment_id`。 |
| `Config/ShowRemediationConfiguration/v1` · 助 | 查询修正配置 | 读取 | 需 `policy_assignment_id`。 |

## IAM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `IAM/GetAccountSummaryV5/v5` · 助 | 获取此账号中IAM实体使用情况和IAM配额的摘要信息 | 读取 | — |
| `IAM/GetFeatureStatusV5/v5` · 助 | 获取此账号的功能状态 | 读取 | 需 `feature_name`。 |
| `IAM/GetPolicyV5/v5` · 助 | 通过身份策略ID获取身份策略 | 读取 | 需 `policy_id`。 |
| `IAM/GetPolicyVersionV5/v5` · 助 | 查询指定身份策略版本 | 读取 | 需 `policy_id`、`version_id`。 |
| `IAM/KeystoneListAllProjectPermissionsForGroup/v3` · 助 | 查询用户组的所有项目权限列表 | 读取 | 需 `group_id`。 |
| `IAM/KeystoneListDomainPermissionsForGroup/v3` · 助 | 查询全局服务中的用户组权限 | 读取 | 需 `group_id`。 |
| `IAM/KeystoneListGroupsForUser/v3` · 助 | 查询IAM用户所属用户组 | 读取 | 需 `user_id`。 |
| `IAM/KeystoneListProjectPermissionsForGroup/v3` · 助 | 查询项目服务中的用户组权限 | 读取 | 需 `group_id`。 |
| `IAM/ListAgencies/v3` · 助 | 查询指定条件下的委托列表 | 读取 | — |
| `IAM/ListAllProjectsPermissionsForAgency/v3` · 助 | 查询委托下的所有项目服务权限列表 | 读取 | 需 `agency_id`。 |
| `IAM/ListAttachedAgencyPoliciesV5/v5` · 助 | 查询指定委托或信任委托附加的所有身份策略 | 读取 | 需 `agency_id`。 |
| `IAM/ListAttachedGroupPoliciesV5/v5` · 助 | 查询指定用户组附加的所有身份策略 | 读取 | 需 `group_id`。 |
| `IAM/ListAttachedUserPoliciesV5/v5` · 助 | 查询指定IAM用户附加的所有身份策略 | 读取 | 需 `user_id`。 |
| `IAM/ListCustomPolicies/v3` · 助 | 查询自定义策略列表 | 读取 | — |
| `IAM/ListDomainPermissionsForAgency/v3` · 助 | 查询全局服务中的委托权限 | 读取 | 需 `agency_id`。 |
| `IAM/ListEnterpriseProjectsForUser/v3` · 助 | 查询用户直接关联的企业项目 | 读取 | 需 `user_id`。 |
| `IAM/ListPermanentAccessKeys/v3` · 助 | 查询所有永久访问密钥 | 读取 | — |
| `IAM/ListProjectPermissionsForAgency/v3` · 助 | 查询项目服务中的委托权限 | 读取 | 需 `agency_id`。 |
| `IAM/ListRolesForUserOnEnterpriseProject/v3` · 助 | 查询企业项目直接关联用户的权限 | 读取 | 需 `enterprise_project_id`、`user_id`。 |
| `IAM/ShowAccessKeyLastUsedV5/v5` · 助 | 查询指定永久访问密钥最后使用时间 | 读取 | 需 `access_key_id`、`user_id`。 |
| `IAM/ShowAgency/v3` · 助 | 查询委托详情 | 读取 | 需 `agency_id`。 |
| `IAM/ShowCustomPolicy/v3` · 助 | 查询自定义策略详情 | 读取 | 需 `role_id`。 |
| `IAM/ShowDomainApiAclPolicy/v3` · 助 | 查询账号接口访问策略 | 读取 | — |
| `IAM/ShowDomainConsoleAclPolicy/v3` · 助 | 查询账号控制台访问策略 | 读取 | — |
| `IAM/ShowDomainQuota/v3` · 助 | 查询账号配额 | 读取 | — |
| `IAM/ShowDomainRoleAssignments/v3` · 助 | 查询指定账号中的授权记录 | 读取 | — |
| `IAM/ShowPermanentAccessKey/v3` · 助 | 查询指定永久访问密钥 | 读取 | 需 `access_key`。 |
| `IAM/ShowProjectQuota/v3` · 助 | 查询项目配额 | 读取 | — |
| `IAM/ShowUser/v3` · 助 | 查询IAM用户详情(推荐) | 读取 | 需 `user_id`。 |
| `IAM/ShowUserLoginProtect/v3` · 助 | 查询指定IAM用户的登录保护状态信息 | 读取 | 需 `user_id`。 |
| `IAM/ShowUserV5/v5` · 助 | 查询IAM用户详情 | 读取 | 需 `user_id`。 |

## IAMAccessAnalyzer

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `IAMAccessAnalyzer/CheckNoNewAccess/v1` · 助 | 校验策略是否有新访问权限 | 校验 | — 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/CreateAccessPreview/v1` · 助 | 创建访问预览 | 创建分析 | 需 `analyzer_id`、`resource_urn`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListAccessPreviewFindings/v1` · 助 | 获取相关预览生成的分析结果 | 读取 | 需 `access_preview_id`、`analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListAccessPreviews/v1` · 助 | 获取所有访问预览 | 读取 | 需 `analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListAnalyzers/v1` · 助 | 检索分析器的列表 | 读取 | — 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListArchiveRules/v1` · 助 | 检索为指定分析器创建的存档规则的列表 | 读取 | 需 `analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListFindings/v1` · 助 | 检索指定分析器生成的访问分析结果列表 | 读取 | 需 `analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListNotificationSettings/v1` · 助 | 获取消息通知配置列表 | 读取 | — 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ListResourceConfigurations/v1` · 助 | 列举资源分析配置 | 读取 | 需 `analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ShowAccessPreview/v1` · 助 | 获取相关访问预览的信息 | 读取 | 需 `access_preview_id`、`analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ShowAnalyzer/v1` · 助 | 显示指定的分析器 | 读取 | 需 `analyzer_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ShowArchiveRule/v1` · 助 | 检索有关存档规则的信息 | 读取 | 需 `analyzer_id`、`archive_rule_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ShowFinding/v1` · 助 | 检索有关指定结果的信息 | 读取 | 需 `analyzer_id`、`finding_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ShowNotificationSetting/v1` · 助 | 获取消息通知配置 | 读取 | 需 `notification_setting_id`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/StartResourceScan/v1` · 助 | 立即开始扫描应用于指定资源的策略 | 策略扫描 | 需 `analyzer_id`、`resource_urn`。 帮助使用区域 ap-southeast-4。 |
| `IAMAccessAnalyzer/ValidatePolicy/v1` · 助 | 校验策略 | 校验 | — 帮助使用区域 ap-southeast-4。 |

## RMS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `RMS/ListPolicyAssignments/v1` · 助 | 列出合规规则 | 读取 | — |
| `RMS/ListPolicyStatesByResourceId/v1` · 助 | 获取资源的合规结果 | 读取 | 需 `resource_id`。 |
| `RMS/ShowEvaluationStateByAssignmentId/v1` · 助 | 获取规则的评估状态 | 读取 | 需 `policy_assignment_id`。 |

## SecMaster

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `SecMaster/ChangeAlert/v1` · 助 | 更新告警 | 修改或执行 | 需 `alert_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ChangeIncident/v1` · 助 | 更新事件 | 修改或执行 | 需 `incident_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ChangePlaybookInstance/v1` · 助 | 操作剧本实例 | 操作剧本 | 需 `instance_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/CreateAdhocQuery/v2` · 助 | 创建adhoc查询 | 查询任务 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/CreateAlertRuleSimulation/v1` · 助 | 模拟告警规则 | 模拟任务 | 需 `workspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/CreateSearchAnalysis/v1` · 助 | 执行分析 | 分析任务 | 需 `workspace_id`、`dataspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/CreateTableAnalysis/v2` · 助 | 创建安全分析查询 | 分析任务 | 需 `table_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/CreateWorkflowInstance/v1` · 助 | 创建流程实例 | 执行流程 | 需 `workflow_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListAlerts/v1` · 助 | 搜索告警列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListAopWorkflowInstance/v1` · 助 | 查询流程实例的列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListCloudLogResources/v1` · 助 | 列出云日志资源 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListCollectConfig/v1` · 助 | 获取云服务采集配置 | 读取 | — |
| `SecMaster/ListCollectConfig/v2` · 助 | 获取云服务采集配置 | 读取 | — |
| `SecMaster/ListCollectorChannels/v1` · 助 | 列出采集通道列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListCollectorConnections/v1` · 助 | 列表采集连接 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListCollectorInstances/v1` · 助 | 列出采集通道实例 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListCollectorNode/v1` · 助 | 列出采集节点 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListDataobjectRelations/v1` · 助 | 查询关联数据对象列表 | 读取 | 需 `data_object_id`、`dataclass_type`、`related_dataclass_type`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListDataobjects/v1` · 助 | 列出所有数据对象 | 读取 | 需 `dataclass_name`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListDataspaces/v1` · 助 | 获取数据空间列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListIncidents/v1` · 助 | 搜索事件列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListIndicators/v1` · 助 | 查询威胁情报列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListNotes/v1` · 助 | 搜索评论列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListPipes/v1` · 助 | 获取数据管道列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListPipes/v2` · 助 | 获取管道列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListPlaybookAuditLogs/v1` · 助 | 查询剧本实例审计日志 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListPlaybookInstances/v1` · 助 | 查询剧本实例列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListPlaybooks/v1` · 助 | 查询剧本列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListReports/v1` · 助 | 获取报告列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListResources/v1` · 助 | 搜索资产列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListSearchConditions/v1` · 助 | 获取检索条件列表 | 读取 | 需 `workspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListSearchHistograms/v1` · 助 | 获取数据分布直方图 | 读取 | 需 `workspace_id`、`dataspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListSearchLogs/v1` · 助 | 获取检索数据 | 读取 | 需 `workspace_id`、`dataspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListShippers/v1` · 助 | 查询投递信息 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListTableHistograms/v2` · 助 | 检索表直方图 | 读取 | 需 `table_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListTableLogs/v2` · 助 | 检索表日志 | 读取 | 需 `table_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListTables/v2` · 助 | 获取表列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListTasks/v1` · 助 | 查询待办列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListVulnerabilities/v1` · 助 | 查询漏洞列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ListWorkspaces/v1` · 助 | 查询工作空间列表 | 读取 | — |
| `SecMaster/SearchBaseline/v2` · 助 | 搜索基线检查结果列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/SearchCheckitems/v2` · 助 | 查询检查项列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/SearchCompliancePackages/v2` · 助 | 查询遵从包列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/SearchPolicy/v1` · 助 | 查询策略视图列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/SearchPolicyRecord/v1` · 助 | 查询任务视图列表 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/SearchPolicyRecordByPolicyId/v1` · 助 | 根据策略ID查询历史记录列表 | 读取 | 需 `policy_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowAdhocResult/v2` · 助 | 获取adhoc查询结果 | 读取 | 需 `query_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowAlert/v1` · 助 | 获取告警详情 | 读取 | 需 `alert_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowAopWorkflowInstance/v1` · 助 | 查询流程实例的详情 | 读取 | 需 `instance_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowCheckitemDetail/v2` · 助 | 查询检查项详情 | 读取 | 需 `checkitem_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowCompliancePackageDetail/v2` · 助 | 查询遵从包详情 | 读取 | 需 `compliance_packages_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowDataobject/v1` · 助 | 查询数据对象 | 读取 | 需 `data_object_id`、`dataclass_name`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowDataspace/v1` · 助 | 获取数据空间详情 | 读取 | 需 `dataspace_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowIncident/v1` · 助 | 获取事件详情 | 读取 | 需 `incident_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowIndicatorDetail/v1` · 助 | 查询威胁情报详情 | 读取 | 需 `indicator_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowMoniterMetricStats/v1` · 助 | 获取指标统计数据 | 读取 | 需 `workspace_id`、`dataspace_id`、`pipe_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowMonitorStats/v2` · 助 | 获取监控统计信息 | 读取 | 需 `table_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPipe/v1` · 助 | 获取数据管道详情 | 读取 | 需 `pipe_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPipe/v2` · 助 | 获取管道详情 | 读取 | 需 `pipe_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPlaybook/v1` · 助 | 查询剧本详情 | 读取 | 需 `playbook_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPlaybookInstance/v1` · 助 | 查询剧本实例详情 | 读取 | 需 `instance_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPlaybookMonitors/v1` · 助 | 剧本运行监控 | 读取 | 需 `playbook_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPlaybookStatistics/v1` · 助 | 剧本数据统计 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPlaybookTopology/v1` · 助 | 查询剧本拓扑关系 | 读取 | 需 `instance_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowPolicy/v1` · 助 | 查询策略视图对象 | 读取 | 需 `policy_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowReportInfo/v1` · 助 | 获取报告详情 | 读取 | 需 `report_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowResource/v1` · 助 | 获取资产详情 | 读取 | 需 `id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowSearchCondition/v1` · 助 | 获取检索条件详情 | 读取 | 需 `condition_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowShipper/v1` · 助 | 投递规则详情 | 读取 | 需 `shipper_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowTable/v2` · 助 | 获取表详情 | 读取 | 需 `table_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowTask/v1` · 助 | 查询待办的详情 | 读取 | 需 `task_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 复用已有任务标识。 |
| `SecMaster/ShowVulnerability/v1` · 助 | 获取漏洞详情 | 读取 | 需 `vul_id`、`workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |
| `SecMaster/ShowWorkspace/v1` · 助 | 查询工作空间详情 | 读取 | 需 `workspace_id`。 未知 workspace_id 时查 [SecMaster/ListWorkspaces/v1](security.md#secmaster)。 |

## WAF

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `WAF/CheckAgency/v1` · 助 | 查询独享引擎代理 | 读取 | — |
| `WAF/ConfirmAsyncJob/v1` · 助 | 查询异步任务详情 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `WAF/ConfirmDnsDomain/v1` · 助 | 查询用户托管在云解析上的域名 | 读取 | — |
| `WAF/ConfirmIpReputationRule/v1` · 助 | 根据Id查询威胁情报访问控制规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ListAntiTamperPolicyRules/v1` · 助 | 查询所有策略网页防篡改 | 读取 | — |
| `WAF/ListAnticrawlerRules/v1` · 助 | 查询JS脚本反爬虫规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListAntileakagePolicyRules/v1` · 助 | 查询所有策略防敏感信息泄露规则 | 读取 | — |
| `WAF/ListAntileakageRules/v1` · 助 | 查询防敏感信息泄露规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListAntitamperRule/v1` · 助 | 查询防篡改规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListAttackActionTypes/v1` · 助 | 查询攻击防护类型 | 读取 | — |
| `WAF/ListBandwidthTimeline/v1` · 助 | 查询安全统计带宽数据 | 读取 | — |
| `WAF/ListCcPolicyRules/v1` · 助 | 查询所有策略CC规则 | 读取 | — |
| `WAF/ListCcRules/v1` · 助 | 查询cc规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListCertificates/v1` · 助 | 查询证书列表 | 读取 | — |
| `WAF/ListCompositeHosts/v1` · 助 | 查询全部防护域名列表 | 读取 | — |
| `WAF/ListCustomPolicyRules/v1` · 助 | 查询所有策略精准防护规则 | 读取 | — |
| `WAF/ListCustomRules/v1` · 助 | 查询精准防护规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListEvent/v1` · 助 | 查询攻击事件列表 | 读取 | — |
| `WAF/ListEventLog/v1` · 助 | 查询事件日志下载的url | 读取下载地址 | — |
| `WAF/ListGeoIpPolicyRules/v1` · 助 | 查询所有策略地理位置访问控制 | 读取 | — |
| `WAF/ListGeoipRule/v1` · 助 | 查询地理位置访问控制规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListHost/v1` · 助 | 查询云模式防护域名列表 | 读取 | — |
| `WAF/ListHostRoute/v1` · 助 | 获取云模式域名路由信息 | 读取 | 需 `instance_id`。 |
| `WAF/ListIgnorePolicyRules/v1` · 助 | 查询所有策略全局白名单 | 读取 | — |
| `WAF/ListIgnoreRule/v1` · 助 | 查询全局白名单(原误报屏蔽)规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListInstance/v1` · 助 | 查询WAF独享引擎列表 | 读取 | — |
| `WAF/ListInstancePools/v1` · 助 | 查询实例组列表 | 读取 | — |
| `WAF/ListInstanceStatus/v1` · 助 | 查询WAF独享引擎状态列表 | 读取 | — |
| `WAF/ListIpGroup/v1` · 助 | 查询地址组列表 | 读取 | — |
| `WAF/ListIpReputationPolicyRules/v1` · 助 | 查询所有策略威胁情报控制规则 | 读取 | — |
| `WAF/ListIpReputationRules/v1` · 助 | 查询威胁情报规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListOverviewsClassification/v1` · 助 | 查询安全总览分类统计top信息 | 读取 | — |
| `WAF/ListOverviewsHostDomains/v1` · 助 | 查询泛域名的防护事件中的子域名,仅泛域名存在子域名 | 读取 | 需 `host_id`。 |
| `WAF/ListPolicy/v1` · 助 | 查询防护策略列表 | 读取 | — |
| `WAF/ListPolicyProtectRules/v1` · 助 | 查询所有策略指定类型的防护规则 | 读取 | 需 `rule_type`。 |
| `WAF/ListPremiumHost/v1` · 助 | 查询独享模式域名列表 | 读取 | — |
| `WAF/ListPrivacyPolicyRules/v1` · 助 | 查询所有策略隐私屏蔽防护规则 | 读取 | — |
| `WAF/ListPrivacyRule/v1` · 助 | 查询隐私屏蔽防护规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListPunishmentRules/v1` · 助 | 查询攻击惩罚规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ListQpsTimeline/v1` · 助 | 查询安全统计qps次数 | 读取 | — |
| `WAF/ListRequestTimeline/v1` · 助 | 查询安全总览中请求次数时间线统计数据 | 读取 | — |
| `WAF/ListResponseCodeTimeline/v1` · 助 | 查询安全统计响应码数据 | 读取 | — |
| `WAF/ListSourceIpTop5/v1` · 助 | 查询攻击源ip | 读取 | — |
| `WAF/ListStatistics/v1` · 助 | 查询安全总览请求与攻击数量 | 读取 | — |
| `WAF/ListThreats/v1` · 助 | 查询攻击事件分布类型 | 读取 | — |
| `WAF/ListTopAbnormal/v1` · 助 | 查询业务异常数量 | 读取 | — |
| `WAF/ListTopDomains/v1` · 助 | 查询top受攻击域名 | 读取 | — |
| `WAF/ListTopIp/v1` · 助 | 查询攻击源ip | 读取 | — |
| `WAF/ListTopUrl/v1` · 助 | 查询被攻击url | 读取 | — |
| `WAF/ListUrl/v1` · 助 | 查询事件日志中的url | 读取 | — |
| `WAF/ListValueList/v1` · 助 | 查询引用表列表 | 读取 | — |
| `WAF/ListWebBasicProtectionRules/v1` · 助 | 查询web基础防护内置规则列表 | 读取 | — |
| `WAF/ListWhiteblackipPolicyRules/v1` · 助 | 查询所有策略黑白名单防护规则 | 读取 | — |
| `WAF/ListWhiteblackipRule/v1` · 助 | 查询黑白名单规则列表 | 读取 | 需 `policy_id`。 |
| `WAF/ShowAnticrawlerRule/v1` · 助 | 查询JS脚本反爬虫防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowAntileakageRule/v1` · 助 | 查询防敏感信息泄露防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowAntitamperRule/v1` · 助 | 查询防篡改防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowCcRule/v1` · 助 | 根据Id查询cc防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowCompositeHost/v1` · 助 | 根据Id查询防护域名 | 读取 | 需 `host_id`。 |
| `WAF/ShowConsoleConfig/v1` · 助 | 局点支持特性查询 | 读取 | — |
| `WAF/ShowCustomRule/v1` · 助 | 根据Id查询精准防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowEvent/v1` · 助 | 查询指定事件id的防护事件详情 | 读取 | 需 `eventid`。 |
| `WAF/ShowGeoipRule/v1` · 助 | 查询地理位置控制防护规则详情 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowHost/v1` · 助 | 根据防护域名Id查询云模式防护域名详细信息 | 读取 | 需 `instance_id`。 |
| `WAF/ShowHostStatus/v1` · 助 | 查询域名运行状态 | 读取 | 需 `host_id`。 |
| `WAF/ShowIgnoreRule/v1` · 助 | 查询全局白名单(原误报屏蔽)防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowInstance/v1` · 助 | 查询WAF独享引擎信息 | 读取 | 需 `instance_id`。 |
| `WAF/ShowIpGroup/v1` · 助 | 查询ip地址组明细 | 读取 | 需 `id`。 |
| `WAF/ShowLtsInfoConfig/v1` · 助 | 查询lts配置信息 | 读取 | — |
| `WAF/ShowPolicy/v1` · 助 | 根据Id查询防护策略 | 读取 | 需 `policy_id`。 |
| `WAF/ShowPool/v1` · 助 | 查询实例组详情 | 读取 | 需 `pool_id`。 |
| `WAF/ShowPremiumHost/v1` · 助 | 查看独享模式域名配置 | 读取 | 需 `host_id`。 |
| `WAF/ShowPrivacyRule/v1` · 助 | 查询隐私屏蔽防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowPunishmentRule/v1` · 助 | 根据Id查询攻击惩罚防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
| `WAF/ShowSourceIp/v1` · 助 | 查询WAF回源Ip信息 | 读取 | — |
| `WAF/ShowValueList/v1` · 助 | 查询引用表 | 读取 | 需 `valuelistid`。 |
| `WAF/ShowWebProtectionRule/v1` · 助 | 根据Id查询Web防护规则 | 读取 | 需 `rule_id`。 |
| `WAF/ShowWhiteBlackIpRule/v1` · 助 | 查询黑白名单防护规则 | 读取 | 需 `policy_id`、`rule_id`。 |
