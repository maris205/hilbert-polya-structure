# Paper30 T 分支：两级矩阵谱的独立算子检查

输入批次日期：2026-09-06；本次检查完成日期：2026-09-07。
范围：显式无限矩阵的核性、解析谱分裂及全部余谱。
审查方式：实际 secondary independent check，非 GPT-5.4 Codex MCP 审稿。
不作 Ruelle 谱识别、Route 评价、新颖性或容量评分，不改作者输入和项目状态。

## Claim

在固定复 Hilbert 空间 $\mathcal H=\ell^2(\mathbb Z^2\setminus\{0\})$ 上，
按状态 $(a,b)$ 标记原频率 $(b-a,a)$。给定矩阵
$$
B(t)_{(b,c),(a,b)}
=t^{|a|-2|b|+|c|-1}[z^{a+c-3b}]e^{tb(z-z^{-1})},
\qquad L(t)=tB(t),
$$
其余项为零，零点按可去奇性延拓。核查两份输入的下列原结论：

1. $B$ 在 $|t|<1/256$ 迹范数全纯，且闭圆盘上
   $\sum_{m,n}\sup|B_{n,m}(t)|\le23040+512/65535<23041$。
2. $B_0=B(0)$ 的秩为八，谱为 $\{0,-1\}$，$-1$ 半单重二；
   $P=B_0^2$ 是其 Riesz 投影，$B_0=-P+N$，$N^2=0$、$\operatorname{rank}N=6$。
3. 对充分小的非零复参数，$L(t)$ 有两条全纯简单分支
   $$
   \lambda_{\rm ev}(t)=-t+\frac{11}{12}t^2+O(t^3),\qquad
   \lambda_{\rm od}(t)=-t+\frac5{12}t^2+O(t^3).
   $$
4. 在 $t=s^2$ 的平方根覆盖上另有八条简单分支
   $$
   \lambda_j(s^2)=s^3(\nu_j+O(s)),
   $$
   其中 $\nu_j$ 是下列四个互异非零数各自的两个平方根：
   $$
   \frac{9+\sqrt{145}}{24},\quad\frac{9-\sqrt{145}}{24},\quad
   \frac{7+i\sqrt{15}}{24},\quad\frac{7-i\sqrt{15}}{24}.
   $$
5. 删除上述十条、按代数重数计的特征值后，全部余谱的最大模为
   $o(|t|^{3/2})$，其中小量对复参数趋零的方向一致。
   整体谱为 $O(|t|)$，谱半径为 $|t|+O(|t|^2)$。

## Status

`PROVABLE AS STATED`。

两份指定输入的上述矩阵结论原样成立。没有发现需要加强假设、减弱定理或
修改作者证明的实质性缺口。以下独立核查展开了有限秩非正交分解、投影导数、
全无限维缩放和统一余谱控制的适用条件。

输入一已经更正的零参数统一符号 $(-1)^j/j!$ 核查正确；本次没有要求重新修改。
本结论不自动给予 $L(t)$ 动力共振身份，也不表示新颖性、价值、稿件或验收通过。

## Assumptions

- 参数可为复数；空间、基和下文的固定分解不依赖参数。
- 原点频率已经排除；不向空间中加回会产生 $t^{-1}$ 项的原点。
- 非零谱按代数重数计。简单性只要求在充分小的非零参数处成立；
  在零参数处，$L(0)=0$，并不具有十个互异简单谱点。
- 仅使用给定矩阵、准确的整数边分类和有界算子的局部解析谱理论。
  不假设全频率的参数相关权重是原动力算子与本矩阵之间的有界相似。

## Notation

$B_1=B'(0)$，$J\mathbf e_{a,b}=\mathbf e_{-a,-b}$，$Q=I-P$。
对一条边，$k=a+c-3b$，$C_{b,k}(t)=[z^k]e^{tb(z-z^{-1})}$。
范数 $\|\cdot\|_1$ 是 trace-class 范数，$\|\cdot\|$ 是算子范数。
有限维坐标的列为输入、行为输出；$\eta=1,-1$ 分别指 $J$ 的偶、奇空间。
所有直和投影均指固定的有界坐标投影，不要求正交。

