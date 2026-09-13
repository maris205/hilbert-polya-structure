# Paper31：全实旋转／twist 完整候选的必要证明图 V1

批次日期标签：2026-09-12；文件名不是独立执行时钟认证。
整理者：`/root/p31_real_candidate_proof_map`；唯一写入为本件。
状态：DEPENDENCY_MAP_ONLY / ACCEPTED_MATHEMATICS_REFERENCED / NOT_FORMAL_VERDICT。
本件整理同一 C1 中心的完整证明负担，不是新证明、重新数学审查、来源排除、新意／价值票或容量票。

## 1. 用途、接受和本人阅读的区别

[最新处置][PF0] 保留唯一上轮非正式 C/D **6.5/10 — PROCEED WITH CAUTION**。
[数学处置][MD] 接受 G/B/M/U/I/S 六稿的明列量词；[PF0] 接受 Q/Z 两个新增来源接口。
MA/MB 是同一非作者的两阶段新增量审查，QR/ZR 亦为同一非作者的两阶段接口审查；均不是正式双席。
作者稿中的 pending、局部未完成项是冻结快照；后继 S/MD/PF0 已闭合的义务不重新标成 OPEN。
本整理者 FULL 读 PF0、MD、A、G、B、M、U、I、S、FRC、Q、Z；不继承任何他人的 FULL 标签。
本人对 MA/MB/QR/ZR 只读下面注明的接受／actual-scope 段；没有自称完整重审四报告。
完整正式席必须自己读本件 §8 的全部 FULL 文件及 §9 的全部指定旧段；读入不等于重新给旧阶段投票。
新 brief、本件、终态来源补单、查新／组合记录及共同 manifest 由主控另行绑定，不以本件代替完整共同输入。

## 2. 共同对象与完整 C1／C2／C3 量词

对每个固定 $T>0$，取原八中心曲面 $\mathcal U_T=S_T\setminus D$，保留四条完整 terminal affine lines。
只将原乘子置为 $1$；固定时间 $T$ 不被置为 $1$。原 torus 上
$$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad h=-x+y+x/y-T/x.$$
每个有限实正则纤维完整地对应
$$E_h:\ v^2+huv-Tv=u^3-Tu^2,\quad O=[0:1:0],\quad P=(0,T),\quad F_T=+P.$$
令 $T=w_\pm^3(w_\pm-1)$，$w_-<0<w_+-1$，$h_\pm=w_\pm(3-2w_\pm)$。
全部有限实坏值恰为两个简单根 $h_-<h_+<1$；所有结论覆盖三个正则开区间的每个能量。
始终取 $\omega=du/(2v+hu-T)$ 的正方向、完整正实周期 $\Omega$ 及 $(0,1)$ 中真实正向积分提升。
下外 $L=(-\infty,h_-)$ 有两圆，$F_T$ 分别保持它们，共同角为 $\rho_-$。
中间 $C=(h_-,h_+)$ 只有一圆，$F_T$ 的角为 $\rho_0$。
上外 $R=(h_+,\infty)$ 有两圆，单步交换，最小分支回返为 $F_T^2=+2P$，共同角为 $\rho_+$。
三个函数各自在完整区间实解析；不能把 $\rho_+$ 当单步角，也不能拼成跨三段的同一实值提升。

### C1：唯一主 finding——全正则实能级的严格五行分类

↑／↓ 表示导数处处严格正／负；↑↓ 表示准确一个简单导数零点，且 $\rho''<0$，其前增后减。

| 固定时间 | $L$：$F_T$ | $C$：$F_T$ | $R$：$F_T^2$ |
|---|---|---|---|
| $0<T<3/16$ | ↑ | ↑↓ | ↑ |
| $T=3/16$ | ↑ | ↓ | ↑ |
| $3/16<T<1$ | ↑↓ | ↓ | ↑ |
| $T=1$ | ↓ | ↓ | ↑ |
| $T>1$ | ↓ | ↓ | ↑↓ |

