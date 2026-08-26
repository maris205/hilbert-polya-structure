# Paper 13 pre-manuscript citation and source audit

Audit date: **2026-08-15 (Asia/Shanghai)**

Pre-manuscript verdict: **PASS — C0 / M0 / m0 at the exact technical-note,
source, locator, and companion-manuscript ceilings below**

Publication ceiling: **EXPLICITLY LABELLED TECHNICAL NOTE ONLY;
STANDALONE_PASS=false; NOTE_OR_MERGE=true; the NOTE branch is selected**

Release verdict: **FAIL-CLOSED / NOT AUTHORIZED**

This is an independent pre-manuscript source and citation control document.
It binds the final composition blueprint, closes the metadata and locator
surface needed for a later technical-note draft, and supplies a literal
BibTeX seed.  It is not manuscript prose, an actual bibliography file, a
final citation audit, a declaration audit, a release audit, or permission for
Git or public synchronization.

## 1. Decision receipt and exact-byte evidence lock

The final upstream handoff was independently rehashed and read in full:

| Artifact | SHA-256 | Exact role |
|---|---|---|
| notes/composition_blueprint.md | af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd | frozen 884-line composition contract and source/citation gate |
| notes/proof_audit.md | e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63 | integrated 579-line proof, ownership, controls, Route, and NOTE ceiling |
| notes/phase2_framework_source_audit.md | b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592 | exact source hypotheses, locators, and named-framework boundaries |
| notes/phase2_convention_owner_audit.md | 498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52 | signs, regularity tiers, and source-owner translations |
| notes/phase2_novelty_search.md | 444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea | bounded precedent search; SUPPORTED_WITHIN_SEARCH only |
| notes/phase2_final_review.md | ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9 | Phase-2 PASS at its stated ceilings |
| notes/sources/framework_source_manifest.md | 4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e | retained manifestation and locator ledger |
| notes/sources/framework_sources.sha256 | 7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f | six PDFs plus six final sidecars |
| notes/route_audit.md | 2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9 | ten Route-A records: three exploratory, seven rejected |
| notes/phase3_v2_note_disposition_gate.md | b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e | PASS_TO_TECHNICAL_NOTE |
| notes/phase3_v2_standalone_review.md | ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e | C0/M1/m0; STANDALONE_PASS=false |

The stable proof and independent-review tuple was also read at its exact
owners:

| Proof or review | SHA-256 | Bound use |
|---|---|---|
| notes/phase3_core_twist_proofs.md | 62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd | P13-1 through P13-5 |
| notes/phase3_core_peer_review.md | a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665 | independent core PASS C0/M0/m0 |
| notes/phase3_support_retention_proofs.md | f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811 | P13-6 through P13-8 |
| notes/phase3_support_peer_review.md | ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed | independent support PASS C0/M0/m0 |
| notes/phase3_v2_corona_proofs.md | 81b0f8aaa1cf6277323452c55107cf33d8ad69783eb80998cc0f4f0d9d636858 | P13-8A through P13-8C |
| notes/phase3_v2_corona_peer_review.md | 0ae271fd99f3290d7d18486cfc98ad8ccf95aa1421619ccd4fdf72865deb28c8 | independent corona PASS C0/M0/m0 |
| notes/phase3_v2_controls_review.md | c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789 | effective replacement-control PASS |
| results/manifest.json | 26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2 | stable replacement-control receipt |

Machine-readable preflight state:

    P13_PRE_MANUSCRIPT_CITATION_AUDIT=PASS
    CITATION_FINDINGS=C0/M0/m0
    BOUND_BLUEPRINT_SHA256=af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd
    BOUND_PROOF_AUDIT_SHA256=e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63
    EXTERNAL_SEED_RECORD_COUNT=12
    COMPANION_SEED_RECORD_COUNT=5
    TOTAL_SEED_RECORD_COUNT=17
    P13_LEDGER_ITEMS_PASS=12/12
    P13_RETAINED_PDF_PREFLIGHT_PASS=6/6
    REUSED_PDF_PREFLIGHT_PASS=3/3
    NEW_SOURCE_PDF_COUNT=0
    SORKIN_FULLTEXT_AVAILABLE=false
    SORKIN_EVIDENCE_LEVEL=OFFICIAL_TITLE_ABSTRACT_ONLY
    AUSTAD_AMENABILITY_LOCATOR=PROPOSITION_2_4_PRINTED_PAGE_7
    KLEPPNER_CONTINUOUS_TRIVIALIZER_OWNER=false
    BHM_SECOND_COUNTABILITY_REQUIRED=false
    UNPROVED_V3_V4_CARTAN_SOURCE_COUNT=0
    NOVELTY_CEILING=SUPPORTED_WITHIN_SEARCH
    STANDALONE_PASS=false
    NOTE_OR_MERGE=true
    NOTE_BRANCH_SELECTED=true
    TECHNICAL_NOTE_LABEL_REQUIRED=true
    BIBTEX_SEED_READY=true
    ACTUAL_BIBLIOGRAPHY_FILE_CREATED=false
    MANUSCRIPT_AUTHORIZED_BY_THIS_AUDIT=false
    FIGURE_ASSET_AUTHORIZED_BY_THIS_AUDIT=false
    RELEASE_AUTHORIZED=false
    GIT_AUTHORIZED=false
    PUBLIC_SYNC_AUTHORIZED=false

