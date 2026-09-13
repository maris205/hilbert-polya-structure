# Proof Package：已有 $p=5$ 例外分支的精确闭合

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
使用本轮完整读取的 `proof-writer` 技能。本件是新的有限例作者证明，
不是旧 V2 的重复审查，不是本件自己的独立验收票，也不是一般素数定理。

## Claim

仅考虑 $p=5$。令 $h^2-5h+5=0$，采用既有正 kick／SUM-action 规范的
精确多项式 $\widetilde C(L),J(L)$。则

$$
\gcd_{\mathbb Q(h)[L]}(\widetilde C,J)=1.
$$

在完成实局部环 $\mathcal O^+=\mathbb Z_5[h]$ 中，令 $\alpha$ 为
$\widetilde C$ 唯一满足 $\alpha\equiv-1\pmod h$ 的根，则

$$
\frac{J(\alpha)}{h^4}\equiv2\pmod h,
\qquad v_h(J(\alpha))=4,\qquad v_\pi(J(\alpha))=8.
$$

由于 $\rho=-h$、$Q(L/\rho)=-5\rho^{-6}J(L)$，进一步有

$$
Q(\alpha/\rho)\equiv2\pmod h,\qquad
v_h(Q(\alpha/\rho))=v_\pi(Q(\alpha/\rho))=0.
$$

因此原有 $p=5$ 单例的最后一个未排除分支也不可能是共同根。

## Status

`PROVABLE AS STATED`。本件给出两个相互校核的精确证书：非零 resultant，
以及例外 Hensel 根附近的有限提升。尚须非作者核查本件新的推导。

## Assumptions

- 输入是 [旧 V2 作者稿](PAPER30_TWIST_PRIME_POST_CANCELLATION_PROBE_V2_20260907.md)
  式 (13)，SHA256
  `6a4a3fa115f277658caed29de4a6f5d35f88d533b3901dd0831e720547c559a1`。
- 该式已在既有[非作者核查](PAPER30_TWIST_PRIME_POST_CANCELLATION_INDEPENDENT_CHECK_20260907.md)
  中从递推精确复算。本轮不重开未变的输入推导。
- $h$ 是 $\mathcal O^+$ 的素元，$v_h(5)=2$，$v_\pi(h)=2$，
  $\mathcal O^+/(h)=\mathbb F_5$。特别是
  $$5=\frac{h^2}{h-1},\qquad \frac5{h^2}\equiv-1\pmod h.$$
- 全部计算在精确域中进行；没有浮点根、其他素数或根清单扫描。

## Notation

用非零常数改变整体规范，定义

$$
f=-\frac{384}{5}\widetilde C
=(1344h-1536)L^2+(528h-560)L+48h-59,
$$
$$
g=9216J
=(53760-49152h)L^3+(46080-55872h)L^2
+(7800-10200h)L+125-240h.
$$

$f,g$ 与原多项式的共同根完全相同。以下 $v_h$ 取 $v_h(h)=1$。
所有模 $h$ 的陈述在完成实局部环中，而不是在大圆分环的非约化商环中。

## Proof Strategy

先在 $\mathbb Q[h]/(h^2-5h+5)$ 中计算 Sylvester 行列式，排除共同根。
再给出一个显式近似根 $a$，以可直接代入的恒等式确定 $J(\alpha)$ 的
确切最低阶和剩余值。最后用 resultant 的赋值再次核对这一个根的阶数。

## Dependency Map

1. 互素性只依赖输入精确多项式、二次域关系及 resultant 的共同根判据。
2. 根提升使用 $\bar f=1-L^2$ 的简单根和完整 DVR 的 Hensel 引理；
   这些假设在 $\mathcal O^+$ 中满足。
3. 精确局部估值由显式代入证书和 $J\in h\mathcal O^+[L]$ 得出。
4. 返回 $Q$ 只使用上述非零缩放及 $5/h^2\equiv-1$。

## Proof

### Step 1. 非零 resultant 短证书

精确结果为

$$
\boxed{
\operatorname{Res}_L(f,g)
=-629145600(42016523h-58061915)
=-2^{23}\cdot3\cdot5^2(42016523h-58061915).}
\tag{1}
$$

给出可直接展开校核的整数证书：若暂将 $h$ 视为自由变量，Sylvester
行列式是

$$
-786432\bigl(281417328h^5-517590243h^4-764101458h^3
+2458365255h^2-1967075690h+512231525\bigr).
\tag{2}
$$

式 (2) 减去式 (1) 恰好等于

$$
-21233664(h^2-5h+5)
\bigl(10422864h^3+32944311h^2+84307181h+347864915\bigr).
\tag{3}
$$

这在二次域中证明 (1)。$h$ 不是有理数，因为其最小多项式的判别式为
$5$；故 $42016523h-58061915\ne0$。Resultant 非零严格排除全部代数共同根，
不只排除所考察的局部剩余类。因此 $\gcd(\widetilde C,J)=1$。

### Step 2. 唯一例外根的直接提升证书

由 $\bar f=1-L^2$，两个剩余根 $1,-1$ 都简单，分别有唯一 Hensel 提升。
取例外类的显式近似值

$$
a=-1+3h+h^2+4h^3=88h-106.
\tag{4}
$$

代入精确二次多项式，得到

