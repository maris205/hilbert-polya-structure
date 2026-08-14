# HCS-C52 integrity report

Status: **PASS; implementation provenance backfilled**

Implementation commit: `208feef86365cd92ace8dad02904acff6623eeec`.

## Mathematical red team

- The complete projective monomial source stabilizer was independently
  reconstructed from all \(8!\) support permutations and identified as
  \(\operatorname{Dih}(C_{12})\) of order \(24\).
- The raw Reynolds projector \(e_G\) is not assigned middle rank.  The
  rank-\(10/158\) statement applies only to
  \(\pi_{\mathrm{core}}=\pi_5e_G\) and
  \(\pi_{\mathrm{lev}}=\pi_5-\pi_5e_G\).
- The six ambient Lefschetz correspondences, the middle projector,
  Reynolds averaging, transposition, and mutual orthogonality were checked
  as Chow-correspondence identities.
- The Cayley action includes the mandatory
  \(\det(M_g)/\det(A_g)\) residue multiplier.  A non-vacuous scalar lift
  \(M\mapsto2M\) verifies cancellation of exponents \(-3\) and \(+3\);
  deletion and inversion are rejected.
- The exact \(H^{3,2}\) character has trivial multiplicity \(4\), while
  \(H^{4,1}\) is one trivial copy.  The resulting graph-algebra lower bound
  is exactly rank \(10\).
- The no-go is restricted to the full rational graph algebra
  \(\mathbf Q[G_{\mathrm{mon}}]\).  The full Chow correspondence ring,
  coniveau, abelian realization, strict local compatibility, automorphy,
  and functional equations remain open.

## Independent machine audit

The release-candidate artifacts record:

- 16/16 independent semantic gates passing;
- 44/44 isolated mutation and transaction tests passing;
- 82 Jacobian relation rows of exact rank 81 in a 164-dimensional ambient
  space, giving quotient dimension 83;
- 1,968 relation-image tests and 94,464 ambient representation-law tests;
- producer arithmetic by custom exact \(\mathbf Q(\rho)\) pairs and dense
  RREF;
- checker arithmetic by an independent SymPy `DomainMatrix` number field;
- fail-closed recursive schema/type checks and isolated named mutation
  gates;
- rollback after injected failures at promotion moves two and three.

Frozen hashes:

- payload:
  `78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1`;
- certificate:
  `a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94`;
- independent check:
  `a4a0180a3e40a8eb82159fcea474221dafabddd728ebf1c2112435b21ad5c6f1`.

The certificate status is `RELEASE_CANDIDATE`.  Machine replay certifies
B0--B2 only; C53 Frobenius and incidence gates remain absent by design.

## Claim and source integrity

All bibliography entries were checked against primary or official records,
and every manuscript citation resolves.  High-impact source-dependent
claims were traced to the locators recorded in `SOURCE_AUDIT.md`.  In
particular, the Fano fivefold Hodge ledger, ordinary Chow--Künneth formula,
graph-character formalism, and arithmetic-descent caveats match their
sources.

The novelty statement is explicitly search-bounded and non-exhaustive.
No claim of global priority, full automorphism classification, actual
Calabi--Yau realization, coniveau, abelian type, or all-correspondence
obstruction is made.

## Paper/PDF audit

The final compilation is frozen in `paper/COMPILATION_REPORT.md`:

- clean `latexmk` build, exit status zero;
- 10 A4 pages and 365781 bytes;
- PDF SHA-256
  `eb999119a0e2291bbd027fb7c70a69297d3421962b1353b83ddeaa9b5b28179d`;
- zero undefined citations/references, package warnings, overfull or
  underfull boxes, and rerun requests in the final logs;
- all fonts embedded and subsetted, no Type 3 fonts;
- successful text extraction and visual inspection of pages 1, 6, and 10.

## Route-A and registry audit

- The root and archived Route-A YAML records are byte-identical and
  schema-parseable.
- The tuple is
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
  A3_PARTIAL_ANALYTIC_STRUCTURE, A4_NATURAL_QUANTIZATION)` with overall
  `ROUTE_A_EXPLORATORY`.
- A2 and A4 are inherited unchanged; the new result improves algebraic A3
  packet control.
- HEN-O95 is uniquely scoped to the rank-two obstruction in
  \(\mathbf Q[G_{\mathrm{mon}}]\).
- Candidate and obstruction registries preserve the C/P namespace policy.

## Release closure

The full-project manifest includes theorem/proof packages, source audit,
paper sources and PDF, compilation and integrity reports, both Route-A
copies, exact code, results, and tests.  The default runner must regenerate
the certificate and independent check byte-for-byte, pass all semantic and
mutation gates, and verify the complete manifest without changing stable
files.

The full implementation SHA is backfilled into this report, the project
README, and both byte-identical Route-A records.  The user-owned
`henon_dynamics/codex_prompt.md` is excluded from every commit.
