# Batch07 五篇跨论文科学边界审计 V1

日期：2026-09-13 UTC。审查席：`/root/batch07_cross_science_v1`，实际 secondary Codex 独立席。
对象：Papers27–31 的五个已经接受的本地版本。唯一写入对象为本报告；不编辑论文、锁、接受记录或索引。

## 1. 结论与审查效力

判定：`CROSS_PAPER_SCIENTIFIC_BOUNDARIES_PASS_WITH_DISCLOSED_BIBLIOGRAPHIC_ERRATA`。

```yaml
scope: five_accepted_manuscripts_cross_paper_scientific_audit
independent_findings: 5
pairwise_comparisons: 10
cross_paper_scientific_blockers: 0
required_fixes: []
disclosed_bibliographic_errata: 1
unresolved_scientific_fixes: 0
route_applicability: NOT_APPLICABLE
route_pass: NOT_GRANTED
new_novelty_score: NOT_PERFORMED
full_proof_rereview: NOT_PERFORMED
new_pdf_acceptance: NOT_PERFORMED
external_effect: NONE
```

五篇接受版的独立中心、共享前提和非主张可以同时成立；本次实际读取范围内没有发现结论相互否定、把前文结论重复申报为后文独立贡献、循环引用或跨系统拼接。P27/P28 的关键区别是“无置换的对角平移”与“同时置换后的残差转动”；P29 与 qPI 的关键区别是具体 Hénon 多项式族与完整有理 qPI 族；P30/P31 的共享接口仅为明确列出的原曲面及 pencil 基础，不是算术临界理想向实相关衰减的迁移。

这不是全球新意证明，不把既有候选评分、证明接受、本地成品接受混成一种 PASS。未变证明、查新及 PDF 验收不重开；本报告也不新增它们的独立票。依项目约定，完成主控汇总及另一席交付身份审计后即可就当前批次汇报并暂停，无需启动第六篇、补实验或扩张模型族。

使用 `research-review` 的实际资料收集、独立批评、claims matrix 和 required/optional 分离结构；该技能没有改变用户限定的审计范围。没有调用或冒称不可用 GPT-5.4、外部 MCP 模型、跨模型或真人评审。本席本人亲读下列主科学输入，没有再委派助手。审查为一轮有限跨文核对；没有因成熟方法重叠或可自含重证而制造必修项。

## 2. 接受输入身份与实际读取范围

### 2.1 源根和边界定位

以下简称只指接受版本，不指原冻结稿或失败构建：

| 简称 | 接受源入口 | 主科学定位 |
|---|---|---|
| P27 | [final-20260905-r0/main.tex](/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/final-20260905-r0/main.tex:28) | 摘要 28–55；引言 57–138；完整五条主定理 417–451；结论 1592–1684 |
| P28 | [paper-successor-20260905/main.tex](/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper-successor-20260905/main.tex:54) | 摘要 54–77；完整引言/Theorem A 79–282；结论 1792–1849 |
| P29 | [paper-successor-20260906-transcription-v1/main.tex](/root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/main.tex:33) | `sections/0_abstract.tex`、`1_introduction.tex`；主定理分列 §§3–8；结语在 §8:322–332 |
| P30 | [paper/v4/main.tex](/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v4/main.tex:26) | 主文件摘要 26–47；完整 `sections/01-introduction.tex` 三条主定理；末边界在 `08-two-jets.tex`:657–666 |
| P31 | [paper/v3/main.tex](/root/autodl-tmp/symplectic_map/papers/31-qpi-sharp-phase-mixing/paper/v3/main.tex:24) | `00-abstract.tex`、`01-introduction.tex`；`02-real-surface-main-theorem.tex`:357–483；`08-conclusion.tex` |

### 2.2 本席 FULL / PARTIAL 记录

FULL 指本人逐行读取该完整文件或所列完整单元；PARTIAL 不推称整篇通读。哈希核验不是语义阅读。

