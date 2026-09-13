# Paper31 Q2：消失椭圆圆的原光滑 jets、全 Fourier 与端点主项 V1

日期标签：2026-09-13。作者：/root/p31_q2_elliptic_jet_proof。
状态：PROVABLE AS STATED / AUTHOR_PROOF_FROZEN / FRESH_ACTUAL_REVIEW_PENDING。
route_applicability: NOT_APPLICABLE。本件不是新意票、容量票或正式准入。
按 proof-writer 保存精确命题、依赖、证明与边界；只纸面推导，无 CAS、数值、枚举或试排。
端点积分的符号及有限导数余项经只读协作 endpoint_integral_sign_check 单独核算；
这是作者证明协作，不冒称对本整件的 fresh 独立数学审查。

## 1. Claim：精确局部结论

固定任意 $T>0$，沿用 [M] 的完整原曲面 $U$、原映射 $F$、能量 $h$、
辛面积 $\mu=|\Omega|$、逐连通圆投影 $\Pi$，不改变原光滑观测类 $C_c^\infty(U)$。
令 $s=s_{w_-}$ 为非退化椭圆中心，$\varepsilon=h_--h$，
$\Gamma_\varepsilon$ 为在 $\varepsilon\downarrow0$ 消失的那条完整圆。
另一条跨 $h_-$ 持续的正则圆不属于本件的局部积分域。
固定充分小的 $\varepsilon_0>0$，使这些小圆全部位于同一 Morse 邻域；
取固定 $\chi\in C_c^\infty([0,\varepsilon_0))$，在 $0$ 的邻域等于 $1$。
这里表示在闭半轴光滑、在右端之前恒零；允许在 $0$ 非零。

令 $G=F^2$，并取原正 Hamilton 时间方向的提升

$$\sigma(\varepsilon)=2\rho_-(h_--\varepsilon),\qquad
\rho_*=\theta(T),\qquad \sigma_0=2\rho_*.$$

对原光滑 $f,g$，定义消失圆局部偶步相关

$$\mathcal E_m(f,g)=\int_0^{\varepsilon_0}\chi(\varepsilon)
\int_{\Gamma_\varepsilon}[(I-\Pi)f](G^mz)
\overline{[(I-\Pi)g](z)}\,dt\,d\varepsilon,\qquad m\ge1.$$

存在与 $f,g$ 无关的 Hamilton 时间角，使全部非零 Fourier 模满足

$$a_k(\varepsilon):=L(\varepsilon)\widehat f_k(\varepsilon)
\overline{\widehat g_k(\varepsilon)}
=\varepsilon A_k+\varepsilon^2R_k(\varepsilon),\qquad k\ne0,\tag{1.1}$$

其中 $A_k=0$ 除非 $k=\pm1$，$R_k$ 在闭区间光滑。对任意整数 $J,S\ge0$，
存在只依赖固定 $T$、固定坐标邻域、$J,S$ 的常数 $C_{J,S}$，使

$$\sup_{k\ne0}(1+|k|)^S\|R_k\|_{C^J([0,\varepsilon_0])}
\le C_{J,S}\|f\|_{C^{2J+4+S}(K)}\|g\|_{C^{2J+4+S}(K)}.\tag{1.2}$$

$K$ 是固定且稍大的紧 Morse 邻域；范数是该原光滑图的普通有限阶范数，
亦可用固定原曲面图册在 $K$ 上的等价范数替代。

若 $T\ne3/16$，记 $\beta=\sigma'(0)\ne0$，缩小 $\varepsilon_0$ 使
$\sigma'$ 在 $\chi$ 的整个支集无零点，则

$$\boxed{\mathcal E_m(f,g)=
-\frac1{m^2}\sum_{k=\pm1}
\frac{A_k e^{2\pi i km\sigma_0}}{(2\pi k\beta)^2}
+O\!\left(m^{-3}\|f\|_{C^{20}(K)}\|g\|_{C^{20}(K)}\right).}\tag{1.3}$$

若 $T=3/16$，记 $\gamma=\sigma''(0)<0$，缩小 $\varepsilon_0$ 使
$\sigma'(\varepsilon)<0$ 对 $0<\varepsilon\le\varepsilon_0$ 成立，则

