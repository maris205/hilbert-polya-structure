# HCS-C22: time-ordered Ruelle cocycle for a two-letter Hénon skew product

**Date:** 2026-08-08
**Status:** Stage 1 design freeze; formal certification has not started
**Candidate:** HCS-C22, promoted from HCS-C01
**Parent candidates:** HCS-C01 and `henon_h6_instability_roof_v1`
**Evidence ceiling:** pilot evidence only; no Route-A verdict yet

## Outcome of the design round

This project asks a deliberately narrower question than a general
nonautonomous-Hénon or random-zeta program.  It fixes the Paper-5 convention

\[
H_a(q,p)=(1-aq^2-p,q)
\]

and studies the autonomous skew product

\[
F(\omega,z)=(\sigma\omega,H_{a_{\omega_0}}z),
\qquad
a_-=\frac{59}{10},\quad a_+=\frac{61}{10},
\]

over the full two-shift.  The fibre return attached to a word
\(w=w_0\cdots w_{n-1}\) is always the chronological product

\[
F_w=H_{a_{w_{n-1}}}\circ\cdots\circ H_{a_{w_0}}.
\]

It is never replaced by a symbol-frequency average, an averaged transition
matrix, or an unordered product.

The selected research question is:

> For the autonomous two-letter Hénon skew product at
> \(a_-=59/10\) and \(a_+=61/10\), what chronological information survives
> after joint parameter--state primitive orbits are passed to an intrinsic
> stability-weighted dynamical determinant?

The intended result is a chronology **classification**, not a claim that the
system detects a physical time arrow.  The common reversor
\(R(q,p)=(p,q)\) forces reversal-related protocols to have the same pure
instability data.  Therefore the first nontrivial comparison is between
words that are neither cyclic rotations nor reversals of one another.

## Why this form was selected

Three dynamical forms were screened.

1. A periodically forced Floquet block is useful as a finite diagnostic, but
   its block determinant collapses to the monodromy determinant.  It is not
   the primary object.
2. A substitution or genuinely aperiodic base has no ordinary periodic-orbit
   zeta on the base; periodic approximants would mix two different clocks.
   This form is rejected for C22.
3. The full-shift skew product is autonomous and retains every ordered
   schedule word as an actual base periodic orbit.  This is the selected
   form.

This is the first-theorem/operator-gate continuation of the already
registered HCS-C01 idea.  It is not a new claim that nonautonomous Hénon maps
can be chaotic; that question already has direct prior art.

## Falsifiable theorem program

The project advances only through the following large gates.

- **T1 -- common survivor:** certify one real four-rectangle survivor and
  one uniform hyperbolicity/contraction package for every
  \(a\in[59/10,61/10]\).
- **T2 -- chronology quotient:** enumerate joint parameter--state primitive
  necklaces and prove exactly which weights are invariant under cyclic
  rotation and reversal.  Exhibit a certified non-dihedral chronology
  witness or stop.
- **T3 -- collapse controls:** prove the bare and signed/global trace
  identities that are independent of protocol chronology.  These controls
  must be removed before interpreting any signal.
- **T4 -- intrinsic weighted determinant:** define the instability-weighted
  cycle expansion with a fixed repetition rule and show convergence in a
  nonzero domain.
- **T5 -- analytic operator gate:** construct a common complex pinning domain
  and a nuclear/trace-class ordered branch operator with a proved trace
  formula.  If this fails, C22 becomes a scoped obstruction paper and the
  search changes dynamical form.

No numerical Ulam matrix, finite-memory truncation, or visually stable root
is allowed to substitute for T5.

## Exact and numerical pilot signals

These observations select the next proof target; they are not final results.

- The signed-root recurrence

  \[
  (T_{\omega,\varepsilon}q)_i
  =\varepsilon_i
   \sqrt{\frac{1-q_{i-1}-q_{i+1}}{a_{\omega_i}}}
  \]

  is uniformly contractive on the inherited real sequence box with the
  candidate bound
  \(\theta=\sqrt{240/1003}<0.49\).
- A direct exact margin calculation suggests that the inherited four-box
  covering graph persists on
  \(289/50<a<99/16\), which contains both frozen parameters.  The tight
  candidate margins at the frozen endpoints are \(7/720\) and \(3/64\).
- The smallest primitive same-bigram, non-dihedral protocol pair is

  \[
  0000101,\qquad 0001001.
  \]

  For the admissible sign word \(++--+--\), a high-precision pilot gives
  instability lengths differing by approximately
  \(1.7210945\times10^{-2}\).  A rigorous interval enclosure is required.
- At the actual rational parameters, reduction modulo \(43\) gives an exact
  chronology witness: one fixed point of the first protocol has monodromy
  trace \(15\), while one fixed point of the second has trace \(18\).
  This proves that ordered full-map data need not collapse to bigram counts;
  it does not yet certify a real local survivor or a difference of aggregate
  zeta coefficients.

All pilot labels and their limitations are recorded in
[`notes/PILOT_LEDGER.md`](notes/PILOT_LEDGER.md).

## Route-A expectation

The honest current ceiling is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall status `ROUTE_A_EXPLORATORY`.  Even a rigorous internal nuclear
dynamical determinant would not by itself pass Route-A A2: no target divisor,
arithmetic normalization, or sealed target comparison has been supplied.
Route B is not authorized by this project.

## Project map

- [`RESEARCH_QUESTION.md`](RESEARCH_QUESTION.md): scope, FINER audit, and
  frozen definitions.
- [`EXPERIMENT_PLAN.md`](EXPERIMENT_PLAN.md): theorem/experiment gates,
  controls, kill rules, and reproducibility contract.
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md): Paper-5 lock, repository novelty
  boundary, and external prior art.
- [`DEVILS_ADVOCATE_CHECKPOINT1.md`](DEVILS_ADVOCATE_CHECKPOINT1.md): first
  adversarial review.
- [`notes/PILOT_LEDGER.md`](notes/PILOT_LEDGER.md): exact and numerical pilot
  evidence with explicit status labels.
- [`code/README.md`](code/README.md), [`results/README.md`](results/README.md),
  and [`paper/README.md`](paper/README.md): Stage-2 artifact contracts.

## Stop/pivot rule

The project does not spend a long round polishing finite sections.  It stops
or pivots as soon as one of the following is certified:

- no common real survivor for the frozen parameter interval;
- no non-dihedral difference after complete local orbit aggregation;
- the intrinsic instability weight is cohomologous to a finite-memory
  potential that destroys the proposed novelty;
- no common complex branch domain or no trace-compatible nuclear operator;
- the only surviving claim is already a standard consequence of an existing
  nonautonomous horseshoe theorem.

The preferred negative paper would state the exact obstruction and identify
which chronological information is necessarily lost.  It would then close
C22 rather than silently changing its determinant.
