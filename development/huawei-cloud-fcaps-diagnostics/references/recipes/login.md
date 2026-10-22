# 登录分诊

| 实际现象 | 下一步 |
| --- | --- |
| 华为云 Linux ECS，SSH 建立连接阶段超时 | 读 [SSH 超时诊断](login/ssh-timeout.sop.md) |
| `Connection refused` | 核对端点、端口和监听证据；专用 recipe 待补，不套超时流程 |
| `Permission denied` 等认证失败 | 查身份、认证配置和相关日志；专用 recipe 待补 |
| 主机密钥校验失败 | 核对目标身份及密钥变化证据；专用 recipe 待补 |
| TCP 已建立后握手/认证超时，或 RDP/VNC 失败 | 保留阶段与日志，按[分诊](../triage.md)选事实；专用 recipe 待补 |

仅描述“连不上”时先区分管理登录与业务访问；已有错误和环境直接复用。当前流程清单见[索引](index.md)。
