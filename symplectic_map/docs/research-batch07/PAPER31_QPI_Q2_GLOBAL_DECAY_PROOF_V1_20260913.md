# Paper31 Q2：原离散相关的全 Fourier 衰减与奇偶主项 V1

日期标签：2026-09-13。作者：/root。
状态：PROVABLE AS STATED / AUTHOR_PROOF_FROZEN / FRESH_ACTUAL_REVIEW_PENDING；尚未独立数学接受。
使用 proof-writer；本件不作新意／容量／正式准入票，不建项目或试排。
原完整曲面、原映射、全部临界邻域及四条 terminal 保留；无数值、CAS或扫描。

## 1. Claim、假设与记号

固定任意 $T>0$，沿用已接受[M]的原 $U,F,h,\Omega,\mu=|\Omega|,\Pi$，
其中 $\Pi$ 是逐连通圆均值，内积第一槽线性，

$$C_n(f,g)=\langle(f-\Pi f)\circ F^n,g-\Pi g\rangle,
\qquad f,g\in C_c^\infty(U).$$

固定闭有限能窗 $J$ 包含两观测的支撑能量，并可扩大使它包含两临界值及存在的驻点能量。
$K=h^{-1}(J)$ 紧[M]；在稍大紧能窗的有限原光滑坐标图定义 $\|\cdot\|_{C^r}$。
常数允许依赖固定 $T,J,r$ 和所选等价原范数，不要求 $T\to0,1,\infty$ 一致。
下面对 $m\ge1$、$r_0\in\{0,1\}$ 表述 $n=2m+r_0$；$r_0$ 不是正则性阶数。

置 $G=F^2$、$f_{r_0}=f\circ F^{r_0}$。在每条正则圆取正 Hamilton 时间角
$\theta\in\mathbb R/\mathbb Z$，$\eta(X)=1$，$d\mu=L(h)\,dh\,d\theta$。
Fourier 约定为 $\widehat f_{c,k}(h)=\int_0^1f(z_c(h,\theta))e^{-2\pi ik\theta}d\theta$。
改变相位原点会给两因子相反相位，乘积 $\widehat f_k\overline{\widehat g_k}$ 不变。
圆上 $G$ 的相位取

$$\sigma(h)=2\rho_-(h)\ (h<h_-),\qquad
2\rho_0(h)\ (h_-<h<h_+),\qquad
\rho_+(h)\ (h>h_+).\tag{1.1}$$

整数提升不影响离散 Fourier 指数。在持续圆上用[B]的解析相位越过 $h_-$。
令 $\mathcal S_T$ 是所有 $\sigma'=0$ 的持续正则圆，而不是仅正则能级：

- $0<T<3/16$：中区间驻点的一圆；
- $T=3/16$：$h_-=-2$ 的持续一圆；
- $3/16<T<1$：下区间同一驻点能量的两圆；
- $T=1$：空集；
- $T>1$：上区间同一驻点能量的两圆。

这是旧[TW]、[B]的已接受分类，不作为新发现。每个成员的 $\sigma''<0$。
对其能量 $h_c$ 定义绝对收敛的振荡级数

$$\mathcal A_{r_0}(m)=
\sum_{c\in\mathcal S_T}\sum_{k\ne0}
\frac{L(h_c)\widehat {f_{r_0}}_{c,k}(h_c)
\overline{\widehat g_{c,k}(h_c)}}{\sqrt{|k\sigma''(h_c)|}}
e^{2\pi ikm\sigma(h_c)+i\pi\operatorname{sgn}(k\sigma''(h_c))/4}.\tag{1.2}$$

椭圆中心记 $s_-$，$\varepsilon=h_--h$，$\sigma_c=2\theta(T)$，
$\sigma_E(\varepsilon)=2\rho_-(h_--\varepsilon)$。
在[E]的正时间、对称角度规范中定义

$$A_k^{(r_0)}=\left.\partial_\varepsilon
\bigl(L(\varepsilon)\widehat {f_{r_0}}_k(\varepsilon)
\overline{\widehat g_k(\varepsilon)}\bigr)\right|_{\varepsilon=0}.
\tag{1.3}$$

