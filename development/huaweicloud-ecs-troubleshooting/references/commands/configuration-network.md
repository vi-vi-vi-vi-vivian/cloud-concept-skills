# 网络配置 C

核对实际路径中的网络配置。配置正常不等于端到端可达。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[CC](#cc) · [DNS](#dns) · [EIP](#eip) · [ELB](#elb) · [ER](#er) · [NAT](#nat) · [VPC](#vpc) · [VPCEP](#vpcep) · [VPN](#vpn)

## CC

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CC/ListAuthorisations/v3` · 助 | 查询授权列表 | 读取 | — |
| `CC/ListBandwidthPackages/v3` · 助 | 查询带宽包列表 | 读取 | — |
| `CC/ListCentralNetworkAttachments/v3` · 助 | 查询中心网络附件列表 | 读取 | 需 `central_network_id`。 |
| `CC/ListCentralNetworkConnections/v3` · 助 | 查询中心网络连接列表 | 读取 | 需 `central_network_id`。 |
| `CC/ListCentralNetworkErRouteTableAttachments/v3` · 助 | 查询中心网络ER路由表附件列表 | 读取 | 需 `central_network_id`。 |
| `CC/ListCentralNetworkGdgwAttachments/v3` · 助 | 查询中心网络GDGW附件列表 | 读取 | 需 `central_network_id`。 |
| `CC/ListCentralNetworkPolicies/v3` · 助 | 查询所有版本的中心网络策略列表 | 读取 | 需 `central_network_id`。 |
| `CC/ListCentralNetworkPolicyChangeSet/v3` · 助 | 查询中心网络策略变化集 | 读取 | 需 `central_network_id`、`policy_id`。 |
| `CC/ListCentralNetworkQuotas/v3` · 助 | 查询中心网络配额 | 读取 | — |
| `CC/ListCentralNetworks/v3` · 助 | 查询中心网络列表 | 读取 | — |
| `CC/ListCloudConnectionQuotas/v3` · 助 | 查询云连接配额 | 读取 | — |
| `CC/ListCloudConnectionRoutes/v3` · 助 | 查询云连接路由条目列表 | 读取 | — |
| `CC/ListCloudConnections/v3` · 助 | 查询云连接列表 | 读取 | — |
| `CC/ListGlobalConnectionBandwidthConfigs/v3` · 助 | 查询全域互联带宽租户配置信息 | 读取 | — |
| `CC/ListGlobalConnectionBandwidths/v3` · 助 | 查询全域互联带宽列表 | 读取 | — |
| `CC/ListInterRegionBandwidths/v3` · 助 | 查询域间带宽列表 | 读取 | — |
| `CC/ListNetworkInstances/v3` · 助 | 查询网络实例列表 | 读取 | — |
| `CC/ListPermissions/v3` · 助 | 查询权限列表 | 读取 | — |
| `CC/ListSiteNetworkQuotas/v3` · 助 | 查询分支网络配额 | 读取 | — |
| `CC/ListSiteNetworks/v3` · 助 | 查询分支网络列表 | 读取 | — |
| `CC/ShowBandwidthPackage/v3` · 助 | 查询带宽包实例 | 读取 | 需 `id`。 |
| `CC/ShowCentralNetwork/v3` · 助 | 查询中心网络详情 | 读取 | 需 `central_network_id`。 |
| `CC/ShowCentralNetworkErRouteTableAttachment/v3` · 助 | 查询中心网络ER路由表附件详情 | 读取 | 需 `central_network_id`、`er_route_table_attachment_id`。 |
| `CC/ShowCentralNetworkGdgwAttachment/v3` · 助 | 查询中心网络GDGW附件详情 | 读取 | 需 `central_network_id`、`gdgw_attachment_id`。 |
| `CC/ShowCloudConnection/v3` · 助 | 查询云连接实例 | 读取 | 需 `id`。 |
| `CC/ShowCloudConnectionRoutes/v3` · 助 | 查询云连接路由条目详情 | 读取 | 需 `id`。 |
| `CC/ShowGlobalConnectionBandwidth/v3` · 助 | 查询全域互联带宽详情 | 读取 | 需 `id`。 |
| `CC/ShowInterRegionBandwidth/v3` · 助 | 查询域间带宽实例 | 读取 | 需 `id`。 |
| `CC/ShowNetworkInstance/v3` · 助 | 查询网络实例 | 读取 | 需 `id`。 |
| `CC/ShowSiteNetwork/v3` · 助 | 查询分支网络详情 | 读取 | 需 `site_network_id`。 |

## DNS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `DNS/ListBatchOperationTasks/v2` · 助 | 查询批量操作任务列表 | 读取 | — |
| `DNS/ListCustomLine/v2` · 助 | 查询自定义线路 | 读取 | — |
| `DNS/ListEndpointIpaddresses/v2` · 助 | 查询IP地址列表 | 读取 | 需 `endpoint_id`。 |
| `DNS/ListEndpointVpcs/v2` · 助 | 查询终端节点VPC列表 | 读取 | — |
| `DNS/ListEndpoints/v2` · 助 | 查询终端节点列表 | 读取 | — |
| `DNS/ListInstances/v2` · 助 | 批量查询DNS解析量统计相关的资源 | 读取 | — |
| `DNS/ListLineGroups/v2` · 助 | 查询线路分组列表 | 读取 | — |
| `DNS/ListNameServers/v2` · 助 | 查询名称服务器列表 | 读取 | — |
| `DNS/ListPrivateZones/v2` · 助 | 查询内网域名列表 | 读取 | — |
| `DNS/ListPtrRecords/v2` · 助 | 查询弹性公网IP的反向解析记录列表 | 读取 | — |
| `DNS/ListPtrs/v2` · 助 | 查询弹性公网IP的反向解析记录列表 | 读取 | — |
| `DNS/ListPublicZoneLines/v2` · 助 | 查询公网域名的线路列表 | 读取 | 需 `zone_id`。 |
| `DNS/ListPublicZones/v2` · 实·空 | 查询公网域名列表 | 读取 | — |
| `DNS/ListRecordSets/v2` · 助 | 查询租户记录集列表 | 读取 | — |
| `DNS/ListRecordSetsByZone/v2` · 助 | 查询域名下的记录集列表 | 读取 | 需 `zone_id`。 |
| `DNS/ListRecordSetsWithLine/v2` · 助 | 查询租户记录集列表 | 读取 | — |
| `DNS/ListResolverQueryLogConfigs/v2` · 助 | 查询解析器访问日志列表 | 读取 | — |
| `DNS/ListResolverRules/v2` · 助 | 查询解析器转发规则列表 | 读取 | — |
| `DNS/ListSystemLines/v2` · 助 | 查询系统线路 | 读取 | — |
| `DNS/ShowBatchCreateRecordSetsTask/v2` · 助 | 查询批量创建记录集任务 | 读取 | 需 `zone_id`。 |
| `DNS/ShowBatchOperationTask/v2` · 助 | 查询批量操作任务 | 读取 | 需 `task_id`。 复用已有任务标识。 |
| `DNS/ShowDnssecConfig/v2` · 助 | 查询DNSSEC | 读取 | 需 `zone_id`。 |
| `DNS/ShowDomainQuota/v2` · 助 | 查询租户配额 | 读取 | — |
| `DNS/ShowEmailRecordSet/v2` · 助 | 查询公网域名的邮箱域名 | 读取 | 需 `zone_id`。 |
| `DNS/ShowEndpoint/v2` · 助 | 查询终端节点 | 读取 | 需 `endpoint_id`。 |
| `DNS/ShowLineGroup/v2` · 助 | 查询线路分组 | 读取 | 需 `linegroup_id`。 |
| `DNS/ShowPrivateZone/v2` · 助 | 查询单个内网Zone | 读取 | 需 `zone_id`。 |
| `DNS/ShowPrivateZoneNameServer/v2` · 助 | 查询内网域名的名称服务器 | 读取 | 需 `zone_id`。 |
| `DNS/ShowPtr/v2` · 助 | 查询弹性公网IP的反向解析记录 | 读取 | 需 `ptr_id`。 |
| `DNS/ShowPtrRecordSet/v2` · 助 | 查询弹性公网IP的反向解析记录 | 读取 | 需 `floatingip_id`、`region`。 |
| `DNS/ShowPublicZone/v2` · 助 | 查询公网域名 | 读取 | 需 `zone_id`。 |
| `DNS/ShowPublicZoneNameServer/v2` · 助 | 查询公网域名的名称服务器 | 读取 | 需 `zone_id`。 |
| `DNS/ShowRecordSet/v2` · 助 | 查询记录集 | 读取 | 需 `recordset_id`、`zone_id`。 |
| `DNS/ShowRecordSetByZone/v2` · 助 | 查询域名下的记录集列表 | 读取 | 需 `zone_id`。 |
| `DNS/ShowRecordSetWithLine/v2` · 助 | 查询记录集 | 读取 | 需 `recordset_id`、`zone_id`。 |
| `DNS/ShowResolverQueryLogConfig/v2` · 助 | 查询解析器访问日志 | 读取 | 需 `id`。 |
| `DNS/ShowResolverRule/v2` · 助 | 查询解析器转发规则 | 读取 | 需 `resolverrule_id`。 |
| `DNS/ShowWebsiteRecordSet/v2` · 助 | 查询公网域名的网站域名 | 读取 | 需 `zone_id`。 |
| `DNS/ShowZoneNameServer/v2` · 助 | 查询公网域名的DNS服务器地址 | 读取 | 需 `domain_name`。 |

## EIP

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EIP/CountEipAvailableResources/v3` · 助 | 查询弹性公网IP可用数 | 读取 | — |
| `EIP/ListBandwidth/v3` · 助 | 查询带宽列表 | 读取 | — |
| `EIP/ListBandwidthPkg/v2` · 助 | 查询带宽加油包列表 | 读取 | — |
| `EIP/ListBandwidthRule/v3` · 助 | 全量查询带宽规则列表 | 读取 | 需 `bandwidth_id`。 |
| `EIP/ListBandwidths/v2` · 助 | 查询带宽列表 | 读取 | — |
| `EIP/ListBandwidthsLimit/v3` · 助 | 查看租户带宽限制 | 读取 | — |
| `EIP/ListEipBandwidths/v3` · 助 | 查询带宽列表 | 读取 | — |
| `EIP/ListProjectGeipBindings/v3` · 助 | 查询GEIP与实例绑定关系的租户列表 | 读取 | — |
| `EIP/ListPublicipPool/v3` · 助 | 查询公网IP池列表 | 读取 | — |
| `EIP/ListPublicips/v2` · 实 | 查询弹性公网IP列表 | 读取 | — |
| `EIP/ListPublicips/v3` · 助 | 全量查询弹性公网IP列表 | 读取 | — |
| `EIP/ListQuotas/v2` · 助 | 查询配额接口 | 读取 | — |
| `EIP/ListTenantVpcIgws/v3` · 助 | 查询指定租户下的虚拟igw列表 | 读取 | — |
| `EIP/NeutronListFloatingIps/v2` · 助 | 查询浮动IP列表 | 读取 | — |
| `EIP/NeutronShowFloatingIp/v2` · 助 | 查询浮动IP | 读取 | 需 `floatingip_id`。 |
| `EIP/ShowBandwidth/v2` · 实 | 查询带宽 | 读取 | bandwidth_id；从关联公网 IP 取得。 |
| `EIP/ShowBandwidthRule/v3` · 助 | 查询带宽规则 | 读取 | 需 `bandwidth_id`、`bandwidth_rules_id`。 |
| `EIP/ShowInternalVpcIgw/v3` · 助 | 查询虚拟igw详情 | 读取 | 需 `vpc_igw_id`。 |
| `EIP/ShowPublicip/v2` · 助 | 查询弹性公网IP | 读取 | 需 `publicip_id`。 |
| `EIP/ShowPublicip/v3` · 实 | 查询弹性公网IP详情 | 读取 | publicip_id；未知时查 [EIP/ListPublicips/v2](configuration-network.md#eip) 并匹配 port_id。 |
| `EIP/ShowPublicipPool/v3` · 助 | 查询公网IP池详情 | 读取 | 需 `publicip_pool_id`。 |

## ELB

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ELB/ListAllL7Rules/v3` · 助 | 查询转发规则全局列表 | 读取 | — |
| `ELB/ListAllMembers/v3` · 助 | 后端服务器全局列表 | 读取 | — |
| `ELB/ListCertificates/v2` · 助 | 查询SSL证书列表 | 读取 | — |
| `ELB/ListCertificates/v3` · 助 | 查询证书列表 | 读取 | — |
| `ELB/ListDomainIPs/v3` · 助 | 查询负载均衡器IP地址的域名解析配置 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ListFeatureConfigs/v3` · 助 | 查询当前租户ELB服务的特性配置 | 读取 | — |
| `ELB/ListFlavors/v3` · 助 | 查询规格列表 | 读取 | — |
| `ELB/ListHealthMonitors/v2` · 助 | 查询健康检查列表 | 读取 | — |
| `ELB/ListHealthMonitors/v3` · 助 | 查询健康检查列表 | 读取 | — |
| `ELB/ListIpGroups/v3` · 助 | 查询IP地址组列表 | 读取 | — |
| `ELB/ListL7Policies/v2` · 助 | 查询转发策略列表 | 读取 | — |
| `ELB/ListL7Policies/v3` · 助 | 查询转发策略列表 | 读取 | — |
| `ELB/ListL7Rules/v2` · 助 | 查询转发规则列表 | 读取 | 需 `l7policy_id`。 |
| `ELB/ListL7Rules/v3` · 助 | 查询转发规则列表 | 读取 | 需 `l7policy_id`。 |
| `ELB/ListListeners/v2` · 助 | 查询监听器列表 | 读取 | — |
| `ELB/ListListeners/v3` · 助 | 查询监听器列表 | 读取 | — |
| `ELB/ListLoadBalancers/v2` · 助 | 查询负载均衡列表 | 读取 | — |
| `ELB/ListLoadBalancers/v3` · 实·空 | 查询负载均衡器列表 | 读取 | — |
| `ELB/ListLoadbalancerFeature/v3` · 助 | 查询指定ELB实例的特性配置 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ListLogtanks/v3` · 助 | 查询云日志列表 | 读取 | — |
| `ELB/ListMasterSlavePools/v3` · 助 | 查询主备后端服务器组列表 | 读取 | — |
| `ELB/ListMembers/v2` · 助 | 查询后端云服务器列表 | 读取 | 需 `pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ListMembers/v3` · 助 | 查询后端服务器列表 | 读取 | 需 `pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ListPools/v2` · 助 | 查询后端云服务器组列表 | 读取 | — |
| `ELB/ListPools/v3` · 助 | 查询后端服务器组列表 | 读取 | — |
| `ELB/ListQuotaDetails/v3` · 助 | 查询配额使用详情 | 读取 | — |
| `ELB/ListSecurityPolicies/v3` · 助 | 查询自定义安全策略列表 | 读取 | — |
| `ELB/ListSystemSecurityPolicies/v3` · 助 | 查询系统安全策略列表 | 读取 | — |
| `ELB/ListWhitelists/v2` · 助 | 查询白名单列表 | 读取 | — |
| `ELB/ShowFlavor/v3` · 助 | 查询规格详情 | 读取 | 需 `flavor_id`。 |
| `ELB/ShowHealthMonitor/v3` · 助 | 查询健康检查详情 | 读取 | 需 `healthmonitor_id`。 |
| `ELB/ShowHealthmonitors/v2` · 助 | 查询健康检查详情 | 读取 | 需 `healthmonitor_id`。 |
| `ELB/ShowIpGroup/v3` · 助 | 查询IP地址组详情 | 读取 | 需 `ipgroup_id`。 |
| `ELB/ShowIpGroupRelatedListeners/v3` · 助 | 查询IP地址组关联的监听器列表 | 读取 | 需 `ipgroup_id`。 |
| `ELB/ShowL7Policy/v2` · 助 | 查询转发策略详情 | 读取 | 需 `l7policy_id`。 |
| `ELB/ShowL7Policy/v3` · 助 | 查询转发策略详情 | 读取 | 需 `l7policy_id`。 |
| `ELB/ShowL7Rule/v2` · 助 | 查询转发规则详情 | 读取 | 需 `l7policy_id`、`l7rule_id`。 |
| `ELB/ShowL7Rule/v3` · 助 | 查询转发规则详情 | 读取 | 需 `l7policy_id`、`l7rule_id`。 |
| `ELB/ShowListener/v2` · 助 | 查询监听器详情 | 读取 | 需 `listener_id`。 未知 listener_id 时查 [ELB/ListListeners/v3](configuration-network.md#elb)。 |
| `ELB/ShowListener/v3` · 助 | 查询监听器详情 | 读取 | 需 `listener_id`。 未知 listener_id 时查 [ELB/ListListeners/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadBalancer/v2` · 助 | 查询负载均衡详情 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadBalancer/v3` · 助 | 查询负载均衡器详情 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadBalancerPorts/v3` · 助 | 查询负载均衡内部转发用的IP | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadBalancerStatus/v3` · 助 | 查询负载均衡器状态树 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadBalancerTopology/v3` · 助 | 查询负载均衡器拓扑 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLoadbalancersStatus/v2` · 助 | 查询负载均衡状态树 | 读取 | 需 `loadbalancer_id`。 未知 loadbalancer_id 时查 [ELB/ListLoadBalancers/v3](configuration-network.md#elb)。 |
| `ELB/ShowLogtank/v3` · 助 | 查询云日志详情 | 读取 | 需 `logtank_id`。 |
| `ELB/ShowMasterSlavePool/v3` · 助 | 查询主备后端服务器组详情 | 读取 | 需 `pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ShowMember/v2` · 助 | 查询后端云服务器详情 | 读取 | 需 `member_id`、`pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ShowMember/v3` · 助 | 查询后端服务器详情 | 读取 | 需 `member_id`、`pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ShowPool/v2` · 助 | 查询后端云服务器组详情 | 读取 | 需 `pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ShowPool/v3` · 助 | 查询后端服务器组详情 | 读取 | 需 `pool_id`。 未知 pool_id 时查 [ELB/ListPools/v3](configuration-network.md#elb)。 |
| `ELB/ShowQuota/v3` · 助 | 查询配额详情 | 读取 | — |
| `ELB/ShowSecurityPolicy/v3` · 助 | 查询自定义安全策略详情 | 读取 | 需 `security_policy_id`。 |
| `ELB/ShowWhitelist/v2` · 助 | 查询白名单详情 | 读取 | 需 `whitelist_id`。 |

## ER

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ER/CreateFlowLog/v3` · 助 | 创建流日志 | 创建或配置 | 需 `er_id`、`flow_log.log_group_id`、`flow_log.log_stream_id`、`flow_log.resource_id`。 |
| `ER/EnableFlowLog/v3` · 助 | 开启流日志 | 修改或执行 | 需 `er_id`、`flow_log_id`。 |
| `ER/ListAssociations/v3` · 助 | 查询路由关联列表 | 读取 | 需 `er_id`、`route_table_id`。 |
| `ER/ListAttachments/v3` · 助 | 查询连接列表 | 读取 | 需 `er_id`。 |
| `ER/ListEffectiveRoutes/v3` · 助 | 查询有效路由列表 | 读取 | 需 `route_table_id`。 |
| `ER/ListEnterpriseRouters/v3` · 实·空 | 查询企业路由器列表 | 读取 | — |
| `ER/ListFlowLogs/v3` · 助 | 查询流日志列表 | 读取 | 需 `er_id`。 |
| `ER/ListPropagations/v3` · 助 | 查询路由传播列表 | 读取 | 需 `er_id`、`route_table_id`。 |
| `ER/ListRouteTables/v3` · 助 | 查询路由表列表 | 读取 | 需 `er_id`。 |
| `ER/ListStaticRoutes/v3` · 助 | 查询静态路由列表 | 读取 | 需 `route_table_id`。 |
| `ER/ListVpcAttachments/v3` · 助 | 查询VPC连接列表 | 读取 | 需 `er_id`。 |
| `ER/ShowAttachment/v3` · 助 | 查询连接详情 | 读取 | 需 `attachment_id`、`er_id`。 |
| `ER/ShowEnterpriseRouter/v3` · 助 | 查询企业路由器详情 | 读取 | 需 `er_id`。 |
| `ER/ShowFlowLog/v3` · 助 | 查询流日志详情 | 读取 | 需 `er_id`、`flow_log_id`。 |
| `ER/ShowQuotas/v3` · 助 | 查询配额 | 读取 | — |
| `ER/ShowRouteTable/v3` · 助 | 查询路由表详情 | 读取 | 需 `er_id`、`route_table_id`。 |
| `ER/ShowStaticRoute/v3` · 助 | 查询静态路由详情 | 读取 | 需 `route_id`、`route_table_id`。 |
| `ER/ShowVpcAttachment/v3` · 助 | 查询VPC连接详情 | 读取 | 需 `er_id`、`vpc_attachment_id`。 |

## NAT

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `NAT/ListNatGatewayDnatRules/v2` · 助 | 查询DNAT规则列表 | 读取 | — |
| `NAT/ListNatGatewaySnatRules/v2` · 助 | 查询SNAT规则列表 | 读取 | — |
| `NAT/ListNatGatewaySpecs/v2` · 助 | 支持创建的NAT网关规格列表 | 读取 | — |
| `NAT/ListNatGateways/v2` · 实·空 | 查询公网NAT网关列表 | 读取 | — |
| `NAT/ListPrivateDnats/v2` · 助 | 查询DNAT规则列表 | 读取 | — |
| `NAT/ListPrivateNats/v2` · 助 | 查询私网NAT网关列表 | 读取 | — |
| `NAT/ListPrivateSnats/v2` · 助 | 查询SNAT规则列表 | 读取 | — |
| `NAT/ListSpecs/v2` · 助 | 查询项目支持的网关规格列表 | 读取 | — |
| `NAT/ListTransitIps/v2` · 助 | 查询中转IP列表 | 读取 | — |
| `NAT/ListTransitSubnet/v2` · 助 | 查询中转子网列表 | 读取 | — |
| `NAT/ShowNatGateway/v2` · 助 | 查询指定的公网NAT网关详情 | 读取 | 需 `nat_gateway_id`。 |
| `NAT/ShowNatGatewayDnatRule/v2` · 助 | 查询指定的DNAT规则详情 | 读取 | 需 `dnat_rule_id`。 |
| `NAT/ShowNatGatewaySnatRule/v2` · 助 | 查询指定的SNAT规则详情 | 读取 | 需 `snat_rule_id`。 |
| `NAT/ShowPrivateDnat/v2` · 助 | 查询指定的DNAT规则详情 | 读取 | 需 `dnat_rule_id`。 |
| `NAT/ShowPrivateNat/v2` · 助 | 查询指定的私网NAT网关详情 | 读取 | 需 `gateway_id`。 |
| `NAT/ShowPrivateSnat/v2` · 助 | 查询指定的SNAT规则详情 | 读取 | 需 `snat_rule_id`。 |
| `NAT/ShowTransitIp/v2` · 助 | 查询指定的中转IP详情 | 读取 | 需 `transit_ip_id`。 |
| `NAT/ShowTransitSubnet/v2` · 助 | 查询指定的中转子网详情 | 读取 | 需 `transit_subnet_id`。 |

## VPC

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `VPC/CreateFlowLog/v2` · 助 | 创建流日志 | 创建或配置 | 需 `flow_log.log_group_id`、`flow_log.log_topic_id`、`flow_log.resource_id`。 |
| `VPC/CreateTrafficMirrorSession/v3` · 助 | 创建流量镜像会话 | 创建或配置 | 需 `traffic_mirror_session.traffic_mirror_filter_id`、`traffic_mirror_session.traffic_mirror_target_id`。 |
| `VPC/ListAddressGroup/v3` · 助 | 查询地址组列表 | 读取 | — |
| `VPC/ListAddressGroupsDependency/v3` · 助 | 查询IP地址组的关联资源 | 读取 | — |
| `VPC/ListFirewall/v3` · 助 | 查询网络ACL列表 | 读取 | — |
| `VPC/ListFlowLogs/v2` · 助 | 查询流日志列表 | 读取 | — |
| `VPC/ListPorts/v2` · 助 | 查询端口列表 | 读取 | — |
| `VPC/ListPorts/v3` · 助 | 查询端口列表 | 读取 | — |
| `VPC/ListPrivateips/v2` · 助 | 查询私有IP列表 | 读取 | 需 `subnet_id`。 |
| `VPC/ListRouteTables/v2` · 实 | 查询路由表列表 | 读取 | — |
| `VPC/ListSecurityGroupRules/v2` · 助 | 查询安全组规则列表 | 读取 | — |
| `VPC/ListSecurityGroupRules/v3` · 实 | 查询安全组规则列表 | 读取 | 按安全组 ID 筛选；ID 来自目标端口或已有配置。 |
| `VPC/ListSecurityGroups/v2` · 助 | 查询安全组列表 | 读取 | — |
| `VPC/ListSecurityGroups/v3` · 助 | 查询安全组列表 | 读取 | — |
| `VPC/ListSubNetworkInterfaces/v3` · 助 | 查询租户下辅助弹性网卡列表 | 读取 | — |
| `VPC/ListSubnets/v2` · 实 | 查询子网列表 | 读取 | 已知 VPC 时按 vpc_id 筛选。 |
| `VPC/ListTrafficMirrorFilterRules/v3` · 助 | 查询流量镜像筛选规则列表 | 读取 | — |
| `VPC/ListTrafficMirrorFilters/v3` · 助 | 查询流量镜像筛选条件列表 | 读取 | — |
| `VPC/ListTrafficMirrorSessions/v3` · 助 | 查询流量镜像会话列表 | 读取 | — |
| `VPC/ListVirsubnetCidrReservations/v3` · 助 | 查询子网预留网段列表 | 读取 | — |
| `VPC/ListVirsubnets/v3` · 助 | 查询虚拟子网列表 | 读取 | — |
| `VPC/ListVpcPeerings/v2` · 助 | 查询对等连接列表 | 读取 | — |
| `VPC/ListVpcRoutes/v2` · 助 | 查询VPC路由列表 | 读取 | — |
| `VPC/ListVpcs/v2` · 助 | 查询VPC列表 | 读取 | — |
| `VPC/ListVpcs/v3` · 助 | 查询VPC列表 | 读取 | — |
| `VPC/NeutronListFirewallGroups/v2` · 助 | 查询所有网络ACL组 | 读取 | — |
| `VPC/NeutronListFirewallPolicies/v2` · 助 | 查询所有网络ACL策略 | 读取 | — |
| `VPC/NeutronListFirewallRules/v2` · 助 | 查询所有网络ACL规则 | 读取 | — |
| `VPC/NeutronListNetworks/v2` · 助 | 查询网络列表 | 读取 | — |
| `VPC/NeutronListPorts/v2` · 助 | 查询端口列表 | 读取 | — |
| `VPC/NeutronListRouters/v2` · 助 | 查询路由器列表 | 读取 | — |
| `VPC/NeutronListSecurityGroupRules/v2` · 助 | 查询安全组规则列表 | 读取 | — |
| `VPC/NeutronListSecurityGroups/v2` · 助 | 查询安全组列表 | 读取 | — |
| `VPC/NeutronListSubnets/v2` · 助 | 查询子网列表 | 读取 | — |
| `VPC/NeutronShowFirewallGroup/v2` · 助 | 查询特定网络ACL组详情 | 读取 | 需 `firewall_group_id`。 |
| `VPC/NeutronShowFirewallPolicy/v2` · 助 | 查询特定网络ACL策略详情 | 读取 | 需 `firewall_policy_id`。 |
| `VPC/NeutronShowFirewallRule/v2` · 助 | 查询特定网络ACL规则 | 读取 | 需 `firewall_rule_id`。 |
| `VPC/NeutronShowNetwork/v2` · 助 | 查询网络 | 读取 | 需 `network_id`。 |
| `VPC/NeutronShowPort/v2` · 助 | 查询端口 | 读取 | 需 `port_id`。 |
| `VPC/NeutronShowRouter/v2` · 助 | 查询路由器 | 读取 | 需 `router_id`。 |
| `VPC/NeutronShowSecurityGroup/v2` · 助 | 查询安全组 | 读取 | 需 `security_group_id`。 未知 security_group_id 时查 [VPC/ListSecurityGroups/v3](configuration-network.md#vpc)。 |
| `VPC/NeutronShowSecurityGroupRule/v2` · 助 | 查询安全组规则 | 读取 | 需 `security_group_rule_id`。 未知 security_group_rule_id 时查 [VPC/ListSecurityGroupRules/v3](configuration-network.md#vpc)。 |
| `VPC/NeutronShowSubnet/v2` · 助 | 查询子网 | 读取 | 需 `subnet_id`。 |
| `VPC/ShowAddressGroup/v3` · 助 | 查询地址组 | 读取 | 需 `address_group_id`。 |
| `VPC/ShowFirewall/v3` · 助 | 查询网络ACL详情 | 读取 | 需 `firewall_id`。 |
| `VPC/ShowFlowLog/v2` · 助 | 查询流日志 | 读取 | 需 `flowlog_id`。 |
| `VPC/ShowNetworkIpAvailabilities/v2` · 助 | 查询网络IP使用情况 | 读取 | 需 `network_id`。 |
| `VPC/ShowPort/v2` · 助 | 查询端口 | 读取 | port_id；ECS 网卡按 [H-port](../helpers.md#h-port) 获取。 |
| `VPC/ShowPort/v3` · 实 | 查询端口详情 | 读取 | port_id；ECS 网卡按 [H-port](../helpers.md#h-port) 获取。 |
| `VPC/ShowPrivateip/v2` · 助 | 查询私有IP | 读取 | 需 `privateip_id`。 |
| `VPC/ShowQuota/v2` · 助 | 查询配额 | 读取 | — |
| `VPC/ShowQuota/v3` · 助 | 查询配额 | 读取 | — |
| `VPC/ShowRouteTable/v2` · 实 | 查询路由表 | 读取 | 需 `routetable_id`。 未知 routetable_id 时查 [VPC/ListRouteTables/v2](configuration-network.md#vpc)。 |
| `VPC/ShowSecurityGroup/v2` · 助 | 查询安全组 | 读取 | 需 `security_group_id`。 未知 security_group_id 时查 [VPC/ListSecurityGroups/v3](configuration-network.md#vpc)。 |
| `VPC/ShowSecurityGroup/v3` · 实 | 查询安全组 | 读取 | 需 `security_group_id`。 未知 security_group_id 时查 [VPC/ListSecurityGroups/v3](configuration-network.md#vpc)。 |
| `VPC/ShowSecurityGroupRule/v2` · 助 | 查询安全组规则 | 读取 | 需 `security_group_rule_id`。 未知 security_group_rule_id 时查 [VPC/ListSecurityGroupRules/v3](configuration-network.md#vpc)。 |
| `VPC/ShowSecurityGroupRule/v3` · 实 | 查询安全组规则 | 读取 | 需 `security_group_rule_id`。 未知 security_group_rule_id 时查 [VPC/ListSecurityGroupRules/v3](configuration-network.md#vpc)。 |
| `VPC/ShowSubNetworkInterface/v3` · 助 | 查询租户下辅助弹性网卡 | 读取 | 需 `sub_network_interface_id`。 |
| `VPC/ShowSubNetworkInterfacesQuantity/v3` · 助 | 查询租户下辅助弹性网卡数目 | 读取 | — |
| `VPC/ShowSubnet/v2` · 实 | 查询子网 | 读取 | VPC 子网 ID；按 [H-subnet](../helpers.md#h-subnet) 区分 Neutron 子网。 |
| `VPC/ShowTrafficMirrorFilter/v3` · 助 | 查询流量镜像筛选条件详情 | 读取 | 需 `traffic_mirror_filter_id`。 |
| `VPC/ShowTrafficMirrorFilterRule/v3` · 助 | 查询流量镜像筛选规则详情 | 读取 | 需 `traffic_mirror_filter_rule_id`。 |
| `VPC/ShowTrafficMirrorSession/v3` · 助 | 查询流量镜像会话详情 | 读取 | 需 `traffic_mirror_session_id`。 |
| `VPC/ShowVirsubnet/v3` · 助 | 查询虚拟子网详情 | 读取 | 需 `virsubnet_id`。 |
| `VPC/ShowVirsubnetCidrReservation/v3` · 助 | 查询子网预留网段 | 读取 | 需 `virsubnet_cidr_reservation_id`。 |
| `VPC/ShowVpc/v2` · 助 | 查询VPC | 读取 | 需 `vpc_id`。 未知 vpc_id 时查 [VPC/ListVpcs/v3](configuration-network.md#vpc)。 |
| `VPC/ShowVpc/v3` · 实 | 查询VPC详情 | 读取 | 需 `vpc_id`。 未知 vpc_id 时查 [VPC/ListVpcs/v3](configuration-network.md#vpc)。 |
| `VPC/ShowVpcPeering/v2` · 助 | 查询对等连接 | 读取 | 需 `peering_id`。 |
| `VPC/ShowVpcRoute/v2` · 助 | 查询VPC路由 | 读取 | 需 `route_id`。 |
| `VPC/UpdateFlowLog/v2` · 助 | 更新流日志 | 修改或执行 | 需 `flowlog_id`。 |

## VPCEP

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `VPCEP/ListEndpointInfoDetails/v1` · 助 | 查询终端节点详情 | 读取 | 需 `vpc_endpoint_id`。 |
| `VPCEP/ListEndpointService/v1` · 助 | 查询终端节点服务列表 | 读取 | — |
| `VPCEP/ListEndpoints/v1` · 助 | 查询终端节点列表 | 读取 | — |
| `VPCEP/ListQuotaDetails/v1` · 助 | 查询配额 | 读取 | — |
| `VPCEP/ListServiceConnections/v1` · 助 | 查询连接终端节点服务的连接列表 | 读取 | 需 `vpc_endpoint_service_id`。 |
| `VPCEP/ListServiceDescribeDetails/v1` · 助 | 查询终端节点服务概要 | 读取 | — |
| `VPCEP/ListServiceDetails/v1` · 助 | 查询终端节点服务详情 | 读取 | 需 `vpc_endpoint_service_id`。 |
| `VPCEP/ListServicePermissionsDetails/v1` · 助 | 查询终端节点服务的白名单列表 | 读取 | 需 `vpc_endpoint_service_id`。 |
| `VPCEP/ListServicePublicDetails/v1` · 助 | 查询公共终端节点服务列表 | 读取 | — |

## VPN

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `VPN/ListCgws/v5` · 助 | 查询对端网关列表 | 读取 | — |
| `VPN/ListConnectionIpsecSa/v5` · 助 | 查询VPN连接网段协商信息 | 读取 | 需 `vpn_connection_id`。 |
| `VPN/ListP2cVgwConnections/v5` · 助 | 查询P2C VPN网关连接信息列表 | 读取 | 需 `p2c_vgw_id`。 |
| `VPN/ListP2cVgws/v5` · 助 | 查询P2C VPN网关列表 | 读取 | — |
| `VPN/ListVgws/v5` · 实·空 | 查询VPN网关列表 | 读取 | 当前 help 没有 limit 参数。 |
| `VPN/ListVpnAccessPolicies/v5` · 助 | 查询VPN访问策略列表 | 读取 | 需 `vpn_server_id`。 |
| `VPN/ListVpnConnections/v5` · 助 | 查询VPN连接列表 | 读取 | — |
| `VPN/ListVpnServersByProject/v5` · 助 | 查询租户下的所有服务端信息 | 读取 | — |
| `VPN/ListVpnServersByVgw/v5` · 助 | 查询一个网关下的服务端信息 | 读取 | 需 `p2c_vgw_id`。 |
| `VPN/ShowCgw/v5` · 助 | 查询对端网关 | 读取 | 需 `customer_gateway_id`。 |
| `VPN/ShowP2cVgw/v5` · 助 | 查询P2C VPN网关 | 读取 | 需 `p2c_vgw_id`。 |
| `VPN/ShowQuotasInfo/v5` · 助 | 查询指定租户配额 | 读取 | — |
| `VPN/ShowVgw/v5` · 助 | 查询VPN网关 | 读取 | 需 `vgw_id`。 |
| `VPN/ShowVpnAccessPolicy/v5` · 助 | 查询VPN访问策略 | 读取 | 需 `policy_id`、`vpn_server_id`。 |
| `VPN/ShowVpnConnection/v5` · 助 | 查询VPN连接 | 读取 | 需 `vpn_connection_id`。 |
| `VPN/ShowVpnConnectionLog/v5` · 助 | 查询VPN连接日志 | 读取 | 需 `vpn_connection_id`。 |
| `VPN/ShowVpnConnectionsLogConfig/v5` · 助 | 查询VPN连接日志配置 | 读取 | 需 `p2c_vgw_id`。 |
| `VPN/ShowVpnGatewayRoutingTable/v5` · 助 | 查询VPN网关路由表 | 读取 | 需 `vgw_id`。 |
