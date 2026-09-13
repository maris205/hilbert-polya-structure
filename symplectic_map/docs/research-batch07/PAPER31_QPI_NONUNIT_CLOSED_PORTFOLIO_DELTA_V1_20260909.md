# Paper31：闭合非单位时间算术方向的组合差额核查 V1

日期：2026-09-09 UTC；核查席：`/root/p31_qpi_novelty_cd_i05_i09_v1`。
类型：`BOUNDED_PORTFOLIO_DELTA / NO_NOVELTY_SCORE / NO_ADMISSION`；`route_applicability: NOT_APPLICABLE`。
对象为新 [Phase A][PHASE] 的完整 C1–C3 同一研究链；本件不是只给最近 G 增量评分，也不是重开旧正式票。

## 1. 结论与两条不可混淆的基线

相对于 P18、P29、P30 的已接受论文及旧非单位时间有界材料，当前链保留两项不重复的原对象差额：
**C1 的全次数真实标记扩张／整数恢复，与 C2 的全次数实际留数格／原次数移位。**
C3 是这两项接口在同一个原上同调上的闭合算术输出：它确实超出旧低阶结果，但不是另外三套独立方法。
本次有界实读没有发现旧组合已经给出上述完整新公式的定理或可直接代入的全部前提；这不是全球新颖性证明。

必须同时保留以下两种时间口径：

| 比较基线 | C1 的地位 | C2–C3 的地位 |
|---|---|---|
| 完整当前 I05 链相对既有 P18/P29/P30、旧全次数 jet／三阶包 | D05 在旧 I05 查新之后实际完成，保留为本链的非重复差额；未成文且先行接受不等于外部先例 | 原格识别及全次数消费者属于这条新链；须扣除旧工具和低阶实例 |
| 最近[两诊断数学快照][BASE]相对新 G/D/C/A 阶段 | 已在 BASE §2 接受，不是 G 阶段再次发现；此次状态变化为零，不是科学贡献被取消 | G 提供该快照尚缺的原格桥；D/C/A 闭合其消费者和新增数字规则 |

因此，不得以“任何结果先证明并接受便成为旧物”的滚动口径清空完整候选贡献；也不得将同一 D05 在前后两阶段计两遍。
旧组合中的 all-degree jet、二阶、三阶和本链固定 M4 锚点则按 Phase A 的明确范围全扣除，不作为新增独立支柱或正文填充。
本件不把本地接受称为已发表，也不判断当前差额是否足够自然形成22–30页长文。

## 2. 对象身份与个人责任

全篇固定 $q=1,R=\mathbb Z[\tau]$、原四簇 $1+2+3+2$ 八截面模型、$\mathscr L=-K$，以及
$$M_n=H^1(S,\mathscr L^n)=\operatorname{coker}J_n,\qquad
T_n=\operatorname{tors}_{\tau}M_n,\quad L_n=M_n/T_n,\quad E_n=L_n^{**}/L_n.$$
这里的 $M_n$ 是整个余核；$\tau=0$ 只延续曲面和层，不延续可逆动力。所有素数结论不推广到任意 $q$。
下文采用[合并定理 A][ALL]的准确记号
$$I_{n,a}=\left(\binom{n-1-b}{a}\tau^b:0\le b\le n-1-a\right),\quad
B_n=\sum_{j=1}^{n-1}j^2,\quad D_n(p)=\sum_{a=0}^{n-1}\min\{b:p\nmid\tbinom{n-1-b}{a},\ 0\le b\le n-1-a\}.$$
其中 $n\ge1$、$0\le a<n$；零次数按空和／空积约定。

本席是 [D05][EXT] 与[一般行列式引理][DET]作者，此前为 [G][GEO] 提交了单独的非作者数学检查。
本件不是对本人 D05/DET 发独立数学票，也不是零接触／盲审或跨模型正式新意票；合并定理 A 的独查由别席承担。
对已接受数学身份消费相应处置／非作者报告，当前只核对主张、对象、依赖和组合包含关系。
使用 novelty-check 的逐主张重叠框架、research-review 的证据层级纪律；依任务仅做本地组合核查，不执行新全球检索或设分数。

## 3. 必须先扣除的原 qPI 内容

### 3.1 全次数呈示已经属于旧基线

[JET] Claim C1–C3 已给每个 $n\ge0$、任意交换基变换上的实际两项复形
$$R\Gamma(S_A,\mathscr L_A^n)\simeq[A^{2n(n+1)+1}\xrightarrow{J_n}A^{2n(n+1)}],$$
原八组评价与它只差单位可缩块；四图二项式条目及受限源 $\Lambda_n$ 都已明确。
这些不是新 C1 的发明，也不因旧材料未独立成文而改称未知。
[NU] §2A–B 还已接受零时间全次数固定部／维数与二阶整数标量分解，全部扣除。

