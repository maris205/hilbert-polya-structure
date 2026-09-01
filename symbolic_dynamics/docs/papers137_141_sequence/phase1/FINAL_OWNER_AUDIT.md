# FINAL OWNER AUDIT — P137–P141

Date: 2026-09-01

Scope reviewed locally:

- `docs/papers137_141_sequence/phase1/FINAL_THEOREM_CONTRACTS.md`
- `docs/papers137_141_sequence/phase1/OWNER_GATE_SUMMARY.md`
- `docs/papers137_141_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md`
- `papers/137-rank-feedback-p-group-splitting/{main.tex,references.bib}`
- `papers/138-palindromic-prefix-xor-feedback/{main.tex,references.bib}`
- `papers/139-lyndon-factor-start-feedback/{main.tex,references.bib}`
- `papers/140-random-majority-triple-contraction/{main.tex,references.bib}`
- `papers/141-weighted-threshold-greedy-mis/{main.tex,references.bib}`
- prior paper-local reports only as leads, not as controlling evidence

Primary-source basis:

- official DOI resolver metadata
- official/publisher records from Springer, Cambridge, Elsevier, APS, SIAM, Wiley, JSTOR, Schloss Dagstuhl, and arXiv

Rule of construction:

- bounded non-hits are not novelty evidence
- all five papers remain `HOLD_EXTERNAL`
- the only question answered here is whether the current zero-credit boundary and residual ownership story are internally coherent

## Batch disposition

| paper | bibliographic status | zero-credit ownership status | direct-owner status for residual package | internal P1–P136 collision | disposition |
|---|---|---|---|---|---|
| P137 | materially correct; one online-first year nuance | correct | no direct owner located for the full residual conjunction | cleared | `GO_INTERNAL` |
| P138 | correct | correct | no direct owner located for the full residual conjunction | cleared | `GO_INTERNAL` |
| P139 | cited metadata correct, but missing a controlling owner citation | incomplete: static suffix-record theorem already owned | no direct owner located for the full dynamic/fibre conjunction, but one advertised static pillar is pre-owned | cleared | `REPAIR` |
| P140 | correct | correct | no direct owner located for the full residual conjunction | cleared | `GO_INTERNAL` |
| P141 | materially correct; one online-first year nuance | correct but owner-thin | no printed direct owner located for the exact weighted package, but the theorem is a short corollary of owned support plus owned weighted-order machinery | cleared | `REPAIR` |

Batch conclusion: no finalist is killed at this stage, but only P137, P138, and P140 are owner-clean enough for continued internal drafting without source repair. P139 and P141 require ownership repair before their current writeups should be trusted.

## Metadata verification ledger

Only material issues are listed below.

### P137

- Fuchs, *Abelian Groups* (Springer Monographs in Mathematics, Springer International Publishing, Cham, 2015, DOI `10.1007/978-3-319-19422-6`): manuscript entry is materially correct.
- Andrews, *The Theory of Partitions* (Cambridge University Press, 1984, DOI `10.1017/CBO9780511608650`): materially correct.
- Delaunay–Jouhet, *Advances in Mathematics* 258 (2014), 13–45, DOI `10.1016/j.aim.2014.02.033`: correct.
- Eliahou–Erickson, *Discrete Mathematics* 313(4) (2013), 422–433, DOI `10.1016/j.disc.2012.11.014`: correct.
- Baalbaki–Bonanno–Del Vigna–Garrity–Isola, *The Ramanujan Journal* 63(3), 873–915, DOI `10.1007/s11139-023-00791-5`: DOI resolver returns online-first year 2023; manuscript uses print issue year 2024. This is a normalization issue, not an ownership defect.

### P138

- Galil, *Journal of Computer and System Sciences* 16(2) (1978), 140–157, DOI `10.1016/0022-0000(78)90042-9`: correct.
- Rubinchik–Shur, *European Journal of Combinatorics* 68 (2018), 249–265, DOI `10.1016/j.ejc.2017.07.021`: correct.
- Harju–Huova–Zamboni, *Journal of Combinatorial Theory, Series A* 129 (2015), 142–159, DOI `10.1016/j.jcta.2014.10.003`: correct.
- Bathie–Ellert–Starikovskaya, *LIPIcs* 359, ISAAC 2025, 9:1–9:16, DOI `10.4230/LIPIcs.ISAAC.2025.9`: correct.

### P139

- Chen–Fox–Lyndon, *Annals of Mathematics* 68(1) (1958), 81–95, DOI `10.2307/1970044`: manuscript page range is correct; DOI BibTeX truncates the page field, but JSTOR confirms 81–95.
- Duval, *Journal of Algorithms* 4(4) (1983), 363–381, DOI `10.1016/0196-6774(83)90017-2`: correct.
- Franek–Islam–Rahman–Smyth, arXiv:1605.08935 (2016): correct as an arXiv entry.
- Badkobeh–Crochemore, *Information and Computation* 285 (2022), article 104884, DOI `10.1016/j.ic.2022.104884`: correct.
- Missing controlling owner citation: Mantaci–Restivo–Rosone–Sciortino, *Journal of Discrete Algorithms* 28 (2014), 2–8, DOI `10.1016/j.jda.2014.06.001`.