| 输入 | 实际范围 |
|---|---|
| 工作区指令 | `AGENTS.md`、`docs/WORKFLOW.md`、`/root/autodl-tmp/.codex/skills/skills-codex/research-review/SKILL.md` 均 FULL；`BATCH_07_CONTEXT.md` PARTIAL，以最新入口及本轮科学边界为导航，未把历史账本全部装入审计 |
| 五篇接受记录 | P27 `LOCAL_ACCEPTANCE_20260905.md`、P28 `LOCAL_ACCEPTANCE_SUCCESSOR_20260905.md`、P29 `LOCAL_ACCEPTANCE_20260906.md`、P30 `LOCAL_ACCEPTANCE_20260909.md`、P31 `LOCAL_ACCEPTANCE_V3_20260913.md` 均 FULL |
| P29/P30/P31 README 与科学锁 | 三份 README 均 FULL；P29 `SOURCE_SCOPE_LOCK_20260906.md`、P30 `SOURCE_SCOPE_LOCK_V2_20260909.md`、P31 `SOURCE_SCOPE_LOCK_V1_20260913.md` 均 FULL；P27/P28 未以不存在的 README 为入口 |
| P27 主文 | PARTIAL：1–461、700–1186、1592–1690；涵盖完整摘要/引言/主结果及主定理所指 equality、tail、reciprocity、radius 的完整声明和这些段落的证明；没有重读整个生存证明及六 fixture |
| P28 主文 | PARTIAL：1–282、285–610、730–849、916–1025、1191–1288、1345–1410、1510–1623、1624–1707、1792–1855；涵盖完整 Theorem A、具体 map、fan、incidence、carry、leading-survival 声明、monodromy、decoder、两个 period 和全部 annihilator 声明；不是完整 §5 生存证明或全部 decoding 例子的再次审查 |
| P29 主文 | `main.tex`、摘要、引言 FULL；§3 PARTIAL 1–90、110–187、240–267；§4 PARTIAL 1–115；§5 PARTIAL 1–120；§6 PARTIAL 1–43、111–209；§7 PARTIAL 1–69；§8 PARTIAL 1–44、135–175、178–216、267–332。四项中心结论及其量词完整读取；§2 原基构造及未列证明段未重读 |
| P30 主文 | `main.tex`、完整 `01-introduction.tex`、完整 `02-surface-pencil.tex` FULL；`08-two-jets.tex` PARTIAL 606–666，覆盖精确阶数/下界与最终边界。§§3–7 的完整证明未重读，不冒称本轮验证了整个 arithmetic 链 |
| P31 主文 | `main.tex`、摘要、引言、完整 `02-real-surface-main-theorem.tex`、完整 `07-global-asymptotics-sharpness.tex`、结论 FULL；`04-global-frequency-geometry.tex` PARTIAL 364–430，核完整分类声明与表。§§3、5、6 及其未列段的未变证明不重开 |
| 宏与书目 | 五篇接受版的宏文件及 `references.bib` 均 FULL；P30 宏名为 `macros.tex`，不是 `math_commands.tex`。这里只核实际书目文本、跨文引用关系和明确归属，不重新验证其所有外部元数据/原文 |
| M1 接续 | P31 `COMPLETE_SOURCE_DISPOSITION_V2_20260913.md` FULL，且亲读 V3 实际归属及全点局部段；不以处置标签替代现稿核对，也未重开 closed proof |
| 本轮书目勘误 | P27 `BIBLIOGRAPHIC_ERRATA_V1_20260913.md` FULL 36行；本人核对其准确源/PDF绑定、改正值与 P28 一致、仅 author 字段且不更换文献对象；外部一手元数据读取由主控承担，不倒签为本席亲读 |

不存在“仅看摘要却声称 FULL manuscript”的覆盖扩大。本报告中未列出的证明正确性沿用既有本地接受，未增加新认证。

### 2.3 有界身份核验

本席只重算五篇接受源与必要绑定记录，没有重扫旧构建树、TeX 依赖、图像或历史失败根。P27/P28 三源的当前 SHA 与接受记录逐项一致；P29/P30/P31 对接受源根实际执行其冻结清单的 `sha256sum -c`，分别 12/11/12 项全部 OK。这里只报告输入身份 MATCH，不据此声称 PDF 字节、数学或版面新通过。

