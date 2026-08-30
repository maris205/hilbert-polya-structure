# Idea report C249--C253

The round was screened against the C1--C248 owner registry and the Route-A
evaluator v0.2.0. The selection deliberately spans smooth, integrable,
discrete, nonsmooth, and stochastic dynamics. The source lock is
`3ff451e904f8f063e88c40ef87f4697a6586b1a5`; all ideas are NEW workspace
bookkeeping and do not assert literature priority.

* **C249 — van der Pol/Liénard.** Existing Duffing, Rayleigh-collapse, and
  other ODE packages do not close the classical Liénard trapping/uniqueness
  mechanism. The advance is a global limit-cycle theorem with an explicit
  parameter boundary, not another local phase portrait.
* **C250 — Ermakov–Pinney/isotonic.** Existing Hamiltonian owners (Euler top,
  Duffing, Toda, spherical pendulum) have no inverse-square singular oscillator.
  The quadratic invariant and exact radial period/action give a genuinely new
  integrable subtype while retaining the singular face as evidence.
* **C251 — majority rule 232.** Rule 90, Rule 184, substitutions, shuffles,
  sandpiles, and rotor-router systems are already represented. Synchronous
  majority has a different nonlinear domain-wall law: every wall block shrinks
  by two, and the only non-fixed orbit is the even-length alternating 2-cycle.
* **C252 — hysteretic relay.** Coulomb friction and impact maps are present,
  but no two-threshold relay with an exact switching-section return map and
  no-Zeno proof is present. The relay convention is frozen explicitly so the
  result is not advertised as a general Filippov selection.
* **C253 — Moran process.** Kingman coalescent, branching, queueing, CIR, and
  TCP/AIMD owners are present; a finite fixed-size reproduction process is not.
  The selection-ratio fixation formula and rational Green matrix are an exact
  stochastic theorem rather than a simulation census.

For every candidate the arithmetic origin is `none`, the determinant
convention is explicit (usually “none; no orbit/Fredholm determinant”), and
all forbidden-data flags remain false. If a proposed theorem would require a
target match, it is recorded as a ROUND2 clue and stopped at A0 instead of
being silently upgraded.
