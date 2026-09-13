# P32 内部研究：字符压力偶对称与 theta 误差的明确速率

记录日期：2026-09-08 UTC。接续[扩散 theta 与临界有限部分笔记][finite]，作为本次 P29–P33 五篇内部论证轮的一部分。本轮将其中只证明趋零的加权 L1 误差量化为

\[
\rho_N=O\!\left(N^{-2}(\log N)^3\right).
\tag{1}
\]

固定对象、带标记的曲率负一闭双曲亏格二曲面、全部有向本原轨道、原 `1/N` 时间缩放和 `1/N³` 对数归一化均不变。常数可依赖这个固定曲面及同调基，不是跨曲面族统一数值常数。结论对充分大整数 N 成立，故也适用于冻结阶乘子序列。

本轮为内部证明增量，不是科学程序执行、正式稿修订、完整性重审或 Route 评估。

## 1. 已有输入与本轮新义务

采用 [上一轮][finite] 的记号

\[
F_N(u)=N^4(N^2u)e^{-N^2u}
\#\{g:\ell_g\le N^2u,\ \alpha_g\in N\mathbb Z^4\setminus\{0\}\},
\]

\[
\Theta_D(u)=\sum_{k\in\mathbb Z^4}e^{-2\pi^2u k^{\mathsf T}Dk},
\qquad F_D(u)=\Theta_D(u)-c_Du^{-2},
\quad c_D=(2\pi)^{-2}(\det D)^{-1/2}.
\]

这里 \(D>0\) 是同一字符压力函数的负 Hessian。此前已证明

