# 真实正弦传播子结构 probe V2：路径身份与 Green 正定性的边界

日期：2026-09-07。作者任务范围：本轮真实
$D_n=4\sin^2(\pi rn/s)$ 的有界结构尝试。
唯一新文件；旧辅助传播子反例及其独立审查均未改动、未重算。
本报告使用本轮重读的 `proof-writer` 技能，因此把下面已证明的两条
结构辨析与未证明的全实根命题分别标示。
没有文献检索、新分母数值扫描、论文、PDF、容量估计或正式候选票。

## Claim

对每个互素 $0<r<s$、$s\ge3$，真实双谐波辛映射

$$
p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,
\qquad q'=q+p'
$$

的首项共振系数 $C_{r,s}(\lambda)$ 是否有
$\lfloor s/2\rfloor$ 个正实单根？本轮具体尝试两条桥接：

1. 把真实正弦传播子代入常系数一步／两步线性路径和，能否得到同一个多项式？
2. 利用循环 Laplacian 的实对称正定 Green 核，能否直接获得实根保持结构？

原全分母命题不缩减成有限低分母清单。以下真实 $s=4$ 计算用于否定
一个明确的身份，而不是以低分母成功替代全分母证明。

## Status

原全实根／简单性命题：`NOT CURRENTLY JUSTIFIED`。

本轮严格证明：第一条最直接的路径身份即使允许总体尺度及参数乘法重标，
仍在真实 $r/s=1/4$ 失败；第二条重写确有正定 Green 核，但实际相位系数
使用复双线性而非 Hermitian 收缩，不能仅凭这个正定性推出实根结论。

没有获得真实模型的非实根／重根反例，也没有排除更深层的 Jacobi 或
稳定多项式表示。这两条辨析不计作一个新的独立论文主结果。

## Assumptions and notation

固定互素 $r,s$，置 $\omega=2\pi r/s$、$a=-4\lambda$。
使用已经核正的正树权规范：

$$
R_n=E_{n-1}+aF_{n-2},\qquad v_n=R_n/D_n\quad(1\le n<s),
$$

其中 $E=e^v$、$F=e^{2v}$、$E_0=F_0=1$、$F_{-1}=0$；
$R_s=E_{s-1}+aF_{s-2}$ 不除以共振分母。
实际作用量的系数为

$$
C_{r,s}(\lambda)=2(-1/2)^sR_s(-4\lambda).
$$

这里只引用该规范，不重开旧首项约化证明。

## Proof strategy and dependency map

第一条尝试先精确定义目标线性路径和，再检查一个在总体尺度和参数乘法
重标下不变的二次系数比。第二条尝试把逆传播子回到物理格点，证明 Green
核身份，并逐项检查正定性所对应的乘积是否就是实际解析相位系数所用的乘积。

依赖关系为：

1. 常系数路径和身份失败只依赖真实 $D_1,D_2,D_3=(2,4,2)$ 及有限代数。
2. Green 核身份由二阶差分和边界条件直接验证。
3. 双线性／Hermitian 区别由真实离散 Fourier 模的求和恒等式直接验证。
4. 任何全实根定理仍需额外的精确行列式、匹配权或其他保根身份证明。

## Proof

### Step 1. 最直接的线性路径对象

定义

$$
T_{-1}=0,\qquad T_0=1,\qquad
T_n=\frac{T_{n-1}+aT_{n-2}}{D_n}\quad(1\le n<s),
\qquad T_s=T_{s-1}+aT_{s-2}.
$$

等价地，对所有由 $1,2$ 构成、和为 $s$ 的有序组合
$(\ell_1,\ldots,\ell_k)$ 求和：每个长度为 $2$ 的步贡献一个 $a$，
每个真部分和 $m_j=\ell_1+\cdots+\ell_j<s$ 贡献 $D_{m_j}^{-1}$。
按最后一步分解组合即得到上式递推，所以这个组合描述与递推一致。

