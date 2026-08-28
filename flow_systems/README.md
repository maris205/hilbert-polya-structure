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
| `8-isotropy-trace` — Route A / A0--A4 | **历史论文完成；实际拓扑归属已由 Paper 9 更正** | Paper 8 的 Zak、Poisson、FNS 与有限角 normality 计算在标准 Hausdorff 圆代理上仍成立；Paper 9 证明真实继承轨道并非该圆，而是非平凡不可分空间，因此这些计算已版本化重归属为 proxy-only。正时间 coefficient-one scalar ledger 不受影响。见[论文](papers/8-isotropy-trace/paper/paper.pdf)、[历史摘要](papers/8-isotropy-trace/notes/stage8_summary_zh.md)与 Paper 9 的[更正矩阵](papers/9-packet-separation/paper/paper.pdf)。 |
| `9-packet-separation` — Route A / A0--A4 | **完成，引用审计与独立同行评审 ACCEPT** | 构造性证明 `Z[1/p]_{>0}` 在实数/prime-to-`p` 完备化中同时稠密，并在同一有限核纤维内合法提升收敛；由此真实 `E_f` 素数 packet、每条继承轨道及 `Q_p` 都是非平凡不可分空间，限制轨道关系非闭。真实标准 LCH 分支在拓扑前提处失败，旧圆周迹公式仅保留为显式代理。见[论文](papers/9-packet-separation/paper/paper.pdf)、[中文摘要](papers/9-packet-separation/notes/stage9_summary_zh.md)与[Route-A 审计](papers/9-packet-separation/notes/route_audit.md)。 |
| `22-fppf-verschiebung-lifts` — 纯代数支撑定理 | **Stage 6 已确认完成；Pipeline completed** | 对所有 `N>1` 证明 fppf 与 finite-flat site 上 Verschiebung 加性 sheaf lift 不存在；`N=1` 为严格对照，并精确限定 Deninger v1 Cor. 4.6 的修正半径。见[论文](papers/22-fppf-verschiebung-lifts/paper/paper.pdf)、[结论概要](papers/22-fppf-verschiebung-lifts/README.md)、[中文流程记录](papers/22-fppf-verschiebung-lifts/notes/stage6_process_record/paper_creation_process_zh.pdf)与[完成收据](papers/22-fppf-verschiebung-lifts/notes/stage6_process_record/stage6_completion_receipt.md)。 |
| `24--28` — 五种连续时间子型 | **Round 6 完成；三席独立复审 CLEAN，5/5 typed records，221/221 全量测试通过** | P24 以 25 个 Nielsen markings 证明当前相位统计量 marking-sensitive 并停止；P25 建立 747-owner 的精确符号 Euler/trace/determinant 负控，得到唯一的 typed A2；P26 证明 inverse-paired 二阶变分与 quadratic degree-moment iff obstruction；P27 将论文定位收窄为 compact-versus-cusped owner audit；P28 用八个精确 `SL(2)` 共轭子闭合 withheld records，owner 数仍为 36/field。形式对象 `5/5` 已分配 tuple，但正向算术候选到达 A2 仍为 `0/5`，Route B `0/5`。见[Round-6 报告](BATCH_ROUND6_PAPERS_24_28.md)。 |

可复现实验、判定 YAML、证明笔记和来源审计保存在各论文目录、
`evaluations/`、`docs/` 与 `skills/`。本地工作目录本身不是 Git 仓库；发布时
按 proposal 统一同步到远端仓库的 `flow_systems/` 子目录。

论文 2--6 的统一封板、Route 状态、障碍、发布哈希与下一批优先级见
[五篇批次报告](BATCH_REPORT_PAPERS_2_6.md)。

## Paper 22 结论概要

