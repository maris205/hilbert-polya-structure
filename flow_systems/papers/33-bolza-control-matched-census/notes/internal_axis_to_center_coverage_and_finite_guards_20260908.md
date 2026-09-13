# P33 内部理论：从轴到中心的全局覆盖与有限 guard

日期：2026-09-08 UTC。本轮只新增内部有界数学笔记，不执行 BP／CP、枚举、实验、旧 fixture 或生产 checker，不修改现稿、旧笔记、输入、合同、guard、状态或 Stage 5／6 边界。固定 `Lambda=21/10`、真实曲面、曲率负一的基底测地长度、磁场锁及外部逆元配对 owner 规则均不变。

[前轮 admission 笔记][admission]证明了两个真实短字的局部判定余量。本轮补充另一条独立责任：在明确的真实基本域及完整邻接前提下，每个短 owner 都能进入一个有限的 identity-connected 候选域。核心链为

\[
\text{短共轭类}
\longrightarrow \text{轴与基本域相交的共轭代表}
\longrightarrow C_{\Lambda+2R}
\subseteq C_T^0
\longrightarrow \text{有限候选的精确 owner 商}.
\tag{1}
\]

中间的共轭移动、邻接覆盖以及末端的精确商均不可省略。本文给出这些箭头成立的充分条件，不把条件性数学定理记成已经运行的普查。

## 1. 一般定理的精确几何前提

在曲率负一的双曲平面中固定基点 `o`，并固定离散、无挠、余紧的定向保持群 `Gamma`。以下 `D` 及邻接前提必须对应同一个真实群作用：

1. `D` 是有非空内部的闭、凸、紧双曲基本多边形，`o in D`。各 `gD` 覆盖双曲平面；不同群元素的 tile 内部互不相交。
2. `D subseteq closed B(o,R)`，其中 `R>0` 有严格的几何界证明。这里 `R` 是双曲半径，不是圆盘模型的欧氏顶点半径。
3. translates 构成 face-to-face 的多边形铺砌。完整的有限对称集合

\[
\mathcal A=\{a\in\Gamma\setminus\{1\}:D\text{ 与 }aD\text{ 共享一条边}\}
\tag{2}
\]

已与实际使用的侧配对字母逐项对应；在顶点处，所有 incident tiles 的有限 star 都按其真实共享边相接。不能把仅仅“生成同一抽象群”的任意字母表当成这个邻接集合。

前两项足以承担轴到中心的代表界；第三项承担下面的邻接路径界。一个精确 relator、近似群条件或旧文件中的 `PASS` 标签，均不单独证明这些前提。实际 P33 模型的来源与冻结矩阵对应沿用[前两轮的明确边界][separation]；本轮不重新进行完整多边形侧／顶点 incidence 的生产认证。

定义中心位移与闭中心球

\[
r_o(g)=d(o,go),\qquad
C_t=\{g\in\Gamma:r_o(g)\le t\},\qquad t\ge0.
\tag{3}
\]

`C_t^0` 表示以 `1` 为起点、在诱导图 `C_t` 内按 `h -> h a`、`a in mathcal A` 可达的连通分量。它不预先等于整个 `C_t`。

## 2. 中心球有限，但短迹不自动给中心界

### 2.1 有限性的直接证明及 CP 的标量含义

将基点移到圆盘模型的 `0`。一个 `SU(1,1)` lift 写作

\[
M_g=\begin{pmatrix}\alpha_g&\beta_g\\
\overline{\beta_g}&\overline{\alpha_g}\end{pmatrix},
\qquad |\alpha_g|^2-|\beta_g|^2=1.
\]

它将 `0` 映到 `beta_g/bar(alpha_g)`。从径向距离 `d(0,z)=2 atanh|z|`，直接得到

\[
\boxed{\cosh^2\!\left(\frac{r_o(g)}2\right)=|\alpha_g|^2.}
\tag{4}
\]

因此 `r_o(g)<=t` 同时界住 `abs(alpha_g)`、`abs(beta_g)`；相应 lift 位于有限维空间中的闭有界集合，因而位于一个紧集。

离散子群在紧集中只能有有限多个元素。具体地，若互异的 `g_n` 在紧集中有收敛子列，则其两两比值可任意接近恒等元，违反恒等元在离散子群中孤立。projective 中心符号只有有限个 lift，不改变结论。因此