$$\boxed{\mathcal E_m(f,g)=
\frac1m\sum_{k=\pm1}
\frac{iA_k e^{2\pi i km\sigma_0}}{2\pi k\gamma}
+O\!\left(m^{-3/2}\|f\|_{C^{20}(K)}\|g\|_{C^{20}(K)}\right).}\tag{1.4}$$

常数可依赖固定 $T,K,\chi$，不要求对 $T\to0,1,\infty$ 一致；
这里 $C^{20}$ 是安全的有限阶上界，不宣称最小正则性。
主项和余项均已对全部 $k$ 求和，不是有限模替代。
对原步数 $n=2m+r$，$r\in\{0,1\}$，把 $f$ 换为 $f\circ F^r$ 即得同一结论，且

$$A_k(f\circ F^r,g)=e^{2\pi i kr\rho_*}A_k(f,g).\tag{1.5}$$

特别在 $T=1$，存在原 $C_c^\infty(U)$ 观测，仅支撑于这些消失圆及中心，
使 $\limsup_{n\to\infty}n^2|C_n(f,g)|>0$；证明使用原一阶 jet，而非任意指定单角模式。

## 2. Status、假设与符号

Status：PROVABLE AS STATED。上述局部命题保留原完整圆、原测度和原光滑观测，不需要削弱。
它没有把原 Q2 全局强定理冒称为已完成；全局 saddle、持续圆驻相及分区合成由主控另证。

消费已接受的 [D] 对 [M]、[N] 的数学处置，以及 [TW]、[B] 的既定旋转结论：

1. $\iota_X\Omega=-dh$，正时间形式 $\eta$ 满足 $\eta(X)=1$；
   $d\mu=L\,d\varepsilon\,d\theta$，$L>0$。
2. $h$ 在 $s$ 为解析非退化极大；$\omega_-=|w_-|\sqrt{3-4w_-}>0$，
   $L(0)=L_0=2\pi/\omega_-$。
3. 下外两圆上的原 $F$ 旋转数相同；$\rho_-$ 经持续圆延至 $h_-$ 实解析。
   $\rho_*=1/2+\pi^{-1}\arctan(1/\sqrt{3-4w_-})$。
4. $\rho_-'(h_-)$ 仅在 $T=3/16$ 为零，在该参数 $\rho_-''(h_-)<0$。
   因此 $\beta=-2\rho_-'(h_-)$，$\gamma=2\rho_-''(h_-)<0$。

这里 $\widehat f_k=\int_0^1f(z_\varepsilon(\theta))e^{-2\pi ik\theta}\,d\theta$；
相关内积在第一槽线性，故振幅为 $L\widehat f_k\overline{\widehat g_k}$。
中心化恰删除 $k=0$，不会改变任何非零模，也不假设 $f-\Pi f$ 在原图仍光滑。

## 3. Proof strategy 与依赖

策略是用解析 Morse 图和一个保留半径反号对称性的时间角，把原光滑 jets 转为全 Fourier 振幅，
随后分别作一次非驻点坐标替换或二次相位坐标替换。

依赖顺序如下：

1. 解析 Morse 引理与面积方向给圆柱参数化；零均值周期原函数使其满足半径反号／半周平移恒等式。
2. Fourier 乘积对半径为偶函数；偶函数除法与 Taylor 积分余项给真实 $\varepsilon$ 光滑性及有限阶范数。
3. $\rho_-$ 的既定解析延拓及 [B] 的非退化结论决定两类端点相位。
4. 紧支积分的显式分部积分给准确系数；逐模有权范数使原级数和余项绝对可求和。
5. 原图中线性复坐标乘径向 bump 给非零 jet；原 $F$ 的旋转作用给奇偶接口。

不调用全局解析作用角定理，也不假定原光滑函数可以任意指定圆上的单个模式。

## 4. Proof，步骤 1：选对方向的解析时间角

由解析 Morse 引理，存在实解析图 $z=\mathcal K(p,q)$，$\mathcal K(0,0)=s$，使

$$h\circ\mathcal K=h_--\frac{p^2+q^2}{2}.$$

若需要，反射 $q$ 而不改变能量式，从而确保

$$\mathcal K^*\Omega=-b(p,q)\,dp\wedge dq,\qquad b>0\ \text{实解析},\qquad b(0,0)=\omega_-^{-1}.$$

