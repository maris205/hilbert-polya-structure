# P30：有限窗口 determinant 零点与真实压力根的逼近

日期：2026-09-10 UTC；文件名沿用 09 日启动的 Goal 01 命名。
这是该持续目标的有界内部纸面推导。
仅新增本笔记；不生成或运行有限矩阵，不执行谱数值、字词／轨道
枚举、producer、census、实验、正式 build 或 Gate／Route／Stage 工作。

## 0. 准确结论

保持原真实一侧 roof g、原 beta 与完整 Hölder 空间。
对[既有有限记忆矩阵][memory] \(A_m(s)\)，记
\[
D_m(s)=\det(I-A_m(s)).
\tag{1}
\]
在已有固定空间 resolvent 条带的一条较窄开子条带内，每个预先
固定的有界复参数窗口最终没有假零：若窗口包含真实物理熵 h，
则恰有一个简单零点 \(h_m\to h\)；若不包含 h，则最终没有零点。
边界不得通过 h，所需记忆深度可依赖整个窗口。

该零点是近似 roof 的唯一**主压力零点**，并有
\[
\boxed{|h_m-h|\le\frac{hGq^m}{2a},\qquad m\ge2.}
\tag{2}
\]
(2) 本身对所有深度成立；它不声称所有深度的全部 determinant
零点都已由此分类。

关键区别：本篇证明约化谱因子的局部一致收敛和原有限 determinant
的零点结论，不证明整个 \(D_m\) 在条带内局部一致收敛，
更不把原无限维算子命名为 ordinary nuclear Fredholm determinant。
全无限频条带共用一个 m、量子谱身份和五通道完整误差定理均未获得。

## 1. 固定对象与已经展开的上游输入

沿用[一侧 roof][roof]、[有限记忆][memory]及
[固定空间 resolvent 条带][strip]中的同一对象：
\[
\begin{gathered}
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},\\
\mathcal B=\mathcal B_\beta=C^\beta(\Sigma^+,d_\theta),\qquad
\|u\|=\|u\|_\infty+[u]_\beta,\qquad q=\theta^\beta<1,\\
2a\le g\le10a,\qquad G=[g]_\beta,\qquad
L(s)u(x)=\sum_{b\ne x_0}e^{-sg(bx)}u(bx).
\end{gathered}
\tag{3}
\]
弱范数是 \(|u|=\|u\|_\infty\)；弱完备空间记为
\(\mathcal C=C(\Sigma^+;\mathbb C)\)。
这里只使用已有强／弱二范数，不替换 \(\mathcal B\) 或降低 beta。

每个深度、每个 cylinder 的代表在 s 变化前固定；不同深度不要求
代表兼容。令
\[
g_m=P_mg,\qquad \varepsilon_m=Gq^m,\qquad
L_m(s)=L_{g_m}(s),\qquad
A_m(s)=L_m(s)|_{\mathcal F_{m-1}}\quad(m\ge2).
\tag{4}
\]
已证
\[
|g_m-g|\le\varepsilon_m,\qquad
[g_m]_\beta\le G,\qquad 2a\le g_m\le10a.
\tag{5}
\]
\(\mathcal F_{m-1}\) 为长 \(m-1\) 柱函数空间，是 \(L_m\) 的不变子空间。
\(A_m\) 是[既有笔记 §4][memory]规定的矩阵，不另选 Galerkin 方案。
\(L_m\) 本身不是有限秩算子。

记 \(\lambda_t=r(L(t))\)、\(\lambda_m(t)=r(L_m(t))\)（t 实）。
各 \(g_m\) 仍是同一有限混合 shift 上的实 Hölder 函数；
这里只用实正 RPF，不要求它们有共同非格或高频相消证书。
实 RPF 与共同分支估计给正简单主谱值及
\[
e^{-|t|\varepsilon_m}\lambda_t
\le\lambda_m(t)\le e^{|t|\varepsilon_m}\lambda_t.
\tag{6}
\]
已有[strip]在
\[
\mathcal S_\eta=\{s:|\operatorname{Re}s-h|<\eta\}
\tag{7}
\]
证明 \(I-L(s)\) 仅在 \(s=h\) 不可逆，且有 rank-one 简单极点。
在 h 附近，其解析本征值分支 \(\Lambda\) 与投影 \(\Pi\) 满足
\[
\Lambda(h)=1,\qquad
\Lambda'(h)=-\mu_h(g),\qquad
\mu_h(g)\in[2a,10a],\qquad
\Pi(h)u=H_h\nu_h(u).
\tag{8}
\]
规范化为 \(\nu_h(H_h)=1\)，且 \(H_h>0\)。
本篇的 h 始终是此前已绑定原单位速度物理流的同一 \(h_T\)。

