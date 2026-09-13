# Paper31 Q2：完整 sharp 相关衰减的数学接受与候选接续处置 V1

日期标签：2026-09-13。主控实际 clock 已读2026-09-13 00:05:38、00:14:06 UTC，与本轮日期一致。
处置者：/root。状态：MATH_ACCEPTED / COMPLETE_Q2_CANDIDATE_BRIEF_FROZEN / NO_FORMAL_ADMISSION。
route_applicability: NOT_APPLICABLE。纯原确定性辛映射分析，不是Route A/B或PDF验收。

## 1. 本轮实际完成与冻结身份

从[前处置][PD]的最早缺口接续，使用proof-writer完成混合节点、椭圆jet和全局合成三件完整证明。
两位fresh非作者分别对三件全部actual数学独查；research-review指定GPT-5.4端点不可用，
使用两个不同的secondary Codex xhigh，未冒称跨模型或外部真人审查。
两人未互读、未校准、未修改作者稿，各自完整审查后给PROVABLE_AS_STATED且required fixes为空。
另有fresh非证明作者按novelty-check执行定向组合内增量检查，不授数学或正式四门票。

主控FULL读回以下七件真实终态；首轮合并读取两审查报告的总输出截断了B开头，
随后单独FULL重读B全部324行，不以截断输出冒称完整。

| 件 | 行数／字节 | SHA-256 |
|---|---|---|
| [K] 节点混合导数与符号 | 292／15637 | f01797fdfaf8bcff40881cac199ff9e06fc1484bc578a2fad2f3c599b129cb79 |
| [E] 椭圆jet与端点 | 377／17873 | adaa676ad6fd049d65f2137eb52ee158a98604a652bcd7505c62f4ddf9aebfe6 |
| [G] 完整全局合成 | 358／18193 | 48fff63450138a788e4442c7b94c90e454eeebee2c1960afd895d15577c0cf6f |
| [RA] fresh实际数学独查A | 241／18684 | 7ed1927c0528cea7a1237ecafe987d7def93b066097dc1507b488dc31e0cc8e3 |
| [RB] fresh实际数学独查B | 324／20553 | 9b42debd1557fefe2986117be4a2aad492254f05481a08d7f218ca813f7707fd |
| [PORT] 组合内增量 | 157／14966 | be9b8f83dd369112963fbe8ea74326cf4089a11a87abf63adde9dde5919d224b |
| [BRIEF] 完整候选brief与证明图 | 160／12249 | 2fc821378e667a068240518489a16f64e6c39661c277c530d204dede9940a1e9 |

三证明共1,027行；两数学报告共565行。K/E作者各有只读证明协作者，他们不是这里的fresh审查席。
RA/RB均FULL读K/E/G及PD/M/N/TW/B；主控本轮也FULL读取这些直接数学输入。
旧[M]/[N]的接受由[PD]继续有效，不因作者稿冻结头中的旧pending重开。
新K/E/G、两审查和PORT的历史pending同样由本件后继处置覆盖，不回写冻结稿。

## 2. 数学接受：原命题未弱化

固定任意 $T>0$，在原完整 $U$ 上取原 $f,g\in C_c^\infty(U)$，
$\mu=|\Omega|$、$\Pi$为逐连通圆条件期望，

$$C_n(f,g)=\langle(f-\Pi f)\circ F_T^n,g-\Pi g\rangle.$$

观测允许跨saddle、椭圆中心、临界能级的持续圆和四条terminal；
没有变成有限Fourier、删节点能窗或常数时间流。
主控接受[G]完整声明，具体以 $n=2m+r$、$r=0,1$ 写为

| 固定参数 | 已接受准确渐近 | 原范数控制 |
|---|---|---|
| $T\notin\{3/16,1\}$ | $m^{-1/2}\mathcal A_r(m)+O(m^{-3/2})$ | $C^{20}$范数乘积 |
| $T=3/16$ | $m^{-1/2}\mathcal A_r(m)+m^{-1}\mathcal D_r(m)+O(m^{-3/2})$ | 同上 |
| $T=1$ | $m^{-2}\mathcal B_r(m)+O(m^{-3})$ | 同上 |

