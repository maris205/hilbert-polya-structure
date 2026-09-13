# Paper30 全奇特征 AS 论证：新鲜独立数学核查

日期：2026-09-07。性质：有界、独立、纯数学核查；不进行数值实验、有限次数枚举、查新、论文写作或正式候选四门评分。

## Claim

本报告核查新作者证明的以下原量词结论，并独立检查其所需的移位勘误：

1. 对任意代数闭域 $K$、任意奇素数 $p=\operatorname{char}K>2$、任意 $c\in K$ 及 $\lambda\in\mathbb F_p^*$，全部有限多项式支撑上的 Frobenius 固定元满足
   $$
   \ker(\phi-1:\overline C_\lambda\to\overline C_\lambda)
   \subseteq K\langle x\rangle.
   $$
2. 当 $p\ge5$ 时，上述固定空间为零，因而既有 Artin–Schreier 桥接给出全部 mixed 支撑上的 $Q^{\sigma=\lambda}=0$。

3. 后续明确追加的完整分类输入：$p=3$ 时，唯一非零特征空间发生在 $c\ne0,\lambda=-1$，恰为 $\mathbb F_3$-直线 $\operatorname{span}_{\mathbb F_3}\{[q^3xy]\}$，其中 $q^2=-1/c$。连通循环次数 $p$ 的有限 étale 覆盖容许 $F_c$ 提升，当且仅当 $p=3,c\ne0$；对每个这样的 $c$，忘掉 deck 生成元后恰有一个固定底空间上的同构类，且没有与 deck 生成元交换的提升。

第 3 项是在额外冻结输入到达后单独检查的，不将它擅自归入第 2 项原文件的主张。

### 冻结输入及实际哈希

本审查员未参与作者构造，未读取并行作者交流；已完整读取以下三个新输入，旧依赖只用于核对实际调用的命题与错误位置。

| 输入 | 实际行数 | SHA256 |
| --- | ---: | --- |
| `PAPER30_AS_ODD_PRIME_EXCEPTION_PROBE_20260907.md` | 341 | `88791cf62e92f9cee913eb51e447269c8ef9b747431fd3a3523c7fc8374ca3cb` |
| `PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md` | 123 | `67b1073152a09ad00565a5721d0c7374480f28bc1d89fc79fbbab8ff9ad3c61e` |
| `PAPER30_AS_FULL_ODD_CLASSIFICATION_20260907.md` | 205 | `bc98b7e02553909ccdecc0f77be4325e3e2a357f260d6535f6311d5d65cfde89` |
| `PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md`（旧依赖） | 336 | `05aba58b468f3c4a5a9201f032200adb96e5acc6216ca65920066d2b2b3fe4d6` |
| `PAPER30_AS_FROBENIUS_COINVARIANT_INDEPENDENT_CHECK_20260907.md`（旧审查记录） | 未作为验收条件 | `5fc8746299f3c3868ecffa5bdacb6d105fec7adad86ffcd40124f0544804ef15` |

任务转述称勘误为 124 行；实际文件为 123 行且以换行符结尾。本报告绑定上述实际内容哈希，不将这一行数转述差异视为数学缺陷。

## Status

**本次实际检查的单字压缩、全奇特征分类、相邻移位修复及循环次数 $p$ 覆盖推论：`PROVABLE AS STATED / PASS — INDEPENDENT MATHEMATICAL CHECK`。**

未发现反例、未闭合的消去情形、额外科学假设或需要缩小的量词。下文给出逐义务的独立推导，裁决不来自作者的自评或旧审查的通过状态。

**旧任意步移位公式及依赖该公式的旧碰撞推理：`REFUTED`。** 新报告通过修复后的命题，不恢复错误公式的正确性，也不覆盖或改写旧审查漏检记录。

这是证明层面的裁决，不是正式候选 `PASS`、Route 评价、容量判断或论文验收；`route_applicability: NOT_APPLICABLE`。

## Assumptions and Notation

