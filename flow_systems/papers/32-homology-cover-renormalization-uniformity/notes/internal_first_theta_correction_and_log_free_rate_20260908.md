# P32 内部研究：首个 theta 修正、无对数损失速率与二阶有限部分

记录日期：2026-09-08 UTC。接续[压力偶对称与定量误差][rate]、
[扩散 theta 与有限部分][finite]，属于第二次 P29–P33 五篇整轮内部论证。
固定带标记、曲率负一的闭双曲亏格二曲面、全部有向本原 owner、
原时钟和原对数归一化不变。所有常数只对这个固定几何对象及整数基统一。

本轮不直接优化上一轮的分割常数，而是显式取出此前被放进误差的
首个修正函数。其小尺度连续积分项恰由同一个零同调计数次系数扣除。
这个抵消使首修正可积，进而证明
\(\rho_N=O(N^{-2})\)，并给出临界有限部分的 \(N^{-5}\) 项。
没有数值认证、谱算子构造、科学程序执行或正式状态变更。

## 1. 输入、四阶项与固定精度

沿用前两篇定义的

\[
F_N(u)=N^4(N^2u)e^{-N^2u}a_N(N^2u),\qquad
F_D(u)=\sum_{k\in\mathbb Z^4}e^{-u q(k)}-c_Du^{-2},
\tag{1}
\]

其中 \(a_N\) 计数非零 \(N\mathbb Z^4\) 同调的全部有向本原轨道，

\[
q(x)=2\pi^2x^{\mathsf T}Dx,\qquad
c_D=\int_{\mathbb R^4}e^{-q(x)}\,dx
=(2\pi)^{-2}(\det D)^{-1/2}.
\tag{2}
\]

[上一轮][rate]已由唯一实极点证明 \(s(-\theta)=s(\theta)\)。
实解析性及固定小邻域内的六阶导数界因此给出

\[
s(\theta)=1-\tfrac12\theta^{\mathsf T}D\theta+s_4(\theta)
+O(|\theta|^6),\qquad P(x):=s_4(2\pi x).
\tag{3}
\]

\(s_4\)、P 都是实四次齐次多项式，可以为零，不预设符号。
将原字符邻域固定缩小后，仍有 \(s\ge s_0>0\) 和
\(1-s(\theta)\ge c|\theta|^2\)。所有缩域只吸收固定环带上的
指数小项，不改变实际计数、字符环面或整数基。

[可积字符尾项笔记][tail]从 Sharp Lemma 3 转换的无权本原计数，
对每个固定 \(p\) 给全字符一致式

\[
\pi_\theta(t)=\mathbf1_{\theta\in U}\operatorname{Li}(e^{s(\theta)t})
+O_p(e^t/t^p).
\tag{4}
\]

本轮一次固定 **p=5**。有限字符平均乘回归一化后，其余项为
\(O(N^4t^{-4})=O(N^{-4}u^{-4})\)，\(t=N^2u\)。
不令 p 随 N 增长，也不把固定同调点态展开直接用于移动类。

本文沿用 (4) 已有的 sharp 端点／重复转换证明。普通来源复核确认
[Sharp 作者稿 Proposition 1][sharp] 的实解析极点输入；
后续段落定位请求出现工具 Internal Error，未将该失败记成成功，
也未换通道重试。新的 p=5 使用的是已记录的“每个固定 p”命题，
不是假称本轮新核完另一份证明。

## 2. 从同一字符平均确定零类次系数

令 \(n_0(t)\) 为同一有向口径的零同调本原计数。Haar 正交性是精确等式

\[
n_0(t)=(2\pi)^{-4}\int_{[-\pi,\pi]^4}\pi_\theta(t)\,d\theta.
\tag{5}
\]

对 \(s\in[s_0,1]\)、充分大 t，Li 的两项展开一致给

\[
t e^{-t}\operatorname{Li}(e^{st})
=e^{-(1-s)t}\left(\frac1s+\frac1{s^2t}+O(t^{-2})\right).
\tag{6}
\]

它来自固定下端的分部积分；下端贡献也可吸收在所示余项中。

