# E8 nonauthor review: unicritical carry extension

2026-09-09 UTC. Independent current-team mathematical review of the
allocated R4 same-paper extension. The proof-writer and research-review
skills are applied under the repository's current-model/no-external-upload
boundary. This is internal model review, not human or external-model review.

## Decision

**PROVABLE AS STATED.** The complete 487-line author proof passes.
There are zero required mathematical repairs in the reviewed scope.
The digit carry stabilization, the stated ordinary-cycle kernel theorem,
both characteristic branches, and the finite two-return certificate are
all justified. The excluded-congruence example is a valid method-blindness
control and is not represented as a counterexample to ordinary-cycle
regularity.

This is an extension inside the already admitted PC424-L paper candidate,
not an additional contract or paper count. The accepted R3 quadratic proof
and its admission remain unchanged. Global source-priority review and
coordinator integration are separate from this mathematical decision.

## Exact reviewed artifact and claim

The fully read primary artifact is
[A2's proof package](../../a2_unicritical_carry_extension/PROOF_PACKAGE.md),
487 lines, SHA256
`766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01`.
The author confirmed that the complete self-read introduced no mathematical
or textual change; the reviewer independently checked this hash.

For every odd prime $p$, every integer $d\ge2$ satisfying
$d\not\equiv1\pmod p$, every $c\in k=\overline{\mathbb F}_p$,
and $f(x)=x^d+c$, the reviewed conclusion is

$$
K_f=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-cycle }O\right\}
=B_f=\{Q\circ f-Q:Q\in k[x]\}.
$$

All ordinary primitive lengths are retained, including lengths divisible
by $p$. Each distinct point is counted once. One application of $f$ is
one native tick. Neither a special parameter nor a degree cap is imposed
on this kernel equality.

For an integer $M\ge1$ and $\deg h\le M$, including zero $h$, set

$$
n=3\lfloor\log_dM\rfloor+4,\qquad
F_j=f^{\circ j}-x,\qquad
\widetilde H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.
$$

The reviewed finite certificate equates coboundary membership with the
two derivative divisibilities $F_j\mid F_j'\widetilde H_j(h)$,
and with ordinary-root return-sum vanishing, at both $j=n,n+1$.
It yields a detecting primitive period at most
$3\lfloor\log_dM\rfloor+5$ and iterate-polynomial degrees at most
$d^5M^3$. It does not assert an optimized complexity bound.

## Proof interface and source subtraction

The proof explicitly credits the
[accepted quadratic ancestor](../../../continuation_round3/a1_periodic_normal_form/PROOF_PACKAGE.md),
whose unchanged SHA256 is
`06d0d06c1798b55d5a052b7ae3874bd176338ff31887a129b80041c5e1147450`.
E8 previously checked that ancestor in full; the current review checks
the actual higher-degree proof rather than assuming that the binary
argument generalizes.

The polynomial normal form, cyclic basis, leading-digit detector, and
Jacobian interface are all established again with their actual new
parameter $d$. The claimed increment is their compatible $d$-ary
carry extension, with the resulting parameter range and its explicit
method boundary. The binary adjacent-level idea, pure-power monomial
bases, normal forms, and classical trace/residue machinery are not newly
owned results of this extension.

The mathematical proof uses no external theorem beyond its elementary
algebraic arguments. Its external source citations concern antecedent
subtraction, not an unverified positive-characteristic regularity theorem.
The coordinator is separately reviewing those external sources; this
report makes no worldwide priority assertion.

## 1. Normal form and full digit algebra: PASS

For every positive integer $s$, $\Delta x^s$ is monic of degree $ds$.
Elimination of positive exponents divisible by $d$ strictly lowers the
largest exponent being eliminated and never raises the input degree.
It gives

$$
k[x]=B_f\oplus V_d,\qquad
V_d=k\oplus\bigoplus_{r\ge1,\ d\nmid r}kx^r.
$$

The directness argument compares the leading degree of a nonconstant
coboundary with a nonzero normal polynomial. It remains valid for
composite $d$ and when $p\mid d$; it uses no division by $d$.
Only the normal representative is unique absolutely; the transfer is
unique up to constants, as the author states.

The cyclic quotient is isomorphic to $k[x]/(F_n)$, of dimension $d^n$.
Replacing $X_i^d$ by $X_{i+1}-c$ decreases total degree, including
at wraparound. The $d^n$ digit monomials with exponents from $0$ to
$d-1$ span and therefore form a basis. This is the full algebra,
without any reducedness assumption. Telescoping gives zero trace class
for a coboundary in this same full quotient.

The derivative identity is