固定
$$
A=K[x,y],\qquad F=(x^2+c-y,x),\qquad \sigma=F^*,
\qquad L=\sigma-\lambda,
$$
$$
\overline C_\lambda=A/(LA+K),\qquad
\phi\langle h\rangle=\langle h^p\rangle,\qquad
Q=A/\{u^p-u:u\in A\}.
$$
既有未改的轨道基与桥接作为明确依赖使用，不作与本次变更无关的泛审。具体调用内容为：二进制 word 给出首一普通次数三角基；每个非空移位轨道贡献 coinvariant 的一个 $K$-基方向；其系数为有限 twisted 和 $\sum_r\lambda^r c_r$；以及
$$
Q^{\sigma=\lambda}\simeq_{\mathbb F_p}\ker(\phi-1).
$$
新证明没有更换这些依赖的假设或应用对象。

令 $X_0=x,X_{-1}=y$，$X_i^2=X_{i-1}+X_{i+1}-c$，$\sigma X_i=X_{i+1}$。二进制 word $M(a,b)$ 的唯一最高普通齐次项为 $x^ay^b$，系数为 $1$。记
$$
\mu(a,b)=a+b,\qquad V(a,b)=a+2b,\qquad U(a,b)=2a+b.
$$
$d(O)$ 是轨道的最小普通次数；$D=\delta(v)$ 是非零有限轨道支撑的最大 $d(O)$。

$\phi$ 是加法的 $p$-半线性映射；$\ker(\phi-1)$ 一般仅为 $\mathbb F_p$-线性空间。包含于 $K\langle x\rangle$ 不声称它自身是一条 $K$-线。

## Proof Strategy and Dependency Map

1. 正确的一步移位与严格离散凸性，替代错误的任意步公式，恢复 strong-balanced 顶层不消去。
2. 递推上的双权重控制，经普通次数三角反演传递到 normal form。
3. 奇反射例外的目标轨道只有两个允许普通次数的代表；其中低次代表违反 $U$ 上界，并且整条轨道位于所有低层来源之上。
4. 第 1、3 项把任意固定元压到唯一的单字轨道。
5. $p\ge5$ 时，在 $x^p$ 的 $V=p$ 边界选择二项式系数非零、且沿整条轨道唯一最低权重的 word，排除单字固定元。
6. 使用未变的全 mixed 桥接得到 Artin–Schreier 结论。
7. 独立计算特征 $3$ 的单字固定方程与桥接代表，完成全参数分类。
8. 核实标准 AS 扭子字典，并逐项证明连通性、无标记等价、提升判据、逆映射和 deck 作用。

## Proof

### 1. 勘误的错误定位与相邻修复 — `PASS / PROVED`

正确移位是
$$
T_+(a,b)=\left(2a+\eta,\frac{b-\eta}{2}\right),\quad\eta=b\bmod2,
$$
$$
T_-(a,b)=\left(\frac{a-\epsilon}{2},2b+\epsilon\right),\quad\epsilon=a\bmod2.
$$
对 $(0,1)$ 连续右移两次，结果为 $(2,0)$，而旧式以同一个余数同时充当移出量和移入量，给出 $(1,0)$。这个反例成立。若移出的低位依次为 $\eta_0,\ldots,\eta_{r-1}$，移入第一坐标的整数是 $\sum_j\eta_j2^{r-1-j}$，不是 $\sum_j\eta_j2^j$；勘误给出的位反转表达也正确。

本次修复没有调用这一任意步表达。单个字母的普通次数沿平移为 $\ldots,4,2,1,1,2,4,\ldots$，其相邻差分严格递增。非空 word 的次数是至少一个这种序列的有限和，因此差分仍在每一步严格增加，且次数在两端趋于无穷。全局最小值恰在一个位置或两个相邻位置达到。

一步差分为
$$
\mu(T_+(a,b))-\mu(a,b)=\frac{2a-b+\eta}{2},\qquad
\mu(T_-(a,b))-\mu(a,b)=\frac{2b-a+\epsilon}{2}.
$$
所以 strong-balanced 的 $(a,b)$ 及 $(pa,pb)$ 都是其轨道的最小普通次数代表。后者最小次数为 $pD$。全部低于 $pD$ 的 normal-form 项无法进入该轨道。

