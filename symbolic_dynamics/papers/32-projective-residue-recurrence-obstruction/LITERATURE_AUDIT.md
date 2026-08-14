# Literature audit — Paper 32 / SD-C34

Search window: 2026-08-14 through 2026-08-15 UTC.

## Search and verification protocol

The search covered official DOI/publisher metadata, Crossref, arXiv freshness
metadata, and the inherited internal papers 20, 21, 30, and 31.  Query
families combined `projective line over Z/nZ`, modular/Farey graphs,
projective residue actions, transfer operators, Fredholm determinants,
finite-index modular groups, direct-sum trace class, and composite cycle
controls.  Sources were included only when they directly addressed finite
projective ring geometry, modular/Farey symbolic dynamics, transfer-operator
determinants, or trace-class determinant theory.  Blog posts, encyclopedic
summaries, and unrelated uses of “residue,” “diamond,” or “Schreier” were
excluded.

The search is bounded rather than exhaustive.  Novelty claims below are
therefore scoped to the documented search, not stated as universal priority.
No cross-model or peer-review loop was run, in accordance with the user's
instruction.

## Verified primary literature

| Source | Role in this paper | Collision assessment |
|---|---|---|
| Blunck and Havlicek (2000), DOI [10.1007/BF02940921](https://doi.org/10.1007/BF02940921) | projective lines over rings and functorial geometry | high overlap with the state space; no all-modulus cycle/Fredholm obstruction |
| Jones, Singerman, and Wicks (1991), DOI [10.1017/CBO9780511661846.006](https://doi.org/10.1017/CBO9780511661846.006) | modular-group and generalized Farey graph combinatorics | high overlap with the \(S,R\) graph mechanism; no semiring-source field-versus-recurrence trilemma |
| Katok and Ugarcovici (2006), DOI [10.1090/S0273-0979-06-01115-3](https://doi.org/10.1090/S0273-0979-06-01115-3) | symbolic dynamics for the modular surface | classical coding background; no prime/composite source-control program |
| Mayer (1991), DOI [10.1090/S0273-0979-1991-16023-4](https://doi.org/10.1090/S0273-0979-1991-16023-4) | transfer-operator realization of Selberg zeta | closest analytic ancestor; its target and operator family differ from the all-residue direct sum here |
| Chang and Mayer (2001), DOI [10.1007/978-3-642-56589-2_23](https://doi.org/10.1007/978-3-642-56589-2_23) | finite-index modular group representations and Fredholm factorization | strongest analytic collision risk; no static field defect or controlled composite-cycle obstruction |
| Bonanno and Isola (2014), DOI [10.1088/0951-7715/27/5/897](https://doi.org/10.1088/0951-7715/27/5/897) | Farey-map two-variable Ruelle/Selberg zeta framework | overlaps free markers and Farey dynamics; no residue-prime ledger classification |
| Simon (1977), DOI [10.1016/0001-8708(77)90057-3](https://doi.org/10.1016/0001-8708(77)90057-3) | trace-class infinite determinants | analytic tool, not an arithmetic collision |
| Saniga et al. (2007), DOI [10.1016/j.chaos.2007.01.008](https://doi.org/10.1016/j.chaos.2007.01.008) | finite projective lines over small rings | confirms classical zero-divisor-sensitive geometry; no recurrent determinant classification |

## Literature synthesis

### Projective lines over rings

Finite-ring projective geometry already supplies the correct state space and
its sensitivity to units and zero divisors.  The count
\(|P^1(\mathbb Z/n\mathbb Z)|=\psi(n)\) is classical and is not presented as
new.  This paper uses the geometry as a controlled source object and asks a
different question: whether the field/composite distinction appears in its
primitive recurrence without a selector.

### Modular and Farey dynamics

The matrices satisfying projective relations of orders two and three belong
to the classical modular/Farey framework.  That literature makes the
universal relations expected, not novel.  Their role here is adversarial:
the same relations that produce elegant shared-state recurrence erase
prime selectivity because they act on every finite residue quotient.

### Transfer operators and determinants

Mayer and later Farey-map work connect modular symbolic dynamics with
Fredholm determinants and Selberg/Ruelle zeta functions.  Finite-index
representations also enter transfer-operator factorizations.  Paper 32 does
not claim a new Selberg determinant.  Its analytic contribution is the much
narrower ownership statement that the frozen all-modulus graph-step direct
sum, including cross-modulus cusp maps, is itself trace class on
\(\operatorname{Re}s>2\).  The owned determinant is then used to show that
analytic well-posedness does not imply an arithmetic primitive ledger.

## Claim-by-claim novelty

| Claim | Assessment | Boundary |
|---|---|---|
| projective line over \(\mathbb Z/n\mathbb Z\) and Dedekind-\(\psi\) count | low | classical finite-ring geometry |
| projective \(S^2=R^3=1\) recurrence | low | classical modular presentation |
| Farey/modular transfer determinants | low | established by Mayer and successors |
| frozen all-modulus trace-class direct sum with original edge marker | medium | elementary construction; exact ownership arrangement not found in the bounded search |
| downward-transient versus bidirectional composite-diamond dichotomy | medium-high, scoped | source-specific no-go not found; proof is elementary once stated |
| static field separator / universal cycle flood / same-object determinant trilemma | medium-high, scoped | combination and strict Route-A interpretation not found; components are classical |
| implication for RH or a new prime theorem | none claimed | outside the paper's claim boundary |

Overall novelty assessment: **6/10**, suitable for a tightly scoped negative or
diagnostic paper.  The manuscript must not market projective lines, modular
relations, or trace-class determinants as new.

## Bounded novelty statement

To our knowledge, based on official publisher/DOI, Crossref, web, and arXiv
searches carried out through 2026-08-15, the nearest work develops the
projective-ring state space, modular/Farey action graphs, or modular transfer
determinants separately.  Within that search, no directly comparable study
was found that freezes an all-residue semiring-source grammar, proves
primitive composite flooding before weights, and simultaneously establishes
ordinary Fredholm ownership for the same uninduced object.  The claim is
search-bounded; it is not an assertion that no such argument exists anywhere.

## Citation integrity

All eight bibliography entries used by the manuscript were verified through
their DOI records.  The bibliography cites only works used in the text.  The
manuscript paraphrases their roles and contains no long quotation.  Classical
facts proved directly in `PROOF_PACKAGE.md` do not depend on secondary
summaries.
