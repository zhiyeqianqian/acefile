# MVP Execution Plan（简版）

## 目标
输入公司名，输出归属资产清单（带证据与置信度）。

## 样本
- Google
- 腾讯
- 美团

## 验收
- Recall@N：对比 Gold Set
- Precision@N：先统计 true/false/uncertain（人工不足时 uncertain 单列）

## 当前策略
- 先做可运行版本，保证可重复输出；
- 标注流程自动化后再提高 Precision 闭环强度。
