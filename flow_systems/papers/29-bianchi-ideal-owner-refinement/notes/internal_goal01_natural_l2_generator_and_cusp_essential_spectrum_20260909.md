# P29 内部研究：自然 L² 传输生成元与 cusp 本质谱边界

记录日期：2026-09-09 UTC。Goal 01 的有界纸面整理单元。
本篇保存已由主线程核对的核心与 Weyl 序列推导，只新增本文件。
继承[正时间 flat trace 笔记][flat]的实际流、线丛及传输方向，
以及[实际有限返回包笔记][packets]的有限体积 cusp 几何。
不改变任何旧文件、协议、锁、回执、失败记录或阶段状态。

**结论。** 对同一实际 Gaussian level-(3) 双曲三流形的完整单位速
测地流，scalar 或平坦 unitary rank-one 传输的自然 Liouville-L²
生成元在紧支撑光滑截面上本质自伴。其闭包的本质谱与谱均为整个
实轴，因而不具有紧 resolvent。下文给出构造性图范数核心证明、
最大分布定义域及深 cusp 内的弱零 Weyl 序列，不作谱型或无点谱断言。

本篇不是 Route-B 审计、候选救活、量子机制认证或全局谱迹等式。
ARS 的 bounded argument-builder 仅用于区分自然生成元、实际
定义域、局部 Weyl 构造与尚未获得的谱侧接口。

## 1. 实际流、Hilbert 空间及传输符号

固定

\[
\Gamma(3)=\{B\in SL_2(\mathbb Z[i]):B\equiv I\pmod3\},
\qquad M=\bar\Gamma(3)\backslash\mathbb H^3,
\qquad Y=SM=T^1M.
\tag{1}
\]

曲率为 -1，\(\phi_t\) 为完整单位速测地流，X 为其生成元。
上游已核查该商无挠、有限体积且具有 cusp；本篇不另换群或时钟。
用 \(d\mu\) 表示 Liouville 正密度。将单位切丛与单位余切丛识别后，
测地流是标准接触形式 \(\alpha\) 的 Reeb 流，满足
\(\alpha(X)=1\)、\(\iota_Xd\alpha=0\)，所以

\[
\mathcal L_X\alpha=0,
\qquad \mathcal L_X\bigl(\alpha\wedge(d\alpha)^2\bigr)=0.
\tag{2}
\]

该接触体积与 Liouville 密度只差固定归一化，故流保 \(d\mu\)。

取 [flat，§5][flat] 中的平坦 Hermitian 线丛 \(L_\theta\to Y\)，
联络记为 \(\nabla\)，正向闭流圈的平行移动为
\(\chi_\theta([\gamma])\)。scalar 情形取平凡线丛与平凡联络。
令

\[
\mathcal H_\theta=L^2(Y;L_\theta,d\mu),
\qquad
(U_\theta(t)f)(x)
=\mathcal P_{\phi_{-t}x\to x}\,f(\phi_{-t}x).
\tag{3}
\]

平行移动沿从 \(\phi_{-t}x\) 到 x 的流段，负时间以反向路径定义。
完整性及路径拼接给一参数群，单位联络与 (2) 给
\(\|U_\theta(t)f\|_2=\|f\|_2\)。

对 \(f\in C_c^\infty(Y;L_\theta)\)，其在任意紧时间区间的支撑
包含于该区间与 \(\operatorname{supp}f\) 的紧流扫集；平行移动光滑，
故 \(U_\theta(t)f\to f\) 于 L²。利用紧支撑光滑截面的密度与酉性，
强连续性推广到整个 \(\mathcal H_\theta\)。

由 [Teschl，Theorem 5.2（Stone），正文 p.124][teschl]，存在自伴
生成元 \(A_\theta\)，使 \(U_\theta(t)=e^{-itA_\theta}\)。在光滑截面上，

