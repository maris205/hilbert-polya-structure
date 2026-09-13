# P29 内部论证：横向外代数 supertrace 与经典 Ruelle 乘积

日期：2026-09-09 UTC。Goal01 的有界纸面续接；只新增本笔记。

本篇把已建立的正时间 scalar flat trace 扩展到同一真实流的横向
微分形式，并直接辨认其交替和的 Laplace 变换。这里的“交替和”
是有限个合法分布迹的线性组合，不是普通 Hilbert 空间 supertrace，
也不据此宣告全平面 Ruelle 延拓、共振或量子谱恒等式。

ARS 的有界论证与来源定位规范用于区分局部束值公式、非紧推送、
无穷时间收敛和 Euler 乘积四个不同接口。

## 1. 对象与实际束值传播子

沿用[正时间迹实现][flat]：M 是 Gaussian level-(3) 双曲三流形，
Y=SM，φ_t 是完整单位速测地流，X 是生成向量场。取
\[
 E_0^*:=\{\xi\in T^*Y:\xi(X)=0\},\qquad
 \mathcal E_k:=\Lambda^kE_0^*\otimes L_\theta,\quad 0\le k\le4.
 \tag{1}
\]
E_0^* 是光滑 rank-four 实向量束；以下外代数与系数取复化。
L_θ 的正向平行移动态仍按 [flat, §5] 明定为 χ_θ(γ)。
对 y=φ_{-t}x，定义
\[
 (U_{k,\theta}(t)\alpha)(x)
 =\bigl(\Lambda^k(D\phi_{-t})_x^*\otimes
        \mathcal P^+_{y\to x}\bigr)\alpha(y).
 \tag{2}
\]
因为 Dφ_{-t}X_x=X_y，拉回保存 ann(X)，所以 (2) 的束型正确。
平行移动态与微分拉回的复合律给群律；它对光滑紧支撑截面合法。
k=0 恢复 [flat] 的正向 transport 约定，而非相反角色。

不要改用完整 \(\Lambda^*T^*Y\)：完整空间还含一个返回特征值 1，
其全部外代数交替迹反而恒为零。式 (1) 明确去掉流方向。

## 2. 正时间逐次数 flat trace

(2) 的联合核是 scalar 图形核乘光滑的有限维 bundle map。
局部乘法不增加 wavefront，故 [flat, §§2–3] 的联合对角拉回、
有界时间窗的有限返回圆周、support-proper 推送及 plateau cutoff
论证逐项适用。先取对角纤维迹，再推送到时间。

令 γ 为有向本原轨道，r≥1，T=rℓ_γ，
P_γ=dφ_{ℓ_γ}|_{E^s\oplus E^u}。
ann(X) 经限制与横向对偶空间同构；返回纤维映射的迹为
\[
 \chi_\theta(r[\gamma])\,
 \operatorname{tr}\Lambda^k(P_\gamma^{-r})^*.
\]
对偶不改变特征多项式与外幂迹，故可省略星号。局部 delta 换元
仍用原来的分母和本原圆周一次积分，得到
\[
 \Theta_{k,\theta}:=\operatorname{tr}^{\flat}_+U_{k,\theta}
 =\sum_{\gamma,r}
 \frac{\ell_\gamma\,\chi_\theta(r[\gamma])\,
       \operatorname{tr}\Lambda^kP_\gamma^{-r}}
      {|\det(I-P_\gamma^{-r})|}
 \delta_{r\ell_\gamma}
 \quad\text{于 }\mathcal D'(0,\infty).
 \tag{3}
\]
这正是 [Dyatlov–Zworski Appendix B (B.6)][dz] 的局部束值计算：
其局部方法只需要 flow box 与横向非退化。本案的非紧推送由
[flat] 独立补上；不把来源的紧流形全局定理直接当成本案定理。

## 3. 交替和严格消掉完整横向分母

