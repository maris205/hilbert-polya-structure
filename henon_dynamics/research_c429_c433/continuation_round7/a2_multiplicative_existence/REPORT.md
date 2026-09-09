# R7: the finite divisor residual for multiplicative existence

2026-09-10 UTC. One bounded theorem-first attempt inside unchanged MS6.

## 1. Frozen question, status, and single mechanism

For every prime $p$, put $k=\overline{\mathbf F}_p$. For every
integer $d\ge2$, every $c\in k$, and every $g\in k(x)^\times$,
let $f(x)=x^d+c$ and $\delta h=h\circ f/h$. Suppose that, except
for finitely many ordinary primitive $f$-cycles, the cycles avoid the
zeros and poles of $g$ and have product $\prod_{a\in O}g(a)=1$.
Call this condition **(CP)**. Does it follow that

$$g^{p^e}=\delta h\quad\text{for some }e\ge0,
\ h\in k(x)^\times?$$

The native clock is one application of $f$. All ordinary primitive
cycles, including periods divisible by $p$, are retained. Cofiniteness
does not mean one finite-field sample or only prime-to-$p$ periods.

**Initial status: NOT CURRENTLY JUSTIFIED.** The exact R7 obligation
is (CP) $\Rightarrow$ $[g]$ torsion in
$k(x)^\times/\delta k(x)^\times$. The frozen
[R6 report](../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
already supplies saturation after that existence step. Its proof is
subtracted and will not be repeated or edited here.

Only one new mechanism is selected: a finite, rational-valued divisor
normal form obtained from pushforward, followed by the test whether
(CP) kills its fiber-balanced residual. No finite-permutation transfer
degree guess or invariant-hypersurface theorem is a second route in
this task.

## 2. Exact decisive lemma frozen before proof work

Let $D=\operatorname{div}(g)$ on $\mathbf P^1_k$. For geometric
points, define $f_*[a]=[f(a)]$, and extend linearly to rational
divisors. Define the candidate divisor

$$E_D=\sum_{n\ge1}d^{-n}f_*^nD. \tag{2.1}$$

The planned normalization proof must justify that this is a finite
rational divisor, not merely a formal or convergent infinite-support
object. Put

$$\mathcal R_f(D)=f^*E_D-E_D-D. \tag{2.2}$$

The decisive existence lemma for this one mechanism is:

> For every frozen $p,d,c,g$, if $g$ satisfies (CP), then
> $\mathcal R_f(\operatorname{div}(g))=0$.

Its proof or a full counterexample satisfying (CP) would settle the
selected bridge. Merely making the residual explicit does not prove
that periodic products annihilate it.

### Dependency map and falsification boundary

1. Prove convergence, finite support, rationality, and the identity
   $(d-f_*)E_D=f_*D$.
2. Prove that $\mathcal R_f(D)$ lies in $\ker f_*$ and that
   $[g]$ is torsion if and only if $\mathcal R_f(D)=0$.
3. Check the coordinator's pure-Frobenius boundary $d=p^r$ by actual
   conjugacy and finite coefficient-field reasoning; do not replace
   the full family by that boundary.
4. Attempt the displayed decisive lemma for the remaining family.
   A nonzero residual by itself only detects a non-torsion rational
   function; it is not an MS6 counterexample unless (CP) also holds.

All earlier author/review files remain frozen. The sole writable path
is this report. No mathematical program, new/nested worker, external
model/API, Git operation, manuscript/PDF, or old/shared-file edit is
allocated. At most two genuinely relevant primary-search batches may
be used, without repeating X2's invariant-hypersurface search.

## 3. Proved: the canonical finite divisor and its residual

All coefficients of divisors in this section lie in $\mathbf Q$, not
in $k$. In particular, $d^{-1}$ is a rational number even when
$p\mid d$. Valuation orders, local degrees, and divisor multiplicities
are integers and are not reduced modulo $p$.

Let $V$ be the rational vector space of finite divisors on
$\mathbf P^1(k)$. Give it the norm
$\|\sum_a u_a[a]\|_1=\sum_a|u_a|$. Write $P=f_*$ and $A=f^*$.
Then

$$\|PU\|_1\le\|U\|_1,\qquad PA=dI. \tag{3.1}$$

The first inequality allows cancellation when different points map to
the same image. To verify the second identity, put
$q=p^{v_p(d)}$ and $s=d/q$, so $p\nmid s$. A finite fiber over
$b\ne c$ has $s$ distinct points of multiplicity $q$ because

$$X^d-(b-c)=\left(X^s-(b-c)^{1/q}\right)^q.$$

The fiber over $c$ is the single point 0 of multiplicity $d$, and
infinity also has local degree $d$. The sum of local degrees in every
fiber is $d$. Each geometric residue-field degree is 1, including for
an inseparable map, which proves $PA=dI$ with the stated convention.

**Theorem 3.1 (finite exact torsion criterion).** For every frozen
$p,d,c,g$, let $D=\operatorname{div}(g)$ and define $E_D$ and
$\mathcal R_f(D)$ by (2.1)--(2.2). Then:

1. $E_D$ is a finite rational divisor of degree zero, supported on
   the forward orbit of $\operatorname{supp}D$;
2. $PE_D=dE_D-PD$ and $P\mathcal R_f(D)=0$;
3. if a finite rational divisor $U$ satisfies $AU-U=D$, then
   $U=E_D$;
4. $[g]\in k(x)^\times/\delta k(x)^\times$ is torsion if and only
   if $\mathcal R_f(D)=0$.

No periodic-product hypothesis is used in this theorem.

**Proof of parts 1--3.** There is a finite field containing $c$ and
every finite point of $\operatorname{supp}D$. The map $f$ preserves
this finite field, and fixes infinity. Consequently the forward
closure $S$ of $\operatorname{supp}D$ is finite and $f(S)\subset S$.
On $\mathbf Q^S$, $P$ is an integer matrix with one 1 in each column.

The series (2.1) is absolutely convergent in $\mathbf R^S$, since

$$\sum_{n\ge1}\|d^{-n}P^nD\|_1
\le\frac{\|D\|_1}{d-1}. \tag{3.2}$$

Every term has degree zero. Summing the shifted geometric series gives
$(dI-P)E_D=PD$. The matrix $dI-P$ is invertible over $\mathbf Q$:
if $PU=dU$, (3.1) implies $d\|U\|_1\le\|U\|_1$, hence $U=0$.
An invertible rational matrix has a rational inverse. Thus $E_D$ has
rational coefficients and the already established finite support and
zero degree. Using $PA=dI$ now gives

$$P(AE_D-E_D-D)=dE_D-PE_D-PD=0.$$

For uniqueness, push $AU-U=D$ forward to get
$U=d^{-1}PU+d^{-1}PD$. Iteration yields

$$U=\sum_{j=1}^n d^{-j}P^jD+d^{-n}P^nU.$$

The final term has norm at most $d^{-n}\|U\|_1$ and tends to zero.
Therefore $U=E_D$, even if the support of $U$ was not initially
assumed to lie in $S$.

**Proof of part 4.** If $g^m=\delta h$ for an integer $m\ge1$,
then $U=m^{-1}\operatorname{div}(h)$ satisfies $AU-U=D$.
Part 3 gives $U=E_D$, so $\mathcal R_f(D)=0$.

Conversely, choose a positive integer $M$ clearing the denominators
of $E_D$. Every integral degree-zero divisor on $\mathbf P^1_k$ is
principal: explicitly, if its finite-point coefficients are $n_a$,
the function $h(x)=\prod_{a\ne\infty}(x-a)^{n_a}$ has that divisor.
Choose $h$ with $\operatorname{div}(h)=ME_D$. If the residual is
zero, then $\operatorname{div}(g^M/\delta h)=0$, so
$g^M/\delta h=\eta\in k^\times$. This constant has finite order
$t$, because it belongs to a finite field. Hence
$g^{Mt}=\delta(h^t)$ and $[g]$ is torsion. $\square$

### A finite denominator and transfer-size bound

The criterion does not involve an unspecified degree search. If $S$
has $T$ nonperiodic vertices and cycles of lengths $r_1,\ldots,r_b$,
one possible denominator-clearing integer is

$$M=\det(dI-P|_{\mathbf Q^S})
  =d^T\prod_{i=1}^b(d^{r_i}-1)>0. \tag{3.3}$$

For the determinant formula, order vertices so that the induced map on
the quotient by the cycle vertices is nilpotent. Its block contributes
$d^T$; each permutation-cycle block has characteristic polynomial
$Z^{r_i}-1$. The adjugate formula then shows that $ME_D$ is integral.
If $D=0$, use $S=\varnothing$ and the empty determinant/product $M=1$.

Let $H(g)$ denote the rational-map degree of a nonconstant $g$, and
put $H(g)=0$ for a constant. Since $\|D\|_1=2H(g)$, (3.2) gives
for the function $h$ above

$$H(h)\le\frac{M H(g)}{d-1}. \tag{3.4}$$

This bounds the function whose divisor is $ME_D$. A constant phase
may still require the extra exponent $t$ in the proof of part 4.
Equations (3.3)--(3.4) are existence bounds for this divisor test,
not a runtime claim or a proof that (CP) passes the test.

The residual is supported on the finite set $S\cup f^{-1}(S)$.
Writing $u_a$ for the coefficient of $E_D$ (zero outside $S$), its
coefficient at $a$ is

$$\mathcal R_f(D)_a=e_f(a)u_{f(a)}-u_a-D_a. \tag{3.5}$$

Here $e_f(a)$ is the total local degree, including its inseparable
factor. Equation $P\mathcal R_f(D)=0$ means that the coefficients
in (3.5) sum to zero over every geometric fiber. It does not mean
that each of those coefficients vanishes.

## 4. Proved: normalization to the norm-one obstruction

Identify the target function field with $k(t)$ through $t=f(x)$.
Let $N_f:k(x)^\times\to k(t)^\times$ be the field norm for this
degree-$d$ extension, with its output subsequently viewed as a rational
function in the base coordinate. With the pushforward convention in
Section 3,

$$\operatorname{div}(N_f u)=P\operatorname{div}(u). \tag{4.1}$$

For this family the formula can be checked directly, including
inseparability. Factor
$u=\alpha\prod_{a\in k}(x-a)^{m_a}$ with finitely many nonzero
$m_a$. The monic minimal polynomial of $x$ over $k(t)$ is
$X^d+c-t$ (irreducible by Eisenstein at $t-c$), so the determinant
definition of the norm gives

$$N_f(x-a)=(-1)^{d+1}(t-f(a)),\qquad N_f(\alpha)=\alpha^d.$$

Multiplying these identities proves (4.1) at finite points, and the
degrees give the coefficient at infinity. No separable-embedding-only
definition of the norm is being used.

**Proposition 4.1.** From any $g$ satisfying (CP), one can construct
integers $M,\nu\ge1$, a rational function $h\ne0$, and

$$w=\left(g^M/\delta h\right)^\nu \tag{4.2}$$

such that $w$ satisfies (CP), $N_f w=1$, and

$$\operatorname{div}(w)=-M\nu\mathcal R_f(D). \tag{4.3}$$

In particular, $w$ is constant if and only if $[g]$ is torsion.

**Proof.** Take $M,h$ as in Section 3, without assuming the residual
is zero. For $v=g^M/\delta h$,

$$\operatorname{div}(v)=MD-M(AE_D-E_D)=-M\mathcal R_f(D).$$

Equation (4.1) and $P\mathcal R_f(D)=0$ imply $N_fv=\eta\in k^\times$.
Take $\nu$ to be the finite order of $\eta$. Then $w=v^\nu$ has norm 1
and satisfies (4.3). Outside the finitely many original exceptional
cycles and those meeting zeros or poles of $h$, the products of
$\delta h$ telescope to 1. Powers preserve product 1, so both $v$
and $w$ satisfy (CP). Equation (4.3) and Theorem 3.1 give the last
assertion. $\square$

Conversely, if $N_f w=1$, then $P\operatorname{div}(w)=0$, whence
$E_{\operatorname{div}(w)}=0$ and

$$\mathcal R_f(\operatorname{div}(w))=-\operatorname{div}(w).$$

Theorem 3.1 therefore shows that a norm-one function has torsion class
only when it is constant. A constant satisfying (CP) is 1 by the
large-prime-period argument in R6 Section 4, which is an imported
result, not repeated here.

Thus the exact remaining lemma for the single selected mechanism is
equivalently the following full-parameter assertion:

> For every prime $p$, every $d\ge2$, every $c\in\overline{\mathbf F}_p$,
> and every $w\in\overline{\mathbf F}_p(x)^\times$, if $N_f w=1$
> and $w$ satisfies (CP), then $w=1$.

This is still unproved in the general family. Proposition 4.1 is a
normalization, not a derivation of its last displayed implication.

## 5. Proved boundary: every pure-Frobenius subtype

Suppose $d=q=p^r$ with $r\ge1$, while $c$ and $g$ are arbitrary.
The map $f(x)=x^q+c$ is a bijection of $\mathbf P^1(k)$, so its
pushforward $P$ is injective on finite rational divisors. Since
$P\mathcal R_f(D)=0$, the residual is always zero. Thus every class
$[g]$ is torsion in this subtype, even without (CP).

The coordinator supplied the following sharper, direct exponent
argument, which is checked here and credited to that input. Choose a
root $\beta\in k$ of $\beta^q+c=\beta$. With $x=z+\beta$,

$$f(z+\beta)-\beta=z^q.$$

Set $\widetilde g(z)=g(z+\beta)$. Its finitely many coefficients
belong to $\mathbf F_{q^s}$ for some $s\ge1$: any finite subfield
of $k$ embeds into one of these extensions after increasing $s$.
Let $\sigma_0a(z)=a(z^q)$ and $\delta_0a=\sigma_0a/a$. Then

$$\sigma_0^s\widetilde g=\widetilde g^{q^s},\qquad
\delta_0\left(\prod_{j=0}^{s-1}\sigma_0^j\widetilde g\right)
=\widetilde g^{q^s-1}. \tag{5.1}$$

Translation transports (5.1) back to $f$. The integer $q^s-1$ is
prime to $p$. If (CP) is imposed, the frozen R6 conditional-saturation
theorem therefore gives $g=\delta h$ itself, with no $p$-power needed.
The converse follows from ordinary telescoping outside finitely many
cycles meeting the transfer's support.

This closes every $d=p^r$, every $c$, and every $g$ as a boundary of
the unchanged question. It does not close mixed inseparable degrees
$d=p^r s$ with $s>1$, or separable degrees, and is not a replacement
contract or an additional paper.

## 6. What the unicritical sibling structure actually supplies

Retain $d=qs$, $q=p^{v_p(d)}$, $p\nmid s$. For the norm-one
function $w$ of Section 4, the norm's explicit factorization gives

$$\left(\prod_{\zeta\in\mu_s(k)}w(\zeta x)\right)^q=1,$$

and hence

$$\prod_{\zeta\in\mu_s(k)}w(\zeta x)=1. \tag{6.1}$$

For example, this follows by checking a factor $x-a$: its product
over the $s$ rotations is $(-1)^{s+1}(x^s-a^s)$; raising to $q$
gives the norm after $t=x^d+c$. The signs agree because $q$ is odd
when $p$ is odd, and all signs coincide in characteristic 2.

If $s=1$, (6.1) already gives $w=1$, consistent with Section 5.
For $s>1$, choose a primitive $s$-th root $\zeta$ and put
$\tau a(x)=a(\zeta x)$. The classical cyclic Hilbert 90 conclusion
is only a sibling coboundary:

$$w=\tau v/v\quad\text{for some }v\in k(x)^\times. \tag{6.2}$$

For completeness, define $b_0=1$ and
$b_i=\prod_{j=0}^{i-1}\tau^jw$ for $1\le i\le s$. Then $b_s=1$.
For $a\in k(x)$, put

$$v_a=\sum_{i=0}^{s-1}b_i^{-1}\tau^ia.$$

Reindexing shows $\tau v_a=w v_a$. At least one choice
$a\in\{1,x,\ldots,x^{s-1}\}$ makes $v_a\ne0$. Otherwise the
invertible matrix $(\zeta^{ij})_{0\le i,j<s}$ would force all the
coefficients $b_i^{-1}$ to vanish, contrary to $b_0=1$. This proves
(6.2) directly and retains the hypothesis $p\nmid s$.

Equation (6.2) does not telescope on an $f$-cycle: generally
$\zeta a$ is not the next point $f(a)$ of that cycle. Indeed,
$f(\zeta x)=f(x)$ identifies siblings in a fiber rather than
successive native times. No argument was found that upgrades this
sibling coboundary, even together with (CP), to $w=1$.

### A complete norm-one negative control, not an MS6 counterexample

In characteristic 5 take $f=x^2$ and $w=(x-1)/(x+1)$. Its norm is 1,
and $P\operatorname{div}(w)=[1]-[1]=0$, but its divisor is nonzero.
Theorem 3.1 already excludes every positive integer-power rational
transfer. Directly, the fixed point 1 has local degree 1, so
$\operatorname{ord}_1(\delta h)=0$ for every $h$, whereas
$\operatorname{ord}_1(w^m)=m$.

This function does **not** satisfy (CP). To show this with infinitely
many native periods, take a prime integer $n\equiv3\pmod4$ and set
$L=2^n-1$. In characteristic 5, $L=2\ne0$. Every root of

$$Q(X)=(X^L-1)/(X-1)$$

has exact $f$-period $n$: it is nonzero, is not 1, and its period
divides the prime $n$. These roots are distinct, avoid $\pm1$, and

$$\prod_{Q(a)=0}w(a)=Q(1)/Q(-1)=L=2\ne1. \tag{6.3}$$

Here $L-1$ is even, $Q(1)=L$, and $Q(-1)=1$. Consequently at least
one primitive $n$-cycle has product different from 1. There are
infinitely many primes $n\equiv3\pmod4$: if they formed a finite
list, the integer four times their product minus one would have a new
prime factor congruent to 3 modulo 4. Thus (6.3) gives infinitely many
bad primitive cycles, not just an exceptional fixed point.

This hand control demonstrates that norm one and sibling Hilbert 90
alone do not supply the sought existence theorem. It is not a
counterexample to MS6 because its periodic hypothesis fails.

### Why merging ordinary cycles is also an information loss

For a small exact illustration, take the same $f,w$ in characteristic
3 and the six nontrivial seventh roots of unity. They form two
primitive 3-cycles. The product of $w$ over all six points is
$7=1$ in this field, by the same quotient-polynomial identity.
Nevertheless each individual cycle has product different from 1.

To check that last assertion, let $\xi$ be a primitive seventh root.
The two cycles have exponent sets $\{1,2,4\}$ and $\{3,6,5\}$.
On each cycle $\prod(a+1)=1$, because
$a+1=(f(a)-1)/(a-1)$. If

$$U=(\xi-1)(\xi^2-1)(\xi^4-1),$$

expansion using $\xi^7=1$ shows that the other cycle's numerator
product is $-U$. Their total product is 1, so $U^2=-1=2$ in
characteristic 3. Neither $U$ nor $-U$ equals 1. This is a finite
information-loss example, not an assertion about cofinite products
in that characteristic. The full condition (CP) retains the separate
primitive-cycle products which such aggregate identities discard.

## 7. Source subtraction, actual access, and stopping boundary

The canonical divisor calculation, principal-divisor construction,
explicit unicritical norm, and cyclic Hilbert 90 proof above are
elementary algebraic tools. They are not claimed as independently
novel theorems or as a new paper. The pure-Frobenius exponent argument
was supplied by the coordinator and verified in Section 5. R6's
conditional saturation and constant-phase result remain imported.

One source-search batch, containing two queries, was used through the
research-lit skill to distinguish a finite rational-solution test from
a theorem producing a solution out of periodic data. The active tools
had no Zotero/Obsidian interface; a relevant-filename check of local
`papers/` and `literature/` found no matching source. The expected
local arXiv fetch-script locations were unavailable, so one query used
the arXiv-domain web fallback. No PDF was downloaded, and no source
algorithm was run.

| Actually inspected primary source | Relevant access and subtraction |
| --- | --- |
| Chyzak--Dreyfus--Dumas--Mezzarobba, [*Computing solutions of linear Mahler equations*, arXiv:1612.05518v2](https://arxiv.org/pdf/1612.05518v2) | Section 1.3 fixes a computable subfield of $\mathbf C$; Section 3.5, Proposition 3.22, Algorithm 9 and its displayed proof provide a rational-solution procedure. These pages were read. Rational-solution algorithms are established prior machinery; their displayed input is an equation, not (CP). No positive-characteristic existence consequence is imported. |
| Faverjon--Poulet, [*Computing basis of solutions of any Mahler equation*, arXiv:2511.18877v1](https://arxiv.org/pdf/2511.18877v1) | Introduction and the complete Theorem 1 statement were read. That algorithmic theorem explicitly assumes an effective characteristic-zero field and gives solutions in larger formal extensions. Its proof was not needed or imported. An abstract's mention of positive-characteristic applications is not a finite algebraic-transfer existence theorem for MS6. |

Neither source was used to infer that a nonzero solution exists in a
specified finite extension from cofinite ordinary cycle products. No
exact-source collision or priority conclusion is inferred from this
bounded search, and the unused second search batch is not expanded
into another mechanism. X2's separate invariant-hypersurface search
was not repeated.

**Final mathematical boundary.** The finite residual criterion and
norm-one normalization are proved, and the full pure-Frobenius
subtype is closed using the coordinator's input and R6. For general
$d$, the decisive all-parameter lemma in Section 2, equivalently the
norm-one assertion in Section 4, remains **NOT CURRENTLY JUSTIFIED**.
The sibling factorization has not bridged it, and the displayed
controls do not refute MS6. No further mechanism, larger parameter
family, computation, or automatic admission is inferred.

The proof-writer skill required keeping that missing implication
explicit; the research-lit skill influenced the source subtraction,
not the mathematical claim. Only this new report was written. There
were no mathematical executions, new agents, external model calls,
Git operations, manuscripts/PDFs, or edits to frozen/shared files.
