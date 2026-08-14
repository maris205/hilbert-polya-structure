# Experiment Report — SD-C28

## Outcome

The exact suite supports

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`

with `ROUTE_A_REJECTED`, Route B locked, and no target-zero data. The positive
result is sharp: a cyclic coefficient equal to one on every pure power and
zero on every mixed word has an exact finite projector realization and an
honest countable de Rham/Fredholm tensor. The ceiling is also sharp: finite
word traces semisimplify to one net color character per supplied label, and
the countable projector fiber is their direct sum.

## Raw exact data table

| Artifact | Rows | Result |
|---|---:|---|
| projector word ledger | 34,636 | all exact |
| radical word ledger | 15,029 | all exact |
| graded word ledger | 1,274 | all exact |
| Hankel/syntactic ledger | 8 | ranks exact |
| aggregate adversary | 34 | 32 aggregate passes; 2 wordwise witnesses |
| support incidence | 12 | all Euler identities exact |
| bar/Hochschild controls | 12 | all atomic H0 certificates exact |
| local de Rham controls | 72 | all chain/power/quotient checks exact |
| tensor de Rham words | 120 | all individual word supertraces exact |
| arbitrary inventories | 21 | all `PROVES_TOO_MUCH` |
| marker controls | 511 | all ownership checks exact |
| regression tests | 58 | 58/58 PASS |

These are deterministic exhaustive or theorem-certificate rows, not random
seeds; means, standard deviations, and relative performance deltas do not
apply.

## Finite selector and collapse

For `m` colors, `P_i=E_ii` gives

\[
 \operatorname{Tr}(P_{i_1}\cdots P_{i_r})=
 \begin{cases}1,&i_1=\cdots=i_r,\\0,&\text{otherwise}.\end{cases}
\]

All 34,636 frozen projector rows pass. The 15,029 radical rows replace these
matrices by populated, generally noncommuting upper-triangular extensions;
all traces remain exact. The 1,274 graded rows add a nontrivial common module
to both parities and a nonsplit even block coupling; the common character
cancels exactly. These controls show why the theorem concludes
semisimplification rather than literal simultaneous diagonalization.

For the character completion `f(empty)=m`, Hankel rank is exactly `m`; for
the literal nonempty language it is `m+1`. Every audited color count through
eight matches. Thus recognizable memory grows with inventory size. The
finite graded character theorem strengthens the generic trace-pairing bound:
after canceling common modules and dormant zero-action lines, one net
one-dimensional color character survives for every supplied label.

## Aggregate-only falsification

With `R_0=E_12`, `R_1=E_23`, and `R_2=E_31`, put the `R_i` sector in even
degree and its transpose in odd degree, alongside the atomic projectors. All
32 scalar-pencil power checks pass exactly for four signed weight fixtures.
Nevertheless,

\[
 \operatorname{Str}(A_0A_1A_2)=1,
 \qquad
 \operatorname{Str}(A_2A_1A_0)=-1.
\]

Therefore an abelianized determinant or aggregate power trace cannot certify
the selector. Individual cyclic words or oriented necklaces are mandatory.

## Support and homological controls

The reduced-support exterior fiber has superdimension
`(1-1)^(|S|-1)`, giving the desired coefficient in all twelve support rows.
For mixed support its cohomology is nonzero in both parities, and the fiber is
chosen only after the complete word support is known. It is an exact
word-indexed virtual coefficient, not a stationary escape.

The canonical stationary alternative is the separable color algebra
`C^m`. All idempotent multiplication and separability checks pass through
`m=12`, but `HH_0(C^m)=C^m` and positive Hochschild homology vanishes. The
homological survivor is exactly one line per supplied color.

## Holomorphic tensor and arbitrary inventories

All 72 local polynomial de Rham rows verify the chain identity, every power
supertrace, and the characteristic quotient. Tensoring with color projectors
then gives 120/120 exact individual word supertraces: pure repetitions retain
their weight powers and mixed words vanish before analytic tracing.

On a countable inventory, `T(a)=sum a_nP_n` is trace class for `a in l1`,
with trace norm `sum |a_n|` and determinant `product(1-za_n)`. At digit marker
`u=1` and weight `n^{-s}`, the honest domain includes `Re(s)>1`. This operator
is unitarily the direct sum of its color blocks. The 21 full-inventory
controls—prime, square, Fibonacci, all integer, matched random, matched hash,
and modular—use the same compiler, exact sums, and exact `z=1` products. Every
row is labeled `PROVES_TOO_MUCH`; prime selectivity credit is zero.

All 511 marker rows retain `u^ell(n)` and distinguish it from the completed
return marker `z`. The selector preserves a supplied marker but does not
derive one.

## Interpretation and implication

The observation is not that the selector fails: it succeeds exactly. The
interpretation is that exact all-repetition mixed-word deletion has a rigid
finite character cost. The implication for the research program is that
finite recognizable/bar/Hochschild memory is now closed as a non-atomic
repair of shared renewal. The smallest next experiment is a genuinely
infinite-dimensional, non-type-I cyclic trace derived from the factorization
source, with independent convergence, wordwise, marker, and non-equivalence
checks.

## Reproducibility and scope

The canonical runner executes generator, 58 tests, and analyzer twice under
`PYTHONHASHSEED=0`, compares code/generated-result bytes, audits strict Route
schema and scientific predicates, removes caches, and freezes a SHA-256
ledger. The certificate is scoped to code and generated results, not writer
documents.

No universal infinite-dimensional semisimplification theorem, analytic
continuation, functional equation, self-adjoint carrier, critical-line
mechanism, RH implication, or Route-B object is claimed.
