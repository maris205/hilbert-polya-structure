# Paper 33 literature and novelty audit — SD-C35

Search date: 2026-08-15 UTC

## Proposed contribution under audit

Take the same all-modulus projective-residue recurrent object as Paper 32,
kill the `S^2`, `R^3`, and cusp-diamond cycles functorially at chain level,
compute the complete surviving ledger, and decide whether the quotient can
support a prime-selective same-object determinant.

## Core claims checked

1. The quotient of `Q[P^1(Z/NZ)]` by the `S` and `R` presentation relations
   is a usable new cycle quotient.
2. Ihara/Hashimoto nonbacktracking or a character twist might kill precisely
   the universal presentation cycles.
3. A graded/homological determinant could inherit the original graph-step
   operator.
4. Filling the cross-modulus `2x3` diamonds and analyzing all-modulus controls
   yields a new scoped obstruction relevant to Route A.

## Search protocol

Only primary research papers, official publisher pages, society archives, and
authoritative preprint records were used for technical claims.  Secondary
pages were used only to discover exact primary metadata and were not used as
evidence.

Representative query families (at least three formulations per core claim):

```text
Manin symbols P1(Z/NZ) S R relations homology Gamma0(N)
modular symbols quotient Q[P1(Z/NZ)] (1+S) (1+R+R^2)
relative homology X0(N) cusps projective line finite ring

Ihara Hashimoto nonbacktracking Schreier graph C2*C3
twisted Ihara zeta finite graph character presentation relations
edge zeta modular Schreier graph congruence subgroup

graded determinant chain complex Hopf trace graph zeta
homological determinant modular symbols graph-step operator
Kac-Ward cycle signs presentation relator cancellation

2024 2025 2026 modular symbols Manin relations determinant
2025 2026 abstract isogeny graph modular curve Ihara determinant
2026 weighted alternating graph zeta Hashimoto Ihara
```

Freshness searches covered February–August 2026 and also inspected relevant
2024–2025 arXiv records.

Search limitations: web/arXiv/publisher search is not an exhaustive theorem
database.  The novelty verdict is search-bounded.  No external model review
was run: the runtime did not expose the specified Codex-review MCP, and the
governing Session explicitly skips review loops.

## Verified closest primary literature