它只可能在 $k=\pm1$ 非零，由两观测原一阶 jet 决定。
当 $T\ne3/16$，置 $\beta=\sigma_E'(0)=-2\rho_-'(h_-)\ne0$，

$$\mathcal B_{r_0}(m)=
-\sum_{k=\pm1}\frac{A_k^{(r_0)}}{(2\pi k\beta)^2}
e^{2\pi ikm\sigma_c}.\tag{1.4}$$

当 $T=3/16$，置 $\gamma=\sigma_E''(0)=2\rho_-''(h_-)<0$，

$$\mathcal D_{r_0}(m)=
\sum_{k=\pm1}\frac{iA_k^{(r_0)}}{2\pi k\gamma}
e^{2\pi ikm\sigma_c}.\tag{1.5}$$

**定理。** 可取有限整数 $R=20$，存在常数 $C$，对原两观测有

$$\begin{array}{ll}
T\notin\{3/16,1\}:&C_{2m+r_0}=m^{-1/2}\mathcal A_{r_0}(m)
+O(C\|f\|_{C^R}\|g\|_{C^R}m^{-3/2}),\\[2mm]
T=3/16:&C_{2m+r_0}=m^{-1/2}\mathcal A_{r_0}(m)
+m^{-1}\mathcal D_{r_0}(m)
+O(C\|f\|_{C^R}\|g\|_{C^R}m^{-3/2}),\\[2mm]
T=1:&C_{2m+r_0}=m^{-2}\mathcal B_{r_0}(m)
+O(C\|f\|_{C^R}\|g\|_{C^R}m^{-3}).
\end{array}\tag{1.6}$$

在平滑能量截断的完整 saddle 邻域，对每个指定整数 $N\ge1$ 可取有限 $R_N=N+2$，
其相关为 $O(C_N\|f\|_{C^{R_N}}\|g\|_{C^{R_N}}m^{-N})$。
全局率是 $T\ne1$ 时 $O(|n|^{-1/2})$、$T=1$ 时 $O(|n|^{-2})$；
每个固定参数均存在原光滑紧支撑观测，使相应归一化绝对相关的 limsup 严格为正。
不声称每对观测或每个整数时刻都有同号下界，也不声称原系统不投影便混合。

## 2. Status、策略及依赖图

Status：PROVABLE AS STATED。主控已FULL读回[K]终态292行、[E]终态377行，
以下实际消费其完整作者证明；原完整观测类没有削弱。
第3—5节另给求和／积分机制，第6—8节完成原曲面拼合及最优性。
三件仍须fresh非作者actual数学审查，不能把作者协作互查当成正式独立票。

1. [M]供应原测度、proper紧性、逐圆投影与原 $F$ 对易、terminal范数接口。
2. [N]供应真实 $L=m_c\mathcal A(e)\log(1/|e|)+\mathcal B(e)$、原 $F^2$ 的解析有界时间 $\tau(e)$。
3. [K]供应原观测的全部混合能量／角度估计和 $q=1/(\tau/L)'$ 的可微符号。
4. 第4节用符号代数、边界检查和绝对求和关闭完整 saddle 积分，不用 $\delta(n)$ 薄层猜测。
5. [TW]、[B]供应全部驻点和椭圆端相位jet；第5节直接证明需要的二次驻相及非驻相估计。
6. [E]供应原光滑椭圆jet及全部Fourier的端点展开；第6节用它和第4—5节拼合完整曲面。
7. 第7—8节还原原单步的换圆奇偶，并用实际原光滑观测证明最优性。

## 3. 原 Fourier 表示和可交换次序

由 $\Pi\mathsf U=\mathsf U\Pi$，有准确等式

$$C_{2m+r_0}(f,g)=C_{2m}(f_{r_0},g).
\tag{3.1}$$

$F$ 保能量且是光滑自同构，所以 $f_{r_0}\in C_c^\infty(U)$；
固定紧能窗上链式法则给 $\|f_{r_0}\|_{C^a}\le C_a\|f\|_{C^a}$。
不在此对有非Hölder损失的 $(I-\Pi)f$ 求原高阶导数。
逐圆 Parseval 得

$$C_{2m+r_0}(f,g)=\sum_c\sum_{k\ne0}
\int_{I_c}L(h)\widehat {f_{r_0}}_{c,k}(h)
\overline{\widehat g_{c,k}(h)}e^{2\pi ikm\sigma_c(h)}\,dh.
\tag{3.2}$$