若另一顶层来源的最高 word 进入该目标轨道，它也有次数 $pD$，故两者都是最小代表。不同代表至多相邻。将相邻关系定向为右移，目标的第一坐标 $2pa+\eta$ 被 $p$ 整除，强制 $\eta=0$。此时 $pb$ 为偶数，由 $p$ 奇得 $b$ 偶；除以 $p$ 恰得来源的一步平移 $(a,b)\mapsto(2a,b/2)$。于是两个来源原本属于同一轨道，与每轨道仅选一个来源代表冲突。若两个最高目标完全相同，指数编码直接识别来源相同。

这排除了所有顶层碰撞；同源低项、其他顶层低项及较低层来源，均由目标轨道最小次数 $pD$ 排除。唯一留下的系数是来源系数的 $p$ 次幂乘某个非零 $\lambda$ 幂。因此 $\delta(\phi v)=pD>D$。修复覆盖原碰撞义务的全部来源，不需额外假设。

### 2. 双权重上界及三角反演 — `PASS / PROVED`

由初值和递推，在正射线上有
$$
\deg_VX_i\le2^i,\qquad\deg_UX_i\le2^{i+1}\quad(i\ge0),
$$
在负射线上有
$$
\deg_VX_i\le2^{-i},\qquad\deg_UX_i\le2^{-i-1}\quad(i\le-1).
$$
两方向的第一步分别是 $x^2-y+c$ 与 $y^2-x+c$；后续平方项的界加倍，而被减的相邻项和常数不超过该界。相乘表明 $M(a,b)$ 的每个普通单项式同时满足普通次数不超过 $a+b$、$V$ 不超过 $a+2b$、$U$ 不超过 $2a+b$。

三角反演减去 $M(\alpha,\beta)$ 时，其唯一最高普通项被消去，余项的普通次数严格下降，且两个权重界均保留。对每个余项递归进行同一操作，产生的新项不超过该余项自身的两种权重，故也不超过初始单项式的权重。对普通次数归纳，得到
$$
M(a,b)\text{ 在 }\operatorname{NF}(x^\alpha y^\beta)\text{ 中出现}
\Longrightarrow
\begin{cases}
a+b\le\alpha+\beta,\\
a+2b\le\alpha+2\beta,\\
2a+b\le2\alpha+\beta.
\end{cases}
$$
这是逐项上界，不要求加权最高项只有一个单项式，也没有把两个偏序当成同一个全序。

### 3. 全部 $n\ge1$ 奇反射例外及跨层排除 — `PASS / PROVED`

固定任意奇素数 $p=2m+1$，$m\ge1$，及任意整数 $n\ge1$。令
$$
D=3n+1,\quad\alpha=pn,\quad\beta=2\alpha+2m+1,\quad N=pD.
$$
若最高来源轨道唯一且为 $(n,2n+1)$，选它为上述方向的最小代表，可取
$$
h=tM(n,2n+1)+h_{<D},\qquad t\ne0,\qquad\deg h_{<D}\le D-1.
$$
Frobenius 加法性以及首一普通最高项给出
$$
\deg(h^p-t^px^\alpha y^\beta)\le p(D-1).
$$

考察 $W_0=(\alpha,\beta)$ 及 $W_1=T_+W_0=(2\alpha+1,\alpha+m)$。其次数为 $N,N-m$。重新代入两侧一步公式得到
$$
\mu(T_-W_0)-N=\frac{3\alpha+4m+2+(\alpha\bmod2)}2>0,
$$
$$
\mu(T_+W_1)-N=\frac{3\alpha-3m+2+((\alpha+m)\bmod2)}2>0.
$$
后一正性由 $\alpha=pn\ge2m+1$ 保证。结合严格离散凸性，$W_1$ 是整条轨道唯一普通次数最小代表；整条轨道次数不超过 $N$ 的位置恰为 $W_0,W_1$。

设 $q=N-m$。跨层截止为
$$
q-p(D-1)=p-m=m+1>0.
$$
因此上述全部低普通次数余项，包括较低轨道来源及最高来源自己的低项，都不能在这个目标轨道作出任何贡献。此处控制的是完整低层多项式，而非一个稀疏来源模板。

