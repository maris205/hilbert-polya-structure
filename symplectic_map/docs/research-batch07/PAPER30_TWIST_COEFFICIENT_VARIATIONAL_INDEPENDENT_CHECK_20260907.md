# 有限系数变分：非作者独立核查

日期：2026-09-07。审查者：`p30_twist_leading_structure_probe`，未参与被审
有限系数泛函的构造或作者计算。使用本轮完整读取的 `proof-writer` 技能，
检查真正成立的有界命题，不把新规约升级成全实根或简单性定理。
只新增本报告，未编辑作者文件、旧接受包或状态索引。

## Claim and status

输入为全文读取的
[有限系数变分作者稿](PAPER30_TWIST_ROOT_SIMPLICITY_PROBE_V1_20260907.md)，
SHA256：`eb332a74bcfed71f2f7d14ab73e5b0851a48eb9bb40e1c9c9b1176c4457e9ede`。

所审有限变分／导数／Hessian 规约：`PROVABLE AS STATED`。
下列 8 项全部 **PASS**，没有要求作者修改的实质错误。
原全分母根实性、简单性及 $C,Q$ 共同根排除均不在本次通过结论内。

## Assumptions and notation

固定 $s\ge3$，传播子满足 $D_n>0$、$D_n=D_{s-n}$，$1\le n<s$。
实际正弦传播子是其特例。作者的 $v$ 是 $s-1$ 个形式级数系数，
$\Phi_s$ 是用 $[t^s]fg$ 双线性配对构成的有限多项式，不是实际周期配置上的
作用量或旧正定零均值 Hessian。记 $\mathscr H=\Phi_{vv}$。

## Itemized verdicts

| 核查项 | 结论 | 证据 |
| --- | --- | --- |
| 1. $\Phi_s$ 临界方程等价正频递推且唯一 | PASS | 反射对称使系数配对下 $\mathcal D$ 对称；反向指标覆盖全部三角方程 |
| 2. 加权齐次性与 $R_s=-sG_s$ | PASS | 权重 $(b,a)=(1,2)$，临界值包络消去隐含响应，Euler 恒等式正确 |
| 3. $R_s'=(s/2)F_{s-2}$ | PASS | 对完整临界值求总参数导数，未冻结 $v^*$ |
| 4. 实际 $C'$ 的缩放与 SUM-action 因子 | PASS | $C'= -4s(-1/2)^sF=-sF^{\mathrm{orig}}$；另作四分母精确核算 |
| 5. 首一 gcd 严格相等 | PASS | 两组生成理想完全相同，不只是共同根集合相同 |
| 6. 反三角 Hessian 及常数行列式 | PASS | 任意 $v,b,a$ 的支撑核对及反列置换；四分母独立 Hessian 行列式为 $-16$ |
| 7. 全实系数空间的固定惯性 | PASS | 正反对角矩阵的二维配对，加固定非零行列式的实对称同伦 |
| 8. $R_s''=s\beta^T\mathscr H^{-1}\beta$ 及边界 | PASS | 两次包络导数和隐含响应独立推导；四分母精确响应为 $1$ |

## Proof strategy and dependency map

先直接重推有限配对、临界值及二次响应的代数证明；再用真实四分母
$D=(2,4,2)$ 独立写出新的系数泛函，验证其梯度、临界值、Hessian 和响应。
这个最小例针对本轮实际新增泛函，不重新证明或扫描旧四分母根。

1. 临界方程依赖传播子反射对称，不能仅以正性替代。
2. 临界点的全局有限系数唯一性来自严格三角递推，不依赖极小化或凸性。
3. 固定惯性与参数根横截性是不同问题；前者不能推出后者。

## Independent proof checks

### 1. 系数变分与临界值

对不含常数项的 $f,g$，$[t^s]f\mathcal Dg$ 只含 $i+j=s$ 的配对，
反射对称保证 $D_i=D_j$，故一阶变分确为

$$
\delta\Phi_s=[t^s]\delta v(\mathcal Dv-bt e^v-at^2e^{2v}).
$$

取 $\delta v=t^i$ 得残差的 $s-i$ 阶。随着 $i=1,\ldots,s-1$，
它恰好覆盖全部非共振阶，不多不少。每阶只依赖更低阶 $v$，所有 $D_n$
均非零，故对每个复参数 $b,a$ 都有唯一系数临界点，且各系数为参数多项式。

缩放 $(b,a)\mapsto(\rho b,\rho^2a)$ 时，$v_n$ 乘 $\rho^n$，
所以临界值 $G_s$ 权重为 $s$。驻值使链式项消失，得到

$$
G_b=-E_{s-1},\qquad G_a=-\frac12F_{s-2},
\qquad sG_s=bG_b+2aG_a=-R_s.
$$

所以 $R_a=-sG_a=sF_{s-2}/2$ 正确。它是包含 $v^*(b,a)$ 响应的导数。

### 2. 缩放和 gcd 的精确含义

设 $h=-1/2$。由 $C(\lambda)=2h^sR_s(-4\lambda)$，直接链式求导得
$C'=-8h^sR_a=-4s h^sF$。而 $F^{\mathrm{orig}}=h^{s-2}F$、$h^2=1/4$，
所以恰等于 $-sF^{\mathrm{orig}}$。从实际投影驻值的 SUM-action 包络
$\partial_\lambda W=-\epsilon^2\sum_j\cos2q_j$ 提取首项也给出同一个因子。

在 $b=1$、以 $a$ 为多项式变量时，写 $E=E_{s-1}$、$F=F_{s-2}$。
由于 $s/2\ne0$，有严格的多项式理想等式

