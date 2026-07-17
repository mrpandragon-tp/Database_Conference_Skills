# 工作流手册

## 目标

将“项目代码 + 实验输出”转化为
“可投稿的 SIGMOD/VLDB 论文稿件”，并保证流程可重复。

## 跨阶段验收门槛

每个阶段都使用 `.references/distilled/good_db_paper_principles.zh-CN.md`，并保持同一个链条：

`重要问题 -> 完整论文对象 -> 核心机制 -> 保证 -> 证据 -> 边界`

不能因为语言已经润色或页数已满就进入下一阶段。只有支撑下一个箭头所需的产物已经存在，才算通过。

## 阶段 1：立项与范围

- 运行 `db-paper-orchestrator`
- 明确论文目标、核心 claim 范围、交付物
- 冻结方法、实验、写作、投稿阶段里程碑

通过门槛：
- 存在清晰阶段计划
- 每阶段需要的产物明确

## 阶段 2：新颖性与定位

- 运行 `db-novelty-positioning`
- 输出 claim-prior-delta 映射
- 对 claim 分类（system/algorithm/proof/evaluation）

通过门槛：
- 每个核心 claim 都有 nearest prior 与可测差异
- 不存在无证据计划的模糊新颖性表述

## 阶段 3：方法与证明骨架

- 用 `db-writing-copilot` 搭方法节骨架
- 用 `db-method-proof-check` 做定理/假设/依赖闭环

通过门槛：
- 定理假设显式且一致
- 核心 claim 的证明义务已闭环

## 阶段 4：证据构建与审计

- 运行 `db-experiment-evidence-auditor`
- 检查 baseline 公平性、协议一致性、压力测试覆盖
- 在语言润色前先补齐 claim-evidence 缺口

通过门槛：
- 最强 baseline 配置公平
- 核心 claim 有对应量化证据

## 阶段 5：图表与读者叙事

- 运行 `db-figure-design`
- 让图表顺序与 claim 顺序、审稿阅读顺序对齐

通过门槛：
- 每个关键 claim 对应图/表锚点
- caption 与坐标设计支持决策性阅读

## 阶段 6：审稿预检与最终格式

- 运行 `db-reader-reviewer-preflight`
- 先修 major/fatal 问题
- 运行 `db-format-finish` 完成最终格式收敛

通过门槛：
- 无未解决 fatal 风险
- 可以仅根据论文回答“好 DB 论文”的十个验收问题
- 稿件通过最终投稿前检查

