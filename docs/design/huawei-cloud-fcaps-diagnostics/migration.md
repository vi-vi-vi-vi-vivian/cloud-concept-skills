# 非 hcloud 命令迁移记录

范围：经确认的基础事实查询、前置发现和有条件采集。共 72 个模式；不是对所有上游脚本逐行复制。保留原 1,282 个云操作。

来源为 2026-10-18 已下载快照；中文契约重新编写，未复制上游脚本。通用主机查询不携带阿里云服务名、云助手参数或固定路径。Kubernetes 移除 GKE 凭据前置，端点查询采用 EndpointSlice。

| 命令 ID | FCAPS | 来源与定位 | 决策 |
| --- | --- | --- | --- |
| `LINUX/os-release` | common | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L47) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/kernel` | common | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-hotplug-disk.md#L8) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/identity` | common | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L4) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/units` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/network-perf-unexpected.md#L39) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/service-status` | fault | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/network-perf-unexpected.md#L39) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/unit-journal` | fault | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/clock-abnormal.md#L38) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/kernel-journal` | fault | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/clock-abnormal.md#L38) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/kernel-ring` | fault | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/clock-abnormal.md#L38) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/block-devices` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-pe-prep.md#L96) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/mounts` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-pe-prep.md#L187) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/addresses` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L3) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/routes` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L3) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/rules` | configuration | 目标帮助与实测 | 新增配套查询：多路由表解释需策略规则；依据目标 iproute2 帮助与实测 |
| `LINUX/modules` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-malware-mining.md#L32) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/timers` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/network-perf-unexpected.md#L39) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/process-snapshot` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L24) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/memory` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/guestos-not-running.md#L11) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/vm-sample` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/memory-oom.md#L23) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/disk-sample` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/disk-iops-high.md#L23) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/process-io` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/cpu-high.md#L41) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/cpu-sample` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/network-latency-high.md#L33) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/filesystem-space` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/diagnosis-report-template.md#L27) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/filesystem-inodes` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/diagnosis-report-template.md#L27) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/nic-statistics` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L3) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/driver-statistics` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/network-latency-high.md#L36) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/connections` | configuration | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L4) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/dns-query` | fault | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-pe-prep.md#L213) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/recent-logins` | security | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L52) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/failed-logins` | security | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-malware-mining.md#L45) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/cron` | security | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-malware-mining.md#L14) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/rpm-verify` | security | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-malware-mining.md#L41) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/deb-verify` | security | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/references/utils/guestos-malware-mining.md#L41) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/packet-capture` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L52) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/syscall-trace` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L52) | 通用命令提炼；语法按目标工具核验 |
| `LINUX/perf-sample` | performance | [S19](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-linux-os-troubleshooting/SKILL.md#L4) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/os` | common | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/WORKFLOW-GUIDE.md#L485) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/powershell` | common | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L93) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/services` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L180) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/service-status` | fault | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L180) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/events` | fault | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/fixes/rdp-auth.md#L149) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/disks` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/WORKFLOW-GUIDE.md#L135) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/partitions` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/WORKFLOW-GUIDE.md#L494) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/volumes` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/WORKFLOW-GUIDE.md#L698) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/adapters` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L234) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/routes` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L234) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/connections` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/WORKFLOW-GUIDE.md#L521) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/counter` | performance | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/performance-slow.md#L36) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/processes` | performance | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/WORKFLOW-GUIDE.md#L692) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/nic-statistics` | performance | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/scripts/networking-tcpip.ps1#L211) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/dns` | fault | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/fixes/networking-dns.md#L84) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/tcp-probe` | fault | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/REMOTE-EXECUTION.md#L234) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/firewall` | security | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/fixes/cloud-metaserver.md#L12) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/firewall-ports` | security | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/fixes/cloud-metaserver.md#L12) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/acl` | security | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/offline/cloud-agent.md#L71) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/local-users` | security | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/WORKFLOW-GUIDE.md#L519) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/local-group` | security | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/WORKFLOW-GUIDE.md#L520) | 通用命令提炼；语法按目标工具核验 |
| `WINDOWS/counter-discovery` | configuration | [S20](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills/blob/809887f613b50aa31c088cac4944fd3b8c1ac521/skills/alibabacloud-ecs-windows-os-troubleshooting/references/online/performance-slow.md#L36) | 通用命令提炼；语法按目标工具核验 |
| `KUBERNETES/context` | common | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/nodes` | configuration | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/pods` | configuration | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/pod-events` | fault | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/pod-describe` | fault | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/container-logs` | fault | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/previous-logs` | fault | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/storage` | configuration | [S14](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-storage-troubleshooting/SKILL.md#L33) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/pv` | configuration | [S14](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-storage-troubleshooting/SKILL.md#L33) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/storageclasses` | configuration | [S14](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-storage-troubleshooting/SKILL.md#L33) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/endpoints` | configuration | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L296) | 通用 kubectl；移除 GKE 前置依赖；Endpoints 改为 EndpointSlice |
| `KUBERNETES/pod-usage` | performance | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/node-usage` | performance | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/networkpolicy` | security | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |
| `KUBERNETES/permission` | security | [S13](https://github.com/google/skills/blob/e86adb9e2b80220a593c2be9a68627171fd17afb/skills/cloud/gke-workload-troubleshooting/SKILL.md#L29) | 通用 kubectl；移除 GKE 前置依赖 |

## 合并、排除与适配边界

| 来源内容 | 处理及原因 |
| --- | --- |
| 阿里云云助手、诊断报告、云监控 API | 不照搬命令；COC、CES 等沿用现有华为云契约，执行通道单独说明 |
| 上游同一查询在多个场景出现 | 合并为一个模式；场景只引用 |
| Linux perf top、持续 iostat、持续跟踪 | 改为有时间或次数边界的模式；采集影响仍保留 |
| Windows 离线挂盘、注册表加载、修复脚本 | 本批不执行或迁移为默认查询；需独立的离线作用域与影响核验 |
| 修改网络、重启、杀进程、修改内核、删除文件、安装组件 | 非事实查询；不作为查询的默认前置操作 |
| 恶意软件的推断规则 | 仅保留观测工具，不移植“单一异常即证明入侵”的结论 |
| 其他云的 hcloud、tccli、aws 等 | 不纳入华为云命令空间；Hetzner hcloud 与 KooCLI 分开 |
| macOS 本地环境 | 只作 Agent 与 kubectl 客户端；Linux 契约在目标 Ubuntu 执行 |

## 验证范围

Linux 使用真实华为云 Ubuntu 主机。Kubernetes 使用用户授权安装的独立本地 kind 集群；该结果不代表 CCE。Windows 无适用主机，逐条记录受阻。条件抓包、跟踪和完整性扫描没有执行。原始证据留在忽略的工作区。

## 官方文档补充

2026-10-22：新增 28 个模式及适配修正，见[官方文档审阅](official-docs-review.md)。上表保留初始 72 个模式的来源记录；当前总数以命令契约与验证清单为准。
