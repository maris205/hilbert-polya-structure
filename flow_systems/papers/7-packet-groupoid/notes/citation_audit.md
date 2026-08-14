# Paper 7 independent citation, source-integrity, and release audit

Audit date: 2026-08-14 (Asia/Shanghai)  
Audit mode: independent ARS citation/integrity/formatting review of frozen bytes  
Manuscript status audited: review draft  
Decision: **REVISE (bibliographic/release metadata); technical claim--source alignment ACCEPT**

## 1. Frozen scope and decision

This audit did not modify the manuscript, bibliography, figures, source PDFs,
preflight sidecars, or release PDF.  It examined the following locked artifacts:

| Artifact | SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `ad14cc033eee56db804dd29e5e44a47fbeb56fac286cda775268d782813830fd` | exact lock matched |
| `paper/references.bib` | `25c8f9c95505c5a752ae2c1bfd7c18cc4811c33fac15a77fdb83bfbf2a0c5bf7` | exact lock matched |
| `paper/paper.pdf` | `77aeaf1c381528998ecd8da591e9630a57326c1ebbf9bc2ac56f956048e22365` | exact lock matched; 22 A4 pages |
| `paper/fig_owner_map.tex` | `684bb3e83de9f12c92651580797d72c0b528051549b80f8239dc083dfcde03f3` | native TikZ source |
| `paper/fig_ef_collapse.tex` | `fca764ba3ee291961c7b9c013544ea5751cc03f6ce8d4168fbd4ddfff9e86959` | native TikZ source |

The `REVISE` decision is not caused by an unsupported mathematical theorem,
an incorrect source locator, or a broken build.  It is caused by mandatory
bibliographic manifestation/DOI corrections and two release-documentation
gaps.  Once the mandatory items below are corrected and the bytes rebuilt and
relocked, the citation/source-integrity decision can become `ACCEPT` without a
new mathematical-source search.

## 2. Mandatory items before release

### M1. DOI completeness for two cited journal articles

The locked bibliography omits DOI and issue metadata from two published
journal manifestations whose DOI records resolve to the corresponding official
journal pages:

1. `Hiai1988`: add issue `1` and DOI
   `10.14492/hokmj/1381517791`.
2. `GuidoIsolaLapidus2009`: add issue `6` and DOI
   `10.1090/S0002-9947-08-04702-8`.

These omissions do not affect the verified local-PDF locators, but they fail
the release bibliography's DOI-completeness requirement.  Exact replacement
entries are supplied in Section 9.

### M2. Cited-manifestation metadata must match the local bytes

Two entries currently mix an original arXiv identifier with a later date or
fail to identify the actual local version used for locators.

1. `BenameurEtAl2006` uses `year = 2006` while presenting itself only as
   `arXiv:math/0512454`; the audited PDF is explicitly arXiv **v1, 20 December
   2005**.  The 2006 date belongs to the published book chapter, pp. 297--352,
   DOI `10.1142/9789812773609_0012`.  Use the published chapter metadata and
   state that all locators refer to arXiv v1, or cite the v1 preprint as a 2005
   item.  The exact replacement below takes the former route.
2. `Laugesen2009` omits the version although the audited PDF title page says
   **arXiv:0903.3845v2, 17 May 2017**, and the cited Definition 14.1 and Theorem
   23.5 are located in that v2 artifact.  Bind the entry to v2 and use the v2
   manifestation year/date.  Retaining the stable citation key is harmless.

### M3. Literal locator declaration and release-manifest coverage

The technical citation practice is sound, but two release claims are too broad
or too fragmented as currently written.

1. Lines 1269--1270 state that *every* source-dependent main-text claim names a
   theorem, equation, or section locator.  The bounded whole-text negative
   search of `Deninger2025Witt` and the positive-value contrast citation
   `FugledeKadison1952` are bare citations.  The former cannot honestly be
   reduced to one theorem locator; the latter can be.  Required resolution:
   add `Definition and Lemma 1, p. 521` (artifact PDF p. 2) to the
   Fuglede--Kadison citation and narrow the declaration, for example:

   > Every positive load-bearing source claim in the main text names a theorem,
   > equation, page, or section locator; bounded whole-text negative searches
   > are identified as such in the source audit.

