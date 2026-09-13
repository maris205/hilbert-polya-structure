# Paper31 D05：二项式格理想的整数消费者 V1

日期：2026-09-09 UTC；作者：主控 `/root`。`route_applicability: NOT_APPLICABLE`。
本件分开证明显式整数理想的结论与假设原格身份后的消费者，不预先接受尚在推导的原留数桥梁。

## Claim and Status

令 $n\ge1$、$N=n-1$，对 $0\le a\le N$ 定义 $R=\mathbb Z[\tau]$ 中的理想
$$I_{n,a}=\left(\binom{N-b}{a}\tau^b:0\le b\le N-a\right).\tag{1}$$
对任意素数 $p$，置 $A_p=R_{(p,\tau)}$。约定 $v_p(1)=0$，此处所有二项系数均为正整数。
定义
$$d_p(N,a)=\min\left\{b\ge0:b\le N-a,\ p\nmid\binom{N-b}{a}\right\},\quad
D_n(p)=\sum_{a=0}^{N}d_p(N,a),\quad D_0(p)=0.\tag{2}$$

**C1（完整格缺陷）。** 对每个 $(n,a,p)$，$I_{n,a}^{**}=A_p$（采用既定 $I\subset A_p$ 嵌入），
且 $E_{n,a}=A_p/I_{n,a}A_p$ 的完整整数系数层由
$$e_b=\min_{0\le j\le b}v_p\binom{N-j}{a}\quad(0\le b<N-a),\qquad
E_{n,a}\cong\bigoplus_{b=0}^{N-a-1}\mathbb Z_{(p)}/(p^{e_b})\cdot\tau^b\tag{3}$$
给出；(3) 是 $\mathbb Z_{(p)}$-模分解，$\tau$ 作用为相邻系数的自然投影，末项送零。
从而 $\dim_{\mathbb F_p}E_{n,a}[p]=d_p(N,a)$。

**C2（素数首次非自由）。** $D_n(p)=0$ 对所有 $1\le n\le p$；$D_{p+1}(p)=p-1$。
更准确地，在 $n=p+1$ 时，$I_{n,0}=I_{n,p}=A_p$，而全部 $1\le a\le p-1$ 都有 $I_{n,a}A_p=(p,\tau)$。
一般 $(n,a)$ 的 $d_p(N,a)$ 可由下面无进位的基 $p$ 数字规则准确决定，不限首次次数。

**C3（原格身份下的条件性扭长）。** 假设下文 H1–H3 的原模及次数连接身份都成立，则对每个域 $k$
$$\operatorname{length}_{k[[\tau]]}\operatorname{Tor}_{\tau}(M_n\otimes_R k[[\tau]])=
\begin{cases}
\displaystyle\sum_{j=1}^{n-1}j^2,&\operatorname{char}k=0,\\
\displaystyle\sum_{j=1}^{n-1}j^2+D_n(p),&\operatorname{char}k=p>0.
\end{cases}\tag{4}$$
所以在这些身份成立时，全素数首次扭长增加恰在 $n=p+1$，增量恰为 $p-1$。
该增量相对**同次数的特征零值**，不是相邻次数长度的增量。

`Status: PROVABLE AS STATED` 对 C1–C2；C3 是 `CONDITIONAL_THEOREM`，本件证明 H1–H3 蕴含 (4)。
不在本件中给原对象自动解除 H2–H3，不宣称原完整模块分块或全部 Smith 指数。

## Assumptions and Notation

H1. $M_0=0$，全部 $M_n$ 是有限呈示 $R$-模，且有实际短正合列
$$0\to M_{n-1}\xrightarrow{\iota_{n-1}}M_n\to R\oplus\bigoplus_{r=1}^{2}\bigoplus_{j=1}^{n-1}R/(\tau^j)\to0.\tag{5}$$
H1 的几何身份已由[相邻扩张接受][ACCEPT]供应；本件只使用 (5) 的明确代数内容。

