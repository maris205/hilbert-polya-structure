# Fresh Independent Manuscript Review — Round 2

**Manuscript:** *An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients*  
**Candidate:** `cat_equivariant_retention_tradeoff_v1`  
**Review date:** 2026-08-15 UTC  
**Review mode:** fresh, hash-bound Round-2 re-review of the revised source,
rendered PDF, Round-1 record and response, frozen scientific evidence, and
release-boundary artifacts  
**Editorial recommendation:** **ACCEPT**  
**Release disposition:** **PASS / MAY_FINALIZE**

## Decision summary

The sole Round-1 finding, `R1-M1`, is fully addressed.  The revision contains
exactly the four requested reader-facing substitutions and no other source
change: four lines are removed, four lines are added, both sources remain
1,238 lines, the revised manuscript contains zero reader-facing `Paper 10` or
`Paper 11` hit, and mechanically reversing the four substitutions recovers
the exact Round-0 source digest.

I found no mathematical, quantifier, evidence, citation, provenance,
anonymity, typography, or release-boundary regression.  The complete finite
\(C\)-set theorem, regular-torsor specialization, \(q=2\) exception,
family-uniform conclusion, nine-row exact ledger, effective \(C_6\) control,
and definition-sensitive nonclaims remain correct and mutually consistent.
The execution and analyzer trees, raw result, strict manifest, scope audit,
bibliography, and complete figure asset tree retain their frozen identities.

Two new isolated clean builds independently reproduced the approved revised
PDF byte for byte.  All 19 pages passed visual inspection; all 39 PDF font
records are embedded, subset, and Unicode-mapped; and the PDF has zero Type-3
font, raster image object, LaTeX/BibTeX warning, undefined citation, or
undefined reference.

**Finding count:** 0 Critical, 0 Major, 0 Minor, and 0 residual blocker.

## Round and artifact bindings

All identities assigned to this review were recomputed from the current
regular files and match exactly.

| Bound artifact | Recomputed SHA-256 | Status |
|---|---|---|
| Round-1 review | `83c6b2ccb48d776f2d23a0ea6423b16504c6f73625b8a85652aad2fa0807da21` | exact |
| Round-1 response | `b74d88f2cec9b8d0655c0ec752441a6ad8d19ee31111dc7c65da9b8842df2869` | exact |
| revised `manuscript.tex` | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` | exact |
| revised `manuscript.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | exact |
| `paper_round1_revision.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | exact and byte-identical to workspace PDF |
| Round-1 integrity record | `7b61e118f2e63530226095bc1a9a79a9e8f219d24e08342727f0a3734eedc223` | exact |
| Round-1 pipeline state | `a17f4eb2e497ba09b754a259e96398fb0d1d03c5f2a25c5a15dec7f33bff7230` | exact; `READY_FOR_INDEPENDENT_ROUND2` |
| Round-0 source snapshot | `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5` | exact and preserved |
| Round-0 pre-review PDF | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` | exact and preserved |
| pre-review integrity record | `4e82724bdee00b1c31858585c6cd1008106b818ef7cef849661767fbdb1a300f` | exact |
| pre-review pipeline state | `8f55bd719f12c2a9cf1dcd83669a6972f80f2f279a58137c9df26100aee86af0` | exact |

No `paper_final.pdf`, `paper_final*`, or other final PDF exists anywhere in
the Paper-11 tree.

## Round-1 finding traceability

### `R1-M1` — standalone reader-facing wording

**Round-1 requirement.** Replace four internal project-sequence labels with
standalone wording without changing scientific content or frozen evidence.

**Round-2 verification.** `FULLY_ADDRESSED`.

| Revised source line | Removed | Added |
|---:|---|---|
| 190 | `Paper 11 neither` | `The present note neither` |
| 627 | `No Paper-10 candidate or calculation is rerun here` | `No candidate or calculation from that centralizer-quotient audit is rerun here` |
| 1028 | `before Paper-11 execution` | `before the registered execution` |
| 1144 | `upstream Paper-10 final PDF` | `frozen upstream centralizer-audit PDF` |

The exact zero-context diff has four hunks, four removed lines, and four
added lines.  There is no fifth hunk.  Both sources contain 1,238 lines.
A case-insensitive reader-facing scan for the Paper-10/Paper-11 forms returns
zero.  Reversing precisely these four replacements in a stream produces
SHA-256
`88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5`,
the frozen Round-0 source identity.  The response's change ledger is
therefore accurate, and `R1-M1` is closed without scientific drift.

