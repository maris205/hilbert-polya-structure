# Paper31 Q2：节点周期、原离散时间、投影范数与薄层尾 V1

日期：2026-09-13 UTC。作者：/root；纸核协作：/root/p31_q2_node_norm_paper_test（只读）。
状态：AUTHOR_PROOF_FROZEN / FRESH_MATH_REVIEW_PENDING。按 proof-writer 保存假设、证明与量词边界。
沿用 [M] 的原完整 \(U,F,h,\Omega,\mu,\Pi\)，固定任意 \(T>0\)；只用纸面数学，无CAS、数值或扫描。
本件所有光滑观测定义在原曲面；需要全局范数时限制于固定闭有限能窗，其紧性由[M]证明。
连续 Hamilton 流只用于识别同一个原 \(F\) 的位移，不另造动力系统替换 Q2。

## 1. 临界点、Hessian 与方向

临界点 \(s_w=(w^2,w)\)，其中 \(T=w^3(w-1)\)、\(h_w=3w-2w^2\)。直接微分有

$$D^2h(s_w)=
\begin{pmatrix}-2(w-1)/w^3&-1/w^2\\-1/w^2&2/w\end{pmatrix},
\qquad\det D^2h(s_w)=\frac{3-4w}{w^4}.$$

对 \(w_-<0\)，矩阵负定，故 acnode 对应非退化局部极大中心；对 \(w_+>1\)，是不定 saddle。
所有临界点均在 torus，四条 terminal 上没有临界点[M]。
离散线性化为

$$A_w=DF(s_w)=
\begin{pmatrix}-w/(w-1)&w/(w-1)\\1/w&-1\end{pmatrix},\qquad
\det A_w=1,\quad \operatorname{tr}A_w=-\frac{2w-1}{w-1}.$$

固定 Hamilton 符号 \(\iota_X\Omega=-dh\)，于是 \(\eta(X)=1\)，并有

$$DX(s_w)=
\begin{pmatrix}w&-2w^2\\-2(w-1)&-w\end{pmatrix},\qquad
A_w=\frac{\operatorname{tr}A_w}{2}I-\frac{DX(s_w)}{2w(w-1)}.$$

在 \(w=w_+\) 令

$$\kappa=w\sqrt{4w-3},\qquad
\mathfrak a=\operatorname{arcosh}\frac{2w-1}{2(w-1)}>0.$$

\(X\) 的本征值为 \(\pm\kappa\)；\(DF\) 在其非稳定／稳定方向上的乘子依次是
\(-e^{\mathfrak a},-e^{-\mathfrak a}\)。所以 \(F\) 翻转两条轴的半支，而 \(F^2\) 保持半支。
在椭圆点相应 Hamilton 频率为 \(\omega_-=|w_-|\sqrt{3-4w_-}>0\)。

## 2. Saddle 周期及可微余项

以下 \(e=h-h_+\)。使用标准解析 Morse 引理，选解析坐标

$$e=pq,\quad \Omega=-a(p,q)\,dp\wedge dq,\quad a>0,\quad a(0,0)=\kappa^{-1}.$$

可交换两轴使 \(p\) 是 \(X\) 非稳定方向；由线性化固定 \(a(0,0)\)。此时

$$X=\frac p a\partial_p-\frac q a\partial_q,\qquad
dt=a(p,e/p)\frac{dp}{p},\qquad \Omega=de\wedge dt.$$

固定充分小的方箱 \(|p|,|q|\le r\)。每次穿箱的正时间为

$$L_{\mathrm{box}}(e)=\int_{|e|/r}^{r}
a(\sigma s,\sigma e/s)\frac{ds}{s},\qquad \sigma\in\{+1,-1\}.$$

由 \(|a-a(0,0)|\le C(|p|+|q|)\)，直接积分给
\(L_{\mathrm{box}}=\kappa^{-1}\log(1/|e|)+O(1)\)。
为使后续微分合法，不能只微分这一裸 \(O(1)\)。展开收敛幂级数
\(a(p,q)=\sum_{j,k\ge0}a_{jk}p^jq^k\)。
当 \(j=k\) 时，积分项为 \(a_{jj}e^j\log(r^2/|e|)\)；
当 \(j\ne k\) 时，两端幂函数在固定 \(e>0\) 或 \(e<0\) 一侧均延为 \(e=0\) 附近的解析函数。
方箱严格缩在幂级数收敛域内，几何级数控制积分后系数及每个所需有限阶导数，故可正常求和。
于是

$$L_{\mathrm{box}}(e)=\mathcal A(e)\log(1/|e|)+\mathcal B_{\sigma,\pm}(e),
\qquad \mathcal A(0)=1/\kappa,$$

