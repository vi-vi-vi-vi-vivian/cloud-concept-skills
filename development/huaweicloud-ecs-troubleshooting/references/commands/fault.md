# 故障 F

查询事件、诊断任务和结果。执行类操作按当前授权范围选择。

验证标记见[索引](index.md)。已知标识直接复用；依赖列不列全部参数。

目录：[AOM](#aom) · [APM](#apm) · [CBR](#cbr) · [CES](#ces) · [COC](#coc) · [DNS](#dns) · [ECS](#ecs) · [EIP](#eip) · [ELB](#elb) · [EVS](#evs) · [IMS](#ims) · [LTS](#lts) · [SMN](#smn) · [VPN](#vpn)

## AOM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `AOM/CountEvents/v2` · 助 | 统计事件告警信息 | 读取 | — |
| `AOM/ExecuteWorkflow/v1` · 助 | 执行工作流 | 执行工作流 | 需 `workflow_id`。 |
| `AOM/ListActionRule/v2` · 助 | 获取告警行动规则列表 | 读取 | — |
| `AOM/ListAlarmRule/v2` · 助 | 查询阈值规则列表 | 读取 | — |
| `AOM/ListAlarmRuleTemplate/v2` · 助 | 查询告警模板列表 | 读取 | — |
| `AOM/ListAllJobByName/v1` · 助 | 作业管理主页模糊查询 | 读取 | — |
| `AOM/ListAllScriptByName/v1` · 助 | 脚本查询 | 读取 | 需 `script_id`。 |
| `AOM/ListEvent2alarmRule/v2` · 助 | 查询事件类告警规则列表 | 读取 | — |
| `AOM/ListEvents/v2` · 助 | 查询事件告警信息 | 读取 | — |
| `AOM/ListMetricOrEventAlarmRule/v2` · 助 | 查询指标类或者事件类告警规则列表 | 读取 | — |
| `AOM/ListMuteRule/v2` · 助 | 获取静默规则列表 | 读取 | — |
| `AOM/ListNotificationTemplateByName/v2` · 助 | 根据消息通知模板名称查询消息通知模板 | 读取 | 需 `name`。 |
| `AOM/ListNotificationTemplates/v2` · 助 | 查询消息通知模板列表 | 读取 | — |
| `AOM/ListNotifiedHistories/v2` · 助 | 获取告警发送结果 | 读取 | — |
| `AOM/ListTemplateByJobId/v1` · 助 | 根据作业id查询方案(自定义模板)列表 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `AOM/ListWorkflow/v1` · 助 | 查询任务列表 | 读取 | — |
| `AOM/ListWorkflowExecutions/v1` · 助 | 获取任务执行历史 | 读取 | 需 `workflow_id`。 |
| `AOM/SearchTemplateById/v1` · 助 | 获取方案信息 | 读取 | 需 `template_id`。 |
| `AOM/SearchWorkflowExecutionDetail/v1` · 助 | 获取工作流执行中的执行详情 | 读取 | 需 `execution_id`、`workflow_id`。 复用已有任务标识。 |
| `AOM/ShowActionRule/v2` · 助 | 通过规则名称获取告警行动规则 | 读取 | 需 `rule_name`。 |
| `AOM/ShowAlarmRule/v2` · 助 | 查询单条阈值规则 | 读取 | 需 `alarm_rule_id`。 |

## APM

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `APM/ListAlarmData/v1` · 助 | 查询告警列表 | 读取 | 需 `x-business-id`、`business_id`。 |
| `APM/ListAlarmNotify/v1` · 助 | 查询告警消息列表 | 读取 | 需 `x-business-id`、`alarm_data_id`。 |

## CBR

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CBR/CheckAgent/v1` · 助 | 查询Agent状态 | 主动检查 | 需 `agent_status.[N].resource_id`。 |
| `CBR/ListOpLogs/v1` · 实·空 | 查询任务列表 | 读取 | — |
| `CBR/RestoreBackup/v1` · 助 | 备份恢复 | 恢复数据 | 需 `backup_id`。 未知 backup_id 时查 [CBR/ListBackups/v1](configuration.md#cbr)。 |
| `CBR/ShowOpLog/v1` · 助 | 查询单个任务 | 读取 | 需 `operation_log_id`。 未知 operation_log_id 时查 [CBR/ListOpLogs/v1](fault.md#cbr)。 |

## CES

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `CES/BatchEnableAlarmRules/v2` · 助 | 批量启停告警规则 | 修改或执行 | — |
| `CES/CreateAlarmRules/v2` · 助 | 创建告警规则(推荐) | 创建或配置 | — |
| `CES/CreateOneClickAlarm/v2` · 助 | 创建一键告警 | 创建或配置 | 需 `one_click_alarm_id`。 |
| `CES/ListAlarmHistories/v1` · 助 | 查询告警历史 | 读取 | — |
| `CES/ListAlarmHistories/v2` · 实·空 | 查询告警记录列表 | 读取 | 按目标资源筛选；from/to 使用 ISO 8601 字符串。 |
| `CES/ListAlarmRulePolicies/v2` · 助 | 查询告警规则策略列表 | 读取 | 需 `alarm_id`。 |
| `CES/ListAlarmRuleResources/v2` · 助 | 查询告警规则资源列表 | 读取 | 需 `alarm_id`。 |
| `CES/ListAlarmRules/v2` · 助 | 查询告警规则列表(推荐) | 读取 | — |
| `CES/ListAlarmTemplateAssociationAlarms/v2` · 助 | 查询告警模板关联的告警规则列表 | 读取 | 需 `template_id`。 |
| `CES/ListAlarmTemplates/v1` · 助 | 查询自定义告警模板列表 | 读取 | — |
| `CES/ListAlarmTemplates/v2` · 助 | 查询告警模板列表 | 读取 | — |
| `CES/ListAlarms/v1` · 助 | 查询告警规则列表(V1) | 读取 | — |
| `CES/ListEventDetail/v1` · 助 | 查询某一事件监控详情 | 读取 | 需 `event_name`。 |
| `CES/ListEvents/v1` · 实 | 查询事件监控列表 | 读取 | — |
| `CES/ListNotificationMaskResources/v2` · 助 | 查询告警通知屏蔽资源列表 | 读取 | 需 `notification_mask_id`。 |
| `CES/ListNotificationMasks/v2` · 助 | 查询告警通知屏蔽列表 | 读取 | — |
| `CES/ListOneClickAlarmRules/v2` · 助 | 查询一键告警关联告警规则列表 | 读取 | 需 `one_click_alarm_id`。 |
| `CES/ListOneClickAlarms/v2` · 助 | 查询一键告警列表 | 读取 | — |
| `CES/ShowAlarm/v1` · 助 | 查询单条告警规则信息 | 读取 | 需 `alarm_id`。 |
| `CES/ShowAlarmTemplate/v2` · 助 | 查询告警模板详情 | 读取 | 需 `template_id`。 |
| `CES/ShowEventData/v1` · 助 | 查询主机配置数据 | 读取 | 仅适用于 SAP HANA 的 SAP Monitor。 |
| `CES/UpdateAlarm/v1` · 助 | 修改告警规则 | 修改或执行 | 需 `alarm_id`。 |

## COC

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `COC/CancelDiagnosisTask/v1` · 助 | 取消诊断任务 | 取消诊断 | 需 `task_id`。 复用已有任务标识。 |
| `COC/CreateDiagnosisTask/v1` · 助 | 提交诊断任务 | 安装 Holmes、主机采集 | 目标已纳管；UniAgent 在线并具备采集授权。ECS 使用 type=ECS。 |
| `COC/CreateScheduledTask/v1` · 助 | 新建定时运维 | 创建或配置 | 需 `associated_task_id`。 |
| `COC/DisableScheduledTask/v1` · 助 | 禁用ScheduledTask | 修改或执行 | 需 `task_id`。 复用已有任务标识。 |
| `COC/EnableScheduledTask/v1` · 助 | 启用ScheduledTask | 修改或执行 | 需 `task_id`。 复用已有任务标识。 |
| `COC/ExecuteDocument/v1` · 助 | 执行自定义作业 | 执行作业 | 需 `document_id`。 |
| `COC/ExecutePublicScript/v1` · 助 | 执行公共脚本 | 主机执行 | 需 `script_uuid`、`execute_batches.[N].target_instances.[N].region_id`、`execute_batches.[N].target_instances.[N].resource_id`。 |
| `COC/ExecuteScript/v1` · 助 | 执行自定义脚本 | 主机执行 | 需 `script_uuid`、`execute_batches.[N].target_instances.[N].region_id`、`execute_batches.[N].target_instances.[N].resource_id`。 |
| `COC/GetDocument/v1` · 助 | 查询自定义作业详情 | 读取 | 需 `document_id`。 |
| `COC/GetDocumentAtomicInfo/v1` · 助 | 获取原子能力详情 | 读取 | 需 `atomic_unique_key`。 |
| `COC/GetExecution/v1` · 助 | 查询作业工单详情 | 读取 | 需 `execution_id`。 复用已有任务标识。 |
| `COC/GetPublicScript/v1` · 助 | 展示公共脚本详情 | 读取 | 需 `script_uuid`。 |
| `COC/GetScript/v1` · 助 | 获取自定义脚本详情 | 读取 | 需 `script_uuid`。 |
| `COC/GetScriptJobBatch/v1` · 助 | 展示批次详情 | 读取 | 需 `batch_index`、`execute_uuid`。 |
| `COC/GetScriptJobInfo/v1` · 助 | 展示脚本工单基本信息 | 读取 | 需 `execute_uuid`。 |
| `COC/GetScriptJobStatistics/v1` · 助 | 展示实例状态统计信息 | 读取 | 需 `execute_uuid`。 |
| `COC/ListAlarmHandleHistories/v1` · 助 | 查询告警工单历史 | 读取 | 需 `alarm_id`。 |
| `COC/ListCocTicketOperationHistories/v1` · 助 | GetCocTicketOperationHistories 获取事件单历史 | 读取 | 需 `ticket_type`。 |
| `COC/ListDiagnosisTasks/v1` · 实·空 | 查询诊断记录 | 读取 | 实测需 page_index 和 page_size；按 type、region 限定。 |
| `COC/ListDocumentAtomics/v1` · 助 | 获取原子能力列表 | 读取 | — |
| `COC/ListDocuments/v1` · 助 | 查询自定义作业列表 | 读取 | — |
| `COC/ListExecutionInstances/v1` · 助 | 查询工单步骤批次实例 | 读取 | — |
| `COC/ListExecutionSteps/v1` · 助 | 查询工单步骤详情 | 读取 | 需 `execution_id`。 复用已有任务标识。 |
| `COC/ListExecutions/v1` · 助 | 查询作业工单列表 | 读取 | — |
| `COC/ListIncidentSimpleTickets/v1` · 助 | 查询简易版事件单列表 | 读取 | — |
| `COC/ListIncidents/v1` · 助 | ListIncidents 查询事件单列表 | 读取 | — |
| `COC/ListIncidentsHistories/v1` · 助 | ListIncidentsHistories 获取事件单历史 | 读取 | 需 `incident_id`。 |
| `COC/ListInstancesBatch/v1` · 助 | 获取自动分批结果 | 计算分批 | 需 `target_instances.[N].region_id`、`target_instances.[N].resource_id`。 |
| `COC/ListPublicScripts/v1` · 助 | 获取公共脚本列表 | 读取 | — |
| `COC/ListScheduledTask/v1` · 助 | 查询ScheduledTask列表 | 读取 | — |
| `COC/ListScheduledTaskHistory/v1` · 助 | 查询定时运维历史记录 | 读取 | 需 `task_id`。 复用已有任务标识。 |
| `COC/ListScriptJobBatches/v1` · 助 | 展示批次列表 | 读取 | 需 `execute_uuid`。 |
| `COC/ListScriptJobs/v1` · 助 | 展示工单列表 | 读取 | — |
| `COC/ListScripts/v1` · 助 | 查询脚本列表 | 读取 | — |
| `COC/OperateExecution/v1` · 助 | 操作工单 | 修改或执行 | 需 `execution_id`。 复用已有任务标识。 |
| `COC/OperateScriptJob/v1` · 助 | 操作脚本工单 | 修改或执行 | 需 `execute_uuid`。 |
| `COC/ResetAccountPassword/v1` · 助 | 主机密码重置 | 修改或执行 | — |
| `COC/RetryDiagnosisTask/v1` · 助 | 重试诊断任务 | 重试诊断 | 需 `task_id`。 复用已有任务标识。 |
| `COC/ShowAlarm/v1` · 助 | 查询Alarm | 读取 | 需 `alarm_id`。 |
| `COC/ShowCocIncidentDetail/v1` · 助 | GetCocIncidentDetail 获取事件单详情 | 读取 | 需 `incident_num`。 |
| `COC/ShowCocIssuesDetail/v1` · 助 | GetCocIssuesDetail 获取问题单详情 | 读取 | 需 `ticket_id`。 |
| `COC/ShowDiagnosisNode/v1` · 助 | 查询指定诊断记录下的指定诊断步骤的详情 | 读取 | task_id、instance_id、code；步骤名以 help 为准。 |
| `COC/ShowDiagnosisSummary/v1` · 助 | 查询批量诊断任务的结果概要 | 读取 | 已有 task_id；未知时查 [COC/ListDiagnosisTasks/v1](fault.md#coc)。 |
| `COC/ShowDiagnosisTask/v1` · 助 | 查询单个诊断任务详情 | 读取 | task_id、instance_id；复用已有诊断任务。 |
| `COC/ShowIncidentTask/v1` · 助 | ShowIncidentTask 获取事件任务 | 读取 | 需 `incident_id`。 |
| `COC/ShowJobDetail/v1` · 助 | 查询任务详情 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `COC/ShowScheduledTask/v1` · 助 | 查询ScheduledTask | 读取 | 需 `task_id`。 复用已有任务标识。 |

## DNS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `DNS/ShowDomainDetection/v2` · 助 | 查询公网域名的域名诊断 | 查询诊断 | 需 `zone_id`。 |

## ECS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ECS/AcceptScheduledEvent/v2` · 助 | 接受并授权执行计划事件操作 | 修改或执行 | 需 `id`。 |
| `ECS/BatchRebootServers/v2` · 助 | 批量重启云服务器 | 修改或执行 | 需 `reboot.servers.[N].id`。 |
| `ECS/BatchResetServersPassword/v2` · 助 | 批量重置弹性云服务器密码 | 修改或执行 | 需 `servers.[N].id`。 |
| `ECS/BatchStartServers/v2` · 助 | 批量启动云服务器 | 修改或执行 | 需 `os-start.servers.[N].id`。 |
| `ECS/BatchStopServers/v2` · 助 | 批量关闭云服务器 | 修改或执行 | 需 `os-stop.servers.[N].id`。 |
| `ECS/ChangeServerOsWithCloudInit/v2` · 助 | 切换弹性云服务器操作系统(安装Cloud init) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ChangeServerOsWithoutCloudInit/v2` · 助 | 切换弹性云服务器操作系统(未安装Cloud init) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ExecuteServerDump/v2` · 助 | 触发云服务器内核dump | 触发内核转储 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ExecuteServerRedeploy/v2` · 助 | 重部署云服务器 | 重部署 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ListScheduledEvents/v2` · 实·空 | 查询计划事件列表 | 读取 | — |
| `ECS/MigrateServer/v2` · 助 | 冷迁移云服务器 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaListServerActions/v2` · 助 | 查询云服务器操作行为列表 | 读取 | 历史接口；操作审计优先 [CTS/ListTraces/v3](../services.md#cts)。 |
| `ECS/NovaRebootServer/v2` · 助 | 重启云服务器 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaShowServerAction/v2` · 助 | 通过请求ID查询云服务器行为 | 读取 | server_id、request_id；历史接口。 缺少标识时查 [ECS/NovaListServerActions/v2](fault.md#ecs)。 |
| `ECS/NovaStartServer/v2` · 助 | 启动云服务器 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/NovaStopServer/v2` · 助 | 关闭云服务器 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ReinstallServerWithCloudInit/v2` · 助 | 重装弹性云服务器操作系统(安装Cloud-init) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ReinstallServerWithoutCloudInit/v2` · 助 | 重装弹性云服务器操作系统(未安装Cloud init) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ResetServerPassword/v2` · 助 | 一键重置弹性云服务器密码(企业项目) | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowJob/v2` · 助 | 查询任务的执行状态 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `ECS/ShowResetPasswordFlag/v2` · 实 | 查询是否支持一键重置密码 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowSerialConsoleActions/v2` · 助 | 获取串口登录地址 | 生成登录地址 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowServerConsoleOutput/v2` · 实 | 获取弹性云服务器的控制台日志 | 读取 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/ShowServerRemoteConsole/v2` · 助 | 获取VNC远程登录地址 | 生成登录地址 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |
| `ECS/UpdateScheduledEvent/v2` · 助 | 更新计划事件 | 修改或执行 | 需 `id`。 |
| `ECS/UpdateSerialConsoleOptions/v2` · 助 | 设置云服务器云主机串口登录 | 修改或执行 | 需 `server_id`。 未知 server_id 时查 [ECS/ListServersDetails/v2](configuration.md#ecs)。 |

## EIP

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EIP/ShowResourcesJobDetail/v2` · 助 | 查询Job状态接口 | 读取 | 需 `job_id`。 复用已有任务标识。 |

## ELB

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `ELB/CreateMemberHealthCheckJob/v3` · 助 | 创建后端服务器检测任务 | 检测任务 | 需 `member_id`。 |
| `ELB/ListJobs/v3` · 助 | 查询异步任务的job列表 | 读取 | — |
| `ELB/ShowJob/v3` · 助 | 查询异步任务的job状态 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `ELB/ShowMemberHealthCheckJob/v3` · 助 | 查询后端服务器检测任务的结果 | 读取 | 需 `job_id`。 复用已有任务标识。 |

## EVS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `EVS/RollbackSnapshot/v2` · 助 | 回滚快照到云硬盘 | 回滚数据 | 需 `snapshot_id`、`rollback.volume_id`。 未知 snapshot_id 时查 [EVS/ListSnapshots/v2](configuration.md#evs)。 |
| `EVS/ShowJob/v2` · 助 | 查询job的状态 | 读取 | 需 `job_id`。 复用已有任务标识。 |

## IMS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `IMS/ShowJob/v2` · 助 | 异步任务查询 | 读取 | 需 `job_id`。 复用已有任务标识。 |
| `IMS/ShowJobProgress/v2` · 助 | 异步任务进度查询 | 读取 | 需 `job_id`。 复用已有任务标识。 |

## LTS

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `LTS/ListActiveOrHistoryAlarms/v2` · 助 | 查询活动或历史告警列表 | 读取 | — |
| `LTS/ListKeywordsAlarmRules/v2` · 助 | 查询关键词告警规则 | 读取 | — |
| `LTS/ListNotificationTemplates/v2` · 助 | 查询消息模板 | 读取 | — |
| `LTS/ListNotificationTopics/v2` · 助 | 查询SMN主题 | 读取 | — |
| `LTS/ListSqlAlarmRules/v2` · 助 | 查询SQL告警规则 | 读取 | — |
| `LTS/ShowNotificationTemplate/v2` · 助 | 查询单个消息模板 | 读取 | 需 `template_name`。 |

## SMN

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `SMN/ListTopicMessageStatistics/v2` · 助 | 查询主题的发送详情 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/PublishHttpDetect/v2` · 助 | 发布探测消息 | 发送探测消息 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/PublishMessage/v2` · 助 | 消息发布 | 发送消息 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |
| `SMN/ShowHttpDetectResult/v2` · 助 | 获取http探测结果 | 读取 | 需 `task_id`、`topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 复用已有任务标识。 |
| `SMN/ShowNotifyPolicy/v2` · 助 | 查询通知策略 | 读取 | 需 `topic_urn`。 未知 topic_urn 时查 [SMN/ListTopics/v2](configuration.md#smn)。 |

## VPN

| 命令与验证 | 用途 | 行为 | 条件依赖 |
| --- | --- | --- | --- |
| `VPN/CreateConnectionMonitor/v5` · 助 | 创建VPN连接监控 | 创建或配置 | 需 `connection_monitor.vpn_connection_id`。 |
| `VPN/ListConnectionMonitors/v5` · 助 | 查询VPN连接监控列表 | 读取 | — |
| `VPN/ListP2cVpnGatewayJobs/v5` · 助 | 查询资源任务列表 | 读取 | — |
| `VPN/ListVpnGatewayJobs/v5` · 助 | 查询资源任务列表 | 读取 | — |
| `VPN/ShowConnectionMonitor/v5` · 助 | 查询VPN连接监控 | 读取 | 需 `connection_monitor_id`。 |
