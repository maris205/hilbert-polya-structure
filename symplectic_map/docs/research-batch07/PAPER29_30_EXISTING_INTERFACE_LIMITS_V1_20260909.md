# P29—P30 已有结果的可复用接口与限界 V1

日期：2026-09-09 UTC。执行者：/root/p29_p30_existing_interface_limits_v1。
类型：局部结果接口盘点；route_applicability: NOT_APPLICABLE。
本件不是候选排名、全球查新、旧论文完整重审、新证明接受或 PDF 验收；只新增本文件。
本次读取固定为 P30 V3，不因随后 V4 构建成功而改称读过 V4；不改变验收、页数合同或批次计数，P31 不提前选题或建项目。

## 1. 对象先于类比

P29 的实际接受入口由 README 与 notes/LOCAL_ACCEPTANCE_20260906.md 确认，是 paper-successor-20260906-transcription-v1/main.tex，不是旧 paper/。
本次复算所读接受源的 SHA，与接受记录指定的 SOURCE_BUILD_MANIFEST_20260906.sha256 对应条目吻合；没有读取或复验 PDF/build 树。
下文 P29/n、P30/nn 对应第 7 节所列源文件；数字均为实际源行号。

| 比较项 | P29 接受稿 | P30 V3 |
|---|---|---|
| 动力对象 | 特征零域上 $H_i(x,y)=(p_i(x)-y,x)$，$d_i\ge2$，宏步 $F=H_{k-1}\cdots H_0$ | 原 qPI 有理映射，$t'=st$，根单位回返；原八中心曲面、时间、谱矩阵及末端线固定 |
| “上同调” | $K[x,y]/(F^*-1)K[x,y]$，向量空间余核，不是商环 | $L_m=\mathcal O_S(mD)$ 的层上同调、实际常数截面和底环 Bockstein |
| “和／迹” | $S_ng=\sum_{j=0}^{n-1}F^{j*}g$，值在完整固定点代数 | $[z^r]\operatorname{tr}(A(s^{r-1}z)\cdots A(z))$，有序矩阵谱系数 |
| 有限精度 | 普通坐标次数滤过与有限支持词的包裹 | 混合特征先除 $p^a$，再约化或模 $\pi_a^2$；两相对状态方向 |

定义见 [P29/1:19–39](/root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/1_introduction.tex:19)、[P30/01:24–119](/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v3/sections/01-introduction.tex:24)。它们是不同系统族，不能以“辛”“上同调”或共有矩阵记号认定同族。
P29 自身的四维保参数辛 lift 则有真正同族接口：$K=\mathbb C(a),x=t,y=t-s,p=2x+V_t$，明确化成单 Hénon 基映射；见 P29/8:35–53。这不把 qPI 的变动时间认成该保参数 lift。

## 2. 差分工具：可以抽出的引理，不能省略的前提

**D1：有限支撑双向移位的余核。** 若向量空间有基 $\{1\}\sqcup\{e_{O,r}:r\in\mathbb Z\}$，且 $\sigma1=1,\sigma e_{O,r}=e_{O,r+1}$，每个向量只有有限个非零系数，则

$g=c_0+\sum c_{O,r}e_{O,r}\in(\sigma-1)V$ 当且仅当 $c_0=0$ 且各 $\sum_r c_{O,r}=0$；取 $u_{O,r}=-\sum_{s\le r}c_{O,s}$ 即得原函数，核恰为 $K1$。

这是 [P29/3:96–153](/root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex:96) 证明中可直接抽取的线性代数；其抽象步骤本身不需特征零。P29 的对象识别另由无限词基和宏步移位供给，不能只保留公式。
对 P30，未提供这样的无限置换基；其节点是有限八环，并有非平凡单位粘合。把 $F^*$ 改名 $q$，不产生 $L_m$ 的层序列，也不计算 $\beta_{L_m}(J)$。

**D2：保滤过原函数。** 在 D1 的基下，另要求 $V_D$ 恰由权重不超过 $D$ 的基向量张成，且每条轨道的权重下水平集是整数区间。
此时累计原函数只占据输入的最左、最右非零项之间，故 $g\in V_D\cap(\sigma-1)V$ 可取 $f,\sigma f\in V_D$。离散凸性是满足区间条件的充分条件，不是“有差分”便自动成立。
P29/3:28–94 用互异非零最高单项式保证无抵消，180–230 用实际相次数乘积证明离散凸；P29/4:23–51 再以核 $K1$ 得精确 rank-nullity。
P30 的 $L_j$ 增量不是这套普通次数滤过，$1-q^j$ 也不是 P29 Hilbert 变量 $1-t^{\delta+1}$ 的改名；不能移植保次数、Hilbert 级数或 $O(D^2)$ 未知数的搜索结论。

