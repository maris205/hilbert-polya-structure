# P32 内部研究：有限部分的调和四次项与绝对收敛对偶格点式

记录日期：2026-09-08 UTC。第三次 P29–P33 五篇整轮内部论证。
承接[首 theta 修正与无对数损失速率][previous]；曲面、整数同调基、
全部有向本原 owner、原时钟及原产品归一化均不变。

本轮进一步识别上一轮的 \(N^{-5}\) 系数。结论是：Li 振幅与二次压力
产生的通用修正在完整产品轮廓中精确抵消；临界有限部分还消去所有
“二次型乘二次多项式”的四阶压力分量。因此新系数只依赖四阶压力的
调和分量，并可写为具有明确截断尾界的绝对收敛对偶格点级数。

这里分析的是原标量产品已经出现的系数，不是改变压力函数以拟合
目标值，也不构造新的几何、谱算子或数值证书。

## 1. 沿用数据与上一轮已经证明的结果

固定

\[
\mathsf Q=2\pi^2D>0,\qquad q(x)=x^{\mathsf T}\mathsf Qx,\qquad
c_D=\int_{\mathbb R^4}e^{-q(x)}\,dx
=(2\pi)^{-2}(\det D)^{-1/2}.
\tag{1}
\]

\(\mathsf Q\) 是本节的二次型矩阵，不是原乘积 \(Q_N(s)\)。
压力四次齐次项记为 \(P(x)=s_4(2\pi x)\)，并置

\[
\Theta(u)=\sum_{k\in\mathbb Z^4}e^{-u q(k)},\quad
F(u)=F_D(u)=\Theta(u)-c_Du^{-2},\quad
p_0=\int_{\mathbb R^4}P(x)e^{-q(x)}\,dx.
\tag{2}
\]

上一轮从实际零同调 Haar 平均识别了 \(c_1=3c_D+p_0\)，定义

\[
H(u)=\sum_{k\in\mathbb Z^4}
(q(k)+uP(k)+u^{-1})e^{-u q(k)}
-(3c_D+p_0)u^{-3},
\tag{3}
\]

并证明 H 在权 \(du/u\) 下绝对可积、\(F(u)/u\) 两端趋零且导数可积。
原有限部分与全开右半单位圆盘的展开为

\[
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D}{N^3}
+\frac{K_{D,P}}{N^5}
+O(N^{-7}(\log N)^4),\qquad
K_{D,P}=\int_0^\infty H(u)\,\frac{du}{u},
\tag{4}
\]

\[
N^3E_N^+(1+z)
=\mathcal J_D(a)+N^{-2}\mathcal L_{D,P}(a)
+O(N^{-4}(\log N)^4),\quad
a=N^2z,\quad \operatorname{Re}z>0,\ |z|\le1,
\tag{5}
\]

其中 \(\mathcal J_D(a)=\int e^{-au}F(u)\,du/u\)，
\(\mathcal L_{D,P}(a)=\mathcal J_H(a)+a\mathcal J_D(a)\)。
本轮复用这些已经证明的统一估计，不重复实际计数的 PGT／Gaussian
推导，不声称新的 N 误差阶。

## 2. 完整轮廓中的精确抵消

定义四次多项式的去连续项格点函数

\[
\Theta_P(u)=\sum_{k\in\mathbb Z^4}P(k)e^{-u q(k)},\qquad
G_P(u)=\Theta_P(u)-p_0u^{-4}.
\tag{6}
\]

由四次齐次性，\(\int P(x)e^{-u q(x)}dx=p_0u^{-4}\)。
多项式 Gaussian 的 Poisson 公式给

\[
G_P(u)=O(u^{-6}e^{-b/u})\quad(u\downarrow0),\qquad
G_P(u)=-p_0u^{-4}+O(e^{-bu})\quad(u\to\infty).
\tag{7}
\]

第一个界沿用上一轮的同一推导：四次 Fourier 导数只产生有限个
Gaussian 多项式项，扣掉零 Fourier 格点，非零格点由正定性控制。
故 \(G_P\in L^1((0,\infty),du)\)。本轮普通浏览核对
[DLMF 1.8.14][poisson] 的公式及正则性条件；这里的四维形式和
多项式导数来自逐坐标应用及绝对收敛，并非来源直接陈述本项目结果。