## Proof Strategy

先重新核对可对全部频率求和的复圆盘主控，再核对完整低阶支持。
去掉半单 leading 簇后，用真实的局部有界相似固定余谱空间。
对平方零链的有限维源空间缩放，得到在零点仍迹范数全纯的无限维算子。
计算它的全部非零极限谱，最后用紧预解集与谱投影秩控制全部余谱。

## Dependency Map

1. 标量展开与整数不等式 $\Rightarrow$ 全矩阵可和主控 $\Rightarrow$ 迹范数全纯。
2. 阶数奇偶性 $\Rightarrow$ 完整 $B_0,B_1$ $\Rightarrow$ 半单 leading 空间与幂零链。
3. 反号对称与半单简单分支 $\Rightarrow$ 两个 leading 导数。
4. 全纯 Riesz 投影与固定空间共轭 $\Rightarrow$ $\mathcal A(t)=N+tM(t)$，
   且 $M(0)=QB_1Q$。
5. 全空间缩放恒等式 $\Rightarrow$ 全纯 $K(s)$ $\Rightarrow$ 八个非零简单极限谱点。
6. 秩一谱投影与统一预解估计 $\Rightarrow$ 八条分支及全部余谱的小量估计。

## Proof

### Step 1. 全矩阵主控与迹范数全纯

当 $b\ne0$ 时，令 $\beta=|b|$、$x=|a|+|c|$、$K=|a+c-3b|$，
$q=K+x-2\beta$。指数乘积展开给出
$$
C_{b,k}(t)=\eta_k\sum_{j\ge0}
\frac{(-1)^j(tb)^{K+2j}}{j!(K+j)!},\qquad
\eta_k=1\ (k\ge0),\quad \eta_k=(-1)^K\ (k<0).
$$
由 $(K+j)!\ge K!j!$ 和指数级数的非负系数比较，
$$
|t^{-K}C_{b,k}(t)|\le\frac{\beta^K}{K!}e^{2|t|\beta}.
$$
三角不等式逐项给出
$$
q\ge\beta\ge1,\qquad x+\beta\le4q,\qquad K\le3q.
$$
因此矩阵最低阶 $q-1$ 非负，且对任意固定 $0<r<1$，
$$
\sup_{|t|\le r}|B_{(b,c),(a,b)}(t)|
\le r^{-1}r^{(|a|+|c|)/8}
\bigl(r^{1/8}e^{r^{1/6}+2r}\bigr)^{|b|}.
$$
这里使用 $r^q=r^{q/2}r^{q/2}$，分别用 $x+\beta\le4q$ 与 $K\le3q$
控制两因子，再以 $\sum_{K\ge0}y^K/K!=e^y$ 的单项上界吸收阶乘项。
指数方向正确，因为 $r<1$。

对 $r_0=2^{-8}$，有 $r_0^{1/8}=1/2$，
$r_0^{1/6}+2r_0<1/2$，以及
$e^{1/2}\le33/20<5/3$，故
$$
\sup_{|t|\le r_0}|B_{(b,c),(a,b)}(t)|
\le256\,2^{-|a|-|c|}(5/6)^{|b|}\quad(b\ne0).
$$
所有这样的矩阵项与整数三元组 $(a,b,c)$ 一一对应，且输入、输出均非原点。
求和得 $256\cdot3\cdot10\cdot3=23040$。
当 $b=0$ 时，唯一非零项为 $c=-a\ne0$，值为 $t^{2|a|-1}$；
其闭圆盘主控之和恰为 $512/65535$。原主控因而覆盖整个无限矩阵。

每个标准矩阵单位的迹范数是 $1$，所以按全部矩阵项求和在闭圆盘上一致、
绝对地收敛于 trace-class 算子。各项是整函数；对任意 $\rho<r_0$，
标量 Cauchy 导数界以原可和主控乘 $(r_0-\rho)^{-1}$ 为统一上界。
导数级数遂在较小圆盘上迹范数一致收敛。这证明所需 Banach 空间值全纯性，
而不只是逐项全纯；并给出原定理的显式范数常数。