对每个 `N>1`，有限自由根覆盖 `k[x] -> k[s]`、`x -> s^N` 强迫出的
Verschiebung 局部前像在 overlap 上不能下降。因此，`V_N` 在 fppf site 上不存在
通过 `omega` 的加性 sheaf lift；finite-flat site 的非存在性由独立论证得到。
等价地，对 `e:0->K->Z->W->0` 不存在 `u:K->K` 使
`u_*e=V_N^*e`；`N=1` 的 identity lift 是严格对照。该反例要求修正
Deninger v1 Corollary 4.6 的 sectionwise Dedekind-ring 表述，但不否定
Propositions 4.3、4.5 或 Corollary 4.7。

## Papers 24--28 最新结论

五篇均处于 Proposal Stage 1 / Route A A0--A1，Route B 未调用，Gates A--E
未到达。Round 6 首次为五个精确冻结对象全部分配 formal Route-A tuple：三个
`ROUTE_A_EXPLORATORY`、两个 `ROUTE_A_REJECTED`。这不等于五个主物理候选已
过 A2：正向算术候选到达 A2 仍为 `0/5`；唯一
`A2_ANALYTIC_DETERMINANT` 属于 P25 的非算术 unit-roof symbolic negative
control。五篇全历史测试 `221/221`、本轮重放测试 `61/61`、五项双遍字节一致
全部通过；ARS Stage 2 仍未授权。

| Paper | 子类型 | 当前明确进展 |
|---|---|---|
| [P24](papers/24-bianchi-holonomy-flow/README.md) | cusped hyperbolic 3-flow | identity 加全部 24 个 elementary right Nielsen moves 的 25-marking panel 已执行；候选宽度 `0.9163000440`、控制宽度 `16.9152926064`，25/25 contrasts 同号，但 current phase statistic 严格判为 marking-sensitive 并 `STOP_SCOPED`。typed proxy 为 `A0_WEAK/A1_WEAK/A2--A4_FAIL`，full flow 仍 `UNASSIGNED` |
| [P25](papers/25-three-disk-scattering-flow/README.md) | open three-disk scattering | unit-roof 三符号 no-repeat suspension 在长度 12 前有 747 oriented primitive owners；Euler、trace exponential 与 `3 x 3` determinant 精确一致，`zeta_pi(z)=zeta_0(-z)`。typed control 为 `A0_FAIL/A1_PASS/A2_ANALYTIC_DETERMINANT/A3--A4_FAIL`；physical billiard 仍 `UNASSIGNED` |
| [P26](papers/26-level11-newform-time-change/README.md) | arithmetic geodesic time change | inverse-paired 二阶变分为 orientation-even；quadratic Euler recurrence 当且仅当 `Q_1=lambda_p I(M)^2`、`Q_d=0 (d>1)`。`a_p` 与 `a_p^2` 各失败 51/55 groups、153/165 rows，`a_p^2-p` 失败 55/55、165/165；仍无 global determinant/A2 |
| [P27](papers/27-congruence-inverse-limit-no-go/README.md) | inverse-limit geodesic lamination | `Per(M_infinity)=empty` 正式记为 `A1_FAIL`；短 compact-versus-cusped owner audit 为 `GO`，一般 aperiodicity novelty 与 same-owner A2 均 `NO-GO`。13-row claim/source matrix 已冻结，9 个外部 locator 等待作者确认 |
| [P28](papers/28-bolza-magnetic-flow/README.md) | magnetic Hamiltonian flow | 八个 withheld records 均有精确直接 `x^-1gx=h` 共轭子，无 inverse fallback；44 个 certified primitive records 精确分成 36 owners + 8 duplicates，576-row branch ledger 不变。bounded proxy 为 `A0_WEAK/A1_WEAK/A2--A4_FAIL`；non-arithmetic control gate 仍 `0/6 FAIL_CLOSED` |

下一批最小合法产物已经收窄：P24 停止当前相位统计量，只有 source-derived
prime-ideal owner theorem 或全新预冻结 invariant 才能重开；P25 保留为 A1--A2
methods negative control；P26 精确分类四个 `p=5` quadratic survivors；P27 在
作者确认九个来源 locator 后形成比较短文；P28 获取满足六项 fail-closed 门禁
的非算术 genus-2 source package，并另行处理 322 个开放 primitivity cases。
详细结论、哈希、路线对应与动力系统计数见
[Round-6 执行报告](BATCH_ROUND6_PAPERS_24_28.md)。

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