这里 $I_c$ 先是三个正则区间中的圆族；$\mu$-零的临界纤维不改变积分。
此式不是形式Fourier展开：逐层Cauchy–Schwarz及Parseval给

$$\sum_{k\ne0}L|\widehat {f_{r_0}}_k\overline{\widehat g_k}|
\le
\left(\int_{C_h}|f_{r_0}-\Pi f_{r_0}|^2dt\right)^{1/2}
\left(\int_{C_h}|g-\Pi g|^2dt\right)^{1/2}.$$

再对 $h,c$ 作Cauchy–Schwarz，上界为两中心化函数的有限 $L^2(\mu)$ 范数之积。
Tonelli和Fubini因此允许全 $k$ 与能量积分交换，且不要求一致有界的角向Sobolev范数。
后续每个导数／渐近余项还需下面独立的可求和界，不能由此一次交换自动取得。

## 4. Saddle：完整符号代数、边界消失及任意有限幂率

固定 $e=h-h_+$ 的一侧及一条完整圆，令 $\ell=1+|\log|e||$。
[K, C2—C3]已给的作者证明输入是：对任意非负整数 $a,s$，

$$|\partial_e^a\widehat f_k(e)|
\le C_{a,s}\|f\|_{C^{a+s}}|e|^{-a}\ell^{M_{a,s}}|k|^{-s},\qquad k\ne0,
\tag{4.1}$$

以及对 $q(e)=1/\alpha'(e)$、$\alpha=\tau/L$，

$$|\partial_e^a q(e)|\le C_a|e|^{1-a}\ell^{M_a}.\tag{4.2}$$

在下侧 $\sigma=1+\alpha$，上侧 $\sigma=\alpha$，所以导数相同、离散指数也相同。
对各侧选 $\chi(e)$，在0邻域等于1、在外端之前光滑变成0，
置 $a_k(e)=\chi(e)L(e)\widehat {f_{r_0}}_k(e)\overline{\widehat g_k(e)}$。
周期的解析对数表达及Leibniz公式给任意有限 $j,s$

$$|\partial_e^j a_k(e)|
\le C_{j,s}\|f\|_{C^{j+s}}\|g\|_{C^{j+s}}
|e|^{-j}\ell^{M_{j,s}}|k|^{-2s}.
\tag{4.3}$$

定义不含 $m,k$ 的转置算子 $\mathcal T a=-\partial_e(qa)$。
若一族函数满足(4.3)，则对任意 $j$

$$\partial_e^j\mathcal T a
=-\sum_{v=0}^{j+1}{j+1\choose v}
(\partial_e^v q)(\partial_e^{j+1-v}a).$$

每项的幂为 $|e|^{1-v}|e|^{-(j+1-v)}=|e|^{-j}$。
因此 $\mathcal T$ 保持这种“每次能量微分仅损失一个 $e^{-1}$”的符号类，
只增加有限对数幂与所需原导数阶。归纳给 $\mathcal T^N a_k=O(|k|^{-2s}\ell^{M_N})$。
特别 $\mathcal T^N a_k$ 可积，而在节点端

$$q\mathcal T^j a_k=O(|k|^{-2s}|e|\ell^{M_j})\longrightarrow0.
\tag{4.4}$$

在外端它及所有所需导数因 $\chi$ 为零而消失。先在截断闭区间作分部积分，再令节点截断趋0，
(4.4)消去每一个边界项，(4.3)的可积主控允许传极限。因此准确有

$$\int a_k(e)e^{2\pi ikm\alpha(e)}de
=(2\pi ikm)^{-N}\int\mathcal T^N a_k(e)e^{2\pi ikm\alpha(e)}de.
\tag{4.5}$$

下侧按递增 $e$ 积分时只有端点顺序变化，边界仍各自为零；同一个公式成立。
取 $s=1$ 即得可对全部 $k\ne0$ 求和的界

$$\sum_{k\ne0}\left|\int a_ke^{2\pi ikm\alpha}de\right|
\le C_N\|f\|_{C^{R_N}}\|g\|_{C^{R_N}}m^{-N}
\sum_{k\ne0}|k|^{-N-2}\int_0^\delta\ell^{M_N}de.
\tag{4.6}$$

