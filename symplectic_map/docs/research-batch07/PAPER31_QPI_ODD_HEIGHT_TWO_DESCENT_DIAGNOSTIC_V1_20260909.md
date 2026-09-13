# D01 Proof Package — fixed odd height-two local descent

日期：2026-09-09。作者证明包，等待非作者对新数学与证书检查；不是正式立项、Route A/B 评价或论文验收。既有 I01/I03 C/D 输入保持冻结。

## Claim

固定 $p=3,m=1,a=2,t_2=1,q=\zeta_9,\pi=q-1$。保持原降序九因子迹、原能级函数

$$
j=J_1(x,y;1)=y-x+x/y-1/x,\qquad z=j-1,\qquad H=j^2-1.
$$

设 $k=\mathbb F_9=\mathbb F_3[a]/(a^2+a+2)$，原环面的残余点为 $P:(x,y)=(a,2)$。在下述完成局部环 $S$ 中，原整除状态形式及其完整两系数理想为

$$
\alpha_9=\frac{1}{9}d_{\mathrm{state}}I_{9,q},\qquad
C=\mathfrak c(\alpha_9)\subset S.
$$

本包证明以下限定结论。

1. 对 $B=\mathcal O[[z]]\subset S$，若一个理想来自 $B$ 的扩张，则每个固定 $\mathcal O,z$ 的连续导子 $D$ 必须保持该理想。有限截断中的严格失败只能据此否定指定基底的精确理想下降。
2. 本次原理想实际满足完整等式

   $$
   C=QS,\qquad Q=(\pi^2-z^4,\pi z^3)\subset B.
   \tag{C}
   $$

   这不是有限截断通过的外推；二阶系数恒等式和原两生成元的一条单位 syzygy 直接控制全部高阶尾项。
3. 对任意 $f\in S$，令 $j'=j+\pi f,z'=j'-1$，则

   $$
   (\pi^2-z'^4,\pi z'^3)S=(\pi^2-z^4,\pi z^3)S.
   \tag{L}
   $$

   因而在该完成邻域中，允许改变残余能级的局部提升不会产生新的精确理想障碍。
4. $B/Q$ 的 $k$-维数为 $10$。对所证邻域中每个允许的无分歧状态，$v_\pi(\alpha_9)=2$，从而 $v_\pi(dI_{9,q})=14$。

空间范围仅为原环面的固定点 $P$ 的完成邻域；不宣称原 $j$ 在 $q=\zeta_9$ 的四末端图正则，也不宣称本等式覆盖完整八中心模型或完整 Hasse 纤维。

## Status

`PROVABLE AS STATED`，指上面明确限定的局部命题。作者层面的证明由已接受原矩阵输入、精确有限 Laurent 多项式证书和局部代数消元组成；尚未由非作者接受。

方向诊断：`SHORT_CLOSED_INTERFACE / STOP_FULL_I01_INVESTMENT`。没有得到需要新增非短比较骨架的下降障碍或原状态阶差异；不因精确计算成功而上调旧查新分数。

## Assumptions

- $\mathcal O_0=W(k)$，$\mathcal O=\mathcal O_0[\zeta_9]$；$\mathcal O$ 为完成离散赋值环，$v_\pi(3)=6$，故 $\mathcal O/(\pi^n)$ 在 $n\le6$ 时特征为 $3$。
- $x,y$ 是原矩阵的两个状态变量，$d$ 固定 $\mathcal O,t_2$ 及谱变量。时间没有重新选择，矩阵没有作等谱替换。
- $S$ 是 $\mathcal O[x^{\pm1},y^{\pm1}]$ 在残余点 $P$ 的完成局部环。取 $w=y-2$。在 $P$ 有 $j_x=a\ne0$，因此 $S\simeq\mathcal O[[z,w]]$，$B=\mathcal O[[z]]$ 是指定原能级基底。
- 所称无分歧状态为局部连续 $\mathcal O$-代数映射 $S\to\mathcal O'$，其中 $\mathcal O'/\mathcal O$ 有限无分歧并将闭点映到所选点或其残余域扩张；特别有 $z,w\in\pi\mathcal O'$。

## Notation

用 $Z$ 表示谱变量，避免与局部能级坐标 $z$ 混淆。写

$$
u=j+1=z+2,\qquad H=zu,\qquad d_0=y-1,\qquad b=x(y-1).
$$

这里 $u$ 在 $S$ 中为单位。用 $\Omega=S\,dx\oplus S\,dy$ 表示原环面的相对余切模扩张到 $S$，亦即连续相对微分模。$\mathfrak c(\alpha)$ 指该模任一正则基底下的两系数理想；可逆换基不改变它。对状态 $s$，$v_\pi(\alpha(s))$ 指两个系数赋值的最小值。

