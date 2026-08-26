# P70 Stage 2.5 correction round 1

Correction date: **2026-08-26 UTC**  
Scope: objective direct-neighbor bibliography, citation, and owner-subtraction corrections requested after the Stage-2.5 audit  
External state: **HOLD**  
Correction-round re-verification: **PASS**  
Full Stage-2.5 release gate: **not re-adjudicated by this receipt**

The two requested direct-neighbor omissions are resolved. This receipt does not
resolve the audit's separate author-identity, contribution, funding,
competing-interest, AI-disclosure, or specialist-release gates, and it is not a
novelty or priority certificate. The pre-existing claim-registry sidecars in
`stage2_5/` were not edited.

## 1. Objective corrections and disposition

1. **Deundyak--Leonov omission — RESOLVED.** The bibliography preserves the
   publisher's title spelling, including “Heisenber” and “Galua,” and records the
   2016 issue and pages. The introduction and Section 7 assign prior ownership of
   left/right finite-Heisenberg convolution, noncommutative Fourier blocks, the
   characteristic-zero representation ledger, and blockwise equation solving.
   They are not represented as a source for P70's cross-characteristic singular
   nullities.
2. **Grassberger--Hörmann omission — RESOLVED.** The bibliography now contains the
   verified 2001 DMTCS article. The introduction, Section 3, and Section 7 identify
   it as a direct owner of the finite-Heisenberg irreducible classification; the
   manuscript still proves its own cross-characteristic classification rather than
   transferring a complex statement silently.
3. **Residual-claim boundary — RESOLVED.** Section 7 limits P70's residual candidate
   contribution to the weighted cross-characteristic congruence-nullity formula,
   character gcd term, central-character-independent Fermat determinant, exact
   corank-one singular blocks, and the `ell(ell-1)` regular-representation jump.
   The exact-neighbor statement is bounded through 2026-08-26 and expressly
   disclaims a worldwide novelty or priority certificate.

No theorem, lemma, proof, table, numerical result, or deterministic-control source
was changed.

## 2. Source re-verification

| Record | Direct authoritative evidence | Metadata/context verdict |
|---|---|---|
| Deundyak--Leonov (2016) | [publisher record](https://vestnik.kubsu.ru/article/view/686), [original PDF](https://vestnik.kubsu.ru/article/download/686/1168/694) | **VERIFIED**; no. 2, pp. 46--53; original-text inspection supports the left/right convolution, FFT, irreducible-block, and solving-algorithm attribution |
| Grassberger--Hörmann (2001) | [publisher](https://dmtcs.episciences.org/284), [DOI](https://doi.org/10.46298/dmtcs.284), [publisher PDF](https://dmtcs.episciences.org/284/pdf) | **VERIFIED**; *Discrete Mathematics & Theoretical Computer Science* 4(2), 91--100; original statement supports the finite-Heisenberg irreducible-classification attribution |

The negative exact-formula search remains only the bounded result recorded in
`SOURCE_SEARCH_LEDGER.md`; it was not promoted to a worldwide claim.

## 3. Changed files and fingerprints

All deliberate source/documentation edits in this round were made with
`apply_patch`. Generated TeX auxiliaries and the PDF were produced only by the
documented build commands.

| File | Pre-correction SHA-256 | Post-correction SHA-256 | Change |
|---|---|---|---|
| `main.tex` | `dee658d7259b0aa69d2255293d87336b54def9c8ed2a47962326e16b3236c984` | `dee658d7259b0aa69d2255293d87336b54def9c8ed2a47962326e16b3236c984` | unchanged modular driver |
| `references.bib` | `a3e0cfa339eaaa8a20d61b9fe4338f0385ad6c982f8be49c11fb5c2773d3b0cc` | `67a2eafcce1eba789e38f6f6781f441ecf7a2acd083fb05dfe072083c1738ee3` | two verified direct-neighbor entries |
| `sections/1_introduction.tex` | `1386879d4d4db2516e23894b1767cdd303c5fdd8b21b4db9588d334db8bca9df` | `3bdebe57ba9bbe82218d482c9b50ae3a53c59a97dbc15d813445a777f9e9f128` | direct computational/representation owners |
| `sections/3_regular_decomposition.tex` | `22ef5a3a3752bae4caa84bbf9a970c2528d5b5579a033b6e87e65cf38985ab63` | `9b046dd288946c723996e36fe5997ee6977c924fc5fd1673ec012cc54520b08c` | direct finite-group classification owner |
| `sections/7_scope_declarations.tex` | `90d603174bd3d4b36dc0dd126db6aad56c1937df30b51de2308c06cfbc8d77ef` | `ad600273fb389f478b91387cd8284754545f5e2d7f47c501711154dd7161f8a0` | owner subtraction and residual boundary |
| `BUILD.md` | `cc27d1894539388727f760b49091c8f55c24b8fdbdf56c7018c8c6aae2c9eb49` | `c40b5c7e70e79b3105f9d1056eb3f8478879548b60e740bc2dd22f784a9d1001` | current correction/artifact status |
| `main.pdf` | `e20e1151597684736d72deeac8875d4be0e5e95d95ef2c187468d07f734f3ac5` | `61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142` | deterministic rebuilt artifact |

Generated bibliography SHA-256: `main.bbl` =
`f8db75f4274fc4c3dcbf8b69dfe98dd583d85f232d923e4f21de423877a939e7`.

## 4. Citation closure

| Check | Result |
|---|---|
| BibTeX entries | 7 |
| Citation commands/contexts | 14 |
| Distinct cited keys | 7 |
| Cited keys absent from bibliography (ghost citations) | 0 |
| Bibliography keys absent from manuscript (dangling entries) | 0 |
| Undefined citations/references in final log | 0 |
| Suspicious rendered markers (`??`, `[?]`, `[VERIFY]`) | 0 |

The new neighbors are cited in five semantically useful placements across the
introduction, the finite regular-decomposition section, and the scope section.
PDF pages 1, 6, and 7 were visually inspected after the final build; the owner
subtraction and all seven references render legibly.

## 5. Deterministic control and build replay

The authoritative sequence was replayed from the package directory:

```sh
python3 code/verify_weighted_heisenberg.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

- Control terminus: `ALL WEIGHTED HEISENBERG CONTROLS PASS`.
- Live control output was byte-identical to `code/verification_output.txt`.
- Control script SHA-256:
  `a476ddddca2d9373c1412039e86dac64457354740e530ff3e20ab7ade4e5b1e1`.
- Frozen/live-output SHA-256:
  `fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f`.
- A second complete build replay left the PDF SHA-256 unchanged, establishing
  byte-for-byte reproducibility under the package's suppressed volatile metadata.
- Final artifact: 7 A4 pages, 345028 bytes; author PDF metadata empty.
- Final `main.log`/`main.blg`: zero warnings, undefined citations/references,
  overfull boxes, underfull boxes, and TeX errors.
- All PDF fonts are embedded and subset.

These finite computations are proof-regression controls, not experiments, and they
do not replace the all-prime theorem.

## 6. Re-verification verdict and remaining boundary

**CORRECTION_ROUND_1_SOURCE_AND_BUILD: PASS.** Every direct-neighbor bibliography
and owner-subtraction item assigned to this round is present, cited, rendered, and
closed under the build. **EXTERNAL_RELEASE: HOLD.** The original audit's unresolved
identity/declaration and specialist-release items remain outside this correction's
authority. Global pipeline state, release state, historical review PDFs, and
root-owned claim-registry sidecars were not modified.
