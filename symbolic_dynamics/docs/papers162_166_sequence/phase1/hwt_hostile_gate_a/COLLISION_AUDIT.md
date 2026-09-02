# P1--P165 structural collision audit

Decision: `GREEN`  
External lifecycle: `HOLD_EXTERNAL`

The gate criterion is structural: a generic “finite functional graph + clock +
fibres” silhouette is assigned zero credit but is not, by itself, a kill.  A
kill requires transfer of the literal carrier/update or of the occupancy
phase/inverse mechanism.

## 1. Repository-wide pass

The audit inspected the paper-directory inventory through P165, the available
sequence-level occupancy/kill ledgers and theorem contracts, and the README or
theorem spine of every close mechanism.  The broad disposition is:

| Portfolio block | Dominant occupied mechanisms | HWT disposition |
|---|---|---|
| P1--P50 | analytic/symbolic obstruction, holonomy, incidence, operator and arithmetic no-go lines | no finite diagonal word map or occupancy phase decoder |
| P51--P56 | no numbered paper directories are present in the current `papers/` inventory; historical work is represented in sequence records | no located literal collision |
| P57--P76 | symbolic shifts, entropy, periodic realization, XOR radius, group/matroid constraints | P63 supplies XOR inverse vocabulary only; no adaptive Hamming translation |
| P77--P96 | automatic digit-weight towers, sandpile translations, majority/CA/word shifts, finite-field local products | P77/P78/P80 are detailed below; none has the same state-dependent diagonal action |
| P97--P111 | sumset, lattice, valuation, group-algebra, adjugate, pruning, ideal and nilpotent maps | algebraic finite-map packaging is occupied, but no occupancy-composition quotient appears |
| P112--P126 | tournament/forest/Cartier/tree/word/random contraction/ideal/quadratic feedback | P118/P124/P125 are the closest packaging neighbours, not mechanism transfers |
| P127--P141 | Boolean-matrix, gcd, composition, prefix/palindrome/Lyndon feedback, rank feedback | P128/P132/P137/P138 receive explicit comparison below |
| P142--P151 | valuation, Boolean residual, Dyck/tree/word extraction, totalized finite-field rational maps | generic exact clocks/fibres heavily occupied; literal map remains distinct |
| P152--P161 | finite planes, dihedral/group, extraction, Hensel, intersection/pruning, corner stripping, orthocenter | every-time inverse atlases are occupied as a format; no diagonal occupancy mechanism |
| P162--P165 | stochastic intersections, complemented shadows, q-ary equality CA, code shortening | current batch has no conjugate carrier/update/inverse grammar |

## 2. Required close comparisons

### P77 — digit-weight automatic towers

P77 fixes the number of nonzero base-$q$ digits of an integer and studies the
shift-orbit closure, Cantor--Bendixson layers, and lowering endomorphisms.  It
does not update a finite word by its current weight.  The shared word “weight”
does not expose the phase map $j\mapsto j+m_j$.

### P80 — cocktail-party majority dynamics

P80 owns a complete finite functional graph, recurrent census, cycle counts,
zeta function, and shallow basins.  Its quotient is a majority statistic on
mate pairs and has only fixed points/two-cycles.  HWT permits every period
$1,\ldots,n$ and its tails are occupancy walks.  Collision is generic package
shape only.

### P124 — cross-colon monomial-ideal basins

P124 uses colon arithmetic, monomial staircases, first occupied diagonals, and
a contact-parity transfer matrix.  It has no free diagonal group action and no
target multiplicity indicators.  “Diagonal” there refers to total degree,
not translation by $\mathbf1$.

### P125 — quadratic-state shear

P125 is a state-gated pair map over a quadratic space with $0/1/2$ fibres,
depth at most two, and Witt-sensitive periods $1$--$4$.  Its polar-bit quotient
and quadratic inverse equation cannot recover HWT's weak-composition phase
map or Stirling cycles.

### P128 — translation--GCD depth fibres

P128 iterates $f\mapsto\gcd(f(x),f(x+1))$.  A fixed order-$p$ translation
creates irreducible-factor orbits; repeated gcd is an intersection/sliding-run
mechanism and the surviving fibre is multiplicative over factors.  HWT instead
uses a state-dependent diagonal translation on vectors and target symbol
multiplicities.  The two systems share translation vocabulary, not a carrier,
update, or inverse proof.

### P138 — palindromic-prefix XOR feedback

This is the strongest theorem silhouette: binary words, feedback, a sharp
$n-2$ maximum depth, and an every-target decoder.  The mechanisms are not
structurally the same:

| Feature | P138 | HWT |
|---|---|---|
| symmetry reduction | quotient by global complement, one phase bit | free diagonal $C_n$ orbit, $n$ phases |
| feedback statistic | palindrome indicators of every prefix | one global support size |
| reduced update | sequential prefix/XOR recurrence | $j\mapsto j+m_j$ on an occupancy composition |
| inverse | left-to-right palindrome decoder | independent multiplicity tests $m_k=n-k$ |
| recurrence | one complement two-cycle | periods of every length, Stirling census |

Thus P138 forces careful subtraction of the generic `n-2 + decoder` story but
does not transfer a theorem proof to HWT.

## 3. Additional close neighbours

| Paper | Shared surface | Structural separation |
|---|---|---|
| P63 rank-one XOR inverse radius | binary XOR/preimage language | infinite/subshift rank-one setting; no Hamming statistic or finite phase composition |
| P78 complete-bipartite sandpile translations | translations and exact cycle census | one fixed bijective sandpile-group translation; HWT's step changes with state and is noninjective for $n\ge3$ |
| P86 finite-field adjacent-product process | finite alphabet and weight-like local counts | stochastic/local multiplicative update, no diagonal orbit |
| P99 unipotent-shear sublattice dynamics | group action, periods, zeta | fixed invertible shear on HNF strata, hence uniform bijective orbits |
| P102 group-algebra involution norm | finite algebra and power-map functional graph | norm/power strata rather than support feedback |
| P106 synchronous MIS polarity | very shallow quotient dynamics | order-reversing Boolean polarity, only periods at most two |
| P109 nilpotent image subspaces | absorption and every-time fibres | fixed linear operator on a subspace lattice |
| P110 cyclic-shift join partitions | cyclic group quotient | repeated lattice join, monotone and eventually idempotent |
| P118 synchronous mex multipartite | quotient + labelled fibre EGF + full functional graph | local absent-colour rule; quotient is part-colour data, not one cyclic occupancy profile |
| P121 random product-plus-one coalescence | current-state statistic and components | stochastic partition coalescence |
| P127 parity-transpose looped digraphs | finite matrix, state correction, fibre trichotomy | transpose/rank-one Boolean correction and parity hyperplanes |
| P132 prefix majority | word feedback and sharp clock | partial-sum threshold recursion, not diagonal translation |
| P135 derived-centralizer orbit partitions | partition quotient and every-target coefficients | group centralizers/orbit partitions, no weight translation |
| P137 rank-feedback p-group splitting | global feedback statistic, sharp clock, partition fibres | adaptive splitting of integer partitions; no free group orbit or occupancy phase map |
| P139 Lyndon-factor start feedback | word factor feedback | factorization/start-set XOR, different inverse grammar |
| P143 Boolean row-inclusion residual | quotient relation and every-target fibre | inclusion-preorder map on row supports |
| P150 zero-totalized Lyness | full affine functional graph and singular inverse tree | rational finite-field recurrence, no Hamming symmetry |
| P153 factorial collapse | all-time target atlas | finite-plane factorial update; generic atlas format only |
| P154 dihedral normalizer | group functional graph and all positive-time fibres | subgroup normalizer/2-adic halving |
| P155/P156 extraction maps | sharp depths and target fibres | selector/extraction maps on permutations |
| P162 random translation intersection | translation, target histories | stochastic set intersection by random finite-field translates |
| P163 complemented shadows | set-family ranks and exact cycles | Johnson-ball/complement shadow operator |
| P164 cyclic equality feedback | q-ary word feedback, affine fibre staircase | local equality mask plus nilpotent cyclic-difference operator at dyadic lengths |
| P165 low-weight support shortening | Hamming support vocabulary and sharp clock | dynamics on linear codes via adaptive shortening; no word translation or occupancy cycle |

## 4. Same-batch scouting firewall

The current scouting ledgers contain Hamming-weight-controlled rotations and
inventory-histogram maps.  The former is a bijective fixed-content group action
with singleton fibres; the latter was killed because it literally iterates the
inventory vector and lacks a stable theorem spine.  HWT neither rotates
coordinates nor replaces a word by its histogram.  Its histogram instead
parametrizes a nonbijective phase map inside a preserved diagonal orbit.

## 5. Collision verdict

No P1--P165 system inspected is conjugate to the literal update or supplies the
same occupancy-composition cycle and inverse proofs.  P138 is a real narrative
collision and must be named, but killing merely because both results contain a
sharp $n-2$ and a target decoder would violate the structural gate requested
for this review.  P128 is similarly a vocabulary rather than mechanism
collision.

**Result: `PASS_STRUCTURAL_FIREWALL`, subject to zero credit for generic finite-
map, Stirling, EGF, and group-action machinery.**

