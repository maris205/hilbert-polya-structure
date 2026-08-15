# Independent Source-Lock Review

Review date: 2026-08-14 UTC.

Verdict: **SOURCE_LOCK_PASS**.

This is a fresh, read-only mathematical, source, and novelty audit of Paper 9
at source-lock v2.  I derived the finite-field classification, product
identities, scalar obstruction, and convergence bounds independently before
opening the author's frozen synthesis.  I then checked every final frozen
document against that derivation and against current primary literature.  No
Paper-9 code was authored or run, no prime shell was enumerated, and no prime
table, generated prime array, numerical value of `s` or `log p`, or
Riemann-zero data was used.  This review is not a deployment pass, registered
execution, result review, or manuscript authorization.

## Final authority and binding checks

The final reviewed source-lock is

`662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`.

All six local design bindings reproduce exactly:

| Artifact | SHA-256 |
|---|---|
| `notes/RESEARCH_QUESTION.md` | `79339c412dc9df2d7babb3ff5b0bf19b5255a2ddc989ac72440200bfeb8563fc` |
| `notes/NOVELTY_ASSESSMENT.md` | `71de2f31ce196e06a4600f0fbc931e7ff707e8634f88fbb6e8d5698b3a4a75a0` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `cbf2f23b6ea3c24b97f731adb3be22c2a685e698f5eb7ea888f1c40b1c6ce8fa` |
| `notes/PROOF_PACKAGE.md` | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| `experiments/EXPERIMENT_PLAN.md` | `6a58e26935a3e406adfa723a2ab304880709667940b76b85707f82f844f94cc5` |
| `experiments/EXPERIMENT_TRACKER.md` | `00fc66f266b7a1ddcccc0b355ff7dbb6ea787f1d60319862dbd7d5da6262d0b9` |

The six declared Paper-8 upstream bindings also reproduce exactly: source
lock `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`,
proof package `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af`,
raw result `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0`,
result manifest `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`,
official result report
`4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d`,
and official validation report
`ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3`.
The final JSON parses successfully and has no duplicate object keys.

## Repair history

The first frozen candidate, source-lock
`fb6a090df356de4601ba48b05379ae8ad0791b48f871a79cea6b7feb0d41087f`,
used `prod_(ell divides q)` in the Jordan-totient formula without explicitly
restricting `ell` to prime divisors.  Read literally as a product over all
positive divisors, that notation is false (and already degenerates at
`q=4`).  I withheld PASS and requested the exact scope repair.  The author
changed only this point, made the prime-divisor restriction explicit in both
the proof and source lock, and refroze v2.  The corrected identity is
`J_2(q) = q^2 product_(prime ell dividing q) (1-ell^(-2))`.

The final proof hash and source-lock hash above contain that repair.  No
remaining defect from the v1 finding survives in v2.

## Independent mathematical audit

### Prime-shell classification and multiplicity

For `A=[[2,1],[1,1]]`, the characteristic polynomial is `X^2-3X+1`,
with discriminant `5`.

1. **Split odd primes `p != 5`: PASS.**  If `(5/p)=1`, then `A` is
   conjugate to `diag(lambda,lambda^(-1))`.  With
   `tau_p=ord(lambda)` dividing `p-1`, every nonzero vector has exact
   period `tau_p`, including vectors on either eigenline.  Thus, writing
   `h_p=(p-1)/tau_p`, one has
   `m_p=(p^2-1)/tau_p=(p+1)h_p`, with `2h_p` eigenline cycles and
   `(p-1)h_p` complement cycles.  In particular `m_p >= p+1`.  No
   maximal-order assumption is used.

2. **Inert odd primes: PASS.**  If `(5/p)=-1`, identify `F_p^2` with
   `F_(p^2)`.  The map is multiplication by an eigenvalue satisfying
   `lambda^p=lambda^(-1)`, so `tau_p` divides `p+1`.  Multiplication by
   `lambda^k` fixes one nonzero vector only when `lambda^k=1`, hence every
   nonzero vector again has exact period `tau_p`.  With
   `h_p=(p+1)/tau_p`, this gives `m_p=(p-1)h_p >= p-1`.

3. **Binary boundary `p=2`: PASS.**  The reduced characteristic polynomial
   is `X^2+X+1`; `A` has order three and no nonzero fixed vector.  The three
   nonzero points form one three-cycle, so `m_2=1`.

