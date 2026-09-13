# Paper30 T 分支：解析核的两级小参数谱分裂

日期：2026-09-06。作者证明 V1；不是候选评分、正式稿或本地验收。
本文件证明显式无限矩阵的谱渐近。与原动力系统 Ruelle 共振的识别是单独义务，
不得由本文件的参数相关对角变换直接推断。

## Claim

令 $\Lambda=\mathbb Z^2\setminus\{0\}$，$\mathcal H=\ell^2(\Lambda)$。
使用状态 $(a,b)$ 标记频率 $m=(b-a,a)$。对边 $(a,b)\to(b,c)$，置
$$
k=a+c-3b,\qquad C_{b,k}(t)=[z^k]\exp\{tb(z-z^{-1})\},
$$
并令
$$
B(t)_{(b,c),(a,b)}
=t^{|a|-2|b|+|c|-1}C_{b,k}(t).
\tag{1}
$$
所有其他矩阵项为零；零点奇性按解析延拓解释。
输入 [解析核证明](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md)
已证明 $B(t)$ 在 $|t|<1/256$ 是固定空间上的迹范数全纯族，
且 $\|B(t)\|_1<23041$。记 $L(t)=tB(t)$。

**两级谱定理。** 存在 $\tau>0$，对所有 $0<|t|<\tau$：

1. $L(t)$ 有两条以 $t$ 为变量的全纯简单特征值，按反号对称的偶、奇空间标记为
   $$
   \lambda_{\rm ev}(t)=-t+\frac{11}{12}t^2+O(t^3),\qquad
   \lambda_{\rm od}(t)=-t+\frac5{12}t^2+O(t^3).
   \tag{2}
   $$
2. 写 $t=s^2$。还有八条在 $s$ 附近全纯的简单特征值
   $$
   \lambda_j(s^2)=s^3\bigl(\nu_j+O(s)\bigr),\qquad 1\le j\le8,
   \tag{3}
   $$
   其中八个不同非零数 $\nu_j$ 是下列四个数的各两平方根：
   $$
   \mu_1=\frac{9+\sqrt{145}}{24},\quad
   \mu_2=\frac{9-\sqrt{145}}{24},\quad
   \mu_3=\frac{7+i\sqrt{15}}{24},\quad
   \mu_4=\frac{7-i\sqrt{15}}{24}.
   \tag{4}
   $$
3. 删除上述十条、按代数重数计的特征值后，剩余谱满足一致结论
   $$
   \sup\{|\lambda|:\lambda\in\operatorname{Spec}L(t)
          \text{ 属于剩余谱}\}=o(|t|^{3/2}).
   \tag{5}
   $$
   因而全部谱为 $O(|t|)$，最大模为 $|t|+O(|t|^2)$。

这里 (3) 是平方根覆盖上的陈述。取正实 $t$ 时可取 $s=\sqrt t$；
负实 $t$ 时可取 $s=i\sqrt{|t|}$。换 $s$ 的符号只重新排列该八元谱簇，
不把负参数的 $t^{3/2}$ 当作未指定分支的实数。
本定理不声称剩余谱没有非零点，也不声称给出其最优衰减指数。

## Status

`PROVABLE AS STATED`：本文件范围内的完整作者证明如下，尚待独立数学审查。
这里的状态只针对矩阵谱定理，不授予动力共振身份、新意、价值或容量 PASS。

## Assumptions and notation

- 所有谱均为复 Hilbert 空间上的算子谱；非零点按代数重数计。
- 输入核性定理的全矩阵估计是已给出的证明依赖，不以有限截断或数值谱替代。
- $B_0=B(0)$、$B_1=B'(0)$。$J\mathbf e_{a,b}=\mathbf e_{-a,-b}$ 是有界对合。
- 以下有限维空间的直和不必正交。它们相对于固定坐标分解的投影均有界，
  因为只改变有限多个标准基向量。

## Proof strategy and dependency map