| 接受记录 | 当前 SHA-256 |
|---|---|
| P27 local acceptance | `c74faa836e06b700b5b41ed40df50435100adb25226b034f4e2bf101db2828ce` |
| P28 successor acceptance | `9f0bb26d43ed68e5d7732b31c784facd2186d6bc15d4527cfdef1a9fbcbad27c` |
| P29 local acceptance | `efb0f0058ae55ab1ffb681581838df1b652985ed2d647ad0a3fbda467245c017` |
| P30 local acceptance | `cfb2f9e034716545fd22d9e7024d7b9b62d89350c3eecc97852870b17f094a52` |
| P31 V3 local acceptance | `179ed9984de2c3e020e690dac11f14b6ebf981a1ec9356e9f5006b8040baa618` |

| 源绑定 | 当前 SHA-256 |
|---|---|
| P27 main / macro / bib | `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8` / `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` / `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |
| P28 main / macro / bib | `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9` / `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` / `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |
| P29 `SOURCE_BUILD_MANIFEST_20260906.sha256` | `958dd5be31db838485feff5512ac675960ce7caa296f02c1f05b82b6b87e01ee` |
| P30 `SOURCE_V4_20260909.sha256` | `f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9` |
| P31 `SOURCE_V3_20260913.sha256` | `4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8` |

三份科学锁当前 SHA 分别为 P29 `87f8e7d4b4f28010ffbd689aa2e9b7c15e3c75240e1611f1b26f125cb4adbcc5`、P30 `66afedb5efe87a29250d24aa2ba275fe79b1ec6eee727e362b0fc7b2c48df5b2`、P31 `b056a664863e41cf778225118ea719a3e43b4a78c451d302703f423c931dd584`。无 Git 元数据，`commit: null`；不初始化仓库。

## 3. 五个精确独立 finding

### F27：严格证书下的对角平移、有限切换和逐字反射互易

对象是特征零、`r≥3`、两组有限非空 collected supports 位于 `Z_{≥2}^r`、系数非零的分离 Hamiltonian 双 shear `F=T_W∘S_V`。完整 source/reflected/target/transformed 条件、所需输入 leading tuples 和每边严格性是输入，不是结论。接受主定理 A–E 给实际 weighted-degree transport、`u'=u+δ1`、无限已存在严格分支上的 `N_pair≤d_V+d_W−2`、等号的唯一代表/实际采样/不同时切换条件、保留全局原点的 stationary tail，以及完整整数域迫使 literal reversed labels 的有限 word reciprocity。最后半裕度半径只保固定行族的一条边及反射逆一步。

独立增量是这组带证书的刚性与互易，不是单独宣称 shear 辛性、秩一矩阵乘法、凸上包络或范数裕度估计新颖。P27 `main.tex`:123–129、1650–1684 明确不作任意支撑分类、预设 word 实现、global reversor、entropy、普通/高阶 dynamical degree 或 all-iterate robustness。其末尾提及更大的 fan 系统是未证方向，不会自动把 P28 纳入 P27 的已经证明范围。

### F28：一个 word 对应一个含置换 map 的内生实现和有信息条件的 monodromy 解码

对每个 rooted primitive pair word、`ℓ≥3`，在 `2(ℓ+1)` 维构造一个固定自治 polynomial symplectomorphism `Π_P∘T_W∘S_V`；support 全正等总次数，系数任意非零。一般 fan iff 只分类 position-weight selectors，actual-degree lift 另要求精确首 carry chamber `0<m_0<A_{α_0}u_0`。incidence 支撑、moving ℓ-cycle 和 fixed star 给每个存在 competitor 的准确间隔 `K(H−1)`，单字母侧的唯一性是空条件，不虚构 gap。

实际更新是 `u_{n+1}=P u_n+1 c_n^T u_n`，故 residual 为 `P^n u_0`；selector word 与 diagonal quotient 的最小周期分别证明为 ℓ。`Q_s=C_{s−1}⋯C_0=P^s+1R_s^T`，`M=I+1R_ℓ^T`；给定 `M,P,λ,ℓ` 和 phase zero 只恢复 rooted digit-vector word，另加无标签 support dictionary 才恢复 exponent pairs，加 labelled dictionary 才恢复 literal labels。相关声明见 `main.tex`:123–195、1210–1250、1360–1407、1539–1544。

这不是多项式状态周期、单个全 word 通用 map、固定维度无界 ℓ、scalar decoder、minimal recurrence、inverse reciprocity 或 entropy 定理。P28 的 rank-one transport 可与 P27 的基础矩阵计算共享，但其非平凡循环和 decoder 不由 P27 的有限切换结论给出。

