# 登录分诊

复用已有目标、时间窗和原始错误，按实际现象读对应 draft 正文。

| 现象 / 任务 | 下一步 |
| --- | --- |
| TCP 建连超时 | [ssh-timeout](login/ssh-timeout.sop.md) |
| SSH 认证被拒 | [ssh-auth-failed](login/ssh-auth-failed.sop.md) |
| Windows RDP 连接/认证/会话失败 | [rdp-unavailable](login/rdp-unavailable.sop.md) |

拒绝连接先核对实际端点、监听及响应来源；主机密钥变化先核对目标身份，握手阶段超时保留具体阶段。VNC 等未覆盖场景走通用分诊，不能套 SSH 建连超时。

未覆盖或描述不明确时回到[分诊](../triage.md)；全部正文见[索引](index.md)。
