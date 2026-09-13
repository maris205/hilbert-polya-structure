# Paper31 D05：原全次数算术上同调的合并定理 V1

日期：2026-09-09 UTC；合并作者：主控 `/root`。`route_applicability: NOT_APPLICABLE`。
本件只合并同一原 $q=1$ 非单位时间族的已明确对象，不拼接不同构造、拟合参数或事后阈值。
本件是新作者定理包，尚待完整新依赖合取和本件新增推论的非作者检查；不是正式候选准入。

## Claim

令 $R=\mathbb Z[\tau]$，$S/R$ 为原 qPI 四簇 $1+2+3+2$ 八截面吹起在 $q=1$ 的模型，
$\mathscr L=\omega_{S/R}^{-1}$。对 $n\ge0$，记
$$M_n=H^1(S,\mathscr L^n)=\operatorname{coker}J_n,\quad
T_n=\operatorname{tors}_{\tau}M_n,\quad L_n=M_n/T_n,\quad E_n=L_n^{**}/L_n.$$
双对偶在 $R$ 上取。令 $B_n=\sum_{j=1}^{n-1}j^2$，$B_0=0$。
对 $n\ge1,N=n-1,0\le a\le N$，定义
$$I_{n,a}=\left(\binom{N-b}{a}\tau^b:0\le b\le N-a\right),\quad
d_p(N,a)=\min\{0\le b\le N-a:p\nmid\binom{N-b}{a}\},\quad D_n(p)=\sum_{a=0}^{N}d_p(N,a).$$
零次数用空和／空乘积约定，$D_0(p)=0$。

**A1（完整原无扭商格与缺陷）。** 留数坐标给指定同构
$$L_n\simeq\bigoplus_{a=0}^{n-1}I_{n,a},\qquad E_n\simeq\bigoplus_{a=0}^{n-1}R/I_{n,a}.$$
原 $s_0=xy$ 次数连接在该坐标中为 $\tau$ 倍右移。每个 $E_n$ 是有限阿贝尔群。
每个素数上的完整整数系数层和 $\tau$ 作用由[二项式消费者][C] C1 的明确公式给出。

**A2（第一个非零原 Fitting 理想）。** 在整个 $R$ 上而非仅在单个域上，
$$\operatorname{Fitt}_j(M_n)=0\quad(0\le j<n),\qquad
\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_{a=0}^{n-1}I_{n,a}.\tag{F}$$
$n=0$ 时 $M_0=0$，(F) 右端和 $\operatorname{Fitt}_0(0)$ 均为 $R$。

**A3（所有特征的完整原扭子长度）。** 对任意域 $k$，令 $M_{n,k}=M_n\otimes_R k[[\tau]]$。
其自由秩为 $n$，且
$$\operatorname{length}_{k[[\tau]]}\operatorname{tors}_{\tau}M_{n,k}=
\begin{cases}B_n,&\operatorname{char}k=0,\\B_n+D_n(p),&\operatorname{char}k=p>0.\end{cases}\tag{L}$$
因此，对每个素数 $p$，相对同次数的特征零长度，第一次严格增加恰在 $n=p+1$，增加 $p-1$。
在 $A_p=R_{(p,\tau)}$ 上，这一次的准确理想为
$$\operatorname{Fitt}_{p+1}(M_{p+1}\otimes A_p)
=\tau^{\sum_{j=1}^{p}j^2}(p,\tau)^{p-1}.\tag{First}$$
它为非主理想；这证明原全素数 Fitting 目标，不证明旧全素数强直和猜式。

**A4（全部次数的无缺陷判据与数字递推）。** 对固定素数 $p$、$n\ge1$，
$$D_n(p)=0\iff \frac{n}{p^{v_p(n)}}<p.\tag{Zero}$$
该条件也等价于 $E_n\otimes_R A_p=0$ 及原 $L_n\otimes_R A_p$ 自由。
令 $H_p(N)=D_{N+1}(p)$ 对 $N\ge0$，约定 $H_p(-1)=0$；令
$Z_p(q)=\prod_i(q_i+1)$，其中 $q_i$ 为 $q$ 的基 $p$ 数字，$Z_p(0)=1$。
对 $N=pq+r$、$0\le r<p$，有准确递推
$$\begin{aligned}
H_p(N)={}&p(r+1)H_p(q)+p(p-1-r)H_p(q-1)\\
&+(r+1)(p-1-r)(Z_p(q)-1).
\end{aligned}\tag{Digit}$$
这是全 $n,p$ 的有限整数规则，不是通过扩大次数样本拟合的规律。

