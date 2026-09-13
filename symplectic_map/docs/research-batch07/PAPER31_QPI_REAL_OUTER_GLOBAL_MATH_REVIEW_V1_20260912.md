# Paper31 Q4：外区间回返、可微无穷渐近与全实正则 twist 的独立审查

日期：2026-09-12 UTC。fresh 非作者审查者：`/root/p31_real_geometry_twist_fresh_check`。
本件只新建当前报告，保留第一阶段冻结审查及所有作者输入；不改索引、锁、FAIL 或接受产物。
任务是新增数学的后继独查，不是正式四门、新意、Route、长文容量或稿件/PDF 验收。

## Claim / Status

对每个固定 $T>0$，审查三个新增实际输入的精确声明：

1. [U]：上外区间真实 $2P$ 回返、split-node 上侧端点、四阶能级、表观极点和有限段 twist。
2. [I]：两个无穷端的旋转极限、带一阶导数余项及实际加权 $J$ 极限。
3. [S]：从已接受基线及上述新增输入合成的全参数五行 twist 表、六端点、准确值域与极大积分刻画。

结论：**PASS_BOUNDED_MATHEMATICS / PROVABLE AS STATED**。三份新增稿的明列数学结论均通过。
无需修改作者量词、方向、阈值、导数阶或合成表；以下给出独立符号核查及关键估计的展开。
现在通过的是固定正时间、全部有限实正则能级上的实际分支回返旋转与 twist 分类。
它不包含节点的全部奇异轨道、逐一有理角的最小周期清单、非自治扰动或一般参数符号。
完整 Q4 的其他义务和强先例包含性不因此自动关闭；本票不产生 Paper31 准入或新意分数。

## Frozen inputs and read scope

本人本任务重新 FULL 读 proof-writer 技能，并 FULL 读下表三份实际冻结作者稿。
输入按任务先后追加，未凭作者消息中的候选公式授票，也未读取全局稿的 DRAFT 作为正式输入。

| 新增实际输入 | 行数 / bytes | SHA-256 |
|---|---|---|
| [U] 上外有限回返 | 112 / 5614 | `beaff1ed89c8f99b71f241340c5833d74ab1debfebf0c408335d2e4ed3dd5bff` |
| [I] 两端 $C^1$ 渐近 | 215 / 11115 | `a6949cdae36598dd7b6d607e32f172321edeb046ebb08d1fab63dd9fa23191f6` |
| [S] 全实正则合成 | 133 / 6753 | `63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24` |

第一阶段 [R1] 是本人已完成、FULL 读回的冻结接受基线：212 行 / 14963 bytes，
SHA `e00f5e920b9a66213e22709e3a7379161d311ee2f735473ba597171ab8d305e8`。
其接受范围是 [G] 实组件/完整原模型、[B] acnode 锚定上界、[M] 中间区间准确分类。
本件不重开这些未变证明；旧 forcing 的同一微分、移动端点和实际 $+P$ 已由 [R1] 核准，仅消费其接口。
本件没有 CAS、Python、数值、参数或阶数枚举、外部查询、上传或再委派。

## Assumptions / Notation / Dependency map

固定 $T>0$，$E_h:v^2+huv-Tv=u^3-Tu^2$，$P=(0,T)$、$O=[0:1:0]$。
由基线，原完整有限纤维上的 $F_T$ 准确对应 $+P$；四 terminal 点保留，不用 affine 删点轨道替换圆回返。
设 $Y=v+(hu-T)/2$、$Y^2=f_h(u)$，不变微分为 $\omega=du/(2Y)$，定向取其正方向。
$\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$、$q=8h-9$、$H=32T+3h$；原能量导数记为撇号。
$h_-<h_+<1$ 为仅有的两个实坏值；下外和中间用 $+P$ 的角，上外用 $+2P$ 的角，均取 $(0,1)$ 提升。
用 $J_-$ 表示下外的 $(\delta/q)\Omega^2\rho_-'$，用 $J_+$ 表示上外二次回返的同式。
其 forcing 分别为 $J_-'=-H\Omega/q^2$ 和 $J_+'=-2H\Omega/q^2$，不能混用倍率。