其中 \(\mathcal A\) 双侧解析，\(\mathcal B_{\sigma,\pm}\) 由各侧解析延至0。
箱外是奇异纤维的紧正则弧；有限解析流盒及进入／退出横截性使其穿越时间随 \(e\) 解析。
[G] 的 split 节点归一化是实射影圆，删去节点的两个实原像得到两条正则弧。
结合其上两圆、下一圆的真实平滑分类，上侧 \(e>0\) 每圆穿箱一次；下侧 \(e<0\) 唯一圆穿箱两次。
因此对每条退化圆 \(\Gamma_e\)，令上侧 \(m=1\)、下侧 \(m=2\)，有

$$L_\Gamma(e)=m\mathcal A(e)\log(1/|e|)+\mathcal B_\Gamma(e),\tag{2.1}$$

$$L_\Gamma(e)=\frac m\kappa\log(1/|e|)+O(1),\qquad
L_\Gamma'(e)=-\frac m{\kappa e}+O(\log(1/|e|)).\tag{2.2}$$

\(\mathcal B_\Gamma\) 在相应一侧解析延至0。上侧两圆周期相等，亦由原 \(F\) 的换圆与时间保持得到。

## 3. 原 \(F^2\) 是能量依赖的有界解析时间位移

有同一个双侧实解析函数 \(\tau(e)\)，使邻近节点的每条完整正则圆上

$$F^2|_{\Gamma_e}=\phi_X^{\tau(e)}|_{\Gamma_e},\qquad
\tau(0)=2\mathfrak a/\kappa>0.\tag{3.1}$$

证明：由 \(F^*\Omega=\Omega\)、\(h\circ F=h\)，有 \(F_*X=X\)。
取足够小的固定横截面 \(p=p_0>0\)，置 \(z_e=(p_0,e/p_0)\)。
\(F^2z_e=(p_1(e),e/p_1(e))\)，其中 \(p_1(e)>0\) 在0附近解析；缩小 \(p_0\) 可使两点及连接轨道都留在图内。
令

$$\tau(e)=\int_{p_0}^{p_1(e)}a(s,e/s)\frac{ds}{s}.\tag{3.2}$$

积分的 \(s\) 有正下界，故 \(\tau\) 真正双侧解析，且在 \(z_e\) 处(3.1)成立。
与流对易使等式在横截面附近的开流盒成立。
可把 \(p_0\) 取得更小并选包含原点及此流盒的连通小邻域，使所有所需有界时间的流都存在；
在这个邻域，\(F^2\) 与 \(z\mapsto\phi_X^{\tau(h(z)-h_+)}z\) 是解析映射。
解析恒等定理将两者相等延至节点邻域，因此不用对不同象限分别任意选周期提升。
每条完整正则圆上的 \(X\) 无零点且流传递；由一个节点邻域内的点及对易，等式延至整圆。
两圆都经过该邻域，所以共用一个 \(\tau\)。
在固定点的非稳定方向微分，\(e^{\kappa\tau(0)}=e^{2\mathfrak a}\)，固定上述正号及数值。
此提升有界，不能另加发散的非零整数倍完整周期来保持同样的解析提升。

令 \(\alpha_\Gamma=\tau/L_\Gamma\)，则(2.1)–(2.2)给

$$\alpha_\Gamma(e)=\frac{2\mathfrak a}{m\log(1/|e|)}
+O(\log^{-2}(1/|e|)),\qquad
\alpha_\Gamma'(e)\sim\frac{2\mathfrak a}{m e\log^2(1/|e|)}.\tag{3.3}$$

所以 saddle 端不是新增的零 twist 点。下侧原 \(F\) 的相位结合其极限1/2[G及旧端点证明]可取
\(1/2+\tau/(2L_\Gamma)\)；上侧 \(F\) 仍交换两圆，\(\alpha_\Gamma\) 是 \(F^2\) 而非原单步圆旋转。
此局部时间表示不等于原曲面上一个常数时间的全局 Hamilton 嵌入结论。

## 4. 原光滑观测的均值与 Fourier 范数

取原光滑 \(f\)，写 \(c=f(s_{w_+})\)、\(b=f-c\)。
节点箱内 \(|b(p,q)|\le C_f(|p|+|q|)\)。每次穿箱中

$$\int_{|e|/r}^{r}\left(s+\frac{|e|}{s}\right)\frac{ds}{s}=O(1).$$

结合箱外统一有界时间，对任意固定实数 \(r_1\ge1\)，

$$\int_{\Gamma_e}|b|^{r_1}dt\le C_{f,r_1}.\tag{4.1}$$