H2. 在逆 $\tau$ 后有 $R[\tau^{-1}]$-同构 $\rho_n:M_n[\tau^{-1}]\to R[\tau^{-1}]^n$，
并且在同一既定坐标下，原 $M_n$ 的像准确等于
$$L_n:=\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a}.\tag{6}$$
不只要求某个与右侧抽象同构的模；包含映射和嵌入标架亦在假设中。

H3. 原 $s_0$ 次数连接在这些坐标中准确为
$$\rho_n(\iota_{n-1}m)=(0,\rho_{n-1}(m)_0,\ldots,\rho_{n-1}(m)_{n-2}).\tag{7}$$
特别地，除去各自公共 $\tau^{-n}$ 后是 $\tau$ 倍移位，不是无移位包含。
H2–H3 是另件正在证明的原 residue／格引理之义务，不由本件的组合恒等式提供。

$E[p]=\ker(p:E\to E)$；双对偶均相对 $A_p$。零模的长度为0，空直和和空和均为0。
特征0中下文可记 $D_n(0)=0$ 统一公式，但0不是素数。

## Proof Strategy and Dependency Map

1. 将 (1) 局部化后按每个 $\tau^b$ 的整数系数理想精确求商，得到 C1。
2. 由 $(1+X)^p=1+X^p$ 在特征 $p$ 中的恒等式证明数字规则，再处理首次次数，得到 C2。
3. 从 H1 证明整数无扭；在 H2 的实际格中按特征计算 free-image 指数；
   利用 H3 与 (5) 的真实商，得到扭长递推并望远镜求和。
4. 标准整数理想、二项系数和 DVR 长度计算不自带原几何身份或新意分。

## Proof

### Step 1. 理想及其双对偶的归一化

令 $d=N-a$。生成元 $b=d$ 为 $\tau^d$；生成元 $b=0$ 为非零整数 $\binom Na$。
若 $d=0$ 或 $a=0$，理想已经是单位理想。否则两者无公共非单位因子，因为 $\tau$ 不整除任何非零整数。
在 UFD $A_p$ 中，若分式 $c$ 满足 $cI\subset A_p$，其约分分母必须同时整除 $\tau^d$ 与 $\binom Na$，所以是单位。
因此 $I^*=A_p$、$I^{**}=A_p$，自然双对偶映射就是原包含。
这里没有把抽象同构的主理想 $cI$ 当成同一个嵌入；该归一化是后续行列式消费者必需的条件。

### Step 2. 每个整数系数层的精确描述

记 $c_j=\binom{N-j}{a}$。在 $\mathbb Z_{(p)}[\tau]$ 中，(1) 的任意元素之 $\tau^b$ 系数属于
由 $c_0,\ldots,c_{\min(b,d)}$ 生成的整数理想；反过来，这些整数线性组合乘以相应 $\tau^{b-j}$ 都由 (1) 生成。
所以在次数 $b<d$，系数理想准确为 $(p^{e_b})$；在 $b\ge d$ 为单位理想。
$e_b$ 非负且随 $b$ 不增。商的每个系数可独立取模 $p^{e_b}$，得到 (3)，没有跨 $\tau$ 次的隐藏关系。
该商被 $p^{e_0}$ 和 $\tau^d$ 消灭，故若非零就已是以 $(p,\tau)$ 为唯一极大理想的 Artin 环；
把底环再局部化到 $A_p$ 不改变此商。各相邻系数的 $\tau$ 作用正是自然投影，因 $e_{b+1}\le e_b$ 而良定。

一个非零循环群 $\mathbb Z_{(p)}/(p^{e_b})$ 的 $p$-核是一维 $\mathbb F_p$ 空间，零循环群没有贡献。
由 $e_b>0$ 当且仅当 $p\mid c_j$ 对全部 $0\le j\le b$ 成立，正的系数层数量正好是首个 $p\nmid c_j$ 的位置。
这个位置存在，因为 $c_d=1$。故 $\dim E_{n,a}[p]=d_p(N,a)$，C1 得证。

### Step 3. 数字规则及首个素数次数

