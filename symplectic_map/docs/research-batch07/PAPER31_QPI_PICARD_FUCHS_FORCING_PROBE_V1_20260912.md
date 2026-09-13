# Proof Package：原 qPI 截面的 Picard–Fuchs forcing 与全特征导数桥 V1

日期：2026-09-12 UTC。作者：`/root/p31_qpi_picard_fuchs_forcing_probe_v1`。
标签：`AUTHOR_PROOF`；`route_applicability: NOT_APPLICABLE`。
这是有界作者探查，不是 fresh 审查、正式候选、新意或长文容量票。

## Claim

保留原对象 $W_h:v^2+huv-Tv=u^3-Tu^2$、原指定截面 $P=(0,T)$，固定 $T\ne0$。
在保留标记的短式 $Y^2=f(X)=X^3+aX+b$ 中，令

$$
\begin{gathered}
s=h^2-4T,\quad q=8h-9,\quad H=32T+3h,\\
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T,\\
a=-\frac{s^2+24hT}{48},\qquad
b=\frac{s^3+36hTs+216T^2}{864},\\
X=u+s/12,\quad Y=v+(hu-T)/2,\quad (X_P,Y_P)=(s/12,T/2).
\end{gathered}
$$

本件证明两条准确接口，并只附所需的 Hasse 简单零引理：

