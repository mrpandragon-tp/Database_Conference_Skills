# 技能目录（v0.3）

## 端到端技能映射

| Skill | 主要职责 | 常见输入 | 常见输出 |
| --- | --- | --- | --- |
| `db-paper-orchestrator` | 项目到论文阶段编排 | 项目代码、结果、目标 venue | 阶段计划、交接产物 |
| `db-novelty-positioning` | claim-prior delta 与增量风险审计 | 贡献陈述、相关工作 | 差异化表、风险标注 |
| `db-writing-copilot` | 按 claim-evidence 纪律分节写作 | 大纲、图表、结果表 | 结构化章节草稿 |
| `db-method-proof-check` | 定理/证明/假设一致性校验 | 方法节、证明附录 | 证明问题清单、闭环检查 |
| `db-experiment-evidence-auditor` | 实验证据公平性与覆盖性审计 | 实验脚本/结果 | 证据缺口报告、修复优先级 |
| `db-figure-design` | 图表叙事与可视化质量 | 数据表、作图脚本、图规格 | 图计划、图质检结论 |
| `db-format-finish` | 投稿前格式与版面收敛 | LaTeX/PDF 草稿 | 最终格式检查清单 |
| `db-reader-reviewer-preflight` | 审稿视角风险预检 | 近最终稿件 | major/fatal 问题清单 |

## 建议触发时机

- `db-paper-orchestrator`：新论文周期开始或范围大改
- `db-novelty-positioning`：问题定义后、深度写作前
- `db-writing-copilot`：章节写作开始或卡住时
- `db-method-proof-check`：定理陈述与假设成形后
- `db-experiment-evidence-auditor`：首轮完整结果出现后
- `db-figure-design`：图表定稿前
- `db-reader-reviewer-preflight`：投稿冻结前
- `db-format-finish`：最终上传前

## 推荐顺序

1. orchestrator
2. novelty positioning
3. writing copilot
4. method/proof check
5. experiment auditor
6. figure design
7. reviewer preflight
8. format finish

## 技能文件位置

所有技能定义位于：
- `.agents/skills/<skill-name>/SKILL.md`

每个技能对应参考文档位于：
- `.agents/skills/<skill-name>/references/`

