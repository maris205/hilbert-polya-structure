# Paper31 D05 后续：原全次数自由格的留数识别与整数控制引理 V1

日期：2026-09-09 UTC。作者席：`/root/p31_qpi_novelty_cd_i01_i03_v1`。
本件是新的有界作者证明，不是 D05 独立审查、正式新意票或论文准入。纯理论 GPU 0；没有运行 CPU 矩阵核验或扩大次数扫描。
仅新增本文；D01 两件、D05 作者及独查、旧接受稿与索引全部保持冻结。

## Claim

固定原 $q=1,R=\mathbb Z[\tau]$，保持已接受的四图、受限源 $V_n$、目标 $W_n$、矩阵 $J_n$ 及原截面

$$
s_0=xy,\qquad s_1=x^2-x^2y+xy^2-\tau y.
$$

令

$$
M_n=\operatorname{coker}J_n,\quad
T_n=\ker\bigl(M_n\longrightarrow M_n[\tau^{-1}]\bigr),\quad
L_n=M_n/T_n,\quad R^\circ=R[\tau^{-1}].
$$

$L_n$ 是原余核的无扭商格，不预设它在 $R$ 上自由。对 $n\ge1$、$0\le a\le n-1$，定义**具体整数理想**

$$
\mathcal I_{n,a}
=\left(\binom{n-1-b}{a}\tau^b:0\le b\le n-1-a\right)\subset R.
\tag{I}
$$

本包证明一条带实际坐标的全次数格控制引理。

**G1：原余核与实际格像。** 下文由原图、原截面和原反典范标架定义的留数映射

$$
\rho_n:W_n\longrightarrow (R^\circ)^n
$$

满足 $\rho_n J_n=0$，诱导同构 $M_n[\tau^{-1}]\simeq(R^\circ)^n$，并且

$$
\ker(M_n\xrightarrow{\rho_n}(R^\circ)^n)=T_n,\qquad
\rho_n(M_n)=\bigoplus_{a=0}^{n-1}\tau^{-n}\mathcal I_{n,a}\,e_a.
\tag{G}
$$

因此 $\widetilde\rho_n=\tau^n\rho_n$ 给出指定的 $R$-模同构

