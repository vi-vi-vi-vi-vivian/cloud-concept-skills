# 扩展与边界

HCS 操作只适用于对应环境。敏感读取和订购命令仅用于识别边界。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[AOM](#aom) · [APM](#apm) · [ECS](#ecs) · [HCSCLOUDNETDEBUG](#hcscloudnetdebug) · [HSS](#hss) · [SecMaster](#secmaster)

## AOM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `AOM/ListAccessCode/v2` · 助 | 获取Prometheus实例调用凭证 | 敏感读取 | — |

## APM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `APM/ListAkSk/v1` · 助 | 获取ak/sk | 敏感读取 | — |
| `APM/ShowAkSks/v1` · 助 | 查询租户的aksk | 敏感读取 | — |
| `APM/ShowToken/v1` · 助 | 获取链路追踪应用的token | 敏感读取 | 需 `x-business-id`、`business_id`。 |

## ECS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ECS/ShowServerPassword/v2` · 助 | 云服务器获取密码(企业项目) | 敏感读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |

## HCSCLOUDNETDEBUG

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `HCSCLOUDNETDEBUG/CreateCurSessionElbQuery/v1` · 助 | 创建ELB当前连接查询任务 | 创建或配置 | — |
| `HCSCLOUDNETDEBUG/CreateHistSessionElbQuery/v1` · 助 | 创建ELB历史连接查询任务 | 创建或配置 | 需 `elb_id`。 |
| `HCSCLOUDNETDEBUG/ListCurSessionElbTask/v1` · 助 | ELB当前连接查询任务列表 | 读取 | — |
| `HCSCLOUDNETDEBUG/ListFlowMonitors/v1` · 助 | 查看网络流监控列表 | 读取 | — |
| `HCSCLOUDNETDEBUG/ListFlowPaths/v1` · 助 | 查询获取业务流监控数据 | 读取 | 需 `id`。 |
| `HCSCLOUDNETDEBUG/ListHistSessionElbTask/v1` · 助 | ELB历史连接查询任务列表 | 读取 | — |
| `HCSCLOUDNETDEBUG/ListVmInfo/v1` · 助 | 查询id信息 | 读取 | — |
| `HCSCLOUDNETDEBUG/Listinstances/v1` · 助 | 查询实例或注入点信息 | 读取 | — |
| `HCSCLOUDNETDEBUG/ShowElbCurSessionElbTaskDetail/v1` · 助 | ELB当前连接查询任务结果查询 | 读取 | 需 `task_id`。 复用已有任务标识。 |
| `HCSCLOUDNETDEBUG/ShowElbHistSessionElbTaskDetail/v1` · 助 | ELB历史连接查询任务结果查询 | 读取 | 需 `task_id`。 复用已有任务标识。 |
| `HCSCLOUDNETDEBUG/ShowFullLinkPaths/v1` · 助 | 全链路虚拟路径查询 | 读取 | 需 `dst_id`、`src_id`。 |
| `HCSCLOUDNETDEBUG/StartElbCurSessionElbTask/v1` · 助 | 执行ELB当前连接查询任务 | 修改或执行 | 需 `task_id`。 复用已有任务标识。 |
| `HCSCLOUDNETDEBUG/StartElbHistSessionElbTask/v1` · 助 | 执行ELB历史连接查询任务 | 修改或执行 | 需 `task_id`。 复用已有任务标识。 |

## HSS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `HSS/CreateQuotasOrder/v5` · 助 | HSS服务创建订单订购配额 | 订购或配置 | — |

## SecMaster

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `SecMaster/CreateSubscriptionOrder/v1` · 助 | 开通或配置安全云脑订阅 | 订购或配置 | — |
