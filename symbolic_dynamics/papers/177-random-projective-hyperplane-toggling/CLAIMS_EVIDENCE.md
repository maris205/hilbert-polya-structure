# Claims and evidence — P177

**Status:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`

| ID | Exact claim | All-parameter proof route | Paper-local exact attack |
|---|---|---|---|
| C1 | `h_ell=1+c_ell`; the masks span `W=<1,C>` with `dim W=d+1` | injectivity of evaluation, `1 notin C`, differences of two nonzero masks, and recovery of `1` | construct every codeword and hyperplane through `d=8`; compare masks, weights, linearity, and generated subgroup |
| C2 | the `2^m` states split into `K=2^(m-d-1)` closed irreducible cosets of size `2q`, with no transient states | a Cayley walk communicates exactly within cosets of its generated subgroup | enumerate and partition the full carriers through `d=4`; check closure, balance, degree, and component sizes |
| C3 | every component support is `K_(q,q)` minus a perfect matching and has period two | coordinates `epsilon 1+c_a`; a step adds `(1,ell)` with `ell!=0`; odd mask weights and a two-step return | compare every component neighborhood through `d=8`; check parity flips and literal two-step returns |
| C4 | the unique endpoint sum `L` has the displayed count, with support `L=0` at `t=0`, `L!=0` at `t=1`, and all `L` at `t>=2` | Fourier inversion on `V*`, where nontrivial characters sum to `-1` over nonzero forms, followed by positivity | author-side dynamic convolution through sixteen steps, literal histories through five steps, and explicit zero-count sentinels |
| C5 | phase-compatible TV is `1/(qN^(t-1))`, whereas ordinary TV to component stationarity is `1/2+1/(2q)` at time one and `1/2` thereafter | subtract the two exact probability levels from `1/q`; then include the empty parity half under stationary mass `1/(2q)` | exact rational probability and both TV computations for `d=2,...,8`, `t=1,...,16` |
| C6 | full spectrum is `1,-1,1/N,-1/N` with multiplicities `K,K,NK,NK`, and the operator is diagonalizable | Boolean-character eigenvalues; surjectivity of `S -> (parity,sigma(S))`; a complete character basis | exhaust all `2^m` characters through `d=4` and compare every rank fibre and multiplicity |
| C7 | within this family, component degree recovers `d`, and total carrier size recovers `K` | `N+1=2^d` and component size `2(N+1)` | integer reconstruction for `d=2,...,8` |
| B1 | `d=1` is excluded because the only sampled hyperplane is empty | direct evaluation of the sole nonzero form | check both literal states are fixed |

The author-side program makes 1,095,999 exact assertions and its canonical transcript is
byte-reproducible.  It proves no infinite-family theorem and makes no
literature, ownership, novelty, or release decision.

## Zero-credit boundary

No separation credit is assigned to simplex/projective codes, hyperplane
incidence and symmetric-difference design operations, additive Cayley walks,
Fourier inversion on finite Abelian groups, crown graphs or their elementary
spectra, uniform stationarity, or recurrence of finite closed irreducible
classes.  The nearest internal collision is P145's abelian/Fourier
vertex-push shell; P172/P173 monotone erosion and P175 commutator language do
not supply the literal update.  The residual conjunction remains owner-thin.