2. The two files named as source manifests cover only 14 unique PDFs:
   `ownership_source_manifest.md` has four rows and
   `operator_source_manifest.md` has eleven rows, with Morishita duplicated.
   The fifteenth source, Connes--Consani v1, is accurately hashed and preflighted
   in `phase2_literature_search.md` Section 8, but is absent from the ownership
   manifest even though the operator manifest says Connes--Consani belongs to
   the ownership audit.  Before release, either add that row to the ownership
   manifest or publish one canonical 15-source union manifest.  This is a
   documentation-coverage defect, not a missing or unread source.

## 3. Recommended metadata and release improvements

### R1. Record known final manifestations without moving technical locators

These are recommendations because the locked entries accurately identify the
arXiv bytes actually read; the final publications are related manifestations
and byte/text identity was not assumed.

- `ConnesConsani2025`: record the final chapter in *Regulators V*,
  *Contemporary Mathematics* 842 (2026), 105--132, DOI
  `10.1090/conm/842/16852`, while retaining a note that equation locators refer
  to arXiv v1 (11 January 2025).  An exact replacement is in Section 9.
- `Deninger2023`: record that the survey was also published in Andrea
  Malchiodi (ed.), *Colloquium De Giorgi 2021 and 2022*, Scuola Normale
  Superiore, 2024, while retaining the arXiv-v1 theorem locator.  The final
  chapter page range was not used or inferred in this audit.
- `Bornemann2010`: issue `2` may be added for fuller journal metadata; the DOI,
  volume, year, and page range are already correct.

### R2. Public redistribution of the local source PDFs

The manuscript contains no copied third-party figure or long quotation; its
two figures are native TikZ diagrams.  However, a lawful retrieval endpoint is
not by itself proof of a right to redistribute a publisher PDF through a public
repository.  Before a public GitHub release, retain the URL/hash/locator
manifests but either (a) document the redistribution license for every retained
PDF, or (b) exclude PDFs without an explicit redistribution license.  The
Laugesen v2 artifact itself states CC BY-NC-ND 4.0; other artifacts require
their own terms check.  This is a packaging recommendation, not a conclusion
that any present local research use is unlawful.

### R3. Venue-specific declarations

The AI-use disclosure is substantive and names the actual assistance
categories, the human verification duty, and the absence of a claimed
cross-model review.  Ethics, contribution, competing-interest, funding, data,
and code statements are present.  No target venue was frozen, so compliance
with a venue's required AI wording, copyright-transfer language, data-policy
template, or declaration order remains unverified and should be checked at
submission time.

## 4. Citation graph and bibliography accounting

Deterministic parsing of the locked `manuscript.tex` and `references.bib`
gave:

- bibliography entries: 15;
- unique cited keys: 15;
- total cited-key occurrences: 24;
- undefined citation keys: 0;
- uncited/orphan bibliography entries: 0;
- duplicate bibliography keys: 0;
- BibTeX warnings in a clean build: 0.

| Key | Citation occurrences | Citation status | Metadata status |
|---|---:|---|---|
| `Deninger2026` | 6 | defined and cited | verified; final journal metadata and arXiv-v4 locator split explicit |
| `Deninger2023` | 2 | defined and cited | cited v1 exact; final 2024 volume cross-record recommended |
| `Deninger2025Witt` | 1 | defined and cited | verified arXiv v1; use is a bounded whole-text negative search |
| `Morishita2026` | 2 | defined and cited | verified arXiv v5, 21 January 2026 |
| `ConnesConsani2025` | 1 | defined and cited | v1 locator exact; 2026 final DOI cross-record recommended |
| `BagarelloTrapaniTriolo2006` | 1 | defined and cited | verified |
| `Hiai1988` | 1 | defined and cited | **mandatory DOI/issue completion** |
| `FackKosaki1986` | 1 | defined and cited | verified |
| `deLaHarpeSkandalis1984` | 1 | defined and cited | verified |
| `HochsKaadSchemaitat2018` | 3 | defined and cited | verified |
| `FugledeKadison1952` | 1 | defined and cited | verified; main-text pinpoint locator should be added |
| `Bornemann2010` | 1 | defined and cited | verified; issue number optional |
| `GuidoIsolaLapidus2009` | 1 | defined and cited | **mandatory DOI/issue completion** |
| `BenameurEtAl2006` | 1 | defined and cited | **mandatory arXiv-v1/final-chapter disambiguation** |
| `Laugesen2009` | 1 | defined and cited | **mandatory v2/date binding** |

