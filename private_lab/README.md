# Private Lab

该目录已恢复到当前仓库内，用于继续推进 MVP。

## 当前已确认决策
1. 样本范围：互联网行业，`Google`、`腾讯`、`美团`。
2. Gold Set 规则：已冻结（见 `00_governance/decision-review-2026-03-02.md`）。
3. 标注流程：暂时缺少人工资源，先留 TODO，后续再自动化。
# Private Lab Workspace（漏洞赏金资产情报与验证框架）

> ⚠️ 仅限合法授权场景（Bug Bounty / 自有资产 / 明确书面授权）。
> 本项目默认不包含对未授权目标的利用动作，不自动执行破坏性 payload。

这个目录用于长期推进你的目标：
- 从“公司名”扩展到“可验证资产图谱”；
- 结合服务识别与漏洞情报，形成可审计的验证流水线；
- 在每个模块动工前，先做公开工具/商业产品调研并记录；
- 过程可中断可恢复（24x7 运维视角），沉淀为可复用 SKILLS。

## 目录结构
- `00_governance/`：边界、授权、日志与证据链规则
- `01_research/`：模块调研模板与调研结论
- `02_architecture/`：总体架构、数据模型、模块接口
- `03_execution/`：里程碑、待办、运行手册、值班记录
- `04_skills/`：经验沉淀（踩坑、反模式、最佳实践）

## 建议下一步
1. 先在 `00_governance/authorization-policy.md` 补全你可扫描的计划范围与账号。
2. 按 `01_research/module-research-template.md` 对首个模块（公司名 -> 实体名）做竞品调研。
3. 在 `03_execution/progress-log.md` 开始第一条“可验证进展记录”。

## 关于“私密”
代码目录已经单独隔离为 `private_lab/`，但 **GitHub 可见性需要在仓库设置里切换为 Private**。
