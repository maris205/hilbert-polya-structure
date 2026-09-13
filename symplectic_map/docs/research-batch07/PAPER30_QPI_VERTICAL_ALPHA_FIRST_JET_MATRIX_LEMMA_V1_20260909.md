# qPI 垂直整除微分：首 jet 的普适二阶矩阵引理 V1

日期：2026-09-09。执行者：`/root/p30_qpi_post_integral_ideas_v1`。
类型：有界矩阵证明与机制诊断；不是尚未终态的 P03 作者件的正式非作者检查。
`route_applicability: NOT_APPLICABLE`。0 GPU；不修改既有作者件、脚本、P04 或 idea 报告。

## Claim

令 $p$ 为奇素数，$N=p^a$、$a\ge1$，$K$ 为任意交换 $\mathbb F_p$-代数。
对任意 $A,B\in M_2(K)$，置
$$S=\operatorname{tr}A,\qquad D=\det A,\qquad\Delta=S^2-4D,
\qquad[A,B]=AB-BA.$$
则有完整的矩阵恒等式
$$
\boxed{\quad
\sum_{j=1}^{N-1}jA^{N-1-j}BA^{j-1}
=\Delta^{(N-3)/2}[A,B].\quad} \tag{1}
$$
因此对任意中心 $K$-模 $\Omega$ 及 $C\in M_2(\Omega)$，
$$
\sum_{j=1}^{N-1}j\operatorname{tr}(CA^{N-1-j}BA^{j-1})
=\Delta^{(N-3)/2}\operatorname{tr}(C[A,B]). \tag{2}
$$
这里 $j$ 指其在 $K$ 中的像；不反演 $\Delta$、$D$、特征根或矩阵 $A$。

令 $\epsilon^2=0$、$q=1+\epsilon$，$A=A(z)\in M_2(K[z])$，并令
$B(z)=z\partial_zA(z)$。固定降序乘积后有
$$
A(q^{N-1}z)\cdots A(qz)
=A(z)^{N-1}+\epsilon\Delta(z)^{(N-3)/2}[A(z),B(z)]. \tag{3}
$$
若 $d$ 只作用于状态变量、固定 $q,z$ 及时间参数，则
$$
\begin{aligned}
Q_N(q,z)&=\operatorname{tr}\bigl(dA(z)A(q^{N-1}z)\cdots A(qz)\bigr),\\
[z^N]Q_N(q,z)&=F_N(A)+\epsilon\beta_N(A),\\
F_N(A)&=[z^N]\operatorname{tr}(dA\,A^{N-1}),\\
\beta_N(A)&=[z^N]\Delta^{(N-3)/2}\operatorname{tr}\bigl(dA[A,z\partial_zA]\bigr).
\end{aligned} \tag{4}
$$
特别是主控提出的 $a=1$ 首谱缩放项 $\beta_p$ 原样成立，符号为正。
式 (1)–(4) 对全部 $a\ge1$ 成立不是样本外推，而由下面的 Frobenius 多项式证明得出。

## Status

**PROVABLE AS STATED。**

本状态仅针对上述普适矩阵引理及 §5 明确归一化后的实际圆分接口。
它不声称已证明原曲面上的首阶项非消失、全局系数理想、超奇异能级局部规范形或 P03 全部主张。
若把 $\beta_N$ 称为同时变动 $t$ 后的完整首阶系数，则必须补入 §6 的时间变化项。

## Assumptions、输入身份与阅读范围

本人全文读取以下两份冻结输入，但本次只消费指定矩阵、相对微分约定和循环整除公式：

