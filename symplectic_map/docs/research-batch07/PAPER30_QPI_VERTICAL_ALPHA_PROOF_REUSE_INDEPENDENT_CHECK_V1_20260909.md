# Paper30 qPI：垂直微分两处同对象证明复用的非作者检查 V1

日期：2026-09-09。检查者：`/root/p30_qpi_vertical_alpha_reuse_check_v1`。
类型：有界非作者数学及消费者检查；不是新意、容量、正式四门或论文准入票。
`route_applicability: NOT_APPLICABLE`；`proof_status: PROVABLE AS STATED`。

## 1. Claim 与结论

本件只检查以下两个冻结替代证明能否接入当前 V1–V3 的同一必要链：

- **A / DB**：[直接边界 Bockstein 复用](PAPER30_QPI_VERTICAL_ALPHA_DIRECT_BOUNDARY_BOCKSTEIN_REUSE_V1_20260909.md)，全文 173 行，
  SHA-256 `a9422fb7f580b1c44e94075181211e1c110245703b4004a8011ae16dfc82ec7c`。
  作者是主控 `/root`。仅替换 TH Step 1 的 U2A 供应，以及 Step 2 的常数上同调消失供应。
- **B / SH**：[完整光滑闭纤维 Hasse 复用](PAPER30_QPI_VERTICAL_ALPHA_SMOOTH_CLOSED_HASSE_REUSE_V1_20260909.md)，全文 242 行，
  SHA-256 `7fc2edb5e5200e499293effb569b328cdd974c3d01119f3aec948e72ee58e4af`。
  作者是 `/root/p30_qpi_nonunit_tau_layer1_v1`。仅替换 Hloc 对所选完整光滑纤维调用 Ffib 的特殊纤维前提。

结论：**DB.1–DB.3、SH.1–SH.3 全部 PASS；无必须修正项、无新发现的未闭合数学缺口。**
两项替换可与当前同哈希已接受的 V1–V3 消费者合取；原命题、原对象和原精度均未削弱。
这不是重新签发 TH／prime trace／OC／TB／P2／PI 六份旧新数学的全面审查票。
它也不证明这些同对象替代具有独立新意，或已经满足正文容量与正式准入条件。

已全文读取 249 行[必要链诊断](PAPER30_QPI_VERTICAL_ALPHA_PROOF_DEPENDENCY_AUDIT_V1_20260909.md)，
SHA-256 `b44ff43bf81163bb8f5a08e8a58f54bc8c3b32a81d78440b0d35c63ae3ef3672`。
该报告正确保留了当时尚未被替代的 U2A/Ssplit 和 Ffib 前两步供应。
本件接受的是现在另行写出、冻结并实读的新证明；不把旧诊断的保留决定当作禁止合法替代的权限文本。
旧诊断、两份替代作者件、TH 和旧证明图均未修改。

## 2. Assumptions、Notation 与检查策略

A 保持素数 $p$、$m\ge1$、$p\nmid m$、任意单位时间 $t$，以及 TH 的无分歧底域范围。
令 $\mathcal O=\mathcal O_0[\zeta_p]$、$\pi=\zeta_p-1$、$s=\widetilde\eta\zeta_p$、
$A_2=\mathcal O/(\pi^2)$、$k=\mathcal O/(\pi)$；$\widetilde\eta$ 精确阶为 $m$，$k$ 完美。
$S,D,U,L_n,\mathscr N,J$ 始终是原八截面模型、原反典范八环及原小阶迹积分。
不把 $J$ 换成新挑选的上同调基元；$1$ 始终是真实常数截面。

B 只处理 Phase A 原来已限定的完整光滑概形纤维 $X_h=(J=h)$。
闭值的有限剩余域扩张记为 $l/k$；它仍完美。令 $T=t_0^m\ne0$、$\varepsilon=(-1)^{m+1}$。
几何局部模型环是 $A=(\bar l[c]_{(c-h)})^h$，其剩余域为 $\bar l$，原基底参数仍是 $c$。
这是剩余几何中的普通 henselization，不是更改原算术状态提升的分歧条件。

检查策略是核对实际层态射、真实模型及指定类，而非比较抽象群的维数或两条谱方程的外观。
未变上游只核实实际调用边界；没有重复打开全部旧结论。
以下别名均指相同冻结原稿：

