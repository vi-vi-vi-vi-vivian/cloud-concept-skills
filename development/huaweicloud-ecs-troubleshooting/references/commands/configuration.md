# 配置 C

查询资源状态、配置和关系。ACTIVE 仅表示平台实例状态。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[AOM](#aom) · [CBR](#cbr) · [COC](#coc) · [CTS](#cts) · [Config](#config) · [ECS](#ecs) · [EPS](#eps) · [EVS](#evs) · [IMS](#ims) · [LTS](#lts) · [RMS](#rms) · [SMN](#smn)

## AOM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `AOM/BatchImportAgent/v4` · 助 | 下发批量安装UniAgent任务 | 安装 Agent | 需 `installer_agent_id`、`proxy_region_id`。 |
| `AOM/BatchUpdateAgent/v4` · 助 | 下发批量升级UniAgent任务 | 升级 Agent | 需 `agent_list.[N].agent_id`。 |
| `AOM/ListAgents/v2` · 助 | 查询主机安装的ICAgent信息 | 读取 | 需 `cluster_id`、`namespace`。 |
| `AOM/ListPermissions/v2` · 助 | 查询aom2.0相关云服务授权信息 | 读取 | — |
| `AOM/ListResourceUnderNode/v3` · 助 | 查询绑定在节点上的资源列表 | 读取 | 需 `rf_resource_type`、`type`。 |
| `AOM/ListServiceDiscoveryRules/v2` · 助 | 查询系统中已有服务发现规则 | 读取 | — |
| `AOM/ShowAgentInfos/v4` · 助 | 查询UniAgent主机列表信息 | 读取 | — |
| `AOM/ShowApp/v3` · 助 | 查询应用详情 | 读取 | 需 `application_id`。 |
| `AOM/ShowAppByName/v3` · 助 | 根据应用名称查询应用详情 | 读取 | — |
| `AOM/ShowComponent/v3` · 助 | 查询组件详情 | 读取 | 需 `component_id`。 |
| `AOM/ShowComponentByName/v3` · 助 | 根据组件名称查询组件详情 | 读取 | 需 `application_id`、`component_name`。 |
| `AOM/ShowEnv/v3` · 助 | 查询环境详情 | 读取 | 需 `environment_id`。 |
| `AOM/ShowEnvByName/v3` · 助 | 根据环境名称查询环境详情 | 读取 | 需 `environment_name`、`component_id`。 |

## CBR

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CBR/CopyBackup/v1` · 助 | 复制备份 | 创建或配置 | 需 `backup_id`、`replicate.destination_project_id`、`replicate.destination_vault_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/CopyCheckpoint/v1` · 助 | 复制备份还原点 | 创建或配置 | 需 `replicate.destination_project_id`、`replicate.destination_vault_id`、`replicate.vault_id`。 |
| `CBR/CreateCheckpoint/v1` · 助 | 创建备份还原点 | 创建或配置 | 需 `checkpoint.vault_id`。 |
| `CBR/DeleteVault/v1` · 助 | 删除存储库 | 删除或移除 | 需 `vault_id`。 未知 vault_id 时查 [CBR/ListVault/v1](configuration.md#cbr)。 |
| `CBR/ListAgent/v1` · 助 | 查询客户端列表 | 读取 | — |
| `CBR/ListBackups/v1` · 实·空 | 查询所有备份 | 读取 | — |
| `CBR/ListDomainProjects/v1` · 助 | 查询租户项目列表 | 读取 | 需 `domain_name`。 |
| `CBR/ListExternalVault/v1` · 助 | 查询其他区域存储库列表 | 读取 | 需 `external_project_id`、`region_id`。 |
| `CBR/ListFeatures/v1` · 助 | 查询服务支持的特性列表 | 读取 | — |
| `CBR/ListOrganizationPolicies/v1` · 助 | 查询组织策略列表 | 读取 | — |
| `CBR/ListOrganizationPolicyDetail/v1` · 助 | 查询组织策略部署状态列表 | 读取 | 需 `organization_policy_id`。 |
| `CBR/ListPolicies/v1` · 助 | 查询策略列表 | 读取 | — |
| `CBR/ListProjects/v1` · 助 | 查询租户的项目信息 | 读取 | — |
| `CBR/ListProtectable/v1` · 助 | 查询可保护资源 | 读取 | 需 `protectable_type`。 |
| `CBR/ListVault/v1` · 实·空 | 查询存储库列表 | 读取 | — |
| `CBR/RegisterAgent/v1` · 助 | 注册客户端 | 创建或配置 | 需 `agent.agent_id`。 |
| `CBR/ShowAgent/v1` · 助 | 查询指定客户端 | 读取 | 需 `agent_id`。 |
| `CBR/ShowBackup/v1` · 助 | 查询指定备份 | 读取 | 需 `backup_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/ShowCheckpoint/v1` · 助 | 查询备份还原点 | 读取 | 需 `checkpoint_id`。 |
| `CBR/ShowDomain/v1` · 助 | 查询租户信息 | 读取 | 需 `source_project_id`。 |
| `CBR/ShowFeature/v1` · 助 | 查询指定特性 | 读取 | 需 `feature_key`。 |
| `CBR/ShowMemberDetail/v1` · 助 | 获取备份成员详情 | 读取 | 需 `backup_id`、`member_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/ShowMembersDetail/v1` · 助 | 获取备份成员列表 | 读取 | 需 `backup_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/ShowMetadata/v1` · 助 | 查询备份元数据 | 读取 | 需 `backup_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/ShowMigrateStatus/v1` · 助 | 查询迁移 | 读取 | — |
| `CBR/ShowOrganizationPolicy/v1` · 助 | 查询指定组织策略 | 读取 | 需 `organization_policy_id`。 |
| `CBR/ShowPolicy/v1` · 助 | 查询单个策略 | 读取 | 需 `policy_id`。 |
| `CBR/ShowProtectable/v1` · 助 | 查询指定可保护资源 | 读取 | 需 `instance_id`、`protectable_type`。 |
| `CBR/ShowReplicationCapabilities/v1` · 助 | 查询复制能力 | 读取 | — |
| `CBR/ShowStorageUsage/v1` · 助 | 查询容量统计 | 读取 | — |
| `CBR/ShowSummary/v1` · 助 | 存储库容量总览 | 读取 | — |
| `CBR/ShowVault/v1` · 助 | 查询指定存储库 | 读取 | 需 `vault_id`。 未知 vault_id 时查 [CBR/ListVault/v1](configuration.md#cbr)。 |
| `CBR/ShowVaultProjectTag/v1` · 助 | 查询存储库项目标签 | 读取 | — |
| `CBR/ShowVaultResourceInstances/v1` · 助 | 查询存储库资源实例 | 读取 | — |
| `CBR/ShowVaultTag/v1` · 助 | 查询存储库资源标签 | 读取 | 需 `vault_id`。 未知 vault_id 时查 [CBR/ListVault/v1](configuration.md#cbr)。 |
| `CBR/UnregisterAgent/v1` · 助 | 移除客户端 | 删除或移除 | 需 `agent_id`。 |
| `CBR/UpdateAgent/v1` · 助 | 修改客户端 | 修改或执行 | 需 `agent_id`。 |

## COC

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `COC/ListResourceViews/v1` · 助 | 查询CMDB跨账号资源视图 | 读取 | — |
| `COC/ListResources/v1` · 助 | 查询用户所有资源 | 读取 | — |
| `COC/ListResourcesOfResourceView/v1` · 助 | 查询CMDB跨账号资源视图聚合的资源 | 读取 | 需 `view_id`。 |
| `COC/ShowLastSyncStatus/v1` · 助 | 查询多云资源最新同步状态 | 读取 | — |
| `COC/SyncResourceAgent/v1` · 助 | 同步华为云资源Agent信息 | 同步 Agent | — |

## CTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CTS/CheckObsBuckets/v3` · 助 | 检查已经配置OBS桶是否可以成功转储 | 转储条件检查 | — |
| `CTS/ListNotifications/v3` · 助 | 查询关键操作通知 | 读取 | 需 `notification_type`。 |
| `CTS/ListOperations/v3` · 助 | 查询云服务的全量操作列表 | 读取 | — |
| `CTS/ListQuotas/v3` · 助 | 查询租户追踪器配额信息 | 读取 | — |
| `CTS/ListTraceResources/v3` · 助 | 查询事件的资源类型列表 | 读取 | — |
| `CTS/ListTrackers/v3` · 实·空 | 查询追踪器 | 读取 | — |
| `CTS/ListUserResources/v3` · 助 | 查询30天事件的操作用户列表 | 读取 | — |

## Config

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `Config/ListAllResources/v1` · 助 | 列举所有资源 | 读取 | — |
| `Config/ListRegions/v1` · 助 | 查询用户可见的区域 | 读取 | — |
| `Config/ListResources/v1` · 助 | 列举指定类型的资源 | 读取 | 需 `provider`、`type`。 |
| `Config/ListTrackedResources/v1` · 助 | 列举资源记录器收集的全部资源 | 读取 | — |
| `Config/ShowConfigurationAggregatorSourcesStatus/v1` · 助 | 查询指定资源聚合器聚合帐号的状态信息 | 读取 | 需 `aggregator_id`。 |
| `Config/ShowResourceById/v1` · 助 | 查询单个资源 | 读取 | 需 `provider`、`resource_id`、`type`。 |
| `Config/ShowResourceDetail/v1` · 助 | 查询帐号下的单个资源 | 读取 | 需 `resource_id`。 |
| `Config/ShowResourceHistory/v1` · 实·空 | 查询资源历史 | 读取 | 需 `resource_id`。 |
| `Config/ShowResourceRelations/v1` · 助 | 列举资源关系 | 读取 | 需 `resource_id`。 |
| `Config/ShowResourceRelationsDetail/v1` · 助 | 列举资源关系详情 | 读取 | 需 `resource_id`。 |
| `Config/ShowTrackedResourceDetail/v1` · 助 | 查询资源记录器收集的单个资源 | 读取 | 需 `resource_id`。 |
| `Config/ShowTrackerConfig/v1` · 助 | 查询记录器 | 读取 | — |

## ECS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ECS/ListCloudServers/v2` · 助 | 查询云服务器列表接口 | 读取 | — |
| `ECS/ListFlavorSellPolicies/v2` · 助 | 查询规格销售策略 | 读取 | — |
| `ECS/ListFlavors/v2` · 助 | 查询规格详情和规格扩展信息列表 | 读取 | — |
| `ECS/ListLaunchTemplateVersions/v2` · 助 | 查询模板版本列表 | 读取 | — |
| `ECS/ListRecycleBinServers/v2` · 助 | 查询回收站中虚拟机列表 | 读取 | — |
| `ECS/ListServerAzInfo/v2` · 助 | 查询可用区列表 | 读取 | — |
| `ECS/ListServerBlockDevices/v2` · 实 | 查询弹性云服务器挂载磁盘列表详情信息 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ListServerGroups/v2` · 实·空 | 查询云服务器组列表 | 读取 | — |
| `ECS/ListServerInterfaces/v2` · 实 | 查询云服务器网卡信息 | 读取 | server_id；端口衔接见 Helper [H-port](../helpers.md#h-port)。 |
| `ECS/ListServerTags/v2` · 助 | 查询项目标签 | 读取 | — |
| `ECS/ListServerVolumeAttachments/v2` · 实 | 查询弹性云服务器挂载磁盘列表信息 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ListServersDetails/v2` · 实 | 查询云服务器详情列表 | 读取 | — |
| `ECS/ListTemplates/v2` · 助 | 查询模板列表 | 读取 | — |
| `ECS/NovaListAvailabilityZones/v2` · 助 | 查询可用区列表 | 读取 | — |
| `ECS/NovaListFlavors/v2` · 助 | 查询云服务器规格列表 | 读取 | — |
| `ECS/NovaListFlavorsDetails/v2` · 助 | 查询云服务器规格详情列表 | 读取 | — |
| `ECS/NovaListKeypairs/v2` · 助 | 查询SSH密钥列表 | 读取 | — |
| `ECS/NovaListServerGroups/v2` · 助 | 查询云服务器组列表 | 读取 | — |
| `ECS/NovaListServerInterfaces/v2` · 助 | 查询云服务器网卡信息 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaListServerSecurityGroups/v2` · 实 | 查询指定云服务器安全组列表 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaListServerVolumes/v2` · 助 | 查询弹性云服务器挂载磁盘信息 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaListServers/v2` · 助 | 查询云服务器列表 | 读取 | — |
| `ECS/NovaListServersDetails/v2` · 助 | 查询云服务器详情列表 | 读取 | — |
| `ECS/NovaListVersions/v2` · 助 | 查询API版本信息列表 | 读取 | — |
| `ECS/NovaShowFlavor/v2` · 实 | 查询云服务器规格详情 | 读取 | 需 `flavor_id`。 |
| `ECS/NovaShowFlavorExtraSpecs/v2` · 助 | 查询云服务器规格extra_specs的详情 | 读取 | 需 `flavor_id`。 |
| `ECS/NovaShowKeypair/v2` · 助 | 查询SSH密钥详情 | 读取 | 需 `keypair_name`。 |
| `ECS/NovaShowServer/v2` · 助 | 查询云服务器详情 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowServerGroup/v2` · 助 | 查询云服务器组详情 | 读取 | 需 `server_group_id`。 |
| `ECS/NovaShowServerInterface/v2` · 助 | 查询指定云服务器网卡信息 | 读取 | 需 `port_id`、`server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowServerMetadata/v2` · 助 | 查询云服务器元数据列表 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowServerMetadataItem/v2` · 助 | 获取云服务器指定Key的元数据 | 读取 | 需 `key`、`server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowServerVolume/v2` · 助 | 查询弹性云服务器挂载的单个磁盘信息 | 读取 | 需 `server_id`、`volume_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowVersion/v2` · 助 | 查询指定API版本信息 | 读取 | 需 `api_version`。 |
| `ECS/ShowAppendableVolumeQuota/v2` · 助 | 查询包周期虚拟机可以追加卷数量 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowMetadataOptions/v2` · 阻·调用 | 查询云服务器元数据配置 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 本次调用受阻：Ecs.0621。 |
| `ECS/ShowRecycleBin/v2` · 助 | 查询回收站配置 | 读取 | — |
| `ECS/ShowServer/v2` · 实 | 查询云服务器详情 | 读取 | server_id；未知时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowServerAttachableNicNum/v2` · 助 | 查询虚拟机可挂载网卡 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowServerBlockDevice/v2` · 助 | 查询弹性云服务器单个磁盘信息 | 读取 | 需 `server_id`、`volume_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowServerGroup/v2` · 助 | 查询云服务器组详情 | 读取 | 需 `server_group_id`。 |
| `ECS/ShowServerLimits/v2` · 实 | 查询租户配额 | 读取 | — |
| `ECS/ShowServerTags/v2` · 实 | 查询云服务器标签 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |

## EPS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EPS/ListMigrationRecord/v1` · 助 | 查询资源迁移记录 | 读取 | — |
| `EPS/ShowEnterpriseProjectQuota/v1` · 助 | 查询企业项目配额 | 读取 | — |

## EVS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EVS/CinderListAvailabilityZones/v2` · 助 | 查询所有的可用分区信息 | 读取 | — |
| `EVS/CinderListQuotas/v2` · 实 | 查询租户的详细配额 | 读取 | target_project_id 与 project_id 相同；当前 CLI 用 usage=True。 |
| `EVS/CinderListVolumeTransfers/v2` · 助 | 查询云硬盘过户记录列表概要 | 读取 | — |
| `EVS/CinderListVolumeTypes/v2` · 助 | 查询云硬盘类型列表 | 读取 | — |
| `EVS/CinderShowVolumeTransfer/v2` · 助 | 查询单个云硬盘过户记录详情 | 读取 | 需 `transfer_id`。 |
| `EVS/CreateSnapshot/v2` · 助 | 创建云硬盘快照 | 创建或配置 | 需 `snapshot.volume_id`。 |
| `EVS/ListSnapshots/v2` · 实·空 | 查询云硬盘快照详情列表 | 读取 | — |
| `EVS/ListVersions/v2` · 助 | 查询接口版本信息列表 | 读取 | — |
| `EVS/ListVolumeTags/v2` · 助 | 获取云硬盘资源的所有标签 | 读取 | — |
| `EVS/ListVolumes/v2` · 实 | 查询所有云硬盘详情 | 读取 | — |
| `EVS/ListVolumesByTags/v2` · 助 | 通过标签查询云硬盘资源实例详情 | 读取 | — |
| `EVS/ListVolumesInRecycle/v2` · 助 | 查询回收站中所有云硬盘详情 | 读取 | — |
| `EVS/RetypeVolume/v2` · 助 | 磁盘类型变更 | 修改或执行 | 需 `volume_id`。 未知 volume_id 时查 [EVS/ListVolumes/v2](configuration.md#evs)。 |
| `EVS/ShowRecyclePolicy/v2` · 助 | 查询回收站策略 | 读取 | — |
| `EVS/ShowSnapshot/v2` · 助 | 查询单个云硬盘快照详情 | 读取 | 需 `snapshot_id`。 未知 snapshot_id 时查 [EVS/ListSnapshots/v2](configuration.md#evs)。 |
| `EVS/ShowVersion/v2` · 助 | 查询API接口的版本信息 | 读取 | 需 `version`。 |
| `EVS/ShowVolume/v2` · 实 | 查询单个云硬盘详情 | 读取 | volume_id；未知时查 [ECS/ListServerBlockDevices/v2](configuration.md#ecs)。 |
| `EVS/ShowVolumeInRecycle/v2` · 助 | 查询回收站中单个云硬盘详情 | 读取 | 需 `volume_id`。 未知 volume_id 时查 [EVS/ListVolumes/v2](configuration.md#evs)。 |
| `EVS/ShowVolumeTags/v2` · 助 | 查询云硬盘标签 | 读取 | 需 `volume_id`。 未知 volume_id 时查 [EVS/ListVolumes/v2](configuration.md#evs)。 |

## IMS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `IMS/CreateImage/v2` · 助 | 制作镜像 | 创建或配置 | — |
| `IMS/CreateWholeImage/v2` · 助 | 制作整机镜像 | 创建或配置 | — |
| `IMS/ExportImage/v2` · 助 | 导出镜像 | 导出镜像 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/GlanceListImageMemberSchemas/v2` · 助 | 查询镜像成员列表视图(OpenStack原生) | 读取 | — |
| `IMS/GlanceListImageMembers/v2` · 助 | 获取镜像成员列表(OpenStack原生) | 读取 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/GlanceListImageSchemas/v2` · 助 | 查询镜像列表视图(OpenStack原生) | 读取 | — |
| `IMS/GlanceListImages/v2` · 助 | 查询镜像列表(OpenStack原生) | 读取 | — |
| `IMS/GlanceShowImage/v2` · 实 | 查询镜像详情(OpenStack原生) | 读取 | image_id；从 [ECS/ShowServer/v2](configuration.md#ecs) 的 server.image.id 取得。 |
| `IMS/GlanceShowImageMember/v2` · 助 | 获取镜像成员详情(OpenStack原生) | 读取 | 需 `image_id`、`member_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/GlanceShowImageMemberSchemas/v2` · 助 | 查询镜像成员视图(OpenStack原生) | 读取 | — |
| `IMS/GlanceShowImageSchemas/v2` · 助 | 查询镜像视图(OpenStack原生) | 读取 | — |
| `IMS/GlanceUpdateImage/v2` · 助 | 更新镜像信息(OpenStack原生) | 修改镜像配置 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/ImportImageQuick/v2` · 助 | 镜像文件快速导入 | 导入镜像 | — |
| `IMS/ListImageByTags/v2` · 助 | 按标签查询镜像 | 读取 | — |
| `IMS/ListImageMembers/v2` · 助 | 获取镜像成员列表 | 读取 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/ListImageTags/v2` · 助 | 查询镜像标签 | 读取 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/ListImages/v2` · 助 | 查询镜像列表 | 读取 | — |
| `IMS/ListImagesTags/v2` · 助 | 查询租户所有镜像标签 | 读取 | — |
| `IMS/ListOsVersions/v2` · 助 | 查询镜像支持的OS列表 | 读取 | — |
| `IMS/ListTags/v2` · 助 | 按条件查询租户镜像标签列表 | 读取 | — |
| `IMS/ListVersions/v2` · 助 | 查询版本列表(OpenStack原生) | 读取 | — |
| `IMS/RegisterImage/v2` · 助 | 注册镜像 | 创建或配置 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/ShowImageMember/v2` · 助 | 获取镜像成员详情 | 读取 | 需 `image_id`、`member_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |
| `IMS/ShowImageQuota/v2` · 实 | 查询镜像配额 | 读取 | — |
| `IMS/ShowVersion/v2` · 助 | 查询版本列表(OpenStack原生) | 读取 | 需 `version`。 |
| `IMS/UpdateImage/v2` · 助 | 更新镜像信息 | 修改或执行 | 需 `image_id`。 未知 image_id 时查 [IMS/ListImages/v2](configuration.md#ims)。 |

## LTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `LTS/ListAccessConfig/v2` · 实·空 | 查询日志接入 | 读取 | — |
| `LTS/ListCharts/v2` · 助 | 查询日志流图表 | 读取 | 需 `log_group_id`、`log_stream_id`。 未知 log_group_id 时查 [LTS/ListLogGroups/v2](../services.md#lts)。 |
| `LTS/ListHost/v2` · 实·空 | 查询主机信息 | 读取 | — |
| `LTS/ListHostGroup/v2` · 助 | 查询主机组 | 读取 | — |
| `LTS/ListTransfers/v2` · 助 | 查询日志转储 | 读取 | — |
| `LTS/ShowAdminConfig/v2` · 助 | 获取日志汇聚开关 | 读取 | — |
| `LTS/ShowAomMappingRule/v2` · 助 | 查询单个接入规则 | 读取 | 需 `rule_id`。 |
| `LTS/ShowAomMappingRules/v2` · 助 | 查询所有接入规则 | 读取 | — |
| `LTS/ShowLogConvergeConfig/v2` · 助 | 获取组织成员汇聚配置 | 读取 | 需 `member_account_id`。 |
| `LTS/ShowMemberGroupAndStream/v2` · 助 | 获取组织成员日志组日志流 | 读取 | 需 `member_account_id`。 |

## RMS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `RMS/ListAllResources/v1` · 助 | 列举所有资源 | 读取 | — |
| `RMS/ListRegions/v1` · 助 | 查询用户可见的区域 | 读取 | — |
| `RMS/ListResources/v1` · 助 | 列举指定类型的资源 | 读取 | 需 `provider`、`type`。 |
| `RMS/ShowConfigurationAggregatorSourcesStatus/v1` · 助 | 查询指定资源聚合器聚合帐号的状态信息 | 读取 | 需 `aggregator_id`。 |
| `RMS/ShowResourceById/v1` · 助 | 查询单个资源 | 读取 | 需 `provider`、`resource_id`、`type`。 |
| `RMS/ShowResourceDetail/v1` · 助 | 查询帐号下的单个资源 | 读取 | 需 `resource_id`。 |
| `RMS/ShowResourceHistory/v1` · 助 | 查询资源历史 | 读取 | 需 `resource_id`。 |
| `RMS/ShowResourceRelations/v1` · 助 | 列举资源关系 | 读取 | 需 `resource_id`。 |
| `RMS/ShowResourceRelationsDetail/v1` · 助 | 列举资源关系详情 | 读取 | 需 `resource_id`。 |
| `RMS/ShowTrackerConfig/v1` · 助 | 查询记录器 | 读取 | — |

## SMN

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `SMN/ListLogtank/v2` · 助 | 查询云日志 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/ListSubscriptions/v2` · 助 | 查询订阅者列表 | 读取 | — |
| `SMN/ListSubscriptionsByTopic/v2` · 助 | 查询指定Topic的订阅者列表 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/ListTopicAttributes/v2` · 助 | 查询主题策略 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/ListTopicDetails/v2` · 助 | 查询主题详情 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/ListTopics/v2` · 助 | 查询主题列表 | 读取 | — |
| `SMN/ListTopicsWithAssociatedResources/v2` · 助 | 查询主题列表及主题关联资源信息 | 读取 | — |
