# 安全分诊

复用已有目标、时间窗和原始错误，按实际现象读对应 draft 正文。

| 现象 / 任务 | 下一步 |
| --- | --- |
| 云 API 鉴权/授权被拒 | [api-permission-denied](security/api-permission-denied.sop.md) |
| SSH 认证失败 | [ssh-auth-failed](login/ssh-auth-failed.sop.md) |

可疑访问或疑似入侵先按[安全事实](../commands/security/linux.md)及已有云安全事件核对目标和时间，保留证据；目前没有完整事件响应 recipe，不能据异常迹象自动清理或隔离。

未覆盖或描述不明确时回到[分诊](../triage.md)；全部正文见[索引](index.md)。
