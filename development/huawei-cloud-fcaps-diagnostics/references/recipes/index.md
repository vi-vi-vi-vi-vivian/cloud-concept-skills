# Recipe 索引

按实际现象和环境选正文；不明确时读[分诊](../triage.md)。以下均为 draft：已整理诊断指导，工具缺口及真实环境验证仍待补。执行沿用共同约束，具体命令只引用 commands；待补项不是可调用工具。

| 现象 / 任务 | 环境 | Recipe | 状态 |
| --- | --- | --- | --- |
| SSH 建立连接超时 | ECS（系统范围见正文） | [ecs-login-ssh-timeout](login/ssh-timeout.sop.md) | draft |
| SSH 认证失败 | ECS（系统范围见正文） | [ecs-login-ssh-auth-failed](login/ssh-auth-failed.sop.md) | draft |
| RDP 远程桌面不可用 | Windows ECS | [ecs-login-rdp-unavailable](login/rdp-unavailable.sop.md) | draft |
| 实例启动失败或 OS 未就绪 | ECS（系统范围见正文） | [ecs-instance-state-boot-failed](instance-state/boot-failed.sop.md) | draft |
| 意外重启或系统崩溃 | ECS（系统范围见正文） | [ecs-instance-state-unexpected-reboot](instance-state/unexpected-reboot.sop.md) | draft |
| 实例出网或业务目标不可达 | ECS（系统范围见正文） | [ecs-network-outbound-unreachable](network/outbound-unreachable.sop.md) | draft |
| DNS 解析失败或结果异常 | ECS（系统范围见正文） | [ecs-network-dns-resolution-failed](network/dns-resolution-failed.sop.md) | draft |
| 网络丢包或间歇重传 | ECS（系统范围见正文） | [ecs-network-packet-loss](network/packet-loss.sop.md) | draft |
| 磁盘空间或 inode 不足 | ECS（系统范围见正文） | [ecs-storage-disk-full](storage/disk-full.sop.md) | draft |
| 扩容后容量未增加 | ECS（系统范围见正文） | [ecs-storage-disk-expand-failed](storage/disk-expand-failed.sop.md) | draft |
| 文件系统挂载失败或挂载异常 | ECS（系统范围见正文） | [ecs-storage-mount-failed](storage/mount-failed.sop.md) | draft |
| 回收已确认可释放的磁盘空间 | ECS（系统范围见正文） | [ecs-storage-reclaim-disk-space](storage/reclaim-disk-space.sop.md) | draft |
| CPU 使用率异常升高 | ECS（系统范围见正文） | [ecs-performance-high-cpu](performance/high-cpu.sop.md) | draft |
| 系统负载升高 | ECS（系统范围见正文） | [ecs-performance-high-load](performance/high-load.sop.md) | draft |
| 内存压力或分配失败 | ECS（系统范围见正文） | [ecs-performance-memory-pressure](performance/memory-pressure.sop.md) | draft |
| 确认与分析 OOM 终止事件 | ECS（系统范围见正文） | [ecs-performance-oom-kill](performance/oom-kill.sop.md) | draft |
| 磁盘 IO 延迟升高 | ECS（系统范围见正文） | [ecs-performance-high-io-latency](performance/high-io-latency.sop.md) | draft |
| cloud-init 或 user-data 初始化失败 | ECS（系统范围见正文） | [ecs-configuration-cloud-init-failed](configuration/cloud-init-failed.sop.md) | draft |
| 云 API 权限被拒 | 华为云 API | [ecs-security-api-permission-denied](security/api-permission-denied.sop.md) | draft |

SSH 超时的云侧/主机端点、启动故障的离线调查仅按父篇条件读取。未覆盖的 Windows 系统细分、VNC、费用问题及安全事件响应回到分诊选择事实，不套用 Linux 流程。维护者读[结构](STRUCTURE.md)与[模板](template.md)。
