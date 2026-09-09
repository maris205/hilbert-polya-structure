# E8 complete mathematical review: finite ordinary CP for $f'=0$

2026-09-10 UTC. Nonauthor internal review under proof-writer,
research-review and the repository batch workflow. This is verification
of the supplied complete proof, not blind reconstruction or a claim of
independent origination of its shared high-level sketch.

## 1. Exact version, decision and scope

The reviewer read all 708 lines of the actual
[A3 author report](../../a3_inseparable_finite_cp/REPORT.md), initially
at SHA256
`d8388154703b8eec0f01992814d20858f712cea2c9adc218fa076ab05b0e85ed`.
The final version has 713 lines and SHA256
`34a773edfce1e02e3dbe39f967888d4e49ba50d1384040f07d350c1e79779f1c`.

The coordinator requested one provenance-only insertion, now at lines
675--679. The reviewer actually read it and the surrounding final
section. Removing exactly those five lines in a read-only stream
reproduced the original 708-line SHA256 above. Thus the reviewed
mathematical body is byte-identical, and the added disclosure was
separately checked. No author file was edited by E8.

**Theorem 1.1 and the frozen finite bound are PROVABLE AS STATED.**
Mathematical must-fixes: **0**. Imported-result applicability
must-fixes: **0**. Outstanding required textual/provenance repairs:
**0**. No counterexample or mathematical gap was found in the full
quantified statement. No weakening of the question or bound is needed.

The positive decision covers all prime characteristics, all polynomials
of the stated degree with derivative zero, every allowed rational
observable, and all ordinary native periods. It is a complete decision
theorem at that scope, not just a necessary finite test.

It does not prove a rational or algebraic transfer existence theorem,
with or without a fixed $p$-power, nor any assertion for general
polynomials with nonzero derivative. Source novelty, independent
substantiality and paper admission remain the separate coordinator/X2
gates; this review has no admission authority.

## 2. Frozen claim, notation and proof dependencies

Let $p$ be any prime, $k=\overline{\mathbf F}_p$, and
$f\in k[x]$ have degree $d\ge2$ and $f'=0$. Let
$g=A/B\in k(x)^\times$, with nonzero coprime polynomials $A,B$,
and $m=\max(\deg A,\deg B)$. Define the integers

$$
a=\left\lceil\frac{m}{d-1}\right\rceil,\qquad b=a+1,
\qquad D=2b^2,\qquad N=3D+1=6b^2+1.
$$

The original return polynomials and whole-product differences are

$$
F_n=f^{\circ n}-x,\qquad
H_n=\prod_{i=0}^{n-1}A(f^{\circ i}(x))-
    \prod_{i=0}^{n-1}B(f^{\circ i}(x)),\qquad
S_* =\prod_{r=1}^{D}F_r.
$$

Condition (CP) means that all but finitely many ordinary primitive
affine cycles avoid the zero/pole support of $g$ and have actual
product one. Each cycle point is counted once. The time step is the
original $f$, not Frobenius or a selected iterate.

For
$I_g=\{S\in k[x]:F_n\mid SH_n\text{ for all }n\ge1\}$,
the four claims are equivalent:

1. (CP) holds.
2. $I_g\ne(0)$.
3. $S_*\in I_g$.
4. $F_n\mid S_*H_n$ for every integer $1\le n\le N$.

The checked dependency chain is: actual monic conjugacy; simple-root
cycle/ideal equivalence; digit basis and exact Laurent functional;
finite transfer-state and word bounds for each fixed $S$; upper and
lower split ranks; long-return persistence of each visible cycle;
replacement of unknown $S$ by the explicit $S_*$; and the final
horizon calculation. Every needed assertion is supplied in the
author report and checked below. Neither the unaccepted R10 A1 proof
nor its review was read or imported as a theorem by this reviewer.

## 3. Monic reduction preserves the actual statement: PASS