\[
\left.\partial_tU_\theta(t)f\right|_{t=0}
=-\nabla_Xf,
\qquad
A_{\theta,0}f:=-i\nabla_Xf,
\qquad D(A_{\theta,0})=C_c^\infty(Y;L_\theta).
\tag{4}
\]

因此 \(A_{\theta,0}\subset A_\theta\)，符号确为
\(U_\theta(t)=e^{-itA_\theta}\)。单位联络与 \(\operatorname{div}_\mu X=0\)
的分部积分亦直接说明 \(A_{\theta,0}\) 对称。
Stone 定理本身尚未说明 (4) 的定义域是核心；这由下一节另证。

## 2. 构造性的时间平均与图范数核心

取 \(\kappa\in C_c^\infty((-1,1))\)，满足 \(\kappa\ge0\)、
\(\int\kappa=1\)。对 \(\varepsilon>0\) 定义

\[
\kappa_\varepsilon(t)=\varepsilon^{-1}\kappa(t/\varepsilon),
\qquad
J_\varepsilon v=\int_{\mathbb R}
\kappa_\varepsilon(t)U_\theta(t)v\,dt.
\tag{5}
\]

积分为 Hilbert 空间中的 Bochner 积分；酉性给
\(\|J_\varepsilon\|\le1\)。对任意 \(v\in\mathcal H_\theta\)，换元得到

\[
U_\theta(h)J_\varepsilon v
=\int\kappa_\varepsilon(t-h)U_\theta(t)v\,dt.
\]

光滑紧支撑核的差商在 L¹ 收敛。因此生成元定义直接给

\[
J_\varepsilon v\in D(A_\theta),
\qquad
A_\theta J_\varepsilon v
=-i\int\kappa_\varepsilon'(t)U_\theta(t)v\,dt,
\]
\[
\|A_\theta J_\varepsilon v\|_2
\le\varepsilon^{-1}\|\kappa'\|_{L^1}\|v\|_2.
\tag{6}
\]

若 \(f\in D(A_\theta)\)，流与其生成元交换，所以

\[
J_\varepsilon f\longrightarrow f,
\qquad
A_\theta J_\varepsilon f
=J_\varepsilon A_\theta f\longrightarrow A_\theta f
\quad\text{于 L²}.
\tag{7}
\]

这些极限来自强连续性与近似恒等核，不要求 f 具有横向光滑性。

取 \(\varepsilon_n\downarrow0\)，由 L² 稠密性选
\(v_n\in C_c^\infty(Y;L_\theta)\)，使
\(\|v_n-f\|_2\le\varepsilon_n^2\)。令
\(w_n=J_{\varepsilon_n}v_n\)。由于

\[
\operatorname{supp}w_n
\subseteq
\{\phi_t x:|t|\le\varepsilon_n,
\ x\in\operatorname{supp}v_n\},
\]

右侧是紧集，且对光滑截面的有限时间传输及积分保持光滑，故
\(w_n\in C_c^\infty(Y;L_\theta)\)。由 (6)，

\[
\|w_n-J_{\varepsilon_n}f\|_2\le\varepsilon_n^2,
\qquad
\|A_\theta(w_n-J_{\varepsilon_n}f)\|_2
\le\varepsilon_n\|\kappa'\|_{L^1}.
\tag{8}
\]

结合 (7)，得到

\[
w_n\to f,\qquad A_{\theta,0}w_n\to A_\theta f.
\tag{9}
\]

这对每个 \(f\in D(A_\theta)\) 成立，因而是明确的图范数核心证明：

\[
\boxed{\overline{A_{\theta,0}}=A_\theta.}
\tag{10}
\]

所以 \(-i\nabla_X\) 在 \(C_c^\infty\) 上本质自伴；不是仅从 Stone
给出的某个自伴扩张反推本质自伴，也没有假设存在横向椭圆估计。
此证明只使用完整光滑保密度流及单位传输所提供的性质。

