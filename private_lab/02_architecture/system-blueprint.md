# 系统蓝图（V1）

## 1. 总体流水线
1) Company Seed（公司名/别名）
2) Entity Expansion（法律实体、集团、投资关系）
3) Asset Discovery（域名、证书、IP、App、代码线索）
4) Asset Attribution（归属打分与证据链）
5) Service Fingerprinting（端口/协议/组件识别）
6) Vuln Intelligence Mapping（CVE/Exploit/PoC 关联）
7) Verification Runner（仅无害 PoC 验证）
8) Analyst Workbench（人工复核与导出）

## 2. 关键设计原则
- 研究先行：每个模块先调研再开发
- 全链路可审计：每个结论有证据来源
- 可恢复执行：任务中断后可继续
- 默认安全：不自动执行破坏性 exploit

## 3. 数据模型（最小集合）
- `entity`：公司与关联主体
- `asset`：域名、子域、IP、证书、应用、仓库
- `evidence`：来源、时间、原始片段、置信度
- `service`：端口、协议、版本、指纹
- `finding`：漏洞映射、验证状态、风险等级
- `task_run`：任务配置、执行日志、状态机

## 4. 验收导向指标（初稿）
- 资产发现召回率（对比人工基线）
- 资产归属准确率（抽样复核）
- 指纹识别准确率
- 漏洞情报关联正确率
- 平均任务恢复时间（中断后）
