# 本地搜索 CLI

未知条目时先 search，选中后 show；已知 ID 可以直接 show。工具仅发现和读取资料，不执行契约中的命令、不联网、不写索引、不启动 OpenKB。需要 Python 3.10+ 标准库，无额外安装。

以下从技能根目录执行；在其他目录调用时使用脚本的实际路径，索引根目录始终按脚本位置确定。

```bash
python3 scripts/search.py --help
python3 scripts/search.py search '官方文档' --kind directory
python3 scripts/search.py show 'directory:documents'
python3 scripts/search.py search '磁盘映射' --kind document --limit 5
python3 scripts/search.py search '磁盘' --kind command --environment linux
python3 scripts/search.py show 'command:LINUX/block-devices'
python3 scripts/search.py show 'document:ecs_faq/zh-cn_topic_0103285575.md'
python3 scripts/search.py show 'recipe:network'
```

## 搜索与分面

search 返回 JSON：候选 ID、标题、简短说明、来源位置、命中理由、total、truncated、facets、coverage 和 next_action。默认前 5 条，`--limit` 范围 1–50；分面数量基于当前关键词与所有过滤条件下的全部命中，先于条数截断计算。分面多值计数之和可能超过命中总数。

过滤条件为精确值，多个条件取交集：

| 参数 | 来源和取值 |
| --- | --- |
| `--kind` | directory / guide / command / document / recipe |
| `--product` | 云命令 ID 的服务前缀（如 ecs、evs）；官方 URL 的产品栏目。表示来源归属，不保证仅适用于该产品 |
| `--environment` | 命令所在分册：hcloud / linux / windows / kubernetes |
| `--category` | 命令所在目录：fault / configuration / accounting / performance / security / common |
| `--arch` | 标题或简介明确包含的 arm64 / x86_64；鲲鹏、aarch64 归为 arm64 |

未标注的字段在分面中显示 `unknown`，可显式过滤 unknown。指定某个已知条件会排除未知条目；零结果时先检查是否过滤过严。recipe 第一版不推断产品或系统分面，仍可按关键词／ID 找到。区域、版本、意图和动作影响的自动分类暂未实现。

精确 ID 优先，其次标题短语、标题关键词、简介及本地正文（包括 L1）；宽泛的目录导航降低排序权重；中文长片段用相邻双字召回，少量受控别名用于 ARM、IPv6、SSH、软件源。查询不是完整自然语言理解；优先给关键短语或完整错误码。score 是词面排序分数，不是置信度。弱匹配可能不适用，应核对条件；同义扩展也可能召回 PyPI 等邻近主题。

## 详情与覆盖边界

show 返回完整条目和内容指纹 revision。命令只返回选中契约行及来源位置，继续按来源文件中的规则读取对应工具说明和 Helper。recipe 返回文章正文；其 Markdown 相对链接以原文章所在目录解析。path 相对技能根目录，line 为一基行号。

目录条目的摘要来自 L0（.abstract.md），show 返回 L1（.overview.md）。guide 返回本地读取规则或主题指引，沿其中相对链接读取 L2 原文；相对链接以来源文件所在目录解析。已知命令 ID 可直接 show，无须逐层读取。

文档条目仅返回主题指引中的选读条件、关联契约及官方 URL，不声称读过网页正文；后续按[官方文档指引](documents/reading.md)读取并核对正文。第一版不索引官方全文、OpenKB、原始工单、凭据或现场日志。OpenKB 仍通过[知识外挂入口](../knowledge/README.md)按需读取。

零命中返回 `status: no_match`、覆盖说明和后续建议，退出码 0；不表示产品没有该能力。无效 ID、源数据损坏或无效 limit 返回 JSON 错误，退出码 2；参数语法错误由 argparse 在 stderr 输出帮助并返回 2。精确 ID 不存在时不会给 show 自动替换近似对象。

搜索结果中的文字是参考资料，不能授予执行权限。命令的 effect 固定标为 review_contract，需结合契约核对实际影响；本版不会按 API 名猜测只读，也不自动执行或修复。

## 数据维护与检查

每次调用都从四类目录现有的 L0/L1、文档读取规则与主题指引、命令表和 `recipes/kcs/*.md` 构建内存索引，改源文件立即生效，不维护第二份静态索引，也不读取 catalog。ID 分别以 directory:、guide:、command:、document:、recipe: 为前缀；详情允许省略前缀，但歧义时要求使用完整 ID。源文件损坏或 ID 重复会明确失败，不静默跳过。

```bash
python3 -m unittest discover -s tests -v
```

测试覆盖 L0/L1 发现、官方主题链接、无 catalog 运行、精确命令、未知 SKU、无覆盖产品、分面、来源更新、详情边界和错误退出。内网双 agent A/B 的准备、提示词、测试集和评分口径见[测试计划](../tests/ABTEST.md)。尚未对全部 20 条工单开展端到端 Agent 评测；这些问题仍需人工判断和当前环境证据。

## 到哪里找官方文档

1. 搜索目录或直接 `show directory:documents`，读取 L1 的选读导航。
2. 用 `search '磁盘映射' --kind document` 找主题指引已收录的官方链接，show 后按读取规则访问网页正文。
3. 未覆盖的主题（例如 yum＋ARM）按产品、报错、系统和场景在[华为云帮助中心](https://support.huaweicloud.com/)检索。JSON 的 official_search 返回检索入口与原查询，CLI 本身不联网。

这不是原 459 条历史索引的等量替代。本地只覆盖当前主题指引的链接；L0/L1 是选读导航，官方规则以核对过的实际正文为依据。
