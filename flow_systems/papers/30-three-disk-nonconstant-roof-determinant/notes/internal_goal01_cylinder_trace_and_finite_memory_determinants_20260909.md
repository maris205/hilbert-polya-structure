# P30 内部理论：柱集有限秩跡与有限记忆行列式的受控极限

日期：2026-09-09 UTC。持续内部研究的纸面单元；只新增本文件，不执行
矩阵／字词枚举、实验、producer、稿件或正式 checker。保持原三盘、
单位速度、全部相空间本原轨道及当前正一侧 roof。

本页补两个有限而准确的算子—周期接口：指定柱集投影的有限秩跡
收敛到真实周期和；有限记忆矩阵的有限维行列式在明确右域局部一致
收敛到周期行列式。**这不建立普通无限维算子跡或 Fredholm 身份。**

## 1. 固定输入与柱集投影

沿用[正一侧 roof 笔记][roof]中的固定空间与实函数：
\[
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},\quad
d_\theta(x,y)=\theta^{N(x,y)},\quad
\mathcal B_\beta=C^\beta(\Sigma^+,d_\theta),\quad q=\theta^\beta<1,
\]
\[
g\in\mathcal B_\beta,\quad 2a\le g\le10a,\quad G=[g]_\beta,\qquad
(\mathcal L_s f)(x)=\sum_{b\ne x_0}e^{-sg(bx)}f(bx).
\tag{1}
\]
其中 \(N\) 是首个不同坐标的位置；一致序列的距离为零。上游给
双向真实飞行时间 \(\tau\) 与一个有界连续函数 \(U\)，满足
\[
g\circ\pi=\tau-U+U\circ\sigma,\qquad
4a\le\tau\le8a,\qquad B=\|U\|_\infty<\infty.
\tag{2}
\]
因此对任意一侧点补任意合法过去，望远镜求和给
\[
S_ng(x)\ge4an-2B;\qquad
S_ng(p)=S_n\tau(p)\ge4an\quad(\sigma_+^np=p).
\tag{3}
\]
周期等式用唯一双侧周期延拓，不要求 \(n\) 是正平均长度的倍数。

令 \(\mathcal W_m\) 是全部长 \(m\) 合法字，\(m\ge1\)，并定义
\[
\mathcal F_m=\operatorname{span}\{1_{[w]}:w\in\mathcal W_m\},\qquad
P_mf=\sum_{w\in\mathcal W_m}f(x_w)1_{[w]},\quad x_w\in[w].
\tag{4}
\]
每个柱集恰选一个代表点，全部选择在 \(s\) 变化前固定，不要求不同
层的选择相容。上游已证它们是有界有限秩投影，且
\[
\|f-P_mf\|_\infty\le q^m[f]_\beta,\qquad
[P_mf]_\beta\le[f]_\beta.
\tag{5}
\]
以下跡均有明确的有限维含义。(5) 不说明 \(P_m\to I\) 在一般大
Hölder 空间的强拓扑或算子范数中成立。

## 2. 固定迭代次数的柱集跡

固定 \(n\ge1\)，取 \(m\ge n+1\)，定义
\[
\mathcal T_{m,n}(s)=\operatorname{tr}_{\mathcal F_m}
\left(P_m\mathcal L_s^nP_m\big|_{\mathcal F_m}\right).
\tag{6}
\]
在柱集基下，属于 \(w\) 的对角 entry 是
\[
(\mathcal L_s^n1_{[w]})(x_w)
=\sum_{\substack{\sigma_+^ny=x_w\\y\in[w]}}e^{-sS_ng(y)}.
\tag{7}
\]
至多有一个前像：其首 \(n\) 字必须为 \(w_0,\ldots,w_{n-1}\)，余下
尾巴为 \(x_w\)。它属于 \([w]\) 当且仅当
\[
w_{n+j}=w_j\quad(0\le j<m-n),
\tag{8}
\]
另需前接边合法。由于 \(m\ge n+1\)，(8) 给 \(w_n=w_0\)，而合法柱字
有 \(w_{n-1}\ne w_n\)，故闭合边自动合法。

这些柱字与 \(\operatorname{Fix}(\sigma_+^n)\) 一一对应：取周期点的
前 \(m\) 字即可，反向则将首 \(n\) 字周期延拓。包含最小周期真除
\(n\) 的点，不只取本原点。对应的唯一前像为
\[
y_{m,p}=p_0p_1\cdots p_{n-1}\,x_{p|m},
\qquad
\boxed{\mathcal T_{m,n}(s)=
\sum_{\sigma_+^np=p}e^{-sS_ng(y_{m,p})}.}
\tag{9}
\]
当 \(n=1\)，相邻字母不等使两边均为空和。

## 3. 跡极限、误差与代表选择独立性

