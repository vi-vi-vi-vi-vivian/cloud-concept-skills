# Helper

只补齐缺少的标识。类型用于区分资源，不是 CLI 参数。多项匹配时按目标选择；无法唯一确定时先澄清目标。

## H-port

| 输入 | 获取命令 | 选择条件 | 输出绑定 |
| --- | --- | --- | --- |
| `server_id: ECS.ServerId` | [ECS/ListServerInterfaces/v2](commands/configuration.md#ecs) | 按目标 IP 或 MAC 选择网卡 | `interfaceAttachments[].port_id` → `VPC.PortId` |
| `port_id: VPC.PortId` | [VPC/ShowPort/v3](commands/configuration-network.md#vpc) | 返回端口 ID 与请求一致 | `port.security_groups[]` → `VPC.SecurityGroupId` |

## H-subnet

| 输入 | 获取命令 | 选择条件 | 输出绑定 |
| --- | --- | --- | --- |
| 网卡 `fixed_ips[].subnet_id: Neutron.SubnetId`、目标 `VPC.VpcId` | [VPC/ListSubnets/v2](commands/configuration-network.md#vpc) | 按目标 VPC 筛选；`subnets[].neutron_subnet_id` 等于网卡子网 ID | 同项 `subnets[].id` → `VPC.SubnetId`，用于 [VPC/ShowSubnet/v2](commands/configuration-network.md#vpc) |

## H-volume

| 输入 | 获取命令 | 选择条件 | 输出绑定 |
| --- | --- | --- | --- |
| `server_id: ECS.ServerId` | [ECS/ShowServer/v2](commands/configuration.md#ecs) | 确认目标系统盘或数据盘；多盘时按目标选择 | `server["os-extended-volumes:volumes_attached"][].id` → `EVS.VolumeId`，用于 [EVS/ShowVolume/v2](commands/configuration.md#evs) |

## H-eip

| 输入 | 获取命令 | 选择条件 | 输出绑定 |
| --- | --- | --- | --- |
| `port_id: VPC.PortId` | [EIP/ListPublicips/v2](commands/configuration-network.md#eip) | `publicips[].port_id` 等于目标端口 ID | 同项 `id` → `EIP.PublicipId`；同项 `bandwidth_id` → `EIP.BandwidthId` |

公网 IP 用于 [EIP/ShowPublicip/v3](commands/configuration-network.md#eip)，带宽用于 [EIP/ShowBandwidth/v2](commands/configuration-network.md#eip)。绑定关系不证明公网服务可达。

需要确认这些衔接的实测范围时，读[验证记录](verification.md)。
