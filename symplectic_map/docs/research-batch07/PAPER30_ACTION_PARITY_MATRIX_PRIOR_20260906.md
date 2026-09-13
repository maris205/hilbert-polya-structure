# Paper30：偶周期作用量奇偶障碍与矩阵多项式 Livšic 的分支先例核查

日期：2026-09-06。状态：`BOUNDED_PRIMARY_PRIOR_REPORT`。
`route_applicability: NOT_APPLICABLE`。本轮不评分、不作容量 PASS、不新建正式项目。

## 1. 分支结论

**A：应扣除的机制比“一般二部图变号”更强。** Gómez–Meiss 的 Hénon 对称分类
不只说明奇多项式有中心反射；其 Example 5.1 已显式处理三次多项式的
$+a/-a$ 配对、$i$ 缩放与平方根结构。锁定二项族的偶次迭代共轭可用同一
有限中心对称机制短证。完整周期 scheme、固定 $P(0)=0$ 下作用量逐项不变，
再与单周期临界值碰撞及非共轭证书结合，是更具体的剩余结论；本轮未读到
直接陈述这一整套作用谱结论的先例，但不能据检索未命中宣称世界首创。
目前证据更支持一个明确的短反例／结构命题，而非自行构成长文的广泛新机制。

**M：一般矩阵 Livšic 母题成熟，但“全局多项式 gauge”不能由常用定理替代。**
已读结果分别输出紧双曲背景中的 Hölder 解、非一致双曲背景中的可测解、
Young tower 上已有可测解的正则性，以及可积系统解析族的解析解。
没有一项直接推出任意 Hénon 多项式 cocycle 的全局可逆多项式解。
这个函数类别差额是真实的命题差额，不等于本轮证明了它可解、为新问题或足以成文。
当前两剪切、次数有界的作者结果只把非交换候选压回三角标量情形，应短停止。

A 与 M 分开定位，不拼接为一篇论文；本报告不重开已冻结的形式 gauge R2 评价。

## 2. 输入、量词与证据级别

### A：同一二项 Hénon 族

固定 $d\ge3$，

\[
 H_B(x,y)=(x^d+Bx-y,x),\qquad
 P_B(x)=\frac{x^{d+1}}{d+1}+\frac B2x^2,\quad P_B(0)=0,
\]
\[
 R_{B,n}=\mathbb C[x_0,\ldots,x_{n-1}]/
 (x_i^d+Bx_i-x_{i-1}-x_{i+1})_i,
\]
\[
 \mathcal A_{B,n}=\sum_{i\bmod n}(x_ix_{i+1}-P_B(x_i)),\qquad
 \chi_{B,n}(T)=\det(T-m_{\mathcal A_{B,n}}\mid R_{B,n}).
\]

短周期的重复邻项不删。特征多项式包含局部长度重数，却不包含乘法算子的全部
Jordan 信息；“完整周期环上定义”不等于“谱能重构完整 scheme”。
本轮输入称 cubic 的 $\chi_1,\chi_2$ 重构与 quartic 的非共轭碰撞已独立通过，
本报告仅承接该状态，没有复审其原证。

本轮新作者输入分三层：

- $d=5$ 的 $\chi_1,\chi_2$ 重构 $B$。
- $d\equiv3\pmod4$ 的全部偶周期作用谱不区分 $B,-B$；特选非零参数还可
  令 $\chi_1$ 相同，并以固定点导数迹区分映射。
- $\chi_2$ 的比值变量分区与平方／四次方因子可能支持统一剥离；这仍是方向，
  不是已经证明的任意次数重构算法。

本报告给先例定位及下面明确标注的短代数识别，不替代独立的作者证明验收。
尤其没有输入允许把“$n=1$ 加所有偶数 $n$”写成“所有周期”。

### M：scheme 周期条件与多项式函数类别

令 $A=\mathbb C[x,y]$、$\sigma=H^*$，$C\in\mathrm{SL}_2(A)$，

