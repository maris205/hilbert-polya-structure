# 全奇素数分母平方自由性：独立核查

日期：2026-09-07。审查者：`p30_twist_leading_structure_probe`，未参与被审
分圆局部证明的构造。使用本轮完整读取的 `proof-writer` 技能，对归一化、
整性、有限特征运算和返回实际多项式逐项核查。

## Claim and status

已全文读取
[作者证明](PAPER30_TWIST_PRIME_SQUAREFREE_PROBE_V1_20260907.md)，其 SHA256 为
`37dac7ae617e0d834f974a4ee17bbca9c2e45e1cef442bb027ba59ffd459297b`。

**所述全奇素数分母定理：`PROVABLE AS STATED`；以下 12 项全部 PASS。**
没有发现需要修改作者科学结论的缺口。
通过结论是：每个奇素数 $p$、每个 $1\le r<p$ 的 $C_{r,p}$ 在特征零中
平方自由、次数为 $(p-1)/2$，因此全部复根互异。
不包含“全部根为实数”、合数分母或 $C,Q$ 无共同根。

本次独立证据不是素数列表试算：对作者关键有限域系数给出另一条
Frobenius／有限二项式证明，另逐项核算常数项和 resultant。

## Assumptions and source verification

设 $p$ 为奇素数，$m=(p-1)/2$，$\zeta=e^{2\pi ir/p}$、$\pi=\zeta-1$，
$\mathcal R=\mathbb Z[\zeta]_{(\pi)}$。
已亲读 Milne 作者官网 PDF 的命题 6.2 及其相关证明：整数环、
$p$ 的全分歧、$1-\zeta$ 为素元，以及剩余域为 $\mathbb F_p$ 的陈述均支持
本稿所需局部事实。本文的 $\pi$ 与该来源符号仅差单位 $-1$。
[Milne，*Algebraic Number Theory*，命题 6.2 及其证明](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=98)

因此 $\mathcal R/(\pi)=\mathbb F_p$，$p$ 与 $\pi^{p-1}$ 相伴，且
$1,\ldots,p-1$ 都是局部单位。没有在工作区增加文献 PDF，未使用其他外部定理。

## Itemized verdicts

| 项目 | 结论 | 核查重点 |
| --- | --- | --- |
| 1. 局部分圆环与单位事实 | PASS | 亲读官方一手讲义命题及相关证明；剩余域和分歧指数匹配 |
| 2. $d_n=D_n/\pi^2$ 的约化 | PASS | 精确因式分解给出 $\bar d_n=-n^2\ne0$；反射对称未丢失 |
| 3. 参数和整体尺度 | PASS | $R_p(d;A)=\pi^{2(p-1)}R_p(D;A/\pi^2)$，方向及幂次正确 |
| 4. 除 $p$ 前的局部整性 | PASS | 有限系数临界值属于 $\mathcal R[A]$；只用指数至 $p-1$ 阶 |
| 5. $R=-pG$、primitive 导数 | PASS | 在特征零先证 Euler／包络身份，再定义 $\mathcal S=-G$ |
| 6. 有限平方传播子分支 | PASS | 直接有理微分身份及 $\bmod t^p$ 的唯一三角分支 |
| 7. $\bar F_{p-2}=(-A)^{m-1}$ | PASS | 独立 Frobenius／二项式推导，不依赖作者的 $\delta$ 部分分式 |
| 8. 常数项严格为 $-1$ | PASS | 独立计算有限临界值；没有除以约化后的零多项式 |
| 9. 导数积分的次数界 | PASS | 次数 $\le m<p$ 排除隐藏的 $A^p$ 导数核 |
| 10. $p=3$ 边界与次数保持 | PASS | $m=1$，$\bar F_1=1$、$\bar{\mathcal S}=-A-1$、导数为单位 |
| 11. resultant 单位与特征零平方自由 | PASS | 保持次数，独立求得约化 resultant 为 $-m^m\ne0$ |
| 12. 返回 $C$、全部互素分子及范围 | PASS | 两次非零尺度变换不改重数；各本原 $\zeta$ 的局部计算相同 |

## Proof strategy and dependency map

审查最关键的顺序为：先在特征零中把 $R$ 识别为 $-pG$，并证明 $G$
局部整，再约化 $\mathcal S=-G$。其后才使用有限域的显式系数和导数。
若逆转这个顺序，约化后的 $R$ 及其导数均为零，无法获得平方自由证据。