1. 核性输入提供固定空间上算子范数与迹范数全纯性。
2. 整数边代价的奇偶性穷尽 $B_0,B_1$；有限坐标给出半单 $-1$ 与平方零部分。
3. 反号对称将 leading 重二根分为两条简单解析分支，导数公式给出 (2)。
4. Riesz 投影的显式解析平凡化将其余谱移至固定空间。
5. 在平方根覆盖上对幂零链的源作有限维缩放，得到新的全纯迹类算子 $K(s)$。
6. $K(0)$ 的非零谱由两个三阶有效矩阵决定；解析简单根及一致谱包含给出 (3)—(5)。

## Proof

### Step 1. 零阶、一阶项的穷尽分类

当 $b\ne0$ 时，记 $\beta=|b|$、$x=|a|+|c|$、$K=|a+c-3b|$。
核系数最低参数阶为
$$
e=K+x-2\beta-1.
$$
设 $\Delta=K+x-3\beta$。三角不等式给出 $\Delta\ge0$；又由
$|n|\equiv n\pmod2$ 得 $\Delta$ 为偶数，所以
$$
e=\beta-1+\Delta,\qquad \Delta\in2\mathbb Z_{\ge0}.
\tag{6}
$$
Bessel 系数除首项外仅增加偶数阶。因此：

- $B_0$ 的非零边必须为 $b=\varepsilon=\pm1$、
  $a=\varepsilon A,c=\varepsilon C$，$A,C\ge0$、$A+C\le3$；
- $B_1$ 中 $b\ne0$ 的非零边必须为 $b=2\varepsilon$、
  $a=\varepsilon A,c=\varepsilon C$，$A,C\ge0$、$A+C\le6$。

第一种边的系数是 $(-1)^{3-A-C}/(3-A-C)!$；
第二种边的系数是
$$
\frac{(-1)^{6-A-C}2^{6-A-C}}{(6-A-C)!}.
\tag{7}
$$
两个符号均有这些相同系数：当 $b>0$，符号来自负的 $k$；当 $b<0$，
符号来自负的 $b$ 的幂。不能遗漏这两种符号来源之一。
当 $b=0$ 时只剩 $c=-a\ne0$，项为 $t^{2|a|-1}$；
因此 $B_1$ 还恰含两边
$$
(1,0)\longrightarrow(0,-1),\qquad
(-1,0)\longrightarrow(0,1),
\tag{8}
$$
系数均为 $1$。这些分类证明低阶矩阵确为有限支撑，不是任意裁剪。

此外，换 $(a,b,c,k)$ 为其相反数时，权指数不变且
$C_{-b,-k}=C_{b,k}$，故 $JB(t)=B(t)J$ 对所有参数成立。

### Step 2. 半单部分及零谱上的完整幂零链

先取正号七维块，并记
$$
x=\mathbf e_{1,1},\qquad
S=(\mathbf e_{0,1},\mathbf e_{2,1},\mathbf e_{3,1}),\qquad
T=(\mathbf e_{1,0},\mathbf e_{1,2},\mathbf e_{1,3}).
$$
$S,T$ 表示有序向量组三元组；矩阵按列为输入、行为输出。
令
$$
u=\begin{pmatrix}1/2\\1\\0\end{pmatrix},\quad v=u^{\mathsf T},\quad
C=\begin{pmatrix}-1/6&-1&1\\-1&0&0\\1&0&0\end{pmatrix}.
$$
由 Step 1 的全分类，
$$
B_0x=-x+Tu,\qquad B_0S=xv+TC,\qquad B_0T=0.
\tag{9}
$$
负号块是每个状态取反的相同矩阵；其他标准基向量由 $B_0$ 消去。
定义向量及线性泛函
$$
r=x-Tu,\qquad \ell=x^*-vS^*.
$$
则 $\ell r=1$、$B_0r=-r$、$\ell B_0=-\ell$。每块的投影为 $r\ell$；
以下 $P$ 表示两块之和。于是
$$
P^2=P,\quad\operatorname{rank}P=2,\quad B_0P=PB_0=-P.
$$
设 $Q=I-P$、$N=B_0+P$。将 (9) 代入得
$$
NS=TD,\quad Nx=NT=0,\qquad
D=C+uv=\begin{pmatrix}1/12&-1/2&1\\-1/2&1&0\\1&0&0\end{pmatrix}.
\tag{10}
$$
且 $Nr=0$。$\det D=-1$，故每块有三个独立长度二的幂零链。
在固定零谱空间 $\mathcal H_Q=\ker P$，用
$$
S'=QS=S+rv
$$
替换源向量，保留 $T$。把两个符号的源、汇分别合成六维空间
$\mathcal S,\mathcal T$；令 $\mathcal E$ 为十四个原标准基向量以外的闭线性张成。
得到有界拓扑直和
$$
\mathcal H_Q=\mathcal S\oplus\mathcal T\oplus\mathcal E,
\qquad
N=\begin{pmatrix}0&0&0\\D_6&0&0\\0&0&0\end{pmatrix},
\quad D_6=\operatorname{diag}(D,D).
\tag{11}
$$
特别地 $N^2=0$、$\operatorname{rank}N=6$，并且 $PN=NP=0$。
在 $\operatorname{ran}P$ 上 $B_0=-I$，在 $\ker P$ 上为 $N$。
这也重新确认 $-1$ 半单重二且 $P$ 就是它的 Riesz 投影。

