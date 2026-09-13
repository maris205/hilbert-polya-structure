# Proof Package：原 qPI 好纤维的准确低阶切触与素域初始交数 V1

日期：2026-09-12 UTC。作者：主控 `/root`。
标签：`AUTHOR_PROOF / NEW_FORCING_CONSUMER`；`route_applicability: NOT_APPLICABLE`。
本件消费新作者[G]的全特征导数桥，尚须与该输入一起经 fresh 数学审查；不是论文准入或数学接受处置。

## Claim

保持原带标记曲线和原基参数

$$
W_h:v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad O=[0:1:0],\qquad z=h-h_*.
$$

固定非零时间 $T$，记

$$
q=8h-9,\quad H=32T+3h,\quad
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T,\quad t_O=-u/v.
$$

有限好点是 $\delta(h_*)\ne0$。令 $i_n=(nP.O)_{h_*}$，不相交时取零。
交数在原 $z$ 上计算，不作分歧重新计量。本件证明以下四项。

**C1：全部代数闭正特征域上的 Manin 根重数。**
若 $\operatorname{char}k=p>3$、$T\in k^\times$，在 $q\delta\ne0$ 处令
$e_* =\operatorname{ord}_{h_*}A\in\{0,1\}$，其中 $A$ 是原短式的 Hasse 系数。
同一已接受多项式 $N_p$ 的每个根都满足

$$
\boxed{\operatorname{ord}_{h_*}N_p=1+e_*+\mathbf1_{H(h_*)=0}\le3.}
\tag{R}
$$

**C2：全部真实 prime-to-characteristic 好纤维切触。**
取代数闭 $k$，特征零或特征 $p>3$；取 $n\ge1$，正特征时要求 $p\nmid n$。
对每个有限好点，若 $i_n>1$，则 $q(h_*)\ne0$，且

$$
\boxed{i_n=2+\mathbf1_{H(h_*)=0}.}
\tag{I}
$$

不仅有界，而且原指定局部参数的首项准确为

$$
\boxed{
t_O(nP)=
\begin{cases}
-\dfrac{nH(h_*)}{2q(h_*)\delta(h_*)}z^2+O(z^3),&H(h_*)\ne0,\\[4pt]
-\dfrac{n}{2q(h_*)\delta(h_*)}z^3+O(z^4),&H(h_*)=0.
\end{cases}}
\tag{J}
$$

这并不说一般代数闭域中每个 $N_p$ 根都是真实切触；(I)–(J) 的前提是实际 $i_n>1$。
特征零也没有由这两个公式决定全部切触位置或断言三阶点必存在。

**C3：素域 prime-to-$p$ 初始交数的准确公式。**
若 $T\in\mathbf F_p^\times,h_*\in\mathbf F_p$ 且 $\delta(h_*)\ne0$，令 $d=\operatorname{ord}P(h_*)$。
当 $p\nmid d$ 时，

$$
\boxed{
i_d=
\begin{cases}
1,&N_p(h_*)\ne0,\\
2,&N_p(h_*)=0,\ H(h_*)\ne0,\\
3,&N_p(h_*)=0,\ H(h_*)=0.
\end{cases}}
\tag{F}
$$

对全部 $p\nmid n$，$d\nmid n$ 时 $i_n=0$，$d\mid n$ 时 $i_n=i_d$；若 $p\mid d$，此类 $n$ 全不相交。
原有限群点阶 $d$ 没有在本件被求成统一闭式；新增输出是初始交数和切触首项，不再把未知 $i_d$ 当答案。

**C4：所有有限好点的 Hasse 零阶。**
正特征时 $A(h_*)=0$ 的每个好点准确有

$$
\boxed{\operatorname{ord}_{h_*}A=1+\mathbf1_{q(h_*)=0}.}
\tag{A}
$$

本件不据此自行宣布 $p$ 倍回返已经分类；这是后续标准形式群传播所需的实际系数输入。

## Status

`PROVABLE AS STATED`，针对 C1–C4 的准确量词；当前为作者证明。
新[G]尚未由独立审查接受，所以本件不继承一个不存在的上游数学 PASS。

## Assumptions and notation

- 只消费原曲线、原 $P$ 泛非挠性和原基身份的既有接受；$nP\ne O$ 泛成立，故局部交数有限。
- 沿用[M]的短式 $X=u+(h^2-4T)/12$、$Y=v+(hu-T)/2$，$Y^2=X^3+aX+b$。
  记 $w=-X/Y$；在 $O$ 附近 $w=t_O+O(t_O^2)$，故二者沿任何相交截面的首非零系数相同。
