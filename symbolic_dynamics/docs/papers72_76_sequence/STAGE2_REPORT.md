# Stage-2 checkpoint -- Papers 72--76

Checkpoint date: 2026-08-27 UTC
State: **FIVE INTERNAL PAPERS LANDED AND COMPILED**
External release: **HOLD**

## Outcome

Five theorem-bearing short papers now exist.  Each contains a self-contained
proof of its main result and a separate deterministic control.  The controls
all pass and are stored beside the source.  The five canonical PDFs contain
4, 5, 4, 5, and 5 pages, respectively (23 pages total); page count is
descriptive, not a theorem-mass gate.

| Slot | Clear mathematical advance | Deterministic control |
|---:|---|---|
| P72 | `Per_theta(a,b)` is exactly the set of commuting blue/red boundary pairs; `P_theta(a,b)=tr(M_{theta,a}^b)`; a binary four-cycle has `P(1,1)=0`, `P(2,2)=8` while the identity rule has `4,16` | all 24 binary bijections and `1<=a,b<=3`: 216/216 agreement among three independent counts; 9 profiles |
| P73 | for the displayed primitive substitution, `D(m,n)=2^max(m,n)(1+min(m,n)/2)` over every configuration and translated dyadic rectangle | exact Jordan/supertile identities through level 32; pointwise envelopes through level 8; 20 legal `2x2` patches and 63 phase-separated `3x3` patches |
| P74 | `F_n=P_n=sum_{j=0}^n M^j`; exact Dyck and Motzkin extender sums; all three context entropies equal `log M` and are strictly below topological entropy | exhaustive word reduction for four `(M,N)` pairs through length 7 or 8; all formulas pass |
| P75 | recurrent SCCs of the clique-automaton edge presentation are indexed by nonempty complement-component support and frozen universal subset; radii add; exactly `2^t` presentation-level ergodic MMEs; determinant zeta factorization | all 1252 atlas component matrices/counts, 995 nontrivial local irreducibility checks, and explicit label-factor counterexample |
| P76 | every word cylinder has max/min linear endpoints; its admissibility set is one rational convex polyhedron; a common rational complex freezes the finite language and makes every cylinder measure linear; explicit hyperplane/chamber bound | 18 exact language-set comparisons containing 207 cylinders, symbolic coefficients, essential wall, and weak-only closure counterexample |

## Artifact boundary

Each paper directory contains `main.tex`, `references.bib`, `main.pdf`, a
`code/verify_*.py` program with stored output, `CONTROL_RESULTS.md`,
`CLAIMS_EVIDENCE.md`, `BUILD.md`, and a bounded Stage-2.5 audit.  Compilation
and visual checks are summarized in [the final QA report](FINAL_QA_REPORT.md),
with a per-paper `FINAL_QA.md` retained beside each canonical PDF.

These are internal mathematical drafts.  Bounded searches and internal
reviews do not establish worldwide novelty, priority, venue fit, authorship,
or permission to circulate.