## 2. 弱—强谱稳定输入及适用窗口

[弱—强有限记忆谱稳定笔记][weak]把 Keller--Liverani 的原刊
Theorem 1、Corollary 1 与本案强／弱范数、统一 Lasota–Yorke、
弱误差及本质谱界相接。本节只列本篇实际消耗的输出；
其源假设及紧参数一致性论证在该笔记展开。

选择固定闭实区间 J，使
\[
h\in\operatorname{int}J,\qquad
J\subset(h-\eta,h+\eta),\qquad
\sup_{t\in J}\lambda_t<M<1/q,
\tag{9}
\]
并令 \(\alpha_*=qM<1\)。这样的 J、M 存在，因为 \(\lambda_h=1\)
且 \(q<1\)。以下开子条带固定为
\[
\mathcal S_*=\{s:\operatorname{Re}s\in\operatorname{int}J\}.
\tag{10}
\]
由 (6)，充分大 m 在 J 上一致满足 \(\lambda_m(t)<M\)。

对任意固定有限频率窗口 \(J+i[-B,B]\)，[weak] 给：

- 原族与近似族有共同的强／弱迭代界，收缩项为 \(\alpha_*^n\)；
- \(L_m(s)-L(s):\mathcal B\to\mathcal C\) 一致趋零，
  且 \(L_m(s):\mathcal C\to\mathcal C\) 一致有界；
- 对在 \(|\zeta|>\alpha_*\) 内的共同无谱 contour，近似 resolvent
  最终存在，相应 Riesz 投影在 \(\mathcal B\to\mathcal C\) 的混合
  范数中局部一致收敛，隔离谱簇的投影秩稳定；
- 商空间 \(\mathcal B/\mathcal F_{m-1}\) 上的算子谱满足
  \[
  r(\overline L_m(s))\le q\lambda_m(\operatorname{Re}s)<\alpha_*.
  \tag{11}
  \]
  因此 (11) 之外的谱及完整代数重数由有限 \(A_m(s)\) 承载。

局部一致性限于固定紧 s-集与隔开的谱边界。
不能把这些条件删去后宣称全复平面或无限频带的统一 m。
混合范数收敛也不等于投影或算子的强范数收敛；
[roof 输入误差笔记][input]中端点 big Hölder 反例仍然有效。

## 3. 在 h 附近构造同一个 rank-one 谱块

选 \(\alpha_*<r_*<1\)，并取足够小的 \(d>0\)，使
\[
\overline{\mathbb D(1,d)}\subset\{|\zeta|>r_*\},
\qquad
\sigma(L(h))\cap\overline{\mathbb D(1,d)}=\{1\}.
\tag{12}
\]
这里要求**整个闭圆盘**在本质／商谱圆盘之外，不仅要求圆周。
还可把 d 缩到 [weak] §5.3 所用的 KL 投影小半径范围，
而不破坏 (12)。
以正方向 contour \(\Gamma=\partial\mathbb D(1,d)\) 定义
\[
\Pi(s)=\frac1{2\pi i}\int_\Gamma(\zeta-L(s))^{-1}\,d\zeta.
\tag{13}
\]
原算子族在固定强范数中整，故可选以 h 为中心的小复圆盘
\(U\Subset\mathcal S_*\)，使 (13) 在 \(\overline U\) 都合法且 rank 为 1，
并与 (8) 的局部分支相同。必要时先在稍大的盘构造，再缩 U，
从而所有“在闭包一致”的断言都有开邻域支持。

