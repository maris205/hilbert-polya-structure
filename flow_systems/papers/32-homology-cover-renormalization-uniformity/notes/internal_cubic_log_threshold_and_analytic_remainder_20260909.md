# P32 内部研究：二阶轮廓的三次对数阈值与亚纯正则部分

记录日期：2026-09-09 UTC。第四次 P29–P33 五篇整轮内部论证。
承接[四次调和有限部分与对偶格级数][previous]。
固定曲面、整数同调基、全部有向本原 owner、时钟、压力函数和原产品
归一化全部沿用。本篇只分析已经出现的辅助二阶轮廓，不另构造谱算子，
不为原 Euler 产品在精确临界点赋有限值，也不提高已有的 N 误差阶。

主结论是：四维四次 theta 扣除的 \(u^{-4}\) 大端尾，恰产生唯一的
局部非解析项 \(-p_0a^3\operatorname{Log}a/6\)。去掉这项后，所得函数
在临界点解析，并有以负二次型格点值为候选简单极点的亚纯延拓。
临界有限部分为零，与这个对数项消失，是两个不同条件。

## 1. 继承的积分表示与二次型下界

沿用

\[
\mathsf Q=2\pi^2D>0,\quad q(x)=x^{\mathsf T}\mathsf Qx,\quad
P(x)=s_4(2\pi x),\quad
c_D=\int_{\mathbb R^4}e^{-q(x)}\,dx,\quad
p_0=\int_{\mathbb R^4}P(x)e^{-q(x)}\,dx.
\tag{1}
\]

P 为真实压力函数的四次齐次项，不是为了取得某种系数而自由拟合的
多项式。记

\[
\Theta_P(u)=\sum_{k\in\mathbb Z^4}P(k)e^{-uq(k)},\qquad
G_P(u)=\Theta_P(u)-p_0u^{-4}.
\tag{2}
\]

上一轮已经证明

\[
\mathcal L_{D,P}(a)=\int_0^\infty e^{-au}G_P(u)\,du,\quad
\operatorname{Re}a>0,\qquad
K_{D,P}=\mathcal L_{D,P}(0)=\int_0^\infty G_P(u)\,du,
\tag{3}
\]

以及 \(G_P(u)=O(u^{-6}e^{-b/u})\) 在零端成立。

令

\[
q_*=\min_{k\in\mathbb Z^4\setminus\{0\}}q(k)>0.
\tag{4}
\]

其存在性不需要实际最短向量求解：正定性给
\(q(k)\ge c\|k\|^2\)，每个有界 q 子水平集只含有限多个格点，
故非零格点上的正最小值存在。以下只以 q_* 表述解析域，不提供它的
数值证书。

因 \(P(0)=0\)，对 \(u\ge1\) 有

\[
|\Theta_P(u)|
\le e^{-q_*u}
\sum_{k\ne0}|P(k)|e^{-(q(k)-q_*)}
=O(e^{-q_*u}).
\tag{5}
\]

求和有限由四次多项式增长与 Gaussian 衰减保证。因此
\(G_P(u)=-p_0u^{-4}+O(e^{-q_*u})\) 在无穷端成立。

## 2. 两阶矩有限，第三阶矩需要有限部分

定义三个绝对收敛矩

\[
M_j=\int_0^\infty u^jG_P(u)\,du,\qquad j=0,1,2.
\tag{6}
\]

零端的指数界允许任何固定多项式权；大端的
\(u^{j-4}\) 在 \(j<3\) 时绝对可积。特别是 \(M_0=K_{D,P}\)。
在闭右半平面用这些可积权作支配，可将 (3) 的前两阶导数连续延伸
至 a=0，得到

\[
\mathcal L_{D,P}(0)=M_0,\quad
\mathcal L_{D,P}'(0)=-M_1,\quad
\mathcal L_{D,P}''(0)=M_2.
\tag{7}
\]

这里导数先在开右半平面定义，a=0 的值为其连续边界值，亦等于
正实半轴的一侧导数。没有在此断言穿过原点的全纯性。

第三阶普通矩的大端为 \(-p_0/u\)。置

\[
\mathcal R_3=
\int_0^1u^3G_P(u)\,du+
\int_1^\infty u^3\Theta_P(u)\,du.
\tag{8}
\]

两个积分都绝对收敛。它不是在 \(p_0\ne0\) 时给发散的
\(\int u^3G_P\) 冒称普通积分，而是明确将大端幂尾分离的有限部分。

