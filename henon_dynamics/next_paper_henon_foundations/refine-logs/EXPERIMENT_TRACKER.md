# Experiment tracker

Project status: **deferred planning only**. No implementation run is authorized
until the expanded G0 literature gate passes. No run below is marked complete
until its artifacts and manifest exist in `../results/`.

## Gate status

| Gate | Requirement | Status | Evidence |
|---|---|---|---|
| G0 | Hénon-specific novelty audit | HIGH-RISK / BLOCKING | Must audit Tabor 1983, Helleman 1988, Fornæss--Weickert 2000, Weickert 2004, Shudo--Ikeda 2008/2016, and exact overlap with the proposed trace theorem |
| G1 | Analytic convention check | PLANNED | Independent derivations required |
| G2 | Local classical completeness | INHERITED, TO RECHECK | R058/R059 and current local catalogue |
| G3 | Quantum trace convergence | NOT RUN | — |
| G4 | Mechanism ablations | NOT RUN | — |
| G5 | Determinant/tail theorem | NOT RUN | Stretch goal |
| G6 | No-target/Route-B firewall | ACTIVE | Protocol forbids Riemann data |

## Run ledger

| Run ID | Description | Status | Config | Artifacts | Decision |
|---|---|---|---|---|---|
| R000 | Pilot: quadrature, cutoffs, \(\hbar\), period safety | CANDIDATE HCS-C09 / BLOCKED ON G0 | TBD | TBD | May tune R001 only after promotion |
| R001 | Frozen main protocol | NOT CREATED | TBD | `R001_FROZEN_PROTOCOL.*` | Required before R050 |
| R010 | Reproduce and diagnose legacy \(a\simeq1.0056\) routine | NOT RUN | TBD | TBD | Audit only |
| R020 | Quartic Weyl numerical sanity check | NOT RUN | TBD | TBD | C1 support |
| R030 | Exact quantum-kernel convention/unitarity checks | NOT RUN | TBD | TBD | G1 |
| R040 | Orbit/action/Hessian/Maslov audit | NOT RUN | TBD | TBD | G2 |
| R050 | Main fixed-period quantum--orbit trace comparison | BLOCKED ON R001 | TBD | TBD | C3 primary |
| R051 | Higher-period extension | BLOCKED ON R050 | TBD | TBD | Optional C3 strengthening |
| R060 | Cutoff and quadrature controls | BLOCKED ON R001 | TBD | TBD | G3 |
| R070 | Mechanism ablations | BLOCKED ON R001 | TBD | TBD | G4 |
| R080 | Determinant/contour experiment | BLOCKED ON G3--G4 | TBD | TBD | G5 stretch |
| R090 | Independent implementation and reproduction | BLOCKED | TBD | TBD | Publication gate |

## Analytic obligation ledger

| ID | Obligation | Owner/check | Status |
|---|---|---|---|
| T1.1 | Verify \(C_aH_aC_a^{-1}(X,Y)=(X^2+Y-a,-X)\) | symbolic + independent hand check | CHECKED INFORMALLY |
| T1.2 | Verify reversor and fixed-point stability range | symbolic + interval check | CHECKED INFORMALLY |
| T2.1 | Derive explicit quartic Weyl constant | two independent derivations | CHECKED INFORMALLY |
| T2.2 | State theorem hypotheses/domain/remainder | spectral-analysis review | OPEN |
| T2.3 | Prove fixed affine rescaling cannot give \(T\log T\) | elementary asymptotic proof | OPEN |
| T3.1 | Derive generating function and map direction | two conventions | CHECKED INFORMALLY |
| T3.2 | Prove unitary factorization including global phase | operator check | OPEN |
| T3.3 | Audit exact overlap with Fornæss--Weickert | full-text review | OPEN |
| T3.4 | Freeze action gauge, Fourier branch, global/subprincipal phase; prove nonuniqueness statement | operator check | OPEN |
| T4.1 | Define trace-class localized chronological operator | functional-analysis check | OPEN |
| T4.2 | Prove stationary points equal certified closed paths | R059 dependency audit | OPEN |
| T4.3 | Prove signed Hessian--monodromy identity, including \(n=1,2\) special cases | algebra + intervals | OPEN |
| T4.4 | Fix Maslov convention from \(\sqrt i=e^{i\pi/4}\) | period-1/2 analytic control | OPEN |
| T4.5 | Prove explicit stationary-phase remainder | semiclassical review | OPEN |
| T4.6 | Verify source-row/target-column block orientation with a non-palindromic word | independent graph test | OPEN |
| T4.7 | Certify cutoff interior, stationary support, and cutoff-dependence theorem | microlocal + interval check | OPEN |
| T5.1 | Prove repeated-orbit instability-amplitude identity | 2D symplectic algebra | CHECKED INFORMALLY |
| T6 | Log-time or contour determinant control | optional | OPEN |

## Claim discipline log

Current permitted language:

- “The original distance-minimization routine does not certify a tangency.”
- “The positive fixed point remains elliptic at \(a=1.02\).”
- “The static quartic surrogate is expected, and will be proved, to have an
  \(E^{3/4}\) Weyl law.”
- “A natural unitary quantized Hénon map is prior work.”
- “The proposed new object is a localized trace on the certified local
  survivor.”

Current forbidden language:

- “There is no tangency anywhere near \(1.0056\).”
- “The first global tangency has been proved at \(5.69931\).”
- “The existing local survivor is the full Hénon horseshoe.”
- “The exact quantum Hénon map has a discrete Hilbert--Pólya spectrum.”
- “The trace determinant equals \(\zeta\), \(\xi\), or the Riemann zeros.”
- “The project has passed Route B.”

## Stop conditions

Stop or pivot before manuscript drafting if any occurs:

1. T4 is already available in prior literature with essentially the same
   certified/localized Hénon content.
2. No trace-class/microlocally meaningful localization can be specified
   without arbitrary boundary data controlling the result.
3. Main trace errors do not decrease under frozen semiclassical refinement.
4. Correct action/stability data do not beat the frozen ablations.
5. A claimed determinant zero lacks a fixed-contour tail bound.
6. Any parameter, phase, scale, or cutoff is selected by consulting Riemann
   zeros.

## Update template

For every completed run, add:

```text
Run ID:
UTC timestamp:
Source hash / dirty-worktree note:
Config path and SHA256:
Input artifact hashes:
Command:
Runtime / peak memory:
Primary metrics:
Control metrics:
Pass/fail against frozen gate:
Unexpected observations:
Claim update:
Artifact manifest path:
```
