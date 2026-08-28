# Papers 92–96 candidate pool and kill ledger

Evidence cutoff: 2026-08-28 UTC. Route: **A / Symbolic Dynamics**.
External release: **HOLD**.

This round enforced a two-probe patience budget. A candidate survived only
when one exact probe exposed a theorem-sized pattern and a second,
implementation-independent probe preserved the mechanism at endpoints or a
new observable. Directly owned mechanisms, P1–P91 collisions, and attractive
formulas without independent theorem mass were stopped. Search absence is
recorded only as `BOUNDED_NO_EXACT_COLLISION_FOUND`, never as proof of
worldwide novelty.

## Selected sequence

| ID | Primary dynamical system | Concrete residual advance | Gate |
|---:|---|---|---|
| P92 | primitive finite-field recurrence-avoidance SFT | a nonzero-error formulation and Fourier transfer compress the `q^r`-state characteristic polynomial to two factors, give all fixed counts/zeta, and expose the first anomaly at `q^r-1` | `GO_OWNER_SUBTRACTED_LFSR_BACKGROUND` |
| P93 | Bernoulli push–pop cocycle on a one-sided full shift | exact bicyclic normal form couples image-cylinder depth and fiber degree to a walk maximum/drawdown; quenched and annealed rates have different thresholds, with a critical stretched/exponential split | `GO_OWNER_SUBTRACTED_RANDOM_WALK_BACKGROUND` |
| P94 | marked symmetric two-letter S-adic shift | the marker `10` gives exact recognizability; the entire invariant-measure simplex is a closed product interval with a sharp summability transition and explicit `n`/`n^2` constants | `GO_OWNER_SUBTRACTED_MEASURE_TRANSFER` |
| P95 | minimal-slack no-repeat SFT | using the Ruskey--Williams Cayley graph as cited background, the no-repeat realization has a two-island short-period desert and a delayed-geometric color-return law with rational generating function | `GO_AFTER_DIRECT_GRAPH_OWNER_SUBTRACTION` |
| P96 | finite-subset hyperspace of the expanding circle map | the circle specialization of binary orbit selection has a rational Euler collapse, exact cardinality strata, odd/even fixed counts, alternating zeta, all temporal orbits, and rigidity; `k log d` is retained as a standard Bowen-factor control | `GO_OWNER_SUBTRACTED_HYPERSPACE_TOPOLOGY` |

## Diversity ledger

| Pairwise field | P92 | P93 | P94 | P95 | P96 |
|---|---|---|---|---|---|
| phase space | mixing finite-state subshift | one-sided full shift under random endomorphisms | minimal nonstationary two-letter subshift | high-block exclusion subshift | compact finite-subset hyperspace of `S^1` |
| action | deterministic shift | iid semigroup cocycle | deterministic shift from a directive sequence | deterministic shift | induced expanding continuous map |
| headline invariant | characteristic polynomial / first zeta anomaly | image and fiber Lyapunov observables | invariant-measure simplex | short periods and color returns | fixed subsets, zeta, and topological entropy |
| proof engine | finite-field characters and Singer orbit | bicyclic normal form plus reflected random walk | exact marker plus two-tower inverse limit | cited Cayley presentation plus cycle-power ledger and renewal | base-orbit Euler transform plus parity collapse |

P92 and P95 are both mixing SFTs, but they do not share the object or proof
engine: P92 removes one linear recurrence successor and is controlled by a
Singer cycle/Fourier transform, while P95 is a nonlinear high-block repulsion
rule controlled by two permutation generators and a color-return renewal.
No other selected pair shares both phase space and headline mechanism.

## Frozen early signals

### P92 — primitive recurrence avoidance

For a primitive degree-`r` companion recurrence over `F_q`, forbid exactly
the predicted next symbol. With `L=q^r-1`, the proposed adjacency matrix has

```text
chi_A(lambda)
  = (lambda-(q-1))
    (lambda^L-(q-1)^(q^(r-1)-1)).
```

Consequently its zeta has two factors and, for every `n<L`, its fixed count
is exactly `(q-1)^n`; the first deviation from the full `(q-1)`-shift occurs
at `L` and recovers `r` when `q` is fixed. Exact characteristic-polynomial,
rank, and trace probes passed at `(q,r)=(3,2),(3,3),(5,2)`.

### P93 — random push–pop

Let pop have probability `p` and each uniformly labelled push probability
`(1-p)/b`. For the walk `S_t=#pop-#push`, put
`M_t=max_(s<=t) S_s`. Every environment word has unique normal form
`C_u D^J`, with

```text
J_t=M_t,       I_t=|u|=M_t-S_t.
```

The image is one cylinder of depth `I_t` and every image point has exactly
`b^J_t` preimages. The pathwise thresholds occur at `p=1/2`; the annealed
degree threshold occurs earlier at `p=1/(b+1)`. A finite-time ballot formula,
all word normal forms through length 12, exact dynamic programming, and the
critical prefactor were independently checked.

### P94 — marked symmetric S-adic family

For `a_n>=1`, use