8-isotropy-trace - Route A / A0-A4（完成） - 在同一个已选定实际 `E_f` 素轨道上闭合 one-orbit groupoid、character trace、fixed regular FNS trace 与 finite-corner normality obstruction；packet 主问题保持 `NOT_TESTABLE`，固定单轨 analogue 为 `REFUTED`，正时间 closed-point scalar ledger 为 `PASS`，18/18 target-free controls 通过，五份 Route-A records 均保持 `ROUTE_A_EXPLORATORY`，Route B 未调用

9-packet-separation - Route A / A0-A4（完成） - 证明真实有限核素数 packet、全部继承周期轨道和时间轨道商均为非平凡不可分空间，限制对角轨道关系非闭；据此撤回 Paper 8 对真实轨道的标准圆/LCH 归属，并将 Zak、Poisson、FNS 与 character-trace 结果严格重归属到标准圆代理，20/20 target-free controls 通过，八份 Route-A records 均保持 `ROUTE_A_EXPLORATORY`，Route B 未调用

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

## Paper 8--9 版本化检查点

Paper 8 在标准 Hausdorff 圆上得到的局部算子数学仍然成立：dual-Haar regular
FNS trace 的值为 `Tau_L(a_f)=L f(0)`，会抹去全部非零回归；
trivial-character C*-trace 则给出 `tau_0(a_f)=L sum_r f(rL)`，并且不能沿固定
regular map 正常延拓。Paper 9 的更正不否定这些公式，而是撤回其“真实继承
Deninger 轨道”owner：真实轨道的继承拓扑不是标准圆，而是非平凡不可分拓扑。

Paper 9 通过同时实数/profinite 逼近与固定阶段有限核特征收敛，证明对同一
`Gamma_p` 中任意有序点对 `x,y`，常值序列 `x,x,...` 都收敛到 `y`。因此
`Gamma_p`、每条继承轨道及 `Q_p` 均不可分且非 `T0`，限制对角等价关系非闭；
朴素阿代尔双重商中的真实继承 `C_p` 也不可分。Connes--Consani scaling site
内生定义的 Hausdorff 圆与显式标准圆代理仍是不同对象，不受此定理否定。

Stage 9 以八份 typed Route-A records 完成版本化重归属：真实 packet/轨道的
标准 LCH--Hausdorff branches 为 `A1_FAIL`，真实拓扑定理 records 为
`A1_WEAK`，标准圆 regular trace proxy 为 `A1_FAIL`，标准圆 trivial-character
proxy 为 `A1_PASS_ANALYTIC`；全部 `A2_FAIL/A3_FAIL/A4_FAIL`、overall
`ROUTE_A_EXPLORATORY`，Route B 未调用。正时间 coefficient-one scalar ledger
`Theta_+` 与拓扑无关，保持原 Stage-8 记录且不重复发放 credit。下一项最小
检验是研究不可分 packet 的 `T0`/Hausdorff 反射与连续可观测量究竟保留多少
算术信息，而不是再把标准圆拓扑倒灌给来源对象。

15-wieferich-ulm-packet-bases - 理论全文 / 用户授权 Stage-2 草稿（2026-08-22） - 已形成 14 页论文与可复建 PDF，证明裸紧群 `B_p` 的 Wieferich--Ulm 主分量结构及按 `kappa_r(p)` 的完整拓扑分类，并以 `r=11` 区分 `B_2` 与 `B_3`；Route-A 仅 required-input `NOT_TESTABLE` 且不分配 A0--A4/overall verdict，Route-B 为 `ROUTE_B_NOT_TESTABLE`，无 Route 晋级、发布或投稿授权。