依赖顺序：基线实组件 → 上外真实积分/端点 → 二倍 forcing 与表观极点 → 有限段符号；
解析根尺度 → 完整对数积分及短弧双尺度估计 → $C^1$ 相消及无穷 $J$ 常数；
基线的锚定符号与新增端点常数 → 全参数零点存在性/唯一性 → 准确值域与非循环积分刻画。

## Proof / itemized audit

### 1. 上外的真实 $2P$ 积分及半周匹配 — PASS

上区间三根满足 $r_1<0<r_2<r_3$；$2P$ 属 identity 圆，且在 $(u,Y)$ 坐标为 $(T,T(h-1)/2)$。
故 $T\ge r_3>r_2$，而 $g_h(T)=(T-r_1)(T-r_2)>0$。
在 $u=r_3+s^2$、$Y=s\sqrt{(s^2+r_3-r_1)(s^2+r_3-r_2)}$ 参数中，其准确有符号坐标是

$$s_2(h)=\frac{T(h-1)}{2\sqrt{(T-r_1)(T-r_2)}},\qquad s_2(h)^2=T-r_3.$$

根及分母在上外区间实解析，故此式解析穿过 $h=1$，不存在对绝对值平方根求导的假奇点。
圆的无穷图与 [R1] 的同类参数相同，微分正则且正向遍历为 $s:-\infty\to+\infty$。
$I_2=\int_{-\infty}^{s_2}\omega$ 满足 $0<I_2<\Omega$，准确代表 $+2P$ 的正向实提升，非跨分支的 $P$ 复积分。
$h=1$ 时 $s_2=0$，偶核给 $I_2/\Omega=1/2$；与 $P$ 准确四阶相容。
在另一实圆上用陪集平移识别，微分和回返同时保持，角度相同；最小分支回返是二次，不是最小点周期必为二。

### 2. split node 上侧端点与表观极点 — PASS

到 $h_+$，令 $a=w_+^2(w_+-1)>0$、$b=-w_+^2/4<0$，则 $r_2,r_3\to a$、$r_1\to b$。
由于 $T=w_+a>a$ 且 $h_+<1$，$s_2\to-\sqrt{T-a}<0$，与零有严格距离。
完整周期的极限核为 $1/(|s|\sqrt{s^2+a-b})$，在零的固定邻域非负且不可积，Fatou 给 $\Omega\to\infty$。
从负无穷到 $s_2$ 的弧不经过该极点；有界段有统一正下界，无穷尾有统一 $C/s^2$ 上界。
支配收敛给 $I_2$ 有限正极限，故实际回返角从正侧趋于零，而不是 $1/2$ 或未知整数平移。

局部复对数的 $\log(2P)-2\log(P)$ 是整数周期的固定组合，旧算子消去全部周期，故 $\mathcal LI_2=-2H/(q\delta)$。
这一步只用复对数比较 forcing，并没有把 $\log(P)$ 宣称为同一实圆的弧。
取 $K=\delta\Omega^2\rho_+'$，则在 $q\ne0$ 有 $qK'-8K=-2H\Omega$。
$h_q=9/8>1>h_+$ 是正则值，$K$、$\Omega$、$\rho_+$ 实解析，等式延拓至该点，给

$$K(h_q)=H(h_q)\Omega(h_q)/4,\qquad
\rho_+'(h_q)=\frac{H(h_q)}{4\delta(h_q)\Omega(h_q)}>0.$$

因此 $J_+=K/q$ 在左、右分别趋 $-\infty,+\infty$，但真实回返角及其导数没有奇点。
全过程没有删除 $h=1$ 或 $h=9/8$，也没有在表观极点直接应用失效的有理表达式。