1. 有限系数变分仅要求非零传播子和反射对称，不要求复数 $d_n$ 实正。
2. 所有指数／对数运算的阶都低于 $p$，故所用整数分母为单位。
3. 显式约化和次数保持使 resultant 的剩余值有效控制特征零 resultant。
4. 局部代数简单性不含任何关于复嵌入下根实性的结论。

## Independent proof checks

### 1. 传播子及缩放

直接分解

$$
\frac{D_n}{\pi^2}
=-\zeta^{-n}(1+\zeta+\cdots+\zeta^{n-1})^2
$$

给出约化 $-n^2$；对 $1\le n<p$ 它不为零，所以 $d_n$ 是局部单位。
$D_n=D_{p-n}$ 在同除 $\pi^2$ 后仍严格成立。

在共同尺度 $c$ 下，递推系数满足
$v_n(cD;a)=c^{-n}v_n(D;ca)$。因此终端满足
$R_p(cD;a)=c^{1-p}R_p(D;ca)$，取 $D=\pi^2d$ 后得到作者式 (5)。
这里参数是 $A/\pi^2$，而不是 $A\pi^2$；返回 $C$ 时才变成
$\mathcal S(-4\pi^2\lambda)$。

### 2. 合法除 $p$ 与不越界的指数

递推构造 $v_1,\ldots,v_{p-1}$ 时只除以 $d_n$ 及 $n<p$。
指数系数最高为 $E_{p-1}$，分母至多 $(p-1)!$。
在有限泛函

$$
\Phi_p=[t^p]\left(\tfrac12v\mathcal Dv-bte^v-\tfrac A2t^2e^{2v}\right)
$$

中，$[t^p]$ 本身没有引入一个 $p!$：动能是两个已知截断多项式的乘积，
两个指数势只提取 $p-1$、$p-2$ 阶。故临界值 $G_p$ 确在局部环多项式中。

权重 $(b,A)=(1,2)$ 的 Euler 身份与驻值包络在特征零给出

$$
R_p=-pG_p,
\qquad \mathcal S_p=R_p/p=-G_p\in\mathcal R[A],
\qquad \mathcal S_p'=\tfrac12F_{p-2}.
$$

这不是从 $\bar R_p=0$ 推断“可以除 $p$”。权重还给出
$\deg_A\mathcal S_p\le m$，后面约化的积分步骤有合法次数界。

### 3. 平方传播子分支的有限域身份

令 $B=(1+A)/4$、$P=1+t+Bt^2$。直接有理函数计算为

$$
(t\partial_t)^2\log P
=\frac{t+(1+A)t^2+Bt^3}{P^2}
=\frac tP+\frac{At^2}{P^2}.
$$

在 $\mathbb F_p[A][t]/(t^p)$ 中，有限对数及指数的所有分母都为单位，
所以 $\bar v=-\log P$、$\bar E=P^{-1}$、$\bar F=P^{-2}$ 合法。
各 $-n^2$ 在所需阶可逆，保证它就是约化递推的唯一分支。
未使用第 $p$ 阶指数或含 $1/p$ 的积分。

### 4. 不同于作者的 $\bar F_{p-2}$ 证明

在该截断环中，由 Frobenius
$P^p=1+t^p+B^pt^{2p}\equiv1$，故

$$
P^{-2}\equiv P^{p-2}\pmod{t^p}.
$$

在 $P^{p-2}$ 中取 $t^{p-2}$，若取 $k$ 个二次项，就必须同时取 $k$ 个
常数项，其余为一次项。于是

$$
\bar F_{p-2}
=\sum_{k=0}^{m-1}
\frac{(p-2)!}{k!^2(p-2-2k)!}B^k.
$$

各阶乘都小于 $p$。模 $p$ 后分子相应的连续 $2k$ 个因子变成
$2,3,\ldots,2k+1$，因此该系数等于 $(2k+1)!/(k!^2)$。
另一方面，$m-1=-3/2$ 在 $\mathbb F_p$ 中成立，逐因子计算给出

$$
\frac{(2k+1)!}{k!^2}=(-4)^k\binom{m-1}{k}.
$$

所以由有限二项式定理，

$$
\bar F_{p-2}=(1-4B)^{m-1}=(-A)^{m-1}.
$$

