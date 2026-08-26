# P67 Stage 2.5 correction round 1

Correction date: **2026-08-26 UTC**  
Scope: objective bibliography, citation, and owner-subtraction corrections requested after the Stage-2.5 audit  
External state: **HOLD**  
Correction-round re-verification: **PASS**  
Full Stage-2.5 release gate: **not re-adjudicated by this receipt**

The requested source defects are resolved. This receipt does not resolve the audit's
separate author-identity, contribution, funding, competing-interest, AI-disclosure,
or specialist-release gates, and it is not a novelty or priority certificate. The
pre-existing claim-registry sidecars in `stage2_5/` were not edited.

## 1. Objective corrections and disposition

1. **KPS title mismatch — RESOLVED.** `KenyonPeresSolomyak2012` now renders as
   “Hausdorff Dimension for Fractals Invariant under Multiplicative Integers”; the
   spurious word “the” was removed. The corrected reference appears on PDF page 11.
2. **Abbe--Spirkl owner omission — RESOLVED.** The bibliography now contains the
   verified 2019 *Entropy* article, and Section 6 assigns to it the general
   finite-field representable-matroid entropy-rank mechanism. P67 retains only the
   arithmetic identification of its evaluation matroid and the resulting Haar
   consequences.
3. **Ban--Hu--Lai--Liao affine-shift omission — RESOLVED.** The verified 2025
   *Advances in Mathematics* record is cited in the introduction and Section 6.
   The text distinguishes their affine index constraints `pk+a` and `qk+b` from
   P67's mixed plaquette rule and globally extendable arbitrary finite projections.
4. **Király--Rosen--Theran owner omission — RESOLVED.** The verified arXiv record is
   cited in Section 6. Their algebraic/graph-symmetric matroid framework is assigned
   prior ownership; P67's residual object is the arithmetic direct sum of the
   particular graphic matroids `M(G_r(F))`.
5. **Residual-claim boundary — RESOLVED.** Section 6 now states the residual P67
   conjunction precisely: the global free-axis homeomorphism, every globally
   extendable finite projection as the stated direct sum, and the prefix,
   rectangle, and Haar forest/cycle formulas. The exact-neighbor conclusion remains
   search-bounded through 2026-08-26 and expressly disclaims worldwide novelty.

No theorem, lemma, proof, table, or deterministic-control source was changed.

## 2. Source re-verification