**D3：带单位粘合的有限环消元。** 对任意交换环 $B$，有限环节点差分 $B^n\to B^n$ 若每条粘合权为单位，消去前 $n-1$ 条边后，仅余 $B\xrightarrow{1-\lambda}B$，$\lambda$ 为定向总粘合；还保留 $n-1$ 个可缩的单位两项复形。
这是和 D1 同属初等差分计算的“有限闭环版”，不是 P29 无限轨道定理的直接特例；扭子、核及底变换必须由实际 $\lambda$ 决定，不能除掉 $1-\lambda$。
P30 已在原整节点帧中实际算出 $\lambda=q^{-j}$，并把目标乘单位 $-q^j$ 得 $1-q^j$；操作在底变换前固定，故兼容非约化底和 Bockstein。见 [P30/02:270–333](/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v3/sections/02-surface-pencil.tex:270)。
还需真实 $R\Gamma(S_B,\mathcal O)=B[0]$ 且常数映射为原 $1$，以及 $1-s^m\equiv-m\pi\pmod{\pi^2}$、$p\nmid m$。这些才给 $\ker\beta_L=k\langle1\rangle$；不是“常数核相同”的类比证明。
P30/06:61–110 继续用低层消失、原 $J$ 非常数和 $J-h\cdot1$ 的纤维正合列得到每条完整光滑 $X$ 上 $\kappa_J=\rho_X\beta_L(J)\ne0$。

## 3. 数字选择：共享算法，不共享被选的系数

**G1：唯一余数恢复。** P29 的混合进位前提是每位底数 $d_i\ge2$、位数有限且 $0\le e_i<d_i$。逐次欧氏除法唯一恢复指数词；再配合实际轨道最高项，才能得到普通次数编码和相位重编码置换 $\rho$。见 P29/3:70–94、P29/4:53–90。
P30/05:141–157 使用的却是特征 $p$ Frobenius 乘积中的谱指数：对交换特征 $p$ 系数环上的多项式 $f$，若 $\deg f\le2p-2$，则

$[Z^{p^a-1}]\prod_{i=0}^{a-1}f(Z)^{p^i}=([Z^{p-1}]f)^{1+p+\cdots+p^{a-1}}$。

精确前提还包括 $a\ge1$ 和非负指数；逐位约束 $\sum_i n_ip^i=p^a-1$ 在 $0\le n_i\le2p-2$ 中唯一迫使 $n_i=p-1$。系数自身也受 Frobenius 幂作用，不是随意只把变量替换为 $Z^{p^i}$。
奇素数实际取 $f=((T+hZ+Z^2)^2-4\varepsilon Z^3)^{(p-1)/2}$；特征二另取二次 $f=T+hZ+Z^2$，允许区间 $[0,2]$ 内唯一奇数是一。
支持界不可删：在 $\mathbb F_2[Z]$ 取 $f=1+Z^3,a=2$，则 $[Z^3]f^3=1$ 而 $([Z]f)^3=0$。这只是说明引理限界的直接代数例子，不是对现稿的反例或新实验。
P29 混合底数允许每个合法位唯一展开；P30 区间允许某些非目标位有进位，只有当前目标位链唯一。二者共享逐位剥离方法，不是相同的数字编码定理。
P30 接到 Hasse 乘子前，已独立供应 rank-two Cayley–Hamilton 递推、$S=T+JZ+Z^2,D=\varepsilon Z^3$、$dD=0$ 与谱系数选取，见 [P30/05:84–161](/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v3/sections/05-integral-trace.tex:84)。
P29 的词度数和 Hilbert 计数不能供应这些恒等式，更不供应高层原块所有扰动、时间完整 jet 的支持界；本件未读 P30 §§7–8 完整证明，不对其全链另发检查票。

## 4. “和”“原函数”和“迹”的三个不可替换处

**T1：动力周期和不等于矩阵迹。** P29 的检测来自包裹与宏步相容、完整固定点基、短词无混叠 $N=kn\ge3,N>2L(g)$；证明用 $nc_0=0\Rightarrow c_0=0$，所以不能忽略特征或 $n$ 是否可逆。
它检验 $S_ng=0$ 于完整代数，明确不是乘法算子的标量迹，也不是几何点取值；见 [P29/5:80–155](/root/autodl-tmp/symplectic_map/papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/5_periodic_detection.tex:80)。
P30 的可复用迹引理则要求有序因子均为同一 $A(s^jz)$、$s^r=1$、导数固定底／时间／谱变量，且提取 $z^r$。循环旋转不交换因子，得 $dI_r=r[z^r]Q_r$，从而在约化前 $p^{-a}dI_r=m[z^r]Q_r$ 整性；见 P30/05:13–48。
这不是 P29 的周期检测。特别是先约化得到 $\bar I=J^{p^a}$ 后再微分只会得到零，不能恢复 $\bar\alpha=H^\sigma dJ$。

