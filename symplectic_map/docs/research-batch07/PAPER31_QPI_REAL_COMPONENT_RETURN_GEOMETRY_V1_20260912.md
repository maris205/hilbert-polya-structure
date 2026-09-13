# Paper31 Q4: all-positive-time real components and the actual return interface

日期：2026-09-12 UTC。作者：`/root/p31_real_components_and_return`。
状态：新增有界证明，待 fresh 非作者独立核准；不授新意、候选或论文准入。
本件只补原 Q4 的必要实几何，不把以下标准实椭圆曲线分类单立长文。

## Claim, status and assumptions

对每个固定 $T>0$，令
$$
W_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0],\quad P=(0,T),
$$
$$
\delta_T(h)=h^4-h^3-8Th^2+36Th+16T^2-27T.
$$
以下有限正则纤维分类为 **PROVABLE AS STATED**；量词是全部 $T>0$，不是样本范围。
原 Q4 的全局旋转数值域、端点及 twist 分类仍为 **NOT CURRENTLY JUSTIFIED**。
实连通分支均指完整射影 $W_h(\mathbb R)$，经下述原模型同构解释为原 $\mathcal U_T$ 的完整有限纤维。
不将 $x,y>0$、单个 affine 图或删除分母为零的轨道冒充这个对象。

设 $w_-<0$、$w_+>1$ 为 $w^3(w-1)=T$ 的两个实解，并定义
$$
h_-=w_-(3-2w_-),\qquad h_+=w_+(3-2w_+).
$$
它们满足 $h_-<h_+<1$，并恰为 $\delta_T$ 的两个实根；两根均简单。
把每个正则纤维的 identity 分支记为 $C^0$；若有第二分支，记为 $C^1$。

| 能级 | $\delta_T$ 符号 | 实分支数 | $P$ 所在分支 | 原 $F_T$ 与最小分支回返 |
|---|---|---|---|---|
| $h<h_-$ | 正 | $2$ | $C^0$ | 分别保持两圆，回返为 $F_T$ |
| $h_-<h<h_+$ | 负 | $1$ | $C^0$ | 保持唯一圆，回返为 $F_T$ |
| $h>h_+$ | 正 | $2$ | $C^1$ | 交换两圆，回返为 $F_T^2$ |

两端奇异纤维不列入圆回返表：$h_-$ 是孤立实 node，$h_+$ 是 split real node。
$h=1$ 对所有 $T>0$ 都是合法上区间正则能级，且 $P$ 的准确阶为 $4$。

## Proof strategy and dependency map

1. 用实际 singular-point 消元参数化全部实坏值，并直接计算 $\delta_T'$。
2. 完成方平方，以实 cubic 三根的符号定位 $P$；上区间用精确 $h=1$ 分解作连续性锚点。
3. 用实椭圆曲线群的连通分支商决定 $+P$ 的分支回返。
4. 使用已接受原曲面的有限纤维与四 terminal charts；显式有理式在每个正则纤维上延拓。
5. 原 terminal 点逐一计算，说明完整圆与单图 affine 轨道的差别。

主要标准事实仅为：实三次多项式判别式根型；光滑射影曲线的双有理映射延拓为同构；
实椭圆曲线连通分支为实 Lie 群的圆及其陪集，两个分支的商群为 $\mathbb Z/2$。
这些事实不作新意计分。以下不使用 CAS、枚举、数值采样或计算实验。

## Proof

### Step 1. 全部实坏值及其顺序

在奇点处 $u,v\ne0$。令 $z=v/u$，直接从原方程及两偏导消元得
$$
u=T-z^2,\quad v=z(T-z^2),\quad u^2=Tz,\quad h=T/z-3z.
$$
令 $w=u/z$；从 $T=w^2z$ 及 $u=T-z^2$ 得 $z=w(w-1)$，故
$$
T=w^3(w-1),\quad h=w(3-2w),\quad u_0=w^2(w-1),\quad v_0=w^3(w-1)^2.
\tag{1}
$$
逆向代入验证每个 $w\notin\{0,1\}$ 都给这个奇点。
当实 cubic 奇异时，其重根必实：否则非实重根及共轭至少占四个次数。
因此每个实坏值的奇点实，式 (1) 的 $w$ 也实，没有遗漏非实参数产生的实坏值。