\[
\boxed{\#C_t<\infty\quad(t<\infty).}
\tag{5}
\]

同一理由也给出铺砌的局部有限性：若一个紧集 `K` 包含在 `B(o,L)`，且 `hD` 与 `K` 相交，则 `r_o(h)<=L+R`；这样的 `h` 只有有限个。

### 2.2 为什么必须先共轭

平移长度 `ell(g)` 是沿轴实现的最小位移；基点 `o` 不必在轴附近。设 `rho` 是 `o` 到某个双曲元轴的距离，在以该轴为基准的双曲面模型坐标中，计算两点的 Lorentz 内积可得

\[
\cosh r_o(g)
=\cosh\ell(g)+\bigl(\cosh\ell(g)-1\bigr)\sinh^2\rho.
\tag{6}
\]

例如取 `o=(cosh rho,0,sinh rho)`，平移后为 `(cosh rho cosh ell,cosh rho sinh ell,sinh rho)`，即得 (6)。固定正的 `ell` 而增加轴到基点的距离，中心位移可任意大。

所以 `abs(tr(g))<=2 cosh(Lambda/2)` 是平移长度条件，不是 `abs(alpha_g)^2` 的中心 guard。这里的反例说明一般几何推理不能省略共轭步骤；它不授权移动真实 P33 模型或基点。

## 3. 轴到中心：每个短类都有有限球内代表

**定理 1。** 在 §1 的前两项几何前提下，若双曲元 `g` 满足 `ell(g)<=Lambda`，则它有共轭代表 `h` 满足

\[
\boxed{r_o(h)\le\Lambda+2R=:S.}
\tag{7}
\]

**证明。** 在 `g` 的轴上任选一点 `p`。由基本域覆盖，存在 `k in Gamma` 使 `p in kD`。令

\[
q=k^{-1}p\in D,\qquad h=k^{-1}gk.
\]

`q` 在 `h` 的轴上，故 `d(q,hq)=ell(h)=ell(g)`。三角不等式及等距性给出

\[
\begin{aligned}
d(o,ho)
&\le d(o,q)+d(q,hq)+d(hq,ho)\\
&=2d(o,q)+\ell(g)\le2R+\Lambda.
\end{aligned}
\]

轴点落在基本域边界也不影响证明；只需选任意一个含它的闭 tile，不需要唯一选择。□

共轭保持本原性、平移长度及外部逆元配对 owner。因而每个 cutoff 内的本原 owner 至少有一个代表在有限集 `C_S` 中。这不表示该 owner 的所有词表示或所有共轭代表都在 `C_S` 中，也不表示 `C_S` 中不同元素一定属于不同 owner。

## 4. 完整顶点 star 给出不扩大常数的邻接路径

**定理 2。** 再假设 §1 的完整铺砌／邻接前提。若 `r_o(g)<=S`，则存在从 `D` 到 `gD` 的边邻接路径，其每个 tile `hD` 都满足

\[
\boxed{r_o(h)\le S+R.}
\tag{8}
\]

因此，只要 `T>=S+R`，就有

\[
\boxed{C_S\subseteq C_T^0.}
\tag{9}
\]

**证明。** 取闭测地线段 `L=[o,go]`。它位于闭球 `B(o,S)` 中：沿这条从 `o` 出发的线段，距 `o` 的距离就是已经走过的弧长。

令 `mathscr T(L)` 为所有与 `L` 相交的闭 tiles。若 `z in L cap hD`，则 `d(z,ho)<=R`，故

\[
d(o,ho)\le d(o,z)+d(z,ho)\le S+R.
\]

由 (5)，`mathscr T(L)` 有限，并包含 `D` 与 `gD`。

每个 `L cap hD` 都是非空闭区间或单点；它们覆盖连接的线段 `L`。这些区间的相交图必连接：若分成两个互不相交的图分量，两组有限闭区间的并就会把 `L` 分成两个不相交的非空闭集，矛盾。

还须把“在一个点相交”转成真正的边邻接。对任意 `z in L`：

- 若 `z` 在一个 tile 内部，只涉及该 tile。
- 若 `z` 在边的相对内部，两侧 tiles 共享该边。
- 若 `z` 是铺砌顶点，含 `z` 的有限 tiles 按局部扇形环绕 `z`；相邻扇形共享从 `z` 发出的边，因而该完整 star 的边邻接图连接。

最后一项来自 face-to-face 的真实多边形铺砌：局部扇形内部不重叠并填满一个小圆邻域。把区间相交图中的每次顶点跳跃替换成这个有限 star 内的边邻接路径。所有插入 tiles 仍含 `z in L`，所以仍满足 (8)。线段沿边行走、触碰顶点或只在端点接触某 tile 的情况也被同一论证覆盖。

每条真实邻接边为 `hD -> h a D`，`a in mathcal A`。故所得路径完全位于 `C_(S+R)` 中，证明 (9)。□

此证明没有用未定大小的 `epsilon` 扰动，也没有把安全界从 `S+R` 改成 `S+2R`。但代价是必须拥有真实、完整的侧邻接及顶点 star 前提；不完整的邻接列表不能享有此结论。

若实现采用左乘而非右乘，须同步绑定其约定。对称字母表下，取逆把右乘路径转成左乘路径，且 `r_o(h^-1)=r_o(h)`；将该论证应用于 `g^-1` 即得同样的覆盖。这个对称性不替代实现与合同之间的明确版本／约定核对。

### 4.1 有限性与 FIFO 完备性仍是两条不同的证据

考虑一个满足以下**语义条件**的 BFS：从恒等元开始；每个已接纳状态恰处理一次；遍历全部 `mathcal A` 邻居；以精确 `r_o<=T` 判断是否在域内；去重当且仅当表示同一个 `PSU` 群元素；所有域内新状态入队。

因为 `C_T` 有限，且每个顶点只有有限个邻居，这个语义 BFS 在每次判定都能正确终止的前提下会耗尽队列。反过来，若完整边记录证明队列已耗尽，就不能遗漏 `C_T^0` 中的任何顶点：从 `1` 到一个所谓遗漏顶点的路径上，取第一个遗漏者，其前驱已处理，应已将它加入，矛盾。

结合 (7)、(9)，取

\[
T\ge\Lambda+3R
\tag{10}
\]

便足以让这个完整有限 component 覆盖每个短 owner 的某个代表。这里不需要、也没有证明整个外层 `C_T` 都连接。只证明“某个中心球有限”或“某次队列为空”，都不能单独替代上述全部语义条件。

## 5. 有 certified separation 时的有限 packing 界

假设另有一个经过证明的常数 `delta>0`，满足

\[
d(o,go)\ge\delta\qquad(g\ne1).
\tag{11}
\]

则不同中心 `go,ho` 的距离至少为 `delta`。半径 `delta/2` 的开球两两不交；以 `C_T` 中中心为球心的这些球全部包含于 `B(o,T+delta/2)`。

曲率负一的极坐标面积元为 `sinh r dr dtheta`，故半径 `r` 的球面积是 `2 pi(cosh r-1)`。比较面积得到

\[
\boxed{
\#C_T\le
\frac{\cosh(T+\delta/2)-1}{\cosh(\delta/2)-1}.
}
\tag{12}
\]

若给的是基点 injectivity radius 的严格下界 `rho_0>0`，可以用 `delta=2rho_0`。另一条充分路线是证明 `B(o,r_0) subset int(D)`：各 translate 的这类开球互不相交，便有中心间距至少 `2r_0`。

定理 (5) 不要求显式给出 `delta`；但一个可交付的数值资源上界若采用 (12)，必须实际认证其 `delta`。两个短见证的长度是 systole 的上界方向，不能未经证明就拿来充当控制群的中心 separation 下界。

若 `N_max` 是 (12) 右端的一个经证明的整数上界，而 `q=|mathcal A|`，则该 component 的简单发现路径长不超过 `N_max-1`，且处理所有已接纳状态至多需要 `q N_max` 个有向边检查。这不认证旧对象中的 `18533` 个状态、最深 `11` 层或任何历史流摘要；这些仍是要按合同重播的独立实例证据。

## 6. 与冻结 CP guard 的逐项对应

### 6.1 读取了什么，没有把什么当成证明

[CP 合同][cp-contract]固定：

- 精确控制矩阵来自[冻结矩阵对象][control-input]。
- guard 来自[冻结 finite-ball 对象][finite-input]，为 `abs(alpha)^2<=20000`。
- 遍历是 identity-connected component，FIFO 字母次序为 `g0,g1,g2,g3,g0^-1,g1^-1,g2^-1,g3^-1`。
- 必须有精确去重、队列耗尽、全部 outgoing edges 分类，以及独立的 bound／coverage／digest／unresolved replay。

finite-ball 对象另存有 `2 atanh(u)<3` 和 `cosh(111/20)^2<20000` 的 guard 条目。本轮读取这些公式，但不采用其 `PASS`、`PROVED`、状态数、旧流摘要或“已证完整”的文字作为本定理的证明。

### 6.2 固定参数下的半径与 guard：直接有理数证明

对 S01 锁定八边形，两个欧氏顶点半径是

\[
u=e^{-1/10},\qquad b_{\rm geom}=\frac1{\sqrt2u}.
\]

`u^4=e^(-2/5)>1-2/5=3/5>1/2`，故 `b_geom<u`。若 `D_C` 已按 §1 识别为该真实凸基本八边形，它的所有顶点距 `0` 均不超过 `2 atanh u`。双曲闭球测地凸，因此整个 `D_C` 也在该球中；这里 `b_geom` 不替换项目磁场参数。

Taylor 二阶上界和指数正项下界给

\[
u<1-\frac1{10}+\frac1{200}=\frac{181}{200},
\qquad
e^3>\sum_{n=0}^{9}\frac{3^n}{n!}
=\frac{22471}{1120}>\frac{381}{19}.
\tag{13}
\]

最后的有理数比较为 `22471*19-381*1120=229>0`。从而

\[
\tanh(3/2)=\frac{e^3-1}{e^3+1}
>\frac{181}{200}>u,
\qquad \boxed{2\operatorname{atanh}u<3.}
\tag{14}
\]

因此 `R=3` 是该几何识别前提下的有效上界。把这个上界代入一般定理，得到

\[
S=\Lambda+2R=\frac{81}{10},\qquad
S+R=\Lambda+3R=\frac{111}{10}.
\tag{15}
\]

现直接证明 (15) 在冻结 `20000` guard 内。由 `n!>=2*3^(n-2)`、`n>=2`，且从 `n=4` 起严格，

\[
e=2+\sum_{n=2}^{\infty}\frac1{n!}<\frac{11}{4},
\qquad e^{1/10}<\sum_{n=0}^{\infty}(1/10)^n=\frac{10}{9}.
\]

又 `(11/4)^3=1331/64<21`、`(11/4)^2=121/16<31/4`，故

\[
e^{111/10}
<21^3\frac{31}{4}\frac{10}{9}
=\frac{159495}{2}.
\]

使用 `e^(-111/10)<1`，得到

\[
\boxed{
\cosh^2(111/20)
=\frac{e^{111/10}+2+e^{-111/10}}4
<\frac{159501}{8}<20000.
}
\tag{16}
\]

这独立给出了所需的标量不等式，不运行旧 interval writer，也不复用其数字输出。

### 6.3 条件性的完整覆盖结论，仍不是运行回执

令

\[
T_{\rm CP}=2\operatorname{arcosh}\sqrt{20000}.
\tag{17}
\]

由 (4)，冻结 `abs(alpha)^2<=20000` 正是 `r_0(g)<=T_CP`，不是 translation-length guard。由 (15)–(16)，`111/10<T_CP`。因此，**如果**该控制基本八边形及八个字母已满足 §1 的全部几何／邻接前提，则

\[
\boxed{
C_{81/10}\subseteq C_{T_{\rm CP}}^0,
\quad\text{每个 }\ell\le21/10\text{ 的短 owner 有代表在此 component 内。}
}
\tag{18}
\]

对应关系不能混写：

| 本文对象 | 冻结对象中的对应 | 本轮所承担的责任 |
| --- | --- | --- |
| `R=3` | `proof_guards.fundamental_polygon_radius` 的半径公式 | 重证固定参数不等式；真实凸基本域／顶点对应仍为明确前提 |
| `S=81/10` | 短类的一个 based-center 代表界 | 定理 1 的共轭步骤；不是 cutoff 本身 |
| `S+R=111/10` | `proof_guards.center_radius_guard` 中 `111/20` 的两倍 | 定理 2 的完整 star 邻接路径界 |
| `T_CP` | `center_guard_alpha_squared=20000` | (4)、(16) 将几何路径放进原 guard，不扩大 guard |
| `C_(T_CP)^0` | 合同的 identity-connected component | 全部侧邻居、精确去重及所有边分类后，才有实例遍历证书 |

每条保证覆盖所需的路径还满足 `abs(alpha)^2<159501/8`，与 guard 的间隔大于 `499/8`。因此，若某条路径状态的 `abs(alpha)^2` 有正确绑定的有效区间，且宽度不超过 `499/8`，其上端点必小于 `20000`。这只是标量判定余量，不证明所有外层状态远离 guard 边界。

尤其，[前轮][admission]的两因子 trace 误差预算既不是任意长字的误差预算，也不是 `abs(alpha)^2` 的误差预算。没有该量自己的包围证明，就不能以“前轮 admission 已可靠”为由让本轮 BFS 自动接受状态。

## 7. 从候选覆盖到 owner census 还差什么

若已经正确、完整地获得 `C_T^0`，再假设对其中每个元素都有完整的精确 hyperbolicity、cutoff、本原性、共轭与逆向配对判定，则

\[
\{g\in C_T^0:g\text{ 双曲、本原且 }\ell(g)\le\Lambda\}
\big/\{\text{完整群共轭与外部逆元配对}\}
\ \cong\ \mathcal O_\Gamma(\Lambda).
\tag{19}
\]

满射来自 (7)、(9)；单射来自真实的 owner 等价关系。不能用相同 trace、相同长度、相同同调或有限 component 内未找到共轭子来替代最后的等价关系。本原性也必须相对于完整 `Gamma`，不是“在有限候选中没找到根”。

本轮未实施上述判定或生成该商。具体保留的义务是：真实基本域和完整侧／顶点 incidence 的版本绑定；实际状态编码与 `PSU` 元素身份的双向正确性；每次 guard 比较的确定结论；队列和全部边的可重播记录；一般 root／conjugacy／inverse 证书；包含 cutoff 等号情形的完整处置；排序流、摘要与零 unresolved ledger。有限数学宇宙本身不证明这些 checker 已实现或每个所选数值方法会终止。

[BP 合同][bp-contract]没有采用 CP 的中心 BFS；它只授权另外冻结并重播的 strict-systole gate 后输出 empty stream。一般定理可以说明另一种数学覆盖路线，但本轮不将 BP 静默迁移到这条路线，也不把其版本空槽或 observed digest 填上。

因此本轮的新增结论是：固定 guard 的候选覆盖可以被明确地分解为轴到中心、完整 star 邻接及有限遍历三项，并且原 `20000` 数值 guard 在这些几何前提下足够；不是完整 CP/BP 运行、owner 数值普查、Route 晋级或 Stage 5／6 解锁。

## 8. 来源、动作和保全

本轮使用 ARS argument-builder，按自含命题、证明、反例和责任分工推进内部理论，不启动 full pipeline 或正式 reviewer 阶段。已完整读取当轮 `AGENTS.md`、`docs/workflow.md`、ARS router／academic-paper workflow／argument-builder role，以及 BP／CP 合同和相应冻结输入的 guard 内容。来源支持与几何识别沿用[此前记录][separation]；本文新的中心界、图覆盖、packing 和有理数比较均给出直接证明，没有新增外部文献主张或重新访问失败来源。

仅用 `apply_patch` 新增和修订本文件。其余动作限于只读定位、读取、保护文件 SHA-256 及文本结构检查；没有科学计算、矩阵数值 replay、程序化枚举、producer、fixture、外部 API、上传或正式状态更新。写后确认两份前轮笔记、现稿、两个合同和三个冻结输入共八项 SHA-256 与写前一致；`node -e` 检查确认六个引用定义、八处引用使用、全部本地目标、26 对显示数学分隔符、连续 (1)–(19) 公式标签及控制字符检查通过。文件保全和同伴只读复核均不构成独立科学认证。

[admission]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_strict_cutoff_margins_and_sound_admission_20260908.md
[separation]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_cutoff_separation_proof_obligations_20260908.md
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[control-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json
[finite-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json
