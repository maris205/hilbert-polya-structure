# Stage 6 Composition Blueprint — The Exact Determinant Owner

Status: source-locked manuscript plan  
Date: 2026-08-13  
Paper number: 6, the fifth and final project of the current batch

## Working title

**Which Operator Owns the Zeta? Koopman and Frobenius Ledgers of an Arithmetic
Suspension**

Alternative subtitle: **A Same-Parent Lefschetz Positive Control and a
Single-Operator Route-B Obstruction**

## Central contribution

The paper completes the finite-field branch opened in Paper 4 and tested
operator-theoretically in Paper 5.  It proves that

\[
 \text{closed-point orbit determinant}
 =\text{graded Frobenius cohomology determinant}
\]

is a genuine same-arithmetic-parent identity, while the natural self-adjoint
Koopman generator is a different operator with essential spectrum
\(\mathbb R\).  The result resolves the apparent temptation to combine
self-adjointness from one ledger and determinant exactness from another.

This is not a universal obstruction to cohomological quantization.  It is an
exact ownership theorem for the frozen \(\mathbb P^1/\mathbb F_2\) suspension
and a reusable Route-B type check.

## Frozen claim ledger

| ID | Claim | Status | Wording boundary |
|---|---|---|---|
| `C1` | every positive degree occurs among closed points of \(\mathbb P^1/\mathbb F_2\) | `PROVED` | use the Mobius lower bound, not a finite table |
| `C2` | cycle, point-count and cohomological graded traces all equal \(1+2^n\) | `PROVED` | keep Deligne Frobenius convention explicit |
| `C3` | native orbit zeta equals the graded Frobenius determinant \(1/((1-t)(1-2t))\) | `PROVED` | call it a cohomological determinant, not a Koopman determinant |
| `C4` | the weighted Koopman generator is self-adjoint on the explicit graph domain | `PROVED` | arbitrary positive weights are unitarily equivalent |
| `C5` | Koopman point spectrum is \((2\pi/\log2)\mathbb Q\), each eigenvalue has infinite multiplicity | `PROVED` | distinguish point spectrum from full spectrum |
| `C6` | full and essential Koopman spectra equal \(\mathbb R\) | `PROVED` | note pure-point spectral measures and continuous-spectrum accumulation points can coexist |
| `C7` | resolvent is noncompact and heat operator is not trace class | `PROVED` | ordinary heat-zeta determinant route only; no universal renormalization no-go |
| `C8` | Koopman and Frobenius are not unitarily equivalent; their direct sum retains essential spectrum | `PROVED` | frozen operators/direct-sum repair only |
| `C9` | substituting \(t=2^{-s}\) lifts two factors to pole lattices on real parts 0 and 1 | `PROVED` | preimage lattice is not a new operator spectrum |
| `C10` | Route B can combine B2 and B4 only after an operator-level bridge | `PROVED` as certificate/type consequence | common arithmetic parent is stronger than unrelated splicing but still insufficient |

## Section order

1. English abstract and keywords.
2. Chinese abstract and keywords.
3. Introduction: exact scalar identities and the operator-ownership problem.
4. Source lock and three ledgers: orbit, Koopman, cohomology.
5. Arithmetic parent and one primitive circle per closed point.
6. Deligne trace and the exact graded determinant.
7. Complete Koopman generator and weight invariance.
8. Exact point/full/essential spectral-type theorem.
9. Which operator owns the determinant?
10. Lift from \(t\) to \(s\) and the vertical pole lattices.
11. Same-object T0--T7 and Route-A/limited-Route-B matrices.
12. Deterministic controls and artifact integrity.
13. Limitations and next smallest theorem.
14. Conclusion, declarations, AI disclosure and artifact map.

## Main display architecture

### Figure 1 — common parent, different analytic owners

Use native TikZ, not a generated bitmap:

```text
                  (P1/F2, Frobenius)
                    /             \
        closed points/cycles      etale cohomology
                 |                      |
          suspension circles       Frobenius Phi
                 |                      |
         Koopman generator A_K     exact graded det
                 |
       self-adjoint but ess spec R
```