| 别名 | 文件与当前作用 |
|---|---|
| Ucoh | [通用上同调](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)：本次只需前两步真实常数／节点图计算 |
| Nbd、P | [边界法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)、[原极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)：单位帧、原中心与原 $J$ 非常数截面身份 |
| Gint、Gfield | [整模型](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)、[原完整 pencil](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md)：同一光滑曲面、完整纤维与几何连通性 |
| Hloc | [局部模型复用](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md)：L(a)、局部点提升和最小正则模型唯一性 |
| Jspec、Wreuse | [实际 Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md)、[Weierstrass V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md)：真实泛谱模／torsor 及全特征、原域谱前提 |
| Bbad、Ddiff | [准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md)、[整除微分](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)：纯 $W$ 模型、当前临界有限代数和实际 Cartier 计算 |
| TH、OC | [首层实际证明](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)、[障碍—Cartier](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md)：A 的直接消费者及保持不变的实际比较 |

## 3. Dependency Map：替换后的准确方向

1. 原八截面图与 Nbd 整单位帧给 $A_2,k$ 上的常数消失、相容边界复形。
2. 非共振低层消失加实际限制序列给 $r_0,r_1$；系数 Bockstein 自然性给 $\ker\beta_L=k\langle1\rangle$。
3. P 的原 $J$ 非常数与完整纤维 Cartier 序列给原 $\kappa_J=\rho_X\beta_L(J)\ne0$。
4. 同一个 $\kappa_J$ 进入未变 TH 的 prime trace／整数 Taylor／非约化四图接口，再进入 OC。
5. Gfield 的几何连通性加既定光滑纤维假设供应 Hloc 的 $X$ 侧特殊纤维条件。
6. Jspec／Wreuse／Bbad 仍供应真实泛 torsor 与另一侧模型；Hloc 给同一 $h$ 的完整几何同构。
7. 原完整谱微分的 Cartier 计算经该同构只把 Hasse 零性质送回原域。
8. 已接受 TB 的一形式恒等式与 V1 合取；PI 则继续直接消费原首层 $\nu$。两者依赖方向不混同。

其中没有 U2A 的通用分裂到 DB 的回边，也没有所求闭纤维同构到原泛 Jacobian 的回边。

## 4. A 的逐项检查与证明理由

| 检查项 | A 位置 | 结果与责任 |
|---|---|---|
| A1 实际常数上同调 | 75–89 | PASS：逐图吹起及 Leray 保留真实常数，对 $A_2,k$ 直接实施 |
| A2 整单位帧与非约化节点 | 91–106 | PASS：原帧仅除单位，分支差值序列真实正合，消元可同时约化 |
| A3 低层与首共振限制 | 108–124 | PASS：全部 $j<m$ 箭头可逆；$r_0$ 满射、$r_1$ 同构及真实常数核准确 |
| A4 系数短正合列与自然性 | 126–138 | PASS：平坦实际层给交换图，准确算得 $\beta_D=-\bar m$ |
| A5 原 $J$ 非核 | 121–124、137–138 | PASS：实际极除子给非常数截面，不需要人为归一 $r_0(J)$ |
| A6 小特征、空归纳及量词 | 111–117、132–142 | PASS：$p=2$ 使用特征四；$m=1$ 空归纳；全部 $p\nmid m$ 和单位时间保留 |
| A7 每条完整纤维限制 | 144–160 | PASS：原 Cartier 序列与指定平凡化给同一个 $\rho_X$ 和 $\kappa_J$ |
| A8 TH／OC 消费者 | 164–173；TH 72–194 | PASS：只替换指定供应，不改变原迹精度、符号、目标层或完整理想结论 |

### A-Step 1. 非约化底环上的实际几何没有被域上维数代替

Ucoh 105–149 的证明先在整基环上给相对吹起图与节点计算；A 重新在所需底环实施。
每个中心的两个相对参数给零截面吹起的两图，其局部模型为 $\mathcal O(-1)$ 的总空间。
投影的结构层推前为 $\bigoplus_{d\ge0}\mathcal O(d)$；有限标准覆盖计算所有高次上同调为零。
因此每步 $b_*\mathcal O=\mathcal O$、$R^ib_*\mathcal O=0$，八步后得到
$$H^0(S_A,\mathcal O)=A\langle1\rangle,\qquad H^{>0}(S_A,\mathcal O)=0.$$
这使用实际坐标变换和局部化，不以任意非平坦吹起的抽象基变换断言代替图计算。

