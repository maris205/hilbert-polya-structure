# P30 Goal01：真实三盘的逐频率谱下降与紧频带统一界

日期：2026-09-09 UTC。本文件为持续目标中的主代理新纸面推导。
只新增内部笔记，不修改既有稿件、实验、锁定输入或任何正式状态。

## 1. 结论与固定输入

固定半径 a、中心距 6a 的原三盘、单位飞行速率及逐碰撞编码。
使用[一侧 roof 笔记][roof]式 (10)、(14)、(16)–(17) 的同一个
正 Hölder 函数 g、固定 Banach 空间 \(\mathcal B_\beta\) 与算子

\[
(\mathcal L_su)(x)=\sum_{j\ne x_0}e^{-sg(jx)}u(jx),
\qquad 2a\le g\le10a,
\qquad q=\theta^\beta=\sqrt\rho<1.
\tag{1}
\]

令 \(\lambda_t=\lim_n\|\mathcal L_t^n1\|_\infty^{1/n}>0\)，t 为实数。
上游式 (28) 已证明

\[
r(\mathcal L_{t+ib})\le\lambda_t,
\qquad r_{\rm ess}(\mathcal L_{t+ib})\le q\lambda_t.
\tag{2}
\]

本文件补足实参数正本征函数的来源接口，并利用[第三周期笔记][period3]
的新几何证明得到

\[
\boxed{r(\mathcal L_{t+ib})<\lambda_t
\quad(t\in\mathbb R,\ b\in\mathbb R\setminus\{0\}).}
\tag{3}
\]

进一步，对任意固定紧区间 I 和 \(0<\delta\le B<\infty\)，存在
\(C<\infty\)、\(0<\kappa<1\)，使

\[
\boxed{\sup_{t\in I,\ \delta\le|b|\le B}
\|\lambda_t^{-n}\mathcal L_{t+ib}^n\|_{\beta\to\beta}
\le C\kappa^n\quad(n\ge0).}
\tag{4}
\]

这是固定参数算子的幂，不是任意变化参数算子的乘积。C、kappa
依赖 I、delta、B；(4) 不含 b 趋零或趋无穷的统一断言。

## 2. 实 RPF 定理的准确来源及空间匹配

一侧允许矩阵 \(A=J-I\) 满足 \(A^2>0\)，故是混合有限型移位。
对实势 \(f=-tg\)，使用 Stoyanov 的 [Theorem 2.1(i)、(iii)][rpf]：
存在同一 Hölder 类的严格正本征函数、正本征值，且正本征值简单，
其余谱与其分离。本文件需要的部分只是

\[
h_t\in\mathcal B_\beta,\qquad
\min h_t>0,\qquad
\mathcal L_t h_t=\lambda_t h_t.
\tag{5}
\]

来源的 \(F_\vartheta\) 以柱集变差定义；这里取
\(\vartheta=q=\theta^\beta\)。如果柱集索引从最后一个相同坐标
而非第一个不同坐标计数，两个半范数只差固定 q 因子，函数空间相同、
范数等价，算子和谱没有改变。

来源本征值确实等于本页的 lambda：若来源本征值为 l>0，
\(0<m\le h\le M\)，正性给

\[
\frac{m}{M}l^n\le\mathcal L_t^n1(x)
\le\frac{M}{m}l^n.
\tag{6}
\]

取 n 次根即 l=lambda。来源身份与定理正文由主代理实际浏览核对；
援引的是数学定理，不是重新证明 RPF，也不是上游只证准紧性的段落
已经包含 (5)。没有把一般正 roof 当作高频抵消前提。

## 3. 外围本征函数推出逐点常相位共调

固定实 t 及 b 非零，反设 \(r(\mathcal L_{t+ib})=\lambda_t\)。
由 (2)，该反设下本质谱半径严格小于谱半径。因此存在外围本征值
\(z\lambda_t\)、\(|z|=1\)，及非零 \(u\in\mathcal B_\beta\)。
这里使用准紧算子的有限维外围谱结论；[Hennion 的 Definition 3.1、
Proposition 3.1][hennion]给出相应谱分解。仅在反设下使用这个结论，
并不事先宣称全部复参数都满足 \(r_{\rm ess}<r\)。

由 (5) 和 Banach 代数的乘积差商，
\(v=u/h_t\in\mathcal B_\beta\)。定义正转移概率

\[
p_t(y\mid x)=\frac{e^{-tg(y)}h_t(y)}{\lambda_t h_t(x)}
\quad(\sigma y=x),\qquad
\sum_{\sigma y=x}p_t(y\mid x)=1.
\tag{7}
\]

本征方程变为

\[
zv(x)=\sum_{\sigma y=x}p_t(y\mid x)e^{-ibg(y)}v(y).
\tag{8}
\]

取 \(|v|\) 在紧空间上的最大点 x，最大值记为 M>0。则

\[
M=|zv(x)|\le\sum_{\sigma y=x}p_t(y\mid x)|v(y)|\le M.
\tag{9}
\]

两个不等式都取等，而所有概率严格为正，所以每个前像也满足
\(|v(y)|=M\)。逐次重复得到全部有限前像均达到 M。

这些有限前像稠密：任给合法有限柱词 w，选择一个同时不同于
w 末字母与 x 首字母的桥接字母 j，则前接后的 wjx 是合法序列，
位于该柱集且经有限次移位回到 x。三个字母保证这种 j 总存在。
于是连续性给 \(|v|\equiv M\)。这先解决了零点问题。

现在在每个 x 上重用 (9) 的等号条件，所有复数项都必须与
\(zv(x)\) 相同，故对每个 y，