对任意四维线性映射 Q，
\[
 \sum_{k=0}^4(-1)^k\operatorname{tr}\Lambda^kQ=\det(I-Q).
 \tag{4}
\]
[自然振幅, §3][amplitude] 已由 Jacobi 方程直接证明
\[
 \det(I-P_\gamma^{-r})
 =\det(I-P_\gamma^r)
 =4(\cosh T-\cos(r\vartheta_\gamma))^2>0.
 \tag{5}
\]
其中 \(\det P_\gamma=1\)；不是仅知道行列式的绝对值。
(4)–(5) 代入 (3) 给
\[
 \boxed{\displaystyle
 \Theta_\theta^{\mathrm{alt}}
 :=\sum_{k=0}^4(-1)^k\Theta_{k,\theta}
 =\sum_{\gamma,r}\ell_\gamma\,
   \chi_\theta(r[\gamma])\,\delta_{r\ell_\gamma}
 =:\nu_\theta.}
 \tag{6}
\]
有限个次数的相加没有无穷重排问题。θ=0 时右侧为正测度；
一般 θ 时为局部复 Radon 测度。

式 (6) 的正号利用了本案的维数与旋转返回结构，不能不经检查地
推广到任意 Anosov 流。分母被完整外代数交替迹消掉，不是擅自
替换 scalar 分母，也不是把 scalar 迹直接改写成 (6)。

## 4. 各次数与交替和的共同 Laplace 右域

[amplitude] 提供以下已核查输入：
\[
 T\ge\delta=2\operatorname{arcosh}(7/2),\quad
 |\det(I-P_\gamma^{-r})|\ge e^{2T}(1-e^{-\delta})^4,\quad
 N(L):=\#\{(\gamma,r):r\ell_\gamma\le L\}\le Ce^{2L}.
 \tag{7}
\]
四个返回特征值的模是 e^{-T},e^{-T},e^T,e^T。
令 q_k=min(k,4-k)。每个 k 重特征值乘积的模至多 e^{q_kT}，所以
\[
 |\operatorname{tr}\Lambda^kP_\gamma^{-r}|
 \le {4\choose k}e^{q_kT}.
 \tag{8}
\]
因此对 I_n=(n,n+1]，n≥0，以 \(C_\delta=(1-e^{-\delta})^{-4}\)，
\[
 |\Theta_{k,\theta}|(I_n)
 \le A_k(n+1)e^{q_kn},\qquad
 A_k={4\choose k}C_\delta Ce^2.
 \tag{9}
\]
这里 q_k−2≤0，故在 (7) 的系数界中使用
e^{(q_k-2)T}≤e^{(q_k-2)n}；返回计数已包括所有重复，
不再额外乘重复次数。由分壳求和，
\[
 \int e^{-\sigma t}\,d|\Theta_{k,\theta}|(t)
 \le\frac{A_k}{(1-e^{-(\sigma-q_k)})^2},
 \qquad \sigma>q_k.
 \tag{10}
\]
所以所有五个次数均可在 Re s>2 中绝对变换并有限相加。
k=0、4 的充分右域是 Re s>0，k=1、3 是 Re s>1；
不宣称这些都是精确收敛边界。

直接对 (6) 也有
\[
 |\nu_\theta|(I_n)\le Ce^2(n+1)e^{2n},\qquad
 \int e^{-\sigma t}\,d|\nu_\theta|(t)
 \le\frac{Ce^2}{(1-e^{-(\sigma-2)})^2},\quad\sigma>2.
 \tag{11}
\]
紧右子域的正常收敛给全纯性。这个指数界不同于 scalar 迹的
二次累积增长界；不能在交替消分母以后沿用 scalar 的 Re s>0。

## 5. 同一有向 primitive-orbit Euler 乘积