### Step 2. 完整低阶支持与 $B_0,B_1$ 的检查

令 $\Delta=K+x-3\beta$。三角界给出 $\Delta\ge0$，而
$$
\Delta\equiv(a+c-3b)+a+c-3b\equiv0\pmod2.
$$
最低阶为 $\beta-1+\Delta$，后续标量级数每次只增加二阶。
故 $B_0$ 恰来自 $b=\varepsilon=\pm1$、
$a=\varepsilon A,c=\varepsilon C$、$A,C\ge0$、$A+C\le3$；
系数为 $(-1)^{3-A-C}/(3-A-C)!$。
$B_1$ 的非零 $b$ 项恰来自 $b=2\varepsilon$、同样的弱同号条件、
$A+C\le6$；系数为 $(-1)^{6-A-C}2^{6-A-C}/(6-A-C)!$。
此外恰有两条系数为 $1$ 的边
$(1,0)\to(0,-1)$、$(-1,0)\to(0,1)$。
这是一阶项的穷尽分类，没有有限截断假设。

每个符号的 $B_0$ 源、汇各含四个向量，仅交于 $(\varepsilon,\varepsilon)$。
源至汇的四阶系数矩阵反三角，反对角为 $1$，故各块秩四。
正号块取 $x=\mathbf e_{1,1}$，有序源向量组
$S=(\mathbf e_{0,1},\mathbf e_{2,1},\mathbf e_{3,1})$，
有序汇向量组 $T=(\mathbf e_{1,0},\mathbf e_{1,2},\mathbf e_{1,3})$；
负号块由 $J$ 作用于各向量给出。星号表示相应原标准坐标的对偶泛函。
按此顺序，直接代入上述系数得到
$$
B_0x=-x+Tu,\quad B_0S=xv+TC,\quad B_0T=0,
$$
其中
$$
u=(1/2,1,0)^{\mathsf T},\quad v=u^{\mathsf T},\qquad
C=\begin{pmatrix}-1/6&-1&1\\-1&0&0\\1&0&0\end{pmatrix}.
$$
令 $r=x-Tu$、$\ell=x^*-vS^*$；则 $\ell r=1$，
$B_0r=-r$、$\ell B_0=-\ell$。两块 $r\ell$ 之和等于 $P=B_0^2$，
并且
$$
B_0=-P+N,\qquad PN=NP=0,\qquad N^2=0.
$$
在 $\ker P$ 内用 $S'=QS=S+rv$ 替换源，得到
$$
NS'=TD,\qquad
D=C+uv=\begin{pmatrix}1/12&-1/2&1\\-1/2&1&0\\1&0&0\end{pmatrix},
\qquad\det D=-1.
$$
两块各有三条独立长度二的链，故 $\operatorname{rank}N=6$。
$B_0$ 在 $\operatorname{ran}P$ 上为 $-I$，在 $\ker P$ 上为平方零算子；
$(I+N)^{-1}=I-N$ 排除后者的 $-1$ 谱点。由此 $-1$ 的广义谱空间
恰为二维 $\operatorname{ran}P$，并且半单，$P$ 确为其 Riesz 投影。

附加核对 $B_1$ 自身的谱，不将其用作两级定理的新假设：
每个符号的 $b=2\varepsilon$ 源、汇集合各含七个向量，仅交于
$p_\varepsilon=\mathbf e_{2\varepsilon,2\varepsilon}$，其对角系数为 $2$。
第一次作用落入汇空间，第二次作用只经 $p_\varepsilon$；
另外两条 $b=0$ 边与这些集合不交，且各自平方为零。因此
$$
B_1^3=2B_1^2,\qquad \operatorname{rank}B_1^2=2.
$$
$P_1=B_1^2/4$ 是秩二投影，$B_1P_1=2P_1$，
$(B_1-2P_1)^2=0$；故 $\operatorname{Spec}B_1=\{0,2\}$，
$2$ 半单、代数重数为二。这也与完整一阶支持一致。

### Step 3. leading 奇偶分支及准确导数

