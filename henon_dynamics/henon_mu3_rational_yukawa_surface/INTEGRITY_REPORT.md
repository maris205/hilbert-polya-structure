# HCS-C55 integrity report

Status: **RELEASE_FROZEN against the persistent scoped code/results and
verified 47-entry full-project inventories; implementation commit
`e5661e80da6f7de53f574f97f768744095ba8ae0` is provenance-locked**.

Audit date: 2026-08-15 UTC.

## 1. Formal upstream provenance and chronology

| Object | SHA-256 |
|---|---|
| HCS-C52 certificate | \(a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94\) |
| HCS-C53 theorem package | \(e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe\) |
| HCS-C54 theorem package | \(d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4\) |
| C55 architecture report | \(21c5fcfdbc4387b141388103c896cf33a32b29cbf2c7cde09d1d04c85b7c49bd\), chronology only |
| C55 theorem design | \(24a7d07fd15399346f4d5efeea10d3ae3b92a31239b523552fc4c51599519161\), chronology only |

Only the HCS-C52--C54 rows are formal upstream provenance. The two C55
planning rows are unpackaged historical records, not theorem inputs,
replayable dependencies, or release source locks. Temporary reconnaissance
and provisional hostile-audit hashes are likewise not release provenance.
The post-code and paper hostile audits passed independently. Their working
files were temporary and are not promoted as hashed release authority.

## 2. Artifact partition

### Mathematics/documentation lane

- README.md
- RESEARCH_QUESTION.md
- THEOREM_PACKAGE.md
- DERIVATION_PACKAGE.md
- PROOF_PACKAGE.md
- METHODOLOGY_BLUEPRINT.md
- EXPERIMENT_PLAN.md
- EXPERIMENT_TRACKER.md
- IMPLEMENTATION_CHECKLIST.md
- INTEGRITY_REPORT.md

### Frozen independent lanes

- exact producer, checker, tests, certificate, and scoped manifest;
- independent hostile schema and paper-source audit;
- source-audit locators and bounded novelty screen;
- paper source.

The compiled PDF, compilation report, and final Route hash were generated
after the release-candidate tuple was inserted. The full-project manifest now
enumerates and verifies all 47 included artifacts. Its SHA-256 is reported
only outside manifest-covered artifacts, so no included file creates a
self-hash cycle.

## 3. Claim-integrity checks already enforced

- The four-dimensional object is a transverse Hilbert slice, not the full
  fixed locus.
- The Hilbert route constructs an algebraic family and does not identify
  tangent representatives with a literal linear family.
- \(H^1(T_X)\) is not computed from \(146-63\) without a vector-field proof.
- The nonconstant group-scheme action is required at ambient
  \(\operatorname{PGL}_8\) level.
- The relative cycle is the intrinsic norm graph over all \(24\) geometric
  elements.
- No relative Chow--Künneth projector is claimed.
- The twist is exactly \(\mathbf Q(1)\).
- Cayley descent uses \(D(z)=\rho z\), and the raw top standard monomial is
  reduced only after it maps to the distinct raw image.
- The four Cayley roles \(yp,y^2p,y^4p^3,y^5p^3\) remain distinct.
- Geometric irreducibility is derived from geometric smoothness.
- “Defined over \(\mathbf Q\)” is not promoted to
  “rational variety over \(\mathbf Q\).”
- BCD is a necessary comparator gate only.
- No Hodge/Yukawa match is promoted to an honest CY3 or motive.

## 4. Exact evidence and frozen provenance fields

