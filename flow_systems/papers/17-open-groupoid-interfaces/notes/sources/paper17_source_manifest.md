# Paper 17 local-only source manifest

Manifest date: **2026-08-17 (Asia/Shanghai)**  
Role: exact-byte source registry for the authorized pre-manuscript
source/citation preflight lane  
Authorization gate:
`papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_gate.md`,
SHA-256
`1a94c73043e01b7d5861a20357abdb26edf5f7115b47d0552ddab376f197e8f9`

This manifest is not a bibliography, manuscript, citation authorization,
artifact receipt, build authorization, or release authorization. The retained
PDFs are local research copies. They are excluded by the adjacent `.gitignore`
and may not enter Git or public synchronization.

## 1. Closed corpus state

```text
EFFECTIVE_WORK_REGISTRY_COUNT=6
EXTERNAL_FRAMEWORK_WORK_COUNT=3
LOCAL_OWNER_WORK_COUNT=3
RETAINED_PDF_MANIFESTATION_COUNT=3
RETAINED_PDF_PREFLIGHT_PASS_COUNT=3
RETAINED_PDF_PREFLIGHT_NONPASS_COUNT=0
MOERDIJK_FULLTEXT_RETAINED=false
MOERDIJK_TECHNICAL_SOURCE_STATUS=METADATA_ONLY_SENTINEL
IMMEDIATELY_PREFLIGHT_ELIGIBLE_UNIQUE_WORK_COUNT=5
```

The six work records are exactly Moerdijk 1988, Forssell 2013,
Protin--Resende 2012, and local owners P9, P10, and P11. The two Forssell PDFs
are manifestations of one work and cannot become two bibliography entries.
Moerdijk remains in the six-work registry as an identity/metadata sentinel,
but is outside the five-work preflight-eligible set until lawful exact full
text, a PASS sidecar, and a claim-specific page locator are frozen by a fresh
gate.

## 2. Retained exact PDF manifestations

The `raw LF` column is the byte-level `wc -l` result for freeze purposes; it
is not a semantic page count. Page anchors are licensed only by the adjacent
ARS sidecars.

| Manifestation | Official/primary acquisition endpoint | SHA-256 | Bytes | Raw LF | ARS pages (`declared/enumerated/reader`) |
|---|---|---|---:|---:|---|
| Forssell, official TAC journal PDF | `https://tac.mta.ca/tac/volumes/28/18/28-18.pdf` | `40372e8c70873d294ecd8ac20bd507b1571eed86c1576e435a0685bfc6023366` | 345,934 | 2,671 | `12/12/12`, PASS, no warnings |
| Forssell, author arXiv v2 | `https://arxiv.org/pdf/1111.2952v2` | `4a121f741bb7204ad7ce6a937599a17b051c673b62d55bc51d785087f3339774` | 180,244 | 3,178 | `14/14/14`, PASS, no warnings |
| Protin--Resende, official EMS journal PDF | `https://ems.press/content/serial-article-files/30505` | `5a32faa1fea2cb07dc6794225f1ebe92b6a8bfbd5cae7d1c21d6df4b8a8d17ed` | 383,791 | 3,470 | `49/49/49`, PASS, no warnings |

### Same-stem ARS preflight sidecars

All three sidecars were generated from the unmodified ARS
`pdf_read_preflight.py` (`pdf_read_preflight/1.0.0`), script SHA-256
`b4239af423a18cce6c7473c880b8d125653c107919a31173a198b8dc8210827e`,
1,455 lines, 59,477 bytes.

| Sidecar | SHA-256 | Lines | Bytes | Verdict |
|---|---|---:|---:|---|
| `forssell-2013-subgroupoids-tac.preflight.json` | `06273f1a752fc8fd62673225d96096f20cbc6a0dc940ae6222cbeccfde17376f` | 12 | 434 | PASS; `12/12/12`; `warnings=[]` |
| `forssell-2013-subgroupoids-arxiv-1111.2952v2.preflight.json` | `20083976ca71cc4e33ed0ad1a84c1206cbcb01b809c8e4c257f445d4dbb15bac` | 12 | 448 | PASS; `14/14/14`; `warnings=[]` |
| `protin-resende-2012-quantales-ems.preflight.json` | `7cf17089919d761096a26dc4ffdb97b893aa98522774ab51c3024a529cb7f00e` | 12 | 437 | PASS; `49/49/49`; `warnings=[]` |

## 3. External work records and manifestation ceilings

### `moerdijk-1988-classifying-topos`

- Correct identity: Ieke Moerdijk, “The classifying topos of a continuous
  groupoid. I,” *Transactions of the American Mathematical Society* 310(2)
  (1988), 629--668.
- DOI: `10.1090/S0002-9947-1988-0973173-9`.
- Canonical AMS record:
  `https://www.ams.org/tran/1988-310-02/S0002-9947-1988-0973173-9/`.
- Registry metadata were confirmed through the DOI/Crossref record: author,
  title, venue, volume 310, issue 2, and pages 629--668 agree.
- Current exact-byte state: no lawful full-text manifestation was obtainable
  from the publisher, stable archive, author, or institutional path checked in
  this lane. No substitute, Paper II, search extract, or fabricated PDF was
  retained.
- Hard ceiling: identity/metadata sentinel only. It supplies no verified
  definition, theorem, quotation, or page anchor and is not eligible for a
  visible technical citation or bibliography seed in the next lane.

### `forssell-2013-subgroupoids`

