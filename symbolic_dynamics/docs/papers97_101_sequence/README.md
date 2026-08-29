# Papers 97–101: five-system Route-A manuscript packet

Status: **FINAL QA PASS; INTERNAL FREEZE; EXTERNAL RELEASE HOLD**.

Evidence cutoff: 2026-08-29 UTC. This round applies the early-signal rule:
a system advances only when two independent exact probes expose a
theorem-sized formula, anomaly, transition, or rigidity invariant. The five
slots deliberately vary the phase space, action, headline invariant, and
proof engine rather than deepening one system repeatedly.

## Five-paper sequence

| Slot | Primary system | Explicit landed result | Artifact |
|---:|---|---|---|
| P97 | sumset squaring on nonempty subsets of `F_p` | complete recurrent core and zeta, exact layerwise worst absorption depth, temporal census, and recovery of `p` and `ord_p(2)` | [paper](../../papers/97-sumset-squaring-dynamics/) |
| P98 | equal adjacent block-sum finite-field shift | affine residue-class normal form, repeated-root fixed-count staircase in every characteristic, exact order, cycle census, zeta, and parameter recovery | [paper](../../papers/98-equal-block-sum-torsion-shifts/) |
| P99 | unipotent shear on index-`N` sublattices of `Z^2` | complete HNF layer cycles, all fixed counts and zeta, prime-power valuation staircase, and recovery of `N` | [paper](../../papers/99-unipotent-shear-sublattice-dynamics/) |
| P100 | least-valuation digit erasure on `Z/p^r Z` | digit-sum absorption conjugacy, complete transient profile, moments and limit laws, periodic blindness, and recovery of `(p,r)` | [paper](../../papers/100-least-valuation-digit-erasure/) |
| P101 | iid random cap/floor interval cocycle | clamp-or-constant word normal form, distribution-free synchronization law, geometric-sum representation, critical prefactor, and exact uniform-threshold mean diameter | [paper](../../papers/101-random-cap-floor-synchronization/) |

P97 and P96 both involve finite subsets, but the former is a nonlinear
Minkowski self-sum rather than a pointwise hyperspace lift. P98 is the only
shift in the batch; P99 is a finite bijective lattice action; P100 is a
noninvertible arithmetic absorber; and P101 is a continuous random
semigroup cocycle. No selected pair shares both its phase space and proof
engine.

## Evidence map

- [problem anchor](PROBLEM_ANCHOR.md)
- [Stage-1 theorem selection](STAGE1_REPORT.md)
- [candidate and rejection ledger](phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md)
- [frozen theorem contracts](phase1/THEOREM_CONTRACTS.md)
- [proof-spike ledger](proof_spikes/README.md)
- [Stage-2 artifact report](STAGE2_REPORT.md)
- [source verification](phase2/SOURCE_VERIFICATION_REPORT.md)
- [Stage-2.5 hostile audit](STAGE2_5_REPORT.md)
- [final QA report](FINAL_QA_REPORT.md)
- [canonical PDF manifest](CANONICAL_PDF_MANIFEST.sha256)
- [pipeline state](PIPELINE_STATE.yaml)
- [material passport](MATERIAL_PASSPORT.md)
- [standing authorization](STANDING_WORKFLOW_AUTHORIZATION.md)

## Authorization boundary

The standing instruction authorizes internal five-paper rounds, exact proof
checks, compilation, and scoped Git synchronization. It does not authorize
public posting, submission, external circulation, editor or author contact,
or an absolute novelty or priority claim. All five papers remain **EXTERNAL
HOLD**.
