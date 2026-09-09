# E8 independent review: cyclic carry stabilization and PC424-L

2026-09-09 UTC. Nonauthor mathematical review by E8, using the current
selected model and hand reasoning. This review was not derived from the
other independent review. No mathematical program or external model was
executed. First-pass and earlier-round artifacts remain read-only inputs.

## Decision and exact scope

**Mathematical status: PROVABLE AS STATED.** The complete A1 proof of
stabilization passes this review. Its application proves the original,
unchanged PC424-L equality, and its appended two-level finite-detection
corollary also passes. There is no unresolved mathematical repair request.

This is a mathematical review decision, not a source-priority clearance,
manuscript admission, evaluation, or new paper count. Local source
subtraction is checked below. Broader literature collision and coordinator
admission remain separate gates.

The exact reviewed claim is: for every odd prime $p$, every
$c\in k=\overline{\mathbb F}_p$, and $f(x)=x^2+c$,

$$
\{h\in k[x]:\sum_{a\in O}h(a)=0
  \text{ for every ordinary primitive }f\text{-orbit }O\}
=\{Q\circ f-Q:Q\in k[x]\}.
$$

Every distinct ordinary point is counted once, including periods
divisible by $p$. There is no restriction on $c$ or the polynomial degree,
no substitution of an iterate for the native one-step map, and no change
to the retained defect-classification alternative. The equality branch
is established, so that alternative is not needed.

## Reviewed version and dependencies