**T2：局部微分原函数不等于动力差分原函数。** P30 的 $G_i=(I-F(j_i))/(p\pi)$ 来自原 $p\pi$ 迹同余和 ramified 整数 Taylor 多项式。
在光滑超奇异完整纤维上 $\bar G_j-\bar G_i=f_{ij}^p$，故局部微分粘成 $\nu$，连接类为 $\partial\nu=\mathrm{Fr}_*\kappa_J\ne0$ 于 $H^1(X,\mathcal O_X^p)$；见 [P30/06:259–340](/root/autodl-tmp/symplectic_map/papers/30-qpi-vertical-critical-ideals/paper/v3/sections/06-first-layer.tex:259)。
P29 解的是 $\sigma f-f=g$，既不是 $df=\nu$，也没有识别 $\mathcal O_X^p$ 这个像层。后续含入 $H^1(X,\mathcal O_X)$ 反而杀掉连接像，不能据词基余核把超奇异 Frobenius 说成可逆。
完整光滑亏格一使非零 $\nu$ 处处不消失，才供应第二方向的单位；随后 $(\widehat H+\pi A,\pi B)=(\pi,\widehat H)$ 是形式消元。这一步的对象责任不是数字选择能替代的。
因此模 $p$ 的 $H^\sigma dJ$ 本身不决定原完整理想。首层 $(\pi,H)$ 是全理想；高层陈述只到加 $(\pi^2)$，特征二长度五只是带沿纤维参数的截断横向长度，均不得升级精度。

**T3：不能移植 Hénon 的无不变量结论。** P29/3:245–315 先排除周期仿射素除子，才由极除子不变性证明有理原函数必为多项式及 $K(x,y)^F=K$。
该“极点支持被差分方程迫为周期”的论证可复用，但必须另有正则自同构及无周期极除子的前提；P30 有原非恒定回返积分和完整能级，不满足直接套用条件。同底域动力双有理共轭保持固定域，不能据表面形式把二者等同。
P29/8:60–136 的一般加法扩张引理确可原样复用，但前提是特征零差分域、已知完整常数域 $K=L^\sigma$、新增超越元 $r$ 且 $\hat\sigma r=r+b$。当前 P30 没有构造这样的扩张或常数域识别，故不是现成消费者。
P29 的单步单变量刚性及无有理 Liouville pair 还依赖特定 Hénon 反射、特征零和指定四维辛形式；P29/7:151–163 已明给正特征失效，不能移植到 qPI 超奇异层。

## 5. 现有 P30 是否已经扣除复用

答案是“已明确扣除共享工具，并已有同对象的证明简化”，不是“P29 定理直接证明了 P30”。
实际组合记录 [PORTFOLIO_DELTA:17–26、130–147](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_PORTFOLIO_DELTA_V1_20260909.md:17) 已扣除 P29 的差分两项对象、常数核、原函数、混合进位与逐词线性代数，并保留原 $L_m$—原迹—完整模型识别。
该记录 87–96 行明确这些是比较近邻，不因此捏造对 P29 的数学依赖；一般工具应归属真正基础来源。P29 自己也在引言 111–123、139–149 行明确基机制、系数和、加法扩张不是新框架。
P30 V3 引言 261–289 行已扣除 Hasse 迭代、Frobenius 差商／障碍、局部机制和“长度五／单位 $T$”的独立创新；§5 为这些消费者直接给出计算，没有把它们宣传成 P29 专属的新机制。
同对象 [PROOF_REUSE_DISPOSITION:24–38、47–60](/root/autodl-tmp/symplectic_map/docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md:24) 接受直接八环 Bockstein 和指定完整光滑闭 Hasse 接口；前者实际体现在 V3/02 节点计算与 V3/06 首层障碍中。
直接八环路线不需把旧全次数分裂体系机械装入当前消费者，但仍保留原常数／节点供应、原迹同余、完整曲面及真实 Jacobian／闭 Hasse 责任；这不是借 P29 删除 P30 必要证明，也不增加新意分。
上述旧记录的“未立项／下一项”等是当时快照，本件只引用其工具扣除和已接受接口，不拿它覆盖主控当前交付状态。

## 6. 盘点结论与数学风险