## Proof Strategy

先证明导子必要条件，再保留完整原积分的整除顺序，计算首个超出已知首 jet 的 $\pi^2$ 系数。此系数沿纤维的全部依赖可被 $H^3$ 吸收；其余项 $(j+1)dj$ 是单位法向项。与首 jet 的单位切向系数配对后，一条原两生成元关系给出 $\pi^3\in C$，故不需继续提升 jet。

## Dependency Map

1. 原矩阵与整除合法性：已接受 [原矩阵定义](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex) 及 [整数 cyclic insertion](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex)。本作者已本人读取这些所需原源。
2. 首 jet 因子 $H^3$：已接受 [完整奇素首 jet 定理](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/07-odd-jets.tex)，使用明确的共同二阶商和匹配时间 $t=1$，不是自然 cyclotomic 嵌入。下述证书另直接核对本例两个一阶系数的整除性与切向单位值。
3. 新增二阶信息：Proof Step 3 的精确 Laurent 恒等式；[伴随精确脚本](qpi_odd_height_two_descent_diagnostic_v1_20260909.py) 是可复算证书，不是数值采样。
4. 完整下降式：Step 4 的单位 syzygy 和 Step 5 的理想相等证明。
5. 提升不变性、长度和状态阶：分别由 Steps 6–7 的有限局部代数推出，不使用有限平台猜测。

## Proof

### Step 1. 指定基底下降的导子必要条件

设 $J\subset B$ 且 $C_0=JS$。取连续 $\mathcal O$-导子 $D:S\to S$，满足 $D(z)=0$。由连续性和幂级数展开，$D$ 在 $B$ 上为零。每个 $c\in C_0$ 是有限和 $\sum_i a_iq_i$，其中 $a_i\in S,q_i\in J$；Leibniz 公式给出

$$
D(c)=\sum_i D(a_i)q_i\in JS=C_0.
$$

若 $K\subset S$ 还满足 $D(K)\subset K$，则导子下推到 $S/K$，并保持 $C_0$ 的像。因此某个严格的有限余类 $D(\bar c)\notin\bar C_0$ 足以否定该指定基底的精确下降。

反向不成立。特征 $3$ 的相对幂级数环中，$(w^3)$ 被 $\partial_w$ 及其任意函数倍数保持，却不来自不含 $w$ 的基底。下文有限检验的 $w^3$ 截断尤其具有这种 Frobenius 盲区。

### Step 2. 固定原矩阵与完整整除展开

所用矩阵严格为

$$
A(Z)=
\begin{pmatrix}1-b&-x\\d_0(b-1)&b\end{pmatrix}
+Z\begin{pmatrix}j-1&1\\j+b-1&1\end{pmatrix}
+Z^2\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

其迹为 $1+jZ+Z^2$，行列式为 $Z^3$。定义

$$
M^{(0)}=\mathrm{id},\qquad M^{(r+1)}=A(q^rZ)M^{(r)}\quad(0\le r<9),
\qquad I_{9,q}=[Z^9]\operatorname{tr}M^{(9)}.
\tag{R}
$$

左乘递推保留原降序 $A(q^8Z)\cdots A(Z)$，未交换矩阵因子。所有中间谱次数大于 $9$ 的项可以舍去，因为其余因子无负谱次数，不能回流到 $[Z^9]$。

整数 cyclic insertion 给出

$$
\alpha_9=[Z^9]\operatorname{tr}\bigl(dA(Z)A(q^8Z)\cdots A(qZ)\bigr).
$$

因此先在 $\mathbb Z[q]/(q^6+q^3+1)$ 中计算完整迹，逐状态微分后除以 $9$ 是整的。不能把残余迹 $j^9$ 先微分再除以 $9$。

更具体地，将 (R) 的 $[Z^9]$ 约化为唯一的

$$
T=\sum_{e,f,r}c_{e,f,r}x^ey^fq^r,\qquad 0\le r\le5,\quad c_{e,f,r}\in\mathbb Z.
$$

此次共有 $427$ 个非零 Laurent 项。整数整除在每个基底系数上成立。令

$$
A_\nu=\sum_{e,f,r}\frac{e c_{e,f,r}}9\binom r\nu x^{e-1}y^f\pmod3,
\qquad
B_\nu=\sum_{e,f,r}\frac{f c_{e,f,r}}9\binom r\nu x^ey^{f-1}\pmod3.
\tag{E}
$$