1. 在特征零，令 $D=\partial_h$，局部选择 $I=\int_O^P dX/(2Y)$，则

   $$
   \boxed{\mathcal L I=-\frac{H}{q\delta}},\qquad
   \boxed{\mathcal L=D^2+\left(\frac{\delta'}\delta-\frac8q\right)D
   +\frac{8h^3-18h^2+9h-12T}{q\delta}}.
   \tag{PF}
   $$

2. 对每个代数闭域 $k$、$\operatorname{char}k=p>3$、$T\in k^\times$，
   对原已接受的 $\mu(P)$、$N_p=q^p\mu(P)$ 及 Hasse 多项式 $A$，有

   $$
   \boxed{\mu(P)'=-\frac{A H}{q^2}},\qquad
   \boxed{N_p'=-q^{p-2}AH}.
   \tag{pD}
   $$

   第二式是 $k[h]$ 中的恒等式，包含特殊时间 $T=-27/256$。
   在有限开集 $q\delta\ne0$，$A$ 的每个零点均为简单零。

## Status

`PROVABLE AS STATED`，仅指上述明列接口。原指定截面和固定时间未替换。
本件不将 $(\mathrm{PF})$ 直接模 $p$ 推广为椭圆积分定理，而另证 $(\mathrm{pD})$。
根重数与实际接触阶的后续消费者留给主控单独证明；本件不报告准确接触分类或三阶切触存在性。

## Assumptions / Notation

- 特征零计算首先在 $\mathbb Q(T,h)$ 上完成；积分解释取固定复数 $T\ne0$，
  在 $q\delta\ne0$ 的小解析邻域选路径及分支。不同分支相差周期，均由 $\mathcal L$ 消掉。
- $D$ 对 $h$ 微分、$DT=DX=0$，且 $DY=f_h/(2Y)$；$d_X$ 是相对微分。
  $f_h(P)$ 指先在固定 $X$ 下微分再评价，不是 $D(f(X_P))$。
- $\omega=dX/(2Y)$，$\omega_1=X\omega$；撇号用于系数或截面坐标的基方向全导数。
- 正特征沿用 [M] 中原 $A,M,L$ 的定义及 $\mu$ 源接口，不重证旧非零性、非 $p$ 可除性和素域充要性。
  下文写低次余项为 $L_{<}$，避免与 $\mathcal L$ 混淆。
- 本件的标量公式在函数域中成立；$q=0$ 是消去系数的退化，不能当作坏纤维判别式。

## Proof Strategy / Dependency Map

1. 两条多项式精确还原给 Gauss–Manin 矩阵及二阶 exact primitive。
2. 先证明组合 primitive 在 $O$ 正则且取零，再保留全部移动端点项，得到 $(\mathrm{PF})$。
3. 正特征对 $f^{(p-1)/2}$ 独立取系数；导出三个有限多项式恒等式，再微分原 $\mu$。
4. Hasse 引理只用第三步的相对导数恒等式及光滑 genus-one 曲线不存在单简单极点函数。

## Proof

### Step 1. 精确 Gauss–Manin 还原

定义

$$
\alpha=-\frac{\delta'}{12\delta},\quad \beta=-\frac q\delta,
\quad\gamma=\frac{a\beta}{3},\quad
\kappa=\frac{\beta'}\beta=\frac8q-\frac{\delta'}\delta,
\quad V=\alpha'+\alpha^2+\beta\gamma-\alpha\kappa.
$$

取

$$
r_0=2\alpha X-2\beta X^2-\frac43a\beta,\qquad
r_1=2\alpha X^2+\frac23a\beta X+2b\beta,\qquad R_j=\frac{r_j}{2Y}.
$$

直接对上述有理多项式展开得

$$
\begin{aligned}
-f_h&=2(\alpha+\beta X)f+2f(r_0)_X-f_Xr_0,\\
-Xf_h&=2(\gamma-\alpha X)f+2f(r_1)_X-f_Xr_1.
\end{aligned}\tag{G0}
$$

乘以 $dX/(4Y^3)$ 后，分别给

$$
D\omega=\alpha\omega+\beta\omega_1+d_XR_0,\qquad
D\omega_1=\gamma\omega-\alpha\omega_1+d_XR_1.
\tag{G1}
$$

可复核的系数关系为 $a'=-4a\alpha+6b\beta$、$b'=-6b\alpha-4a^2\beta/3$。
另由 $Y^2=f$ 逐项得 $R_1-XR_0=\beta Y$。不需要假设任何积分满足方程。
对第一式再微分并用第二式消去 $\omega_1$，得到

$$
(D^2-\kappa D-V)\omega=d_XQ,\quad
Q=(D+\alpha-\kappa)R_0+\beta R_1
=\frac{2VX-\beta a'}{2Y}-\frac{r_0f_h}{4Y^3}.
\tag{G2}
$$

最后一个等式来自 $r_0'+(\alpha-\kappa)r_0+\beta r_1=2VX-\beta a'$。
系数通分给 $-V=(8h^3-18h^2+9h-12T)/(q\delta)$，故该算子正是 $(\mathrm{PF})$ 中的 $\mathcal L$。

### Step 2. 无穷远端点与移动端点

在 $O$ 选局部参数 $t=X^{-1/2}$ 及符号 $Y=t^{-3}(1+at^4+bt^6)^{1/2}$。
这是局部解析坐标，给 $\omega=-(1+O(t^4))dt$，因此 $I$ 收敛。
但

$$
R_0=-\beta/t+\alpha t+O(t^3),\qquad R_1=\alpha/t+\gamma t+O(t^3).
$$

两项不能各自取 $R_j(O)=0$。在 $Q$ 中，极部系数准确为
$-\beta'-(\alpha-\kappa)\beta+\beta\alpha=0$；展开没有常数项，故 $Q(O)=0$。
也可由 $(\mathrm{G2})$ 的简式直接检查 $Q=O(t)$。
对收敛积分以固定 $X$ 下的 $D$ 两次应用 Leibniz 法则，得到

$$
\mathcal L I=Q(P)-Q(O)
+\frac{X_P''-\kappa X_P'}{2Y_P}
-\frac{2X_P'f_h(P)+(X_P')^2f_X(P)}{4Y_P^3}.
\tag{E}
$$

这与 [UV] Proposition 4.11 的 corrected endpoint 机制一致，微分规范为该源的一半。
特别不能因 $Y_P'=0$ 就把 $f_h(P)$ 删掉：$f_h(P)+f_X(P)X_P'=0$，两项不分别为零。
本点有 $X_P'=h/6$、$f_X(P)=-Th/2$、$Y_P=T/2$，所以 $(\mathrm E)$ 的移动项为
$-h^3/(36T^2)+(1-\kappa h)/(6T)$，而

$$
Q(P)=\frac{h^3}{36T^2}+\frac{\kappa h-1}{6T}-\frac{H}{q\delta}.
$$

相加即证明 $(\mathrm{PF})$，没有丢失边界项。

### Step 3. 与原 $B$ 的低阶代数接口

令 $u_P=X_P'/(2Y_P)$。由 [M] 已接受表达及本件坐标直接核对

$$
B=\frac{2h^2-3h-8T}{2q}
=\frac{u_P+R_0(P)}\beta,\qquad
\boxed{B'+(\alpha+\beta X_P)B+\beta Y_P=\frac H{q^2}}.
\tag{B}
$$

这些只是 $\mathbb Q(T,h)$ 上的有理恒等式；清分母后只需 $2,3$ 可逆。
因此对每个 $p>3$ 均可代数使用，而不调用特征零积分。
第二式乘以 $\beta$ 恰等于 $(\mathrm{PF})$ 的 forcing。

### Step 4. 正特征的独立系数证明

现在完全转到 $k(h)$、$\operatorname{char}k=p>3$，令 $m=(p-1)/2$ 并写

$$
F=f^m=X^pM(X)+AX^{p-1}+L_{<}(X),\qquad
\deg L_{<}\le p-2,\quad C=[X^{p-2}]F.
$$

在 $k$ 中 $m=-1/2$。所以 $2fF_X+f_XF=0$。
代入分解，仅看次数至少 $p$ 的部分：$X^pM$ 贡献
$X^p(2fM_X+f_XM)$，$AX^{p-1}$ 贡献 $AX^{p+1}$，
$L_{<}$ 仅贡献 $-CX^p$；其余次数小于 $p$。故

$$
2fM_X+f_XM=C-AX.
\tag{C1}
$$

由 $(\mathrm{G0})$，或把 $(\mathrm{G1})$ 乘以 $2Y^p$，得到另一个多项式恒等式

$$
F_h=(\alpha+\beta X)F+(r_0F)_X.
\tag{C2}
$$

取 $X^{p-1}$ 系数，导数项该系数为零；再取除以 $X^p$ 的多项式商，分别得

$$
\boxed{A'=\alpha A+\beta C},\qquad
M_h=(\alpha+\beta X+(r_0)_X)M+r_0M_X-\beta A.
\tag{C3}
$$

后一式中 $-\beta A$ 来自 $AX^{p-1}$；$L_{<}$ 因次数限制没有贡献。
设 $U=YM(X)$。由 $(\mathrm{C1})$、$(\mathrm{C3})$ 和 $(\mathrm{G0})$ 消去 $f_h$，逐项得

$$
2Y U_X=C-AX,\qquad U_h=r_0U_X-\beta AY.
\tag{C4}
$$

沿原指定截面求全导数，并用 $(\mathrm B)$，于是

$$
U(P)'=\beta(C-AX_P)B-\beta AY_P.
$$

原正特征接口准确是 $\mu(P)=U(P)+B^p-AB$；因 $(B^p)'=0$，有

$$
\begin{aligned}
\mu(P)'&=\beta(C-AX_P)B-\beta AY_P-(\alpha A+\beta C)B-AB'\\
&=-A\bigl[B'+(\alpha+\beta X_P)B+\beta Y_P\bigr]
=-\frac{AH}{q^2}.
\end{aligned}
$$

又 $(q^p)'=0$，即得 $(\mathrm{pD})$。由于 $p-2\ge0$，该清分母式在整个 $k[h]$ 成立。
这是每个实际 $p$ 的系数证明，无小素数归纳、采样或不可分积分假设。

### Step 5. 所需 Hasse 简单零引理

取 $h_*$ 满足 $q(h_*)\delta(h_*)\ne0$ 且 $A(h_*)=0$。
若同时 $C(h_*)=0$，$(\mathrm{C4})$ 意味着光滑闭纤维上 $d_X(YM)=0$。
在代数闭完美域上的一变量光滑函数域中，微分的核为其 $p$ 次幂子域；
这里 $X$ 是可分变量，因为 $Y^2=f(X)$ 的函数域扩张次数为 $2$，且 $p\ne2$。
于是 $YM=v^p$。
但 $M$ 是首一、次数 $(p-3)/2$，$X,Y$ 在 $O$ 的极阶分别为 $2,3$，
所以 $YM$ 仅在 $O$ 有极点且准确极阶为 $p$；$v$ 将仅有 $O$ 处的一阶极点。
genus-one Riemann–Roch 给 $\dim H^0(E,\mathcal O_E(O))=1$，排除这种非常数 $v$。
故 $C(h_*)\ne0$。由 $(\mathrm{C3})$，$A'(h_*)=\beta(h_*)C(h_*)\ne0$，引理成立。∎

## Corrections / Open Risks / 价值边界

- $\mathcal L\omega$ exact 不意味着 $\mathcal LI=Q(P)$；$(\mathrm E)$ 是不可删除的移动边界。
- 源 §4.10 的勘误警告已实际处理；未假设旧错误公式以消去 $f_h(P)$。
- 正特征的 $D(g^p)=0$ 会使一般微分阶推理失效；本件不把 $(\mathrm{pD})$ 自动报成全部根重数分类。
- $q=0$、坏纤维及无穷远不由 Hasse 简单零引理覆盖；多项式恒等式本身仍成立。
- 新增内容是原指定截面的准确 forcing 与同一 $N_p$ 的全 $p$ 导数约束。
  Griffiths–Dwork 还原、源 Manin 机制、系数比较与 Riemann–Roch 都是标准机制，应扣除。
  尚无 fresh 非作者核验；不预授非标准新意、独立长文价值或 22–30 页自然容量。

## 实读来源与实际验证

- 本人 FULL 读取 [M]，446 行，SHA-256 `48029bd31748637edaa6a9a123cd0d525406ea5b65f7eab53799606a5c97dbe2`。
- 本人 FULL 读取 [D]，176 行，SHA-256 `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a`。
- 本人 FULL 读取 `AGENTS.md`、`docs/WORKFLOW.md`、proof-writer 技能；批次入口仅读第 1–90 行。
- [UV] 为官方 HTML `2508.06680v1`；本次实际读取 §4.1–Proposition 4.11 证明末尾，
  重点完整读 §4.10–4.11 的勘误与端点证明（页面归一化行 541–584）；另核对 §2 原公式。
  不冒称全文或上游 Manin 原文实读。页面页头仍为 2025-08-08，正文 Date 为 2026-08-24；未解释日期差。
- 主作者实际用 SymPy 精确核验 $(\mathrm{G0})$ 两式、$R_1-XR_0$、算子常数项、
  $Q$ 分子、$B$ 端点、短 forcing 及完整端点 forcing 八项，通分结果全部为零。
  并行 `pf_algebra_aux` 另行核对 GM、$O$ 处组合极部及 forcing；它仅回消息、不写文件，属于作者辅助而非 fresh 票。
- proof-writer 技能使本件逐项陈述微分提升、量词与未证消费者；未触发额外暂停或权限扩大。
  唯一写入为本文件；没有新候选、锁、论文、编译、GPU、采样扩展、外发或旧记录改写。

[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[D]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[UV]: https://arxiv.org/html/2508.06680v1#S4.SS10