该证明在多项式环中进行，没有删去 $A=0$、$A=-1$ 或二次分解重根点。
$p=3$ 时和式仅有 $k=0$，结果为 $1$，无负次方或空分母。
另直接核对了作者的部分分式式和 Frobenius 符号，二者也正确。

### 5. 常数项、导数核与 primitive 约化

由 $\mathcal S_p'=F_{p-2}/2$，约化导数等于
$\tfrac12(-A)^{m-1}=\frac d{dA}(-A)^m$，因为 $-m=1/2$。
次数均小于 $p$，故只差常数，不能产生额外 $A^p$ 项。

在 $A=0$ 时，$P=(1+t/2)^2$，独立展开得到

$$
\bar v_n=\frac{(-1)^n}{n2^{n-1}},
\qquad\bar E_{p-1}=0.
$$

对每个 $1\le n<p$，利用 $p-n=-n$ 及 $p$ 奇数可得

$$
(-n^2)\bar v_n\bar v_{p-n}=-2^{2-p}.
$$

所以

$$
\bar G_p(1,0)=\tfrac12(p-1)(-2^{2-p})=2^{1-p}=1,
\qquad\overline{\mathcal S_p}(0)=-1.
$$

这里的除法只用 $2$、$n$ 和 $p-n$ 的剩余域单位。
故独立确认

$$\boxed{\overline{\mathcal S_p}(A)=(-A)^m-1.}$$

最高次系数为单位，因而 $\mathcal S_p$ 的次数恰为 $m$，且其系数最小
$\pi$ 赋值为零。于是 $R_p(d;A)=p\mathcal S_p(A)$ 的系数最小赋值
恰为 $p-1$，作者关于整体因子精确性的结论正确。

### 6. 边界和 resultant 转移

当 $p=3,m=1$，约化多项式为 $-A-1$、导数为 $-1$，直接平方自由。
一般 $1\le m<p$ 时，$f=(-1)^mA^m-1$ 的导数为
$g=m(-1)^mA^{m-1}$；$A=0$ 不是 $f$ 的根。
还可不求根直接用 resultant 的乘法性算出

$$
\operatorname{Res}(f,g)
=[m(-1)^m]^m\operatorname{Res}(f,A)^{m-1}
=-m^m\ne0.
$$

$\mathcal S_p$ 与其导数的次数都保持，Sylvester 矩阵因此可逐系数约化，
其行列式的剩余值就是上式。特征零 resultant 是局部单位，故非零。
这严格排除 $\mathcal S_p$ 在特征零代数闭包中的重根。

最后

$$
C_{r,p}(\lambda)=2(-1/2)^p p\pi^{-2(p-1)}
\mathcal S_p(-4\pi^2\lambda).
$$

常数和参数乘法均非零，不改变根重数。每个 $1\le r<p$ 都给出本原
$\zeta$，其 $d_n$ 的剩余值同为 $-n^2$；没有遗漏非首分子或另一个复嵌入。
所以所有奇素数分母、全部互素分子的结论成立。

## Minimal exact symbolic check actually run

只运行以下抽象有理恒等式检查，未运行任何素数列表或根数扫描。
全素数结论来自上述一般证明，不来自此有限计算。

```python
import sympy as S
t,A,k = S.symbols("t A k")
B = (1+A)/4
P = 1+t+B*t*t
Nlog = t*S.diff(P,t)/P
assert S.factor(t*S.diff(Nlog,t)-t/P-A*t*t/P**2) == 0
ratio_factorials = (2*k+3)*(2*k+2)/(k+1)**2
ratio_binomial = -4*(-S.Rational(3,2)-k)/(k+1)
assert S.factor(ratio_factorials-ratio_binomial) == 0
print("EXACT_PASS: rational identity and abstract coefficient ratio")
```

## Corrections or missing assumptions

没有发现本次作者输入中需要修改的定理、尺度、符号或边界。
特征零合法除 $p$、指数止于 $p-1$、次数低于 $p$、$p=3$ 和全部 $r$
均已明确处理。局部分圆标准输入已作独立一手核对。

## Open risks

本审查证明的是一个真实无限分母族的平方自由性，不是全部分母结论。
奇素数分母的全部根是否实、合数分母的重数及 $C,Q$ 的公共根仍是独立义务。
不把分圆局部简单根误称实数简单根，不作篇幅、正式候选票、PDF 或批次验收。