### P140

- Krapivsky–Redner, *Physical Review Letters* 90(23) (2003), article 238701, DOI `10.1103/PhysRevLett.90.238701`: correct.
- Goles–Montealegre–Salo–Törmä, *Theoretical Computer Science* 609 (2016), 118–128, DOI `10.1016/j.tcs.2015.09.014`: correct.

### P141

- Klivans, *Discrete Mathematics* 307(21) (2007), 2591–2597, DOI `10.1016/j.disc.2006.11.018`: correct.
- Pippenger, *SIAM Journal on Discrete Mathematics* 2(3) (1989), 393–401, DOI `10.1137/0402034`: correct.
- Krivelevich–Mészáros–Michaeli–Shikhelman, *Random Structures & Algorithms* 64(4), 986–1015, DOI `10.1002/rsa.21200`: DOI resolver returns online-first year 2023; manuscript uses print issue year 2024. Acceptable, but should be normalized consistently if strict metadata hygiene is required.
- Plackett, *Journal of the Royal Statistical Society: Series C (Applied Statistics)* 24(2) (1975), 193–202, DOI `10.2307/2346567`: manuscript entry is correct; DOI BibTeX truncates the page field, but the official Wiley/RSS record confirms 193–202.

## Per-paper ownership findings

### P137 — rank-feedback splitting of finite abelian p-groups

Residual contract checked:

- recomputed-rank split map on finite abelian `p`-group types
- monotone rank growth and fixed-state census
- sharp triangular-depth theorem with unique maximizer `(n)`
- all-target one-step inverse formula

Zero-credit ownership check:

- Fuchs directly supports the finite abelian group classification and the cyclic-factor formulas used to compute `p^r G` and `G[p^r]`.
- Andrews directly supports the Gaussian-binomial partition enumeration.
- Delaunay–Jouhet legitimately own nearby torsion/partition machinery, but not the feedback iteration.
- Eliahou–Erickson and Baalbaki et al. are only contextual examples of partition dynamics; that use is defensible.

Direct-owner check:

- no official source was located that directly owns the full conjunction “recompute rank after each split + permanent-marker proof + sharp `D(n)` + exact every-target inverse formula”
- this is only a bounded non-hit, not a novelty claim

Internal collision check:

- nearest occupied internal objects remain P126 and P135
- those papers use ordered-composition refinement or centralizer multiplicity dynamics, not unordered `p`-group isotype splitting at recomputed rank
- no literal P1–P136 collision found

Decision:

- `GO_INTERNAL`
- keep `HOLD_EXTERNAL`

### P138 — palindromic-prefix XOR feedback

Residual contract checked:

- XOR feedback by the full palindromic-prefix indicator vector
- complement quotient and normalized amplifier
- unique recurrent class `0^n <-> 1^n`
- sharp depth `n-2`
- exact left-to-right decoder for every target fibre

Zero-credit ownership check:

- Galil directly owns all-prefix palindrome recognition as a classical input.
- Rubinchik–Shur and Bathie–Ellert–Starikovskaya legitimately support static palindrome/palindromic-prefix data-structure and compression context.
- Harju–Huova–Zamboni legitimately support static palindromic generation context.
- none of these sources is misused as owner clearance for the repeated XOR feedback system itself.

Direct-owner check:

- no official source was located that directly owns the repeated palindromic-prefix XOR map, its quotient amplifier, its sharp linear clock, and its exact decoder as one package
- again, this is only a bounded non-hit

Internal collision check:

- nearest internal neighbors remain P117 and P134
- those papers study odd-run flipping or whole-border-array recomputation, not XOR feedback from palindromic-prefix predicates
- no literal P1–P136 collision found

Decision:

- `GO_INTERNAL`
- keep `HOLD_EXTERNAL`

### P139 — Lyndon-factor-start feedback on binary words

Residual contract checked:

- suffix-record characterization of factor starts
- leading-one amplifier and unique fixed point `1^n`
- sharp unique deepest alternating witness
- fibre theorem via nonincreasing chains of binary Lyndon words

Zero-credit ownership check:

- Chen–Fox–Lyndon, Duval, Franek et al., and Badkobeh–Crochemore correctly support classical CFL factorization, linear factorization algorithms, and Lyndon array/tree infrastructure.
- However, the manuscript’s Proposition 2.1 is not a residual theorem. The exact static statement “factor starts are the left-to-right strict new suffix minima / inverse-suffix-array record minima” is already owned in the suffix-array/Lyndon literature.
- The controlling missing owner is Mantaci–Restivo–Rosone–Sciortino (J. Discrete Algorithms 28 (2014), 2–8, DOI `10.1016/j.jda.2014.06.001`). The publisher record identifies their Theorem 2.2 as an alternative route to Duval’s factorization, and later official Dagstuhl literature explicitly restates that theorem as the factor-start/new-minimum equivalence.

Static-comparison warning:

- the ordered-tail comparison lemma used to prove Proposition 2.1 is also standard CFL machinery
- it cannot be used to thicken the residual boundary once Proposition 2.1 is owner-subtracted

Direct-owner check on the surviving residual:

- no official source was located that directly owns the full dynamic conjunction “iterate the factor-start mask + unique deepest alternating orbit + ordered-Lyndon fibre atlas”
- but the current draft overstates ownership by foregrounding an externally owned static proposition as part of the paper’s result package

Internal collision check:

- nearest internal objects remain P105, P114, and P134
- none shares the literal carrier/update pair “binary word -> Lyndon factor-start mask -> recompute”
- no literal P1–P136 collision found

Required repair:

1. add Mantaci et al. 2014 to the bibliography
2. move Proposition 2.1 and its suffix-record characterization behind the zero-credit boundary
3. stop presenting the static suffix-record theorem as part of the residual contribution in the abstract/introduction/ownership language
4. keep only the iterated-mask dynamics, unique deep clock witness, and ordered-Lyndon fibre atlas as residual

Decision:

- `REPAIR`
- keep `HOLD_EXTERNAL`

### P140 — random majority-of-three contraction

Residual contract checked:

- shrinking majority-of-three word process
- exact two-run kernel
- endpoint probabilities and complete history counts
- marked cross-boundary law
- continuous-time odd-rate clock law, Beta transform, and Gamma limit

Zero-credit ownership check:

- Krapivsky–Redner directly own majority-rule background on fixed populations.
- Goles et al. directly own majority-network background on fixed carriers.
- the manuscript does not misattribute those sources as owners of the shrinking carrier or exact two-run law.

Direct-owner check:

- no official source was located that directly owns the full conjunction “uniform local majority contraction on a shrinking binary word + exact two-run kernel + endpoint counts + marked cross-boundary law + odd-rate hypoexponential clock law”
- bounded non-hit only

Internal collision check:

- nearest internal neighbors remain P132 plus stochastic contraction papers such as P121/P129
- P132 is length-preserving prefix-majority thresholding, not local random contraction
- P121/P129 are different stochastic coalescence mechanisms on different carriers
- no literal P1–P136 collision found

Decision:

- `GO_INTERNAL`
- keep `HOLD_EXTERNAL`

### P141 — weighted threshold greedy MIS

Residual contract checked:

- threshold-graph endpoint support `S_Z` and `S_d`
- weighted endpoint masses `p_d`, `p_Z`
- hazard inversion/open-simplex theorem
- accepted-size PGF and vertex marginals
- state-dependent Laplace recursion for elapsed completion time

Zero-credit ownership check:

- Klivans directly owns the threshold-graph support structure used in Proposition 2.1.
- Pippenger directly owns the random sequential adsorption / random-order greedy occupancy process on graphs.
- Krivelevich et al. legitimately own modern random-greedy MIS framing.
- Plackett directly owns the weighted random-order model used as the exponential-priority/Plackett–Luce interface.
- So the cited sources do own the zero-credit inputs attributed to them.

High-risk owner-thin point:

- no official source was located that prints exactly the reverse-hazard endpoint formula in the paper’s notation
- however, once the support sets are imported from Klivans and the weighted order law is imported from Plackett/exponential races, Theorem 3.1 is a very short conditioning argument
- Theorems 3.2 and 4.1 plus the marginal formulas are then immediate algebraic corollaries of that endpoint law
- this makes the residual package unusually thin and plausibly unpublished folklore even though a direct printed owner was not found

Direct-owner check:

- no direct official-source hit was found for the exact conjunction “weighted threshold support law + hazard inversion + PGF + marginals”
- this remains a bounded non-hit only and does not clear external ownership risk

Internal collision check:

- closest internal graph-system neighbor remains P106
- P106 is a synchronous deterministic Boolean MIS polarity map with `F^3=F`; P141 is an absorbing weighted random greedy endpoint law on threshold graphs
- no literal P1–P136 collision found

Required repair:

1. keep the paper’s ownership language narrow: it is a specialized exact-law note, not a new greedy-MIS process
2. state explicitly that the support and process are fully owned inputs
3. treat the weighted endpoint law as owner-thin and folklore-risky in all internal summaries
4. do not let bounded non-hits be recast as novelty language

Decision:

- `REPAIR`
- keep `HOLD_EXTERNAL`

## Final gate

Final status by paper:

- P137: `GO_INTERNAL`, `HOLD_EXTERNAL`
- P138: `GO_INTERNAL`, `HOLD_EXTERNAL`
- P139: `REPAIR`, `HOLD_EXTERNAL`
- P140: `GO_INTERNAL`, `HOLD_EXTERNAL`
- P141: `REPAIR`, `HOLD_EXTERNAL`

No paper is cleared for public novelty, priority, posting, submission, or specialist contact. The main concrete owner defect in the batch is P139’s missing attribution of the static suffix-record theorem. The main residual-risk paper in the batch is P141, whose weighted theorem package is not directly owned by a located printed source but is close enough to owned support plus owned weighted-order folklore that external restraint remains mandatory.