本次未遇到需升级为 P29 接受稿或 P30 V3 新缺陷的实际数学问题；这只覆盖列明的实读接口，不是整篇正确性重签。
可带走的是 D1–D3、G1、循环插入及加法扩张等带精确前提的引理；不可带走的是原对象识别、Hénon 无不变量、层 Bockstein 非零、原第二方向单位或更高厚度。
最有用的相互启发是明确“底变换前的实际基／节点帧”“支持界下的逐位恢复”“完整代数而非点集”的证明纪律；P30 已在相关接口落实，未发现尚可直接省去的对象证明。
跨 P29 Hénon 与 P30 qPI 的任何后续构造至多记作 ROUND2_CLUE；本件不生成候选、不给价值或新意排序、不授权 P31，也不把跨族类比充作族内下一题。

## 7. 本次实际输入身份与读取范围

以下 SHA-256 均本次对列明文件实际计算；“局部”不冒称全文读。定位搜索不等于全文阅读，旧报告结论不代替作者证明。
P29 根 A=papers/29-filtered-henon-cohomology/，接受源 S=A/paper-successor-20260906-transcription-v1/；P30 源 T=papers/30-qpi-vertical-critical-ideals/paper/v3/sections/；记录根 D=docs/research-batch07/。

| 输入（相对上述根） | 本次读取范围 | 实际 SHA-256 |
|---|---|---|
| A/README.md | 全文 | 3b3f5a7bc444ee5747201b71ebb2760d2a3730225951682972e35be762e0119f |
| A/notes/LOCAL_ACCEPTANCE_20260906.md | 全文 | efb0f0058ae55ab1ffb681581838df1b652985ed2d647ad0a3fbda467245c017 |
| A/notes/SOURCE_BUILD_MANIFEST_20260906.sha256 | 全文；只比对本次所读源 | 958dd5be31db838485feff5512ac675960ce7caa296f02c1f05b82b6b87e01ee |
| S/main.tex | 全文 1–49 | 2cf3dd2419e4349910055da786bed739e0de02177ba3f2fc869fb07c97df86ea |
| S/sections/0_abstract.tex | 全文 1–19 | 5b692a7a380f7af064d5be044c7ff02f6ff9bcd2b6566974839ceaa94f69e285 |
| S/sections/1_introduction.tex | 全文 1–160 | 7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8 |
| S/sections/2_orbit_algebras.tex | 全文 1–236，分段读取 | a36bebf59d412cc72ba52b38eb38da5f65cda0d0e79500642a7599004cb9520f |
| S/sections/3_filtered_primitives.tex | 全文 1–315，差分及滤过必要接口 | e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1 |
| S/sections/4_hilbert_series.tex | 局部 1–155：定义、重编码、主定理及证明开头 | e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884 |
| S/sections/5_periodic_detection.tex | 全文 1–166，和／迹与概形界面 | 862d363763a2a0dc3491903539ff0f5b0c75df7c8aed56f4c5af9d10eb4e21a8 |
| S/sections/6_effective_periods.tex | 局部 113–168、336–353；不核全阈值尖锐性证明 | fccfef37b05fafaff300a2f9a84f4796ca2ef902f365133c5069f459c89c271e |
| S/sections/7_univariate_rigidity.tex | 局部 1–70、145–163；定义、定理与明确边界 | ce400f2ae1a49abeb78b2f4045203aa24c6849b3213d4c0f0c4024cfe374c2cd |
| S/sections/8_symplectic_lift.tex | 局部 1–180、275–332；扩张接口、定理及结论 | d9c5d2279bc23ff4954bf0f2d20ff58b000b13e093ff09ad37791e5de8cce0d0 |
| T/01-introduction.tex | 全文 1–300 | 9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e |
| T/02-surface-pencil.tex | 局部 228–333：实际常数／整节点帧 | 573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f |
| T/05-integral-trace.tex | 全文 1–246 | 925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0 |
| T/06-first-layer.tex | 全文 1–394，原障碍—迹—完整理想接口 | f4232d918c4d78bacfc7c7a9dea2fbbe0aa60e634fbf27354d1708e02d84792d |
| D/PAPER30_QPI_VERTICAL_ALPHA_PORTFOLIO_DELTA_V1_20260909.md | 局部 1–27、72–96、130–149、301–314；另有关键词定位行 | 03219910add96d998bb3636f1d77e830be688d8852b437da7c8d01be9f3e6499 |
| D/PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md | 全文 1–67；只核复用处置，不代读全部上游 | 9656193743a15267572a4e10e7c80686338fdff44acf843a6a42576c8ea32fb9 |

工作入口另读 docs/WORKFLOW.md 全文、BATCH_07_CONTEXT.md 前 180 行；Phase B 仅搜索“扣除／数字”等匹配行，未作为本件数学证据或全球文献排除。
没有外网、编译、实验、修改旧稿／锁／接受记录、重扫构建树或对外操作。