已亲读 Nbd 的节点帧及四个传播比证明。四个点在不同分量上，坐标为 $1,t,t,s$，
均为单位，因而在 $\mathcal O,A_2,k$ 都不碰节点。
四个次数一限制中的指定截面是相应线性因子 $z-t$、$y-1$、$z-s$、$z-t$。
减去对应点截面后，它们给平凡线丛的实际单位帧；在无穷端的首系数同样是单位。
其余四个分量使用原 toric 单项式帧，不是由“次数零”独自推断任意底环上线丛平凡。
因此 $-1/t,-1,-1/s,-t$ 及乘积 $s^{-1}$ 是整单位公式。

节点环 $A[u,v]/(uv)$ 的两分支差值序列对非约化 $A$ 也正合：
相等常数项的分支多项式唯一拼成 $f(u)+g(v)-f(0)$。
结合各分量上同调消失，得到实际两项复形 $[A^8\to A^8]$。
前七个单位枢轴先在 $\mathcal O$ 上消去，再把次数一坐标乘 $-s^j$，得到
$$K_{j,A}=[A\xrightarrow{1-s_A^j}A].$$
这一固定整系数消元与系数约化、乘 $\pi$ 交换，足以计算真实边界 Bockstein。
这里无需也未断言整张曲面的通用导出直和分裂。

### A-Step 2. 实际限制与真实常数核

素于 $p$ 的根单位约化保持精确阶：若非平凡的素于 $p$ 阶根约化为一，
其几何和因子约化为单位，和 $(\zeta-1)$ 的乘积为零将迫使 $\zeta=1$，矛盾。
故 $1\le j<m$ 时 $1-s^j$ 在 $A_2,k$ 均为单位。
由边界有效 Cartier 序列逐层归纳，DB1 成立；$m=1$ 只有已证的 $n=0$。
在 $j=m$ 的剩余层，边界两项微分为零，长正合列准确给
$$\ker r_0=k\langle1\rangle,\quad r_0\text{ 满射},\quad r_1\text{ 同构}.$$
P 已在原完整模型证明 $J$ 的极除子为 $mD$，因而它是 $L_m$ 的非常数截面。
所以 $r_0(J)=b_J\ne0$，这不是把 $J$ 默认为某个分裂坐标。

### A-Step 3. 连接交换图及准确斜率

$S,D$ 对 $\mathcal O$ 平坦，两个相关层可逆，故系数序列
$$0\to k\xrightarrow{\pi}A_2\to k\to0$$
分别给实际层上的短正合列。原 $L_m\to i_*\mathscr N^m$ 与三项系数态射相容，
上同调自然性因此给 $r_1\beta_L=\beta_Dr_0$。
在共同固定的边界复形中，提升次数零生成元、求微分、除 $\pi$ 后约化得到
$$\beta_D(1)=\overline{(1-s^m)/\pi}=-\bar m,$$
因为 $\widetilde\eta^m=1$ 且 $1-(1+\pi)^m\equiv-m\pi\pmod{\pi^2}$。
$p\nmid m$ 使其可逆，故
$$\ker\beta_L=k\langle1\rangle,\qquad r_1\beta_L(J)=-\bar m b_J\ne0.$$
时间的任意单位提升没有被固定成 Teichmüller 代表；节点乘积中时间因子准确消去。

当 $p=2$ 时 $\pi=-2$、$\mathcal O=\mathcal O_0$、$A_2=\mathcal O_0/(4)$。
这是特征四环，不是特征二双数环；$m$ 奇数给 $1-s^m=2\equiv2m=-m\pi\pmod4$。
A 的“通常特征四”可在该假设下读成“实际特征四”，无需为此修改结论或冻结作者字节。
当 $m=1$ 时斜率为 $-1$，与空归纳完全相容。

### A-Step 4. 限制后仍是原来的类

