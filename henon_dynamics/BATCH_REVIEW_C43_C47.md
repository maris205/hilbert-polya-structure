# Pressure-lane Batch Review: HCS-P43 through HCS-P47

The five frozen bundles retain their original unqualified `HCS-C43` through
`HCS-C47` strings internally for byte-level provenance.  After integration
with the independently frozen full-kernel cubic lane, their unique registry
aliases are **HCS-P43** through **HCS-P47**; unqualified legacy IDs must not
be used to identify these projects.

## Completed papers

1. **[P43 — entropy--von Mangoldt mass bridge](henon_entropy_von_mangoldt_bridge/README.md).**  The exact-period marked
   census of the certified four-state H6 survivor is asymptotic to
   \(\vartheta(\varphi^n)\), while primitive cycles are asymptotic to
   \((\log\varphi)\pi(\varphi^n)\).
2. **[P44 — raw-instability amplitude and overconvergence](henon_instability_amplitude_overconvergence/README.md).**  One primitive
   instability Euler factor has the correct all-repetition logarithmic atom,
   but the complete raw zeta converges absolutely on the critical line and
   therefore cannot be the all-prime Euler product.
3. **[P45 — pressure-normalized prime-orbit bridge](henon_pressure_normalized_prime_orbit_bridge/README.md).**  The canonical pressure
   root turns the same positive non-lattice roof into an entropy-one
   suspension with the source-backed law \(\Pi(T)\sim e^T/T\), while leaving
   its positive real orbit labels arithmetically unclassified.
4. **[P46 — integral monodromy units](henon_integral_monodromy_units/README.md).**  After the canonical integral scaling,
   every period-\(n\) fixed algebra is finite free of rank \(2^n\), every
   return trace is an algebraic integer, and every multiplier is an algebraic
   unit.
5. **[P47 — repetition-compatible scalar classification](henon_repetition_label_classification/README.md).**  Every functorial
   rational label obeying \(R(X^r)=R(X)^r\) is \(X^k\); hence no rational
   scalar repair turns the P46 units into rational primes, whereas the
   nonrational pressure power \(X^{h_*}\) survives.

## Decision chain

```text
intrinsic entropy mass agrees with prime mass (P43)
  -> test the exact local Euler amplitude (P44)
  -> raw time has the wrong global convergence class (P44)
  -> normalize the same roof by its pressure root (P45)
  -> prime-orbit density and repetition syntax now agree (P45)
  -> audit the arithmetic type of the underlying multipliers (P46)
  -> classify every rational repetition-compatible scalar repair (P47)
  -> retain only the nonrational pressure label or a nonlocal trace bridge
```

## Current strongest Route-A state

The strongest coordinatewise result is P45:

```text
(A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

Its overall verdict remains `ROUTE_A_EXPLORATORY`, not a Route-A pass.  P46
and P47 strengthen the negative arithmetic boundary but must not be combined
coordinatewise with P45 into a stronger certificate.  Route B remains
unauthorized because this batch constructs no self-adjoint operator, domain,
trace formula, or completed \(\xi\)-determinant.

## Strongest positive result

P45 is the main survivor.  On the certified mixing H6 subshift, pressure
normalization of the positive H\"older non-lattice instability roof gives an
entropy-one suspension and therefore a genuine dynamical prime-orbit theorem

\[
\Pi(T)\sim \frac{e^T}{T}.
\]

The corresponding labels \(P_\gamma=|\Lambda_\gamma|^{h_*}\) preserve every
Euler repetition exactly.  This is a dynamical theorem, not an arithmetic
orbit--prime correspondence.

## Strongest obstruction

P46 and P47 give the strongest combined no-go.  Every raw H6 multiplier is
an algebraic unit, and every functorial rational scalar label that preserves
all repetitions is a monomial.  Such a label remains a unit and cannot be a
rational prime.  Independently, P44 shows that even the locally correct raw
instability amplitude has the wrong critical-line convergence class.

## Reusable structure

The most reusable positive compiler is:

```text
positive non-lattice Hölder roof
  -> solve P(-h_* tau)=0
  -> normalize tau_hat=h_* tau
  -> entropy one
  -> prime-orbit law e^T/T
  -> exact repetition labels exp(period)
```

The most reusable hostile compiler is the power-map divisor test: rational
labels compatible with all repetitions are forced to be monomials before any
finite orbit fitting is allowed.

## ROUND2_CLUE

The pressure power \(|\Lambda|^{h_*}\) is now the unique scalar large-road
survivor isolated by the batch.  Its status may depend on transcendence or
algebraic-independence information about the pressure root and H6 units.  If
that scalar lane fails, the next legitimate object is nonlocal: an orbit
packet, prime ideal, cyclic resultant, or distributional/scattering trace
whose arithmetic information is collective rather than one rational number
per primitive orbit.

## Current largest blocker

No source-native theorem identifies the real labels
\(|\Lambda_\gamma|^{h_*}\) with rational primes, prime ideals, or an
arithmetic Euler product.  No critical-line continuation, Riemann functional
equation, or Hilbert--P\'olya operator has been obtained.  More rational
functions of one multiplier are now scope-exhausted by P47.

## Batch certification

All five project-local reproduction scripts pass (20/20 unit tests), all
five certificates rebuild deterministically, and all five papers compile to
nonempty three-page PDFs.  Each project contains the required `README.md`,
`paper/`, `code/`, `experiments/`, `results/`, and `notes/` artifacts.

## Next batch: three highest-value directions

1. **Pressure-label arithmetic.**  Determine rigorous algebraic or
   transcendental consequences for \(h_*\) and
   \(|\Lambda_\gamma|^{h_*}\), with Gelfond--Schneider/Baker-type hypotheses
   stated explicitly and adversarially tested.
2. **Nonlocal packet arithmetic.**  Test whether cyclic resultants, prime
   ideals, or Galois packets can preserve repetition collectively without
   contradicting the P46 unit theorem or the P47 scalar classification.
3. **Distributional trace bridge.**  Seek a transfer/scattering trace whose
   prime information is encoded in a distribution or determinant rather
   than by termwise rational-prime labels; require source-native continuation
   and operator-domain evidence before Route-B promotion.

## Recommendation

`CONTINUE` — with a scoped pivot away from rational scalar repairs and toward
the pressure-power arithmetic gate first.  The batch has a real positive
dynamical bridge and a sharp negative scalar classification, so the route is
narrower but not exhausted.