这正是先作完整整数整除，再代入 $q=1+\pi$ 的准确系数，不是对单一选中单项式的近似。因 $3\in(\pi^6)$，$(A_\nu,B_\nu)$ 在 $0\le\nu<3$ 时准确给出 $\alpha_9\bmod\pi^3$。脚本通过整数稀疏乘法直接实现 (R)–(E)，并断言全部微分系数可整除 $9$。

### Step 3. 新的二阶 Laurent 证书

本步的等式均在 $\mathbb F_3[x^{\pm1},y^{\pm1}]$ 中。令

$$
L=(y-1)x^2-y(y-1)x+y=-xy(j-1),\qquad d_0=y-1.
$$

由 (R)–(E) 精确展开，两个二阶系数同时满足

$$
\begin{aligned}
A_2-(j+1)j_x&=x^{-5}y^{-7}L^3Q_x,\\
B_2-(j+1)j_y&=x^{-4}y^{-8}L^3Q_y,
\end{aligned}
\tag{E2}
$$

其中完整的短多项式商为

$$
\begin{aligned}
Q_x={}&-x^6d_0^5+x^3y^3(y+1)^3d_0^2-x^2y^3d_0-y^3(y^2+1),\\
Q_y={}&x^6d_0^4(y+1)-x^3y^3d_0(y+1)^4-x^2y^3+x y^5+y^3d_0(y+1).
\end{aligned}
\tag{Q2}
$$

这是两项完整 Laurent 恒等式，而不是在有限 $w$-jet 中声称整除。验证方式是将 (R)–(E) 的系数分别乘以 $x^5y^7,x^4y^8$ 后，与 $L^3Q_x,L^3Q_y$ 逐单项式比较；脚本同时断言零余式与上述完整商相等。两个商各有 $16,12$ 个展开项。由 $L=-xyz$，(E2) 的余项属于 $z^3\Omega$；由于 $u=j+1$ 在所选邻域为单位，这与 $H^3\Omega$ 相同。

零阶系数为

$$
A_0dx+B_0dy=H^4dj.
$$

一阶系数满足

$$
A_1dx+B_1dy=H^3\gamma.
\tag{E1}
$$

已接受首 jet 定理给出 (E1)；脚本也直接检查 $L^3$ 整除 $A_1,B_1$，两项多项式商各为 $25$ 项。在基底 $(dj,dy)$ 中写 $\gamma=a_1dj+b_1dy$。这里确有 $b_1(P)=2+a\ne0$，不是只知某个法向系数不为零。一个小的精确核对为：

$$
j_xB_1-j_yA_1=x^{-8}y^{-9}L^3R(x,y),\qquad
R(x,2)\equiv2\pmod{x^2+x+2}.
$$

该整除关系和余式也是 (R)–(E) 的逐系数检查。由于 $j_x(P)=a$、$u(P)=2$、$a^2+a=1$，有

$$
b_1(P)=\left.\frac{j_xB_1-j_yA_1}{j_xH^3}\right|_P=2a^2=2+a.
$$

由 (E1)–(E2)，提升其系数至 $S$ 后，完整形式可以写为

$$
\alpha_9=U\,dj+V\,dy,
$$

$$
\begin{aligned}
U&=H^4+\pi H^3a_1+\pi^2(u+H^3a_2)+\pi^3r,\\
V&=\pi H^3b_1+\pi^2H^3b_2+\pi^3s,
\end{aligned}
\tag{UV}
$$

其中 $a_1,a_2,b_1,b_2,r,s\in S$，$b_1$ 为单位。先取 Laurent 系数的整数提升，再作上述余切换基，即得到 (UV)：整数系数的模 $3$ 差属于 $(\pi^6)$。若另改一阶系数的局部提升，相应差先吸收到 $a_2,b_2$，再把剩余差放入 $\pi^3r,\pi^3s$。这一步保留任意完整尾项，尚未舍去它们。

### Step 4. 两生成元消元，严格消尽全部尾项

令 $B_1^*=b_1+\pi b_2$，它是单位。对原两生成元做可逆操作：

$$
G=V/B_1^*=\pi H^3+\pi^3b,\qquad
F=U-(a_1+\pi a_2)G=H^4+\pi^2u+\pi^3a,
$$

其中 $a,b\in S$。故 $C=(U,V)=(F,G)$，且有完整等式

$$
\pi F-HG=\pi^3(u+\pi a-Hb).
\tag{S}
$$

括号内在 $P$ 的残余值是 $2$，因此是单位。这给出 $\pi^3\in C$，不是由某个稳定有限长度推测 $\pi^3\in C$。于是完整原理想恰为

$$
C=(\pi^3,H^4+\pi^2u,\pi H^3).
\tag{C3}
$$