For leading coefficient $c_d\ne0$, choose $t\ne0$ with
$c_dt^{d-1}=1$. Algebraic closedness supplies such a $t$. The
change $x=ty$ gives the actual conjugate
$\widetilde f(y)=t^{-1}f(ty)$, not the different dynamics obtained
by merely multiplying $f$ by a scalar. It is monic, has degree $d$
and derivative zero. Substitution in $A,B$ preserves coprimality
and both degrees, hence the same height $m$.

The conjugacy preserves least periods, support avoidance and every
ordinary product. Independent substitution gives exactly

$$
\widetilde F_n(y)=t^{-1}F_n(ty),\qquad
\widetilde H_n(y)=H_n(ty),\qquad
\widetilde S_*(y)=t^{-D}S_*(ty).
$$

Thus the original and tilded divisibility tests are equivalent under
an invertible variable substitution and nonzero scalar factors.
A general fixed $S$ corresponds to $S(ty)$ without degree change.
The constants $D,N$ are therefore unchanged, and the final criterion
is valid directly for the original nonmonic input.

## 4. Simple roots and the exact ordinary CP ideal: PASS

The chain rule gives $(f^{\circ n})'=0$ for every positive $n$,
so $F_n'=-1$ without an exception for $p\mid n$ or $p=2$.
In the monic normalization each $F_n$ has exactly $d^n$ distinct
roots. Define

$$
\mathcal B_n=\{x:F_n(x)=0,\ H_n(x)\ne0\},\qquad
\mathcal B=\bigcup_{n\ge1}\mathcal B_n.
$$

At a return point, applying $f$ cyclically permutes each of the two
lists of numerator/denominator factors. Thus $H_n$ is constant on
every native cycle in $\operatorname{Fix}(f^{\circ n})$ even when
some factors are zero. The set $\mathcal B_n$ is a union of full
cycles and is genuinely permuted by $f$.

Simple roots give $F_n\mid SH_n$ exactly when $S$ vanishes on
$\mathcal B_n$. Hence $I_g\ne(0)$ is equivalent to finiteness of
$\mathcal B$; if finite, its vanishing ideal is generated by
$\prod_{x\in\mathcal B}(X-x)$, with empty product one.

Only finitely many cycles can meet the finite support of $g$.
Each such cycle has finite length, so their full union is finite,
without any coefficient-independent length bound being assumed.
On a support-avoiding cycle $O$ of least period $r\mid n$, the
denominator product is nonzero and

$$
H_n(x)=\left(\prod_{i=0}^{n-1}B(f^{\circ i}(x))\right)
\left(\left(\prod_{y\in O}g(y)\right)^{n/r}-1\right).
$$

Consequently (CP) makes $\mathcal B$ finite. Conversely, every
admissible bad cycle is visible in $\mathcal B_r$ at its own least
period, so finiteness of $\mathcal B$ leaves only finitely many
bad cycles, in addition to the finite support cycles. This is the
full equivalence of (CP) with the ideal condition.

A cycle meeting both a numerator zero and a denominator zero has
both whole products zero at every return and is never visible.
It is a legitimate finite support exception, not a counterexample
to this equivalence. A one-sided support cycle is visible. The later
period bound must treat the latter but need not cover the former.

## 5. Digit basis, top pairing and the Laurent extractor: PASS

The cyclic algebra with relations $f(X_i)=X_{i+1}$ is isomorphic
to $k[x]/(F_n)$ via $X_i=f^{\circ i}(x)$. Monicity expresses each
$X_i^d$ by terms of smaller total degree. This also holds for
$n=1$, whose relation is $f(X_0)-X_0$.

The digit monomials with $0\le\epsilon_i<d$ have images that
are monic of the distinct degrees $\sum_i\epsilon_i d^i$,
covering $0,\ldots,d^n-1$. They form a basis; no assumption that
$d$ is prime or a prime power is used.