它就是“保留一步／两步常谐波路径结构，只把传播子换成实际正弦分母”的
具体对象。这里没有允许任意依赖阶数的新权重，因为那已是额外的待证结构，
不再是直接替换分母。

### Step 2. 真实四分母下不存在比例或乘法重标身份

在 $r/s=1/4$ 时，$D_1=D_3=2,D_2=4$。树递推给出

$$
v_1=\frac12,\quad
v_2=\frac18+\frac a4,\quad
v_3=\frac18+\frac{5a}8,
$$

继而

$$
E_3=\frac5{24}+\frac{3a}4,\qquad
F_2=\frac34+\frac a2,
\qquad R_4=\frac5{24}+\frac{3a}2+\frac{a^2}2.
$$

线性路径和则为

$$
T_4=\frac1{16}+\frac a2+\frac{a^2}4.
$$

其中常数项来自组合 $1111$；一次项分别来自 $211,121,112$，权重为
$1/8,1/4,1/8$；二次项来自 $22$，权重为 $1/4$。

对系数 $b_0,b_1,b_2$ 均非零的二次多项式，定义

$$
I(b_0+b_1a+b_2a^2)=\frac{b_1^2}{b_0b_2}.
$$

若 $Q(a)=A\,P(Ba)$ 且 $A,B\ne0$，分子和分母均乘以 $A^2B^2$，
故 $I(Q)=I(P)$。但本例

$$
I(R_4)=\frac{108}{5},\qquad I(T_4)=16.
$$

因此不存在任何非零 $A,B$ 使 $R_4(a)=A\,T_4(Ba)$。
这个结论也覆盖给每个一步一个固定非零权 $b$、每个两步一个固定权 $ca$
的修改，因为总步长为 $s$，相应多项式必为
$b^sT_s(ca/b^2)$；$c=0$ 时次数已经不符。

此处否定的是明确的直接路径桥接，**不是**任意更复杂的三对角表示。∎

### Step 3. 真实循环 Green 核的精确重写

令 $L$ 是 $s$ 周期二阶差分，

$$
(Lx)_j=2x_j-x_{j-1}-x_{j+1},\qquad j\pmod s.
$$

定义 $0\le j<s$ 上的核

$$
g_j=\frac{s^2-1}{12s}-\frac{j(s-j)}{2s}.
$$

对 $1\le j<s$，二次多项式差分给出 $(Lg)_j=-1/s$；在 $j=0$，
由 $g_1=g_{s-1}$ 得 $(Lg)_0=(s-1)/s$。又因为
$\sum_{j=0}^{s-1}j(s-j)=s(s^2-1)/6$，有 $\sum_jg_j=0$。
因此

$$
Lg=\delta_0-\frac1s\boldsymbol1.
$$

将此式作用于非零 Fourier 模便得到

$$
\sum_{j=0}^{s-1}g_je^{-i\omega nj}=\frac1{D_n},
\qquad1\le n<s.
$$

若把坐标 $0$ 固定为零，剩余路径 Laplacian 的逆为

$$
K_{ij}=\min(i,j)-\frac{ij}{s},\qquad1\le i,j<s.
$$

固定 $j$ 后，该式关于 $i$ 在 $i<j$ 和 $i>j$ 各自线性，端点值为零，
在 $i=j$ 的二阶差分为 $1$，所以它确是相应逆矩阵。
路径 Laplacian 的二次型为零端点离散差分平方之和，仅在零向量上为零，
从而 $K$ 实对称正定。

这给出了真实正弦分母的精确核表示，不是任意传播子的泛化。

### Step 4. 为什么上述正定性还不是所需保根结论

置 $\zeta=e^{i\omega}$，用完整源 $\phi_j=\zeta^j$，$0\le j<s$。
由于 $\zeta$ 是本原 $s$ 次单位根且 $s\ge3$，

$$
\sum_j\phi_j=0,\qquad \sum_j\phi_j^2=0.
$$