“实际呈示决定所有不变量”在逻辑上当然正确；因此这里的“旧组合未供应”不是说新命题不由旧对象数据蕴含。
准确差额是：旧呈示尚未给出统一的全次数标记连接、闭式整数格及其算术规律；求取这些需要新写的对象识别和全称论证，
不能由“余核已定义”直接称为一个已完成的短推论，也不能将换成另一张同规模矩阵当成同等增量。

### 3.2 三阶与四阶必须完整扣除

[M3] §1、§4 Steps 4–6 已有
$$M_3\simeq R^2\oplus(R/(\tau^2))^2\oplus
\operatorname{coker}(R\xrightarrow{(\tau^2,2\tau)^t}R^2),
\qquad\operatorname{Fitt}_3(M_3)=\tau^5(2,\tau).$$
其混合块无扭商就是 $(2,\tau)$，且原专门化扭长为5／6；因此“原自由商可能非自由”“双对偶会有高度二缺陷”
和“底层维数相同但扭长变化”的机制已经出现。由该理想互素生成元得到双对偶缺陷 $R/(2,\tau)$，也只是旧式的短推论。
不能把新 C2/C3 的 $n=3,p=2$ 特例重新计一次。

[M4] Claim 与 [M4R] 已核准固定 $A=R_{(3,\tau)}$ 上
$$L_4\otimes A\simeq A^2\oplus(3,\tau)^{\oplus2},\qquad
E_4\otimes A\simeq\mathbb F_3^2,$$
以及真实 $M_4$ 块化和泛特征／特征3长度14／16。
从该完整块呈示直接取最大子式还给 $\operatorname{Fitt}_4(M_4\otimes A)=\tau^{14}(3,\tau)^2$；这不另算新结果。
M4 强于一个拉回／推出影子，但它仍是本链的固定低阶锚点，不为全次数公式增加第三个独立核心。
该原块化只在所指局部环成立，不将其悄然推广为全局 $\mathbb Z[\tau]$ 分解。

[OLD] Claim 已把全素数强直和 (P)、较弱 Fitting 目标 (F) 和两特征 Smith 数据分开，且如实列为未证。
有限 $p=2,3,5,7$ 样本不是已接受全称结论；新 A 的 (First) 解决旧 Fitting 目标，不能将“此前已猜到公式”误当此前已证明。
反过来，旧样本、三阶和 M4 都不再按素数各自增加一份新意。

## 4. P18/P29/P30 实际定理的包含与限界

| 实际读取的旧定理／证明 | 可以原样扣除的工具或输出 | 不供应当前链的输入 |
|---|---|---|
| [P18] 主定理(4)–(5)，`prop:fitting-basechange` 及其证明，§Fitting 的行列式／泛长度段 | 兼容完成坐标、有限呈示子式任意基变换、理想而非根式、局部单位换帧、DVR 长度等于阶数 | 其对象是复数 simple-exact-disjoint 标记 Hénon 的相对微分，平方呈示的 $\operatorname{Fitt}_0$；没有原 $M_n$、整数坏素格或高度二理想乘积 |
| [P29-3] `lem:degree-basis`、`thm:orbit-obstructions`、`thm:bounded-primitive`；[P29-4] 式 `rho-reencoding` | 有限支持累计原函数、系数和障碍、常数核、欧氏除法的有限数字恢复，以及有正确滤过前提的支持控制 | 对象是特征零 $K[x,y]/(F^*-1)K[x,y]$ 的向量空间余核；没有 $\mathbb Z[\tau]$ 模、原四簇标架、留数格或基 $p$ 二项系数消失的实际系数身份 |
| [P30-2] `geom:constants` 完整证明；[UNIT] U1–U3 的已接受声明 | 原常数、八环节点单位消元、单位时间全次数对角复形和任意基变换；令 $q=1$ 后已给 $M_n[1/\tau]\simeq R[1/\tau]^n$ | 单位时间底环已反演 $\tau$；该复形不能恢复被反演删去的原整数格、$\tau$ 扭子或高度二缺陷 |
| [P30-5] `trace:residue` 及完整证明 | 原 rank-two 递推后的有支持界逐位系数选择、Hasse 乘子的 Frobenius 迭代 | 被选择的是谱系数，支持界为 $[0,2p-2]$；不是 $I_{n,a}$ 的整数系数行，也不给 $\rho_nJ_n=0$ 或原次数移位 |