## 5. Load-bearing claim--source alignment

Technical content was checked only against the locally retained primary full
texts whose hashes are listed in Section 7.  Later/final web records were used
only for bibliographic metadata.

| Main-text claim or boundary | Primary source and exact locator | Artifact location | Audit result |
|---|---|---|---|
| Prime packets, isotropy, unique packet membership, and least period `log p` | Deninger, Theorems 5.2 and 6.1 | PDF pp. 34 and 39 | supported; manuscript does not infer a trace from these topological results |
| Packet compactness and compact-group fibration | Deninger survey, Theorem 4.2 | PDF pp. 11--12 | supported; locators bind to arXiv v1 |
| Choice-dependent packet parametrizations and canonical projection boundary | Deninger, Section 5, equations (32), (35), (37)--(40) | PDF pp. 31--33 | supported; the manuscript correctly marks the coordinate choices |
| Deninger's distinct Haar convolution construction | Deninger, Section 11 | PDF pp. 66 ff. | supported negative comparison: it concerns a different inverse-limit group |
| No audited packet disintegration/operator/determinant theorem | Deninger v4, survey v1, and Witt-sheaf v1, bounded whole-text audit | 119 + 16 + 31 pages | acceptable as a scoped negative certificate, not a universal nonexistence theorem; declaration must distinguish whole-text negative searches |
| Direct-integral trace decomposition | Hiai, journal p. 118 and Lemma 2.1(1),(5) | PDF pp. 2, 5, and 7; scan order anomaly already recorded in manifest | supported; the concrete proof checks its own hypotheses |
| Assembly of a faithful normal semifinite trace | Bagarello--Trapani--Triolo, Theorem 2.1 | PDF pp. 3--4 | supported as context; manuscript supplies the concrete block proof |
| Generalized singular-number trace integral and `L^p` formula | Fack--Kosaki, Proposition 2.7 and Corollary 2.8 | PDF pp. 10--11 | supported |
| Bounded relative trace ideal and its Banach norm | Hochs--Kaad--Schemaitat, Sections 6.2--6.4 | PDF p. 12 | supported |
| Fourier convention and scaled Poisson summation | Laugesen, Definition 14.1 and Theorem 23.5 | PDF pp. 79 and 137 | supported; the cited artifact is v2 (2017), which the BibTeX must say |
| Quotient-valued determinant associated to a trace | de la Harpe--Skandalis, Definition and Proposition 2 | PDF pp. 6--7 | supported; manuscript does not misstate it as an automatic complex scalar |
| Positive semifinite Fuglede--Kadison determinant | Hochs--Kaad--Schemaitat, Definition 7.4 and Proposition 7.6 | PDF pp. 13--14 | supported; codomain and loss of phase are stated correctly |
| Original finite-factor determinant is positive-valued | Fuglede--Kadison, Definition and Lemma 1 | PDF p. 2 / journal p. 521 | supported; add this pinpoint to the bare citation |
| Ordinary Fredholm determinant has trace-class domain | Bornemann, Section 3, especially (3.1)--(3.5) | PDF pp. 9--10 (trace-class background on p. 7) | supported; used only as a contrast source |
| Breuer--Fredholm supplies a semifinite index | Benameur et al., Section 3, Definition 3.1 and Lemma 3.4 | PDF pp. 5--6 | supported; the manuscript's zero index for an invertible operator is its own immediate inference |
| Finite-trace-state analytic determinant may fail the product law | Guido--Isola--Lapidus, Remark 4.5 | PDF p. 13 | supported |
| Morishita uses the full character set and omits Deninger's refinement | Morishita v5, (2.1.5) and Remark 2.1.13 | PDF pp. 12--13 | supported |
| Printed full-Hom surjection and prime-circle proof do not close | Morishita v5, (2.2.7) and Theorem 3.6(2) | PDF pp. 16 and 25 | the manuscript correctly labels both counterchecks as its own derivations; it does not attribute the repair to Morishita |
| Continuity/equivariance of the root-of-unity map | Morishita v5, Lemmas 3.4--3.5 | PDF pp. 23--24 | supported |
| Finite-kernel repair and away-coordinate units | Deninger, equation (35), Section 7 | PDF p. 32 and the cited topology section | supported; the restricted theorem is plainly labelled new |
| Root-of-unity exponent image has at most one finite zero coordinate | Deninger, equations (62)--(68) | PDF pp. 48--49 | supported |
| Zero-coordinate set is a quotient invariant | Connes--Consani v1, equation (2) | PDF p. 10 | supported; the two-zero counterexample and strict non-surjectivity are the manuscript author's deductions |