因此除 $T=3/16,1$ 外恰有一个有限实正则驻点能级；这两个特殊时间没有。
外区间的一个驻点能级含两圆，不是两个能级；不允许遗漏水平拐点或退化零点。
$T=3/16,h_-=-2$ 的持续光滑圆另有非退化极大，但该能级奇异，不计入正则表。

### C2：同一原状态的六端点、七值域和回返匹配

设 $\theta(T)=\frac12+\pi^{-1}\arctan(1/\sqrt{3-4w_-})\in(1/2,2/3)$。
三个区间的左／右端准确为 $(5/8,\theta)$、$(\theta,1/2)$、$(0,3/4)$。
当极大存在时，以 $M_-,M_0,M_+$ 表示其唯一准确值；它们均小于 $1$，且严格超过对应两端。

| 区间及参数 | 准确值域 |
|---|---|
| $L,T\le3/16$ | $(5/8,\theta)$ |
| $L,3/16<T<1$ | $(\min\{5/8,\theta\},M_-]$ |
| $L,T\ge1$ | $(\theta,5/8)$ |
| $C,T<3/16$ | $(1/2,M_0]$ |
| $C,T\ge3/16$ | $(1/2,\theta)$ |
| $R,T\le1$ | $(0,3/4)$ |
| $R,T>1$ | $(0,M_+]$ |

其中 $\theta=5/8$ 恰在 $T=(1+\sqrt2)/4$，仅改变较低端点，不是额外 twist 数目阈值。
$h=1$ 是合法上外四阶能级，$\rho_+(1)=1/2$；$h=9/8$ 同样正则且导数严格正。
极大能量由 S §6 的唯一实积分解刻画，再用真实实弧评价极大值；不声称初等闭式。
在 $L$ 或 $C$ 的相应极大存在范围，$h_m$ 是其区间内（排除锚点 $h_-$）的唯一解
$$\int_{h_-}^{h_m}\frac{(32T+3s)\Omega(s)}{(8s-9)^2}\,ds=0.$$
上外仅当 $T>1$ 有极大，其 $h_m>9/8$ 是唯一解
$$\int_{h_m}^{\infty}\frac{2(32T+3s)\Omega(s)}{(8s-9)^2}\,ds=\frac14\log T.$$
两个式子使用各区间实际完整周期；后式的绝对收敛由 I 的 $\Omega=O_T(\log s/s)$ 给出。

### C3：C1 必需的带一阶导数控制的边界常数

写 $\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$，$q=8h-9$，$H=32T+3h$。
此处 $q$ 不是原乘子，也不是 Tate 参数。固定 $T$ 的能量导数记为撇号，$J_\pm=(\delta/q)\Omega_\pm^2\rho_\pm'$。
对每个固定 $T>0$，
$$J_-(-\infty)=\frac18\log T,\qquad J_+(+\infty)=-\frac14\log T,$$
两者误差均为 $O_T(\log|h|/|h|)$，包括 $T=1$ 的准确零极限。
I 的完整周期常数、短弧两个移动尺度和可微余项实际承担此证明；不对未控制的 $o(1)$ 求导。
常数与充分大的能量阈值可依赖固定 $T$；不申报 $T\to0$ 或 $T\to\infty$ 一致性。
C2 是同一中心的结果，C3 是必要分析支撑，不拆成三个独立 finding 或三篇论文。

## 3. 必要依赖图：证明承担者与接受记录分栏

