# 技能构建日志（v0.3）

## 为什么有这个版本

用户要求：
- 面向 SIGMOD/VLDB 的项目无关流程技能
- 逐篇全文语义解析
- 技能包可放到 `.codex/skills` 风格目录

## 包含技能

- db-paper-orchestrator
- db-novelty-positioning
- db-writing-copilot
- db-method-proof-check
- db-experiment-evidence-auditor
- db-figure-design
- db-format-finish
- db-reader-reviewer-preflight

## 知识构建流水线

1. `scripts/refresh_paper_index.sh` -> 论文元数据索引
2. `scripts/distill_topconf_patterns.py` -> 元数据层模式矩阵
3. `scripts/distill_fulltext_semantics.py` -> 全文语义 profile 与全文蒸馏模式

## 本次全文覆盖

- 目标论文：81
- 全文 profile：80
- 缺失：1（缺少可用全文缓存）

## 新增全文产物

- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/paper-corpus/fulltext_section_signal_matrix.md`
- `.references/paper-corpus/fulltext_writing_signal_matrix.md`
- `.references/paper-corpus/fulltext_proof_signal_matrix.md`
- `.references/paper-corpus/fulltext_experiment_signal_matrix.md`
- `.references/paper-corpus/fulltext_reviewer_risk_matrix.md`
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/distilled/novelty_patterns_fulltext.md`
- `.references/distilled/proof_patterns_fulltext.md`
- `.references/distilled/experiment_patterns_fulltext.md`
- `.references/distilled/reader_reviewer_patterns_fulltext.md`

## 验证说明

- 全量重建流水线已执行成功。
- skill frontmatter（`name` + `description`）已校验。
- 可选 `quick_validate.py` 仍依赖本地 Python `yaml` 模块。