最后积分有限。上侧两圆、下侧一圆的有限求和完成全 saddle 邻域。
这里不声称 $\mathcal T^j a$ 自身趋零：它可以仅被对数幂控制；真正趋零的是边界中的 $q\mathcal T^j a$。
不曾把原离散位移换成一个全局常数时间流，也没有删除随 $m$ 缩小的节点能带。

## 5. 正则圆族的驻相和非驻相：有余项的直接证明

在避开临界点的紧圆管内，原 $C^a$ 与能量—角度有限阶范数等价[M]。
对 $s$ 次角向分部积分，再作 $j$ 次能量微分，给
$|\partial_h^j\widehat f_k|\le C_{j,s}\|f\|_{C^{j+s}}|k|^{-s}$。
所有常数在固定紧圆管上一致，包括跨 $h_-$ 的持续圆。

先证明标量驻相式。令 $a\in C_c^4(I)$，$\sigma$ 在 $I$ 光滑，只有一个
$\sigma'(h_*)=0$、$\sigma''(h_*)\ne0$，且支撑足够靠近 $h_*$。
一维Morse变换
$y=\operatorname{sgn}(h-h_*)\sqrt{2|\sigma(h)-\sigma(h_*)|}$
是光滑微分同胚，$\sigma=\sigma(h_*)+s_*y^2/2$，$s_*=\operatorname{sgn}\sigma''(h_*)$，
其正Jacobian在0为 $|\sigma''(h_*)|^{-1/2}$。
令 $b(y)=a(h(y))h'(y)$，按 $e^{-2\pi i\xi y}$ 约定取Fourier变换。
高斯积分及Fourier反演给，对实 $v\ne0$

$$\int b(y)e^{i\pi vy^2}dy
=|v|^{-1/2}e^{i\pi\operatorname{sgn}(v)/4}
\int\widehat b(\xi)e^{-i\pi\xi^2/v}d\xi.
\tag{5.1}$$

可先乘 $e^{-\epsilon y^2}$ 使用绝对收敛高斯积分，随后令 $\epsilon\downarrow0$；
Fourier侧核的模一致有界，$\widehat b\in L^1$，故支配收敛合法。
四次分部积分和紧支撑给
$\int \xi^2|\widehat b(\xi)|d\xi\le C\|b\|_{C^4}$。
在(5.1)用 $|e^{-i\pi\xi^2/v}-1|\le\pi\xi^2/|v|$，再令 $v=mks_*$，得到

$$\int a(h)e^{2\pi ikm\sigma(h)}dh
=\frac{a(h_*)e^{2\pi ikm\sigma(h_*)+i\pi\operatorname{sgn}(k\sigma''(h_*))/4}}
{\sqrt{m|k\sigma''(h_*)|}}
+O(C\|a\|_{C^4}(m|k|)^{-3/2}).\tag{5.2}$$

振幅取能量平滑截断乘 $L\widehat {f_{r_0}}_k\overline{\widehat g_k}$，
四阶能量范数具有任意指定的 $k$ 快衰减，故主项和全部余项绝对求和。
这给(1.2)和 $O(m^{-3/2})$，不是只对固定模态的结论。
在其余紧正则圆管，$|\sigma'|$ 有正下界。
用 $q=1/\sigma'$ 和第4节的分部积分恒等式，所有有限导数有界、支撑边界为零，
得到任意指定 $O(m^{-N})$ 的全Fourier估计。
所需的有限原导数阶可按“能量微分阶＋角向分部积分阶”取足，不宣称最小阶。

## 6. 椭圆端点和完整曲面的拼合

[E, §§4—6]给出一个正时间角规范，在带符号半径 $r=\sqrt{2\varepsilon}$ 上满足
$z(-r,\theta)=z(r,\theta+1/2)$，从而 $\widehat f_k(-r)=(-1)^k\widehat f_k(r)$。
两因子同 $k$ 的乘积是偶函数，在 $\varepsilon$ 光滑；对每个 $k\ne0$

$$L\widehat {f_{r_0}}_k\overline{\widehat g_k}
=\varepsilon A_k^{(r_0)}+\varepsilon^2R_k(\varepsilon),\tag{6.1}$$

