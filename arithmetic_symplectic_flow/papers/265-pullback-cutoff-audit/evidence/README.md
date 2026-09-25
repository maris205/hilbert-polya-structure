# CS15 evidence index

Scope ID: `ASFS-DISCOVERY-20260919-CS15`。

## Material Passport

- Origin Skill: ARS academic-research-suite / experiment-agent。
- Modes: bounded local `run` plus saved-array `validate`。
- Origin Date: 2026-09-19；Version: CS15 fixed-parameter audit v1。
- Run status: completed, root-observed exit0；原始run passport为UNVERIFIED。
- Verification Status: 保存证据 **ANALYZED**，非独立科学重跑VERIFIED。
- 数据均本地既有；无上传、新目标、安装/GPU、提交/推送或PDF。

计算前：[形式审查](form-review.md)、[代码预审](preflight-code-review.md)、
[实现锁](implementation-freeze.json)、[16输入锁](../input-locks.json)。
实际执行：[父进程回执](execution-receipt.json)、[原始结果](run-1/result.json)、
[完整103文件库存](run-1/file-inventory.json)、[事件流](run-1/events.jsonl)。
数组审计：[检查器](../check_saved_outputs.py)、[首次调用完整stdout](saved-analysis-stdout.txt)。
[分析JSON](saved-analysis-result.json)、[独立保存审查报告](saved-output-review.md)
包含实际首次exit0回执、覆盖边界及11/11方法谬误适用性扫描。

10对象、24完整分解、零额外求谱/优化/目标生成；48NPZ、103科学文件，
202811855字节。264完整185文件原SHA保全。全部四窗/双读出、五项比较、
连续残差三部分、原始矩阵、全部λ/重数与规定前缀态均保存。
未保存的高位向量不冒充已重检。实际监控间隔与预定30秒有偏差，
回执保留精确时戳；无严格周期或连续监控声称。

同对象完整，有限稳定门通过，低指标误差保留。连续索引证书及算术
机制OPEN/NOT SUPPLIED；Route未评，formal UNASSIGNED，B NOT INVOKED。

交接文档检查：10份Markdown及两个总览的当前段共75个本地链接有效；
正文、README、claim ledger、结果卡的Scope ID和当前状态一致。
计算前卡按原字节保留。16输入锁及实现锁未变；新增文本无行末空白，
两个总览的git diff --check通过。文档整合后没有科学重跑。