在 $\operatorname{NF}(x^\alpha y^\beta)$ 中，$W_0$ 的系数为 $1$。唯一剩余可能伙伴 $W_1$ 满足
$$
U(W_1)-U(W_0)=\alpha+1-m>0,
$$
被第 2 节的 $U$ 界排除。所有其他移位位置又被普通次数界排除。目标 twisted 系数因而等于非零的 $t^p$ 乘一个非零 $\lambda$ 幂，无同源或跨源消去。

最后
$$
\delta(\phi v)\ge q,
\qquad q-D=(p-1)D-m=m(2D-1)>0.
$$
此证同时覆盖全部奇素数与全部 $n\ge1$；没有按素数或次数有限枚举。

### 4. 全部 $p>2$ 的固定空间压缩 — `PASS / PROVED`

对非零固定元的最高支撑，第 1 节排除任一 strong-balanced 顶层来源。普通次数最小判据与非 strong-balanced 的整数条件只允许
$$
(a,b)=(n,2n+1)\quad\text{或}\quad(2n+1,n).
$$
这两个代表右移相接，属于同一轨道；给定 $D=a+b$ 后，$n=(D-1)/3$ 唯一，故最高支撑确实只有这一条例外轨道。这一唯一性正好满足第 3 节的前提，不暗中假定一般输入稀疏。

若 $n\ge1$，第 3 节与固定方程矛盾。故 $n=0$、$D=1$。含至少两个字母的 word 的每个代表普通次数均至少为 $2$；非空单字又只有一个移位轨道。因此
$$
\ker(\phi-1)\subseteq K\langle x\rangle
$$
对全部 $p>2$ 成立。该推理允许任意数量、任意跨度和任意次数的较低支撑，只使用每个多项式实际有限支撑。

### 5. $p\ge5$ 的单字边界系数与唯一最小权重 — `PASS / PROVED`

令 $p=2m+1\ge5$。第 2 节保证 $\operatorname{NF}(x^p)$ 中所有 word 的 $V$ 均不超过 $p$。递推中的实际最高 $V$ 部分为
$$
\operatorname{in}_V X_0=x,\qquad
\operatorname{in}_V X_i=(x^2-y)^{2^{i-1}}\ (i\ge1),\qquad
\operatorname{in}_V X_i=y^{2^{-i-1}}\ (i\le-1).
$$
正向从 $X_1$ 开始、负向从 $X_{-1}$ 开始，每次后续平方项严格高于被减相邻项及常数；显示出的最高多项式非零，其纯幂首项系数为 $1$。所以这些最高部分在特征 $p$ 中也不会整体消失。

$V=p$ 的所有指数对恰为 $(2j+1,m-j)$，$0\le j\le m$。二进制位相乘给出
$$
\operatorname{in}_VM(2j+1,m-j)=x(x^2-y)^jy^{m-j}.
$$
置 $z=x^2$，除去共同因子 $x$ 后，$(z-y)^jy^{m-j}$ 是次数 $m$ 齐次空间的一组基，因为 $(z,y)\mapsto(z-y,y)$ 可逆。代入 $z=x^2$ 在相应多项式空间中保持线性无关。于是恒等式
$$
x^p=x((x^2-y)+y)^m
=\sum_{j=0}^m\binom mjx(x^2-y)^jy^{m-j}
$$
精确识别 normal form 在边界 $V=p$ 的系数为 $\binom mj$。低于该权重的 word 不会改变这个比较。

取
$$
j=\lfloor m/2\rfloor,\qquad a=2j+1,\qquad b=m-j.
$$
由于 $0\le j\le m<p$，$\binom mj$ 在 $K$ 中非零，不依赖 $c$ 或 $\lambda$。

每个 word 的 $V$ 沿移位等于 $\sum_i e_i2^{|i+r|}$。函数 $2^{|r|}$ 的离散二阶差分在每个整数位置均严格为正，故非空 word 的这个有限和也严格离散凸。因 $a$ 为奇数，两侧一步差分是
$$
V(T_+(a,b))-V(a,b)=a-b,
\qquad
V(T_-(a,b))-V(a,b)=\frac{4b-a+3}{2}.
$$
若 $m=2k$，则 $k\ge1$、$(a,b)=(2k+1,k)$，两个差分都是 $k+1>0$。若 $m=2k+1$，则 $k\ge1$、$(a,b)=(2k+1,k+1)$，两个差分分别是 $k>0$ 和 $k+3>0$。因此这个代表是整条移位轨道唯一的最小 $V$ 代表，最小值恰为 $p$。