高次幂由 \(b\) 在紧能窗有界归约。令 \(B_f(e)=\int_{\Gamma_e}b\,dt\)，则

$$\Pi_\Gamma f=c+B_f/L_\Gamma=c+O(L_\Gamma^{-1}),\tag{4.2}$$

$$\int_{\Gamma_e}|f-\Pi_\Gamma f|dt=O(1),\qquad
\int_{\Gamma_e}|f-\Pi_\Gamma f|^2dt
=\int_{\Gamma_e}|b|^2dt-\frac{|B_f|^2}{L_\Gamma}=O(1).\tag{4.3}$$

进一步，\(B_f(e)\) 趋于对应一条或两条 separatrix 弧上 \(b\) 的收敛时间积分 \(B_f(0)\)，且有可微控制

$$B_f(e)=B_f(0)+O(|e|\log(1/|e|)),\qquad B_f'(e)=O(\log(1/|e|)).\tag{4.4}$$

证明：对局部 \(Q(p,q)=b(p,q)a(p,q)\)，\(Q(0,0)=0\)，有精确分解
\(Q(p,q)=Q(p,0)+Q(0,q)+pqR(p,q)\)，其中 \(R\) 光滑。
前两项在穿箱积分换元后只有 \(O(|e|)\) 截断误差及 \(O(1)\) 导数；
最后一项为 \(e\int R(\sigma s,\sigma e/s)\,ds/s\)，其值 \(O(|e|\log)\)，
微分后积分与移动端点项为 \(O(\log)\)（含 \(e\int ds/s^2=O(1)\)）。
箱外正则流盒给有界一阶导数。各有限段求和得到(4.4)。

取 Hamilton 角 \(\theta=t/L_\Gamma\in\mathbb R/\mathbb Z\)。对全部 \(k\ne0\)，由(4.1)

$$|\widehat f_k(e)|\le C_f/L_\Gamma.\tag{4.5}$$

这不是仅固定模的估计。对整数 \(j\ge1\)，\(X^jf\) 在节点为零，满足同样的 \(L^1(dt)\) 界；
在周期圆上分部积分给

$$|\widehat f_k(e)|\le C_{f,j}L_\Gamma^{j-1}|k|^{-j}.\tag{4.6}$$

对任意 \(s\ge0\)，选整数 \(j>s+1\)，按 \(|k|\le L_\Gamma\) 与其补集分割(4.5)–(4.6)，得到

$$\sum_{k\ne0}|k|^s|\widehat f_k|\le C_{f,s}L_\Gamma^s,\qquad
\sum_{k\ne0}|k|^{2s}|\widehat f_k|^2\le C_{f,s}L_\Gamma^{2s-1}.\tag{4.7}$$

所用常数只需要相应有限阶原光滑范数。Wiener \(\ell^1\) 可一致有界，不能说“所有 Fourier 范数都发散”。
归一化中心化 \(L^2(d\theta)\) 是 \(O(L_\Gamma^{-1/2})\)；有权角向范数则可真实发散。
例如在 separatrix 正则点附近选非零紧 bump，则对 \(j\ge1\)，

$$\|\partial_\theta^j f\|_{L^2(d\theta)}^2
=L_\Gamma^{2j-1}\int_{\Gamma_e}|X^jf|^2dt\asymp L_\Gamma^{2j-1}.$$

沿所选 separatrix 弧，非零紧 bump 的任意正阶时间导数不恒零，其平方积分极限正，故这里的下界有依据。

## 5. 投影损失正阶 Hölder 的严格例子

取在 saddle 邻域恒零、在上侧某条退化圆所趋正则 separatrix 弧上非负非零的光滑 bump。
则 \(c=0\)、\(B_f(0)>0\)，由(2.1)、(4.4)

$$\Pi_\Gamma f(e)\sim\frac{\kappa B_f(0)}{m\log(1/|e|)},\qquad
(\Pi_\Gamma f)'(e)\sim\frac{\kappa B_f(0)}{m e\log^2(1/|e|)}.\tag{5.1}$$

在该圆所占的 \(e>0\) 节点象限，取趋节点路径 \(p=q=r\) 或 \(p=q=-r\)。
原 \(f\) 在此恒零，但 \(f-\Pi f\) 的绝对值与 \(1/\log(1/r)\) 同阶。
赋节点值0使其连续趋0，却对任意 \(\beta>0\) 都不满足 \(O(r^\beta)\)。
因此 \(f-\Pi f\) 不能被误当作仍属于原 \(C^\infty\) 类；观测远离 saddle 并不能避免均值投影的此类损失。

## 6. 面积尾、中心化相关尾及尖锐量词