### F29：指定 Hénon 族的普通次数滤过上同调及单个完整周期概形测试

对象是特征零 `F=H_{k−1}⋯H_0`，`H_i=(p_i(x)−y,x)`、`d_i≥2`、`δ=∏d_i`。`K[x,y]/(F*−1)K[x,y]` 是向量空间商，不是商环。接受结果把 basis orbit coefficient sums 与保次数 primitive 联系起来：`deg g≤D` 且是余边界，则有 `deg f≤D`；有理 primitive 不增加解，primitive 模常数唯一。精确 associated-graded Hilbert series 是

`1+(1−t)^(−2)−[C_ρ(t)+2t^δ/(1−t)]/(1−t^(δ+1))`，

其中 `ρ` 来自有序 phase degrees 的 mixed-radix 重编码，固定坐标滤过下与系数无关。周期测试要求 `N=kn≥3`、`N>2L(g)`，在整个 `K[Fix(F^n)]` 中 `W_N(S_ng)=0` 当且仅当全局余边界；uniform 阈值以 `L_ph(D)` 定义，`D≥1` 才有测试代数长度 `≤δ^4D^4`。leading constant 4 的 sharpness 仅用于 scalar `d≥3` 的“此后每个 n 都有效”阈值，不是最短可挑选周期。

单因子的 `f∘H_p−f=R(x)` 精确迫使 `f=c(x−y)+c_0`、`R=c(p−2x)`，再用于所列四维保参数 lift：全有理固定域为 `C(a)` 或 `C(a,r−c(a)s)`，后者恰当 `V_a=cV_t`、等价 `V(t,a)=W(t+A(a))`；仍无有理 Poisson 对易独立积分对。不得把这一特定 Hénon/lift 结论扩大到所有辛映射。

Bousch 的 quadratic orbit basis/wrapping、其 coefficient-sum 线性代数及 Karr additive-extension 方法已在引言 111–149 明确扣除。未约化概形上的几何点全零只给 nilpotence，不给概形零；几何点测试的未证边界在 §8:322–332 保留。`D^4` 是代数长度而非最优复杂度，filtered Hilbert series 也不是任意共轭不变量。

### F30：原 qPI 两状态方向的完整首层理想与高层 cyclotomic first jets

对象保留 JR 原 `F_t(x,y)=(t/(x−y/s),sx/y)`、`t'=st`、原矩阵规范及 descending trace product。`α_{mp^a}=p^(−a)d_state I_{mp^a,s_a}` 的除法先在特征零作，微分固定时间/底环。`p∤m`、允许 unit-time jets、完整八中心曲面和四 terminal 不能删除。

引言三条完整定理的独立中心为：首层 `a=1`、完美剩余域时，在每条原完整光滑有限纤维所有点的完整 coefficient ideal 是 `(π_1,H̃)`，并有实际 Bockstein 和在 supersingular complete fibre 上到 `O_X^p` 的正确 connecting-class 身份；奇素数 `a≥2` 的形式与几何结论保留有限域/完整 time-jet 条件，只模 `π_a²`，其理想为 `(π_a²,H̃^σ,π_a H̃^(σ−1))`；特征二从 height 2 的 dual-number base 开始，形式比较与几何理想的完美/有限域条件分别保留，截断理想为 `(π_a²,j^(N−1)+π_a T̃j^(N−4),π_a j^(N−2))`。

height 2 的 `z^5` 是沿曲线参数 `w` 保留后的截断横向商，且 `π_2↦z^3/T`；不是原完整高层理想/完整长度定理。所有精确 order 和 `≥2` 的 lower bounds 在引言表及末尾 606–666 一致。三条定理、摘要与结尾均未宣称完整高层 thickness、singular-energy ideal、额外 ramified-state 精确阶或通用 crystalline/formal-group 比较。原模型、Hasse/Frobenius 迭代及成熟消元不是另外三个新机制。

### F31：同一原自治 qPI 完整实曲面的 sharp circlewise-centered 相关