余项任意所需有限 $\varepsilon$ 导数具有可求和的 $k$ 快衰减，并受有限原范数控制。
[E, §§7—8]据此给实际平滑局部截断积分

$$C^{E}_{2m+r_0}=
\begin{cases}
m^{-2}\mathcal B_{r_0}(m)+O(m^{-3}),&T\ne3/16,\\
m^{-1}\mathcal D_{r_0}(m)+O(m^{-3/2}),&T=3/16.
\end{cases}\tag{6.2}$$

这里 $\beta,\gamma$ 是 $G=F^2$ 的相位导数，所以系数不得漏掉因子2。
收缩圆在 $T=3/16$ 的项是 $m^{-1}$，并非持续圆的 $m^{-1/2}$。

选择有限不变分割如下。先在 $h_+$ 取平滑能量截断，覆盖每条退化完整圆；
在 $h_-$，孤立临界点的小盘与持续紧圆有不相交邻域。
在充分窄能带，两种圆族分离，分别取能量截断；每个截断在自己的整个圆上常值。
小盘截断在中心附近为1，故延到中心为光滑；持续圆截断跨 $h_-$ 为光滑。
两者在正则侧之和恰为该能带的能量截断。
再把其余紧正则能区分成驻点圆管和有限非驻点圆管，取光滑能量单位分解。
这些权重在积分中只乘一次，不将任意非不变空间切片错误地当独立旋转圆。
上侧两圆在 $F$ 下交换，但均被 $G$ 保持；分解分析的是准确(3.1)，无需每个局部权重都被 $F$ 保持。

在 $T=3/16$，持续圆的驻点圆管跨整个 $h_-=-2$，只应用一次双侧(5.2)，
不能拆成两个带人为端点的半管并遗失或重复主项。
在其他参数，持续圆跨 $h_-$ 非驻相。
空间无穷远没有新端点：两观测能量支撑饱和后仍紧；四条terminal在这些圆管内完全正则[M]。
将第4—5节及(6.2)相加，取 saddle／非驻相部分的 $N\ge3$，便得(1.6)。
对 $T\notin\{3/16,1\}$，椭圆 $m^{-2}$ 项被 $m^{-3/2}$ 余项吸收，未伪称其不存在。
在 $T=1$ 没有任何有限驻点圆，椭圆项成为全局主项。

## 7. 原单步的全部奇偶系数

下／中区间以及 $h_-$ 持续圆，$Fz_c(h,\theta)=z_c(h,\theta+\rho(h))$。
故准确有

$$\widehat {f_{r_0}}_{c,k}=e^{2\pi ikr_0\rho(h)}\widehat f_{c,k}.
\tag{7.1}$$

椭圆端取一阶jet极限，(1.3)给
$A_k^{(r_0)}=e^{2\pi ikr_0\theta(T)}A_k^{(0)}$。
这是原 $DF(s_-)$ 对一阶模的作用；不是在奇数时刻使用另一套系统。

上区间在所需能窗选第一条圆参数 $z_0(h,\theta)$，并定义 $z_1=Fz_0$。
因 $F_*X=X$，第二条圆仍为相同正时间角且周期相同。
原映射准确满足

$$Fz_0(h,\theta)=z_1(h,\theta),\qquad
Fz_1(h,\theta)=z_0(h,\theta+\sigma(h)).\tag{7.2}$$

所以把上区间两圆相同相位合在一起时，偶数振幅为
$L(\widehat f_{0,k}\overline{\widehat g_{0,k}}+
\widehat f_{1,k}\overline{\widehat g_{1,k}})$，奇数振幅为

$$L\bigl(\widehat f_{1,k}\overline{\widehat g_{0,k}}
+e^{2\pi ik\sigma(h)}\widehat f_{0,k}\overline{\widehat g_{1,k}}\bigr).
\tag{7.3}$$

将它们在驻点处代入(1.2)便得到完全显式的奇偶主项。
特别仅在一条上圆支撑的观测可以使奇数相关恒零而偶数相关不为零；因此不能要求所有 $n$ 的一致正下界。
负时刻由不变测度及酉性给 $C_{-n}(f,g)=\overline{C_n(g,f)}$，从正时刻结论得到相应率。