换 $(a,b,c)$ 为相反数保持系数，因为 $C_{-b,-k}=C_{b,k}$。
因此 $JB(t)=B(t)J$；在两个闭奇偶空间内，$B_0$ 的 $-1$ 各为简单。
围绕 $-1$ 的半径 $1/3$ 圆周与 $\operatorname{Spec}B_0$ 分离。
全纯性及预解 Neumann 级数使其在小参数下仍为合法 Riesz 轮廓。
所得投影解析且秩为一：若解析投影为 $E(t)$、$E(0)=E_0$，
$E(t)E_0+(I-E(t))(I-E_0)$ 在零点等于 $I$，
邻近可逆并将两个投影共轭，故秩不变。

从投影施于原特征向量获得解析向量，按固定左泛函归一化后，
微分特征方程得到 $b_\eta'(0)=\ell_\eta B_1r_\eta$。
完整一阶分类给出 $B_1x=B_1S=0$，$B_1T$ 不含 $x$ 输出；
$T\to S$ 角块在奇偶空间内为
$$
A_\eta=\operatorname{diag}(\eta,2/3,0).
$$
第一项来自两条跨符号的 $b=0$ 边，第二项来自
$(1,2)\to(2,1)$ 的系数 $2^4/4!=2/3$，第三项由 $b=3$ 不可能一阶得零。
于是
$$
b_\eta'(0)=vA_\eta u=\frac\eta4+\frac23=\frac{8+3\eta}{12}.
$$
乘以 $t$ 得原两条 leading 展开。两条 $B(t)$ 分支之差为
$t/2+O(t^2)$，故对充分小的非零复参数不相等；总空间中的重数也是一。

### Step 4. Riesz 平凡化导数没有遗漏项

将两个奇偶 Riesz 投影相加为 $P(t)$，置 $Q(t)=I-P(t)$，以及
$$
U(t)=P(t)P+Q(t)Q.
$$
$U(0)=I$，故在小圆盘内是解析可逆的有界算子；恒等式
$U(t)P=P(t)U(t)$ 将全部空间分成固定的 leading 块与 $\mathcal H_Q=\ker P$。
trace-class 双边理想在有界算子乘法下保持不变，且乘法连续双线性，
所以
$$
\mathcal A(t)=QU(t)^{-1}B(t)U(t)Q\big|_{\mathcal H_Q}
$$
仍迹范数全纯。其零值为 $N$，因此 Banach 空间 Taylor 展开给出
$\mathcal A(t)=N+tM(t)$，$M$ 迹范数全纯。

投影微分给出 $PP'(0)P=QP'(0)Q=0$，且
$U'(0)=P'(0)(P-Q)$，从而 $QU'(0)Q=0$。
由 $B_0$ 的固定块对角性，
$$
\mathcal A'(0)=Q\bigl(B_1+B_0U'(0)-U'(0)B_0\bigr)Q
=QB_1Q\big|_{\mathcal H_Q}.
$$
这证明 $M(0)$ 没有来自投影变化的额外 $Q$ 块项。
$Q$ 保持原 $S$ 坐标，$QT=T$，因此 $M(0)$ 的 $\mathcal T\to\mathcal S$
块确为 $A_6$，它在奇偶分解中是 $A_\eta$。

### Step 5. 全空间平方根缩放在迹范数中解析

将两符号的 $S'$、$T$ 分别合为六维 $\mathcal S,\mathcal T$，
其余十四个原坐标之外的闭空间记为 $\mathcal E$。这是有界拓扑直和，且
$$
\mathcal H_Q=\mathcal S\oplus\mathcal T\oplus\mathcal E,\qquad
N=\begin{pmatrix}0&0&0\\D_6&0&0\\0&0&0\end{pmatrix},
\quad D_6=\operatorname{diag}(D,D).
$$
非正交性不妨碍迹类估计：可由一个仅改变有限坐标的固定有界可逆坐标算子
将此直和与 Hilbert 正交直和互相识别，迹范数由双边理想不等式控制。

