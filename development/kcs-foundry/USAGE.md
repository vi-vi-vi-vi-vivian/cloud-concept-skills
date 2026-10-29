# KCS Foundry 接入程序

本层调用仓库固定快照的 OpenKB，不修改 `vendor/openkb/`。流程为：选取获准材料 → 原文快照及带行号文本 → OpenKB 编译 wiki → 显式调用 `kcs-extractor` → 检查 KCS 草稿。

## 运行边界

- 整理、预演、校验和离线测试只需要 Python 3.10+ 标准库。
- 真正编译和提炼需要安装 OpenKB 的固定依赖，并配置可以处理这些材料的模型。调用的是 Python 接口，不需要启动 Web 服务。
- 当前版本输入为 UTF-8 文本及代码文件。工单先在内部导出为 Markdown／文本／JSON／CSV 等；PDF、Word、Excel、图片等附件会列入 skipped，需另行转换或明确记录缺口。
- 材料目录应是已获准处理的选定范围。工具会保留文本原文，不负责自动识别或清除其中的敏感信息。隐藏文件、常见依赖目录不采集，符号链接拒绝跟随。
- 不执行源材料脚本。真实运行会将材料发送给所配置的模型；内部资料须使用内部获准部署。

## 1. 准备材料包

以下命令从仓库根目录执行，路径按实际环境替换。目录只需提供一次明确的输入范围；不要将整个 source 仓库默认作为一次处理任务。

```bash
python3 development/kcs-foundry/scripts/prepare_materials.py \
  --source /path/to/approved-skill \
  --kind skill \
  --source-name vendor/repository \
  --revision source-commit \
  --include SKILL.md \
  --include 'references/*.md' \
  --include 'references/utils/*.md' \
  --output /path/to/material-pack
```

`--include` 可重复，匹配相对输入根目录的路径；没有该选项时采集支持的非隐藏文本文件。默认最多 200 个文件、每个文件 1 MiB；超限时报错，先缩小范围或显式调整限额。排除和不支持的文件写入清单，不假装完整读取。工单使用 `--kind ticket --source-name approved-ticket-alias`；版本不明时省略 `--revision`。

产物：

```text
material-pack/
├── manifest.json          # 来源别名、版本、原路径、原文/导入文本哈希、遗漏项
├── sources/               # 保持原目录关系的逐字节快照
└── documents/             # 供 OpenKB 导入的带原行号 Markdown
```

包必须放在原始材料目录之外，已有包不覆盖。原文哈希与转换后文档哈希分开保存；不同目录同名文件不会互相覆盖。脚本也包装成文本供静态阅读，源内链接通过清单解析，不要求编译后的 wiki 保留原目录关系。

## 2. 无模型预演

```bash
python3 development/kcs-foundry/scripts/extract_kcs.py \
  --materials /path/to/material-pack \
  --kb /path/to/ecs-kb \
  --run-id ssh-pilot-01 \
  --scenario 'SSH 建连超时' \
  --dry-run
```

检查材料哈希、路径、任务 ID，并输出调用计划。此模式不导入 OpenKB、不写文件、不调用模型，知识库可以尚未创建。材料包必须与知识库分开，不能放进模型可写的 `output/`；原始包是独立校验依据。

## 3. 在目标环境安装并初始化 OpenKB

下面是部署操作示例，本次实现未执行安装。使用独立环境；源码快照的包版本采用明确的本地标记，避免构建工具误用外层仓库版本。OpenKB 依赖仍按其 pyproject 中的版本安装。

```bash
python3 -m venv workspaces/kcs-env
SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENKB=0.0.0+vendored \
  workspaces/kcs-env/bin/python -m pip install -e development/kcs-foundry/vendor/openkb
```

在选定的知识库目录执行该虚拟环境中的 `openkb init --model 'provider/model-id' --language zh`，模型名称换为实际部署的 LiteLLM 标识。初始化前确认终端的当前目录是知识库目录。按内部方式配置知识库 `.env`，不要在命令参数中传密钥。OpenAI 兼容网关可通过 `OPENAI_API_BASE` 指定地址，凭据使用 `LLM_API_KEY`。

