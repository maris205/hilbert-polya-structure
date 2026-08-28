# Papers 87–91: five-system Route-A manuscript packet

Status: **FINAL QA PASS; INTERNAL FREEZE; EXTERNAL RELEASE HOLD**.

Evidence cutoff: 2026-08-28 UTC. This round again applies a two-probe
early-signal rule: a candidate advances only after a short exact calculation
exposes a closed formula, sharp transition, reconstruction threshold, or
rigidity invariant, and a second calculation shows that the signal persists.

## Five-paper sequence

| Slot | Primary system | Explicit result | Artifact |
|---:|---|---|---|
| P87 | nonzero-socle product shifts over finite chain rings | equal-entropy valuation components, parity mixing/MME transition, zeta, rank, and four-period `(q,a)` rigidity | [paper](../../papers/87-chain-ring-socle-product-shifts/) |
| P88 | finite-field linear parity tree shifts | exact leaf parametrization, normalized complexity, iid rays, and full-level coordinate-deletion reconstruction | [paper](../../papers/88-finite-field-parity-tree-shifts/) |
| P89 | Bernoulli-reset golden random SFT | Fibonacci regeneration, closed quenched and annealed exponents, strict gap, and renewal CLT | [paper](../../papers/89-bernoulli-reset-golden-random-sft/) |
| P90 | Rule 184 on finite binary rings | sharp particle-layer core-entry depth, weighted iterate-fixed polynomial, exact temporal orbits, and zeta | [paper](../../papers/90-rule184-particle-periodic-zeta/) |
| P91 | generalized-dihedral reverser shifts | canonical `(N,t)` collapse, mixing, cubic spectral/zeta compression, and two-period family rigidity | [paper](../../papers/91-generalized-dihedral-reverser-shifts/) |

The mechanisms are deliberately distinct: a reducible arithmetic relation
SFT, a free-semigroup tree-SFT, a random matrix cocycle, a conservative
cellular automaton, and a primitive group-relation SFT. P87 and P91 both use
finite one-step presentations, but their dynamical signatures are opposite:
P87 splits into equal-entropy components, whereas P91 is mixing.

## Evidence map

- [Stage-1 theorem selection](STAGE1_REPORT.md)
- [Candidate and rejection ledger](phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md)
- [Proof-spike ledger](proof_spikes/README.md)
- [Stage-2 artifact report](STAGE2_REPORT.md)
- [Source verification](phase2/SOURCE_VERIFICATION_REPORT.md)
- [Stage-2.5 hostile audit](STAGE2_5_REPORT.md)
- [Final QA report](FINAL_QA_REPORT.md)
- [Canonical PDF manifest](CANONICAL_PDF_MANIFEST.sha256)
- [Pipeline state](PIPELINE_STATE.yaml)
- [Material passport](MATERIAL_PASSPORT.md)
- [Standing authorization](STANDING_WORKFLOW_AUTHORIZATION.md)

## Authorization boundary

The standing instruction authorizes internal five-paper rounds, exact proof
checks, compilation, scoped Git commits, and synchronization to the configured
research mirror. It does not authorize public posting, submission, external
circulation, editor or author contact, or an absolute novelty/priority claim.
All five papers remain **EXTERNAL HOLD**.