P/Gfield 的原 pencil 使每个有限纤维与 $D$ 不交，且原截面 $J-h\cdot1$ 定义完整 Cartier 纤维。
真实常数截面 $1$ 在该纤维非零，故指定 $L_{m,k}|_X\simeq\mathcal O_X$。
剩余曲面 $S_k$ 上的实际序列
$$0\to\mathcal O_{S_k}\xrightarrow{J-h\cdot1}L_{m,k}\to L_{m,k}|_X\to0$$
和 $H^1(S_k,\mathcal O)=H^2(S_k,\mathcal O)=0$ 给出 $\rho_X$ 同构。
在覆盖 $X$ 的原开集用 $1$ 平凡化并取局部提升 $j_i$，连接的限制代表准确为
$$\rho_X\beta_L(J)=\left[\overline{(j_j-j_i)/\pi}\big|_X\right].$$
覆盖仅需覆盖 $X$；这句计算的是限制后的类，不需预先给整张曲面选择同一函数提升。
换提升只加余边界，故与 TH 的 Čech 符号及 $\kappa_J$ 完全一致。
已全文读 TH 219 行、OC 177 行；后续原 $p\pi$ 同余、四图延拓、A1–A4 与
$\partial\nu=\operatorname{Fr}_*\kappa_J$ 均不因更换 Bockstein 的计算证明而改变。

## 5. B 的逐项检查与证明理由

| 检查项 | B 位置 | 结果与责任 |
|---|---|---|
| B1 原完整纤维和同能级 | 85–102 | PASS：原 $1,J$ pencil，有限纤维不碰边界，不删末端点 |
| B2 光滑与几何连通 | 104–118 | PASS：得到几何整约化，伴随给亏格一，不再需该纤维的 Ffib 分量排除 |
| B3 $X$ 模型全部前提 | 120–131 | PASS：proper、flat、有限表示、正则与几何泛光滑均有实际供应 |
| B4 $W$ 模型与当前泛光滑供应 | 133–140 | PASS：保留原纯方程证明和完整有限临界代数，不由总空间正则推泛光滑 |
| B5 原泛 Jacobian／torsor | 142–146 | PASS：谱模、原状态逆、无核及原域下降全部保留 |
| B6 几何点与局部截面 | 148–158 | PASS：只在原 $c-h$ 的 henselian 局部底上取截面，不预设原域有点 |
| B7 最小模型双向延伸 | 159–165 | PASS：主纤维自交零给相对最小，指定泛同构及逆均延伸 |
| B8 原完整谱微分 | 167–188 | PASS：同 $h$ 两图、四端点、完整光滑模型和正则非零微分均核到 |
| B9 Cartier 与下降范围 | 190–209 | PASS：拉回基上显示系数正确；原域只返回零性质 |

### B-Step 1. 新特殊纤维前提确实足够

Gfield Step 3 经 Stein 分解排除了包括不可分次数在内的复合次数，供应所有几何纤维连通。
它并非只说一般纤维连通。对已假定光滑的 $X_h$，基变换到 $\bar l$ 后各局部环正则。
两个不同不可约分量不能相交；Noetherian 曲线只有有限个分量，因此这些分量开闭。
几何连通性遂强迫唯一分量，且光滑性保证约化。
原类 $X_h\sim mD$ 和 $K_S=-D,D^2=0$ 给 $p_a(X_h)=1$；光滑整曲线的几何亏格同为一。
伴随公式在整数交数中除以二，不排除特征二、三；$m=1$ 也无额外步骤。

这只替换 Hloc 所选光滑特殊纤维的前提，不证明所有有限奇异纤维整约化。
Ffib 128–245 的旧整数格及分量排除已按供应边界亲读；没有发现其他部分因此也必须重审。
Gfield 的完整泛光滑证明仍保留，不能把“算术亏格一”直接当作全部小特征泛光滑。

### B-Step 2. Hloc 的其他前提未被压缩掉

原光滑整曲面到原基曲线的局部 DVR 模无挠，给平坦；射影性给 proper。
局部化再作 Noetherian ind-étale henselization 的正则性，与 Hloc 已接受的实际接口一致。
$\mathscr X$ 的特殊纤维条件现在由上一小节供应，其几何泛光滑亏格一仍由 Gfield 供应。