## Mathematical and claim-scope audit

### General finite-translation layer

The manuscript correctly treats a finite abelian \(C\)-set
\(X=\bigsqcup_K n_K(C/K)\) with translation by \(a\) and
\(H=\langle a\rangle\).  For each orbit type it obtains

\[
d_K=[H:H\cap K],\qquad M_K=[C:HK].
\]

Thus one copy of \(C/K\) contributes \(M_K\) source cycles of length
\(d_K\), while its coarse \(C\)-quotient is one fixed point.  The point-order
exact class is supported at \(d_K\), the fixed-orbit exact class is supported
at one, and the resulting point-order and orbit-order Burnside zetas are
kept distinct.  The point-counting specialization is explicitly additive
but not multiplicative; the action-kernel, effectivization, and
rigidification statements are not conflated.

The stabilizer convention is correct for the locked left action:
\((1,a^{-1})\), not \((1,a)\).  Combining represented orbit types recovers
the label only modulo the action kernel \(\bigcap K\); exact labelled recovery
is asserted only in the effective case.  The enhanced return twist is
correctly \(a\), while the 2013 stabilizer triple records \(a^{-1}\).  The
action-groupoid and inertia arguments correctly distinguish
presentation-sensitive carriers from Morita- and 2-isomorphism-invariant
static quotient data.

The effective structural control
\(C_6/C_2\sqcup C_6/C_3\) is also correct: the source supports are three and
two, there is no support-six source factor, the action kernel is trivial,
the quotient stack is \(BC_2\sqcup BC_3\) with identity dynamics, and the
static inertia-sector count is five.  It remains separately typed and is
never presented as a tenth arithmetic row.

### Regular-torsor layer and exact nine-row ledger

For the regular \(G_q\)-torsor, the manuscript consistently uses
\(n_q=|G_q|\), \(r_q=\operatorname{ord}(A)\), and \(m_q=n_q/r_q\).  Direct
comparison with the immutable raw result reproduced every row and all 36
support--exponent cells:

| \(q\) | \(n_q\) | \(r_q\) | \(m_q\) | point cardinality | point orbifold | orbit cardinality | orbit orbifold |
|---:|---:|---:|---:|---|---|---|---|
| 2 | 3 | 3 | 1 | \((1-t^3)^{-1}\) | \((1-t^3)^{-1/3}\) | \((1-t)^{-3}\) | \((1-t)^{-1}\) |
| 3 | 8 | 4 | 2 | \((1-t^4)^{-2}\) | \((1-t^4)^{-1/4}\) | \((1-t)^{-8}\) | \((1-t)^{-1}\) |
| 5 | 20 | 10 | 2 | \((1-t^{10})^{-2}\) | \((1-t^{10})^{-1/10}\) | \((1-t)^{-20}\) | \((1-t)^{-1}\) |
| 7 | 48 | 8 | 6 | \((1-t^8)^{-6}\) | \((1-t^8)^{-1/8}\) | \((1-t)^{-48}\) | \((1-t)^{-1}\) |
| 11 | 100 | 5 | 20 | \((1-t^5)^{-20}\) | \((1-t^5)^{-1/5}\) | \((1-t)^{-100}\) | \((1-t)^{-1}\) |
| 4 | 12 | 3 | 4 | \((1-t^3)^{-4}\) | \((1-t^3)^{-1/3}\) | \((1-t)^{-12}\) | \((1-t)^{-1}\) |
| 6 | 24 | 12 | 2 | \((1-t^{12})^{-2}\) | \((1-t^{12})^{-1/12}\) | \((1-t)^{-24}\) | \((1-t)^{-1}\) |
| 9 | 72 | 12 | 6 | \((1-t^{12})^{-6}\) | \((1-t^{12})^{-1/12}\) | \((1-t)^{-72}\) | \((1-t)^{-1}\) |
| 10 | 60 | 30 | 2 | \((1-t^{30})^{-2}\) | \((1-t^{30})^{-1/30}\) | \((1-t)^{-60}\) | \((1-t)^{-1}\) |