由 §2，对所有充分大 m，同一 contour 给
\[
\Pi_m(s)=\frac1{2\pi i}
 \int_\Gamma(\zeta-L_m(s))^{-1}\,d\zeta,\qquad
\operatorname{rank}\Pi_m(s)=1,
\tag{14}
\]
并有
\[
\sup_{s\in\overline U}
 \|\Pi_m(s)-\Pi(s)\|_{\mathcal B\to\mathcal C}\longrightarrow0.
\tag{15}
\]
各 \(L_m(s)\) 在固定 \(\mathcal B\) 中也是整算子族，故
\(\Pi_m(s)\) 对 s 强算子范数全纯；这与只在混合范数中收敛是
不同的两个命题。

由 (11)–(12)，商 resolvent 在整个 \(\mathbb D(1,d)\) 内全纯。
(14) 投影到商空间的积分因而为零，得到
\[
E_m(s):=\operatorname{ran}\Pi_m(s)\subset\mathcal F_{m-1}.
\tag{16}
\]
这正是把无限维近似算子的孤立谱簇合法放回既定有限矩阵的接口，
不是先假定全近似算子有限秩。

## 4. 一个评价比值给解析特征值的局部一致收敛

固定 \(e=H_h\in\mathcal B\)，并取任意一个
\(x_*\in\Sigma^+\)。因为 \(\Pi(h)e=e\) 且 \(e(x_*)>0\)，
缩小 U 后可令
\[
v(s)=\Pi(s)e,\qquad |v(s)(x_*)|\ge c_*>0
\quad(s\in\overline U).
\tag{17}
\]
令 \(v_m(s)=\Pi_m(s)e\)。由 (15)，充分大 m 有
\(|v_m(s)(x_*)|\ge c_*/2\)，从而 v、\(v_m\) 分别是各 rank-one
谱空间的非零解析标架。定义
\[
\Lambda_m(s)=
 \frac{[L_m(s)v_m(s)](x_*)}{v_m(s)(x_*)},
\qquad
\Lambda(s)=
 \frac{[L(s)v(s)](x_*)}{v(s)(x_*)}.
\tag{18}
\]
不变性及一维性说明 \(L_mv_m=\Lambda_mv_m\)，且原来的比值
恰是 (8) 的分支。两个比值都全纯。

分子收敛需要单独证明，不能仅凭 (15) 直接乘两个强算子。
精确分解为
\[
L_m\Pi_m e-L\Pi e
=L_m(\Pi_m-\Pi)e+(L_m-L)\Pi e.
\tag{19}
\]
第一项以统一 \(\mathcal C\to\mathcal C\) 界和 (15) 控制；
第二项以混合误差及 \(\sup_{\overline U}\|\Pi(s)e\|<\infty\) 控制。
因此分子、分母均在弱范数中一致收敛，后者一致远离零，得到
\[
\boxed{\Lambda_m\longrightarrow\Lambda
       \quad\text{在 }\overline U\text{ 一致}.}
\tag{20}
\]
这完全不需要 \(\Pi_m\to\Pi\) 的强算子范数收敛。
在内部较小圆盘，解析函数的导数亦可由 Cauchy 积分收敛，
但本篇不藉此宣称整个 determinant 的导数受控。

## 5. 有限 determinant 的无零因子分解

对固定 m，把 (14) 限制到 \(\mathcal F=\mathcal F_{m-1}\)，记
\[
p_m(s)=\Pi_m(s)|_{\mathcal F}.
\tag{21}
\]
\(\mathcal F\) 不变且 contour 在完整算子的 resolvent 集中；
有限矩阵上 resolvent 的解由唯一性与完整 resolvent 的限制一致。
所以 (21) 是 \(A_m\) 的 rank-one Riesz 投影，解析并交换 \(A_m\)，
其值域恰为 (16)。

定义解析有限维因子
\[
Q_m(s)=\det_{\mathcal F}
 \bigl(I_{\mathcal F}-A_m(s)(I_{\mathcal F}-p_m(s))\bigr).
\tag{22}
\]
它在 \(\operatorname{ran}p_m\) 上对应 identity，
在 \(\ker p_m\) 上对应 \(I-A_m\)。
后一个补空间的谱位于 contour 圈定簇之外，所以不含 1。
因此
\[
Q_m(s)\ne0\qquad(s\in U).
\tag{23}
\]
投影与 \(A_m\) 交换、两个谱块互相湮灭，故有限矩阵恒等式
\[
I-A_m=(I-A_mp_m)
       (I-A_m(I-p_m))
\]
给
\[
\boxed{D_m(s)=Q_m(s)\,[1-\Lambda_m(s)]\qquad(s\in U).}
\tag{24}
\]
(23)–(24) 使两个因子的零点及零阶完全相同。
这里既不要求 \(Q_m\) 有共同下界，也没有证明 \(Q_m\) 收敛。
不能从约化因子 \(1-\Lambda_m\) 的一致收敛反推 \(D_m\) 一致收敛。

