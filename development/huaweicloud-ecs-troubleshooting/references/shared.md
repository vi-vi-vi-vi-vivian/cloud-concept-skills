# Shared

- 使用已配置的 hcloud。缺少 CLI 或认证时说明缺口。
- 用 `--cli-profile` 和 `--cli-region` 选择已有配置和区域。API 要求 `project_id` 时使用对应区域的 IAM project。企业项目与 IAM project 分别处理。
- 用 `rtk proxy hcloud configure test` 检查本地配置格式。认证是否有效，以实际 API 响应为准。
- 命令行数组使用 `.1`、`.2`。详细参数、枚举和分页方式查当前操作的 help。
- 已核实的同版本帮助可在会话中复用。help 失败时暂停该操作，继续其他可用证据路径。
- 检查响应中的错误对象。CLI 退出码为 0 也可能表示调用失败。
- 保留资源范围和时间窗。指标毫秒时间戳与告警 ISO 8601 字符串分别按接口要求填写。
- 列表翻页直到所需范围完整。未收全时注明范围和下一页标识。
- 业务影响按契约判断。GET 可能启动检测；POST 可能只读取数据。
- 配置、调试输出、控制台日志和登录地址可能包含敏感内容。报告只保留诊断所需字段。

## 工具入口

下表命令接在 `rtk proxy hcloud` 后。`本地实测` 表示实际执行；`助` 表示只执行帮助查询。

| 命令 | 用途 | 行为 | 验证 |
| --- | --- | --- | --- |
| `version` | 查看 CLI 版本 | 读取 | 本地实测 |
| `configure test` | 检查配置文件格式 | 检查 | 本地实测 |
| `configure list` | 查看配置项列表 | 本地读取 | 助 |
| `configure show` | 查看指定配置项 | 本地读取 | 助 |
| `configure set` | 配置认证与默认作用域 | 修改本地配置 | 助 |
| `log show` | 查看 CLI 日志配置 | 本地读取 | 助 |
| `log set` | 调整本地日志级别 | 修改本地配置 | 助 |
| `meta download` | 更新离线元数据 | 下载并修改缓存 | 助 |
| `meta clear` | 清理损坏或过期元数据 | 删除本地缓存 | 助 |
| `update` | 更新 CLI 版本 | 修改本机安装 | 助 |

## 诊断选项

以下选项已核验根帮助。使用时附加到所选命令，详细格式查 help。

| 选项 | 用途与约束 |
| --- | --- |
| `--debug` | 输出调用信息；原命令仍执行。 |
| `--dryrun` | 预览请求；跳过目标业务 API，仍可能读取元数据或项目资料。 |
| `--skeleton` | 生成 JSON 入参骨架。 |
| `--cli-profile`、`--cli-region`、`--cli-project-id` | 选择配置、区域与默认项目。API 的 `project_id` 另按操作 help 填写。 |
| `--cli-domain-id`、`--cli-x-project-id` | 指定账号或鉴权项目；按 API 要求使用。 |
| `--cli-endpoint` | 排查端点选择；使用官方服务端点。 |
| `--cli-connect-timeout`、`--cli-read-timeout`、`--cli-retry-count` | 设置连接、读取超时与重试；重试不会修复权限拒绝。 |
| `--cli-query`、`--cli-output` | 筛选返回字段与显示格式；不改变服务端查询范围。 |
| `--cli-waiter` | 轮询原 API；使用前确认原操作只读。 |

命令发现与共享查询见 [Service](services.md)。
