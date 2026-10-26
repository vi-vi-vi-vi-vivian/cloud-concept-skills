# 存储分诊

复用已有目标、时间窗和原始错误，按实际现象读对应 draft 正文。

| 现象 / 任务 | 下一步 |
| --- | --- |
| 空间或 inode 不足 | [disk-full](storage/disk-full.sop.md) |
| 扩容后容量未增加 | [disk-expand-failed](storage/disk-expand-failed.sop.md) |
| 挂载失败、错挂或只读 | [mount-failed](storage/mount-failed.sop.md) |
| 已明确可回收对象，要求释放空间 | [reclaim-disk-space](storage/reclaim-disk-space.sop.md) |

未覆盖或描述不明确时回到[分诊](../triage.md)；全部正文见[索引](index.md)。