## 6. Rouché 计数与实压力零点的身份

由 (8)，
\[
d(s):=1-\Lambda(s),\qquad
d(h)=0,\qquad d'(h)=\mu_h(g)>0.
\tag{25}
\]
因此可取 \(0<r_0\) 使
\(\overline{\mathbb D(h,r_0)}\subset U\)，
d 在该闭盘内仅有 h 这个简单零点，边界上不为零。
由 (20)，充分大 m 在边界满足
\[
|(1-\Lambda_m(s))-d(s)|<|d(s)|.
\tag{26}
\]
Rouché 定理给 \(1-\Lambda_m\) 恰有一个零点，按解析零阶计数为 1，
故它是简单零点。由 (24)，\(D_m\) 亦有同一唯一简单零点。

现在识别它，不把一个未定复零点默认叫作物理 h。
令实近似压力
\[
\mathfrak p_m(t)=\log\lambda_m(t).
\tag{27}
\]
对 \(u\ge0\)，从 \(2a\le g_m\le10a\) 的每条 n 步权重直接比较，
再取增长率，得
\[
-10au\le\mathfrak p_m(t+u)-\mathfrak p_m(t)\le-2au.
\tag{28}
\]
故 \(\mathfrak p_m\) 连续严格递减。
\(L_m(0)=L(0)\) 每点恰有两个前像，给
\(\mathfrak p_m(0)=\log2>0\)，且
\(\mathfrak p_m(t)\le\log2-2at\to-\infty\)。
因此有唯一 \(h_m>0\) 满足
\[
\mathfrak p_m(h_m)=0.
\tag{29}
\]

由 (6) 与 \(\lambda_h=1\)，
\[
|\mathfrak p_m(h)|\le h\varepsilon_m.
\tag{30}
\]
将 (28) 用于 h、\(h_m\) 之间的区间（按二者先后选非负 u），得
\[
\boxed{|h_m-h|\le
 \frac{|\mathfrak p_m(h)|}{2a}
 \le\frac{h\varepsilon_m}{2a}
 =\frac{hGq^m}{2a}.}
\tag{31}
\]
这个实压力估计不需要 KL、Rouché 或强范数近似，
对每个 \(m\ge2\) 成立。

在 \(t=h_m\)，正 RPF 给 \(L_m(t)\) 的主特征值 1。
同一 finite-memory 商估计为 \(r(\overline L_m(t))\le q<1\)，
即使 m 尚未进入 §2 的统一尾部也成立。
所以该本征函数位于 \(\mathcal F_{m-1}\)，1 是 \(A_m(h_m)\) 的特征值，
从而 \(D_m(h_m)=0\)。由 (31)，h_m 最终位于上述小盘内，
恰好是 (26) 得到的唯一简单零点。

“主压力零点唯一”不等于“对任意 m，整个 \(D_m\) 在全部正实轴
仅有一个零点”；本篇未排除远处非主谱分支的零点。
简单性也不是仅由固定参数的简单特征值自动得出：
(25) 的非零参数导数，或本节的完整 Rouché 计数，不能省略。

## 7. 任意固定有限窗口中的无假零结论

设 \(K\Subset\mathcal S_*\setminus\{h\}\)。
[strip] 给每个 \(s\in K\) 的 \(I-L(s)\) 可逆，其逆在 K 上强范数有界。
\(\operatorname{Re}s\) 和 \(|\operatorname{Im}s|\) 也在固定有限范围，
且谱参数 \(\zeta=1\) 位于 \(|\zeta|>\alpha_*\)。
[weak] 的紧参数 resolvent 稳定性遂给
\[
I-L_m(s)\ \text{在全部 }s\in K\text{ 上可逆}
\quad(m\ge m_0(K)).
\tag{32}
\]
若 \(D_m(s)=0\)，有限矩阵有特征值 1，其非零本征向量同时属于
\(\mathcal B\)，会与 (32) 矛盾。因此 K 上最终没有 \(D_m\) 零点。

