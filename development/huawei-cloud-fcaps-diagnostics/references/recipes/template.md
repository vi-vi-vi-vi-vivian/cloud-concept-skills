# Recipe 编写模板

维护者复制下列结构到对应场景目录，填写后删除占位说明。文件使用 .sop.md；正文含 Overview 和 Steps 两个顶层章节。完整样例见 [SSH 超时诊断](login/ssh-timeout.sop.md)，收录与维护规则见 [STRUCTURE](STRUCTURE.md)。本文件不是可执行流程。

```markdown
---
id: 唯一且稳定的场景标识
intent: diagnose
environment: 适用资源与系统
status: draft
---

# 具体症状或任务名称

## Overview

### Issue
用户描述、同义表述和关键报错；匹配条件及排除条件，必要时链接其他入口。

### Environment
适用环境、所需输入和通道；复用已有信息，缺少且影响当前检查时再补齐。

### Resolution
本流程的交付目标；步骤见下文，结果按既有 report.md 输出。

### Cause
可选：已有依据的原因及确认条件；未知时保持未知，候选原因在 Steps 验证。

### Constraints
跨步骤的必要约束；引用共同约束，具体命令链接到既有契约。

### Stop conditions
何时完成、转诊或因依赖受阻而停止；记录已有证据和缺口后输出。

## Steps

### 1. 明确一个检查目标
读取哪些事实，引用哪些命令契约，依据结果选择什么分支。

**Constraints:** 必要输入、执行边界、证据不能外推的范围。

**Stop conditions:** 什么证据表明本步完成；何时继续、跳转或结束。
```

MUST 表示必要约束，SHOULD 表示推荐做法，MAY 表示可选。约束写在相关步骤附近，既说明动作，也说明结果支持的边界；避免用“检查是否正常”代替可判断的完成条件。
