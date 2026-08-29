# Claims–Evidence Map

Status: **anonymous author draft / exact controls pass / external HOLD**.

Finite computation is falsification evidence only. It is not an asymptotic
proof, owner verdict, novelty result, or priority claim.

| Claim | Proof anchor | Independent exact control | Residual risk |
|---|---|---|---|
| Both generators have tropical spectral radius zero, bounded powers, and tropical rank two | Proposition 2.1: cycle means, cross-sum rank criterion, explicit even/odd powers | Cycle means and cross-sums; literal powers through exponent 64 | “Rank one” is fixed to the finite 2-by-2 tropical row-scalar criterion; no other rank convention is silently used |
| No reset occurs at lengths one or two, and exactly `ABA/ABB/BAA/BAB` reset at length three with output gaps `-3,0,0,3` | Proposition 2.2: exhaustive cross-sum defects, literal products, constant row differences | All words through length three, exact four matrices, both column gaps, and finite input-gap sentinels | The reset/coupling mechanism is classical background and is not claimed as a novelty |
| At `p=0,1`, height is `n mod 2`, rate and pressure are zero, and fluctuations are degenerate | Corollary 2.3, proved directly from deterministic powers | Exact endpoint laws through time 32 and powers through exponent 64 | Endpoint statements must not be inferred from interior primitivity |
| The chronological literal gap is confined to `{-3,-2,0,2,3}` | Equations (3.2)–(3.3) and Theorem 3.1 | Every word through length 16; direct local vector actions for all ten gap/letter cases | Reversing `M_n=X_n⊗...⊗X_1` changes literal products |
| Sign grouping gives the requested strong reward lumping to `N,Z,P` | Theorem 3.1 checks both representatives of each nonzero lump | Literal gap/lumped state/reward agreement for all 131,071 words | State lumping without reward lumping would be insufficient; both are checked |
| `H_n` equals the accumulated reward and has the exact finite-time PGF | Equation (3.1), Theorems 3.1–3.2 | Literal product, vector action, five-gap reward, lumped reward, exhaustive histograms, and independent DP | A misplaced row/column orientation in `Q` would preserve some low moments; full laws and a nonpalindrome are checked |
| The characteristic cubic is `r^3+(2a-1-ay^2)r-ay` | Determinant expansion in Theorem 3.2 | Direct 3-by-3 determinant versus closed cubic at 175 exact `(p,r,y)` triples | The variable `r` is an ordinary characteristic root; `y` is the reward tilt |
| The stationary law and positive drift are explicit | Lemma 4.1: balance equations and negative-transition mass | Exact stationarity and reward sums at seven interior probabilities | The stationary law is not asserted at reducible endpoints |
| The SLLN and CLT hold with the displayed variance | Theorem 4.2: finite-chain ergodic theorem, explicit Poisson solution, bounded martingale CLT | Exact Poisson equations, zero conditional means, and stationary second moments | Exact arithmetic verifies formulas, not convergence; the probabilistic proof supplies convergence |
| The same drift and variance are Perron derivatives | Proposition 4.3: first and second implicit differentiation of the cubic | Exact derivative identities at seven interior probabilities | Agreement is a cross-route check, not a third generic limit theorem |
| Pressure is the log Perron root and `H_n/n` has the Legendre LDP | Theorem 5.1: primitive finite kernel, analytic perturbation, full-domain differentiability, vacuous boundary steepness, exponential tightness, Gärtner–Ellis | Exact DP/transfer PGFs through time 32 at seven biases and five positive rational tilts | Generic Gärtner–Ellis and Perron theory are owned background |
| The attainable heights are exactly all parity-compatible values, with exactly two alternating maximizers | Proposition 5.2: isolated negative rewards, `(AA)^k` plus alternating-suffix witnesses, and forced alternation | Exhaustion of all words through length 16, explicit support witnesses, empty-word and rare-event sentinels | “Exactly two” is restricted to `n>=1`; the empty word is handled separately |
| The extremal masses and both temperature edges are exact | Proposition 5.2 and Theorem 5.3: alternating/block probabilities, scaled kernel, diagonal similarity | Exact extremal masses; conjugated kernels and limiting characteristic polynomials | Temperature-edge formulas assume `0<p<1`; deterministic endpoint pressure is separately zero |

## Proof-route dependency map

1. Literal products give generator behavior and the minimal reset audit.
2. Literal matrix/vector equality gives the global height.
3. Five-gap closure gives the exact local state.
4. Strong reward lumping gives the finite transfer matrix.
5. The untilted kernel gives stationarity and the Poisson equation.
6. The tilted kernel and cubic give pressure derivatives and LDP.
7. Local reward geometry gives exact words and rare events.
8. Scaled/conjugated kernels give the two spectral edges.

No theorem depends on finite enumeration for its proof.

## Owner subtraction

- Baccelli–Cohen–Olsder–Quadrat provide the max-plus/discrete-event algebraic
  framework.
- Gaubert (1995), Mairesse (1997), Baccelli–Hong (2000), and
  Blondel–Gaubert–Tsitsiklis (2000) own direct automata, random-product
  Lyapunov, analytic-expansion, and set-spectral-radius frameworks.
- Merlet provides projective-semigroup, memory-loss, and topical-operator
  SLLN/CLT/LDP theory.
- Goverde–Heidergott–Merlet (2011), van den Boom–De Schutter (2012), and
  Kordonis–Maragos–Papavassilopoulos (2018) own direct coupling-estimation,
  switching-system, and Markov-jump frameworks.
- Dembo–Zeitouni provide the general large-deviation theorem invoked after
  the pair-specific pressure has been computed.

These sources receive full background credit. The residual is only the
displayed pair's five gaps, reward table, rational drift/variance, cubic,
exact word extremes, and temperature formulas. Tropical equivalence classes
have not been exhausted. The residual is not labeled novel, first, or
priority-bearing.

## Internal mechanism comparisons

- **P89:** both systems have reset/coupling features. Here the carrier is a
  finite max-plus projective state, the observable is additive matrix height,
  and the proof uses a three-state reward kernel rather than a regeneration
  decomposition; absence of resets is not a distinction.
- **P93:** unbounded stack/free reduction/reflection; absent here.
- **P101:** cap–floor and coalescence time; absent here.
- **P104:** ordinary contracting monomial matrices, parity, singular values;
  absent here.
- **P111:** positive unipotent products and quadratic ordered-subword area;
  absent here.

The present primitive object is a full finite max-plus pair; its observable
is the order-`n` global matrix maximum with a three-state projective reward.