## 3. 精确分离全部非解析性

定义

\[
\mathscr B(a)=
\int_0^1e^{-au}G_P(u)\,du+
\int_1^\infty e^{-au}\Theta_P(u)\,du.
\tag{9}
\]

第一项为整函数：紧 u 区间上的 \(|G_P|\) 可积，且
\(|e^{-au}|\le e^{|a|}\)。第二项由 (5) 在
\(\operatorname{Re}a>-q_*\) 全纯，任意固定阶微分可在该半平面的紧集
上一致支配。因此 \(\mathscr B\) 在该半平面全纯，且
\(\mathscr B'''(0)=-\mathcal R_3\)。

使用广义指数积分

\[
E_4(a)=\int_1^\infty e^{-au}u^{-4}\,du,\qquad
\boxed{\mathcal L_{D,P}(a)=\mathscr B(a)-p_0E_4(a)}
\quad(\operatorname{Re}a>0).
\tag{10}
\]

该积分定义与主支约定核对 [DLMF 8.19.3][en]。
以下仅用标准指数积分公式，模型相关的分离与收敛证明均由 (2)–(9)
给出。

对 \(E_n(a)=\int_1^\infty e^{-au}u^{-n}du\) 分部积分，端点直接给
\(nE_{n+1}(a)=e^{-a}-aE_n(a)\)，与
[DLMF 8.19.12][recurrence] 一致。连续用 n=1,2,3 得

\[
E_4(a)=\frac{(2-a+a^2)e^{-a}-a^3E_1(a)}6.
\tag{11}
\]

在主支 \(\operatorname{Log}\) 下，
[DLMF 6.6.2][e1] 给出
\(E_1(a)=-\gamma-\operatorname{Log}a-
\sum_{n\ge1}(-a)^n/(n\,n!)\)，其中 \(\gamma\) 为 Euler 常数，
幂级数对全部有限 a 收敛。代入 (11)，定义整函数

\[
V_4(a)=\frac{(2-a+a^2)e^{-a}}6+
\frac{a^3}{6}
\left(\gamma+\sum_{n=1}^\infty\frac{(-a)^n}{n\,n!}\right).
\tag{12}
\]

于是以下是精确恒等式，而不只是有限阶渐近式：

\[
E_4(a)=\frac{a^3}{6}\operatorname{Log}a+V_4(a),\qquad
\boxed{
\mathcal L_{D,P}(a)
=-\frac{p_0}{6}a^3\operatorname{Log}a+\mathscr A(a)},
\quad \mathscr A(a)=\mathscr B(a)-p_0V_4(a).
\tag{13}
\]

\(\mathscr A\) 在 \(\operatorname{Re}a>-q_*\) 全纯。
等式先在 \(\operatorname{Re}a>0\) 成立，再给出与其相接的 slit 域
上的延拓；原积分 (3) 本身并不因这个表达式而在左半平面收敛。

**命题 1。** \(\mathcal L_{D,P}\) 可全纯延拓穿过 a=0，当且仅当
\(p_0=0\)。

充分性由 (13) 立即成立。必要性也可由第 4 节沿正实轴的第三导数
对数发散证明，因此不能靠另选对数支消去。对非零小 a 绕原点正向
延拓一周，(13) 的变化量为
\(-2\pi i\,p_0a^3/6\)；这是同一个障碍的分支表述。

## 4. 明确三次展开、余项与正则性

从 (12) 展开普通整函数得到

\[
E_4(a)=\frac13-\frac a2+\frac{a^2}{2}
+\frac{a^3}{6}
\left(\operatorname{Log}a+\gamma-\frac{11}{6}\right)
+O(|a|^4).
\tag{14}
\]

常数 \(11/6=1+1/2+1/3\) 来自
\((2-a+a^2)e^{-a}\) 的三次系数，不改变原产品中的任何归一化常数。

由 (6)、(8)、(9) 识别 \(\mathscr B\) 的前三阶导数，再结合 (14)，得

\[
\boxed{
\begin{aligned}
\mathcal L_{D,P}(a)
={}&K_{D,P}-aM_1+\frac{a^2}{2}M_2
-\frac{p_0}{6}a^3\operatorname{Log}a\\
&+\frac{a^3}{6}
\left[p_0\left(\frac{11}{6}-\gamma\right)-\mathcal R_3\right]
+O(|a|^4).
\end{aligned}}
\tag{15}
\]

取任意固定 \(0<r<q_*\)，余项在
\(0<|a|\le r,\ \operatorname{Re}a\ge0\) 中一致成立，包括任意切向趋近。
更精确地，减去所列对数项后，余项是 \(\mathscr A\) 的普通 Taylor
余项；所以同一结论在主支 slit 小圆盘内也一致成立。这里不需要
令 \(\operatorname{Re}a\) 与 \(|a|\) 保持某个正比例。

不能只从一个未说明解析性的 \(O(|a|^4)\) 符号随意求三阶导数；
本篇能求导是因为 (13) 已将其余部分证明为解析函数。由
\(E_4'''(a)=-E_1(a)\) 及 \(\mathscr B'''(0)=-\mathcal R_3\)，对实
\(a\downarrow0\) 有

\[
\boxed{
\mathcal L_{D,P}'''(a)
=-p_0\log a-p_0\gamma-\mathcal R_3+O(a).}
\tag{16}
\]

