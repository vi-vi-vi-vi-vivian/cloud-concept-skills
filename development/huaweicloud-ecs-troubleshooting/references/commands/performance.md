# 性能 P

按同一资源和时间窗查询指标。OS 指标依赖实际采集能力。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[AOM](#aom) · [APM](#apm) · [CES](#ces) · [COC](#coc) · [ECS](#ecs) · [EVS](#evs)

## AOM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `AOM/ListAllVersionByVersionId/v1` · 助 | 脚本版本查询 | 读取 | 需 `script_id`。 |
| `AOM/ListDashBoards/v2` · 助 | 查询仪表盘列表 | 读取 | — |
| `AOM/ListDashboardsFolder/v2` · 助 | 查询仪表盘分组列表 | 读取 | — |
| `AOM/ListInstantQueryAomPromGet/v2` · 助 | GET方法查询瞬时数据 | 读取 | — |
| `AOM/ListInstantQueryAomPromPost/v2` · 助 | (推荐)POST方法查询瞬时数据 | 读取 | — |
| `AOM/ListLabelValuesAomPromGet/v2` · 助 | 查询标签值 | 读取 | 需 `label_name`。 |
| `AOM/ListLabelsAomPromGet/v2` · 助 | GET方法获取标签名列表 | 读取 | — |
| `AOM/ListLabelsAomPromPost/v2` · 助 | (推荐)POST方法获取标签名列表 | 读取 | — |
| `AOM/ListLogItems/v2` · 助 | 查询日志 | 读取 | — |
| `AOM/ListMetadataAomPromGet/v2` · 助 | 元数据查询 | 读取 | — |
| `AOM/ListMetricItems/v2` · 助 | 查询指标 | 读取 | — |
| `AOM/ListPromInstance/v2` · 助 | 查询Prometheus实例 | 读取 | — |
| `AOM/ListRangeQueryAomPromGet/v2` · 助 | GET方法查询区间数据 | 读取 | — |
| `AOM/ListRangeQueryAomPromPost/v2` · 助 | (推荐)POST方法查询区间数据 | 读取 | — |
| `AOM/ListSample/v2` · 助 | 查询时序数据 | 读取 | — |
| `AOM/ListSeries/v2` · 助 | 查询时间序列 | 读取 | — |
| `AOM/ShowDashBoard/v2` · 助 | 查询仪表盘详情 | 读取 | 需 `dashboard_id`。 |
| `AOM/ShowMetricsData/v2` · 助 | 查询监控数据 | 读取 | — |

## APM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `APM/ChangeAgentStatus/v1` · 助 | 更改实例的采集状态 | 修改或执行 | 需 `x-business-id`。 |
| `APM/ListAppEnvs/v1` · 助 | 获取组件下的环境列表 | 读取 | 需 `x-business-id`、`app_id`。 |
| `APM/ListApps/v1` · 助 | 获取组件列表 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ListBusiness/v1` · 助 | 查询应用列表 | 读取 | — |
| `APM/ListBusinessEnv/v1` · 助 | 查询URL跟踪Region环境列表 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ListEnvInstances/v1` · 助 | 获取实例信息列表 | 读取 | 需 `x-business-id`、`env_id`。 |
| `APM/ListEnvMonitorItem/v1` · 助 | 查询监控项列表 | 读取 | 需 `x-business-id`、`env_id`。 |
| `APM/ListEnvTags/v1` · 助 | 查询环境标签 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ListOpenRegion/v1` · 助 | 查询开通的region | 读取 | — |
| `APM/ListSupportedRegion/v1` · 助 | 查询所有的支持的region | 读取 | — |
| `APM/SaveMonitorItemConfig/v1` · 助 | 保存监控项 | 修改采集配置 | 需 `x-business-id`、`env_id`、`monitor_item_id`。 |
| `APM/SearchAgent/v1` · 助 | 查询应用下所有探针 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/SearchApplication/v1` · 助 | 对指定区域下的组件和环境及其探针情况进行搜索 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/SearchBusinessTopology/v1` · 助 | 查询应用全局拓扑图 | 读取 | 需 `x-business-id`、`target_business_id`。 |
| `APM/SearchEnvTopology/v1` · 助 | 查询组件环境拓扑图 | 读取 | 需 `x-business-id`、`target_env_id`。 |
| `APM/SearchTransaction/v1` · 助 | 查询URL跟踪视图列表 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/SearchTransactionConfig/v1` · 助 | 查询URL跟踪配置列表 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ShowBusinessDetail/v1` · 助 | 查询单个应用的详情 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ShowClobDetail/v1` · 助 | 获取原始数据详情 | 读取 | 需 `x-business-id`、`clob_id`、`env_id`。 |
| `APM/ShowEnvMonitorItems/v1` · 助 | 获取监控项信息 | 读取 | 需 `x-business-id`、`env_id`。 |
| `APM/ShowEventDetail/v1` · 助 | 获取event的详情 | 读取 | 需 `env_id`、`event_id`、`span_id`、`trace_id`。 |
| `APM/ShowFlameLineTree/v1` · 助 | ShowFlameLineTree | 读取 | 需 `x-business-id`、`instance_id`。 |
| `APM/ShowMonitorItemDetail/v1` · 助 | 获取一个监控项的详情 | 读取 | 需 `x-business-id`、`env_id`、`monitor_item_id`。 |
| `APM/ShowMonitorItemViewConfig/v1` · 助 | 查询监控项配置信息 | 读取 | 需 `x-business-id`、`collector_id`、`env_id`。 |
| `APM/ShowRawTable/v1` · 助 | 获取原始数据表格 | 读取 | 需 `x-business-id`、`env_id`。 |
| `APM/ShowSpanSearch/v1` · 助 | 查询span数据 | 读取 | 应用 x-business-id、biz_id 和 region；IAM 访问级别标为 Write。 |
| `APM/ShowSubBusinessDetail/v1` · 助 | 查询子应用详情 | 读取 | 需 `x-business-id`、`sub_business_id`。 |
| `APM/ShowSumTable/v1` · 助 | 获取汇总表格数据 | 读取 | 需 `x-business-id`、`env_id`。 |
| `APM/ShowTopology/v1` · 助 | 调用链拓扑图 | 读取 | 需 `trace_id`。 |
| `APM/ShowTopologyTree/v1` · 助 | 获取应用树 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ShowTraceEvents/v1` · 助 | 获取一个trace的所有调用链数据 | 读取 | 需 `trace_id`。 |
| `APM/ShowTransactionDetail/v1` · 助 | 查询URL跟踪视图详情 | 读取 | 需 `x-business-id`。 |
| `APM/ShowTrend/v1` · 助 | 获取趋势图 | 读取 | 需 `x-business-id`、`env_id`。 |

## CES

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CES/BatchCreateAgentInvocations/v3` · 助 | 批量创建Agent任务 | 安装或维护 Agent | — |
| `CES/BatchListMetricData/v1` · 助 | 批量查询监控数据 | 读取 | — |
| `CES/BatchListSpecifiedMetricData/v2` · 助 | 批量查询指标数据 | 读取 | — |
| `CES/ListAgentDimensionInfo/v2` · 助 | 查询主机监控原始维度值 | 读取 | 需 `instance_id`。 |
| `CES/ListAgentInvocations/v3` · 助 | 查询Agent任务列表 | 读取 | — |
| `CES/ListAgentStatus/v3` · 实 | 插件状态查询 | 读取 | — |
| `CES/ListDashboardInfos/v2` · 助 | 查询监控看板列表 | 读取 | — |
| `CES/ListDashboardWidgets/v2` · 助 | 查询指定监控看板下的监控视图列表 | 读取 | 需 `dashboard_id`。 |
| `CES/ListMetrics/v1` · 实 | 查询指标列表 | 读取 | ECS 基础指标用 SYS.ECS；维度来自目标实例。 |
| `CES/ListResourceGroup/v1` · 助 | 查询所有资源分组 | 读取 | — |
| `CES/ListResourceGroups/v2` · 助 | 查询资源分组列表 | 读取 | — |
| `CES/ListResourceGroupsServicesResources/v2` · 助 | 查询资源分组下指定服务类别特定维度的资源列表 | 读取 | 需 `group_id`、`service`。 |
| `CES/ShowMetricData/v1` · 实 | 查询监控数据 | 读取 | 已有指标及维度；from/to 为毫秒时间戳。 缺少标识时查 [CES/ListMetrics/v1](performance.md#ces)。 |
| `CES/ShowQuotas/v1` · 助 | 查询配额 | 读取 | — |
| `CES/ShowResourceGroup/v1` · 助 | 查询资源分组下的资源 | 读取 | 需 `group_id`。 |
| `CES/ShowResourceGroup/v2` · 助 | 查询指定资源分组详情 | 读取 | 需 `group_id`。 |
| `CES/ShowWidget/v2` · 助 | 查询指定监控视图信息 | 读取 | 需 `widget_id`。 |

## COC

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `COC/ListAssessTask/v1` · 助 | 分页查询评估任务列表 | 读取 | — |
| `COC/ListCapacityOrder/v1` · 助 | 查询应用、组件、分组容量数据的排名 | 读取 | — |
| `COC/ListCapacityView/v1` · 助 | 查询应用的容量数据 | 读取 | — |

## ECS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ECS/BatchResizeServers/v2` · 助 | 批量变更云服务器规格 | 修改或执行 | 需 `resize.servers.[N].id`。 |
| `ECS/ListResizeFlavors/v2` · 助 | 查询云服务器规格变更支持列表 | 读取 | — |
| `ECS/RegisterServerMonitor/v2` · 助 | 注册云服务器监控 | 注册监控 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ResizePostPaidServer/v2` · 助 | 变更云服务器规格(按需) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ResizeServer/v2` · 助 | 变更云服务器规格 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowFlavorCapacity/v2` · 助 | 查询规格的容量 | 读取 | 需 `flavor_id`。 |

## EVS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EVS/BatchResizeVolumes/v2` · 助 | 批量扩容云硬盘 | 修改或执行 | 需 `volumes.[N].id`。 |
| `EVS/ModifyVolumeQoS/v2` · 助 | 修改云硬盘QoS | 修改或执行 | 需 `volume_id`。 未知 volume_id 时查 [EVS/ListVolumes/v2](configuration.md#evs)。 |
| `EVS/ResizeVolume/v2` · 助 | 扩容云硬盘 | 修改或执行 | 需 `volume_id`。 未知 volume_id 时查 [EVS/ListVolumes/v2](configuration.md#evs)。 |
