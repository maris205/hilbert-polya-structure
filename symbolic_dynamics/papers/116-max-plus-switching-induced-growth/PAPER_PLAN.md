# Paper Plan — Switching-Induced Growth for a Neutral Max-Plus Pair

Status: **independent author draft / external HOLD**.

## One-sentence contribution

For one explicit Bernoulli pair of full tropical-rank (2\times2) matrices,
both deterministic generators have bounded powers and zero tropical growth,
whereas every nondegenerate iid mixture has an exactly computable positive
growth rate, full finite-time transfer law, Gaussian fluctuation variance,
pressure, large-deviation principle, and two zero-temperature pressure edges.

## Scope and non-scope

The paper treats only

```text
A = [[-2,-1],[ 1,-1]],   P(A)=p,
B = [[-1, 1],[-1,-2]],   P(B)=q=1-p,
M_n = X_n ⊗ ... ⊗ X_1,   H_n=max entries of M_n,   H_0=0.
```

It does not claim generic max-plus automata, random-product Lyapunov theory,
reset/coupling or memory loss, switching models, SLLNs, CLTs, LDPs, or
topical-operator spectral theory. Those are owner-subtracted background.
It does not claim that tropical equivalences of the displayed pair have been
exhausted. It makes no novelty or priority assertion, and external
circulation remains HOLD.

## Theorem chain

1. **Neutral generator proposition.** Compute both tropical spectral radii,
   tropical-rank obstructions, and all deterministic powers. Conclude
   `H_n(A^n)=H_n(B^n)=n mod 2` and deterministic growth zero.
2. **Minimal reset proposition.** Prove that lengths one and two contain no
   tropical-rank-one product and that exactly `ABA/ABB/BAA/BAB` reset at
   length three, with their literal matrices and constant output gaps.
3. **Literal projective theorem.** Starting from `(0,0)`, prove that the gap
   lies in `{-3,-2,0,2,3}` and that sign-lumping gives the exact `N/Z/P`
   reward table under the chronological left-product convention.
4. **Finite-law theorem.** Derive
   `E[y^H_n]=e_Z^T Q_p(y)^n 1` and the cubic characteristic polynomial.
5. **Interior limit theorem.** Compute the stationary law, drift, explicit
   Poisson solution, martingale CLT variance, and recover the derivatives of
   the same kernel's Perron cubic; only the two variance calculations are
   independent once the literal kernel is fixed.
6. **Pressure/LDP theorem.** Identify the pressure with the logarithm of the
   Perron root, prove analyticity and the Legendre-transform LDP, then prove
   exact parity-compatible word support and both zero-temperature edges.
7. **Scope theorem-by-context.** Subtract all listed direct owners and state
   truthful P89/P93/P101/P104/P111 mechanism comparisons.

## Two complementary proof routes

| route | primitive object | principal outputs | local failure modes |
|---|---|---|---|
| Tropical literal/projective | raw max-plus products and the row-max gap | orientation, minimal reset products, five reachable gaps, strong lumping, bounded generator powers, exact word support | a reversed product or incorrect row maximum breaks the route before probability enters |
| Markov-additive spectral | the tilted three-state kernel | finite PGF, stationary drift, Poisson variance, Perron cubic, pressure, LDP, temperature edges | a misplaced reward or transition probability changes the cubic and all derivatives |

The two routes meet at the identity between the literal height and the
accumulated reward. The first supplies the kernel consumed by the second, so
they are complementary rather than logically independent. Conditional on
that kernel, the Poisson and Perron computations of the variance are
independent checks.

## Section plan

1. Introduction: anomaly, exact package, owner subtraction, contribution list.
2. Neutral max-plus generators: definitions, ranks, spectral radii, powers,
   minimal reset words, endpoints.
3. Literal projective reduction: five gaps, strong lumping, reward table,
   finite-time PGF, characteristic cubic.
4. Interior stochastic limit theory: stationary law, SLLN, martingale CLT,
   explicit variance, independent Perron derivatives.
5. Pressure and rare words: LDP, exact word support and maximizers,
   extremal-event masses, positive/negative temperature limits.
6. Proof architecture and scope: complementary routes, owner subtraction,
   internal mechanism comparisons, exact controls and limitations.
7. Conclusion: exact switching-induced growth boundary and HOLD status.

## Claims–evidence matrix

| claim | proof evidence | exact finite control |
|---|---|---|
| each generator is neutral, bounded, and not tropical rank one | cycle means, cross-sum test, explicit power cycle | powers through exponent 64 |
| exactly four shortest reset words occur at length three | exhaustive rank defects and literal product matrices | all words through length three; constant-gap actions |
| the literal five-gap process lumps strongly | local max-plus vector formulas for both representatives of each sign lump | all words through length 16; local transition checks |
| the PGF and cubic are exact | Markov-additive transfer and direct determinant expansion | DP/transfer agreement through time 32 at seven biases and five tilts |
| the interior drift and variance have the displayed rational forms | stationary balance, Poisson martingale, implicit Perron derivatives | exact Fraction checks at seven interior biases |
| exact parity-compatible support and two maximizers hold | isolated negative rewards, `AA`-block witnesses, and forced alternation | all 131,071 words through length 16 plus explicit witnesses |
| both pressure edges have the displayed constants | scaled Perron matrices and diagonal similarity | exact limiting-polynomial and rare-event identities |

Finite computation is falsification evidence only. It does not prove an
infinite-horizon statement or establish external ownership.

## Reproducibility and packaging

- `main.tex`, `math_commands.tex`, `sections/*.tex`, `references.bib`:
  anonymous amsart manuscript.
- `code/verify.py`, `code/verify.out`: standard-library exact verifier and
  stored fresh author run.
- `NARRATIVE_REPORT.md`: derivation spine and proof-dependency narrative.
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`: traceability and control limits.
- `README.md`, `BUILD.md`: package entry point and reproducible build record.

No final QA, hash seal, Git action, public posting, or paper priority decision
belongs to this author-stage plan. Independent hostile reviews and their
resolution ledger remain internal inputs under external HOLD.
