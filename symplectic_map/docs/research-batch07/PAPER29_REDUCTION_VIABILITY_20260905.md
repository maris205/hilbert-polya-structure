# Paper29 分离乘积剪切：约化与积分完备性可行性调查

日期：2026-09-05。性质：有界作者侧调查／证明输入，不是独立终审，不授予新颖性或产物验收。仅写本文件；不创建论文项目。采用 `proof-writer` 与 `research-lit`；纯结构问题，`route_applicability: NOT_APPLICABLE`。

## Claim / Status / Assumptions

**总判定：PROVABLE AS STATED（下列明确限定的代数命题）；选题价值仍为 PARTIAL。**

令基域为 $\mathbb C$，$r\ge3$，$f,g\in\mathbb C[t]$ 都非恒定，$m=\deg f$、$n=\deg g$。在 $\mathbb A^{2r}$ 上记
$$
Q=\prod_iq_i,\quad P=\prod_ip_i,\quad x_i=q_ip_i,\quad c_i=x_i-x_r,\quad c_r=0,
$$
$$
S_f(q,p)_i=(q_i,p_i+f'(Q)\prod_{j\ne i}q_j),\qquad
T_g(q,p)_i=(q_i+g'(P)\prod_{j\ne i}p_j,p_i),\quad F=T_gS_f.
$$
这里两个加号是对象定义；按通常 Hamiltonian 符号约定，一步分别对应带适当正负号的 Hamiltonian 时间一流。记 $A=rm-1$、$B=rn-1$、$L=AB>1$。

| 命题 | 当前科学状态 |
| --- | --- |
| 全仿射分类商、固定动量曲面及边界正则延拓 | PROVED，§1 |
| $\deg F^k=L^k$，无系数一般性限制 | PROVED，§2 |
| 每个固定动量商曲面上没有周期仿射代数曲线 | PROVED，§3；核心极点论证来自主代理，本调查独立检查 |
| 对每个 $N\ge1$，全部高维有理积分为 $\mathbb C(c_1,\ldots,c_{r-1})$ | PROVED，§4；不是仅环面不变积分 |
| 两个单剪切的共同积分及动量碰撞层的共同积分 | PROVED，§5 |
| 商曲面的内禀坐标次数指数增长率为 $L$ | PROVED，§2 |
| 将后一增长率正式识别为任意光滑射影模型的第一动力次数 | PARTIAL：需正文补比较引理或准确引用，不影响§3–4 |
| 重复动量层上单个 $F^N$ 的全部有理积分分类 | PROVED，§5末的追加论证；需独立审查 |
| 文献原创性 | OPEN，本报告不宣称已解决 |

## Proof Strategy / Dependency Map

1. 环面权的单项式正规形给全局商；动量互异时给显式局部平凡化。
2. 无穷远极点的两个严格增长区域排除商曲面周期曲线，不依赖动力次数分类定理。
3. 泛动量层的素元局部化给 UFD 与平凡单位；分式积分转成多项式特征函数。
4. 按环面权分解特征函数，其零除子下降为周期曲线，产生矛盾。
5. 单剪切共同积分另由导子括号的 Vandermonde 矩阵直接决定；不能用这一较弱结论替代第4步。

## 1. PROVED：分类商与真正的全局边界

令 $T=\{(t_i)\in(\mathbb C^*)^r:\prod_it_i=1\}$，作用为 $q_i\mapsto t_iq_i$、$p_i\mapsto t_i^{-1}p_i$。单项式 $q^\alpha p^\beta$ 不变，当且仅当所有 $\alpha_i-\beta_i$ 相等。若共同值非负，单项式是 $Q$ 的幂乘 $x_i$ 的单项式；若为负则用 $P$。因此
$$
\mathbb C[q,p]^T=\mathbb C[x_1,\ldots,x_r,Q,P]/(QP-\prod_ix_i).
$$
这也是全部关系：先用该关系消去同时含 $Q,P$ 的项，再嵌入 $\mathbb C[x_i,Q^{\pm1}]$，不同 $Q$ 幂线性独立。故该谱是整个仿射空间的分类商，不仅是 $QP\ne0$ 图册。

固定 $c$ 后令 $x=x_r$、$h_c(x)=\prod_i(x+c_i)$，动量层与分类商分别为
$$
M_c=\operatorname{Spec}\frac{\mathbb C[x,q_i,p_i]}{(q_ip_i-x-c_i)_i},\qquad
D_c=\{QP=h_c(x)\}.
$$
$M_c$ 对所有 $c$ 都整。证明：每个单项式先消去同指标的 $q_ip_i$；将正规形送入 $\mathbb C[x,q_1^{\pm1},\ldots,q_r^{\pm1}]$，用 $p_i=(x+c_i)/q_i$，不同 $q$ 指数向量独立，同一向量的系数乘非零多项式，故映射单射。环面权分次还表明取固定动量理想后再取不变量，与先取不变量再取该理想相同。

写 $d=Qf'(Q)$。约化剪切不是带未定义除法的形式映射，而是
$$
S_f:(Q,P,x)\mapsto
\left(Q,\ P+\frac{h_c(x+d)-h_c(x)}Q,\ x+d\right).
$$
差商属于 $\mathbb C[Q,x]$，因为 $d$ 被 $Q$ 整除。$T_g$ 交换 $Q,P$ 并将 $d$ 换为 $Pg'(P)$；逆映射用 $-f,-g$。所以边界上也为正则自同构。

当 $c_i$ 两两互异，$M_c\to D_c$ 是全域 Zariski 局部平凡 $T$-torsor。具体地，
$$
U_i=\{H_i(x):=\prod_{j\ne i}(x+c_j)\ne0\}
$$
覆盖 $D_c$。在 $U_i$ 上任取 $q_j\in\mathbb G_m$（$j\ne i$），唯一恢复
$$
q_i=Q/\prod_{j\ne i}q_j,\quad p_j=(x+c_j)/q_j,\quad
p_i=P\prod_{j\ne i}q_j/H_i(x).
$$
该式包括 $Q=P=0$；所选 $r-1$ 个环面字符构成字符格基，给出平凡化。不能仅在 $Q\ne0$ 上证明后忽略其余除子。

若某值 $a$ 在 $(c_i)$ 中出现 $k\ge2$ 次，商点 $(Q,P,x)=(0,0,-a)$ 为局部 $A_{k-1}$ 型奇点。令 $I=\{i:c_i=a\}$。其逆像在 $I$ 内满足 $q_ip_i=0$、$\prod_{i\in I}q_i=\prod_{i\in I}p_i=0$；外部各对非零。唯一闭轨道由 $q_i=p_i=0$（$i\in I$）给出，稳定子维数为 $k-1$；其余混合零模式产生非闭轨道。此处不能宣称整个分类商仍是几何商／torsor。

Poisson 约化也全局成立：$c_i$ 是 $T$ 不变量代数的 Casimir，
$$
\{Q,x\}=Q,\quad\{P,x\}=-P,\quad\{Q,P\}=h_c'(x).
$$
在 $Q\ne0$ 上约化形式是 $dQ/Q\wedge dx$；在 $P\ne0$ 上用 $-dP/P\wedge dx$。在单根的 $Q=P=0$ 点用 $dQ\wedge dP/h_c'(x)$，证实非退化延拓。以上属于熟知的 Danielewski 几何框架，不能作为原创性声明。

## 2. PROVED：无一般性假设的次数增长

对 $k\ge1$，所有坐标都有精确次数
$$
\deg(q_i\circ F^k)=L^k,\qquad
\deg(p_i\circ F^k)=A L^{k-1}.
$$
第一步中，$S_f$ 的增量最高次为 $A>1$，接着 $T_g$ 增量为 $AB$。归纳时所有 $q_i$ 同次数 $a$，$S_f$ 的非零最高齐次积次数为 $Aa$，严格超过旧 $p_i$ 次数；所有新 $p_i$ 同次数，$T_g$ 的最高积次数为 $BAa$，严格超过旧 $q_i$ 次数。最高积不为零，旧项次数较低，不存在相消。因此 $\deg F^k=L^k$，并直接得到全空间第一代数动力次数 $L$。

固定任意 $c$，在商曲面取 $Q=t,x=\xi,P=h_c(\xi)/t$，其中 $h_c(\xi)\ne0$。在 $t=\infty$，一次 $S_f,T_g$ 后 $(Q,x)$ 极点阶为 $(L,nA)$；反复操作得到 $Q\circ F^k$ 的极点阶恰为 $L^k$。关键严格不等式是
$$
rmn-m-n\ge1.
$$
若 $\delta_k$ 是在商环中表达三个像坐标所需的最小普通多项式次数，则该 Laurent 曲线给 $\delta_k\ge L^k$。全空间不变多项式的单项式正规形给 $\delta_k\le rL^k$：一个全空间次数 $d$ 的不变单项式可用总次数不超过 $d$ 的 $Q,P,x_i$ 表达，再代入 $x_i=x+c_i$。所以 $\lim\delta_k^{1/k}=L$。

**PARTIAL 边界：**若正式论文把该式写成商曲面的射影第一动力次数，必须补坐标次数与图拉回次数的双边比较；不能只说“半共轭故相等”。可取曲线 $x=\xi$ 的射影闭包做下界、用正规形做上界。本报告不将未展开的比较当作已完成证明；§3–4完全不依赖它。

## 3. PROVED：任意固定动量商曲面均无周期仿射曲线

更一般地，令 $h$ 为任意次数 $r\ge3$ 的多项式。曲面 $QP=h(x)$ 上的上述两剪切组合没有不可约周期仿射曲线，包括 $h$ 有重根的情况。

反设 $C$ 被某个 $F^N$ 保持。取 $C$ 的归一化光滑射影完备化上的一个无穷远点 $v$，使至少一个坐标具有正极点阶。记
$$
a=-v(Q),\quad b=-v(P),\quad e=-v(x).
$$
恒等于零的函数极点阶记为 $-\infty$。若 $e>0$，则 $a+b=re$，从而 $a>e$ 或 $b>e$；若 $e\le0$，至少一个 $a,b$ 为正。因此该点至少落在以下一个区域：
$$
\mathcal Q:\ a>\max(e,0),\qquad
\mathcal P:\ b>\max(e,0).
$$
在 $\mathcal Q$ 中，$S_f$ 后 $x$ 的阶为 $ma$，$P$ 的阶为 $Aa$。$T_g$ 后 $x$ 的阶为 $nAa$，$Q$ 的阶为 $La$；由于 $B>n$，仍落在 $\mathcal Q$。所有最大阶比较严格，不能发生最高项抵消。于是对 $F^{Nk}$，$Q$ 的极点阶等于 $L^{Nk}a$。

若初始点只选到 $\mathcal P$，用 $F^{-1}=S_{-f}T_{-g}$；依次得到 $x$ 阶为 $nb$、$Q$ 阶为 $Bb$，再得到 $x$ 阶为 $mBb$、$P$ 阶为 $Lb$，仍落在 $\mathcal P$。用负迭代同样指数增长。该处理也覆盖 $Q$ 或 $P$ 在原曲线上恒为零的边界线。

但 $F^N|_C$ 为仿射曲线自同构，诱导归一化完备化的自同构，只能置换有限多个无穷远点。任一固定坐标函数在这些点的极点阶构成有限集，不能随迭代指数增长，矛盾。证毕。

推论：对全部 $N\ge1$，$\mathbb C(D_c)^{F^N}=\mathbb C$。非恒定不变有理函数的一般水平集含曲线，有限个不可约分支被置换，其中一个对某次迭代周期，违反已证结论。奇异曲面只影响点，不破坏曲线归一化论证。

## 4. PROVED：全部高维有理积分，无未处理的环面 cocycle

固定两两互异的 $c$，先在任意代数闭特征零基域 $k$ 上工作。记 $R=k[M_c]$。它 Noetherian 且为整环，并有
$$
R[(\prod_iq_i)^{-1}]=k[x,q_1^{\pm1},\ldots,q_r^{\pm1}],\qquad
R/(q_i)\cong k[p_i,q_j^{\pm1}:j\ne i].
$$
故每个 $q_i$ 为素元。Nagata factoriality 判据给 $R$ 为 UFD；Noetherian 性保证非零非单位可分解为不可约元，满足判据的额外条件。采用 [Stacks Project, Lemma 10.120.7](https://stacks.math.columbia.edu/tag/0afu) 的准确版本。单位在局部化后形如 $a\prod_iq_i^{v_i}$，沿各素元 $q_i$ 的赋值必须为零，故 $R^*=k^*$。

令 $H\in\operatorname{Frac}(R)^{F^N}$，写成互素 $u/v$。UFD 中比较
$$
(F^{N*}u)v=u(F^{N*}v)
$$
的互素分解，得到 $F^{N*}u=\lambda u$、$F^{N*}v=\lambda v$，其中 $\lambda\in k^*$。

$F$ 与 $T$ 对易，所以 $u$ 的每个非零有限权分量 $u_\chi$ 都满足相同特征方程。若 $u_\chi$ 非单位，其零集是非空 $T$-不变除子。由§1的全域 torsor 平凡化，该零集沿每个环面纤维全有或全无，下降为 $D_c$ 上非空真闭曲线；零集对 $F^N$ 不变，故其有限个曲线分支中至少一个周期，违反§3。于是每个 $u_\chi$ 都为单位，故为常数。相同论证给 $u,v\in k$。因此
$$
k(M_c)^{F^N}=k\qquad(c_i\text{ 两两互异}).
$$
对全空间，令 $K=\mathbb C(c_1,\ldots,c_{r-1})$，使用泛动量层并扩张至 $\overline K$。此层满足互异条件；上述证明只用代数闭特征零性质，得到其固定域为 $\overline K$。又
$$
\mathbb C(q,p)=K(x,q_1,\ldots,q_r)
$$
是纯超越扩张，$K$ 在其中相对代数闭，故与 $\overline K$ 的交为 $K$。因此对每个 $N\ge1$，
$$
\boxed{\ \mathbb C(q,p)^{F^N}=\mathbb C(c_1,\ldots,c_{r-1}).\ }
$$
相应全空间多项式固定环为 $\mathbb C[c_1,\ldots,c_{r-1}]$：将固定多项式写为 $a(c)/b(c)$ 后，在恒等式 $b(c)H=a(c)$ 中代入截面 $q_i=1,p_r=0,p_i=c_i$，可知该有理式实际为 $c$ 的多项式。

**实质提升：**只证明 $k(D_c)^{F}=k$ 原本留下环面乘法 cocycle 障碍。本节通过 UFD、平凡单位、全域 torsor 和权除子完成了提升；不能省略其中任何一环。无需假设 $f,g$ 系数“足够一般”。

## 5. PROVED：两单剪切共同积分与碰撞层分层

令 $D_Q=\sum_i(Q/q_i)\partial_{p_i}$、$D_P=\sum_i(P/p_i)\partial_{q_i}$。非恒定 $f,g$ 下，$S_f$ 的有理固定域等于 $\ker D_Q$：整数迭代给 $R(q,p+t f'(Q)\nabla Q)$ 在无穷多个整数 $t$ 上等于 $R$，故作为 $t$ 的有理函数恒等，求导后除去非零 $f'(Q)$ 即得；逆向由导数为零得到。$T_g$ 同理。

在函数域中设 $U=D_Q/Q$、$V=D_P/P$、$E_i=q_i\partial_{q_i}-p_i\partial_{p_i}$。直接作用于 $q_i,p_i$ 得
$$
V-U=\sum_ix_i^{-1}E_i,\quad[U,E_i]=0,\quad Ux_i=1,
$$
$$
(\operatorname{ad}U)^j(V-U)=(-1)^j j!\sum_ix_i^{-j-1}E_i.
$$
对 $j=0,\ldots,r-1$，泛点的 Vandermonde 矩阵可逆。共同积分被所有 $E_i$ 消去，故属于 $\mathbb C(x_1,\ldots,x_r)$；再由 $U$ 消去，得到 $\mathbb C(c)$。

在某个固定 $c$ 层，按相等的 $c_i$ 分为 $s$ 个块 $I_\alpha$，各取代表 $i_\alpha$。同一计算只产生块导子 $E_\alpha=\sum_{i\in I_\alpha}E_i$，有 $s$ 个不同的 $(x+c_{i_\alpha})^{-1}$；括号秩恰为 $s+1$。因此
$$
\boxed{\ k(M_c)^{S_f}\cap k(M_c)^{T_g}
=k(q_i/q_{i_\alpha}:i\in I_\alpha\setminus\{i_\alpha\},\ \alpha=1,\ldots,s).\ }
$$
证明完备性：在 $q\ne0$ 的函数域坐标 $(x,q_i)$ 中，$U=\partial_x$，$E_\alpha=\sum_{i\in I_\alpha}q_i\partial_{q_i}$；其共同核正是上式。每块内比值又直接被两次剪切保持。超越次数为 $r-s$；全碰撞层 $c=0$ 给 $r-1$ 个比值。这不是与泛层固定域定理矛盾，而是特殊化后新积分出现。

**追加 PROVED：这些比值也穷尽每个碰撞层的 $F^N$ 固定域。** 这是主代理与本调查在提交前并行发现的进一步降维，尚未经独立终审。设 $n_\alpha=|I_\alpha|$、$d_\alpha=c_{i_\alpha}$，令 $z_i=q_i/q_{i_\alpha}$、$Z=\prod_{\alpha}\prod_{i\ne i_\alpha}z_i$，并以 $K=k(z_i)$ 为基域。原函数域变为
$$
K(x,u_1,\ldots,u_s),\quad v_\alpha=(x+d_\alpha)/u_\alpha,\quad
Q=Z\prod_\alpha u_\alpha^{n_\alpha},\quad
P=Z^{-1}\prod_\alpha v_\alpha^{n_\alpha}.
$$
使用 $R_s=K[x,u_\alpha,v_\alpha]/(u_\alpha v_\alpha-x-d_\alpha)$ 作为仿射模型。$d_\alpha$ 互异，故§4的素元局部化证明仍给 UFD 和单位群 $K^*$；当 $s=1$，这是多项式环 $K[u_1,v_1]$。剪切更新 $v_\alpha\mapsto v_\alpha+Qf'(Q)/u_\alpha$ 与 $u_\alpha\mapsto u_\alpha+Pg'(P)/v_\alpha$ 都是该模型的多项式自同构，因为 $n_\alpha\ge1$。

取完整对角化群
$$
H=\ker\left((\mathbb G_m)^s\longrightarrow\mathbb G_m,
\quad(t_\alpha)\mapsto\prod_\alpha t_\alpha^{n_\alpha}\right).
$$
**不要擅自取单位连通分支。** 当 $\gcd(n_\alpha)>1$ 时 $H$ 不连通，但仍是特征零对角化群，有限权分解仍适用。字符群为 $\mathbb Z^s/\mathbb Z(n_\alpha)$。正规形的权为零，当且仅当 $u,v$ 的指数差为 $(n_\alpha)$ 的整数倍，所以
$$
R_s^H=K[Q,P,x]/(QP-\prod_\alpha(x+d_\alpha)^{n_\alpha}).
$$
在代数闭包上，每个商纤维是一个 $H$ 轨道：$Q\ne0$ 时用全部 $u_\alpha$ 之比确定 $t_\alpha$，$P\ne0$ 时用全部 $v_\alpha$；在 $Q=P=0,x=-d_\beta$ 时只有第 $\beta$ 对同时为零，其他 $t_\alpha$ 任给后，方程为 $t_\beta^{n_\beta}$ 指定一个非零值，总有解。该点稳定子为 $\mu_{n_\beta}$。因此所有轨道闭且维数均为 $s-1$，虽一般不是 torsor。

§4的互素分式和权分量论证现用于 $H$：非单位权函数的零除子饱和，闭像非空且真，维数为 $s-(s-1)=1$；其周期曲线与§3矛盾。得到代数闭包上的固定域只有常数，再由纯超越扩张将常数下降到 $K$。从而对任意固定 $c$ 和任意 $N\ge1$，
$$
\boxed{\ k(M_c)^{F^N}
=k(q_i/q_{i_\alpha}:i\in I_\alpha\setminus\{i_\alpha\}),\quad
\operatorname{trdeg}=r-s.\ }
$$
这里使用原次数为 $r$ 的商曲面即可，无需另证明低次数加权商曲面的增长定理。

## 6. 文献边界、风险与是否值得选

本次只查与对象直接相关的一手公开来源，未下载 PDF 到项目、未改文献库。arXiv 定向搜索已做；无可用 Zotero／Obsidian 接口。检索结果中的抓取日期未当作发表日期。

| 一手来源 | 已核实内容 | 对本项目的直接约束 |
| --- | --- | --- |
| Leuenberger–Regeta，2017 arXiv 版本及其后更新，[Automorphism Groups of Danielewski Surfaces](https://arxiv.org/pdf/1710.06045)，§3、Proposition 3 | 两族三角加性作用、生成与自由积结构；来源还回溯 Makar-Limanov 和 Kutzschebauch–Leuenberger | 约化剪切就是已知作用，不可包装成新曲面／新剪切；最新 PDF 与旧 arXiv 元数据标题存在版本差异，正式引用需锁版本 |
| Leuenberger，2016，Ann. Inst. Fourier 66(2), 433–454，[Complete algebraic vector fields on Danielewski surfaces](https://aif.centre-mersenne.org/item/AIF_2016__66_2_433_0/) | 完备代数向量场分类及相关纤维化 | 单剪切流与曲面几何已属成熟文献 |
| Stacks Project，[Nagata criterion, 0AFU](https://stacks.math.columbia.edu/tag/0afu) | 素元局部化的 factoriality 判据及因子分解条件 | §4 使用的外部交换代数依据，不是本项目定理 |

**值得保留为候选，但选题必须以§3–5为核心。** 最强可行主定理是：任意非恒定多项式两剪切、任意 $r\ge3$，全空间所有正迭代的有理积分域精确为动量差域，而每个固定动量层的全部积分由相等动量块内坐标比精确生成；同时给出全空间精确次数。无周期曲线提供一个可直接审查的证明支点，特殊层积分的阶跃给出实质边界信息。

**仍须解决的选择障碍（OPEN）：** 定向检索尚未排除这些结论已作为 Danielewski 循环约化字、仿射辛约化、universal torsor／Cox lifting 或高维保体积多项式自同构的一般定理出现。尤其无周期曲线很可能属于 Hénon 型剪切的已知现象，证明短并不等于新。应继续检查上述文献的引用链及族内 Papers1–28 的精确主定理，不能依据本报告宣布原创。

**不能接受的缩减或夸大：** 不可把共同单剪切积分冒充单个 $F$ 的积分；不可在奇异层继续套互异层 UFD/torsor；不可仅凭次数大于一宣布实辛 Liouville、解析或亚纯非可积；不可把仿射无周期曲线扩大成射影完备化无周期边界曲线；不可由主定理泛层结论强行推出每个特殊层无额外积分。

独立内容审查仍应优先攻击：§3 恒零坐标及负迭代、§4 特征函数的权分解与零除子下降、§5 非连通对角化群和有限稳定子、泛基域扩张后的常数下降。上述环节已在本报告展开，但作者侧互检不替代独立终审。若继续选中，本内容适合一篇紧凑结构论文；不应仅为了预定正文页数把约化公式与标准背景反复拆分。