| Source | Verified technical role | Collision with SD-C35 |
|---|---|---|
| Yu. I. Manin, “Parabolic points and zeta-functions of modular curves,” *Math. USSR-Izv.* 6 (1972), 19–64, DOI [10.1070/IM1972v006n01ABEH001867](https://doi.org/10.1070/IM1972v006n01ABEH001867) | Foundational modular-symbol presentation and modular-curve homology | **Direct collision with the quotient mechanism.** The Manin relation quotient is classical, not a new construction. |
| Loïc Merel, “Opérateurs de Hecke pour Gamma_0(N) et fractions continues,” *Ann. Inst. Fourier* 41 (1991), 519–537, DOI [10.5802/aif.1264](https://doi.org/10.5802/aif.1264) | Official abstract explicitly describes relative homology of `X_0(N)` as a quotient of the free module on `P^1(Z/NZ)` and constructs lifts of Hecke actions | Strongest exact collision; also shows that operators descending to modular symbols require a separately constructed lift, not automatic descent of `S+R`. |
| Yasutaka Ihara, “On discrete subgroups of the two by two projective linear group over p-adic fields,” *J. Math. Soc. Japan* 18 (1966), 219–235, DOI [10.2969/jmsj/01830219](https://doi.org/10.2969/jmsj/01830219) | Origin of the Ihara zeta framework | Establishes that prime nonbacktracking graph cycles and their zetas are classical machinery; no all-`N` field selector. |
| Ki-ichiro Hashimoto, “Zeta functions of finite graphs and representations of p-adic groups,” *Adv. Stud. Pure Math.* 15 (1989), 211–280, DOI [10.1016/B978-0-12-330580-0.50015-X](https://doi.org/10.1016/B978-0-12-330580-0.50015-X) | Edge/nonbacktracking operator and representation twists | Direct method ancestor. Nonbacktracking removes inverse traversal, not the universal nonbacktracking cusp `RS` survivor. |
| Hyman Bass, “The Ihara-Selberg zeta function of a tree lattice,” *Int. J. Math.* 3 (1992), 717–797, DOI [10.1142/S0129167X92000357](https://doi.org/10.1142/S0129167X92000357) | Determinant formula for graph/tree-lattice zeta | Classical determinant ancestor; does not provide a homological field/composite selector. |
| Harold Stark & Audrey Terras, “Zeta Functions of Finite Graphs and Coverings,” *Adv. Math.* 121 (1996), 124–165, DOI [10.1006/aima.1996.0050](https://doi.org/10.1006/aima.1996.0050) | Multivariable edge/path zetas, coverings, and generalized Ihara formula | High overlap with marker/twist vocabulary; no relation-homology prime sieve. |
| M. Kac & J. C. Ward, “A Combinatorial Solution of the Two-Dimensional Ising Model,” *Phys. Rev.* 88 (1952), 1332–1337, DOI [10.1103/PhysRev.88.1332](https://doi.org/10.1103/PhysRev.88.1332) | Source of Kac–Ward signed walk determinant | Requires embedding/turning or spin data and produces nonzero phases, not chain-level annihilation of the mandated relation cells. |
| David Cimasoni, “A generalized Kac-Ward formula,” *J. Stat. Mech.* (2010) P07023, DOI [10.1088/1742-5468/2010/07/P07023](https://doi.org/10.1088/1742-5468/2010/07/P07023) | Extends Kac–Ward to graphs on orientable surfaces through embedding/spin structures | Confirms that a Kac–Ward choice needs extra geometric data absent from the frozen source; not a canonical all-modulus sieve. |
| Xiao-Jie Zhu, “Explicit formulae for linear characters of Gamma_0(N),” *Commun. Algebra* 53 (2025), 4499–4510, DOI [10.1080/00927872.2025.2488029](https://doi.org/10.1080/00927872.2025.2488029) | Current primary work on characters of congruence subgroups across many levels | Reinforces that congruence-subgroup characters are not field-only phenomena; no collision with the exact virtual-character cusp theorem. |
| Jun Bo Lau et al., “Zeta functions of abstract isogeny graphs and modular curves,” arXiv:2509.15214 (2025), [primary preprint](https://arxiv.org/abs/2509.15214) | Defines nonbacktracking primes and an Ihara determinant for abstract isogeny graphs, with modular-curve relations | Important current collision risk for graph/modular-curve zeta language. It starts from finite-field isogeny graphs and supplied characteristics/levels, not an all-`Z/NZ` emergent selector. |
| Ayaka Ishikawa & Hideaki Morita, “On the Ihara expression for the generalized weighted zeta function,” *Aequationes Math.* 100 (2026), article 43, DOI [10.1007/s00010-026-01288-4](https://doi.org/10.1007/s00010-026-01288-4) | Fresh generalized weighted digraph-zeta determinant theory, including inverse-arc conventions | Shows that weighted/partially directed determinant technology is active and classical; no chain-level arithmetic separation. |
| Rongrong Lu, Tingzeng Wu & Lihua Feng, “New relations between zeta functions of a graph,” online 13 Aug. 2026, DOI [10.1007/s40314-026-03891-2](https://doi.org/10.1007/s40314-026-03891-2) | Fresh alternating/weighted/quaternionic Hashimoto- and Ihara-type determinant relations | Two-day freshness check; no modular-symbol quotient or prime/composite control claim. |

## Claim-by-claim novelty verdict

| Claim | Novelty | Reason |
|---|---|---|
| Quotient by `1+S` and `1+R+R^2` on `P^1(Z/NZ)` | **LOW** | This is classical Manin-symbol machinery. |
| Ihara/Hashimoto removal of immediate reversals | **LOW** | Classical; it leaves the `RS` cusp cycle. |
| Character, Kac–Ward, or generic graded determinant as a technique | **LOW** | Each technique has extensive prior literature; applying it here is not independently novel. |
| Exact theorem that every `N>=2` Manin quotient has the same two-edge cusp survivor | **MEDIUM, scoped** | Elementary once formulated; the exact all-modulus control interpretation was not found in the searched Route-A context. |
| Contractibility of the filled `2x3` cross grid and resulting direct-sum block ledger | **MEDIUM, scoped** | The topology is elementary, but the consequence for this frozen source/ownership problem was not found. |
| `S+R` non-descent plus trace-class scalar-comparison boundary | **MEDIUM-HIGH, scoped** | Merel motivates special operator lifts, but the exact ownership failure for this candidate and Route-A implication were not found. |
| Complete 6-character/15-superdifference census retaining `SR` | **MEDIUM, scoped** | Finite character algebra is elementary; the control theorem is specific and keeps identity-word traces distinct from Manin norm-polynomial evaluations. |
| Universal claim that all homological/super twists fail | **NOT CLAIMED** | The research does not justify such a quantifier. |

## Overall novelty assessment

- Score: **6/10 for the negative classification paper; 2/10 for the quotient method itself**.
- Recommendation: **PROCEED with the negative paper; abandon the positive candidate**.
- Positioning: make the direct collision with Manin symbols explicit.  The
  contribution is not “a new homology construction,” but a controlled
  completion of the Paper 32 obligation: the classical quotient kills exactly
  the generic relations, destroys cross-modulus linkage, preserves composite
  block homology, and breaks graph-step determinant descent.
- Principal citation risk: any wording that markets Manin relations,
  nonbacktracking determinants, or modular-symbol homology as new.

## Strongest counter-argument

**Counter-argument.**  Relative Manin homology includes Eisenstein/cusp
classes; quotienting the cusp boundary might leave only genuine cuspidal
arithmetic and recover prime selectivity.

**Resolution.**  The finite exact census computes the cuspidal dimension
`2g_0(N)`: it is nonzero on 139 of 148 composite blocks through `N=192` and
zero on five prime blocks.  Thus the stronger cusp quotient fails both
directions of a field selector.  Any further exact all-composite block
suppression must introduce new data; if it is the static field defect, it is
the forbidden terminal projector.
