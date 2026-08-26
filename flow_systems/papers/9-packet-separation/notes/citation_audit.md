# Paper 9 independent citation and source-integrity audit

**Audit date:** 2026-08-14 (Asia/Shanghai)  
**Audit role:** independent ARS citation/source/integrity reviewer  
**Final verdict:** **ACCEPT**, conditional only on (i) the public-release index
check in Section 9 excluding every retained source PDF and (ii) the human
author confirming the provisional journal-facing declarations before
submission.

This audit was read-only with respect to the manuscript, bibliography, figures,
compiled paper, evidence locks, Route records, retained sources, manifests, and
preflight sidecars.  The only file written by the audit is this report.  The
review distinguishes source-owned facts, manuscript-owned proofs, exact
manifestation identity, bibliographic identity, and permission to redistribute
source bytes.

## 1. Exact candidate lock

The decision attaches only to these final candidate bytes:

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` |
| `paper/references.bib` | `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35` |
| `paper/paper.pdf` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |

The released PDF has 21 A4 pages and exposes the expected title, author,
subject, and keywords.  A fresh independent
XeLaTeX--BibTeX--XeLaTeX--XeLaTeX rebuild in a temporary directory completed
with:

- zero compilation errors;
- zero undefined citations or references;
- zero BibTeX warnings;
- zero missing-glyph diagnostics; and
- zero overfull boxes.

The remaining six underfull-box diagnostics are harmless paragraph-spacing
notices.  The released and independently rebuilt PDFs have identical
`pdftotext -layout` bytes, SHA-256
`fb94d76d0b9be5649a836cd8d3f46dbdb8a5c6a7d0e69143d4eda9aee391755d`.
Their visible/textual content therefore agrees despite timestamp-dependent PDF
container bytes.  Visual checks of pages 1, 7, 14--16, and 19--21 covered the
bilingual abstract, CRT proof, topology-owner figure, corrigendum, exact Route
table, evidence locks, declarations, and complete bibliography; no clipping,
overlap, truncated formula, malformed citation, or broken table was found.

## 2. Citation closure

The manuscript contains 20 citation commands and seven unique cited keys.  The
bibliography contains exactly the same seven keys:

```text
ConnesConsani2016  ConnesConsani2026  Deninger2024  Deninger2026
Justel2018         LeBruyn2016        Morishita2026
```

- cited but absent from `references.bib`: **0**;
- bibliography entries never cited: **0**;
- duplicate bibliography keys: **0**; and
- undefined citations in the independent final build: **0**.

Citation-command counts are nine for `Deninger2026`, four for
`Morishita2026`, two each for `Deninger2024` and `ConnesConsani2016`, and one
each for `ConnesConsani2026`, `LeBruyn2016`, and `Justel2018`.  Every entry is a
primary article, chapter, or exact primary preprint used for a mathematical or
topology-ownership claim.  No search-result page, secondary summary, or
unverified metadata record is used as proof authority.

## 3. Exact manifestations and retained-source integrity

The seven retained primary manifestations are the exact full texts named by
`notes/sources/paper9_source_manifest.md`:

| Key | Exact technical manifestation | Pages | PDF SHA-256 prefix | Result |
|---|---|---:|---|---|
| `Deninger2026` | arXiv `1807.06400v4`, 2024-02-07 | 119 | `edd0bc8c2efb` | PASS |
| `Deninger2024` | arXiv `2301.11643v1`, 2023-01-27 | 16 | `453c19e9daa2` | PASS |
| `Morishita2026` | arXiv `2508.15971v5`, 2026-01-21 | 26 | `3a5a34165a4b` | PASS |
| `ConnesConsani2016` | exact Numdam/publisher PDF | 6 | `fc10fee06a68` | PASS |
| `ConnesConsani2026` | arXiv `2501.06560v1`, 2025-01-11 | 30 | `f200c41d6d77` | PASS |
| `LeBruyn2016` | institutional author version, including repository cover | 10 | `50895be562a1` | PASS |
| `Justel2018` | arXiv `1605.05168v2` | 30 | `6e8f63351b20` | PASS |

All seven same-stem ARS preflight sidecars report `PASS`, equal declared,
enumerated, and reader page counts, and empty warning arrays.  A fresh
`sha256sum -c notes/sources/paper9_sources.sha256` check passes all 14 entries:
seven PDFs and seven sidecars.  The source-manifest and checksum-ledger hashes
printed in the manuscript also match the current bytes:

```text
paper9_source_manifest.md  8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906
paper9_sources.sha256      6413af8f2d0afec7158aec123f32a641776edcef0a9a9e747fd0ebc5c5f697e4
```

The first three PDFs are reused byte-for-byte from Paper 8, exactly as the
manifest states; no duplicate or silently substituted manifestation was used.

## 4. Load-bearing locator and claim graph

Every source-dependent claim was traced to the retained full text.  The
following table records the load-bearing edges rather than merely counting
citations.

| Source | Manuscript use | Exact checked support | Result |
|---|---|---|---|
| `Deninger2026` | finite-kernel parametrization; Galois/balanced-product set coordinates; suspension, right action, packet clock and isotropy; pre-suspension topology; warning that suspension-coordinate maps need not be homeomorphisms | equation (35), physical p. 32; equations (38)--(39), pp. 32--33; Section 6 and Theorem 6.1, pp. 38--39; Proposition 7.4, p. 43; Propositions 7.6--7.7, Corollaries 7.8--7.9, Theorem 7.10, Remark 2 and the `E_f` paragraph, pp. 44--47 | PASS |
| `Deninger2024` | compactness wording without a Hausdorff promotion; second continuous-bijection warning | Theorem 4.2, physical pp. 11--12; Theorem 4.4 and following sentence, pp. 12--13 | PASS |
| `Morishita2026` | character/adelic comparison, omitted-refinement boundary, continuity and flow anti-equivariance; source proof ceiling requiring the manuscript's away-from-`p` nonvanishing repair | equation (1.1.5), p. 5; Remark 2.1.13, p. 13; equation (2.2.7) and Theorems 2.2.8--2.2.9, pp. 14--17; Lemmas 3.4--3.5 and Theorem 3.6, pp. 23--25 | PASS |
| `ConnesConsani2016` | intrinsic scaling-topos prime circle, with its own topology | Lemma 6.3(i), physical/printed p. 5 | PASS |
| `ConnesConsani2026` | specifically defined natural quotient/scaling object and mapping-torus comparison | physical p. 9; Proposition 3.4, pp. 11--12 | PASS |
| `LeBruyn2016` | warning that a related finite-adele-class topology must not be mislabeled indiscrete | Theorem 1, printed p. 2/physical p. 3; correction acknowledgement, printed p. 9/physical p. 10 | PASS |
| `Justel2018` | explicit locally compact Hausdorff/strong properness prerequisites before orbital averaging and Zak/Weil machinery | Definition 2.1, physical pp. 3--4; Lemma 2.3, p. 5; Theorem 2.4, p. 6 | PASS |

The important negative controls also pass.  Deninger's equations (38)--(39)
are used as equivariant **set** bijections, not as inherited-topology
homeomorphisms.  The survey's compactness statement is not silently upgraded
to compact Hausdorff.  Morishita's coarser full-character wording and incomplete
away-from-`p` orbit-image check are disclosed rather than imported.  The
Connes--Consani intrinsic circle is not identified topologically with the naive
adelic subspace.  Le Bruyn's different quotient and Deninger's related generic
`T1` quotient are not promoted to the fixed-prime packet.

## 5. Proof ownership and claim strength

The manuscript correctly owns the new proofs instead of attributing them to
the cited literature:

1. the open quotient and saturated-restriction lemma;
2. constructive diagonal density of
   `Z[1/p]_{>0}` in `R_{>0} x A_p`, with the congruence imposed on the rational
   number rather than only its numerator;
3. finite-kernel membership and fixed-stage pointwise convergence;
4. unit normalization and exact normalized equivalence;
5. universal constant-class convergence, packet/orbit/quotient
   indiscreteness, and nonclosedness of the restricted relation;
6. indiscreteness of the exact naive adelic prime orbit; and
7. the repaired actual-to-actual Morishita comparison.

The final finite-kernel proof no longer calls a general
`q_j=m_j/p^{k_j}` an away-from-`p` unit.  It explicitly factors
`m_j=p^{s_j}m'_j`, separates automorphic factors from the finite
`m'_j`-torsion kernel, and proves eventual character equality modulo the
finite order of each torsion element.  The manuscript also checks all
away-from-`p` components in the Morishita image before asserting that the
restriction lands in the exact naive adelic orbit.  These repairs match the
proof audit and do not ask the sources to prove more than they do.