## 3. 最大分布定义域

对紧支撑测试截面作形式分部积分，单位联络与 (2) 表明
\(A_{\theta,0}^*\) 正是分布表达 \(-i\nabla_X\) 的最大 L² 实现。
具体地，f 属于其定义域，当且仅当分布 \(-i\nabla_Xf\) 可由一个
L² 截面表示；这与伴随定义中测试配对为有界 L² 泛函完全等价。

由 (10) 及自伴性，\(A_\theta=A_{\theta,0}^*\)，所以

\[
\boxed{
D(A_\theta)=
\{f\in\mathcal H_\theta:
\nabla_X f\in\mathcal H_\theta\text{（分布意义）}\},
\qquad A_\theta f=-i\nabla_Xf.
}
\tag{11}
\]

分布导数以全局线丛的光滑局部标架及转换规则理解，不把不同 cusp
当作另加边界条件的独立区间。这里只要求沿 X 的弱导数，不能将 (11)
替换成要求全部方向弱导数的通常 H¹ 定义域。相对 Liouville 密度
没有额外的 \(\tfrac12\operatorname{div}X\) 修正，因为该散度为零。

## 4. 深 cusp 内的双向长流管及单射性

沿用 [packets，§2][packets] 的精确 cusp 几何：某个 cusp 可写为

\[
F\times(r_*,\infty),\qquad
g=dr^2+e^{-2r}g_F,
\tag{12}
\]

F 为紧平坦截面，r 为对数高度。精确 cusp 分解的既有一手来源是
[Müller–Pfaff，§2，正文 p.10，(2.12)–(2.13)][mp]。
本篇只使用这一局部模型，不援引该来源的 Laplace 谱或解析 torsion
结论来替代传输生成元的计算。

令

\[
L_n=n,\qquad r_n=r_*+10n^2,\qquad n\ge1.
\tag{13}
\]

在高度 \(r_n\) 取向上竖直单位速度。其流段 \(|s|<2L_n\) 完全
位于 cusp，高度为 \(r_n+s\)，并有 \(Xr=1\)。在相空间截面
\(\{r=r_n\}\subset Y\) 中，围绕这一单位速度选择足够小的、相对紧的
四维开圆盘 \(B_n\)。由紧时间区间上的光滑依赖，可使全部相关流段满足

\[
Xr>\tfrac12,\qquad
r_n-3n<r(\phi_s z)<r_n+3n
\quad(z\in B_n,\ |s|<2L_n).
\tag{14}
\]

取

\[
\Psi_n:(-2L_n,2L_n)\times B_n\longrightarrow Y,
\qquad\Psi_n(s,z)=\phi_s z.
\tag{15}
\]

横截性说明这是局部微分同胚。其全局单射性须另外核查，不能偷用
尚未建立的 \(|s|<4L_n\) 一致流管。

假设 \(\phi_s z=\phi_t w=p\)，其中 \(s,t\in(-2L_n,2L_n)\)、
\(z,w\in B_n\)。以 p 为同一轨道的零时刻，两段已受 (14) 控制的
完整流段分别对应参数区间

\[
I_s=(-2L_n-s,2L_n-s),\qquad
I_t=(-2L_n-t,2L_n-t).
\tag{16}
\]

这两个区间都含 0，因而其并是一个区间。在并内每个参数点都由
两条已知流段之一覆盖，故沿合并轨道始终有 \(Xr>1/2\)。于是高度
对这一合并参数严格递增。初始点 z、w 分别位于参数 \(-s\)、\(-t\)，
但它们的高度同为 \(r_n\)，所以 \(s=t\)，继而 z=w。

即使中心时差 \(|s-t|\) 接近 \(4L_n\)，上述合并区间仍由原来两段
覆盖；证明没有要求从单个初始点出发的整个 \(4L_n\) 区间已满足 (14)。
因此 (15) 是嵌入流管坐标，其中 \(X=\partial_s\)。