$$
\boxed{\frac{f(a)}{h^4}=382457h-506337,\qquad
f'(a)=627984h-857648.}
\tag{5}
$$

第一式整，第二式模 $h$ 为 $2$，所以 $a$ 与唯一根 $\alpha$ 满足
$\alpha-a\in h^4\mathcal O^+$。也可直接利用

$$
f(\alpha)-f(a)=(\alpha-a)
\bigl((1344h-1536)(\alpha+a)+(528h-560)\bigr),
$$

括号模 $h$ 为 $f'(-1)=2$，因而为单位，严格推出这一提升精度。

对 $J$ 的代入证书是

$$
\boxed{\frac{J(a)}{h^4}
=\frac{4285396327}{9216}-\frac{1037721109}{3072}h
\equiv2\pmod h.}
\tag{6}
$$

输入多项式的全部系数都属于 $h\mathcal O^+$：每个常数系数都含因子
$5$，其余系数含 $h$，分母均为 $5$-单位。因此多项式差分恒等式给出

$$
J(\alpha)-J(a)\in h(\alpha-a)\mathcal O^+
\subset h^5\mathcal O^+.
$$

将其与 (6) 合并便得 $J(\alpha)/h^4\equiv2$，从而确切地
$v_h(J(\alpha))=4$、$v_\pi(J(\alpha))=8$。

### Step 3. 为什么不能删去含 $5$ 的常数项

上述代入从始至终使用 $h^2-5h+5=0$，没有先设置 $5=0$。这种区别
在本例是实质性的。例如精确地

$$
J(-1)=\frac{45h}{128}-\frac{15355}{9216},\qquad
\frac{J(-1)}{h^2}
=\frac5{h^2}\left(\frac{9h}{128}-\frac{3071}{9216}\right)
\equiv1\pmod h.
\tag{7}
$$

而原平方传播子展开中的真正常数项是
$J_0(L)=-35W_6(L)$。在 $L\equiv-1$ 时，
$q=(1-4L)/16\equiv0$，故由 $W=-\log(1-x/2+qx^2)$ 得
$W_6\equiv1/(6\cdot2^6)=4\pmod5$。因此

$$
\frac{J_0(\alpha)}{h^2}
=-7\frac5{h^2}W_6(\alpha)\equiv3\pmod h.
\tag{8}
$$

所以形式 $J_0$ 本身就贡献非零的 $h^2$ 项；它不能像更高分歧阶情形那样
从二阶分析中直接删除。式 (4)–(6) 使用全部精确系数，已包括此项以及其余
项在真实首项根处的相消，最终首个非零项为 $2h^4$。

### Step 4. Resultant 估值的独立一致性核对

在 (1) 中，$42016523$ 是 $5$-单位，而 $58061915$ 可被 $5$ 整除且
不可被 $25$ 整除。因此括号中两项的 $h$ 赋值分别为 $1,2$，不能相消。
于是

$$
v_h(\operatorname{Res}(f,g))=4+1=5,
\qquad \frac{\operatorname{Res}(f,g)}{h^5}\equiv3\pmod h.
\tag{9}
$$

令 $\beta\equiv1\pmod h$ 为另一个根。旧第一曲率约化
$\overline{J/h}=3L^2(L+1)$ 给出 $J(\beta)/h\equiv1$。
$f$ 首项系数模 $h$ 为 $4$，而 $9216\equiv1$。故 resultant 的乘积式

$$
\operatorname{Res}(f,g)=(1344h-1536)^3g(\alpha)g(\beta)
$$

先给出 $v_h(J(\alpha))=5-1=4$，再给出
$J(\alpha)/h^4\equiv3/4=2$，与直接证书一致。

### Step 5. 返回物理规范的 $Q$

利用 $\rho=-h$ 及 $p+1=6$，

$$
Q(\alpha/\rho)
=-\frac5{h^6}J(\alpha)
=-\frac5{h^2}\frac{J(\alpha)}{h^4}
\equiv-(-1)\cdot2=2\pmod h.
$$

它是局部单位，故不会为零。至此 $p=5$ 原有例外分支完全闭合。$\square$

## Exact Verification Actually Run

已运行以下精确符号检查；没有浮点数或其他素数输入。

```python
import sympy as S
h, L = S.symbols("h L")
H = h*h - 5*h + 5
f = (1344*h-1536)*L**2 + (528*h-560)*L + 48*h-59
g = ((53760-49152*h)*L**3 + (46080-55872*h)*L**2
     + (7800-10200*h)*L + 125-240*h)
def red(e):
    n, d = S.fraction(S.cancel(e))
    return S.rem(n*S.invert(d, H, h), H, h)
R = -S.Integer(629145600)*(42016523*h-58061915)
assert red(S.resultant(f, g, L)-R) == 0
a = -1 + 3*h + h*h + 4*h**3
assert red(f.subs(L, a)/h**4 - (382457*h-506337)) == 0
assert red(S.diff(f, L).subs(L, a) - (627984*h-857648)) == 0
assert red(g.subs(L, a)/(9216*h**4)
           - S.Rational(4285396327, 9216)
           + S.Rational(1037721109, 3072)*h) == 0
print("EXACT_PASS p=5 resultant and exceptional-root certificates")
```

## Corrections or Missing Assumptions

无须改变输入或增加科学假设。本件新增的是原有 $p=5$ 单例的精确根值分析，
不更改旧 V2 在其写作时将该类列为 OPEN 的历史记录。

## Open Risks

- 尚待非作者对本件新证书的独立核验，作者运行通过不替代独审。
- 这里只闭合 $p=5$；其他奇素数的例外分支未由本件证明。
- 没有关于首项根实性、合数分母或允许参数随振幅调整的推论。
- 本轮仅新增本文件；冻结稿、旧证明、锁、状态和验收产物未改。
