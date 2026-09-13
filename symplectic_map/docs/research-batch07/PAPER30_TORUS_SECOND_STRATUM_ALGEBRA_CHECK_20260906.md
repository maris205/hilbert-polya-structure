# Paper30 环面小耦合：零阶与第二谱层的独立精确代数核查

日期：2026-09-06。性质：独立、有界、纯数学核查。
仅新增本文件；不修改作者原证明，不作数值实验、文献查新、Route 评价、
新意或容量评分。本文件使用 `proof-writer` 技能的完整证明与边界分离要求。

## Claim

在状态集 $\Lambda=\mathbb Z^2\setminus\{(0,0)\}$ 的标准基
$\mathbf e_{a,b}$ 上，给定沿边 $(a,b)\to(b,c)$ 的矩阵核
$$
B(t)_{(b,c),(a,b)}
=t^{|a|-2|b|+|c|-1}C_{b,k}(t),\qquad
k=a+c-3b,\qquad
C_{b,k}(t)=[z^k]\exp\{tb(z-z^{-1})\}.
\tag{1}
$$
非边位置为零，输入、输出状态均要求属于 $\Lambda$。写
$$
B(t)=B_0+tB_1+O(t^2).
\tag{2}
$$
核查下列纯代数结论：

1. $B_0$ 恰有两个相同七维支撑块，下面指定的 $u,v,C$ 全部正确；
   它的 $-1$ 谱投影为秩二投影 $P$，且 $B_0=-P+N$、$N^2=0$、
   $\operatorname{rank}N=6$。
2. 在 $Q=I-P$ 的六条长度二幂零链两端，$QB_1Q$ 的返回角块在反号奇偶
   $\eta\in\{1,-1\}$ 下为 $A_\eta=\operatorname{diag}(\eta,2/3,0)$。
3. 第二层有限矩阵的非零特征值恰为八个互异的简单数 $\pm\sqrt\mu$，其中
   $$
   \mu_{+,\pm}=\frac{9\pm\sqrt{145}}{24},\qquad
   \mu_{-,\pm}=\frac{7\pm i\sqrt{15}}{24}.
   \tag{3}
   $$
4. 反号算子与完整 $B(t)$ 对易。$-1$ 谱子空间在每个奇偶扇区各一维，
   相应归一化左右本征向量给出的第一扰动系数为
   $$
   \beta_\eta=\frac{8+3\eta}{12}.
   \tag{4}
   $$

## Status

`PROVABLE AS STATED`，限于上述矩阵代数结论。
给定的 $u,v,C,D,A_\eta$、四个 $\mu$、八个非零平方根，以及偶奇
$11/12,5/12$ 系数均保持不变，无需符号修正。

八个数是本文件有限第二层矩阵的简单非零特征值；本文件不把这一点单独表述为
无限维 $B(t)$ 或某个真实 Ruelle 算子的已经建立的八条谱分支。
第 8 步仅说明：若相应解析主分支由另外的解析谱论确立，则 (4) 强制决定其
一阶系数。全局核性、无限维重标度全纯性及 Ruelle 谱识别不在核查范围内。

## Assumptions

- 矩阵按“列为输入、行为输出”理解；$B_0,B_1$ 是 (1) 的 Taylor 系数，
  因而 $B_1=B'(0)$，没有额外阶乘。
- 原点状态从输入与输出两端排除。
- 输入材料中的固定空间解析 trace-class 性由另份作者证明处理；这里仅从
  (1) 独立计算零阶、一阶系数，并对由此形成的有限矩阵作精确代数证明。
- 不引用渐近数值计算、截断特征值实验或符号系统的近似输出。

## Notation

对符号 $\sigma\in\{1,-1\}$，定义七个基向量
$$
x_\sigma=\mathbf e_{\sigma,\sigma},\qquad
S_\sigma=(\mathbf e_{0,\sigma},\mathbf e_{2\sigma,\sigma},
\mathbf e_{3\sigma,\sigma}),\qquad
T_\sigma=(\mathbf e_{\sigma,0},\mathbf e_{\sigma,2\sigma},
\mathbf e_{\sigma,3\sigma}).
\tag{5}
$$
这里 $S_\sigma,T_\sigma$ 是有序的基向量组；若 $w$ 为三维列向量，
$T_\sigma w$ 表示其线性组合。相应的 $x_\sigma^*,S_\sigma^*,T_\sigma^*$
均是坐标泛函，而不是未经归一化的左本征向量。