这些流管落在两两不交的高度带

\[
(r_n-3n,r_n+3n),
\]

因为相邻两带的间隔为 \(14n+7>0\)。其最低高度趋于无穷，故任一
固定紧集只与有限个流管相交。圆盘 \(B_n\) 可以随 n 急剧缩小；
本论证不要求其宽度、体积或坐标导数有一致下界或上界。

## 5. 流平行标架、归一化及精确 Weyl 误差

在 (15) 的坐标中，由 \(\mathcal L_Xd\mu=0\) 得

\[
\Psi_n^*d\mu=ds\,d\nu_n(z),
\tag{17}
\]

其中 \(d\nu_n\) 为 B_n 上的光滑正密度，不依赖 s。理由是若拉回
密度写为 \(J_n(s,z)\,ds\,dz\)，流不变性正给 \(\partial_sJ_n=0\)。

在圆盘 \(B_n\) 上选光滑单位截面，再沿 s 方向平行移动，得到
流管内的单位标架 \(e_{\theta,n}\)，满足

\[
\nabla_Xe_{\theta,n}=0,
\qquad |e_{\theta,n}|=1.
\tag{18}
\]

因此扭曲在这个局部沿流计算中消失。这里没有假设全 cusp 的线丛
平凡，也没有把其非平凡 holonomy 改成 1；标架只在嵌入流管内使用。

固定任意 \(\lambda\in\mathbb R\)。取
\(\chi\in C_c^\infty((-1,1))\)、\(\|\chi\|_{L^2(\mathbb R)}=1\)，
以及 \(b_n\in C_c^\infty(B_n)\)，使
\(\|b_n\|_{L^2(d\nu_n)}=1\)。定义

\[
f_n(\Psi_n(s,z))
=L_n^{-1/2}\chi(s/L_n)e^{i\lambda s}
b_n(z)e_{\theta,n}(s,z),
\tag{19}
\]

并在流管外零延拓。\(\chi\) 与 \(b_n\) 的支撑离相应坐标边界有
正距离；其乘积支撑的像紧，故 \(f_n\in C_c^\infty(Y;L_\theta)\)。
由 (17)–(18)，

\[
\|f_n\|_2^2
=L_n^{-1}\int|\chi(s/L_n)|^2ds
\int|b_n(z)|^2d\nu_n(z)=1.
\tag{20}
\]

在此标架中 \(A_{\theta,0}=-i\partial_s\)，所以

