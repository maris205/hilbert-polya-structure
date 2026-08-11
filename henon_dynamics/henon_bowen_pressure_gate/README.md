# HCS-C31: certified Bowen-pressure gate for the H6 horseshoe

## Outcome

This round takes the most persistent positive zero from the earlier
instability-roof cycle sections and asks a larger structural question: is it
an unexplained arithmetic spectral signal, or the ordinary pressure boundary
of the underlying hyperbolic dynamics?

The intrinsic infinite-system quantity is now certified.  On the exact
four-state survivor of

\[
H_6(q,p)=(1-6q^2-p,q),
\]

the adapted unstable roof

\[
\tau_{\mathrm{ad}}
=\log\left|-12q-\frac{123}{112}\mu^u\right|
\]

has a unique Bowen-pressure root \(h_*\), and the complete length-13 cylinder
certificate proves

\[
\boxed{0.277980<h_*<0.277987.}
\]

The earlier period-20 finite-section value
\(0.277982981676189\ldots\) lies strictly inside this interval.  It is used
only for the final comparison, not in the interval or Collatz proof.

The certified root \(h_*\) is a genuine geometric invariant: it is the
suspension pressure boundary and the unstable-slice Hausdorff dimension of
this local H\'enon basic set.  The old finite-section value is consistent with
that invariant to the certified resolution; no equality or convergence of
the old sections is claimed.  Area preservation makes the stable root equal
to the unstable root, so

\[
0.555960<\dim_H\Lambda_*<0.555974.
\]

This is a positive theorem about the dynamics and a negative result for the
proposed arithmetic interpretation.  It supplies no prime law, completed
Riemann determinant, functional equation, critical-line symmetry, or
self-adjoint Hilbert--P\'olya operator.

## The large-door theorem chain

1. The R058/R059 rational rectangles and signed square-root contraction give
   a complete symbolic conjugacy with the frozen four-state shift.
2. Strict realized-coordinate bounds place the whole survivor inside the
   isolating neighborhood.  Thus it is compact, mixing, locally maximal, and
   uniformly hyperbolic.
3. A self-consistent invariant-slope inequality sharpens the adapted
   expansion to

   \[
   J^u_{\mathrm{ad}}
   \ge \frac{\sqrt{17}+\sqrt{13}}2.
   \]

4. The adapted and Euclidean unstable roofs differ by the explicit bounded
   H\"older coboundary

   \[
   \tau_E^u
   =\tau_{\mathrm{ad}}+b\circ H_6-b.
   \]

   They therefore have the same pressure and the same periodic sums.
5. All 1,156 admissible length-13 words are retained as chronological edges
   of a 714-vertex higher-block graph.  Every bi-infinite extension of each
   cylinder is enclosed by outward rational interval arithmetic.
6. Exact rational Collatz--Wielandt inequalities put the lower pressure at
   \(s=0.277980\) above zero and the upper pressure at \(s=0.277987\) below
   zero.  Positivity of the roof gives uniqueness.

No chronological cocycle is replaced by an averaged transition matrix, and
no periodic-orbit cutoff is used in the pressure proof.

## Certificate summary

| Item | Certified value |
|---|---:|
| state-window length | 13 |
| higher-block vertices | 714 |
| chronological edges | 1,156 |
| rational outward grid | \(10^{-50}\) |
| lower Collatz margin | \(8.52903537\times10^{-8}\) |
| upper Collatz margin | \(1.69312437\times10^{-6}\) |
| checker gates | 6/6 |
| regression/mutation tests | 30/30 |

Binary floating point is used only to propose positive Perron vectors.  The
released checker independently reconstructs every cylinder and verifies the
final square-root, logarithm, exponential, and Collatz inequalities with
integer and rational arithmetic.

## Route-A decision

For the frozen claim that this positive zero supplies a Riemann/Hilbert--P\'olya
signal, the strict evaluation is

```text
(A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FORMAL_HINT)

overall: ROUTE_A_REJECTED
```

The pressure enclosure itself is `NUMERICALLY_CERTIFIED`, and the analytic
implications from cylinder containment, pressure monotonicity, and the local
dimension theorems are `PROVED`.  Those statuses do not promote the object to
a Route-A determinant match.

## Reproduction

From any working directory, run

```bash
/absolute/path/to/henon_bowen_pressure_gate/code/run_c31.sh
```

The default runner first verifies the frozen hash manifest, regenerates the
certificate and checker report in a temporary directory, runs the mutation
suite, compares the regenerated artifacts byte for byte, and verifies the
manifest again.  It never refreshes released hashes unless
`--refresh-manifest` is passed explicitly.

## Project map

- `RESEARCH_QUESTION.md` -- selected question and falsification rule;
- `METHODOLOGY_BLUEPRINT.md` -- interval and pressure design;
- `DEVILS_ADVOCATE.md` -- adversarial checkpoint;
- `THEOREM_PACKAGE.md` -- theorem statements and status boundaries;
- `DERIVATION_PACKAGE.md` -- detailed proofs;
- `SOURCE_AUDIT.md` -- local and literature source lock;
- `route_a_evaluation.yaml` -- strict Route-A record;
- `code/` -- producer, independent checker, tests, runner, and manifest;
- `results/` -- complete cylinder certificate and validation reports;
- `paper/` -- LaTeX manuscript and compiled PDF.

## Next genuinely different door

Extending only the same finite-cycle cutoff near this numerical location
would not open a new arithmetic door; it would first require a separate
convergence theorem and would still be testing a certified geometric
benchmark.  A reopening must add a canonical arithmetic fibre or twist over
this proven hyperbolic base while preserving chronology and the intrinsic
instability roof.  It must then produce a new trace or divisor law, not
another version of the same pressure root.
