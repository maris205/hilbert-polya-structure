# R7 E5 — full independent review of the multiplicative divisor residual

## 1. Decision, scope, and exact author version

**The new finite-divisor criterion, norm-one normalization, pure-Frobenius
boundary, sibling factorization, and the two stated controls are
PROVABLE AS STATED.** There are **zero unresolved mathematical or
source-applicability must-fixes** in these claims. No author repair was
requested by this review.

**The original MS6 existence implication remains NOT CURRENTLY JUSTIFIED.**
In particular, this review does not prove that cofinite ordinary cycle
products annihilate the finite residual, nor does either control supply
an MS6 counterexample. These auxiliary results are not a new contract,
a full MS6 PASS, or a paper admission.

I read the actual [R7 author report](../../a2_multiplicative_existence/REPORT.md)
in full, all 434 lines, at SHA256

`2cd5f0765f382180badde4ffe9f3ec20f77649be5e461a41dfe81cb8731d88b2`.

The already accepted
[R6 saturation report](../../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
was checked at the exact theorem and hypotheses used here: its frozen
question, Theorem 1, the support/ordinary-cycle convention, and §4's
constant-phase consequence. I also read the corresponding scope and
conclusions in the accepted
[E8 review](../../../continuation_round6/reviews/e8_multiplicative_saturation/REVIEW.md).
Those accepted results remain imported; this is not a fresh review of
their entire Hodge/Kummer proof or a rewriting of their frozen status.

This is an assigned current-team nonauthor mathematical review under
proof-writer/research-review and the repository workflow. Research-lit
was used for direct primary-source scope checks, with no external
model/reviewer upload. Only this exclusive review file was written.

## 2. Exact question and dependency boundary

For every prime $p$, let $k=\overline{\mathbb F}_p$. For every integer
$d\ge2$, $c\in k$, and $g\in k(x)^\times$, put
$f=x^d+c$ and $\delta h=h\circ f/h$. Condition (CP) says that all
but finitely many ordinary primitive native $f$-cycles avoid the zeros
and poles of $g$ and have product one. Periods divisible by $p$ are
not discarded. Passing to $\mathbb P^1$ for divisors adds only the
single fixed cycle at infinity and does not change a cofinite condition.

The unchanged MS6 question asks whether (CP) implies
$g^{p^e}=\delta h$ for some $e\ge0$ and rational $h\ne0$.
R6 Theorem 1 already proves

$$
(\mathrm{CP})\ \text{and}\ g^m=\delta a
\quad\Longrightarrow\quad
g^{p^{v_p(m)}}=\delta b.
$$

Its additional integer-power existence premise is essential. The R7
criterion decides that premise from a divisor residual; it does not
show that (CP) makes the residual vanish.

The new dependency chain is correct:

1. A finite rational divisor $E_D$ is obtained from the forward action
   on $D=\operatorname{div}(g)$.
2. Its residual $\mathcal R_f(D)$ is fiber-balanced, and its vanishing
   is equivalent to torsion of $[g]$ in the multiplicative quotient.
3. A power and a genuine rational coboundary normalize a (CP) function
   to a norm-one function with divisor proportional to that residual.
4. Injectivity of geometric pushforward settles the pure-Frobenius
   boundary; a prime-to-$p$ exponent permits the precise R6 conclusion.
5. For the remaining degrees, sibling Hilbert 90 does not by itself
   give a native coboundary or the missing periodic-data implication.

## 3. Pushforward, pullback, and finite rationality: PASS

Write $P=f_*$ on finite rational divisors with
$P[a]=[f(a)]$, and $A=f^*$. Divisor coefficients and their
$\ell^1$ norm are rational/real numbers. In particular, $d^{-1}$,
orders of zeros, and local degrees are not field scalars modulo $p$.

The estimate $\|PU\|_1\le\|U\|_1$ is valid even when distinct
points collide, since collision only adds coefficients before taking
absolute values. For $d=qs$ with $q=p^{v_p(d)}$ and $p\nmid s$,
a fiber over $b\ne c$ has $s$ distinct geometric points each of
local degree $q$. The fiber over $c$ is $0$ with degree $d$, and
infinity also has local degree $d$. The geometric residue fields are
all $k$, so their residue-field degrees are one. Consequently

$$PA=dI$$

uses the **total** degree, including the inseparable factor. It is not
the generally false equality $AP=dI$.

A finite field contains $c$ and all finite support points of $D$.
The polynomial preserves this field and fixes infinity. Thus the full
forward closure $S$ of the support is finite, with $f(S)\subset S$.
This step genuinely uses $k=\overline{\mathbb F}_p$; no corresponding
finite-support assertion over an arbitrary algebraically closed field
is being silently assumed.

On $\mathbb Q^S$, each column of $P$ has one entry equal to one.
The series

$$E_D=\sum_{n\ge1}d^{-n}P^nD$$

converges absolutely in the finite-dimensional space $\mathbb R^S$,
with norm at most $\|D\|_1/(d-1)$. Every summand has degree zero.
Shifting the series gives

$$ (dI-P)E_D=PD. $$

If $PU=dU$, the norm inequality and $d>1$ force $U=0$.
Thus the square rational matrix $dI-P$ is invertible over $\mathbb Q$,
so the limiting vector has rational coefficients. This proves finite
support, actual rationality, and degree zero; convergence alone would
not have proved rationality.

The calculation

$$P\mathcal R_f(D)=P(AE_D-E_D-D)=dE_D-PE_D-PD=0$$

is valid. The residual is supported on $S\cup f^{-1}(S)$ and has
coefficient $e_f(a)(E_D)_{f(a)}-(E_D)_a-D_a$ at $a$.
Fiber-balanced means the sum of these coefficients over each fiber
vanishes, not that each coefficient vanishes.

## 4. Uniqueness and exact torsion criterion: PASS

Suppose a finite rational divisor $U$, with unrestricted initial
support, solves $(A-I)U=D$. Pushing forward and iterating gives

$$
U=\sum_{j=1}^n d^{-j}P^jD+d^{-n}P^nU.
$$

The remainder has norm at most $d^{-n}\|U\|_1$ and tends to zero.
The partial sum tends to the already constructed finite vector $E_D$.
Hence $U=E_D$. No restriction of a hypothetical solution's support
to $S$ is imposed in advance, and no completeness assertion about the
space of all finite divisors is needed.

If $g^m=\delta h$ for any positive integer $m$, the rational divisor
$m^{-1}\operatorname{div}(h)$ solves this equation. Thus the residual
vanishes. This covers $m$ divisible by $p$ because divisor orders are
integers, not elements of the coefficient field.

Conversely, if the residual vanishes, choose $M>0$ clearing the
denominators of $E_D$. Its integral degree-zero multiple is principal
on $\mathbb P^1_k$. The explicit product
$h=\prod_{a\ne\infty}(x-a)^{M(E_D)_a}$ has exactly that divisor,
including the correct coefficient at infinity. Then

$$\operatorname{div}(g^M/\delta h)=0,$$

so $g^M/\delta h=\eta\in k^\times$. This constant is not simply
discarded: it belongs to a finite field and has some finite order $t$.
Therefore $g^{Mt}=\delta(h^t)$.

Theorem 3.1's equivalence between residual zero and torsion is therefore
proved without (CP). The extra constant phase is indispensable for that
unconditional statement. For $D=0$, the construction gives $E_D=0$,
and the result correctly says that every nonzero constant has torsion
class over this particular constant field.

## 5. Explicit denominator and function-degree bound: PASS

The functional graph on $S$ consists of finite trees entering directed
cycles. Let $T$ count all nonperiodic vertices and let the cycle lengths
be $r_1,\ldots,r_b$. Modulo the cycle subspace the pushforward is
nilpotent; each cycle contributes the characteristic polynomial
$Z^{r_i}-1$. Consequently

$$
M=\det(dI-P)=d^T\prod_{i=1}^b(d^{r_i}-1)>0.
$$

Here $T$ is a number of vertices, not a maximum preperiod. Since $PD$
is integral, the integer adjugate of $dI-P$ shows that this $M$ clears
the denominators of $E_D$. The empty-support convention $M=1$ for
$D=0$ is consistent.

For a rational function, its rational-map degree is half the
$\ell^1$ norm of its principal divisor, with both sides zero for a
constant. Therefore the specific function with divisor $ME_D$ satisfies

$$H(h)=\tfrac12 M\|E_D\|_1\le \frac{M H(g)}{d-1}.$$

This bounds $h$ **before** the additional constant-killing power $t$.
The report explicitly retains that distinction. These bounds use the
actual finite forward graph and make no runtime claim or assertion
that (CP) passes the residual test.

## 6. The inseparable norm and (CP)-preserving normalization: PASS

Use $t=f(x)$ to identify the target field. The polynomial
$X^d+c-t$ is Eisenstein at $t-c$ in $k[t][X]$, so is the monic
minimal polynomial of $x$ over $k(t)$, of full degree $d$, even if
inseparable. The determinant norm gives

$$
N_f(x-a)=(-1)^d(a^d+c-t)=(-1)^{d+1}(t-f(a)),
\qquad N_f(\alpha)=\alpha^d.
$$

The sign and the exponent on a constant are correct. Factoring a
nonzero rational function into constants and integral powers of linear
factors then gives
$\operatorname{div}(N_fu)=P\operatorname{div}(u)$; the infinity
coefficient is fixed by degree. The proof does not treat the norm as
a product over only the distinct embeddings of an inseparable extension.

Choose $M,h$ without presupposing residual zero and set
$v=g^M/\delta h$. Its divisor is $-M\mathcal R_f(D)$.
Pushing this divisor forward makes $N_fv$ a nonzero constant $\eta$.
If $\nu$ is its finite order, then $w=v^\nu$ has

$$N_fw=1,\qquad \operatorname{div}(w)=-M\nu\mathcal R_f(D).$$

Only finitely many ordinary cycles meet the support of $h$.
Outside those and the original finite (CP) exceptions, every transfer
value used is finite and nonzero, and the products of $\delta h$
genuinely telescope. Hence $v$ and $w$ retain (CP). No evaluation of
an uncancelled zero/pole of $h$ is slipped into this argument.

Since $M\nu$ is a positive integer, $w$ is constant exactly when the
residual is zero, hence exactly when $[g]$ is torsion.
Conversely, for any norm-one $w$, writing $D_w=\operatorname{div}(w)$
gives $PD_w=0$, $E_{D_w}=0$, and $\mathcal R_f(D_w)=-D_w$.
Thus a norm-one function can have torsion class only if it is constant.

R6 Corollary 4.3 applies to this same full parameter range and same
cofinite ordinary-cycle condition: a constant satisfying (CP) is one.
It follows that the proposed all-parameter assertion

$$N_fw=1\ \text{and (CP)}\quad\Longrightarrow\quad w=1$$

is indeed equivalent to the remaining (CP)-to-residual-zero bridge.
No step above proves that assertion for general $d$.

## 7. Complete pure-Frobenius boundary and R6 compatibility: PASS

If $d=q=p^r$, $r\ge1$, then $x\mapsto x^q+c$ is a bijection on
$\mathbb P^1(k)$. Pushforward is injective on finite divisors, so
$P\mathcal R_f(D)=0$ forces $\mathcal R_f(D)=0$. Every class is
therefore torsion in this subtype, even without (CP).

The stronger explicit argument credited to the coordinator is valid.
Choose $\beta^q+c=\beta$ and set $x=z+\beta$; the map becomes
$z\mapsto z^q$. All coefficients of $\widetilde g(z)=g(z+\beta)$
belong to some $\mathbb F_{q^s}$. With the coefficient-fixing
substitution $\sigma_0 a(z)=a(z^q)$ and
$\delta_0a=\sigma_0a/a$, one obtains

$$
\sigma_0^s\widetilde g=\widetilde g^{q^s},\qquad
\delta_0\left(\prod_{j=0}^{s-1}\sigma_0^j\widetilde g\right)
=\widetilde g^{q^s-1}.
$$

The first identity uses that $q^s$ fixes **all coefficients**; it would
be unjustified for an arbitrary coefficient-fixing substitution without
that finite-field choice. Translation back gives a rational transfer
for the original native map. The finite product converts the iterate
identity into a one-step coboundary, so no alternate native clock is used.

The exhibited exponent $m=q^s-1$ is prime to $p$. Under (CP), R6
Theorem 1 therefore gives $g=\delta h$ itself, because $v_p(m)=0$.
This includes $m=1$. The converse is ordinary telescoping after finitely
many support exceptions. Thus the entire stated pure-Frobenius subtype
is closed, with all $c,g$ retained. This does not include degrees
whose prime-to-$p$ part exceeds one, whether mixed or separable.

## 8. Sibling norm, Kummer direction, and Hilbert 90: PASS

For $d=qs$, the pullback of the field norm satisfies

$$ (N_fw)(f(x))=\left(\prod_{\zeta\in\mu_s(k)}w(\zeta x)\right)^q.$$

On a factor $x-a$, the product before taking the $q$th power is
$(-1)^{s+1}(x^s-a^s)$. Its sign after that power agrees with
$(-1)^{d+1}$: $q$ is odd in odd characteristic, while signs coincide
in characteristic two. Constants and negative exponents also match.
Since a field of characteristic $p$ has no nontrivial $q$th root of
one, norm one implies the exact sibling-product identity (6.1).

For $s>1$, the applicable cyclic action is
$\tau a(x)=a(\zeta x)$ for a primitive $s$th root $\zeta$.
It is the separable degree-$s$ Kummer action for
$k(x)/k(x^s)$, not the generally inseparable full extension of
degree $d$ and not the native substitution $a\mapsto a(f(x))$.

The explicit Hilbert 90 proof has the correct orientation. With
$b_i=\prod_{j=0}^{i-1}\tau^jw$ and $b_s=1$,
$\tau b_i=b_{i+1}/w$. Therefore

$$
\tau\left(\sum_{i=0}^{s-1}b_i^{-1}\tau^ia\right)
=w\sum_{i=0}^{s-1}b_i^{-1}\tau^ia.
$$

For $a=x^j$, division by the nonzero $x^j$ leaves the Fourier matrix
$(\zeta^{ij})$. Its nodes $1,\zeta,\ldots,\zeta^{s-1}$ are distinct,
so its Vandermonde determinant is nonzero. Hence some listed $a$ gives a nonzero
$v$, proving $w=\tau v/v$, not its inverse. For $s=1$, the sibling
product already gives $w=1$.

The identity $f(\zeta x)=f(x)$ identifies points in one fiber.
It does not identify $\zeta x$ with the next native iterate $f(x)$.
Thus the sibling coboundary is not entitled to telescope around native
cycles. The report preserves this unresolved distinction.

## 9. Both negative controls and their exact scope: PASS

### 9.1 Characteristic five: infinitely many bad primitive cycles

For $f=x^2$ and $w=(x-1)/(x+1)$ over $\overline{\mathbb F}_5$,
the numerator and denominator have the same norm, so $N_fw=1$.
Their divisor pushes to $[1]-[1]=0$ but is nonzero.
At the fixed point $1$, the local degree of $f$ is one, giving
$\operatorname{ord}_1(\delta h)=0$ for every rational $h$.
The order of $w^m$ there is the integer $m>0$, including when
$5\mid m$. Thus no positive integer-power transfer exists.

The failure of (CP) is not inferred from this single exceptional point.
For a prime integer $n\equiv3\pmod4$, put $L=2^n-1$.
In characteristic five, $L=2\ne0$. The roots of
$Q=(X^L-1)/(X-1)$ are distinct, avoid $0,\pm1$, and have exact
native period $n$: their period divides the prime $n$, and the only
nonzero fixed point is the removed point $1$.

The monic quotient has $Q(1)=L$ and $Q(-1)=1$, so the product of
$w$ over all its roots is $2$, not one. Hence at least one primitive
$n$-cycle has nontrivial product. There are infinitely many primes
congruent to three modulo four: the stated $4\prod n_i-1$ argument
forces a new such prime if the list were finite. Distinct prime
periods yield distinct bad cycles. This establishes failure of (CP),
not a counterexample to MS6.

### 9.2 Characteristic three: aggregate products lose cycle information

The six nontrivial seventh roots split into the two squaring cycles
with exponent sets $\{1,2,4\}$ and $\{3,6,5\}$, each of period
three. Each denominator product $\prod(a+1)$ is one by telescoping
$a+1=(a^2-1)/(a-1)$ along that actual cycle.

Choose a primitive seventh root $\xi$ and let
$U=(\xi-1)(\xi^2-1)(\xi^4-1)$. The other cycle is the set
of reciprocals of the first, so its numerator product is
$(-1)^3U/\xi^{1+2+4}=-U$. The aggregate quotient product is
$7=1$ in characteristic three. Hence $-U^2=1$, or $U^2=2$;
neither $U$ nor $-U$ is one. The two individual cycle products are
nontrivial although the merged product is one.

This verifies the stated finite information-loss example. No cofinite
conclusion in characteristic three, or MS6 counterexample, follows from
this six-point illustration, and the report does not claim one.

## 10. Actual primary-source scope and subtraction

The algebraic norm, principal-divisor construction, finite functional
graph calculation, and cyclic Hilbert 90 argument were directly checked
above. They are elementary/classical tools, not an independently novel
theory. The explicit pure-Frobenius exponent remains credited to the
coordinator; R6 saturation and the constant-phase result remain imported.

Two named primary sources were independently read at the relevant passages:

- Chyzak–Dreyfus–Dumas–Mezzarobba,
  [*Computing solutions of linear Mahler equations*, arXiv:1612.05518v2](https://arxiv.org/pdf/1612.05518v2):
  §1.3 specifies a computable subfield of $\mathbb C$. I read §3.5,
  Proposition 3.22, Algorithm 9, and its displayed proof through the
  complexity conclusion. The input is a specified Mahler equation;
  the output is its rational-solution space, which may be zero. The
  native substitution here is instead $x^d+c$, and the field is positive
  characteristic. No applicable theorem producing a nonzero transfer
  from (CP) is supplied by those passages. This is a scope/subtraction
  check, not execution of the algorithm or a re-audit of all its earlier
  subroutine proofs.

- Faverjon–Poulet,
  [*Computing basis of solutions of any Mahler equation*, arXiv:2511.18877v1](https://arxiv.org/pdf/2511.18877v1),
  November 2025 preprint: I read the introduction, the formal-extension
  discussion and complete Theorem 1 statement. The algorithmic theorem
  assumes an effective characteristic-zero field and describes solutions
  using Puiseux/Hahn and additional formal factors. Its symbol $p$ for
  the Mahler radix is an integer at least two, not an assumption that
  the coefficient field has characteristic $p$. General formal solution
  existence does not construct the finite algebraic transfer needed in
  MS6. Neither the theorem's full proof nor a positive-characteristic
  existence theorem is imported by this review.

These source claims match the author's stated boundaries. No exact
priority conclusion or full novelty search is claimed. The old R6
source review was not silently substituted for these new direct reads.

The active tool list had no Zotero/Obsidian interface. A local filename
filter found no matching primary Mahler paper or arXiv fetch script;
the one distinct divisor-named local PDF was screened through its first
three pages and concerns a different finite integer-divisor system, so
was not used as an MS6 source. Duplicate versions were not reread.
Primary web access supplied the named papers. No source PDF was saved
or modified, and no source algorithm was run.

## 11. Final issue ledger and execution boundary

| Reviewed item | Final result |
| --- | --- |
| Finite support, rationality, $dI-P$ invertibility, unrestricted-support uniqueness | PASS |
| Residual in $\ker P$ and exact torsion equivalence, including constants | PASS |
| Explicit determinant denominator and the correctly scoped function-degree bound | PASS |
| Full-degree inseparable norm, signs, and (CP)-preserving normalization | PASS |
| Pure-Frobenius all-parameter boundary and exact invocation of R6 | PASS |
| Sibling Kummer/Hilbert 90 orientation and distinction from native time | PASS |
| Infinite characteristic-five bad cycles and finite characteristic-three aggregate control | PASS |
| New mathematical/source-applicability must-fixes | Zero unresolved; no author revision required |
| General (CP) $\Rightarrow\mathcal R_f(D)=0$, equivalently norm-one (CP) $\Rightarrow w=1$ | NOT CURRENTLY JUSTIFIED |

The final author hash was checked against the actual file and remains
the identity recorded in §1. Hash verification binds this review to
specific bytes; it is not the mathematical evidence for its conclusions.

Verification consisted of independent hand divisor, norm, field,
finite-graph, and cycle-product calculations, actual file reads, and the
specified primary-source passages. There was no mathematical execution,
new/nested agent, external model/API, Git operation, author/old/shared-file
edit, manuscript/PDF build, formal evaluation, or admission write.
Only this review was created. The unresolved MS6 bridge and
`NO_BAD_EULER_OR_ROOT_NUMBER` remain unchanged.
