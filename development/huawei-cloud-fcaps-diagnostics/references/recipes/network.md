# 网络分诊

复用已有目标、时间窗和原始错误，按实际现象读对应 draft 正文。

| 现象 / 任务 | 下一步 |
| --- | --- |
| ECS 出网/业务目标不可达 | [outbound-unreachable](network/outbound-unreachable.sop.md) |
| DNS 超时或回答异常 | [dns-resolution-failed](network/dns-resolution-failed.sop.md) |
| 丢包、间歇超时或重传 | [packet-loss](network/packet-loss.sop.md) |

未覆盖或描述不明确时回到[分诊](../triage.md)；全部正文见[索引](index.md)。