模型须明确配置在此知识库的 `.openkb/config.yaml`，接入程序不会仅靠全局默认模型开始生成。凭据和其他设置按固定 OpenKB 的加载规则解析：使用知识库自己的配置可以避免误用其他任务的模型。不要将 `.env` 提交 Git。

知识库可以放在内部仓库的 `knowledge/ecs-kb/`；当前仓库的临时试点也可以放在被忽略的 `workspaces/`。原文包、wiki 和 KCS 草稿是否提交，按内部内容范围决定；接入程序不会自动提交或推送。

## 4. 执行编译与提炼

```bash
workspaces/kcs-env/bin/python development/kcs-foundry/scripts/extract_kcs.py \
  --materials /path/to/material-pack \
  --kb /path/to/ecs-kb \
  --run-id ssh-pilot-01 \
  --scenario 'SSH 建连超时'
```

这条命令会：

1. 核对材料，安装完整元技能到 `<kb>/skills/kcs-extractor/`。已有同名技能内容不同时停止，由维护者先归档／更名旧版后再更新。
2. 为本次任务建立原文及清单的可读副本；只复制清单列出的文件。
3. 用 OpenKB `add_single_file()` 导入每份带行号文档。返回 failed 时停止，不把它当成导入完成，也不开始生成。
4. 调用 `run_skill()`，告知参考文件、原文映射、来源身份、场景及输出根目录。默认保留来源平台；可用 `--target-platform` 明确目标，但缺少目标契约时仍需记录适配缺口。
5. 验证输入副本未被改写，检查生成结果；不向正式 `recipes/kcs` 自动同步。

目录：

```text
ecs-kb/
├── .openkb/kcs-foundry/<run-id>/  # 程序维护的计划、可信清单与运行状态
├── skills/kcs-extractor/         # 元技能及三份参考规则
├── wiki/                        # OpenKB 编译维护
└── output/
    ├── kcs-inputs/<run-id>/      # 模型可读原文与来源映射
    └── kcs/<run-id>/
        ├── articles/
        ├── evidence/
        ├── extraction-report.md
        └── validation.json      # 外层程序生成的校验结果
```

现有 OpenKB runner 的写权限覆盖知识库 `output/` 与 `wiki/explorations/`，不是按 run-id 隔离的文件沙盒；程序要求只写本次输出，并在生成后重新核对输入副本。需要更强任务隔离时，为任务使用独立知识库和运行账号。

已有 run-id 不覆盖，不自动重试。失败时保留现场，查看 `.openkb/kcs-foundry/<run-id>/state.json` 的 phase 与逐文档结果；修复原因后用新 run-id 重跑。OpenKB 对已导入且未变更的文档可返回 skipped。模型异常只记录异常类型，不将请求内容或凭据异常正文写入运行状态。

## 5. 独立校验与纳入知识库

```bash
python3 development/kcs-foundry/scripts/validate_kcs.py \
  --materials /path/to/material-pack \
  --output /path/to/ecs-kb/output/kcs/ssh-pilot-01
```

必须传入原始可信材料包，不能用模型可写的输入副本替代。检查四字段、编号步骤、草稿状态、文章与证据配对、来源路径／哈希／版本、claim 引用关系和输出内文件链接。非零退出表示未通过；生成器正常返回但没有文章，也判失败。

`valid: true` 只表示上述机械检查通过。`partial` 草稿会给出提醒，仍须核对诊断逻辑、来源段落是否真的支持结论、平台差异及敏感信息。运行验证固定为 not_run，不会凭生成过程升级可信状态。

第一版手动选定文章后纳入诊断技能的 `references/recipes/kcs/`，更新索引、重算移动后的相对链接；来源和验证记录放在权限合适的内部 Git 目录。自动同步、对外发布、内部工单附件转换均不在本版实现中。

## 离线测试

```bash
python3 -m unittest discover -s development/kcs-foundry/tests -v
```

测试使用临时目录和替代后端，覆盖真实文件流转、错误退出与来源篡改等边界；不需要模型或云账号。它们不证明模型提炼质量，也不代替目标部署的真实 OpenKB 集成试点。