- Correct identity: Henrik Forssell, “Subgroupoids and Quotient Theories,”
  *Theory and Applications of Categories* 28(18) (2013), 541--551.
- Official TAC DOI metadata: `10.70930/tac/jgiz1j78`.
- Official journal manifestation: the TAC PDF above. Physical pages 1--11 are
  printed pages 541--551; physical page 12 is the journal colophon.
- Author manifestation: arXiv `1111.2952v2`, revised 28 June 2013, 14 physical
  pages, described by arXiv as the short revised version accepted for
  publication.
- Exact framework locator in the TAC manifestation: Section 2.1 at printed
  pp. 542--543 / physical pp. 2--3. Printed p. 542 defines an open topological
  groupoid using open domain and codomain maps and sets up equivariant sheaves;
  printed p. 543 continues the Moerdijk-site construction. The final TAC
  typesetting labels the generating-object statement **Proposition 2.2**.
- Exact corresponding locator in arXiv v2: Section 2.1 at physical pp. 2--3;
  the same generating-object statement is **Proposition 2.1.1** on physical
  p. 3. This numbering difference is manifestation-specific and must not be
  collapsed.
- Hard ceiling: open-groupoid/equivariant-sheaf/Moerdijk-site framework only.
  Forssell does not receive credit for Paper 17's direct openness proof,
  classifying-topos equivalence, connected/discrete examples, quantale
  calculation, or Top-to-Locale point-loss inference.

### `protin-resende-2012-quantales`

- Correct identity: M. Clarence Protin and Pedro Resende, “Quantales of open
  groupoids,” *Journal of Noncommutative Geometry* 6(2) (2012), 199--247.
- DOI: `10.4171/JNCG/90`.
- Official article record:
  `https://ems.press/journals/jncg/articles/4489`.
- Exact official PDF mapping:
  - printed pp. 203--205 = physical pp. 5--7: locale/open-set notation,
    groupoid-quantale setup, and the distinction between the etale unital case
    and the open non-etale case, where the bare `O(G)` need not be unital;
  - printed pp. 214--215 = physical pp. 16--17: Theorem 2.41 and Theorem 2.45;
  - printed pp. 245--246 = physical pp. 47--48: the topological/localic warning,
    the frame-quotient comparison, and local compactness as a sufficient
    condition in the stated setting.
- Theorem 2.41 sends a quantal groupoid to a multiplicative semi-open quantal
  frame and preserves openness. Theorem 2.45 states the localic reconstruction
  isomorphisms for its registered localic domains; its proof is omitted in the
  source. These are not bare-topological-quantale reconstruction claims.
- Hard ceiling: cite only the displayed definitions, hypotheses, theorem
  statements, and local-compactness boundary. Keep bare `O(H)`, the comparison
  map `q_H`, and local compactness as distinct inputs. The source does not state
  Paper 17's `Top -> Loc` point-loss conclusion, and that conclusion may never
  be attributed to Protin--Resende.

## 4. Exact local owner registry

The owner files remain at their original locations; no duplicate was placed in
this source directory.

| Slug | Exact owner bytes | Registered locator | Role and negative ceiling |
|---|---|---|---|
| `paper9-actual-owner` | `papers/9-packet-separation/paper/manuscript.tex`; SHA-256 `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`; 752 lines; 61,831 bytes | lines 409--426 | TN-10 only: actual packet/orbit indiscreteness and literal set stabilizer/period boundary. No standard topology, new topos result, operator, trace, or global obstruction. |
| `paper10-separated-reflection-owner` | `papers/10-separated-reflection/paper/manuscript.tex`; SHA-256 `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315`; 602 lines; 61,214 bytes | claim ledger lines 132--135; P10-1--P10-4 theorem and scope-stop blocks, lines 201--306 | **TN-11 only**, “builds on” and prior-subtraction wording: separated universal images, continuous scalar observables, Borel/measurable maps on the stated target domain, and positive finite measures. No P10-5; no proxy, copied component, coordinate, spectral, operator, support, Radon/Haar/state/trace/determinant, Route, or Paper-17 theorem. |
| `paper11-range-first-owner` | `papers/11-indiscrete-convolution/paper/manuscript.tex`; SHA-256 `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`; 1,128 lines; 50,802 bytes | lines 255--277, 313--324, 337--405, 1079--1087 | TN-01/TN-08/TN-11 ownership only: range-first formulas, standard-circle owner, arrow-open/composable-pair facts, and the owner-splice stop. No transfer of standard topology or coordinates and no new Paper-17 topos/quantale/reconstruction credit. |

For future bibliographic metadata only, these local works identify Liang Wang
as author and carry the titles/dates frozen in their exact TeX bytes. This
manifest does not create BibTeX records or decide publication status.

## 5. Checksum and retention contract

- `paper17_sources.sha256` covers exactly the three retained PDFs and their
  three same-stem sidecars.
- The ledger intentionally does not hash itself, this manifest, `.gitignore`,
  or the separate citation audit.
- PDF copyright and redistribution permissions are not inferred here. All
  retained manifestations stay local-only even where an endpoint is openly
  accessible.
- Discovery pages, search snippets, abstracts, Crossref metadata, and the
  Moerdijk sentinel may establish identity but cannot support technical
  claim/page alignment.
- No additional etale-only Resende source, textbook, review, aggregator,
  Paper II surrogate, or convenience citation is included. A later source may
  be added only for a separately recorded claim need and a fresh exact-byte
  gate.

