# Collision firewall

The comparison is at the level of carrier, literal update, proof engine,
temporal invariant, and fibre engine.  Shared words such as “matrix” or
“subspace” are not enough either to kill or to clear a candidate.

## Direct comparison with the coordinator's NFIT matrix candidate

NFIT acts on matrices over `GF(2^r)` by conditionally adding the identity when
the current matrix is nonsingular.  Its proof engine pairs states by the
translation `A <-> A+I`; its fibre theorem is a linear-derangement census.

| Axis | NFIT | A01 / CLC | A02 / LDS |
|---|---|---|---|
| carrier | individual square matrices | triples in a subspace lattice | all subspaces of a central Lie algebra |
| update | determinant test followed by `+I` | rotate, meet, join | span of all internal Lie brackets |
| temporal engine | translation pairs in characteristic two | lattice absorption, `T^4=T^2` | rank trichotomy under `Lambda^2 sl_2 ~= sl_2`, `D^3=D^2` |
| recurrent clock | periods 1 and 2 | periods 1 and 2, but as an outer-register swap over an interval | two fixed points only |
| fibre engine | linear derangements/every-target matrix fibres | ordered complements in `J/M` | central graph lifts `E_{z,r}` and bracket polarity |
| unbounded axes | field extension and matrix size | field size `q` and dimension `d` | field size `q` and centre dimension `z` |

Conclusion: neither survivor is NFIT in disguise.  A01 shares the coarse
`height=2, periods<=2` headline but none of NFIT's carrier, update, or counting
engine.  A02 even has a different recurrent clock.  NFIT currently has the
clearest matrix-specific owner story; A01 has the widest lattice theorem; A02
has the most rigid image atlas.  The coordinator should compare paper value,
not merge these systems.

## P115 and P178 finite-linear/Jordan firewall

- **P115 (bounded Cartier operator dynamics)** and the broader finite-linear
  image/kernel engine study iterates of a fixed linear operator, with ranks,
  kernels, and Jordan blocks controlling the graph.
- **P178 (state-selected finite differences)** selects a linear finite-
  difference operator from the current state and again closes through a
  finite-linear/Jordan analysis.
- A01 is a nonlinear three-register lattice polynomial.  Its proof uses
  absorption and complementary subspaces; there is no fixed operator, rank
  sequence, rational canonical form, or Jordan block.
- A02 maps a *subspace state* to the span of pairwise brackets inside it.  The
  alternating bilinear map `Lambda^2 sl_2 -> sl_2` is part of the local
  geometry, not a linear time-evolution operator.  No Jordan classification is
  used in either the temporal or fibre theorem.

Therefore neither theorem is a deduction from the P115/P178 engine.  Any
future draft must preserve this distinction and must not market “short image
tower” alone as new.

## Explicit P172--P181 mechanism matrix

| Prior paper | Occupied mechanism | A01 / A02 verdict |
|---|---|---|
| P172 fresh-map self-image erosion | random functions repeatedly restricted to their own images | deterministic lattice polynomial / deterministic Lie-derived subspace; no random-map erosion |
| P173 random quotient leakage erosion | stochastic quotient and leakage chain | neither survivor forms a quotient or uses a Markov kernel |
| P174 minimum-pivot Möbius feedback | state-chosen pivot and fractional/projective update | neither has a pivot, Möbius map, or projective chart |
| P175 diagonal-feedback commutator | state-selected diagonal commutator with project-local square-zero collapse | **A02 survives narrowly:** `[U,U]` uses every pair inside a varying subspace and a bracket-polarity/fibre theorem. **A03 is killed here** because its transpose commutator has the same square-zero collapse headline |
| P176 first-frequency rotation | word statistic chooses a cyclic rotation | no word carrier or frequency-selected rotation |
| P177 random projective hyperplane toggling | random Cayley/Fourier walk | both survivors are deterministic; no convolution spectrum.  A12 is killed by this engine |
| P178 state-selected finite differences | adaptive linear operator and Jordan clock | excluded in the dedicated comparison above |
| P179 random singleton isolation | commuting idempotent stochastic deletion | no random idempotents or partition isolation |
| P180 bilinear radial scaling | collapse to a scalar/radial coordinate followed by one-dimensional dynamics | neither survivor scalarizes.  A05 is killed by this transfer |
| P181 first-descent prefix reversal | permutation prefix involution with a descent selector | no permutation, first-descent selector, or reversal |

## Earlier high-pressure regions

- **P97 sumset squaring / subspace products.** A01 uses lattice meet and join,
  not an additive/multiplicative set product.  A02 deliberately omits the
  extensive closure `U+[U,U]`; its derived map can shrink, jump to `sl_2`, and
  has a rank-polarity atlas.  A14, which uses the Jordan product of subspaces,
  is killed under this pressure.
- **P109/P115/P164 linear image/kernel dynamics.** Neither survivor iterates a
  linear endomorphism of the underlying vector space.
- **P110/P128 monotone join/gcd folds.** A01 is closest here, but it retains
  three registers and simultaneously emits `meet` and `join`; it is not a
  monotone one-coordinate fold.  Its recurrent outer swap and ordered-
  complement fibre `K_k(q)` are the nontransferable parts.
- **P137 rank feedback.** Neither update chooses an action from a rank statistic.
- **P143 and OFP polarities.** A01 has no orthogonal complement or Galois
  residual, and A02's plane-to-line bracket polarity is a proof lemma rather
  than the update.  A06/A15 are killed because polarity *is* their update.
- **P168 inverse span.** Neither survivor takes inverses of elements or spans
  their inverse set.
- **P171 Boolean Gram.** Neither uses a Gram map or characteristic-two Boolean
  matrix geometry.

## Frozen decision

The lane selects A01 for P182 and holds A02 as its sole reserve.  This firewall establishes internal
nonidentity only.  `OWNER_SEARCH_LOG.md` records a bounded external adjacency
check; it explicitly does not certify novelty.
