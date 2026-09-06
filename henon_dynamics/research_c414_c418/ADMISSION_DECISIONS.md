# Research admission decisions for the authorized C414–C418 batch

Updated 2026-09-07. Coordinator-owned current decision record. This is not
the final five-contract paper plan, a formal Route A evaluation, or a release.
Author files and initial scout metadata retain their historical baseline
status; the adjudicated status is recorded here.

## Current tally

**3 substantive contracts admitted; 0 manuscripts/PDFs; 2 contracts still
needed before the five-paper plan can be frozen.** No C-number is assigned
to a reserve or companion. One result is not split by degree, characteristic,
residue class or analytic corollary. No target A1/A2 success is claimed.

## Admitted: full polynomial-point canonical-height distribution

Object: `H(x,y)=(y,f(y)-ax)` on `F_q[t]^2`, every prime power q, every
degree d>=2, every degree-d polynomial f over F_q and every nonzero a.
The observable is the point-height series `sum_P q^(-s hhat(P))` for the
sum of forward and backward canonical heights, normalized by log(q).
This is not the ordinary periodic-orbit zeta and not a series over all
rational-function points. Those boundaries remain fixed.

The independent increment is the exhaustive, disjoint all-orbit degree-valley
census and coefficient-uniform height distribution, with exact convergence
abscissa one, the complete aggregated simple/double pole divisor on `Re s>0`,
a meromorphic natural boundary at `Re s=0`, and a real-height counting
asymptotic retaining the fractional-part oscillation. Canonical-height
existence/scaling, local escape, and rational-cone methods are credited as
classical inputs; they are not counted as new theorems.

Primary evidence:

- [Complete proof baseline](spectral/HEIGHT_PROOF_PACKAGE.md), SHA256
  `fc2fd3acdcbd1695997cecf02aaf6024e224fb89918777775ac95111a77d7ae7`.
- [Corrected bounded source audit](spectral/HEIGHT_SOURCE_AUDIT.md), SHA256
  `32ded9aa931d95ccd5374b4df947b91c5b5a1a6efdd2495deab3883dfb9f13fc`.
- [Full independent proof/source review and affected-fix closure](arithmetic/REVIEW_HEIGHT_PROOF.md),
  SHA256 `e6437f12b739d68ef29116dd2775aa476732618b93802b9524cfb0fe1e55af6a`.
- [Auxiliary independent residue and exceptional-pole check](positive_characteristic/REVIEW_HEIGHT_RESIDUES.md).
- [Exact finite diagnostic receipt](spectral/HEIGHT_EXACT_CHECK_REPORT.md):
  eleven selected cases, 77,974 polynomial pairs; not the proof of the
  universal or infinite analytic assertions.

The coordinator read the entire independent review and its auxiliary check,
adjudicated the mathematical and ownership reasoning, and verified the
requested provenance corrections directly in the primary PDF text. The
source record now separates arXiv-header dates from internal manuscript
dates and attributes the height-zeta definition to Silverman's 1994 talk
via Takehira/Hsia while crediting Hsia's published development. The reviewer
checked only those affected rows afterward and closed both requests. The
mathematical baseline did not change and did not need a rerun.

Decision: **ADMITTED_BOUNDED_SUBSTANTIVE_CONTRACT**. The original Hsia text
and final Ingram/Takehira versions remain outside the actual text access;
this is a bounded ownership decision, not worldwide priority or publication
readiness. Internal model review is not human peer review. Writing, formal
evaluation and final reproducible PDF release remain future gates.

## Retained companion: congruence-compatible all-SL2 inverse theorem

The complete proof is mathematically coherent at its all-SL2 scope, including
nonhyperbolic boundary cases and one compatible nonlinear profinite conjugacy.
The coordinator's [independent review](REVIEW_ARITHMETIC_ROOT.md) found no
blocking defect and reproduced the new finite orbit-tree diagnostic once.

Decision: **UNADMITTED_COMPANION**. After the old census quotient, BRW
classification and general orbit-tree/LTE inputs are deducted, the remaining
homogeneous dyadic calculation and its direct operator consequences do not
meet this batch's substantial-independent-paper gate. The older BF source
access limit remains. Correctness is retained; no claim that the exact
residual is known verbatim is made. The author accepted this disposition.

## Admitted: full degree-2p resonant Hénon–Frobenius coefficient space

For every odd prime p, every q=p^e with e>=3, every degree-2p polynomial
g over F_q and every nonzero determinant a, fix
`H=(y,y^q+g(y)-ax)` and the single map `S=H^(-1) Phi_q` on the whole
geometric affine plane. The observable is the ordinary fixed-point count
of every positive iterate of S, not forward periodic points of H on a
fixed finite extension or the generic inverse tree.

The high-support branch is classified by the largest nonzero exponent
between p+2 and 2p-1. The complementary low-support branch, including an
arbitrary y^(p+1) coefficient and every lower coefficient, is closed by a
finite two-term invariant in the perfected polynomial ring. Semilinear
coefficient descent gives exact all-height leading degrees and nonzero
coefficients, and hence the complete reduced counts
`N_n=q^(2n-w)D_w`, with `w=p^v_p(n)` and the two explicit D formulas.
No all-inseparable-degree theorem is inferred from this precise family.

Primary evidence:

- [Full family proof](positive_characteristic/FULL_DEGREE_2P_PROOF.md),
  SHA256 `683f4212a1f405fc4d2d5c67ba88e00a34595fb4172a25f1cdad9604841317f5`.
- [Source and ownership record](positive_characteristic/SOURCE_AUDIT.md),
  SHA256 `670b5e33dcee25b230589d68da750f737b2162616fd9b6b439bd3ec44e84630e`.
- [Independent full proof/source/substance review and revision closure](arithmetic/REVIEW_CHARP_PROOF.md),
  SHA256 `2b45469507c55cd49a93b8ae3e666585ab2758781ca2e15192dd31c6a5ab4412`.

The coordinator read the complete producer and review documents. Since the
coordinator contributed the all-odd-p generalization, the nonauthor review
was performed by the separate arithmetic agent, not replaced by coordinator
self-approval. The sole requested precision fix explicitly limits the
primitive p^a-root radial-tail statement to a>=1; the reviewer confirmed
the changed sentence and that no other proof bytes changed. The direct
argument covers non-prime-field coefficients and arbitrary perfected mixed
remainders; an expanded finite census is not its evidence.

Decision: **ADMITTED_BOUNDED_SUBSTANTIVE_CONTRACT**. The classical perfection
construction, C404's period conversion/reducedness/analytic mechanism,
strict-gap companion and pure-pth-power face are deducted. The actual
additional step resolves the mixed fractional tail that violates C404's
integer-remainder hypothesis and proves a complete coefficient threshold
uniformly in odd characteristic. This is one family contract, not separate
high/low, degree-six or source-zeta papers. The source comparison remains
bounded and no hidden-group exclusion, target arithmetic success or global
priority is claimed.

## Admitted: every rational cycle in the all-odd-degree discrete-sine family

The map is exactly `h_d=(y,-x+s_d(y))` with the central-factorial polynomial
printed in the proof, every odd degree `d>=3`, all of `Q^2`, and ordinary
iteration. Opposite or reversed cycles are not artificially identified.
The complete theorem gives the actual phase-corrected core and signed
boundary cycle graph, every primitive-cycle multiplicity, total point
counts, every fixed-point count and the resulting finite source-cycle zeta.

The family, rational/integer escape box, positive-phase bulk residue/period
table with 17 central exceptions, and growing-cycle existence are credited
to Kim–Krieger–Postolache–Szeto, especially Corollary 4.3, Proposition 5.2
and Theorem 5.1. Their short rederivations do not count as the increment.
What remains is exact all-radius clipping and full boundary closure,
including every escape alternative, multiplicity, long-chain uniqueness
and smallest admissible radius. This decides the exact all-family count
question rather than extending a finite degree census.

Primary evidence:

- [Complete proof](nonlinear_geometry/PROOF_PACKAGE.md), SHA256
  `a1a0c8fbd2ff8b1fbd3bc73606c8dd435c727fe914cbf907d9e55d7f8c9891e0`.
- [Corrected bounded source audit](nonlinear_geometry/SOURCE_AUDIT.md),
  SHA256 `3b89e0e5bf4586b55f270bfe3391bb8607e9eddd30e748e2b670d6a151deb3e9`.
- [Coordinator's full nonauthor proof/source review and closure](REVIEW_GEOMETRY_ROOT.md).
- [Independent symbolic-certificate review](positive_characteristic/REVIEW_GEOMETRY_CERTIFICATE.md),
  SHA256 `45761e4d9da58b56642946d2d1370696b760a6e52fda0ff4b30e9e6723735d06`.

The coordinator read both final reports completely. The certificate review
caused real repairs: exact endpoint complements, admissible-radius alias
exclusion, a central-orbit radius check and progression-derived counts
replaced assumed coverage and hand-entered cardinality checks. The final
code was reproduced once by the separate reviewer with assertions enabled;
an additional distinct check covered both central phases and 128 alias
equations. The remaining all-branch routing and growing-chain proof was
checked by the coordinator, not mislabeled as an automatic code conclusion.
Three prose/source precision requests were checked on the final inputs.

Decision: **ADMITTED_BOUNDED_SUBSTANTIVE_CONTRACT**. The accessed source's
date fields and version-specific count discrepancy remain explicit; no
claim is made about an unseen corrected/final version or worldwide priority.
All congruence classes and analytic corollaries count together as one
contract. No target arithmetic bridge, formal evaluation, manuscript or PDF
has been produced by this admission.

## Concrete shortfall after the bounded scout

The [independent 12-contract selection audit](arithmetic/REVIEW_BATCH_SHORTFALL.md),
SHA256 `731932cea613551ddbc1d5adb74873f3eb6f409d0dc1315e44668ea37c107c12`,
was read completely by the coordinator. Its reading baseline had two
admissions and geometry pending; the sole later decision is geometry's
one admission above, not a change to any other proof or disposition.
The final mutually exclusive tally is:

**3 admitted + 1 mathematically correct companion + 1 refuted inverse claim
with a short correct counterexample + 4 unclosed/no independent complete
increment + 3 classical collisions/insufficient residual = 12.**

No already-proved fourth or fifth substantive contract was overlooked.
The two remaining gaps need new complete arguments or genuinely independent
post-classical mechanisms, not typesetting, a larger finite table or more
pages. Per the batch selection gate, this is a research-shortfall checkpoint,
not a five-paper completion. Further work must still complete C414–C418;
no C419, Route B or renumbered reserve is authorized by this record.
