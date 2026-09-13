# Review Summary

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

This is a transparent synthesis of the candidate gate. It is not the fresh
independent source-design review required for exit.

## Problem

On the single-factor monic-centered generalized Hénon space, determine
whether pure formal trace data, without supplied Jacobian, has a sharp
quartic cutoff, and identify the exact non-quasi-finite locus one period
earlier.

## Historical proposal

The first proposal was the naked assertion

\[
P_{\mathcal H^1}(4)=3,
\]

based on the Cantat--Dujardin lower-period exceptional family and the local
period-three moment developed in Paper 12.

The candidate gate rejected this as too small and incomplete. It separated
one known curve but did not prove global period-three quasi-finiteness or
remove the Jacobian input needed by Cantat--Dujardin Theorem 4.2.

## Resolution log

| Stage | Concern | Resolution | Status |
|---:|---|---|---|
| 1 | naked cutoff lacks standalone size | require one unified three-theorem package | resolved at proposal level |
| 1 | Cantat--Dujardin Theorem 4.2 takes fixed Jacobian | prove \(C_f'(1-a)=0\) from pure fixed traces first | author proof written |
| 1 | an early elimination note said seven Jacobian candidates | correct to \(\deg C_f'=d-1\), hence three in degree four | resolved |
| 2 | \(a=1\) lower fibers not globally closed | exhaust \([1111],[31],[211],[22],[4]\) | author proof written |
| 2 | Sugiyama might be read beyond its scope | use it only on \([1111]\), where all fixed multipliers differ from \(1\) | scope locked |
| 2 | singular strata need direct proofs | write \(-64r^3\) for \([31]\) and \(A,B\) ratio for \([211]\) | author proof written |
| 2 | closure cases could escape the strata | send \(u=0,v=0,u=v,u=v=0\) to \([31],[22],[4]\) | author proof written |
| 3 | formal period two could be confused with reduced pairs | use the tensor algebra and subtract the embedded formal fixed cycle | author proof written |
| 3 | Paper 12 could remain a black-box dependency | reproduce support, slope, constant, subtraction, and local-length proofs | author proof written |
| 3 | coefficient formula vulnerable to transcription | retain two slope ledgers and one constant ledger | fresh replay pending |
| 3 | pointwise/cyclewise sums could be conflated | prove length \(60\), then divide by three | author proof written |
| 4 | quotient coordinate not explicit | compute \(L\mapsto\zeta L\), invariant \(L^3\) | author proof written |
| 4 | quasi-finite could be overstated as injective | define cutoff by finite geometric fibers; freeze non-injectivity | resolved |
| 4 | field scope overextended | state global Parts B--C over \(\mathbb C\); only Part A is characteristic-zero algebraic | scope locked |
| 4 | Paper 12 and Paper 15 could overlap in publication | Paper 15 absorbs Paper 12; parallel submission forbidden | policy locked |

## Final theorem selected

### A. Fixed-trace Jacobian enumeration

For

\[
s=1-a,\qquad q=p-sx,
\]

the formal fixed-trace characteristic polynomial satisfies

\[
C_f'(s)=0.
\]

Thus fixed traces leave at most \(d-1\) Jacobians.

### B. Exact lower failure locus

On \(\mathcal H^1_4\) over \(\mathbb C\), the exact non-quasi-finite locus
of \(\mathfrak T_{\le2}\) is

\[
E=\{a=1,\ p=(x^2-L)^2\},
\]

with trace fiber

\[
(0^{\times4},2^{\times12})
\]

and quotient \(E/\mu_3=\mathbb A^1_{L^3}\).

### C. Sharp global cutoff

\(\mathfrak T_{\le3}\) is quasi-finite on the normalized space and finite
quotient, while \(\mathfrak T_{\le2}\) is not. The separating exceptional
moment is

\[
-1296000-1572864L^3.
\]

## Independent candidate-gate record

The adversarial assessment of the strengthened package was:

- novelty: \(6.6\)--\(6.9/10\);
- standalone size: \(6.0\)--\(6.3/10\);
- proof confidence: \(9.2\)--\(9.5/10\);
- decision: **GO** for the strengthened package;
- decision for the naked cutoff: **STOP**.

This assessment emphasized that the result must remain:

- pure trace;
- quasi-finite rather than injective;
- single-factor;
- formal-period;
- over a verified field;
- explicit about known family and method prior art.

## Final synthesis record

The final synthesis scored:

- novelty: \(6.9/10\);
- standalone size: \(7.4/10\);
- proof confidence: \(8.7/10\).

The proof score is below the frozen \(9.0\) exit threshold because:

1. the integer ledger requires an independent transcription replay;
2. formal-cycle multiplicities need a fresh check;
3. Cantat--Dujardin and Sugiyama scopes must be re-opened in primary text;
4. the finite-type/quasi-finite and finite-quotient passages must be
   checked in the exact trace target.

The score reduction does not identify a counterexample, but it does block
source lock.

## Threshold ledger

| Dimension | Frozen threshold | Current synthesis | Passed? |
|---|---:|---:|---|
| novelty | \(6.5\) | \(6.9\) | yes |
| standalone size | \(6.0\) | \(7.4\) | yes |
| proof confidence | \(9.0\) | \(8.7\) | **no** |

The package remains conditional until all three pass simultaneously.

## Alternative-candidate disposition

Nine alternative directions were screened. None matched the strengthened
quartic package on the combined novelty, size, and proof thresholds.
All-degree and quintic cutoffs had major unresolved global fibers; arithmetic
periodic-point and dynatomic alternatives had very low proof confidence.

The recommendation is to pause Paper 15 if the quartic proof fails, rather
than substitute an underproved alternative.

## Novelty boundary

Already known:

- Cantat--Dujardin's exceptional curve and lower-period blindness;
- general finite trace rigidity and some finite cutoff;
- fixed-Jacobian \(a\ne1\) low-period finiteness;
- one-variable fixed-multiplier results;
- Hénon normal forms;
- residue and formal-cycle methods;
- Paper 12's local exceptional-curve calculation.

Candidate residual contribution:

- pure-trace Jacobian enumeration;
- exact global lower non-quasi-finite locus;
- global quartic quasi-finiteness through period three;
- unified sharp cutoff theorem absorbing the local Paper 12 calculation.

No absolute priority claim is made.

## Scope audit

The following are frozen:

- Part A: algebraically closed characteristic zero;
- Parts B--C: \(\mathbb C\);
- source: \(\mathcal H^1_4\), single factor;
- trace data: formal, nonreduced;
- Sugiyama: \([1111]\) only;
- Cantat--Dujardin Theorem 4.2: fixed \(a\ne1\) only;
- conclusion: quasi-finite, not injective;
- period-three moment: separator only on \(E\).

## Publication relationship

Paper 15 absorbs Paper 12's central theorem and proof. Paper 12 remains a
provenance artifact. The two may not be submitted as separate overlapping
papers.

## Final disposition

**AUTHOR STOP / CONDITIONAL GO REMAINS AT SOURCE DESIGN.**

The exact next admissible action is a newly authorized, fresh, read-only
proof-and-citation review. It must issue its own artifact and certify proof
confidence at least \(9.0\). This summary does not perform or pre-empt that
review.