15-wieferich-ulm-packet-bases - Stage-2.5 完整性门 PASS（2026-08-22） - 10/10 来源、22/22 引用语境、8/8 claim 与 14 条 evidence rows 已核验；一轮局部书目/措辞修订后 open issues=0，14 页 PDF 干净重建通过。当前停在强制用户确认点，Stage 3 模拟同行评审尚未启动，发布/投稿/Route 晋级仍无授权。

19-standardized-nerve-cohomology - Phase-2 去留结题/归并（2026-08-24） - 在精确 author-complex 比较成立的条件下，标准化 owner 的连续非正规化上同调 theorem shape 为 `H^0=H^1=R^Q`、`H^n=0 (n>=2)`；比较、cup 与高阶 `J*` 尚待本地证明。经典先例已足以停止独立 Paper 19，材料留作 Paper 12 修订。

20-wieferich-ulm-separation - Phase-2 技术推论/归并（2026-08-24） - 每个固定有限 `kappa` 模式具有显式乘积相对素数密度，故每个固定有限坐标投影都有正密度无限纤维；局部计数有既有先例且一篇 2023 近邻全文仍待核，停止独立 Paper 20，归并 Paper 15。

21-effective-exact-order-witnesses - Phase-2 来源门 PASS / 存活（2026-08-24） - 精确条件总密度修正为 `(r-1)/r^(m+1)`，单一冻结类密度为 `r^(-(m+1))`；无条件与 ERH/GRH 黑箱最小见证界已闭合。Phase 3 唯一硬门是计算 `E/Q(zeta_r)` 的局部 Artin 导子并证明相对导子界确有改进。

22-fppf-verschiebung-lifts - Stage-6 完成 / Pipeline completed（2026-08-26） - 13 页终稿论文保持不变；1,653-word 中文 Markdown 与 14 页流程记录 PDF 已生成。用户以精确事件 `确认完成 Paper 22 Stage 6` 接受已交付记录，Stage 6 与全局 pipeline 均转为 `completed`；流程记录原字节保持不变，另以完成收据承载 post-delivery 状态。Git 同步在既有授权范围内；投稿、额外公开发布、外联和 Route 晋级仍未授权。

23-normal-trace-return-erasure - Phase-2 技术短注/归并（2026-08-24） - normal semifinite tracial weights 是中心密度权；全圆平移不变性恰好选出标量 Haar 权（正标量时为 FNS）并推出非零回归擦除，反向命题在一般 semifinite 类上未证明。分类主体属经典结果，停止独立全文，优先并回 Paper 8，且不转移到真实非 Hausdorff packet。

24-bianchi-holonomy-flow - Stage 1 / A0--A1（2026-08-26） - 已自包含证明 level-`(3)` neat/torsion-free，冻结 complex length、cusp-aware zeta 与 `Q(i)` prime-ideal owner；rational-prime push-forward 单列 split/inert/ramified 规则，正式 Route tuple 尚未分配。

25-three-disk-scattering-flow - Stage 1 / A0 负控（2026-08-26） - `d=6a` no-eclipse 条件已证明，exact multiple-scattering determinant 与 semiclassical orbit zeta 已分层；算术来源按控制设计缺失，word-length-12 half-density `PROVES_TOO_MUCH` 检验内部预声明但尚未执行，正式 tuple 未分配。

26-level11-newform-time-change - Stage 1 / A0--A1（2026-08-26） - level-11 newform one-form、time-density `rho`、速度乘子 `1/rho`、`X/rho` generator、正性区间和闭轨周期一阶变分已冻结；Hecke/Euler decomposition 保持 `HEURISTIC`。

27-congruence-inverse-limit-no-go - Stage 1 / local A1 obstruction（2026-08-26） - 对 `Gamma(3n!)` residual tower 证明极限 geodesic flow 无任何周期点，记录 `PROVED_A1_OBSTRUCTION`；因 formal evaluator tuple 尚未分配，不写正式 `A1_FAIL`，有限层 renormalized statistic 必须另列 owner。