- 正特征中 $\mu(Q)$ 为[M]的加法同态；$N_p=q^p\mu(P)$。
  对当前 $p$ 写
  $$
  (X^3+aX+b)^{(p-1)/2}=X^pM+AX^{p-1}+L_{<},\qquad C=[X^{p-2}]L_{<}.
  $$
- 记 $\beta=-q/\delta$、$\alpha=-\delta'/(12\delta)$；星号表示在 $h_*$ 评价。
  在 $q\delta\ne0$ 上 $\lambda=\beta\,dz$ 是单位微分。
- [G]新证明的实际输入为 $\mu(P)'=-AH/q^2$、$A'=\alpha A+\beta C$，
  以及光滑闭纤维上 $A=C=0$ 不可能；不是从有限表推定这些恒等式。

## Proof strategy and dependency map

1. 新导数式的低阶非零项先消除特征 $p$ 的导数失明问题，给 C1。
2. 将原 Manin 消去精确到 $w$ 的线性项：普通点与超奇异点分别给不同阶。
3. C1 和局部下界先把实际交数压到小于 $p$，再读首项；不循环假设 $p\nmid i_n$。
4. 特征零使用[G]的完整非齐次 Picard–Fuchs 式及周期被消去，得到相同首项。
5. 只有素域 C3 使用前轮已接受的充分性[PF]；C4由同一 Gauss–Manin 恒等式在 $q=0$ 再微分。

## Proof

### Step 1. 先证明根重数，不能直接对最低项除以其指数

取正特征、$q_*\delta_*\ne0$、$N_p(h_*)=0$。新[G]证明此处 $A$ 的零阶 $e_*$ 为 $0$ 或 $1$。
因 $H'=3\ne0$，$H$ 的零阶是 $\epsilon_*=\mathbf1_{H_*=0}\in\{0,1\}$。
故

$$
\operatorname{ord}_z\mu(P)'=e_*+\epsilon_*=:j\in\{0,1,2\}.
$$

写 $\mu(P)=\sum_{r\ge1}c_rz^r$；常数项确实为零，因为 $q_*$ 非零且 $N_p(h_*)=0$。
导数的首项说明 $c_1=\cdots=c_j=0$、$(j+1)c_{j+1}\ne0$。
这里 $j+1\le3<p$，所有这些指数可逆，且不可能有更低的正 $p$ 倍指数项。
所以 $\operatorname{ord}\mu(P)=j+1$。$q^p$ 为单位，得到 (R)。
这一步明确排除了先有 $z^p$ 隐藏首项的可能，而非无条件使用 $\operatorname{ord}f'=\operatorname{ord}f-1$。

### Step 2. 原 Manin 消去的准确局部首项

仍取 $q_*\delta_*\ne0$，令 $Q=nP$ 且 $i=i_n\ge2$。
写 $w(Q)=c z^i+O(z^{i+1})$、$c\ne0$。原短模型的整展开是

$$
X=w^{-2}+O(w^2),\qquad Y=-X/w=-w^{-3}+O(w).
$$

由 $w^2X^3-X^2+aw^2X+bw^2=0$ 逐阶解得这些展开，系数均在 $k[[z]]$。
对系数同时取基方向导数，仍有

$$
\frac{dX(Q)}{2Y(Q)}=(1+O(w^4))w'(Q)\,dz+O(w^5)\,dz.
\tag{D1}
$$

因为 $X$ 的负阶唯一项 $w^{-2}$ 的系数固定为一，基系数导数的最早贡献来自 $O(w^2)$，除以 $Y$ 后至少为 $O(w^5)$。
定义

$$
D_Q=\frac{dX(Q)/(2Y(Q))}{\lambda},\qquad
E_Q=\frac{(d\Delta/\Delta)X(Q)}{12\lambda Y(Q)},\qquad \Delta=T^3\delta.
$$

[M]已核定的完整消去为

$$
\mu(Q)=R_Q+\wp_A(D_Q)-\wp_A(E_Q),\qquad \wp_A(x)=x^p-Ax,
$$

$$
R_Q=\wp_A\left(\frac{aX+3b}{3XY}\right)-\frac{YL_{<}(X)}{X^p}.
\tag{D2}
$$