在 (5) 的局部主项中令 \(\theta=2\pi x/\sqrt t\)。Haar 测度化为
\(t^{-2}dx\)，并且

\[
\begin{aligned}
(1-s(2\pi x/\sqrt t))t&=q(x)-t^{-1}P(x)+O(t^{-2}|x|^6),\\
s(2\pi x/\sqrt t)^{-1}&=1+t^{-1}q(x)+O(t^{-2}|x|^4).
\end{aligned}
\tag{7}
\]

因此主项被积函数的展开为

\[
e^{-q(x)}
\left[1+t^{-1}\bigl(1+q(x)+P(x)\bigr)\right]
+O\!\left(t^{-2}(1+|x|^2+|x|^4+|x|^6+|x|^8)e^{-c|x|^2}\right).
\tag{8}
\]

说明统一性：缩小固定 U 后，真实相位、二次相位及二次减四次的
相位都大于 \(c|x|^2\)；在它们之间用实指数的一阶／二阶 Taylor
积分余项即可得到 (8)。不能只写
\(\exp(P(x)/t)=1+P(x)/t+O(P(x)^2/t^2)\)
而忘记增长区间的指数因子。补成全 \(\mathbb R^4\) 的截断尾
由 \(|x|\ge c_U\sqrt t\) 上的 Gaussian 界指数小。

四维 Gaussian 的各固定阶矩可积。将 (8) 积分，(4) 的 p=5
余项对 \(te^{-t}n_0\) 是 \(O(t^{-4})\)，恰足够吸收在括号的二阶余项中。
于是

\[
\boxed{
n_0(t)=\frac{e^t}{t^3}
\left(c_D+\frac{c_1}{t}+O(t^{-2})\right),\qquad
c_1=\int_{\mathbb R^4}(1+q(x)+P(x))e^{-q(x)}\,dx.}
\tag{9}
\]

特别地，\(\int q e^{-q}=2c_D\) 可由
\(\int e^{-a q}=a^{-2}c_D\) 对 a 微分得到，所以
\(c_1=3c_D+\int P e^{-q}\)。
该系数来自实际零类的同一个精确平均；不是为了抵消下面的积分
而自由选择的归一化。它若与先前固定零类展开的次系数比较，唯一性
强迫相等。没有新增正反向合并或因子二。

## 3. 首修正函数及其可积抵消

对 \(u>0\) 定义

\[
\boxed{
H(u)=
\sum_{k\in\mathbb Z^4}
\bigl(q(k)+uP(k)+u^{-1}\bigr)e^{-u q(k)}
-\frac{c_1}{u^3}.}
\tag{10}
\]

其级数在任意紧正 u 区间连同各阶 u 导数绝对一致收敛。
H 是实函数，但不预设正负。由齐次性，令 \(y=\sqrt u\,x\) 得

\[
\int_{\mathbb R^4}
\bigl(q(x)+uP(x)+u^{-1}\bigr)e^{-u q(x)}\,dx
=\frac{c_1}{u^3}.
\tag{11}
\]

所以 (10) 正是同一个多项式乘 Gaussian 的格点和减连续积分。
对它逐坐标应用 [DLMF 1.8.14 的 Poisson 公式][poisson] 合法：
函数及所有导数快速衰减，迭代积分、求和和微分均绝对可换序。
这里的四维推广和多项式系数是本轮推导，不是来源原式的直接陈述。

在 Fourier 核 \(e^{-2\pi i x\cdot\xi}\) 下，基本 Gaussian 变换是
\(c_Du^{-2}\exp(-\xi^{\mathsf T}D^{-1}\xi/(2u))\)。
乘 x 的多项式对应对 \(\xi\) 微分；二次项最多产生
\(u^{-3}\) 乘关于 \(\xi/\sqrt u\) 的二次多项式，
四次项 uP 则产生同一 \(u^{-3}\) 乘四次多项式。
扣掉 (11) 正好删除零 Fourier 格点。正定性给

\[
H(u)=O(u^{-5}e^{-b/u})\quad(0<u\le1).
\tag{12}
\]

多项式格点因子可用一半 Gaussian 指数吸收，常数 b 可适当减小。
微分后的同类级数另给 \(H'(u)=O(u^{-7}e^{-b'/u})\)。