在 Re s>2 定义规范化的经典乘积
\[
 \zeta_\theta^{\mathrm{cl}}(s)
 :=\exp\left(
 \sum_{\gamma\ \mathrm{primitive}}\sum_{r\ge1}
 \frac{\chi_\theta(r[\gamma])}{r}e^{-sr\ell_\gamma}
 \right)
 =\prod_{\gamma\ \mathrm{primitive}}
   (1-\chi_\theta([\gamma])e^{-s\ell_\gamma})^{-1}.
 \tag{12}
\]
对 Re s≥σ>2，log 级数逐项绝对值可用
\(\sum_{\gamma,r}e^{-\sigma r\ell_\gamma}\) 控制；由 (7) 分壳可和。
其 s 导数由 \(\ell_\gamma e^{-\sigma r\ell_\gamma}\) 控制，
由 (11) 可和。因此 (12) 是非零全纯函数、分支取 log→0
当实 s→+∞，且可合法逐项微分：
\[
 \boxed{\displaystyle
 -\partial_s\log\zeta_\theta^{\mathrm{cl}}(s)
 =\int_0^\infty e^{-st}\,d\nu_\theta(t)
 =\sum_{k=0}^4(-1)^k
   \int_0^\infty e^{-st}\,d\Theta_{k,\theta}(t),
 \qquad \operatorname{Re}s>2.}
 \tag{13}
\]
本篇“Ruelle 乘积”只指 (12) 的有向 primitive-flow convention。
不额外识别正反方向、计起点或写入一个尚未核查的 Selberg
factorization。也不把 (13) 称为 resolvent flat trace；它先是
已建立时间分布的绝对 Laplace 变换。

常数钟 c>0 给 U_{c,k,θ}(t)=U_{k,θ}(t/c)，从而
\[
 \Theta^{\mathrm{alt}}_{c,\theta}
 =c\,(t\mapsto ct)_*\nu_\theta,\qquad
 \zeta^{\mathrm{cl}}_{c,\theta}(s)=\zeta^{\mathrm{cl}}_\theta(cs).
 \tag{14}
\]
于是 (13) 对应的充分右域变为 Re s>2/c；导数自动产生 c。
ann(X/c)=ann(X)，不需要更换横向束。

## 6. 支撑障碍的范围与仍未建立的接口

(6) 的完整同周期包具有正权重 ℓ_γ；其零 Fourier 系数包含此前
三条零同调见证的严格正贡献。由[实际有限包, §6][packets] 的
有限三角多项式论证，存在依赖这些新权重的开稠密、满 Haar 测度
集合 \(G_{\mathrm{alt}}\)，满足
\[
 \forall\theta\in G_{\mathrm{alt}}\ \forall c>0:
 \quad \Theta^{\mathrm{alt}}_{c,\theta}
 \text{ 不集中于 }\{r\log p:r\ge1,\ p\text{ 为有理素数}\}.
 \tag{15}
\]
这不是预先假定它与 scalar 权重产生相同的 G。
若要同时使用二者，取 \(G_{\mathrm{alt}}\cap G_{\mathrm{scalar}}\)
即可；有限交仍然开稠密且满测度。无需对不可数 c 取零集并。

本篇只补全同一流的横向束值正时间迹、其有限交替和与
右域经典 Euler 乘积。未建立：零时间正则化、所有时空极限交换、
普通 L² supertrace、resolvent／共振迹、全平面延拓、Selberg
行列式身份、自然自伴量子模型或任何 Route／Stage 晋级。
例外角色、非阿贝尔 twists 和一般非恒定时钟亦不被 (15) 否定。

本篇是 AI 辅助内部纸面推导，不是正式证明认证。主代理实际读取
[flat]、[amplitude] 及来源 Appendix B 的局部公式 (B.2)–(B.6)，
通过 apply_patch 新增本文件。未运行科学、符号、census、producer、
实验或稿件 build；旧 formal 笔记、锁和失败状态保持原样。
单独的差异读审与文本检查若完成，将由工作索引记录。

[flat]: internal_goal01_positive_time_flat_trace_realization_20260909.md
[amplitude]: internal_goal01_geometric_return_amplitude_and_laplace_bound_20260909.md
[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[dz]: https://arxiv.org/pdf/1306.4203v4