| 义务 | 真正证明位置 | 数学接受／下游 |
|---|---|---|
| O1 原八中心、四末端、完整有限曲线及完整映射 | S02/F30/R30 的 §9 指定段；FIX Step 1；G Step 4 | P30 已接受基础；实数当前接口由 MA、MD 接受 |
| O2 全部实坏值及原 $+P$、组件和最小回返 | G Steps 1–5，51–193 | MA、MD；进入全部 C1/C2/C3 |
| O3 同规范非齐次 Picard–Fuchs 方程 | FRC Claim/Assumptions、Steps 1–2，7–60、71–151 | RG §§3.1–3.2；FMD §2.1；供 B/U |
| O4 acnode 持续圆解析性、真实 $J(h_-)=0$ | G Step 3，130–139；B §§3–4，59–115 | MA、MD；零点上界及 $3/16$ 符号 |
| O5 中区间两个端点、极大实际存在 | M §§2–5，35–104 | MA、MD；C1 中列、C2 |
| O6 上外真实 $2P$ 弧、$h=1$ 和 node 端点 | U §§2–3，28–66 | MB、MD；C2、上外有限符号 |
| O7 二倍 forcing、$q=0$ 延拓及至多一个极大 | U §§4–5，68–100 | MB、MD；C1 上列，不删除 $9/8$ |
| O8 两端根尺度、完整积分常数、短弧双尺度 $C^1$ 界 | I §§3–6，57–200 | MB、MD；C3 及外区间存在阈值 |
| O9 全参数严格性、六端点、七值域、唯一积分解 | S §§2–6，31–127；B/M/U/I 的对应输入 | MB、MD；完整 C1/C2 |
| O10 整个正域与下外无 terminal 圆同一 | Q Steps 1–4，42–87 | QR、PF0；经典特例扣除，不增加 finding |
| O11 CGM 映射、能量、迭代和方向一致 | Z Steps 1–4，41–93 | ZR、PF0；下外结果严格传递，不授优先权 |

最小逻辑顺序：O1 → O2；O2+O3 → O4/O6/O7；O4+O5+O7+O8 → O9。
源桥 O10 → O11 只消费已接受的 O2/O9；它不反过来替代全实分类的证明，也不成为第四个中心。
本件所有“接受”均指所链接历史记录，不是整理者新独立验算所得的 PASS。

## 4. 原完整模型：不能以泛方程或有限点集替代

S02 的八中心专门化为原乘子 $1$、时间 $T$；$D=-K_S$ 与 $(h)_\infty=D$ 固定完整原空间。
F30 Steps 1–2 的整数正交格及正整数重数证明所有有限纤维几何整、约化、算术亏格一。
在 $r=1$，其 $0<\ell_j<r$ 分支为空；不消费一般 $r$ 的法丛阶或整条高阶上同调链。
S02 的无基点和有限纤维完整性、F30 的原临界计算、R30 的全部合法状态正则同构缺一不可。
指定有理式及逆式是
$$\phi(x,y)=\left(T/y,Tx(y-1)/y^2\right),\qquad x=Tu/(T-hu-v),\quad y=T/u.$$
FIX Step 1 明确核定 $\phi F_T=\tau_P\phi$，不是 $-P$、未知倍点或另一个自同构像。
FIX 119–139 用双方正则最小 proper 模型作全有限基延拓和分离粘合；S02/F30/S03 给其实际几何假设。
但 FIX/FXD 原完整声明的常数域是特征 $p>3$；不得直接把该旧概形定理标成实数定理。
当前实数所需的完整正则纤维同构及动力等式，在 G Step 4 自行使用光滑射影曲线延拓和分离性证明。
所以当前 C1/C2/C3 不依赖“将正特征 PASS 自动移植到特征零”，也不要求重审节点固定理想。

| 原 terminal 图 $(a,b)$ | 原 $(x,y)$ | 能量限制 | 完整像 |
|---|---|---|---|
| 1 | $(a^{-1},1+ab)$ | $1-b$ | $-2P=(T,T(1-h))$ |
| 2 | $(a(T+ab),a^{-1})$ | $b/T$ | $-P=(0,0)$ |
| 3 | $(a(T+ab),a^2(T+ab))$ | $b/T$ | $O$ |
| 4 | $([a(1+ab)]^{-1},a^{-1})$ | $1+b$ | $P=(0,T)$ |

四点两两不同；下外都在 $C^0$，中区间都在唯一圆，上外每圆两个。无合法末端被删除。
F30 的末端能量导数均非零；R30 另覆盖第四末端原点与 torus 分母零 locus，不能只保留一般末端点。
一般 $r$ 的谱 Jacobian、torsor 选点、Picard 非挠增长和有限域全周期清单不是当前直接 $+P$ 识别的必要额外链。

