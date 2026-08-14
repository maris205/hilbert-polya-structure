# Stage 3 Composition Blueprint — One Object, One Clock, One Trace

Status: source-locked composition plan  
Date: 2026-08-13  
Target layer: Route A / A3--A4  
Route B: not invoked

## Working title

**One Orbit Is Not a Trace: A Same-Object Certificate for Classical--Spectral Bridges**

## Central contribution

The paper defines a typed same-object certificate `T0--T7` and uses it to
separate five theorem families that are often conflated under the word
“trace.”  It then proves two exact limits on inference:

1. a local closed-orbit trace germ does not determine a global trace
   distribution, even when its singular coefficient is exact; and
2. the frozen Deninger and modular ledgers cannot be fused atom by atom while
   preserving their standard clocks, because every modular repeated length is
   disjoint from every rational-prime-power logarithm.

The result is a certification theorem and candidate-specific no-splicing
theorem, not a universal no-go theorem for quantization.

## Frozen claim ledger

| ID | Claim | Status | Permitted wording |
|---|---|---|---|
| `C1` | A trace bridge is a predicate of one typed record, not of a coordinatewise union of records. | `PROVED` (definition/type lemma) | “A bridge must identify one classical object, one analytic object, and the map tying them together.” |
| `C2` | If two distributions differ by a nonzero smooth compactly supported term away from an audited period, their local germs at that period agree but their global distributions differ. | `PROVED` | “One exact local orbit contribution cannot determine a full global trace.” |
| `C3` | Under a prior containing every possible nonzero singular location, equality of all nonzero singular germs leaves a difference smooth on the punctured line; fixing the zero germ leaves a globally smooth difference. | `PROVED` with support-prior qualification | Without the prior an unlisted delta singularity may be added; do not say arbitrary local germs glue. |
| `C4` | For hyperbolic `gamma in PSL(2,Z)`, `r ell_gamma != k log p` for all positive `r,k` and rational primes `p`. | `PROVED` | “No atomwise clock-preserving transfer of Selberg coefficients to the prime ledger.” |
| `C5` | The Duistermaat--Guillemin result supplies local wave-trace singular information under PDO/clean hypotheses. | `PROVED` from source | Do not call its local expansion a global orbit sum. |
| `C6` | The complete cofinite Selberg formula is an exact same-quotient spectral/geometric framework with identity, elliptic, parabolic/cusp, continuous/scattering, and hyperbolic terms. | framework `PROVED`; local convention `NOT_TESTABLE` in this stage | Use only the schematic typed identity; no complete convention was locally acquired, so do not transcribe unverified constants. |
| `C7` | ALKL supplies a cohomological/b-trace Lefschetz distribution under its smooth foliated-flow hypotheses. | `PROVED` from source | Do not identify a compact family of periodic orbits with a preserved leaf. |
| `C8` | The Anosov flat trace is exact in positive time under wavefront/hyperbolicity hypotheses; Pollicott--Ruelle resonances are not thereby a self-adjoint quantum spectrum. | `PROVED` from source | Keep flat trace, resonance trace, and Hilbert--Pólya spectrum distinct. |
| `C9` | Rigorous Gutzwiller results are smoothed semiclassical asymptotics for an `hbar`-family, with localization and remainder. | `PROVED` from source | Never promote to an exact global identity for one fixed operator. |
| `C10` | `MOD-GEO` passes same-object trace/quantization gates but fails rational-prime promotion; `DEN-WITT-Z-FIN` has the arithmetic period coordinate but lacks trace/operator coordinates. | `PROVED` / `NOT_TESTABLE` split | Never take their coordinatewise maximum. |

## Schematic exact formula policy

For the noncompact modular quotient, write only the typed identity

```text
discrete spectrum + continuous/scattering
  = identity + elliptic + parabolic/cusp + hyperbolic classes
```

and state the verified hyperbolic repeated-orbit coefficient separately:

\[
\frac{\ell_{\gamma_0}}
     {2\sinh(r\ell_{\gamma_0}/2)}
 =\frac{(\log N_{\gamma_0})N_{\gamma_0}^{-r/2}}
        {1-N_{\gamma_0}^{-r}}.
\]

Do not print the full cofinite normalization until one complete Selberg/Hejhal
version has been read.  Venkov (1978) may be cited as a modular-group primary
source, but a search-result excerpt or metadata page is not formula-level
verification.

## Section order

1. Abstract and Chinese abstract.
2. Introduction: the “one orbit is not a trace” error and the inherited two-halves obstruction.
3. Source lock, candidate records, and evidence vocabulary.
4. A trace is a typed mathematical object: analytic ledger, functional, test class, extent, operator regime, orbit geometry, equality strength.
5. Same-object certificate `T0--T7` and the no-coordinatewise-max lemma.
6. Five theorem families, each stated with hypotheses, output, and exact non-implication.
7. Smooth-ambiguity theorem for local trace data.
8. Modular/Deninger clock-support non-composability theorem.
9. Candidate gate matrix and Route-A consequences.
10. Deterministic zero-free controls and falsification cases.
11. Limitations and smallest missing theorem for each frozen object.
12. Conclusion, declarations, AI disclosure, artifact map.

## Mandatory controls

- `COMPACT-HYP-TRACE`: exact trace and natural Laplacian without rational-prime A0.
- `LOCAL-GERM-SMOOTH-SHIFT`: identical audited germ, different global trace.
- `HBAR-FAMILY`: detects fixed-operator/semiclassical substitution.
- `MOD-OMITTED-CONTINUUM`: full cofinite identity fails if the continuous/scattering ledger is silently deleted.
- `CLOCK-RESCALE`: any post-hoc rescaling creates a new candidate.
- `DEN+MOD-SPLICE`: fails T0 and, for atomwise clock preservation, fails the support theorem.

## Route decision boundary

- `DEN-WITT-Z-FIN`: retain `A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_WEAK`,
  conventional `A2_FAIL`; A3/A4 remain downstream `FAIL` with evidence
  `NOT_TESTABLE`.  Overall `ROUTE_A_EXPLORATORY`.
- `MOD-GEO`: retain exact A1--A4 benchmark status, including
  `A2_ANALYTIC_DETERMINANT`, `A3_PARTIAL_ANALYTIC_STRUCTURE`, and
  `A4_NATURAL_QUANTIZATION`; for the rational-prime target its A0 mechanism is
  refuted and the overall status remains `ROUTE_A_REJECTED`.
- Route B cannot be invoked for either object.

## Falsification and wording constraints

- If a source-defined morphism later connects the two ledgers while preserving
  clock, normalization, and coefficient provenance, the no-splicing conclusion
  must be re-evaluated for that new candidate.
- If Deninger’s frozen object is enriched with an explicit smooth/groupoid or
  cohomological trace object, this paper does not rule it out; the enriched
  object restarts the certificate.
- Smooth ambiguity is an inference obstruction, not a denial that an already
  specified operator defines its global trace.
- No Riemann-zero table, fitted scale, fitted phase, or manually inserted
  von Mangoldt coefficient is permitted in code or prose.
