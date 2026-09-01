# P142 paper plan

**Working title:** Valuation--GCD Dynamics on Prime-Power Divisors: Exact
Entry Times and Every-Target Fibres
**Type:** anonymous rigorous mathematical short note
**Status:** `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`
**Target length:** 4--6 A4 pages including references
**Absolute ceiling:** P142 in
`docs/papers142_146_sequence/phase1/FINAL_THEOREM_CONTRACTS.md`
**One-sentence contribution:** For the literal odd-prime divisor map
`d -> gcd(p^e,d^2+p^e/d)`, prove its exact valuation conjugacy and the complete
recurrent, entry-time, temporal-polynomial, image, and every-target fibre
atlas, including the sharp binary obstruction.

## Claims--evidence matrix

| Claim | Formal proof object | Paper-local control | Credit boundary |
|---|---|---|---|
| The literal gcd map is conjugate under `p^a <-> a` to `T_e(a)=min(2a,e-a)` for odd `p`; at `p=2,e=3a` its valuation is `2a+1`. | Valuation lemma and binary-boundary remark. | Literal gcds in 508 odd-prime boxes and 47 binary boxes. | Elementary valuation algebra is zero credit; oddness must stay visible. |
| The recurrent set is `{0} union [L,U]`; zero and, for even `e`, `e/2` are fixed, all other recurrent states pair, and `Fix(T_e^k)` depends only on the parity of `k`. | Recurrence theorem using the invariant complement band and entry argument. | Complete bounded functional graphs and iterates `k=1,...,12`. | Generic finite-map and zeta bookkeeping are zero credit. |
| The four-case pointwise entry law holds; the maximum is `1+ceil(log_2 L)` with the stated unique deepest exponent. | Doubling/reflection theorem, including separate `e=2,3` boundary. | Every state through `e=128`; exact deepest-set comparison. | Ceiling-log manipulation is zero credit. |
| The exact temporal polynomial is `R+z+(1+z) sum c_j z^j`. | Dyadic-layer count paired by reflection. | Complete depth histograms in every odd-prime box. | Formal generating-function packaging is zero credit. |
| The image is `[0,U]` and every target has the displayed zero/one/two-element fibre. | Direct solution of the two branch equations and their inequalities. | All 33,528 target cells for each odd prime, including coincident branches. | Generic inverse-branch vocabulary is zero credit. |

## Paper architecture

1. **Scope, ownership, and complete statement.**  Define the literal map,
   exponent carrier, entry time, and frozen notation.  State all claims in one
   theorem without novelty language.
2. **Literal valuation and binary boundary.**  Prove the arithmetic identity
   before using the exponent map; isolate the exact characteristic-two
   failure.
3. **Recurrent band and fixed iterates.**  Establish the branch decomposition,
   invariant band, complement cycles, fixed-iterate counts, and the
   zero-credit zeta corollary.
4. **Pointwise entry times and temporal polynomial.**  Prove the four cases,
   sharp uniqueness, and the complete dyadic layer census.
5. **Image and every-target fibres.**  Solve both branch equations, enforce
   their domains, and handle the coincidence as set union.
6. **Exact controls and limitations.**  Report deterministic falsification
   coverage, primary-source boundary, cosmetic-lift risk, and
   `HOLD_EXTERNAL`.

## Figure decision

No figure is needed or planned.  The state space is a one-dimensional integer
interval, and the two branch equations, entry-time formula, and temporal
polynomial carry the exact information more efficiently than a graph drawing.
One compact table reports selected exact control profiles; it is evidence
bookkeeping, not a figure or empirical experiment.

## Citation plan

Only the three primary sources already verified in the algebraic scout are
used:

- Milnor--Thurston for general piecewise-monotone interval-map background;
- Kuzovlev for reversible finite discrete tent-map cycle investigations; and
- Choi--Kim--Song--Shin--Lee--Noh for a different bijective finite skew-tent
  construction.

All three citations delimit zero-credit background.  None is cited as
evidence that the literal gcd map is new.  Exact metadata and claim use are
recorded in `SOURCE_VERIFICATION.md`.

## Closure conditions

- Every frozen item has a complete symbolic proof in `main.tex`.
- The characteristic-two failure is displayed, not hidden in a hypothesis.
- The verifier transcript replays byte for byte.
- `pdflatex`, `bibtex`, and two settling `pdflatex` passes succeed cleanly.
- `main_round0_original.pdf` preserves the first stable author build.
- No review files are created in this stage.
- No novelty, priority, authorship, posting, contact, submission, or release
  claim is made; external status remains `HOLD_EXTERNAL`.
