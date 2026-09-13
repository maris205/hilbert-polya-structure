# Proof Package：原 qPI 准确局部厚度的全倍数合并推论 V1

日期：2026-09-12 UTC；作者：主控。
身份：AUTHOR_SYNTHESIS / NEW_CONSUMER_CHECK_REQUIRED。
route_applicability: NOT_APPLICABLE。
本件只合并本轮实际证明与已接受固定概形；不构成独立数学票、查新或完整候选准入。

## Claim

固定原自治族、标点与原基参数

$$
W_h:v^2+huv-Tv=u^3-Tu^2,\quad P=(0,T),\quad
O=[0:1:0],\quad z=h-h_*,
$$

$$
q=8h-9,\quad H=32T+3h,\quad
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T.
$$

令 $i_n=(nP.O)_{h_*}$，不相交时为零；所有长度在原 $z$ 上计算。
以下两部分的常数域量词不同，不将素域充分性扩张为一般代数闭域充分性。

### S1. 所有素域好点、所有正整数倍数

设 $p>3$、$T\in\mathbf F_p^\times$、$h_*\in\mathbf F_p$、$\delta(h_*)\ne0$。
令 $d=\operatorname{ord}P(h_*)$；它是原有限椭圆群中可确定的点阶，不是未知交数。
采用[M]的短式 $f(X)=X^3+a_4X+a_6$，记
$A=[X^{p-1}]f^{(p-1)/2}$，以及同一非零多项式 $N_p=q^p\mu(P)$。
定义以下只依赖闭点代数数据的整数：

$$
e_*=
\begin{cases}
0,&A(h_*)\ne0,\\
1+\mathbf1_{\{q(h_*)=0\}},&A(h_*)=0,
\end{cases}
\tag{1}
$$

$$
c_*=
\begin{cases}
1+\mathbf1_{\{q(h_*)=0\}},&p\mid d,\\
1,&p\nmid d,\ N_p(h_*)\ne0,\\
2+\mathbf1_{\{H(h_*)=0\}},&p\nmid d,\ N_p(h_*)=0.
\end{cases}
\tag{2}
$$

则 $c_*=i_d$，并且对全部 $n\ge1$，

$$
\boxed{
i_n=
\begin{cases}
0,&d\nmid n,\\[2pt]
p^a c_*+e_*\dfrac{p^a-1}{p-1},
&d\mid n,\quad a=v_p(n/d).
\end{cases}}
\tag{3}
$$

这是在规定全部素域好点上的准确交数公式，包含 $p\mid n$、超奇异好点和好点 $q=0$。
保留 $d$ 这个闭有限群输入，不声称给出其随所有 $T,h_*,p$ 的统一闭式；
但 (1)–(3) 不再以未知局部交数、未知导数 jet 或除法多项式零阶作为答案。

### S2. 所有代数闭正特征常数域的有限节点、所有倍数

设 $k$ 代数闭、$\operatorname{char}k=p>3$、$T\in k^\times$，$h_*$ 为有限节点。
从原唯一奇点按[NODE]取得 $w$：

$$
T=w^3(w-1),\quad h_*=w(3-2w),\quad w\ne0,1,3/4.
$$

