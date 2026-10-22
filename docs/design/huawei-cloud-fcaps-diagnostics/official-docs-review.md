# 华为云官方 ECS 文档补充审阅

来源：引用任务“下载华为云故障排除文档”的本地归档，2026-10-22 审阅。目录包含 452 个 Markdown 文件：llms.txt 中的故障排除 190 篇、常见问题 251 篇，加保留的索引等文件。

方法：全目录扫描候选工具；逐条读取采用条目的原文上下文；以实际帮助和目标主机执行校正语法。导航、输出样例、安装和修复语句不直接当诊断命令。截图未做全量 OCR，因此不宣称穷尽截图中独有的工具。

新增 28 个模式：Linux 23、Windows 5。已有命令补充边界，不重复定义。未新增 hcloud 操作，也未据 ECS 文档推导 Kubernetes 命令。

| 命令 ID | FCAPS | 官方来源 | 处理理由 |
| --- | --- | --- | --- |
| `LINUX/icmp-probe` | fault | [高频常见问题/ecs_faq_2604.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_2604.html)，归档行 5 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/mtr-report` | fault | [故障排除/zh-cn_topic_0191526703.md](https://support.huaweicloud.com/trouble-ecs/zh-cn_topic_0191526703.html)，归档行 1513 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/trace-route` | fault | [高频常见问题/ecs_faq_2604.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_2604.html)，归档行 5 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/deleted-open-files` | fault | [故障排除/ecs_trouble_1552.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_1552.html)，归档行 107 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/disk-by-id` | configuration | [高频常见问题/ecs_faq_2529.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_2529.html)，归档行 9 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/udev-device` | configuration | [高频常见问题/zh-cn_topic_0103285575.md](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0103285575.html)，归档行 80 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/filesystem-id` | configuration | [高频常见问题/ecs_faq_2529.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_2529.html)，归档行 4 | 由官方重复 UUID 场景提炼 blkid 文件系统标识查询；不复制修改 UUID 的命令 |
| `LINUX/partition-table` | configuration | [高频常见问题/ecs_faq_1127.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_1127.html)，归档行 15 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/kernel-setting` | configuration | [故障排除/ecs_trouble_0317.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0317.html)，归档行 10 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/service-enabled` | configuration | [故障排除/ecs_trouble_0313.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0313.html)，归档行 16 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/network-manager` | configuration | [故障排除/ecs_trouble_0313.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0313.html)，归档行 21 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/directory-usage` | performance | [故障排除/ecs_trouble_1552.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_1552.html)，归档行 40 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/run-queue` | performance | [故障排除/ecs_trouble_0372.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0372.html)，归档行 30 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/thread-inventory` | performance | [故障排除/ecs_trouble_0372.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0372.html)，归档行 18 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/conntrack-capacity` | performance | [故障排除/ecs_trouble_0324.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0324.html)，归档行 10 | 由官方连接跟踪容量场景提炼只读 count/max 查询；不是复制 sysctl -w 修复命令 |
| `LINUX/cpu-mitigation` | security | [故障排除/ecs_trouble_1790.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_1790.html)，归档行 21 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/iptables-filter` | security | [故障排除/ecs_trouble_0104.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0104.html)，归档行 1516 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/firewalld-state` | security | [故障排除/ecs_trouble_0402.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0402.html)，归档行 46 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/firewalld-zones` | security | [故障排除/zh-cn_topic_0000001694942236.md](https://support.huaweicloud.com/trouble-ecs/zh-cn_topic_0000001694942236.html)，归档行 16 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/firewalld-rules` | security | [故障排除/zh-cn_topic_0000001694942236.md](https://support.huaweicloud.com/trouble-ecs/zh-cn_topic_0000001694942236.html)，归档行 9 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/chrony-sources` | configuration | [高频常见问题/zh-cn_topic_0093971249.md](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0093971249.html)，归档行 88 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/ntp-peers` | configuration | [高频常见问题/zh-cn_topic_0093971249.md](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0093971249.html)，归档行 164 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `LINUX/metadata-http` | fault | [高频常见问题/ecs_faq_1322.md](https://support.huaweicloud.com/ecs_faq/ecs_faq_1322.html)，归档行 35 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `WINDOWS/logical-disk-links` | configuration | [高频常见问题/zh-cn_topic_0103285575.md](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0103285575.html)，归档行 57 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `WINDOWS/disk-identity` | configuration | [高频常见问题/zh-cn_topic_0103285575.md](https://support.huaweicloud.com/ecs_faq/zh-cn_topic_0103285575.html)，归档行 120 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `WINDOWS/signed-drivers` | configuration | [故障排除/ecs_trouble_0278.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0278.html)，归档行 29 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `WINDOWS/pid-services` | fault | [故障排除/ecs_trouble_0213.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0213.html)，归档行 14 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |
| `WINDOWS/firewall-profile-state` | security | [故障排除/ecs_trouble_0401.md](https://support.huaweicloud.com/trouble-ecs/ecs_trouble_0401.html)，归档行 23 | 提取事实查询；按目标环境帮助与执行核验；移除安装和修复步骤 |

## 合并、修正和未纳入

| 原文工具或说法 | 处理 | 理由 |
| --- | --- | --- |
| df/free/top/vmstat/iostat、ip/route、journalctl/dmesg、tcpdump | 复用已有模式；补充 df/du、时间口径和执行影响边界 | 避免同义条目和重复上下文 |
| netstat / findstr / grep 端口文本 | 复用 ss 或 Get-NetTCPConnection；要求数值端口精确匹配 | 子串 80 可能误匹配其他端口 |
| sar -q 的历史统计、sar --q 字样 | 使用已验证 sar -q 1 5 | 显式当前有限采样，不混淆历史文件与当前状态 |
| lsof 管道及终止进程步骤 | 使用 +L1 字段输出，限定时长；不终止进程 | 精确查询未链接打开文件；查询不隐含修复 |
| 文件系统 UUID 与磁盘标识 | 增加 blkid、udev、by-id，细化 H-device | UUID 可因克隆重复；序列号映射按 bus 分支 |
| VBD 序列号前 20 位 | 增加 virtio、整盘、实例内唯一性和 PCI 检查 | 解决上次缺证据的映射，不外推 SCSI/WWN/XEN |
| CPU 缓解状态与禁用建议 | 只读取 sysfs；Not affected 不解释为已关闭缓解 | 状态观测不授权降低防护 |
| sysctl -w/-p、iptables -A、路由添加、磁盘修复、重启 | 不迁移为事实查询 | 会改变系统或数据 |
| netperf／iperf3 并发测试 | 留作后续有负载测试候选，不执行、不创建监听端 | 需要测试对端、吞吐预算、并发和时长范围；现有授权仅覆盖本次诊断验证 |
| 第三方公网 IP 回显网站 | 本批不新增默认请求 | 出口 NAT 地址不等于绑定 EIP；发送至第三方不是默认前置 |
| 元数据 curl | 只读固定根目录 HTTP 状态，绕过代理且丢弃正文 | 检查链路，不读取临时凭据或遍历元数据 |
| NFS 预读、mountpoint/bdi 命令 | 保留为 NFS 专项候选，未添加通用规则 | 无 NFS 测试对象；不能把 NFS 条件直接用于所有本地挂载 |
| perfmon、WinMTR、VNC 与控制台入口 | 保留来源中的人工辅助路径，不伪装为返回结构化事实的命令 | 依赖交互环境；现有通道说明与 Windows 工具入口承接 |
| Windows 旧 wmic/Get-WmiObject | 优先补充 CIM 模式 | 按原文现代分支提炼；未把版本相关的旧工具作为必装依赖 |
| 费用中心、续费页面 | 复用现有 A 类查询 | 原文未提供新增 hcloud 计费命令；续费不是查询 |

## 证据边界

Linux 在已授权的 Ubuntu ECS 上核验；ping/MTR 仅使用回环测试语法和输出，不能宣称公网链路正常。Windows 没有适用环境，新增条目继续标为受阻。缺少 traceroute、firewalld 或 NTP 工具时不安装补齐。原有五项条件扫描／采集仍未运行。Recipe 继续只保留规划。

运行文档只承载地图与必要约束。原文出处、取舍与本次原因集中在此，避免每次调用加载归档全文。

## Windows 语法复核

微软 [tasklist 参数说明](https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist)规定 /svc 使用 table 格式；已将初稿的 CSV 组合改为 table。该文档核对不记为 Windows 实测。

[Win32_PnPSignedDriver 定义](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/whqlprov/win32-pnpsigneddriver)包含 DeviceClass、DeviceID、DeviceName、DriverVersion 和 DriverDate；按 NET 类筛选，避免从名称子串直接断定驱动故障。