4. **Ramified boundary `p=5`: PASS.**  Setting `N=A+I` gives a nonzero
   rank-one nilpotent with `N^2=0` and `A=-I+N`.  The four nonzero vectors
   in `ker N` have exact period two.  For `Nv != 0`, the formula
   `A^k=(-1)^k I+k(-1)^(k-1)N` excludes every odd return and makes the least
   even return ten.  Hence the shell has two two-cycles and two ten-cycles,
   so `m_5=4`.

These four cases exhaust the primes and prove that `p=2` is the unique
single-orbit shell, while every odd prime satisfies `m_p >= p-1`.  The
frozen profiles at `p=2,3,5,7,11` agree with these formulas, but the source
correctly treats them as inherited, development-seen controls rather than
evidence for the all-prime theorem.

### The two products and their repetition ledgers

The source keeps two genuinely different constructions separate.  For the
point observable `L(x)=log p` on `V_p`, a primitive orbit of length `ell`
contributes `p^(-s r ell)/r` at its `r`-fold traversal.  Grouping the
fixed-point exponential therefore gives
`Z_raw,p(s)=product_(gamma in Gamma_p)(1-p^(-s|gamma|))^(-1)`.

Thus it is `(1-p^(-s tau_p))^(-m_p)` away from the ramified prime, while
at `p=5` it is `(1-5^(-2s))^(-2)(1-5^(-10s))^(-2)`.  By contrast,
assigning `log p` once to each primitive orbit by an external shell label
gives `Z_lab,p(s)=(1-p^(-s))^(-m_p)`, whose logarithmic coefficient at
repetition `r` is exactly `m_p/r`.
Dividing a raw orbit sum by the primitive period changes its label but does
not remove any of the `m_p` denominator factors.  All frozen documents
respect this semantic boundary.

### Fixed scalar denominator obstruction

For the explicitly frozen product `product_gamma(1-w_gamma z)^(-1)`, with
fixed scalar coefficients independent of `z`, equality to `(1-z)^(-1)`
would imply `product_gamma(1-w_gamma z)=1-z`.  If every weight is nonzero,
the left side has degree `m_p`; for odd `p`, `m_p>1`, so equality is
impossible.
If zero weights are admitted, equality forces the multiset
`{1,0,...,0}`.  The equivalent power-sum condition is
`sum_gamma w_gamma^r=1` for every `r>=1`; the tempting equal choice
`w_gamma=1/m_p` gives `m_p^(1-r)`, repairing only `r=1`.

The source properly limits this theorem to pure scalar denominator factors.
It does not exclude `z`-dependent weights, matrix-valued factors,
numerators, alternating products, transfer/Fredholm determinants, or
cohomological cancellation.  Finite scalar or Hölder-potential orbit weights
are covered only because their exponential weights are nonzero when placed
in this same frozen product form.

### Fractional normalization and composite shells

Since the primitive cycles partition `V_p`,
`sum_gamma |gamma|=p^2-1`, and therefore
`product_gamma (1-p^(-s))^(-|gamma|/(p^2-1))=(1-p^(-s))^(-1)`.

This identity is exact, but its outer exponents use the complete shell
cardinality; it is normalized finite counting, not an ordinary local scalar
weight.  The repaired `J_2(q)` formula shows that precisely the same
argument works for every exact additive-order-`q` shell and every
permutation of that shell.  The mechanism therefore has no intrinsic prime
specificity.  The locked conclusion `A0_FAIL_GLOBAL_NORMALIZATION_ONLY` is
the right one: normalization succeeds algebraically and is rejected only as
global and tautological, not as impossible.

### Safe global analytic bounds

For the label product, the first logarithmic terms and the lower bound
`m_p >= p-1` imply divergence for real `1<s<=2`; the same first terms
preclude absolute convergence when `1<Re(s)<=2`.  On the other hand
`m_p<=p^2-1`, and comparison with `sum_p p^(2-sigma)` proves absolute
convergence for `sigma=Re(s)>3`.  The proof uses no numerical evaluation.
It correctly makes no claim for `2<Re(s)<=3`, no exact
abscissa claim, and no continuation or zero statement.

