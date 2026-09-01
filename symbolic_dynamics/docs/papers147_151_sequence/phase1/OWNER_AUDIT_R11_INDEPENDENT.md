# Independent owner audit — R11 finite-spider absorption

**Auditor:** root lane, independent of the stochastic scout.  **Date:**
2026-09-01 UTC.  **External status:** `HOLD_EXTERNAL`.

## Decision

`PASS_OWNER_REPAIRED_INTERNAL`.

R11 may enter the cross-lane freeze only after three additional subtractions:
the unequal-arm endpoint law, the general-tree mean, and the equal-arm hitting
distribution are prior background.  The admissible residual is the joint
leaf/time transform for arbitrary unequal arms, its compact variance and
sharp fixed-mass extremizers, and the deliberately modest endpoint-plus-mean
geometry recovery statement.  This is an internal value decision, not a
novelty or priority certificate.

## Literal system checked

Join `r` finite paths of positive edge lengths `ell_1,...,ell_r` at a common
centre.  Start simple random walk at the centre and absorb at the first leaf.
The marked outcome is `(I,T)`, the absorbing leaf and first-passage time.

## Primary-source subtraction

| source | direct ownership | required subtraction |
|---|---|---|
| Lynn Hauser Pearce, ["Random walks on trees"](https://doi.org/10.1016/0012-365X(80)90234-4), *Discrete Mathematics* 30 (1980), 269--276 | finite trees with leaves as absorbing barriers; graph-structural endpoint absorption probabilities and expected walk length | the carrier, endpoint law and mean receive zero contribution credit |
| Soumik Pal and Tim Mesikepp, [*Finite Markov chains and Monte-Carlo Methods: An Undergraduate Introduction*](https://arxiv.org/abs/2510.14165), Problem 2.4 | explicitly asks for the absorption probability at a designated leaf of a finite star with unequal arm lengths | `Pr(I=i)=ell_i^{-1}/sum_j ell_j^{-1}` is direct pedagogical background, not a paper result |
| François Castella and Bruno Sericola, ["Hitting and cover times of the star graph and the sun graph"](https://doi.org/10.1016/j.peva.2026.102575), *Performance Evaluation* 173 (2026), 102575 | distributional recurrences and moments for hitting leaves of a star with equal arm length, plus cover-time results | every equal-arm specialization and generic recurrence-to-distribution language receive zero credit |
| Victor de la Peña, Henryk Gzyl and Patrick McDonald, ["Inverse problems for random walks on trees: network tomography"](https://arxiv.org/abs/math/0610821), *Statistics & Probability Letters* 78 (2008), 3176--3183 | an explicit algorithm recovering unknown transition probabilities on a known rooted tree from joint hitting-time/hitting-place data on boundary layers | inverse-first-passage framing and generic identifiability language receive zero credit; R11 must state that its unknown is the arm geometry, its data are only the endpoint vector and one mean, and the transitions are fixed simple-walk transitions |
| Manuel D. de la Iglesia and Claudia Juarez, ["Birth-death chains on a spider: spectral analysis and reflecting-absorbing factorization"](https://arxiv.org/abs/2111.10450) | matrix-valued spectral analysis for birth--death chains on half-line spiders, including a constant-probability random-walk example | spider terminology, spectral/resolvent rationality, and birth--death reduction receive zero credit |

The 2026 equal-arm paper is especially consequential: R11 cannot advertise a
star hitting-time distribution as such.  Its first axis must remain the
**leaf-marked, arbitrary unequal-arm closed transform** and must display the
strict equal-arm collapse as owned background.

## Focused non-hit search

The independent search combined `finite spider`, `generalized star`,
`unequal arms`, `absorbing leaves`, `hitting time`, `probability generating
function`, `Chebyshev`, `variance`, and inverse phrases.  It also screened
the general-tree inverse paper and the new equal-arm distribution paper.
No screened primary source stated the arbitrary-profile formula

`F_i(z)=z^ell_i product_(j!=i)P_(ell_j)(z)/D(z)`

with a common denominator assembled from the continuants `P_ell`, nor the
displayed arbitrary-profile variance and its fixed-total equality classes.
This is a bounded non-hit only; vocabulary and indexing misses remain
possible.

## Residual theorem gate

After subtraction, the paper contract must retain all of the following:

1. a direct excursion proof of the leaf-marked all-time transform for
   arbitrary ordered positive arm lengths, including parity and first atoms;
2. the compact formula
   `Var(T)=(sum ell_i^3-2 sum ell_i)/(3 sum ell_i^-1)
   +(sum ell_i)^2/(3(sum ell_i^-1)^2)`;
3. the sharp fixed-`(r,L)` interval for the mean with the exact unbalanced and
   balanced equality classes; and
4. the precise data boundary: endpoint probabilities determine only the
   primitive length ratios, while adding the mean recovers the common integer
   scale.

The endpoint and mean formulas may appear only as owned inputs used inside
items 2--4.  The inverse statement must not imply recovery of an unknown tree
topology or unknown transitions and must cite the network-tomography owner.

## Internal collision firewall

P136 and P140 are interacting random contraction processes, P141 is a greedy
independent-set process, and P146 is random polygon deletion.  R11 instead is
a fixed-state absorbing spatial walk with a marked first-passage transform;
none of their main proof engines transfers.  Generic Markov resolvents and
one-dimensional gambler's ruin are tools, not residual results.

Final status: **`PASS_OWNER_REPAIRED_INTERNAL`; `HOLD_EXTERNAL`.**
