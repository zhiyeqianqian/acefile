# Progress Log

## 2026-03-02
- private_lab 已恢复到当前仓库。
- 决策已更新：样本范围固定为 Google/腾讯/美团。
- Gold Set 概念与冻结规则已写清。
- 标注流程因人工资源不足，先记 TODO，不阻塞 MVP 第一阶段。

## 2026-03-02 / MVP 开工（Phase-1）
- 新增 `mvp_tool` 最小可运行实现：company profiles + passive asset discovery CLI。
- 新增评测脚本 `evaluate.py`，支持对 gold set 计算 Recall@N。
- 提供 Google/Tencent/Meituan 样本配置与首个 gold set 示例。