$$
(R,R')=(E+aF,(s/2)F)=(E,F).
$$

因此两个首一 gcd 完全相等，包含全部因子重数。
这不是从“共同根集合相同”直接跳到 gcd 重数相同。
作者也没有声称该公共 gcd 已经是 $1$。

### 3. 系数 Hessian 的支撑、行列式和惯性

直接二次求导得到

$$
\mathscr H_{ij}=D_j\mathbf1_{i+j=s}
-bE_{s-i-j-1}-2aF_{s-i-j-2}.
$$

当 $i+j>s$，所有下标项为零；当 $i+j=s$，只剩反对角 $D_j$。
反转 $s-1$ 列后得到三角矩阵，列置换符号是
$(-1)^{(s-1)(s-2)/2}$，故作者的恒定行列式正确。
实际正弦情形的 $\prod D_n=s^2$ 也吻合单位根乘积。

实系数时，纯反对角矩阵有每对 $i,s-i$ 的正负特征值各一个；
偶数 $s$ 另有中央正块。到实际 $\mathscr H$ 的实对称直线同伦保持整个
反三角支撑及反对角元，所以行列式始终非零，没有特征值过零。
这证明对所有实 $v,b,a$，不只临界点，惯性固定为

$$
(\lfloor s/2\rfloor,\lfloor(s-1)/2\rfloor,0).
$$

$s\ge3$ 因而确有负方向。作者正确把它称为系数鞍点规约，未误认成旧实际
配置的正定横向 Hessian，也未从其常数行列式推出 $R$ 的参数谱表示。

### 4. 二阶响应

在临界点，$\Phi_{va}=-\beta$，其中 $\beta_i=F_{s-i-2}$。
对 $\Phi_v(v^*(a),a)=0$ 求导给出
$\mathscr H v_a^*=\beta$。又因为 $\Phi$ 对 $a$ 显式线性，

$$
G_{aa}=-\beta^T\mathscr H^{-1}\beta,
\qquad R_{aa}=s\beta^T\mathscr H^{-1}\beta.
$$

无缺少 $1/2$ 或反号。它使用双线性收缩；固定鞍点惯性不能给这个响应
统一正号，作者没有以此宣称凸性或全根横截性。

### 5. 独立真实四分母泛函核算

写 $v=xt+yt^2+zt^3$，直接系数提取得到

$$
\Phi_4=2xz+2y^2-bz-bxy-\frac b6x^3-ay-ax^2.
$$

先解 $\Phi_z=0$，再解 $\Phi_y=0$、$\Phi_x=0$，得到

$$
x^*=b/2,\qquad y^*=b^2/8+a/4,\qquad z^*=b^3/8+5ab/8.
$$

代入得

$$
G_4=-a^2/8-3ab^2/8-5b^4/96=-R_4/4.
$$

独立 Hessian 为

$$
\mathscr H_4=
\begin{pmatrix}-2a-bx&-b&2\\-b&4&0\\2&0&0\end{pmatrix},
\qquad\det\mathscr H_4=-16.
$$

在临界点 $\beta=(b,1,0)^T$，解线性方程得到
$\mathscr H_4^{-1}\beta=(0,1/4,5b/8)^T$，所以
$4\beta^T\mathscr H_4^{-1}\beta=1=R_{4,aa}$。
这是对本轮新泛函与响应的直接检查，不依赖旧四分母根证明。

## Exact computation actually run

以下独立精确片段已执行，返回 `EXACT_PASS`。没有新根扫描，没有重跑
作者的六分母辅助凸性例；其有限实例不承担上面的全分母惯性证明。

```python
import sympy as S
x,y,z,b,a,lam = S.symbols("x y z b a lambda")
Phi = 2*x*z+2*y*y-b*z-b*x*y-b*x**3/6-a*y-a*x*x
variables = (x,y,z)
grad = S.Matrix([S.diff(Phi,t) for t in variables])
H = S.hessian(Phi,variables)
star = {x:b/2, y:b*b/8+a/4, z:b**3/8+5*a*b/8}
assert all(S.expand(c.subs(star)) == 0 for c in grad)
G = S.factor(Phi.subs(star))
R = a*a/2+3*a*b*b/2+5*b**4/24
assert S.expand(R+4*G) == 0
F2 = S.expand((2*y+2*x*x).subs(star))
assert S.expand(S.diff(R,a)-2*F2) == 0
assert S.factor(H.det()) == -16
beta = S.Matrix([b,1,0])
response = S.simplify((4*beta.T*H.subs(star).inv()*beta)[0])
assert response == S.diff(R,a,2) == 1
C = S.expand(2*S.Rational(-1,2)**4*R.subs({b:1,a:-4*lam}))
Forig = S.Rational(1,4)*F2.subs({b:1,a:-4*lam})
assert S.expand(S.diff(C,lam)+4*Forig) == 0
print("EXACT_PASS: finite coefficient variational identities")
```

## Corrections or missing assumptions

未发现需要作者修正的有界公式或结论。传播子反射对称性、$b=1$ 下的 gcd
变量规范、首一 gcd、实系数惯性与双线性配对等必要限定已经写明。

## Open risks

PASS 只接受有限系数变分、导数及 Hessian 规约。它们仅用正性和反射对称性，
仍未利用足够的真实三角结构排除 $(E,F)$ 的公共零点。
原全分母实根／重数及固定消失点后 $Q$ 的非零性继续 OPEN。
旧两轮 11／7 项审查不重开；本报告不作候选票、容量、PDF 或批次完成判断。