### 3. 上外有限区间的严格符号 — PASS

$H(h_+)=w_+(2w_++1)(4w_+-3)^2>0$ 且 $H'=3$，故上区间的 $q\ne0$ 两段各有 $J_+'=-2H\Omega/q^2<0$。
若 $(h_+,h_q)$ 中有 $J_+(s)\ge0$，其左方全部 $J_+>0$，而 $q/\delta<0$，导致角度严格递减。
这与左端极限零及区间内 $\rho_+>0$ 矛盾，所以这一整段 $J_+<0$、$\rho_+'>0$。
$h_q$ 处已单独给准确正导数；右侧 $J_+$ 从 $+\infty$ 严格递减，至多一次过零。
若过零，$\rho_+''=qJ_+'/(\delta\Omega^2)<0$，零点简单且前正后负；有限稿没有偷加该零点存在性。

### 4. 无穷端的全部根和实际积分尺度 — PASS

令 $h=\sigma/\varepsilon$，$\sigma=\pm1$、$\varepsilon\downarrow0$，$\ell=\log(1/\varepsilon)$、$c=\log T$。
采用 [I] 的 $O_{C^1,T}$ 记号：余项及其 $\varepsilon\partial_\varepsilon$ 同时受界，常数仅要求对固定 $T$ 有效。
第4–6节的余项与 $B_0,C_0$ 撇号指 $\varepsilon$ 导数；转换回原 $h$ 导数时另写链式因子。
代入 $u=\sigma T\varepsilon+\varepsilon^2z$，逐项展开 $f_h=u^3-Tu^2+(hu-T)^2/4$ 得

$$\varepsilon^{-2}f_h=z^2/4-T^3+\sigma\varepsilon(T^3-2T^2z)
+\varepsilon^2(3T^2z-Tz^2)+3\sigma T\varepsilon^3z^2+\varepsilon^4z^3.$$

零阶方程的两根为 $\pm2T^{3/2}$，导数非零；实解析隐函数定理给小根及全部可微 Taylor 余项。
第三根由 Vieta 给 $r_1=T-1/(4\varepsilon^2)-r_2-r_3$；三根次序对小正 $\varepsilon$ 严格成立。
于是 $D=r_3-r_1=(4\varepsilon^2)^{-1}(1+O_{C^1,T}(\varepsilon^2))$，
$d=r_3-r_2=4T^{3/2}\varepsilon^2(1+O_{C^1,T}(\varepsilon))$，$\kappa=\sqrt{d/D}=4T^{3/4}\varepsilon^2(1+O_{C^1,T}(\varepsilon))$。
正向短弧的上端分别为 $U_-=0$、$U_+=T$；两端充分远时回返点的 $Y$ 均正，上端只在这里使用 $h>1$。
因此 $\rho_\sigma=1/2+A_\sigma/\Omega$，其中 $A_\sigma=\frac12\int_{r_3}^{U_\sigma}du/\sqrt{f_h(u)}$，没有整数或方向自由度。

### 5. 对数常数及完整周期的一阶控制 — PASS

变量代换给 $\Omega=2K_c(\kappa)/\sqrt D$，$K_c=\int_0^\infty dt/\sqrt{(1+t^2)(t^2+\kappa^2)}$。
[I] 从 $K_c$ 减去 $\operatorname{arsinh}(1/\kappa)$ 的做法保留了准确常数，而不是只估计主导对数阶。
记 $a(t)=(1+t^2)^{-1/2}-1$；剩余积分的零参数极限由
$F(t)=\log(t/(1+\sqrt{1+t^2}))$ 的原函数计算，两个分界端抵消，得到 $\log2$。
另一个 $\log2$ 来自 $\operatorname{arsinh}(1/\kappa)$，所以常数确为 $\log(4/\kappa)$。
近零使用 $|a(t)|\le Ct^2$，在 $(0,\kappa)$、$(\kappa,1)$ 分别积分，误差为 $O(\kappa^2)$、$O(\kappa^2\log(1/\kappa))$。
乘 $\kappa$ 后的导数核为 $\kappa^2a(t)/(t^2+\kappa^2)^{3/2}$，同样两段给完全相同的界；尾段为 $O(\kappa^2)$。
对每个正参数的积分号下求导有局部可积控制，所以这是实际 $C^1$ 估计，不是对未控制的 $o(1)$ 求导。
由于 $\varepsilon\kappa'/\kappa=2+O_T(\varepsilon)$，链式法则给