系数按[G]的(1.2)—(1.5)，由实际正时间、完整周期、原Fourier与原一阶jet给出。
全部级数及余项绝对求和。每个固定参数均有原光滑实／复观测的非零归一化limsup；
因此全局 $n^{-1/2}$（$T\ne1$）与 $n^{-2}$（$T=1$）不能在此观测类中统一改善。
这不意味着每对观测、每个时刻都有正下界。$T=1$ 的泛型非消失用原一阶jet对的开稠密条件说明，
主jet消失至少给更快的 $O(m^{-3})$；未申报全部高阶jet的最优分类。
所有常数允许依赖固定参数和紧能窗；不新增参数极限一致性。

## 3. 闭合最早缺口的实际证据

此处 $e=h-h_+$、$\ell=1+\log(1/|e|)$，限制在固定的充分小单侧节点能带。
**节点坐标。** [K]以 $u=\log|p|$ 把固定 $u$ 的Euler微分化为 $q\partial_q$，
穿箱时间的全部移动端点项有显式递推；归一化时间隐函数的分母有正下界。
正则弧、大小Morse箱和周期基点用同一轨道映射的开重叠匹配，不微分移动特征函数。
全圆得到

$$|\partial_e^a\partial_\theta^b(f\circ z)|
\le C\|f\|_{C^{a+b}}|e|^{-a}\ell^{a+b},\qquad
|\partial_e^a\widehat f_k|\le C\|f\|_{C^{a+s}}|e|^{-a}\ell^{a+s}|k|^{-s}.$$

**原离散相位与反复积分。** 同一个 $\alpha=\tau/L$ 给
$q=1/\alpha'=eL^2/R$、$R(0)>0$，所以
$\partial_e^a q=O(|e|^{1-a}\ell^2)$。
转置 $\mathcal Ta=-\partial_e(qa)$ 保持能量符号类；$\mathcal T^Na$仅有可积对数增长，
而每一级真正边界 $q\mathcal T^ja=O(e\ell^M)\to0$。
全模求和是 $\sum_{k\ne0}|k|^{-N-2}$，不是固定模态论证。
对任何指定整数 $N\ge1$，完整saddle截断相关为 $O(m^{-N})$，原 $C^{N+2}$ 足够；
不将任意 $N$ 的这一范数误读为统一固定 $C^{20}$。

**椭圆端点。** [E]明确选 $\Omega=-b\,dp\wedge dq$ 使角度正向，
利用零均值周期原函数构造 $z(-r,\theta)=z(r,\theta+1/2)$。
同模乘积为偶函数，真实光滑下推为
$L\widehat f_k\overline{\widehat g_k}=\varepsilon A_k+\varepsilon^2R_k$，
$A_k$仅在 $k=\pm1$ 非零，余项全k及有限能量导数由原有限范数控制。
非退化端点系数是 $-A_k/(2\pi k\beta)^2$；二次端点系数是 $iA_k/(2\pi k\gamma)$。
两审查均独立核了能量反向及 $F^2$ 的因子2，没有遗漏或误号。

**完整拼合。** [G]直接证明带 $C^4$ 余项的二次驻相并全Fourier求和。
$T=3/16$ 的持续圆跨 $h_-=-2$ 作一次双侧驻相；同能量的小圆另给 $m^{-1}$ 次项。
上区间用 $z_1=Fz_0$ 写出真实换圆交叉振幅；奇数步归约不损失随时间增长的原范数。
原光滑下界由正则圆管bump／中心线性jet构造，不把n=0薄层尖锐性当成时间最优性。

## 4. 本地增量、来源与容量仍须严格分开