令 $\mathcal R=\mathcal T\oplus\mathcal E$，对 $s\ne0$ 置
$V_s=s\Pi_S+\Pi_R$。由于 $N$ 仅从源映入汇，
$$
K(s)=s^{-1}V_s^{-1}\mathcal A(s^2)V_s
=N+\begin{pmatrix}
sM_{SS}(s^2)&M_{SR}(s^2)\\
s^2M_{RS}(s^2)&sM_{RR}(s^2)
\end{pmatrix}.
$$
这是全算子的精确等式；没有把 $\mathcal E$ 删去。
所有块均为迹类全纯族乘固定投影与非负参数幂，故 $K$ 在零点迹范数全纯，
并有 $\|K(s)-K(0)\|=O(|s|)$。其极限是
$$
K_0=\begin{pmatrix}0&A_6&G\\D_6&0&0\\0&0&0\end{pmatrix},
\qquad G=M(0)_{SE}.
$$
$G$ 被保留；无须额外假设它为零或无耦合。其像属于六维源空间，
故 $K_0$ 是有限秩算子。

### Step 6. 全部非零极限谱及简单性

记 $\mathcal F=\mathcal S\oplus\mathcal T$。$K_0$ 的像属于 $\mathcal F$，
因而在商空间 $\mathcal H_Q/\mathcal F$ 上为零。
若 $\nu\ne0$ 且 $(K_0-\nu)^j w=0$，则在商空间中
$(-\nu)^j[w]=0$，所以 $w\in\mathcal F$。
有限秩算子的非零谱都是孤立特征值；因此其全部非零广义谱恰由
$$
F_0=\begin{pmatrix}0&A_6\\D_6&0\end{pmatrix}
$$
给出。保留的 $G$ 不改变这些特征值或代数重数。
Schur 行列式公式先对 $\nu\ne0$ 给出
$\det(\nu I-F_0)=\det(\nu^2I_6-A_6D_6)$，
再由两侧为多项式而对全部 $\nu$ 成立。

奇偶空间内
$$
DA_\eta=\begin{pmatrix}
\eta/12&-1/3&0\\-\eta/2&2/3&0\\\eta&0&0
\end{pmatrix},
$$
其特征多项式为
$$
\mu\left(\mu^2-\frac{8+\eta}{12}\mu-\frac\eta9\right).
$$
两个二次多项式分别有判别式 $145/144$、$-15/144$。
第一组两个根一正一负，第二组是非实共轭根；四根因此非零且两两不同。
平方根给出八个两两不同的非零数。每个二次根简单，且
$\nu\mapsto\nu^2$ 在这些非零点的导数 $2\nu$ 不为零，
故八个 $\nu_j$ 都是 $F_0$，从而也是完整 $K_0$ 的代数简单谱点。

### Step 7. 分支与全部余谱的统一控制

围绕八个 $\nu_j$ 选取闭包互不相交且不含零的小圆盘。
算子范数收敛给出合法的局部 Riesz 轮廓；各投影在零点的秩为一，
由 Step 3 的显式投影共轭，邻近仍为一。因此每个圆盘内恰有一条
全纯简单特征值 $\nu_j(s)=\nu_j+O(s)$。

对每个固定的 $s\ne0$，$V_s$ 确为有界可逆算子，故
$\mathcal A(s^2)$ 的相应特征值为 $s\nu_j(s)$，代数重数不变；
再乘 $s^2$ 得原定理的 $s^3(\nu_j+O(s))$。
leading 分支模为 $|s|^2(1+O(|s|^2))$，第二簇为 $O(|s|^3)$，
所以充分小时两簇不相交。

