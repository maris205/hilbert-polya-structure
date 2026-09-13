# Paper30 内部算术定理包：最小作者证明依赖与去重模块图

日期：2026-09-08。性质：有界本地依赖清点，不是新证明、数学重审、篇幅估计、候选票或 Route 评价。
文件所有权：本件为唯一新增文件；所有作者稿、冻结原稿、独审及处置记录均保持不变。

## 1. 固定对象与清点结论

本件按[对象简报](PAPER30_TWIST_INTERNAL_ARITHMETIC_OBJECT_BRIEF_20260908.md)及
[完整负结构接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_COMPLETE_STRUCTURE_DISPOSITION_20260908.md)
所确定的接受范围清点。固定所有素数 \(p\ge5\)、\(a\ge2\)，
\(m=(p-1)/2\)、\(M=p^{a-1}m\)、\(D=3m+1=p+m\)、\(\chi=(-1)^{m+1}\)。
同一实际分支的 \(h=2-\zeta-\zeta^{-1}\)、\(\rho=-h\)、\(L=\rho\lambda\)
及 SUM action 规范不变。对象是前三个内部 forcing \(\mathcal B_1,\mathcal B_2,\mathcal B_3\)，
不是完整周期 \(p^a\) 的最终 forcing。

中心闭合目标为
\[
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\qquad
\operatorname{NP}(S):(0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m),
\]
以及 \(\mathcal B_1,\mathcal B_2,\mathcal B_3\) 两两互素。正因子的次数 \(m\)、温和循环分裂，
负因子的次数 \(p\)、不可约及单根域野全分歧，可随同一闭合证明保留。
不纳入负因子的完整分裂域、负根全部间距、第二 forcing 的完整 Newton 图，
也不纳入 \(p\ge7\) 的下一阶根平移作为中心义务。

清点结果是下面的 **10 个非重复论证模块**。模块数不是定理数、创新数或篇幅代理量。
可以按这些模块重排成一条向前引用的作者证明包，不需要新增数学前提；
这句话以保留所列原论证，或把已接受 lemma 连同完整量词、工作环、误差精度准确导入为前提。
它不表示仅拼接最后几份结论稿就自动成为自含论文，也没有证明存在更短的替代论证。

## 2. 十个模块及准确作者来源

下表的 A 编号在第 3 节给出准确文件路径。处置和独审只确定接受边界，不充当作者证明。