函数 $t(w)=w^3(w-1)$ 在 $(-\infty,0)$ 严格递减，从正无穷到零；
在 $(1,\infty)$ 严格递增，从零到正无穷，因为 $t'(w)=w^2(4w-3)$。
区间 $[0,1]$ 上 $t(w)\le0$，所以固定 $T>0$ 恰有上述两个实解。
写 $w_-=-a$、$w_+=1+b$，其中 $a,b>0$，则
$$
T=a^3(a+1)=b(b+1)^3.
$$
$s\mapsto s(s+1)^3$ 严格递增，且 $a(a+1)^3>a^3(a+1)$，故 $b<a$。
于是 $h_-=-3a-2a^2$、$h_+=1-b-2b^2<1$，并有
$$
h_+-h_-=1+3a-b+2(a^2-b^2)>0.
$$
Weierstrass 判别式是 $T^3\delta_T$；式 (1) 给全部两个实零点。
直接代入导数还给整式恒等式
$$
\delta_T'\bigl(w(3-2w)\bigr)=w^2(4w-3)^3\quad\text{when }T=w^3(w-1).
\tag{2}
$$
两值均非零，在 $w_-$ 为负，在 $w_+$ 为正。
因首项为 $h^4$，$\delta_T$ 在两外区间为正，在两根之间为负。

### Step 2. 三次实根与 $P$ 的分支

这里只完成方平方，不平移横坐标：令 $Y=v+(hu-T)/2$，则
$$
Y^2=f_h(u)=u^3+(h^2/4-T)u^2-hTu/2+T^2/4,\qquad P=(0,T/2).
\tag{3}
$$
$\operatorname{disc}(f_h)=T^3\delta_T/16$。
若 $\delta_T<0$，$f_h$ 有一个实根，完整实曲线有一个圆。
若 $\delta_T>0$，写三个实根为 $r_1<r_2<r_3$；
位于 $r_1\le u\le r_2$ 的 oval 是 $C^1$，位于 $u\ge r_3$ 并加上 $O$ 的圆是 $C^0$。
此描述来自方程 $Y=\pm\sqrt{f_h(u)}$ 在根处的粘合；两圆不在无穷点再次相接。
因为 $f_h(0)=T^2/4>0$，$P$ 只能属于其中恰有 $u=0$ 的圆，不能经过根端点。

当 $h<h_-$ 时，$h<0$，且
$$
h_-^2/4-T=w_-^2(9/4-2w_-)>0.
$$
所以 $h^2/4-T>0$，式 (3) 所有系数都正。
因此 $f_h(u)>0$ 对全部 $u\ge0$，三个实根全为负，$P\in C^0$。

上区间含 $h=1$。这个能级有精确分解
$$
f_1(u)=(u-T)(u^2+u/4-T/4).
$$
二次因子的根为 $\alpha=(-1-\sqrt{1+16T})/8<0$ 和
$\beta=(-1+\sqrt{1+16T})/8>0$；关系 $T=4\beta^2+\beta$ 给 $T>\beta$。
故三根严格为 $\alpha<0<\beta<T$，$P$ 在 bounded oval。
在连通区间 $(h_+,\infty)$，三个简单实根可按大小连续标记，且没有一个能穿过零。
所以整个上区间均有 $r_1<0<r_2<r_3$，从而 $P\in C^1$。
这也直接核验 $\delta_T(1)=T(1+16T)>0$，未删除正常形缺图 $h=1$。

### Step 3. 奇异端点的实型及四阶点