## 8. 最优性：合法原观测和非零 limsup

先设 $T\ne1$。取任一 $c\in\mathcal S_T$ 的紧正则圆管，其中也允许
$T=3/16$ 时的持续圆管（它离椭圆点有正距离）。
在此取实能量bump $\chi$，$\chi(h_c)=1$，并令
$f=g=\chi(h)e^{2\pi i\theta}$，在圆管外置零。
圆管平凡化光滑，能量bump在其边界附近为零，所以这是真正的 $C_c^\infty(U)$，
跨terminal也由原正则平凡化保证光滑，不是临界点不兼容的单角函数。
当驻点能量有两圆时，只在一条圆支撑；两圆在该管中分离。
它只有 $k=1$ 的Fourier模，且逐圆均值零。在偶数时刻(1.6)化为

$$C_{2m}(f,f)=
\frac{L(h_c)}{\sqrt{m|\sigma''(h_c)|}}
e^{2\pi im\sigma(h_c)-i\pi/4}+O(m^{-3/2}).\tag{8.1}$$

故 $\lim_{m\to\infty}m^{1/2}|C_{2m}(f,f)|=L(h_c)/\sqrt{|\sigma''(h_c)|}>0$。
若只允许实观测，可取该函数实部；主项为非零常数乘
$\cos(2\pi m\sigma(h_c)-\pi/4)$。
该序列不可能趋零：若趋零，$e^{4\pi im\sigma(h_c)}\to-i$，
相邻商常数迫使 $e^{4\pi i\sigma(h_c)}=1$，继而左侧恒1，矛盾。
所以实观测也有严格正的归一化 limsup。

再设 $T=1$。在[E]定向Morse坐标取原光滑复函数
$f=g=\chi(\varepsilon)(p+iq)$，$\chi$ 在中心附近为1并紧支撑于椭圆小盘。
其一阶时间角模只有 $k=1$，所以 $A_1^{(0)}>0$、$A_{-1}^{(0)}=0$；
该断言由原线性jet证明，不任意指定中心附近的单角函数。
(1.4)、(1.6)给

$$C_{2m}(f,f)=
-\frac{A_1^{(0)}}{(2\pi\beta)^2m^2}e^{2\pi im\sigma_c}+O(m^{-3}).\tag{8.2}$$

归一化模趋正。实线性坐标 $p$ 给两个共轭且相同非零系数，主项为非零常数乘
$m^{-2}\cos(2\pi m\sigma_c)$；若余弦趋零则平方指数趋 $-1$，相邻商论证再次矛盾。
因此实原光滑类也不能统一改善 $n^{-2}$。

对一般复观测，在 $T=1$ 只要 $A_1^{(0)},A_{-1}^{(0)}$ 不同时为零，
主项作为整数序列就有正limsup：$\sigma_c\in(1,4/3)$，故
$e^{2\pi i\sigma_c}\ne e^{-2\pi i\sigma_c}$。
有限两个不同单位频率的平方模Cesàro平均为两系数模平方之和，严格正。
两系数是有限jet的非恒零双线性／共轭双线性表达，它们同时为零是一个真闭代数条件。
因而这里“泛型”可准确理解为一阶jet对中开稠密的非消失集合；不是对每对函数的声明。
若一阶jet消失则主项消失，(1.6)至少给更快的 $O(m^{-3})$；本件不另宣称全部高阶jet的最优分类。

## 9. 尚待核对的风险与非数学边界

主控已FULL读回[K]、[E]，核其有限原范数、接缝与端点系数；现在仍须fresh实际独查，不先授数学接受。
第4节只依赖所列明确符号，不把薄能带尖锐性当时间下界。
第5节给直接驻相证明；第8节的下界不借目标零点、共振扫描或数值实验。
全局主项是能量系综的相混合，不是单圆轨道混合、CLT、均匀遍历速度或全局常数时间嵌入。
既有FHR等的跨separatrix技术压力保留[S]；本件实际完成与否都不自行改变新意7.6／价值8.2／容量MID的旧条件预核。
两位fresh非作者完整四门、22–30页真实内生容量及最终稿件／PDF验收仍是独立后续义务。
旧twist新意双FAIL及全部历史FAIL保留，批次仍4/5。

[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[K]: PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[S]: PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md
