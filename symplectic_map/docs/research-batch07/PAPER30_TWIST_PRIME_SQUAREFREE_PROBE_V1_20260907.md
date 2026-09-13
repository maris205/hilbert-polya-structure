# 奇素数分母的平方自由性：分圆局部归一化证明 V1

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
已在本轮完整读取 `proof-writer` 技能。
本稿只处理首项 $C$ 的奇素数分母平方自由性，不计算 $Q$、不增加根扫描。

## Claim

**定理。** 对每个奇素数 $p$ 和每个 $1\le r<p$，原双谐波辛映射

$$
p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,
\qquad q'=q+p'
$$

在既有 SUM action／零均值规范下的首项共振多项式
$C_{r,p}(\lambda)$ 在特征零中平方自由。
其次数为 $(p-1)/2$，所以全部复根互异；特别地，所有实根均为单根。

这**不证明**这些复根全部为实数，也不处理一般合数分母。

下面证明更精确的局部归一化式。取
$\zeta=e^{2\pi ir/p}$、$\pi=\zeta-1$，设 $m=(p-1)/2$。
若 $R_p(D;a)$ 是正树规范的首项多项式，则

$$
\mathcal S_p(A)
=\frac{\pi^{2(p-1)}}pR_p\left(D;\frac A{\pi^2}\right)
\in\mathcal O_{(\pi)}[A],
\qquad
\boxed{\overline{\mathcal S_p}(A)=(-A)^m-1\in\mathbb F_p[A].}
\tag{1}
$$

上横线表示在分圆局部环中模 $\pi$ 约化。

## Status

上述奇素数分母平方自由性及归一化闭式：`PROVABLE AS STATED`。

原全部分母的根实性／简单性及 $C,Q$ 共同根排除：`NOT CURRENTLY JUSTIFIED`。
本定理只关闭其中一个真实无限分母族的重根义务，不替换其他义务。
本稿为作者证明，非作者核查需另存；没有正式候选票或论文验收结论。

## Assumptions and Notation

令 $K=\mathbb Q(\zeta)$，$\mathcal O=\mathbb Z[\zeta]$，
$\mathcal O_{(\pi)}$ 表示在 $(\pi)$ 的局部化，以下简记为 $\mathcal R$。
标准分圆整数结论给出 $(\pi)$ 为素理想、
$\mathcal R/(\pi)=\mathbb F_p$，并且 $p$ 与 $\pi^{p-1}$ 相伴。
本轮在作者官网核对了这些局部事实；本文的 $\zeta-1$ 与该来源的 $1-\zeta$
只差一个单位。[Milne，*Algebraic Number Theory*，命题 6.2](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=98)

实际传播子及其单位归一化为

$$
D_n=2-\zeta^n-\zeta^{-n},\qquad
d_n=\frac{D_n}{\pi^2},\qquad1\le n<p.
$$

采用已核正的正树变量 $a=-4\lambda$：

$$
v_n=\frac{E_{n-1}+aF_{n-2}}{D_n},\quad
E=e^v,\quad F=e^{2v},\quad
R_p(D;a)=E_{p-1}+aF_{p-2},
\tag{2}
$$

其中只需 $v_1,\ldots,v_{p-1}$，负下标系数为零。
实际作用量首项是

$$
C_{r,p}(\lambda)=2(-1/2)^pR_p(D;-4\lambda).
\tag{3}
$$

在使用 $d$ 作为传播子时，参数写为 $A$，以避免尺度混用。
所有模 $p$ 的指数、对数均只取到 $t^{p-1}$；不存在除以 $p!$ 的步骤。

## Proof Strategy and Dependency Map

1. 用 $D_n/\pi^2$ 得到局部单位传播子，其剩余值为 $-n^2$。
2. 在特征零有限系数变分中证明 $R_p(d;A)=-pG_p(A)$，
   从而在约化之前合法除去整体因子 $p$。
3. 在 $\mathbb F_p$ 的有限截断中求得平方传播子分支及
   $F_{p-2}=(-A)^{m-1}$。
4. 对 primitive 候选的导数积分，并独立计算常数项，得到 $(1)$。
5. 约化多项式与其导数互素且次数保持，故特征零 resultant 非零。

其中第 2 步不可跳过：未经除 $p$ 的第一层约化是零多项式，
直接对它检查导数或判别式不会提供平方自由证据。

## Proof

### Step 1. 单位传播子与参数缩放

直接分解得

$$
d_n=-\zeta^{-n}\left(\frac{\zeta^n-1}{\zeta-1}\right)^2
=-\zeta^{-n}(1+\zeta+\cdots+\zeta^{n-1})^2.
$$

所以 $d_n\in\mathcal R^\times$，并且

$$
\overline{d_n}=-n^2\ne0\quad(1\le n<p).
\tag{4}
$$

反射对称性 $d_n=d_{p-n}$ 仍在特征零中严格成立。
全部整数 $1,\ldots,p-1$ 及 $2$ 在 $\mathcal R$ 中是单位。

对任意非零共同尺度 $c$，三角递推直接归纳给出