对 \(u\ge1\)，直接使用原格点表示，单独保留 k=0：

\[
H(u)=u^{-1}-c_1u^{-3}+O((1+u)e^{-bu}),
\tag{13}
\]

\[
H'(u)=-u^{-2}+3c_1u^{-4}+O((1+u)e^{-b'u}).
\tag{14}
\]

由 (12)–(14)，以下均为绝对收敛的普通积分：

\[
\|H\|_{1,*}:=\int_0^\infty |H(u)|\,\frac{du}{u}<\infty,
\qquad K_{D,P}:=\int_0^\infty H(u)\,\frac{du}{u}.
\tag{15}
\]

此外 \(h(u)=H(u)/u\) 在两端趋零且 \(\int|h'|du<\infty\)。
这些导数结论来自明确级数，不是由 H 的大小界推测；
更没有对实际阶梯计数 \(F_N\) 求导。

## 4. 全格点的二阶余项

令 \(K_N\) 为中心字符代表中满足 \(2\pi k/N\in U\) 的整数格点集，
\(t=N^2u\)。由 (3)，对所有 \(k\in K_N\) 有

\[
(1-s(2\pi k/N))t
=u q(k)-N^{-2}uP(k)+O(N^{-4}u|k|^6).
\tag{16}
\]

在上一节同样的固定正相位控制下，实指数的 Taylor 积分余项及
(6) 给出逐格点式

\[
\begin{aligned}
&t e^{-t}\operatorname{Li}(e^{s(2\pi k/N)t})\\
&\quad=e^{-u q(k)}
\left[1+N^{-2}\bigl(q(k)+uP(k)+u^{-1}\bigr)\right]+R_{N,k}(u),\\
&|R_{N,k}(u)|\le C N^{-4}e^{-cu|k|^2}
\left(u|k|^6+u^2|k|^8+|k|^4+u^{-1}|k|^2+u^{-2}\right).
\end{aligned}
\tag{17}
\]

例如 \(u|k|^6\) 同时覆盖真实六阶相位余项及一阶振幅乘四阶相位
的交叉项；\(u^2|k|^8\) 是指数 Taylor 的二次余项；
k=0 的 \(u^{-2}\) 来自 Li 下一项，不能删去。

这里 (17) 不要求 \(uP(k)/N^2\) 对所有格点绝对小；
只要求固定 U 上它相对二次正相位足够小，保证 Taylor 途径中
所有指数都受 \(e^{-cu|k|^2}\) 支配。

由有限字符平均与 (9)，

\[
N^4t e^{-t}n_0(t)
=c_Du^{-2}+N^{-2}c_1u^{-3}+O(N^{-4}u^{-4}).
\tag{18}
\]

在 \(0<u\le1\)，四维 Gaussian 矩界
\(\sum|k|^{2j}e^{-cu|k|^2}\le C_j u^{-2-j}\)，\(0\le j\le4\)，
使 (17) 每个余项求和后都是 \(O(N^{-4}u^{-4})\)。
未纳入的格点必满足 \(|k|\ge c_U N\)；将指数分半，主项及
首修正的合并截断尾至多 \(C u^{-3}e^{-cN^2u}\)。

记 \(\Delta_N(u)=F_N(u)-F_D(u)-N^{-2}H(u)\)。
合并 p=5 PGT、(17)、(18) 得，当 \(N^2u\ge T_0\) 时

\[
\boxed{
|\Delta_N(u)|\le C N^{-4}u^{-4}
+C u^{-3}e^{-cN^2u}\quad(0<u\le1).}
\tag{19}
\]

对 \(u\ge1\)，非零格点各固定阶矩指数小，而 k=0 需保留，
同样得到

\[
\boxed{
|\Delta_N(u)|\le
C N^{-4}\bigl(u^{-2}+u^{-4}+(1+u^2)e^{-bu}\bigr)
+C e^{-cN^2u}.}
\tag{20}
\]

这些估计对所有充分大整数 N 统一，不是用固定层未知常数作对角线估计。

## 5. 加权 L1 二阶展开与无对数损失主速率

[此前实际 Gaussian 界][rate]给
\(0\le F_N(u)\le C e^{-c/u}\)，而 \(F_D\) 的 Poisson 表示及 (12)
控制另外两项。取某个固定 \(b_0>0\)，有

\[
\int_0^{u_0}|\Delta_N(u)|\,\frac{du}{u}
\le C e^{-b_0/(2u_0)}
\quad(0<u_0\le1,\ N\ge1).
\tag{21}
\]

此处将固定负幂 u 因子吸收到半个小端指数中，且 \(N^{-2}\le1\)。
选择

\[
u_0=\frac{b_0}{16\log N}.
\tag{22}
\]

对充分大 N，(21) 是 \(O(N^{-8})\)，且 \(N^2u_0\ge T_0\)。
在 \([u_0,1]\) 积分 (19) 得
\(O(N^{-4}u_0^{-4})\)，截断尾比任意固定 N 负幂都小。
在 \([1,\infty)\) 积分 (20) 则为 \(O(N^{-4})\)。所以

\[
\boxed{
\sigma_N:=\int_0^\infty
|F_N(u)-F_D(u)-N^{-2}H(u)|\,\frac{du}{u}
=O\!\left(N^{-4}(\log N)^4\right).}
\tag{23}
\]

这是真实 sharp 计数在整个正轴上的加权 L1 展开，包含小尺度区域，
而不是只在固定紧区间上的形式展开。因为 H 可积，立即有

\[
\boxed{\rho_N:=\int_0^\infty|F_N-F_D|\,\frac{du}{u}
=O(N^{-2}).}
\tag{24}
\]

更精确地，逆三角不等式给

\[
\left|N^2\rho_N-\|H\|_{1,*}\right|
\le N^2\sigma_N\longrightarrow0.
\tag{25}
\]

(13) 说明 H 在充分大的 u 为正且不恒为零，故
\(\|H\|_{1,*}>0\)。因此 (24) 对这个特定绝对误差范数的幂次是精确的：
\(\rho_N\sim N^{-2}\|H\|_{1,*}\)。
这不说明有符号积分 \(K_{D,P}\) 非零，也不证明 (23) 的对数因子必要，
更不等于所有产品误差或其他范数均有相同最优阶。

## 6. 临界有限部分的第二项

沿用[有限部分笔记第 5 节][finite]已经建立的精确恒等式

\[
N^3\log(\kappa_N/B_*^N)+2\log N
=A_N-\gamma+N^3\mathcal E_N(1),
\quad C_D=A_D-\gamma,
\quad \mathcal E_N(1)=O(e^{-cN}).
\tag{26}
\]

其中 \(\mathcal E_N(1)\) 的合法边界值早已由其级数证明，不只是大小猜测。
由于 \(A_N-A_D=\int(F_N-F_D)\,du/u\)，(15)、(23) 给

\[
A_N-A_D=N^{-2}K_{D,P}
+O\!\left(N^{-4}(\log N)^4\right).
\tag{27}
\]

因而

\[
\boxed{
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D}{N^3}
+\frac{K_{D,P}}{N^5}
+O\!\left(N^{-7}(\log N)^4\right).}
\tag{28}
\]