固定任意 `T>0`，`F_T=(T/(x−y),x/y)`、`h=−x+y+x/y−T/x`、`Ω=dx∧dy/(xy)`；原观测为 `C_c^∞(U_T)`，保留两节点、同坏能量的持续圆和四 terminal。`Π` 是每个连通正则圆的均值投影，并不是整纤维均值或 `ker(U−I)` 投影。

写 `n=2m+r`；相位为原 `F²` 的 `σ`，下/中为 `2ρ`，上为实际 `F²` 回返相位。完整主定理给：`T∉{3/16,1}` 时 `m^(−1/2)A_r(m)+O(M20 m^(−3/2))`；`T=3/16` 加 `m^(−1)D_r(m)`；`T=1` 为 `m^(−2)B_r(m)+O(M20 m^(−3))`。驻圆和全部 Fourier 模的系数确切定义；`T=3/16` 的持续圆双侧驻相与消失圆端点是同能量的不同部分，不重复计同一圆。固定 saddle 邻域对每指定 `N` 有 `C^(N+2)` 控制的 `O(m^(−N))`，不是固定 C20 控制所有 N。

上区间 F 交换两圆，所以 odd coefficient 是实际交叉配对，不能只把 F² 结果改写时间指数。sharp 指合法实/复原观测的正归一化 limsup；不保证每对观测、每时刻、每条 parity 子列的正下界。P31 `02-…`:435–483、`07-…`:151–267 与完整结论一致。

独立 finding 是这个具体离散 map 的完整 sharp 相关、准确系数/余项和参数/奇偶转换。原曲面、PF/完整 twist 证明作为必要负载纳入，不再次分别计为新稿贡献；成熟 Fourier/驻相、跨 separatrix 和 elliptic original-jet 机制在引言 55–89 已归属。不是未投影混合、单圆混合、CLT、统一 T 转换极限或新的普适阻尼原理。

## 4. 可用共享输入 / 不得主张内容矩阵

| 出口 | 可用共享输入及实际条件 | 不得作为下游已得结论 |
|---|---|---|
| P27 | 分离 gradient shear 的辛性、`A_α=1α^T−I`、`B_βA_α=I+1c^T` 及严格 leading-degree/carry 检查思路；完整结论只能带原证书使用 | 不能以其有限切换界限制含非平凡 P 的系统；不能把有限词反射升格 global reversor；不能给 P28 自动赋 inverse reciprocity |
| P28 | 固定 word 的 incidence supports、normal-fan selector cone、精确 carry lift、marked monodromy 及字典条件；均是对应维数/map/seed 数据 | 不能以 digit 解码推出 P29 periodic-scheme cohomology；不能把 selector period 当实际周期或 spectral eigenvalues；不得从 scalar annihilator 解码 word |
| P29 | 对其明确 Hénon recurrence 的 orbit basis、degree filtration、scheme no-alias 和 additive-extension 判据；通用 telescoping 只给必要周期和式 | 不能把 Hénon 的无有理积分或无周期 affine curve 移植到 qPI；不能在 qPI 假定 `δ^n` basis/length、`L_ph(D)` 或 degree-preserving primitive；不能抹去非约化性 |
| P30 → P31 | 原八中心 chart、polar divisor、非退化二形式、primitive pencil、完整连通有限纤维，准确特化 `q=s=1, τ=t=T, r=1`；P31 自己验证实曲线识别/+P、组件、测度及全点 lift | P30 的 arithmetic Bockstein/Hasse/critical ideal 不给实 frequency 或 correlation；其 terminal 泛点 pole 论证不能单独充当全点 lift；不得把未成篇后续 full height-two ideal 反灌接受 V4 |
| P31 | 同一原实 qPI 的 circlewise coarea/projection、F² 频率和原 F parity 接口，固定 T/紧能窗/原 norm 的精确相关渐近 | 不推出 positive-characteristic Hasse/完整 thickness、周期阶计数或 Riemann 谱；不消除 P30 finite smooth-fibre 假设；不赋 P29 的多项式过滤器新的 qPI 有效性 |

P30 README 中另列的 post-acceptance height-two 全理想及 cuspidal 计算已清楚标成后续数学 continuation，不修改接受 PDF/锁，也不是接受 P31 的中心。它们不计入本报告五个 finding，更不能拼进 P30 的最好结论制造“所有层完整厚度”。