因为 \(\Theta'=-\sum q(k)e^{-u q(k)}\)，直接微分 (2)、整理 (3) 得

\[
H(u)=-F'(u)+\frac{F(u)}u+uG_P(u),
\qquad
\boxed{\frac{H(u)}u=-\left(\frac{F(u)}u\right)'+G_P(u).}
\tag{8}
\]

注意 \(F'=\Theta'+2c_Du^{-3}\)，正是这个符号与维数系数使
右侧连续项为 \(-(3c_D+p_0)u^{-4}\)。

对 \(\operatorname{Re}a>0\)，(8) 可绝对积分。分部积分端点为零，
且 \(\int e^{-au}(F/u)'du=a\mathcal J_D(a)\)，故

\[
\boxed{
\mathcal L_{D,P}(a)=\int_0^\infty e^{-au}G_P(u)\,du,\qquad
K_{D,P}=\int_0^\infty G_P(u)\,du.}
\tag{9}
\]

第二式也可直接对 (8) 不加指数积分得到。因此不是把原计数中的 Li
修正忽略掉：它们在 H 中存在，在完整轮廓的 \(a\mathcal J_D\) 项
加入之后才精确抵消。若只看 H，不能先删除其 \(u^{-1}\) 大端项。

由 (7)，(9) 在 \(\operatorname{Re}a>0\) 全纯、有界，连续延伸到
闭右半平面，且 \(a\to0\) 时趋于 \(K_{D,P}\)。
这一连续边界值是辅助二阶轮廓的值，不给原临界 Euler 产品赋有限值。

## 3. 有限部分消去全部 q 乘二次项

令 R 为任意实二次齐次多项式，定义

\[
r_0=\int_{\mathbb R^4}R(x)e^{-q(x)}\,dx,\qquad
G_R(u)=\sum_{k\in\mathbb Z^4}R(k)e^{-u q(k)}-r_0u^{-3}.
\tag{10}
\]

这里 R 是多项式，不是项目的相对产品 \(R_N(s)\)。
与 (7) 相同的二次 Gaussian 计算给
\(G_R(u)=O(u^{-4}e^{-b/u})\) 在零端，且
\(G_R(u)=-r_0u^{-3}+O(e^{-bu})\) 在无穷端。
其导数也在两端可积，且 \(G_R(0+)=G_R(\infty)=0\)。

对 \(\int R e^{-uq}=r_0u^{-3}\) 求导得
\(\int qR e^{-q}=3r_0\)。逐项微分格点级数于是给

\[
G_{qR}(u)=-G_R'(u),\qquad
\boxed{K_{D,qR}=-[G_R(u)]_{0+}^{\infty}=0.}
\tag{11}
\]

所以 P 只要增加任意 \(qR\)，有限部分系数 K 就不变。
这是一条关于既定线性泛函 \(P\mapsto K_{D,P}\) 的恒等式，
不是允许任意更改真实压力四次项。

完整二阶轮廓却一般会改变：
\(\mathcal L_{D,qR}(a)=-a\int e^{-au}G_R(u)\,du\)。
例如纯代数检验情形 \(P=\alpha q^2\) 给

\[
G_{q^2}=F'',\qquad
K_{D,\alpha q^2}=0,\qquad
\mathcal L_{D,\alpha q^2}(a)
=-\alpha a^2\mathcal J_D'(a).
\tag{12}
\]

对实 \(a>0\)，\(F>0\) 使 \(\mathcal J_D'(a)<0\)，故 \(\alpha\ne0\)
时右侧不为零。这严格区分“有限部分的 \(N^{-5}\) 系数为零”和
“整个二阶复轮廓消失”。没有断言实际曲面的 P 具有这一径向形式。

## 4. 显式调和投影：35 维四次空间中的 10 维消去方向

定义与 q 相配的常系数微分算子

\[
\Delta_{\mathsf Q}
=\sum_{i,j=1}^4(\mathsf Q^{-1})_{ij}\partial_i\partial_j.
\tag{13}
\]

本文“调和四次多项式”指 \(\Delta_{\mathsf Q}P_{\mathrm h}=0\)。
它不是曲面上的调和函数或另一个谱算子构造。

对任意二次齐次 R，乘积法则及 \(x\cdot\nabla R=2R\) 给

\[
\Delta_{\mathsf Q}q=8,\qquad
\Delta_{\mathsf Q}(qR)=16R+q\Delta_{\mathsf Q}R.
\tag{14}
\]

令 \(S=\Delta_{\mathsf Q}P\)（二次）、\(c=\Delta_{\mathsf Q}^2P\)
（常数），设置

\[
R_P=\frac{S}{16}-\frac{qc}{384},\qquad
\boxed{
P_{\mathrm h}
=P-qR_P
=P-\frac{q\Delta_{\mathsf Q}P}{16}
+\frac{q^2\Delta_{\mathsf Q}^2P}{384}.}
\tag{15}
\]

由 \(\Delta_{\mathsf Q}R_P=c/24\)，(14) 给
\(\Delta_{\mathsf Q}(qR_P)=S\)，所以 \(P_{\mathrm h}\) 确实调和。

分解 \(P=P_{\mathrm h}+qR_P\) 唯一：若 \(qR\) 调和，则
\(16R+q\Delta_{\mathsf Q}R=0\)；再施一次 \(\Delta_{\mathsf Q}\)
得 \(24\Delta_{\mathsf Q}R=0\)，继而 R=0。
因此四变量四次齐次空间分成调和部分与 q 乘二次部分，
维数分别为 \(35-10=25\) 与 10。

结合 (11)，

\[
\boxed{K_{D,P}=K_{D,P_{\mathrm h}}.}
\tag{16}
\]

这是 K 的一组精确消去方向，不是说一个标量能恢复 25 个调和系数；
K 作为标量线性泛函在调和空间内还可能有核。

Gaussian 生成函数
\(\int e^{-q(x)+t\cdot x}dx=c_D\exp(t^{\mathsf T}\mathsf Q^{-1}t/4)\)
逐次微分还给

\[
\int P(x)e^{-q(x)}dx=\frac{c_D}{32}\Delta_{\mathsf Q}^2P.
\tag{17}
\]

所以 \(P_{\mathrm h}\) 的连续积分系数为零。
对它有 \(G_{P_{\mathrm h}}=\Theta_{P_{\mathrm h}}\)，而这个格点和在
零端及无穷端都指数衰减。原非调和 P 的连续扣除仍不能省略。

## 5. 调和 Gaussian 的 Fourier 变换与对偶格点式

采用 Fourier 核 \(e^{-2\pi i x\cdot\xi}\)，并记

\[
B(\xi)=\pi^2\xi^{\mathsf T}\mathsf Q^{-1}\xi
=\frac12\xi^{\mathsf T}D^{-1}\xi.
\tag{18}
\]

基本 Gaussian 变换为
\(\widehat{e^{-uq}}(\xi)=c_Du^{-2}e^{-B(\xi)/u}\)。
因乘 x 对应 \((i/(2\pi))\partial_\xi\)，

\[
\widehat{P_{\mathrm h}e^{-uq}}(\xi)
=\left(\frac{i}{2\pi}\right)^4
P_{\mathrm h}(\partial_\xi)
\left(c_Du^{-2}e^{-B(\xi)/u}\right).
\tag{19}
\]

为核对常数及调和性如何删除低阶项，可对平移参数 t 使用

\[
e^{t\cdot\partial_\xi}e^{-B(\xi)/u}
=e^{-B(\xi)/u}
\exp\!\left(-\frac{2\pi^2}{u}t^{\mathsf T}\mathsf Q^{-1}\xi\right)
\exp\!\left(-\frac{\pi^2}{u}t^{\mathsf T}\mathsf Q^{-1}t\right).
\tag{20}
\]

设 \(v=-2\pi^2\mathsf Q^{-1}\xi/u\)。对 t 取四次多项式微分再令 t=0，
所得多项式为

\[
P_{\mathrm h}(v)-\frac{\pi^2}{u}\Delta_{\mathsf Q}P_{\mathrm h}(v)
+\frac{\pi^4}{2u^2}\Delta_{\mathsf Q}^2P_{\mathrm h}(v)
=P_{\mathrm h}(v).
\tag{21}
\]

这里可直接将最后一个指数展开到 t 的四次项；更高次项对四次微分
无贡献。由齐次次数四及 \(i^4=1\)，(19) 化为

\[
\boxed{
\widehat{P_{\mathrm h}e^{-uq}}(\xi)
=c_D\pi^4u^{-6}P_{\mathrm h}(\mathsf Q^{-1}\xi)
e^{-B(\xi)/u}.}
\tag{22}
\]

特别是没有负号或额外方向因子二。Poisson 求和给

\[
\Theta_{P_{\mathrm h}}(u)
=c_D\pi^4u^{-6}
\sum_{m\in\mathbb Z^4\setminus\{0\}}
P_{\mathrm h}(\mathsf Q^{-1}m)e^{-B(m)/u}.
\tag{23}
\]

m=0 项为零。对每个正 B，换元 \(v=B/u\) 给

\[
\int_0^\infty u^{-6}e^{-B/u}\,du
=B^{-5}\int_0^\infty v^4e^{-v}\,dv=24B^{-5}.
\tag{24}
\]

由于 \(P_{\mathrm h}(\mathsf Q^{-1}m)=O(|m|^4)\) 而
\(B(m)\ge c|m|^2\)，下面的绝对值级数被 \(\sum_{m\ne0}|m|^{-6}\)
支配，在四维绝对收敛。因此对 (23) 的 u 积分交换求和有绝对依据，
不是把尚未可积的原格点项形式积分。结合 (9)、(16)，得到

\[
\boxed{
K_{D,P}
=24c_D\pi^4
\sum_{m\in\mathbb Z^4\setminus\{0\}}
\frac{P_{\mathrm h}(\mathsf Q^{-1}m)}
{(\pi^2m^{\mathsf T}\mathsf Q^{-1}m)^5}.}
\tag{25}
\]

完全用 D 表示的等价形式为

\[
\boxed{
K_{D,P}
=\frac{48c_D}{\pi^4}
\sum_{m\in\mathbb Z^4\setminus\{0\}}
\frac{P_{\mathrm h}(D^{-1}m)}
{(m^{\mathsf T}D^{-1}m)^5}.}
\tag{26}
\]

两个系数的换算使用
\(\mathsf Q^{-1}=(2\pi^2)^{-1}D^{-1}\) 和四次齐次性。
这是普通绝对收敛级数，无须为它另定义一个求和顺序或 zeta 正则化。

相反，不能从 \(K=\int\Theta_{P_{\mathrm h}}(u)du\) 直接写
\(\sum P_{\mathrm h}(k)/q(k)\) 并声称绝对收敛。原格点逐项积分
没有上面的绝对 Fubini 支配，零端抵消发生在整个格点和之内。

## 6. 明确的有限截断尾界

将
\(\widetilde P(y)=P_{\mathrm h}(\mathsf Q^{-1}y)
=\sum_{|\alpha|=4}a_\alpha y^\alpha\)，并记

\[
A_{\mathrm h}=\sum_{|\alpha|=4}|a_\alpha|.
\tag{27}
\]

选任一已证明的 \(b>0\)，使
\(B(y)\ge b\|y\|_\infty^2\) 对所有实 y 成立。
正定性保证存在这种 b；实际数值使用时仍须认证该下界及多项式系数，
不能把未认证的浮点最小特征值当作 b。

在整数格壳 \(\|m\|_\infty=n\ge1\) 上，单项绝对值至多
\(A_{\mathrm h}b^{-5}n^{-6}\)，且该格壳的点数恰为

\[
(2n+1)^4-(2n-1)^4=64n^3+16n.
\tag{28}
\]

令 \(K^{(M)}\) 为 (25) 只保留 \(0<\|m\|_\infty\le M\) 的有限和，
M 为正整数。对递减幂函数与积分比较得到

\[
\boxed{
|K_{D,P}-K^{(M)}|
\le24c_D\pi^4\frac{A_{\mathrm h}}{b^5}
\left(\frac{32}{M^2}+\frac4{M^4}\right).}
\tag{29}
\]

这是一个在系数与正定下界已知时可用于有限计算的数学尾证书。
本轮没有计算实际 D、P、\(A_{\mathrm h}\)、b、\(K^{(M)}\) 或任何数值 K，
也没有选择格点截断参数、执行级数求和或注册新的实验。
有限和本身的舍入误差若将来实际求值，还需另加，不能包含在 (29)
而未说明。

## 7. 整数换基不变性

令 \(A\in\operatorname{GL}_4(\mathbb Z)\)，沿用同调换基约定

\[
D'=ADA^{\mathsf T},\quad
\mathsf Q'=A\mathsf QA^{\mathsf T},\quad
P'(x)=P(A^{\mathsf T}x),\quad q'(x)=q(A^{\mathsf T}x).
\tag{30}
\]

链式法则直接给
\(\Delta_{\mathsf Q'}P'(x)=(\Delta_{\mathsf Q}P)(A^{\mathsf T}x)\)，
再施一次亦然，所以投影 (15) 满足
\(P_{\mathrm h}'(x)=P_{\mathrm h}(A^{\mathsf T}x)\)。
又 \(|\det A|=1\)，故 \(c_{D'}=c_D\)。

在 (25) 中，

\[
P_{\mathrm h}'(\mathsf Q'^{-1}m)
=P_{\mathrm h}(\mathsf Q^{-1}A^{-1}m),\qquad
B'(m)=B(A^{-1}m).
\]

整数格点双射 \(m\mapsto A^{-1}m\) 及绝对收敛给

\[
\boxed{K_{D',P'}=K_{D,P}.}
\tag{31}
\]

同理，由原格点双射 \(k\mapsto A^{\mathsf T}k\)，
\(G_{P'}^{D'}=G_P^D\) 及 \(\mathcal L_{D',P'}=\mathcal L_{D,P}\)。
它们是同一几何在整数坐标变换下的不变性，不是跨曲面族统一定理。
有限立方截断及 (29) 的具体常数可以依赖坐标，不能要求每个有限
\(K^{(M)}\) 也逐项换基不变。

## 8. 回到原产品与证据边界

将 (25) 或 (26) 代入 (4)，给出了原临界有限部分
\(N^{-5}\) 系数的更明确表达。将 (9) 代入 (5)，则完整二阶复轮廓
由单个 \(G_P\) 的 Laplace 积分表示。原两项产品轮廓的
\(O(N^{-7}(\log N)^4)\) 相对误差、任意切向的域和全部固定曲面
量词均继承上一轮，没有因为表达式变换自动取得更高 N 阶。

本轮精确说明了两种不同抵消：

- 完整二阶复轮廓中，Li 与纯二次压力的通用部分合为一个导数而抵消；
- 在临界有限部分 K 中，四次压力的 \(qR_2\) 部分进一步成为零边界项。

K 是否非零、符号如何，仍取决于实际压力的调和四次分量及格点几何，
本轮未判定。即使 \(P_{\mathrm h}\ne0\)，一个标量线性泛函也可能为零；
若 \(P_{\mathrm h}=0\)，则 K=0，但 (12) 说明完整二阶轮廓仍可非零。
没有从 K 推出全部四阶压力、几何唯一性或量子对象。

ARS 的有界论证组织用于区分已有计数定理、积分交换、代数投影、
新级数与未来计算责任。新 Fourier 常数和投影均有自含计算；
普通来源浏览仅核对 DLMF Poisson 公式，不重试此前失败的 Sharp
PDF 定位、截图或其他来源通道，不把旧访问失败改成成功。

实际只新增本笔记，并由主线程追加总记录。没有运行数值或符号程序、
科学格点求和、实验、fixture、历史 artifact writer、论文构建或正式审查。
旧笔记、正式稿、冻结输入、协议、回执、失败记录、FAIL / BLOCK、
Route 以及 Stage 5／6 边界保持不变。

[previous]: internal_first_theta_correction_and_log_free_rate_20260908.md
[poisson]: https://dlmf.nist.gov/1.8#E14
