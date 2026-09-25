# CS14 证据索引

Scope ID: `ASFS-DISCOVERY-20260919-CS14`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run / separate saved-evidence validate
- Origin Date: 2026-09-19
- Verification Status: raw run UNVERIFIED; separate saved analysis ANALYZED
- Version Label: cs14_evidence_v1

Current status: `COMPLETE; FINITE-320 FIT SIGNAL; JOINT AND ROBUSTNESS GATES FAIL`。

## 定义和权限

[冻结卡](../candidate-card.md)、[预审澄清](../pre-execution-clarifications.md)、
[执行合同](../execution-card.md)和[输入锁](../input-locks.json)先于科学执行。
沿用用户的本地自动实现/执行授权，不重复逐命令确认。
不安装、不GPU、不外传、不生成新目标、不提交推送、不制作PDF。
原始候选卡字节保留，澄清单列且一同SHA锁；旧资料只读。

## 已完成证据

1. [形式审查](preflight-form-review.md)、[代码预审](preflight-code-review.md)、
   [实现SHA锁](implementation-freeze.json)：先于唯一科学执行。
2. [实际执行回执](execution-receipt.json)：session41077/PID118228，exit0，
   27.154567秒；外部8秒/23秒及首尾监控，无超过30秒的空档。程序在首次
   内部30秒资源采样前结束。峰值RSS363032KiB，无超时/硬控制失败/重试。
3. [run-1原始结果](run-1/result.json)、[运行清单](run-1/manifest.json)、
   [事件](run-1/events.jsonl)、[全部调用](run-1/calls.json)：30对调用，
   29独立点、1缓存、66物理全分解；另2次矩阵控制组装，无额外谱解。
4. [身份冻结](run-1/winners-frozen.json)、[训练数组冻结](run-1/training-arrays-frozen.json)：
   主赢家0028和两格数组先冻结，后解析已知开发数据，不重选。
5. [逐点CSV](run-1/points.csv)、[四窗拟合](run-1/fit-rows.csv)、
   [比较窗口](run-1/comparison-rows.csv)、[必要条件判定](run-1/finite-discovery-assessment.json)：
   4480/56/48行，主3/2和原始J两读出均保存，失败窗口不删除。
6. [完整文件库存](run-1/file-inventory.json)：184个成员，加库存文件自身共
   185文件、34560025字节。科学目录排他创建且完成后未修改。
7. [只读保存分析器](../check_saved_outputs.py)、[首次调用真实结果](saved-analysis-result.json)、
   [独立保存报告](saved-output-review.md)：session45051、exit0、failures为空；
   68 NPZ=66物理调用+2赢家副本、10份含态、16输入锁/4冻结/全库存一致。

原始目录保存完整矩阵/全谱/规定同次态及全部控制。没有科学重跑；
保存分析不调用谱分解/优化/求积/求根，只标ANALYZED，不能升级原run为VERIFIED。
非赢家态未按卡保留，审查不声称复核缺失态的向量方程。

## 结果范围

主n52全320 MAPE1.149170%是有限积极信号，但J1.856056>1、低100最坏
误差9.568466%，两细截断/基宽G12.534604%/2.314617%/3.025945%均未过门。
决策为保留解析构造及有限信号，stop稳健晋升并fork；不追加预算。

## 明确限制

所有320目标此前已知，后220不是盲测。角色分工是本地模型辅助检查，
不是外部同行评审、跨模型验证或用户已读确认。精确形式论证、相体积、
浮点矩阵检查与有限目标误差分别报告；不汇成Route信用。
ARS数字解释已覆盖全部11类适用性检查，但不为确定性拟合制造p值或CI。