$$
R_p(cD;a)=c^{1-p}R_p(D;ca).
$$

令 $D=\pi^2d$，便得到

$$
R_p(d;A)=\pi^{2(p-1)}R_p\left(D;A/\pi^2\right).
\tag{5}
$$

因此只需研究 $R_p(d;A)/p$。

### Step 2. 在特征零中证明整体 $p$ 因子与局部整性

以 $d_n$ 替换 $(2)$ 的传播子。三角递推和指数微分递推只除以单位
$d_n$ 及整数 $1\le n<p$，所以全部所需 $v_n,E_n,F_n$
均在 $\mathcal R[A]$ 中。
次数／权重归纳还给出 $\deg_A R_p\le m$。

为证明可合法除以 $p$，临时引入一步幅度 $b$，定义

$$
\Phi_p(v;b,A)=[t^p]\left(
\frac12v\mathcal Dv-bte^v-\frac A2t^2e^{2v}\right),
\quad \mathcal D(t^n)=d_nt^n.
\tag{6}
$$

这只涉及有限多项式系数；两项指数分别只用到 $p-1,p-2$ 阶。
反射对称性保证 $[t^p]f\mathcal Dg=[t^p](\mathcal Df)g$。
对每个系数变量求导，驻值方程正是
$d_nv_n=bE_{n-1}+AF_{n-2}$、$1\le n<p$。
这些方程三角可解。此推导只用反射对称性和非零传播子，
不要求复数 $d_n$ 具有实正性。

记临界值为 $G_p(b,A)$。给 $b$ 权重 $1$、$A$ 权重 $2$，
递推使 $G_p$ 具有权重 $p$。在特征零中，Euler 恒等式与驻值 envelope 给出

$$
pG_p=b\,\partial_bG_p+2A\,\partial_AG_p
=-bE_{p-1}-AF_{p-2}=-R_p(d;b,A).
$$

故在 $b=1$ 时

$$
\mathcal S_p(A):=R_p(d;A)/p=-G_p(1,A)\in\mathcal R[A],
\qquad
\mathcal S_p'(A)=\frac12F_{p-2}(A).
\tag{7}
$$

局部整性来自 $(6)$ 的系数表达，绝不是在剩余域里把零多项式除以零。
因此 $\deg\mathcal S_p\le m<p$。
未经这一步的 $R_p(d;A)$ 在模 $\pi$ 下确实恒为零。

### Step 3. 剩余域中的有限平方传播子分支

在 $\mathbb F_p[A][t]/(t^p)$ 中，令

$$
B=\frac{1+A}{4},\qquad P(t)=1+t+Bt^2.
$$

截断对数 $\bar v=-\log P\pmod{t^p}$ 合法，因为只除以 $1,\ldots,p-1$。
有限指数与对数的复合身份同样合法，故
$\bar E=e^{\bar v}=P^{-1}\pmod{t^p}$。

用 $N=t\partial_t$，直接对二次多项式作代数微分可验证

$$
N^2\log P=\frac tP+\frac{At^2}{P^2}.
$$

因此对全部 $1\le n<p$，$\bar v$ 满足
$-n^2\bar v_n=\bar E_{n-1}+A\bar F_{n-2}$。
由这些非零分母的三角唯一性，它就是 $(4)$ 的约化分支。
所以

$$
\bar E=P^{-1}\pmod{t^p},\qquad
\bar F=P^{-2}\pmod{t^p}.
\tag{8}
$$

这一步是有限剩余域代数验证，不借助跨越第 $p$ 阶的形式指数，
也不需要在特征 $p$ 中积分一个带 $1/p$ 的方程。

### Step 4. 精确计算 $\bar F_{p-2}$

暂在函数域扩张 $\mathbb F_p(A,\delta)$ 中令 $\delta^2=-A$，
$\alpha=(-1+\delta)/2$、$\beta=(-1-\delta)/2$。
这是证明装置；最终结果是 $\mathbb F_p[A]$ 中的多项式身份。
有 $\alpha+\beta=-1$、$\alpha-\beta=\delta$、
$\alpha\beta=B$，以及 $P=(1-\alpha t)(1-\beta t)$。

部分分式系数计算给出

$$
[t^n]P^{-2}
=\frac{(n+1)(\alpha^{n+2}+\beta^{n+2})}{\delta^2}
-\frac{2\alpha\beta(\alpha^{n+1}-\beta^{n+1})}{\delta^3}.
$$

取 $n=p-2$。在特征 $p$ 中，
$\alpha^p+\beta^p=(\alpha+\beta)^p=-1$，并且

$$
\beta\alpha^p-\alpha\beta^p=\frac{\delta-\delta^p}{2}.
$$

由于 $n+1=-1$，上述两项分别为
$\delta^{-2}$ 与 $-\delta^{-2}+\delta^{p-3}$，所以

$$
\boxed{\bar F_{p-2}(A)=\delta^{p-3}=(-A)^{m-1}.}
\tag{9}
$$

