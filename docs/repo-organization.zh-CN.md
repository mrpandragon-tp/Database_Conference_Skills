# 仓库组织说明

## 设计原则

1. 运行安全优先：
   技能运行文件统一放在 `.agents/skills`。
2. 知识与运行分离：
   蒸馏产物集中在 `.references`。
3. 可重建性：
   蒸馏脚本统一放在 `scripts/`。
4. 读者友好：
   根 `README.md` 与 `docs/` 负责快速上手。

## 为什么使用隐藏前缀（`.agents`、`.references`）

该布局是有意设计：
- 将运行时文件与大体量参考材料分层
- 降低核心 skill 内部文件的误改风险
- 贴合 agent 工作区约定

## 建议的后续重构

1. 增加稳定 manifest（`pack_manifest.yaml`）：
   - skill 名称
   - 版本号
   - 依赖指针
   - 测试用例
2. 增加 CI 校验：
   - 所有 `SKILL.md` 的 frontmatter 校验
   - references/docs 断链检查
   - 最小脚本 dry-run 检查
3. 增加发布规范：
   - 语义化 tag（`v0.3.x`）
   - changelog 按 skill/规则/数据更新分区

## 当前入口

- 英文主页：`README.md`
- 中文主页：`README.zh-CN.md`
- 能力目录（英文）：`docs/skill-catalog.md`
- 能力目录（中文）：`docs/skill-catalog.zh-CN.md`
- 执行流程（英文）：`docs/workflow-playbook.md`
- 执行流程（中文）：`docs/workflow-playbook.zh-CN.md`
- 使用示例与融合（英文）：`docs/usage-examples.md`
- 使用示例与融合（中文）：`docs/usage-examples.zh-CN.md`
- 运行时 skills：`.agents/skills/`
- 知识库：`.references/`

