# Flow Systems — Session 5

本目录依据 [`propose-flow-systems.md`](propose-flow-systems.md) 推进连续时间流、闭轨、动力 Zeta、trace 与自然量子化研究。所有正式 Route-A/Route-B 判定均区分定理、数值观察、启发式和建模选择；黎曼零点数据不参与候选定义、筛选或参数调整。

## 进度索引

| 阶段 | 状态 | 结论与入口 |
|---|---|---|
| `1-classical-flow` — Route A / A0--A1 | **第一阶段完成，检查点已确认** | 得到“两半阻碍”：Deninger 算术流内生地产生周期为 `log p` 的紧致轨道包，但尚无规范化单轨 trace；模曲面测地流具备完整闭轨与 Selberg/Ruelle 架构，但其标准长度支撑与所有 `k log p` 严格不相交。见[中文阶段摘要](papers/1-classical-flow/notes/stage1_summary_zh.md)与[研究论文](papers/1-classical-flow/paper/paper.pdf)。 |
| `2-flow-zeta` — Route A / A1--A3 | **完成，独立审稿修订通过** | 证明每个素数 packet 含不可数条同长本原轨道，故普通逐轨 Ruelle 乘积在单个 packet 内即发散；测度/群胚/上同调替代仍为 `NOT_TESTABLE`，不是被否证。见[论文](papers/2-flow-zeta/paper/paper.pdf)、[审稿](papers/2-flow-zeta/notes/peer_review_round1.md)与[Route-A 记录](evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage3.yaml)。 |
| `3-trace-bridge` — Route A / A3--A4 | **完成，独立审稿 ACCEPT** | 建立同一对象 trace certificate `T0--T7`；证明局部 trace germ 的 smooth ambiguity、不同对象 coordinate-splice 失效，以及模曲面重复长度与所有 `k log p` 严格不相交。见[论文](papers/3-trace-bridge/paper/paper.pdf)与[发布审计](papers/3-trace-bridge/notes/release_audit.md)。 |
| `4-arith-flow` — Route A / A0--A3 正控 | **完成，独立审稿 ACCEPT** | 有限域 Frobenius suspension 精确生成原生 Hasse--Weil zeta；一时钟定理排除 characteristic-zero 全素数目标，逐素数圆周拼接被认证为 `PROVES_TOO_MUCH` 编译器。见[论文](papers/4-arith-flow/paper/paper.pdf)。 |
| `5-quantum-flow` — Route A / A4 与有限 Route B / B1--B3 | **完成，独立审稿 ACCEPT** | 典范 Koopman 生成元定义完整且自伴，但点谱为 `(2*pi/log(2))*Q`、每点无穷重、全谱与本质谱均为 `R`，故在 B3 严格失败。见[论文](papers/5-quantum-flow/paper/paper.pdf)。 |
| `6-cohomological-owner` — 同母体 operator ownership | **完成，独立审稿 ACCEPT** | 精确 Hasse--Weil 行列式由分次 étale Frobenius 拥有，自伴悬挂时间由另一 Koopman 算子拥有；共同算术母体不允许跨算子拼接 Route-B credits。见[论文](papers/6-cohomological-owner/paper/paper.pdf)。 |
| `7-packet-groupoid` — Route A / A0--A3 | **完成，引用审计 ACCEPT、同行评审 FINAL ACCEPT** | 修复 finite-kernel `E_f` 的同一来源拓扑桥并证明其横向塌缩与严格非满射；在显式 proxy 上分离局部有限 return distribution 与右半平面零模 trace-log determinant，证明后者 base-blind、可编译任意时钟，故四个 typed records 均保持 `ROUTE_A_EXPLORATORY`。见[论文](papers/7-packet-groupoid/paper/paper.pdf)、[中文摘要](papers/7-packet-groupoid/notes/stage7_summary_zh.md)与[Route-A 审计](papers/7-packet-groupoid/notes/route_audit.md)。 |

可复现实验、判定 YAML、证明笔记和来源审计保存在各论文目录、
`evaluations/`、`docs/` 与 `skills/`。本地工作目录本身不是 Git 仓库；发布时
按 proposal 统一同步到远端仓库的 `flow_systems/` 子目录。

论文 2--6 的统一封板、Route 状态、障碍、发布哈希与下一批优先级见
[五篇批次报告](BATCH_REPORT_PAPERS_2_6.md)。

## 按时间记录

1-classical-flow - Route A / A0-A1（研究中） - 已冻结比较问题、候选流、禁用数据与验证方法，主检验为“算术自然性”和“可复现 primitive/repetition ledger”能否同时成立

