# Service：发现与共享查询

先选命令，再查询该操作的 help。下表中的共享查询按当前问题引用。

验证标记见[索引](commands/index.md)。已知标识直接复用；依赖列不列全部参数。

命令 ID 为 `Service/Operation/version`。调用形式为 `rtk proxy hcloud Service Operation/version`。

```bash
rtk proxy hcloud --help
rtk proxy hcloud ECS --help
rtk proxy hcloud ECS ShowServer/v2 --help
```

CLI 版本后缀与 HTTP 路径版本可能不同。使用本文件核实的命令 ID。

目录：[CTS](#cts) · [EPS](#eps) · [IAM](#iam) · [LTS](#lts)

## CTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CTS/ListTraces/v3` · 实 | 查询事件列表 | 读取 | 管理事件用 trace_type=system；在线记录窗口为近 7 天。 |

## EPS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EPS/ListEnterpriseProject/v1` · 阻·调用 | 查询企业项目列表 | 读取 | — 本次调用受阻：EPS.0004。 |
| `EPS/ListProviders/v1` · 助 | 查询企业项目支持的服务 | 读取 | — |
| `EPS/ListResourceMapping/v1` · 助 | 查询资源类型映射 | 读取 | — |
| `EPS/ShowAssociatedResources/v1` · 助 | 查询关联资源 | 读取 | 需 `resource_id`、`region_id`。 |
| `EPS/ShowEnterpriseProject/v1` · 助 | 查询企业项目详情 | 读取 | 需 `enterprise_project_id`。 |
| `EPS/ShowResourceBindEnterpriseProject/v1` · 助 | 查询企业项目绑定的资源列表 | 读取 | 需 `enterprise_project_id`。 |

## IAM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `IAM/KeystoneListAuthDomains/v3` · 助 | 查询IAM用户可以访问的账号详情 | 读取 | — |
| `IAM/KeystoneListAuthProjects/v3` · 实 | 查询IAM用户可以访问的项目列表 | 读取 | — |
| `IAM/KeystoneListEndpoints/v3` · 助 | 查询终端节点列表 | 读取 | — |
| `IAM/KeystoneListProjects/v3` · 实 | 查询指定条件下的项目列表 | 读取 | — |
| `IAM/KeystoneListProjectsForUser/v3` · 助 | 查询指定IAM用户的项目列表 | 读取 | 需 `user_id`。 |
| `IAM/KeystoneListRegions/v3` · 实 | 查询区域列表 | 读取 | — |
| `IAM/KeystoneListServices/v3` · 助 | 查询服务列表 | 读取 | — |
| `IAM/KeystoneShowCatalog/v3` · 助 | 查询服务目录 | 读取 | — |
| `IAM/KeystoneShowProject/v3` · 助 | 查询项目详情 | 读取 | — |
| `IAM/ShowProjectDetailsAndStatus/v3` · 助 | 查询项目详情与状态 | 读取 | — |

## LTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `LTS/ListBreifStructTemplate/v2` · 助 | 查询结构化模板简略列表 | 读取 | — |
| `LTS/ListCriterias/v2` · 助 | 获取快速查询 | 读取 | 需 `group_id`、`topic_id`。 |
| `LTS/ListHistorySql/v2` · 助 | 查询用户历史sql | 读取 | 需 `log_group_id`、`log_stream_id`。 未知 log_group_id 时查 [LTS/ListLogGroups/v2](services.md#lts)。 |
| `LTS/ListLogContext/v2` · 助 | 查询上下文日志 | 读取 | 使用已查日志的 line_num；自定义时间另需 __time__。 缺少标识时查 [LTS/ListLogs/v2](services.md#lts)。 |
| `LTS/ListLogGroups/v2` · 实·空 | 查询账号下所有日志组 | 读取 | — |
| `LTS/ListLogHistogram/v2` · 助 | 查询日志直方图 | 读取 | 需 `group_id`、`stream_id`。 |
| `LTS/ListLogStream/v2` · 助 | 查询指定日志组下的所有日志流 | 读取 | 需 `log_group_id`。 未知 log_group_id 时查 [LTS/ListLogGroups/v2](services.md#lts)。 |
| `LTS/ListLogStreamIndex/v2` · 助 | 查询日志流索引 | 读取 | 需 `group_id`、`stream_id`。 |
| `LTS/ListLogStreams/v2` · 助 | 查询日志流信息 | 读取 | — |
| `LTS/ListLogs/v2` · 助 | 查询日志 | 读取 | 日志组、日志流及时间窗；仅查询已接入日志。 |
| `LTS/ListQueryAllSearchCriterias/v2` · 助 | 查询日志组下所有快速查询 | 读取 | 需 `group_id`。 |
| `LTS/ListQueryStructuredLogs/v2` · 助 | 查询结构化日志 | 读取 | 需 `log_group_id`、`log_stream_id`。 未知 log_group_id 时查 [LTS/ListLogGroups/v2](services.md#lts)。 |
| `LTS/ListStructTemplate/v2` · 助 | 查询结构化模板 | 读取 | — |
| `LTS/ListStructuredLogsWithTimeRange/v2` · 助 | 查询结构化日志(新版) | 读取 | 需 `log_stream_id`。 未知 log_stream_id 时查 [LTS/ListLogStreams/v2](services.md#lts)。 |
| `LTS/ShowStructTemplate/v2` · 助 | 查询结构化配置 | 读取 | — |
