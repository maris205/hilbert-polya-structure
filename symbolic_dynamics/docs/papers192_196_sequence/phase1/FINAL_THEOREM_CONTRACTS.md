# Frozen theorem contracts — P192–P196

Status: `5/5 SELECTED / HOLD_EXTERNAL`.

Every item below requires an all-parameter proof in the manuscript.  Exact
enumeration is bounded falsification pressure only.  P192 remains
`OWNER_RED_AMBER`; P193--P196 remain `OWNER_AMBER`.

## P192 — first-collision Hurwitz dynamics

On minimal transposition factorizations of the long cycle, apply the right
Hurwitz move at the first adjacent pair with equal numeric lower endpoint.
The paper must prove:

1. update indices increase strictly, every recurrent state is fixed, and the
   sharp maximum tail is `n-2`;
2. fixed-state count `(n-1)^(n-2)` through the classical lower-endpoint
   parking-function bijection and Pollak's circular model;
3. an every-target inverse Hurwitz atlas, including empty fibres;
4. maximum one-step fibre `n-1`, uniquely at the adjacent-transposition chain;
5. the full history-set formula is labelled only as a conjecture, with exact
   evidence through `n=8` locally and `n=9` in a separate streaming control.

## P193 — mutual-best block refinement

On a permutation, simultaneously exchange every mutually nominating pair,
where a position nominates its smallest later smaller value and that value
nominates its earliest earlier larger position.  The paper must prove:

1. the literal pairs are exactly first/minimum pairs of nontrivial direct-sum
   indecomposable blocks;
2. strict block refinement, unique identity absorber, exact recursive clock,
   sharp tail `n-1`, and `(n-1)!` deepest states;
3. cumulative depth series
   `A_t=1/(1-B_t)`, `B_0=x`, `B_(t+1)=x+x^2 A_t B_t'`;
4. an every-target component-size fibre product, image iff the first value is
   `1`, and unique maximum fibre `2^(n-1)` at the identity.

## P194 — least-raising type-A word-crystal dynamics

On words over `[k]`, apply the Kashiwara raising operator `e_i` with the least
usable color `i`, holding at a highest word.  The paper must prove:

1. exact identification of recurrent states with crystal-highest words and
   absence of nontrivial cycles;
2. the pointwise clock as the weight drop to the component highest weight;
3. component and global depth polynomials through Schur specialization and
   Robinson--Schensted multiplicities;
4. sharp tail `n(k-1)`, uniquely at `k^n`;
5. a complete one-step inverse criterion, fibre bound `k`, and the stated
   stable sharpness range via a staircase highest word.

Crystal operators, RSK, Schur functions, and hook/tableau counts receive zero
contribution credit.

## P195 — odd-side least-neighbour tree walk

On a labelled tree with a marked root, move to the least-labelled neighbour
whose far-side component has odd order; hold if no such neighbour exists.  The
paper must prove:

1. the parity orientation of every edge, including the odd/even order split;
2. fixed sinks for odd order and mutually selected two-cycles for even order,
   without the false assertion that one odd-edge component has one cycle;
3. sharp maximum tail `floor((n-1)/2)` with explicit witnesses;
4. exact fixed/recurrent exponential generating functions;
5. an every-target local fibre criterion and sharp parity-dependent fibre
   maxima `(n+1)/2` and `n-1`.

## P196 — cyclic Gödel-implication dynamics

For a cyclic word on the chain `{0,...,M}`, send coordinate `i` to `M` when
`x_i<=x_(i+1)` and otherwise to `x_(i+1)`.  The paper must prove:

1. the exact one-step image/core inequality and rotation action on the core;
2. depth at most one, unique fixed point, and complete periodic-point/cycle
   counts through a transfer-matrix trace;
3. the correct characteristic polynomial
   `lambda^q-(lambda+1)^(q-1)` for the core matrix, not the rejected
   q-bonacci polynomial;
4. a gap-factorized every-target fibre formula, including all-top and
   off-core cases, and its rotation rule for higher-time fibres.

## Common delivery contract

Each package contains anonymous LaTeX, proof/source/claim ledgers, one
paper-local exact verifier and frozen transcript, immutable Round-0/1/2 PDFs,
two process-separated hostile review packages, accepted deltas, source-only
cold builds, page-level visual QA, and non-self manifests.  Posting,
submission, or any other external circulation remains unauthorized.