28-bolza-magnetic-flow - Stage 1 / A0--A1（2026-08-26） - 曲率 `-1` Bolza surface 上 `b=1/2` 给出 degree-one flux；非 exact 场排除全局 `A`，phase owner 修正为 connection holonomy；主量子架构冻结为随 `N` 改变的 `Delta^{L^N}` 半经典族，固定 `Delta^L` 的高能 trace 与磁轨 ownership 明确保留为 `OPEN/NOT_ESTABLISHED`，Route B 未调用。

24--28-round2 - Stage 1 / Route A A0--A1（2026-08-27） - 五种连续时间子型均落地一个 target-free 可执行产物，31/31 测试与 5/5 确定性复验通过；P25 的 generic half-density statistic 局部判定 `STOP_SCOPED / PROVES_TOO_MUCH`，P27 的 `Per(M_infinity)=empty` 保持 `[PROVED] PROVED_A1_OBSTRUCTION`，其余有限账本不越界为 full owner。正式 Route-A tuples `0/5`、A2--A4 `0/5`、Route-B invocations `0/5`。详见 [Round-2 报告](BATCH_ROUND2_PAPERS_24_28.md)。

24--28-round3 - Stage 1 / Route A A0--A1（2026-08-27） - 五篇分别落地 Schottky 非格控制、2,241/2,241 直接物理稳定性复验、newform 共轭/反向/重复 owner 定理、最近先例收窄和 source-bound magnetic even-subsequence trace 定理；34/34 测试通过。P27 不再主张一般 aperiodic laminated-flow novelty，P28 严格区分 frozen subtype `PROVED` 与 full/fixed regimes `OPEN/NOT_ESTABLISHED`。正式 Route-A tuples `0/5`、A2--A4 `0/5`、Route-B invocations `0/5`。详见 [Round-3 报告](BATCH_ROUND3_PAPERS_24_28.md)。

24--28-round4 - Stage 1 / Route A A0--A1（2026-08-27） - 五篇分别落地 finite-volume/cusp non-arithmetic 控制、fallback-selection 方法审计、Hecke correspondence cycle-sum owner theorem 与 genus-one kill、残余塔 quotient-order/period-escape theorem、48 行 Bolza magnetic owner seed；45/45 本轮测试和 5/5 确定性复验通过。正式 Route-A tuples `0/5`、A2--A4 evaluations `0/5`、Route-B invocations `0/5`，Stage 2 未授权。详见 [Round-4 报告](BATCH_ROUND4_PAPERS_24_28.md)。

24--28-round5 - Stage 1 / Route A A0--A1（2026-08-27） - 五篇分别落地 matched marked-word comparison、universal symplectic half-density theorem、canonical zeta first-variation zero 与 Hecke degree-moment obstruction、closed-surface factorial period escape、390-class Bolza marked-cyclic census/576-branch magnetic ledger；55/55 本轮测试和 5/5 确定性复验通过。正式 Route-A tuples `0/5`、A2--A4 evaluations `0/5`、Route-B invocations `0/5`，Stage 2 未授权。详见 [Round-5 报告](BATCH_ROUND5_PAPERS_24_28.md)。

24--28-round6 - Stage 1 / Route A A0--A1 与 A1--A2 负控校准（2026-08-28） - 五个精确冻结对象首次全部分配 typed Route-A tuple：P24 Nielsen marking-sensitivity stop、P25 exact symbolic Euler/trace/determinant negative control、P26 inverse-paired second variation 与 quadratic degree-moment obstruction、P27 compact-versus-cusped owner-audit go/no-go、P28 八个 exact `SL(2)` conjugacy duplicates。全量测试 `221/221`、本轮 replay tests `61/61`、5/5 双遍确定性复验通过；typed tuples `5/5`，但正向算术候选到达 A2 仍 `0/5`，Route-B invocations `0/5`，Stage 2 未授权。详见 [Round-6 报告](BATCH_ROUND6_PAPERS_24_28.md)。