No load-bearing claim was found to reverse a source implication, omit a
material source hypothesis, or present the manuscript's new calculation as a
source theorem.  In particular, the phrases “cannot hold as written,” “second,
independent gap,” and “new finite-kernel restriction” correctly separate the
printed Morishita statements from the Paper-7 repair.

## 6. Ownership of new results

The following are not claimed as consequences already proved in the cited
literature; they are visibly presented and proved as Paper-7 results:

- the concrete product-algebra faithful normal semifinite trace and its bounded
  `L^1` membership criterion;
- the component Poisson trace formula and global `sum m_p log p` boundary;
- the positive-time return measure and the trace/non-trace boundary;
- the relative-norm holomorphic zero-mode family and branch-fixed scalar;
- the frozen central-scalar trace-family classification and clock controls;
- the trivial-character counterexample to the printed full-Hom surjection;
- the away-coordinate repair, packetwise surjectivity, transverse collapse, and
  two-zero strict non-surjectivity certificate.

The manuscript consistently labels modeling choices (abstract Haar base,
decomposable proxy, masses, clocks, and branch) separately from source-owned
packet topology.  No source-ownership misattribution was found.

## 7. Primary artifacts, preflight sidecars, and exact hashes

All 15 PDFs have a same-stem JSON sidecar.  Independent recomputation found
that every sidecar says `PASS`, its embedded PDF hash equals the actual PDF,
declared/enumerated/reader page counts agree, and the warning array is empty.

