# Eighth-pass coordinator adjudication

2026-09-08 UTC. The unchanged C419–C423 batch now has
**four admitted complete contracts: M1, AS2, IR1 and P7**.
One substantial independent contract is still missing. There are
**zero new manuscripts, PDFs, assigned paper numbers or formal
Route-A evaluations**. This is a research checkpoint, not the
authorized five-paper delivery.

The [frozen plan](PLAN.md) continued four original questions. It did
not authorize four smaller replacement contracts, renewed testing of
accepted proofs, or Git writes. All four bounded attempts are complete
for this pass; an unresolved original question is not reported solved
merely because its new helper passed review.

## Dispositions

| Original question | Eighth-pass result | Admission decision |
| --- | --- | --- |
| P7, all-state finite-field q-Painlevé I upper bound | Full original bound proved, including every allowed characteristic, all parameter orders, seven native branches and singular finite fibres; nonauthor review PASS | **ADMIT ONE COMPLETE CONTRACT** after the coordinator's separate source/increment check |
| AY7, all-integer-parameter Adler–Yamilov structural atlas | Uniform ordinary rational native-period bound $N\le24$ for nonzero states and nonzero integer parameter, plus exact infinite six-cycle and eight-cycle controls; helper review PASS | **HELPER ONLY; FULL INTEGRAL ATLAS NOT CLOSED** |
| TR7, strong totally-real height-gap classification | Effective zero-gap witnesses for every rational $c\le-16$, an explicit gap for every rational $c>1$, and a qualitative zero-gap-to-real-support implication; helper review PASS | **HELPERS ONLY; FULL RATIONAL-PARAMETER CLASSIFICATION NOT CLOSED** |
| FC7, cancellation on every long native finite-field cycle | Exact first three ambient lag correlations and an explicit logarithmic-shift bound, with all frequency degeneracies; helper review PASS | **HELPERS ONLY; ORIGINAL POWER-SAVING TARGET NOT CLOSED** |

## 1. P7: full original contract admitted

