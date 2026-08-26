# Paper 15 — Wieferich--Ulm classification

## Current status

- Deliverable: **Stage-2.5 integrity-PASS full-paper research draft**.
- Title: *Wieferich--Ulm Signatures and the Classification of Compact Arithmetic Packet Bases*.
- Retained PDF: [`paper/paper.pdf`](paper/paper.pdf).
- The mandatory pre-review integrity gate passed with zero open issues after
  one correction round. Stage 3 simulated peer review is awaiting explicit
  user confirmation; this is not a release or submission candidate.
- `PUBLIC_RELEASE_AUTHORIZED=false`; no repository publication, venue submission,
  or Route advancement is implied.

## Main mathematical result

For a rational prime \(p\), the paper studies the bare compact abelian group

\[
U_p=\prod_{\ell\ne p}\mathbf Z_\ell^\times,
\qquad
B_p=U_p/e_p(\widehat{\mathbf Z}).
\]

It computes every primary torsion-closure quotient in terms of the local
Wieferich--Ulm depth \(\kappa_r(p)\), proves

\[
B_p\cong_{\mathrm{top}}B_q
\quad\Longleftrightarrow\quad
\kappa_r(p)=\kappa_r(q)\text{ for every prime }r,
\]

and gives the concrete separation \(B_2\not\cong_{\mathrm{top}}B_3\) at
\(r=11\). The proof combines the diagonal homogeneous-triangular/Kulikov
argument with an off-local exact-order Kummer--Chebotarev construction and a
kernel-internal root correction.

The theorem is deliberately limited to the unmarked compact groups. It does
not recover actual packet topology, measure, a flow, trace, operator, or
determinant, and it does not prove that the full signature determines the
prime.

## Route-map correspondence

The governing roadmap documents are
[`skills/route-a-evaluator.md`](../../skills/route-a-evaluator.md) and
[`skills/route-b-evaluator.md`](../../skills/route-b-evaluator.md).

- **Route A:** the object has arithmetic provenance but no frozen dynamics,
  clock, primitive-orbit ledger, normalization, determinant convention, or
  train/validation split. Its required-input screen is `NOT_TESTABLE`; no
  A0--A4 tuple and no overall Route-A verdict are assigned.
- **Route B:** the paper supplies no Hilbert space, dense domain, boundary
  conditions, operator action, arithmetic clock, trace theorem, or determinant
  on one common object. Advancement is not authorized and the exact overall
  status is `ROUTE_B_NOT_TESTABLE`; no Hilbert--Pólya claim is allowed.

Accordingly, the paper is a compact-group classification result, not a Route-A
or Route-B milestone.

## MG11 relationship

The local MG11 B00/B01 chain is included only as a nonnormative,
machine-readable conformance record. Its schema and persisted 0/1/2-row and
E10-reject instance receipts do not constitute an executed checker, a proof of
universal correctness, or evidence for the mathematical theorem.

## Package

- [`paper/manuscript.tex`](paper/manuscript.tex) — LaTeX source
- [`paper/references.bib`](paper/references.bib) — bibliography
- [`paper/figures/classification_pipeline.tex`](paper/figures/classification_pipeline.tex)
  — native-vector classification diagram
- [`paper/claim_intent_manifest.json`](paper/claim_intent_manifest.json) —
  pre-composition claim-intent manifest
- [`paper/paper.pdf`](paper/paper.pdf) — retained 14-page PDF
- [`paper/README.md`](paper/README.md) — build and integrity receipt

The next manuscript gate is Stage 3 simulated peer review, which cannot begin
without explicit user confirmation. The Stage-2.5 report is
[`notes/stage2_5_integrity_report_v1.md`](notes/stage2_5_integrity_report_v1.md).
Release and submission remain downstream actions requiring separate explicit
authorization.