The functional $L_n$ selecting the top digit coefficient is exactly
the coefficient of $x^{d^n-1}$ in the remainder. Its multiplication
pairing is nondegenerate: for a nonzero remainder of degree $q$,
multiplication by $x^{d^n-1-q}$ exposes its nonzero leading
coefficient without reduction. Since the digit monomials span, all
tests $L_n(X^\epsilon U)=0$ are equivalent to $U=0$. This does
not rely on a trace pairing or on squarefreeness of the algebra.

For the author's Laurent functional, an input monomial of total
degree $J_0$ can contribute only if

$$
J_0-n(d-1)=(d-1)\sum_iq_i+\sum_i u_i,
\qquad q_i,u_i\ge0.
$$

Here $-d(q_i+1)-u_i$ is the selected exponent in the expansion
of $f(X_i)^{-q_i-1}$ at infinity. The equality bounds every
index and proves local finiteness. Each inverse is the formal inverse
of a monic Laurent unit; no division by an integer in $k$ is used.

Multiplying the geometric series at site $j$ by
$f(X_j)-X_{j+1}$ telescopes to one. In the remaining factors,
$X_j$ can occur only in nonnegative powers, so multiplication by
any polynomial still has zero coefficient at $X_j^{-1}$.
The local-finiteness bound justifies cancellation and removes the
unbounded tail. Thus the defining ideal is annihilated.
For $n=1$ the canceled expression is simply a polynomial, and its
$X_0^{-1}$ coefficient is zero; cyclic index coincidence causes
no exception.

The top digit input forces all $q_i,u_i$ to be zero and gives
coefficient one. Every other digit input has insufficient total
degree and gives zero. Therefore the Laurent functional is exactly
$L_n$, not only an approximation or a formal residue heuristic.

## 6. All transfer states and the fixed-$S$ horizon: PASS

For
$T_h(r,s)=[X^{-1}]X^rh(X)/f(X)^{s+1}$, a nonzero entry
requires $ds\le r+\deg h-d+1$ by its largest possible exponent.
Cancellation can make additional entries zero, but cannot invalidate
this necessary bound. Factoring the locally finite Laurent sum gives
the exact cyclic product of these matrices with incoming row and
outgoing column indices.

For a fixed nonzero $S$ of degree $\ell$, ordinary digit factors
give $ds\le r+m$; the single distinguished factor gives
$ds\le r+m+\ell$. At an occurrence of the largest cyclic index
$s$, the incoming index is no larger, so
$(d-1)s\le m+\ell$. All nonzero cyclic contributions are
therefore inside $0,\ldots,R$, where $R=a+\ell$ is a valid
uniform upper bound.

The range $0,\ldots,a$ is closed under every ordinary transition,
because $m\le(d-1)a$. More precisely,

$$s-a\le(r-a)/d.$$

After $j$ bulk transitions a path starting anywhere up to $R$
is at most $a+\ell/d^j$. The chosen
$k_S=\lfloor\log_d\ell\rfloor+1$ for $\ell>0$ ensures the
strict inequality $d^{k_S}>\ell$, including when $\ell$ is an
exact power of $d$. Integrality then puts the path in the low range.
For $\ell=0$, $k_S=0$ and the whole cyclic path is already low.

The numerator and denominator remain in separate blocks. The
distinguished block contains $S$ and one minus sign, so its trace
is exactly $L_n(SX^\epsilon H_n)$. All coefficients and constant
phases in $A,B$ occur once per site; none is normalized away.

For $n\ge k_S+1$, the $n-1$ bulk sites before the distinguished
site force its incoming index low. The distinguished site followed
by the first $k_S$ bulk sites also ends low. Its effective prefix
matrix retains every high intermediate state up to $R$ before
taking low rows and columns. Only the remaining tail is restricted
to the closed low range. Thus the reduction to equation (6.8) does
not prematurely discard any high-state contribution. At
$n=k_S+1$ the tail is empty, which is included.

The low two-block matrices have size $v=2b$. The spaces spanned by
all words of length at most $j$, including the identity, start in
dimension one. Equality at one step implies stability under every
letter. Otherwise dimension strictly increases in a space of
dimension at most $v^2=4b^2$. Hence length at most $4b^2-1$
spans every word. This direct argument works over any characteristic
and does not assume a nondegenerate trace.

