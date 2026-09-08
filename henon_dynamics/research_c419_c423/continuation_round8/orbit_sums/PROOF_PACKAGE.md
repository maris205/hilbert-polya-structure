# FC7 proof package: exact short correlations and a method boundary

## Claim and status

The original [FC7](../../continuation_round7/arithmetic_scout/SCOUT_REPORT.md)
is unchanged: for the native map
$$F(x,y)=(y,y^2+1-x)$$
on every odd-prime field, every complete cycle $\mathcal O$ of least
length $L\ge p^{1/2+\eta}$ and every nonzero frequency $(r,s)$ should
satisfy $|S|\le C(\eta)Lp^{-\delta(\eta)}$, for explicit positive
constants and every fixed $0<\eta<1/2$.

**Original-claim status: NOT CURRENTLY JUSTIFIED.**
Neither a proof at that length nor an unbounded-prime obstruction is
obtained. The complete helper below diagnoses the specified
ambient second-moment method; it is not a replacement contract.

**Helper status: PROVABLE AS STATED, author hand derivation.**
Independent internal review is not yet recorded in this author file.

## Assumptions, notation and strategy

Throughout $p$ is odd, $(r,s)\ne(0,0)$ in $\mathbb F_p^2$,
$\ell(x,y)=rx+sy$, and $\psi(t)=\exp(2\pi i t/p)$. Fractions in
character phases mean operations in $\mathbb F_p$. Set
$$
C_d(r,s)=\sum_{P\in\mathbb F_p^2}\psi(\ell(F^dP)-\ell(P)),\qquad
S=\sum_{P\in\mathcal O}\psi(\ell(P)).
$$
Write $\chi$ for the quadratic character, extended by $\chi(0)=0$,
and $G(a)=\sum_t\psi(at^2)$ for $a\ne0$.

Dependency map:

1. Invertibility and orbit invariance give the exact shift moment.
2. Linear orthogonality and quadratic completion evaluate the first
   three lag correlations, which determine the first four shifts.
3. A constant leading coefficient in each longer phase permits
   a univariate Weil estimate at logarithmic lag.
4. Substitution gives the actual orbit-length scale, not the FC7 scale.

The classical input in step 3 is the univariate additive Weil bound:
if $f\in\mathbb F_p[t]$ has degree $1\le D<p$, then
$|\sum_t\psi(f(t))|\le(D-1)\sqrt p$. For $D=1$ this is linear
orthogonality. We impose $D<p$ explicitly; no assertion that arbitrary
nonconstant polynomial functions have cancellation is needed.
The use of this bound and of shifted moments is classical, as in
[Ostafe–Shparlinski, section 3.2](https://arxiv.org/pdf/0902.3884).
Their triangular-system theorem is not being applied to this Hénon map.

## Proof

### 1. Shift identity and elementary Gauss sums

The inverse is $F^{-1}(x,y)=(x^2+1-y,x)$, so $F$ permutes both the
ambient field and the complete cycle. For any integer $H\ge1$,
$$
H S=\sum_{P\in\mathcal O}\sum_{h=0}^{H-1}\psi(\ell(F^hP)).
$$
Cauchy–Schwarz followed by inclusion of the nonnegative summands in
the ambient plane yields
$$
|S|^2\le\frac{L}{H^2}M_H,\qquad
M_H:=\sum_{P\in\mathbb F_p^2}
\left|\sum_{h=0}^{H-1}\psi(\ell(F^hP))\right|^2.
\tag{1}
$$
Changing variables by $F^j$ in each pair with $h-j=d>0$ gives the
exact formula
$$M_H=Hp^2+2\operatorname{Re}
\sum_{d=1}^{H-1}(H-d)C_d(r,s).
\tag{2}$$
The complete-cycle convention removes endpoint-error terms.

For $a\ne0$, quadratic completion gives
$$\sum_t\psi(at^2+bt+c)=G(a)\psi(c-b^2/(4a)).
\tag{3}$$
Also $|G(a)|^2=p$: in
$\sum_{u,v}\psi(a(u^2-v^2))$, the invertible substitution
$(u-v,u+v)=(z,w)$ reduces the sum to $\sum_{z,w}\psi(azw)=p$.
Thus no unproved square-root cancellation is being assumed for
the quadratic cases.

### 2. Lag one: an actual rank-one degeneracy

The phase is
$$
\ell(F(x,y))-\ell(x,y)
=-(r+s)x+sy^2+(r-s)y+s.
$$
Summing over $x$ proves
$$
C_1(r,s)=
\begin{cases}
0,&r+s\ne0,\\
pG(s),&r=-s\ne0.
\end{cases}
\tag{4}
$$
In the second case the remaining phase is $s(y-1)^2$.
Consequently the exceptional magnitude is exactly $p^{3/2}$
for every odd prime. A uniform $O(p)$ assertion for all short-lag
correlations is false. This is an ambient correlation fact, not
a counterexample to orbit cancellation.

### 3. Lag two: two independent quadratic variables

Put $u=y^2+1-x$. The substitution $(x,y)\leftrightarrow(u,y)$ is
bijective. Direct expansion gives
$$
\ell(F^2(x,y))-\ell(x,y)
=su^2+2ru-ry^2-2sy+(s-r).
$$
If $r=0$ then $s\ne0$ and the $y$ sum vanishes; if $s=0$ then
$r\ne0$ and the $u$ sum vanishes. Otherwise (3) gives
$$
C_2(r,s)=G(s)G(-r)
\psi\left(s-r-\frac{r^2}{s}+\frac{s^2}{r}\right).
\tag{5}
$$
Hence $|C_2|=p$ when $rs\ne0$, and $C_2=0$ when $rs=0$.

### 4. Lag three: every exceptional frequency retained

In the same coordinates define $v=u^2+1-y$. Then
$F^3(x,y)=(v,v^2+1-u)$, and expansion gives
$$
\ell(F^3(x,y))-\ell(x,y)=A y^2+B(u)y+C(u),
\tag{6}
$$
where
$$
\begin{aligned}
A&=s-r,\\
B(u)&=-2su^2-r-3s,\\
C(u)&=su^4+(r+2s)u^2+(r-s)u+2s.
\end{aligned}
$$

If $A=0$, nonzero frequency implies $s=r\ne0$. Linear
orthogonality in $y$ imposes $u^2=-2$. On these roots,
$C(u)=r(u^4+3u^2+2)=0$. Therefore
$$C_3(r,r)=p(1+\chi(-2)).
\tag{7}$$
This includes every odd characteristic.

If $A\ne0$, applying (3) in $y$ gives the exact expression
$$C_3(r,s)=G(A)\sum_u\psi(R(u)),\qquad
R(u)=C(u)-\frac{B(u)^2}{4A}.
\tag{8}$$
The reduced polynomial is
$$
R(u)=-\frac{rs}{A}u^4-\frac{(r+s)^2}{A}u^2
+(r-s)u+2s-\frac{(r+3s)^2}{4A}.
\tag{9}
$$
If $r=0$, then $s\ne0$ and
$R(u)=-su^2-su-s/4$; its nonzero quadratic coefficient gives
$|C_3|=p$. If $s=0$, then $r\ne0$ and
$R(u)=ru^2+ru+r/4$, again giving $|C_3|=p$.
If $rs\ne0$, its quartic coefficient is nonzero. For $p\ge5$
the stated Weil bound applies with $D=4<p$ and gives $|C_3|\le3p$.
For $p=3$ the ambient trivial bound is $9=3p$.
Together with (7), these cases prove
$$|C_3(r,s)|\le3p\quad\hbox{for every allowed frequency and prime.}
\tag{10}$$

### 5. What the first four shifts actually prove

Equations (1)–(2) with $H=4$ give
$$
|S|^2\le\frac{L}{16}
\{4p^2+2\operatorname{Re}(3C_1+2C_2+C_3)\}
\le\frac{L}{16}(4p^2+6p^{3/2}+10p).
\tag{11}
$$
There is also a lower estimate on this *ambient moment*:
$$M_4\ge4p^2-6p^{3/2}-10p.
\tag{12}$$
In particular $M_4=4p^2+O(p^{3/2})$ uniformly in the frequency.
Thus even exact evaluation of these three correlations leaves the
ambient second-moment bound at scale $p\sqrt L$.
At the FC7 lower length its displayed relative scale is
$p^{3/4-\eta/2}$, not a negative power. This statement concerns
the upper bound produced by (1); it is not a lower bound on $|S|$.

### 6. Logarithmic lags: a directly proved classical-scale estimate

Define polynomials $X_0=x$, $X_1=y$ and
$X_{n+1}=X_n^2+1-X_{n-1}$. Induction shows that for every $n\ge1$,
$X_n$, as a polynomial in $y$ with coefficients in $\mathbb F_p[x]$,
is monic of degree $2^{n-1}$. The squaring term has twice the
previous degree and cannot cancel with $1-X_{n-1}$.

For $d\ge1$, the phase in $C_d$ is
$$rX_d+sX_{d+1}-rx-sy.$$
If $s\ne0$ its $y$ degree is $2^d$ with constant nonzero
leading coefficient $s$. If $s=0$ and $d\ge2$, its degree is
$2^{d-1}$ with leading coefficient $r$. If $s=0,d=1$,
linear orthogonality gives $C_1=0$.
For $2^d<p$, applying the univariate Weil bound for each fixed
$x$, then the triangle inequality over $p$ values of $x$, proves
$$|C_d(r,s)|\le2^d p^{3/2}.
\tag{13}$$

For $p\ge17$ choose $H=\lfloor(\log_2p)/4\rfloor\ge1$.
Then $2^{H}\le p^{1/4}$ and all lags $1\le d<H$ obey the degree
condition. From (2), using
$\sum_{d=1}^{H-1}(H-d)2^d\le H2^H$, one obtains
$$
M_H\le Hp^2+2H2^Hp^{3/2}
\le Hp^2(1+2p^{-1/4})\le2Hp^2.
$$
The elementary inequality $\lfloor t\rfloor\ge t/2$ for $t\ge1$
gives $H\ge(\log_2p)/8$. Therefore
$$
\boxed{\quad
|S|\le4p\sqrt{\frac{L}{\log_2p}}\quad(p\ge17).
\quad}
\tag{14}
$$
For odd $p<17$, retain the valid trivial bound $|S|\le L$.
No original-body theorem from the inaccessible 2010 article is
needed for (14).

The certified relative bound in (14) becomes less than one only
when $L>16p^2/\log_2p$. Since $L\le p^2$, the largest permitted
length yields only logarithmic improvement in this expression.
At $L=p^{1/2+\eta}$ its relative expression is
$4p^{3/4-\eta/2}/\sqrt{\log_2p}$ and grows. Thus (14) does not
prove the original FC7 power saving anywhere near its stipulated
lower length.

## Source comparison and ownership

The accessible [Roy–Steiner v1, section 5.5](https://arxiv.org/html/2204.01802v1#S5.SS5)
attributes a generic estimate
$O(N^{1/2}p^{n/2}/\sqrt{\log p})$ to the 2010
Ostafe–Pelican–Shparlinski work. With $n=2$ its reported scale
matches (14), up to constants and log base. This is verification
of what the later authors report, not of every original 2010
hypothesis or theorem. Their section 5.2 stronger moment theorem
has an explicit assumption; it is not imported here.

Classical Gauss/Weil bounds and shifted moments own the general
mechanism. Equations (4)–(10) are explicit hand specializations
for this map, not a claimed independent paper-level advance.
The [source ledger](SOURCE_AUDIT.md) records the remaining
original-body access limitation and actual retrieval scope.

## Corrections or missing assumptions

No modification of FC7 is proposed. Closing it would require a
substantive new estimate for the *actual invariant cycle* at
length $p^{1/2+\eta}$, or a genuine unbounded-prime obstruction.
Replacing the cycle by the full plane in (1) is precisely where
the presently obtained estimates lose the desired length scale.

## Open risks and verification boundary

- The full power-saving theorem and its negative direction remain open
  in this package. No global novelty clearance is claimed.
- The method boundary concerns this second-moment completion and these
  bounds, not all weighted shifts, high moments or incidence arguments.
- No mathematical code was run; no finite-prime census or old
  mathematical/build rerun was performed. The derivation is symbolic.
- Independent review is pending, not inferred from the author check.
  No contract admission, paper number, PDF, formal Route-A evaluation,
  or A2 advancement is asserted. NO_BAD_EULER_OR_ROOT_NUMBER.