对非负整数 $m$，写基 $p$ 展开 $m=\sum_i m_ip^i$。在 $\mathbb F_p[X]$ 中，Frobenius 恒等式反复给出
$$ (1+X)^m=\prod_i(1+X^{p^i})^{m_i}.$$
每个右侧因子的指数选择在 $0,\ldots,m_i<p$ 中，故选择后的和已经是唯一基 $p$ 展开。
比较 $X^a$ 系数，得到
$$\binom ma\equiv\prod_i\binom{m_i}{a_i}\pmod p.$$
右侧非零当且仅当所有 $a_i\le m_i$；若 $a_i>m_i$，该因子为0。
因此
$$d_p(N,a)=N-\max\{m\le N: a_i\le m_i\text{ 对所有基 }p\text{ 数字成立}\}.\tag{8}$$
集合非空，因为 $m=a$ 可取；(8) 完整覆盖一般次数，不要求预先假设首现规律。

若 $N<p$，所有 $\binom Na$ 都非零模 $p$，故每个 $d_p(N,a)=0$。
若 $N=p$，端点 $a=0,p$ 的常数均为1。对 $1\le a\le p-1$，
$\binom pa$ 的 $p$ 赋值准确为1，而 $\binom{p-1}{a}\not\equiv0\pmod p$。
因此对应理想由常数给 $(p)$、一次项给 $(\tau)$，其余生成元已在 $(p,\tau)$ 中，准确等于 $(p,\tau)$。
每个中间 $a$ 的 $d_p(p,a)=1$，共 $p-1$ 项。这证明 C2，包含 $p=2$ 的唯一中间项。

### Step 4. 专门化保留真实相邻正合列

H1 中的商 $Q_n=R\oplus2\bigoplus_{j=1}^{n-1}R/(\tau^j)$ 没有任何整数素数扭子。
因此 $\operatorname{Tor}_1^R(Q_n,R/(p))=\ker(p:Q_n\to Q_n)=0$，(5) 模 $p$ 后仍短正合。
特征0先作平坦的有理数张量；再扩任意域 $k$、完成到 DVR $O_k=k[[\tau]]$ 均为平坦操作。
故对每个域 $k$，都有
$$0\to M_{n-1,k}\to M_{n,k}\to Q_{n,k}\to0,\qquad M_{n,k}=M_n\otimes_R O_k.\tag{9}$$
同一整数无扭性也从 $M_0=0$ 和 (5) 逐步传给全部 $M_n$，但 (9) 的论证不需要预先假设取扭子与张量交换。

H2 的逆 $\tau$ 同构经基变换给 $M_{n,k}[\tau^{-1}]\simeq k((\tau))^n$。
令 $T_{n,k}$ 为 $M_{n,k}$ 的全部 $\tau$-扭子，$F_{n,k}$ 为它在该向量空间中的实际像。
局部化的核恰为被某个 $\tau$ 幂消灭的元素，故准确有
$$0\to T_{n,k}\to M_{n,k}\to F_{n,k}\to0.$$
由 (6) 的原像生成元，$F_{n,k}$ 等于原系数理想在 $O_k$ 中生成的像；
这使用 $M_n\twoheadrightarrow L_n$ 的右正合张量和随后映入 $k((\tau))^n$，不声称 $L_n\otimes O_k$ 自身无扭。

在特征0，每个理想的常数生成元都是非零单位，所以 $F_{n,k}=\tau^{-n}O_k^n$。
在特征 $p$，首个非零模 $p$ 系数的位置正是 $d_p(N,a)$，在 DVR 中它生成 $\tau^{d_p(N,a)}O_k$；
故统一写成
$$F_{n,k}=\bigoplus_{a=0}^{n-1}\tau^{-n+d_{n,a}(k)}O_k,\quad
d_{n,a}(k)=\begin{cases}0&\operatorname{char}k=0,\\d_p(n-1,a)&\operatorname{char}k=p.\end{cases}\tag{10}$$
每个 $F_{n,k}$ 在 DVR 上自由秩为 $n$；原整数格不自由与此不矛盾。

### Step 5. 自由格指数的准确次数移位