[PORT]定向实读P27–30的当前接受源，确认新Q2不是它们已读主断言的同义改写。
P27–29的权重、循环字及多项式周期概形测试不提供当前原光滑相关渐近；
P30原曲面、辛形式、proper pencil、实际谱曲线及旧twist全分类必须全部扣除。
它的PARTIAL/FULL边界保留，不称P1–30全文无碰撞证明，也不称全球新意PASS。

本轮未重跑[S]/[CD]的强目标外部检索；新证明正是其已核的同一强量词，不是新来源阴性证据。
FHR跨separatrix技术、标准驻相及原jet端点机制的压力仍在；新定理成立不自动创造一般新方法。
旧条件新意7.6、价值8.2、容量MID、STOP定位建议，以及[PD]的量词澄清均完整保留，不校准或重抽。
两份actual数学接受也不是正式两席分别全四门PASS。

[BRIEF]已形成唯一中心、完整主断言、来源扣除和必要证明图。
容量须同时计入新分析与旧未成篇twist链的真实必要正文，不把内部接受记录冒称公开已发表定理；
已可合法引用的标准理论与P30成果则不为填页重复。必要证明不能外移来满足页窗。
因此容量可能不足22，也可能因完整负担超过30；本轮未给任一方向的FAIL或PASS。
旧组合报告“不重抄计新”的话只限制重复计功，不解除完整正文证明约束。

## 5. 下一项：冻结共同全包后作正式完整双席

下一项不再补本次已经接受的混合导数或端点证明，也不转回Q3或重评同一短引理。
按[BRIEF] §3—4，把以下内容汇成双方相同的精确FULL／PARTIAL／一手来源清单并绑定终态身份：
新M/N/K/E/G、必要旧GEO/B/MID/UP/INF/TW/PF链、原完整模型相关旧段、两actual报告、
两处置、S/CD来源风险、PORT与brief。不机械加载未消费的厚度祖先或旧构建树。
公开来源沿现有已成功范围核读；已拒绝访问的入口不绕过，缺读如实保留。

随后由两个fresh非作者各自完整评价四门：新意≥7.5、独立价值≥7.5、证明信心≥9、可信22–30页容量PASS。
必须两席各自完整合取通过；不将本次数学A/B拼成正式票，不平均、挑最好项或同包反复换席。
若完整正式评估失败，保存实际失败并依既定门槛处置；不得靠改参数、删原观测类或增小推论救分。
若通过，才接source/publication locks、正文、确定性构建及独立稿件/PDF与终局验收。
这都是既定goal内接续，不需要再询问已获授权的本地动作。

## 6. 产物、执行边界与goal

本轮只增K/E/G/RA/RB/PORT/BRIEF及本处置，更新两个当前入口；没有改旧接受论文或冻结失败记录。
一次主控及一次组合代理路径定位列出旧build文件名后都停止该路线；未读内容、未哈希旧构建产物或重验旧树。
此后均使用明确原路径；没有新数值、CAS、参数／阶数枚举、N≥10扫描或实验。
未创建Paper31项目、source/publication locks、稿件、PDF或试排根；无任何外部写入或付费操作。
Paper31原22–30页、旧所有FAIL/HOLD/STOP及P27–30接受保持。
本轮是完整强Q2数学PROGRESS；批次仍4/5，goal active，Paper31及第五篇后的跨论文统一审计未完成。

[PD]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[K]: PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[G]: PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md
[RA]: PAPER31_QPI_Q2_DECAY_ACTUAL_REVIEW_A_V1_20260913.md
[RB]: PAPER31_QPI_Q2_DECAY_ACTUAL_REVIEW_B_V1_20260913.md
[PORT]: PAPER31_QPI_Q2_PORTFOLIO_DELTA_V1_20260913.md
[BRIEF]: PAPER31_QPI_Q2_COMPLETE_CANDIDATE_BRIEF_V1_20260913.md
[S]: PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md
[CD]: PAPER31_QPI_Q2_STRONG_CENTER_PREFLIGHT_CD_V1_20260913.md