## 5. 十对论文的非碰撞判断

这里的“非碰撞”仅为组合内主结果可区分，不是全球先例排除或新意分数。

| 论文对 | 实际对照与风险处置 | 判定 |
|---|---|---|
| 27 / 28 | P27 `F=T_W S_V` 给 `u'=u+δ1`，其商 residual 固定；P28 `F=Π_P T_W S_V` 给 residual `P^n u_0`。P28 每 word 一个 map、维数随 ℓ，P27 只是既有严格 branch 的有限切换/互易。共有正支撑矩阵与 strict-carry 方法不重复计为两个独立新机制 | 非碰撞；无“有限 vs 周期”矛盾 |
| 27 / 29 | P27 是高维正 Newton support 的 weighted leading-degree 证书；P29 是平面 Hénon 多项式 additive cohomology 的 ordinary degree filtration。相似的 leading-term/no-cancellation 论证不等于同一 obstruction space 或 Hilbert 结果 | 非碰撞；无直接科学依赖 |
| 27 / 30 | P27 的 characteristic-zero support exponents/certificates 与 P30 cyclotomic integral division、完整 qPI 曲面及两方向 coefficient ideal 不同；“正”支撑条件不是 arithmetic 普通/超奇异条件 | 非碰撞；跨用只能先建新接口 |
| 27 / 31 | P27 weighted-degree growth/局部裕度不是 qPI 能量 ensemble 的相关；P31 曲面观测、条件期望及 analytic time phase 不能由 P27 affine tail 得到 | 非碰撞；不拼成 degree→mixing 定理 |
| 28 / 29 | P28 word/dictionary/monodromy 的 finite encoding 与 P29 integer orbit basis wrapping 都有组合语言，但前者解码 support labels，后者检验 polynomial coboundaries；“word 周期”也不是完整固定点概形测试 | 非碰撞；不把两种周期混同 |
| 28 / 30 | P28 ordered matrix product 是选取的 degree transport；P30 matrix trace 是 JR 原 Lax/invariant construction。相同“monodromy/trace”词汇不把二者识别为同一算子或同一 invariant | 非碰撞；无矩阵对象偷换 |
| 28 / 31 | P28 diagonal quotient 的 ℓ-period 与 P31 椭圆圆周 rotation phase/两圆 return 不同；前者明确非 polynomial-state periodic，后者未主张从 selector word 推相关 | 非碰撞；无周期/频率重复计功 |
| 29 / 30 | P29 的有理固定域 K 及无周期 affine curve 只属特征零 Hénon `d_i≥2`；P30 qPI 正好带非恒定 invariant 和 complete genus-one fibres，其模型不是这一 Hénon recurrence。二者都保留 scheme 信息，但这不是把 P29 finite no-alias 搬到 qPI 的充分桥 | 非碰撞；有理可积/不可积表述不矛盾 |
| 29 / 31 | P29 的 polynomial cohomology/periodic sums 与 P31 的 `L²` circlewise-centered `C_c^∞` correlations 是不同系统与函数类；P29 rational Liouville-pair 排除不限制 P31 可积 qPI 的相混合，P31 也不证明 P29 几何点-only 检测 | 非碰撞；不误用一般 Livšic/Koopman 术语 |
| 30 / 31 | 只共享同一原曲面/pencil 的 `s=1` 特化；P30 新中心是 p-adic critical ideal/first jets，P31 新中心是 full real sharp correlations。P31 不消费 P30 的 arithmetic 主定理或从 P30 未证高阶厚度获得衰减 | 非碰撞；共享几何归属与增量均清楚 |

### 5.1 27/28：为何不能用一个结论否定另一个

P27 主定理 finite-transience 依赖实际 `u_n=u_0+t_n1`，所以 equal-total score differences 固定，其变更统计再由 total-envelope 单调性控制；`d_V=d_W=1` 时在该前提下无非平凡 pair switch。P28 的同总次数并未让 residual 固定：`P≠I` 随每一步移动 spike，同一 support pair 比较沿 `P^n u_0` 进行。P27 去掉 P，P28 固定 P 后构造支持，这两个量词顺序和更新法不同。无需宣称 P28 反驳 P27，也无需把 P27 人为扩大成已有 every-word construction。