\[
 C_n(z)=C(H^{n-1}z)\cdots C(Hz)C(z).
\]

问题要求每个 $n$ 的 $C_n=I$ 在完整 $\operatorname{Fix}(H^n)$ 坐标环中成立，
而非只在其约化闭点上成立。目标为

\[
 C=\sigma(G)G^{-1},
\]

其中 gauge 要求为可逆多项式矩阵；正式命题应写明 $\mathrm{SL}_2(A)$ 或常数
非零行列式的 $\mathrm{GL}_2(A)$ 规范。可测、连续、Hölder、局部解析、全纯、
有理矩阵解不能直接替代这一目标。上述公式若成立，周期条件由望远镜乘积
在整个固定点环中成立；本轮关注的是反向蕴含。

当前有界作者输入仅为

\[
 C=U(f(x))L(g(y)),\quad \deg f,\deg g\le\deg p,\quad
 U(s)=\begin{pmatrix}1&s\\0&1\end{pmatrix},\quad
 L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix}.
\]

作者称完整 Fix1 强制 $f=a(p-2x)$、$g=b(p-2y)$，Fix2 的
$4ab(y-x)^2$ 障碍强制 $ab=0$。这里只定位此窄结果，不把它变成一般矩阵
Livšic 定理，也不重包装旧 companion 差分 Galois 或幺幂逐层标量理论。

## 3. 检索覆盖与执行边界

完整读取 `research-lit` 与 `novelty-check`，采用其分 claim、多角度、最新窗口、
核对一手正文的步骤。按本轮明确授权取消评分和跨模型评价，不另建文献库、
不下载 PDF、不扫旧 build/PDF 树、不调用子代理。复用
[上一先例预筛](PAPER30_GAUGE_ACTION_PRIOR_PREFLIGHT_20260906.md) 的 A/LL 定位，
并重新定向读取 LL 主定理；旧报告和旧 R2 文件均未修改。

以下是本轮实际执行的代表查询；同义拼写 Henon/Hénon、Livsic/Livšic 均有使用。

| 核心 | 至少三个查询角度 | 结果作用 |
| --- | --- | --- |
| A1 逆作用量与二项族 | `Henon action spectrum inverse`；`Henon action isospectral parity`；`Hénon period two action polynomial`；`periodic action resultant Henon` | 未找到直接覆盖所锁定完整 $\chi_n$ 的二项族定理；排除 Hénon–Heiles、Toda、导数谱等不同对象。 |
| A2 交替规范与奇偶障碍 | `discrete Lagrangian alternating gauge symmetry`；`bipartite graph switching sign reversal adjacency spectrum theorem Zaslavsky signed graphs`；`Henon polynomial automorphism symmetry roots unity` | 定位签名图 switching；继而读到 Gómez–Meiss 的有限对称与 $\pm a$ 三次实例。 |
| A3 临界值及低周期剥离 | `polynomial critical values binomial Lyashko Looijenga`；`polynomial critical values reconstruction binomial`；`Hénon period two action polynomial` | LL 扣除可复用；没有把单变量临界值理论冒充高周期重构。 |
| M1 矩阵周期余边界 | `matrix cocycles Livsic polynomial regular algebraic`；`Henon Livsic cocycles`；`polynomial coboundary SL(2)`；`algebraic Livsic polynomial` | 定位 Kalinin、Backes–Poletti、Bruin–Holland–Nicol；输出函数类别与本题不同。 |
| M2 多项式 versus 解析 gauge | `regular cocycles Hénon matrix`；`polynomial cocycle periodic coboundary`；`noncommutative coboundary equations integrable systems` | 核对 de la Llave–Saprykina 的参数解析族与近单位条件；未找到直接全局多项式化的定理。 |
| M3 两剪切短停止 | `upper lower unipotent polynomial Livsic`；`polynomial matrix periodic orbit coboundary`；`polynomial coboundary SL(2)` | 没有命中作者给出的特定 Fix1/Fix2 分类；未命中不能给这项初等消元赋予独立新机制。 |
| 2024–2026 | 对 Hénon/action/critical values 与 matrix/Livsic/polynomial 两线加入年份及 `after:2024-01-01 before:2026-09-07` | LL 的 2024 预印本与 2026 Hénon 乘子 cocycle 工作纳入；旧经典源保留作真正机制扣除。 |
| 最近六个月 | 两线 arXiv 域检索，使用 `after:2026-03-06 before:2026-09-07` 及 `recency:184`；窄查询无结果后放宽至 `site:arxiv.org Hénon cocycle` 同窗口 | 核实 Bianchi–He 的 2026-06-28 v1。矩阵全局多项式目标未命中直接结果；此处仅报告检索覆盖。 |