记
$$
u=\begin{pmatrix}1/2\\1\\0\end{pmatrix},\qquad
v=\begin{pmatrix}1/2&1&0\end{pmatrix},\qquad
C=\begin{pmatrix}-1/6&-1&1\\-1&0&0\\1&0&0\end{pmatrix},
\tag{6}
$$
$$
D=C+uv=\begin{pmatrix}1/12&-1/2&1\\-1/2&1&0\\1&0&0\end{pmatrix}.
\tag{7}
$$
令 $\mathcal E$ 为 (5) 两个符号块之外全部标准基的闭线性包。
反号算子定义为 $J\mathbf e_{a,b}=\mathbf e_{-a,-b}$，奇偶参数
$\eta=1$ 表示 $J$ 的偶扇区，$\eta=-1$ 表示奇扇区。

## Proof Strategy

先用整数缺额的非负性与偶性穷尽零阶、一阶边，再逐列给出 $B_0$。
不假设候选投影正确，而是直接验证左右本征关系和幂等性。
通过 $Q$ 投影后的明确基，计算幂零链的返回角块；最后使用二次多项式判别式
和六维块行列式确定全部非零根与重数。主分支修正另以归一化左右向量直接求得。

## Dependency Map

1. 指数生成函数的系数展开与整数缺额偶性，给出全部 $B_0,B_1$ 支撑及符号。
2. 零阶支撑表给出 $u,v,C$，再给出左右向量 $r_\sigma,\ell_\sigma$。
3. 左右关系与 $\ell_\sigma r_\tau=\delta_{\sigma\tau}$ 给出 $P,N,Q,D$。
4. 一阶支撑分类给出 $T\to S'$ 角块 $A_\eta$，不依赖其他一阶块。
5. $D$ 可逆及 $A_\eta D$ 的三次特征多项式确定第二层有限矩阵全部重数。
6. 全核反号恒等式和相同的一阶角块给出主分支系数；谱分支存在性另行处理。

## Proof

### Step 1. 全部最低阶及下一阶边的穷尽分类

若 $b\ne0$，令 $K=|k|$。指数乘积展开给出
$$
C_{b,k}(t)=\epsilon_k\sum_{j=0}^{\infty}
\frac{(-1)^j(tb)^{K+2j}}{j!(K+j)!},\qquad
\epsilon_k=\begin{cases}1,&k\ge0,\\(-1)^K,&k<0.\end{cases}
\tag{8}
$$
因此 (1) 的最低参数阶为
$$
e=|a|+|c|+|a+c-3b|-2|b|-1,
\tag{9}
$$
此后只出现 $e+2,e+4,\ldots$ 阶。置 $b=\sigma\beta$，其中
$\beta=|b|\ge1$，再置 $A=\sigma a$、$H=\sigma c$，以及
$$
L=|A|+|H|+|A+H-3\beta|-3\beta.
\tag{10}
$$
因为三实数 $A,H,3\beta-A-H$ 的和为 $3\beta>0$，三角不等式给出
$L\ge0$；等号成立当且仅当三数都非负，即
$$
L=0\quad\Longleftrightarrow\quad A\ge0,\ H\ge0,\ A+H\le3\beta.
\tag{11}
$$
对任意整数 $n$ 有 $|n|\equiv n\pmod2$，故
$$
L\equiv A+H+(A+H-3\beta)-3\beta\equiv0\pmod2.
$$
于是
$$
e=\beta-1+L,\qquad L\in2\mathbb Z_{\ge0}.
\tag{12}
$$

由 (12)，$e=0$ 当且仅当 $\beta=1,L=0$；$e=1$ 当且仅当
$\beta=2,L=0$。此外，$e=0$ 边的 (8) 下一项是二阶，不能对 $B_1$ 作贡献。
综上，对于每个 $\sigma\in\{1,-1\}$：

- $B_0$ 恰在 $(\sigma A,\sigma)\to(\sigma,\sigma H)$ 非零，
  其中 $A,H\ge0$、$A+H\le3$，每个符号共 $10$ 条边。
- $B_1$ 的 $b\ne0$ 部分恰在
  $(\sigma A,2\sigma)\to(2\sigma,\sigma H)$ 非零，
  其中 $A,H\ge0$、$A+H\le6$，每个符号共 $28$ 条边。

在这些边上，令 $d=3\beta-A-H\ge0$，则 $k=-\sigma d$。
直接代入 (8)，两个符号块的首项系数完全相同，均为
$$
\frac{(-1)^d\beta^d}{d!}.
\tag{13}
$$
特别地，负块不是额外再乘一个统一的 $(-1)^d$；负的 $b$ 与 $k$ 符号
已在 (8) 中共同计入。

