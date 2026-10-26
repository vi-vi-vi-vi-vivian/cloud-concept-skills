# 配置分诊

复用已有目标、时间窗和原始错误，按实际现象读对应 draft 正文。

| 现象 / 任务 | 下一步 |
| --- | --- |
| cloud-init/user-data 初始化未生效 | [cloud-init-failed](configuration/cloud-init-failed.sop.md) |
| 扩容后容量未更新 | [disk-expand-failed](storage/disk-expand-failed.sop.md) |
| 挂载配置与实际不符 | [mount-failed](storage/mount-failed.sop.md) |

未覆盖或描述不明确时回到[分诊](../triage.md)；全部正文见[索引](index.md)。
