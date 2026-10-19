# 开发稿验收

在仓库根目录执行：

```bash
rtk proxy bash qa/development/huaweicloud-ecs-troubleshooting/validate.sh --evidence .workspaces/hcloud-fcaps-validation-20261019
```

脚本检查命令覆盖、唯一归属、帮助输出哈希、逐条验证标记、依赖链接、引用可达性、Recipe 规划范围和写入后依赖链记录。它不调用云 API。

证据目录需要 `manifest.json`、`help-results.jsonl`、`live-results.jsonl`、`cli-results.json`、`post-write-checks.json`，以及各记录引用的帮助文本。重复查询以最后一条记录为准。API 记录保存响应摘要和断言，不保存密钥或完整业务响应。

校验还读取本机 hcloud 的服务目录，核对操作与版本。缺少本次证据或本机元数据时，需先收集对应事实，不能以空样本通过验收。

输出 `acceptance.json` 和 `acceptance.md` 到证据目录。PASS 表示列出的验收检查通过；具体 API 仍按成功、空结果、受阻分别报告。帮助通过不证明业务调用成功。