| 输入 | 实读范围 | SHA-256 |
|---|---|---|
| [整数候选 brief](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 全文 270 行、17,780 字节；实际接口为 §§2–3 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| [圆分整除微分诊断](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 全文 268 行、12,988 字节；实际接口为 §1、§4 Steps 2、4–5 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |

矩阵 $A(z)$ 没有独立的 $q$ 系数依赖，$q$ 通过谱变量缩放 $z\mapsto q^jz$ 进入。
原 qPI 矩阵具体为
$$
A(z)=A_0+zA_1+z^2\begin{pmatrix}1&0\\0&0\end{pmatrix},
$$
$$
A_0=\begin{pmatrix}
t+x-xy&-x\\
t+x-ty-2xy+xy^2&x(y-1)
\end{pmatrix},\qquad
A_1=\begin{pmatrix}
y-x+x/y-1-t/x&1\\
y-2x-1+xy+x/y-t/x&1
\end{pmatrix}.
$$
它满足
$$\operatorname{tr}A=t+Jz+z^2,\qquad\det A=z^3,
\qquad J=y-x+x/y-t/x. \tag{5}$$
状态微分固定 $t,q,z$，只作用于 $x,y$。
因此 $dS=z\,dJ$、$dD=0$。式 (1) 本身不需要这些 qPI 特有等式。

原乘积的次序固定为 $M_N(z)=A(q^{N-1}z)\cdots A(qz)A(z)$；
本件不改成升序乘积，也不在展开中交换两个矩阵因子。
实际圆分段仅取 $m=1$；未将结论直接移到含非平凡剩余阶 $m$ 的矩阵块。

## Notation 与 Proof Strategy

用 $\mathsf L_A(X)=AX$、$\mathsf R_A(X)=XA$ 表示 $M_2(K)$ 上的左右乘算子。
它们彼此交换，$\operatorname{ad}_A=\mathsf L_A-\mathsf R_A$。
$\Delta$ 是标量，故与这些算子交换。
包含单个 $\Omega$-值矩阵 $C$ 的迹是 $\Omega$ 中的双线性表达式；
没有两个一形式相乘，也没有交换奇次形式产生的额外符号。

使用 `proof-writer` 的主张—依赖—边界结构，责任链是：

1. 对有限几何级数的多项式恒等式求导，识别带权算子为 $\operatorname{ad}_A^{N-2}$。
2. 二阶 Cayley–Hamilton 恒等式给 $\operatorname{ad}_A^3=\Delta\operatorname{ad}_A$。
3. 按原降序乘积逐因子作首 jet 展开，确定非交换位置与正号。
4. 在特征零先证明并使用 $dI_N=N[z^N]Q_N$，再约化到实际圆分一阶厚化。
5. 区分固定矩阵系数的谱缩放项与时间参数提升带来的附加项。

## Proof

### Step 1. 带权和是伴随算子的幂

在 $\mathbb F_p[X,Y]$ 中，因 $N=p^a$，Frobenius 给
$$X^N-Y^N=(X-Y)^N.$$
另一方面，整系数几何级数恒等式为
$$X^N-Y^N=(X-Y)\sum_{j=0}^{N-1}X^{N-1-j}Y^j.$$
先在多项式整环 $\mathbb F_p[X,Y]$ 中约去 $X-Y$，得到
$$\sum_{j=0}^{N-1}X^{N-1-j}Y^j=(X-Y)^{N-1}. \tag{6}$$
这是通用多项式恒等式，随后特化到含零因子的任意 $K$ 时不再作约分。

对 (6) 关于 $Y$ 作形式求导。由于 $N=0$、$N-1=-1$ 在特征 $p$ 中，得到
$$
\sum_{j=1}^{N-1}jX^{N-1-j}Y^{j-1}
=-(N-1)(X-Y)^{N-2}=(X-Y)^{N-2}. \tag{7}
$$
将两个交换算子 $\mathsf L_A,\mathsf R_A$ 代入 (7)，并作用于 $B$，即得
$$\sum_{j=1}^{N-1}jA^{N-1-j}BA^{j-1}
=\operatorname{ad}_A^{N-2}(B). \tag{8}$$
这里的正号来自 $-(N-1)=1$；不是依靠交换迹中的 $A$ 与 $B$ 得到。

### Step 2. 二阶矩阵的伴随三次关系

二阶 Cayley–Hamilton 在任意交换系数环上给
$$A^2-SA+DI_2=0,\qquad A^3=(S^2-D)A-SDI_2.$$
直接展开三次伴随并代入上述两式：
$$
\begin{aligned}
\operatorname{ad}_A^3(B)
&=A^3B-3A^2BA+3ABA^2-BA^3\\
&=(S^2-D)[A,B]-3D[A,B]\\
&=(S^2-4D)[A,B]=\Delta\operatorname{ad}_A(B).
\end{aligned} \tag{9}
$$
第二行的中间两项来自
$A^2BA=SABA-DBA$ 与 $ABA^2=SABA-DAB$，所以其合计是 $-3D[A,B]$。
这个三次关系甚至是整系数恒等式，不需要除以 $2$ 或假设矩阵可对角化。

由于 $p$ 为奇数，$N-2=2k+1$，其中 $k=(N-3)/2\ge0$。
按 (9) 归纳得到
$$\operatorname{ad}_A^{2k+1}=\Delta^k\operatorname{ad}_A.$$
代入 (8) 证明 (1)，再左乘 $C$ 取迹证明 (2)。

$N=3$ 时 $k=0$，约定 $\Delta^0=1$，无论 $\Delta$ 是否为零。
特别地，特征三中的左端是 $AB+2BA=AB-BA$，直接核准了符号。
当 $A$ 为标量矩阵、奇异矩阵，或者 $\Delta$ 为零因子乃至零时，同一证明仍有效。

### Step 3. 原降序乘积的首 jet

因 $\epsilon^2=0$，每个整数 $j$ 都满足
$$q^j=1+j\epsilon,\qquad A(q^jz)=A(z)+j\epsilon\,z\partial_zA(z).$$
在降序乘积 $A(q^{N-1}z)\cdots A(qz)$ 中，选出索引 $j$ 的线性项后，
其左边有 $N-1-j$ 个零阶 $A$ 因子，右边有 $j-1$ 个。
故线性项准确为
$$\epsilon\sum_{j=1}^{N-1}jA^{N-1-j}BA^{j-1}.$$
应用 (1) 得 (3)；左乘固定的 $dA(z)$、取迹及 $z^N$ 系数，得到 (4)。

整个展开没有 $d(q^j)$，因为这是相对状态微分。
也没有对置于最左的 $dA(z)$ 作谱缩放：它正是已归一化循环插入表达式的指定因子。
若改成升序乘积，权重经 $j\mapsto N-j$ 变为 $-j$，线性项符号会相反。
本件的正号绑定原降序次序与 $\epsilon=q-1$ 的选择。

### Step 4. 原矩阵的零阶项

为说明首 jet 的参照项，保留旧输入中的秩二递推：
$$U_{-1}=0,\quad U_0=1,\qquad U_n=SU_{n-1}-DU_{n-2}.$$
由 Cayley–Hamilton 和 $dD=S\,dS-\operatorname{tr}(A\,dA)$，有
$$\operatorname{tr}(dA\,A^{N-1})=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD.$$
在对称变量 $u,v$ 上，$U_{N-1}(u+v,uv)$ 就是 (6) 的左端，故
$$U_{N-1}(S,D)=\Delta^{(N-1)/2}$$
作为 $\mathbb F_p[S,D]$ 中的恒等式成立。
这可由 $S\mapsto u+v,D\mapsto uv$ 的对称多项式嵌入检验，不要求实际矩阵可分裂。
对 (5) 的原 qPI 矩阵，得到
$$F_N(A)=[z^{N-1}]\Delta(z)^{(N-1)/2}\,dJ. \tag{10}$$
这是既有零阶 Hasse 系数表达式的矩阵形式，不是新的 Hasse 几何识别。
本件不重新证明或评价其原 Jacobian、闭能级及全开放空间接口。

### Step 5. 实际圆分环：先除以 $N$，再作首阶约化

这一段与形式变量 $\epsilon$ 的证明分开。
取 $N=p^a$、$q=\zeta_N$，在 $p$ 上的圆分 DVR $\mathcal O$ 中取
$$\pi=q-1.$$
圆分参数满足 $p=u\pi^{\varphi(N)}$、$u\in\mathcal O^*$。
此处可直接核准：$\Phi_{p^a}(1+X)$ 的常数项为 $p$，而模 $p$ 为
$X^{\varphi(N)}$，所以它是 Eisenstein 多项式；在其参数 $\pi$ 上给出该赋值。
因 $p$ 奇且 $a\ge1$，$\varphi(N)=p^{a-1}(p-1)\ge2$，故
$$p=0\quad\text{于 }\mathcal O/(\pi^2),\qquad q=1+\pi.$$
因此一阶厚化是特征 $p$ 的交换环，即使 $p=3,a=1$ 也有效。

但不能在该环中直接写“除以 $N$”。所需整表达式来自特征零中的循环插入。
对 $M_N(z)=A(q^{N-1}z)\cdots A(z)$ 求相对状态微分，
在第 $k$ 个位置插入 $dA(q^kz)$，再循环移动迹使它居首。
以 $w=q^kz$ 为变量且用 $q^N=1$，该项准确成为 $Q_N(q,q^kz)$。
其 $z^N$ 系数等于 $Q_N(q,z)$ 的 $z^N$ 系数，因为 $q^{kN}=1$。
共有 $N$ 个插入位置，因此在整系数状态一形式中已有
$$dI_N=N[z^N]Q_N(q,z). \tag{11}$$
这就是已接受输入的循环整除公式在 $m=1$ 的情形；只需 $I_N$ 是原迹的 $z^N$ 系数。
在特征零定义并识别
$$\alpha_N:=N^{-1}dI_N=[z^N]Q_N(q,z)$$
后，右端是整数表达式，才可以约化到 $\mathcal O/(\pi^2)$。

在该特征 $p$ 商环中应用 Steps 1–3，得到实际同余式
$$
\boxed{\quad
\alpha_N\equiv F_N(A)+\pi\,[z^N]\Delta^{(N-3)/2}
\operatorname{tr}\bigl(dA[A,z\partial_zA]\bigr)
\pmod{\pi^2}.\quad} \tag{12}
$$
$F_N(A)$ 先取整系数的迹表达式；在模 $\pi^2$ 中可再用 (10) 替代它，
因为两种多项式表达式之差被 $p$ 整除，而 $p\in(\pi^2)$。
乘 $\pi$ 的系数只依赖 $A$ 的剩余值。

对 $a=1$，这是原 $p^{-1}dI_p$ 的首阶公式。
对 $a>1$，这是不同的归一化 $N^{-1}dI_N=p^{-a}dI_{p^a}$ 的公式，
有效性由 (11) 单独承担；不从 $a=1$ 的 $1/p$ 表达式作替换猜测。
只在整数环中保留 $p^{-1}dI_{p^a}$ 会多出因子 $p^{a-1}$，不是同一个对象。

### Step 6. 时间提升不能从首 jet 中省略

式 (12) 的 $F_N(A)$ 使用实际时间参数 $t$；它不是任意选定的 $\bar\alpha_N$ 提升。
所以 $\beta_N$ 精确指固定矩阵系数时 $q$ 的谱缩放项。

例如在特征 $p$ 的一阶厚化中，若同时令
$$t=t_0+\epsilon t_1,$$
其中 $t_0,t_1$ 对状态微分为常数，记 $A_*=A(t_0)$，则完整一阶式是
$$
\alpha_N=F_N(A_*)+\epsilon\left(
\beta_N(A_*)+t_1\left.\partial_tF_N(A(t))\right|_{t=t_0}\right).
\tag{13}
$$
其中 $\partial_t$ 也作用于 $J(t)$ 及 $dJ(t)$；不能只微分系数而冻结一形式。
这是系数环中的 Taylor 恒等式，不预判两种时间提升下原局部理想是否相同。
若还变动状态坐标或能级提升，需要另行记录相应变化；本件不承担它们。

以上证明完成了准确主张及所列接口。∎

## 实际有限恒等式检查

另以只读内存 `python -B` 作以下符号核验，正常结束（session 99819，exit 0）：

| 对象 | 核验结果 |
|---|---|
| 通用 $A=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$、通用 $B$ 的 $\operatorname{ad}_A^3(B)-\Delta[A,B]$ | 在整数多项式环中逐项为零 |
| 通用 $A,B$ 的式 (1)，$(p,N)=(3,3),(5,5),(3,9)$ | 分别模 $3,5,3$ 全部为零 |
| 另选非交换矩阵多项式，按降序双数乘法直接展开上述三组 $N$ | 全部线性矩阵系数与式 (3) 一致 |
| 对另选的矩阵多项式 $C(z)$ 取迹及 $z^N$ 系数 | 与式 (4) 一致 |
| 原输入 qPI 矩阵的迹与行列式 | 精确得到 $t+Jz+z^2$ 与 $z^3$ |

这些样本只检查符号、次序和抄写，不承担全部 $p^a$ 的证明。
没有展开原 $I_N$ 的高阶积分、没有采样原几何非消失，也没有写新脚本或生成数据文件。

## 机制诊断与来源边界

式 (1) 的机制完全由“有限几何级数求导 + Frobenius + 二阶 Cayley–Hamilton”构成。
更强的矩阵恒等式先于任何 qPI 专有矩阵、谱曲线或 Hasse 解释成立；
其本身不是一种依赖 qPI 几何的新一般方法，也不应独立包装成新的结构理论。

实际 $\alpha_N$ 的归一化入口是旧接受链的循环插入式 (11)，本件没有把它重新计为新整除机制。
本件的有界增量是确认指定非交换首项的准确闭式、正号、全部 $p^a$ 的量词及实际一阶接口。
它是否在原超奇异能级上给出非形式的新几何信息，要由实际系数和局部两方向结构另行判断。

这里未开展新的外部文献检索；不声称已定位“式 (1) 原样发表”的具体先例，
也不声称其全球首创。上述机制扣除来自正文给出的普适直接推导，不是根据题名猜测来源包含。
已有垂直微分先例筛查及主控正在进行的切向 Hasse 识别仍由各自实际输入负责。

## Corrections or Missing Assumptions

1. 原猜测的乘法次序与正号无需纠正；交换子必须定义为 $[A,B]=AB-BA$。
2. $N=p^a$ 的同式已经在本文证明，不再只是未经证明的外推；实际圆分对象必须使用
   §5 单独接入的 $p^{-a}dI_{p^a}$。
3. “首 $\pi$ 项”须声明参照项及固定参数。若 $t$ 也随 $\pi$ 变化，应使用 (13)，不能只取 $\beta_N$。
4. $p=2$ 不在本引理范围，半整数指数不能照搬；一般非 $p$ 幂的 $N$ 也没有由本文证明。
5. 对 $q$ 有独立系数依赖的其他矩阵族，其系数变化会另加项；不能只用谱变量缩放式。

## Open Risks 与任务边界

- 未核查或代签尚未终态的 P03 作者报告。
- 未证明原几何上的 $\beta_N$ 非零、完整两方向理想、超奇异能级首非零阶或跨末端线延拓。
- 未证明一般剩余阶 $m>1$ 的实际首 jet；长度 $m$ 的块内变化须另行处理。
- 未评估候选新意、独立长文价值、正式分数或自然正文容量；没有创建候选、稿件、锁或 PDF。
- 仅新增本报告；旧 P04 数学接受及旧 idea 报告保持冻结。