### 5.2 29/30：为何 scheme 语言不是可迁移的 theorem

P29 中关键充足性依赖 `p_i(X_i)=X_{i−1}+X_{i+1}` 的 bounded-exponent basis、macro shift 和 unique-long-gap no-alias；P30 的有限临界代数、完整 elliptic fibres 与 Hasse ideal 没有提供这一 basis 或 phase degree cost。一般 telescoping 只给“余边界的周期和式为零”，不提供 P29 特有的反向蕴含。现接受稿没有把该短一般事实冒充 qPI 有效 cohomology 定理；跨族假设若以后提出，应登记为 `ROUND2_CLUE`，当前不创建或执行新路线。

### 5.3 30/31：来源责任、模型特化和 M1

P30 `02-surface-pencil.tex`:14–20 的 terminal charts 特化 `q=1,τ=T`，与 P31 `02-real-surface-main-theorem.tex`:139–144 的四图一致；二形式系数依次为 `−1/(1+ab),1/(T+ab),−1/(T+ab),−1/(1+ab)`。P30 的 `I_{1,1}=J_1(t)` 与 P31 的 h 符号/原 F 式一致。这里只核接口，不重新审整个原谱 Jacobian 证明。

P30 §2:189–215 以 terminal generic points 到 torus、配合 normality 排除 poles，这足够支持该处极除子证明，却不能单凭这段概括为“每个 terminal 点的 map isomorphism”。P31 V3 §2:57–63 已限定 P30 的 geometric interface，并明说 JR §2.1 是 finite-field 描述；§2:65–105 自己给前三条局部式、第四线 `(0,0)`、torus diagonal 和分层覆盖，随后用 symplectic/étale/open immersion 论证全点 lift。它没有把有限域来源替代原实证明。

因此本轮所见现稿归属与 `COMPLETE_SOURCE_DISPOSITION_V2_20260913.md` 的 “M1 CLOSED” 接续一致；不重新开启同一已关闭 proof obligation。P31 `references.bib`:55–60 明确 P30 是 `unpublished local manuscript, version 4`，未伪造正式出版身份；JR 则明确用固定 arXiv v2。P30 书目写期刊记录并指定同一 author v2，P31 选固定预印本记录，两者不构成不同原模型或矛盾责任。

## 6. 重复计功、循环、术语与未知边界

1. **只计五个中心，不把所有引理相加。** P27/P28 的 shear 辛性、严格最大单项及 rank-one 运算属于共享基础；P29 basis/shift 的已有源和 Karr 明确归属；P30 模型、Hasse 迭代、形式群背景明确扣除；P31 原曲面、旧 PF/twist、FHR/HRSS 和经典驻相是必要输入。正文为自足而重证一个成熟引理不自动构成重复发表，也不自动产生缺引用阻断。
2. **组内显式依赖是单向。** 五份 bibliography 全文与所读主科学段显示，唯一已采用的组内书目依赖为 P31 的 `QPI30Local2026`。P30 没有反引 P31，P27–29 未以这些后篇作为证明前提。现有共享依赖图是外部 JR/成熟工具加上 `P30 基础几何 → P31`，不是 `P30 算术主定理 ↔ P31 相关主定理` 的闭环。对未重读的证明段不额外授完整依赖形式验证。
3. **符号必须连同对象读。** P27/P28 的 α/β 是 exponent labels；P30 α 是整除 state differential，β 也可表示 Bockstein；P31 α/β 等 analytic 局部量不能据同名字迁移。P29 的 D 是 ordinary degree cutoff，P30 的 D 是 polar divisor。P31 主文已把 period 统一为 L、Ω 留给 symplectic form。这些局部定义无冲突，无需跨五篇强行一套全局符号。
4. **两种 trace 和多种 period 不合并。** P28 degree monodromy characteristic polynomial 不等于 P30 spectral Jacobian；P29 orbit sum 是 scheme-ring 元素而不是 scalar trace，P31 是 ensemble correlation。selector period、macro fixed-point scheme、cyclotomic height、circle-return period、时间 n 各有原定义，五文没有将它们拼成 Riemann determinant 或 Hilbert–Pólya 结论。
5. **已有未知仍未知。** 本席未发起新的文献检索，未用组合内独立性补分或宣称全球首次。P27/P28 原定日期的 bounded positioning 不升级 exhaustive priority；P30 接受记录明确 `CORRECTION_IMPACT_UNKNOWN` 的 Vlasenko correction-content 缺口保持，且其比较不是必要 theorem black box；P31 既有缺读来源范围也不因本次组内审计得到补全。此处“无组内碰撞”不能替代任一外部全文包含检验。
6. **科学与产物边界。** 本席不改变五篇本地接受，不复跑编译、不重新计算页数。P30 的 22–40 页例外只属 P30；P31 已接受版仍原 22–30 页。P27 preserved builder FAIL 不因科学矩阵 PASS 改写成 clean build。所有这些成品事实仅沿用接受记录，独立交付席负责当前所需 artifact consistency。