在整形式环中，右侧准确有 $R_Q=Cw+O(w^3)$；第一项的内部量阶至少三，
第二项的最高 $X$ 次幂 $CX^{p-2}$ 给 $-CY/X^2=Cw+O(w^5)$，其余给至少 $w^3$。
此外 $\operatorname{ord}D_Q\ge i-1$、$\operatorname{ord}E_Q\ge i$。
因此普通点 $A_*\ne0$ 时 $\operatorname{ord}\mu(Q)\ge i-1$；
超奇异点 $A_*=0$ 时，因 $\operatorname{ord}A=1$，每一项的阶至少为 $i$。
此处使用 $p(i-1)\ge i$（$i\ge2,p>3$），不要求 $p\nmid i$。

### Step 3. 正特征的准确交数与统一首项

由于 $p\nmid n$，$\mu(Q)=n\mu(P)$ 的阶等于 $\mu(P)$ 的阶。
切触必要性[M]给 $N_p(h_*)=0$。若 $A_*\ne0$，(R) 的阶是 $1+\epsilon_*$，
Step 2 给 $i\le2+\epsilon_*\le3$；若 $A_*=0$，(R) 的阶是 $2+\epsilon_*$，
Step 2 同样给 $i\le2+\epsilon_*\le3$。所以现在才得到 $i<p$。

普通点中，(D1)–(D2) 的唯一最低项为 $-AD_Q$，故

$$
\mu(Q)=-\frac{A_* i c}{\beta_*}z^{i-1}+O(z^i).
\tag{D3}
$$

超奇异点中，设 $a_1=A'(h_*)\ne0$。由[G]的 $A'=\alpha A+\beta C$，$C_*=a_1/\beta_*$。
在次数 $i$，$R_Q$ 和 $-AD_Q$ 之和给

$$
\mu(Q)=\frac{(1-i)a_1c}{\beta_*}z^i+O(z^{i+1}).
\tag{D4}
$$

$D_Q^p$ 的阶为 $p(i-1)>i$，而 $\wp_A(E_Q)$ 的阶至少 $i+1$，没有漏掉同阶项。
$i=2$ 或 $3$，所以 (D3)–(D4) 的所列系数非零。与 (R) 比较，两种约化都给 $i=2+\epsilon_*$。

为读出 $c$，直接展开新导数式 $\mu(P)'=-AH/q^2$。四种情况依次为

| 状态 | $\mu(P)$ 的首项（已知常数项为零） |
|---|---|
| $A_*\ne0,H_*\ne0$ | $-A_*H_*z/q_*^2$ |
| $A_*\ne0,H_*=0$ | $-3A_*z^2/(2q_*^2)$ |
| $A_*=0,H_*\ne0$ | $-a_1H_*z^2/(2q_*^2)$ |
| $A_*=0,H_*=0$ | $-a_1z^3/q_*^2$ |

用 $\mu(Q)=n\mu(P)$ 分别代入 (D3)–(D4)，都得到
$c=n\beta_*H_*/(2q_*^2)$（$H_*\ne0$），或 $c=n\beta_*/(2q_*^2)$（$H_*=0$）。
再用 $\beta_*=-q_*/\delta_*$ 及 $w=t_O+O(t_O^2)$，得到 (J)。

唯一 $q_*=0$ 的好点是 $h_*=9/8$、$256T+27\ne0$；[M]已证明那里不存在 prime-to-$p$ 切触。
它没有被当作坏纤维删除，故正特征 C2 覆盖全部有限好点。

### Step 4. 特征零的同一交数和首项

先在复数上工作。在实际相交点附近，令 $J_Q=\int_O^Q\omega$ 取在 $O$ 邻域的小分支。
若 $w(Q)=c z^i+\cdots$，则 $J_Q=c z^i+O(z^{i+1})$，因为 $\omega=(1+O(w^4))dw$。
局部 $J_Q$ 与 $n\int_O^P\omega$ 之差是周期；[G]证明 $\mathcal L$ 杀掉周期并保留全部移动端点，故

$$
\mathcal L J_Q=-\frac{nH}{q\delta}.
\tag{D5}
$$