令 $p=r\cos\varphi,q=r\sin\varphi$。此时
$\Omega=-br\,dr\wedge d\varphi$，而 $-dh=r\,dr$，故
$X=b^{-1}\partial_\varphi$；正 Hamilton 时间就是 $dt=b\,d\varphi$。
此反射选择至关重要：若取 $+b\,dp\wedge dq$，正时间方向会相反。

令 $r_0=\sqrt{2\varepsilon_0}$，允许暂时令 $r\in[-r_0,r_0]$ 取正负值；
这是证明装置，不增加物理圆。
写

$$b_r(\varphi)=b(r\cos\varphi,r\sin\varphi),\qquad
\bar b(r)=\frac1{2\pi}\int_0^{2\pi}b_r(\varphi)\,d\varphi,\qquad L(r)=2\pi\bar b(r).$$

令 $B_r$ 为 $b_r-\bar b(r)$ 的唯一零均值周期原函数，即
$\partial_\varphi B_r=b_r-\bar b(r)$、$\int_0^{2\pi}B_r\,d\varphi=0$。
它关于 $(r,\varphi)$ 实解析：将 $b$ 的局部收敛幂级数代入后，每个齐次项是有限三角多项式，
扣去均值并积分其非零整数频率不破坏在更小圆柱上的正常收敛及每个有限阶导数。

定义角的提升

$$\Psi_r(\varphi)=\varphi+\frac{B_r(\varphi)}{\bar b(r)},\qquad
\theta=\frac{\Psi_r(\varphi)}{2\pi}.$$

有 $\partial_\varphi\Psi_r=b_r/\bar b(r)>0$，且
$\Psi_r(\varphi+2\pi)=\Psi_r(\varphi)+2\pi$。
解析隐函数定理加紧角区间的有限覆盖给实解析逆提升 $\varphi_r(\psi)$。
于是

$$z(r,\theta)=\mathcal K\big(r\cos\varphi_r(2\pi\theta),
r\sin\varphi_r(2\pi\theta)\big)\tag{4.1}$$

在包括 $r=0$ 的圆柱上实解析、关于 $\theta$ 周期，且
$dt=L(r)d\theta$、$d\mu=L(\varepsilon)d\varepsilon d\theta$，其中 $r=\sqrt{2\varepsilon}$。
在 $r=0$ 有 $B_0=0$，因此

$$z(0,\theta)=s,\qquad
\partial_r z(0,\theta)=D\mathcal K_0(\cos2\pi\theta,\sin2\pi\theta).\tag{4.2}$$

## 5. 步骤 2：半径反号对称性与有限原范数

有 $b_{-r}(\varphi)=b_r(\varphi+\pi)$，所以 $\bar b(-r)=\bar b(r)$。
零均值周期原函数的唯一性进一步给 $B_{-r}(\varphi)=B_r(\varphi+\pi)$。
因此

$$\Psi_{-r}(\varphi)=\Psi_r(\varphi+\pi)-\pi,\qquad
\varphi_{-r}(\psi)=\varphi_r(\psi+\pi)-\pi,$$

进而得到精确恒等式

$$\boxed{z(-r,\theta)=z(r,\theta+1/2).}\tag{5.1}$$

写 $F_f(r,\theta)=f(z(r,\theta))$，并暂以 $r$ 为参数定义 $f_k(r)$。
由(5.1)及 Fourier 定义，

$$f_k(-r)=(-1)^k f_k(r),\qquad f_k(0)=0\quad(k\ne0).\tag{5.2}$$

对整数 $u,v\ge0$，复合函数的有限阶链式法则给
$\|\partial_r^u\partial_\theta^vF_f\|_\infty
\le C_{u,v}\|f\|_{C^{u+v}(K)}$。
将 $v=S$ 阶角导数在周期角上分部积分，对 $k\ne0$ 得

$$\|f_k\|_{C^u([-r_0,r_0])}
\le C_{u,S}(1+|k|)^{-S}\|f\|_{C^{u+S}(K)}.\tag{5.3}$$

$S=0$ 直接来自积分估计。全部导数在一个固定圆柱上估计，常数不依赖 $k$。
周期 $L(r)$ 是正的偶解析函数。因此

$$\widetilde a_k(r):=L(r)f_k(r)\overline{g_k(r)}$$

