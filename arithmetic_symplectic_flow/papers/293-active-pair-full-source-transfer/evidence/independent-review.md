# Independent internal review — full-source transfer and cylinder trace

Audit ID: ASFS-AUDIT-20260920-AFT01.
Candidate ID: ANG-20260920-APR01, unchanged from 288/289/291.
Date: 2026-09-20.
Status: OWNED TRANSFER; COFINAL CYLINDER TRACE MISMATCH — SCOPED ADVANCE / STOP.

## 1. Scope, bindings and actual review order

This ARS three-checkpoint review concerns the frozen classical transfer
on the entire locally constant compact-support space and the specified
finite observable traces. It does not construct a global Fredholm,
Hilbert/quantum or self-adjoint owner, or evaluate any formal Route.
Only this report was written; no scientific run or external lookup occurred.

Exact SHA-256 bindings:

- Original 293 candidate-card.md:
  ebd6c1c2a68ac1af187c93ea71e7c889ceb206d59c1b5b3e35bf1f372791c868.
- 288 candidate-card.md:
  cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78.
- 288 paper.md:
  b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8.
- 291 candidate-card.md:
  84e7abac8515301102e7df48f7ed80bcc57ef0a6f14fe4a3ee6ed10f0674ed35.
- 291 paper.md:
  7dd25c66e30d80a454f0a375c29caacf993280fa85231e82ec5358054ad3f366.
- Initial 293 manuscript, fully read, 292 lines:
  fc0aa6bb76991b59c7478f0a6271eaf3a89b675e9a3d2d5f4e4ef7e198d824ce.
- Updated manuscript with forward non-descent example, fully read, 298 lines:
  9610e27113a200cc79c12619faddebb271ae7076582c21b284a4b53992882e57.
- Final manuscript, after targeted terminology readback, 299 lines:
  1a089d81b80d9a3957d277e6c7076a2e5ad7aaac326d95bbb468f35ce966d074.

The entire card was read first. Raw transfer, trace, cofinal-kernel and
control findings were sent before any manuscript access. Previously
reviewed dependencies were hash-checked and pertinent branch/clock and
counting-normalization passages reread before the manuscript. The
original-card binding excludes any later administrative outcome appendix.

A bounded auxiliary received only the raw card to check congruence
kernels, low iterates and compatible limits. Its results arrived before
the completed raw checkpoint and were checked before integration.
Function-space, closed-root-path and owner analysis remained with the
main reviewer. The auxiliary read no manuscript and ran no computation.
Inherited same-model/shared-context execution is not external peer review,
cross-model verification, formal verification or independent-error evidence.
The separate author-side scout proposal was not audited or used here.

## 2. Checkpoint 1 — full transfer and finite observation

Each summand is an actual inverse branch, with weight u^(-s) from its
owned inverse-arrow clock. For input support R, u<=R and
v<=3u+w(u)-3<=4R-5, giving L_s V_(R,M) subset V_(4R,M).
Integer-affine inverse seeds preserve level M. Thus the maps are
continuous on each finite stage and hence on the stated locally convex
inductive limit. For each f, the parameter dependence is a finite sum
of entire coefficients u^(-s), with values in one finite stage.
No boundedness on an unspecified Banach completion is inferred.

E_M is conditional Haar averaging, with the factor M² compensating
the class mass M^(-2). It commutes with root cutoff. On V_(R,M),
the inverse action already stays at level M, so C=P_R L_s.
Ordinary algebraic trace has no additional factor M^(-2).
Finite cofactor differentiation of det(I-zC), followed by formal
integration, proves -log D=sum_(r>=1) z^r Tr(C^r)/r.
Here z records iterate number, not a new physical clock.

This does not require an autonomous forward map on residue classes.
At root (2,2), seeds (0,0) and (2,0) agree modulo 2 and both
have digit zero, but their forward seeds (0,0) and (0,1) disagree
modulo 2. The inverse branch is nevertheless an integer matrix and
has a well-defined finite observation action. This example was also
sent in the raw findings, before being added to the manuscript.

## 3. Checkpoint 1 — exact traces and decisive mismatch

In the indicator basis, a diagonal term is a closed root/branch path
and a fixed residue class of its composed inverse seed map.
Summing the unchanged root recurrence forces every digit and every
w(b_i) to vanish; cyclic first differences then vanish. The only
surviving root paths are constant prime roots, with zero branches.
Consequently, for all finite R,M and all r>=1,

    Tr(C_(R,M,s)^r)=sum_(p<=R) p^(-rs) kappa_(p,r)(M),
    kappa_(p,r)(M)=#ker(B_p^r-I modulo M).

This finite diagonal is not obtained by first taking full K² periodic
points. For A=B_p^r-I, the two real eigenvalues of B_p lie in
(0,1) and below -p, so det A is a nonzero integer. With positive
Smith factors d_1,d_2, the raw congruence check gives

    kappa(M)=gcd(M,d_1)gcd(M,d_2), d_1 d_2=|det A|.

Every cofinal divisibility refinement eventually includes both factors.
For each fixed p,r, the count therefore stabilizes at |det A|.
For fixed R,r this gives the finite sum of those weighted determinants.
In contrast, adjugate multiplication and integer injectivity on K
give ker(A:K²->K²)={0}. Kernel cardinality cannot be commuted with
this inverse limit. No field or integral-domain assumption on K is used.

At r=1, det(B_p-I)=1 and every kappa equals one. At r=2 the
Smith factors are (1,2p-1), so kappa=gcd(M,2p-1).
Thus R=2 and 3|M already give second trace 3*2^(-2s), rather
than the required 2^(-2s), although the first trace agrees.
The discrepancy changes the formal z² coefficient and persists cofinally.

For p=2,r=2, mod 3 has solutions (0,0),(1,2),(2,1), whereas
the mod-9 solutions (0,0),(3,6),(6,3) all reduce to zero mod 3.
The extra finite solutions do not lift to actual nonzero periodic
seeds or create additional source packets. This is an exact congruence
argument, not a scientific finite-modulus census or extrapolation.

## 4. Checkpoint 2 — manuscript comparison and controls

Both full manuscript versions agree with the raw conclusions. The
author's lattice-cokernel proof correctly bounds kappa by |det A|:
the finite cokernel is Z²/(A Z²+M Z²). If |det A| divides M,
the adjugate makes M A^(-1) integral, giving equality. This is a
valid alternative to the raw Smith proof.

The added measure duality is correct: branch substitution with inverse
IMAGE 1/b gives integral (L_s f)g = integral_D b^(1-s) f(g composed T).
At s=1 this is transfer compatibility for the actual partial map,
not a Hilbert adjoint, invariance claim, self-adjointness or trace.
The forward mod-2 example added in the second version is correct.

The sole requested correction was terminology in Section 6:
determinant and product have constant term one; their formal logarithms
have constant term zero. Targeted final readback confirms the correction.
No change to the operator, trace prescription or conclusion was needed.

## 5. Checkpoint 3 — strongest counterargument and verdict

M=1 is a genuine positive control: every kernel has one class, all
finite traces match, and D_(R,1)=product_(p<=R)(1-z p^(-s)).
The seed-constant subspace, union_R V_(R,1), is invariant under L_s.
It is legitimate but not cofinal in full V. Its possible future global
representations are not ruled out; their analytic domains and determinant
claims need their own proof. Fixed-R subspaces need not themselves be
invariant before compression.

Conversely, dividing the finite trace by M² gives zero for fixed R,r
under cofinal refinement, since the numerator is uniformly bounded.
Basis normalization does not change ordinary trace; dividing it is a
different functional. No unproved repetition-dependent correction is used.

**Verdict: no outstanding blocking issue or requested correction.**
Advance the actual full-source transfer construction; STOP this cofinal
cylinder-trace identification with ordinary orbit repetitions. The failure
is not a theorem about every Banach, distributional or quotient analytic
representation, nor a refutation of 291's scalar zeta. Naturalness remains
OPEN. No global trace/Fredholm, quantum, completed-Xi or formal Route
result is supplied; Route B remains NOT INVOKED. All source states,
earlier packages and paused 241/242 remain unchanged.