把式 (1) 代入 (3) 给
$$
f_{h(w)}(u)=(u-w^2(w-1))^2(u+w^2/4).
$$
node 的切锥为 $Y^2=\kappa(u-u_0)^2$，其中
$\kappa=w^2(4w-3)/4\ne0$。
对 $w_-$，$\kappa<0$，所以该奇点是实孤立点，两切线非实；
对 $w_+$，$\kappa>0$，所以有两条不同实切线，是 split node。
这些局部实型不自行决定旋转数的端点常数。
另有可直接消费的解析接口：在 $h_0=h_-$，记 $r_0=-w_-^2/4$，则 $u_0<r_0<0$。
孤立 node 以外的实圆由 $u\ge r_0$ 加 $O$ 组成，与 node 有正的分离邻域。
由隐函数定理，simple root $r_0$ 延拓成实解析 $r(h)$，并写 $f_h(u)=(u-r(h))g_h(u)$。
在 $h_0$，$g_{h_0}(u)=(u-u_0)^2$，所以 $u\ge r(h)$ 上的 $g_h$ 在充分小的双侧邻域保持正。
这里在有界 $u$ 段使用严格正下界，在无穷端使用首项为 $u^2$，故该邻域可统一选择。
取 $s\in\mathbb R\mathbf P^1$，用 $u=r(h)+s^2$、$Y=s\sqrt{g_h(r(h)+s^2)}$ 参数化这个圆。
无穷端用 $1/s$ 图；不变微分 $\omega=du/(2Y)=ds/\sqrt{g_h(r(h)+s^2)}$ 在该图仍实解析且非零。
$P$ 对应 $s=\sqrt{-r(h)}>0$，故在这族紧圆上取向一致的完整周期 $\Omega>0$ 和选定 $O$ 到 $P$ 的局部积分提升均双侧实解析。
在端点 $\Omega(h_0)=\int_{-\infty}^{\infty}ds/(s^2+r_0-u_0)=\pi/\sqrt{r_0-u_0}$。
这个结论只提供没有实周期发散的局部接口，不在本件推导加权 twist 或零点结论。
任意正则 $h$ 上，$-P=(0,0)$ 处切线为 $v=0$，第三交点是 $(T,0)$，故 $2P=(T,0)$。
当 $h=1$ 时此点等于其负点且不是 $O$，故 $P$ 准确四阶，而不是二阶或仅阶整除四。

### Step 4. 原实曲面、实际平移及完整圆

原对象是 $F_T(x,y)=(T/(x-y),x/y)$，能级 $h=-x+y+x/y-T/x$。
采用 P30 已接受的原吹起曲面 $\mathcal U_T=S_T\setminus D$，不是另选的椭圆紧化。
其 finite fiber 完整、proper、连通且算术亏格一；原 $\mathcal U_T$ 覆盖为 torus 加四条完整 terminal affine lines。
原自主临界点计算给 $x=y^2$、$y^4-y^3-T=0$、$h=3y-2y^2$；
四 terminal 线的能级限制导数均非零（下表），没有额外有限临界点。
因此 $\delta_T(h)\ne0$ 时原完整纤维光滑；其连通性使它几何整，亏格为一。
在稠密开集上的实有理式及逆式是
$$
\phi(x,y)=\left(T/y,\ Tx(y-1)/y^2\right),\qquad
x=Tu/(T-hu-v),\quad y=T/u.
\tag{4}
$$
逐项代入原能级验证两式互逆并满足 $W_h$ 方程。
在每个正则实 $h$ 上，光滑射影曲线的双有理映射延拓定理使 (4) 唯一延拓为实同构。
这里不把旧限特征 $p>3$ 的固定概形定理直接引用成特征零定理，也不需要重审其厚度结论。
令 $m=(v-T)/u$，稠密开集上的弦切公式及原能级恒等式给
$$
\tau_P(u,v)=\bigl(m^2+hm+T-u,-(m+h)(m^2+hm+T-u)\bigr)
=\left(Ty/x,T^2y/x^2\right)=\phi F_T(x,y).
$$
原 $F_T$ 已在完整 $\mathcal U_T$ 上延拓为自同构；分离性使上述等式延拓到每个遗漏点。
故是准确 $+P$，不是未知倍点、负点或只在有限点集上的替代共轭。