## Status, Assumptions and Boundaries

`PROVABLE AS STATED / AUTHOR_SYNTHESIS`，等待针对新原格桥梁、一般工具及本件合并推论的独立报告完成合取。
使用[原实际复形][JET]和[相邻扩张接受][BASE]的已接受几何身份；新增直接依赖为[原格识别][G]、[行列式引理][D]、[整数消费者][C]。
这些文件中的具体对象、标架和条件不可略去；下文逐项提供其应用输入，而不是用未来要证的 (F) 或 (L) 反向证明它们。
本文不声称 $M_n=T_n\oplus L_n$，不声称完整扭子 Smith 指数或全部 $\operatorname{Fitt}_{j>n}$ 已分类。
原 $\tau=0$ 动力公式仍塌缩；本件研究整族上反典范上同调，不宣称零时间动力仍可逆。
不将 $q=1$ 的结论推广到任意 $q$，也不把指定整数理想换成未归一的抽象同构理想。

## Strategy and Dependency Map

原八截面实际复形 → 全截面核的单位补基 → 实际长度一自由分辨率。
另一支是原四中心留数／整数正规形 → 完整无扭商格及真实次数移位。
两支合成后，格指数消费者给 (L)，互补最大子式给 (F)；最后才施加二项系数数字判别。
下列 Step 1–3 检查这些输入匹配，Step 4–5 是本件新写的全次数无缺陷判据与递推证明。

## Proof

### Step 1. 原模的长度一自由分辨率及缺陷条件

[JET] 给原 $J_n:R^{2n(n+1)+1}\to R^{2n(n+1)}$。由 [BASE]，它的核恰由
$$P_k=s_0^{n-k}s_1^k,\qquad 0\le k\le n,\quad s_1=x^2-x^2y+xy^2-\tau y$$
自由生成。该核不仅抽象自由，而且在原源中有单位补基：$P_k$ 的最高 $y$ 次为 $n+k$，
且该项恰为系数1的 $x^ny^{n+k}$。在源坐标 $(n,n+j)$ 上，系数矩阵为对角全一的三角矩阵。
把这 $n+1$ 个单项式源向量替换成 $P_k$，保留其他原单项式，便是行列式为单位的基底变换。
删去这些零列后，剩余矩阵 $\Phi_n$ 单射，因为已知原核恰是上述直接和项。
故有真实正合列
$$0\to R^{n(2n+1)}\xrightarrow{\Phi_n}R^{2n(n+1)}\to M_n\to0.\tag{Resolution}$$
$n=0$ 时两个自由模均为零，与 $M_0=0$ 一致。

[G] 通过原 $J_n$ 的湮灭、逆 $\tau$ 满射与原秩 $n$，识别的是 $M_n[\tau^{-1}]$ 的实际坐标，
而不是未证明可分离的一组函数。这提供 [C] 的 H2。其原 $s_0$ 右移身份提供 [C] 的 H3；H1 正是 [BASE]。
因此 [C] 的条件性结论 (4) 对本原模解除条件，给出 (L)，同时给泛长度 $B_n$。
此处解除的是明确证明并匹配的 H2–H3，不依赖有限四阶样本。

[G] 还给 A1 及每个 $I_{n,a}^{**}=R$ 的具体归一化。局部化到 $A_p$ 后，
$L_n^{**}=A_p^n$、$E_n$ 有限长，且 $M_n[1/\tau]$ 自由秩为 $n$。
由局部化的平坦性，(Resolution) 仍为指定长度一自由分辨率；全部 [D] 假设至此齐备。