由 \(d\mu=de\,dt\)，两侧每层的总穿箱次数均为2，取 \(\delta>0\) 足够小，有

$$\mu\{0<|h-h_+|<\delta\}
=\frac4\kappa\,\delta\log(1/\delta)+O(\delta).\tag{6.1}$$

这指整个原能带，紧性来自[M]，不存在未控制的仿射无穷远尾。
任意 \(u,v\in L^\infty\) 的能带相关因此对所有 \(n\in\mathbb Z\) 一致为
\(O(\|u\|_\infty\|v\|_\infty\delta\log(1/\delta))\)。
若 \(f,g\) 原光滑并逐圆中心化，圆上(4.3)、Cauchy–Schwarz 及 \(F^n\) 保时间给

$$\left|\int_{|h-h_+|<\delta}
(f-\Pi f)(F^nz)\overline{(g-\Pi g)(z)}\,d\mu\right|
\le C_{f,g}\delta,\qquad n\in\mathbb Z.\tag{6.2}$$

上侧可交换圆，但两个被积分圆都有同样的一致范数界，故不受奇偶影响。
实际上一个因子是此类中心化光滑函数、另一个仅 \(L^\infty\)，用(4.3)的 \(L^1\) 界也足够得到 \(O(\delta)\)。

仅要求有界且逐圆均值零不够：在各正则圆上取 \(u(e,\theta)=\operatorname{sgn}\cos(2\pi\theta)\)，
置 \(v=u,n=0\)，相关尾就是(6.1)，它不是节点处原光滑函数。
对原光滑中心化类，要求对全部 n 一致时 \(O(\delta)\) 也一般不能改成 \(o(\delta)\)：
取第5节非零 bump，\(f=g,n=0\)，未归一化方差趋正的 separatrix 平方积分，减项 \(|B_f|^2/L_\Gamma\to0\)。
积分有限条支即得正数乘 \(\delta+o(\delta)\)。
这仅证明能带截断阶的尖锐性，绝不是关于 \(n\to\infty\) 的相关率下界。

## 7. Acnode 消失小圆的独立尾界

在 \(w_-\) 节点附近，令 \(\varepsilon=h_--h>0\)，用解析 Morse 坐标
\(h=h_--(p^2+q^2)/2\)，\(\Omega\) 在这些坐标的绝对密度为正解析函数 \(b(p,q)\)。
极坐标给沿圆时间密度为 \(b(r\cos\varphi,r\sin\varphi)d\varphi\)，\(r=\sqrt{2\varepsilon}\)。
角积分消去全部奇次数项，且线性化频率给 \(b(0)=1/\omega_-\)，故

$$L(\varepsilon)=2\pi/\omega_-+O(\varepsilon),\qquad
\Pi f=f(s_{w_-})+O(\varepsilon).$$

后式来自原 \(f\) 的 Taylor 展开及一阶项的角积分消失；光滑面积密度的一阶修正只造成二阶贡献。
点态 \(f-f(s)=O(\sqrt\varepsilon)\)，因此
\(\int_{\Gamma_\varepsilon}|f-\Pi f|^2dt=O(\varepsilon)\)。
对两原光滑函数，消失小圆上 \(0<\varepsilon<\delta\) 的中心化相关尾为 \(O(\delta^2)\)，对所有离散 n 一致。
本结论不包含同能级处持续的另一圆；[G]与旧[B]证明它跨 \(h_-\) 是正则解析族。
特别在 \(T=3/16\) 它还有真实 twist 驻点，不能因 acnode 尾小就删除那条圆的贡献。

## 8. 可用与不可用结论

可用的作者结论：完整 saddle 周期与可微余项、原 \(F^2\) 的有界解析能量时间、
全部非零 Fourier 的上述范数界、投影的非-Hölder例子、saddle中心化 \(O(\delta)\) 与acnode消失圆 \(O(\delta^2)\) 尾。
四条 terminal 的正则性及逐圆投影合法性由[M]另证，不靠删去terminal。
这些结论须 actual fresh 数学独查后才能给新数学接受；它们本身不是新的独立長文中心。
仍未证明：混合能量／角度导数的全 Fourier 求和、完整 \(n^{-1/2}\) 或 \(n^{-2}\) 率、振荡主项及其最优性。
选择 \(\delta=\delta(n)\) 而无截断补区的统一常数不能完成这些义务。
与摆系统强先例的关系见[S]，不要因原表面出现 logarithm 就断言新机制或真实阻断。
原22–30页、P31未准入及批次4/5不变。

[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[S]: PAPER31_QPI_Q2_STRONG_TARGET_SOURCE_SCREEN_V1_20260913.md
