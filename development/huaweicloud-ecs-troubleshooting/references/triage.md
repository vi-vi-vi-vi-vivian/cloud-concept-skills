# 分诊

确认目标、现象、时间窗和影响范围。已有事实足够时直接选命令分册。

| 现象 | 命令入口 | 配方规划 |
| --- | --- | --- |
| 启动失败、状态异常 | [故障](commands/fault.md)、[配置](commands/configuration.md) | [boot](recipes/boot.md) |
| 登录失败 | [网络配置](commands/configuration-network.md)、[安全](commands/security.md) | [login](recipes/login.md) |
| 网络不通、DNS 或 ELB 异常 | [网络配置](commands/configuration-network.md)、[性能](commands/performance.md) | [network](recipes/network.md) |
| 磁盘、挂载或容量异常 | [配置](commands/configuration.md)、[性能](commands/performance.md) | [storage](recipes/storage.md) |
| CPU、内存、IO 或业务变慢 | [性能](commands/performance.md) | [performance](recipes/performance.md) |
| 崩溃、卡死、异常重启 | [故障](commands/fault.md)、[共享审计](services.md#cts) | [crash](recipes/crash.md) |
| 配置未生效 | [配置](commands/configuration.md)、[网络配置](commands/configuration-network.md) | [configuration](recipes/configuration.md) |
| 疑似入侵或防护拦截 | [主机安全](commands/security-host.md)、[安全](commands/security.md) | [security](recipes/security.md) |
| 需要恢复方案 | [故障](commands/fault.md) | [recovery](recipes/recovery.md) |

配方仅为规划。新证据改变故障边界时切换分册。