Show the exact orbit/cohomology equality with a solid horizontal bridge and the
absent \(A_K\)-determinant identification with a labeled dashed arrow.

### Table 1 — operator ownership

Columns:

```text
ledger | space | operator/action | domain/topology | spectrum | trace | determinant
```

Rows: primitive orbit product, Koopman generator, etale Frobenius.

### Table 2 — Route decisions

Separate native Hasse--Weil, Riemann target and limited Route-B rows.  Never
write a coordinatewise maximum.

### Figure 2 — finite cutoff multiplicity growth

Optional PGFPlots figure from `results/koopman_multiplicity_controls.csv`.
Caption must say the plot is a regression illustration, while the theorem is
cutoff-free.

## Mandatory proof order

1. Prove all degrees exist before using infinitely many multiples of a
   denominator.
2. Derive the cohomological determinant before discussing operator ownership.
3. State the exact Koopman domain before self-adjointness.
4. Prove point spectrum, then closure/full spectrum, then essential spectrum.
5. Use the infinite-dimensional zero eigenspace for the shortest compactness
   and heat-trace proof.
6. Only after both operators are fully typed, prove the no-merger statement.

## Language safeguards

Required phrases:

- “same arithmetic parent”;
- “different analytic operator owners”;
- “graded finite-dimensional cohomological determinant”;
- “limited early Route-B audit”;
- “pure-point spectral measures with dense point spectrum”;
- “set-theoretic continuous spectrum at non-eigenvalue accumulation points”;
- “frozen-object theorem, not a universal no-go.”

Forbidden phrases:

- “the Koopman determinant equals the Hasse--Weil zeta”;
- “Frobenius is the Hilbert--Polya Hamiltonian”;
- “unitary therefore discrete”;
- “the two factors generate an infinite quantum spectrum”;
- “finite-field RH proves or models Riemann RH”;
- “no cohomological Hilbert--Polya operator can exist.”

## Citation policy

- Cite Deligne directly at the trace and determinant equations.
- Cite Koopman for the invariant-measure unitary representation.
- Cite Stone/Teschl at the self-adjoint generator and orthogonal-sum theorem.
- Cite the Stage-4 paper/result internally for the suspension homeomorphism,
  but restate enough definitions for this manuscript to stand alone.
- Source exact \(\mathbb P^1\) cohomology either through Deligne/Milne or derive
  its two trace eigenvalues explicitly from the point-count identity.
- Do not cite search-result pages.

## Deterministic artifact statement

The paper must report:

- 10/10 unit tests;
- exact cycle/point/cohomology matches through degree/power 24;
- output manifest SHA after final reproduction;
- no Riemann zeros, optimizer, random seeds, network data or floating root
  finder;
- finite tables are regression controls, not evidence for infinite claims.

## Route wording

Native finite-field calibration:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_CONTROLLED_CONTINUATION,
 A4_UNITARY_OR_SCATTERING_CANDIDATE)
overall: ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
```

Riemann target:

```text
A0_FAIL; A1 native-only/wrong support; A2_FAIL; A3_FAIL;
A4_UNITARY_OR_SCATTERING_CANDIDATE but irrelevant to failed A0--A3
overall: ROUTE_A_REJECTED
```

Limited Koopman Route B:

```text
(B1_COMPLETE_OPERATOR_DEFINITION,
 B2_SELF_ADJOINT,
 B3_FAIL,
 B4_FAIL,
 B5_FAIL)
overall: ROUTE_B_REJECTED
hilbert_polya_claim_allowed: false
```

## Release gates

- all proof/source claims mapped;
- bilingual abstracts agree on scope;
- no unresolved reference or citation;
- no serious overfull box or missing glyph;
- all tables legible at 100% PDF zoom;
- Route tuples use only exact roadmap enumerations;
- source-manifest and result-manifest hashes regenerated;
- independent mathematical and citation review completed;
- PDF visually inspected at title, theorem, figure, route table and bibliography pages.