$$\Omega=\varepsilon(8\ell-3c+r),\qquad
|r|+|\varepsilon r'|=O_T(\varepsilon).$$

$D$ 的相对 $O_{C^1}(\varepsilon^2)$ 误差乘 $\ell$ 后仍为 $O_{C^1}(\varepsilon)$，这一吸收同时控制导数。

### 6. 短弧双移动尺度与加权相消 — PASS

令 $B_\sigma=U_\sigma-r_3$、$\eta=d/B_\sigma$、$\zeta=B_\sigma/D$；短弧减去准确的 $\operatorname{arsinh}$ 后，误差积分是

$$\mathcal E(\eta,\zeta)=\int_0^1
\frac{(1+\zeta x)^{-1/2}-1}{\sqrt{x(x+\eta)}}\,dx.$$

分子绝对值至多 $C\zeta x$，而 $x/\sqrt{x(x+\eta)}\le1$。
$\eta\partial_\eta$ 额外产生的比例 $\eta/(2(x+\eta))\le1/2$；$\zeta\partial_\zeta$ 的分子也受 $C\zeta x$ 控制。
所以 $|\mathcal E|+|\eta\mathcal E_\eta|+|\zeta\mathcal E_\zeta|\le C\zeta$，已包含两个端点尺度移动的导数。
$B_-=T\varepsilon(1+O_{C^1}(\varepsilon))$、$B_+=T(1+O_{C^1}(\varepsilon))$ 给 $\eta_-=O(\varepsilon)$、$\eta_+=O(\varepsilon^2)$；所有对数导数有界。
将准确 $\operatorname{arsinh}(\eta^{-1/2})$ 的常数和余项带入，得到

$$A_\sigma=\varepsilon(a_\sigma\ell-c/2+s),\qquad
a_-=1,\quad a_+=2,\quad |s|+|\varepsilon s'|=O_T(\varepsilon).$$

记 $B_0=8\ell-3c$、$C_0=a_\sigma\ell-c/2$；真正求导后，两个外层 $\varepsilon$ 的零阶乘积抵消，留下

$$\Omega A_\varepsilon'-A\Omega_\varepsilon'
=\varepsilon^2(B_0C_0'-C_0B_0')+O_T(\varepsilon^2\ell)
=\varepsilon(3a_\sigma-4)c+O_T(\varepsilon^2\ell).$$

这里 $r',s'=O_T(1)$，故含误差的交叉项确实不超过所写阶；不是把比值的弱余项拿来求导。
原导数转换为 $\partial_h=-\sigma\varepsilon^2\partial_\varepsilon$，且 $\delta/q=\sigma(1+O_T(\varepsilon))/(8\varepsilon^3)$。
所以 $J_\sigma=-(3a_\sigma-4)c/8+O_T(\varepsilon\ell)$，准确得到

$$\lim_{h\to-\infty}J_-=(\log T)/8,\qquad
\lim_{h\to+\infty}J_+=-(\log T)/4.$$

相同比值给旋转端点 $5/8$ 与 $3/4$；所有估计在 $c=0$ 时仍有效，没有除以 $\log T$。
上端的因子二来自实际回返短弧的 $a_+=2$，与第2步的 forcing 倍率一致。