```text
sigma_n(0)=0^(a_n+1)1,
sigma_n(1)=0 1^(a_n+1).
```

The word `10` appears exactly at supertile boundaries. The normalized
incidence matrix contracts the bias coordinate by
`rho_n=a_n/(a_n+2)`. Recognizable two-tower measure transfer therefore gives
the full bias interval `[-R,R]`, where `R=prod rho_n`; in the frequency
coordinate `mu([0])`, the interval is `[(1-R)/2,(1+R)/2]`. Unique ergodicity
holds exactly when `sum 1/a_n` diverges; otherwise the interval has exactly
two ergodic endpoints. Marker, contraction, and product-constant probes all
passed.

### P95 — minimal-slack no-repeat

Forbid a repeated color at gaps `1,...,q-2`. Completing a legal
`(q-1)`-block by its unique missing color identifies the block graph with
the Ruskey--Williams Cayley graph on `S_q`; that graph is cited background,
not a residual contribution. The two successors are a `(q-1)`-cycle and a
`q`-cycle. Exact probes
give

```text
F_n=0                 for n<=q-2,
F_(q-1)=F_q=q!,
F_n=0                 for q+1<=n<=2q-3,
```

and the conditional color-return series `(2-z)/(2-z-z^(q-1))`. Sparse graph
traces and literal cyclic-word enumeration agree.

### P96 — finite-subset circle expansion

Let `exp_k(S^1)` be the nonempty subsets of the circle of size at most `k`,
and let `H_(d,k)` be induced by `x -> d x mod 1`. For `Q=d^n`, a subset fixed
by `H^n` is a disjoint selection of periodic orbits of the base map. Its
exact-cardinality generating series is

```text
prod_(ell>=1) (1+u^ell)^O_ell(Q)
  = (1-Q u^2)/((1-Q u)(1+u)).
```

This gives the stratum coefficient
`E_j(Q)=(Q-1)(Q^j-(-1)^j)/(Q+1)`, an odd/even total fixed-count polynomial,
an alternating product for the Artin–Mazur zeta, temporal orbit census, and
parameter rigidity. Entropy `k log d` is a standard finite-to-one Bowen
control, not a novelty claim. Euler-transform, formal-zeta, and literal
rational-circle orbit probes passed through the registered cutoffs.

## Killed or reserved candidates

| Candidate | Decision | Reason |
|---|---|---|
| higher-form closed cubical cochain shift | `KILL_INTERNAL_P67_P69_P70` | the rank and torus-count formulas are correct, but the engine is cellular cohomology and collides with three recent linear/flat shifts; small literal quotients also require repeated-face care |
| multiplicative Fibonacci map `(a,b)->(b,ab)` over `F_q` | `KILL_OWNER_AND_INTERNAL` | monomial finite-system work owns the support/core and logarithmic linearization; the remaining SNF ledger overlaps P70 and the transient-core story overlaps P90 |
| projective-plane consecutive-triple independence | `KILL_DIRECT_OWNER` | it is the nonbacktracking edge shift of the projective-plane Levi graph sampled every two steps; the attractive spectrum is an Ihara–Bass/design-spectrum corollary |
| nonabelian constant-window product | `KILL_INTERNAL_P91` | the centralizer/root census reuses the generalized-dihedral relation semantics too soon |
| two-reflection adjacent-sum SFT | `KILL_INTERNAL_P84_P91` | its path spectrum and first-wrap anomaly remain a finite relation-graph spectral package |
| cyclic bijective substitutions | `KILL_DIRECT_OWNER_AND_P77` | reversing/extended symmetries of bijective substitutions are directly owned and the automatic-tower mechanism is occupied |
| independent-set Coxeter toggles | `KILL_DIRECT_OWNER_NO_SIGNAL` | direct toggle/homomesy owners exist and the second cycle probe loses a closed pattern |
| bounded-density shift | `KILL_DIRECT_OWNER_NO_CLOSED_SECOND_PROBE` | structural properties are owned and the proposed exact entropy did not survive the patience budget |
| finite-field closed cochain and Johnson-replacement shifts | `RESERVE_INTERNAL_COLLISION` | exact formulas exist, but the residual advance is weaker than the selected systems and too close to prior rank/spectral packages |
| equal-window-sum torsion shift | `RESERVE_GO_INTERNAL` | telescoping, root-count fixed formula, and torsion resonance are exact, but the finite-subset hyperspace contributes a stronger and more distinct fifth system |
| Bernoulli-leaky cyclic register | `RESERVE_GO_INTERNAL` | exact image law and geometric-maximum synchronization are strong, but selecting it beside P93 would spend two slots on closely related random information-loss cocycles |
| Margolus two-matching swap | `RESERVE_P90_PROXIMITY` | the parity-dependent cycle normal form is exact, but a reversible finite lattice update immediately after Rule 184 weakens batch diversity |

## Release boundary

All five selections are internal theorem contracts. Public posting,
submission, author contact, venue selection, specialist priority clearance,
and absolute novelty language remain unauthorized and `HOLD`.
