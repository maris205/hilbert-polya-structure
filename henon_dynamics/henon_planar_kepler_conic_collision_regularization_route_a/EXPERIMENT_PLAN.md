# Experiment plan and evidence boundary

## Frozen owner

The owner is the two-degree-of-freedom Hamiltonian

\[
 H=|p|^2/2-\mu/r,\quad r=|q|,\quad q\in\mathbb R^2\setminus\{0\},\quad \mu>0.
\]

The source baseline is commit `077a098ac5811e465b69db71b5e6031a4827eb55`; the evaluator is route-a v0.2.0 with SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`; scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Claim-driven tests

| Claim | Deterministic test | Boundary |
|---|---|---|
| Invariants and Runge–Lenz identities | exact Fraction reconstruction on 10 states | finite probes regression-test the algebra; theorem carries all \(q\ne0\) |
| Conics and energy signs | exact residuals and eccentricity classification | only \(L\ne0\) is claimed for the polar equation |
| Period and radial action | 68-digit quadrature plus SymPy derivative check | \(E<0\), with \((2\pi)^{-1}\oint=(\pi)^{-1}\int_{r_-}^{r_+}\) explicitly fixed |
| Scattering | exact eccentricity identity and independent angle reconstruction | \(E>0,L\ne0\) |
| Radial collision | closed-form quadratures for all three energy signs | \(L=0\), inward branch, admissible \(r_0\) |
| Levi–Civita | rational lift and symbolic equation/constraint checks | configuration continuation only; no global symplectomorphism |
| Strobe boundary | shell dimension and resonance text | \(T=mP(E),m\ge1\) gives a continuum, so isolated count is undefined |

## Execution protocol

The producer emits a canonical JSON receipt.  The checker repeats the formulas without importing producer code; the SymPy script supplies a symbolic cross-check; replay verifies byte identity; and the hostile mutation harness repairs payload hashes before injecting semantic, unknown-key, and stale-hash mutations.  The release manifest then closes the file ledger and PDF hashes.

No training data, fitted target clock, target table, arithmetic local data, or external numerical trajectory is used.  The ledger is intentionally small and exact so that a reviewer can inspect every row.