## 7. 必修项与已披露书目勘误

### 必修项

`required_fixes: []`。没有发现本次跨论文科学边界任务的真实阻断项，因此不要求修改接受源、科学合同、证明、页数或重新产物验收。

### E1：P27 三条同文献作者字段笔误（非阻断；附属勘误已提供）

五份书目对照中，P27/P28 对同一 DOI 或同一 arXiv 标识的作者名写法有三处不能仅解释为正常 full-name/initial 缩写：

| 对应来源 | P27 实际字段 | P28 实际字段 |
|---|---|---|
| `10.1112/blms/bdm112` | `references.bib`:85，`Janeczko, J.` | `references.bib`:2，`Stanisław Janeczko` |
| `10.1017/S0143385707000168` | `references.bib`:26，`Propp, T.` | `references.bib`:58，`James Propp` |
| `arXiv:2509.14584` | `references.bib`:162，`Shao, Y. and Sun, Y.` | `references.bib`:47，`Enbo Shao and Xiaosong Sun` |

本席最初由两份实际书目对照发现差异；主控随后作有界一手元数据核验，确认这三处是 P27 author 字段笔误，已写成 [BIBLIOGRAPHIC_ERRATA_V1_20260913.md](/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/BIBLIOGRAPHIC_ERRATA_V1_20260913.md)。该件为 36行、3705 bytes，SHA-256 `065896f56ba8d41135fe99ebc04a3a2428f5730ac13be9b8610badd65062cf1f`；本席随后 FULL 亲读。它给出应读作者 Boris Hasselblatt/James Propp、Stanisław Janeczko/Zbigniew Jelonek、Enbo Shao/Xiaosong Sun，与 P28 实际条目一致。外部核验分别使用作者 arXiv 身份页及 Janeczko 学校所存首页/本人目录，其实际读取责任与范围由主控在勘误中披露；本席没有重新浏览或声称亲读这些外部页面。

独立判断：本席已读 P27 §2 的三个实际引用语境，均属相邻研究定位而非主定理必要外部黑箱；相同 DOI/arXiv 与题名仍明确指向同一文献对象。这三处作者名错误是真实问题，不能称冻结 PDF 无任何瑕疵，但不改变五文的科学定理或共享责任。附属勘误的身份和权限边界可以接受：当前交付应明确为 P27 接受 PDF 连同本勘误，旧 PDF 字母未被偷偷更改、不虚称 PDF 已嵌入修正，不重编译、不回写旧接受/锁/失败。因此本次科学 required fixes 仍为空，已有书目问题以实际 companion errata 披露处置；并非靠省略错误取得 PASS。

可选未来建议仅为：若以后另有适用的后继制作授权，再把已经核准的三条 author 修正纳入明确 successor。此建议不自动启动本轮任何新构建。

## 8. 最终交接

本报告完成五个独立 finding、可用共享输入/反主张矩阵和全部十对非碰撞核对。当前科学结论限于实际阅读的接受版；不新评分、不重查新、不重审未变整条证明、不 CAS/数值/阶数扫描，不产生上传、投稿、托管、push、发信或付费资源效力。主控应把本报告与另一席的交付身份结论分别读取、再作一次总处置，并随 P27 提供已核准的附属书目勘误；不要将 E1 包装成新增科学合同或重新抽票理由。

此文件经本席最终自查后以行数、字节数、SHA-256 向主控交付；该身份在外部回执中报告，避免把自哈希写入自身。交付后停止编辑。
