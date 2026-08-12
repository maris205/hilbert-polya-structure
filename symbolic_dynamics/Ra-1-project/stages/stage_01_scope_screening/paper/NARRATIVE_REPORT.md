# Narrative Report

**Working title:** Falsification-First Symbolic Dynamics for Arithmetic Determinants: Six Audits and Seven Scoped Obstructions
**Paper type:** theory + reproducible diagnostic audit
**Status represented:** frozen Stage 01 only
**Anonymity:** anonymous shareable preprint

## One-sentence contribution

We source-lock and adversarially audit six symbolic-dynamics constructions against a five-obligation arithmetic-determinant route, proving seven scoped obstructions and finding that no single frozen object passes all five obligations or unlocks the subsequent operator route.

This sentence is deliberately weaker than a nonexistence theorem for symbolic dynamics. It concerns the six frozen objects and the explicitly stated obstruction classes only.

## Research question

Can a low-description-complexity symbolic system provide, in one and the same object,

1. an endogenous rational-prime source and logarithmic clock;
2. a complete primitive-orbit and repetition ledger;
3. a natural Fredholm or dynamical determinant;
4. the required global analytic divisor structure; and
5. a same-clock route to an operator realization?

Stage 01 tests this question without loading Riemann-zero data, fitting orbit weights to zeros, or combining favorable coordinates from different candidates.

## Claims and evidence

### Claim C1 — the audit is falsification-first and object-local

Each candidate freezes its phase space, dynamics, arithmetic origin, clock, potential/cocycle, determinant convention, function space, cutoffs, precision, controls, and forbidden data before interpretation. The Route-A records then evaluate A0--A4 for that same object. Evidence is the preregistration, methodology note, six append-only YAML evaluations, and machine-readable source locks.

**Boundary:** this is a documented protocol property, not proof that the search was exhaustive.

### Claim C2 — seven exact obstructions localize recurring failure modes

The proof packages establish:

- `SD-O01`: finite graph + finite-range data + finite-dimensional cocycle gives a finite exponential polynomial with disk divisor count $O(R)$, incompatible with a completed-Riemann $\Theta(R\log R)$ divisor;
- `SD-O02`: the squarefree admissible shift has only the zero periodic point;
- `SD-O03`: a freely concatenable shared-base renewal code creates mixed primitive words;
- `SD-O04`: unrestricted complex renewal weights represent every normalized holomorphic germ locally and therefore do not identify arithmetic structure;
- `SD-O05`: unary regular or context-free return languages cannot select exactly the prime lengths;
- `SD-O06`: finite-dimensional unitary twists cannot erase a mixed primitive factor identically;
- `SD-O07`: the endogenous wheel recursion generates primes and $\log p$ scale increments but its strict level shift is acyclic.

**Boundary:** every theorem retains its hypotheses. In particular, `SD-O01` says nothing about countable-state or genuinely infinite-dimensional transfer operators, and `SD-O05` says nothing about arbitrary computational grammars.

### Claim C3 — no frozen candidate closes A0--A4 on one object

The six Route-A records show that no candidate reaches `A4_ROUTE_B_READY`; every record has `route_b_invocation_allowed: false`. The strongest coordinates occur in different systems: `SD-C05` has the strongest endogenous rational-prime source, `SD-C04` has the strongest natural primitive/Fredholm determinant, and `SD-C06` has the strongest exact zeta-quotient identity. These coordinates are not combined.

**Boundary:** the conclusion is “none of these six frozen objects passes,” not “no symbolic-dynamics object can pass.”

### Claim C4 — finite computations certify implementations and expose controls, but do not establish analytic continuation

The four runners execute 29 tests. Exact and finite certificates include 63,319 primitive Gauss necklaces at the largest cutoff with zero cyclic/reversal/repetition failures, a wheel DAG with 98,460 vertices and 98,459 edges, and a Knauf audit through $2^{22}=4{,}194{,}304$ configurations with an independent 100-decimal-digit precision check. The renewal mechanism reconstructs both on-circle and off-circle controls exactly. Near-boundary drift is retained as a limitation.

