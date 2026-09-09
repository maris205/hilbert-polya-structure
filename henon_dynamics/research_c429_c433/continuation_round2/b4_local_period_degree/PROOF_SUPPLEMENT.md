# Local period, displacement, and ramification constraints

2026-09-09. Proof-only supplement to [REPORT.md](REPORT.md).

## Claim and status

**PROVABLE AS STATED:** the displacement bound, the different bound,
and the exclusion of one common finite extension for unbounded native
small periods below.

**NOT CURRENTLY JUSTIFIED:** the original bound $[L:K]\ge p^e$ for each
individual native small $p^e$-cycle. No counterexample to that bound is
constructed here. The results do exclude the more specific alternative
that all levels live in the first-level cyclic degree-$p$ field.

## Assumptions and notation

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $K=k((s))$,
$v(s)=1$, and $P=P_s=(1+s)z+z^2$. Let $\alpha$ be any root of the
accepted small factor $M_e$, so its ordinary least period is $p^e$.
Put

$$
r=\frac{p-1}{p},\qquad v(\alpha)=r,\qquad
L=K(\alpha),\qquad [L:K]=q=p^h,\quad 1\le h\le e.
$$

The accepted one-small-cycle and separability facts imply that $L$ is
the cyclic splitting field and that its Galois group acts on the
native cycle as

$$
\operatorname{Gal}(L/K)
 =\langle P^{p^{e-h}}\rangle\le\langle P\rangle=C_{p^e}.
                                                               \tag{1}
$$

Equation (1) is an equality of permutations of the root set; the
displayed generator is a field automorphism because it belongs to
the actual Galois subgroup. It does **not** assert that $P$ itself
acts as a $K$-automorphism unless $h=e$.

The integer-normalized extension valuation is $v_L=qv$, so
$v_L(s)=q$ and $v_L(\alpha)=q r=p^{h-1}(p-1)$. These extensions are
totally ramified. Indeed their residue field is still $k$, and a finite
extension of this complete discretely valued field has degree equal
to ramification index times residue degree. The rings of integers are
complete discrete valuation rings; $O_L=k[[t]]$ for a uniformizer $t$.

Write $d_L$ for the different exponent, defined by the trace-dual
fractional ideal

$$
\{x\in L:\operatorname{Tr}_{L/K}(xO_L)\subseteq O_K\}
 =\mathfrak p_L^{-d_L}.                                    \tag{2}
$$

No Artin–Schreier resolvent of $M_e$ is computed or replaced here.
The trace in (2) is used only for a local ramification inequality.

## Strategy and dependencies

1. The substitution operator minus the identity increases weighted
   Gauss valuation by at least $r$; its $p^j$-th power is the
   $p^j$-iterate operator minus the identity in characteristic $p$.
2. The exact quadratic difference identity controls how the displacement
   of one pair changes under every native iterate.
3. A trace-one ramification estimate bounds how close a nonintegral-
   valuation element can be to its Galois conjugates.
4. When $h=1$, the prime-to-$p$ valuation of $\alpha$ reads the unique
   lower break directly and gives a sharper bound.

Only the small-factor/cyclic-field setup is imported from A3.
The lower-break convention agrees with Elder–Keating, Section 2;
the displacement and trace estimates are proved below.
The stronger weighted-operator argument in Section 1 was proposed by
the coordinator and independently verified by B4 before adoption.
Section 1.1 preserves B4's earlier weaker argument as a redundant
historical derivation, not as the bound used in the final conclusions.

## 1. Growth of native displacements

For $0\le j<e$ define the finite valuation

$$
\delta_j=v(P^{p^j}(\alpha)-\alpha).
$$

Then the following exponential lower bound holds:

$$
\delta_0=2r,\qquad
\delta_j\ge(p^j+1)r\quad(0\le j<e).                       \tag{3}
$$

**Proof.** For a polynomial $Q(z)=\sum_i a_i z^i\in K[z]$,
define its weighted Gauss valuation by

$$
w_r(Q)=\min_{a_i\ne0}\{v(a_i)+ir\},\qquad w_r(0)=+\infty.
$$

Let $U$ be the $K$-linear substitution operator
$UQ=Q(P(z))$, and let $\Delta=U-I$. For every integer $i\ge1$,

$$
\Delta(z^i)=z^i\big((1+s+z)^i-1\big).
$$

Every surviving monomial in the bracket has weight at least $r$:
the constant term in the expansion in $s,z$ has canceled, and
$v(s)=1\ge r>0$ while $w_r(z)=r$. Coefficient cancellations in
characteristic $p$ can increase the weight, not decrease it. For
$i=0$ the difference is zero. Using $K$-linearity and the
non-Archimedean inequality for the finite sum gives

$$
w_r(\Delta Q)\ge w_r(Q)+r.
$$

Induction on every integer $N\ge0$ therefore gives

$$
w_r(\Delta^N z)\ge(N+1)r.
$$

The operators $U$ and $I$ commute. The binomial identity in
characteristic $p$, iterated $j$ times, yields

$$
\Delta^{p^j}=(U-I)^{p^j}=U^{p^j}-I,
\qquad
\Delta^{p^j}z=P^{p^j}(z)-z.
$$

Evaluation at $v(\alpha)=r$ satisfies $v(Q(\alpha))\ge w_r(Q)$.
Apply it to the last identity to obtain the inequality in (3).
Finally, $P(\alpha)-\alpha=s\alpha+\alpha^2$ has term valuations
$1+r>2r$, which gives the equality $\delta_0=2r$.
Ordinary least period makes all the displayed $\delta_j$ finite.
$\square$

### 1.1 Earlier weaker proof and distance preservation

The earlier argument proves the valid but weaker estimates

$$
\delta_{j+1}\ge\delta_j+r\ (0\le j<e-1),\qquad
\delta_j\ge(j+2)r.                                       \tag{3w}
$$

**Proof.** Every point of the cycle has valuation $r$, since
$P(x)=x(1+s+x)$ and $v(x)>0$. For two distinct points $x,y$ in
this cycle,

$$
P(x)-P(y)=(x-y)(1+s+x+y),\qquad v(s+x+y)\ge r.
                                                               \tag{4}
$$

The factor in (4) is a unit. Inducting on the number of native steps
shows both that $P$ preserves the distance between the two points and
that, for every integer $\ell\ge0$,

$$
\frac{P^\ell(x)-P^\ell(y)}{x-y}
 \in 1+\{u:v(u)\ge r\}.                                  \tag{5}
$$

The last assertion follows by multiplying the $\ell$ factors in (4):
the set on the right is closed under multiplication.

Fix $j<e-1$, put $u=p^j$ and
$\Delta=P^u(\alpha)-\alpha$. For $0\le a<p$, apply (5) to the
pair $P^u(\alpha),\alpha$ and to $\ell=au$. It gives

$$
P^{(a+1)u}(\alpha)-P^{au}(\alpha)
 =\Delta+\epsilon_a,\qquad v(\epsilon_a)\ge\delta_j+r.
$$

Summing these $p$ equalities yields

$$
P^{pu}(\alpha)-\alpha
 =p\Delta+\sum_{a=0}^{p-1}\epsilon_a
 =\sum_{a=0}^{p-1}\epsilon_a,
$$

and hence $\delta_{j+1}\ge\delta_j+r$. The first displacement is
$P(\alpha)-\alpha=s\alpha+\alpha^2$. Its two terms have distinct
valuations $1+r>2r$, so $\delta_0=2r$. Induction proves (3w).
All displacements in (3w) are nonzero by ordinary least period.
$\square$

## 2. Ramification cost of small conjugate displacement

**Lemma.** Let $L/K$ be a finite totally ramified Galois extension of
degree $q$ and different exponent $d_L$. If $x\in L$ has valuation
$v(x)=r\notin\mathbb Z$ and

$$
v(x-\gamma x)\ge D\quad\text{for every }\gamma\in
\operatorname{Gal}(L/K),\ \gamma\ne1,
$$

then

$$
D\le r+\frac{d_L-q+1}{q}.                                \tag{6}
$$

**Proof.** First the trace-dual definition (2) gives, for any integer $m$,

$$
\operatorname{Tr}_{L/K}(\mathfrak p_L^m)
 =\mathfrak p_K^{\lfloor(m+d_L)/q\rfloor}.                \tag{7}
$$

To verify (7), let $a$ be any integer. The containment of its left
side in $\mathfrak p_K^a$ is equivalent to
$\operatorname{Tr}(s^{-a}\mathfrak p_L^m)\subseteq O_K$.
The fractional ideal $s^{-a}\mathfrak p_L^m$ is stable under
multiplication by $O_L$, so the last containment is equivalent, by
(2), to

$$
s^{-a}\mathfrak p_L^m\subseteq\mathfrak p_L^{-d_L}
\quad\Longleftrightarrow\quad m-aq\ge-d_L.
$$

The largest allowed $a$ is $\lfloor(m+d_L)/q\rfloor$,
which proves (7). The trace ideal is nonzero because $L/K$ is
separable; the trace pairing is nondegenerate.

Taking $m=q-1-d_L$ in (7) gives a trace-one element $w$ with

$$
\operatorname{Tr}(w)=1,\qquad
v(w)\ge-\frac{d_L-q+1}{q}.                                \tag{8}
$$

Set $b=\operatorname{Tr}(wx)\in K$. Since
$\operatorname{Tr}(w)=1$ and all conjugates of $w$ have the same
valuation,

$$
x-b=\sum_\gamma\gamma(w)(x-\gamma x),\qquad
v(x-b)\ge v(w)+D.                                        \tag{9}
$$

On the other hand, $v(b)\in\mathbb Z\cup\{+\infty\}$ differs
from $r$, so $v(x-b)=\min\{r,v(b)\}\le r$. Combine this
with (8)–(9) to obtain (6). $\square$

**Application to the native root field.** Put $j=e-h$ and choose
the actual Galois generator $\tau=P^{p^j}$ from (1).
Every $\tau^a(\alpha)-\alpha$ is a sum of $a$ successive
$p^j$-step displacements. By (4) each summand has valuation
$\delta_j$, so all these conjugate differences have valuation at
least $\delta_j$. Apply (6) with $x=\alpha$, $D=\delta_j$,
and use (3). The result is

$$
d_L\ \ge\
q-1+p^{e-h}qr
 =
p^h-1+p^{e-1}(p-1).                                    \tag{10}
$$

Equivalently,

$$
p^{e-1}\le\frac{d_L-p^h+1}{p-1}.                        \tag{11}
$$

This is a necessary ramification-cost bound, not the desired bound
$h\ge e$. At a fixed degree, cyclic extensions can have unbounded
different, so (10) does not by itself produce a contradiction.

## 3. The degree-$p$ alternative has growing conductor

Suppose $h=1$. Let $b_L$ be the unique lower ramification break
of the cyclic degree-$p$ root field. Then

$$
b_L=p\,\delta_{e-1}-(p-1)\ge p^{e-1}(p-1).               \tag{12}
$$

**Proof.** Here $\tau=P^{p^{e-1}}$ is an actual generator of
$\operatorname{Gal}(L/K)$ and $v_L(\alpha)=p-1$ is prime to $p$.
The automorphism fixes $k$ pointwise. Its leading multiplier on
a uniformizer has $p$-power order in $k^\times$, so it is $1$.
Since $\tau$ is nontrivial, its first nonidentity coefficient
occurs in some degree $b_L+1\ge2$.
For a uniformizer $t$, write

$$
\tau(t)=t+c t^{b_L+1}+\text{higher terms},\qquad c\in k^\times.
$$

For an integer $a>0$ prime to $p$, the coefficient of the leading
term of $\tau(t^a)-t^a$ is $ac$ at degree $a+b_L$; it is nonzero.
If $p\mid a$, the binomial expansion instead gives valuation
strictly greater than $a+b_L$. Write
$\alpha=c_0t^{p-1}+\sum_{a>p-1}c_at^a$, with $c_0\ne0$.
The first term of its difference has valuation $(p-1)+b_L$,
and every later term has greater valuation. Thus

$$
v_L(\tau\alpha-\alpha)=(p-1)+b_L.
$$

Since $v_L=pv$, the equality in (12) follows. Its inequality is
(3) with $j=e-1$. $\square$

For the accepted first-level root field $L_1$, $e=h=1$ and
$\delta_0=2r$, so the same proof gives $b_{L_1}=p-1$.
Therefore:

$$
L_1\text{ contains no small native }p^e\text{-cycle for }e\ge2.
                                                               \tag{13}
$$

Indeed a root of such a cycle in $L_1$ would generate a degree-$p$
subfield, hence all of $L_1$, but (12) would require
$p-1\ge p^{e-1}(p-1)$. More generally a fixed degree-$p$ cyclic field
of lower break $b$ can contain such a cycle only if
$p^{e-1}(p-1)\le b$.

## 4. No common finite extension contains arbitrarily high levels

For any fixed finite extension $B/K$, there is an upper bound on the
integers $e$ for which $B$ contains a small ordinary $p^e$-cycle.

**Proof.** Every such root generates a finite separable Galois cyclic
field $L/K$ inside $B$. There are only finitely many such intermediate
fields: take the finite normal closure of the maximal separable
subextension of $B/K$ and use its finite Galois group. For each possible
$L$, its degree $p^h$ and different $d_L$ are fixed, and (11) bounds
$e$. Taking the largest of finitely many bounds proves the assertion.
$\square$

This is not a degree-uniform result: allowing $B$ to vary while keeping
its degree fixed also allows its ramification conductor to vary.

## 5. Exact remaining gap and source subtraction

The proofs establish (3), (10), (12), and (13). They do not rule out,
at some fixed higher level $e$, a degree-$p$ cyclic root field of
break at least $p^{e-1}(p-1)$, or a root field of degree $p^h$ with
$1<h<e$ and sufficiently large different.

The missing dynamical information is an obstruction to these
high-conductor proper rotation subgroups for the actual quadratic
$P_s$. One precise **sufficient**, but unproved, estimate would be

$$
d_L<p^h-1+p^{e-1}(p-1)
\quad\text{for any proposed root field with }h<e,
$$

which would contradict (10). This upper bound is not asserted to be
necessary or equivalent to the original question. Computing the
actual Artin–Schreier class is A3's separate approach; no step here
has supplied its nonvanishing.

Classical subtraction:

- The existence, uniqueness, separability, and slope of the small
  cycle are accepted A3 inputs backed by Lindahl–Rivera-Letelier,
  [Theorem C and Lemmas 2.1–2.3](https://arxiv.org/html/1311.4478v3).
  They are not new degree or Galois-transitivity statements.
- The trace-dual definition and trace ideal argument in (7) are
  elementary different theory, included in full rather than claimed
  as a new ramification theorem.
- The weighted substitution argument is elementary filtered operator
  algebra. The native-cycle consequences are recorded as auxiliary
  proof interfaces, without a claim that this general technique is new.
- Elder–Keating,
  [Lemma 2.1 and Theorem 2.3](https://arxiv.org/html/2503.16830v1),
  apply to arbitrary perfect residue fields. In particular
  $Y^p-Y=s^{-b}$ gives a cyclic degree-$p$ extension with break $b$
  for every positive $b$ prime to $p$. Thus fixed-degree cyclicity
  has no conductor upper bound. This is a control for the logical
  limitation of (12), not a constructed periodic point of $P_s$.
- Keating,
  [Theorem 6.1 and its opening proof estimates](https://arxiv.org/html/math/0312391v2),
  concern finite extensions of $\mathbb Q_p$, $p>3$, with bounded
  absolute ramification and a finite-index reduction subgroup.
  Those hypotheses do not hold here. Its characteristic-zero
  multiplier valuation increment is not available when
  $(1+s)^{p^j}-1=s^{p^j}$. No degree bound from that theorem is
  imported into equal characteristic or the excluded prime $3$.

There is no remaining unproved step in the stated auxiliary
inequalities. The original (LD) conclusion remains unproved, not
refuted. All proof work is within the frozen native clock and all
odd-prime quantifiers.