P18 的一般子式基变换不能直接升级为本件 $\operatorname{Fitt}_n(M_n)=\tau^{B_n}\operatorname{detideal}(L_n)$：
后式还需原长度一分辨率、自然双对偶、互补最大子式的共同标量和全部高度一赋值。
[DET] 给这些标准交换代数步骤的自足桥梁，不能称 P18 早已声明该完整引理，更不能给本人引理另授独立创新或独立数学票。

P29 的“数字”与 P30 的“数字”共享逐位恢复办法，而非同一个计数对象。
当前 Lucas 型判别是 [BIN] Step 3 对 $(1+X)^m$ 的标准展开；它确实应扣除，但不是通过把 Hénon 相次数改名为素数得到。
这些跨族比较只用于工具扣除，不构造虚假的 P29→qPI 原模证明箭头。

特别是 [P30-2] 的单位传播出现 $-\tau^{-1}$；[UNIT] Assumption 1 明确排除非单位参数。
所以“既然旧单位时间分裂已对任意基变换成立，就令 $\tau=0$”不是合法包含论证：不存在到非零目标环、把该单位送为零的基环映射。
在反演 $\tau$ 后原格全变自由，只保留秩 $n$，不保留当前需要的新算术信息。

## 5. 新 C1–C3 的逐项差额，不按消费者数量计方法

### 5.1 C1：保留全次数标记扩张与恢复，扣除通用 Ext 计算

[EXT] T1–T2、Proof Steps 1–8 给原乘 $s_0$ 的实际复形单射、商及 $s_1^{n+1}$ 提升，进而
$$0\to M_n\to M_{n+1}\to R\oplus2\bigoplus_{j=1}^{n}R/(\tau^j)\to0,$$
并在每个原商标记上给完整类
$$\left[u^{a-1}\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b\right]_{r,n}
\pmod{\tau^mM_n},\qquad m=n+1-a.$$
四边兼容及保原 jet 标记、严格降次数的整数还原，供应旧 JET 没有写出的统一连接；它是完整本链相对旧组合的实际差额。

长正合列、$\operatorname{Ext}^1_R(R/(\tau^m),M)=M/\tau^mM$、几何级数恒等式、单位插值和单首项整除均为工具扣除。
旧 [OLD] W2 只写另一个 Koszul 长正合列且保留未知连接；W3 的单位三角 minor 不给完整核或全连接。
其 Steps 5/Pascal 边界已经写出的三角补基／完整平移可逆性也须扣除，不能再称新技术。
但这既不意味着旧 W1–W3 已独立接受，也不代替当前 C1 对原四图连接的实际计算。

全列非分裂、固定 $n=4\to5$ 的素数3效应及统一 $P_m$ 是该扩张的后果；
尤其 $P_m$ 的 $\tau^{m-1}(\tau,m)$ 不能单独支撑“全部素数在原 $M_n$ 首现”，更不能冒充原直和块。
目前完整 C1 不只是形式 Ext 定义；其非重复内容是原受限源／目标上全部类和可恢复规则的绑定，而非 Ext 理论本身。

### 5.2 C2：新接口在于实际格的识别，不在双对偶符号

[GEO] G1–G2、Proof Steps 1–7 依次保留原四中心、反典范符号、完整留数和、原余核秩／满射与整数坐标正规形，得到
$$\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a},\qquad
\rho_{n+1}\iota_n=\operatorname{shift}\rho_n.$$
归一化后连接是 $\tau$ 倍右移，不是随意选择的自由坐标或无移位包含。
这条同对象全次数识别是当前新格残余的核心；旧单位族只给逆 $\tau$ 后的抽象自由秩，旧三阶／M4 只给低阶格。

全局留数和为零、形式逆函数、整数负二项式系数与 UFD 互素分母都是标准机制。
原坏图化为 $F=U(\tau+V),G=V$ 并计算其完整 jet 像，是这些机制在固定原几何中的实现，不能称一种新普适留数理论。
一旦 G1 成立，G3 的 $I_{n,a}^{**}=R$、$E_n=\bigoplus_aR/I_{n,a}$ 及有限性即为短推论；
[BIN] 的各 $\tau$ 系数层累积 $p$ 赋值和相邻投影进一步是显式整数理想的直接计算。
因此“留数格”“双对偶缺陷”“每层有限群”不应拆为三次创新。

C2 不能恢复 C1 的全部原 Ext 类：它忘掉 $T_n$，并未分类整个 $M_n$。
C1 的递归呈示虽可决定原模，也不自动供应 C2 的闭合格式。
两者分别提供真实连接与闭合格坐标，是同一线上的互补接口，不能互相抹去，也不宜包装成互不相关的两套新理论。