另一侧 $W$ 的唯一无穷远点相对光滑；任何几何正次数分量必须与无穷远相交，
所以多个或重分量将破坏该点光滑性。平面超曲面无嵌入分量，得到完整几何整约化纤维。
三次 Hilbert 多项式、射影性与实际偏导给 flat、proper 及总空间正则。
泛光滑继续由 Bbad 的纯临界理想和完整消元
$$Z_W\simeq\operatorname{Spec}\bar l[z]/((T-z^2)^2-\varepsilon Tz)$$
供应；首一四次使其有限，泛化后为空。这不消费实际动力临界长度或乘 $c$ 特征多项式。

Jspec 的谱代数模线丛族、原 $x,y$ 有理逆、不可分次数排除、固定循环除子差、
不变 Picard 单位分支、全群固定点无核证明，以及原域上的作用下降均仍在必要链。
Wreuse V2 Step 2a 仍供应任意原域接口，不能只在代数闭常数域作比较后称其自动下降。
因此用于 Hloc 的确为原泛曲线的真实 $E$-torsor，而非未知核同源；
Bbad 原点检查给带原点的 $E_L\simeq W_L$，能级参数没有改变。

### B-Step 3. 同一局部参数上的完整同构

在 $\bar l$ 上取光滑几何点，étale 坐标与 henselian 点提升产生 $e_A$。
这没有制造 $X_h(l)$ 的点或 $k(c)$ 的全局截面；只平凡化基变换后的局部泛 torsor。
两个模型特殊纤维都是唯一重数一竖直整分量，且为 $c-h$ 的主 Cartier 除子，
正规线丛次数为零。因此没有竖直第一类例外曲线，满足 Hloc 正亏格最小正则 proper 模型的前提。
将指定泛同构及其逆分别延伸，两复合由泛纤维概形稠密和目标分离为恒等。
得到的是同一 $c=h$ 的完整特殊纤维同构，不是只在环面上的双有理对应。

### B-Step 4. 闭谱几何和 Hasse 零性质

由完整同构已知 $W_{h,\bar l}$ 光滑，再用原两图的开集互逆变换与四端点偏导
$-T,T,-1,1$ 证明完整 $E_{h,\bar l}$ 光滑。
原有限平坦推下 $\mathcal O\oplus\mathcal O(-2)$ 给射影、几何连通和亏格一，因而几何整。
这时开集同构才延伸成完整 $E_{h,\bar l}\simeq W_{h,\bar l}$，并与原 $X_{h,\bar l}$ 对接。

原 $\omega=dZ/(2\lambda-(T+hZ+Z^2))$ 在有限分母消失处以 $-d\lambda/\Phi_Z$ 表示，
在无穷远以 $-dV/(2\mu-(1+hV+TV^2))$ 表示；光滑性与端点单位保证完整正则性。
例如 $Z=\lambda=0$ 处 $\Phi_\lambda=-T$，$Z$ 是局部参数，故该微分非零。
奇特征 Cartier 提取次数不超过 $2p-2$ 中唯一的 $p-1$ 次项；特征二只提取 $hZ$。
因此对原指定谱微分及其几何拉回微分，显示系数确为 $H_p(T,h;\varepsilon)^{1/p}$。
若改微分基为 $a\omega$，系数变为 $a^{1/p-1}H_p^{1/p}$；数值规范并非任意换基不变。
但 Cartier 是否为零不变，并恰检测几何 Jacobian 的超奇异性。
域嵌入 $l\hookrightarrow\bar l$ 只下降这个零性质；B 没有声称几何点或所选曲线同构也下降。

## 6. 与 V1–V3 的合取及替换边界

已全文读 [Phase A](PAPER30_QPI_VERTICAL_ALPHA_SCOPE_PHASE_A_V1_20260909.md)、
[全 tame 接受](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_MATHEMATICS_DISPOSITION_V1_20260909.md)及
[全素数接受](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md)。
Phase A 中 V3 待审文字是旧快照；本次按最终同字节接受接续，不修改快照。

| 当前消费者 | 新供应后的结论 | 不改变的边界 |
|---|---|---|
| V1／TH | DB 给同一 $\kappa_J$；SH 给原完整光滑闭纤维几何／Hasse 身份；原 $\mathfrak c(\alpha)=(\pi,\widetilde H)$ 保持 | prime trace 的整 $p\pi$ 同余、OC A1–A4、两方向理想及全部末端点均保留 |
| V2／TB | 已接受的一形式因子分解与同模型 V1 合取，仍为 $(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1})$ | TB 代数证明不先消费 V1；仅模平方，超奇异状态仍只给至少二 |
| V3／PI | 保持实际特征四比较 $\chi_m|_{T_X}=\nu$，再接全高层 P2 因子分解 | 首层特征四与高层特征二商不合并，混合项及底参数作用不删 |