### Step 2. 最大子式、局部化和全局原 Fitting

应用 [D] 主引理及其**已归一化**的直和推论，对每个有理素数 $p$ 得
$$\operatorname{Fitt}_n(M_n)A_p=\tau^{B_n}\prod_a I_{n,a}A_p.\tag{LocalF}$$
使用的是同一原模的分辨率、自然扭子商及格双对偶；[D] 中的高度一指数为 Step 1 的实际泛长度。
共同因子 $\tau^{B_n}$ 和高度二理想乘积来自同一互补子式关系，不能各从不同呈示选择最好值。

为将 (LocalF) 升为 $R$ 中的理想相等，取任意素理想 $\mathfrak q\subset R$。
若 $\tau\notin\mathfrak q$，则原 $M_n$ 在此局部自由秩 $n$，左侧为单位理想；
右侧亦为单位理想，因为每个 $I_{n,a}$ 含 $\tau$ 的某个幂。
若 $\tau\in\mathfrak q$，则 $R/(\tau)=\mathbb Z$ 给出 $\mathfrak q=(\tau)$ 或 $(p,\tau)$。
后一种由 (LocalF) 给出相等；前一种再局部化任一 (LocalF) 即可。
两有限生成理想在全部素点局部化后相同，故它们相同：否则其中一个在和理想中的非零商有某个素点支撑，与局部相等矛盾。
这证明 (F) 的非零式。在 (Resolution) 中，对于 $j<n$ 所需的子式阶大于列数，故 $\operatorname{Fitt}_j(M_n)=0$。

### Step 3. 全素数首次消费者与旧强猜式边界

[C] C2 给 $n\le p$ 时全部 $I_{n,a}A_p=A_p$、$D_n(p)=0$。
在 $n=p+1$，两端理想为 $A_p$，其余 $p-1$ 个恰为 $(p,\tau)$，且 $D_{p+1}(p)=p-1$。
将这些准确理想代入同一个 (F) 得 (First)，代入 (L) 得首次长度跳跃。
$(p,\tau)^{p-1}$ 含 $p^{p-1}$ 和 $\tau^{p-1}$，在 UFD 中公因子为单位，但它是极大理想的正幂，因而为真理想。
若它主生成，则生成元只能是单位，与真理想矛盾。因此 (First) 非主。

这解决的是旧[首素数探针][OLD]的 Fitting 目标 (F)，并提供其之外的全次数公式。
旧强猜式 (P) 还断言整个原模出现指定 $V_p$ 的直和，不能由 Fitting 或长度反推，本件不宣布其已证。
已独立核验的固定三阶及[固定四阶真分块][M4]是相容的低阶锚点，不是全称证明的前提。

### Step 4. 哪些次数完全没有该素数缺陷

[C] 的数字公式说明 $D_n(p)=0$ 当且仅当对所有 $0\le a\le N$，每个基 $p$ 数字都满足 $a_i\le N_i$。
若 $N>0$ 的最高非零数字位置为 $h$，且所有低位 $N_0,\ldots,N_{h-1}$ 都是 $p-1$，
那么任意 $a\le N$ 的最高位不会超过 $N_h$，低位也不会超过 $p-1$，所以该条件成立。
反之，若某个 $j<h$ 满足 $N_j<p-1$，取最高位为 $N_h-1$、其余全部 $h$ 个低位为 $p-1$ 的整数 $a$。
它满足 $0\le a<N$，而 $a_j=p-1>N_j$，所以产生严格正的 $d_p(N,a)$。
故无缺陷当且仅当 $N$ 最高位以下全为 $p-1$，包括 $N=0$ 的空条件。

把 $n=N+1$ 写成 $n=c p^v$、$p\nmid c$。若 $1\le c<p$，则
$N=(c-1)p^v+(p^v-1)$ 的低位全为 $p-1$，上述条件成立。
若 $c\ge p$，因 $p\nmid c$，$c$ 的个位在 $1,\ldots,p-1$ 且另有更高非零位；
$N$ 的第 $v$ 位为 $c_0-1<p-1$，其上仍有非零位，所以上述条件失败。
这证明 (Zero)。

