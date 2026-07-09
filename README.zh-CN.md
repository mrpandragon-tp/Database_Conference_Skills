# Database Conference Skills（SIGMOD/VLDB）

语言：
- 中文（本文件）
- English: [README.md](./README.md)

这是一个面向数据库顶会写作的、项目无关的技能包，目标是把
“项目代码 + 实验结果”稳定转化为“可投稿的 SIGMOD/VLDB 论文稿件”。

仓库包含三类核心资产：
- 可执行的技能系统（`.agents/skills`）
- 论文蒸馏后的知识库（`.references`）
- 可重复运行的知识重建脚本（`scripts/`）

## 为什么做这个仓库

目标不是给单个项目做一次性润色，而是建立可复用的写作流水线。

当前蒸馏深度：
- 目标论文：81 篇
- 完成全文语义 profile：80 篇
- 已覆盖 novelty / evidence / proof 风险信号

详见：[distillation_depth.md](./distillation_depth.md)

## 技能包（v0.3）

共 8 个端到端技能：
1. `db-paper-orchestrator`
2. `db-novelty-positioning`
3. `db-writing-copilot`
4. `db-method-proof-check`
5. `db-experiment-evidence-auditor`
6. `db-figure-design`
7. `db-format-finish`
8. `db-reader-reviewer-preflight`

技能目录： [docs/skill-catalog.md](./docs/skill-catalog.md)

## 使用示例（重点）

如果你喜欢 `awesome-ai-research-writing` 这类“按场景给具体用法”的风格，
建议直接看：

- 场景化示例 + 可复用调用模式：
  [docs/usage-examples.md](./docs/usage-examples.md)
- 端到端流程手册：
  [docs/workflow-playbook.md](./docs/workflow-playbook.md)

覆盖的典型场景：
- 从代码/实验结果出发，搭建完整写作流程
- novelty 风险排查与 claim-prior-delta 重写
- 证明闭环与实验公平性审计
- 图表与 claim 的绑定设计
- 投稿前审稿人视角预检 + 格式终检

## 与其他 Skills 的融合

本仓库除了本体 8 个技能，也整理了与外部技能的融合方式（如已安装）：
- `research-paper-writing`, `ml-paper-writing`, `humanizer`
- `scientific-figure-making`, `canvas-design`, `pdf`

融合策略与风险控制：
- [docs/usage-examples.md](./docs/usage-examples.md)
- 源数据映射：
  [./.references/distilled/existing_skill_integration.md](./.references/distilled/existing_skill_integration.md)

## 如何新增论文并蒸馏新知识

你可以持续把新论文注入知识库。

快速路径：
1. 把新论文加入 Zotero 的目标集合（默认 `ANN` 与 `SIGMOD/VLDB`）
2. 在仓库根目录执行：

```bash
./rebuild_knowledge.sh
```

若你要自定义集合名或 Zotero 路径，需要改：
- `scripts/refresh_paper_index.sh`（`DB_URI` + 集合名）
- `scripts/distill_fulltext_semantics.py`（`DB_URI` + `ZOTERO_STORAGE`）

详细步骤与验证标准见：
- [docs/usage-examples.md](./docs/usage-examples.md)

## 快速开始

### 1）直接在本仓库使用

如果你的 agent 运行时可读取本地路径，指向：
- skills: `.agents/skills/`
- distilled references: `.references/distilled/`
- corpus matrices: `.references/paper-corpus/`

### 2）安装到本地 Codex skills 目录（可选）

```bash
mkdir -p ~/.codex/skills/db-topconf-paper-pack-v03
rsync -av --delete \
  /path/to/db_topconf_skill_pack_v03/ \
  ~/.codex/skills/db-topconf-paper-pack-v03/
```

## 推荐执行顺序

1. 立项与阶段规划 -> `db-paper-orchestrator`
2. 新颖性定位 -> `db-novelty-positioning`
3. 分节写作 -> `db-writing-copilot`
4. 方法与证明校验 -> `db-method-proof-check`
5. 实验证据审计 -> `db-experiment-evidence-auditor`
6. 图表设计与质检 -> `db-figure-design`
7. 审稿视角预检 -> `db-reader-reviewer-preflight`
8. 最终格式收敛 -> `db-format-finish`

## 仓库结构

```text
.
├── .agents/
│   ├── skills/            # 可执行技能（SKILL.md + references）
│   └── skill_tests/       # 每个技能对应的回归测试提示
├── .references/
│   ├── paper-corpus/      # 蒸馏矩阵/profile/报告
│   └── distilled/         # 可复用的高层模式总结
├── scripts/               # 重建与蒸馏脚本
├── docs/                  # 面向使用者的文档
├── rebuild_knowledge.sh   # 一键重建知识
└── skill_*.md             # 范围、日志、缺口说明
```

进一步说明： [docs/repo-organization.md](./docs/repo-organization.md)

## 关键产物

- 全文 profile：
  `.references/paper-corpus/fulltext_semantic_profile.csv`
- 全文蒸馏报告：
  `.references/paper-corpus/fulltext_distillation_report.md`
- 新颖性模式：
  `.references/distilled/novelty_patterns_fulltext.md`
- 证明模式：
  `.references/distilled/proof_patterns_fulltext.md`
- 实验模式：
  `.references/distilled/experiment_patterns_fulltext.md`

## 文档导航

- 技能能力总览： [docs/skill-catalog.md](./docs/skill-catalog.md)
- 流水线执行手册： [docs/workflow-playbook.md](./docs/workflow-playbook.md)
- 使用示例/融合/蒸馏操作： [docs/usage-examples.md](./docs/usage-examples.md)
- 贡献指南： [CONTRIBUTING.md](./CONTRIBUTING.md)

## 版本说明

- 当前版本：v0.3
- `.agents/skills/README.md` 已同步到 v0.3
- 后续缺口见： [skill_gap_report.md](./skill_gap_report.md)