For each prefix of length $k_S+1$, the trace functional therefore
needs tail lengths only through $4b^2-1$. Adding the short returns
$n\le k_S$ gives precisely

$$
\left[\forall n\ge1:\ F_n\mid SH_n\right]
\Longleftrightarrow
\left[\forall n\in\{1,\ldots,k_S+4b^2\}:\ F_n\mid SH_n\right].
$$

The off-by-one accounting is correct. This result is for each fixed
$S$ and by itself places no bound on an unknown annihilator.

## 7. Split rank and both full evaluation ranks: PASS

With $S=1$, every state is low. Products of the two-block matrices
belong to
$\operatorname{Mat}_b(k)\oplus\operatorname{Mat}_b(k)$, of
dimension $D=2b^2$. Splitting a digit word at any $1\le h<n$
factors its coefficient matrix through the bilinear expression
$\operatorname{tr}(E M_uM_v)$ on that space. Its rank is at most
$D$ whether or not that bilinear form is degenerate.

The same matrix has an independent ordinary-point factorization.
For monic squarefree $F_n$, the Lagrange interpolation polynomials
have top coefficients $1/F_n'(x)$. Since $F_n'=-1$,

$$L_n(R)=-\sum_{F_n(x)=0}R(x).$$

This applies to every polynomial through its remainder. Removing
the zero weights gives the exact matrix factorization

$$\mathcal F_{n,h}=V\operatorname{diag}(-H_n(x))W^{\mathsf T},
\qquad x\in\mathcal B_n.$$

Put $t_n=|\mathcal B_n|$. If $d^h\ge t_n$, the left digit
polynomials span all degrees below $d^h$. Lagrange polynomials of
degree below $t_n$ realize arbitrary values at the $t_n$ distinct
points, so $V$ has full column rank $t_n$.

The right columns evaluate the other digit polynomials at
$f^{\circ h}(x)$. Section 4 shows that $f^{\circ h}$ actually
permutes $\mathcal B_n$, despite the map's global inseparability.
Thus these are again $t_n$ distinct evaluation points. If
$d^{n-h}\ge t_n$, the same degree argument gives full column
rank for $W$ as well.

The diagonal weights are all nonzero. Multiplying the factorization
by a left inverse for $V$ and a right inverse for $W^{\mathsf T}$
recovers this invertible diagonal matrix. This proves rank exactly
$t_n$, not just an upper bound. Consequently $t_n\le D$ when
both length conditions hold. For $t_n=0$ the rank is zero.

These ranks are ordinary integer dimensions, not point counts
reduced modulo $p$. No Gram matrix, positivity, separability of
$f$ on neighborhoods, or nondegeneracy of a matrix trace form is
being presumed.

## 8. Persistence and the unknown exceptional set: PASS

Suppose $I_g\ne(0)$, so the full visible set $\mathcal B$ is
finite. Fix any $x\in\mathcal B_{n_0}$ and let $r$ be its
ordinary least period. Denote the two whole products at this return
by $\alpha,\beta$, so $\alpha-\beta\ne0$. Repetition of the
actual $n_0$-step return gives

$$H_{qn_0}(x)=\alpha^q-\beta^q.$$

Choose $M$ divisible by the finite multiplicative orders of the
nonzero members of $\{\alpha,\beta\}$. For arbitrarily large
$q=1+jM$, every nonzero member is unchanged by the $q$th power,
and a zero member stays zero. Thus the same nonzero difference
persists. This proves the claim also for one-sided support zeros,
without dividing by either product. Both cannot be zero at a
visible point.

Write $t=|\mathcal B|$. It is fixed; no numerical bound in terms
of $d,m$ has yet been established or assumed. Choose a persisting
return $n$ large enough that both halves have at least $t$
available digit degrees. Then $t_n\le t$ supplies both hypotheses
of Section 7. The entire native $r$-cycle lies in $\mathcal B_n$,
so