$$
L_n\xrightarrow{\sim}\bigoplus_{a=0}^{n-1}\mathcal I_{n,a}.
\tag{G'}
$$

**G2：原次数连接，不丢移位。** 对乘原 $s_0$ 诱导的 $\iota_n:M_n\to M_{n+1}$，有严格身份

$$
\rho_{n+1}\iota_n(c)=(0,\rho_n(c)_0,\ldots,\rho_n(c)_{n-1}),
\tag{S}
$$

所以在 (G') 的具体理想坐标中，$L_n\to L_{n+1}$ 为 **$\tau$ 倍右移**。特别地，实际自由格商为

$$
\frac{L_{n+1}}{\iota_n(L_n)}
\simeq R\oplus\bigoplus_{a=1}^{n}
\frac{\mathcal I_{n+1,a}}{\tau\mathcal I_{n,a-1}}.
\tag{Q}
$$

**G3：指定归一化的双对偶缺陷。** 在 (G') 的坐标中，各 $\mathcal I_{n,a}^{**}=R$，从而

$$
E_n:=L_n^{**}/L_n\simeq
\bigoplus_{a=0}^{n-1}R/\mathcal I_{n,a}.
\tag{D}
$$

右端是有限阿贝尔群。局部化到每个 $A=R_{(p,\tau)}$ 后，它给原自由格的实际有限长缺陷，不是未绑定的关联分次影子。

本件不声称 $M_n\simeq T_n\oplus L_n$，也不把各 $\mathcal I_{n,a}$ 或旧 $P_m$ 称为原 $M_n$ 的直和块。原全部扭子块、Fitting 与所有素数首次消费者不在本 Claim 中；(G)–(D) 给这些消费者所需的新接口。

## Status

`PROVABLE AS STATED`：指上述具体原自由格、原次数连接和指定双对偶缺陷；作者证明已闭合，尚待非作者针对本件新桥梁核验。

此处没有把 $2\sum R/(\tau^j)$ 的商扭子直接当成原扭子增量，也没有用逐域 Smith 或有限次数样本猜全次数式。
证明的非标准绑定是原反典范标架、四中心的完整留数和及原坏图的整数坐标正规形；全局留数定理本身是标准工具，应在新意判断中扣除。

## Assumptions

1. 按已接受原实际复形 [JET]，$Y/R$ 是先做四次 toric 节点吹起的原曲面，$\mathscr L=\omega_{Y/R}^{-1}$，$V_n=H^0(Y,\mathscr L^n)$，$W_n$ 为四个末次原中心的 $n$-fat jets。
2. 使用已通过独查的 [D05] T1–T2。特别是 $M_n[\tau^{-1}]$ 在 $R^\circ$ 上自由秩 $n$；这里只消费这一已证明后果，不消费旧未独审 W1–W3。
3. 只为定义分式坐标与识别自由余核而暂时到 $R^\circ$。最终格、坐标替换与 (I) 均在原 $R$ 上明确给出；从未反演整数素数。
4. 采用连续形式幂级数及其有限 fat-jet 商。每个固定 $n$ 的计算仅需总次小于 $n$ 的系数；不存在无限提升参数或未定义的旧类识别器。
5. 全局留数和只在特征零的紧复曲面上使用一次来证明一个 $R^\circ$ 系数恒等式。随后通过 $R^\circ$ 的注入性返回整数身份，不将复分析定理直接宣称为任意非平坦基变换定理。

## Notation

令 $A_n=R[u,v]/(u,v)^n$，$W_n=A_n^{\oplus4}$；$A_0=0$、$M_0=L_0=0$。
保持原单项式源

$$
\Lambda_n=\{(i,j):0\le i,j\le2n,\ n+i-j\ge0,\ i+j\ge n,\ i+2j\ge2n,\ i+j\le3n\}.
$$

对 $x^iy^j\in V_n$，四个原局部系数为

$$
\begin{aligned}
Q_{1,n}&=u^{2n-i}(1+v)^j,& Q_{2,n}&=u^{n+i-j}(\tau+v)^i,\\
Q_{3,n}&=u^{i+2j-2n}(\tau+v)^{i+j-n},&
Q_{4,n}&=u^{3n-i-j}(1+v)^{2n-i}.
\end{aligned}
\tag{J}
$$

写 $F_r=Q_{r,1}(s_0)$、$G_r=Q_{r,1}(s_1)$；$F,G$ 则是各图用于留数提取的共同形式变量。
令 $N=n-1$，$e_a$ 是 $(R^\circ)^n$ 中以 $F^aG^{N-a}$ 标记的标准向量。
$\Delta_r=\det\partial(F_r,G_r)/\partial(u,v)$ 是实际图中 Jacobian，不是从其他矩阵借来的权。

## Proof Strategy

从原图计算反典范标架的符号，构成直接湮灭原 $J_n$ 的全局留数和。利用已接受的逆 $\tau$ 自由秩确定该映射就是原自由余核，而非另一组 shadow 消费者。
接着在坏图中把两个原截面同时化为 $F=U(\tau+V),G=V$；此变换及其 Jacobian 在整数形式环中均可逆。
于是完整 jet 像按 $F$ 次数真正分离，负二项展开给 (I)。最后保留原 $s_0$ 乘法的坐标移位，并计算具体理想的双对偶。

## Dependency Map

1. 原几何与实际源／目标：已接受 [JET] 的原四图及标架，本作者本人读取所需 1–285 行。
2. 逆 $\tau$ 后原余核的自由性：已通过独查的 [D05] 与 [CHECK]，本作者两件均全文读取并核对指定 SHA。
3. 留数和为零：Griffiths 的紧流形留数定理，§III(a), (3.7)，及其 Stokes 证明 [GR]；本作者定向读取原文 pp. 368–373 的所需定义、坐标公式及定理证明。没有使用其要求正性的逆定理。
4. 新整数桥梁：下文 Steps 1–6 的四中心范围、标架符号、原余核识别及坏图正规形。
5. 全次数链与格缺陷：Steps 7–8。无需主控正在检查的 $M_4$ 分块锚点，也不依赖任何有限矩阵运行。

## Proof

### Step 1. 原两个截面在四图中的完整式

直接将 $s_0,s_1$ 逐单项式代入 (J)，得到

$$
\begin{array}{c|c|l}
r&F_r&G_r\\\hline
1&u(1+v)&-v+u(1+v)^2-\tau u^2(1+v)\\
2&u(\tau+v)&v+u^2(u-1)(\tau+v)^2\\
3&u(\tau+v)&v+u^2(u-1)(\tau+v)^2\\
4&u(1+v)&v+u-\tau u^2(1+v)^2.
\end{array}
\tag{FG}
$$

两坏图的多项式相同，但它们仍是两个原中心，不能合并其余核类。线性项的 Jacobian 值分别为

$$
\Delta_1(0)=-1,\qquad \Delta_2(0)=\Delta_3(0)=\tau,\qquad\Delta_4(0)=1.
\tag{Jac}
$$

所以在 $R^\circ$ 上 $(F_r,G_r)$ 是每图的形式坐标；好图在 $R$ 上已经如此。

### Step 2. 逆 $\tau$ 后没有遗漏的共同零点

原 $Y$ 的 toric 边界由八条射线

$$
(1,0),(1,1),(1,2),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1)
$$

标记。它们分别来自乘积射影线的四条边界，以及原四次节点吹起；簇 3 的第二次节点吹起给 $(1,2)$。
相对于原对数体积形式 $dx\wedge dy/(xy)$，$s_0$ 对应常数 Laurent 多项式 $1$，其除子就是整个 toric 边界。
$s_1/s_0=y-x+x/y-\tau/x$，四项指数为 $(0,1),(1,0),(1,-1),(-1,0)$。

对每条上述射线取最低权面，最低内积均为 $-1$，相应的边界最低项为：

| 射线 | $s_1/s_0$ 的最低权项 | 对共同零点的贡献 |
|---|---|---|
| $(1,0)$ | $-\tau/x$ | 单项，逆 $\tau$ 后不为零 |
| $(1,1)$ | $-\tau/x$ | 单项，逆 $\tau$ 后不为零 |
| $(1,2)$ | $x/y-\tau/x$ | 原第3图，$\xi=\tau$ |
| $(0,1)$ | $x/y$ | 单项，不为零 |
| $(-1,0)$ | $-x+x/y$ | 原第1图，$\xi=1$ |
| $(-1,-1)$ | $y-x$ | 原第4图，$\xi=1$ |
| $(0,-1)$ | $y$ | 单项，不为零 |
| $(1,-1)$ | $y-\tau/x$ | 原第2图，$\xi=\tau$ |

四条二项边的原边坐标正是 (FG) 的 $1+v$ 或 $\tau+v$；沿 $u=0$ 时 $G_r$ 为 $-v,v,v,v$，所以各自恰有一个简单零点。其根 $1,\tau,\tau,1$ 为单位，均不落在相邻 toric 节点。
各相邻面共有的顶点系数属于 $\{1,-1,-\tau\}$，在逆 $\tau$ 后全为单位，因此节点也不是额外共同零点。
边界之外 $s_0$ 不为零。由此 $\operatorname{div}(s_0)$ 与 $\operatorname{div}(s_1)$ 没有公共分量，全部共同零点恰为四个原中心；(Jac) 还说明它们在每个非零复数时间上横截。

### Step 3. 原反典范标架给出的符号与留数映射

令 $\xi=1+v$ 或 $\tau+v$，与各图对应。原坐标代入及原局部系数乘子 $t_r$ 满足 $Q_{r,n}(P)=t_r^nP(x(u,v),y(u,v))$：

| 图 | $(x,y)$ | $t_r$ | $\det\partial(x,y)/\partial(u,v)$ | $\kappa_r=t_r\det\partial(x,y)/\partial(u,v)$ |
|---:|---|---|---|---:|
| 1 | $(u^{-1},\xi)$ | $u^2$ | $-u^{-2}$ | $-1$ |
| 2 | $(u\xi,u^{-1})$ | $u$ | $u^{-1}$ | $1$ |
| 3 | $(u\xi,u^2\xi)$ | $u^{-2}\xi^{-1}$ | $-u^2\xi$ | $-1$ |
| 4 | $((u\xi)^{-1},u^{-1})$ | $u^3\xi^2$ | $-u^{-3}\xi^{-2}$ | $-1$ |

表内带负幂的 $t_r$ 仅记录原标架转换；(J) 已保证原受限源的最终局部系数是正则多项式，未在非单位族反演 $\xi$。
因为 $a+(N-a)+2=n+1$，一个原 $P\in V_n$ 给全局亚纯二形式

$$
\omega_{n,a}(P)=\frac{P}{s_0^{a+1}s_1^{n-a}}\,dx\wedge dy.
\tag{omega}
$$

这是 $\mathscr L^n/\mathscr L^{n+1}=\omega_Y$ 的真实截面比值；在第 $r$ 图恰写成

$$
\omega_{n,a}(P)=
\kappa_r\frac{Q_{r,n}(P)\,du\wedge dv}{F_r^{a+1}G_r^{n-a}}.
\tag{frame}
$$

故符号与 $n$ 无关；不能漏掉 $\kappa_r$，也不能改成其任意 $n$ 次幂。

现在对任意 $w=(w_1,\ldots,w_4)\in W_n$，在 $R^\circ[[F,G]]$ 中定义

$$
\rho_{n,a}(w)=
\sum_{r=1}^4\epsilon_r
[F^aG^{N-a}]
\left(\frac{w_r}{\Delta_r}\right)\bigl(u_r(F,G),v_r(F,G)\bigr),
\quad (\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4)=(1,-1,1,1)=-\kappa.
\tag{rho}
$$

由于 $\Delta_r$ 在 $R^\circ[[u,v]]$ 为单位、形式坐标变换保持极大理想的幂，系数只依赖 $w_r\bmod(u,v)^n$。每一项均属于 $R^\circ$，不是需要选择根或除以阶乘的数值留数。

对原源的 (frame)，(rho) 是四个局部留数之和的负值：以 $(F,G)$ 作坐标后，二变量 Cauchy 系数公式正好提取 $F^aG^{N-a}$。
固定任一非零复数 $\tau$，Step 2 给紧光滑曲面 $Y_\tau$ 上两组极除子相交于上述四点；(omega) 的极点只位于这两组除子。紧流形留数定理给其四点留数和为零。该定理允许重数极除子，且不要求除子 ample；这里不用要求正性的逆定理。[Griffiths, §III(a), (3.7), pp. 372–373](https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf)

因此 $\rho_nJ_n=0$ 在每个非零复数时间成立。左端各条目是整数 Laurent 多项式于 $\tau$，在所有这些时间为零便是 $R^\circ$ 中的零多项式。这证明精确整数身份

$$
\rho_nJ_n=0.
\tag{zero}
$$

还可与原相邻商的自由坐标直接核准归一化。令 $g_r(v)=w_r(0,v)$。在 $F=0$ 上，第1图有 $v=-G,\Delta_1=-(1+v)$，第4图有 $v=G,\Delta_4=1+v$；两坏图有 $v=G,\Delta_r=\tau+v$。取 $G^N$ 系数后得到

$$
(-1)^{n-1}\tau^n\rho_{n,0}(w)
=g_3(-\tau)-g_2(-\tau)
+(-1)^n\tau^n g_1(-1)+\tau^n g_4(-1)
=\Psi_n(g).
\tag{Psi}
$$

这恰是已接受 D05 的原四边兼容泛函；特别是原第三图常数的自由坐标仍为 $1$，没有另选无法追溯的自由商。

### Step 4. 留数坐标确实识别原自由余核

已接受 (D05) 的相邻短正合列在逆 $\tau$ 后为

$$
0\longrightarrow M_{n-1}[\tau^{-1}]
\longrightarrow M_n[\tau^{-1}]
\longrightarrow R^\circ\longrightarrow0.
$$

右端自由，因此分裂；由 $M_0=0$ 归纳，$M_n[\tau^{-1}]$ 自由秩 $n$，没有遗留整数扭子。

(rho) 在逆 $\tau$ 后满射：对任一 $0\le a\le N$，仅在第三图放入

$$
w_3=\Delta_3 F_3^aG_3^{N-a}\pmod{(u,v)^n},\qquad w_1=w_2=w_4=0.
$$

其留数向量就是 $e_a$，因为 $\epsilon_3=1$。截去项的总次数至少为 $n$，除单位及作形式坐标替换后仍至少为 $n$，不改变所提取的次数。
所以 (zero) 诱导一个自由秩 $n$ 到自由秩 $n$ 的满射。它的方阵有右逆，行列式为单位，从而是同构。

在原 $M_n$ 上，$\rho_n(c)=0$ 当且仅当 $c$ 在逆 $\tau$ 后为零，等价于某个 $\tau$ 幂杀死 $c$；这正是 $c\in T_n$。因此 $L_n$ 就是 (rho) 的实际像。此时才可以由目标 jet 像计算原自由格，而不是把一组外加泛函冒称为原直和块。

### Step 5. 两坏图的整数正规形与 Jacobian 单位

在第2或3图，令

$$
\lambda=1+u^2(u-1)(\tau+v),\qquad
U=u/\lambda,\qquad
V=v+u^2(u-1)(\tau+v)^2.
\tag{normal}
$$

$\lambda\in1+(u,v)^2R[[u,v]]$ 为单位；$(U,V)=(u,v)\bmod(u,v)^2$。按总次数逐次解出逆代换，只需消去恒等线性部分，故得到 $R[[U,V]]\simeq R[[u,v]]$ 的整数形式同构；不反演 $\tau$ 或任何整数。
直接相乘可得

$$
\tau+V=(\tau+v)\lambda,\qquad F_r=U(\tau+V),\qquad G_r=V.
\tag{simple}
$$

该变换的 Jacobian 在 $R[[u,v]]$ 中为单位。因此

$$
w(u,v)\,du\wedge dv=h(U,V)\,dU\wedge dV
$$

给两个完整 fat-jet 模之间的 $R$-线性同构：先作整数形式坐标替换，再乘一个 Jacobian 单位。这里的 $u,v$ 乘法只用于目标多项式和坐标变换；没有给原 $M_n$ 添加 $R[u,v]$-模结构。

在 (simple) 中，$\det\partial(F,G)/\partial(U,V)=\tau+V$。于是局部留数系数改写为

$$
[F^aG^{N-a}]
\frac{h(F/(\tau+G),G)}{\tau+G}.
\tag{simple-rho}
$$

这是同一个原局部留数的坐标计算；Jacobian 单位已准确包含在任意 $h$ 的取值范围中，不能删掉该因子而固定原 $w$ 不变。

### Step 6. 完整 jet 格像按实际 $F$ 次数分离

$h$ 遍历全部 $R[U,V]/(U,V)^n$。取其基单项式 $U^rV^b$，$r+b\le N$，则 (simple-rho) 的被提取式为

$$
F^rG^b(\tau+G)^{-r-1}.
$$

它只贡献第 $a=r$ 个坐标，贡献值准确为

$$
(-1)^{N-a-b}\binom{N-b}{a}\tau^{b-n},
\qquad 0\le b\le N-a.
\tag{coeff}
$$

公式来自整数负二项恒等式

$$
(\tau+G)^{-a-1}
=\sum_{d\ge0}(-1)^d\binom{a+d}{a}\tau^{-a-1-d}G^d;
$$

只需 $d=N-a-b$ 这一项，不涉及无界计算。因此单独第三图的完整像已经是

$$
\bigoplus_{a=0}^{N}\tau^{-n}\mathcal I_{n,a}e_a.
\tag{bad-image}
$$

第2图同样给该像，整体负号不改变理想。第1、4图中 $(F_r,G_r)$ 及其 Jacobian 已在 $R$ 上可逆，因此 $w_r\mapsto(w_r/\Delta_r)\circ(F_r,G_r)^{-1}$ 遍历全部整数 fat jets；其像为 $R^n$。
而 (I) 含有 $b=N-a$ 的生成元 $\tau^{N-a}$，故 $\tau^{-n}\mathcal I_{n,a}$ 含 $\tau^{-a-1}R$，进而含 $R$。两好图的像已包含在 (bad-image) 中。
四图直和的完整像恰为 (bad-image)，结合 Step 4，证明 (G) 和 (G')。这是真正的原无扭商格直和理想描述，不是只得到一张同规模关系矩阵。

### Step 7. 原截面乘法的实际移位

原链映射在第 $r$ 图是乘 $F_r$，即已接受的 $u(1+v),u(\tau+v),u(\tau+v),u(1+v)$。
在 (rho) 的共同坐标中，这只是将被提取式乘 $F$。因此新第0坐标为零，而新第 $a\ge1$ 坐标等于旧第 $a-1$ 坐标，逐项证明 (S)。
乘归一化公因子后，有

$$
\widetilde\rho_{n+1}\iota_n=\tau\cdot\operatorname{shift}\circ\widetilde\rho_n.
$$

包含 $\tau\mathcal I_{n,a}\subset\mathcal I_{n+1,a+1}$ 也可直接核对：每个旧生成元满足

$$
\tau^{b+1}\binom{n-1-b}{a}
=\tau\left[\tau^b\binom{n-b}{a+1}\right]
-\tau^{b+1}\binom{n-1-b}{a+1},
$$

右端两项属于新理想；越界二项系数按零处理。因为新第0坐标 $\mathcal I_{n+1,0}=R$，其余坐标彼此独立，取商即得 (Q)。
由此可读原自由格的实际饱和指数；不能改用 D05 扩张商中的全部循环扭子长度替代它。

### Step 8. 具体理想的双对偶与原格缺陷

对 $a=0$ 或 $a=N$，$\mathcal I_{n,a}=R$。对 $0<a<N$，该理想同时包含非零整数 $\binom Na$ 与 $\tau^{N-a}$，两者无公因子。
每个 $R$-线性映射 $\mathcal I_{n,a}\to R$ 延伸到分式域后是一个一维线性映射，因此由唯一分式乘法给出。
在 UFD $R=\mathbb Z[\tau]$ 中，若既约分式 $f/g$ 满足 $(f/g)\mathcal I_{n,a}\subset R$，则 $g$ 同时整除这两个互素元素，因此 $g$ 是单位。
故在指定的分式域嵌入中

$$
\operatorname{Hom}_R(\mathcal I_{n,a},R)=R,
\qquad \mathcal I_{n,a}^{**}=R.
$$

这里使用的是 (I) 的具体子理想归一化，而不是任意抽象同构后未指定的双对偶标架。对 (G') 逐项取双对偶，便得到 (D)。
$R/\mathcal I_{n,a}$ 被上述非零整数及 $\tau^{N-a}$ 同时杀死，所以是有限阿贝尔群；有限直和亦然。对 $A=R_{(p,\tau)}$ 重复同一互素分式证明，得到 $(L_n\otimes A)^{**}=A^n$ 及缺陷的明确局部化。

至此 G1–G3 得证。$\square$

## Corrections or Missing Assumptions

- “自由格”始终指原余核的无扭商嵌入其泛自由空间；(G') 中的整数理想一般不自由。没有预设所有 $L_n$ 为自由模。
- 四中心的完整范围只在逆 $\tau$ 后用于留数和；在 $\tau=0$ 不能照搬其简单交点几何。但原格像由整数目标及整数正规形计算，(G') 与 (D) 没有删去 $\tau=0$ 的缺陷。
- 本包没有重新证明旧实际复形的几何身份，只按 [JET] 与其接受范围消费；新留数桥梁与原标架逐步验证。
- 不消费旧 W1–W3 的 Koszul 论断；原逆 $\tau$ 自由秩直接来自已独查的 D05。全局留数定理只用于湮灭原源，不用于未经证明地指定整个余核。
- 不把 $P_m$、关联分次循环商或 (Q) 的各商项称作原 $M_n$ 直和因子。原 $M_n$ 的扩张仍可能不分裂。

## Open Risks / Blocking

作者证明的主要新检查风险为：(i) Step 2 的完整四中心范围；(ii) Step 3 的原标架 $\kappa_r$ 与 $\epsilon_r$；(iii) Step 4 从留数满射到真实原自由余核的识别；(iv) Step 5–6 中 Jacobian 单位对整个原 fat-jet 模的作用。
这些都必须针对本终态由非作者检查；旧 D05 独查不替新桥梁签字。没有尚待追加有限 $n$ 样本才能陈述的量。
本件完成的是原自由格及双对偶缺陷的封闭控制，不是原全扭子直和块分类、正式新意分或22–30页容量证明。

## Next — 唯一下一实质引理

在本格身份被独立接受后，检查**原呈示的最大子式与格行列式比较引理**：对 $A=R_{(p,\tau)}$，将原 $M_n$ 的实际长度一自由呈示与 (G') 的指定 $\mathcal I_{n,a}^{**}=A$ 标架相比较，确定

$$
\operatorname{Fitt}_n(M_n\otimes A)
\stackrel{?}=\tau^{B_n}\prod_{a=0}^{n-1}\mathcal I_{n,a}A,
\quad B_n=\operatorname{length}_{\mathbb Q[[\tau]]}
\bigl(T_n\otimes_R\mathbb Q[[\tau]]\bigr).
$$

该句是下一引理目标，不是本包新增已证声明；主控另席正在做独立消费者推导。本件不为获得原块化而再添加有限 Smith 样本。

## Source scope, verification, and ownership

| 本人读取对象 | 范围 | 指定 SHA-256 |
|---|---|---|
| [D05] 作者终态 | FULL，318行 | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` |
| [CHECK] 独查终态 | FULL，179行 | `12b9ce4f6b6e485c8457478821eb3c2cc8afca74807aa98daf17240b586d4370` |
| [JET] 原实际复形 | 本人定向1–285；非全文 | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| proof-writer 技能 | 本人全文读取并按其 Claim／Status／假设／依赖／证明／边界结构执行 | 非数学来源 |
| [GR] Griffiths 原文 | §III(a) 所需局部定义、坐标公式及紧流形定理(3.7)和证明，pp.368–373；非全篇。定理/证明在 PDF 第52–53页（零基51–52），印刷页372–373 | 官方作者机构公开 PDF |

没有以主控 $M_4$ 手工分块或条件性整数消费者作为本证明输入；没有运行 CPU、调用旧矩阵代码或新增脚本。只有本文是本席新增本地文件。
正文各次数由统一纸面证明承担；可逆形式坐标及留数理论是实际推导工具，不是运行成功标签。终态已全文自读并核对本次三个直接本地输入哈希，行数与输出 SHA 随交付提供。

[D05]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[CHECK]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_INDEPENDENT_CHECK_V1_20260909.md
[JET]: PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[GR]: https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf
