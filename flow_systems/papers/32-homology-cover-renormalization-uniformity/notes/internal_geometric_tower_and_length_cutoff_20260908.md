# P32 内部研究：几何同调覆盖塔、长度截断与固定层乘积

记录日期：2026-09-08 UTC。接续[正 content 族穷尽障碍][family-note]和[标量无限接口][interface-note]。本轮落实两项此前保留的抽象几何前提：从同一个真实带标记闭双曲曲面构造纯同调覆盖塔；证明物理长度截断有限且共尾，并建立足够的轨道计数上界与指数尾界。

由此，固定层的规定 Euler 乘积不再仅依赖一个未验证的抽象求和假设：本轮在 `Re(s)>N` 构造它，并连接全部覆盖本原轨道的几何乘积。另一方面，上一轮的实轴发散现在适用于明确定义的几何长度截断。这里没有运行规范枚举或认证数值矩阵，也没有修改论文、归一化或正式审查状态。

## 1. 固定几何输入与标记的含义

输入仍是[既定 H0][cover-note]：一个真实的、曲率为 `-1` 的带标记闭双曲亏格二曲面 `Sigma`，使用单位速度测地流，标记为

\[
\Gamma=\pi_1(\Sigma)
\cong\langle a_1,b_1,a_2,b_2\mid[a_1,b_1][a_2,b_2]=1\rangle.
\]

闭性保证度量完备。使用该度量的普遍覆盖，将其等距识别为 `H^2`，并把 `Gamma` 识别为实际的、忠实且自由的 deck 等距群，得到

\[
\Sigma=\Gamma\backslash\mathbb H^2.
\]

这是对已给几何的表示，不是用一份抽象群关系或未经认证的矩阵表代替几何。一般的完备双曲曲面商表示见 Caroline Series 讲义 Theorem 7.17；其 Example 7.16 和相邻段落说明普遍覆盖与 deck 群的对应。[一般几何来源][series-unif]

`Gamma` 的作用具有普遍覆盖的小邻域性质：每个 `x in H^2` 有一个开球 `B(x,r_x)`，其不同 `Gamma` 平移互不相交。这来自普遍覆盖的均匀覆盖邻域与 deck 唯一性；群作用商覆盖的一般论述见 Hatcher Proposition 1.40，其 Proposition 1.39 给出正规覆盖的 deck 商群。[一般拓扑来源][hatcher]

本文的数学 owner 集 `O` 是按时间平移识别的全部本原有向基流轨道，与既有本原有向共轭类对应；逆向不合并。它不是轨道上所有起点的集合，也不是一份尚待认证完备性的有限数据表。各长度 `ell_g>0` 是同一个固定度量的最小流周期。[已有轨道绑定及显式族][owner-note]

## 2. H1 的抽象几何构造与整除塔

### 2.1 子群、商面与覆盖图

交换子 relator 在阿贝尔化后不产生额外关系，故阿贝尔化映射为满射

\[
\alpha:\Gamma\twoheadrightarrow\mathbb Z^4.
\]

对每个整数 `N>=1`，定义

\[
H_N=\alpha^{-1}(N\mathbb Z^4),\qquad
\Sigma_N=H_N\backslash\mathbb H^2,\qquad
p_N([x]_{H_N})=[x]_\Gamma.
\]

于是 `H_N` 正规，且

\[
\Gamma/H_N\cong(\mathbb Z/N\mathbb Z)^4,
\qquad[\Gamma:H_N]=N^4.
\]

对第 1 节的 `Gamma`-小球 `B`，令 `U=pi_Gamma(B)`。直接由商的定义，

\[
p_N^{-1}(U)=
\bigsqcup_{H_N\gamma\in H_N\backslash\Gamma}
\pi_{H_N}(\gamma B).
\]

若两项相交，存在 `h in H_N` 使 `h gamma B` 与 `gamma' B` 相交；小球性质迫使 `gamma'=h gamma`，恰好为同一个左陪集。每项到 `U` 都是微分同胚，且保持双曲度量。因此 `p_N` 是度数 `N^4` 的无分歧局部等距覆盖。同一个小球对所有 `N` 都有效。

球像给出商面的光滑图册。不同基底像的点由基底开集分离，同一纤维的不同点由不同 sheets 分离，故商面 Hausdorff；开商映射下的可数基给出第二可数性。商面的连通性来自 `H^2` 连通，且没有边界。度量由 deck 等距性下降，恰为 `p_N` 的拉回度量。

### 2.2 完整 deck 群、对应子群与紧致性

正规性使

\[
D_\gamma([x]_{H_N})=[\gamma x]_{H_N}
\]

良定义，且给出 `Gamma/H_N` 在每个纤维上的自由、传递作用。若一个 deck 映射与某个 `D_gamma` 在一点相同，均匀覆盖图使二者在邻域内相同；相同点集合开闭，连通性使它们处处相同。因此没有额外的 deck 变换，

\[
\operatorname{Deck}(p_N)=\Gamma/H_N.
\]

在一致的环路／deck 标记下，基点环路 `gamma` 的提升终点为 `[gamma x]_(H_N)`，它闭合当且仅当 `gamma in H_N`。所以这是对应规定子群的覆盖，不只是一个碰巧同度数的覆盖。

紧致性也可直接检查：选有限个紧闭片 `K_i subset U_i` 覆盖紧基底 `Sigma`，每个 `U_i` 均匀覆盖。每个 `p_N^{-1}(K_i)` 是 `N^4` 个与 `K_i` 同胚的紧片之并，故 `Sigma_N` 紧致。这样，每一层都是连通闭双曲曲面。

### 2.3 整除映射与同一个物理时间

若 `N|M`，则 `H_M subset H_N`，并有自然商映射

\[
p_{M,N}:\Sigma_M\to\Sigma_N,
\qquad[x]_{H_M}\mapsto[x]_{H_N},
\qquad\deg p_{M,N}=(M/N)^4.
\]

它是正规局部等距覆盖，deck 群为 `H_N/H_M`。这些映射逐点满足

\[
p_M=p_N\circ p_{M,N},\qquad
p_{L,N}=p_{M,N}\circ p_{L,M}\quad(N|M|L).
\]

各层度量 `mathbf g_N` 满足 `mathbf g_N=p_N^*mathbf g_Sigma`、`mathbf g_M=p_(M,N)^*mathbf g_N`。具体的恒等映射为 `p_1=id_Sigma` 与 `p_(N,N)=id_(Sigma_N)`；一般的 `p_(M,1)=p_M` 并非恒等。

局部等距的微分在每个 sheet 上唯一提升单位切向量，所以 `P_N=T^1p_N` 是同度数覆盖。双曲平面上的单位速度测地流与 deck 等距变换交换，下降后满足

\[
P_N\circ\phi_t^{(N)}=\phi_t\circ P_N,
\qquad t\in\mathbb R.
\]

整除塔的单位切丛映射也保持这个 `t`。这完成了 H1 的抽象几何内容；此处没有先行重参数化时间。H3 所规定的后续 `1/N` 时间缩放及 `1/N^3` 对数归一化保持原样。

## 3. 本原有向轨道的有限长度计数

### 3.1 一个轨道点的球包装上界

固定 `x in H^2`，从普遍覆盖小球性质选定 `r>0`，使所有 `B(gamma x,r)` 两两不交。令 `p=pi_Gamma(x)`，取

\[
D=\operatorname{diam}(\Sigma)+1<\infty.
\]

对任意 `y in H^2`，从 `pi_Gamma(y)` 到 `p` 可选长度小于等于 `D` 的路径；提升后终点为某个 `gamma x`。因此每个 `y` 距离 `Gamma x` 至多 `D`。不需要先构造带数值顶点的基本多边形。

记 `A_R={gamma:dist(x,gamma x)<=R}`。对其任意有限子集，相应半径 `r` 球均包含于 `B(x,R+r)`。曲率 `-1` 的球面积为

\[
V(u)=2\pi(\cosh u-1)=4\pi\sinh^2(u/2).
\]

该面积公式及计算见 Series Lemma 2.16。[面积公式来源][series-area] 因 `V(r)>0`，包装不等式给每个上述有限子集的基数以共同有限上界，因此 `A_R` 本身有限，且

\[
|A_R|\le\frac{V(R+r)}{V(r)}.
\]