## 2. Retained manifestations and PDF-read preflight

The Paper-13 checksum ledger was rerun from its source directory and all
twelve entries returned OK.  The six exact Paper-13 source PDFs and their
same-stem sidecars are:

| ID | PDF SHA-256 | Pages | Sidecar SHA-256 | Final preflight |
|---|---|---:|---|---|
| FW-AO20-v1 | c4b7b1cb7e225e3873b1071deb844b047ba0f1404aac4ca97002862aec2682c7 | 13 | f48bbf527341557458f970163c12f309c56224ec9fe212a2f0b4ea507d93ebe8 | PASS; 13=13=13; warnings 0 |
| SRC-AUSTAD21 | 9edaf338a3d1f2f1b503a3709f20fceaa2bf1a6624a8d6fce0d80f3f15c77bc3 | 22 | 00d34a9fb17f2bcb5e00192f4ed4c3f9fd35848b6c12783023b0f877eb5b752e | PASS; 22=22=22; warnings 0 |
| SRC-HUL66 | eacf80abfbd7dc7320b4130ff2a2028d98cbd89b48bcf8ee62562d3e79f64f4a | 10 spread images | 0cb8bad6a64a131656bbb7b392c08554056a8e61fa3443cfd47093951c13aea6 | PASS; 10=10=10; warnings 0 |
| SRC-HUL64 | a30bcf1bda9699b56f1a846f15bc46f0ce420fb42f114fdc22d564d0a6f321fa | 12 spread images | 029aa3aff02517d95fea74f72f7b1d26c5cbeb5e7df4922d6aff6384e9d8bff6 | PASS; 12=12=12; warnings 0 |
| SRC-KLEP65 | 75f9f5e62e47e8c9dc885a5eba74ccbdfaefa296c02b1fcc5de8fbcf9dd51264 | 73 issue pages | 2eda422adce992695f0a2c4ea1b68ab821ee9a34790d32fc96c16689c38dc1f0 | PASS; 73=73=73; warnings 0 |
| SRC-LEPTIN68 | 0bde30eba4eb8cee42bed5285e32272994090d04fc8880f841799ed75c96039c | 25 | 7e29d6f893f7a6ea3674c7295f221637c339cfc0c86b70e8a7e3c815554bfb39 | PASS; 25=25=25; warnings 0 |

Three already-preflighted Paper-11 manifestations are reused in place.  They
were not copied:

| ID | PDF SHA-256 | Pages | Sidecar SHA-256 | Final preflight |
|---|---|---:|---|---|
| REUSE-TU04 | ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897 | 34 | e82c95d4c3fd668d43c324db0631216372cc67505234a73e2ddc9ebf875884af | PASS; 34=34=34; warnings 0 |
| REUSE-BHM18-v2 | 8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6 | 30 | c288efb2dca89ca8fd47bd9371decb7d042853dd6b60b35897df2f70214bfb59 | PASS; 30=30=30; warnings 0 |
| REUSE-WIL07-d3.1 | 3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2 | 540 | 80a77e556a133a33f2db2667e79bac8219fc7babfba1487aec93f54e5d01c86c | PASS; 540=540=540; warnings 0 |

The reused Paper-11 source manifest is
SHA-256 b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f.

No Sorkin PDF exists in the audited corpus.  No Packer--Raeburn or Stacks PDF
was retained.  This preflight fetched and retained **zero** new PDFs.  A
publisher abstract, HTML page, or metadata response was not converted into a
surrogate PDF.

Local PDF paths, checksums, and preflight sidecars are internal
reproducibility locators.  They are not public scholarly identities and must
not enter a public bibliography.

## 3. Exact external metadata and manifestation rules

Current publisher, DOI-registry, arXiv, author, and stable-tag records were
checked on 2026-08-15.  The exact twelve-record external tuple is:

| Key | Exact bibliographic identity | Canonical public endpoint and metadata rule |
|---|---|---|
| Sorkin1978Triviality | Rafael Sorkin, “The triviality of continuous multipliers for the real line,” International Journal of Theoretical Physics 17(5) (1978), 369--376 | Springer record and DOI 10.1007/BF00674107.  Current Springer/Crossref metadata supplies no middle initial, so none is inserted. |
| Austad2021Spectral | Are Austad, “Spectral Invariance of *-Representations of Twisted Convolution Algebras with Applications in Gabor Analysis,” Journal of Fourier Analysis and Applications 27(3) (2021), article 56 | Springer record and DOI 10.1007/s00041-021-09860-z.  “56” is an article number, not a page. |
| Leptin1968Darstellungen | H. Leptin, “Darstellungen verallgemeinerter L1-Algebren,” Inventiones Mathematicae 5(3) (1968), 192--215 | Springer record and DOI 10.1007/BF01425550.  The literal publisher metadata uses H. Leptin; the retained manifest's Horst expansion is an authority-record enhancement. |
| Hulanicki1964WeakContainment | A. Hulanicki, “Groups whose regular representation weakly contains all unitary representations,” Studia Mathematica 24(1) (1964), officially registered 27--59 | IMPAN record and DOI 10.4064/sm-24-1-27-59.  The official downloadable scan visibly starts at printed p. 37 and ends at p. 59.  Preserve the registry pagination bibliographically and disclose the scan anomaly. |
| Hulanicki1966Folner | A. Hulanicki, “Means and Følner condition on locally compact groups,” Studia Mathematica 27(2) (1966), 87--104 | IMPAN record and DOI 10.4064/sm-27-2-87-104. |
| Kleppner1965Multipliers | Adam Kleppner, “Multipliers on Abelian groups,” Mathematische Annalen 158(1) (1965), 11--34 | Springer record and DOI 10.1007/BF01370393. |
| PackerRaeburn1989Twisted | Judith A. Packer and Iain Raeburn, “Twisted crossed products of C*-algebras,” Mathematical Proceedings of the Cambridge Philosophical Society 106(2) (1989), 293--311 | Cambridge record and DOI 10.1017/S0305004100078129.  Cambridge's 2011 online date is digitization, not the bibliographic year. |
| BussHolkarMeyer2018Universal | Alcides Buss, Rohit D. Holkar, and Ralf Meyer, “A universal property for groupoid C*-algebras. I,” Proceedings of the London Mathematical Society (3) 117(2) (2018), 345--375 | Wiley DOI 10.1112/plms.12131; technical locators refer to final accepted arXiv 1612.04963v2, 7 February 2018. |
| Williams2007CrossedProducts | Dana P. Williams, Crossed Products of C*-Algebras, Mathematical Surveys and Monographs 134, AMS, 2007 | AMS DOI 10.1090/surv/134 and ISBN 978-0-8218-4242-3; technical locators refer to the author's Version 3.1 draft of 6 September 2006. |
| AustadOrtega2022Uniqueness | Are Austad and Eduard Ortega, “C*-uniqueness Results for Groupoids,” International Mathematics Research Notices 2022(4) (2022), 3057--3073 | OUP DOI 10.1093/imrn/rnaa225; locators refer to arXiv 2005.06208v1, 13 May 2020.  The 2020 online-publication date does not replace the 2022 issue year. |
| Tu2004NonHausdorff | Jean-Louis Tu, “Non-Hausdorff groupoids, proper actions and K-theory,” Documenta Mathematica 9 (2004), 565--597 | EMS DOI 10.4171/DM/178; there is no issue number. |
| Stacks0B1W | The Stacks Project Authors, “The Stacks Project, Section 5.29 (Tag 0B1W): Colimits of spaces” | Stable URL https://stacks.math.columbia.edu/tag/0B1W, accessed 15 August 2026.  The current official title is “Colimits of spaces,” not the legacy seed wording “Topological colimits.”  Do not manufacture a DOI, journal, volume, pages, or fixed numeric publication year. |

Canonical public records:

- Sorkin: https://link.springer.com/article/10.1007/BF00674107
- Austad: https://link.springer.com/article/10.1007/s00041-021-09860-z
- Leptin: https://link.springer.com/article/10.1007/BF01425550
- Hulanicki 1964: https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/studia-mathematica/all/24/1/95703/groups-whose-regular-representation-weakly-contains-all-unitary-representations
- Hulanicki 1966: https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/27/2/96164/means-and-folner-condition-on-locally-compact-groups
- Kleppner: https://link.springer.com/article/10.1007/BF01370393
- Packer--Raeburn: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/twisted-crossed-products-of-calgebras/79B8947245C46351F7F003D7F3BFBC39
- Buss--Holkar--Meyer: https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms.12131 and https://arxiv.org/abs/1612.04963v2
- Williams: https://bookstore.ams.org/SURV/134 and https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf
- Austad--Ortega: https://academic.oup.com/imrn/article/2022/4/3057/5901311 and https://arxiv.org/abs/2005.06208v1
- Tu: https://ems.press/journals/dm/articles/8965109
- Stacks: https://stacks.math.columbia.edu/tag/0B1W

## 4. Literal 17-record BibTeX seed

This block is the mechanically consumable preflight tuple: twelve external
records plus five honest unpublished companion records.  It is not an actual
references.bib file and does not authorize one.  A venue conversion may
change formatting fields, but not identities, dates, DOI strings, versions,
unpublished status, or companion URL absence.

Every record has a planned deployment in Section 6 below.  If a later draft
does not cite a record, that record must be removed before bibliography
freeze; uncited prestige padding is forbidden.

~~~bibtex
@article{Sorkin1978Triviality,
  author  = {Rafael Sorkin},
  title   = {The triviality of continuous multipliers for the real line},
  journal = {International Journal of Theoretical Physics},
  year    = {1978},
  volume  = {17},
  number  = {5},
  pages   = {369--376},
  doi     = {10.1007/BF00674107}
}

@article{Austad2021Spectral,
  author  = {Are Austad},
  title   = {Spectral Invariance of {$*$}-Representations of Twisted Convolution Algebras with Applications in Gabor Analysis},
  journal = {Journal of Fourier Analysis and Applications},
  year    = {2021},
  volume  = {27},
  number  = {3},
  doi     = {10.1007/s00041-021-09860-z},
  note    = {Article 56}
}

@article{Leptin1968Darstellungen,
  author  = {H. Leptin},
  title   = {Darstellungen verallgemeinerter {$L^1$}-Algebren},
  journal = {Inventiones Mathematicae},
  year    = {1968},
  volume  = {5},
  number  = {3},
  pages   = {192--215},
  doi     = {10.1007/BF01425550}
}

@article{Hulanicki1964WeakContainment,
  author  = {A. Hulanicki},
  title   = {Groups whose regular representation weakly contains all unitary representations},
  journal = {Studia Mathematica},
  year    = {1964},
  volume  = {24},
  number  = {1},
  pages   = {27--59},
  doi     = {10.4064/sm-24-1-27-59},
  note    = {The official registry gives pages 27--59; the official article scan visibly begins at printed page 37}
}

@article{Hulanicki1966Folner,
  author  = {A. Hulanicki},
  title   = {Means and {F{\"o}lner} condition on locally compact groups},
  journal = {Studia Mathematica},
  year    = {1966},
  volume  = {27},
  number  = {2},
  pages   = {87--104},
  doi     = {10.4064/sm-27-2-87-104}
}

@article{Kleppner1965Multipliers,
  author  = {Adam Kleppner},
  title   = {Multipliers on Abelian groups},
  journal = {Mathematische Annalen},
  year    = {1965},
  volume  = {158},
  number  = {1},
  pages   = {11--34},
  doi     = {10.1007/BF01370393}
}

@article{PackerRaeburn1989Twisted,
  author  = {Judith A. Packer and Iain Raeburn},
  title   = {Twisted crossed products of {$C^*$}-algebras},
  journal = {Mathematical Proceedings of the Cambridge Philosophical Society},
  year    = {1989},
  volume  = {106},
  number  = {2},
  pages   = {293--311},
  doi     = {10.1017/S0305004100078129}
}

@article{BussHolkarMeyer2018Universal,
  author        = {Alcides Buss and Rohit D. Holkar and Ralf Meyer},
  title         = {A universal property for groupoid {$C^*$}-algebras. I},
  journal       = {Proceedings of the London Mathematical Society},
  series        = {3},
  year          = {2018},
  volume        = {117},
  number        = {2},
  pages         = {345--375},
  doi           = {10.1112/plms.12131},
  eprint        = {1612.04963},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/1612.04963v2},
  note          = {Technical locators refer to the final accepted arXiv version 2, 7 February 2018}
}

@book{Williams2007CrossedProducts,
  author    = {Dana P. Williams},
  title     = {Crossed Products of {$C^*$}-Algebras},
  series    = {Mathematical Surveys and Monographs},
  volume    = {134},
  publisher = {American Mathematical Society},
  address   = {Providence, RI},
  year      = {2007},
  doi       = {10.1090/surv/134},
  isbn      = {978-0-8218-4242-3},
  url       = {https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf},
  note      = {Published monograph; technical locators refer to author manuscript Version 3.1, 6 September 2006}
}

@article{AustadOrtega2022Uniqueness,
  author        = {Are Austad and Eduard Ortega},
  title         = {{$C^*$}-uniqueness Results for Groupoids},
  journal       = {International Mathematics Research Notices},
  year          = {2022},
  volume        = {2022},
  number        = {4},
  pages         = {3057--3073},
  doi           = {10.1093/imrn/rnaa225},
  eprint        = {2005.06208},
  archivePrefix = {arXiv},
  primaryClass  = {math.OA},
  url           = {https://arxiv.org/abs/2005.06208v1},
  note          = {Technical locators refer to arXiv version 1, 13 May 2020}
}

@article{Tu2004NonHausdorff,
  author  = {Jean-Louis Tu},
  title   = {Non-Hausdorff groupoids, proper actions and {$K$}-theory},
  journal = {Documenta Mathematica},
  year    = {2004},
  volume  = {9},
  pages   = {565--597},
  doi     = {10.4171/DM/178}
}

@misc{Stacks0B1W,
  author = {{The Stacks Project Authors}},
  title  = {The Stacks Project, Section 5.29 (Tag 0B1W): Colimits of spaces},
  url    = {https://stacks.math.columbia.edu/tag/0B1W},
  note   = {Tag 0B1W; accessed 15 August 2026}
}

@unpublished{Wang2026ArithmeticPeriodPackets,
  author = {Liang Wang},
  title  = {Arithmetic Period Packets and the Missing Trace: A Source-Locked Zeta Audit of Deninger's Rational-Witt Flow},
  year   = {2026},
  note   = {Companion manuscript, 13 August 2026}
}

@unpublished{Wang2026IsotropyAveraging,
  author = {Liang Wang},
  title  = {Isotropy Averaging Erases Returns: Character Traces and a Fixed-Map Normality Obstruction on Deninger Prime Orbits},
  year   = {2026},
  note   = {Companion manuscript, 14 August 2026}
}

@unpublished{Wang2026PacketSeparation,
  author = {Liang Wang},
  title  = {Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous Approximation and a Topological Corrigendum},
  year   = {2026},
  note   = {Companion manuscript, 14 August 2026}
}

@unpublished{Wang2026ContinuousConvolution,
  author = {Liang Wang},
  title  = {Continuous Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids},
  year   = {2026},
  note   = {Companion manuscript, 15 August 2026}
}

@unpublished{Wang2026MarkedTime,
  author = {Liang Wang},
  title  = {Marked Time Cohomology and Orbitwise Standardization of Indiscrete Arithmetic Action Groupoids},
  year   = {2026},
  note   = {Companion manuscript, 15 August 2026}
}
~~~

No local path, checksum, mutable branch URL, repository status, acceptance
status, or invented DOI appears in the five companion records.  If an
immutable public identity later exists, it may replace the unpublished record
only after exact-byte and metadata audit.

## 5. Technical locators and claim ceilings

### 5.1 Continuous real-line multiplier sentinel

**Sorkin.**  The official Springer title, abstract, volume, issue, pages, and
DOI were confirmed.  The accessible record is subscription-only and no
lawful author or repository full text was located in the bounded audit.
Evidence status is:

    UNAVAILABLE_FULLTEXT / OFFICIAL_TITLE_ABSTRACT_ONLY

The abstract advertises continuous remultiplication of every continuous
group multiplier on the usual real line to the identity.  This supplies
mandatory prior credit and an existence-level sentinel.  It supplies no
Paper-13 normalization, sign, quotient orientation, proof step, page
locator, actual-owner transfer, twisted product, or completion statement.
P13-3 remains a direct author proof at the frozen convention.

### 5.2 Twisted group formulas and the amenability endpoint

**Austad.**

- Physical/published p. 5, Definitions 2.1--2.2 and equations (2.1)--(2.2):
  strongly continuous projective representation and continuous normalized
  circle-valued cocycle.
- Physical/published p. 6: twisted left regular representation, convolution,
  and involution.
- Physical/published p. 7: integrated form and **Proposition 2.4**.
  Proposition 2.4 says that for an amenable locally compact group and a
  continuous cocycle, the twisted regular norm is the maximal norm; the text
  identifies this as a special case of Leptin, Satz 6.

The canonical downstream locator is **Proposition 2.4, printed p. 7**.
Every legacy neighboring-number reference is superseded and must not enter
the manuscript.

**Leptin.**  Physical p. 14 / printed p. 204, Satz 6 is the generalized
L1-algebra endpoint cited by Austad.  Leptin's setting permits measurable
factor systems.  It is used through Austad's continuous specialization and
never as a continuous-gauge or Paper-13-sign source.

**Hulanicki 1966.**  Physical p. 1 / printed p. 87 and physical p. 2 /
printed p. 88 place Abelian groups in the invariant-mean class.  This
supports the usual group's amenability context for the usual real line, not
amenability of an actual action-groupoid owner.

**Hulanicki 1964.**  Physical scan p. 11 / visible printed pp. 56--57 and
physical scan p. 12 / printed p. 58 supply weak-containment and
invariant-mean context.  They do not supply the exact twisted equality or an
actual-groupoid completion.  Bibliographic pages remain the official
27--59, with the visible-scan 37--59 anomaly expressly disclosed.

### 5.3 Borel background and generic twisted precedent

**Kleppner.**  Physical issue p. 31 / article printed p. 28, Section 7
defines a Borel multiplier and Borel similarity cochain.  The operative tier
is BOREL/BOREL.  Kleppner may support one historical terminology sentence
and the regularity firewall; it may not support a continuous trivializer.

**Packer--Raeburn.**  The Cambridge publisher extract verifies the generic
locally compact-group twisted-action and twisted-crossed-product scope.
No uninspected theorem, sign, or actual-owner transfer is load-bearing.
Use it for prior positioning only, never to imply Paper-13 novelty.

### 5.4 Ordinary component bridge

**Buss--Holkar--Meyer.**

- Physical pp. 1--2 state the locally compact Hausdorff groupoid with Haar
  system and explain that the construction as written is Hausdorff-only.
- Corollary 6.2, physical/published p. 21 removes the second-countability
  dependence for the relevant representation boundedness result.
- Theorem 7.1, physical/published p. 23 identifies the ordinary
  transformation-groupoid full algebra with the ordinary crossed product.

BHM **does not require second countability** at this use.  It supplies an
untwisted Hausdorff component bridge and a framework firewall.  It supplies
no twisted actual non-Hausdorff record.

**Williams, author manuscript Version 3.1.**

- Lemma 2.27 and Remarks 2.29--2.30, printed pp. 52--53: the ordinary
  universal crossed-product completion and dense test algebra.
- Proposition 2.34, printed pp. 54--55: canonical coefficient and
  group-valued multiplier maps.  Injectivity of the group-valued map alone
  does not establish faithfulness of an integrated group C-star map.
- Equation (4.63) and Theorem 4.30, printed p. 138 / physical p. 150:
  the homogeneous-space component model, only after the audited
  sign/measure conversion and only up to component isomorphism.
- Definition 7.7 and Examples 7.9 and 7.11, printed pp. 198--199, and
  Theorem 7.13, printed p. 199 / physical p. 211: regular norm and
  full/reduced equality for an action of an amenable group.

These locators support ordinary components and the amenable action endpoint.
They do not select common origins, identify whole maximal and reduced
component algebras, or name a global actual twisted groupoid algebra.

### 5.5 Named framework comparators

**Austad--Ortega.**  The locator manifestation is arXiv 2005.06208v1.
Physical pp. 1 and 3 fix second-countable, locally compact Hausdorff,
**étale** groupoids with continuous cocycle.  This is a named-framework
comparator only.  It does not apply to the actual non-Hausdorff owner and
does not apply to the nondiscrete one-object group R, whose source map to a
point is not a local homeomorphism.

**Tu.**

- Physical p. 3 / printed p. 567, Definition 1.1: Tu's local compactness
  convention uses compact neighborhoods and hence local Hausdorffness.
- Physical p. 17 / printed p. 581: the Hausdorff-open zero-extension span
  convention for C-c functions.
- Physical p. 19 / printed p. 583, Definition 4.6: Haar-system domain.

Tu permits globally non-Hausdorff objects within a locally Hausdorff
framework.  It does not admit the nowhere locally Hausdorff actual owner
with at least two units.

**Stacks Tag 0B1W.**  Section 5.29 and Lemma 5.29.1 support arbitrary
set-indexed topological coproducts and their componentwise topology.  They
supply no action continuity, component completion, cardinality, actual
topology, or Paper-13 theorem.  The current title “Colimits of spaces” is
the title frozen in the seed.

Correct framework sentence:

> For an actual owner with at least two units, the named audited Hausdorff
> Haar-groupoid, Hausdorff étale, and locally Hausdorff frameworks do not
> apply.

Do not replace that sentence by “no framework exists.”

## 6. Claim-to-citation and placement plan

The English and Simplified-Chinese abstracts contain no citation commands
under the blueprint.  Their factual prior/companion subtraction must be
cited at the first corresponding introduction/body occurrence.

| Claim surface | Required record and locator | Planned placement | Nonpromotion ceiling |
|---|---|---|---|
| advertised continuous real-line collapse | Sorkin official title/abstract only | Introduction and immediately before P13-3 | prior credit; P13 owns only its direct sign-exact proof |
| continuous normalized cocycle and time-group formulas | Austad pp. 5--6 | conventions and P13-4 | usual time group only |
| amenable twisted norm endpoint | Austad Proposition 2.4, printed p. 7, citing Leptin Satz 6, printed p. 204 | P13-5 max/r argument | identify the author transport with the time owner before using the endpoint |
| amenability and weak-containment context | Hulanicki 1966 pp. 87--88 and Hulanicki 1964 visible pp. 56--58 | one source/limitations paragraph around P13-5 | contextual group result, not exact twisted actual completion |
| Borel multiplier terminology | Kleppner Section 7, printed p. 28 | conventions/source-ceiling paragraph | Borel/Borel only; never continuous trivializer |
| generic twisted crossed-product precedent | Packer--Raeburn publisher-level scope | Introduction prior subtraction | no theorem/sign import and no novelty implication |
| ordinary Hausdorff component bridge | BHM Corollary 6.2 p. 21 and Theorem 7.1 p. 23 | framework dictionary and Section 5 | no second-countability obstruction; no twisted actual record |
| ordinary component norms and amenability | Williams locators in Section 5.4 above | Section 5 component isometries | group-valued injectivity is not C-star faithfulness |
| Hausdorff étale comparator | Austad--Ortega arXiv v1 pp. 1 and 3 | owners/source ceilings and limitations | comparator only |
| locally Hausdorff comparator | Tu Definition 1.1 and Section 4 locators | owners/source ceilings and limitations | comparator only |
| arbitrary coproduct topology | Stacks Tag 0B1W, Section 5.29 and Lemma 5.29.1 | fixed-prime standard/discrete context | set-index topology only |
| continuum lower bound | Paper 2 Proposition prop:uncountable | Introduction subtraction and P13-8A context | Paper 2 owns the hard lower bound; P13 owns only elementary upper closure |
| one-orbit proxy, traces/returns, scalar ledger | Paper 8 exact manuscript | Introduction subtraction and limitations | no Paper-13 trace/return ownership |
| actual packet/topology/stabilizer/period and bare quotient | Paper 9 cor:packet and cor:orbit | Introduction, fixed-prime setup, limitations | no standard topology or twist imported |
| actual time-only collapse and untwisted author records | Paper 11 thm:qc, thm:phi, thm:star-algebra, thm:regular, thm:completions | Introduction and P13-4/5/8 premises | untwisted baseline only |
| all-degree factorization, standardization, components, J | Paper 12 thm:factorization, def:std, thm:std-topology, cor:packet-comparison | Introduction and P13-1/2/8/8B premises | no actual-to-standard topology transfer |
| generic constant-diagonal lemma | direct P13 proof | state generic lemma before packet instantiation | no external source is needed merely for prestige; no owner-specific obstruction |
| finite controls and Route | frozen internal manifest/reviews, not scholarly source substitution | controls/limitations section | diagnostics only; all A2--A4 fail; Route B false |

The source set is closed against orphan inflation.  Gillaspy, Omland,
Sims--Williams, Cattaneo, Exel v3, Muhly--Williams, and generic textbooks
are not added merely because they appeared in discovery or neighboring
corpora.  No Deninger v3/v4 or Cartan source is added.  In particular,
Kleppner's bibliography does not authorize importing its Cartan reference
into Paper 13.

## 7. Exact companion identities, bytes, and ownership subtraction

The five companion records were independently rehashed at their current
exact bytes:

| Companion | Manuscript SHA-256 | Proof-audit SHA-256 | PDF SHA-256 | References SHA-256 |
|---|---|---|---|---|
| Paper 2 | 72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc | aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae | 86a60810f1f2a975bc5e694cb854a7de4bb796168f9a273888c013f84323a183 | cdeab58c00d1129612c444a712485aa8163b3411d0527ca58cd5f6047c38d1a3 |
| Paper 8 | c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa | 1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990 | fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a | a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e |
| Paper 9 | 24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb | c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8 | c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02 | 0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35 |
| Paper 11 | eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002 | 03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28 | 15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d | 33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877 |
| Paper 12 | c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163 | c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab | 3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294 | e1f4d0f6589ce0710173bad1c0089b5d6746d09010cc448d6d387ad8c9e17dcf |

Exact inherited premises and ceilings:

- **Paper 2:** Proposition prop:uncountable, manuscript lines 391--436,
  owns the sign-subgroup/procyclic continuum lower bound.  Lines 438--442
  explicitly withhold topology.  P13-8A owns only the elementary upper bound
  and equality closure.
- **Paper 8:** owns the selected one-orbit standard-circle proxy,
  unstabilized C(T)-tensor-K completion, character trace/return formula,
  regular FNS trace, local/packet firewall, and positive-time scalar ledger.
  Paper 13 defines no trace or return amplitude.
- **Paper 9:** cor:packet at lines 409--415 and cor:orbit at lines 421--427
  own the actual nontrivial indiscrete packet/orbits, stabilizer p^Z, period
  log p, and the bare carrier U_p/H_p.  No twist or standard topology is
  imported.
- **Paper 11:** thm:qc at line 360, thm:phi at line 466,
  thm:star-algebra at line 524, thm:regular at line 598, and
  thm:completions at line 681 own actual support, time-only collapse, and
  untwisted author test/full/reduced records.  Paper 13 must prove every
  twisted identity.
- **Paper 12:** thm:factorization at line 437, def:std at line 671,
  thm:std-topology at line 688, and cor:packet-comparison at line 1062 own
  all-degree factorization, same-carrier standardization, compact-open
  components, the continuous direction J from standard to actual, and the
  fixed-prime comparison.  No actual topology, count, measure, or twist is
  transferred.

Current public-identity state is intentionally conservative.  The five
records remain unpublished companion manuscripts with no URL in the seed.
Local hashes above are audit bindings, not BibTeX fields.  Before public
release, each load-bearing companion must either:

1. receive an honest immutable public record for the exact cited bytes; or
2. remain under an explicitly approved and venue-compatible
   companion-manuscript policy that does not invent availability,
   acceptance, or permanence.

This unresolved release choice is not a pre-manuscript metadata blocker
because the seed states the current unpublished status truthfully.  It is a
hard public-release stop.

## 8. Technical-note ownership and novelty firewall

The manuscript must subtract the following before stating any residual
Paper-13 contribution:

1. Sorkin's advertised real-line collapse;
2. standard twisted group, crossed-product, amenability, c0-sum,
   multiplier, and corona mechanisms;
3. Paper 2's hard continuum lower bound;
4. Paper 8's one-orbit proxy and trace/return/scalar ledger;
5. Paper 9's actual packet, topology, stabilizer, period, and bare quotient;
6. Paper 11's time-only collapse and untwisted author records; and
7. Paper 12's factorization, standardization, components, J, and comparator.

The permitted residual centre is an exact sign- and owner-safe verification
and typed synthesis.  The constant-diagonal/corona result is a **generic**
lemma for an arbitrary c0 sum after the selected component maps have been
proved isometric.  The actual-author and fixed-prime conclusions are typed
instantiations.  They are not a new packet obstruction, classification, or
prime-sensitive invariant.

The maximum precedent statement remains:

    SUPPORTED_WITHIN_SEARCH, cutoff 2026-08-15

It means only that the bounded search did not locate a direct exact-package
match.  It proves no absence, firstness, priority, novelty, or standalone
weight.

The title and document metadata must visibly say “Technical Note” or an
equally unambiguous equivalent.  Abstract, introduction, conclusion,
metadata, cover letter, and publicity must not say first, new
classification, novel obstruction, breakthrough, standalone pass, or any
equivalent promotion.

No citation in this seed licenses:

- a globally named twisted groupoid C-star algebra on the actual owner;
- topology transfer among actual, bare, standard, and discrete records;
- equality of whole maximal and reduced component algebras;
- erasure of a literal stabilizer, embedding, topology, or period;
- a prime-selective invariant;
- a trace, determinant, zeta object, analytic continuation, A3/A4 object,
  Hilbert--Polya operator, quantization, or Route-B entry; or
- proof by finite controls.

## 9. Formatting, visual, and final-citation preflight

No manuscript, references.bib, figure asset, or compiled PDF exists under
this audit's authorization.  A later draft must still pass all of the
following on its frozen exact bytes:

1. every citation command resolves;
2. every bibliography entry is cited;
3. every theorem-level external citation matches a locator in Sections 5--6;
4. Sorkin remains title/abstract-only unless a separately lawful stronger
   manifestation is audited;
5. Austad is always Proposition 2.4, printed p. 7;
6. Kleppner is never a continuous-trivializer owner;
7. BHM is never assigned a second-countability hypothesis;
8. Williams Proposition 2.34 is never used as a C-star-faithfulness proof;
9. all five companions remain honestly unpublished unless immutable public
   identities have been verified;
10. no local source path, checksum, sidecar, credential, or mutable branch URL
    appears in the public scholarly record;
11. no claim exceeds its owner, topology, regularity, or completion ceiling;
12. the build has zero unresolved citation/reference and bibliography
    warnings; and
13. the compiled PDF is visually inspected after a clean build.

The two blueprint visuals, if later authorized, must be repository-native
TikZ or equivalent vector source.  No source-PDF figure may be copied,
traced, embedded, or rasterized.  The diagrams are schematic transcriptions
of project-authored owner/proof relations; the external source PDFs are not
visual assets.  Figure creation remains separately gated.

The English and Simplified-Chinese abstracts must be composed independently
from their frozen ledgers and later checked for factual parity.  Neither
abstract may contain citation commands, local paths, hashes, Route field
names, or control counts.

This preflight does not infer or close author identity, affiliation,
correspondence, funding, conflict, contributor roles, AI/tool disclosure,
venue, style, repository, archive, DOI, or license declarations.

## 10. Source-PDF and public-release boundary

All source PDFs under every papers/*/notes/sources directory are local
research inputs.  They are excluded from every public payload regardless of
downloadability, open-access label, or source-side licence.  This includes
the CC-BY-labelled Austad and IMPAN manifestations as well as restricted or
copyrighted scans and the Williams author draft.

The project-authored compiled paper/paper.pdf is a different object.  It may
ship only after its own manuscript, build, citation, visual, declaration,
peer, and release gates.  Its status does not authorize redistribution of a
research-source PDF.

A future release audit must require **zero matches** at every layer:

~~~sh
git ls-files | rg '/notes/sources/.*[.]pdf$'
git ls-tree -r --name-only HEAD | rg '/notes/sources/.*[.]pdf$'
git lfs ls-files | rg '/notes/sources/.*[.]pdf$'
git archive --format=tar HEAD | tar -tf - | rg '/notes/sources/.*[.]pdf$'
find <dry-run-payload-root> -type f -path '*/notes/sources/*.pdf' -print
find <fresh-clone-root> -type f -path '*/notes/sources/*.pdf' -print
~~~

The same zero-source-PDF test must cover the index, staged content, current
commit, LFS, release archive, attachments, supplementary payload, and fresh
clone.  The exact future payload must be enumerated and hashed before
release.  A source PDF found at any layer is an automatic release failure.

No Git command or public synchronization was executed by this audit.  The
commands above are future release requirements, not a record of completed
checks.

## 11. Handoff and remaining gates

This preflight closes the bounded source, locator, metadata, regularity,
companion-identity, and literal-seed work needed before a separately
authorized technical-note draft.  It does not close:

- author and venue intake;
- creation or style conversion of an actual bibliography;
- manuscript citation deployment;
- an independent citation audit on the frozen manuscript and Bib;
- mathematical review of the composed manuscript;
- bilingual abstract parity;
- declaration and disclosure review;
- figure trace review;
- public companion identities;
- release payload review; or
- Git/public action.

The later final citation audit must bind the exact manuscript, bibliography,
figure, and compiled-PDF hashes.  It must report zero unresolved citations,
zero uncited entries, zero fabricated identifiers, zero local source paths,
zero source-PDF payloads, zero owner/locator/regularity upgrades, and zero
technical-note positioning violations.

**Final pre-manuscript verdict:** the exact 17-record seed and deployment
plan are source-feasible and internally consistent at C0/M0/m0.  Sorkin
remains an abstract-only sentinel; Austad Proposition 2.4 and the
Leptin/Hulanicki endpoint are exact; Kleppner remains Borel-only; BHM,
Williams, Tu, and Austad--Ortega retain their named framework ceilings; all
five companions are honest unpublished records; no unproved v3/v4 Cartan
source or new PDF was added.  Composition may proceed only under the frozen
technical-note and release boundaries, after separate root authorization.