\[
(A_\theta-\lambda)f_n
=-iL_n^{-3/2}\chi'(s/L_n)e^{i\lambda s}
b_n(z)e_{\theta,n}(s,z),
\]
\[
\boxed{
\|(A_\theta-\lambda)f_n\|_2
=\frac{\|\chi'\|_{L^2}}{L_n}\longrightarrow0.
}
\tag{21}
\]

没有横向截断误差：b_n 在流管坐标中不依赖 s，且联络项已由 (18)
消去。因此即使横向圆盘缩小、归一化振幅变大，其横向导数也不进入
(21)。这里的常数只来自固定的一维截断函数。

支撑位于 §4 的逃逸高度带。对任意 \(g\in\mathcal H_\theta\)，

\[
|\langle g,f_n\rangle|
\le\|1_{\operatorname{supp}f_n}g\|_2\longrightarrow0,
\tag{22}
\]

因为 L² 函数在趋于无穷的 cusp 尾部的质量趋零。这给
\(f_n\rightharpoonup0\)；这里支撑实际上还两两不交，故序列为
正交归一序列。该论证只用局部有限／逃逸，不从有限体积本身推断弱零。

## 6. 本质谱、非紧 resolvent 及固定常数时钟

对自伴算子，归一化、弱零且满足残差趋零的序列是本质谱的奇异
Weyl 序列；精确判准见 [Teschl，Lemma 6.17，正文 p.145][teschl]。
(20)–(22) 对每个实 \(\lambda\) 成立，结合自伴谱为实数，得到

\[
\boxed{\sigma_{\mathrm{ess}}(A_\theta)
=\sigma(A_\theta)=\mathbb R.}
\tag{23}
\]

序列及局部线丛标架允许随固定 \(\theta\) 选择；没有将不同角色的
Hilbert 空间默认为已作同一全局平凡化。

非紧 resolvent 也可直接从该序列证明。若
\(R_i=(A_\theta-i)^{-1}\) 紧，令
\(r_n=(A_\theta-\lambda)f_n\to0\)，则

\[
f_n=R_i\bigl((\lambda-i)f_n+r_n\bigr)\longrightarrow0
\quad\text{于 L²},
\tag{24}
\]

因为紧算子将弱零有界序列映为范数零序列，与 (20) 矛盾。
resolvent 恒等式进一步说明，任一其他非实点的 resolvent 若紧，
也会迫使 R_i 紧。因此本生成元不具有紧 resolvent。

对任意一个固定 \(c>0\)，若沿用 [flat，§6][flat] 的常数时钟

\[
U_{c,\theta}(s)=U_\theta(s/c),
\qquad A_{c,\theta}=A_\theta/c,
\tag{25}
\]

则定义域不变，图范数等价，\(C_c^\infty\) 核心不变。
将 (21) 用于旧生成元的谱参数 \(c\lambda\)，再除以 c，即得
\(\sigma_{\mathrm{ess}}(A_{c,\theta})=\mathbb R\)，同样没有紧 resolvent。
这只处理固定正实常数钟；不扩展到一般 \(\rho\) 换时或其他项目。

## 7. 与 flat trace、量子解释及 Route 的分离

(23) 是通常 Liouville-L² 自伴算子的本质谱结论，不等于谱型分类。
它允许嵌入点谱，不推出纯绝对连续谱、纯连续谱或无点谱；本篇不作
这些声明，也不计算谱重数。

[flat] 已建立的对象是正时间联合核的 distributional flat trace。
本篇的本质自伴与 (23) 不把它自动变成普通 L² 算子迹、resolvent
trace、谱迹公式或全局 determinant。非紧 resolvent 是该自然传输
模型的明确边界，不是对任意正则化、其他算子或所有量子构造的否定。
这些结论不赋予量子机制有效性，不启动 Route-B、不改 Route verdict，
也不作为救活旧失败候选的理由。

## 8. 来源范围、实际动作与保全

来源分工如下：

- [flat] 固定实际流、正向 unitary transport 及其 flat-trace 边界；
  [packets] 固定实际有限体积 cusp 几何。
- [Müller–Pfaff][mp] 只支持已核读的精确 cusp 分解段落。
- [Teschl][teschl] 的作者公开版本，只援用已核读的 Theorem 5.2
  与 Lemma 6.17 的精确陈述。它们分别提供 Stone 与奇异 Weyl 判准，
  不直接陈述本案线丛生成元的核心或 cusp 序列。

时间平均图范数逼近、最大分布定义域的识别、双向长流管单射性、
局部标架、归一化及 (21) 的误差，均是本篇展开的数学推导，
不是把来源中的别的算子结论照搬成本案定理。同模型代理与主线程
核对只作内部逻辑校对，不当作外部独立科学证据或正式证明认证。

本次只以 apply_patch 新增本文件，随后作一次最小静态检查；
保存时不新增搜索。未执行科学、符号、格点、谱数值、实验或 build，
未改旧笔记、论文、书目、协议、锁、正式回执或失败记录。
既有 STOP、FAIL / BLOCK、Route 与 Stage 5／6 边界保持原状。

[flat]: internal_goal01_positive_time_flat_trace_realization_20260909.md
[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[mp]: https://arxiv.org/pdf/1307.4914v1
[teschl]: https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf
