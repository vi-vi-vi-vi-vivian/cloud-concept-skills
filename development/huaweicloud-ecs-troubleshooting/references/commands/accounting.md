# 计量计费 A

核对用量、费用和订购状态。BSS 查询按账号站点和 help 选择区域。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[BSS](#bss) · [LTS](#lts) · [WAF](#waf)

## BSS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `BSS/ListCosts/v2` · 助 | 查询成本数据 | 读取 | 需 `time_condition.time_measure_id`。 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerBillsFeeRecords/v2` · 助 | 查询流水账单 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerBillsMonthlyBreakDown/v2` · 助 | 查询月度成本 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerOnDemandResources/v2` · 助 | 查询客户按需资源列表 | 读取 | 需 `customer_id`。 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerOrders/v2` · 助 | 查询订单列表 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerselfResourceRecordDetails/v2` · 助 | 查询资源详单 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListCustomerselfResourceRecords/v2` · 助 | 查询资源消费记录 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListFreeResourceInfos/v2` · 助 | 查询资源包列表 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListFreeResourceUsages/v2` · 助 | 查询资源包使用量 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListFreeResourcesUsageRecords/v2` · 助 | 查询资源包使用明细 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ListPayPerUseCustomerResources/v2` · 实 | 查询客户包年/包月资源列表 | 读取 | 查询包年/包月资源；当前 CLI 使用 cn-north-1。 |
| `BSS/ShowCustomerAccountBalances/v2` · 实 | 查询账户余额 | 读取 | 当前 CLI 使用 cn-north-1。 |
| `BSS/ShowCustomerMonthlySum/v2` · 助 | 查询汇总账单 | 读取 | — 帮助使用区域 cn-north-1。 |
| `BSS/ShowCustomerOrderDetails/v2` · 助 | 查询订单详情 | 读取 | 需 `order_id`。 帮助使用区域 cn-north-1。 |

## LTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `LTS/EnableLogCollection/v2` · 助 | 打开超额采集开关 | 开启超额采集 | — |
| `LTS/ListTimeLineTrafficStatistics/v2` · 助 | 按时间段统计查询资源 | 读取 | — |
| `LTS/ListTopnTrafficStatistics/v2` · 助 | 统计top n的日志组或日志流流量 | 读取 | — |

## WAF

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `WAF/ConfirmUserBundle/v1` · 助 | 获取用户套餐信息 | 读取 | — |
| `WAF/ShowSubscriptionInfo/v1` · 助 | 查询租户订购信息 | 读取 | — |