若 $q_*\ne0$ 且 $i\ge2$，$\mathcal L$ 的其余系数正则，左侧最低项是
$i(i-1)c z^{i-2}$。右侧在 $H_*\ne0$ 时为非零常数，在 $H_*=0$ 时首项是 $-3nz/(q_*\delta_*)$。
于是分别得到 $i=2,c=-nH_*/(2q_*\delta_*)$ 与 $i=3,c=-n/(2q_*\delta_*)$。

若 $q_*=0$ 而 $\delta_*\ne0$，把 (D5) 乘以 $q$。所得方程两边在该好点都正则，且

$$
qJ_Q''+(q\delta'/\delta-8)J_Q'
+\frac{8h^3-18h^2+9h-12T}{\delta}J_Q=-\frac{nH}{\delta}.
$$

假如 $i\ge2$，左侧在 $z=0$ 为零；右侧不为零，因为
$H_*=(256T+27)/8$、$\delta_*=(256T+27)^2/4096\ne0$。矛盾，因此该点无切触。
一般代数闭特征零域的结论由有限生成子域嵌入 $\mathbb C$ 得到：实际 $nP$ 坐标及交数由
有限多个有理表达及 $T,h_*$ 决定，嵌入保持其零阶。故 C2 在所列特征零量词也成立。

### Step 5. 素域初始交数与 Hasse 的唯一二重零位置

在 C3 的范围，前轮[PF]已证明 $N_p(h_*)=0$ 当且仅当 $p\nmid d$ 且 $i_d>1$。
对 $p\nmid d$，$dP(h_*)=O$，所以非零 $N_p$ 给 $i_d=1$；零值由 C2 给准确 $2$ 或 $3$。
有限群阶判据和 prime-to-$p$ 形式群线性项给所列全部允许 $n$，得到 (F)。
没有把这个充分方向外推到一般代数闭域或扩域。

最后证明 C4。在任意好点 $A_*=0$，[G]的 Riemann–Roch 论证给 $C_*\ne0$，不要求 $q_*\ne0$。
若 $q_*\ne0$，$A'_* =\beta_*C_*\ne0$，零阶为一。
若 $q_*=0$，$\beta_* =0$ 而 $\beta'_*=-8/\delta_*\ne0$。
先用 $A'=\alpha A+\beta C$ 得 $A'_* =0$，再微分得 $A''_* =\beta'_*C_*\ne0$。
因 $2$ 可逆，零阶准确为二，证明 (A)。∎

## Corrections and open boundaries

- 精细下界本身已有[UV] Remark 2.4；本件的准确低阶结论消费新原 forcing/导数式，不能把旧下界再算新理论。
- 普通点的 $\operatorname{ord}N_p=i_d-1$ 与超奇异点的 $\operatorname{ord}N_p=i_d$ 仅在实际切触时成立；
  不能对一切 $i_d=1$ 的代数闭域点沿用。这是根重数与交数间不可省略的区别。
- 一般域中 $N_p=0$ 仍可能是横截或无 prime-to-$p$ 回返的零值；本件未排除。
- 三阶真实切触在素域由 (F) 判定，但尚未在本件给出实现它的具体素数／时间；不把候选线 $H=0$ 当作存在性证明。
- $p\mid d$ 的初始交数、$p\mid n$ 的传播、节点、尖点、无穷远及完整固定理想不在本件证明范围。
- C2不等于关闭旧特征零I03的全部能级／点阶异常谱；它确定实际切触的阶和首项，不定位全部发生处。
- 原[G]与本件均待独立核验；未授长文新意、价值、容量或完整候选 PASS。

## Actual reading and verification boundary

主控本人 FULL 读取新[G]267行、旧[M]446行、旧[PF]325行及前轮接受176行；
当前碰撞图107行与组合基线121行亦实际读取，只消费所列已接受结果，不重开旧证明。
[UV] 本人实际读取官方HTML §§2–3；Remark 2.4的界和Definition 3.4的更广局部 $p$ 可除接触量保持不同身份。
新[G]的八项CAS核验属于其作者侧，本件不冒称主控执行了那些调用或继承其全部外文阅读。
本件首项由(D1)–(D5)书面逐项推出；旧F5三项首系数与(J)相容不作为一般证明依赖，没有扩展其锁定采样。
proof-writer用于固定原量词、消除低于 $p$ 之前的循环推理，以及保留尚未定位的三阶存在性边界。
唯一新增本文件，使用apply_patch；冻结原件、旧接受／失败、项目锁和索引不改。无编译、GPU、投稿、上传或其他外部效力。

[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S2