\(y_{m,p}\) 与 \(p\) 至少一致于前 \(m+n\) 个坐标。因此
\[
|S_ng(y_{m,p})-S_ng(p)|
\le G\sum_{j=0}^{n-1}q^{m+n-j}
=\delta_{m,n}:=\frac{Gq^{m+1}(1-q^n)}{1-q}.
\tag{10}
\]
置
\[
Z_n(s)=\sum_{\sigma_+^np=p}e^{-sS_ng(p)}.
\tag{11}
\]
对实 \(X,Y\)，指数级数或线段积分给
\[
|e^{-sX}-e^{-sY}|
\le |s|\,|X-Y|e^{|s||X-Y|}e^{-(\Re s)Y}.
\tag{12}
\]
所以对全部 \(s\in\mathbb C\)，
\[
|\mathcal T_{m,n}(s)-Z_n(s)|
\le |s|\delta_{m,n}e^{|s|\delta_{m,n}}Z_n(\Re s).
\tag{13}
\]
固定 \(n\) 时右边在紧 \(s\)-集上一致趋零，得到
\[
\boxed{\lim_{m\to\infty}\mathcal T_{m,n}(s)=Z_n(s).}
\tag{14}
\]
不同代表选择都满足同一 (10)，故极限与代表选择无关。

可把 (14) 称为本页指定的“柱集正则化跡”。没有证明任意有限秩
逼近、任意正则化或任意基给相同结果，更没有证明核算子跡或跡范数
收敛。特别地，一般不能断言
\[
P_m\mathcal L_s^nP_m=(P_m\mathcal L_sP_m)^n.
\tag{15}
\]
例如 \(n=1\) 时相等，但这不提供一般幂恒等式。上述证明还要求
\(m\ge n+1\)，所以不能固定 \(m\) 后直接
将 (14) 对全部 \(n\) 求和。下一节是独立的有限记忆构造。

## 4. 有限记忆矩阵及全部周期的精确跡

对 \(m\ge2\) 令 \(g_m=P_mg\)，\(\varepsilon_m=Gq^m\)。这是理论近似，
不替换实际物理时钟。由 (5)，
\[
2a\le g_m\le10a,\qquad
\|g_m-g\|_\infty\le\varepsilon_m\longrightarrow0.
\tag{16}
\]
以 \(g_m\) 代替 (1) 中的 \(g\)，记算子为 \(\mathcal L_s^{[m]}\)。
它保持 \(\mathcal F_{m-1}\)，定义
\[
A_m(s)=\mathcal L_s^{[m]}\big|_{\mathcal F_{m-1}}.
\tag{17}
\]
明确矩阵方向：行是输出状态 \(v=(v_0,\ldots,v_{m-2})\)；对每个
\(b\ne v_0\)，列 \(u=(b,v_0,\ldots,v_{m-3})\) 上填
\[
(A_m(s))_{v,u}=\exp\bigl(-s\,g_m(bv_0\cdots v_{m-2})\bigr);
\tag{18}
\]
其余为零。\(m=2\) 时该列只有一个字母 \(b\)。\(g_m\) 在长 \(m\)
字上表示其柱集常值。矩阵是向前重叠字图加权邻接矩阵的转置，
这与前像算子的作用方向一致。排除 \(m=1\)，因为常数空间一般并非不变子空间。

**命题。** 对每个 \(m\ge2\)、全部 \(n\ge1\)，有
\[
\boxed{\operatorname{tr}(A_m(s)^n)
=\sum_{\sigma_+^np=p}e^{-sS_ng_m(p)}=:Z_n^{[m]}(s).}
\tag{19}
\]
证明：矩阵跡展开为带起始状态标记的长 \(n\) 闭合字图路径。每一步
的 \(m-2\) 字重叠和闭合条件，使这些状态成为一个 \(n\)-周期序列的
连续长 \(m-1\) 窗口；反向从周期序列取窗口得到唯一闭合路径。
这在 \(n<m-1\) 时仍成立，不需要短周期修正。各边权的乘积恰是
\(e^{-sS_ng_m}\)。最小周期 \(d\mid n\) 的轨道贡献 \(d\) 个起点，
不是 \(n\) 个。当 \(n>m-1\) 时，一个状态可以起始多条闭合路径，
所以此处不能沿用 §2 的“每个状态至多一项”说法。□

## 5. 物理右域与有限矩阵谱半径

考虑开域
\[
\mathcal D=\{(s,z)\in\mathbb C^2:
\sigma:=\Re s>0,\quad 2|z|e^{-4a\sigma}<1\}.
\tag{20}
\]
周期点数至多 \(3\cdot2^n\)，(3) 因而给
\[
|Z_n(s)|\le3(2e^{-4a\sigma})^n.
\tag{21}
\]
于是
\[
\mathfrak d(s,z)=
\exp\left(-\sum_{n\ge1}\frac{z^n}{n}Z_n(s)\right)
\tag{22}
\]
在 \(\mathcal D\) 非零、联合全纯，对数级数在紧子集绝对一致收敛。

为了使用有限矩阵的跡级数，还需控制其谱，不能只作形式重排。
由 (3)、(16)，所有一侧点都满足
\[
S_ng_m\ge(4a-\varepsilon_m)n-2B.
\tag{23}
\]
每点有 \(2^n\) 个合法前像，故在柱集系数 sup 范数下
\[
\|A_m(s)^n\|_\infty
\le2^ne^{2\sigma B}e^{-(4a-\varepsilon_m)\sigma n},
\qquad
r(A_m(s))\le2e^{-(4a-\varepsilon_m)\sigma}.
\tag{24}
\]
前一个常数不依赖 \(n\)，取 \(n\) 次根即得后式。此处使用真实
共边界 (2) 保留长段 \(4a\) 下界，没有错误宣称 \(g_m\ge4a\)。