这不改变先前 \(C_D\) 的定义。新系数通常还涉及压力四次项 P；
本轮只给其绝对收敛积分表达，不计算数值、不判定符号或非零性，
也不声称 D 单独决定全部高阶几何信息。

## 7. 全开右半单位圆盘的二阶复轮廓

对 \(\operatorname{Re}a>0\) 定义

\[
\mathcal J_H(a)=\int_0^\infty e^{-au}H(u)\,\frac{du}{u},\qquad
\mathcal L_{D,P}(a)=\mathcal J_H(a)+a\mathcal J_D(a).
\tag{29}
\]

其中 \(\mathcal J_D\)、\(\mathcal J_N\) 沿用[有限部分笔记][finite]。
由 (15)、(23)

\[
\sup_{\operatorname{Re}a>0}
|\mathcal J_N(a)-\mathcal J_D(a)-N^{-2}\mathcal J_H(a)|
\le\sigma_N,\qquad
|\mathcal J_H(a)|\le\|H\|_{1,*}.
\tag{30}
\]

另由 h 的端点和导数界分部积分，
\(a\mathcal J_H(a)=\int e^{-au}h'(u)\,du\)，故
\(\sup|a\mathcal J_H(a)|<\infty\)。
此前已经独立证明 \(\sup|a\mathcal J_D(a)|<\infty\)，
所以 \(\mathcal L_{D,P}\) 在该半平面也有界。

取 \(\operatorname{Re}z>0,\ |z|\le1,\ a=N^2z\)。精确式
\(N^3E_N^+(1+z)=(1+z)\mathcal J_N(a)+N^3\mathcal E_N(1+z)\)
与 (30) 给

\[
\boxed{
N^3E_N^+(1+z)
=\mathcal J_D(a)+N^{-2}\mathcal L_{D,P}(a)
+O\!\left(N^{-4}(\log N)^4\right)}
\tag{31}
\]

一致成立。交叉项是 \(N^{-4}a\mathcal J_H(a)\)，确实被上述单独导数
估计统一控制；不能因为 \(|z|\le1\) 就直接将它误记为 \(O(N^{-4})\)。
误差 (30) 的前因子 \(1+z\) 模长不超过 2。

完整产品因此满足

\[
\boxed{
\frac{Q_N(N(1+z))}
{B_0(1+z)^N
\exp\!\left(N^{-3}\mathcal J_D(N^2z)
+N^{-5}\mathcal L_{D,P}(N^2z)\right)}
=1+O\!\left(N^{-7}(\log N)^4\right).}
\tag{32}
\]

R_N 用同一分母也满足该式，因为被另外除去的
\(\log B(N(1+z))\) 在此域指数小。若只保留上一轮的首阶轮廓，
由于 \(\mathcal L_{D,P}\) 有界，其相对误差改进为 \(O(N^{-5})\)，
不再含 \((\log N)^3\)。

由 H 的可积性，\(a\to0,\ \operatorname{Re}a>0\) 时
\(\mathcal J_H(a)\to K_{D,P}\)，而
\(a\mathcal J_D(a)\to0\)，与 (28) 的新有限部分系数一致。
全程保留复 Laplace 函数及复相位，不以 \(\log|z|\) 替换复对数。
没有给 \(z=0\) 的原 Euler 产品赋有限值，也未声称整条临界边界可延拓。

## 8. 证据分工与仍未完成的事项

ARS 有界论证组织要求来源输入、系数识别、统一余项与产品转移分开。
本篇的新增数学是 (9)–(32)，尤其是零类次系数与连续积分的同源性；
实解析压力、全字符 PGT 转换、真实全局 Gaussian 界、原有限部分
恒等式及首阶 Laplace 导数界均明确继承。

本轮普通浏览成功读到 Sharp 作者稿的极点段落及 DLMF Poisson
公式；Sharp 后续 open／find 定位请求的工具错误保留，未绕路重试。
没有新增程序化来源核验、数值积分、矩阵／长度实验、枚举、论文构建、
artifact writer 或正式 reviewer／Route 流程。

本轮只针对充分大整数 N（因此包括冻结阶乘子序列），常数与阈值没有
数值认证。只对 \(\rho_N\) 证明了 (25) 的精确幂次；
没有证明 K 非零、余项最优、完整高阶级数、跨曲面族统一性或谱等式。
本文的有限部分及首修正是原标量产品的分析，不构造任何量子算子。

旧笔记中的当时边界不回写；本轮新证明通过新增笔记承接。
原论文、输入锁、失败记录、canonical 产品、FAIL / BLOCK、
Route 及 Stage 5／6 状态全部保持。文本保全检查和同系代理复核
不等于数学有效性或外部定理的独立认证。

[rate]: internal_quantitative_theta_error_and_pressure_symmetry_20260908.md
[finite]: internal_diffusive_theta_profile_and_critical_finite_part_20260908.md
[tail]: internal_integrable_character_tail_and_global_radial_profile_20260908.md
[sharp]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf
[poisson]: https://dlmf.nist.gov/1.8#E14