用 $(a,b)$ 表示 terminal 局部坐标，以免与 Weierstrass $(u,v)$ 混淆：

| chart | $(x,y)$ | $a=0$ 时的能级 | 式 (4) 的完整像 |
|---|---|---|---|
| $1$ | $(a^{-1},1+ab)$ | $1-b$ | $(T,T(1-h))=-2P$ |
| $2$ | $(a(T+ab),a^{-1})$ | $b/T$ | $(0,0)=-P$ |
| $3$ | $(a(T+ab),a^2(T+ab))$ | $b/T$ | $O$ |
| $4$ | $([a(1+ab)]^{-1},a^{-1})$ | $1+b$ | $(0,T)=P$ |

charts $1,2,4$ 的有限像由代入后取 $a=0$ 得到；chart $3$ 的 $u\sim a^{-2}$、$v\sim-a^{-3}$，像为唯一无穷点 $O$。
每条线与每个 finite fiber 恰交一个实点，因此 torus 补集准确是这四点。
它们两两不同：$P$ 不是二阶，且 $2P$ 的横坐标 $T\ne0$ 排除三阶；$-2P$ 不可能为 $O$。
下外区间四点全在 $C^0$，故 $C^1$ 整圆留在原 torus；中区间唯一圆含全部四点。
上外区间 $O,-2P\in C^0$，$-P,P\in C^1$，所以每圆都含两个 terminal 点。
所有这些完整圆均包含在原开放曲面 $\mathcal U_T(\mathbb R)$ 内，并不接触被删除的 polar cycle $D$。

### Step 5. 实际回返及对旋转数接口的限度

实群 $W_h(\mathbb R)$ 的 identity component 是圆群，其他分支是其陪集。
平移保留群给出的圆定向；当有两分支时，陪集商是阶二群。
Step 2 的 $P$ 所在陪集因此逐项给出开头表：上区间交换分支，其第一次分支回返严格为 $F_T^2=\tau_{2P}$；其余是 $F_T=\tau_P$。
选一个正向实周期 $\Omega$ 后，分支回返的角度须用该 identity 圆上 $P$ 或 $2P$ 的积分模 $\Omega$ 表示。
尤其不能在上区间把跨两个分支的 $O$ 到 $P$ 复路径积分直接当作单圆回返旋转数。
在 torus 图上删除四个 terminal 点后，部分圆被切成开弧；通常的 affine 坐标可能在迭代中离图。
这不表示原合法轨道终止；也不表示每条单个轨道一定恰好击中 terminal 点。
完整圆动力与要求永不离开某个 affine 图的受限轨道，是不同问题。∎

## Remaining obligations and actual read scope

本件没有证明回返旋转数的端点极限、全局范围、单调性或 twist 零点数，也没有完成强先例查新。
所用正则回返表不包含两个 node 本身；$q=8h-9=0$ 的微分方程延拓亦仍需另证。
因此原 Q4 保持原量词与未闭合状态，不因这个必要接口可证就升级候选。
本人 FULL 读 proof-writer 技能；本地 PARTIAL 读旧 post-exact scope §3、nodal scalar Step 1、
P30 v4 §2 原四 chart／有限完整纤维段及 §3 finite critical lemma、旧 actual-singular Step 7、
旧 fixed-scheme-interface Step 1 的有理式与符号；不声称整份旧稿重审或外文来源新检索。
文件所有权只限本件；未改旧稿、索引、锁、FAIL 或接受产物，未作任何外部效力。

本地证明入口：[P30 原曲面](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex)、
[P30 critical lemma](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex)、
[原自主四 chart 临界检查](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md#step-7-自治-r1-的完全识别以及全阶剩余接口)、
[显式共轭式](PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md#step-1-实际原自治曲面上的显式带标记同构)。