包含关系的两方向分别来自：$F,G$ 和 $\pi^3$ 生成右端的两个主项；反过来 $F,G$ 与主项只差右端已有的 $\pi^3$ 倍数。

### Step 5. 保持原 $z=j-1$ 的最终理想相等

在 (C3) 中只除以单位 $u$ 的幂，得到

$$
C=(\pi^3,z^4u^3+\pi^2,\pi z^3).
$$

在 $S/(\pi^3)$ 中特征为 $3$，故 $u^3=(z+2)^3=z^3+2$。因此

$$
C=(\pi^3,f_0,g_0),\qquad f_0=z^7+2z^4+\pi^2,\quad g_0=\pi z^3.
\tag{C4}
$$

所有此处使用的特征 $3$ 替换之差属于 $(3)\subset(\pi^3)$，所以 (C4) 仍是 $S$ 中的准确理想等式。

先在 $S/C$ 中计算。由 $g_0=0$ 得 $\pi^2z^3=0$，继而

$$
z^3 f_0=z^7(z^3+2)=0.
$$

$z^3+2$ 为单位，所以 $z^7=0$；再由 $f_0=0$ 和特征 $3$ 得 $\pi^2-z^4=0$。因此 $Q S\subset C$。

反过来，$Q S$ 包含

$$
\pi^3=\pi(\pi^2-z^4)+z(\pi z^3),\qquad
z^7=\pi(\pi z^3)-z^3(\pi^2-z^4).
$$

故还包含 $3$ 及 $f_0=(\pi^2-z^4)+z^7+3z^4$，也包含 $g_0$。这证明 $C\subset Q S$，从而 (C) 成立。整个证明未将原能级改为某个拟合坐标。

### Step 6. 允许提升改变后的精确不变性与积分闭包边界

记 $Q_z=(\pi^2-z^4,\pi z^3)S$。Step 5 的第一条恒等式对任意 $z$ 均给出 $\pi^3\in Q_z$，对 $z'$ 也成立。因此可以同时在 $S/(\pi^3)$ 中比较两个理想。该商特征为 $3$，且

$$
\pi z'^3=\pi z^3,\qquad z'^4=z^4+\pi z^3f.
$$

故其生成元只相差另一生成元的倍数，证明 (L)。由于 $z'=z+\pi f$，替换 $(z,w)$ 为 $(z',w)$ 的形式 Jacobian 行列式为单位；在完成局部环中存在逆替换，所以这确实是同一原残余能级的允许局部提升，不是退化基底。

须区分三种说法：

- 已证明的是指定原 $j$ 的精确理想下降，并进一步证明上述全部局部提升的相同正规形。
- 导子失败本来只能否定指定提升的精确下降；有限导子通过本身不证明精确下降，尤其不证明积分闭包下降。
- 由 (C) 自动有 $\overline C=\overline{QS}$。本包不把这个等式偷换成另一个未检查的基变定理 $\overline Q\,S=\overline{QS}$，也不新增积分闭包、Rees 赋值或正规化爆破分类。这里无须积分闭包才能保住精确下降结论。

### Step 7. 横截长度与真实原状态阶

$\pi^3\in Q$ 且 $3\in(\pi^3)$，所以 $B/Q$ 是特征 $3$ 的 Artin 局部环，写成

$$
B/Q\simeq k[[\pi,z]]/(\pi^2-z^4,\pi z^3).
$$

关系还给出 $z^7=0$。以 $\pi>z$ 的字典顺序，三个多项式 $\pi^2-z^4,\pi z^3,z^7$ 的首项为 $\pi^2,\pi z^3,z^7$；唯一新增的交叠 $z^3(\pi^2-z^4)-\pi(\pi z^3)=-z^7$ 已在集合中，其余交叠约化为零。因此剩余单项式恰为

$$
1,z,z^2,z^3,z^4,z^5,z^6,\pi,\pi z,\pi z^2,
$$

它们线性无关并张成，长度为 $10$。这是二维基底 $B$ 的横截长度；三维 $S$ 中 $S/C\simeq(B/Q)[[w]]$，不得称整个闭点局部商具有有限 Artin 长度 $10$。

对假设中的无分歧状态，$v_\pi(z)\ge1$，故

$$
v_\pi(\pi^2-z^4)=2,\qquad v_\pi(\pi z^3)\ge4.
$$

由完整两系数理想相等，$v_\pi(\alpha_9)=2$。又 $dI_{9,q}=9\alpha_9$，$v_\pi(9)=12$，所以 $v_\pi(dI_{9,q})=14$。这只用于所证邻域中的允许状态。至此限定 Claim 得证。∎