Inputs are the [original seven-branch contract](../continuation_round7/charp_scout/FROZEN_CONTRACTS.md#p7--finite-field-q-painlevé-i-uniform-native-periods),
[eighth-pass freeze](painleve/FROZEN_ATTEMPT.md), complete
[proof](painleve/PROOF_PACKAGE.md), [author ledger](painleve/SOURCE_LEDGER.md),
[nonauthor mathematical review](painleve_review/REVIEW.md), and the
coordinator's [source/increment decision](P7_SOURCE_CHECK.md).
The coordinator read all of these in full, not only their summaries.

For every $k=\mathbb F_q$, every $s,t_0\in k^*$ and
$r=\operatorname{ord}(s)$, every original ordinary state has least
native period $\ell$ satisfying

$$r\mid\ell,\qquad \frac{\ell}{r}\le q+1+2\sqrt q.$$

There is no prime-field, odd-characteristic, generic-fibre or
nonzero-exceptional-coordinate restriction. The seven branches and
phase clock are unchanged. This proves source Conjecture 1.2.A,
not the bin-distribution conjecture or a replacement model.

The root reconstruction checked the boundary/linear-equivalence logic,
uniform-pole argument, face endpoint obstruction, exact source-integral
pole, component multiplicities, normalization count and native clock.
The actual nonauthor review separately reconstructs every local map
extension, all seven inverse branches, the integer Picard calculation,
four face relations and the specialization argument in characteristics
two and three. It confirms no remaining mandatory mathematical repair.

The decisive geometric argument is that every integral curve disjoint
from the anticanonical eight-cycle $D$ has linear class $dD$; every
nonconstant regular function with pole $mD$ has $r\mid m$; and the
source integral has exact pole $rD$. Therefore every finite geometric
fibre has exactly one component, of multiplicity one. It is an integral,
reduced arithmetic-genus-one curve. Its singular point bound is at most
$q+2$, and a smooth fibre containing a state has the usual Hasse bound.
This covers exceptional states without assuming a conjectured
discriminant, translation structure or spectral identification.

The source/increment gate deducts the original map, domain, integral,
conjecture, Halphen framework and classical curve facts. The retained
increment is the all-characteristic, all-finite-fibre closure described
above, not merely “an integral exists, so Hasse applies.” It closes an
independent complete question absent from the inspected source theorems.
That is sufficient for this internal contract admission. The current
bounded literature search is not a worldwide novelty certificate;
the unavailable final journal body and unpublished related work remain
explicit access limits in the source check.

The review was not blind: the author discussed its mechanism and the
reviewer sent preliminary corroboration before reading the final file.
The reviewer did not author or edit the proof; its final full-file
report is the nonauthor check being credited. Equation (15)'s rendering,
the explicit denominator list and three trailing spaces were corrected;
the former two passages were rechecked by the mathematical reviewer,
and the last changes are whitespace only.

**P7 is the fourth admitted contract, not a fourth finished paper.**
No formal C-number or A2 grade has been allocated.

## 2. AY7: global period helper, not a structural atlas

The coordinator read the entire [proof](adler_yamilov/PROOF_PACKAGE.md),
[source audit](adler_yamilov/SOURCE_AUDIT.md), diagnostic protocol,
implementation, actual emitted output and
[execution receipt](adler_yamilov/DIAGNOSTIC_RECEIPT.md), and performed
the separate [nonauthor hand review](adler_yamilov/COORDINATOR_HELPER_REVIEW.md).
The reviewed mathematical proof does not rely on a finite census.

For each nonzero integer $k$, every nonzero ordinary rational periodic
state has

$$N=m\text{ or }2m,\qquad m\in\{3,4,5,6,7,8,9,10,12\},$$

so $N\le24$. The proof retains zero entries and singular quotient
fibres. It handles the origin and inherited $k=0$ pair swap separately.
The product quotient reduces to a cubic translation; rational torsion
limits its possible order, while the free rational scaling lift adds
at most a factor two. Quotient fixed/two-period cases and zero product
matrices are treated explicitly, not discarded.

The frozen diagnostic refuted origin-only rigidity. The subsequently
hand-derived six-cycle family works for every nonzero integer $k$,
including its zero-coordinate instances at $k=\pm1$. A true eight-cycle
at $k=4$, and its negative-parameter conjugate, are also checked.
These results do not identify every integral family or every allowed
parameter/scaling stratum; a list of possible periods is not a proof
that all occur or that the integral atlas has been exhausted.

The known quotient/lift mechanism and rational torsion theorem remain
credited external inputs. **No smaller replacement contract is admitted.**
The next mathematical requirement is the full all-parameter integral
family/divisibility classification, not another fixed-parameter box.

## 3. TR7: two effective regions and a qualitative reduction

The entire [proof](totally_real/PROOF_PACKAGE.md),
[source audit](totally_real/SOURCE_AUDIT.md) and freeze were read by
the coordinator. The separate
[nonauthor coordinator review](totally_real/COORDINATOR_HELPER_REVIEW.md)
contains hand rederivations and actual checks of the external height,
no-periodic-curve and equidistribution theorem hypotheses.

For the original map $F_c(x,y)=(y,y^2+c-x)$:

- Every rational $c\le-16$ has an exact terminating algorithm producing
  distinct nonperiodic totally-real points of positive total canonical
  height tending to zero, with the requested effective upper bound.
- Every rational $c>1$ has an explicit rational positive lower bound
  for all totally-real algebraic points, with no degree or denominator
  restriction.
- For any fixed rational $c$, zero nonperiodic height infimum forces
  Zariski density of small sublevels and full real support of the
  equilibrium measure. This last result is qualitative.

The kicked finite cyclic system has exactly $2^N$ real solutions,
which exhaust its finite reduced algebra; hence all conjugates are
real. An explicitly selected branch escapes after its endpoint kick,
establishing nonperiodicity, while a midpoint estimate gives the
decaying height. The positive-region proof combines two-sided escape
with the real second-difference inequality.

The earlier concern that generic equidistribution alone misses curve
concentration is now resolved for the stated implication, using
invariant Zariski saturation and the no-periodic-curve theorem.
It must not remain listed as an unproved helper. Nevertheless the
interval $-16<c\le1$, a converse support criterion, the full decision
procedure and general effective positive gap are unproved here.
Thus the **original TR7 classification remains unclosed**.
The algorithm is proved terminating but has not been implemented/run.

The coordinator suggested testing a kick before the author developed
the proof; the review is nonauthor but not blind or independent idea
discovery. This disclosure does not weaken the actual helper scope or
turn it into the entire parameter classification.

## 4. FC7: precise method boundary, not a negative answer

The coordinator authored the [proof](orbit_sums/PROOF_PACKAGE.md)
and [source audit](orbit_sums/SOURCE_AUDIT.md). The nonlinear-lane
agent independently rederived the entire package and wrote the
[254-line helper review](orbit_sums/INDEPENDENT_HELPER_REVIEW.md),
which the coordinator read in full. All stated helpers pass without
a mandatory mathematical correction.

For the fixed map $F_1(x,y)=(y,y^2+1-x)$, all odd primes and every
nonzero linear frequency, the first three completed ambient
correlations are determined exactly or sharply bounded. In particular,
the first lag has size $p^{3/2}$ on $r=-s\ne0$, refuting a uniform
$O(p)$ ambient-lag shortcut, not the original orbit-sum claim.
The third-lag case audit includes $p=3$ and both frequency axes.

The explicit long-shift consequence for $p\ge17$ is

$$|S|\le4p\sqrt{L/\log_2p}.$$

It provides only a logarithmic-scale improvement near maximal orbit
length and does not meet FC7's frozen $L\ge p^{1/2+\eta}$
power-saving target. The four-shift moment's leading ambient scale
also cannot supply that target. An upper-bound expression too large
to help is not a lower bound on an individual orbit sum.

The original broader 2010 paper body was not obtained. The later
primary paper's attribution of a generic logarithmic bound is read
and labelled as such, not as original-body verification. The separate
triangular slow-degree theorem has inapplicable hypotheses and is
not imported. The helper's hand proof does not depend on an unseen
2010 statement. **FC7 remains open here**, requiring a genuine estimate
on the native cycle or an unbounded-prime obstruction.

## 5. Actual review, source and execution receipts

All four complete/helper packages received substantive current-team
nonauthor checks of their stated scope. The coordinator read the two
delegate-authored full review reports and wrote the two separate
reviews above. AI-assisted internal review is not external or human
peer review. The unavailable named external GPT-5.4 MCP workflow did
not run; the repository-authorized current-team fallback was disclosed.

Fresh successful search-query submissions total **54**:

| Lane | Successful submissions |
| --- | ---: |
| Coordinator FC source lane | 17 |
| Coordinator P7 current-source/increment check | 9 |
| P7 author | 7 |
| AY author | 13 |
| TR author | 8 |
| Nonauthor reviews | 0 |

Additionally, one failed TR request contained three attempted
formulations whose actual delivery is unknown. The receipt is
**54 successful plus three attempted/unknown**, not an invented exact
total of 57. Direct source opens/finds, local searches and old queries
are not extra submissions. This is not globally exhaustive coverage.

Mathematical executions: **exactly one**, the AY diagnostic on the
twelve frozen inputs $k=\pm1,\ldots,\pm6$, with its declared
60-second CPU and 256-MiB limits. It exited successfully once;
no repair, extension or rerun occurred. Its counts were checked against
actual output, not independently computationally reconstructed.
The global proof uses none of those counts. P7, TR, FC and all reviews
ran zero mathematical programs. Static document/code checks are
recorded separately in the [documentation review](CHECKPOINT_DOCUMENTATION_REVIEW.md).
No old accepted proof, census or PDF build was rerun.

No GPU, paid model API, saved source PDF, manuscript build, release
manifest, formal evaluator invocation or Git write occurred.
The opening and closing read-only Git checks preserve the inherited
worktree; no fetch, staging, commit or push is claimed.

## 6. Current state and next gate

The current batch is **M1/AS2/IR1/P7: 4/5 complete admitted contracts**,
still missing one. Author files' pre-review pending language and the
seventh pass's earlier gap table remain historical snapshots; the
final reviews and this adjudication determine the current scope.
The fifth contract must close a substantial independent full question,
not relabel AY/TR/FC helpers or revive eliminated shortcuts. AS1's
all-depth radial result and AF5-C's completed short algorithm remain
preserved without reruns or changed admission.

The batch skill keeps the five-contract manuscript gate; novelty-check
separates prior ownership from the residual; proof-writer keeps
exceptional cases explicit. Bounded research-lit/ARS source verification
does not claim full-paper access where only selected sections were read.
No C424, Route B or new external publication activity is authorized here.
NO_BAD_EULER_OR_ROOT_NUMBER: source periods and fibre geometry establish
no target Euler factors, root numbers, automorphy, target-zero
correspondence or Hilbert–Pólya realization.