The source cycles, divisor inversion, unique twisted fixers
\(g=A^{-k}\), regular action kernel, one quotient-groupoid isomorphism
class, one identity inertia sector, shortening factor \(1/r_q\), and gluing
multiplicity \(m_q\) are all stated with the correct direction and
normalization.

### \(q=2\), family-uniform quantifier, and nonclaims

The unique locked row/type combining source support with unit exponent is
the point-cardinality factor at \(q=2\), \((1-t^3)^{-1}\).  The manuscript
states this exception repeatedly and never revives the superseded
point-by-point nonattainment claim.  Its negative scalar statement is only
family-uniform: no single one of the four scalar-reduction types has both
properties throughout all nine rows.

The collisions \(r_2=r_4=3\) and \(r_6=r_9=12\) are correctly recorded.
Consequently the local \(q=2\) exception is not modulus-specific.  The A0
disposition means failure to obtain a **common intrinsic** modulus clock or
prime selector; it does not mean that every local one-cycle factor fails.
The finite rows are exact implementation and falsification controls rather
than an all-\(q\) empirical fit.

The abstract, introduction, figures, Section 7, route decision, conclusion,
and appendices agree on this corrected scope.  They also retain the explicit
nonclaims: no new equivariant/orbifold/enhanced/stacky zeta theory, no
universal no-go theorem, no canonical cross-\(q\) coefficient-ring
identification, no analytic evaluation or prime-zero claim, and no opening
of Route B.  I found no stronger-quantifier or claim-strength regression.

## Frozen evidence and provenance

The principal scientific and publication authorities were independently
rehash-checked:

| Authority | SHA-256 | Round-2 result |
|---|---|---|
| source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | exact |
| proof/formula package | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` | exact |
| claims/evidence matrix | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` | exact |
| raw registered result | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` | exact |
| strict V2 result manifest | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` | exact; pass |
| independent result review | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` | exact; `RESULT_PASS` |
| post-run analyzer review | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` | exact; `ANALYZER_PASS` |
| independent scope audit | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` | exact; `PASS_WITH_SCOPE_CORRECTION` |
| figure asset tree | `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c` | exact; all 25 records close |
| figure manifest | `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc` | exact; pass |

I independently recomputed the documented framed tree digests without
running or importing the candidate:

- immutable registered execution tree: 36 closed paths, including the exact
  26-file code inventory, SHA-256
  `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`;
- separate post-run analyzer tree: 12 closed paths, SHA-256
  `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3`.

The inventories contain only the declared regular files and directories;
there is no symlink, nonregular object, cache, or extra source path.  Their
roles remain distinct: the analyzer has validator-only authority and does
not rewrite the immutable execution tree or raw result.  The historical
first manifest attempt remains recorded as a prewrite failure caused by a
JSON-list/Python-tuple comparison; the later analyzer corrects exactly that
serialized K005 predicate.  The closed V2 manifest's 13 non-self file
bindings all match.  The raw result contains exactly the ordered nine rows,
the separately typed structural control, and K001--K012 all true.

The complete Paper-10 upstream binding set in the source lock also rehashes
exactly, including source lock, source review, raw result, result manifest,
result review, both official reports, Round-2 review, final integrity, final
pipeline state, and the frozen centralizer-audit PDF
`f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`.
Paper 11 uses only that frozen theorem/result boundary and performs no
upstream rerun.

No candidate command, registered audit, candidate/registered test, analyzer
command, figure generator, or scientific rerun was invoked in this review.
No network or external dataset was used.  Review operations were read-only
parsing, hashing, static inspection, independent exact checks, PDF QA, and
the two required LaTeX builds in disposable trees.

## Citations, figures, anonymity, and standalone presentation

### Citation closure

The manuscript cites exactly 14 unique keys.  They equal the 14 unique
entries in `references.bib`; there is no missing key, unused entry,
duplicate bibliography item, or BibTeX warning.  The direct-construction and
scope-boundary roles remain calibrated, and the manuscript does not turn
frontier-context citations into implementation or priority authority.

The publication Walton record is correct and consistent in prose and
bibliography: *Journal of Number Theory* **192** (2018), 386--405, DOI
`10.1016/j.jnt.2018.03.023`.  The manuscript transparently preserves the
different frozen design-side transcription as provenance and makes no
scientific inference from that correction.  Because network access was
prohibited, this review verifies the frozen citation package and its internal
closure; it does not claim a new online literature-completeness search.

### Figure closure

Exactly three publication figures are included, in the declared order and
with the declared captions:

| Figure | PDF SHA-256 | Integrated page | Status |
|---|---|---:|---|
| retention hierarchy | `f80ea5a21d46f7b419196689b96127efc37e842fc21b890b28a02f02a722c525` | 4 | exact, legible |
| nine-row retention ledger | `9525b8c11d7da9fe00409bebc591d1d792867176e8a7e764c95bbbabafeba329` | 12 | exact, legible |
| effectivity counterexamples | `aaef94b667ede3c309044f28be9c029ab2435b5a5d77031e292ed0dc257c8c5b` | 13 | exact, legible |

Figure 2 has the unique \(q=2\) star and both exact period collisions;
Figure 3 keeps the effective \(C_6\) control outside the arithmetic-row
namespace.  The integrated PDF uses the vector figure PDFs and contains zero
raster image object.

### Anonymity and presentation

The source and PDF metadata identify the author only as `Anonymous Authors`.
There is no author name, email address, affiliation, ORCID, local filesystem
path, or reader-facing Paper-10/Paper-11 sequence label in the rendered PDF.
The withheld contribution, conflict, and funding metadata are explicitly
marked as anonymous-review placeholders.  No anonymity or standalone-
presentation regression remains.

## Independent clean builds and PDF QA

I created two separate disposable clean trees containing only
`manuscript.tex`, `math_commands.tex`, `references.bib`, `build.sh`, and the
three referenced figure PDFs, and ran the frozen build once in each tree.
Both builds exited successfully.  Each output was byte-identical to the
other build and, where applicable, to the approved Round-1 revision:

| Artifact | Build 1 SHA-256 | Build 2 SHA-256 | Status |
|---|---|---|---|
| PDF | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | approved PDF reproduced |
| LOG | `36d5b80b76d0e226af83dfbbbe294dbecd8f308d2a78f8f6dbb5b8b083c9cc7b` | `36d5b80b76d0e226af83dfbbbe294dbecd8f308d2a78f8f6dbb5b8b083c9cc7b` | exact |
| BLG | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` | exact |
| BBL | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` | exact |
| AUX | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` | exact |
| OUT | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` | exact |

The changed prose renders cleanly on pages 3, 8, 15, and 17.  I inspected
all 19 pages at rendered original resolution, including all equations,
tables, captions, figures, footnotes, appendices, and references.  There is
no clipping, overlap, missing glyph, broken link text, or unreadable figure
annotation.

Mechanical closure:

- 19 pages, letter size, unencrypted, no JavaScript or form;
- 39 font records; 39 embedded, 39 subset, 39 Unicode-mapped;
- zero Type-3 font and zero raster image object;
- zero LaTeX/package warning, BibTeX warning, overfull/underfull box,
  undefined citation/reference, or multiply defined label in either clean
  build;
- 65 labels, all unique; 40 referenced targets, zero missing target;
- 14 cited keys, 14 bibliography entries, zero missing or unused key;
- title and subject metadata appropriate; author metadata anonymous; no
  metadata stream, custom metadata, or identifying path.

## Integrity and release boundary

The source lock, proof package, code inventories, registered claim/run and
raw result, analyzer tree, scope audit, bibliography, three figure PDFs,
25-file asset tree, and Round-0 pre-review source/PDF are unchanged.  Only
the four authorized manuscript lines and their downstream Round-1 build and
integrity nodes differ from Round 0.  This review did not modify any
manuscript, figure, reference, source, code, result, test, manifest, or
lifecycle file.

This report is an independent Round-2 gate.  It authorizes the separate
finalization step by returning **MAY_FINALIZE**, but it does not perform that
step, create or copy a final PDF, rewrite a pipeline state, or bless any
future bytes that differ from the exact approved revision bound above.

## Final verdict

**PASS / MAY_FINALIZE — ACCEPT.**

- Critical blockers: **0**
- Major blockers: **0**
- Minor blockers: **0**
- Residual blockers: **0**
- Round-1 `R1-M1`: **FULLY_ADDRESSED**

The revised manuscript and approved 19-page PDF satisfy the complete
Round-2 acceptance gate.  Finalization may now proceed as a separate,
hash-preserving lifecycle operation.  No finalization was performed by this
review.
