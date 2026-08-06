# Breadth-first Hénon structure search

Status: **C02C effective finite-window theorem retained; C02D is closed
`NO_GO` with a formal Route-A rejection; the next breadth-first source lock
is HCS-C12A, and no Hilbert--Pólya claim is made**.

Primary legacy source:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`

This project takes the exact reversible, area-preserving family from Paper 5,

\[
H_a(q,p)=(1-aq^2-p,q),\qquad \det DH_a=1,
\]

and searches breadth-first for intrinsic periodic-orbit, analytic, arithmetic,
or operator structures.  It does not inherit the legacy zero fits, fitted
parameter schedules, quartic Schrödinger surrogate, or averaged transition
matrices as mathematical foundations.

## Current ruling

Three source-locked first-round micro-pilots, followed by the C02C theorem
experiment, were run without Riemann-zero or target-prime fitting data.

## Layered status

| Layer | Status |
|---|---|
| C02C experiment | `PASS` |
| C02C theorem | `PROVED_EFFECTIVE_SPECIALIZATION; NOVELTY_DELTA_UNCONFIRMED` |
| paper | `MANUSCRIPT_HOLD` |
| C02C formal Route-A validator | `NOT_TESTABLE` |
| C02C informal Route-A ceiling | `ROUTE_A_EXPLORATORY` |
| C02D | `CLOSED_NO_GO; ROUTE_A_REJECTED; NO_SPECTRUM_RUN` |

| Candidate | Strongest result | Route-A screening | Decision |
|---|---|---|---|
| C02/C02B: complex/projective strictification | Explicit complex signed-root sequence polydiscs strictly self-map with contraction \(2/\sqrt{17}\); the true projective derivative cocycle contracts separated complex fibre disks. | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`; `ROUTE_A_EXPLORATORY` | retained and extended by C02C |
| C02C: effective finite-window pinning | Full endpoint disks, exponential localization, genuine two-coordinate gluing, exact matching/Hill/monodromy identity, and exact complex-base projective disks. | same informal ceiling; formally `NOT_TESTABLE` because no infinite operator or normalization is frozen | `RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD; NOVELTY_DELTA_UNCONFIRMED` pending a trace-compatible operator approximation theorem |
| C02D: trace-compatible finite-memory pinning operator | New explicit mixed BPS domains; exact proof that C02C windows are \(\mathcal L^N\) word data rather than the frozen same-clock approximants; orbitwise scalar repetition obstruction. | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`; formal `ROUTE_A_REJECTED` | close the pre-registered operator lane; retain the domain lemma and HEN-O15/HEN-O16 |
| C03: finite-field Euler product | Exact local permutation zetas over 54 primes, but matched reversible controls explain the conspicuous cycle statistics and no canonical global mechanism exists. | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`; `ROUTE_A_REJECTED` | stop naive global product; retain local arithmetic ledger |
| C05: action--Maslov determinant | Exact Hill/repetition ledger, but \(S\mapsto S+C\) rotates the determinant variable and \(\mu(\gamma)=\#\{i:q_i<0\}\) is only a one-symbol weight. | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`; `ROUTE_A_REJECTED` for intrinsic fixed-\(z\) phase | hard-kill absolute-phase claim; retain obstruction and ledger |

None of the original three pilots reached BF3, so no schema-complete Route-A
YAML was created for them. C02C still lacks the function space, infinite
operator and normalization needed for Route-A input validation. The later
C02D closure froze a narrower standard-kernel/scalar-repair object and created
a schema-complete rejection YAML. Route B remains closed.

## Positive theorem and its boundary

For every admissible sign itinerary, define

\[
K_\varepsilon=
\prod_i\overline D\left(\varepsilon_i\frac{23}{48},\frac7{48}\right).
\]

The signed-root Hénon orbit solver

\[
(T_\varepsilon q)_i=
\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}
\]

is holomorphic near \(K_\varepsilon\), strictly preserves it, and contracts
by at most \(2/\sqrt{17}\).  An independent audit verified the proof,
including the doubled chronological neighbor occurrences for cyclic periods
one and two.  The underlying real SFT and real signed-root uniqueness are not
new: they are the \(b=1,k=6\) case of Sterling--Dullin--Meiss Theorem 3 after
the linear sign/scale conjugacy.

The second-stage C02C theorem converts this into a finite-window system.  For
every admissible extended word and both full complex endpoint disks it proves
a unique jointly holomorphic solution and