| Primary PDF | Pages | PDF SHA-256 | Preflight sidecar SHA-256 |
|---|---:|---|---|
| `bagarello_trapani_triolo_2006_faithful_traces.pdf` | 7 | `6b856e6c8157eb391a870de83727634f8a0188d7cd1c3d53e255eea92f796a35` | `fee6947e62b6f1397a4e9b6ce913c38ececce48bbf771b5070d325a1b253a4cd` |
| `benameur_carey_et_al_2006_breuer_fredholm_spectral_flow.pdf` | 44 | `f23ea51962ac7f496ab3d7a28b6068fabfe2128d14c3126d373fe918608899a8` | `a36197c0fd2a473aaa16413e8f869c851620bf2b666c3786029e6d0b2f6dba59` |
| `bornemann_2010_fredholm_determinants.pdf` | 43 | `0652a97dcc57ec8727dbef4f60d14cb22c7b428b8551e3ecf67464803bde798a` | `762be61353a0e965ec1a12ffe7f81f7488a76b8842e7e953c0e923b971eb6bb5` |
| `connes_consani_2025_knots_primes_class_field_v1.pdf` | 30 | `f200c41d6d772389528bb1de58ad7fe98fd8db807d72360d4311ecb3c44d2fe5` | `fb83d21739951aa78ff72f9009fc5875b1e8df6c2e437165d4d222146f0f1c4b` |
| `de_la_harpe_skandalis_1984_determinant_trace.pdf` | 21 | `f61b5bbcbaed0a177e85b40e4aa14c033c16f42d6c483fbfe2b2bcb2175e10fd` | `5570b627bb3c36f92fa47ba9d15c8dde0464c74271d1702bd957fa26fda38654` |
| `deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `e1d48da27567747dd880666d881ddd211021800cdde99c195e5434b114e42626` |
| `deninger-primes-knots-periodic-orbits.pdf` | 16 | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | `74a0ccb32aa1f22ea3b93c3b9fc65b362c8072f4bc7d50526a8d10489a375ff6` |
| `deninger-rational-witt-vectors-associated-sheaves-v1.pdf` | 31 | `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002` | `810b5e253ab86b16e8197ae36efa5ef49889221b0202c94ec3fe2aeae562b75f` |
| `fack_kosaki_1986_generalized_s_numbers.pdf` | 35 | `3c11d3eba00268fd2222709b7ec24bf8adade4a7b3218fc8375aeec01e452503` | `7b2213335b932b7a915f8d973b12cad1e684062ac3c6bc657323dd1b1d5a4a35` |
| `fuglede_kadison_1952_determinant_finite_factors.pdf` | 11 | `403af865f539289bdf34a0d5294195d77c7ee6580f0940b5991f7125243b108e` | `6280b00dcee513f076122bea28891c6fb08085e2b7e4d65909d170b22f03dadd` |
| `guido_isola_lapidus_2009_analytic_determinant.pdf` | 30 | `a988508518f4f4ac0d7e04d91d4a88ba304221a37321fa7694c23ded30e07636` | `8b087d1ed534fef72143add485442918999c8b387dd73a72b716a91832f9a0cf` |
| `hiai_1988_spectral_relations_unitary_mixing.pdf` | 21 | `f50d9641d20cc3bab62dda6b728b5729acdf6bee15bc14c5db4cc11b50dba5f0` | `06877a3bacddbbcb4d50bbc39d9de61fdfd3f5e855730680ad89b98d83b573bb` |
| `hochs_kaad_schemaitat_2018_semifinite_fk.pdf` | 17 | `04fc2fc6b9748547505a98f4007dbeaaedbfe749d3d199cf3db84779ccc9743c` | `ef6bbf55464e0821ece2d663b4d18b0685ce5b522a2811ad32961aacec451f00` |
| `laugesen_2009_harmonic_analysis_notes.pdf` | 176 | `b1ef00490b91e492cd9906849256a172a0ea261f7d19fa6b6265ef425d78d51c` | `5ed524d75f4091180f397413be4cff65a89271a09fb4df9c1b75bb43802b1a1e` |
| `morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf` | 26 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `1ca5ab980f477868a0600a8b53c2d04ea2a10e9702973c92e6c8177b8277d75f` |

Related audit-document hashes at the time of this review:

| File | SHA-256 |
|---|---|
| `notes/sources/ownership_source_manifest.md` | `ca28c2d24223d7031ca9a5ae0e20c50cbb57ff8b13f8f897efa262b916f4df68` |
| `notes/sources/operator_source_manifest.md` | `b737593273b0ebf34e87875062cd339c43fda5e2184a13b65aab6a34ddc0bff4` |
| `notes/phase2_literature_search.md` | `fe8705ddd87d9d809b9ebd81f3d9f23d14d7488ed2dbf12a70f3a0ccbc82ade7` |

## 8. Build, PDF, formatting, and declarations

The locked TeX, BibTeX, and two figure sources were copied to a fresh temporary
directory and built with XeLaTeX/BibTeX followed by three XeLaTeX passes.

| Check | Result |
|---|---|
| Build completion | success; 22 pages, A4 |
| Undefined citations/references | 0 |
| Multiply defined labels | 0 |
| BibTeX warnings | 0 |
| LaTeX/package warnings | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 35; nonblocking typography notices |
| Missing-character/font warnings | 0 |
| Fonts | all fonts embedded and subset where applicable |
| Text extraction | successful for English and Chinese; release and clean rebuild have byte-identical `pdftotext -layout` output |
| Extracted-text SHA-256 | `2dcdd03ff979ebfcbc7a9fc10d4480690ee2c9f5eb78b98e24f4ba9fcf20d429` |
| Visual sample | pages 1, 8, 15, and 22 inspected; no clipping, collision, missing glyph, or broken hyperlink display observed |
| Encryption | none |

Some embedded TeX math Type-1 fonts do not expose a Unicode map, which is
normal for this toolchain; this did not prevent whole-document text extraction.
The rebuilt PDF is not expected to be byte-identical because of PDF metadata,
but its extracted text is identical to the release PDF.

The paper's research-integrity section contains data/code availability, ethics,
CRediT-style contribution, competing-interest, funding, AI-use, and
acknowledgment statements.  The AI system is not listed as an author, and human
responsibility is explicit.  The two displayed figures are manuscript-native,
so no third-party figure permission or caption credit is missing.

## 9. Exact BibTeX replacements

The following blocks preserve the existing citation keys, so no `manuscript.tex`
citation command needs to change.

### 9.1 Mandatory: `Hiai1988`

```bibtex
@article{Hiai1988,
  author  = {Hiai, Fumio},
  title   = {Spectral relations and unitary mixing in semifinite von {Neumann} algebras},
  journal = {Hokkaido Mathematical Journal},
  year    = {1988},
  volume  = {17},
  number  = {1},
  pages   = {117--137},
  doi     = {10.14492/hokmj/1381517791}
}
```

### 9.2 Mandatory: `GuidoIsolaLapidus2009`

```bibtex
@article{GuidoIsolaLapidus2009,
  author  = {Guido, Daniele and Isola, Tommaso and Lapidus, Michel L.},
  title   = {A trace on fractal graphs and the {Ihara} zeta function},
  journal = {Transactions of the American Mathematical Society},
  year    = {2009},
  volume  = {361},
  number  = {6},
  pages   = {3041--3070},
  doi     = {10.1090/S0002-9947-08-04702-8}
}
```

### 9.3 Mandatory: `BenameurEtAl2006`

```bibtex
@incollection{BenameurEtAl2006,
  author       = {Benameur, Moulay-Tahar and Carey, Alan L. and Phillips, John and Rennie, Adam and Sukochev, Fedor A. and Wojciechowski, Krzysztof P.},
  title        = {An analytic approach to spectral flow in von {Neumann} algebras},
  booktitle    = {Analysis, Geometry and Topology of Elliptic Operators},
  publisher    = {World Scientific},
  year         = {2006},
  pages        = {297--352},
  doi          = {10.1142/9789812773609_0012},
  eprint       = {math/0512454},
  archiveprefix= {arXiv},
  primaryclass = {math.OA},
  url          = {https://arxiv.org/abs/math/0512454v1},
  note         = {Section and page locators in this paper refer to arXiv version 1 (20 December 2005)}
}
```

### 9.4 Mandatory: `Laugesen2009`

```bibtex
@misc{Laugesen2009,
  author       = {Laugesen, Richard S.},
  title        = {Harmonic analysis lecture notes},
  year         = {2017},
  eprint       = {0903.3845},
  archiveprefix= {arXiv},
  primaryclass = {math.CA},
  howpublished = {arXiv:0903.3845v2},
  url          = {https://arxiv.org/abs/0903.3845v2},
  note         = {arXiv version 2, 17 May 2017}
}
```

### 9.5 Recommended: `ConnesConsani2025`

```bibtex
@incollection{ConnesConsani2025,
  author       = {Connes, Alain and Consani, Caterina},
  title        = {Knots, primes and class field theory},
  booktitle    = {Regulators V},
  series       = {Contemporary Mathematics},
  volume       = {842},
  publisher    = {American Mathematical Society},
  year         = {2026},
  pages        = {105--132},
  doi          = {10.1090/conm/842/16852},
  eprint       = {2501.06560},
  archiveprefix= {arXiv},
  primaryclass = {math.NT},
  url          = {https://arxiv.org/abs/2501.06560v1},
  note         = {Equation locators in this paper refer to arXiv version 1 (11 January 2025); byte or text identity with the final chapter is not assumed}
}
```

### 9.6 Recommended: `Deninger2023`

Because the exact technical source remains v1, the least conflating update is
to retain the preprint entry and cross-record the 2024 volume in the note:

```bibtex
@misc{Deninger2023,
  author       = {Deninger, Christopher},
  title        = {Primes, knots and periodic orbits},
  year         = {2023},
  eprint       = {2301.11643},
  archiveprefix= {arXiv},
  primaryclass = {math.NT},
  howpublished = {arXiv:2301.11643v1},
  url          = {https://arxiv.org/abs/2301.11643v1},
  note         = {Theorem locators in this paper refer to arXiv version 1 (27 January 2023); also published in Andrea Malchiodi (ed.), Colloquium De Giorgi 2021 and 2022, Scuola Normale Superiore, 2024}
}
```

## 10. Release gate

The frozen draft should not be labelled citation-release-final until all of the
following hold:

- replace the four mandatory BibTeX entries in Section 9;
- add the Fuglede--Kadison pinpoint and narrow the literal locator declaration;
- put Connes--Consani v1 into a named ownership/canonical 15-source manifest;
- rebuild, confirm no new warnings/undefined citations, and recompute the TeX,
  BibTeX, PDF, and amended-manifest hashes;
- decide whether source PDFs are private audit artifacts or publicly
  redistributable package contents.

Subject to those release corrections, this audit accepts the mathematical
claim--source alignment, the distinction between source results and new
derivations, the scoped wording of the two printed Morishita gaps, all 15 local
primary-source preflights, and the 22-page PDF build.

## 11. Closure addendum -- exact-byte re-lock

Closure date: 2026-08-14 (Asia/Shanghai)  
Final decision: **ACCEPT**  
Mandatory issues remaining: **0**

This addendum supersedes the decision and release gate in Sections 1 and 10
for the final candidate bytes below.  The original audit is retained as the
historical correction record; its pre-addendum SHA-256 was
`0426a898a2b7a052520f6a6e799abd639592bcd89f20ee0c2100e9bcf064ed93`.
No manuscript, bibliography, release PDF, source PDF, preflight sidecar, or
manifest was modified by this closure audit.

### 11.1 Final protected-artifact locks

| Artifact | Final SHA-256 | Closure result |
|---|---|---|
| `paper/manuscript.tex` | `5fd2f30d072b5c629a67c2be95b8fcc95a917e694f7e6be13a45f347f0e0c384` | exact lock matched |
| `paper/references.bib` | `68d96e5857dafd0594acd5d465637487c9281e06a178faed3e2998c231d3b48f` | exact lock matched |
| `paper/paper.pdf` | `4f0f9fbebf705e6b73c34fb66b01d4dda9d6ac37b7409f587bbefd8fecdcbd8d` | exact lock matched |
| `notes/sources/paper7_source_manifest.md` | `d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e` | exact lock matched |
| `paper/README.md` | `523e3d5bccf36054783e793eb2c6b35ea1dcc0b00d6e9d468cb0fee3ae6a15d0` | exact lock matched; release hashes agree |

The two native figure locks remain
`684bb3e83de9f12c92651580797d72c0b528051549b80f8239dc083dfcde03f3`
for `fig_owner_map.tex` and
`fca764ba3ee291961c7b9c013544ea5751cc03f6ce8d4168fbd4ddfff9e86959`
for `fig_ef_collapse.tex`.

### 11.2 Closure of mandatory and recommended items

- **M1 closed.** `Hiai1988` now records volume 17, issue 1, and DOI
  `10.14492/hokmj/1381517791`; `GuidoIsolaLapidus2009` records volume 361,
  issue 6, and DOI `10.1090/S0002-9947-08-04702-8`.
- **M2 closed.** `BenameurEtAl2006` separates the 2006 final book chapter
  (pp. 297--352, DOI `10.1142/9789812773609_0012`) from the arXiv-v1 bytes
  used for locators.  `Laugesen2009` is explicitly bound to arXiv v2,
  17 May 2017.
- **M3 closed.** The finite-factor contrast now cites Fuglede--Kadison,
  Definition and Lemma 1, journal p. 521.  The integrity declaration is
  narrowed to positive load-bearing claims and explicitly separates bounded
  whole-text negative searches.  The canonical manifest enumerates all 15
  locally read primary PDFs, including Connes--Consani v1.
- **R1 closed where bibliographic facts are fixed.** Connes--Consani records
  the 2026 final chapter while retaining its arXiv-v1 equation-locator note;
  the Deninger survey records the 2024 collected-volume manifestation while
  retaining its arXiv-v1 theorem locators.  Deninger's main article retains
  the verified final journal manifestation and arXiv-v4 formula-locator
  split, and Morishita remains explicitly bound to arXiv v5.  The final
  bibliography also records Fack--Kosaki as 123(2), Bagarello--Trapani--Triolo
  as 55(1), and Bornemann as 79(270).
- **Historical correction to R1.** The Section 3 suggestion that Bornemann's
  issue might be `2` is withdrawn.  The DOI metadata and final bibliography
  correctly give journal number **270**, not 2.
- **R2 closed as a release boundary.** The canonical manifest now states that
  lawful retrieval does not establish redistribution rights and requires a
  license check or exclusion of the PDF bytes before public distribution.
- **R3 remains venue-contingent and nonblocking.** The current declarations
  passed this integrity audit; any future target venue's exact wording and
  ordering remain a submission-stage check because no venue is frozen.

The corrections above change metadata and audit wording, not the ownership of
mathematical results.  The claim--source table in Section 5 remains valid:
load-bearing facts are attributed to primary sources at the stated theorem,
equation, section, or page locators, while the manuscript's packet trace,
proxy, zero-mode, and determinant consequences remain visibly marked as new
derivations, definitions, controls, or scoped negative conclusions.

### 11.3 Deterministic closure checks

- Citation graph: 24 cited-key occurrences, 15 unique cited keys, 15 unique
  BibTeX entries, zero undefined keys, zero uncited/orphan entries, and zero
  duplicate keys.
- Primary-source integrity: 15 PDFs, 15 same-stem preflight sidecars, and 15
  canonical-manifest rows.  Every sidecar says `PASS`; its embedded PDF hash
  matches the artifact; declared, enumerated, and reader page counts agree;
  warning arrays are empty; and both the PDF and sidecar hashes occur in the
  canonical manifest.
- Clean build: an isolated XeLaTeX--BibTeX--XeLaTeX x3 build completed with
  zero BibTeX warnings, zero undefined citations or references, zero LaTeX or
  package warnings, zero overfull boxes, zero missing-character diagnostics,
  and 35 nonblocking underfull boxes.
- Release equivalence: `pdftotext -layout` output from the clean build and the
  locked release PDF is byte-identical, with SHA-256
  `0fa1f50432c4d219aa84289f4c63f7938b890bf1b3a6c533eb8c9e562d719b34`.
  PDF byte identity across builds is not asserted because generated metadata
  may differ.
- PDF checks: 22 A4 pages, PDF 1.5, unencrypted, successfully extractable
  text, and 22 font records with every font embedded and subset.

Accordingly, the citation/source-integrity/release audit is closed at
**ACCEPT with zero mandatory items** for the exact final locks in Section
11.1.  Venue-specific house-style review is the only remaining advisory and
is not a defect in this release candidate.
