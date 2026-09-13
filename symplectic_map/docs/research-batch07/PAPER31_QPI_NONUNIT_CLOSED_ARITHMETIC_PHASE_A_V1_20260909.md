# Paper31：闭合非单位时间算术方向的 Phase A V1

日期：2026-09-09 UTC；主控 `/root`。`NOVELTY_PHASE_A / NEW_MATHEMATICAL_DELTA / NO_ADMISSION`。
使用 novelty-check 的逐核心主张提取；这是同族实际新结果后的有界增量查新，不覆盖原五方向的历史分数。

## 1. 对象与当前证明状态

固定 $q=1,R=\mathbb Z[\tau]$，原八截面 qPI 曲面 $S/R$、反典范层 $\mathscr L$、原实际 $M_n=H^1(S,\mathscr L^n)$。
保持所有 $n\ge0$ 与所有整数素数；$\tau=0$ 为整族几何退化，不是可逆动力的延拓。
原 [D05][BASE] 的真实相邻扩张已独立接受；新 [G] 原留数格识别和 [D] 行列式工具已作者终态，独查进行中。
[C] 的整数消费者在 H1–H3 下证明完整；[A] 已逐一匹配前提并另证全次数数字递推，等待独立合并核查。
因此本件抽取的是**实际已经写出完整证明的新增主张**，不是把此前 I05 未证目标提前授予高分；数学独查与查新仍分开。

## 2. 三个技术核心

### C1：原受限四簇的全次数整数扩张与可恢复连接

原 $s_0=xy$ 给整个 $M_n$ 的真实短正合列
$$0\to M_n\to M_{n+1}\to R\oplus2\bigoplus_{j=1}^{n}R/(\tau^j)\to0.$$
每个商循环分量的完整 Ext 类由原旧 jet 的几何级数多项式给出；四边整数插值和精确除法将任意旧类还原，次数严格下降。
所有 $n\ge1$ 的整列不分裂；这不是仅给域上 Smith 表或无闭合规则的另一张同规模矩阵。
指定 $P_m$ 拉回／推出只作为消费者，不冒称原 $M_{n+1}$ 直和块。

需要查清：一般 fat-point／近点簇上同调、Koszul／Rees 或完整 Pascal 整数等价是否已经给出同一原受限源的连接。
必须扣除标准长正合列、Ext、四边插值、几何级数及二项差分本身。

### C2：原自由余核的留数识别、实际整数格与完整缺陷

由四个原共同零点及反典范标架定义 $\rho_n$，先证明 $\rho_nJ_n=0$，再由原秩／满射证明它识别实际 $M_n[1/\tau]$。
原坏图的整数形式坐标同时把两截面化为 $F=U(\tau+V),G=V$，Jacobian 单位在全部 fat jets 上保留。
由此真正得到
$$\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a},\qquad
I_{n,a}=\left(\binom{n-1-b}{a}\tau^b:0\le b\le n-1-a\right).$$
原 $s_0$ 在归一化理想坐标中为 $\tau$ 倍右移；各 $I_{n,a}^{**}=R$，故原 $E_n=L_n^{**}/L_n=\bigoplus R/I_{n,a}$。
该式控制全部次数的实际整数格，不仅是关联分次、任意选择的影子或某个域上的余核秩。

需要查清：多变量留数／toric residue／Cayley–Bacharach、整数 principal parts／Taylor／jet bundles、算术曲面的碰撞截面或插值格理论，是否直接涵盖该完整格与连接。
不能仅因检索缺少 qPI 专名就判断新颖；将所算格忘掉原几何后，它是否只是一个标准 Pascal／jet 对象是最强包含压力。
必须扣除紧流形留数定理、形式逆函数定理、负二项式展开、UFD 双对偶等标准机制。

### C3：同一原上同调的全次数 Fitting、素数跳跃与消失规律

同对象合取得到全局整数理想
$$\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_a I_{n,a},\qquad B_n=\sum_{j=1}^{n-1}j^2.$$
特征 $p$ 的原扭子长度是 $B_n+D_n(p)$，其中 $D_n(p)$ 是 [A] 明确定义的数字差总和；不是底层纤维维数。
每个 $p$ 第一次长度增加恰在 $n=p+1$，增量 $p-1$，原局部 Fitting 为 $\tau^{B_{p+1}}(p,\tau)^{p-1}$。
全部后续次数满足无缺陷判据 $n/p^{v_p(n)}<p$ 及 [A] 的终止数字递推。
完整原模的强直和 (P)、全部 Smith 指数及高于秩的其他 Fitting 均不在主张中。

需要查清：主部丛在正特征的分裂／失败、二项系数行的全非零判据、受限 Pascal 子式理想、Fitting 与饱和格的一般比较，是否让整个新发现成为已有结果的短推论。
一般互补 Plücker 子式、DVR 长度及 Lucas／数字二项式必须扣除；不能将首现、总和和消失判据重复计三种独立方法。

## 3. 组合基线与不得重投的内容

原全次数实际 jet 复形、零时间固定部／维数、二阶标量分解、三阶混合块和三阶非主 Fitting 已接受，全部从新意中扣除。
固定四阶的真块化也只作为验证锚点，不能与新全次数式重复计功或用来凑正文。
旧 I05 6.5／CAUTION 及“不应只换矩阵／Smith表”的反对意见保持，见[原独立C/D][OLDCD]。
新差额是 C1 的实际全部连接加 C2 的闭合原格及 C3 的全次数原消费者，不是旧变基反例或又一个素数样本。
P18 的一般 Fitting／基变换工具、P29 数字选择工具及 P30 已接受迹／Hasse内容按[组合基线][PORT]扣除。
不从其他族加入最好的结论，也不把已接受但未独立成文的旧材料重新标成新问题。

## 4. 本轮 Phase B 分工与证据规则

来源任务针对这三个核心，不复查全部十项发现。
每核心至少三个不同技术表达式，含2024–2026及最近六个月（2026-03-09至09-09）arXiv覆盖；尝试Scholar／S2公开入口并如实保留失败。
纯代数几何／数论题目不机械转成ICLR／NeurIPS／ICML实验检索；只在确有相关数学来源时纳入。
所有来源区分摘要／元数据、相关段落、实际定理／证明、全文；以一手研究论文或官方作者机构版本为准。
对最近文献和既有强先例分别检查，不能只查最近论文而遗漏经典包含。

- 主控拥有 C1/C3 的来源报告 `PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C1_C3_V1_20260909.md`。
- 原格作者席拥有 C2 的来源报告 `PAPER31_QPI_NONUNIT_CLOSED_SOURCES_C2_V1_20260909.md`，身份明确为来源搜集，不能为自己的 G 投独立新意票。
- 之后另行交非作者 C/D 合并新意／价值与反对意见；未配置指定GPT-5.4端点时如实用可用独立Codex席替代，不称跨模型验证。

本阶段不设预期分数，不为了达到7.5而重新包装主张；若强来源直接包含，则按准确差额降级或停止。
没有GPU、付费资源、外部上传或项目写稿测页；P31仍未立项且正文22–30页要求不变。

[BASE]: PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[D]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[C]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[A]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[OLDCD]: PAPER31_QPI_NOVELTY_CD_I05_I09_V1_20260909.md
[PORT]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