| 模块 | 必须自含的具体义务／可直接导入的接受 lemma | 最小必要作者段落 | 向前依赖及引用闭合风险 |
| --- | --- | --- | --- |
| M1 实际对象、圆分局部环与统一记号 | 从正 kick、SUM action、零均值消元固定对角递推；解释 \(\mathcal B_k=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V}=2d_{kp}V_{kp}\)。固定 \(K^+,\mathcal O^+\)、剩余域 \(\mathbb F_p\)、\(v_h(p)=M\)、实际传播子层级；后文只取 \(n<3p<p^a\)。 | A01 Notation、Proof Steps 1–2；A02 Notation、Step 1；A07 Step 9 的 \(d_{3p}\) 倍频身份只需保留一次。 | 无后置数学依赖。不能把内部 \(p,2p,3p\) 模态当作周期共振而置零；不能把 \(\mathbb Z_p[\zeta]/(h)\) 当作已指定实局部环的剩余域。旧全分母根诊断不属于此模块。 |
| M2 第一内部 forcing 的有限整块与反射缺陷 | 低块形式整性；非驻值有限 action 的准确 Euler 缺陷；首个反射层和有限平方传播子配对和；真正形式身份 \(\mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R+pT\)。再导出实际 \(h^{-m}\mathcal B_1\) 整、剩余 \(\chi(2-L^m)\)，及第一 forcing 全部 \(L\) 根赋值为零。 | A02 Steps 2–6，尤其 (11)–(15)。Step 4 的有限求和是后续形式微分所需原证明，不能只留下实际赋值结论。 | M1。准确形式身份是 A02 式 (15)，不是只含实际结论的 Claim 式 (2)；后来的 Ward 稿必须引用前者。A02 Step 7 的详细 Frobenius 因子次数不是当前两边 Newton 加互素目标所必需。 |
| M3 两条阶乘带、实际块桥与第二 forcing | 在有限次数中先清一个或两个 \(p\)，保留全部实际内部初值及旧高块平方；证明 \(Y^{\rm act}=pV_{p+\bullet}\)、\(Z^{\rm act}=p^2V_{2p+\bullet}\) 整及初值高度；得到准确形式桥、耦合单位模型和实际比较误差。第二端点保留非驻值 action、移位响应及 \((2-L^m)+L^m=2\)，给 \(h^{-2m}p\mathcal B_2\) 整且剩余为 2，以及 \(\gcd(\mathcal B_1,\mathcal B_2)=1\)。 | A03 Steps 1–3；A04 Steps 1–7；A05 Steps 1–2 的入口／全块整性；A06 Steps 1–7，核心为 (19)–(28) 与准确耦合消元。重复的阶乘推导、模型定义和低阶导数基解各保留一份。 | M1–M2。逻辑顺序为第一阶乘带→第二 forcing→第二块整性→二阶响应桥，不能把它们改写成互相担保整性的循环。原始块误差是 \(h^{M-m}\)，只有端点另乘 \(h^m\) 缺陷才到 \(h^M\)；A06 Step 7 的低精度截断不能冒充高精度准确模型。 |
| M4 第三 forcing 的完整端点、首层与唯一因子分离 | 同一实际有限 action 的 Euler 身份及全部舍项界；两种真实配对缺陷、四项重组、合法有限移位及响应。证明 \(S\) 整且 \(\bar S=-3\chi L^m/64\)。保留全 \(H\) 精确响应和完整 \(\mathcal F_3\)，并证明 \(\mathcal E=r^3\mathcal F_3+r^4E_4+O(H^{4m+1})\)。最后给出实际次数 \(D\) 和唯一首一分解 \(P_{\rm cl}U_{\rm cl}\)，商次数 \(p\) 及基础系数高度。 | A07 Steps 1–8，尤为 (15)–(18)、合法移位、全部 \(3m\) 层取消及 (57)；A09 Step 1 和 Step 2 的 (15)–(16)；A10 Steps 1–4；A08 Steps 1–2、Step 5–7 的次数、形式模型次数及首一商转移。 | M1–M3。A07 的旧 action 和三次端点不是被新 Newton 结论取代的废稿。A09 的三个二阶矩计算不必导入，但全 \(H\) 响应与四项端点必须导入。A10 的 \(E_4(0)=-3/32\) 只是一项组成量，不能独自给实际常数；必须与三次项合并。 |
| M5 正簇的全参数支撑、临界常数及温和分裂 | 高阶低块有理性及总阶 \(n\le m\) 的有限 \(p\)-整性；预临界 \(W\) 矩支撑；临界纯 \(H^m\) 的真实 Chebyshev 投影。由完整端点压缩消去临界混合项，合并三／四次移位得 \(S(0)=-3h^{m-1}/4+O(h^m)\)。转移至首一因子得到 \(b_0=16\chi h^{m-1}+O(h^m)\)、\(b_j\in h^{m-j}\)，再证明单边、不可约可分、正根距离和循环分裂域。 | A11 Steps 1–6；A12 Steps 1–6；A13 Steps 1–5。A13 Step 6 的距离点值可作推论；其最后 \(p\ge7\) 平移段不是核心。 | M2–M4。有理性原证明中的有限无穷远值不等于零；全阶有理性不等于全阶模 \(p\) 整性。预临界偶反射不能延到纯 \(H^m\)；A12 的临界反对称项与先约去 \(p\) 的有限终项必须保留。临界正参数项消失来自完整 \(\mathcal F_3\) 算子，不是擅自宣布临界 \(W\) 主部为零。 |
| M6 全部负侧中间系数的区间高度 | 共同高项 \(p[L^j]\mathcal B_3\in h^m\)（\(j>m\)）；上半段 \(p[L^j]\mathcal B_3\in h^{2m}\)（\(p<j\le D\)）；单独处理分界 \(j=p\)。通过首一递降比较形成最终所需 \(v_h(u_r)\ge M-p\)（\(1\le r\le m\)）和 \(\ge M-m-1\)（\(m+1\le r<p\)）。 | A14 Steps 1–5；A15 Steps 1–6 及 Step 7 的商系数转移；A16 Steps 1–5 与 Conditional coefficient transfer。A14 的加强证明自含必要前置，不需另保留较弱首层结论。 | M2–M4。A14 保留完整实际初值 \(q=pV_p\)，先作高参数投影再除 \(p\)。A15 的 \(t^p=0\) 窗口不能覆盖 A16 的 \(j=p\)：后者新增 \(t^p\) 阶乘带，两个常数缺陷为 1 和 \(1/2\)，Ward 系数为 \(\lambda_H\) 和 \(\lambda_H/4\)。不能因结论相邻而合并掉这一证明。 |
| M7 最高参数端点的有限偶奇带基础 | 由幅度齐次性提取同一 \(C_D=[L^D]\mathcal B_3\)，得到实际 \(W,A\) 方程和含系数 16 的完整端点；证明低带、正规化高带整性及中间共振污染支撑。保留准确匹配低带的有限参照引理和有限一次低解 \(w_1,a_1\)。 | A17 Steps 1–2、Step 4 中正规化高带整性段、Steps 5–6 的基带导数与奇污染支撑；A18 Steps 1–2 的有限参照／实际窗口，以及 Step 4 的 (17)–(19)。A17 Step 4 的倍角身份可与 A16 Step 5 只保留一份。 | M1–M2；A17 的旧全局参照若原样引用还带 M5 的有理性依赖。后续已经采用 A18 的有限参照，不需要把未知 \(R_{m+1,0}\) 全局极部变成新义务。A18 旧结论被加强，不意味着其有限参照、\(w_1,a_1\) 和支持整性的原论证可以删除。 |
| M8 最高端点的完整 Ward 段与零阶二次边界 | 保留真实 \(2p\) 移位至二次常数项；证明两带 Ward 响应及完整端点压缩 \(-\lambda_H(H\partial_H-m)B_{\rm low}\)，其中 \(B_{\rm low}=-4^m[L^m]\mathcal B_1\)。保留两条二次有限方程、显式 \(X_0,Y_0\) 和完整零阶二次端点 \(\mathfrak c_{2,0}=0\)。 | A19 Steps 1–6，尤为 Steps 2–5 的 (14)–(38)；这里只导入其一般证明，不导入末尾 \(p=5\) 专表或核验代码。 | M2、M7。形式 \(H\) 导数不能改为对已取值的局部数求导。二次传播子 \(-4H^{2m}\)、线性响应的再反馈及 \(Y_0(0)=-6\) 都不可丢。其旧高度 \(pC_D\in h^p\) 后来变为等号，但 Ward 和零阶二次解仍是新层实际输入。 |
| M9 实际最高系数的首个非零层 | 三个不同义务一并闭合：第一 forcing 最高项次层给线性端点 \(-1/4\)；有限参照 ghost 的直接项和高带反馈共同缩放给净端点 0；完整新二次响应、有限伴随和单／双和给 \(\mathfrak c_{2,1}=-1/2\)。合并得到 \(pC_D=-3h^p/16+O(h^{p+1})\)。 | A20 Steps 1–5；A21 Proof 的首误差计算、实际高带方程和共同缩放，特别 (18)–(27)；A22 Steps 1–8，不能只取 Step 7 的总结果。 | M2、M7–M8。旧 \(O(h^p)\) 参照精度不能被直接删去；ghost 各来源不分别为零。有限伴随恒等式仅在 \(\mathbb F_p\) 使用，特征零卷积应理解为 \(p\)-整代表，不得将一个同余再除以 \(p\)。\(p=5\) 时须先合并四次幂被加数为三次再求和；实际 \(4^D\equiv4\)，不是 16。 |
| M10 完整两边 Newton、因子型和首三互素 | 将中间区间高度与准确最高高度 \(v_h(u_p)=M-m\) 比较严格弦上位置；由赋值分母 \(p\) 证明负因子不可约、可分及单根域野全分歧。另以纯偶倍角求 \([L^p]\mathcal B_2=4\chi h^m+O(h^{m+1})\)，排除 \(\mathcal B_2\) 与负因子成比例；合并所有根赋值和第二 forcing 的整点非零性得两两互素。 | A23 Steps 1–4。Step 5 的全参数点值为同一乘积身份的可选推论，不是另一证明主线。 | M2–M6、M9。第二 forcing 的真实次数是 \(p\)，不能用“次数小于 \(p\)”排除共同因子；其最高／常数比首余式为 \(2\chi ph^{-m}\)，负因子为 \(4\chi ph^{-m}\)。不可把单根域次数 \(p\) 扩成已确定负分裂域或 Galois 群。 |