是偶光滑函数，且在 $r=0$ 至少二阶消失；其每个固定径向导数仍满足任意指定的 $k$ 负幂界。

下面记录所用偶函数事实及范数。若 $v$ 是偶 $C^{2J}$ 函数，则
$V(\varepsilon)=v(\sqrt{2\varepsilon})$ 在闭半轴为 $C^J$，其范数受 $\|v\|_{C^{2J}}$ 控制。
证明从

$$\frac1r\partial_r v(r)=\int_0^1v''(tr)\,dt$$

开始，连续 $J$ 次应用 $r^{-1}\partial_r$。
各次被积函数的奇阶导数在零点为零，故再次使用同一个积分恒等式，得到由 $v^{(2j)}$
组成、带有界非负权重的多重积分，$0\le j\le J$。
这些表达式在 $r=0$ 连续；因为 $\partial_\varepsilon=r^{-1}\partial_r$，结论及范数随之成立。

令 $d_{f,k}=\partial_rf_k(0)$、$d_{g,k}=\partial_rg_k(0)$。
对 $\widetilde a_k$ 减去二阶 Taylor 项后，奇次 Taylor 系数均为零，四阶 Taylor 积分余项给

$$\widetilde a_k(r)=r^2L_0d_{f,k}\overline{d_{g,k}}+r^4q_k(r),\tag{5.4}$$

其中 $q_k$ 是偶光滑函数。
$\|q_k\|_{C^{2J}}$ 受 $\|\widetilde a_k\|_{C^{2J+4}}$ 控制，
例如除法可直接用四阶 Taylor 积分公式在 $r=0$ 延拓；除后函数在 $r\ne0$ 为偶，连续延拓保留偶性。
将上一段偶函数事实用于 $q_k$，并用(5.3)与有限乘积法则，即得(1.1)–(1.2)，
其中

$$A_k=2L_0d_{f,k}\overline{d_{g,k}},\qquad
R_k(\varepsilon)=4q_k(\sqrt{2\varepsilon}).\tag{5.5}$$

## 6. 步骤 3：原一阶 jet 的准确系数

写原函数在 Morse 图的一阶部分为

$$f\circ\mathcal K(p,q)=f(s)+a_fp+b_fq+O(p^2+q^2),$$

$a_f,b_f$ 允许为复数。由(4.2)，

$$d_{f,1}=\frac{a_f-ib_f}{2},\qquad
d_{f,-1}=\frac{a_f+ib_f}{2},\qquad d_{f,k}=0\quad(|k|\ne1).\tag{6.1}$$

所以

$$A_1=\frac{L_0}{2}(a_f-ib_f)(\overline{a_g}+i\overline{b_g}),\qquad
A_{-1}=\frac{L_0}{2}(a_f+ib_f)(\overline{a_g}-i\overline{b_g}).\tag{6.2}$$

这说明主项只由原一阶 jets 决定，却不意味着完整观测只有两个模式。
所有高模与低模的高阶余项都保留在 $R_k$ 中。

## 7. 步骤 4：完整 Fourier 表达与无驻点端点

对每个 $\varepsilon>0$，$F$ 在 Hamilton 时间角中为
$\theta\mapsto\theta+\rho_-(h_--\varepsilon)$。
因为它保持 $h$、$\Omega$，与 $X$ 对易，位移在同圆上为常量；其提升就是已接受的同方向 $\rho_-$。
圆上 Fourier 正交及逐圆中心化于是给

$$\mathcal E_m(f,g)=\sum_{k\ne0}\int_0^{\varepsilon_0}
\chi(\varepsilon)a_k(\varepsilon)e^{2\pi ikm\sigma(\varepsilon)}\,d\varepsilon.\tag{7.1}$$

(1.1)–(1.2)在 $J=0,S=2$ 时给一个可积的绝对求和上界，故 Fubini 合法；
这也直接证明完整原 Fourier 级数的使用没有截断残差。

设 $\beta\ne0$，记 $s_\beta=\operatorname{sgn}\beta$，以
$x=s_\beta(\sigma(\varepsilon)-\sigma_0)$ 换元，逆映射记 $\varepsilon=E(x)$。
所选支集上此坐标严格递增，$E(0)=0$、$E'(0)=|\beta|^{-1}$。
换元振幅