因此若 \(p_0\ne0\)，正实半轴上的连续延伸具有两阶连续导数，却
没有有限的第三阶一侧导数。确切地，由 (13)–(15) 两次求导可得
\[
\frac{\mathcal L_{D,P}''(a)-M_2}{a}
=-p_0\log a+p_0(1-\gamma)-\mathcal R_3+O(a),
\]
所以在零点的一侧差商本身发散，不只是三阶导数的邻域值无界。
前两阶连续性不能提升为三阶或解析。
若 \(p_0=0\)，则 (13) 直接给穿过零点的全纯延拓，而不只是三阶光滑。

### 4.1 任意分割点给出同一个三次常数

对任意 \(U>0\)，令

\[
\mathcal R_3(U)=
\int_0^Uu^3G_P(u)\,du+
\int_U^\infty u^3\Theta_P(u)\,du.
\tag{17}
\]

微分上下限，利用 \(G_P-\Theta_P=-p_0u^{-4}\)，得到

\[
\frac{d}{dU}\mathcal R_3(U)=-\frac{p_0}{U},\qquad
\mathcal R_3(U)+p_0\log U=\mathcal R_3(1).
\tag{18}
\]

相应的大端幂尾是 \(U^{-3}E_4(aU)\)；其中的
\(\operatorname{Log}(aU)=\operatorname{Log}a+\log U\) 与 (18)
恰好抵消。故 (15) 的三次常数不依赖人为选择的积分分割点。
这不是再调整一次有限部分定义。

## 5. 正则部分的亚纯延拓与可消极点

对 \(\operatorname{Re}a>-q_*\)，(5) 的绝对支配允许对 (9) 的第二项
逐格点积分：

\[
\mathscr B(a)
=\int_0^1e^{-au}G_P(u)\,du
+\sum_{k\in\mathbb Z^4\setminus\{0\}}
\frac{P(k)e^{-(q(k)+a)}}{q(k)+a}.
\tag{19}
\]

这个指数加权级数与上一轮不能未经论证使用的
\(\sum P(k)/q(k)\) 不同。对任何避开分母零点的紧复集，除有限多个
k 外，分母模长至少 \(q(k)/2\)，而分子被
\(C|P(k)|e^{-q(k)}\) 支配，所以级数绝对且局部一致收敛。

集合
\(\mathcal E=\{q(k):k\in\mathbb Z^4\setminus\{0\}\}\)
在任意有界区间中有限。每个 q 值的格点层也有限。因此 (19) 将
\(\mathscr B\)，进而 \(\mathscr A=\mathscr B-p_0V_4\)，延拓为整个
复平面上的亚纯函数，候选极点只位于 \(a=-\lambda\)，
\(\lambda\in\mathcal E\)，阶数至多一，且

\[
\boxed{
\operatorname*{Res}_{a=-\lambda}\mathscr A(a)
=\sum_{\substack{k\in\mathbb Z^4\\q(k)=\lambda}}P(k).}
\tag{20}
\]

证明中每个分子在该点的指数因子等于 1；其余格点及两个整函数项
都解析。若该层总权重为零，候选极点完全可消，不能把每个 q 值都
宣称为实际极点。

当 \(p_0=0\) 时，这也是 \(\mathcal L_{D,P}\) 自身的单值亚纯延拓。
当 \(p_0\ne0\) 时，具有单值亚纯延拓的是去对数后的
\(\mathscr A\)，而非 \(\mathcal L_{D,P}\) 本身；两者不可混报。
这里的负 q 值和留数是一个已定义 theta 系数的解析结构，不是已经
构造的 Hilbert–Pólya 谱或全局 determinant equality。