The fully read primary artifact is
[A1's proof package](../../a1_periodic_normal_form/PROOF_PACKAGE.md),
444 lines, SHA256
`06d0d06c1798b55d5a052b7ae3874bd176338ff31887a129b80041c5e1147450`.
This review includes its final Section 5, not only the earlier core draft.

The imported facts were checked against their actual source proofs:

- [Initial normal form](../../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md),
  Step 4, lines 128–149: $k[x]=B_c\oplus V$ with
  $V=k\oplus xk[x^2]$. Elimination does not increase degree.
- [Old cyclic proof](../../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md),
  Step 1, lines 75–112: the full algebra $A_n\simeq k[x]/(f^n-x)$
  has the squarefree monomial basis, and coboundaries have zero trace
  class in this algebra.
- The same old proof, Step 2, lines 114–175: if $v\in V$ has positive
  odd leading degree $D$, then $[P_{E_D}]H_n(v)=a_D$ for $n>2m$,
  where $m=\lfloor\log_2D\rfloor$ and $E_D$ is the binary support of $D$.
- The same old proof, Steps 3 and 5, lines 183–207 and 276–321:
  ordinary orbit vanishing implies $J_nH_n(v)=0$, with
  $J_n=2^nP_{\rm all}-1$; a converse at one level is false.
- [Frozen original continuation contract](../../../../research_c424_c428/continuation_round2/positive_characteristic/FROZEN_CONTRACTS.md),
  especially lines 8–35 and 57–85: the original quantifiers, ordinary
  orbit convention, subtraction obligations, and full-question gate.

The old cyclic proof has SHA256
`54ed0c693c1bcfee128b759a82b3dc09f828896450466706fba885653489371e`.
The initial normal-form proof has SHA256
`d4a451c0596f04cc41f9272769026036898e41d6451f24d5c317bcfbca3697d4`.

## Claim dependency audit

The new mathematical step is the equality

$$
[P_E]\left(P_{\rm all}\sum_{i=0}^{n-1}v(X_i)\right)
=
[P_E]\left(P_{\rm all}\sum_{i=0}^{n}v(X_i)\right),
\qquad n\ge3m+4,
$$

with the left expression in $A_n$ and the right expression in $A_{n+1}$,
for every nonempty $E\subseteq[0,m]$ and every $v\in V$ of degree at most
$D$. The theorem uses $E=E_D$.

The reviewed chain is exact one-circuit reduction, then source
localization, then a weight-preserving insertion/deletion bijection,
then two adjacent Jacobian identities. These are distinct implications;
the proof does not infer reduced-root detection from full-scheme
nonvanishing at one level.

## 1. One-circuit reduction: PASS

For odd $d\le D$ and $L=m+1$, the authored states satisfy

$$
t_0=d,\qquad
0\le t_{s+1}\le\left\lfloor\frac{1+t_s}{2}\right\rfloor,
\qquad
t_s\le1+\frac{d-1}{2^s}.
$$

The last inequality is preserved at each step. Since $2^L>D-1$,
$t_L\le1$, and subsequent states cannot grow. The binomial expansion
of $X^{1+t_s}$ using $X^2=X_{\rm next}-c$ gives the stated weights
exactly. Finite path sums include zero weights, so characteristic-$p$
binomial cancellation and $c=0$ are both retained.

The cyclic boundary is valid: the first output bit is zero because $d$
is odd. The final incoming factor at the source has exponent $t_n\le1$,
so it does not collide with a retained source exponent. Every other
processed site has its recorded bit in $\{0,1\}$. One circuit therefore
really yields squarefree monomials without an omitted second reduction.

This proof also covers the auxiliary endpoint $n=L$. When $D=1$ and
$n=L=1$, it reads $X_0^2=X_0-c$, with the outgoing variable identified
with the source. No distinct-site assumption fails there. The theorem
itself uses the safer range $n\ge3m+4$.

## 2. Source localization: PASS

Consider a target path for nonempty $E\subseteq[0,m]$. If the source
is not in $E$ and none of its first $L-1$ successors is in $E$, then
the final carry is zero and those initial output bits are zero.
At step $L$, the state is either zero or one.

If it is zero, every later output bit is one, and $n\ge L+1$ ensures
that the last site exists in this range. If it is one, reaching final
carry zero requires a $1\to0$ transition. A drop only at the last
site would leave the entire final support empty. Since $E$ is nonempty,
the drop must occur earlier, again making the last output bit one.
Thus in either case the predecessor of the source lies in $E$.

It follows that every source belongs to

$$
\bigcup_{s=0}^{L-1}(E-s)\ \cup\ (E+1)
\subseteq[-m,m+1]\pmod n.
$$

In the stabilization range this is contained in the disjoint blocks
$I_n=[0,m+1]\cup[n-m,n-1]$. The upper block is empty for $m=0$.
The reasoning does not assume the path weight is nonzero, so it
localizes the entire finite path set required for the later bijection.

## 3. Insertion and deletion: PASS

Put $j=2m+2$. For $n\ge3m+4$, the sites $j,j+1$ lie outside both
the target and the possible source set. From either source block,
the forward cyclic distance to $j$ is at least $L$. Consequently
the incoming state at $j$ is at most one. Its zero output forces
incoming state one; the next site's zero output forces outgoing
state one. The transition at $j$ is therefore exactly $1\to1$ with
weight one.

Insert a zero-output $1\to1$ site after $j$, relabeling later old
indices upwards by one. This keeps the initial state, all old
transitions in cyclic source order, the final carry, the special
source exponent, the target, and the product of weights unchanged.
The source relabeling maps the two blocks of $I_n$ exactly onto
the corresponding blocks of $I_{n+1}$.

For the inverse, every contributing longer path again has localized
source. The inserted site $j+1$ and its successor $j+2$ are neither
source nor target, including the minimal permitted value of $n$.
The cyclic distance estimate forces incoming state at most one;
the two zero outputs force the deleted transition to be $1\to1$.
Removing it concatenates equal boundary states and gives a valid
shorter path. The newly available source at $j+1$ cannot contribute,
because it lies outside $I_{n+1}$.

Deletion and insertion are inverse on all source/path pairs, not only
on paths with a chosen source or nonzero weight. This addresses both
possible wrapping sources and the additional summand at level $n+1$.

## 4. Lower terms and boundary checks: PASS

The same proof applies separately to every odd $d\le D$, using the
same $m,L,j$ and source bounds. Summing with coefficients therefore
preserves all lower-degree contributions and their cancellations.
The constant contribution is $na_0P_{\rm all}$, whose coefficient at
a nonempty short target is zero because $n>m+1$.

As a hand check, for $D=1$, $m=0$, and target $E=\{0\}$, the only
possible sources are $0$ and $1$. For $n\ge2$, the first has the
all-$1\to1$ path of weight one. The second has a unique path that
drops immediately before reaching site $0$, of weight $-c$.
Thus the coefficient for $v=a_0+a_1x$ is $a_1(1-c)$, independent
of $n$. This is consistent with, but not a substitute for, the
general bijection. The theorem's $m=0$ threshold is $n\ge4$.

No argument assumes that $F_n$ is squarefree, that $p$ does not divide
$n$, that a binomial weight survives modulo $p$, or that $c$ avoids
a parabolic parameter. Root multiplicities are never bounded or divided.

## 5. Closure of the original theorem: PASS

Normalize $h=\Delta Q+v$. Telescoping preserves membership in $K_c$.
If $v$ has positive degree $D$, ordinary-root vanishing gives
$J_nH_n(v)=0$ at every level. The required root-multiplicity argument
is valid even when a multiplicity is divisible by $p$: differentiation
has vanishing order at least one less than the original multiplicity.

At two adjacent levels with $n\ge3m+4$, the imported leading
coefficient and new stabilization give

$$
2^n C_n-a_D=0,\qquad
2^{n+1} C_n-a_D=0.
$$

Subtracting twice the first equation from the second yields $a_D=0$.
The subtraction is valid in the stated field and divides by no integer.
This excludes every positive-degree normal defect. A constant normal
defect vanishes on a fixed point of $f$, which exists over $k$; hence
it is zero. The reverse inclusion is telescoping. All original
quantifiers and ordinary primitive periods survive unchanged.

The old characteristic-three, $c=0$, level-six Jacobian counterexample
does not contradict this argument: it invalidates a one-level
converse, whereas the present proof uses two consecutive levels and
a degree-dependent stable coefficient. No such converse is invoked.

## 6. Appended finite-detection corollary: PASS

For $M\ge1$, $\deg h\le M$, and
$n=3\lfloor\log_2M\rfloor+4$, the following are equivalent:
polynomial coboundary; derivative divisibility at both $n,n+1$;
ordinary-root return-sum vanishing at both $n,n+1$.

Coboundaries telescope modulo $F_j$. Ordinary-root vanishing implies
the derivative divisibility by the same valid multiplicity argument.
For the reverse implication, normalization does not increase degree,
so the chosen two levels meet the stabilization threshold of every
possible positive-degree remainder. The preceding subtraction excludes
such a remainder without assuming all-level orbit vanishing.

For a constant remainder $a_0$, the two divisibilities reduce to
$F_j\mid j a_0F_j'$. In odd characteristic, $F_j'$ has degree
$2^j-1$ and nonzero leading coefficient $2^j$, strictly below
$\deg F_j$. Therefore $j a_0=0$ at each level, and consecutive
levels force $a_0=0$. This also covers constant or zero input $h$.

Failure of an ordinary-root return-sum test produces a primitive
orbit of some length $r\mid j$ with

$$
0\ne\widetilde H_j(h)(a)=(j/r)S_h(O).
$$

Nonzero product implies $S_h(O)\ne0$ without dividing in $k$.
Thus a detecting primitive period is at most
$3\lfloor\log_2M\rfloor+5$. The certificate polynomials have degree
at most $2^{n+1}=32(2^{\lfloor\log_2M\rfloor})^3\le32M^3$.
The tests concern every root of the two return polynomials, not only
primitive cycles of exact lengths $n$ and $n+1$.

## Source subtraction, remaining gates, and work receipt

The new mechanism is stabilization of a binary coefficient after
multiplication by $P_{\rm all}$, with an explicit cross-level path
bijection. The old package already had the full cyclic basis,
leading coefficient of $H_n(v)$, and necessary Jacobian annihilation;
it explicitly left simultaneous kernel exclusion unresolved. The
present proof supplies that missing cross-level step. It is not
another $c=0$ necklace proof or a renamed full-scheme nonvanishing
lemma. The finite-detection result is a same-theorem consequence,
not an independent paper question.

There is no reliance on formal Böttcher evaluation at finite points,
an uncontrolled Laurent tail, multiplicity-growth estimates, existence
of an algebraic transfer, or finite Frobenius dependence. None of
those earlier unresolved mechanisms is silently promoted to a theorem.

Local subtraction passes. This review does not assert global novelty
or clearance against every external source. Those source checks and
the final original-contract admission belong to the coordinator's
remaining gates. No target Euler factor, root number, automorphy,
target-zero statement, or Hilbert–Pólya claim follows from this review.

Verification used full-file reading, source comparison, symbolic hand
reasoning, and read-only hashes. No mathematical execution, finite-field
census, paid API, Git operation, old-artifact edit, shared-state edit,
manuscript edit, PDF build, or additional subagent was performed. The
only new workspace write by this review is this file.
