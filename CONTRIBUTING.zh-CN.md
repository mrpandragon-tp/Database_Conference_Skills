# 贡献指南

感谢你参与 `Database Conference Skills (SIGMOD/VLDB)`。

本仓库定位为“可复用、项目无关”的数据库论文技能系统。请优先保证可重复性与审稿友好性。

## 贡献范围

欢迎的贡献：
- 新增可复用的 SIGMOD/VLDB 流程技能
- 优化现有技能的 workflow / output contract / rules
- 增强 novelty/proof/experiment 的参考规则
- 改进蒸馏脚本与文档可用性

建议避免：
- 将项目专属约束硬编码进通用技能
- 牺牲可复现性的 venue 无关“技巧”

## 仓库地图

- 技能：`.agents/skills/`
- 技能测试：`.agents/skill_tests/`
- 蒸馏知识：`.references/`
- 脚本：`scripts/`
- 用户文档：`README.md`、`README.zh-CN.md` 与 `docs/`

## 新增一个 Skill

### 1）创建技能目录

创建：
- `.agents/skills/<skill-name>/SKILL.md`
- `.agents/skills/<skill-name>/agents/openai.yaml`
- `.agents/skills/<skill-name>/references/*.md`

命名约定：
- `<skill-name>` 使用 kebab-case
- `SKILL.md` 中 `name` 与目录名一致

### 2）编写 `SKILL.md`

frontmatter 必填：
- `name`
- `description`

主体建议包含：
- workflow
- output contract
- rules

### 3）新增回归测试提示

创建：
- `.agents/skill_tests/<skill-name>-test.md`

建议格式：
- Input
- Expected
- Failure mode

### 4）同步文档

至少更新：
- `docs/skill-catalog.md` 与 `docs/skill-catalog.zh-CN.md`
- `docs/workflow-playbook.md` 与 `docs/workflow-playbook.zh-CN.md`（若流程顺序变化）
- `.agents/skills/README.md` 与 `.agents/skills/README.zh-CN.md`（若技能清单变化）

## 修改现有技能

修改行为规则时：
- 尽量保持 output contract 向后兼容
- 在 references 中解释决策规则变化
- 同步更新对应 `.agents/skill_tests/` 测试提示

## 回归检查

在仓库根目录执行。

### A）结构完整性

```bash
find .agents/skills -mindepth 1 -maxdepth 1 -type d | while read -r d; do
  test -f "$d/SKILL.md" || echo "Missing SKILL.md: $d"
  test -f "$d/agents/openai.yaml" || echo "Missing openai.yaml: $d"
done
```

### B）frontmatter 校验

```bash
rg -n "^name: " .agents/skills/*/SKILL.md
rg -n "^description: " .agents/skills/*/SKILL.md
```

### C）测试覆盖校验

```bash
for s in .agents/skills/*; do
  n="$(basename "$s")"
  test -f ".agents/skill_tests/${n}-test.md" || echo "Missing test: $n"
done
```

### D）蒸馏流水线校验（脚本/数据改动后）

```bash
./rebuild_knowledge.sh
```

若环境不便全量执行，可分步运行：

```bash
./scripts/refresh_paper_index.sh
./scripts/distill_topconf_patterns.py
./scripts/distill_fulltext_semantics.py
```

## 提交信息建议

建议使用“意图优先、简洁”的提交说明，例如：
- `Add db-related-work-auditor skill and tests`
- `Refine novelty rubric and preflight checks`
- `Improve README onboarding and docs navigation`

## PR 检查清单

- 新增/修改技能都有对应测试提示
- 文档已同步更新（中英双语）
- 回归检查已运行（或注明限制）
- 未把项目专属约束泄漏到通用技能