| Record | Direct authoritative evidence | Metadata/context verdict |
|---|---|---|
| Kenyon--Peres--Solomyak (2012) | [publisher DOI](https://doi.org/10.1017/S0143385711000538), [arXiv](https://arxiv.org/abs/1102.5136) | **VERIFIED_AFTER_CORRECTION**; title now matches |
| Abbe--Spirkl (2019) | [publisher DOI](https://doi.org/10.3390/e21100948), [arXiv](https://arxiv.org/abs/1909.12175) | **VERIFIED**; *Entropy* 21(10), article 948; cited only for the general representable-matroid entropy mechanism |
| Ban--Hu--Lai--Liao (2025) | [publisher record](https://www.sciencedirect.com/science/article/pii/S0001870825001641), [DOI](https://doi.org/10.1016/j.aim.2025.110266) | **VERIFIED**; *Advances in Mathematics* 471, article 110266; affine-shift geometry accurately distinguished |
| Király--Rosen--Theran (2013) | [arXiv abstract/record](https://arxiv.org/abs/1312.3777), [arXiv DOI](https://doi.org/10.48550/arXiv.1312.3777) | **VERIFIED**; graph-symmetric algebraic-matroid ownership accurately subtracted |

The negative exact-neighbor search remains only the bounded result recorded in
`SOURCE_SEARCH_LEDGER.md`; it was not promoted to a worldwide claim.

## 3. Changed files and fingerprints

All deliberate source/documentation edits in this round were made with
`apply_patch`. Generated TeX auxiliaries and the PDF were produced only by the
documented build commands.

| File | Pre-correction SHA-256 | Post-correction SHA-256 | Change |
|---|---|---|---|
| `main.tex` | `940ceda23385c37a2c3f362640c8cd362807685b848329bbf4897b8f2b4984ae` | `940ceda23385c37a2c3f362640c8cd362807685b848329bbf4897b8f2b4984ae` | unchanged modular driver |
| `references.bib` | `2851302e6b59779e23cee662718950514f8220930a8508b42343552f129b58e2` | `ff523453c6f1ddb518319d6d15c815071e449fd85f97f7115b3fdd24eda23628` | title correction and three verified entries |
| `sections/1_introduction.tex` | `fdc642229f41a624642b0bbc82b1cb993a321c6940342d7c404c94d6fbc99ef5` | `77868f1c8e13d6fb4599f8678466ac0a28b4b8293c182f58ccc4bce9580ed70f` | affine-shift context citation |
| `sections/6_scope.tex` | `9831b3753d5e50931db3bafe9d4e2cc1bbb15c683d1cd66d8558e3c41d56590e` | `b0f0e141f8bd602ef8bf2c965051fcde659a0630d795afd51f7dcc34fdf0ef7a` | owner subtraction and residual boundary |
| `BUILD.md` | `7063618161e9f3731f52b7a8d7ccc207d5cbeb9f5b4ece031c44d57376b310f0` | `46a96eaa6a33821620d04a3817d8c738be744664f9479361e41e81549951ca9f` | current reference count/artifact status |
| `main.pdf` | `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e` | `ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da` | deterministic rebuilt artifact |

Generated bibliography SHA-256: `main.bbl` =
`a5c6cca4f325cf80513b44a8f350f83fddad1012f345da02d145ef7238e9ae97`.

## 4. Citation closure

| Check | Result |
|---|---|
| BibTeX entries | 11 |
| Citation commands/contexts | 17 |
| Citation-key mentions | 21 |
| Distinct cited keys | 11 |
| Cited keys absent from bibliography (ghost citations) | 0 |
| Bibliography keys absent from manuscript (dangling entries) | 0 |
| Undefined citations/references in final log | 0 |
| Suspicious rendered markers (`??`, `[?]`, `[VERIFY]`) | 0 |

The three new sources are cited in four semantically useful placements: the affine
neighbor in the introduction and comparison section, and the entropic-matroid and
graph-symmetric-matroid owners in the comparison section. PDF pages 9--11 were
visually inspected after the final build; the owner subtraction and all eleven
references render legibly.

## 5. Deterministic control and build replay

The authoritative sequence was replayed from the package directory:

```sh
export SOURCE_DATE_EPOCH=1787616000
python3 code/verify_plaquette_matroid.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

- Control terminus: `ALL CHECKS PASS`.
- Live control output was byte-identical to both frozen receipts.
- Control script SHA-256:
  `d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158`.
- Both frozen/live-output SHA-256 values:
  `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26`.
- A second complete build replay left the PDF SHA-256 unchanged, establishing
  byte-for-byte reproducibility under the declared epoch.
- Final artifact: 11 A4 pages, 408243 bytes; author PDF metadata empty.
- Final `main.log`/`main.blg`: zero warnings, undefined citations/references,
  overfull boxes, underfull boxes, and TeX errors.
- All PDF fonts are embedded and subset.

These finite computations are proof-regression controls, not experiments, and they
do not replace any infinite or arbitrary-size proof.

## 6. Re-verification verdict and remaining boundary

**CORRECTION_ROUND_1_SOURCE_AND_BUILD: PASS.** Every objective bibliography and
owner-subtraction item assigned to this round is present, cited, rendered, and
closed under the build. **EXTERNAL_RELEASE: HOLD.** The original audit's unresolved
identity/declaration and specialist-release items remain outside this correction's
authority. Global pipeline state, release state, historical review PDFs, and
root-owned claim-registry sidecars were not modified.