取 $(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0$ 的任意根。
对 $n=p^a m$、$p\nmid m$，令

$$
j_n=
\begin{cases}
0,&\zeta^m\ne1,\\
2p^a,&\zeta^m=1,\ p>5,\ (T,h_*)=(3/16,-2),\\
p^a,&\zeta^m=1,\ (T,h_*)\ne(3/16,-2).
\end{cases}
\tag{4}
$$

则 $i_n=j_n$。特征 $5$ 的所列例外是尖点，已不在当前节点域。
这部分没有素域参数限制，也不假设 $k^\times$ 的全部元素都是根单位。

### S3. 原完整固定概形的实际消费者

沿用[FIX]已接受同基底同构 $\mathcal U\simeq W$ 及
$\phi F_T=\tau_P\phi$，其中

$$
\phi(x,y)=\left(\frac Ty,\frac{Tx(y-1)}{y^2}\right),\qquad
F_T(x,y)=\left(\frac T{x-y},\frac xy\right).
$$

对 S1 中任一好点，在该整个纤维的形式邻域上准确有

$$
\mathcal I_{\operatorname{Fix}(F_T^n)}=(z^{i_n})\mathcal O_{\widehat{\mathcal U}_{h_*}},
\tag{5}
$$

其中 $i_n$ 由 (3) 给出，$i_n=0$ 时右侧是单位理想。
对 S2 中任一节点，在原节点处选择 $z=\xi\eta$ 的完成坐标，则

$$
\boxed{\widehat{\mathcal I}_{\operatorname{Fix}(F_T^n)}
=z^{j_n}(\xi,\eta)\subset k[[\xi,\eta]].}
\tag{6}
$$

节点纤维的其余光滑点处为 $(z^{j_n})$。
故 $j_n=0$ 时只剩约化孤立节点；$j_n>0$ 时是厚度 $j_n$ 的 Cartier 纤维，
并在节点有长度一的嵌入部分，仍由同一原基 $z$ 作用。
这些完整理想是既有[FIX]与新标量公式的直接合成，不另计第三个非标准结构定理。

## Status, assumptions and dependency map

PROVABLE AS STATED，指 S1–S3 的作者推论；新上游证明的独立接受须另由主控处置记录。
新[G]/[C]/[PP]/[NODE]在本件写成时处于本轮独查流程，不能用本件反向代签它们。
沿用已接受[M]/[PF]/[FIX]的原对象身份、泛 $P$ 非挠性及原好模型；
不修改任一旧作者稿、旧审查或旧失败。

1. [C] C3及[PP] P1分别给 (2) 的互补分支。
2. [C] C4给原短模型 Hasse 系数的准确零阶 (1)。
3. 下文只补核 Hasse 与形式 $[p]$ 系数的同规范身份及标准传播适用性，得到 (3)。
4. [NODE]的全部节点公式就是 (4)，不在本件重证其 Taylor 系数。
5. [FIX] 的已接受完整理想代入所得标量，得到 (5)–(6)。

## Proof

### Step 1. 初始交数及形式 Hasse 系数

[C] C3 给 (2) 的 $p\nmid d$ 两支；[PP] P1 给 $p\mid d$ 一支，故 $c_*=i_d\ge1$。
其中 $p\mid d$ 必有 $A(h_*)=1$，所以该支 $e_*=0$；
超奇异纤维上没有非零几何 $p$ 挠点，也不会误用该支。
由[C] C4，$e_*=\operatorname{ord}_z A$ 且 $0\le e_*\le2$。

现核定这个 $A$ 正是所用正规形式参数的 $p$ 次项系数。
在短模型中固定 $t=-X/Y$，不变微分写为
$\omega=dX/(2Y)=\sum_{j\ge0}b_jt^jdt$，$b_0=1$。
相对 Cartier 计算从
$\omega=\frac12Y^{-p}f^{(p-1)/2}dX$ 给出
$C(\omega)=A^{1/p}\omega$；可先扩张泛系数域至完美闭包作此计算。
因为 $f^{(p-1)/2}$ 的次数小于 $2p-1$，只有其 $X^{p-1}$ 项贡献。
在形式 $t$ 展开比较常数项，得到 $b_{p-1}=A$，再由忠实域扩张返回原系数域。

形式群对数也可精确识别同一个系数。将通用好短模型提升到
$\mathbf Z_{(p)}[a_4,a_6,\Delta^{-1}]$，写
$\log_{\widehat E}(t)=t+\sum_{j\ge1}b_jt^{j+1}/(j+1)$。
在次数小于 $p$，全部分母与 $p$ 互素，故 $[p](t)$ 的这些系数都被 $p$ 整除。
在恒等式 $\log([p](t))=p\log(t)$ 的 $t^p$ 系数中，
$2\le j+1<p$ 的组合项均被 $p$ 整除；
对数的 $t^p/p$ 项在左侧贡献也含 $p^{p-1}$。
所以约化后 $[t^p][p](t)=b_{p-1}=A$。
这是通用形式群与 Cartier 的标准身份，本件只核对原规范，不申报新意。

最后，特征 $p$ 中 $[p]=V\circ F$；原短参数经相对 Frobenius 变为 $t^p$。
因此在整系数环 $R=\overline{\mathbf F}_p[[z]]$，

$$
[p](t)=At^p+\sum_{r\ge2}a_rt^{rp},\qquad a_r\in R.
\tag{7}
$$

原广义模型的 $-u/v$ 与 $t$ 生成同一个零截面理想；其线性变换是单位，不改变此处交数。

### Step 2. 全部倍数的标准传播

对任意 $f\in zR$、$b=\operatorname{ord}_z f\ge1$，
(7)第一项的阶为 $e_*+pb$，其余项的阶至少为 $2pb$。
由于 $e_*\le2<p\le pb$，前者严格更小，不会发生首项抵消：

$$
\operatorname{ord}_z[p](f)=e_*+p\operatorname{ord}_z f.
\tag{8}
$$

这一步允许闭纤维超奇异；不能把 $A$ 非零的泛普通性误写成所有闭纤维普通。
若 $r$ 与 $p$ 互素，则 $[r](t)=rt+O(t^2)$ 保持正赋值。
原有限群中 $nP(h_*)=O$ 当且仅当 $d\mid n$。
对相交分支写 $n=drp^a$、$p\nmid r$，从 $i_d=c_*$ 迭代 (8)，得到

$$
i_n=p^ac_*+e_*(1+p+\cdots+p^{a-1}).
$$

$a=0$ 时空和为零，故准确成为 (3)。
该传播已有[N] Lemma 8.2；原好模型最小、泛普通、$P$ 非挠，
且本处 $h_{E,v}=e_*\le2<p-1$（对 $p=5$ 仍成立），符合其低 Hasse 阶分支。
以上自足低阶比较用于核定适用性，不将文献一般传播记作本轮原创。

### Step 3. 节点与原完整理想

[NODE]证明 (4)，使用二次根只是取原指定点乘法坐标或其逆。
其固定 $T$ 的参数比较已证明与原 $z$ 无分歧，故数值可直接消费，不能再乘一个猜测分歧指数。
在节点，原总空间正则、有限纤维为简单节点，故[FIX]允许完成坐标 $z=\xi\eta$。
若先得到 $z=u\xi\eta$、$u$ 为单位，吸收单位到一支即给该式；原基 $z$ 本身未改。

[FIX]已接受半稳定基上的
$\mathcal I_{\rm Fix}=f^*\mathcal I_{(nP)^*O}\operatorname{Fitt}_1\Omega^1_{\mathcal U/C}$。
好点处 Fitting 因子是单位，节点处是 $(\xi,\eta)$，
而 $(nP)^*O$ 的局部理想是 $(z^{i_n})$。代入 (3)或(4)得 (5)–(6)。
节点 $j_n>0$ 的长度一嵌入部分由
$(z^{j_n})/(z^{j_n}(\xi,\eta))\simeq k$ 直接给出。
没有把节点存在本身错误判为 $nP$ 已在光滑群中回到 $O$。∎

## Boundaries and novelty deduction

- S1 是所有素域好点的全倍数结果，不是所有闭点度数、所有扩域或整个 $\mathbb A^1_{\overline{\mathbf F}_p}$ 的好点分类。
- S2 覆盖一般代数闭正特征域的全部有限节点；不能因为 S1 较窄而把 S2 也缩到素域。
- 尖点 $T=-27/256,h=9/8$、无穷远、$T=0$、非自治有限阶回返的整个原 torsor 上相对作用，不在 S1–S3。
- 特征零或一般正特征域中，真实 prime-to-characteristic 好切触阶仍由[C]给出准确 $2/3$，但本件未定位全部真实发生处。
- 旧F5证书未扩样；(3) 是证明的消费者，不是从 F5 表猜出的公式。
- 原曲线模型、指定点、形式群、Tate参数、Igusa/Manin/PF通用方法及固定理想均扣除；
  本轮潜在新增为原截面初始阶的实际确定，是否足够长文须独立评价。
- 未声称三阶好切触有实例；条件 $N_p=H=0$ 是准确判据而不是存在性证书。

## Actual reading and verification

主控本轮本人FULL读取四新作者[G]267／[C]281／[PP]254／[NODE]346行，
以及旧[PF]325、[M]446、前轮接受176、组合基线121与碰撞图107行；
[FIX]本轮消费既有完整数学接受及前轮已FULL核准的348行作者和297行独查。
[N]本人实读官方PDF pp.1003–1005，含 Lemma 8.2 完整陈述与证明。
UV本人实读 §§2–3；未继承任一代理所列其它外文的FULL身份。
本件的新消费者论证为上文书面证明，未运行新采样或冒称执行代理CAS。
proof-writer用于保持两种量词、明确上游独查状态并展开标准传播的实际前提。
仅新增本件；不改冻结原件、锁、索引或接受产物，无编译、GPU或外部效力。

[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[PP]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[NODE]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[N]: https://nyjm.albany.edu/j/2016/22-46v.pdf
