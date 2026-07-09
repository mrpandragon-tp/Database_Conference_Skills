# 蒸馏深度说明（v0.3）

## 当前深度

当前版本基于 Zotero 的全文缓存文件（`.zotero-ft-cache`）对目标集合中的论文进行逐篇全文语义解析。

本次覆盖：
- 目标论文总数：81
- 已构建全文语义 profile：80
- 未覆盖：1（所选附件缺少可用全文缓存）

## 全文蒸馏提取了什么

对每篇可解析论文，流水线提取：
- 章节结构信号（introduction/method/experiments/conclusion）
- 写作链路信号（problem -> gap -> proposal -> quantified evidence）
- 证明信号（theorem/lemma/proof/assumption/complexity）
- 实验信号（quality/latency/throughput/build/update/memory/ablation/fairness）
- 性能主张信号（speedup/percent/tradeoff）
- 审稿风险估计（novelty/evidence/proof）

输出位置：
- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/paper-corpus/fulltext_*_matrix.md`
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/distilled/*_fulltext.md`

## 当前限制

- 这是语义层信号抽取，不是对每条定理证明进行完整逻辑重建。
- 公式级等价检查与完整证明依赖图仍需更深层 theorem parser。
- PDF OCR 质量受 Zotero 全文缓存质量影响。

## 下一步可深化方向

1. 增加基于章节片段的定理依赖图抽取。
2. 增加每篇论文的 claim-to-figure/theorem 指针抽取。
3. 增加录用论文的章节修辞模板挖掘。