特别地，对任意预先固定的有界 Jordan 域
\(\Omega\Subset\mathcal S_*\)，假设 \(h\notin\partial\Omega\)。
若 h 在域内，取 §6 的足够小闭盘包含于 \(\Omega\)，其余闭窗口
为避开 h 的紧集；若 h 不在域内，则整个闭窗口避开 h。
用 \(N_\Omega(D_m)\) 表示域内零点的解析零阶总数。
结合 (24)–(32)，对充分大 m，
\[
\boxed{N_\Omega(D_m)
 =\begin{cases}1,&h\in\Omega,\\0,&h\notin\Omega.\end{cases}}
\tag{33}
\]
唯一零点的情形就是简单实零点 \(h_m\)。

(33) 中 m 可以依赖 \(\Omega\) 的频率高度、离条带边界与 h 的距离，
以及 KL 所需的未扰动 resolvent／谱隔离常数。
不能交换量词写成一个固定 m 对全部无限高频窗口同时成立。
本篇没有给已计算的 m 阈值或具体可执行数值 enclosure。

## 8. 与旧右域极限、真实时钟和误差合同的关系

[有限记忆笔记][memory]已经在明确物理右域证明
\(D_m(s)\to Z_g(s)^{-1}\) 的函数值／对数误差结论。
本篇新增的是另一种、局部谱约化的零点接口。
两者不能仅因使用同一 \(D_m\) 就自动拼成整个条带的函数值
一致收敛、非零因子身份或全局 determinant 等式。

在当前条带中，固定空间 resolvent 的唯一奇点是 h，
经典 zeta 的相应 h 亦已经单独核过。
这不证明所有延拓区域的共振／零点重数身份，
也不识别物理波、散射或自伴量子算子。

(31) 控制的是近似 roof 的主压力根偏移。
各 \(g_m\) 的单条周期时间通常仍不同于原真实时间；
没有把近似屋顶替换成新的 canonical 物理输入。
原大 Hölder 空间的非紧性和普通核性障碍仍保留。

本篇与[weak]补进旧 rank／projection、roof-input 传播接口的一部分，
但还没有共同控制全部 orbit tail、rank、quadrature／evaluation、
roundoff、geometry／roof-input 五通道，也没有整体 determinant
conditioning、已选择算法／精度或可执行总误差上界。
不改变任何既有 Gate、Route 或 Stage 的未完成／停止状态。

## 9. 来源、方法与实际动作

主代理全文核读本篇引用的固定 roof、有限记忆、resolvent 条带及
弱—强谱稳定输入，并按本案直接推导评价坐标、(19)、(24) 与
压力根误差。来源方法层为
[Keller--Liverani 原刊][kl] Theorem 1、Corollary 1：
其原刊 141–142、144–145 页的公式和 149–150 页的投影／秩证明
已通过原 PDF 实际读审。网页公式抽取为空的尝试没有算作已读。

为读清这些来源页，主代理只在独立临时目录下载公开 PDF，
使用常规 PDF 渲染器生成阅读页；这是文献格式读取，不是科学、
符号或谱计算，也不产生项目输入。没有执行候选矩阵或压力数值。
ARS 的有界论证与来源核对用于保持弱／强收敛、谱值、零阶、
函数身份及执行证据互相分离。同模型只读逻辑校对不构成独立
科学证明或新颖性认证。

本次项目写入仅为 apply_patch 新增本文件，随后完整回读及一次
必要的文本静态检查。不会清除历史失败、回写锁定输入、晋升正式
输出或启动未获批准的研究执行；文字检查也不证明数学成立。

[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[memory]: internal_goal01_cylinder_trace_and_finite_memory_determinants_20260909.md
[strip]: internal_goal01_fixed_space_resolvent_strip_and_simple_pressure_pole_20260909.md
[weak]: internal_goal01_weak_strong_finite_memory_spectral_stability_20260909.md
[input]: internal_goal01_roof_input_error_and_resolvent_stability_20260909.md
[kl]: https://www.numdam.org/article/ASNSP_1999_4_28_1_141_0.pdf
