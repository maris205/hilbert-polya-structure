# HCS-C50 integrity report

Status: **release candidate; PENDING_RELEASE_COMMIT and final manifest refresh**

This report separates mathematical proof, external source support, finite
validation, machine-replayed certificate scope, and PDF integrity. A PASS in
one layer is not promoted into another.

## 1. Independent mathematical red team

The independent mathematical review returned PASS on all five theorem gates:

1. the rational identities generate an order-\(12\)
   \(C_2\times S_3\) subgroup, without claiming the full automorphism group;
2. quotient genera and rational \(M_2(\mathbf Q)\)-idempotents give the
   \(K\)-isogeny \(\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2\);
3. the sign, split-prime multiplicity, and integer powers in
   \(\zeta_K^7L(C/K)H_2\) agree with the complete second logarithm;
4. the coefficient-one recurrence ideal proves characteristic-zero
   smoothness, while the \(p=181\) witness correctly refutes all-split
   smoothness; and
5. the fourth-moment weights, continuation thresholds, and
   normalized-semifinite/classical operator orders are mutually consistent.

The proof package now states explicitly that equivalent primitive
idempotents in \(M_2(\mathbf Q)\) are connected by off-diagonal matrix
units, which yield the required \(K\)-quasi-isogenies after denominators are
cleared.

## 2. Primary-source and novelty audit

The external theorem-bearing inputs were checked against primary or official
archival sources:

- Kani--Rosen, *Math. Ann.* 284 (1989), 307--327, Theorem A, for the
  idempotent/isogeny mechanism;
- Izquierdo--Ying, Theorem 6, pp. 26--28, for cyclic trigonal genus-four
  moduli context;
- Moonen, §3.4, Table 1 and Theorem 3.6, pp. 801--802, for the exhaustive
  positive-dimensional special-family list;
- Jiménez, §5.1 and Theorem 3, pp. 193--196, for the two genus-four
  reduced-\(D_3\)/reduced-\(D_6\) four-elliptic precedents;
- Caraiani--Newton, Theorem 1.1, p. 2, for modularity over
  \(\mathbf Q(\sqrt{-3})\);
- Godement--Jacquet, “Global Theory,” pp. 136--184, for the standard
  automorphic functional equation of the extracted elliptic factors;
- Deligne, Théorème 1.6, pp. 275--277, for Frobenius weights;
- SGA 2, Exposé XIV, Corollaire 4.6, for weak Lefschetz; and
- Simon, Chapter 9, for classical regularized-determinant background only.

The novelty firewall is explicit. The paper does not claim novelty for group
algebra decompositions, completely decomposable trigonal Jacobians, cyclic
cover moduli, modularity, Weil bounds, or regularized determinants. It does
not identify the full automorphism group of \(C\), place the curve in either
Jiménez row, or claim a special/CM family. The claimed increment is the
explicit \(K\)-rational Hénon-fibre decomposition, its exact integer-power
Euler resummation, and its combination with the fourth moment.

## 3. Exact algebra and smoothness replay

The typed Singular input in **PROOF_PACKAGE.md** and the paper appendix was
replayed locally with Singular 4.2.1. It returns exactly

\[
x_7,x_6,x_5,x_4,x_3,x_2,x_1,x_0,r^2+r+1.
\]

This proves that the characteristic-zero recurrence has no nonzero
projective solution. Openness is invoked only afterward to obtain a finite
bad set. Direct modular substitution independently verifies that

\[
(9,158,158,9,104,128,171,153)
\]

is a nonzero singular point for \(p=181,r=48\). The coefficient-one
normalization is used consistently in docs, paper, producer, and checker.

## 4. Producer/checker scope

The release-candidate independent checker has 16 fail-closed gates, and the
isolated mutation suite has 53 named mutations. The frozen run reports
16/16 checker gates PASS and 53/53 mutations rejected as intended.
Source-ordered chronology is independently replayed at
\(p=7,13,19,31\).

The checker independently recomputes:

- the rational automorphism identities by a separate symbolic path;
- the finite matrix-idempotent ledger;
- the exact Singular basis through its own typed script;
- 21 degree-one curve/elliptic trace controls;
- four degree-one-through-four Newton reconstructions;
- frozen fourth-moment rows, direction identities, and rational
  normalizations;
- the \(p=181\) singular-point set by reverse recurrence; and
- schema, source hashes, analytic-scope labels, Route-A enum, and operator
  thresholds.

It does **not** replace the proofs of Riemann--Hurwitz, algebraic
idempotent-to-isogeny descent, Deligne purity, weak Lefschetz,
Caraiani--Newton modularity, Godement--Jacquet theory, or complex-analytic
normal convergence. Those claims are carried by the mathematical proof and
primary sources. The four-prime extension ledger and 21-prime trace ledger
are validations, not all-prime proofs.

After promotion to `RELEASE_CANDIDATE`, the producer/checker were regenerated.
The final provenance is:

- certificate SHA-256:
  `ef77b61758ccaf59e2e24e79dc535e2216d794843ff5f16ae0ca4ded12eb9dde`;
- independent-check SHA-256:
  `c561c81e2dbacc37baaf4bed769ae635246b1dab0fa56f748666ba41f3e43fbb`;
- canonical payload digest:
  `d2d78b6992d97bada0119416171d9d091f6d04eb9bcf93d9a71427f2589aed6a`.

These are the release-candidate hashes; the earlier pre-freeze hashes are
not release provenance.

## 5. Route-A and claim-scope consistency

The root and archived Route-A YAMLs use the evaluator-compatible tuple

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

The A3 metrics separately record
**holomorphic_continuation: PROVED_RE_GT_1_5**. They do not promote this
domain theorem to a full functional equation. Route B remains unauthorized.
The ordinary Hilbert trace is never identified with the normalized
semifinite trace.

## 6. Paper/PDF integrity

The manuscript contains the complete theorem statement, proof architecture,
primary-source firewall, exact Singular transcript, bad-prime negative
control, finite-factor validation scope, Route-A audit, limitations, data
availability, ethics, CRediT contributions, funding, conflict-of-interest,
and AI-use statements.

The warning-free 15-page PDF has SHA-256
`a44b1ac7f6a987a45a1c9a5d9677d0f8b401b81e9ae56b2dd97c0782b1b68a8c`.
The final log contains no warning, overfull or underfull box, undefined
citation, or undefined reference. All fonts are embedded and subsetted, with
no Type 3 font. Title/author/subject/keywords metadata and rendered pages 1,
11, 12, and 15 were inspected. The exact build command, toolchain, source
hashes, citation audit, and visual-QA scope are recorded in
**paper/COMPILATION_REPORT.md**.

The root and archived Route-A YAMLs are byte-identical, parse to the same
object, and have common SHA-256
`e103f34d7485c88b22230a57879c12d14afd71ec1202da4b274dd1ab68af742a`.
Their implementation commit remains intentionally pending.

## 7. Remaining release operations

- [x] Freeze the final warning-free PDF and compilation report.
- [x] Create and compare the byte-identical archived Route-A YAML.
- [x] Promote the code/results artifact status and regenerate certificate
  and independent-check hashes.
- [ ] Refresh the expanded manifest after all documentation is stable.
- [ ] Backfill the implementation commit in both Route-A YAMLs and replace
  PENDING_RELEASE_COMMIT.

No commit or push is performed by this documentation lane.
