# HCS-C02C frozen finite-window protocol

Freeze date: 2026-08-06  
Protocol version: `HCS_C02C_V1`

## 1. Question

Can the proved C02B complex signed-root polydisks be converted into an
effective finite-window pinning certificate that preserves the genuine
second-order Hénon chronology and exactly recovers the periodic matching
Jacobian and monodromy denominator?

The experiment is a regression/adversarial audit of analytic derivations.  It
is not evidence for a theorem by enumeration.

## 2. Frozen mathematical object

\[
H_6(q,p)=(1-6q^2-p,q),
\qquad
q_{i+1}=1-6q_i^2-q_{i-1}.
\]

Endpoint disks:

\[
D_\sigma=\overline D\left(\sigma\frac{23}{48},\frac7{48}\right).
\]

For an extended word \(\varepsilon_0,\ldots,\varepsilon_{N+1}\), every
internal position must satisfy

\[
\neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1).
\]

The principal square-root branch is fixed.  All chronological neighbor
occurrences are retained.

## 3. Frozen analytic claims

The producer must audit, without weakening them after seeing output:

1. full endpoint disks, with no post-hoc shrink;
2. unique finite-window fixed points;
3. crossed identity
   \(H_6^N(Q_1,u)=(v,Q_N)\);
4. one-sided derivative bounds
   \[
   |Q_{i,u}|\le\beta\kappa^{i-1},\qquad
   |Q_{i,v}|\le\beta\kappa^{N-i},
   \]
   where
   \(\kappa=2/\sqrt{17}\) and
   \(\beta=1/(\sqrt{17}-2)\);
5. exact two-coordinate gluing;
6. continuant/monodromy formulas and
   \[
   \det DF_N=-\frac{\det(I-M_N)}{\det L_N}
   =\frac{\det C_N}{\det L_N};
   \]
7. the exact complex-base projective child disks and the composed endpoint
   sensitivity bounds in `../DERIVATION_PACKAGE.md`.

## 4. Frozen enumeration and probes

### Open windows

- Exhaust all locally admissible extended sign words for
  \(1\le N\le8\) at center endpoints.
- Require exact complete case-ID sets, not prefix agreement.
- Recheck every word for \(N=1,2,3\) at the four endpoint-angle pairs
  \[
  (0,0),\quad(\pi/2,-\pi/2),\quad(\pi,\pi/2),
  \quad(3\pi/2,\pi/4).
  \]
- The expected admissible counts at \(N=1,2,3\) are `6, 9, 15`.

### Cyclic windows

- Exhaust all cyclically admissible sign words for \(1\le N\le8\).
- Treat words rather than rotation classes; record minimal symbolic period
  separately.
- Period one must retain two self-neighbor incidences.
- Period two must use cyclic off-diagonal multiplicity two.
- Projective composition still applies one map per Hénon time step.

### Frozen gluing control

- Extended word: `++--++--` (six internal coordinates).
- Split after the third internal coordinate.
- Endpoints:
  \[
  u=c+i\rho,qquad
  v=-c+\rho e^{i\pi/3}.
  \]
- Direct union solving and two-coordinate interface solving must agree.
- Replacing the consecutive interface pair by its scalar average is an
  `EXPECTED_FAIL` control and must leave a nonzero recurrence residual.
- Reversing the monodromy product is a second `EXPECTED_FAIL` control.

### Projective adversarial points

For both \(\varepsilon=\pm1\), include:

1. \((q,m)=(\varepsilon/3,-\varepsilon R)\), whose image is
   \(-\varepsilon224/773\);
2. \((q,m)=(5\varepsilon/8,\varepsilon R)\), whose image is
   \(-\varepsilon224/1803\);
3. \((q,m)=(\varepsilon c-i\rho,-iR)\), which lies on the exact child circle.

## 5. Numerical conventions

- Producer solver: complex fixed-point iteration.
- Independent solver: complex Newton iteration on the orbit residual; it may
  not import the producer.
- Iteration tolerance: `1e-13` for fixed-point increments.
- Required displayed residual tolerance: `5e-11`.
- Maximum iterations: `10000` for nested fixed-point routines and `100` for
  independent Newton routines.
- Exact constants and sign/count assertions use integer or rational
  arithmetic.  Floating computations are regression checks only.

### Conditioning erratum recorded after the first full run

The complete frozen length-eight run exposed expected hyperbolic conditioning:
binary64 local residuals near \(10^{-13}\) can grow under direct forward
iteration, and subtracting large Hill/monodromy determinants loses absolute
digits.  The producer therefore retains those raw binary64 discrepancies and
recomputes the *same frozen cases* at 100 decimal digits for the global crossed
and determinant assertions.  This does not change the map, domains, word set,
chronology, formulas, or `5e-11` threshold.  The independent checker uses a
Newton residual route and must explicitly revisit the worst conditioned cases.

## 6. Required artifacts

The producer writes only to `results/c02c_finite_window/`:

- `certificate.json`;
- `open_windows.csv`;
- `cyclic_matching.csv`;
- `gluing_controls.csv`;
- `RESULTS.md`.

The checker writes `independent_check.json` in the same directory.

## 7. Tamper and truncation rule

The independent checker must compare exact row counts and complete case-ID
sets.  It must run in-memory negative controls showing that a truncated open
ledger, a truncated cyclic ledger, and a modified projective constant are all
rejected.

## 8. Stop rules

Stop and record a counterexample if any of the following occurs:

- a legal endpoint leaves its frozen coordinate disk;
- the direct and glued union disagree above tolerance;
- a chronological product passes only after reversal or averaging;
- the matching/Hill determinant identity fails;
- the complex projective disks touch a pole, overlap, or leave the parent
  disk;
- the checker accepts a truncated/tampered ledger.

Do not rescue a failed claim by shrinking domains, changing norms, changing
chronology, or dropping signs after the run.

## 9. Route-A firewall

For the finite certificate, freeze unit discrete time and the signed formal
flat-trace denominator \(\det(I-DH_6^n)\).  The absolute denominator is a
separate orientation-twisted object.

No operator, infinite determinant, normalization to \(\xi\), arithmetic
clock, or sealed zero test exists at this stage.  Therefore C02C cannot receive
an A2 verdict even if every certificate passes.
