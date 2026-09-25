# DS03 — 已存谱态的能量混合与读出诊断冻结卡

**Scope ID:** `ASFS-DISCOVERY-20260919-DS03`。  
**Paper ID:** `246-spectral-readout-mixing`。  
**Version / date:** 1 / 2026-09-19；先于本轮数组分析冻结。  
**Freeze status:** `AUTHORIZED SAVED-ARRAY ANALYSIS; NOT YET ANALYZED`。  
**Current status:** `READOUT DIAGNOSIS COMPLETE; EXPECTATION-BASED LOGARITHM IDENTIFIED`。  
**Formal coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

此状态为分析结束后追加；其余执行前方法不变。原字节保留为
[frozen-v1](candidate-card-frozen-v1.md)，诊断结果不覆盖 245。

## 授权与边界

用户在 245 交接“利用现有数组解释低阶态期望能量分布，再决定是否
追加稳定性实验”后答复“继续”。本轮仅只读分析 245 已存 NPZ/CSV
与源码，推导读出恒等式并记录诊断；不导入 solve、不重新传播、
不重新分解 U_tot、不调参、不新增零点、网格、模型或谱系。
可对已存同一 H_base 作一次 Hermitian 特征分解以表达已有态，
该分解是观测基底，不替代原读出或增记一次动力学实验。

原对象 DS02-D/S 的全部输入仍由
[245 原卡](../245-dynamic-start-ablation/candidate-card-frozen-v1.md) 定义。
两组独立演化/谱/排序/首点尺度保持分开。共享 H_base 必须先验证
逐元素相同；不相同时停止共同基底比较。

## 冻结方法

1. 验证 NPZ、来源代码和比较文件身份；只读加载 allow_pickle=False。
2. 检查 evecs 列范数、正交偏差、ee 重算、H_base 相同；不通过
   基底旋转、正交化或删除态来改善原结果。
3. 对共同 H_base=Q diag(epsilon) Q*，计算 W_kj=|Q* v_j|²；
   以列范数校正的权重用于期望/方差诊断，并保留原 ee 读出。
   核对 ee、动能/势能期望、能量方差、最大权重与有效参与数。
4. 报告全部态汇总及按原重构能量排序最低 10 态；重点比照最低
   三态的能量混合。不同组排序号相同不等于同一物理态。
5. 检查 [H_base,U_tot] 与低阶态的 H_base 本征态残差；低残差
   不是无限算子或收敛认证。静态原模型保留 kick 乘积，不偷换为
   exp(-i S H_base/hbar)。不从一次静态观测推导普适劣势。
6. 分离原整数重构偏移与首点尺度：用已存 ee 顺序及单独排序
   各作明确标识的纯期望诊断。不得把诊断改写为新“最优”基线。
7. 只作有限描述性分析，无 p 值、置信度或因果机制证明；完成
   ARS validate 的 11 项谬误覆盖，适用性不足如实标记 N/A。

后处理命令、输入 hash、stdout 和方法写入本包证据记录。计算只
输出 stdout，文件整理采用显式补丁；不改写 244/245 或上游快照。
未能解释的更深本征态形成原因保留 OPEN，不自动扩大实验预算。

## 谱系和原门状态

素数符号观测 → 非自治 Logistic 动机 → Hénon 有限数值几何提升；
本包诊断最后一箭头的有限算子读出，不宣称严格素数编码。
经典相空间、roof、悬流和闭轨账本 `NOT APPLICABLE`；
A0/A1/A2/T0–T3 `NOT EVALUATED`。原 241/242 仍暂停。