**Boundary:** finite cutoffs validate code paths and stated finite ledgers. They neither prove asymptotic convergence nor evaluate a Riemann-zero fit.

## Candidate-by-candidate story

| ID | Frozen object | Strongest supported coordinate | Decisive failure |
|---|---|---|---|
| `SD-C01` | finite full shifts and finite-memory controls | exact function-field necklace ledger | no rational-prime ledger; $O(R)$ divisor obstruction |
| `SD-C02` | squarefree admissible subshift | classical arithmetic grammar | primes inserted; only zero is periodic |
| `SD-C03` | shared-base weighted renewal shift | exact return determinant algebra | inverse design proves too much; mixed words |
| `SD-C04` | Gauss shift and Mayer operator | natural primitive ledger and Fredholm determinant | primitive species is modular/hyperbolic, not rational primes |
| `SD-C05` | recursive wheel-sieve level shift | endogenous primes and $\log p$ increments | strict level graph is acyclic |
| `SD-C06` | Knauf binary recursion | exact unsigned zeta quotient in the proved half-plane | partition sum has no primitive-cycle Fredholm ledger; sign is extra input |

## Quantitative evidence selected for the paper

- Route-A status matrix: six YAML records under `../evaluations/route_a/`.
- Exact-certificate matrix: candidate JSON summaries and frozen CSV tables.
- Gauss cutoff ledger: `../farey_gauss_transfer/results/cutoff_table.csv` and `summary.json`.
- Wheel control separation: `../wheel_sieve_level_shift/results/level_table.csv` and `dag_certificate.json`.
- Knauf finite-depth behavior: `../knauf_spin_chain_audit/results/final_grid_analytic_errors.csv`, `precision_audit.csv`, and `summary.json`.
- Cross-candidate experiment synopsis: `../EXPERIMENT_REPORT.md`.

All figure scripts must resolve these paths relative to the paper directory and must derive plotted values from the source files.

## Figure story

1. **Route-A matrix:** a categorical view of what each frozen object actually supplies. The empty column-wise intersection is the result; the figure must not imply that strong cells from different rows can be assembled.
2. **Finite audit diagnostics:** Gauss primitive-ledger growth together with trace collisions, wheel arithmetic/control Jaccard separation with universal acyclicity, and Knauf benchmark error in and outside the proved domain. The panels demonstrate why finite evidence is useful yet obligation-specific.
3. **Candidate summary table:** exact YAML-derived verdicts and Route-B lock, suitable for black-and-white reading.

## Literature positioning

The paper uses only sources already verified in the local literature audit. The minimal cited spine is:

- Artin--Mazur for periodic-point zeta;
- Bowen--Lanford and Ruelle for finite and transfer-operator determinants;
- Pollicott and Sarig for the boundary beyond finite-memory systems;
- Mayer for the Gauss/modular Fredholm construction;
- Knauf, together with its erratum, for the arithmetic recursion;
- Cellarosi--Sinai and El Abdalaoui--Lemańczyk--de la Rue for squarefree/ℒ-free symbolic systems;
- Esparza--Ganty--Kiefer--Luttenberger for the unary semilinearity ingredient.

No citation is introduced solely from model memory.

## Limitations and nonclaims

- The six candidates do not exhaust symbolic dynamics.
- A literature gap is not a nonexistence theorem.
- A finite numerical certificate is not a proof of meromorphic continuation.
- The paper does not claim a Hilbert--Pólya operator, a proof of the Riemann hypothesis, or a fit to Riemann zeros.
- The paper does not join `SD-C04`, `SD-C05`, and `SD-C06` into a synthetic candidate.
- Ideas needing modular geometry, quantum graphs, scattering, or another primary family remain out of scope and are not developed here.

## Intended conclusion

The audit does not produce a positive candidate. Its reusable output is a collection of scoped stop rules and a reproducible example of how to prevent exact but non-identifying determinant fits from being mistaken for arithmetic dynamics. Any later symbolic candidate must source-lock the arithmetic generator, orbit ledger, determinant, analytic structure, and lift on one object before target comparison.