### 5.3 C3：算术闭合是新原对象结论，主要方法负担在前置桥梁

| 当前结论 | 相对旧组合的准确剩余 | 已给前提后的推导负担／不得重复计功 |
|---|---|---|
| A 的 (Resolution)，$\operatorname{Fitt}_{j<n}=0$ | 不是旧有限呈示自动具有的指定单射分辨率，但也不需再发明几何 | C1 给完整核；旧单位三角补基给直和项；删零列及子式阶数是短推论 |
| 全局 $\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_aI_{n,a}$ | 原全次数整数理想并未在旧组合计算；包含高度二内容，不只是一串域上 Smith 长度 | 在 G 的归一化、实际分辨率及泛长度明确后，DET 的标准互补子式和局部化合取给出；不是独立几何桥 |
| 所有特征的原扭长 $B_n+D_n(p)$ | 超出旧零纤维维数和固定低阶长度；必须识别实际自由像 | [BIN] H1–H3 齐备后由格指数、蛇形引理和望远镜求和推出；不能直接累加商扭子 |
| 首次 $n=p+1$、增量 $p-1$、$(p,\tau)^{p-1}$ | 旧 (F) 目标在全部素数上得到新结论；$p=2$ 三阶和 $p=3$ 四阶先扣除 | $n\le p$ 的单位常数与 $n=p+1$ 的 $p-1$ 个 $(p,\tau)$ 理想是标准二项式短计算；非主性又是其短推论 |
| $D_n(p)=0\iff n/p^{v_p(n)}<p$ | 旧组合未写出此原模的全部次数消失规律 | 它等价于二项式第 $n-1$ 行全部非零的 Lucas 数字判别；再接有限 $p$-群及自然双对偶即得自由性，不另计新框架 |
| (Digit) 全次数递推 | 旧 P29/P30 未包含这个实际计数函数；A Step 5 写出明确终止式 | 从 $d_p(N,a)$ 的数字最大值按 $N=pq+r,a=pb+s$ 分两类求和，是同一 Lucas 消费者的聚合；不是第三项原对象识别 |

“短推论”修饰的是前提已经闭合后的计算成本，不把 C3 对原对象的结论宣布为旧论文已经证明。
特别是 $\dim_{\mathbb F_p}E_n[p]=D_n(p)$ 不等于完整有限群的 $p$-对数阶；后者还包含各系数层的高 $p$ 赋值。
扭长首次增加不意味着以后每个次数都增加；(Zero) 正是在同一格中刻画后续无缺陷次数。
公式数量、素数数量及“首现／总和／消失／非主”四个名称，不能变成四个独立创新计数。

## 6. 有界反对意见与仍未被本件关闭的事

1. 最强包含压力仍是：遗忘原 qPI 名称后，这个受限四簇格是否就是既有整数 principal-parts／Taylor／Pascal 对象，且已有统一定理连同嵌入和移位直接给出 C1–C3。
   本地 P18/P29/P30 没有提供这个完整识别；外部来源任务仍需核对，不能据此授全球排他性。
2. 旧 [NU] §4 已扣除 Harbourne、近点簇／fat-jet、平移差分及完整 Pascal 工具。当前报告继承该扣除的接受身份，不冒称本次重读全部外部文献。
3. 不能因把旧 JET 压缩成闭式就预先授足够价值；但也不能把任意呈示在原则上含全部信息当作否定所有结构定理的理由。应比较实际新桥梁的统一性、可恢复性及其非平凡消费者。
4. 整个 $M_n$ 的强直和 (P)、全部原扭子 Smith 指数、高于秩的其他 Fitting、一般 $q$ 和非加法结构仍未包含。不能借这些开放目标的潜在价值补足已证包。
5. D01 的固定完整临界理想、P30 单位时间迹／Hasse及其他系统族结果均不并入本包扩充成果；共同工具只扣除，不拼成新对象。

本件结论为：**保留 C1＋C2 的同一原对象全次数差额，把 C3 作为统一算术消费者；旧低阶／旧呈示全扣除。**
它允许后续据实际来源讨论完整链，不预设新意／价值分数，不重置旧6.5／CAUTION，不将数学接受等同长文准入。

## 7. 本人实际读取与输入身份

FULL 表示本人读完本文件；PARTIAL 只表示列明范围。整文件 SHA 绑定所读版本，不把局部读取冒充全文。
GEO／JET／EXT／DET 的既往个人全文读取单独标出，不继承其他席的阅读量；本轮仍核对其当前身份。