The topology-owner boundary remains explicit throughout: actual inherited
packet, actual inherited orbit, intrinsic scaling circle, naive adelic orbit,
and imposed standard-circle proxy are different typed objects.  The standard
LCH--Hausdorff groupoid branch is stopped only at its failed named prerequisite;
the manuscript does not infer a universal no-go for non-Hausdorff groupoids,
Haar systems, completions, traces, or spectral constructions.

The novelty statement is bounded to the retained search through 2026-08-14
and says that no direct theorem was located.  It explicitly disclaims absolute
historical priority and generic novelty for CRT, quotient topology, or
indiscrete-space facts.  This is the strongest wording justified by the source
audit.

## 6. Bibliographic metadata and DOI audit

The seven records were compared with their exact arXiv, publisher, DOI, and
Crossref identities.  Author lists, titles, years, venues, volume/issue data,
page/article ranges, and manifestation notes agree.  Every record in
`references.bib` carries a DOI field.

Material metadata checks include:

- `Deninger2026`: *Indagationes Mathematicae* **37**(1) (2026), 25--136,
  DOI `10.1016/j.indag.2024.05.007`; technical pages remain explicitly bound
  to arXiv v4.
- `Deninger2024`: *Colloquium De Giorgi 2021 and 2022* (2024), pp. 177--196,
  ISBN `978-88-7642-773-2`, with arXiv DOI
  `10.48550/arXiv.2301.11643`; locators remain on v1.