### Step 3. 两条 leading 分支及二阶系数

在 $J$ 的两个闭特征空间 $\mathcal H_\eta$（$\eta=\pm1$）上，
$B_0$ 的 $-1$ 特征值各为简单。围绕 $-1$ 取半径 $1/3$ 的正向圆周。
由算子范数全纯性和 Neumann 逆级数，该圆周在小参数下仍属于预解集；
Riesz 积分定义全纯秩一投影 $P_\eta(t)$。
投影秩保持一，因为邻近投影之差范数小于一时可用显式近单位可逆算子共轭。

在这条一维不变空间上，$B(t)$ 的特征值 $b_\eta(t)$ 全纯，
$b_\eta(0)=-1$。取以固定左泛函归一化的全纯特征向量并微分特征方程，得到
$$
b_\eta'(0)=\ell_\eta B_1r_\eta.
\tag{12}
$$
这里 $r_\eta,\ell_\eta$ 由两符号的 $r,\ell$ 作奇偶组合并归一化
$\ell_\eta r_\eta=1$。此式并未对重复的总特征值任意选分支。

Step 1 表明 $B_1x=B_1S=0$。在 $T$ 输入到 $S$ 输出的角块中，
$T_0=(1,0)$ 经 (8) 到负号的 $S_0$，系数为 $1$；
$T_2=(1,2)$ 到正号的 $S_2=(2,1)$，其 $k=-4$，系数为
$2^4/4!=2/3$。$T_3$ 的 $b=3$ 不产生一阶项。
没有其他 $T\to S$ 一阶边，且 $B_1T$ 不含 $x$ 输出。
因此在奇偶块上该角矩阵是
$$
A_\eta=\operatorname{diag}(\eta,2/3,0).
\tag{13}
$$
由 $r=x-Tu$、$\ell=x^*-vS^*$ 得
$$
\ell_\eta B_1r_\eta=vA_\eta u
=\frac\eta4+\frac23=\frac{8+3\eta}{12}.
$$
乘以 $t$ 得 (2)。两系数相差 $1/2$，所以当 $t\ne0$ 充分小时两条特征值不同；
它们在总空间中也都是简单，而非仅在奇偶限制中简单。

### Step 4. 去除 leading 簇并固定剩余空间

设 $P(t)=P_+(t)+P_-(t)$、$Q(t)=I-P(t)$。
定义
$$
U(t)=P(t)P+Q(t)Q.
\tag{14}
$$
由于 $U(0)=I$，它在小圆盘上有全纯有界逆。
直接乘法给出 $U(t)P=P(t)U(t)$，因此
$U(t)^{-1}B(t)U(t)$ 关于固定分解 $\operatorname{ran}P\oplus\ker P$ 块对角。
其零谱块为
$$
\mathcal A(t)=Q U(t)^{-1}B(t)U(t)Q\big|_{\mathcal H_Q}
=N+tM(t),
\tag{15}
$$
其中 $M(t)$ 为迹范数全纯族。这来自全纯展开以及
$\mathcal A(0)=N$，不是仅逐矩阵项的形式除法。

