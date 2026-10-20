# 契约验收标准

以下标准适用于四列契约修订。帮助核验、历史实测和当前修订的真实复核分别记录。

| 验收项 | 通过标准 |
| --- | --- |
| 覆盖与唯一性 | 既定 33 个服务、1,282 个命令版本全部保留；每条仅有一个契约定义 |
| 表述 | 固定为命令、作用、输入与来源、约束四列；契约不混入验证状态与历史错误 |
| 验证记录 | 逐条包含帮助状态、业务调用状态、日期和范围；与实际记录一致；未调用不得标成功 |
| 标识与依赖 | 引用存在且指向唯一契约；Helper 明确类型、获取命令、选择条件和输出绑定；时间粒度枚举不得当资源 ID |
| 执行影响 | 检测、安装、采集、同步、登录地址生成和消息发送等已知影响完整保留；不能由 GET/POST 推断只读 |
| 易错约束 | 子网 ID、配额参数大小写、COC 分页、时间单位及参数触发同步等已知差异保留 |
| 渐进加载 | 所有参考可从入口到达；已知命令搜索命中行；Helper 和验证记录按需读取 |
| 实际复核 | 当前契约修订对应的 ECS→端口/子网/安全组、ECS→云盘、端口→公网 IP→带宽检查 10/10 通过 |
| 防漂移检查 | 9 类错误注入全部被拒绝；真实复核记录的文档摘要与当前修订一致 |
| 范围与隐私 | 9 个 Recipe 仍仅规划；运行文档无真实资源 UUID 或凭据；原始响应留在忽略的工作区 |

## 执行

更新独立验证表时，显式运行写入模式：

```bash
rtk proxy python3 qa/development/huaweicloud-ecs-troubleshooting/validate.py --evidence .workspaces/hcloud-fcaps-validation-20261019 --recheck .workspaces/hcloud-contract-refinement-20261020/post-write-checks.json --write-verification
```

执行验收和错误注入检查：

```bash
rtk proxy bash qa/development/huaweicloud-ecs-troubleshooting/validate.sh --evidence .workspaces/hcloud-fcaps-validation-20261019 --recheck .workspaces/hcloud-contract-refinement-20261020/post-write-checks.json --report-dir .workspaces/hcloud-contract-refinement-20261020
rtk proxy python3 qa/development/huaweicloud-ecs-troubleshooting/test_validation.py --evidence .workspaces/hcloud-fcaps-validation-20261019 --recheck .workspaces/hcloud-contract-refinement-20261020/post-write-checks.json
```

这些脚本不调用云 API。证据目录需包含清单、实际帮助输出及其哈希、CLI 元工具记录和业务调用摘要。复核文件需包含执行完成标记、10 项断言、实际调用摘要与 `contract_digest()` 生成的文档摘要。缺证据、缺元数据或修订不一致时验收失败。

输出 acceptance.json 和 acceptance.md 到报告目录。PASS 只表示上述检查通过；不代表全部 1,282 个业务接口均已实测，也不是运行时命令拦截器。原始证据不提交仓库。
