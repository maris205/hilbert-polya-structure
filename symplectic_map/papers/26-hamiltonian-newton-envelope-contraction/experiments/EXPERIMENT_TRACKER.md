# Symbolic validation tracker

## Status convention

This tracker records the state of exact derivations planned for a proof-first paper. It is not a computational run log.

- DERIVED means the identity is worked out in notes/PROOF_PACKAGE.md.
- CROSS-CHECKED means an independent route or an exact fixture also checks it.
- BOUNDARY-FROZEN means the limitation has an explicit counterexample or a named failed proof step.
- FUTURE-TYPESET-CHECK means only exposition, equation numbering, or bibliography formatting remains.

No CAS, numerical experiment, temporary build, or external search has been run in this source-design stage.

## Core obligations

| ID | Obligation | State | Exact witness | Failure action |
|---|---|---|---|---|
| T01 | Lower and upper shears are symplectic | DERIVED | Symmetric-Hessian block multiplication | Kill the map class if either error block survives. |
| T02 | Inverse has subtraction signs and reversed phases | DERIVED | \(F^{-1}=S^{-1}T^{-1}\) | Correct indexing before using inverse degrees. |
| T03 | Every positive exposed face has nonzero Hessian determinant | DERIVED | Minimal-\(x\) coefficient \(c_0^2x_0y_0(1-x_0-y_0)\) | Kill arbitrary-support claim. |
| T04 | Face-gradient coordinates are algebraically independent | DERIVED | Characteristic-zero Jacobian criterion | Do not claim wall cancellation safety. |
| T05 | Leading-form independence persists through pure powers and substitution | DERIVED | Injective polynomial substitutions | Stop all exact degree recurrences. |
| T06 | Forward lower-shear carry is strict | DERIVED | \(\mathcal A_i(u)>\|u\|_\infty\) | Restrict support or weaken to inequalities. |
| T07 | Forward upper-shear block is visible | DERIVED | \(B\mathcal A(u)\) dominates both carried blocks | Do not identify \(\deg F^n\) with \(\|u_n^+\|_\infty\). |
| T08 | Inverse upper and lower carries are strict | DERIVED | \(Bv\), then \(\mathcal A(Bv)\) | Do not identify inverse visible block. |
| T09 | Shifted forward–inverse bridge is exact | DERIVED, CROSS-CHECKED | \(u^+_{n+1}=c_\star Bv^-_n\); fixture F1 | Remove equality of dynamical degrees if the bridge fails; never use it alone to transfer a scalar-max recurrence. |
| T10 | Projective map is decreasing on every chamber | DERIVED | Chamber derivative numerator \(1-x-y\) | Kill selector-rigidity claim. |
| T11 | Log derivative has a strict positive denominator gap | DERIVED | Quadratic gap with positive coefficients | Kill contraction. |
| T12 | One contraction constant is uniform over finite support | DERIVED | Compactification plus finite maximum | Restrict theorem to a quantified support if uniformity fails. |
| T13 | Newton walls preserve global contraction | DERIVED | Continuity plus interval splitting | Do not infer a unique fixed ray globally. |
| T14 | Inverse projective map is conjugate to forward map | DERIVED | \(L\psi=\phi L\) | State only forward selector theorem. |
| T15 | Interior fixed ray yields a stationary selector tail | DERIVED | Positive distance from chamber walls | Reclassify unresolved boundary orbit. |
| T16 | Wall fixed ray yields fixed-wall or strict alternation | DERIVED | Decreasing injective contraction | Do not advertise high-period no-go. |
| T17 | Interior Perron value has degree at most two | DERIVED | \(2\times2\) integer selector matrix | Kill uniform quadratic cap. |
| T18 | Wall per-step Perron value is a positive integer | DERIVED, CROSS-CHECKED | Common primitive wall ray; fixture F2 gives 132 | Retain only a quadratic monodromy statement. |
| T19 | Forward and inverse interior scalar degree tails have order at most two | DERIVED | Cayley–Hamilton for \(C_\xi\) and \(D_\xi=B^{-1}C_\xi B\); stable \(s_\star\ne1\) visibility; geometric \(s_\star=1\) seed | Do not claim a minimal order or omit either inverse seed case. |
| T20 | Forward and inverse strict-wall scalar degree tails have order at most four | DERIVED | Both \(M_\pm\), both \(N_\pm=B^{-1}M_\pm B\), common trace/determinant, and parity-wise inverse visibility | Do not conflate parity recurrence with consecutive order two or infer it from the bridge. |