$$r\le t_n\le D.$$

This argument is applied separately to every visible cycle. It
needs neither a uniform multiplicative order nor simultaneous
visibility of the entire finite set at one return. The unknown
$t$ is used only to select an arbitrarily long return in the proof,
not as an input to the final finite criterion.

The conclusion is a bound on each visible native period, not an
assertion that $|\mathcal B|\le D$. Cycles with both support
products zero remain outside this conclusion, exactly as required.

## 9. Explicit annihilator, constants and remaining boundaries: PASS

Each point in $\mathcal B$ now has least period $r\le D$ and
is a root of the corresponding factor $F_r$ of $S_*$. Thus
$S_*$ vanishes on all of $\mathcal B$, and the simple-root
criterion gives $S_*\in I_g$. Conversely this membership supplies
a nonzero ideal element because every $F_r$, and hence $S_*$,
is a nonzero polynomial.

The actual degree calculation is

$$
\ell_* =\sum_{r=1}^{D}d^r
=\frac{d^{D+1}-d}{d-1}<d^{D+1},\qquad
k_{S_*}\le D+1.
$$

These are integer degree computations, not divisions of field
scalars. Substitution in the fixed-$S$ horizon yields

$$k_{S_*}+4b^2\le D+1+2D=3D+1=N.$$

Therefore passing every prescribed finite test implies membership
in the full all-return ideal, and membership implies every test.
Together with the earlier equivalences, this proves the full frozen
criterion in both directions. Testing only some selected return
integers would not be the theorem that has been checked.

The remaining boundary checks are as follows:

- For $m=0$, the low range has one state, $D=2$ and $N=7$.
  The only nonzero scalar-factor letter has digit $d-1$; its two
  blocks retain $A$ and $B$ themselves. The resulting coefficient
  is $A^n-B^n$, not a phase-free replacement. If that constant
  difference is nonzero at one return, the same persistence argument
  produces arbitrarily large visible root sets, so constants are
  not an untreated exception.
- In characteristic two, $-1=1$ is still nonzero. The derivative,
  interpolation and single subtraction block keep their correct
  meanings. The rank upper bound never requires the trace pairing
  to be nondegenerate in that characteristic.
- Unequal numerator/denominator degrees and every multiplicity are
  included in the degree inequalities. Whole products are used;
  factorwise (CP) is never inferred.
- The degree $d$ need not be a prime power, and $f$ need not be
  monomial or unicritical. The general Laurent expansion retains
  all lower coefficients; $f'=0$ is used for simple returns, not
  as a substitute Frobenius normal form.
- All positive return integers and all ordinary least periods,
  including those divisible by $p$, are retained throughout.
  Infinity is only one extra fixed cycle and does not alter the
  affine cofinite question.

## 10. Provenance, source boundary and work receipt

The final added disclosure correctly records that the coordinator
supplied the high-level general-polynomial two-block/carry/rank/
persistence adaptation and proposed constants before the author
proof. The reviewer knew this provenance and reviewed the actual
complete proof as a nonauthor. No blind or independent-origin
description is appropriate. The coordinator-requested disclosure
is now read back and closed; it changes no mathematical statement.

The needed finite-word span bound is proved directly in Section 6.
No result from an unaccepted A1 shortcut, external automata theorem,
rational-field positivity argument or general cohomological existence
theorem is required for the positive mathematical verdict. This review
does not recertify the author's primary-PDF access receipt, antecedent
hashes or external priority assessment. Those separate source and
substantiality checks belong to X2/coordinator; no new search was
needed for the self-contained proof audit.

Verification used complete actual text, independent hand calculations,
read-only version hashes, the targeted provenance readback and final
review-file readback. Mathematical programs: zero. Source-query
batches: zero. No new agent, external API/model call, GPU job, Git
action, author/old/shared-file edit, manuscript or PDF work occurred.
The only new workspace write is this allocated review file.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
