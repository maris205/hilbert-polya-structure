# Novelty Assessment

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_FRESH_INDEPENDENT_REVIEW / NO_SOURCE_LOCK / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Candidate evaluated

The candidate is not merely the sentence “the quartic cutoff is three.” The
only admissible paper-sized object is the unified package:

1. pure fixed traces leave at most \(d-1\) Jacobian candidates;
2. the exact period-\(\le2\) non-quasi-finite locus in
   \(\mathcal H^1_4\) is
   \[
   E=\{a=1,\ p=(x^2-L)^2\};
   \]
3. formal traces through period three are quasi-finite globally and on the
   finite quotient, making the cutoff sharply three.

The safe title is **Low-Period Trace Fibers of Quartic Generalized Hénon
Maps**.

## Gate history

### Naked cutoff candidate

**STOP.**

A theorem consisting only of \(P_{\mathcal H^1}(4)=3\) was judged too small
as a standalone paper, even if correct. It would also obscure the main
logical issue: a pure trace theorem cannot silently feed the Jacobian into
Cantat--Dujardin Theorem 4.2.

### Strengthened three-theorem package

**CONDITIONAL GO TO SOURCE DESIGN ONLY.**

The strengthened package has a coherent theorem architecture:

\[
\text{pure fixed traces}
\to
\text{finite Jacobian enumeration}
\to
\text{exact exceptional lower fiber}
\to
\text{period-three removal}.
\]

The package is large enough to investigate as a focused theorem paper, but
it has not crossed the source-design exit gate.

## Preserved independent assessments

### Adversarial assessment

- novelty: \(6.6\)--\(6.9/10\);
- standalone size: \(6.0\)--\(6.3/10\);
- proof confidence: \(9.2\)--\(9.5/10\);
- verdict: strengthened package **GO**, naked cutoff **STOP**.

The adversarial review required:

- the fixed-algebra identity \(C_f'(s)=0\);
- at most three, not seven, quartic Jacobian candidates;
- the exact five-partition \(a=1\) analysis;
- formal rather than reduced periodic cycles;
- a strict quasi-finite/non-injective distinction;
- no scope beyond the single-factor normalized space.

### Final synthesis

- novelty: \(6.9/10\);
- standalone size: \(7.4/10\);
- proof confidence: \(8.7/10\);
- verdict: author-side source package may be written, but source-design exit
  is not authorized.

The proof score was lowered below \(9.0\) for exact-ledger transcription risk
and theorem-scope risk, not for an identified counterexample.

## Frozen thresholds

Lifecycle progression requires all three:

- novelty at least \(6.5\);
- standalone size at least \(6.0\);
- proof confidence at least \(9.0\).

The first two thresholds are currently met by the synthesis. The proof
threshold is not. A fresh reviewer must replay the proof and cite exact
source scopes before any source lock.

## Component-level novelty map

| Component | Prior-art strength | Residual contribution | Conservative novelty |
|---|---|---|---:|
| general full-spectrum finite rigidity | Cantat--Dujardin Theorem A / 3.5 | none claimed | none |
| existence of some finite period cutoff | Cantat--Dujardin Theorem 3.7 | explicit sharp quartic value, if proved | medium |
| Jacobian-\(-1\) quartic exceptional family | Cantat--Dujardin Example 4.3 | none claimed for discovery | none |
| period-one/two blindness on that family | Cantat--Dujardin Example 4.3 | exact full-fiber role inside a global classification | low--medium |
| fixed-Jacobian \(a\ne1\) period-\(\le2\) finiteness | Cantat--Dujardin Theorem 4.2 | pure-trace finite Jacobian enumeration before applying it | medium--high |
| fixed-multiplier finiteness on simple roots | Sugiyama | use only to close \([1111]\) | none as a method |
| \(C_f'(s)=0\) and at most \(d-1\) Jacobians | no direct indexed collision located | pure fixed-trace bridge removing hidden \(J\) | high within the package |
| exact lower non-quasi-finite locus | closest source exhibits only \(E\) | five-stratum global closure and exactness | medium--high |
| period-three affine moment on \(E/\mu_3\) | internal Paper 12 provenance | absorbed calculation supporting global cutoff | not new relative to Paper 12; new only as part of unified result |
| global quartic quasi-finiteness through period three | no direct indexed collision located | explicit cutoff on all of \(\mathcal H^1_4\) | medium--high |
| residue and formal-cycle machinery | classical method literature | exact Hénon bookkeeping only | none as a method |

## Why the package is now standalone

The paper narrative has three necessary layers rather than three parallel
contributions:

1. **Pure-trace bridge.** It solves the hidden-Jacobian problem and reduces
   the global quartic question to finitely many fixed-Jacobian slices.
2. **Exact lower-fiber geometry.** It proves that every lower-period
   positive-dimensional fiber is the known exceptional curve.
3. **Sharp removal.** It shows that one formal period-three invariant
   collapses the exceptional quotient coordinate to finite fibers.

Removing any layer breaks the headline:

- without Layer 1 the theorem is not pure trace;
- without Layer 2 the exceptional locus is not exact;
- without Layer 3 there is no explicit cutoff.

This dependency is why the strengthened package is focused rather than
contribution sprawl.

## Closest prior work

### Cantat--Dujardin

This is the mandatory direct neighbor. It gives general trace rigidity, an
unspecified finite cutoff, low-period finiteness away from Jacobian \(-1\)
when the Jacobian is supplied, and the exact exceptional quartic family.

The residual delta is narrow and explicit:

- derive finitely many Jacobians from pure fixed traces;
- close the entire Jacobian-\(-1\) quartic slice;
- prove the exceptional family is the exact lower non-quasi-finite locus;
- give the explicit sharp cutoff three.

### Sugiyama and Huguin

Sugiyama supplies fixed-multiplier fiber results for one-variable
polynomials; this package uses only the no-multiple-fixed-point quartic
stratum. Huguin supplies one-variable small-cycle moduli results used by
Cantat--Dujardin. Neither source states the Hénon exceptional-locus theorem
or the pure-trace quartic cutoff.

### Residue, formal-period, and orbit-sum literature

Multidimensional residues, quotient-algebra traces, dynatomic/formal cycles,
and exact Hénon orbit sums are established methods. No novelty credit is
assigned to those tools. The exact coefficients are proof content, not a
claim that the algebraic machinery is new.

## Bounded collision conclusion

A targeted primary-source search through 2026-08-17 found no indexed source
stating the combined result:

- single-factor monic-centered quartic Hénon space;
- pure traces without Jacobian input;
- exact period-\(\le2\) non-quasi-finite locus;
- global formal-trace quasi-finiteness through period three;
- sharp cutoff three.

The exact integer formula and \(P(4)=3\) queries produced no direct hit
beyond the known Cantat--Dujardin neighbor and the local Paper 12 artifact.

This is a bounded search statement. It is not an assertion of absolute
priority or nonexistence of unpublished work.

## Alternative-candidate screen

Nine alternatives were independently screened, including an all-degree
\(P=3\) theorem, a quintic cutoff, fixed-trace classifications in higher
degree, reversible quadratic-Hénon monodromy, collision divisors,
dynatomic-gonality questions, rational-periodic classifications,
conservative common-periodic uniformity, and cyclotomic effectiveness.

Every alternative failed at least one frozen gate, mainly proof confidence.
The recommendation was:

> Proceed only with the strengthened quartic package; if it fails fresh
> proof review, pause Paper 15 rather than substitute a weaker candidate.

No alternative score is theorem evidence.

## Publication relationship to Paper 12

Paper 12 contains the provenance calculation on \(E\). Paper 15 is a
unified strengthening and reproduces that proof as an internal section.
Accordingly:

- Paper 12 remains a local provenance artifact;
- Paper 15 may absorb Paper 12's theorem and calculation;
- the two central claims may not be submitted in parallel as overlapping
  papers;
- no novelty credit in Paper 15 is assigned to the already-developed
  Paper 12 \(E\)-classification or period-three ledger.

This policy is part of the source design, not a later editorial option.

## Risks

- A referee may regard \(C_f'(s)=0\) as an elegant lemma but ask whether the
  remaining partition analysis is deep enough.
- The exact period-three coefficients are vulnerable to a single sign,
  multiplicity, or trace--residue exponent error.
- A mismatch between reduced period points and formal-period cycles would
  invalidate the claimed trace morphism.
- Misusing Cantat--Dujardin without fixed Jacobian would destroy the
  pure-trace claim.
- Extending Parts B--C beyond \(\mathbb C\) without descent would exceed the
  verified sources.
- “Quasi-finite” may be misreported as “injective.”
- A current direct collision may emerge when the fresh reviewer repeats the
  search.

## Complete novelty nonclaims

No novelty or priority is claimed for:

- the exceptional family itself;
- its lower-period blindness;
- Cantat--Dujardin's general rigidity or Noetherian cutoff;
- Sugiyama's or Huguin's theorems;
- Friedland--Milnor normal forms;
- residue identities;
- formal or dynatomic cycles;
- Morton-type fixed-point identities;
- Paper 12's exceptional-curve classification or coefficient ledger;
- an all-degree cutoff;
- positive characteristic;
- compositions of Hénon maps;
- exact degree, branch locus, or injectivity of the trace map;
- any computational, experimental, or scan-based evidence.

## Conservative disposition

**AUTHOR STOP AT SOURCE DESIGN.**

The candidate remains viable because novelty and size clear their frozen
thresholds. It cannot leave source design until a fresh reviewer certifies
proof confidence at least \(9.0\) and all citation scopes.