每个 $E_n\otimes A_p$ 是有限 $p$-群，因此它非零时其 $p$-核必非零：取非零元素并乘以尽可能高的 $p$ 幂即可。
由 [C] C1，其 $p$-核维数为 $D_n(p)$，故与缺陷为零等价。
缺陷为零时自然 $L_n=L_n^{**}=A_p^n$。反过来，若 $L_n$ 自由，自然双对偶映射是同构，缺陷为零。
这给 (Zero) 的三种准确等价，不把扭子长度相等误称整个模同构。

### Step 5. 完整数字递推

按 [C]，$d_p(N,a)=N-m_p(N,a)$，其中 $m_p(N,a)$ 是不超过 $N$ 且各数字支配 $a$ 的最大整数。
写 $N=pq+r$、$a=pb+s$。对每个 $b\le q$，令 $\delta_b=d_p(q,b)$；
若 $\delta_b=0$，则 $q$ 的数字已支配 $b$。这样的 $b$ 有 $Z_p(q)=\prod_i(q_i+1)$ 个。

对 $0\le s\le r$，允许全部 $0\le b\le q$。若 $\delta_b=0$，最大可取数就是 $N$，故该项贡献0。
若 $\delta_b>0$，最高可用商为 $q-\delta_b<q$，个位可取 $p-1$，所以
$$d_p(N,pb+s)=p\delta_b+r-p+1.$$
这部分对 $s,b$ 求和给
$$ (r+1)\{pH_p(q)+(r-p+1)(q+1-Z_p(q))\}.\tag{Case1}$$

对 $r<s<p$，条件 $a\le N$ 迫使 $0\le b\le q-1$；商 $q$ 不可取，因个位 $r<s$。
最高可用商为 $q-1-d_p(q-1,b)$，个位取 $p-1$，故
$$d_p(N,pb+s)=p\,d_p(q-1,b)+r+1.$$
这部分求和给
$$ (p-1-r)\{pH_p(q-1)+(r+1)q\}.\tag{Case2}$$
若 $q=0$，第二部分为空；约定 $H_p(-1)=0$、$Z_p(0)=1$ 同样覆盖它。
将 (Case1) 与 (Case2) 相加，常数项准确化成
$(r+1)(p-1-r)(Z_p(q)-1)$，得到 (Digit)。
当 $q\ge1$ 时递归参数 $q,q-1$ 均小于 $N$；当 $q=0$ 时 $H_p(N)=0$，所以这是一条终止的明确规则。∎

## Verification and Open Risks

主控本人已全文读取 [G] 429行、[D] 297行、[C] 176行及已接受 D05 作者／独查；
针对新几何桥读取原 [JET] 的实际图与标架所需段落，不重开未变几何。
主控本人另实读 Griffiths 原文 §III(a) 的局部定义及 (3.4)–(3.7) 与证明（印刷pp368–373），
确认紧流形定理不要求正性；正性属于不用的逆定理 (3.8)。[机构公开原文](https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf)
这是定向一手来源适用性核验，不是全文审计、全球查新或新意扣除已经完成。
原文检索只新增一次 arXiv 精确题名入口查询，未返回结果；不据此声称排除了相关研究。

本件没有CPU或GPU运算，也未增加次数／素数样本。A4 的新推论由完整数字证明承担，需由非作者审查。
整个合并的关键风险是实际 (Resolution)、[C] H1–H3 与 [D] 的同对象前提是否完整匹配；
它们必须被独立检查，不能因为各工具分开正确就跳过应用审查。
旧原强 (P)、全部原扭子块、其他 $q$ 与非加法结构仍开放；不把这些开放项计作本件已证明的结果。
本件不自授新意／价值或正文容量，不建立P31项目、锁、稿件或PDF。后续需基于真实新增 A1–A4 重新做有界查新和组合非碰撞判断。

[JET]: PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[BASE]: PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[D]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[C]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[OLD]: PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md
[M4]: PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_LEMMA_V1_20260909.md
