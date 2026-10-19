# 工程结构

一个技能入口。五类内容按职责组织，不要求分别建技能。

```text
huaweicloud-ecs-troubleshooting/
├── SKILL.md                         # Persona：目标、路由、输出
├── README.md                        # 开发状态
├── STRUCTURE.md                     # 工程约定
└── references/
    ├── shared.md                    # Shared：配置、认证与共用约束
    ├── services.md                  # Service：命令发现与共享查询
    ├── helpers.md                   # Helper：已验证的资源标识衔接
    ├── triage.md                    # 现象入口
    ├── report.md                    # 结果字段
    ├── commands/                    # Service 契约，按 FCAPS 分册
    │   ├── index.md
    │   ├── fault.md
    │   ├── configuration.md
    │   ├── configuration-network.md
    │   ├── accounting.md
    │   ├── performance.md
    │   ├── security.md
    │   ├── security-host.md
    │   └── extensions.md
    └── recipes/                     # 仅规划，每项 1～2 句指导
        ├── boot.md
        ├── login.md
        ├── network.md
        ├── storage.md
        ├── performance.md
        ├── crash.md
        ├── configuration.md
        ├── security.md
        └── recovery.md
```

## 归属

- Shared 保留共用规则。服务命令不复制这些规则。
- Service 保留命令目的、行为、条件依赖和验证状态。FCAPS 是跨服务分类；每条命令只在一个分册定义。
- Helper 保留跨命令的字段衔接。已知标识直接复用。
- Recipe 当前只保留目标和规划指导。后续实现时引用现有命令契约。
- Persona 放在 SKILL.md，选择证据路径并规定输出。

## 渐进加载

入口只载入目标和路由。未知现象时读 triage；已知命令时直接读对应契约。首次调用或访问失败时读 Shared；缺少资源标识时读对应 Helper。

FCAPS 索引只用于选册。每册按服务设置目录，可搜索完整命令 ID，再读取对应服务段。详细参数使用当前 hcloud help。只在参数易错或命令需衔接时保留字段。

配置和安全内容较多，分别拆出网络配置、主机安全。共享查询集中在 services.md。其余内容保持合并，减少小文件。

## 开发与验收

命令事实先执行后编写。记录 CLI 版本、时间、范围和逐条验证状态。真实调用、空结果、帮助通过和受阻分别计数。

QA 位于仓库 `qa/development/huaweicloud-ecs-troubleshooting/`。原始输出和验收报告位于忽略的 `.workspaces/`。运行载荷不包含账号标识、密钥、测试脚本或原始响应。

本次不实现 Recipe、不注册技能、不发布版本。晋升正式技能时再按仓库规则同步本地化与发布目录。
