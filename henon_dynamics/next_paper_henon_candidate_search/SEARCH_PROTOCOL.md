# Search protocol

## 1. Research mode

This is an RH breadth-first search, not a conditional proof program.  The unit
of progress is either a new invariant structure or a reusable obstruction.
The protocol is deliberately asymmetric: ideas are cheap to generate and
expensive to promote.

## 2. Promotion gates

### BF0 -- source lock

Freeze the dynamics, phase space, parameter provenance, chronology, symbolic
partition, primitive-orbit definition, clock, weight, repetition rule,
normalization, determinant convention, cutoff, precision, and data firewall.
Missing any of these gives `NOT_TESTABLE`.

### BF1 -- distinctness

Reject or merge a candidate if it is only:

- a coordinate conjugacy;
- a Markov recoding;
- a roof changed by a Hölder coboundary;
- a gauge change of orbit weights;
- a determinant multiplied by a known zero-free factor;
- an existing repository experiment under new notation.

Short-cycle fingerprints are only rapid de-duplication checks.  Exact roof
equivalence is decided through periodic sums/Livšic criteria where applicable.

### BF2 -- orbit readiness

Verify primitive/repeated separation, orientation, phase, multiplicity,
monodromy, reversor pairing, enumeration risk, and the exact repetition law.
This gate does not by itself give a formal A1 pass.

### BF3 -- internal structural anomaly

After the source lock, require an effect that survives three consecutive
cutoffs, precision changes, independent code where feasible, neighboring
parameters, and all prespecified parent/random controls.  Internal determinant
stability is recorded separately from formal Route-A A2.

### RA -- Route-A promotion

Apply the repository Route-A evaluator without relaxing its vocabulary.  A
candidate needs an intrinsic primitive-orbit mechanism and a frozen determinant
before any target comparison.  Extra and missing zeros, argument-principle
counts, cutoff drift, and precision drift are mandatory if a sealed comparison
is eventually authorized.

### RB -- Route-B entry

The complete Route-B audit is allowed only after `A4_ROUTE_B_READY` or explicit
project-lead authorization.  A finite real spectrum, PT symmetry, or a formal
Hamiltonian cannot open this gate.

## 3. Common cheap falsifiers

| ID | Question | Kill or downgrade action |
|---|---|---|
| F0 | Are object, clock, normalization, determinant, cutoff, precision and data split frozen? | `NOT_TESTABLE` |
| F1 | Is the object distinct up to conjugacy, recoding, coboundary, gauge and zero-free factors? | Merge with parent |
| F2 | Are primitive cycles and repetitions exact, including signs and complex phases? | Reject A1 |
| F3 | Is the construction invariant under admissible coordinates/recodings/cross-sections? | Mark as post-hoc graft |
| F4 | Does a non-autonomous object preserve ordered chronology? | Reject averaged surrogate |
| F5 | Does a simple counting-law or spectral-type theorem already exclude \(T\log T\)? | Remove from HP pool; record obstruction |
| F6 | Do root counts and values stabilize across cutoff, precision and implementation? | Do not open sealed target data |
| F7 | Does the anomaly beat constant-roof, shuffled, random-phase, same-density and neighboring-parameter controls? | Downgrade to baseline |
| F8 | Is any functional symmetry intrinsic rather than forced by multiplying a conjugate/reflected factor? | Reject A3 promotion |
| F9 | Is the Hilbert space/operator/scattering lift natural and clock-preserving? | Reject A4 promotion |

For an alleged exact roof bridge, one sealed primitive orbit with a mismatched
periodic sum after the frozen global scale is enough to kill exact cohomology.

## 4. Data firewall

Before BF3:

- allowed: Hénon geometry, orbit words, actions, multipliers, symmetries,
  finite-field counts, analytic theorems, random and neighboring controls;
- forbidden: Riemann zero ordinates, target prime weights used for parameter
  selection, post-hoc unfolding, and any validation-region refit.

If a target comparison is later authorized, use one frozen calibration region,
one validation region, and one sealed region.  Report every extra and missing
zero.  Do not select the clock, scale, phase, cutoff, or branch after viewing
the validation or sealed regions.

## 5. Chronological non-autonomous rule

For a base map \(T:X\to X\) and Hénon fibre family \(H_{a(x)}\), the admissible
object is the skew product

\[
F(x,z)=(Tx,H_{a(x)}z)
\]

or its ordered transfer cocycle

\[
\mathcal L_x^{(n)}=
\mathcal L_{T^{n-1}x}\cdots\mathcal L_{Tx}\mathcal L_x.
\]

Periodic data use the ordered monodromy along a closed base orbit.  In general

\[
\mathcal L_x^{(n)}\ne
\left(\frac1n\sum_{j=0}^{n-1}\mathcal L_{T^jx}\right)^n,
\]

so the right-hand object is forbidden as a replacement.

## 6. Exploration budget

Use 100 abstract exploration credits; one credit is at most two CPU-hours or
one quarter researcher-day, whichever is exhausted first.

- 12 credits: source-lock twelve candidates;
- 24 credits: common cheap falsifiers;
- 18 credits: at most three micro-pilots;
- 24 credits: at most two sealed replications;
- 12 credits: certified baseline/control maintenance;
- 10 credits: anomaly replication or one new generation round.

No idea receives more than one credit before BF0, three before BF2, or seven
before BF3.  The pressure/dimension baseline receives 10--15% of the search
budget unless a genuinely new analytic determinant anomaly promotes it.

## 7. Promotion decision

After the first pilots, choose exactly one of:

1. freeze a positive structural candidate and run a theorem-oriented
   refine/experiment plan;
2. write a negative paper around a sharp obstruction shared by several
   candidates;
3. if no RH-relevant candidate survives, promote the certified
   Ruelle/dimension fallback explicitly as a dynamical-systems paper, without
   HP inflation.

## 8. Round HCS-2026-08-05 decision

No candidate passed BF3 or became an RH-relevant Route-A candidate.  The round
nonetheless produced one theorem-engineering lane and two reusable
obstructions:

- C02/C02B is retained as analytic infrastructure.  Its next gate is the
  WP0 prior-art delta audit, followed conditionally by the finite-window
  endpoint lemma plus crossed/pinning-map composition in `PAPER_PLAN.md`.
- C03 and C05 are stopped under their frozen definitions.
- No formal Route-A YAML and no Route-B audit is authorized.

This is a conditional version of outcome 1 at the level of a rigorous
dynamical-systems paper, not a freeze of an RH paper.  If the C02/C02B theorem
delta collides with prior art or its endpoint/crossed-map gate fails, the project
returns to breadth-first candidate generation.

## 9. C02C addendum — 2026-08-06

WP0 found that the conjugate real SFT/uniqueness, qualitative complex pinning,
chronological composition, periodic closure and the absolute-denominator
Fredholm mechanism are prior art, while an explicit complex effective
\(H_6\) specialization remained worth testing.  C02C then proved the
full-endpoint finite-window, localization, two-coordinate gluing,
matching/Hill and complex-projective statements and passed its independent
adversarial checker.

Decision: `RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.  The next authorized gate is a separately frozen
signed, aggregate trace-compatible operator approximation theorem.  Route-A
promotion, Route B and RH target data remain closed.