## Fixture ledger

### F1: one-face quadratic

| Quantity | Expected exact value | State |
|---|---:|---|
| Support | \(\{(2,2)\}\) | CROSS-CHECKED |
| Scaling | \(\operatorname{diag}(3,2)\) | CROSS-CHECKED |
| Selector matrix | \(\begin{psmallmatrix}3&6\\4&2\end{psmallmatrix}\) | CROSS-CHECKED |
| Characteristic polynomial | \(t^2-5t-18\) | CROSS-CHECKED |
| Perron root | \((5+\sqrt{97})/2\) | CROSS-CHECKED |
| \(u_1^+\) | \((9,6)^\top\) | CROSS-CHECKED |
| \(v_1^-\) | \((7,8)^\top\) | CROSS-CHECKED |
| \(u_2^+\) | \((63,48)^\top=3Bv_1^-\) | CROSS-CHECKED |

### F2: transient and wall alternation

| Quantity | Expected exact value | State |
|---|---:|---|
| Support | \(\{(2,8),(4,5),(5,3)\}\) | CROSS-CHECKED |
| Walls | \(3/2,2\) | CROSS-CHECKED |
| Selector prefix | low, high, middle, high | CROSS-CHECKED |
| \(r_1,r_2,r_3\) | \(24/11,1548/781,51294/25619\) | CROSS-CHECKED |
| Common wall ray | \((2,1)^\top\) | CROSS-CHECKED |
| Common multiplier | \(132\) | CROSS-CHECKED |
| Monodromy trace | \(17648\) | CROSS-CHECKED |
| Monodromy determinant | \(3902976\) | CROSS-CHECKED |
| Monodromy eigenvalues | \(17424,224\) | CROSS-CHECKED |

## Boundary ledger

| ID | Excluded perturbation | State | Frozen reason |
|---|---|---|---|
| B01 | Axis exponents | BOUNDARY-FROZEN | Face-gradient independence and the strict two-coordinate carry can fail. |
| B02 | Exponent one | BOUNDARY-FROZEN | Strict carry is no longer automatic. |
| B03 | Mixed \(W\) | BOUNDARY-FROZEN | The projective map need not be decreasing. |
| B04 | Positive characteristic | BOUNDARY-FROZEN | Hessian and derivative coefficients may vanish. |
| B05 | Uncollected support | BOUNDARY-FROZEN | The envelope can encode absent monomials. |
| B06 | Dimension at least three | BOUNDARY-FROZEN | A one-dimensional decreasing contraction no longer classifies projective dynamics. |
| B07 | Changed seed or phase order | BOUNDARY-FROZEN | The exact bridge base case changes. |
| B08 | Genericity replacement | BOUNDARY-FROZEN | The theorem is coefficient-uniform and cannot hide wall cancellation in a generic clause. |
| B09 | Higher dynamical degrees, entropy, compactification, or integrability | BOUNDARY-FROZEN | None is computed by the present total-degree argument. |
| B10 | Global priority or classification | BOUNDARY-FROZEN | Local bibliography has not undergone an external novelty search. |

## Expository work remaining

| Item | State | Completion test |
|---|---|---|
| Convert proof package into numbered lemmas and one main theorem | FUTURE-TYPESET-CHECK | All hypotheses appear once and dependencies are forward-only. |
| Keep the two fixtures in the main text | FUTURE-TYPESET-CHECK | Every displayed integer can be checked without software. |
| Condense boundary ledger into a limitations proposition and discussion | FUTURE-TYPESET-CHECK | No excluded case reads like a conjectural extension. |
| Build bibliography from locally frozen metadata | FUTURE-TYPESET-CHECK | Every entry is independently verified before publication. |
| Audit page allocation | FUTURE-TYPESET-CHECK | Proof content, not process text, occupies the planned 22–30 pages. |

## Stop conditions for the later manuscript stage

The manuscript must pause if any of these occurs:

1. a wall face is replaced by a single tied monomial in a proof;
2. algebraic independence is assumed rather than derived;
3. a numerical selector alternation is called a two-cycle;
4. the wall Perron value is reported as quadratic rather than integral;
5. the exact bridge loses its shift or ordinary-seed hypothesis;
6. the theorem is compared to recent literature without external verification;
7. an excluded support or mixed momentum Hamiltonian is silently reintroduced.

The present source package marks every mathematical obligation as derived or boundary-frozen. It reports no experimental result.