首层保持完美剩余域；TB 和 PI 几何保持其各自有限剩余域范围，不因 SH 的几何论证而扩大。
无分歧状态准确阶／下界、Hasse 根重数和完整／截断理想的区别全按现有消费者。
两替代没有核准奇异能级、额外分歧状态、全厚度、全初始理想或新的典范模同构。

在这条特定链中，A 使 Ssplit 通用整数截面、逐级扩张分裂和 U2A 不再承担该 Bockstein 供应；
Ucoh 前两步的实际常数／节点证明仍保留。B 使 Ffib 前两步不再供应所选光滑纤维前提。
这不允许整包删除旧正确结果，也不影响其他仍消费这些结论的旧任务。
Jspec 全谱模链、Wreuse 实际谱几何及原域接口、W0 当前有限代数、Hloc 双向延伸和 Ddiff Cartier 都保留。
必要链缩短属于同对象证明复用；不能把替换本身或节省的段落算作新 finding、新意加分或容量票。

## 7. 实读责任、身份及 Corrections / Open Risks

本人不是 A/B 作者；任务开始后收到冻结 A，B 终态消息及哈希到达后才全文消费 B。
已知研究方向与旧接受状态，不称盲审、跨模型认证或 fresh 正式四门票。
另委派 `boundary_sanity` 作两份作者件的只读内部反例／边界辅助检查；其没有读取旧供应链，
没有写文件，也没有为上游几何代签。本文旧输入真实性和消费者核对由本人亲读承担。

实际读取范围：A 1–173、B 1–242、依赖诊断 1–249、TH 1–219、OC 1–177；
Ucoh 1–149；Nbd 全文 1–284 与 P 1–270 的模型／极除子证明；Gfield 全文 1–270；
Gint 1–150、210–246；Hloc 1–110、165–307；Wreuse V2 全文 1–213；
Jspec 1–126、214–454；Ffib 128–245；Bbad 138–167、217–251、305–365；Ddiff 206–233。
Phase A 与两份现行数学处置全文；TB／PI 仅定向读其实际输入与消费者接口，不冒称本次重审全文。
AGENTS.md、WORKFLOW.md 与 proof-writer 已全文读；批次接续只用于定位当前分支，不作为数学证明。

| 实际核对对象 | SHA-256 |
|---|---|
| Ucoh | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| Nbd | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| P | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` |
| Gfield | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |
| Gint | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| Jspec | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| Wreuse V2 | `21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2` |
| Bbad | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |
| Hloc | `0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e` |
| Ddiff | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| TH | `43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75` |
| OC | `81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa` |
| Phase A | `ca6a8e6695709c2eaaff4707bcb94ccfd86367afb492d5ea87da6a1d90396f2f` |
| 全 tame 接受 | `a71577e3bbced32f05b1546b9a6373a4d977ce1f60bcb5dce7e7e8ce5f3e8302` |
| 全素数接受 | `e1d2897841fa89b95f8339a9af64f0901183cef47d49be75076f7a18b6ab5cc8` |
| TB | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| PI | `1d2ff70c69cb26ec2009055f3161cb44758338db8912b9654ab8c53b5d7c59d3` |

无必要修正、无新数学阻塞；未读的旧独立出口不因此获得新的核准。
仍须保留的风险是范围风险：把光滑概形纤维缩成支集、把 Hasse 零性质改写为任意原域基下同系数、
把共同首层 Bockstein 推广到任意高度，或把几何同构宣称自动下降，均不由本报告支持。
proof-writer 的实际作用是强制分开命题、假设、真实依赖与可下降结论；没有要求扩大本任务。

本报告是唯一新增文件；已作全文回读和定向输入身份核对。
没有修改上游、索引、稿件、锁或接受产物；没有数值实验、GPU、联网或外部写入。
所有旧失败、新意 C/D 的谨慎继续状态、完整自然正文要求及正式双份准入责任保持不变。