| Field | Current value |
|---|---|
| code_commit | `e5661e80da6f7de53f574f97f768744095ba8ae0` |
| producer_payload_sha256 | `6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323` |
| certificate_sha256 | `aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f` |
| independent_check_sha256 | `e24c90fac1b222ed161eec677c06209c901f0decc335e769dc7df4ce53c68469` |
| schema_sha256 | `2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53` |
| code_results_manifest_sha256 | `7f1fa8bc6f22dd89b6b9a41ae2353129853f39430ba932f048ff295e56ba30e6` |
| hostile_audit_sha256 | null; independent read-only PASS, no packaged artifact |
| paper_pdf_sha256 | `ea75d7e0134531bd02b9ed32ae96aa8cd4416214d3913e19816922af6c30ccae` |
| paper_source_sha256 | `93495af19048605bd814af264bcf3b2d745a5fdd4f94af31c9422d3bc3782221` |
| paper_log_sha256 | `690ea4a3fd8af63384f02cf05eebadab5c2a4b9746bc7da999e54c18c59135a2` |
| paper_text_sha256 | `6eb5fb4b9bb4a23b68cadbce75c9cf16a61637031a3dba7dc3106a4cf5d32b19` |
| compilation_report_sha256 | `b38790520104f13bf8c4348bf7c9453c86ed1f3d09bfda98e024172556ec812b` |
| route_record_sha256 | `320b561d1a6fd9a23daafefc3bfdd75d5cf41d6e1eaee6c353bec6f956e7c4a2` |
| full_project_manifest_inventory | 47 verified entries; SHA-256 external-only to avoid a self-cycle |
| route_verdict | ROUTE_A_EXPLORATORY |

The top-level status promotion is status-only: deleting
`artifact_status` from the prefreeze and release-candidate payloads yields
the same 30,949-byte canonical mathematical subpayload, SHA-256
`a3da70ceaea6f0ac270cb746a78840ca63367e9b01e02835ad6020e4c76f37ec`.
The paper-source aggregate is the SHA-256 of the lexicographically ordered
`sha256sum` lines for the 17 TeX files and `paper/references.bib`, evaluated
from the project root. The aggregate excludes generated build products and
the compilation report.

## 5. Basis-integrity gate

The theorem polynomial uses \(q_0=e_0\). A known exploratory output uses
\(q_0=2e_0\). The release must demonstrate that the tangent certificate,
all tensor entries, generic cubic reduction, polynomial, derivatives, and
smoothness checks use one convention consistently. A partial basis rescaling
is a mandatory negative test.

## 6. Source-integrity gate

Every external theorem used in the geometric proof must have:

- primary or authoritative bibliographic metadata;
- an exact theorem/proposition/section locator;
- a statement no stronger than the cited result;
- a local PDF hash when a local source copy is part of the release audit.

Romagny is used specifically for smoothness of fixed points under a linearly
reductive group scheme. Rim is background for equivariant versality and is
not used to algebraize the family. Nagel/Konno support the Cayley residue,
operator, and pairing mechanisms; exact coefficients remain internal.

## 7. Hostile-gate closure

- ambient group-scheme action and ideal covariance replay: PASS;
- exact deformation and Hodge ranks: PASS;
- top-component normalization and semilinear descent: PASS;
- all \(20\) paired reductions and direct/reconstructed cubic equality: PASS;
- independent gradient quotient: PASS;
- every basis, grading, conjugation, coefficient, and overclaim mutation:
  PASS;
- scalar inventory
  \(1589=292\) central (+1296) independently derived (+1)
  chronology-only, with all \(292\) central semantic leaves rebound: PASS.

The prefreeze hostile run reproduced a concrete fail-open: after changing
the Boolean field finite_prime_matches_prove_motive from false to true and
rebinding payload/schema hashes, the then-current checker still passed.
This is evidence that a list of selected semantic paths is insufficient.
The release-candidate checker now rejects that exact rebound mutation. The
full suite passes (15/15) test methods and (13/13) named semantic gates.

## 8. Current integrity verdict

**RELEASE_FROZEN_INTEGRITY_PASS; IMPLEMENTATION_PROVENANCE_LOCKED.**

There is no identified conceptual, exact, source, paper, documentation,
inventory, or provenance blocker. The 47-entry full-project manifest is
verified, and implementation commit
`e5661e80da6f7de53f574f97f768744095ba8ae0` is backfilled without changing
the frozen theorem, paper, PDF, or scoped evidence tuple.