$$
[F_n']=d^nP_n-1,\qquad P_n=\prod_{i=0}^{n-1}X_i^{d-1}.
$$

It is the chain rule, not a trace formula that needs separable periodic
points. When $p\mid d$, it specializes correctly to $F_n'=-1$.

## 2. Leading digit detector, including composite degrees: PASS

Let $D$ be the positive leading degree of a normal polynomial and let
$m=\lfloor\log_dD\rfloor$. The first and last base-$d$ digits of
$D$ are both nonzero: the first by $d\nmid D$, the last by the
definition of $m$.

A local forward reduction of $X_i^r$ for $r\le D$ stays in the
window of $m+1$ sites when those sites have weights $1,d,\ldots,d^m$.
Every constant choice strictly loses weight. Reaching a reducible
$d$th power at the final site would require weight at least
$d^{m+1}>D$, so no untracked carry leaves that window.

For $n>2m$, the only such cyclic window containing both target endpoints
$0,m$ is $[0,m]$. For $m=0$, the window is a singleton and the
same unique-source statement holds. The unique no-constant reduction
branch supplies the leading digit monomial with coefficient one;
all lower terms have insufficient weight. Hence its coefficient in
$H_n(v)$ is exactly $a_D$.

This reasoning concerns integer place values and digit exponents, not
prime-base arithmetic. Composite $d$, digits greater than one, and
characteristic-$p$ cancellation of other branches do not invalidate it.

## 3. Weighted circuit and the final source digit: PASS

For a normal positive exponent $r\le M$, set
$L=\lfloor\log_dM\rfloor+1$. The expansion of $P_nX_i^r$ uses

$$
t_0=r,\quad
b_s=(d-1+t_s)\bmod d,\quad
q_s=\left\lfloor\frac{d-1+t_s}{d}\right\rfloor,
\quad 0\le t_{s+1}\le q_s.
$$

The binomial weights are exactly those in the local defining relation.
All paths are finite, and zero-weight paths are retained. The induction

$$
t_s\le1+\frac{r-1}{d^s}
$$

gives $t_L\le1$, because $d^L>M-1$. States zero and one cannot
grow again, so the final carry is at most one.

The crucial higher-degree boundary is checked correctly:

$$
b_0=(r-1)\bmod d\le d-2,\qquad b_0+t_n\le d-1.
$$

The final carry therefore fits at the source without a second circuit.
The final source digit is the sum $b_0+t_n$, not merely a Boolean
support bit. All other sites retain their exact digit $b_s$. The
authored expansion consequently gives actual digit-basis coefficients.

This also handles the auxiliary endpoint $n=L=1$: then $M<d$ and
$1\le r<d$, so the one-variable identity is
$X_0^{d-1+r}=X_0^r-cX_0^{r-1}$ in the cyclic quotient. Its
exponents are already legal digits. The stabilization argument itself
uses the larger bound $n\ge3m+4$.

## 4. Source localization and full-digit bijection: PASS

For a nonzero target digit vector supported in $[0,m]$, let $E$ be
its nonzero support. If neither the source nor its first $L-1$
successors belongs to $E$, the final source digit is zero. This is
the integer equality $b_0+t_n=0$, which forces both $b_0=0$ and
$t_n=0$. The initial nonsource outputs are also zero.

At time $L$ the state is zero or one. In state zero all subsequent
digits are $d-1>0$. In state one the path must eventually drop to
zero to have final carry zero. Dropping only at the last processed
site would leave the entire target zero, contradicting its nonzero
support. Thus in either case the last processed site has digit
$d-1$, and the predecessor of the source belongs to $E$.

This proves the exact source inclusion

$$
i\in\bigcup_{s=0}^{L-1}(E-s)\cup(E+1)
\subseteq[-m,m+1]\pmod n.
$$

For $n\ge3m+4$, possible sources lie in the disjoint blocks
$[0,m+1]\cup[n-m,n-1]$. The upper block is empty when $m=0$.
Digit $d-1$ is a positive exponent for every integer $d\ge2$;
it is not replaced by its residue as a scalar in $k$.

With $j=2m+2$, the sites $j,j+1$ are outside the target and source
blocks. Every localized source is at forward distance at least $L$
from $j$, so the incoming state there is at most one. The two zero
output digits force the transition at $j$ to be $1\to1$, of
weight one. Inserting another such site after $j$ preserves all old
transitions in cyclic source order, the initial and final carries,
the full source digit, every other target digit, and the weight.

Conversely, at level $n+1$ the inserted site and its successor are
outside the source and target sets. The same distance and two-output
arguments force the inserted transition to be $1\to1$. Deleting
it is valid. The source blocks relabel exactly into each other,
and a new source at the inserted site cannot produce the target.

These operations are inverse on all source/path pairs, including
wrapping sources and zero-weight paths. The proof preserves arbitrary
target digits, not only support. Each normal monomial satisfies the
same coefficient equality, so all lower normal terms and cancellations
are retained after summation. Constants contribute $na_0P_n$, which
has zero coefficient at a nonzero short target.

The stabilization lemma therefore holds for every integer $d\ge2$
independently of its residue modulo $p$. The later Jacobian comparison,
not this lemma, has the exceptional-congruence limitation.

## 5. Explicit higher-digit boundary check: PASS

As a supplementary symbolic hand check, take $d=3$, $m=0$,
$v=a_0+a_1x+a_2x^2$, and $n\ge2$. For target $X_0$, source $0$
with exponent one and no drop contributes $a_1$. Source $0$ with
exponent two and a drop only at the last site contributes $-ca_2$.
For target $X_0^2$, source $0$ with exponent two and no drop contributes
$a_2$; source $1$ with exponent one, dropping immediately before site
$0$, contributes $-ca_1$. Localization and the source digit exclude
other paths. Thus

$$
[X_0](P_nH_n(v))=a_1-ca_2,\qquad
[X_0^2](P_nH_n(v))=a_2-ca_1.
$$

This verifies a digit greater than one and is valid also in
characteristic three. It agrees with, but does not replace, the full
bijection proof. No mathematical program was used for this check.

## 6. Ordinary-cycle theorem in both branches: PASS

For $p\nmid d(d-1)$, ordinary primitive-cycle vanishing implies
vanishing of the complete return sum at every root of every $F_n$.
At a root of multiplicity $e$, the derivative has order at least
$e-1$, including when $p\mid e$. Multiplication by the root-vanishing
return sum therefore proves the necessary divisibility and Jacobian
annihilation. No converse at one level is invoked.

For a positive normal leading degree, the digit detector and stabilization
give, at two adjacent levels,

$$
d^nC_n=a_D,\qquad d^{n+1}C_n=a_D.
$$

Subtracting $d$ times the first equality from the second forces
$(d-1)a_D=0$. The hypothesis $p\nmid d-1$ excludes this for a
nonzero leading coefficient. A constant remainder is zero at an
ordinary fixed point. Telescoping gives the reverse inclusion.

For $p\mid d$, the derivative is $F_n'=-1$, so every return
polynomial is squarefree. Ordinary-root vanishing therefore gives
$H_n(v)=0$ directly in the full algebra. The leading digit detector
excludes every positive-degree normal part, and a fixed point excludes
constants. This branch is independent of the carry stabilization.
It does not replace the native map by a Frobenius clock.

These branches cover exactly the stated range $d\not\equiv1\pmod p$.
The original all-odd-prime quadratic case is contained without change.

## 7. Finite certificate, constants, and wild periods: PASS

Coboundaries telescope to zero modulo $F_j$, so they satisfy both
types of test. Ordinary-root vanishing implies derivative divisibility
by the same multiplicity argument. Conversely, normalization preserves
the test and does not increase degree. The chosen two levels meet
both the leading-digit and stabilization bounds for every possible
positive normal remainder of degree at most $M$.

The carry branch excludes that remainder by the adjacent comparison;
the $p\mid d$ branch excludes it by $F_j'=-1$ and the digit detector
at either level. A constant remainder $a_0$ would give
$F_j\mid ja_0F_j'$. In either branch $F_j'$ is a nonzero polynomial
of degree below $\deg F_j$, so $ja_0=0$. Applying this at $n,n+1$
forces $a_0=0$. This covers constant inputs and the explicitly included
zero polynomial; no logarithm of degree zero is taken.

If an ordinary-root test fails at a root of primitive period $r\mid j$,
then

$$
0\ne\widetilde H_j(h)(a)=(j/r)S_h(O).
$$

The primitive sum is nonzero because the product is nonzero. There
is no division by a period or by $j/r$ in the field. Wild primitive
periods and levels divisible by $p$ are not discarded. The tests
are full return sums over every ordinary root, not merely exact-period
tests at lengths $n$ and $n+1$.

Finally, $d^{\lfloor\log_dM\rfloor}\le M$ gives
$d^{n+1}=d^{3\lfloor\log_dM\rfloor+5}\le d^5M^3$.
This bounds the two iterate polynomials as stated, without claiming
the same bound for every intermediate expression or running time.

## 8. Excluded congruence and verification boundary: PASS

For $d\equiv1\pmod p$, $c=0$, $h=x$, put
$R_n=x^{d^n-1}-1$. The exact identities are $F_n=xR_n$ and
$F_n'=R_n$. Since every $\widetilde H_n(x)$ is divisible by $x$,
every Jacobian divisibility holds. However, the ordinary fixed point
$1$ has sum one, and $x$ is not a coboundary by the normal-form degree
argument. This proves all-level Jacobian blindness in the excluded
range. It neither proves nor refutes the kernel theorem from ordinary
cycle sums in that range.

No missing hypothesis, unproved transfer existence, reduced-quotient
coefficient functional, multiplicity-growth estimate, or infinite-tail
limit is used. The complete mathematical claim survives unchanged.
External source assessment remains the coordinator's separate task;
this review does not award novelty, paper admission, or a target
arithmetic grade. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.

Work receipt: full proof and relevant local-scope reading, direct hand
derivation and boundary checking, and read-only integrity hashes only.
No mathematical execution, finite-field census, external model/API call,
new subagent, Git operation, frozen-file edit, shared-state edit,
manuscript edit, or PDF build was performed. The only new workspace
write by this review is this file.