工具中没有可调用的 Zotero/Obsidian 或外部模型评审端点；未找到可用
`arxiv_fetch.py`，依技能回退 arXiv 定向网页检索。未声称完成数据库全覆盖或
跨模型独立验证。ML 会议目录不是本次数学问题的相关来源，不为数量加入。
搜索中同名 M. S. Livšic 的算子 vessels／行列式表示结果不等于动力系统
Livšic 余边界定理，已排除名称碰撞。

## 4. 八个核心一手入口及实际定理条件

“已读”指下面所列正文段和假设，不表示已独立验证原论文全部证明。
经典机制的作者论文／作者讲述是本轮可核入口，不冒称本轮读过全部首创文献。

| ID | 来源、发表状态及一手入口 | 实际读取与严格覆盖范围 |
| --- | --- | --- |
| A-P1 | M. Dougherty、J. McCammond，*Geometric Combinatorics of Polynomials II: Polynomials and Cell Structures*，arXiv:2410.03047v1，2024-10-04，预印本。[正文](https://arxiv.org/html/2410.03047v1) | §7 Theorems 7.3/7.14：monic centered 的 $D$ 次多项式之 LL 映射是次数 $D^{D-2}$ 的有限多项式映射；按临界点／值形状分层的限制为覆盖。沿用已读 §11 Proposition 11.6：标记 monodromy 与临界值可恢复多项式。该文明确归因经典 LL 结果，并非把这些结论首创于 2024。 |
| A-P2 | T. Zaslavsky，*Matrices in the Theory of Signed Simple Graphs*，Proc. ICDM 2008，RMS Lecture Notes **13** (2010)，207–229，作者讲述。[作者正文](https://people.math.binghamton.edu/zaslav/Oldcourses/510.S18/mts.pdf) | §1.7、Corollary 1.3、§2.3–2.4／Proposition 2.3：顶点符号 switching 给邻接矩阵对角相似；负号与二部性相关。对象是有限签名简单图的邻接矩阵，不是非线性作用量的临界 scheme。 |
| A-P3 | A. Gómez、J. D. Meiss，*Reversors and symmetries for polynomial automorphisms of the complex plane*，Nonlinearity **17** (2004)，975–1000，DOI 10.1088/0951-7715/17/3/012。[作者所供发表版](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf) | Theorem 1、Proposition 8／Corollary 9、§5：非平凡多项式平面自同构的对称正规形含有限对角对称；单 Hénon 的奇 $p$ 有中心反射。Example 5.1 明列 $y^3\pm ay$ 的二步组合，在等 Jacobian 参数时利用 $ip_2(iy)=p_1(y)$ 构造平方根。未陈述本题作用量乘法谱碰撞。 |
| M-P1 | B. Kalinin，*Livšic Theorem for matrix cocycles*，Annals of Mathematics **173** (2011)，1025–1042，DOI 10.4007/annals.2011.173.2.11。[出版社](https://annals.math.princeton.edu/2011/173-2/p11)、[作者预印本正文](https://arxiv.org/html/0808.0350) | Theorem 1.1 及前置 closing property：紧度量空间上的拓扑传递同胚，具文中指数 closing 条件，$\alpha$-Hölder 的 $\mathrm{GL}(m,\mathbb R)$ cocycle，所有周期点乘积平凡，则有 $\alpha$-Hölder transfer。群值可限制到闭子群；无需额外 fiber-bunching。不是非紧 $\mathbb C^2$ 上的多项式结论。 |
| M-P2 | H. Bruin、M. Holland、M. Nicol，*Livšic regularity for Markov systems*，Ergodic Theory and Dynamical Systems **25** (2005)，1739–1765，DOI 10.1017/S0143385705000179。[作者预印本正文](https://arxiv.org/html/math/0503690v2) | §6／Theorem 7：满足文中 Young tower 假设的 $C^{1+\epsilon}$ 系统，另有一维不稳定方向或条件 (26)，Lie 群值 Hölder cocycle 满足所列部分双曲 pinching，则已有可测 transfer 在塔基有 Hölder 版本。$\lambda_s^\alpha<\mu_s\le1\le\mu_u<\widetilde\lambda_u^\alpha$ 不能从一般 $\mathrm{SL}_2$ 自动删去。Hénon 应用是特定耗散实参数区的 SRB/Young tower 情形，且这是正则性定理，不是仅凭周期条件得到解。 |
| M-P3 | L. Backes、M. Poletti，*A Livšic theorem for matrix cocycles over non-uniformly hyperbolic systems*，arXiv:1802.04217v1 (2018)，原记录关联 DOI 10.1007/s10884-018-9691-x。[版本记录](https://arxiv.org/abs/1802.04217)、[作者正文](https://arxiv.org/html/1802.04217) | §1.1 Theorems 1.1/1.2：闭光滑流形上的 $C^{1+\epsilon}$ 微分同胚、双曲遍历测度和 Hölder 矩阵 cocycle，全部周期点乘积平凡，给出几乎处处可测解；测度有 local product structure 时，在测度任意接近 1 的集合上 Hölder。未输出全局正则代数解。本轮定理按预印本核对，不凭 DOI 猜卷页。 |
| M-P4 | R. de la Llave、M. Saprykina，*Noncommutative coboundary equations over integrable systems*，Journal of Modern Dynamics **19** (2023)，773–794，DOI 10.3934/jmd.2023020。[出版社](https://www.aimsciences.org/article/doi/10.3934/jmd.2023020)、[作者预印本](https://arxiv.org/html/2205.12356v1) | 预印本 Theorem 3、Definition 2、Remark 4／6：基映射 $f(\theta,I)=(\theta+I,I)$，$\eta_\varepsilon$ 为解析族且 $\eta_0=I$，每个参数均满足全部周期乘积条件，等价于参数形式解存在及缩小域上解析解存在；可扩展至 Lie 群。原给定形式解本身不必收敛。不是任意非参数 Hénon cocycle 的多项式化。 |
| X-P1 | F. Bianchi、Y. He，*A thermodynamic path metric for complex Hénon maps*，arXiv:2606.29363v1，2026-06-28，预印本。[版本](https://arxiv.org/abs/2606.29363)、[正文](https://arxiv.org/html/2606.29363v1) | Theorem 1.1、§1.1、§2.1–2.3：固定次数／多次数的 Hénon 双曲分支内，由复不稳定导数 cocycle 的 covariance 构造的路径伪距离实际分离点。用的是符号模型上的标记复不稳定乘子与其 Livšic 类，不是未标记作用量 $\chi_n$，也不是任意 $\mathrm{SL}_2(A)$ cocycle 的全局多项式 gauge。 |

访问与日期限制：M-P3 的关联 DOI 本次直接打开返回 internal error，未核出版社
全文／卷页；原作者预印本的上述定理可读。既有 LL 预筛记载的受限原始条目
不在本轮重复尝试，也不把二手归因算作已读原定理。A-P1 的 HTML 页面写有
2026 年的 Date 字段，但 arXiv v1 明确为 2024-10-04；不能算成近六个月新版本。
M-P2 的 HTML 日期也不覆盖其 2005 年发表事实。X-P1 的 2026-06-28 已核版本记录。
未绕过受限访问，未下载本地文献文件。

## 5. A 的直接覆盖、具体差额与短组合风险

### 5.1 LL 扣除仍是完整有限性，不止 generic 有限性

令 $D=d+1$、$Q=D(P_B-x^2)$，则 $Q$ monic centered、$Q(0)=0$，
$Q'=D(x^d+(B-2)x)$，而单周期作用量等于 $-Q/D$。
所以 $\chi_{B,1}$ 是单变量临界值多重集的固定缩放，含非约化临界点的长度重数。
A-P1 的有限映射限制到常数零的闭切片仍有限；进一步限制二项族也不会产生
一条正维同 $\chi_1$ 纤维。这不等于 $\chi_1$ 单射。
因此“单周期谱给有限候选”“要处理临界值碰撞”都不能作为新机制。

二项族中奇数 $d$ 的 $\chi_1$ 只依赖 $(B-2)^{(d+1)/2}$，可以直接由
$x(x^{d-1}+B-2)=0$ 及 $x\leftrightarrow-x$ 消元得到；这类根单位歧义
与临界值相同的有限纤维一致。真正额外的问题是哪个较高周期数据消去这些歧义。
LL 不给出 $\chi_2$ 的任意次数剥离，也不自动证明 $d=5$ 的特定重构。

### 5.2 偶周期机制：既有有限对称的直接代数落地

以下公式是本报告为定位先例所作的短直接识别，不归为 A-P3 已陈述的原定理。
取 $J(x,y)=(-x,-y)$、$S(x,y)=(ix,-iy)$。当 $d\equiv3\pmod4$ 时，

\[
 JH_{-B}=H_{-B}J,\qquad
 SH_BS^{-1}=JH_{-B},\qquad
 SH_B^{2k}S^{-1}=H_{-B}^{2k}.
\]

其中 $S$ 为辛线性变换。故偶次迭代之间的共轭已有极短的“中心有限对称”解释。
A-P3 的奇多项式反射和显式 $\pm a,i$ 例子比只援引图论更贴近；次数同余推广
只用 $i^d=-i$。它不能推出 $H_B$ 与 $H_{-B}$ 本身共轭。

周期变量版令 $c_j=i(-1)^j$、$z_j=c_jx_j$。对偶数 $n$，此赋值与周期边界相容，

\[
 z_j^d-Bz_j-z_{j-1}-z_{j+1}
 =-c_j(x_j^d+Bx_j-x_{j-1}-x_{j+1}),
\]
\[
 z_jz_{j+1}=x_jx_{j+1},\qquad P_{-B}(z_j)=P_B(x_j).
\]

于是它是理想层面的可逆线性代换，不需要先删去非约化点；作用量也逐项相同，
乘法算子因此相似。这个核查解释为什么“完整 scheme＋固定常数规范”确实被照顾到，
同时说明它并未引入一种超出有限对称／交替缩放的庞大新机制。
A-P2 的 switching 应扣除为概念祖先，但邻接矩阵谱本身不能充当这里的证明。

奇数 $n$ 时 $c_{j+n}=-c_j$，同一赋值不再满足周期边界；它至多提示扭曲边界
问题，不能制造本合同的奇周期同谱。偶数周期的无限序列并非全部周期数据。

### 5.3 与单周期补丁、非共轭证书合起来，增量仍须准确命名

作者指定 $m=(d+1)/2$，选择

\[
 B=\frac{2(1+\eta)}{1-\eta},\qquad \eta^m=1,\quad\eta\ne\pm1,
\]

得到非零 $B$ 且 $\chi_{B,1}=\chi_{-B,1}$；$d=7$ 可取 $B=\pm2i$。
$d=3$ 的 $m=2$ 没有满足排除条件的 $\eta$，不可把非零碰撞例子延伸到该次数。
固定点导数迹的含重数总和为

\[
 2d(d-1)-d(d-2)B,
\]

故对 $B\ne0$，两侧不同；该共轭不变量支持作者的非共轭区分。
这不是借用导数谱替代作用谱，导数迹仅用于区分已经构造的两张映射。

精确可定位的结论是：某些 $d\equiv3\pmod4$ 的二项族参数对，单周期加全部
偶周期的完整作用量特征多项式一致，却不共轭。未见上述八源直接陈述这一结论。
不过证明骨架是已知对称、两行作用量代换、单变量临界值消元及简单共轭不变量的
短组合；本轮没有依据把它扩张为一般逆作用谱理论或长文主体。

$\chi_2$ 按 $r=y/x$ 区分固定／反对角／一般轨道的平方与四次方因子，是作者
提出的下一层剥离线索。正式声称统一算法前，须处理 $x=0$、特殊参数碰撞、
非约化长度及轨道退化；仅在一般参数写出因子次数不解决全参数问题。
本轮不把未证的奇周期分离或剥离完备性列为已有成果。

## 6. M 的直接覆盖、真正缺口与停止点

M-P1 扣除了“矩阵值、非交换、所有周期乘积为单位则为余边界”这一母题的新意；
M-P3 进一步说明，放宽一致双曲性也已有成熟版本，但输出会降到测度类别。
M-P2 尤其容易被错误使用：文中含 Hénon 应用不表示任意复辛 Hénon 均符合其
塔模型及 pinching，更不表示周期条件单独构造了 transfer。
M-P4 扣除了参数形式／解析非交换余边界等价这一母题，同时明确保留了近单位
解析族、可积基系统和缩域条件。

要从这些先例到锁定命题，至少还缺三件事：

1. **基动力系统匹配。** 在某个紧双曲不变集上应用定理，不能覆盖全仿射平面、
   任意参数与全部非约化周期 scheme；非一致双曲测度结论也不是此种覆盖。
2. **代数正则性提升。** 在不变集上的 Hölder 解即使唯一至常矩阵，也不自动
   延拓为全局多项式；全局全纯解也不自动有多项式增长。需要独立的代数化或
   次数控制定理，而不能把“数据是多项式”当作推理步骤。
3. **scheme 条件的作用。** 当前输入比文献的点值周期数据更强，但这种增强
   如何强制多项式 gauge 尚无本轮证明。不能只强调条件更强就跳过反向论证。

故本轮结论是“已读定理未直接覆盖”，不是“一般命题已获正面答案”，也不是
“一般命题已确认为此前未知”。检索空白不足以排除其他术语下的代数余边界结果。

另一方面，有界两剪切结果没有填上上述三项一般缺口。Fix1 的整除及次数约束
先将 $f,g$ 压成各一个参数，再由 Fix2 排除 $ab\ne0$，留下的只是三角标量机制。
即使作者给出的非约化 Fix2 计算完全正确，其定位也是窄 ansatz 的短否定分类，
不是完成非交换多项式 Livšic。不能把“尚未找到一般代数化定理”用来放大这个
短消元结果，也不能靠加入旧 scalar tower／companion 构造补长。

## 7. 本轮交付状态

本报告完成八个核心一手入口的条件核查、两线各核心多角度查询、2024–2026 与
最近六个月覆盖、准确的直接覆盖／剩余差额及访问限制记录。
`NO_WORLD_PRIORITY_CLAIM`；`NO_NOVELTY_SCORE`；`NO_CAPACITY_PASS`。
仅创建本文件；未修改冻结原稿、旧报告、正式项目、账本、正文、实验或构建产物。
行数和 SHA256 在交付消息中给出，避免文件自哈希的循环依赖。