固定非空 \(K\Subset\mathcal D\)，令
\[
S=\max_K|s|,\qquad r_0=\max_K2|z|e^{-4a\Re s}<1.
\tag{25}
\]
选 \(r_0<r_1<1\)，再取 \(m\) 充分大使
\(r_0e^{S\varepsilon_m}\le r_1\)。若 \(r_0=0\)，任取 \(0<r_1<1\) 即可。
由 (24)，这些 \(m\) 在整个 K 上满足 \(|z|r(A_m(s))<1\)，所以
\[
\det(I-zA_m(s))
=\exp\left(-\sum_{n\ge1}\frac{z^n}{n}
\operatorname{tr}(A_m(s)^n)\right).
\tag{26}
\]
这是有限矩阵 eigenvalues 的标准对数级数，由 \(z=0\) 处取值 0
规范化；不是任意选取 scalar principal logarithm。没有声称每个小
\(m\) 的行列式都在整个
\(\mathcal D\) 无零；充分大的 \(m\) 可依赖紧集 K。

## 6. 有限行列式的受控极限

周期点上 \(|S_ng_m-S_ng|\le n\varepsilon_m\)。由 (3)、(12)，
\[
|Z_n^{[m]}(s)-Z_n(s)|
\le3|s|n\varepsilon_m
\left(2e^{-4a\Re s+|s|\varepsilon_m}\right)^n.
\tag{27}
\]
对 K 使用 (25) 的 \(r_1\)，结合 (19)、(26)，得到
\[
\boxed{
|\log\det(I-zA_m(s))-\log\mathfrak d(s,z)|
\le\frac{3S\varepsilon_m r_1}{1-r_1}.}
\tag{28}
\]
两边 log 均取上述级数指定的规范，不存在未追踪的 \(2\pi i\) 常数。
指数化即得
\[
\boxed{\det(I-zA_m(s))\longrightarrow\mathfrak d(s,z)}
\tag{29}
\]
在 \(\mathcal D\) 的紧子集上一致。改变柱集代表仍有 (16)、(27)、
(28)，故极限也不依赖代表选择。

取 \(z=1\)，收敛域是 \(\Re s>\log2/(4a)\)。最小周期 \(d\) 的符号
循环在 \(n=rd\) 的周期和出现 \(d\) 次；由 \(d/n=1/r\) 及绝对重排，
\[
\boxed{\mathfrak d(s,1)
=\prod_{[p]\ {\rm primitive}}(1-e^{-sT_p})=Z_g(s)^{-1}.}
\tag{30}
\]
上游真实编码和保周期共边界使 \(T_p\) 正是原物理最小周期。
不按速度反转或几何对称另取商；两碰撞循环不会凭空乘二。

## 7. 精确能力边界

本页三个相容而不同的输出是：固定 \(n\) 的压缩跡极限 (14)；
有限记忆矩阵对所有 \(n\) 的精确周期跡 (19)；有限行列式的受控
极限 (29)–(30)。没有将第一种压缩误当成第二种矩阵。

\(g_m\to g\) 的现有证据是 sup 范数逼近，不推出
\(\mathcal L_s^{[m]}\to\mathcal L_s\) 的 \(C^\beta\) 算子范数收敛。
周期级数与有限行列式的极限证明不需要该未证结论。它们也不使
\(\mathcal L_s\) 自动成为核算子，不赋予其普通无限维跡，不能将
(22) 改名为已认证的 \(\det_{\rm Fredholm}(I-z\mathcal L_s)\)。

每个有限矩阵 determinant 都是整函数，不代表受限域内的极限
自动延拓到 \(\mathbb C^2\)。域外的一致界、收敛、谱重数身份、量子
determinant 与自伴性均未证明。有限记忆 roof 的周期通常不同于
原物理周期；只有所证极限回到同一原对象，不能提升近似为 canonical 输入。

## 8. 方法、实际动作与来源层

全部新增公式在本文直接推导；没有使用外部 RPF、核性或一般 trace
定理作为黑箱。有限矩阵特征值的跡级数与上游真实几何／一侧化条件
是明列依赖，不声称原创优先权、独立发表结果或形式化验证。

ARS 有界 argument 使定义、有限维恒等式、正常收敛与未证明的无限维
身份分开。主代理重读上游固定空间、共边界和柱集投影段落，并以
只读搜索确认没有同题内部笔记。平行只读审查挑战柱集闭合、投影与
幂、矩阵方向及求和界；同模型的审查不计为外部独立科学证据。

写前确认目标不存在。首次 apply_patch 因新文件一行缺少补丁标记
被拒绝，未产生文件；随后仅以 apply_patch 新建本文件。没有运行
科学程序、矩阵／字词枚举、数值实验、稿件或 checker。只读文字／
链接检查不认证数学成立，结果由主工作记录另汇总。

[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