这样不以“已经知道 `A_R` 有限”作为包装论证的循环前提。

### 3.2 从短测地线到有限位移元素

给定长度 `ell_g<=L` 的有向本原 owner，取其提升轴上的点 `y`，再取 `gamma` 使 `dist(y,gamma x)<=D`。将轴与群元素一起以 `gamma^{-1}` 共轭，得到同一有向共轭类的代表 `h`，其轴含一个距 `x` 至多 `D` 的点 `y'`。于是

\[
\operatorname{dist}(x,hx)
\le 2\operatorname{dist}(x,y')+
\operatorname{dist}(y',hy')
\le 2D+\ell_g\le2D+L.
\]

因此每个这样的 owner 共轭类都与有限集合 `A_(L+2D)` 相交。不同共轭类互不相交，故以有限位移元素向共轭类取像便足以计数，不需要选择规范代表。方向已包含在 owner 的定义中，不另除以二。

记 `n(L)=#{g in O:ell_g<=L}`。对所有实数 `L>=0`，

\[
n(L)\le\frac{\cosh(L+2D+r)-1}{\cosh r-1}
\le C_{\rm cnt}e^L,
\qquad
C_{\rm cnt}=\frac{e^{2D+r}}{2(\cosh r-1)}>0.
\]

最后一步使用 `cosh u-1=(e^u/2)(1-e^{-u})^2<=e^u/2`。这是粗略上界，不是素测地线渐近或精确增长率的证明；常数依赖固定度量，未计算其数值。

## 4. 几何截断共尾性、正长度下界与指数尾和

定义数学上的几何集合

\[
E(T)=\{g\in\mathcal O:\ell_g\le T\},\qquad
E_+(T)=E(T)\cap\mathcal O_+,\qquad T\ge0.
\]

第 3 节证明它们有限。对任何固定有限 `F subset O`，当 `T>=max({0} union {ell_g:g in F})` 时就有 `F subset E(T)`。所以长度截断在全部有限 owner 子集网中共尾；整数截断也已足够，并且 `O=union_(j>=1)E(j)` 可数。

因为 `E(1)` 有限，取

\[
\ell_*:=\min\bigl(\{1\}\cup\{\ell_g:g\in E(1)\}\bigr)>0.
\]

它是所有 owner 的长度下界，且覆盖 `E(1)` 为空的情形。没有以一份未执行的短轨道列表认证这个常数。

对每个 `a>1`，定义 `S_0(a)=sum_g e^{-a ell_g}`。利用正项恒等式 `e^{-a ell}=integral_(ell)^infinity a e^{-au}du`，对 `T>=0` 有

\[
\begin{aligned}
\sum_{\ell_g>T}e^{-a\ell_g}
&=\int_T^\infty a e^{-au}
\#\{g:T<\ell_g\le u\}\,du\\
&\le\int_T^\infty aC_{\rm cnt}e^{-(a-1)u}\,du\\
&=\frac{aC_{\rm cnt}}{a-1}e^{-(a-1)T}.
\end{aligned}
\]

求和与积分的交换可先对任意有限子集作等式，再以非负单调极限通过；没有条件收敛重排。取 `T=0`，所有长度严格为正，得到

\[
\boxed{S_0(a)\le\frac{aC_{\rm cnt}}{a-1}<\infty
\quad\text{对每个 }a>1.}
\]

这把上一轮的求和前提落实为固定闭双曲几何下的定理。尾界适用于每个实数截断 `T>=0`，不会漏掉非整数截断与下一个整数之间的轨道；同样适用于正 owner 子集。它仍是含理论几何常数的界，不是已经计算出的数值包络。

## 5. 固定层的非零全纯产品及完整几何连接

### 5.1 基底与归一化后产品

沿用既有单周期归零全纯对数

\[
L_t(s)=\sum_{r\ge1}\frac{e^{-rst}}r\qquad(\operatorname{Re}s>0),
\]

以及分支整数

\[
m_{N,g}=\begin{cases}
\gcd(N,d_g),&g\in\mathcal O_+,\\
N,&g\in\mathcal O_0.
\end{cases}
\]

基底乘积 `B(s)=exp(sum_g L_(ell_g)(s))` 由第 4 节及[上一轮的绝对收敛引理][interface-note]在 `Re(s)>1` 上定义为非零全纯函数。

固定 `N>=1`。因 `1<=m_(N,g)<=N`，对任意 `a>1`，有

\[
\sum_gm_{N,g}e^{-Na\ell_g/m_{N,g}}\le NS_0(a)<\infty.
\]

故

\[
\mathscr L_N(s)=\sum_gm_{N,g}L_{\ell_g/m_{N,g}}(s),
\qquad Q_N(s)=e^{\mathscr L_N(s)}
\]

在 `Re(s)>Na` 上有绝对、局部一致收敛的定义。对任意非空紧集 `K subset {Re(s)>N}`，可选 `1<a<min_K Re(s)/N`；不同 `a` 使用的是同一绝对收敛级数，因此定义一致，得到

\[
\boxed{Q_N\text{ 在 }\operatorname{Re}s>N
\text{ 上全纯且无零点。}}
\]

在这个半平面上 `R_N=Q_N/B` 也全纯、非零。正 owner 子乘积 `Q_N^+,B^+,R_N^+` 以同样方式构造，并具有相同的充分定义域。不能从这项上界证明临界线或域外的不存在性。

进一步记 `c_a=1-e^{-a ell_*}>0`。对长度截断，有明确的对数尾界

\[
\sup_{\operatorname{Re}s\ge Na}
|\mathscr L_N(s)-\mathscr L_{N,E(T)}(s)|
\le\frac N{c_a}\sum_{\ell_g>T}e^{-a\ell_g}
\le\varepsilon_{N,a}(T),
\]

\[
\varepsilon_{N,a}(T)=
\frac{NaC_{\rm cnt}}{c_a(a-1)}e^{-(a-1)T}.
\]

相应相对产品误差至多为 `exp(epsilon_(N,a)(T))-1`。这里 `N,a` 固定；该界没有给出冻结层数趋于无穷时的共同固定参数域。

### 5.2 所有覆盖本原轨道都被基底 owner 分拆捕获

设 `tilde gamma` 是 `Sigma_N` 上任意本原有向流轨道。其投影是基流的周期轨道；取投影轨道自身的最小周期，得到唯一基底本原 owner `g` 及 `ell_g`。投影可能多次遍历它，但这不产生第二个基底 owner。

在该基轨道上固定一个单位切向量。`tilde gamma` 与其纤维的交点组成一次基周期返回置换的一个完整循环。[既有纤维推导][cover-note]已证明：循环与提升本原轨道一一对应，循环长度是首次返回倍数。因此反向也成立，每条覆盖本原轨道恰被某个基底 owner 的一个循环捕获。

不同循环不能给出同一条覆盖轨道，不同基底 owner 的提升也不能相同。这里使用 `T^1Sigma` 中的返回，不能用曲面自交处的位置返回替代。于是全部覆盖本原有向轨道被完整、无重复地分拆为

\[
h_{N,g}=N/m_{N,g},\quad
c_{N,g}=N^3m_{N,g},\quad
\widetilde T_{N,g}=h_{N,g}\ell_g
\]

所规定的各基底提升块。`c_(N,g)` 仍是返回循环数，不是额外按 deck 对称取商。

### 5.3 无限几何对数的固定归一化

对固定 `N`，缩时后的全部覆盖轨道对数为

\[
\mathscr L_{V,N}(s)=
\sum_{\widetilde\gamma\ \mathrm{primitive}}
L_{\widetilde T_{\widetilde\gamma}/N}(s).
\]

第 5.2 节的分拆与第 5.1 节的绝对 majorant 使此级数在 `Re(s)>N` 绝对、局部一致收敛；其绝对总和由相应基底 majorant 乘固定 `N^3` 控制。因此可以合法按提升块重排，得到

\[
\mathscr L_{V,N}(s)
=\sum_gc_{N,g}L_{\ell_g/m_{N,g}}(s)
=N^3\mathscr L_N(s).
\]

任意有限覆盖轨道集合的投影只涉及有限多个基底 owner，因此这些完整提升块在全部有限覆盖轨道子集之间共尾；使用完整块没有暗中选取较有利的无限乘积顺序。

定义 `V_N=exp(mathscr L_(V,N))`，则

\[
\boxed{\exp\!\left(N^{-3}\mathscr L_{V,N}(s)\right)
=Q_N(s),\qquad\operatorname{Re}s>N.}
\]

各局部对数沿正实 `s -> infinity` 归零，固定 `N` 的可求和 majorant 允许有限头部／小尾部论证，故 `mathscr L_(V,N)` 也归零。连通半平面上两个全纯对数之差为常数 `2 pi i` 的整数倍，归零条件使该常数为零。因此使用的是唯一的归零全纯对数，不是无说明的 principal Log 或任意 `N^3` 次根。

未缩时的全部覆盖 Euler 产品可写为

\[
U_N(w)=V_N(Nw),\qquad\operatorname{Re}w>1.
\]

这完成固定层、明确半平面内的新无限标量产品及其理论几何连接。H3 的单轨道 Euler 因子仍是规定的乘积约定；本轮没有从谱算子推出它，也没有将这个对象称为谱行列式或整个 `R_+`／Hahn 载体的求值延拓。

## 6. 几何长度截断中的恢复障碍

令任意实序列 `T_k>=0` 满足 `T_k -> infinity`，不要求单调，冻结层数仍为 `N_k=k!`。第 4 节保证 `E(T_k)`、`E_+(T_k)` 都是真正有限的数学集合，并最终保留各自总体中的每个固定 owner。

沿用[正 content 族笔记][family-note]的固定环路常数 `A>0,C_0>0`，其中 `ell_d<=dA+C_0`。在 `k>=2`、`T_k>=2A+C_0` 的尾端，令

\[
D_k=\min\!\left(k,\left\lfloor\frac{T_k-C_0}{A}\right\rfloor\right)\ge2.
\]

则 `g_2,...,g_(D_k)` 都在 `E_+(T_k)` 中，且其 content 均整除 `k!`；同时 `D_k -> infinity`。对任意正实紧区间 `I`，取前一笔记的常数 `c_I>0`，得到

\[
\inf_I Q_{k!,E_+(T_k)}
\ge\exp\!\left[c_I\left(\frac{D_k(D_k+1)}2-1\right)\right],
\]

\[
\inf_I R_{k!,E_+(T_k)}
\ge\exp\!\left[c_I\frac{D_k(D_k-1)}2\right].
\]

两者均趋于正无穷；加入其余正、零因子后，相同下界也适用于 `E(T_k)`。完整集合还最终包含已有零 owner `g_0`，可另外应用它的更强单因子实增长下界。两条证明分别说明零分支和 content 无界正族的作用，不将它们混成一个未定义的形式乘积。

这并未替换冻结规范前缀：`E(T)` 是物理长度阈值的数学集合，不是 `SG2OwnerCanonical-v1` 的字长／字典序前缀，也没有执行原定 `m_k=2^k` 或任何 panel。集合共尾性已在理论上证明，计算它的全部成员、比较边界长度和绑定规范输出仍是不同任务。

### 固定层收敛与层数发散不矛盾

第 5 节固定 `N`、先增加长度截断，在 `Re(s)>N` 得到有限值全纯产品。第 6 节固定正实参数区间，同时令 `N=k!` 和长度阈值增长，得到发散。保证域随 `N` 右移，没有一个固定复数 `s` 属于全部已证明的域，故不能把两句话合并为共同全纯域内的层数极限。

[上一轮的扩展正实上确界][interface-note]仍对每个实数 `s>0` 有定义，可能取无穷。现在当 `s>1` 时，基准 `B(s)` 已由第 5 节证明有限，因此扩展相对乘积可以合法写成扩展 `mathcal Q_N(s)/B(s)`；但这仍不保证每个 `mathcal Q_N(s)` 都有限。一般 `s>0` 继续保留独立的相对乘积定义，不使用 `infinity/infinity`。

## 7. 本轮明确完成与保留的边界

| 项目 | 本轮理论状态 | 仍未取得的证据或对象 |
| --- | --- | --- |
| H1 规定覆盖及塔 | 从同一个真实标记双曲曲面构造，并证明 deck、度数、度量及未缩时流相容 | 具体矩阵／覆盖输入的机器认证 |
| 长度截断及基底指数尾 | 证明有限、共尾、正长度下界及对每个 `a>1` 的指数尾界 | 实际列表、数值常数、边界长度判定、规范枚举证书 |
| 固定层无限几何 Euler 产品 | 在 `Re(s)>N` 构造并完成全部提升块的对数归一化连接 | 精确收敛边界、共同固定参数域、谱行列式或迹公式 |
| 几何截断的实轴恢复 | 任意 `T_k -> infinity` 下的正分支与全分支阶乘截断均绝对及相对发散 | 任意正则化的排除、增长截断的无条件复域结论、正式 Route 结论 |

这里不再把 H1 的抽象存在性、数学长度截断共尾性或基底 `S_0(a)` 写作尚未证明；但也不把这些理论证明当成机器实现、独立科学认证或发表放行。旧笔记记录其当时状态，保留原文不回写。原稿 AN-1–AN-5 的指定域、索引与双序列合同并未由本轮自动完成，正式 `FAIL / BLOCK` 及 Stage 5／6 保持不变。

## 8. 来源与文档核对范围

本轮使用 ARS 的论证流程，分别检错覆盖塔、计数尾界与几何乘積／截断接口，再由主线程整合。同系助手的复核不是独立科学证据。外部来源只承担第 1 节一般覆盖／商表示及第 3 节球面积的指定事实，项目应用和不等式推导写在正文；没有据此声称文献新颖性或重新认证旧的全部 owner 来源。

本轮通过普通浏览核对 Hatcher 章内 PDF 的 Proposition 1.39–1.40（印刷页 71–72），以及 Series 讲义的 Theorem 7.17（印刷页 118）和 Lemma 2.16（印刷页 23）相应解析文本。未逐页通读整本资料，也未生成 human-read 声明。一次 Series 面积页截图获取返回 Internal Error；相关公式已有原 PDF 解析文本，并与正文等价式相符，截图失败保留为显示层限制，不记为成功截图或额外来源认证。没有重试此前已返回 403 的 Utah 路径，没有上传私人稿件或笔记。

仅新增此内部笔记，并在前两份内部笔记和总内部记录追加入口。只读 Node 文档检查核对三个旧文件的原文前缀、十个指定保护文件的原始长度及 SHA-256、局部链接、数学环境配对和必要范围标记。首轮链接正则把公式中的相邻交换子 `[a_1,b_1][a_2,b_2]` 误识别为未定义的 Markdown 引用；诊断定位了这一处误报，改为排除数学环境与行内代码后复核，保留该次失败记录。这类检查是文档保全与结构检查，不认证数学正确性。`git status --short` 返回当前路径不属于 Git 仓库，因此不据此声称工作树干净；保全比较使用编辑前快照。未运行科学实验、owner 枚举、矩阵／长度程序、旧审查脚本或论文构建；未修改论文、代码、结果、锁、正式回执或 Route 判定。

[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[family-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_positive_content_exhaustion_obstruction_20260908.md
[interface-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_infinite_product_interfaces_20260908.md
[hatcher]: https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf#page=51
[series-unif]: https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hyperbolic_geometry_ma448_lecture_notes.pdf#page=135
[series-area]: https://warwick.ac.uk/fac/sci/maths/people/staff/caroline_series/hyperbolic_geometry_ma448_lecture_notes.pdf#page=40

## 追加进展：精确阈值与移动参数主项（2026-09-08）

后续[未缩时覆盖乘积与移动参数极限](internal_unscaled_cover_products_and_moving_parameter_limit_20260908.md)从本笔记的有限位移几何证明全体同调向量及正 content 的线性长度界；结合指定外部素测地线定理，将完整普通乘积的 `Re(s)>N` 由充分域补证为精确绝对收敛域，并处理正实临界点及 `N=1` 的相对例外。在移动参数 `s=Nw`、`Re(w)>1` 下，另得正分支指数趋一、全乘积以零同调子乘积 `B_0(w)^N` 为相对主项、有限字符分解和两种长度截断精度界。这里不是共同固定 `s` 的恢复，也未更换冻结归一化；本笔记保留当时范围原文，数值认证、谱连接与正式状态不变。
