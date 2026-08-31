# Final QA — P130 round 2

Date: 2026-08-31  
Result: **PASS — GO_INTERNAL / HOLD_EXTERNAL**

## 1. Frozen source and exact control

- `main.tex`:  
  `70f020aa1b89353b94f76b781bee19e6c6fbc2d56824431d95090e3e4fcb033a`
- `code/verify.py`:  
  `abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d`
- `code/verification_output.txt`:  
  `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`

A fresh run used `PYTHONDONTWRITEBYTECODE=1`; its stdout had SHA-256
`89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`
and `cmp` returned success against the canonical transcript.

Exact scope:

- **735,609 assertions**;
- every rooted chord matching for `0<=n<=7`;
- 146,600 states, including the empty state;
- 626 noncrossing targets;
- 146,600 independently reconstructed sources;
- forward map, idempotence, component supports, four-stage target-wise
  inverse, pointwise products, mass and unique maximizer all checked.

## 2. Four-stage builds

The following settled sequence passed locally:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The same sequence passed independently in a fresh temporary directory whose
initial payload was only `main.tex` and `references.bib`.  Its copied source,
bibliography and final PDF matched the local files byte for byte.  The settled
local and isolated log scans found no error, warning, undefined
citation/reference, rerun request, or overfull/underfull box.  All 8
bibliography entries are cited.

## 3. PDF archive and byte identity

| Artifact | Pages | Bytes | SHA-256 | Relation |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 4 | 342,739 | `4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9` | frozen round 0 |
| `main_round1.pdf` | 4 | 345,749 | `6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb` | frozen round 1 |
| `main.pdf` | 4 | 346,056 | `c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa` | current round 2 |
| `main_round2.pdf` | 4 | 346,056 | `c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa` | byte-identical final snapshot |

`cmp main.pdf main_round2.pdf` passed.  The final isolated PDF also matched
these bytes exactly.  Historical round-zero and round-one PDFs were not
modified.

## 4. All-page visual audit

Each page was rasterized after the final build and inspected individually at
original detail.

| Page | Material checked | Result |
|---:|---|---|
| 1 | anonymous title and abstract, scope/owner boundary, definitions and Proposition 1.1 opening | PASS |
| 2 | Proposition 1.1 conclusion and Theorem 2.1 forward/converse Steps 1--2 | PASS |
| 3 | inverse completion, connected decoration, mutual inverse, corrected owner/firewall remark and Theorem 3.1 opening | PASS |
| 4 | unique-maximum proof, census/control statement and all eight references | PASS |

No clipping, overlap, missing glyph, bad line or theorem break, hidden markup,
path leak or identifying content was found.

## 5. Fonts, metadata and anonymity

- 25/25 font records are embedded, subsetted and Unicode-mapped.
- PDF format is 1.5; page size is A4; all page rotations are zero.
- Title, author, subject and keyword metadata fields are blank.
- There is no metadata stream, custom metadata, embedded file, form,
  JavaScript or encryption.
- Text scans found no `??`, unresolved citation marker, TODO/FIXME/DRAFT tag,
  filesystem path, ORCID or affiliation leak.

## 6. Review closure

- Hostile Review A: 0 CRITICAL, 2 MAJOR, 2 MINOR; all closed in round one.
- Hostile Review B: 0 CRITICAL, 0 MAJOR, 2 MINOR; both closed in round two.
- B1 closure: only nonempty sibling lists are called exact Igusa parallel
  sets; degree zero is explicitly `A_0=1` bookkeeping.
- B2 closure: P110 is correctly identified as cyclic partition shift--join
  dynamics.
- Consolidated open findings: **0 CRITICAL / 0 MAJOR / 0 MINOR**.

The residual claim ceiling remains the literal target-wise decorated sibling
inverse/product and unique maximal fibre.  Owned generic geometry and
enumeration receive zero contribution credit.  A bounded owner non-hit is not
novelty evidence.

## 7. Integrity manifest and release boundary

`SHA256SUMS` covers the manuscript source, bibliography, verifier, canonical
stdout, all four PDF artifacts, plans/reports, both independent reviews,
consolidated review and final QA.  `sha256sum -c SHA256SUMS` must return success
for every listed file.

Internal mechanics and review closure pass: **GO_INTERNAL**.  External novelty,
priority, submission and release authorization remain outside this package:
**HOLD_EXTERNAL**.
