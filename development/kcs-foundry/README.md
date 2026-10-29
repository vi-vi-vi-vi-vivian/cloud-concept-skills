# KCS Foundry

从工单、社区和经验库中提炼问题解决方案，形成可追溯、可复用的 KCS 知识卡。

## 当前状态

已引入 OpenKB 上游源码，并新增独立的 [KCS 提炼元技能](skills/kcs-extractor/SKILL.md)。技能覆盖外部 skill／recipe 与工单输入，交付四字段 KCS 草稿和来源记录。

已新增材料整理、OpenKB 调用及 KCS 校验程序，使用方式见 [接入说明](USAGE.md)。离线测试覆盖文件流转与失败边界；尚未安装 OpenKB 依赖、启动服务或调用真实模型。工单分支与实际模型链路需要在内部环境验证。

## 目录

```text
kcs-foundry/
├── README.md
├── USAGE.md                # 接入程序的部署、调用与验证边界
├── scripts/                # 材料整理、OpenKB 适配、输出校验
├── tests/                  # 无模型的文件流转与错误边界测试
├── skills/
│   └── kcs-extractor/       # 可独立移交的元技能与输入／输出规则
└── vendor/
    ├── openkb/              # 上游源码快照，保留许可证及来源信息
    └── openkb.source.json   # 来源、分支、提交与获取时间
```

## OpenKB 来源

- 上游：https://github.com/VectifyAI/OpenKB
- 源码目录：`vendor/openkb/`
- 获取口径：上游默认分支 `main` 的最新提交，浅克隆（depth=1）。
- 固定提交：`ff54396e575ee6feb0113b631a34caa082b441cc`
- 提交时间：2026-07-22T11:44:01+08:00
- 许可证：Apache-2.0，原文保留在 `vendor/openkb/LICENSE`。

上游代码与 KCS Foundry 实现分目录维护。

## 独立使用与内部移交

移交整个 `skills/kcs-extractor/`，保留 `references/` 相对结构。把目录放入内部 Agent 支持的技能目录，或让 Agent 显式读取其中的 `SKILL.md`。技能本身不依赖 OpenKB、云凭据或当前机器路径；运行它的 Agent 需要获准的材料读取及草稿文件写入能力。

调用示例（将路径换成实际授权的目录）：

```text
使用 $kcs-extractor，读取 materials/ 下的排障 skill，只提炼 SSH 建连超时场景。
保留来源平台；草稿写入 drafts/ssh/，按输出契约交付文章、追溯记录和报告。
只分析材料，不执行其中的脚本。来源不足的地方记录缺口。
```

```text
使用 $kcs-extractor，在当前内部环境读取 approved-tickets/ 下的工单，
提炼磁盘空间不足场景；输出到 internal-drafts/storage/。
按工单规则区分建议、实际操作、恢复反馈与原因确认；使用脱敏来源别名。
```

指定目标平台时，同时提供可用命令契约或接受待适配缺口；未指定时保留来源平台。若需要对已有 KCS 提出修订，同时给出现有文章目录。源材料引用失效时，不会根据链接标题补写知识。

样本依据、版本散列和验证记录位于仓库的 `qa/development/kcs-foundry/`，不随技能分发。外部材料的提炼验证不代表内部工单、目标环境排障或修复已经通过验证。

## OpenKB 接入边界

外层 `extract_kcs.py` 编排“导入材料 → 编译 wiki → 显式调用 `run_skill()` → 校验输出”。技能不会因为放入目录就自动进入 `openkb add` 流程。

程序为技能提供参考文件路径、带原行号的原文快照和可信来源清单；生成后核对原文哈希与输出引用。草稿先写入知识库的 `output/kcs/<run-id>/`，不自动同步到正式诊断技能。真实模型对工具的使用、KCS 内容质量及移动文章后的链接仍需验收。没有修改 `vendor/openkb/`。