normal form 中全部其他移位伙伴的权重均大于 $p$，故无一能够出现。所选轨道的 twisted 系数只有 $\binom mj$ 乘一个非零 $\lambda$ 幂，不能消去。

$a\ge3$ 且奇，其二进制编码至少有两个正侧字母；$b\ge1$ 至少贡献一个负侧字母。平移不改变字母数，故所选轨道不是单字轨道。得到
$$
\phi\langle x\rangle\notin K\langle x\rangle.
$$
这证明的是整条目标轨道的 obstruction 非零，不只是一个 word 的系数非零。

### 6. 全 mixed 零结论及量词 — `PASS / PROVED`

固定 $p\ge5$。第 4 节将任意固定元写为 $v=t\langle x\rangle$。若 $t\ne0$，半线性给出
$$
\phi v=t^p\phi\langle x\rangle\notin K\langle x\rangle,
$$
与 $\phi v=v$ 矛盾。因此固定空间为零；既有全 mixed 桥接使 $Q^{\sigma=\lambda}=0$。

所有差分、不等式与边界系数均对任意素数 $p\ge5$ 同时成立。$c$ 只处于低权重项，未被设为零或限制取值；$\lambda$ 只需原有的 $\lambda\in\mathbb F_p^*$，其非零幂不改变不消去。未增加次数上界、支撑稀疏性、参数泛性或有限域定义条件。原主张的量词完整保留。$\square$

### 7. 特征 $3$ 的全参数固定空间与 AS 代表（C3–C5）— `PASS / PROVED`

此节与以下几何核查绑定新增的 205 行完整分类输入，不依赖其所列冗余 cubic-zero 作者文件；本审查没有读取或为该冗余文件赋予新状态。

记 $u=\langle x\rangle$、$E=\langle X_0X_1\rangle$。直接由 $x^3=X_0X_{-1}+X_0X_1-cX_0$，并使用 $\sigma(X_0X_{-1})=X_0X_1$，得到
$$
\phi(u)=(1+\lambda^{-1})E-cu.
$$
单字与双字的移位轨道不同，故 $E,u$ 线性无关。当 $\lambda=1$，$\phi(tu)$ 的 $E$ 分量为 $2t^3$，对 $t\ne0$ 不为零。当 $\lambda=-1$，固定方程恰为
$$
-ct^3=t.
$$
$c=0$ 时只有零解；$c\ne0$ 时取 $q^2=-1/c$，$q\ne0$，所有解恰为 $0,q,-q$。因特征为 $3$，这正是 $\mathbb F_3q$，不是整个 $K$-直线。

由 $cq^3=-q$，直接计算
$$
(\sigma+1)(q^3xy)
=q^3(x^3+cx)
=q^3x^3-qx
=\wp(qx).
$$
既有桥接把 $[q^3xy]$ 映到 $qu$。$u\ne0$ 且桥接单射，故该类非零。第 4 节已经控制任意 mixed 支撑，桥接满射因此表明这些类穷尽全部特征类，不只是构造出一个例子。换 $q$ 为 $-q$ 恰把类取负，保持同一 $\mathbb F_3$-直线。

结合第 6 节，得到完整分类
$$
Q^{\sigma=\lambda}=
\begin{cases}
\operatorname{span}_{\mathbb F_3}\{[q^3xy]\},
&p=3,\ c\ne0,\ \lambda=-1,\ q^2=-1/c,\\
0,&\text{其他情形}.
\end{cases}
$$
新增输入把 $\mathbb F_3[q^3xy]$ 明确解释为加法类的线性张成，不是多项式代数；其记号虽可更直观，但不存在实际定义歧义。

### 8. 全部连通循环覆盖、无标记等价与提升判据（C6–C7）— `PASS / PROVED`

