# Source lock — Paper 30 / SD-C32

Lock date: 2026-08-14 UTC

## Frozen research authority

| Artifact | SHA-256 | Status |
|---|---|---|
| `/tmp/paper30_research_package.md` | `98b58fd77ac6bd3fd7aa5c1f662d2203a34fa2891c631fad36ed8c9a19f45b1d` | frozen mathematical, analytic, literature, and claim-boundary authority |
| `/tmp/paper30_coherence_prototype/SHA256SUMS.txt` | `65d382a3be32c347636f789194146396b3d7498dd1fa23fa3db364df3450ac52` | frozen first-prototype ledger; research input only |
| `EXPERIMENT_REPORT.md` | `c9ca998826d8556c8c63c9f7c3dd029d03753bfc7366c982a2fa76ef7a0b1a1c` | frozen exact-report authority after root EOF/whitespace hygiene; writer did not modify it |
| `results/SHA256SUMS.txt` | `99be21c67f12234d5b5b6ae854bd2c6695aabebec953fa8fe217bce452045bd0` | canonical 31-entry code/result authority ledger; all entries verify |
| `results/double_run_certificate.json` | `7eef85e74ec0785cf30b19e81aee35b1c9753ad1f51f5fca6ea65568466dea1c` | two fresh 17-artifact runs byte-identical |
| `results/integrity_audit.json` | `48ed4bd36205888cac4b9200a93a78f78ae851ac9890f8e8d4f8eecc2bfd25b2` | source, route, scientific, LF/control-byte/cache, and ledger audit PASS |
| `results/evaluation.json` | `5296832adbac5830089e75bb3711918d7ca665e031468326ae3308103aa84e35` | independent evaluator 1616/1616 PASS |
| `results/test_report.json` | `eccb97b47d5446b4279cce5df75de924ca3b16d401b8f1e2259edc58b86756ac` | regression suite 28/28 PASS |
| `results/clone_certificate.json` | `82ef019f1054ade3e3417fb3807e9663781094b077954139c6495273c508052d` | finite transported-clone certificate |
| `results/summary.json` | `e27e9be1e6516a6bd009af1e6d919d91dbf20ca2a62c5c63e3d09eb75f8dcd4a` | frozen SD-C32 decision summary |

The independent authority package is final.  It reports 28/28 regression
tests, 1616/1616 independent evaluator checks, 17 generated artifacts per
fresh run, byte-identical fresh runs, and a 31-entry authority ledger.  The
double-run aggregate is
`b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316`.
The theorem itself is proved from the first row and does not depend on finite
testing; the integrated package is canonical implementation evidence.

## Frozen exact census

| Inventory | Atoms | qualified pairs | qualified triples |
|---|---:|---:|---:|
| integer divisibility, cutoff 12 | 5 | 10 | 10 |
| integer divisibility, cutoff 18 | 7 | 21 | 35 |
| integer divisibility, cutoff 30 | 10 | 45 | 120 |
| mutated cover, object 6 promoted | 8 | 3 | 0 |
| composite-only inventory | 3 | 0 | 0 |
| seeded generic DAG (29031) | 4 | 0 | 0 |
| seeded random inventory (29032) | 5 | 0 | 0 |
| transported free-commutative clone, cutoff 30 | 10 | 45 | 120 |

The full five-predicate pair selector retains exactly the mutated-cover pairs
\((2,5),(2,7),(3,5)\).  The full triple selector is nonzero at all three
integer cutoffs and exactly zero on all four finite non-UFD fixtures.  It is
nevertheless copied term by term by the transported free-monoid and
polynomial-UFD controls.  The authority row census is 241 baseline subsets,
118 finite-control subsets, 45 free/UFD rows, 186 predicate-mask rows, and
165 marker rows.  None of the 31 nonempty predicate masks separates pairs;
28 masks separate baseline triples from the four finite fixtures, but every
mask is cloned by the mandatory UFD controls.

## Frozen category and information boundary

An admissible decorated source is

\[
X=(|X|,\leq,\bot,\operatorname{At},\vee,\mu,(F_N)_N,w,G,\ldots),
\]

where the ellipsis may include only source-resident roof, metric, Gram, and compiled-operator data already admitted by Papers 28–29.  Isomorphisms preserve and reflect the order, bottom, covers/atoms, every defined finite join, interval structure, the ambient compatible-cutoff filtration, and every decoration.  Incidence Möbius values are then preserved by interval isomorphism.

The invariant may be local or nonlocal, may have any finite arity, and may be scalar-, kernel-, formal-ledger-, holomorphic-function-, trace-, determinant-coefficient-, or new-functional-valued.  It may not branch on printed decimal names, call an external primality/factorization oracle, use target zeros or sampled ordinates, fit coefficients after controls, or silently reclassify a new functional as an ordinary trace or determinant.

## Frozen theorem boundary

Let

\[
M_{\mathbb Z}=(\mathbb N_{>0},\mid,1,\operatorname{lcm})
\]

and let (P) be its atom set.  The valuation map

\[
\Phi(n)=(v_p(n))_{p\in P}
\]

is a pointed join-semilattice and monoid isomorphism onto

\[
F(P)=\bigoplus_{p\in P}\mathbb N e_p.
\]

Transport (F_N,w,G), and every other admitted decoration along \(\Phi\).  Then the decorated sources are isomorphic.  Consequently, every isomorphism-natural invariant (I) satisfies

\[
I(M_{\mathbb Z})=\Phi^*I(F(P)).
\]

Therefore no admissible (I) can be nonzero on the integer baseline and zero on every free-commutative/UFD control.  This theorem covers arbitrary local or nonlocal join/lcm coherence, incidence Möbius and incidence-Hopf transforms, connected cumulants after a natural moment is fixed, and every same-object mixed/compiled functional natural in the admitted decorations.

The theorem does not cover a genuinely new source object carrying independently motivated nonmultiplicative data, such as an addition–multiplication interaction, congruence correspondence, or transfer operator not transported by \(\Phi\).  Excluding the transported clone from the controls or adding a label oracle weakens or changes the problem.

## Frozen candidate and analytic ownership

For a distinct atom tuple (A=(a_1,\ldots,a_r)), (r\in\{2,3\}), with join (j(A)), define

\[
K_r^{\mathrm B}(A)=
\mathbf 1_{\beta_A:2^{[r]}\cong[\bot,j(A)]}
(-1)^r\mu(\bot,j(A)).
\]

The weight is unique only after Boolean support, \(\{0,1\}\)-range, and unit normalization are imposed.  Naturality alone permits arbitrary functions on pointed interval isomorphism classes and still more global schemes.  On a free commutative source, (K_r^{\mathrm B}=1) for every distinct atom tuple.  The connected cumulant of a factorizing moment vanishes for (r\ge2).

The pair embedding

\[
\mathcal M_K(s)=2\sum_{p<q}K_2^{\mathrm B}(p,q)G_{pq}
\bigl(p^{-s}q^{s-1}+q^{-s}p^{s-1}\bigr)
\]

is a new source-weighted mixed functional, holomorphic for

\[
1-2\eta<\operatorname{Re}s<2\eta.
\]

It is not an ordinary trace, a relative determinant, a modified Fredholm determinant, or \(\det_3\).  The previously established \(\det_3\) owns A2 and removes the quadratic power rather than owning this series.  The marker \(q/p\leftrightarrow\log(q/p)\) belongs to \(\mathcal M_K\) and is transported unchanged to the clone.  No target-zero statement is permitted.

## Frozen route and branch decision

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

- Decision: `ROUTE_A_REJECTED`.
- Route B: locked.
- Branch action: `CLOSE_CHIRAL_INCIDENCE_COUNTERTERM_BRANCH`.
- Paper31 gate: a new source-derived nonmultiplicative operation is required.  Changing coefficients, arity, cumulant convention, cutoff, or finite-part scheme does not reopen the branch.

## Writer authority

The writer may create or edit only the narrative, proof, derivation, literature, planning, figure, LaTeX, bibliography, PDF, and compilation-audit files listed in `README.md`.  The writer may not modify any experiment, code, result, evaluation, manifest, repository README, plain-text mirror, or Git state.
