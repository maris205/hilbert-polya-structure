# Paper31 D05：原四阶整模及自由格缺陷的固定锚点 V1

日期：2026-09-09 UTC；作者：主控 `/root`。`route_applicability: NOT_APPLICABLE`。
本件在已选择的 $q=1,n=4\to5,p=3$ 诊断对象内解析旧四阶核，不扩大次数或参数。
不是正式候选、独立审查、新意票或全次数分类；旧失败、旧猜想和所有冻结件保持。

## Claim

令 $A=\mathbb Z[\tau]_{(3,\tau)}$，$M=M_4\otimes A$，其中 $M_4$ 是[原相邻扩张][D05]中整个实际余核。
定义 $V=\operatorname{coker}(A\xrightarrow{(\tau^3,3\tau^2)^t}A^2)$。
本件限定证明
$$M\cong A^2\oplus V^{\oplus2}\oplus A/(\tau)\oplus(A/(\tau^3))^{\oplus3}.\tag{1}$$
若 $T=\{m\in M:\tau^N m=0\text{ 对某个 }N\}$，$L=M/T$，则进一步有
$$T\cong(A/(\tau^2))^{\oplus2}\oplus A/(\tau)\oplus(A/(\tau^3))^{\oplus3},\quad
L\cong A^2\oplus(3,\tau)^{\oplus2}.\tag{2}$$
所以 $L^{**}/L\cong(A/(3,\tau))^{\oplus2}$；泛特征与特征三专门化的完整 $\tau$-扭子长度分别为 $14,16$。
这里的 $T$ 在 $A$ 上是原模扭子，不等于特征三专门化后的全部扭子。

## Status

`PROVABLE AS STATED`，作者结论，等待非作者检查。
证明含固定规模的可复算精确矩阵证书；这是有限的符号基底等价，不是根据域上 rank/Smith 数表外推。
一般 $p$、其他次数及全部 $n$ 的原规范块分类仍 `OPEN`；不把本锚点计成独立长文的主结果。

## Assumptions and Notation

采用 D05 式 (7) 的原四簇评价、原受限源 $V_4$ 及 $W_4$，在 $q=1$ 后局部化到 $A$。
整数 $2$ 在 $A$ 是单位，$3,\tau$ 均非单位；下文只允许分母为 $2$ 的幂。
用 $A_0,B_0,\ldots,J_0$ 表示十个剩余目标的**自由生成元**，不将其当成余核上的变量作用。
$N^*=\operatorname{Hom}_A(N,A)$；双对偶中的映射为自然评估映射。
专门化长度分别在 $\mathbb Q[[\tau]]$ 和 $\mathbb F_3[[\tau]]$ 上计算，只计其扭子部分。

## Proof Strategy and Dependency Map

1. 从原 $40\times41$ 矩阵中用五个原截面关系更换源基底，再消去30个单位可缩块。
2. 核对六个剩余关系，并给两组行列式均为单位的显式基底变换，得到 (1)。
3. 对单个混合块直接计算其饱和子模、扭子和无扭商，得到 (2) 与缺陷。
4. 专门化原呈示直接计算长度；不假设取扭子与基变换交换。

## Proof

### Step 1. 固定原矩阵到六关系的精确证书

原 $J_4$ 由 D05 式 (7) 定义；[伴随脚本][CODE]只读调用[原固定核验实现][HELPER]的 `actual_jet(4)`。
其行按 $(r,a,b)$ 字典次序、源按 $(i,j)$ 字典次序排列。源维数41，目标维数40。
取 $s_0=xy,s_1=x^2-x^2y+xy^2-\tau y$，五个 $s_0^{4-k}s_1^k$ 都在原核中。
在五个源坐标 $(4,4+k)$ 上的系数小行列式为1；本件脚本逐项验证这两条有限多项式恒等式。
因此可将该五个源基向量替换成上述五个核向量，而保留其他36个原单项式，得到行列式为单位的新源基底。
丢去五个零列不改变余核；不需要用某一域上的核维数代替这一步。

对余下 $40\times36$ 矩阵，固定执行 helper 的 `unit_reduce`：按现存行、现存源列顺序选首个常数局部单位 $c$，
消去其所在行列，以 $b_{ij}\leftarrow b_{ij}-b_{ic}b_{rj}/c$ 更新其余项。
此处第二个下标 $c$ 指所选列；除数 $c$ 指该 pivot 的数值。
每次操作由初等行列变换和删除一个同构 $A\xrightarrow{c}A$ 组成，故保余核；
脚本断言实际恰30次，pivot 数值只有 $\pm1$，并核对新源列在原源中的精确证书。
算法终止时的十个原目标标签依次为
$$
(2,1,0),(2,2,0),(2,2,1),(2,3,0),(3,0,0),
(3,1,0),(3,1,1),(3,2,0),(3,2,1),(3,3,0).
$$
以此指定 $A_0,\ldots,J_0$，剩余六个完整关系准确为
$$\begin{aligned}
c_0&=\tau^2B_0+2\tau C_0+\tau^2H_0+2\tau I_0,\\
c_1&=\tau^3D_0+\tau^3J_0,\\
c_2&=\tau^3B_0+3\tau^2C_0,\\
c_3&=\tau^3H_0+3\tau^2I_0,\\
c_4&=2\tau^3F_0+3\tau^2G_0+\tau^4J_0,\\
c_5&=-\tau^3A_0-\tau^3F_0.
\end{aligned}\tag{3}$$
本件脚本将剩余矩阵与 (3) 的全部60个条目逐项比较，零条目亦参与，不按抽选子式判断。
输入原式、确定性消元规则、实际单位限制与完整输出 (3) 构成固定有限证书；没有未指定的浮点或数值 rank 步骤。