- `Morishita2026`: arXiv v5, DOI `10.48550/arXiv.2508.15971`, dated
  2026-01-21 and described only as “to appear”; no invented journal volume or
  pages.  The `plainnat` style omits this `@misc` DOI in rendered prose, but the
  exact DOI remains in the Bib source and the rendered v5 URL uniquely binds
  the manifestation.
- `ConnesConsani2016`: volume 354(1), pp. 1--6, DOI
  `10.1016/j.crma.2015.09.027`.
- `ConnesConsani2026`: *Contemporary Mathematics* **842**, pp. 105--132,
  DOI `10.1090/conm/842/16852`; technical locators remain on arXiv v1.
- `LeBruyn2016`: volume 15(2), article 1650020, DOI
  `10.1142/S0219498816500201`; the repository-cover pagination offset is
  explicitly disclosed.
- `Justel2018`: *Journal of the London Mathematical Society* **97**(1),
  pp. 47--76, DOI `10.1112/jlms.12097`; technical locators remain on arXiv v2.

No title/author ambiguity, fabricated identifier, retraction signal, or exact
manifestation mismatch remains.

## 7. Controls, evidence locks, and Route boundary

The manuscript accurately describes the deterministic controls as finite
regression witnesses, not proofs of infinite density, pointwise convergence,
indiscreteness, or nonclosedness.  The locked control manifest is current:

```text
results/packet_separation_manifest.json
52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668
```

It records 20/20 passing tests, eight CSV artifacts, and 240 data rows.  The
proof-audit, Phase-3 peer-review, route-audit, composition-blueprint, and all
eight Stage-9 Route-A YAML hashes printed in Appendix A match the actual files.
The exact eight Route tuples agree with the canonical `notes/route_audit.md`:
all have `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`; only the separately typed proxy
trivial-character owner has `A1_PASS_ANALYTIC`; every overall verdict remains
`ROUTE_A_EXPLORATORY`; and Route B is not invoked.

No target zero, fitted parameter, determinant, analytic continuation,
functional equation, zero/divisor correspondence, natural quantization, or
Hilbert--Pólya claim is introduced.  The positive-time scalar ledger, proxy
formulas, and actual topology are not spliced into one owner.

## 8. Abstracts, declarations, and integrity modes

The English and Chinese abstracts agree on the load-bearing scope: diagonal
approximation, legal finite-kernel convergence, universal specialization,
three indiscreteness conclusions, nonclosed relation, naive adelic comparison,
intrinsic-circle separation, Paper-8 owner correction, and the absence of a
general analytic no-go.  Neither abstract promotes a set bijection to an
unproved homeomorphism or widens the theorem to the global suspension.

The declarations cover data/code availability, ethics and consent, author
contributions, competing interests, funding, acknowledgements, and AI
assistance.  The AI statement names exact-byte comparison, proof drafting,
control generation, adversarial review, consistency checking, code assistance,
and language editing; it denies authorship credit and assigns verification and
submission responsibility to the human author.  The author-contribution,
competing-interest, funding, and acknowledgement wording is deliberately
provisional.  This is transparent rather than fabricated, but those entries
must be confirmed by the human author before journal submission.

The ARS integrity-mode review found:

| Mode | Audit result |
|---|---|
| fabricated or phantom sources | none; 7/7 exact primary full texts retained and hashed |
| citation misattribution or scope inflation | none after the explicit Deninger/Morishita ceilings |
| data or computation fabrication | none; deterministic controls, hashes, counts, and limitations agree |
| proof/source ownership confusion | none; source facts and manuscript derivations are separated |
| topology/type splicing | none; actual, intrinsic, naive, and proxy owners remain distinct |
| duplicate-publication concealment | none; Paper 8 is named and corrected through an explicit versioned matrix |
| authorship/conflict/funding opacity | no hidden assertion; provisional fields and AI use are disclosed for human confirmation |

## 9. Copyright and public-release boundary

Reproducible citation does not establish redistribution permission.  The seven
PDFs include arXiv copies, a publisher PDF, an institutional author version,
and byte-reused Paper-8 research copies.  Even where a publication has an open
licence, the audit does not infer a blanket file-level licence for every exact
retained manifestation.

The accepted conservative release policy is:

1. retain the seven PDFs locally for page-level verification;
2. exclude all Paper-9 `notes/sources/*.pdf` and all three reused Paper-8 source
   PDFs from public GitHub synchronization unless an exact-manifestation
   redistribution licence is documented;
3. publish the Bib metadata, canonical URLs, exact versions and locators,
   manifests, checksum ledger, preflight sidecars, audits, code, results,
   manuscript source, figures, and built paper; and
4. preserve both source directories' `.gitignore` rule `*.pdf`.

This workspace is not a Git worktree, so the final staged/tracked file set
cannot be inspected here.  The public-package acceptance condition is that a
fresh repository check returns no retained research PDF in `git ls-files` or
`git diff --cached --name-only`.  Any such tracked or staged PDF changes the
public-release verdict to **REVISE** until removed or supported by an exact-file
licence record.

## 10. Closed findings and decision

| Earlier mandatory finding | Final disposition |
|---|---|
| Inline mathematics was emitted as literal parentheses and the first XeLaTeX pass failed | all 321/321 inline and 38/38 display boundaries restored; clean build passes |
| `M_j` exponent and two `\quad` strings were malformed | corrected |
| structured math macros were used ungrouped and `\C` was undefined | macros grouped/defined; all sequential compile blockers closed |
| general `q_j` was incorrectly called an away-from-`p` unit | replaced by the exact finite-kernel factorization and torsion proof |
| Morishita restriction did not print the away-from-`p` nonvanishing check | exact componentwise check and normalization now printed |
| `Deninger2024` was present but uncited | exact Theorems 4.2/4.4 citations added; 7/7 closure achieved |
| `Deninger2024` arXiv DOI and `ConnesConsani2026` page range were initially absent | DOI `10.48550/arXiv.2301.11643` and pp. 105--132 added |
| large overfull boxes in the corrigendum, Route table, and lock table | table reflow/path breaks complete; final build has zero overfull boxes |
| retained PDFs risked blanket public synchronization | local-only `*.pdf` policy retained; final Git index check remains external |

**Manuscript/bibliography/source-claim verdict: ACCEPT.**  No citation,
metadata, locator, manifestation, claim-strength, proof-ownership, bilingual
abstract, build, evidence-lock, or Route-boundary blocker remains on the exact
candidate lock.

**Journal-submission integrity verdict: ACCEPT conditional on human confirmation
of the explicitly provisional declaration fields.**

**Public GitHub package verdict: ACCEPT conditional on the Section 9 zero-PDF
tracked/staged-path check.**  These are external packaging/author-confirmation
conditions, not requests to alter the accepted manuscript, bibliography,
figures, or compiled paper.