\[
|\partial_uQ_i|\le\beta\kappa^{i-1},\qquad
|\partial_vQ_i|\le\beta\kappa^{N-i},
\quad
\beta=\frac1{\sqrt{17}-2}.
\]

It also proves genuine two-coordinate chronological gluing and

\[
\det DF_N=-\frac{\det(I-DH_6^N)}{\det L_N},
\]

with the signed trace-residue factor and exact complex-base projective disks.
This is still **not** a nuclear transfer operator, an infinite Fredholm
determinant, an arithmetic divisor, or a Hilbert--Pólya structure.

## Next paper decision

The scoped WP0 source-location audit is complete for routing.
Sterling--Dullin--Meiss Theorem 3 already covers the linearly conjugate real
\(b=1,k=6\) signed-root SFT and real uniqueness.  Rugh and
Baladi--Pujals--Sambarino contain the qualitative analytic pinning,
composition and periodic-closure mechanisms; BPS's trace convention yields an
absolute determinant denominator, not the signed operator still proposed.
C02C therefore survives only as an explicit complex effective \(H_6\)
specialization whose publishable novelty is unconfirmed: exact domains,
constants, chronological identities and independent certificates.

C02D has now performed that gate and returned `NO_GO` before any spectrum
run. The standard BPS/Rugh kernel is already exact at one step; C02C windows
supply \(\mathcal L^N\) word-pinning data or exact higher-block recodings, not
the frozen finite-memory approximation. The raw-kernel sign also cannot be
repaired orbitwise by a scalar multiplicative edge cocycle across primitive
cycles and their repetitions. Aggregate-only accidental cancellation between
different orbits is not ruled out. The complete closure is in
`../henon_pinning_trace_obstruction/`.

The next authorized package is **HCS-C12A WP0 only**: source-lock the two-axis
Frobenius--dynamical periodic-point scheme
\(N_{a,p}(r,n)=\#\operatorname{Fix}(H_a^n)(\mathbb F_{p^r})\), keeping
Frobenius degree \(r\) and chronological time \(n\) distinct. No finite-field
engine, diagonal \(r=n\), Euler product, or \(p^{-s}\) substitution is
authorized before that audit. The roadmap is
`../henon_pinning_trace_obstruction/NEXT_BREADTH_ROADMAP.md`.

## Reusable laboratory

The pilots use the certified local \(H_6\) subsystem and its orbit catalogue:

- four-state mixing symbolic dynamics and certified local hyperbolicity;
- 2,170 primitive local cycles through period 20;
- exact/certified coordinates, words, reversors, actions, and monodromy data;
- a positive non-lattice instability roof;
- deterministic controls and independent checks.

These data describe a certified **local** survivor, not the entire bounded
Hénon set.

## Navigation

- `PAPER_PLAN.md` -- next-paper theorem and manuscript roadmap;
- `DERIVATION_PACKAGE.md` -- analytic T2--T3 derivation, constants and claim
  boundaries;
- `refine-logs/EXPERIMENT_PLAN.md` -- frozen first-round protocols;
- `refine-logs/EXPERIMENT_RESULTS.md` -- raw comparison tables, findings, and
  Route-A screening;
- `refine-logs/PAPER_PLAN_AUDIT.md` -- independent theorem/roadmap and
  prior-art collision audit;
- `paper/c02b_complex_polydisc_theorem.md` -- proved analytic bridge;
- `paper/c02c_effective_finite_window_theorem.md` -- effective endpoint,
  matching/Hill and complex-projective theorem;
- `refine-logs/C02D_OPERATOR_EXPERIMENT_PLAN.md` -- closed trace-compatible
  operator gate;
- `../henon_pinning_trace_obstruction/` -- C02D obstruction project, formal
  Route-A rejection, and HCS-C12A next-breadth roadmap;
- `code/README.md` -- canonical reproduction commands;
- `results/README.md` -- artifact map and decisions;
- `SOURCE_AUDIT.md` -- local/external novelty boundary;
- `CANDIDATE_REGISTRY.md` -- all twelve generated candidate families;
- `SEARCH_PROTOCOL.md` -- breadth-first gates and data firewall.

## Claim boundary

The surviving direction is a rigorous complex-dynamics construction, not an
RH result.  The real SFT/uniqueness and general analytic-hyperbolic
pinning/absolute-Fredholm mechanisms are prior art.  Complex Hénon literature
supplies collision context but does not directly certify the present
determinant-one complex disks or a signed operator.  If C02D adds no genuinely
new aggregate trace-compatible theorem, this lane returns to infrastructure
and the RH search resumes breadth-first generation.