本处还需要确知 $M(0)$，避免谱投影变化造成未计算项。
对 $P(t)^2=P(t)$ 微分，得 $PP'(0)P=QP'(0)Q=0$。
由 (14)，$QU'(0)Q=0$。因 $B_0$ 关于 $P,Q$ 块对角，
$$
Q[B_0,U'(0)]Q=0,\qquad
M(0)=QB_1Q\big|_{\mathcal H_Q}.
\tag{16}
$$
在 Step 2 的坐标下，$Q$ 不改变向量的 $S$ 坐标，并把 $S$ 变成 $S'$。
对 $T$ 向量有 $QT=T$。于是 $M(0)$ 的 $\mathcal T\to\mathcal S$ 角块
就是 (13) 的两符号六维版本，记为 $A_6$。
这里不需要忽略 $\mathcal E$ 耦合；它将在下步显式保留。

### Step 5. 平方根覆盖上的全无限维解析缩放

令 $\Pi_S$ 为直和 (11) 的源空间投影，$\Pi_R=I-\Pi_S$。
在 $s\ne0$ 时定义有界可逆算子
$$
V_s=s\Pi_S+\Pi_R.
$$
虽然 $V_s^{-1}$ 在零点发散，以下归一化整体有可去奇性：
$$
K(s)=s^{-1}V_s^{-1}\mathcal A(s^2)V_s.
\tag{17}
$$
先由 (11) 得 $s^{-1}V_s^{-1}NV_s=N$。
再将 $M(s^2)$ 按 $\mathcal S\oplus(\mathcal T\oplus\mathcal E)$ 分块，
则 (17) 精确写成
$$
K(s)=N+
\begin{pmatrix}
sM_{SS}(s^2)&M_{SR}(s^2)\\
s^2M_{RS}(s^2)&sM_{RR}(s^2)
\end{pmatrix}.
\tag{18}
$$
每一块是对迹类算子左右乘固定有界投影所得；其系数全纯且没有负幂。
所以 $K(s)$ 在零点延拓为固定空间上的迹范数全纯族，并特别有算子范数收敛。
它的零阶值是
$$
K_0=\begin{pmatrix}
0&A_6&G\\
D_6&0&0\\
0&0&0
\end{pmatrix},\qquad G=M(0)_{SE}.
\tag{19}
$$
$G$ 不一定为零；其像包含在六维 $\mathcal S$，故 (19) 仍为有限秩。
这一步控制了完整无限维余项，而非只对有限幂零块作形式 Newton 多边形计算。

### Step 6. 有效矩阵的全部非零谱

由 (19)，$K_0$ 的像包含 $\mathcal S\oplus\mathcal T$。
对任何非零特征值的广义特征向量，其 $\mathcal E$ 分量为零：
在 $\mathcal E$ 商空间上 $K_0$ 是零算子，而减去非零特征值后可逆。
因此其非零谱及代数重数完全由
$$
\begin{pmatrix}0&A_6\\D_6&0\end{pmatrix}
\tag{20}
$$
决定。$D_6$ 可逆，(20) 的特征多项式为
$\det(\nu^2I_6-A_6D_6)$。
在奇偶分解下，$D_6$ 各化为 $D$，$A_6$ 各化为 $A_\eta$。
使用 $DA_\eta$ 或 $A_\eta D$ 得相同特征多项式，因为 $D$ 可逆。
具体地
$$
DA_\eta=\begin{pmatrix}
\eta/12&-1/3&0\\
-\eta/2&2/3&0\\
\eta&0&0
\end{pmatrix}.
$$
其非零根来自二阶多项式
$$
\mu^2-\frac{8+\eta}{12}\mu-\frac\eta9.
\tag{21}
$$
当 $\eta=1$，判别式为 $145/144$；当 $\eta=-1$，判别式为 $-15/144$。
因此得到 (4) 的四个不同非零数。其各两个平方根彼此不同，总共八个，
且它们在 (20) 的特征多项式中均为简单根。
故 $K_0$ 的全部非零谱恰为这八个简单特征值。

### Step 7. 从极限谱恢复分支、重数与一致余谱

围绕八个非零 $\nu_j$ 取互不相交且不包围零点的小圆周。
由 $K(s)\to K_0$ 的算子范数收敛，每条圆周在小参数下仍位于预解集。
各 Riesz 投影全纯、秩保持一，故各有一条全纯简单特征值
$$
\nu_j(s)=\nu_j+O(s).
$$
对 $s\ne0$，(17) 是固定这个参数后的真实有界相似关系；因此
$\mathcal A(s^2)$ 的对应特征值是 $s\nu_j(s)$，代数重数不变。
再乘以 $t=s^2$，得到 $L(s^2)$ 的 (3)。其尺度与 (2) 分离，
当参数充分小时不会与两条 leading 分支碰撞。

为得到 (5)，不能仅证明每条固定序号的剩余特征值趋零。
给定任意 $\epsilon>0$，先取上述八条圆周足够小，再考虑一个固定大圆盘中
删去八个小圆盘及 $|z|<\epsilon$ 后的紧集。
该紧集在 $K_0$ 的预解集中，预解算子范数有统一界；Neumann 级数使它在
小 $s$ 下仍处于 $K(s)$ 的预解集。
大圆盘之外由 $K(s)$ 的局部统一算子范数界排除谱。
每个小圆盘内已由秩一投影穷尽一条简单特征值。因此其余全部谱均在
$|z|<\epsilon$ 内。由于 $\epsilon$ 任意，剩余谱最大模为 $o(1)$。
将其乘以 $|s|^3=|t|^{3/2}$ 就是 (5)。

最后，$\operatorname{Spec}\mathcal A(t)$ 在 $t=0$ 只有零点，
而 Step 4 的另一个固定块恰是 Step 3 已计的秩二块。
所有 $L(t)$ 的谱已被这些块覆盖，没有未处理的第三空间。
(2)—(5) 推出整体 $O(|t|)$ 及最大模 $|t|+O(|t|^2)$。∎

## Corrections, boundary cases, and open risks

- 当 $t=0$ 时 $L(0)=0$；定理讨论的是非零参数附近的分支，不声称
  $B(0)$ 就是原线性 cat 的普通 Koopman 算子。
- (2) 的偶、奇下标指 Fourier 反号对合，绝不表示特征值正负。
- (3) 的八条根来自完整低阶矩阵和全无限维归一化，
  不使用早期三频率简化的 $\sqrt{2/3}$ 首项猜测。
- 原动力系统为 $F_\kappa=A\circ S_\kappa$、$t=\pi\kappa$。
  若要把 (2)—(5) 称为其面积 Ruelle 共振定理，必须另证
  $1\oplus L(t)$ 的动力谱识别；本文件不越过该义务。
- 普通解析迹类理论、Riesz 投影与简单特征值全纯性是既有谱论。
  本文件把所需局部机制展开，以说明实际适用条件；不把这些一般工具当新贡献。
- 无数值实验，无候选评分，无正文容量声明。已停止的上同调及随机多点混合
  结果不作为本文件的证明依赖，也不拼接为本次谱结果。

## Input identity and actual execution

解析核输入为 320 行报告，SHA-256：
`c85dfa0ed29f1c6eb7d29d0898984bf9e2536da5ec89868c4582db9ea7381826`。
主控已全文读取该输入，再建立本文件的谱分裂论证。
有限层角块另有独立检查在进行，本文件作为作者证明先行封存送审。
本轮使用 `proof-writer` 将矩阵谱、动力谱识别与尚未授予的候选判断明确分开。
