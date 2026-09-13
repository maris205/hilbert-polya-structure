# Review Summary

## Review layer completed

Two fresh adversarial candidate-level reviews returned GO after independent
proof and novelty challenges.  Their role was to decide whether the candidate
was sufficiently closed to enter source design.  They do not replace the fresh
independent review still required before a source lock.

No raw reviewer quotation or invented numerical score is recorded here.  The
summary records the issues tested and their mathematical disposition.

## Candidate selection

The support-size-`s>=2` two-transition theorem was selected as the dominant
claim.  The alternative complete support-one stratification was retained only
as PC3, a fully absorbed comparison theorem.  A counterexample-only project was
rejected as insufficiently standalone.

## Proof issues tested and resolved

| Audit issue | Resolution in the final source design |
|---|---|
| Correct Hénon normal form | Fixed as `H(x,y)=(P(x)+ay,x)` with `a!=0`; the inverse is displayed. |
| Ground field of Amoroso--Viada | Theorem 6.2 is acknowledged as algebraically closed.  The proof explicitly base-extends arbitrary characteristic-zero `K`; original solutions inject and rank does not increase. |
| Sparse-image variable rank | The tuple is a homomorphic image of `Gamma^2`, so its rank is at most `2r`. |
| First-local variable rank | `(z,u,v^(e_1),...,v^(e_s))` is an image of `Gamma^3`, so rank is at most `3r`. |
| Coefficients outside `Gamma` | They remain fixed coefficients of the linear equation and are never adjoined to the variable group. |
| Degenerate sparse-image solutions | All proper zero subsets of sizes `2,...,q-1` are unioned; their count is `2^q-q-2`, each with at most `d` roots. |
| Exhaustiveness of local degeneracy | The fixed `Z/U/M_j` convention gives exactly GZ, GU, R0, and R1. |
| Graph endpoint `J=[s]` | The `B_J` side has `s>=2` terms. |
| Graph endpoint `|J|=1` | The complementary side, including the constant, has `s>=2` terms. |
| R0 root degree | Nonzero roots are bounded by `e_maxJ-e_minJ` after factoring the lowest power. |
| R1 root degree | Roots of `c+B_J` are bounded by `e_maxJ`. |
| Vertical constant cancellation | If `c+a rho=0`, the second-step polynomial still has the `s>=2` nonconstant monomials. |
| Simultaneous zero subsums | Any available label may be selected; union over all labels intentionally overcounts. |
| Infinite torsion | AV is rank-based, and every remaining fiber uses an ordinary polynomial root bound in characteristic zero. |
| Component constant | `M(e)` is defined by two explicit subset sums; the closed form and crude inequality are checks only. |
| Support-one free chains | The nine adjacent transitions leave only `BA` and `CB`; compatible `CBA` is the sole three-label free chain; every fourth label closes. |
| PC3 sharpness coordinates | Correct recurrence order is `t^d,t,c,-t,(-t)^d` for `Q_t=(t,t^d)`. |

## Counterexample audit

The reviews required exact failures at every tempting boundary:

- `c=0`: `P=X^d+X`, `a=-1` gives an infinite two-transition chain.
- `a=0`: `P=-1+X+X^2` forgets the free second coordinate.
- `s=1`: the support-one `CBA` family makes `T_3` infinite.
- `T_1` for every `s>=2`: the rational family with `P(1)=0` gives an infinite
  rank-one example.

These examples are now part of the theorem package rather than informal
warnings.

## Citation and novelty audit

The literature freeze is 2026-08-17 and uses current primary sources.  The
exact Amoroso--Viada constant and algebraically closed domain were checked from
Theorem 6.2.  ESS remains historical context.

A previous local citation label for Krieger et al. was not inherited.  The
published source was rechecked: Theorem 1.7 is the monic `S`-integral
polynomial image bound; Theorem 1.8 is the local non-Archimedean
exceptional-coefficient valuation statement; Corollary 1.9 is its number-field
one-orbit consequence.  These are adjacent to, but do not imply, the
two-dimensional all-initial-state finite-rank theorem here.

Bell--Ghioca Theorem 1.1 was kept at its exact scope: one fixed orbit, finitely
generated subgroup, arithmetic progressions plus a zero-density residual, with
only that residual finite for regular maps; a Hénon torus restriction is
generally rational.  Ji--Xie--Zhang v2 Theorem 1.8 and Corollary 1.9 give
cyclotomic periodic-point non-density, not finiteness.  The incompatible
epsilon ranges and additional hypotheses between the front conditional results
and Vojta discussion in Mello--Yasufuku were recorded rather than merged.  Kim
et al. Theorems A and B were kept to their odd-degree and congruence-restricted
rational/integer constructions.  No direct collision was located.  The outcome
is a provisional novelty GO, never a priority assertion.

## Standalone and absorption audit

PC1 and PC2 form an independent theorem-and-sharpness pair.  PC3 is included
with its entire A/B/C proof, so no logical step depends on the local predecessor.
The predecessor is hash-identified, treated as provenance, and barred from
parallel external submission.

## Final disposition

- Novelty axis: **provisional GO** after bounded current search.
- Standalone axis: **GO** with PC1 dominant and PC3 absorbed.
- Proof-closure axis: **GO to independent source review**; no computation is
  needed.
- Lifecycle: **AUTHOR COMPLETE / PENDING INDEPENDENT SOURCE REVIEW**.

No manuscript, code, data, experiment, result generation, or submission is
authorized by this review summary.
