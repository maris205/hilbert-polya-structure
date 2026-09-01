# Primary-source verification and closest-owner gate — P151

Checked 2026-09-01 UTC.  This is a bounded primary-source subtraction audit,
not novelty, priority, ownership, freedom-to-operate, or release clearance.
Only publisher DOI records, arXiv primary manuscripts, and DOI metadata were
used in the bibliography.

## Databases and query lanes

The audit checked Crossref/DOI metadata, ScienceDirect publisher records, and
arXiv primary records.  Query lanes included:

- `Pearce random walks on trees absorbing endpoints expected length`;
- `unequal arm star random walk designated leaf probability`;
- `hitting distribution equal arm star graph Castella Sericola`;
- `random walks on trees network tomography first passage`; and
- `birth-death chains spider spectral reflecting absorbing factorization`;
- `finite Markov chain joint hitting time place law moments`; and
- `random walk tree hitting-time probability generating function`.

## Verified primary records

1. Lynn Hauser Pearce, “Random Walks on Trees,” *Discrete Mathematics* 30(3)
   (1980), 269--276,
   [DOI 10.1016/0012-365X(80)90234-4](https://doi.org/10.1016/0012-365X(80)90234-4).
   The publisher abstract places the walk on a finite tree with absorbing
   endpoints and states endpoint probabilities and expected duration.  Those
   two outputs receive zero contribution credit here.
2. Soumik Pal and Tim Mesikepp, *Finite Markov Chains and Monte-Carlo Methods:
   An Undergraduate Introduction*,
   [arXiv:2510.14165](https://arxiv.org/abs/2510.14165), Problem 2.4.
   The primary manuscript explicitly asks for the probability of exiting at a
   designated leaf of a star with unequal arm lengths.  The unequal-arm
   endpoint formula therefore receives zero credit.
3. François Castella and Bruno Sericola, “Hitting and Cover Times of the Star
   Graph and the Sun Graph,” *Performance Evaluation* 173 (2026), 102575,
   [DOI 10.1016/j.peva.2026.102575](https://doi.org/10.1016/j.peva.2026.102575).
   The publisher record studies finite stars with the same length on every
   arm and gives hitting distributions and moments.  Equal-arm distribution
   theory is treated as directly owned background.
4. Victor de la Peña, Henryk Gzyl, and Patrick McDonald, “Inverse Problems for
   Random Walks on Trees: Network Tomography,” *Statistics & Probability
   Letters* 78(18) (2008), 3176--3183,
   [DOI 10.1016/j.spl.2008.06.001](https://doi.org/10.1016/j.spl.2008.06.001)
   and [author manuscript arXiv:math/0610821](https://arxiv.org/abs/math/0610821).
   Their inverse problem assumes a known augmented tree and uses rich joint
   time/place observations at boundary layers to recover unknown transition
   probabilities.  General tree-tomography framing receives zero credit.
5. Manuel D. de la Iglesia and Claudia Juarez, “Birth-Death Chains on a
   Spider: Spectral Analysis and Reflecting-Absorbing Factorization,”
   *Journal of Mathematical Analysis and Applications* 517(2) (2023),
   126624,
   [DOI 10.1016/j.jmaa.2022.126624](https://doi.org/10.1016/j.jmaa.2022.126624),
   with primary manuscript
   [arXiv:2111.10450](https://arxiv.org/abs/2111.10450).
   This is a spectral/QBD framework for half-line spider chains.  Its
   “reflecting--absorbing” phrase denotes a stochastic matrix factorization
   and Darboux transform, not first absorption at finite leaves.  Generic
   spectral and factorization claims are excluded here.
6. Bruno Sericola, “On Cover Times of Markov Chains,” *Stochastic Models*
   40(4) (2024), 685--727,
   [DOI 10.1080/15326349.2024.2319201](https://doi.org/10.1080/15326349.2024.2319201),
   [author-hosted HAL record](https://inria.hal.science/hal-04364216).
   Equations (1)--(5) give the generic finite-chain joint hitting-time/place
   law, endpoint masses, and first/second moment matrices.  Their generating
   series supplies generic rational marked-law machinery.  All of this
   receives zero credit.  Inspection found no unequal-spider continuant
   product or the scalar formula retained here.
7. Haiyan Chen, “The Generating Functions of Hitting Times for Random Walk on
   Trees,” *Statistics & Probability Letters* 77(15) (2007), 1574--1579,
   [DOI 10.1016/j.spl.2007.03.044](https://doi.org/10.1016/j.spl.2007.03.044).
   This gives an algorithmic treatment of hitting-time probability generating
   functions on general trees.  Generic tree-PGF existence and computation
   receive zero credit; the inspected record does not state a leaf-marked
   unequal-spider continuant factorization.

## Claim subtraction

| source | collision class | zero-credit material | residual boundary left in P151 |
|---|---|---|---|
| Pearce | same carrier class, broader trees | endpoint probabilities and expected time | variance after specialization, plus downstream extremal/inverse uses |
| Pal--Mesikepp | same unequal-arm endpoint object | designated-leaf probability | no endpoint novelty; only the residual transform/variance/extremal/inverse conjunction |
| Castella--Sericola | direct equal-arm distribution owner | equal-arm hitting law and moments | arbitrary unequal arms with labelled leaf mark |
| Sericola | direct generic finite-chain owner | joint hitting-time/place law, endpoint law, and first/second moment matrices | explicit unequal-spider continuant product and compact scalar variance specialization only |
| Chen | nearest general-tree PGF owner | generic hitting-time PGF algorithm on trees | leaf-marked unequal-spider closed continuant factorization |
| de la Iglesia--Juarez | nearest spider-process framework | spectral analysis, QBD and stochastic factorization language | elementary finite-leaf excursion renewal only |
| de la Peña--Gzyl--McDonald | nearest inverse first-passage framework | general tomography framing and unknown-transition recovery | fixed simple-walk kernel, known spider class, unknown integer arm lengths, endpoint vector plus one mean |

## Surviving conjunction and limitation

After subtraction, the manuscript retains only the narrowed conjunction: the
explicit unequal-spider continuant factorization of the already-generic
time/place law, the compact scalar variance specialization, sharp
fixed-total-length extremizers with equality classes, and the exact
coarse-data inverse boundary.  Generic joint laws, rationality, resolvents,
tree-PGF algorithms, endpoint/mean formulas, and generic second moments are
background and are not residual claims.

The bounded search did not locate a primary source stating that complete
residual conjunction.  This non-hit is not a novelty or priority certificate.
It does not authorize external circulation or specialist contact.  Status
remains `HOLD_EXTERNAL`.