### Step 2. 完整显式块化

在十维自由目标中依次采用下列新生成元：
$$E_0,\ J_0,\ 2F_0+\tau J_0,\ G_0,\ H_0,\ I_0,\ D_0+J_0,\ A_0+F_0,
\ B_0+H_0,\ C_0+I_0+\frac\tau2(B_0+H_0).\tag{4}$$
该基底变换的行列式为 $-2$，在 $A$ 可逆。
将源关系依次改成
$$c_4,\ c_3,\ c_1,\ -c_5,\ -2c_2-2c_3+3\tau c_0,\ c_0/2.\tag{5}$$
其行列式为 $-1$。在 (4) 的基底下，前两个关系分别是第3–4及5–6生成元上的列 $(\tau^3,3\tau^2)^t$；
后三个三阶关系分别是第7、8、9生成元上的 $\tau^3$，最后是第10生成元上的 $\tau$。
第1、2生成元没有关系。这可直接将 (3) 代入 (5) 验证，脚本还核对整个 $10\times6$ 等价式。
所有变换均在原自由呈示中实施，没有把已消去余核类非法乘 $u$ 或 $v$。
所以 (1) 是原 $M_4$ 的真直和分解，不只是相邻扩张的拉回／推出消费者。

### Step 3. 混合块的扭子与非自由格

在 $A^2$ 内令 $v=(\tau,3)^t$。$A$ 为 UFD，$3,\tau$ 无公共非单位因子，
故直线 $\operatorname{Frac}(A)v$ 与 $A^2$ 的交恰为 $Av$：若 $a\tau,a3\in A$，约分后的 $a$ 之分母必同时整除 $\tau,3$，因而是单位。
$V=A^2/(\tau^2Av)$ 的全部整环扭子因此是 $Av/(\tau^2Av)\cong A/(\tau^2)$，也是其全部 $\tau$-扭子。
映射 $A^2\to A,(a,b)\mapsto3a-\tau b$ 的像为 $(3,\tau)$、核为 $Av$，故
$$0\longrightarrow A/(\tau^2)\longrightarrow V\longrightarrow(3,\tau)\longrightarrow0.\tag{6}$$
不声称 (6) 分裂；事实上 $V$ 只需两个最小生成元，而假设的分裂和需要三个。
由 (1) 对直和逐项取扭子，即得到 (2)。

理想 $I=(3,\tau)$ 的对偶可识别为 $I^{-1}=\{a\in\operatorname{Frac}(A):aI\subset A\}=A$，证明仍是上述互素分母论证。
因此 $I^{**}=A$，自然映射为原包含 $I\subset A$，其余核为 $A/(3,\tau)$。
由 (2) 得 $L^{**}/L\cong(A/(3,\tau))^{\oplus2}$，其残余域维数为2。

### Step 4. 原专门化的完整扭子长度

在 $\mathbb Q[[\tau]]$ 上，$3$ 为单位，$V$ 的单列 $(\tau^3,3\tau^2)^t$ 可消为 $(\tau^2,0)^t$。
两个 $V$ 贡献长度 $2+2$，其余循环块贡献 $1+3+3+3$，合计 $14$。
在 $\mathbb F_3[[\tau]]$ 上，该原列成为 $(\tau^3,0)^t$，两个 $V$ 贡献 $3+3$，其余不变，合计 $16$。
两边自由秩均为4；长度差2与上述双对偶缺陷维数一致。
本计算不把 $T/3T$ 错认成专门化余核的全部扭子；额外两单位长度来自原非自由格。限定 Claim 得证。∎

## Actual Evidence, Corrections and Open Risks

本轮先有固定 $(9,\tau^4)$ 的 [Ext 消灭子必要条件核验][NULL]，实际输出为 `NO_COUNTERCERTIFICATE`。
该零结果不证明任何分解，也不因本件后续证明而回写为旧测试成功。
本件另外给出上述显式完整变换，实际运行 `python docs/research-batch07/qpi_nonunit_m4_integral_block_certificate_v1_20260909.py`，
退出码0，精确符号运行 $0.153188$ 秒、GPU0；[JSON][JSON] 保存这次实际输出的同一数据（仅压缩空白）。
没有反复扩大原必要条件、修改阈值或扫描新次数。该执行与独立数学接受仍分开。
主控本人已全文读取本件脚本、helper及新的 D05 作者包；本件自身按 proof-writer 组织完整命题、依赖、证明和边界。
新风险是 Step 1 原矩阵消元转录与 Step 2 完整等价，以及 Step 3 饱和商的身份；交非作者直接检查这些实际变化。

本锚点不解决全 $n$ 格缺陷 $E_n=L_n^{**}/L_n$，不证明每个素数首现，不把两个混合块拼成新论文容量。
唯一后续目标是用原全次数扩张控制实际 $L_n$ 或 $E_n$；标准 UFD 饱和、双对偶与特征专门化机制须在新意评价中扣除。
原相邻 $P_m$ 消费者与本件真实 $M_4$ 分块的逻辑身份不同，不能将两者的最好结果拼成未证的全次数分类。

[D05]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[CODE]: qpi_nonunit_m4_integral_block_certificate_v1_20260909.py
[HELPER]: qpi_nonunit_adjacent_extension_check_v1_20260909.py
[JSON]: PAPER31_QPI_NONUNIT_M4_INTEGRAL_BLOCK_CERTIFICATE_V1_20260909.json
[NULL]: PAPER31_QPI_NONUNIT_M4_EXT_ANNIHILATOR_CHECK_V1_20260909.json