### 5.1 低阶矩也有合法的指数加权格点表达

对非负整数 j 和正 q，反复分部积分给

\[
I_j(q)=\int_1^\infty u^j e^{-qu}\,du
=e^{-q}j!\sum_{\ell=0}^j
\frac{1}{\ell!\,q^{j+1-\ell}}.
\tag{21}
\]

于是对 \(j=0,1,2\)，

\[
M_j=
\int_0^1u^jG_P(u)\,du
+\sum_{k\ne0}P(k)I_j(q(k))
-\frac{p_0}{3-j},
\tag{22}
\]

而
\(\mathcal R_3=\int_0^1u^3G_P(u)du+\sum_{k\ne0}P(k)I_3(q(k))\)。
这些格点和绝对收敛，因为 (21) 保留了 \(e^{-q}\)。
它们是有证明的求值表达，不是本轮已经求出的数值。

不能把上一轮 K 的绝对收敛对偶格级数随意加入 u 或 \(u^2\) 权后
逐项积分；所得幂次支配已经不同，上一轮的 Fubini 论证不能原样继承。
(22) 提供的合法途径是先保留有限分割与指数权。

## 6. 调和临界值与径向对数项是不同信息

上一轮证明

\[
K_{D,P}=K_{D,P_{\rm h}},\qquad
p_0=\frac{c_D}{32}\Delta_{\mathsf Q}^2P.
\tag{23}
\]

所以 K 消去全部 \(qR_2\) 分量，而三次对数系数由 Gaussian 平均
p_0 决定。若 P 本身为 Q-调和四次多项式，p_0=0，二阶轮廓在
原点解析；其临界值 K 仍可能为零或非零。

用纯代数测试方向 \(P=\alpha q^2\) 可看出逆向误推的危险。
由 \(\Delta_{\mathsf Q}q=8\)、
\(\Delta_{\mathsf Q}(q^2)=24q\)，有
\(\Delta_{\mathsf Q}^2(q^2)=192\)，故

\[
K_{D,\alpha q^2}=0,\qquad
p_0=6\alpha c_D,\qquad
-\frac{p_0}{6}a^3\operatorname{Log}a
=-\alpha c_Da^3\operatorname{Log}a.
\tag{24}
\]

当 \(\alpha\ne0\) 时，临界有限部分恰为零，但轮廓仍不在零点解析。
这个例子只检验已定义线性泛函与正则性的区别，不断言实际曲面的
压力四次项是径向的，也没有改变实际 P。

对于原几何，p_0 是否为零、K 的符号、(20) 中哪些层留数消失，本轮
均未数值认证或作一般非消失结论。

## 7. 返回原产品时的范围限制

此前的双尺度产品展开含 \(a=N^2z\) 和
\(N^{-2}\mathcal L_{D,P}(a)\)。本篇 (15) 可用于其中
\(|N^2z|\) 小的区域，必须继续携带既有的 N 余项。
它不改变全右半圆盘展开的
\(O(N^{-7}(\log N)^4)\) 相对误差，也不通过形式求导得到原产品的
同阶导数误差。原精确临界 Euler 产品的定义与边界仍旧保持。

ARS 有界 argument-builder 流程用于区分继承的 theta 尾项、
可积矩、对数支、解析余项、亚纯延拓和实际求值。
普通公开来源仅核对 DLMF 的标准指数积分定义、递推及 E1 幂级数；
本案的 p_0 系数、低阶矩、延拓域、留数和输入限制均逐项证明。
没有进行新颖性检索，也不把这些标准 Laplace 技巧当作新方法命名。

首次文件补丁的一条数学行遗漏新增标记，补丁验证拒绝且未产生文件；
只读确认目标不存在后修正补丁格式并重试，没有改动任何旧文件。

实际仅新增本笔记，由主线程追加总记录。没有执行数值积分、格点
求和、符号代数、实验、fixture、历史 artifact writer、论文构建
或正式审查；未重试旧 Sharp／Bolza 来源失败。
旧稿、书目、冻结输入、协议、正式回执、失败记录、FAIL / BLOCK、
D06 Recovery 3、Route 与 Stage 5／6 边界均不变。

[previous]: internal_harmonic_quartic_finite_part_and_dual_lattice_series_20260908.md
[en]: https://dlmf.nist.gov/8.19#E3
[recurrence]: https://dlmf.nist.gov/8.19#E12
[e1]: https://dlmf.nist.gov/6.6#E2