若 $b=0$，只有 $k=0$ 才有 $C_{0,k}=1$，故 $c=-a$ 且
$$
B(t)_{(0,-a),(a,0)}=t^{2|a|-1},\qquad a\ne0.
\tag{14}
$$
这里无零阶项。一阶项恰为 $(1,0)\to(0,-1)$ 与
$(-1,0)\to(0,1)$，系数均为 $1$。因此 $B_0$ 一共 $20$ 个非零矩阵项，
$B_1$ 一共 $58$ 个非零矩阵项，以上分类穷尽全部整数边。

### Step 2. 两个零阶七维块的直接计算

对正符号块，以 $A=0,1,2,3$ 为输入第一坐标，以 $H=0,1,2,3$ 为
输出第二坐标，(13) 给出矩阵表
$$
\begin{array}{c|rrrr}
 &A=0&A=1&A=2&A=3\\\hline
H=0&-1/6&1/2&-1&1\\
H=1&1/2&-1&1&0\\
H=2&-1&1&0&0\\
H=3&1&0&0&0
\end{array}.
\tag{15}
$$
负块的表相同，由 (13) 的双符号计算保证。
表中输入、输出标准基的并集恰为 (5) 的七个向量。
因此对每个 $\sigma$，
$$
B_0x_\sigma=-x_\sigma+T_\sigma u,\qquad
B_0S_\sigma=x_\sigma v+T_\sigma C,\qquad
B_0T_\sigma=0,
\tag{16}
$$
且 $B_0|_{\mathcal E}=0$。式 (16) 独立验证了 (6) 的全部元素。

### Step 3. 精确谱投影与幂零部分

定义
$$
r_\sigma=x_\sigma-T_\sigma u,\qquad
\ell_\sigma=x_\sigma^*-vS_\sigma^*,\qquad
P=\sum_{\sigma=\pm1}r_\sigma\ell_\sigma.
\tag{17}
$$
由于 $r_\sigma$ 只有同符号的 $x,T$ 分量，
$\ell_\sigma r_\tau=\delta_{\sigma\tau}$，从而 $P^2=P$，
$\operatorname{rank}P=2$。由 (16) 分别作用于 $x,S,T,\mathcal E$，得到
$$
B_0r_\sigma=-r_\sigma,\qquad
\ell_\sigma B_0=-\ell_\sigma,\qquad
B_0P=PB_0=-P.
\tag{18}
$$
令 $N=B_0+P$。逐列计算得
$$
Nx_\sigma=0,\qquad
NS_\sigma=T_\sigma(C+uv)=T_\sigma D,\qquad
NT_\sigma=0,\qquad N|_{\mathcal E}=0.
\tag{19}
$$
式 (7) 中第一元素为 $-1/6+1/4=1/12$，两个非对角元素为
$-1+1/2=-1/2$。沿第三行展开得
$$
\det D=\det\begin{pmatrix}-1/2&1\\1&0\end{pmatrix}=-1.
\tag{20}
$$
因此 $N$ 的像恰为两个 $T$ 空间之和，维数 $6$。
由 (19)，$N^2=0$；由 (18)，$PN=NP=0$。于是
$$
B_0=-P+N,\qquad B_0^2=P,\qquad B_0^3=-P=-B_0^2.
\tag{21}
$$
在 $\operatorname{ran}P$ 上 $B_0=-I$，在 $\ker P$ 上
$B_0=N$ 且平方为零，故 $P$ 确为 $-1$ 的谱投影，特征值 $-1$
半单、代数与几何重数均为 $2$。此外
$\operatorname{rank}B_0=2+6=8$。

### Step 4. $Q$ 空间的精确基及角块坐标