前向排列可取 M1→M2→M3→M4→M5→M6→M7→M8→M9→M10。
M6 与 M7 的部分准备可并列，但不产生新的批次论文并行立项。
其中 M7 的低带基础不使用 M8 的结论，M8 只使用 M2 的既有首层，
M9 才引入第一 forcing 的新次层，因此不存在“用第三非零层证明自己”的循环。

## 3. 作者源索引与实际阅读范围

下表的行号仅用于如实记录本次阅读，不作为证明长度、自然篇幅或容量估计。
“定向读取”只表示核对依赖声明、相应原证明段落及边界；不表示重新验算该稿全部数学。
未读的中间证明可作为接受 lemma 的来源，但本件不声称做过其全文审查。

| 号 | 准确作者文件 | 本次实际正文阅读范围 |
| --- | --- | --- |
| A01 | [ROOT_COUNTEREXAMPLE V1](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.md) | 1–250；仅 Steps 1–2 为本包入口，未声称本次阅读全文 |
| A02 | [PRIME_POWER_LOCAL_STRUCTURE V1](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | 1–368；另读章节索引，未展开 Step 7 |
| A03 | [POST_POLE_BLOCK V1](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md) | 81–277；另读全稿章节索引 |
| A04 | [SECOND_INTERNAL_FORCING V1](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md) | 85–249、412–581；另读全稿章节索引 |
| A05 | [SECOND_FACTORIAL_BLOCK V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md) | 83–237；另读全稿章节索引 |
| A06 | [SECOND_FACTORIAL_RESPONSE_BRIDGE V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | 114–368、559–640；另读全稿章节索引 |
| A07 | [THIRD_FORCING_GENERAL_PRIME V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | 86–277、470–528、687–808；另读全稿章节索引 |
| A08 | [ROOT_CLUSTER_SEPARATION V1](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md) | 1–250、300–480（至文件末尾）；未连续读 251–299 |
| A09 | [GENERAL_NEXT_LAYER V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) | 84–328；另读全稿章节索引，未展开 Steps 3–8 的三个新二阶矩计算 |
| A10 | [FOURTH_SHIFT_RESIDUE V1](PAPER30_TWIST_THIRD_FORCING_FOURTH_SHIFT_RESIDUE_PROBE_V1_20260907.md) | 1–99、235–316；另读全稿章节索引 |
| A11 | [HIGHER_RESPONSE_STRUCTURE V1](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | 1–119、254–393；另读全稿章节索引 |
| A12 | [CRITICAL_PROJECTION V1](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | 1–191、313–469；另读全稿章节索引 |
| A13 | [UNIFORM_POSITIVE_CLUSTER V1](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | 1–450；另读全稿章节索引 |
| A14 | [NEGATIVE_HIGH_PRECRITICAL V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_PRECRITICAL_PROOF_V1_20260908.md) | 1–410（文件在此范围内结束） |
| A15 | [NEGATIVE_UPPER_HIGH_CRITICAL V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_HIGH_CRITICAL_PROBE_V1_20260908.md) | 1–495；未声称读末尾剩余核验记录 |
| A16 | [NEGATIVE_BOUNDARY_HIGH V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_BOUNDARY_HIGH_PROOF_V1_20260908.md) | 1–370（文件在此范围内结束） |
| A17 | [NEGATIVE_TOP_PRECRITICAL V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md) | 43–282；其中输出截断过的 155–282 已另行完整读取；另读全稿章节索引 |
| A18 | [NEGATIVE_TOP_POSTCRITICAL V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md) | 40–239、303–353；另读全稿章节索引 |
| A19 | [NEGATIVE_TOP_SECOND_POSTCRITICAL V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_SECOND_POSTCRITICAL_PROBE_V1_20260908.md) | 1–576；另读全稿章节索引，未展开末尾 \(p=5\) 表及代码 |
| A20 | [FIRST_FORCING_TOP_NEXT_LAYER V1](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md) | 1–89；另读全稿章节索引，Steps 1–5 的结论按接受输入端点导入 |
| A21 | [NEGATIVE_HP_GHOST V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md) | 1–130；其必要后段范围由 A22 的明确输入 (18)–(27) 定位，未声称全文阅读 |
| A22 | [NEGATIVE_HP_RESPONSE V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md) | 1–323、370–550；另读全稿章节索引，未逐项复算六核与有限和 |
| A23 | [NEGATIVE_NEWTON_AND_COPRIME V1](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_PROOF_V1_20260908.md) | 1–280（全文） |

本次还全文读取了对象简报及以下定向处置：完整负结构、统一正簇、
[上半段／分界／二次边界](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_BOUNDARY_AND_QUADRATIC_DISPOSITION_20260908.md)、
[第二内部 forcing](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)。
另读取 [第三 forcing 早期处置](PAPER30_TWIST_THIRD_FORCING_DISPOSITION_20260907.md) 的 1–220 行，
以及若干直接相关作者稿的章节／链接索引。
较弱 [NEGATIVE_HIGH_LAYER](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_LAYER_PROOF_V1_20260908.md)
和 [NEGATIVE_TOP_CRITICAL](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_PROBE_V1_20260908.md)
在本次仅做章节／直接引用定位，未当作重新全文审查的对象。
没有遍历 build 树、重扫旧构建、加载整份历史总账或新增文献检索。

## 4. 去重与覆盖：可不纳入正文，不是删除历史文件

1. **定义只设一次。** 实际 map/action、\(h,\rho,L,d_n,V_n,\mathcal B_k\)、
   辅助幅度 \(b\)、形式变量 \(H\)、低块 \(P\)、\(J,K\) 及负下标约定可集中于 M1–M3。
   但双变量窗口 \(t=bx,u=Lx^2/4\) 与两带 \(W,A\) 是服务于不同系数提取的后续坐标，
   不能把它们当成重复模型而删去必要缩放证明。
2. **阶乘与 action 的共用证明只写一份。** 第一阶乘桥在 A03、A04、A06 有重复转述；
   第二阶乘的四项有限展开在 A05、A06、A07 有重复转述。可由 M3 的精确 lemma 供后文调用。
   各端点 \(p,2p,3p\) 的权重、非驻值缺陷和所需误差不同，不能仅因 Euler 模板相同而删去
   第二／第三端点的真实误差核定。
3. **五、七的幂专表被统一正簇证明覆盖。** 正簇中心结论采用 A11–A13，
   不再以特殊 \(p=5,p=7\) 的有限表、判别式或拟合承担无限族证明。
   A19 末尾 \(p=5\) 二次表也不承担普遍量词；其统一 Steps 2–6 已明确覆盖最小素数。
   这些表及失败／成功记录保留历史文件，不纳入最小主线。
4. **一般下一层稿可按段落分拆。** A09 Step 1 的精确 \(t,q\) 和 Step 2 开头完整
   \(\mathcal F_3\) 必须留；其用于 \(p\ge7\) 次首层／平移
   \(-41h/(384m)\) 的三个新二阶矩、求值证书及平移结论可不纳入中心包。
   A10 的四次项来源不同，不能跟着这些非核心二阶矩一起排除。
5. **加强的系数高度覆盖旧根界，不自动覆盖证明工具。** A14 的整个预临界共同高界
   覆盖较弱 NEGATIVE_HIGH_LAYER 结果；A15–A16 覆盖旧上半段／次高的不足界；
   A19–A22 覆盖最高项逐层的旧下界。最终根界只陈述 A23 的准确斜率即可，
   无需逐次重放旧开区间。但 A17 的权重／整性／基导数、
   A18 的有限参照与一次低解、A19 的 Ward 和二次基解仍是 M7–M9 必需输入。
6. **不重复证明已有互素。** 第一／第二互素来自 M3；第一／第三可在 M10 按完整根赋值
   分离一次给出，不必再复制 A07 Step 9 的旧剩余论证。
   第二／第三的新比例排除不能以这些旧互素结果替代。
7. **一般 DVR/Hensel 机制是支撑，不单列科学增量。** A08 的固定次数存在唯一性、
   首一商高度转移和 A13 的简单根提升各写一次即可。可把最终点值式置为短推论，
   不再重复早期较弱根界的每一条点值区间。
8. **独审、处置与失败账本不是作者证明模块。** 它们承担来源、纠错和接受状态；
   可在写作来源表或审查交付记录中保留准确指向，不应把多轮 review 文本、
   哈希列表、检查计数、脚本输出或旧“待审”状态拼成正文的论证长度。
   作者稿中历史“待独审”的字样由现有接受处置解释，不在本件覆盖原文。

## 5. 不可丢失的原证明及引用整理边界

最容易被“只保留最新结论”误删的内容，共有以下六组：

- A02 **形式**整除式 (15)：M6/M8/M9 所用 Ward 导数的合法输入，不只是第一根型结果。
- A03/A05 的实际块整性及 A06 的准确模型桥：没有它们，A07 的实际端点与形式端点缺少可用误差连接。
- A07 的非驻值 action、准确四项端点及合法移位，加上 A09 的全 \(H\) 响应和 A10 的真实四次项：
  正簇常数必须使用全部同阶组成量。
- A11 的有理性原证明、有限整性桥及 A12 的临界投影：不能用已知 \(p=5,7\) 表或普通偶反射取代。
- A17/A18 的实际最高权重、有限窗口／整性、有限参照与一次低解，
  以及 A19 的 Ward／零阶二次系统：其旧下界虽已加强，后续计算仍明确调用这些作者事实。
- A23 Step 3–4 的第二 forcing 最高项及比例差：真实次数 \(p\) 必须正面处理。

重排时有两处应按实际公式定位，避免照抄旧文字中的短引用：
A19 对第一内部形式整除的来源应指向 A02 **Step 4、式 (15)**；
A23 输入栏提到的纯偶倍角，在 A16 的准确位置是 **Step 5、式 (20)–(21)**，
并且 A23 Step 3 已自含核回其缩放。此处只是引用定位，不改写已接受数学。

本清点不判定任何新科学缺口，也不触发重审未变输入。
后续作者若仅按本表复制／准确导入接受 lemma、统一记号及删去重复叙述，
其待解决工作是作者化组织与引用闭合；若改造证明、提高精度、删去仍被调用的 lemma
或扩大量词，则超出了本依赖清点已经支持的范围。