两边均为 $A$ 的多项式，故在函数域中证明后即在 $\mathbb F_p[A]$ 中恒等，
包括 $A=0$ 或 $A=-1$ 等退化二次分解点，不需删去任何参数。

### Step 5. 导数与常数项锁定 primitive 约化

由 $(7)$、$(9)$，

$$
\overline{\mathcal S_p}'(A)=\frac12(-A)^{m-1}
=\frac d{dA}(-A)^m,
$$

最后等号使用 $-m=1/2$ 在 $\mathbb F_p$ 中成立。
两边所对应多项式的次数均小于 $p$，故导数相等意味着只差常数。
不能省略这个次数界：一般特征 $p$ 导数核还含 $A^p$。

在 $A=0$ 时，$P=(1+t/2)^2$，所以对 $1\le n<p$，

$$
\bar v_n=\frac{(-1)^n}{n2^{n-1}},\qquad
\bar E_{p-1}=\frac{p}{2^{p-1}}=0.
$$

用有限临界值 $(6)$ 求常数项，不通过除以约化后的 $R_p$：

$$
\begin{aligned}
\bar G_p(1,0)
&=\frac12\sum_{n=1}^{p-1}(-n^2)\bar v_n\bar v_{p-n}-\bar E_{p-1}\\
&=\frac1{2^{p-1}}=1.
\end{aligned}
$$

其中每个求和项在 $\mathbb F_p$ 中为 $-2^{2-p}$，
共有 $p-1$ 项；最后使用 $2^{p-1}=1$。
因而 $\overline{\mathcal S_p}(0)=-1$，得到

$$
\boxed{\overline{\mathcal S_p}(A)=(-A)^m-1.}
$$

这也说明 primitive 候选确为局部 primitive：其最高次系数为单位，
次数没有塌缩。原 $R_p(d;A)$ 所有系数的最小 $\pi$ 赋值恰为 $p-1$，
即整体 $p$ 因子精确到局部单位。

### Step 6. 平方自由性返回实际多项式

约化多项式有次数 $m$，导数为
$m(-1)^mA^{m-1}$，其中 $1\le m<p$。
导数的唯一可能零点是 $A=0$，但多项式在该点为 $-1$；
当 $m=1$ 时导数本身为非零常数。
故两者在 $\overline{\mathbb F_p}$ 中没有共同根。

$\mathcal S_p$ 及其导数均次数保持，Sylvester resultant 的矩阵按系数约化，
因此它的约化是上述两个互素多项式的非零 resultant。
所以 $\operatorname{Res}(\mathcal S_p,\mathcal S_p')$ 是 $\mathcal R$ 中的单位，
特别在特征零域 $K$ 中非零。这证明 $\mathcal S_p$ 在特征零中平方自由。

由 $(3)$、$(5)$，

$$
C_{r,p}(\lambda)
=2(-1/2)^p\,p\,\pi^{-2(p-1)}
\mathcal S_p(-4\pi^2\lambda).
$$

总体因子与参数乘法因子都非零，故根及其重数只作可逆尺度变换。
因此 $C_{r,p}$ 平方自由，次数为 $m$。
对每个 $r$ 使用其本原 $\zeta$ 和 $\pi$，上述局部约化完全相同，
所以结论覆盖全部 $1\le r<p$。$\square$

## Corrections or Missing Assumptions

- 不能把 $R_p'$ 在模 $p$ 下消失解释为特征零必有重根。
  本例未经 primitive 归一的 $R_p$ 整个约化就是零；合法除去 $p$ 后，
  约化反而具有保持次数的简单根。
- 合法除 $p$ 必须先在特征零中证明 $R_p=-pG_p$ 及 $G_p$ 的局部整性。
- $p$ 必须是奇素数；$2$ 的可逆性以及全部 $1\le n<p$ 分母的单位性均实际使用。
- 局部剩余域的简单性没有提供复嵌入下的根实性，本文未作该推断。

## Evidence and Coordination Record

本轮没有执行任何素数列表、根数扫描或数值实验。
推导从一般奇素数 $p$ 的符号恒等式完成。
主控独立核得特征零平方传播子的二次分母式，并另外核对了
有限域的 $(9)$ 及常数项 $-1$；这些沟通不代替本稿后续正式非作者核查。
本稿没有重复主控的 ODE 求解，只给出所需有限剩余域身份的直接验证。

唯一外部文献动作是两条定点检索及打开 Milne 作者官网讲义核对局部分圆事实。
未将这一标准数论输入或新证明直接宣布为全球原创。
旧作者稿、已接受产物、$Q$ 算法及所有诊断文件均未修改。

## Open Risks and Handoff

1. 奇素数分母的平方自由性已由本稿证明；这些分母的全部根是否实仍未证明。
2. 合数分母的重根结构不由本局部素数论证覆盖。
3. $C,Q$ 在实际首项消失点是否共同为零仍是独立问题。
4. 需要针对本稿实际归一化、模 $p$ 系数及 resultant 转移做非作者核查。
5. 不产生正文容量、正式候选票、论文立项、Route 评价或 PDF 产物结论。