## Bounded CPU Diagnostic — 不参与完整下降证明的有限平台

GPU 使用为 $0$；只做秒级精确整数/有限域运算，无浮点、拟合、时间重选或样本扫描。最初估计为秒至分钟，实际完整最终运行的原迹展开耗时 $0.212940$ 秒，有限检验总计 $0.247511$ 秒，连同符号证书总计 $0.521452$ 秒。计时由脚本单调时钟记录，不包括解释器启动。

固定检验商为

$$
S/(\pi^n,z^8,w^3)\simeq k[\pi,z,w]/(\pi^n,z^8,w^3),\qquad 2\le n\le6.
$$

$D=\partial_w$ 固定 $\pi,j$，且 $D(w^3)=0$，故每个商都合法下推。状态由原方程

$$
(y-1)x^2-y(y-j)x+y=0,\qquad y=2+w,\quad j=1+z
$$

在 $x\equiv a$ 分支精确 Hensel 展开；没有独立指定另一个能级。有限域线性消元同时测试原两系数在基底 $(dj,dy)$ 中的导数余类。

| $n$ | 商环 $k$-维数 | $\dim_k(S/(C,\pi^n,z^8,w^3))$ | 导子必要条件 |
|---:|---:|---:|---|
| 2 | 48 | 21 | `PASS_BOUNDED_ONLY` |
| 3 | 72 | 30 | `PASS_BOUNDED_ONLY` |
| 4 | 96 | 30 | `PASS_BOUNDED_ONLY` |
| 5 | 120 | 30 | `PASS_BOUNDED_ONLY` |
| 6 | 144 | 30 | `PASS_BOUNDED_ONLY` |

$n=3$ 包含首个超出已知首 jet 的实际二阶系数；但没有出现严格失败余类。后续有限通过不构成完整下降证据，$w^3$ 盲区也不能通过反复相同计算消除。本包的出口是 (E2) 的完整 Laurent 恒等式及 (S) 的完整 syzygy，因而没有继续提高 $\pi$ 阶或切向截断。

运行命令：`python docs/research-batch07/qpi_odd_height_two_descent_diagnostic_v1_20260909.py`。脚本不写数据文件，依赖 Python 标准库及 SymPy 的精确多项式运算；重要断言为原矩阵迹/行列式、整数整除、完整零阶式、首切向非零值、两项完整二阶商证书。有限平台与这些精确证书在输出中明确分开。

## Corrections or Missing Assumptions

- 原诊断没有预设同纤维必须有差异；本例结果是完整局部下降与局部提升不变性，不能为保住方向而改选时间或另选能级。
- 全局原 $j$ 的末端正则性未被证明，也不是本包的假设或交付。本包不把原环面 Laurent 恒等式自动推到四末端。
- 并未证明所有奇素数、所有高度或所有 Hasse 根的分类；本例的简单根 $u(P)=2$ 与切向单位是关键。

## Open Risks / Blocking

- 作者新增的风险集中于 (R)–(E) 的原矩阵转录、(E2)–(Q2) 的精确证书及 (S) 的单位判定，必须交给非作者针对这些实际新输入检查。有限运行成功不替代该检查。
- 在本文限定命题内，没有需要继续加 jet 的数学尾项。完整 I01 研究所需的非短比较骨架、选择无关障碍与差异化原状态消费者均未出现；短正规形反而触发已约定的停止信号。
- 不申请新预算，不新造实验锁，不启动新论文目录、PDF 构建或正式评分；既有 C/D 与已接受论文源文件均不改动。

## Next — 唯一下一引理检查目标

交非作者独立核验 **Step 3 的二阶原 Laurent 证书引理 (E2)–(Q2)**，然后检查它确能通过 (UV)–(S) 推出完整等式 (C)。这是接受当前有界诊断的单一门槛，不是新增完整纤维延拓引理或开启另一轮无限 jet。若该检查通过，保存本短接口并停止当前完整 I01 投入；后续科学重排由主控综合 D01/D05 的实际结果处理。

## Input and ownership record

本轮作者仅新增本文与上述伴随脚本。已本人全文读取 [I01/D01 选择与停止规则](PAPER31_QPI_IDEA_REPORT_V1_20260909.md) 的初始本轮版本，并核对终态 D05 方位句更正；终态输入 SHA-256 为 `c559e9202916a7ed6bae8a07d57deccaf35a1136cf7108149a2fb825967a4e3f`。使用 proof-writer 技能将原必要条件问题收为限定 Claim、全部假设、依赖、证明、边界与单一检查目标；没有以技能流程代替数学证明。