1-classical-flow - Route A / A0-A1（第一阶段完成） - 完成 Deninger 与模曲面两条最强路线、通用流和先前工作的基线比较；证明标准模曲面长度支撑的 rational-prime obstruction，并将 Deninger 保留为 packet-trace 探索候选

2-flow-zeta - Route A / A1-A3（Phase 1 完成，等待确认） - 冻结 Deninger packet trace 的存在性/规范性问题、模曲面 Ruelle 校准、target-free trace obligations 与八项 falsification controls；独立对抗审查无 critical flaw

2-flow-zeta - Route A / A1-A3（完成） - 证明 Deninger 素数 packet 的不可数同长轨道使普通逐轨乘积严格发散；区分 Haar 基概率、packet lift、跨素数质量与 operator trace，独立 peer/citation audit 修订后封版

3-trace-bridge - Route A / A3-A4（Phase 2 完成） - 建立同一对象 trace certificate，并完成 local-germ smooth ambiguity、模曲面/素数时钟支撑不交与 coordinate-splice 三项证明及零点无关控制

4-arith-flow - Route A / A0-A3（Phase 1 完成） - 冻结有限域 Frobenius suspension 正控，精确复现 Hasse--Weil zeta，同时证明固定有限域时钟与 characteristic-zero 全素数目标不兼容

3-trace-bridge - Route A / A3-A4（完成） - 同一对象证书、局部 germ 歧义和模曲面/素数时钟不交定理通过独立审稿，11/11 控制复现通过

4-arith-flow - Route A / A0-A3（完成） - 原生有限域正控与 one-clock/普适 Euler 编译器负控通过独立审稿，13/13 控制复现通过

5-quantum-flow - Route A / A4，有限 Route B / B1-B3（完成） - 典范 Koopman 算子通过 B1/B2，但以稠密无穷重本质谱在 B3 失败，8/8 控制复现通过

6-cohomological-owner - Route A / A0-A4，有限 Route B / B1-B5（完成） - 精确区分 étale Frobenius 行列式拥有者与 Koopman 自伴时间拥有者，禁止跨算子 credits 拼接，10/10 控制复现通过

7-packet-groupoid - Route A / A0-A3（Phase 1 完成） - 冻结 mass-family decomposable proxy；证明计划已将局部有限回归分布与零模迹行列式分离，并在独立复审中关闭 global L1 trace-domain Critical 与 theorem/certificate 命名冲突

7-packet-groupoid - Route A / A0-A4（完成） - 证明 finite-kernel 同一来源拓扑桥的 packetwise 满射、横向塌缩与严格全局非满射；建立 FNS trace/domain、局部有限 return Radon measure 和右半平面 principal trace-log 的严格分层，21/21 控制通过，独立引用审计与同行评审封板

## 本批（论文 2--6）统一结论

最强正进展是得到一个完全精确的有限域校准链：闭点、Frobenius 周期、悬挂
闭轨、点计数、Lefschetz 迹与分次上同调行列式全部同源且全局相等。最强负
进展是证明“同一个算术母体”仍弱于“同一个算子”：自然自伴 Koopman 算子
不拥有该行列式，且其稠密、无穷重本质谱排除标准 Hilbert--Pólya 谱型。

当前 rational-prime Route A 没有可晋级候选；Deninger packet 路线保持探索态，
其下一门槛是从来源内生地产生可测 packet lift、跨素数质量与一个真正的
trace-bearing operator。Route B 当前整体不就绪；任何下一候选必须先证明
单一算子的域、自伴/闭性和谱型，再证明同一算子的素数幂 trace 与全局
completed-`xi` 行列式。

## Paper 7 单篇检查点

Paper 7 的最强正进展不是又得到一个 Euler product，而是把三个容易混同的
owner 严格拆开：来源对象拥有 packet/时钟，return record 拥有精确的
primitive/repetition Radon ledger，零模 record 在 `Re(s)>1` 拥有精确的
principal trace-log scalar。最强负进展是证明这些 credits 不能拼接：来源桥
压塌横向 packet 标签且不传输测度或 trace；零模标量对基底几何完全盲，并能
编译任意 locally finite 时钟。

因此 source、mass family、return distribution 与 unit-mass zero mode 四份
Route-A 记录均为 `ROUTE_A_EXPLORATORY`，Route B 未调用。下一项最小而关键的
研究不是解析延拓，而是构造或排除一个来源内生、对 packet 几何敏感的真实
groupoid/Haar/representation/trace transport；它必须在 singleton base、
copied packet 或 arbitrary-clock controls 中表现出非平凡区分力。
