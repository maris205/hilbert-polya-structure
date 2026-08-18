# Writer handoff

## Candidate

Title: *q-adic Finite-Size Boundary Spectra of Multiplicative Shifts of Finite
Type: Exact General Remainders and Golden Cantor Boundaries*.

The sealed writer candidate is represented by `main.pdf` (16 A4 pages,
SHA-256 `3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`)
and the C-sorted, self-excluding `WRITER_MANIFEST.sha256` produced after this
handoff.  The LaTeX source is standalone and contains no generated build
auxiliaries.

## Mathematical payload

The paper proves an exact finite-size identity for a primitive multiplicative
shift of finite type by combining the (q)-adic chain partition, a chain-count
product, valuation census, Perron deviations, and exact summation by parts.  It
identifies the full remainder accumulation set as the continuous image of

\[
  \mathbb Z_q=\varprojlim \mathbb Z/q^m\mathbb Z,
\]

including composite (q), with both accumulation inclusions proved.

For the binary golden control, it derives the residue coefficients exactly,
uses the algebraic certificate

\[
  6557^2-5\cdot2929^2=99044>0,
\]

to obtain all-level strong separation, and proves equal Hausdorff and box
dimension

\[
  \frac{\log 2}{2\log\varphi}.
\]

For the ordinary generating function, it proves at every primitive dyadic root
(\xi) of order (2^v) the exact radial coefficient

\[
  \lim_{s\uparrow1}(1-s)G(s\xi)
  =-\frac{\gamma_{v-1}}{2^{v-1}(1-\xi)}\ne0,
\]

checks the normalization at (Q=4,\xi=i), and converts dense radial divergence
into a unit-circle natural boundary by an explicit bounded-holomorphic
continuation contradiction.

## Prior-work correction and scope

The Ban--Hu--Lai reconciliation is explicitly limited to the checked author
manuscript `arXiv:2210.09115v1`.  The paper spells out the exact locator chain:
Theorem 3.3(2) reduces through Theorem 3.1; the proof of Theorem 3.1(2) states
the one-dimensional mixing-SFT hypothesis; and Remark 3.4 gives
(d=1,N=p^{kn}).  The primitive full shift (J_D) satisfies those hypotheses
and contradicts the displayed subleading term.  No claim is transferred to an
uninspected version of record or erratum.

The ownership table assigns zero novelty credit to prior-owned inputs.  General
(q) receives only the exact remainder and accumulation-image results.  Cantor
dimension and the natural-boundary theorem are confined to the golden binary
control.  Operator determinants, spectral realizations, zeta identities, and
Riemann-hypothesis consequences are expressly outside the result.

The exact experimental canonical block is mechanically copied from the frozen
post-output authority artifacts; it is not reconstructed from prose or used as
a proof of the infinite theorems.  Route, nonclaim, and retrospective chronology
records are quarantined in non-anonymous reproducibility appendices.

## Reviews and repairs

- The plan audit first returned `PLAN_NOT_READY` (0 critical, 6 major, 5 minor);
  all findings were repaired and the recheck returned `PLAN_READY`.
- Improvement round 1 scored 7/10 with 0 critical, 3 major, and 4 minor issues.
  All three major presentation/provenance issues and all four minor proof/prose
  issues were repaired.
- Improvement round 2 scored 9/10 with 0 critical, 0 major, and 3 minor issues.
  All three minor source-locator/wording issues were repaired before the final
  deterministic builds.

The full reviews and repair ledger are in `PAPER_IMPROVEMENT_LOG.md`; raw review
artifacts are retained under `evidence/`.

## Build and QA

Two clean builds under fixed `SOURCE_DATE_EPOCH=1700000000`, `TZ=UTC`, and
`FORCE_SOURCE_DATE=1` are byte-identical.  Logs are clean.  Citation-key and
bibliography-item sets match.  All 25 font rows are embedded, subset, and have
Unicode maps.  Text and bounding-box extraction, control-character checks, and
page-by-page visual inspection all pass.  Details and reproducible hashes are
in `COMPILATION_REPORT.md` and `evidence/FINAL_QA_SUMMARY.txt`.

The final bibliography audit also checks the Ban--Hu--Lai title at three
levels: protected `\(\mathbb{N}^d\)` in BibTeX, uppercase `\mathbb{N}^d` in
the generated BBL, and a readable blackboard-bold $\mathbb N^d$ on page 16.
The synchronized plan matches the compiled six-section, three-appendix page
map.  These repairs were followed by a new two-build deterministic seal.

The protected 62-file authority tree exactly replays against its frozen
bytes-and-metadata snapshot.  The writer made no authority, Git, README, or
mirror write.

## Required next action

The writer content received an independent `CLEAN` audit at its original
40-file seal.  A later disposable overlay probe exposed a publication-mode
gap: the intentionally frozen pre-output auditor rejects any root-level writer
files as `STATIC_TREE_MISMATCH`.  No TeX or PDF byte was changed to repair that
gap.

This publication candidate adds a strict two-state auditor and bounded
transaction under `evidence/publication_gate/`.  The former requires either
the exact legacy authority or the exact legacy authority plus the entire
writer overlay; in the latter state it explicitly records the legacy rejection
as expected state supersession.  Neither tool is self-authenticating: every
invocation requires the independently approved SHA-256 of the raw publication
seal and checks it before trusting the seal or writer manifest.  The
transaction passes that exact external anchor through every preflight, staged,
target, and post-install audit.  It stages all bytes before any target write,
has an exit-86 late-failure path with zero changes, rolls back mid-install
errors, and makes a second identical invocation a zero-replacement operation.
The physical suite includes full-reclose content-delete, content-add, and
auditor-rewrite attacks against the old approved anchor.  Exact envelopes are
recorded in `PUBLICATION_SMOKE_EVIDENCE.json` without embedding the anchor.

After commit, use the selected Git blob/commit and the self-excluding
`PAPER_MANIFEST.sha256` as the persistent anchor for selecting the approved
publication-seal hash.

Request an independent **publication-mode** audit of the new manifest, seal,
auditor, transaction, and evidence.  Status remains
`HOLD_FOR_INDEPENDENT_PUBLICATION_AUDIT`; do not install or publish until that
audit returns `CLEAN`.  Any later installation must preserve the protected 62
files, exact integration results, Route tuple and lock, canonical block,
protected-input map, PDF SHA-256, and nonclaim boundary.