### 7. 全参数表和两个阈值的严格性 — PASS

由基线，$T\le3/16$ 时下外严格增；$T>3/16$ 时设 $h_0=-32T/3<h_-$，$J_-$ 在左段严格增，在 $[h_0,h_-)$ 为正。
若 $3/16<T<1$，无穷极限负而 $J_-(h_0)>0$，所以恰一次过零，因 $q/\delta<0$ 得非退化极大。
若 $T\ge1$，左极限非负使每个有限点的 $J_-$ 严格正，故下外严格减。
特别在 $T=1$，可对任意有限点再取更左一点，用严格递增及极限零得严格正；不需要更高阶展开。
上外 $J_+$ 在 $h_q$ 右侧从正无穷严格减：$T\le1$ 时右极限非负，所以始终严格正；$T>1$ 时恰一次过零。
$T=1$ 的上外严格正同样由单调性和零极限给出；左有限段已由第3步覆盖。
结合基线中区间结论，得到 [S] 的五行表：小于 $3/16$ 的极大在中间，介于 $3/16$ 与 $1$ 的在下外，大于 $1$ 的在上外。
$T=3/16$、$T=1$ 没有正则驻点能级；前者有一个位于奇异 acnode 能级的持续圆极大，不混入正则计数。
每个其余 $T>0$ 准确一个驻点能级；外区间该能级有两个圆，但不是两个不同能级。
简单零点与 $\rho''<0$ 来自基线或第3步，排除遗漏水平拐点和退化驻点。

### 8. 六端点、值域及极大的积分刻画 — PASS

六个单侧端点依次是下外 $(5/8,\theta)$、中间 $(\theta,1/2)$、上外 $(0,3/4)$；上外始终指二次回返。
严格单调段的值域为两端之间的开区间；唯一极大段的值域为 $(\min\{\text{两端}\},M]$。
每个有限内部值严格介于零与一，故 $M<1$；极大两侧的严格号还保证 $M$ 大于对应两端。
因此 [S] 的七行值域包括全部开闭端点，尤其上外 $T>1$ 的下界仍为零，不是 $3/4$。
$\theta=5/8$ 等价于 $w_-=-\sqrt2/2$，代入准确给 $T=(1+\sqrt2)/4$；这只交换下外较低端点，不改变驻点个数。
下外/中间用锚定积分 $\int_{h_-}^{h_m}H\Omega/q^2=0$，排除锚点，已有唯一性保证定义非循环。
上外由 $J_+'=-2H\Omega/q^2$ 从 $h$ 积至无穷，得到 $J_+(h)=-(\log T)/4+\int_h^\infty2H\Omega/q^2$。
所以驻点方程的右侧准确为正的 $(\log T)/4$，没有尾积分符号翻转。
尾核为 $O(\log s/s^2)$，绝对收敛；其严格正性与此前唯一性相容，可再用实际 $2P$ 积分唯一评价 $M_+$。
这些积分定义不使用目标角拟合，也不把未知极值本身当作未证的存在性假设。

## Corrections / Open risks / Final disposition

没有需作者修正的数学错误或隐藏附加假设；三份输入的限定结论按原文通过。
新增接受补齐了实正则区间的外端、表观极点与全参数 twist 合成；第一阶段未变证明不因本次后继接受被重审或改写。
需持续保留原完整圆/affine 删点、一次/二次回返、能级数/圆数，以及奇异/正则能级的区别。
没有声称最大值或驻点能量有初等闭式，也没有证明驻点随时间的全局光滑分岔、逃逸速率或完整有理共振清单。
科学证明接受不等于先例排除、长文价值或正式准入；本任务没有重评分或改变任何锁定验收门槛。

[R1]: PAPER31_QPI_REAL_GEOMETRY_TWIST_MATH_REVIEW_V1_20260912.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
[M]: PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md
[U]: PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md
[I]: PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