为核对整数包含，Pascal 公式给出
$$\tau^{b+1}\binom{N-1-b}{a}
=\tau\left(\tau^b\binom{N-b}{a+1}\right)
-\tau^{b+1}\binom{N-1-b}{a+1}.\tag{11}$$
最后一项超出非零范围时其二项系数为0。(11) 对全部旧生成元成立，故
$\tau I_{n-1,a}\subset I_{n,a+1}$。这是 H3 所声称原移位的代数相容性核对，不单凭 (11) 证明原映射就是该移位。

由 H3 和 (10)，$F_{n-1,k}\to F_{n,k}$ 在第 $a+1$ 坐标的包含指数为
$$h_{n,a}(k)=1+d_{n-1,a}(k)-d_{n,a+1}(k)\ge0\qquad(0\le a\le n-2).$$
非负性也由 (11) 专门化直接给出。新第0坐标是自由商，且 $d_{n,0}(k)=0$。
因此格商 $G_{n,k}=F_{n,k}/F_{n-1,k}$ 的自由秩为1，扭子长度准确为
$$\kappa_n(k)=\sum_{a=0}^{n-2}h_{n,a}(k)
=(n-1)+D_{n-1}(k)-D_n(k).\tag{12}$$
其中 $D_n(k)=0$ 在特征0、$D_n(k)=D_n(p)$ 在特征 $p$；$n=1$ 的空和为0。
这正是原相邻商的扭子不能全部累加到 $T_{n,k}$ 的那部分指数。

### Step 6. 蛇形引理与扭长递推

将 (9) 与 $0\to F_{n-1,k}\to F_{n,k}\to G_{n,k}\to0$ 组成交换图。
前两个竖直映射是定义中的满射，第三个商映射因而也是满射。
蛇形引理给出
$$0\to T_{n-1,k}\to T_{n,k}\to Q_{n,k}\to G_{n,k}\to0.\tag{13}$$
令 $K$ 为最后满射的核。$Q_{n,k},G_{n,k}$ 自由秩均为1，所以 $K$ 为扭子。
在 DVR 上该满射诱导无扭商间的满射 $O_k\to O_k$，即乘一个单位；
任意 $G_{n,k}$ 的扭子元素之原像的无扭坐标因此必须为0。
故其扭子间亦有短正合列
$$0\to K\to\operatorname{Tor}_{\tau}Q_{n,k}\to\operatorname{Tor}_{\tau}G_{n,k}\to0.$$
由 (13)，$\operatorname{length}T_{n,k}-\operatorname{length}T_{n-1,k}=\operatorname{length}K$。
H1 给 $\operatorname{length}\operatorname{Tor}_{\tau}Q_{n,k}=2\sum_{j=1}^{n-1}j=n(n-1)$，
再用 (12) 得
$$\operatorname{length}T_{n,k}-\operatorname{length}T_{n-1,k}
=(n-1)^2+D_n(k)-D_{n-1}(k).$$
从 $M_0=0,D_0(k)=0$ 逐次相加，右侧的 $D$ 项望远镜相消，即得 (4)。
结合 Step 3 的 C2，给出全部素数的首次差异和准确增量；这始终以 H2–H3 已成立为前提。∎

## Open Risks and Scope

C1–C2 是显式整数理想本身的结论；H2–H3 尚需原上同调／标架／连接的实际证明与独立核验。
新意必须扣除标准数字二项式、整数理想及自由格方法，不能因写出总和公式就把原未证接口视为自动成立。
完整缺陷的 (3) 描述各整数系数层及 $\tau$ 作用；它不是原 $M_n$ 的完整直和分解，也不确定全部原扭子 Smith 指数。
尚未以本件授予原全部 Fitting；另件一般行列式理想工具须分别证明和合取，不能反向以目标乘积倒证原格。
本件已全文自读并固定准确次数移位；待独立检查 C1–C3 的实际新证明，尤其 (9) 的 Tor、(10) 的像与 (13) 的格指数扣除。
本件无CPU/GPU运行、参数扫描或浮点数据，不改变两项原固定诊断对象。
既有 Paper30、旧全素数强猜式及所有冻结失败件均不修改；全原整模直和仍未由本件给出。

[ACCEPT]: PAPER31_QPI_TWO_DIAGNOSTICS_DISPOSITION_V1_20260909.md