$$b_k(x)=\chi(E(x))a_k(E(x))E'(x)$$

紧支且光滑，$b_k(0)=0$、$b_k'(0)=A_k/\beta^2$。
对实数 $\omega\ne0$，三次普通分部积分给

$$\int_0^\infty b_k(x)e^{i\omega x}\,dx
=-\frac{b_k'(0)}{\omega^2}+E_k(\omega),\qquad
|E_k(\omega)|\le\frac{|b_k''(0)|+\|b_k'''\|_{L^1}}{|\omega|^3}.\tag{7.2}$$

边界仅来自 $x=0$；右端振幅及其导数恒零。
固定解析换元及固定 $\chi$ 的有限链式法则给

$$|b_k''(0)|+\|b_k'''\|_{L^1}
\le C\bigl(|A_k|+\|R_k\|_{C^3}\bigr).$$

令 $\omega=2\pi km s_\beta$，乘回 $e^{2\pi ikm\sigma_0}$ 并逐模求和。
(1.2)的 $J=3,S=2$ 已足够使余项和有界；其原范数阶为 $12$，从而更保守的 $C^{20}$ 足够。
这证明(1.3)，且 $\beta$ 的符号不改变主项前的负号。

## 8. 步骤 5：二次端点与 $m^{-1}$ 次层

当 $T=3/16$，由既定 $\gamma<0$，令

$$x=\sqrt{\frac{2(\sigma(\varepsilon)-\sigma_0)}{\gamma}}.$$

在 $\varepsilon=0$ 取正向延拓：解析展开使 $x=\varepsilon(1+O(\varepsilon))$，
缩小邻域后是解析递增坐标，逆函数 $\varepsilon=E(x)$ 满足 $E'(0)=1$。
相位恰为 $\sigma_0+\gamma x^2/2$。写换元振幅为

$$b_k(x)=\chi(E(x))a_k(E(x))E'(x)=x c_k(x).$$

$c_k$ 光滑紧支，$c_k(0)=A_k$，且

$$\|c_k'\|_\infty+\|c_k''\|_{L^1}
\le C\bigl(|A_k|+\|R_k\|_{C^2}\bigr).\tag{8.1}$$

令 $\omega=2\pi km\gamma$。使用紧支振幅，直接分部积分得到

$$\int_0^\infty x c_k(x)e^{i\omega x^2/2}\,dx
=\frac{iA_k}{\omega}-\frac1{i\omega}\int_0^\infty c_k'(x)e^{i\omega x^2/2}\,dx.\tag{8.2}$$

为了控制后一积分，若 $d$ 是紧支 $C^1$ 函数，置 $\delta=|\omega|^{-1/2}$。
$[0,\delta]$ 上积分至多 $\delta\|d\|_\infty$；
$[\delta,\infty)$ 上利用 $\partial_x e^{i\omega x^2/2}=i\omega x e^{i\omega x^2/2}$ 分部积分，
其边界与导数项至多

$$\frac{\|d\|_\infty}{|\omega|\delta}
+\frac1{|\omega|}\int_\delta^\infty
\left(\frac{|d'|}{x}+\frac{|d|}{x^2}\right)dx
\le |\omega|^{-1/2}\bigl(2\|d\|_\infty+\|d'\|_{L^1}\bigr).$$

因此

$$\left|\int_0^\infty d(x)e^{i\omega x^2/2}\,dx\right|
\le |\omega|^{-1/2}\bigl(3\|d\|_\infty+\|d'\|_{L^1}\bigr).\tag{8.3}$$

将 $d=c_k'$ 代入(8.2)，得到每模主项 $iA_k/(2\pi km\gamma)$，
余项受 $C|km|^{-3/2}(|A_k|+\|R_k\|_{C^2})$ 控制。
用(1.2)的 $J=2,S=2$ 求和即得(1.4)。
本证明不把通常并不收敛的裸积分 $\int_0^\infty xe^{i\omega x^2/2}\,dx$ 当普通广义积分使用。

这个 $m^{-1}$ 项来自消失圆；同能量上的持续圆有另外的非退化驻相贡献。
后者的 $m^{-1/2}$ 项既未包含于本积分，也不能被本局部尾估计删除。

## 9. 步骤 6：原奇数步与真实光滑最优性例子

在每个小圆上，Fourier 变换的平移恒等式精确给

$$\widehat{f\circ F^r}_k(\varepsilon)
=e^{2\pi ikr\rho_-(h_--\varepsilon)}\widehat f_k(\varepsilon),\qquad r=0,1.$$

因此一阶 jet 系数在 $\varepsilon=0$ 乘以 $e^{2\pi ikr\rho_*}$，证明(1.5)。
同时 $\Pi$ 与原 Koopman 对易[M]，故原 $2m+r$ 步局部相关准确等于
$\mathcal E_m(f\circ F^r,g)$。
固定紧能窗上 $F$ 为光滑自同构，$\|f\circ F^r\|_{C^{20}(K)}$
受相应原紧集的 $C^{20}$ 范数控制；这里只用 $r=0,1$，无随 $m$ 增长的范数损失。

构造最优性观测时，选实值 $\zeta\in C_c^\infty([0,\varepsilon_0))$ 在 $0$ 附近等于 $1$，
在 Morse 图内置

$$f\circ\mathcal K(p,q)=g\circ\mathcal K(p,q)
=\zeta\!\left(\frac{p^2+q^2}{2}\right)(p+iq),\tag{9.1}$$

并在图外延为零。径向 cutoff 在图边界之前恒零，所以这确为原 $C_c^\infty(U)$ 函数。
其支撑仅在中心小圆盘，不触及持续圆或其他临界域；缩小支撑可令 $\chi=1$ 于该支撑的全部能量。
由(6.1)，$d_{f,1}=d_{g,1}=1$、$d_{f,-1}=d_{g,-1}=0$，故
$A_1=2L_0>0$、$A_{-1}=0$。
此观测在真实 Hamilton 时间角下一般仍有全部高模，不是非法指定单角函数。

在 $T=1$，$\beta\ne0$，原完整相关只剩本局部积分，所以

$$C_{2m}(f,f)=-\frac{2L_0}{(2\pi\beta)^2m^2}e^{2\pi im\sigma_0}+O(m^{-3}),$$

从而

$$\lim_{m\to\infty}(2m)^2|C_{2m}(f,f)|
=\frac{8L_0}{(2\pi\beta)^2}>0.\tag{9.2}$$

若希望观测必须实值，可改用(9.1)的实部，即径向 bump 乘 $p$。
此时 $A_1=A_{-1}=L_0/2$，其偶步主项为非零常数乘
$m^{-2}\cos(2\pi m\sigma_0)$。
该余弦不能趋于零：若趋零，则恒等式 $\cos(2x)=2\cos^2x-1$
使偶子列趋于 $-1$，与同一假设矛盾。
所以实值观测同样给严格正的归一化 $\limsup$。
这只是存在观测的最优性，不主张每对观测或每个步数有一致非零下界。∎

## 10. Corrections、Open risks 与交付边界

本局部原命题无需削弱；使用半径负值只是建立偶函数性质的证明装置。
注意以下不能省略的限定：

- 非退化公式的 cutoff 必须完全位于无驻点中心邻域，不能扩到下外区间的可能内部 twist 极大。
- 旋转方向由 $\Omega=-b\,dp\wedge dq$ 和 $\iota_X\Omega=-dh$ 同时固定；反射后的 jets 必须使用同一图。
- 本件的 $m^{-1}$ 项不是 $T=3/16$ 的全局最慢项；持续圆的 $m^{-1/2}$ 项需另算。
- 中心化本身是否保原全局光滑在本件不作假设；所有导数估计只施于原 $f,g$，再取非零 Fourier 模。
- $C^{20}$ 足够但不优化；(1.2)给更细的有限范数依赖。不存在以某个未定义的无限光滑范数藏常数。
- 已接受的 [M]/[N]/[TW]/[B] 不在本件重新验票；本件作者证明仍待 fresh 实际整件检查。
- 不给 Paper31 的新意／价值／容量或正式准入结论，也不启动项目、锁、稿件、PDF 或试排。

完整读取记录：proof-writer/SKILL.md 全部223行；[D]全部118行、[N]全部238行、
[M]全部128行、[TW]全部133行、[B]全部144行。
这些读取是本件依赖消费，不把文献摘要或旧作者状态字段当作新的数学票。

[D]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