\[
0\le F_N(u)\le C e^{-c/u},\qquad
0<F_D(u)\le C u^{-2}e^{-c'/u}\quad(0<u\le1),
\tag{2}
\]

以及

\[
\rho_N:=\int_0^\infty|F_N(u)-F_D(u)|\,\frac{du}{u}\longrightarrow0.
\tag{3}
\]

[可积字符尾项笔记][tail]的 Sharp 输入经无权、本原和端点转换后，对**每个固定**整数 \(p\ge1\) 有全字符一致式

\[
\pi_\theta(t)=\mathbf1_{\theta\in U}\operatorname{Li}(e^{s(\theta)t})
+O_p(e^t/t^p).
\tag{4}
\]

本轮仍一次固定 \(p=4\)，不令 p 随 N 增长。零类计数首两阶和精确字符平均给，在 \(t=N^2u\) 大于一个固定阈值时

\[
F_N(u)-F_D(u)
=\sum_{k\in K_N}t e^{-t}\operatorname{Li}(e^{s(2\pi k/N)t})
-\Theta_D(u)+O(N^{-2}u^{-3}),
\tag{5}
\]

其中 \(K_N\) 由中心字符代表且 \(2\pi k/N\in U\) 确定。式 (5) 包含全字符 PGT 余项及零类扣除的误差，没有把固定同调渐近用于随 N 移动的单个类。

新义务是控制 \(u\) 随 N 缩到零时的格点误差。仅有局部一致收敛不够；下面先把旧 \(O(|\theta|^3)\) Taylor 余项改进为四阶，再进行端点分割。

## 2. 唯一实极点迫使 s 为偶函数

本轮普通浏览核对了 Richard Sharp 的 [作者版原文][sharp]：第 3 页的 Euler 定义、第 4 页 Proposition 1 的唯一极点及实解析性质，以及 Lemma 1 的 Hessian 约定。该来源给的是这些输入；偶对称推导和以下 N 速率是本笔记的推论，不冒称为该文原结论。

用 v 表示 Euler 函数的复变量，避免与函数 \(s(\theta)\) 混用。在 \(\operatorname{Re}v>1\) 的绝对收敛域上，因 \(\ell_g\) 和 \(\alpha_g\) 为实数据，逐项共轭给

\[
L(v,-\theta)=\overline{L(\bar v,\theta)},\qquad
\frac{L'}{L}(v,-\theta)=
\overline{\frac{L'}{L}(\bar v,\theta)}.
\tag{6}
\]

这只需要真实计数的复共轭关系，不需要合并正反向轨道或另加方向因子二。由亚纯延拓的唯一性，(6) 继续成立于共同的近临界条带。

Proposition 1 给出在足够小字符邻域内的唯一简单极点 \(v=s(\theta)\)，且 \(s(\theta)\) 为实数、\(s(0)=1\)。先固定该条带，再将字符邻域收缩到一个对称 U，使这两个极点都位于共同条带内。由 (6) 的极点集合相等与实值性，

\[
\boxed{s(-\theta)=s(\theta).}
\tag{7}
\]

必要的邻域收缩不破坏 (4)：被移除的固定环带上 \(s(\theta)\le1-\eta\)，其指数小主项可吸收进每个固定 p 的余项。

因此所有奇数阶 Taylor 齐次项消失。把 U 再固定得足够小，其闭包位于解析域内，得到统一的四阶界

\[
\boxed{s(\theta)=1-\tfrac12\theta^{\mathsf T}D\theta+O(|\theta|^4),}
\qquad s(\theta)\ge s_0>0,
\quad 1-s(\theta)\ge c_0|\theta|^2.
\tag{8}
\]

这里使用固定邻域内有界的四阶导数，而不是在随 N 收缩的域中假定 Taylor 常数统一。没有声称一般缺乏这种实极点结构的任意 Anosov 流都满足 (7)。

## 3. 从四阶余项到整个字符格点和

对 \(k\in K_N\) 记

\[
A_{N,k}(u)=(1-s(2\pi k/N))N^2u,
\qquad B_k(u)=2\pi^2u k^{\mathsf T}Dk.
\]

由 (8)，有与 k、N、u 无关的常数使

\[
A_{N,k},B_k\ge c u|k|^2,\qquad
|A_{N,k}-B_k|\le C N^{-2}u|k|^4,
\tag{9}
\]

\[
|s(2\pi k/N)^{-1}-1|\le C N^{-2}|k|^2.
\tag{10}
\]

由实指数的均值定理，

\[
|e^{-A_{N,k}}-e^{-B_k}|
\le C N^{-2}u|k|^4 e^{-cu|k|^2}.
\tag{11}
\]

对 \(s\in[s_0,1]\)、固定足够大的 t，一次分部积分给一致的 Li 展开

\[
t e^{-t}\operatorname{Li}(e^{st})
=s^{-1}e^{-(1-s)t}
+O(t^{-1}e^{-(1-s)t}).
\tag{12}
\]

从而每个纳入格点的总差受

\[
C N^{-2}\left(u|k|^4+|k|^2+u^{-1}\right)e^{-cu|k|^2}
\tag{13}
\]

控制。\(k=0\) 的前两项为零，但 Li 的 \(N^{-2}u^{-1}\) 修正仍在；不能把整个大 u 误差都误写成指数衰减。

### 3.1 小 u 的四维 Gaussian 矩

对 \(0<u\le1\)、\(j=0,1,2\)，分单位格壳并与径向 Gaussian 积分比较，给出

\[
\sum_{k\in\mathbb Z^4}|k|^{2j}e^{-cu|k|^2}
\le C_j u^{-2-j}.
\tag{14}
\]

\(j=0\) 时把 \(|0|^0\) 理解为 1。这些指数是四维格点密度 \(u^{-2}\) 乘上第 2j 阶矩的 \(u^{-j}\)。代入 (13) 的三项，分别均得到 \(O(N^{-2}u^{-3})\)。

U 含有一个固定零点邻域，故未纳入的任何整数 k 满足 \(|k|\ge c_U N\)。将 Gaussian 指数分成两半，得

\[
\sum_{k\notin K_N}e^{-cu|k|^2}
\le C u^{-2}e^{-c_1N^2u}\quad(0<u\le1).
\tag{15}
\]

这同时包含中心代表域截断及 U 截断，不把有限网格硬当成全整数格。

结合 (5)、(13)–(15)，在 \(0<u\le1\)、\(N^2u\ge T_0\) 有

\[
\boxed{|F_N(u)-F_D(u)|
\le C N^{-2}u^{-3}+C u^{-2}e^{-c_1N^2u}.}
\tag{16}
\]

### 3.2 大 u 的平凡字符项须单独保留

对 \(u\ge1\)，非零格点的固定阶矩和均为 \(O(e^{-bu})\)，零阶全格点和有界。截断尾项仍由分半指数给 \(O(e^{-c_2N^2u})\)。于是

\[
\boxed{|F_N(u)-F_D(u)|
\le C N^{-2}\left(u^{-1}+u^{-3}+(u+1)e^{-bu}\right)
+C e^{-c_2N^2u}.}
\tag{17}
\]

特别地，

\[
\int_1^\infty|F_N-F_D|\,\frac{du}{u}=O(N^{-2}).
\tag{18}
\]

每个系数均在一个固定几何对象上统一；没有由固定层 \(O_N\) 余项猜测 N 的速率。

## 4. 小端点分割闭合加权 L1 速率

由 (2)，取某个固定 \(b_0>0\)，对 \(0<u_0\le1\) 有

\[
\int_0^{u_0}|F_N-F_D|\,\frac{du}{u}
\le C\int_0^{u_0}u^{-3}e^{-b_0/u}\,du
\le C e^{-b_0/(2u_0)}.
\tag{19}
\]

最后一步可由 \(v=b_0/u\) 后的 \((v_0+1)e^{-v_0}\) 精确尾积分得出。取

\[
u_0=\frac{b_0}{8\log N}.
\tag{20}
\]

对充分大 N，\(u_0\le1\) 且 \(N^2u_0\ge T_0\)。因此 (19) 是 \(O(N^{-4})\)，而中间段由 (16) 给

\[
\begin{aligned}
\int_{u_0}^{1}|F_N-F_D|\,\frac{du}{u}
&\le C N^{-2}\int_{u_0}^1u^{-4}\,du
 +C e^{-c_1N^2u_0}\int_{u_0}^1u^{-3}\,du\\
&\le C N^{-2}u_0^{-3}
 +C u_0^{-2}e^{-c_1N^2u_0}\\
&=O\!\left(N^{-2}(\log N)^3\right).
\end{aligned}
\tag{21}
\]

这里第二项比任何固定 N 负幂都小，因为其指数为负常数乘 \(N^2/\log N\)。合并 (18)–(21) 便得 (1)。这三次使用的输入分别是实际全局计数界、统一四阶字符格点估计、可积大端点误差，彼此不能互相替代。

本证明没有说明 \((\log N)^3\) 是必需的，也没有证明不带对数的 \(O(N^{-2})\)。这些对数来自当前分割与绝对误差估计，不是已确定的次级渐近系数。

## 5. 临界振幅和全部复参数轮廓的定量推论

沿用 [上一轮第 5 节][finite] 的精确恒等式

\[
N^3\log(\kappa_N/B_*^N)+2\log N
=A_N-\gamma+N^3\mathcal E_N(1),
\quad |A_N-A_D|\le\rho_N,
\quad C_D=A_D-\gamma.
\]

其中 \(\mathcal E_N(1)=O(e^{-cN})\) 的合法边界值已在先前笔记证明，而 \(C_D\) 已有绝对收敛 theta 积分与明确标量格点 zeta 导数表达。本轮不重新引入或重选该常数。由 (1)，

\[
\boxed{
N^3\log\frac{\kappa_N}{B_*^N}+2\log N
=C_D+O\!\left(N^{-2}(\log N)^3\right),}
\tag{22}
\]

\[
\boxed{
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D}{N^3}
+O\!\left(N^{-5}(\log N)^3\right).}
\tag{23}
\]

再用 [上一轮第 6 节][finite] 的 Laplace 函数
\(\mathcal J_D(a)=\int_0^\infty e^{-au}F_D(u)du/u\)，及其中已经单独证明的
\(\sup_{\operatorname{Re}a>0}|a\mathcal J_D(a)|<\infty\)，得

\[
\boxed{
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
\left|N^3E_N^+(1+z)-\mathcal J_D(N^2z)\right|
=O\!\left(N^{-2}(\log N)^3\right).}
\tag{24}
\]

故在整个开右半单位圆盘上，

\[
\boxed{
\frac{Q_N(N(1+z))}
{B_0(1+z)^N\exp\!\left(N^{-3}\mathcal J_D(N^2z)\right)}
=1+O\!\left(N^{-5}(\log N)^3\right)}
\tag{25}
\]

一致成立。\(R_N\) 除以相同基准也满足 (25)，因 \(\log B(N(1+z))\) 在该域指数小。这里的精细轮廓是复函数 \(\mathcal J_D\)，不是用 \(\log|z|\) 替换复对数而丢失相位的径向近似。

没有给 \(z=0\) 的原 Euler 产品赋有限值，没有证明边界导数或整条边界的延拓性质。即使 z 任意极端切向逼近，本结论仍只覆盖 \(\operatorname{Re}z>0\)；统一性来自 (3) 的绝对可积差和此前 Laplace 导数论证。

## 6. 证据与状态边界

- 新数学增量为 (7)–(25) 的推导；全局 Gaussian 界、统一本原 PGT 转换、零类首系数、有限部分恒等式与 Laplace 转移界均明确继承前两篇笔记。
- 本轮仅通过普通浏览核对 Sharp 作者版相关段落，没有补跑数值实验、改变来源旧状态、导入外部模型或使用 API 获取资料。此前 PDF 截图访问失败记录不被改写为成功，本轮不重试它们。
- \(O\) 常数及足够大 N 的阈值没有数值认证；不宣称最优误差、非零下一阶系数或全曲面族一致性。
- 不改变冻结方案、正式稿、输入锁、审查回执、canonical 产品或 Route 状态。文档结构／字节保全检查和另一研究代理的复核不是独立科学证据。

[finite]: internal_diffusive_theta_profile_and_critical_finite_part_20260908.md
[tail]: internal_integrable_character_tail_and_global_radial_profile_20260908.md
[sharp]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf
