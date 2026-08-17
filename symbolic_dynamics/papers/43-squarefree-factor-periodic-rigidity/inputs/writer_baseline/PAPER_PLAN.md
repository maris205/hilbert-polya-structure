# Paper 43 writer plan

## Working title and role

**Factors Cannot Resurrect Cycles: Periodic-Ledger Rigidity for the
Squarefree Admissible Shift**

This is a typed internal closure note, not a standalone novelty claim.  The
standalone novelty assessment is `1/10`; the only positive credit is for the
program-specific assembly of an arbitrary-factor theorem, its exact
periodic ledger, its determinant owner, and its repair firewalls.  Known
squarefree/B-free proximality, factor permanence, periodic separation, and
the rank-one determinant receive zero credit.

## Claim hierarchy

1. **Main theorem.** Every continuous surjective equivariant factor of the
   exact two-sided all-prime-square admissible shift into an arbitrary compact
   metrizable Z-system has exactly one periodic point.
2. **Ledger corollary.** Every fixed-point count equals one, so the
   Artin--Mazur zeta is `1/(1-z)` and the inverse determinant is `1-z`.
3. **Typing obstruction.** The single primitive fixed orbit and its temporal
   repetitions cannot be retyped as the infinitely many rational-prime
   primitives.
4. **Sharpness.** Every finite prime set has an explicit periodic witness;
   the nonempty and empty cases are proved separately.
5. **Governance conclusion.** Strict Route A is rejected with tuple
   `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` and Route B
   invocation is false.

## Evidence map

| Claim | Evidence | Main location | Failure boundary |
|---|---|---|---|
| source compactness | finite cylinder witness for each failed modulus | Section 3, Appendix A | changed source |
| source proximality | fresh prime-square CRT for every point/window pair | Section 3, Appendix A | finitely many exclusions |
| factor proximality | surjective lifts, compact uniform continuity, equivariance | Section 4 | nonfactor observations |
| periodic rigidity | fixed-point anchor plus finite-orbit positive separation | Section 4 | nonproximal source |
| zeta and determinant | exact fixed counts and Artin--Mazur definition | Section 5 | changed observable |
| prime mismatch | primitive-support cardinality and marker ownership | Section 5 | forbidden retyping |
| finite-P0 repair | `x_n=1 iff n=1 mod Q`, plus empty-set case | Section 6, Appendix A | none within finite-P0 claim |
| literature boundary | primary-source chronology and bounded collision audit | Section 2, Appendix B | `STOP_DUPLICATE` |

## Modular outline and target length

The target is 10--14 A4 pages at 11pt after compilation.  Length is earned by
proofs, typed boundaries, and controls; there is no general background
tutorial.

| File | Purpose | Approximate compiled pages |
|---|---|---:|
| `abstract.tex` | theorem, method, result, novelty disclaimer | 0.5 |
| `sections/1_introduction.tex` | problem, exact contribution, roadmap, Figure 1 | 1.5 |
| `sections/2_prior_scope.tex` | source ownership, bounded collision audit, retrospective selector | 1.5 |
| `sections/3_source_proximality.tex` | topology, missing residues, exact CRT proof | 1.5--2 |
| `sections/4_factor_rigidity.tex` | arbitrary factor theorem and separation proof, Figure 2 | 1.5--2 |
| `sections/5_periodic_ledger.tex` | Artin--Mazur ledger, operator and prime-type firewall | 1.5 |
| `sections/6_sharpness_route.tex` | finite-P0 theorem, repairs, Route tuple, Figure 3 | 1.5--2 |
| `sections/7_limitations_conclusion.tex` | limitations, STOP_DUPLICATE, conclusion | 0.75 |
| `appendices/A_proof_details.tex` | exact metric, CRT, period, and series checks | 1--1.5 |
| `appendices/B_types_provenance.tex` | type table, falsifiers, chronology | 1--1.5 |

## Figure plan

Exactly three vector figures are used, all drawn in pure TikZ and checked into
`figures/`.

1. `figures/fig1_proof_chain.tex`: prime-square omissions to CRT zero windows,
   source and factor proximality, unique periodic point, determinant.
2. `figures/fig2_factor_separation.tex`: arbitrary compact metrizable factor
   map and the two finite-orbit separation contradictions.
3. `figures/fig3_sharpness.tex`: all-prime source versus nonempty finite-P0
   periodic witness and empty-P0 two-fixed-point witness, plus prohibited
   repair directions.

No raster figure, generated plot, external asset, or fourth figure is allowed.

## Citation placement

| Source | Manuscript use | Credit boundary |
|---|---|---|
| Artin--Mazur (1965) | definition of the periodic-point zeta | determinant convention only |
| Sarnak (2011) | squarefree admissible flow and known proximality | zero novelty |
| El Abdalaoui--Lemańczyk--de la Rue (2015) | broader B-free dynamical context | source chronology |
| Bartnicka--Kasjan--Kułaga-Przymus--Lemańczyk (2018) | general two-sided B-free proximality classification | strongest direct mechanism collision |
| Kasjan--Keller--Lemańczyk (2019) | window characterization of proximality | independent broader route |
| Gundlach--Klüners (2024/2025 v2) | nearby power-free factor rigidity | adjacent target category, no novelty proof |

## Non-negotiable wording

- Say “arbitrary compact metrizable Z-factor” only together with continuous,
  surjective, and equivariant.
- Say “internal exact closure,” never “new proximality theorem.”
- State that the selector is retrospective and was written with all outcomes
  known.
- State both finite-P0 cases; do not infer the universal claim from the
  modulus-four example.
- Keep the periodic-core matrix separate from any full-state transfer or
  Hilbert--Polya operator.
- Keep `STOP_DUPLICATE` live.  An exact published theorem ends the external
  claim without invalidating the internal proof record.
- Do not insert experiment or canonical-result counts, hashes, or blocks in
  this draft.
