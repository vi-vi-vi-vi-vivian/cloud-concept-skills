# Helper

只补齐当前命令缺少的标识。以下衔接已用现有 ECS 实测。

## H-port

- 输入：已知 `server_id`。
- 衔接：[ECS/ListServerInterfaces/v2](commands/configuration.md#ecs) 的 `interfaceAttachments[].port_id` → [VPC/ShowPort/v3](commands/configuration-network.md#vpc) 的 `port_id`。
- 多网卡时按目标 IP 或 MAC 选择。端口的 `port.security_groups[]` 用于后续安全组规则查询。

## H-subnet

- 输入：ECS 网卡的 `fixed_ips[].subnet_id` 和已确认的 VPC。
- 用 [VPC/ListSubnets/v2](commands/configuration-network.md#vpc) 返回的 `neutron_subnet_id` 匹配该标识。
- 将匹配项的 `id` 传给 [VPC/ShowSubnet/v2](commands/configuration-network.md#vpc)。Neutron 子网 ID 与 VPC 子网 ID 不能直接互换。

## H-volume

- 输入：已知 `server_id`。
- [ECS/ShowServer/v2](commands/configuration.md#ecs) 的 `server.os-extended-volumes:volumes_attached[].id` → [EVS/ShowVolume/v2](commands/configuration.md#evs) 的 `volume_id`。
- 先确认目标盘是系统盘还是数据盘，再解释容量或挂载结果。

## H-eip

- 输入：已确认的 `port_id`。
- 在 [EIP/ListPublicips/v2](commands/configuration-network.md#eip) 中匹配 `port_id`，使用该项 `id` 查询公网 IP 详情。
- 使用同一项的 `bandwidth_id` 查询带宽。绑定关系不表示公网服务已经可达。