## 5. 旧 forcing 的全部必要证明，不以消费者式子代替

FRC 使用 $X=u+(h^2-4T)/12$、$Y=v+(hu-T)/2$，故纤维内 $dX/(2Y)=\omega$，无额外依赖 $h$ 的缩放。
固定 $X$ 的 $D=\partial_h$ 与移动截面全导数须区别；$P$ 在短式上为 $((h^2-4T)/12,T/2)$。
这里 $Y^2=f(X)=X^3+aX+b$ 的系数见 FRC Claim，$f_h$ 固定 $X$ 求偏导，$\kappa=8/q-\delta'/\delta$。
FRC Step 1 逐多项式恒等式 G0 给真实 Gauss–Manin 还原 G1，再消去第二类微分得到 G2。
其 $\beta=-q/\delta$ 消去造成 $q=0$ 表观极点，$\mathcal L$ 的零阶项由实际有理恒等式确定。
FRC Step 2 不将两个发散的 $R_j$ 各自置零；组合 primitive $Q$ 的极部抵消且 $Q(O)=0$。
两次 Leibniz 的全部移动端点为
$$\frac{X_P''-\kappa X_P'}{2Y_P}-\frac{2X_P'f_h(P)+(X_P')^2f_X(P)}{4Y_P^3}.$$
不能因为 $Y_P'=0$ 删除固定 $X$ 下的 $f_h(P)$；该项与 $Q(P)$ 的相消才给非齐次 forcing。
由此在 $q\delta\ne0$ 有
$$\mathcal LI=-\frac H{q\delta},\quad\mathcal L\Omega=0,\quad
\mathcal L=\partial_h^2+(\delta'/\delta-8/q)\partial_h+\frac{8h^3-18h^2+9h-12T}{q\delta}.$$
RG 72–139 记录原非作者对此整条链的核验，FMD 24–34 明确接受；旧 brief 的 V1a 只是消费者。
完整正式席 FULL 读 FRC 267 行以保持原证明身份；其 Steps 3–5 的正特征消费者不进入本实候选结论。
其 UV 来源校正是方法背景；这里的 G0/G2/端点已显式自证，不因未追加外文读取而制造证明缺口。

## 6. 新全局链的易错义务与实际落点

G 的 $\mathbb RP^1$ 持续圆参数化给跨 acnode 双侧解析周期；B §3 才据此固定 $J(h_-)=0$。
B §4 的 $H(h_-)=w_-(2w_-+1)(4w_--3)^2$ 给 $T=3/16$；仅有 $J'=-H\Omega/q^2$ 不给全局符号。
M §§3–4 分别用显式有限 acnode 积分、短弧有界与 Fatou 的完整周期发散给两个端点；§5 才得到“恰一个”。
U §2 的有符号 $s_2(h)$ 在 $h=1$ 解析；不得对 $\operatorname{sign}(h-1)\sqrt{T-r_3}$ 形式求导。
U §4 使用局部 $\log(2P)=2\log P$ 模固定整数周期，故 $J_+'=-2H\Omega/q^2$，倍率不能漏。
在 $h_q=9/8$，$K=\delta\Omega^2\rho_+'$ 解析，$qK'-8K=-2H\Omega$ 给 $K(h_q)=H\Omega/4$。
因此 $\rho_+'(h_q)=H/(4\delta\Omega)>0$；$J_+$ 有单极而真实旋转函数无奇点。
I §3 以解析根方程给 $D\sim1/(4\varepsilon^2)$、$d\sim4T^{3/2}\varepsilon^2$，不是数值根表。
这里仅沿用 I 的局部记号：$\varepsilon=1/|h|$、$D=r_3-r_1$、$d=r_3-r_2$、$\kappa=\sqrt{d/D}$，与 FRC 的 $D,\kappa$ 不同。
I §4 自证完整积分 $\log(4/\kappa)$ 与 $\kappa\partial_\kappa$ 余项；§5 同时控制两个移动尺度的偏导。
I §6 先求导再相消得两个准确 $J$ 常数，误差覆盖 $T=1$，不靠除以 $\log T$ 的推导。
S §§4–5 将无穷零极限与严格单调的 $J$ 合取：$T=1$ 两外区间仍严格，没有“极限为零所以导数为零”。
S §6 的下方积分排除锚点 $h_-$，上方从无穷积分且绝对收敛；唯一性先由符号证明，不循环定义极大。

## 7. 源桥的方向和声明边界

Q 证明 $D(x,y)=(-x/y,-y)$ 在整个 $x>0,y<0$ 正域与正象限之间双向共轭，$G_T=-h$。
适当能量、唯一极小和双曲坐标证明每个非平衡正域能级就是下外无 terminal 的完整 $C^1$，不是开弧。
BR2005 的准确固定特例是 $(T,0,0,1)$；倒数缩放后为 $(T^{1/3},1,0,0)$，均需扣除经典身份。
Q 当时没有核角度定向，不能仅凭 QR 的代数 PASS 与某个 BR 角直接比较极大／极小。
Z 后继闭合 CGM：$\Phi_T=(T^{2/3}/x,-T^{1/3}y/x)$，$\Phi_TF_T\Phi_T^{-1}=L_0\circ L_{T^{1/3}}$。
原一次迭代对应文献两次交替更新，不是原 $F_T^2$；$E=-h$；原 $\omega$ 正向准确对应 CGM 逆时针。
所以 $\rho^{\rm CGM}_{0,\lambda}(E)=\rho_T(-E)$，不取补角，且 $E>-h_-$、$\lambda=T^{1/3}>0$。
按 $E$ 增大，$0<\lambda\le(3/16)^{1/3}$ 递减，中间到 $1$ 唯一非退化极大，$\lambda\ge1$ 递增。
全部零参数正边界的 $5/8$ 极限由原下外结论严格传递；不声称首次证明或解决正二参数全平面。
PF0 记录的 BR 后段、BC 主定理、Duistermaat 强正文缺读须按同轮来源补单的真实终态处理；本件不自行改变。
CGM p18 的末条 “decreasing” 与严格传递不符，原文字保留；数值列表不升级旧定理，差异不作为首创证书。

## 8. 正式席必要 FULL 数学／断言输入与文件身份

以下 FULL 是未来每位完整席的本人阅读要求，不是声称本整理者已 FULL 读四份数学报告。
每个链接指准确原文件；数字为整文件行数／bytes，SHA256 绑定整文件。

| ID／文件 | 行／bytes | SHA256 |
|---|---:|---|
| [PF0 当前处置][PF0] | 130／11107 | `0923e18bd1286daa421a5656cffe8f4bb31aaa3e1a7ffd2ba8030f0fbcd25ce1` |
| [MD 全局数学接受][MD] | 135／10371 | `c3325516b39ad2595863de544f7db577c6a65f72511f379c1f566a8aae8c568b` |
| [A 原 C1/C2/C3][A] | 77／5629 | `18076931181e67484cf6d676cf94438d719c1575014ed4e4b5819f388964ff6a` |
| [G 实几何][G] | 208／11847 | `f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196` |
| [B acnode 锚定][B] | 144／7701 | `9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d` |
| [M 中间端点][M] | 115／6053 | `4b07925048eb416d431d1e924c7d54a46c90c1a9b08708b6647c4430a79860a3` |
| [U 上外有限回返][U] | 112／5614 | `beaff1ed89c8f99b71f241340c5833d74ab1debfebf0c408335d2e4ed3dd5bff` |
| [I 无穷 C¹][I] | 215／11115 | `a6949cdae36598dd7b6d607e32f172321edeb046ebb08d1fab63dd9fa23191f6` |
| [S 全局合成][S] | 133／6753 | `63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24` |
| [FRC 原 forcing 证明][FRC] | 267／10608 | `c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b` |
| [Q 正域对应][Q] | 140／8737 | `089df2e31231d3bf2288525dd2fd99f7c3a7fda0f01fb98d2fb7543715cb0c44` |
| [Z 零参数桥][Z] | 123／7175 | `3c5809411c9979b6d6702dbb867af85fce78dff15fb568fddabc204dbc2d5ceb` |
| [MA 第一阶段接受报告][MA] | 212／14963 | `e00f5e920b9a66213e22709e3a7379161d311ee2f735473ba597171ab8d305e8` |
| [MB 第二阶段接受报告][MB] | 201／14712 | `5e99316e1e20caca644ffe76724d86a62e791e7276e2168bb8527e230f2c5320` |
| [QR 正域接受报告][QR] | 97／6141 | `279651002d1ec3dfa6ba7eaae3feaf65a16f7eddf071ad92b93b66cb8ab274aa` |
| [ZR 零参数接受报告][ZR] | 107／7140 | `e70025868b6dd4321435dc6667456de0c2c70918ffad11fd7c488c7d3a89809d` |

本人实际只 PARTIAL 读 MA 1–49、196–212；MB 1–51、187–201；QR 1–25、83–97；ZR 1–25、89–107。
这些范围足够确认其接受结论、输入身份、独立角色及实际范围；不用于冒领其完整逐式核验。

## 9. 正式席必要 PARTIAL 旧输入：精确范围及足够性的理由

| ID／文件；整文件行／bytes | 必须本人读取的闭区间及消费理由 | 整文件 SHA256 |
|---|---|---|
| [S02 原曲面][S02]；446／20456 | 1–226、388–437：八中心/四末端、极除子/无基点、flat/泛光滑、有限完整性；一般法丛阶段不进入 $r=1$ 的下述证明 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [S03 cubic 几何][S03]；438／19219 | 1–111：记号及 finite-critical lemma 的完整证明；总空间正则、proper/flat、每条纤维整约化和原奇点消元；不消费后续谱 Jacobian | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |
| [F30 原有限纤维][F30]；466／22170 | 7–26、66–92、128–245、362–416：假设、整 Picard 基、Steps 1–2 的全有限整约化证明及 Step 7 原自治全部临界/terminal 消元；$r=1$ 的中间法丛分支为空 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| [R30 完整原映射][R30]；368／16747 | 1–18、54–70、107–160：映射/末端记号与 Step 1 全部状态同构；泛非挠/Picard 增长不被本表消费 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |
| [FIX 指定原共轭][FIX]；348／20304 | 30–71、86–139：原假设/对象及 Step 1 整个原共轭证明；特征限定公开；不消费 equalizer/节点厚度 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [FXD 原接口接受][FXD]；176／11013 | 1–19、61–75、140–161：原全基共轭接受、$p>3$ 量词、报告身份；不把概形接受自动外推实数 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [FMD forcing 接受][FMD]；234／13710 | 1–34、111–133：原 forcing 明确接受及作者/非作者身份；不要求读未消费厚度消费者 | `5340f77faa1354b1239240e3d7ba7068ae32e752e6d4550e32b2f243ea08bc99` |
| [RG forcing 独查][RG]；331／17843 | 1–59、72–139：原范围/身份与 §§3.1–3.2 的完整特征零还原和移动端点核验；不消费正特征或交数分析 | `7f7d6f659b69af334a32dca24ae4335ff98965a4de01f4643a56032aeea6b0e1` |
| [OB 旧准确厚度 brief][OB]；360／24719 | 130–139、210–248：旧 V1a 和旧 $3/16$ 节点因子/例外的已有性扣除；只是比较基线，不作 forcing 证明替身 | `1d00acccbd1056f361ac2736cbe9c035c965a566167bf6f8b9efdc4da1ba01dd` |
| [OS 旧实方向 scope][OS]；179／16523 | 49–82：原路径、旧 $J'$ 的有限接口和旧全局缺项；证明本次差额并防止把标准两行工具计作新中心 | `737b52c9217187897eaef5e12bbd63d6907282464ba458b94d4d0be79cf41426` |

以上必要旧段本人均已读；必要证明未以“源文件已接受”一句替代定位。没有机械追加旧厚度全包或其未消费祖先。
S02/F30/S03 的几何已经足够核定 FIX 所用最小性假设；当前实正则核心更直接由 G Step 4 延拓。
S02 的完整 pencil 总证明曾另外读 336–446 作定位；其 228–335 一般整法丛链不是本件要求的新增依赖。
另定向参考旧必要证明图 §3、P30 闭模型 Step 1 和接受入口，仅作依赖定位，不加入重复理论或称其 FULL。

## 10. 必须扣除、未申报及不变正式门槛

必须扣除 P30 的原模型、完整末端、原平移基础；旧准确 forcing、标准 $J'$、原 $3/16$ 节点代数因子。
实椭圆群圆旋转/有限回返、光滑射影延拓、实解析积分、Wronskian、一阶符号、Fatou/中值定理和标准积分渐近方法均非新方法。
Q/Z 的经典正常形身份和下外向已有边界问题的转移只缩小先例差额，不提高新意分数；来源优先权另核。
本件未发现当前 C1/C2/C3 内真实必要证明文件缺项；这是依赖定位结论，不是新完整证明信心票。
不申报节点全部奇异轨道、逐一有理角最小周期清单、非自治扰动、负/零时间、驻点随 $T$ 的全局分岔或逃逸速率。
不申报最大值初等闭式、$T$ 一致渐近、指定 $b$ 全阶满群、全部正二参数 Lyness 分类或首创认证。
旧准确厚度正式双 FAIL、指定 $b$ 的旧票、所有 HOLD/STOP 和隔离枚举保持；不拼接其他中心或扩 $N\ge10$ 扫描。
没有网络、CAS、数值、扫描、构建、稿件/PDF、项目或锁写入；没有 Route A/B 评价。
正式准入仍需两位 fresh 非作者，每位本人完成全部四门：新意≥7.5、独立价值≥7.5、完整证明信心≥9、可信22–30页容量 PASS。
不平均、不校准或重抽票，不按证明/来源分工拼四门；P30 的22–40页例外不传递。
本件不给页数 PASS、页数估计或凑页建议；旧6.5 C/D 不改，数学接受不等于候选准入或第五篇完成。

[PF0]: PAPER31_QPI_REAL_GLOBAL_TWIST_PREFLIGHT_DISPOSITION_V1_20260912.md
[MD]: PAPER31_QPI_REAL_GLOBAL_TWIST_MATHEMATICS_DISPOSITION_V1_20260912.md
[A]: PAPER31_QPI_REAL_GLOBAL_TWIST_NOVELTY_PHASE_A_V1_20260912.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[M]: PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
[U]: PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md
[I]: PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[FRC]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[Q]: PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md
[Z]: PAPER31_QPI_REAL_ZERO_LYNESS_SOURCE_BRIDGE_V1_20260912.md
[MA]: PAPER31_QPI_REAL_GEOMETRY_TWIST_MATH_REVIEW_V1_20260912.md
[MB]: PAPER31_QPI_REAL_OUTER_GLOBAL_MATH_REVIEW_V1_20260912.md
[QR]: PAPER31_QPI_REAL_POSITIVE_QRT_INTERFACE_MATH_REVIEW_V1_20260912.md
[ZR]: PAPER31_QPI_REAL_ZERO_LYNESS_BRIDGE_MATH_REVIEW_V1_20260912.md
[S02]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[S03]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
[F30]: PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md
[R30]: PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[FXD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[FMD]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md
[RG]: PAPER31_QPI_GOOD_CONTACT_INDEPENDENT_V1_20260912.md
[OB]: PAPER31_QPI_EXACT_THICKNESS_CANDIDATE_BRIEF_V1_20260912.md
[OS]: PAPER31_QPI_POST_EXACT_SOURCE_AND_SCOPE_V1_20260912.md