\[
e^{-ibg(y)}v(y)=zv(\sigma y).
\tag{10}
\]

令 \(F=v/M\)，则 F 逐点取值于单位圆，并满足

\[
e^{ibg}=z^{-1}\frac{F}{F\circ\sigma}.
\tag{11}
\]

这正是非零频率带任意常相位的逐点共调关系。

## 4. 三条实际周期排除外围谱

由上游保周期共边界，g 在三条实际周期上的和分别为

\[
T_2=8a,\quad T_3=(18-3\sqrt3)a,\quad
T_4=4a\bigl(\sqrt{37-6\sqrt3}-1\bigr).
\tag{12}
\]

第三周期不是拟造的符号势；[其几何证明][period3]逐项验证了反射、
首次碰撞、本原性以及盘 1 两次相同位置对应不同速度。该笔记证明

\[
\frac{T_4/4-T_2/2}{T_3/3-T_2/2}\notin\mathbb Q.
\tag{13}
\]

沿三周期相乘 (11)，再消去常相位，必使 (13) 的 2/3 倍为两个
整数之比；分母由 b 非零和 \(2T_3-3T_2>0\) 保证非零，矛盾。
故反设不成立，(3) 得证。此处没有使用仅几乎处处成立的方程，
也没有调用 Livšic 逆向充分性。

## 5. 紧频带不能只交换极限与上确界

先证明 lambda 连续。因为 \(|S_ng|\le10an\)，对任意实 t、t'，

\[
e^{-10an|t-t'|}A_n(t)\le A_n(t')
\le e^{10an|t-t'|}A_n(t),
\]
\[
|\log\lambda_t-\log\lambda_{t'}|\le10a|t-t'|.
\tag{14}
\]

取紧参数集 \(K=I\times\{b:\delta\le|b|\le B\}\)，记
\(A_p=\lambda_t^{-1}\mathcal L_{t+ib}\)。上游算子范数整性与
(14) 给 p 到 A_p 的算子范数连续性。谱半径公式
\(r(A)=\inf_{n\ge1}\|A^n\|^{1/n}\) 表明谱半径上半连续。
紧性及 (3) 因而给

\[
r_*:=\max_{p\in K}r(A_p)<1.
\tag{15}
\]

选择 \(r_*<\kappa<1\)。对每个 p，有某个整数 \(n_p\ge1\)
满足 \(\|A_p^{n_p}\|<\kappa^{n_p}\)；此严格不等式在 p 的
一个邻域内保持。有限子覆盖只需有限个块长，令最大块长为 N，
并令 \(D=\max(1,\sup_K\|A_p\|)\)。对任意固定 p，取其覆盖邻域
的块长 n_j，把 n 写成 kn_j+r，\(0\le r<n_j\)。则

\[
\|A_p^n\|\le\kappa^{kn_j}D^r
\le(D/\kappa)^{N-1}\kappa^n.
\tag{16}
\]

这证明 (4)，而没有交换未经控制的 sup 与 n 极限。对应归一化
resolvent 在 \(|z|>\kappa\) 满足

\[
\sup_{p\in K}\|(zI-A_p)^{-1}\|
\le\frac{C}{|z|-\kappa}.
\tag{17}
\]

取 z=1 时得到紧频带上的逆算子界。它是归一化传输的 resolvent，
不自动等于物理散射 resolvent 或某个量子算子的 resolvent。

## 6. 证据边界与后续最小问题

- (3) 是相对于实权增长率的严格下降，不是断言复算子自身总是准紧；
  若其实际谱半径已落入本质谱圆盘，本页不排除这种情况。
- (4) 的 B 有限、delta 正，不能延拓为所有频率的同一常数。近零
  二阶展开、实际 roof 方差及高频抵消是不同的后续义务。
- [高频来源接口笔记][highfreq]指出真实平面开放台球已有几何空间
  的 Dolgopyat 型结果，但自然盘字的整个符号 Hölder 空间不能
  未经映射与范数核对便直接承接这些估计。
- 没有声明核性、trace-class、Fredholm determinant、完整流 zeta
  延拓或量子谱身份；本页也不重新定义算术时钟或改变 Route 状态。
- 主代理先独立推导，再委派同模型家族的有界反对意见核查。核查
  要求补清反设下外围本征函数、先证无零点、有限开覆盖分块三个
  环节；本稿已显式写出。这不构成外部独立科学认证。

主代理真实浏览了 Stoyanov Theorem 2.1 及其定义，另核对 Pollicott
作者论文集载体中的 Chapter 1 §1 Theorem 1、§2 Theorem 2，作为
经典实／复 RPF 背景；本稿实定理引用以前者精确正文为准。初始 DOI
直接打开与 Walters 数字化 PDF 打开返回技术错误，未把失败访问
冒称成功或将其正文作为证据。无需为该结果访问受限全文或上传私稿。

本文件仅经 apply_patch 新建；未执行科学／符号程序、轨道枚举、
实验、producer、checker、构建或正式审查。ARS 用于区分来源定理、
本地新几何应用、非一致性边界与未解问题。

[roof]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[period3]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_third_period_and_phase_obstruction_20260909.md
[highfreq]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_geometric_high_frequency_source_interface_20260909.md
[rpf]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CB2551C056FCA34005BC6EA1B4C9DBB3/S0008439500022980a.pdf/on_gibbs_measures_and_spectra_of_ruelle_transfer_operators.pdf
[hennion]: https://www.numdam.org/item/PSMIR_1995___2_A6_0.pdf