取去掉坐标 $0$ 的列向量 $f=(\zeta,\ldots,\zeta^{s-1})^T$。
$u_j=(\phi_j-1)/D_1$ 满足 $u_0=0$ 且 $Lu=\phi$，故
$Kf=(u_1,\ldots,u_{s-1})^T$。于是

$$
f^T Kf
=\frac1{D_1}\sum_{j=0}^{s-1}\phi_j(\phi_j-1)=0,
$$

而

$$
f^* Kf
=\frac1{D_1}\sum_{j=0}^{s-1}\overline{\phi_j}(\phi_j-1)
=\frac{s}{D_1}>0.
$$

这里第 $0$ 项为零，可以合法加入求和。第二式使用
$|\phi_j|=1$ 及 $\sum_j\overline{\phi_j}=0$。

真实首项的纯正相位展开是解析 Taylor 展开：两个相位因子相乘时频率相加，
并不引入复共轭。所以树边产生的是前一种双线性收缩；把它替换为后一种
Hermitian 收缩会把频率相加改成频率相减，改变正在计算的量。

例如在 $s=4,r=1$，

$$
K=\frac14\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix},
\qquad f=\begin{pmatrix}i\\-1\\-i\end{pmatrix},
$$

确有 $f^TKf=0$、$f^*Kf=2$。这不是正定性失败，而是两种乘积不同。
因此上述 Green 正定性本身没有提供 $R_s(a)$ 的保实根定理。∎

## Reproducible exact check

下面只核对本轮的真实四分母身份及 Green 示例，不新增数值分母清单。

```python
import sympy as sp
a = sp.symbols("a")
D = [0, 2, 4, 2]
v, E, F = [sp.Integer(0)], [sp.Integer(1)], [sp.Integer(1)]
for n in range(1, 4):
    v.append(sp.expand((E[n-1] + (a*F[n-2] if n >= 2 else 0))/D[n]))
    E.append(sp.expand(sum(k*v[k]*E[n-k] for k in range(1, n+1))/n))
    F.append(sp.expand(sum(E[k]*E[n-k] for k in range(n+1))))
R = sp.Poly(E[3] + a*F[2], a)
T = { -1: sp.Integer(0), 0: sp.Integer(1) }
for n in range(1, 4):
    T[n] = sp.expand((T[n-1]+a*T[n-2])/D[n])
Q = sp.Poly(T[3]+a*T[2], a)
assert R.as_expr() == sp.Rational(5,24)+3*a/2+a*a/2
assert Q.as_expr() == sp.Rational(1,16)+a/2+a*a/4
invariant = lambda P: sp.cancel(P.nth(1)**2/(P.nth(0)*P.nth(2)))
assert invariant(R) == sp.Rational(108,5)
assert invariant(Q) == 16
K = sp.Matrix([[3,2,1],[2,4,2],[1,2,3]])/4
f = sp.Matrix([sp.I, -1, -sp.I])
assert sp.expand((f.T*K*f)[0]) == 0
assert sp.expand((sp.conjugate(f).T*K*f)[0]) == 2
print("EXACT_PASS: path identity fails; bilinear and Hermitian contractions differ")
```

## Corrections or missing assumptions

这轮没有得到能关闭原命题的新充分条件。其中特别没有证明：

- 某个非事后构造的 Jacobi 矩阵以 $R_s$ 为特征多项式；
- 某个明确、正权的匹配模型与全部分叉树等价；
- 正弦加法恒等式能消去全部非路径贡献；
- 从 Green 核正定性可推出所需复解析系数多项式稳定。

以上是真正尚缺的身份或引理，而不是通过增加有限根表就能补上的量化误差。

## Open risks and handoff

真实全分母根及重数分类保持 OPEN。原简单消失点后的首个真实分裂项
也不由本报告处理。本轮只关闭两个具体的未经证明桥接：
“直接替换线性路径分母”与“把双线性系数当成 Hermitian 正型”。
没有把新报告与旧辅助反例拼成论文，也没有修改接受状态、科学约束或批次3/5进度。