为核对全余谱的小量量词，固定上述八圆盘，再给定
$0<\epsilon<\tfrac12\min_j|\nu_j|$，并可将圆盘缩小以与
$\{|z|\le\epsilon\}$ 分离。取一个常数
$R>1+\sup_{|s|\le s_0}\|K(s)\|$，其中 $s_0>0$ 充分小。
令 $C_\epsilon$ 为 $\{|z|\le R\}$ 中删去八个开圆盘及
$\{|z|<\epsilon\}$ 后的紧集。该集属于 $K_0$ 的预解集，故
$$
H_\epsilon=\sup_{z\in C_\epsilon}\|(z-K_0)^{-1}\|<\infty.
$$
选 $\delta_\epsilon>0$ 使 $|s|<\delta_\epsilon$ 时
$H_\epsilon\|K(s)-K_0\|<1$，则 Neumann 级数排除
$C_\epsilon$ 上的全部谱；$|z|>R$ 的谱由算子范数界排除。
八个小圆盘内每个仅有一条已计的简单谱点，所以删除它们后的全部谱都满足
$|z|<\epsilon$。这些估计只依赖 $|s|$，与趋零方向无关。

因此若 $r_K(s)$ 是删除八个谱点后 $K(s)$ 的余谱最大模，
则 $r_K(s)\to0$，并且
$$
\frac{\sup|\operatorname{Spec}_{\rm rem}L(t)|}{|t|^{3/2}}
=r_K(s)\longrightarrow0,\qquad t=s^2\ne0.
$$
两种平方根对应同一原算子，其簇作为多重集合相同；无需在穿孔 $t$ 圆盘上
为八条单独分支选取全局单值平方根。另一固定块恰为两维 leading 块，
不存在被遗漏的第三个空间。全部谱由这两个固定块穷尽，故最终谱半径为
$|t|+O(|t|^2)$。原矩阵两级谱定理得证。∎

## Corrections or Missing Assumptions

没有必要修正或新增假设。尤其：

- 非正交固定分解只需有界投影；作者已经满足这一点。
- $U'(0)$ 的变化没有额外的一阶零谱块贡献；作者的 $M(0)$ 正确。
- $G$ 无需消失，作者已保留它；非零广义谱的商空间论证有效。
- 统一余谱结论并未把逐条收敛偷换成谱半径收敛；预解紧集论证足够。
- 八分支的全纯性在平方根覆盖上成立，不应改写为八条关于 $t$ 的单值全纯分支。

## Open Risks

本任务的矩阵结论没有尚未闭合的证明义务。
原动力系统的谱识别、周期迹身份及任何 Ruelle 共振命名仍是本任务之外的独立问题；
本报告未检查未提供的识别论证，也不暗示该义务已完成。
未检验原定理明确不声称的最佳余谱指数、最优解析半径或有限参数全局谱结构。

## Input identity and actual execution

仅以以下两个实际文件为数学输入，均已全文读取并以本地命令核验：

1. [重加权核性输入](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md)，
   320 行，SHA-256：
   `c85dfa0ed29f1c6eb7d29d0898984bf9e2536da5ec89868c4582db9ea7381826`。
2. [两级矩阵谱作者证明 V1](PAPER30_TORUS_TWO_SCALE_MATRIX_PROOF_V1_20260906.md)，
   363 行，SHA-256：
   `a5cc67aad167207330a98f88ff45c26e4977285df1e14c8aaabf727eb2483d2c`。

实际执行记录：

- 全文读取工作区 `AGENTS.md`、`proof-writer/SKILL.md` 与
  `research-review/SKILL.md`。前者的证明技能用于严格区分原结论、假设与风险。
- 检查当前工具目录，未发现所需 `mcp__codex__codex` 或 `codex-reply` 审稿工具；
  出现的 document-control 工具不是审稿后端，未作替代调用。
  按本次任务明确指定的 secondary fallback 独立核查，未调用 GPT-5.4 MCP，
  无外部审稿轮次或 `threadId`，不把本次执行标注为该模型审稿。
- 对两份输入执行 `wc -l`、`sha256sum`，并全文读取；另以行号定位复核作者的
  Riesz 平凡化、缩放与余谱段落。全部推导为手工精确数学检查。
- 本报告未把另一个低阶检查代理的结论用作前提；这里的有限角块、符号、
  根与无限维论证均独立检查。没有数值实验、浮点特征值、有限截断数值谱或外部检索。
- 唯一新增文件是本报告；未改两份输入、冻结产物、状态、锁或稿件，
  无外部写入、提交、付费资源操作、新颖性或容量评分。完成本次有界独立检查后停止。
