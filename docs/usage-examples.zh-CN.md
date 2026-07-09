# 使用示例与技能融合

本页给出 `db_topconf_skill_pack_v03` 的场景化用法与可复用模板。

## 1）能力速查表

| Skill | 触发时机 | 你可以这样提需求 | 预期输出 |
| --- | --- | --- | --- |
| `db-paper-orchestrator` | 项目启动/范围重置 | “基于代码、日志和图表规划完整 SIGMOD/VLDB 流程。” | 阶段计划 + 产物清单 + 风险台账 |
| `db-novelty-positioning` | 深度写作前 | “把我的 claims 映射到最近工作并标出增量风险。” | claim-prior-delta 表 + 证据需求 |
| `db-writing-copilot` | 章节草拟 | “起草 Introduction + Method，并给 claim-evidence 指针。” | 章节草稿 + claim-evidence 映射 |
| `db-method-proof-check` | 证明收敛 | “检查定理假设与依赖闭环。” | 假设缺口 + 证明改写项 |
| `db-experiment-evidence-auditor` | 实验设计/审计 | “检查 baseline 公平性与缺失压力测试。” | 公平性发现 + 修复优先级 |
| `db-figure-design` | 图表规划/QA | “按核心 claim 设计图并面向审稿问题。” | 图计划 + caption 草案 + 视觉 QA |
| `db-reader-reviewer-preflight` | 投稿前 | “用严格 SIGMOD/VLDB 审稿视角预检。” | fatal/major 问题 + 行动计划 |
| `db-format-finish` | 最终阶段 | “做最终 LaTeX/PDF 格式检查。” | 阻断格式问题 + 最终清单 |

## 2）端到端配方

### 场景 A：从代码与原始结果到完整写作流程

1. 运行 `db-paper-orchestrator`，明确阶段与产物。
2. 运行 `db-novelty-positioning`，锁定核心差异。
3. 运行 `db-writing-copilot`，起草 Abstract/Intro/Method/Experiments。
4. 运行 `db-method-proof-check`，收敛证明质量。
5. 运行 `db-experiment-evidence-auditor`，补齐公平性与覆盖性。
6. 运行 `db-figure-design`，让图证据与 claim 对齐。
7. 运行 `db-reader-reviewer-preflight`，做拒稿风险排查。
8. 运行 `db-format-finish`，完成投稿前收尾。

### 场景 B：审稿意见指出“新颖性偏弱”

1. 重跑 `db-novelty-positioning`，重建 claim-prior 映射。
2. 重跑 `db-experiment-evidence-auditor`，补齐决定性证据。
3. 重跑 `db-writing-copilot`，把叙述收敛到可测差异。
4. 重跑 `db-reader-reviewer-preflight`，确认风险等级下降。

### 场景 C：后期暴露证明问题

1. 先用 `db-method-proof-check` 关闭假设缺口。
2. 用 `db-experiment-evidence-auditor` 增补经验性交叉验证。
3. 用 `db-writing-copilot` 回写受影响段落。

## 3）与外部技能融合

本技能包支持与通用写作/制图技能融合（如已安装）：

| 外部技能 | 融合方式 | 价值 |
| --- | --- | --- |
| `research-paper-writing` | 放在 `db-novelty-positioning` 之后、定稿写作之前 | 提升段落层科学论证流 |
| `ml-paper-writing` | 仅用于 DB 论文中学习相关技术表述 | 提升 ML-heavy 段落表达，但不破坏 DB 叙事 |
| `humanizer` | 只在技术风险关闭后使用 | 优化语言自然度，不改技术语义 |
| `scientific-figure-making` | 与 `db-figure-design` 搭配 | 将图计划转成高质量图表 |
| `canvas-design` | 用于系统架构图优化 | 提升复杂架构图可读性 |
| `pdf` | 与 `db-format-finish` 搭配 | 做最终版面与渲染质量检查 |

护栏：
- 以 DB venue 评审偏好为最高优先级
- 不让“风格类技能”覆盖“证据/证明正确性”

## 4）新增论文并蒸馏新知识

该技能包支持从本地 Zotero 持续扩库。

### 4.1 只加论文（不改代码）

1. 把论文加入脚本使用的集合：
   - `ANN`
   - `SIGMOD/VLDB`
2. 确保 Zotero 已生成 PDF 全文缓存。
3. 执行：

```bash
./rebuild_knowledge.sh
```

### 4.2 自定义集合或 Zotero 路径

修改：
- `scripts/refresh_paper_index.sh`
  - SQL 集合名（默认 `('ANN', 'SIGMOD/VLDB')`）
  - `DB_URI`
- `scripts/distill_fulltext_semantics.py`
  - `DB_URI`
  - `ZOTERO_STORAGE`

然后重跑：

```bash
./rebuild_knowledge.sh
```

### 4.3 蒸馏质量验证

重点检查：
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/distilled/*_fulltext.md`

合理性标准：
- profile 行数应与目标论文数大致匹配
- novelty/proof/experiment 矩阵应随新论文刷新

## 5）更新后的回归检查

执行：

```bash
find .agents/skills -mindepth 1 -maxdepth 1 -type d | while read -r d; do
  test -f "$d/SKILL.md" || echo "Missing SKILL.md: $d"
  test -f "$d/agents/openai.yaml" || echo "Missing openai.yaml: $d"
done

for s in .agents/skills/*; do
  n="$(basename "$s")"
  test -f ".agents/skill_tests/${n}-test.md" || echo "Missing test: $n"
done
```

若改了脚本或数据规则，再跑：

```bash
./rebuild_knowledge.sh
```

