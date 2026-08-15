# HCS-C57 exact experiment plan

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; execution design locked; machine
PREFREEZE_CODE_RESULTS_PASS; NOT_RELEASED.**

## 1. Objective

Produce a compact, independently replayable certificate for the implication

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0
\Longrightarrow
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q],
\]

the degree-36 attaining field \(F_D=K^{U_1}\), and the explicit generator

\[
(\delta_D,Q_D/u_0^4).
\]

The machine lane certifies finite instance data. The universal
\(U_1/U_3\) containment and the arithmetic/cohomological implications remain
written proof steps.

## 2. Experiment matrix

| ID | exact task | required output | independent replay | kill condition |
|---|---|---|---|---|
| X0 | frozen C56 import | exact cubic, eliminant, line shape, layered status | rerun C56 checker and reconstruct imported arrays | any byte/semantic mismatch |
| X1 | characteristic-zero incidence | \(H_x,Q_x\), degrees \(10/17\), \(g=H_xQ_x\), no diagonal | recompute \(J\), gcd, quotient, multiplication | missing identity or degree |
| X2 | configuration enumeration | counts \(135,72,36\), canonical labels | rebuild graph and configurations at exact good specializations | any missing/extra object |
| X3 | Weyl/subgroup/Picard | \(W,U_1,U_1^+\), core, normalizer, orbits, \(H^1\) | independent line/Picard matrices and integral SNF | wrong order, orbit, or cohomology |
| X4 | theta resolver | exact degree-36 coefficients and all-and-only binding | redo CRT bounds and stabilizer orbit | ambiguous coefficient or collision |
| X5 | delta/orientation resolver | exact \(R_\delta\), irreducibility, \(\beta^2=\delta\), stabilizers | redo factors, subset sums, and action | no fixed-field or orientation proof |
| X6 | twelve-line carrier | exact \(A_{12},B_{15}\), \(g=A_{12}B_{15}\) | division plus independent forward product | nonzero remainder or wrong roots |
| X7 | gauge and quartic matrix | gauge determinant, \(60\times31\) matrix, locked rows/columns | reconstruct from cubic and line restrictions | convention or rank mismatch |
| X8 | canonical quartic | nonzero pivot, Cramer vector, all \(36\times60\) zeros | recompute determinant norm and every restriction | any zero determinant or nonzero restriction remainder |
| X9 | divisor/quaternion | \(\operatorname{div}Q_D=\mathcal E+\mathcal G\), norm identity, cocycle match | recompute degree, line containment, and class map | residual, multiplicity, or zero class |
| X10 | fail-closed release | schema, leaf inventory, rebound tests | mutation suite and default runner | any semantic fail-open |

The \(X\)-rows are lower-level execution tasks, not a second theorem-gate
numbering. Rows X7--X8 jointly implement G6, the determinant quartic and its
rank certificate. Row X9 implements G7, the divisor, quaternion, and
nonzero-class matching. X10 implements the separate unnumbered negative-scope
and release firewall; it is not G7.

## 3. Exact formulas and conventions

### 3.1 Incidence

The checker must derive the divided differences from the imported line
back-substitution formulas. It may not accept stored \(H_x\) or \(Q_x\)
without recomputing

\[
g=H_xQ_x,\qquad
\gcd(H_x,y-x)=1.
\]

### 3.2 Resolvers

The two degree-36 coefficient arrays must be canonical and ordered
low-to-high. CRT reconstruction is valid only when the modulus exceeds twice
the proved uniform coefficient bound. Modular factors must include:

- proven-prime status;
- surviving leading coefficient;
- squarefreeness;
- full factors and multiplicities;
- exact multiplication;
- subset-sum sets.

### 3.3 Gauge

The checker must reconstruct the triangular gauge block and verify

\[
[u_0^3]F=75081586157,
\]

\[
\det(\text{gauge block})
=31778526453059635681033276764499400992765201.
\]

The locked 31-monomial order is valid only after this gate.

### 3.4 Restriction matrix

Rows use

\[
\text{row}=12\,(\text{binary degree})+(\text{carrier degree}),
\]

with binary degree \(0,\ldots,4\) and carrier degree \(0,\ldots,11\).
The normalization monomial is \(u_0^2u_1^2\). The pivot rows are

\[
0,\ldots,10,12,\ldots,20,24,\ldots,29,36,37,38,48.
\]

These conventions are semantic fields, not comments.

## 4. Written/machine interface

The certificate may state:

- the selected \(U_1\) has index 36 and \(H^1=\mathbf Z/2\);
- the selected fields and quartic identities pass;
- the resulting divisor is a norm.

The certificate may not state that enumerating natural stabilizers proves the
complete base-change classification. The written proof imports SD93/EJ10 and
uses:

\[
\begin{array}{c|c}
\mathbf Z/2&U_1,\ \text{index }36\\
(\mathbf Z/2)^2&U_3,\ \text{index }720.
\end{array}
\]

## 5. Adversarial tests

At minimum, the mutation suite must reject:

1. \(E=K\) or “\(E\) is Galois”;
2. \(F_D\ne K^{U_1}\);
3. omission of the \(U_3\) branch;
4. weakening divisibility to an unsupported field identity;
5. ordinary \(S_{27}\) sign substituted for \(E_6\) structure;
6. \(\delta=P(\theta)\) marked certified;
7. expanded quartic table marked necessary/certified;
8. wrong gauge coefficient or determinant;
9. altered monomial, row, column, or normalization order;
10. rank 30 inferred from specialization without the upper bound;
11. divisor equality inferred from vanishing without degree exhaustion;
12. quaternion unramifiedness treated as nontriviality;
13. rational point, no-point, Hasse, weak-approximation, or Brauer--Manin
    claim switched on;
14. local-Artin or stable-rationality novelty switched on;
15. a temporary digest accepted as release provenance.

Every scalar leaf and every derived/envelope field must belong to an explicit
classification and rebound inventory.

## 6. Acceptance sequence

1. producer exact run;
2. independent checker exact run;
3. unit tests;
4. exhaustive semantic rebound;
5. scoped manifest verification;
6. default runner from an external working directory;
7. before/after byte, size, mode, and nanosecond-mtime nonmutation snapshot;
8. formal-doc hostile audit;
9. only then authorize paper source;
10. independent hostile paper audit;
11. official controlled compilation and artifact audit;
12. post-compile root binding and release provenance.

Steps 1--11 pass. The producer, independent checker, 33/33 tests, 535/535
rebound cases, 28-entry scoped manifest, external-cwd replay, 29-file
nonmutation snapshot, formal source gate, hostile paper audit, and official
24-page build are complete. Step 12 remains the pre-release gate.

## 7. Current state

The official machine tuple and independent checker pass G0--G7, with G6
ending at the determinant quartic/rank certificate and G7 containing the
divisor/quaternion/class match. The separate negative-scope contract passes
with all 30 nonclaim leaves false. The certificate, schema, check report,
scoped manifest, 33/33 tests, and 535/535 rebound are project-local exact
evidence; Phase-1 and `/tmp` artifacts remain non-provenance. No C57
implementation/provenance commit exists. The 18-file paper-source digest, PDF,
log, extracted-text, and compilation-report digests are bound; the
post-compile formal-package digest, full-project manifest, archive, commits,
and release remain pending.

No later-batch topic is selected by this plan.