令 $Q=I-P$，并定义有序三元组
$$
S'_\sigma=QS_\sigma=S_\sigma+r_\sigma v.
\tag{22}
$$
由 (17)，$Qr_\sigma=0$、$QT_\sigma=T_\sigma$。
每个原七维块有基 $(r_\sigma,S'_\sigma,T_\sigma)$，因为
$$
x_\sigma=r_\sigma+T_\sigma u,\qquad
S_\sigma=S'_\sigma-r_\sigma v.
$$
所以
$$
\operatorname{ran}Q
=\operatorname{span}\{S'_+,S'_-,T_+,T_-\}\oplus\mathcal E,
\qquad NS'_\sigma=T_\sigma D.
\tag{23}
$$
投影 $Q$ 只加减 $r_\sigma$，而 $r_\sigma$ 没有原始 $S$ 坐标。
故对任意 $y$，$Qy$ 在基 $S'_\sigma$ 下的系数，正是 $y$ 原来的
$S_\sigma$ 坐标。这个事实保证返回角块可从原核的 $T\to S$ 项直接读取，
无需把 $S'$ 当作原正交基或混入额外投影系数。

### Step 5. 一阶返回角块的全部边

设输入为 $T_{\sigma,i}=(\sigma,\sigma h_i)$，其中
$(h_1,h_2,h_3)=(0,2,3)$；目标为 $S_{\tau,j}=(\tau h_j,\tau)$。
形成核边的必要条件为 $\sigma h_i=\tau h_j$。
逐一分三种可能：

1. $h_i=h_j=0$：由 (14)，必须 $\tau=-\sigma$，系数为 $1$。
2. $h_i=h_j=2$：必须 $\tau=\sigma$，此时 $\beta=2,A=H=1$，
   由 (13) 得 $d=4$，一阶系数为 $2^4/4!=2/3$。
3. $h_i=h_j=3$：必须 $\tau=\sigma$，但 $\beta=3$ 使
   (12) 的 $e\ge2$，因此一阶系数为零。

不同 $h_i,h_j$ 不可能满足必要条件。于是 $QB_1Q$ 从 $T$ 空间返回
$S'$ 空间的角块，对同符号和反符号分别为
$$
A_{\sigma,\sigma}=\operatorname{diag}(0,2/3,0),\qquad
A_{-\sigma,\sigma}=\operatorname{diag}(1,0,0).
\tag{24}
$$
式 (24) 没有声称 $B_1T$ 全部落在 $S'$ 中；其余输出可落在
$\mathcal E$ 或其他分量，而不改变这里明确定义的角块。

### Step 6. 反号对称及奇偶约化

由生成函数换元 $z\mapsto z^{-1}$，
$$
C_{-b,-k}(t)=C_{b,k}(t).
\tag{25}
$$
权重指数也在 $(a,b,c)\mapsto(-a,-b,-c)$ 下不变，故 (1) 给出
$JB(t)=B(t)J$，是对完整核的精确恒等式。
此外 $Jr_\sigma=r_{-\sigma}$，$JS'_\sigma=S'_{-\sigma}$，
$JT_\sigma=T_{-\sigma}$，因此 $P,Q,N$ 也与 $J$ 对易。

在奇偶 $\eta$ 的基 $S'_++\eta S'_-$、$T_++\eta T_-$ 下，
由 (24)，返回角块为
$$
A_\eta=\operatorname{diag}(\eta,2/3,0),
\tag{26}
$$
而 $N$ 的前向角块仍为 $D$。

### Step 7. 第二层有限矩阵的根与全部重数

在上述每个奇偶六维核心上，定义第二层有限矩阵
$$
M_\eta=\begin{pmatrix}0&A_\eta\\D&0\end{pmatrix},
\tag{27}
$$
其中前后三维分别按 $S'$、$T$ 排列。
由于 $D$ 可逆，$DA_\eta=D(A_\eta D)D^{-1}$，故两种乘积具有相同
特征多项式与重数。直接计算
$$
A_\eta D=
\begin{pmatrix}
\eta/12&-\eta/2&\eta\\
-1/3&2/3&0\\
0&0&0
\end{pmatrix},
$$
$$
\det(\mu I-A_\eta D)
=\mu\left(\mu^2-\frac{8+\eta}{12}\mu-\frac{\eta}{9}\right).
\tag{28}
$$
对 $\eta=1$，二次因子的判别式为 $145/144$，其根即 (3) 的
$\mu_{+,\pm}$。对 $\eta=-1$，判别式为 $-15/144$，根即
$\mu_{-,\pm}$。两个二次因子的常数项均非零，所以四根均不为零。
前一对是互异实根，后一对是互异非实共轭根，因此四根两两互异。

先对 $\zeta\ne0$ 用 Schur 补，再由多项式恒等延拓至所有 $\zeta$，得
$$
\det(\zeta I-M_\eta)
=\det(\zeta^2I-A_\eta D)
=\zeta^2
\left(\zeta^4-\frac{8+\eta}{12}\zeta^2-\frac{\eta}{9}\right).
\tag{29}
$$
每个非零 $\mu$ 产生两个互异数 $\pm\sqrt\mu$；不同 $\mu$ 的平方根
不可能重合。由于每个 $\mu$ 是简单根且 $2\zeta\ne0$，(29) 中这八个
非零根全部为简单根，不依赖平方根支路的命名选择。

零点在每个 (29) 中代数重数为 $2$。对 $p,q\in\mathbb C^3$，有
$$
M_\eta(p,q)=0\quad\Longleftrightarrow\quad Dp=0,\ A_\eta q=0.
$$
由 (20)，$p=0$；由 (26)，$\ker A_\eta$ 一维。因此每个奇偶块零特征值
几何重数为 $1$，恰对应一个长度二的零 Jordan 块。
两奇偶块合计：八个简单非零特征值，零点代数重数 $4$、几何重数 $2$。
这些重数专指十二维核心 $M_+\oplus M_-$，不把无限维剩余零空间计入有限重数。

### Step 8. 主分支第一修正的符号与归一化

定义奇偶右向量与左泛函
$$
R_\eta=r_++\eta r_-,\qquad
L_\eta=\frac{\ell_++\eta\ell_-}{2}.
\tag{30}
$$
使用大写符号避免与频率正负块 $r_\sigma,\ell_\sigma$ 混淆。
由 (17)，$L_\eta R_\eta=1$；不同奇偶的左右配对为零。
每个奇偶扇区内 $P$ 的秩为 $1$，其投影为 $R_\eta L_\eta$。

由第 1 步，一阶非零列只可能有 $b=\pm2$ 或 (14) 的 $b=0$，所以
$$
B_1x_\sigma=0,\qquad B_1S_\sigma=0.
\tag{31}
$$
另外 $B_1T_\sigma$ 没有任一 $x_\tau$ 分量：$T$ 输入的第二坐标
属于 $\{0,\pm2,\pm3\}$，必等于输出的第一坐标，而 $x_\tau$ 的
第一坐标是 $\pm1$。结合 (17) 的左右向量公式，有
$$
L_\eta B_1R_\eta=vA_\eta u
=\frac\eta4+\frac23=\frac{8+3\eta}{12}.
\tag{32}
$$
这里两个负号分别来自 $r_\sigma$ 的 $-T_\sigma u$ 与
$\ell_\sigma$ 的 $-vS_\sigma^*$，故符号为正。
等价地，$PB_1P$ 在 $(r_+,r_-)$ 基下的矩阵为
$$
\begin{pmatrix}2/3&1/4\\1/4&2/3\end{pmatrix},
\tag{33}
$$
其偶奇本征值分别为 $11/12$、$5/12$。

若其他解析谱论步骤已给出每个奇偶扇区内的解析主分支
$b_\eta(t)$ 与解析右向量 $R_\eta(t)$，满足
$b_\eta(0)=-1$、$R_\eta(0)=R_\eta$，对
$B(t)R_\eta(t)=b_\eta(t)R_\eta(t)$ 在零点求导，并左乘
$L_\eta$，利用 $L_\eta B_0=-L_\eta$，得到
$b'_\eta(0)=L_\eta B_1R_\eta$。因此必有
$$
b_+(t)=-1+\frac{11}{12}t+O(t^2),\qquad
b_-(t)=-1+\frac{5}{12}t+O(t^2).
\tag{34}
$$
同一个矩阵族 $tB(t)$ 的对应分支随即为
$$
-t+\frac{11}{12}t^2+O(t^3)\quad\text{（偶）},\qquad
-t+\frac{5}{12}t^2+O(t^3)\quad\text{（奇）}.
\tag{35}
$$
式 (35) 不自行识别 $tB(t)$ 与任何另一算子的谱。上述全部有限代数结论证毕。$\square$

## Corrections or Missing Assumptions

- 本轮待核公式无错误，无需修改原断言。
- (30) 中左泛函的 $1/2$ 不能漏去；若左右都取未归一化奇偶和，
  则左右配对为 $2$，计算扰动系数时必须除以该配对。
- 第二层每个奇偶六维核心除了四个简单非零根，还保留一个长度二零 Jordan 块。
  “八个简单根”只指非零第二层常数，不声称十二维核心全部简单。

## Open Risks

本文件代数范围内无未闭合步骤。以下义务明确交由其他工作承担，不能由本核查替代：

1. 固定 Hilbert 空间上的解析 trace-class 族及其适用参数圆盘。
2. 参数依赖谱投影转为固定 $Q$ 空间、无限维重标度算子的全纯性，
   以及剩余谱的统一阶数控制。
3. 有限第二层八个简单常数到真实无限维谱分支的转移。
4. 任何 Ruelle 共振、周期迹或动力系统谱不变性识别。

本文件未审核其他作者提出的第 2 项抽象引理，亦未将其视为本轮已独立核查结论。