标准输入的条件已核实：特征 $p$ 的 étale AS 正合列和仿射结构层一阶上同调消失给出 $H^1_{\mathrm{et}}(\operatorname{Spec}A,\mathbb Z/p)\simeq A/\wp(A)$；交换层的 $H^1$ 分类其扭子同构类。这里底空间仿射且特征正确。来源分别为 [Stacks Project §59.63](https://stacks.math.columbia.edu/tag/0A3J) 与 [§21.4，Lemma 21.4.3](https://stacks.math.columbia.edu/tag/03AG)。本次只为核实这项新增输入的标准依赖打开原始来源，未进行查新检索。

给定 $[g]$，对应
$$
B_g=A[z]/(z^p-z-g),\qquad\tau(x,y,z)=(x,y,z+1).
$$
首一性给出有限自由秩 $p$，导数 $-1$ 为单位给出 étale 性。反之，连通循环 Galois 次数 $p$ 覆盖在选定 deck 生成元后是一个常值 $\mathbb Z/p$-扭子，故该字典覆盖作者声明的全部几何对象。

连通性不另需假定。令 $k_0=K(x,y)$。AS 多项式的任意一个根 $\alpha$ 所生成的域已经含有所有根 $\alpha+a$，$a\in\mathbb F_p$；它是可分正规扩张，Galois 群是 $\mathbb F_p$ 的子群。因 $p$ 为素数，扩张次数只能是 $1$ 或 $p$。故多项式要么在 $k_0$ 中有根，要么不可约。若 $r\in k_0$ 满足 $r^p-r=g$，任一不可约分母因子处的负赋值 $-d<0$ 会使左端赋值为 $-pd$，与 $g\in A$ 矛盾。$A$ 为 UFD，因此 $r\in A$，于是 $[g]=0$。

所以 $[g]\ne0$ 时多项式在 $k_0$ 上不可约。首一除法把 $B_g$ 嵌入其域商，故 $B_g$ 是整环，特别连通。$[g]=0$ 时，平移 $z$ 后多项式分解为互素的 $p$ 个线性因子，$B_g\simeq A^p$，覆盖分裂而不连通。

忘掉 deck 生成元正好商去 $\operatorname{Aut}(\mathbb Z/p)=\mathbb F_p^*$ 对非零 AS 类的标量作用。必要性也可直接检验：两个连通覆盖在固定底空间上的同构共轭其完整 deck 群，故把一个生成元送到另一个生成元的非零幂。若相应纤维坐标是 $w$，则 $w(z+1)-w(z)=a$，某个 $a\in\mathbb F_p^*$，所以 $w-az$ 为 deck 不变量。任意不变量在唯一的次数小于 $p$ 的 $z$ 展开中，若最高非零次数为 $j\ge1$，平移差的最高项系数为 $j$ 乘原系数，因 $j<p$ 而非零；故不变量必在 $A$ 中。于是 $w=az+h$，且相应 AS 类仅差非零标量。反向，类差为 $[g'] = a[g]$ 时，相应 $az+h$ 直接给出覆盖同构。无标记等价因此确为非零 $\mathbb F_p$-直线，不额外商去底空间自同构。

同一论证用于提升：若 $f$ 诱导底空间自同构 $F_c$，则 $f\tau f^{-1}$ 仍是 deck 自同构，故等于唯一的 $\tau^\lambda$，$\lambda\in\mathbb F_p^*$。因此点映射的纤维坐标满足 $w(z+1)-w(z)=\lambda$，从而
$$
f(x,y,z)=(F_c(x,y),\lambda z+h(x,y)),\qquad h\in A.
$$
这个点映射约定给出 $f\tau=\tau^\lambda f$；没有把拉回的反序共轭误当作点映射共轭。

代入覆盖方程，利用 $\lambda^p=\lambda$，保持方程当且仅当
$$
g\circ F_c=\lambda g+h^p-h,
$$
即 $\sigma g-\lambda g=\wp(h)$。这恰好是 $[g]\in Q^{\sigma=\lambda}$。反向由这个方程构造的映射确为自同构，其点映射逆为
$$
(P,z)\longmapsto
\left(F_c^{-1}(P),\lambda^{-1}\bigl(z-h(F_c^{-1}(P))\bigr)\right).
$$
因为 $\lambda^{-1}\in\mathbb F_p$，代入 AS 差得到 $g(F_c^{-1}(P))$；该逆保持覆盖且与正向复合为恒等。

因此，容许提升的无标记覆盖精确对应被 $\sigma$ 保持的非零 $\mathbb F_p$-直线；每条这样的直线上 $\sigma$ 乘一个非零标量，即已分类的某个特征空间。第 7 节表明只有 $p=3,c\ne0$ 时存在，且这时恰一条线。与 deck 生成元交换等价于 $\lambda=1$；该特征空间在所有情形均为零。

### 9. 显式例外提升、逆与全部三种提升 — `PASS / PROVED`

取 $p=3,c\ne0,q^2=-1/c$。第 7 节的恒等式给出
$$
Y_q:\ z^3-z=q^3xy,\qquad
f(x,y,z)=(x^2+c-y,x,-z+qx).
$$
独立代入可得
$$
(-z+qx)^3-(-z+qx)
=-q^3xy+q^3x^3-qx
=q^3(x^2+c-y)x,
$$
所以正向映射保持曲面。其逆为
$$
(x',y',z')\longmapsto
\bigl(y',(y')^2+c-x',qy'-z'\bigr),
$$
两个复合的底坐标与末坐标逐项恢复原值。

对这个固定覆盖代表，非零类只有特征值 $-1$，所有提升因而有末坐标 $-z+h$。由 $\wp(h)=\wp(qx)$，$h-qx$ 属于 $\ker(\wp:A\to A)=\mathbb F_3$；后者也可由整环中的分解 $s^3-s=s(s-1)(s+1)$ 直接得到。因此恰有三个提升
$$
f_a(x,y,z)=(x^2+c-y,x,-z+qx+a),\qquad a\in\mathbb F_3.
$$
对每个 $a$，$f_a\tau=\tau^{-1}f_a$，而 $\tau^{-1}\ne\tau$，所以无一交换。换另一个 deck 生成元也不改变这个不交换结论。以上完成新增几何推论的全部实际义务。$\square$

## Corrections or Missing Assumptions

1. 旧任意步公式是实际错误，旧独立审查也实际漏检；本报告不是把该错误降格为排版问题。相邻最小代表修复已在新输入原假设下独立闭合。
2. 例外的次数公式 $q=pD-(p-1)/2$ 及“只有两个允许代表”只在 $n\ge1$ 使用，不能推广到 $n=0$。新证明明确另行处理单字，没有发生边界偷换。
3. 当 $p=3$ 时，$m=1$，第 5 节所选 word 的一侧权重差为零；该统一单字排除不适用。作者没有将其误用于 $p=3$。第 4 节对 $p=3$ 的压缩仍有效。
4. 未发现需要添加的科学假设或未证明的中间引理。使用既有桥接不等于重新给全部旧命题授予独立通过状态。
5. 覆盖输入明确限定循环 Galois 次数 $p$、固定底空间上同构及底映射 $F_c$ 本身；新核查没有把这些结论扩展到任意次数 $p$ 的非 Galois 覆盖或任意迭代。

## Open Risks and Boundaries

- 对上述三个新冻结输入的实际数学主张，未保留未闭合的证明义务；特征 $3$ 的全参数汇总及新增循环覆盖推论均已纳入本报告第 7–9 节。
- 不推出非代数闭基域、$\lambda\notin\mathbb F_p^*$、一般 Hénon 次数、特征 $2$、无限支撑完成空间、非循环覆盖、高次 $p$-幂覆盖、任意迭代的提升或其他构造的结论。
- 数学通过不替代新意审查、正式候选四门、用户范围决策、构建或 PDF 验收。

## 最终核验记录

- 按 `proof-writer` 核对精确主张、假设、依赖、边界与量词，并据实际证明给出裁决。
- 已重新推导两种一步差分、普通次数与权重的严格凸性、顶层相邻碰撞、跨层截止和全部平移伙伴排除。
- 已核对特征 $3$ 所有 $c$ 与两个 $\lambda$、非零桥接代表、循环覆盖字典、无标记等价、一般提升判据、显式逆及 deck 共轭方向。
- 未作数值或有限次数实验；未使用作者自评或旧 `PASS` 代替证明。
- 只新增本报告，未修改冻结输入、旧审查、状态索引或其他作者文件。