### Centralizer and selector escape

The non-scalar centralizer is a real escape outside the degree theorem.  In
the inert case `F_(p^2)^x` acts transitively on the nonzero
shell; in the split case the diagonal centralizer has the two nonzero
eigenlines and their complement as three natural orbits; and at `p=5` the
Jordan centralizer separates `ker N minus {0}` from its complement.
A quotient may therefore collapse multiplicity after enriching the
construction.  The source neither constructs nor rules out such a quotient,
and it also notes that a quotient remains shell-dependent and receives its
prime label from the externally specified additive order.  Reserving this
question for Paper 10 is mathematically honest.  Likewise, selecting one
orbit gives one factor only by adding symmetry breaking and discarding
`m_p-1` cycles; no universal selector impossibility is asserted.

## Current primary-literature and novelty audit

The literature search was refreshed through 2026-08-14 and used primary
publisher or arXiv records.  Gaspari's 1994 prime-lattice paper is a direct
collision with the common-period and orbit-decomposition result.  Baake,
Neumärker, and Roberts (2013), especially Appendix A.1, directly records the
standard cat map's finite-lattice cycle polynomials, including the `p=2`
and `p=5` boundaries, and supplies the relevant symmetry context.  Baake,
Roberts, and Weiss (2008) already develops finite/rational-lattice Euler
products.  The standard primitive/repetition and weighted-zeta framework is
classical in Ruelle (1976) and Parry--Pollicott (1990).  Tan and Li's 2025
prime-power work strengthens the current finite-ring cycle collision, while
Chandra's 2026 preprint explicitly packages a finite permutation determinant
as a product over its cycles.

Primary records checked include
[Gaspari (1994)](https://doi.org/10.1016/0167-2789(94)90105-8),
[Baake--Roberts--Weiss (2008)](https://arxiv.org/abs/0808.3489),
[Baake--Neumärker--Roberts (2013)](https://doi.org/10.3934/dcds.2013.33.527),
[Ruelle (1976)](https://doi.org/10.1007/BF01403069),
[Parry--Pollicott (1990)](https://doi.org/10.24033/ast.28),
[Tan--Li (2025)](https://arxiv.org/abs/2506.20118), and
[Chandra (2026)](https://arxiv.org/abs/2607.24857).

No source located in this bounded search packages exactly the same
Riemann-local-factor failure audit, but almost all mathematical ingredients
have strong prior collisions.  Absence from a bounded search is not evidence
of priority.  The locked score of 2.5--3/10 and the decision
`GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY` are therefore well calibrated.  The
safe contribution is only the explicit juxtaposition of known shell
multiplicity, the raw-versus-label semantic distinction, and the scoped
scalar failure/tautological-normalization decision.  Claims of a new orbit
classification, new finite-lattice zeta theory, prime-generating cat map,
transfer determinant, Riemann model, or historical priority would be false
or unsupported and remain prohibited by the lock.

## Cross-document and execution-boundary audit

The research question, novelty assessment, claims matrix, proof package,
experiment plan, tracker, and v2 source lock agree on the theorem, product
semantics, nonzero scalar scope, composite normalization, safe analytic
strip, low-novelty position, and outside-theorem escapes.  Controls
K001--K012 cover the partition, binary and ramified boundaries, odd-prime
bound, split strata, product and repetition separation, equal-weight failure,
fractional identity, selector cost, analytic nonclaim, and escape boundary.
The future five-prime audit is explicitly a development-seen falsification
control and cannot prove the all-prime or analytic claims.

At final review time, the Paper-9 directory contained only the seven frozen
design files before this report: no candidate code, result artifact,
deployment authority, or registered claim existed.  Every planned run remains
`TODO_NOT_AUTHORIZED`.  The source lock requires a new explicit
implementation task and a fresh deployment review bound to this source-lock
and the future code-tree hashes before any registered audit.  This
`SOURCE_LOCK_PASS` closes the independent source-design gate only; it does
not authorize code execution, Route B, centralizer-quotient work, or
manuscript claims beyond the frozen scope.

## Blockers

None.  The sole v1 notation defect was repaired and rebound in v2.  The
final source lock is mathematically coherent, internally consistent,
correctly low-novelty, and safe to use as the authority for a later,
separately authorized implementation phase.