| ID | 本次个人读取层级／实际段落 | SHA-256 |
|---|---|---|
| [PHASE] | FULL 83行 | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` |
| [ALL] | FULL 180行；与指定终态一致 | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` |
| [PORT] | FULL 121行 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| [BASE] | FULL 96行 | `3a3d3444e5237af5dab971d488fa1d513d5fcc4bdb32d3c4cd1a008e0d19ee59` |
| [LIMIT] | FULL 121行；只沿其接受源入口读取 | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |
| [NU] | FULL 146行；历史状态不覆盖当前接受 | `cf438f313d34c70f8dc7d775894524164460ba8a69d16c01c712a174a8200de0` |
| [INT] | FULL 162行；只消费既有接受身份 | `1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af` |
| [UNIT] | PARTIAL 1–98：Claim、全部 U1–U3／底环边界，非全证明复审 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| [JET] | 本次 PARTIAL 1–90；此前 G 独查任务本人 FULL 358行，当前同 SHA | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| [M3] | PARTIAL 1–160、190–文件末尾；Claim及相关 Fitting／理想商／特征消费者证明完整，未全读块化 | `fe9f9f1c70b20eea4d587d57959eafd9dd8ab42cc128119c32ac6714c77470e8` |
| [OLD] | PARTIAL 1–125、199–242：原目标／W1–W3／W3完整证明及 Pascal 边界，不重签 W1/W2 | `360741298e0a3478586031eb7ef19b18e0a36ce899b78c856cd3473c8671249a` |
| [M4] | FULL 127行；未读或运行其脚本 | `1161e63f35fa07ac401d9fc21fe58167f2cad39b0a810e37638b663f3ed8f663` |
| [M4R] | FULL 149行；主控告知已全文合取通过，本件不复跑证书 | `6bef85adcd0708abd00af14704413645351e803aaa03d0aa94a77d46f46286f6` |
| [EXT] | 本次 PARTIAL 1–85及段落定位；此前本人作者 FULL 318行；接受由 BASE 供应 | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` |
| [GEO] | 本次 PARTIAL 1–105及段落定位；紧邻 G 独查任务本人 FULL 429行，同 SHA | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` |
| [DET] | 本次 PARTIAL 1–90及段落定位；此前本人作者 FULL 297行；不自审 | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` |
| [BIN] | FULL 176行；消费范围核对，不另发完整数学票 | `25bb87a365eaf5a9d37c192a47f99d454007aa14e265668c34465cc3e2154e10` |
| [P18] | PARTIAL 525–618、1053–1295：完整主定理及 Fitting/泛长度相关证明 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| [P29-1] | PARTIAL 19–39：对象及特征零假设 | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| [P29-3] | PARTIAL 1–244：数字基、轨道障碍、保次数原函数三个完整命题／证明 | `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1` |
| [P29-4] | PARTIAL 53–100：相位数字重编码及所用定义 | `e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884` |
| [P30-2] | PARTIAL 228–338：`geom:constants` 完整命题／证明，随后下一节开头 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [P30-5] | PARTIAL 84–161：rank-two接口及 `trace:residue` 完整命题／证明 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |

本次无数学脚本、参数样本、CPU/GPU实验、联网、编译、上传或外发；SHA／文本读取仅用于上述指定身份。
一次文件名发现命令枚举出了部分旧 build 文件名；未读取其内容、未核其哈希，后续直接按已知接受源路径读取，没有作构建树审计。
仅新增本报告；未改旧稿／旧票／锁／接受产物／索引，未创建 P31 项目或正文。终态全文自读，行数与 SHA 随交付报告。

[PHASE]: PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md
[ALL]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[PORT]: PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md
[BASE]: PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md
[LIMIT]: PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md
[NU]: PAPER30_QPI_NONUNIT_TAU_MATHEMATICS_AND_SCREEN_DISPOSITION_V1_20260909.md
[INT]: PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md
[UNIT]: PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md
[JET]: PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[M3]: PAPER30_QPI_NONUNIT_TAU_DEGREE3_MIXED_OBSTRUCTION_PROOF_V1_20260909.md
[OLD]: PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md
[M4]: PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_LEMMA_V1_20260909.md
[M4R]: PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_INDEPENDENT_CHECK_V1_20260909.md
[EXT]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[GEO]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[DET]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[BIN]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[P18]: ../../papers/18-marked-henon-scalar-boundary/paper/main.tex
[P29-1]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex
[P29-3]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex
[P29-4]: ../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/4_hilbert_series.tex
[P30-2]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[P30-5]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex
