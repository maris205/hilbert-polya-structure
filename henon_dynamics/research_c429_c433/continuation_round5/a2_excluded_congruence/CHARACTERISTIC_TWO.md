# Characteristic two and the complete prime/degree boundary

2026-09-10 UTC. Same PC424-L contract; separately allocated parameter
addendum. No frozen proof or report is changed.

## Claim and status

**PROVABLE AS STATED — author addendum complete; its targeted nonauthor
review is pending.** The earlier E8 review certifies the original odd-
characteristic R5 statement, not this new parameter domain by itself.

Let $k=\overline{\mathbf F}_2$, let $d\ge2$ be any integer,
and let $c\in k$. Put

$$f(x)=x^d+c,\qquad \Delta Q=Q\circ f-Q,\qquad
B_f=\Delta k[x],$$

$$K_f=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\}.$$

Write $S_h(O)=\sum_{a\in O}h(a)$. Then $K_f=B_f$.
All coefficients of $h,Q,c$ lie in $k$, with
no restriction to $\mathbf F_2$. Every distinct point of an ordinary
primitive orbit is counted once; periods divisible by two are included.
One application of $f$ is the native time step throughout.

For $j\ge1$ write

$$F_j=f^{\circ j}-x,\qquad
\widetilde H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.$$

For an integer $M\ge1$ and every $h$ of degree at most $M$,
including zero, the following are exact finite certificates:

| Degree | Two return levels | Equivalent polynomial divisibilities |
| --- | --- | --- |
| Odd $d$ | $n=7\lfloor\log_d(PM)\rfloor+22$ and $n+1$, where $P=2^{v_2(d-1)}$ | $F_j\mid D^{[P]}F_j\,\widetilde H_j(h)^P$ at both levels |
| Even $d$ | $n=3\lfloor\log_d M\rfloor+4$ and $n+1$ | $F_j\mid\widetilde H_j(h)$ at both levels |

In each row the two divisibilities, membership in $B_f$, and
ordinary-root vanishing of $\widetilde H_j(h)$ at both specified
levels are equivalent. Here $D^{[P]}$ is the Hasse derivative,
defined by the coefficient of $z^P$ in evaluation at $x+z$.
The corresponding detecting primitive-period bounds are $n+1$.
The iterate-degree bounds are respectively $d^{23}(PM)^7$ and
$d^5M^3$; no optimized algorithmic complexity is claimed.

## Frozen dependencies and proof strategy

The following actual proofs were read; this addendum does not silently
extend the hypotheses of their theorem statements:

- [R4 degree-$d$ proof](../../continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md),
  originally stated for odd $p$ and $d\not\equiv1\pmod p$;
  SHA256 `766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01`.
- [R5 Hasse-carry proof](PROOF_PACKAGE.md), originally stated for odd
  $p$ and $d\equiv1\pmod p$; 517 lines;
  SHA256 `b703fde520e5405b6ab28833a40dcce324925bebbbeaefea6b9ca22de57445e3`.
- The [E8 R5 review](../reviews/e8_excluded_congruence/REVIEW.md)
  passes that original parameter domain. Its existence does not replace
  the new-domain checks below.

The strategy is to recheck every characteristic-sensitive condition of
the existing proofs, then import their explicitly identified algebraic
lemmas with the conditions now verified in characteristic two. The
marked-carry proof is not duplicated in full.

| Dependency | Actual condition used | Characteristic-two verification |
| --- | --- | --- |
| R4 §§1–2; R5 §1: normal form and full digit basis | Monic degree $d\ge2$ and reductions $X_i^d=X_{i+1}-c$ | Integer degree decreases and dimension $d^j$ are unchanged; no division by two |
| R5 §§2–3: Hasse certificate and one marked site | $P$ is a characteristic power, $1<P<d$, and $\alpha=(d-1)/P\bmod p\ne0$ | For odd $d$, $P\ge2$, $P<d$, and $\alpha=1$ |
| R5 §§4–5: target and adaptive-cut overflow exclusion | $d-P+1<d$ and target cut digit $d-1>1$ | $P\ge2$ and $d\ge3$ suffice |
| R5 §§6–7: localization and fixed cut | $P<d$, integer carry inequalities, and a sufficiently long source-free block | All are independent of field parity |
| R5 §§8–10: insertion, leading isolation, constants | Weight-one transitions, nonnegative integer losses, and adjacent return levels | No sign distinction or nonzero factor two is used; one of two adjacent integers is odd |
| R4 §§3,8–9: derivative-zero branch | $p\mid d$, squarefree $F_j$, and $j>2\lfloor\log_d D\rfloor$ | For even $d$, $F_j'=1$; the leading-digit proof and adjacent-level constant test are rechecked in §3 below |

## 1. Common normalization, zero input, and ordinary cycles

For every $d\ge2$, including even $d$ in characteristic two,
the polynomial $\Delta x^r$ is monic of degree $dr$ for
$r\ge1$. Triangular elimination gives the unique normal part

$$h=\Delta Q+v,\qquad
v\in V_d:=k\oplus\bigoplus_{r\ge1,\ d\nmid r}kx^r,
\qquad \deg v\le\deg h\quad(h\ne0).\tag{1}$$

A nonconstant coboundary has leading degree divisible by $d$, and
a nonzero constant is not a coboundary. Thus the decomposition is
direct. For $h=0$, take $Q=v=0$; no logarithm of degree zero
will be taken. All logarithms in the finite statements use $M\ge1$.

The full cyclic algebra

$$\mathcal A_j=k[X_0,\ldots,X_{j-1}]/(X_i^d+c-X_{i+1})
\simeq k[x]/(F_j)$$

uses indices modulo $j$. Set $H_j(w)=\sum_{i=0}^{j-1}w(X_i)$.
It has its degree-$d$ digit basis in characteristic two. Replacing
$X_i^d$ by $X_{i+1}-c$ decreases total degree, and the $d^j$
resulting digit monomials match its dimension. Telescoping gives
$H_j(\Delta Q)=0$ in this full algebra, without any reducedness
assumption.

An ordinary root of $F_j$ has a primitive period $r\mid j$,
and

$$\widetilde H_j(h)(a)=(j/r)S_h(O_a).\tag{2}$$

This is repetition of a finite sum, not division by $r$ in $k$.
It remains valid when $r$ or $j/r$ is even. In particular,
$h\in K_f$ implies ordinary-root vanishing at every level.
Polynomial coboundaries always have zero ordinary sums by telescoping.

## 2. Odd degree: complete parity audit of the Hasse proof

Assume $d$ is odd. It is at least three. Define

$$P=2^{v_2(d-1)},\qquad A=(d-1)/P.$$

When excluding a positive normal part, let its leading degree be
$D\le M$ and its leading coefficient be $a_D\ne0$.
Then $P\ge2$, $A$ is odd, $d=PA+1$, $P<d$, and
$\gcd(P,d)=1$. Hence every normal positive exponent remains normal
under $r\mapsto Pr$, and
$H_j(v)^P=H_j(v^P)$ with the coefficients of $v$ also raised
to their $P$th powers. No coefficient is presumed fixed by Frobenius.

### 2.1. Hasse differentiation and the marked backgrounds

For a nonzero polynomial $G$ and an integer $E\ge1$, the
multiplicity argument of R5 §2 uses only the inequality

$$\operatorname{ord}_a(D^{[E]}G)\ge
\max(\operatorname{ord}_aG-E,0).$$

Thus ordinary-root vanishing of $H$ implies
$G\mid D^{[E]}G\,H^E$ in characteristic two as well, without
a bound on any root multiplicity. For the chosen $P$,

$$f(x+z)=(x+z)(x^P+z^P)^A+c,\qquad
f'(x)=x^{d-1},\qquad D^{[P]}f(x)=x^{d-P}.\tag{3}$$

The absent Taylor orders $2,\ldots,P-1$ give the same one-mark
composition formula. When $P=2$, this interval is empty. If
$g(x+z)=g(x)+a(x)z+b(x)z^2+O(z^3)$, the coefficient-of-$z^2$
composition formula is still
$f'(g)b+D^{[2]}f(g)a^2$. There is no additional term.

Consequently R5 formula (8) holds with $\alpha=1$:

$$[D^{[P]}F_j]=\sum_{t=0}^{j-1}
\left(\prod_{i<t}X_i^{P(d-1)}\right)X_t^{d-P}
\left(\prod_{i>t}X_i^{d-1}\right).\tag{4}$$

The numbers $P(d-1),d-P,d-1$ in (4) are integer exponents.
They are not scalar coefficients to be reduced modulo two.

### 2.2. All cut, localization, and insertion requirements

Use the R5 choices $m=\lfloor\log_d(PM)\rfloor$, $L=m+2$,
$s\ge4L+4$, and $j\ge s+3L+4$. Its target has anchor digit
$d-P+1$, a long block of $d-1$, the digits of $PD-1$, and
a zero block. Since $P\ge2$,

$$d-P+1<d,\qquad d-1\ge2>1.\tag{5}$$

These replace precisely the stronger lower bounds $P\ge3$ and
$d-1\ge3$ used in the odd-characteristic wording. For a positive
normal leading degree $D$, coprimality gives

$$d\nmid PD,\qquad (PD-1)\bmod d\le d-2,\tag{6}$$

so the required first digit smaller than the long-block digit remains.

The adaptive-cut estimate in R5 §5 is the integer inequality
$t\le P+(Pr-1)/d^h$. It still makes the last cut exponent at
most $d$. An overflowing cut sends at most a unit carry around the
already reduced digit string and leaves its cut digit at most one.
By (5), this cannot produce the target cut digit $d-1$.
Legal branches retain the exact cyclic quotient and binomial weight.

For R5 §6, the baseline is $P-1$ before or at the mark and
zero after it. The excess equation is

$$e_a=d-1+u_a+Pr\mathbf1_{a=i}-du_{a+1}-d\kappa_a,
\qquad \kappa_a\ge0.$$

Without a source, $u_a\le0$ forces the integer $u_{a+1}\le0$.
Because $P<d$, among carries from zero to $P$ a digit $d-1$
forces the low baseline, whereas a zero digit requires one more.
All source localization and source-free exclusions therefore retain
their original inequalities. The common cut at zero then has final
digit at most $d-P+1<d$ and still imposes $t_0=t_j=1$.

The insertion/deletion in R5 §8 adds a transition of weight one.
Its proof does not require $-c$ and $c$ to differ: every old
binomial weight is preserved, including a weight that is zero in
characteristic two. With $N=j+1$ and $S=s+1$, R5 §9 isolates
the new marked contribution by the integer equality

$$Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1},
\qquad r\le D,\ i\le S.$$

Its nonnegative losses still force $i=S$, $r=D$, and all
$\kappa_u=0$. The unique surviving weight is one. Thus the exact
coefficient identity becomes, with $C(j,s)$ denoting the specified
target coefficient of $[D^{[P]}F_j]H_j(v^P)$ as in R5 §§4 and 8,

$$C(j+1,s+1)-C(j,s)=a_D^P\ne0.\tag{7}$$

Subtraction in (7) is valid in characteristic two; neither a division
by two nor cancellation of a nonzero scalar two occurs.

### 2.3. The smallest boundary and the finite conclusion

For $d=3$ and $P=2$, the marked backgrounds in (4) are
$4,1,2$. The anchor digit is $d-P+1=2$, equal to the long-block
digit $d-1=2$. No step of the proof requires these two digits
to be unequal. Adaptive cuts lie in the long block, where the
required digit two is still greater than every overflowing outcome
zero or one. At the fixed cut, $d-P+1=2<3$ still prevents
overflow. The first post-block digit is
$(2D-1)\bmod3\le1$ whenever $3\nmid D$, retaining the
only strict digit comparison used for leading-source isolation.

At the two prescribed levels, the Hasse divisibilities make both
coefficients in (7) zero. A positive normal part is impossible.
For a constant normal part $a_0$, one of the levels $j$ is odd.
The leading term of $D^{[P]}F_j$ is
$j x^{d^j-P}=x^{d^j-P}$, nonzero and of degree below $\deg F_j$.
The remaining divisibility
$F_j\mid j a_0^P D^{[P]}F_j$ therefore forces $a_0=0$.
Together with (1)--(4) and telescoping, this proves every equivalence
in the odd-degree row, with exactly its stated bounds.

## 3. Even degree: rechecked derivative-zero proof and bound

The R4 theorem statement assumed an odd prime. We do not apply that
statement directly to characteristic two. Instead, its §§1–3 and
§§8–9 proof ingredients have the following verified hypotheses here.

For even $d$, $f'=0$ in $k[x]$. The chain rule gives

$$F_j'=(f^{\circ j})'-1=-1=1\qquad(j\ge1).\tag{8}$$

Every $F_j$ is therefore squarefree. Ordinary-root vanishing is
equivalent to $F_j\mid\widetilde H_j(h)$, or to
$H_j(h)=0$ in the full cyclic algebra.

The R4 leading-digit detector does not use an odd characteristic.
For a positive normal degree $D$ with leading coefficient $a_D\ne0$,
let $q=\lfloor\log_d D\rfloor$
and write $D=\sum_{a=0}^q e_ad^a$. Normality and positivity give
$e_0>0$ and $e_q>0$. For $j>2q$, reduce each $X_i^r$,
$r\le D$, in its forward window of $q+1$ variables using the
integer weights $1,d,\ldots,d^q$. Choosing the next variable in
$X_i^d=X_{i+1}-c$ preserves weight, and choosing the constant
strictly decreases it. No reduction leaves the window, since
$r\le D<d^{q+1}$. Its unique
no-constant branch is the base-$d$ digit monomial with coefficient one.

Only the window starting at zero can contain both target endpoints
$0,q$, because the opposite forward distance is $j-q>q$.
For $q=0$ the window is a singleton. Thus only the leading term
at source zero reaches the target of weight $D$, and

$$\left[\prod_{a=0}^qX_a^{e_a}\right]H_j(v)=a_D\ne0.\tag{9}$$

This proof uses integer weights and a unique coefficient one, so
characteristic-two cancellations cannot remove the displayed coefficient.

Now put $m_0=\lfloor\log_d M\rfloor$ and $n=3m_0+4$.
If the two divisibilities of the even-degree row hold, normalizing
by (1) gives $H_n(v)=H_{n+1}(v)=0$. Any positive degree
$D\le M$ contradicts (9), since both levels exceed $2m_0$.
For constant $v=a_0$, these equations are $na_0=0$ and
$(n+1)a_0=0$. One of these two integers is odd, so $a_0=0$.
The reverse implications follow from telescoping and (8).

If $h\in K_f$, equation (2) supplies the required root vanishing,
proving $K_f=B_f$ also for even $d$. If a polynomial is not a
coboundary, failure of a finite root test gives a primitive orbit
with nonzero sum by (2), without dividing by its period. Finally,
$d^{n+1}=d^{3m_0+5}\le d^5M^3$, exactly the stated even-degree
bound. The logarithms were used only for positive degree or the
positive cap $M$; zero input and constants were handled separately.

## 4. Combined boundary for every prime

Combining this addendum with the reviewed R4 and odd-characteristic
R5 proofs gives the single mathematical conclusion

$$\boxed{\text{For every prime }p,\ d\ge2,\ c\in\overline{\mathbf F}_p,
\quad K_{x^d+c}=\Delta\overline{\mathbf F}_p[x].}$$

The proof coverage is disjoint and exhaustive:

| Parameter range | Mathematical dependency | Certificate type |
| --- | --- | --- |
| $p\nmid d(d-1)$ | Reviewed R4 carry branch; this range has no $p=2$ instance | Two ordinary Jacobian tests, $n=3\lfloor\log_dM\rfloor+4$ |
| $p\mid d$ | Reviewed R4 for odd $p$; §3 above for $p=2$ | Squarefree return tests at that same $n,n+1$ |
| $p\mid d-1$ | Reviewed R5 for odd $p$; §2 above for $p=2$ | Two Hasse tests, $n=7\lfloor\log_d(PM)\rfloor+22$ |

All statements concern the complete ordinary periodic data, including
wild primitive periods; the finite tests use full return sums at
ordinary roots, not only primitive orbits of exact return length.
They neither replace the native clock with Frobenius nor assert that
every ordinary-root test at a single level detects every obstruction.

This is one same-PC424-L parameter completion and its finite
certificates, not another contract or independent paper. No novelty,
target-arithmetic advancement, or new formal admission is claimed here.

## Verification and remaining review gate

The proof-writer skill was used to retain the exact characteristic-two
claim and make every removed oddness condition explicit. This addendum
uses only the identified frozen proofs and the hand checks displayed
above. No mathematical program, new agent, external model, Git operation,
or old/shared-file edit was performed. The 517-line R5 proof and
203-line report retain their previous hashes. The remaining gate is
E8's separately allocated targeted review of this new parameter domain.
