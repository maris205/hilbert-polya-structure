# P27 Stage 5 content preflight — 2026-08-31

## Outcome

**PASS PREFLIGHT / STAGE 5 `in_progress`.** The format-only payload builds
cleanly and reproduces the accepted Stage-4.5 content proof at the extracted
text level. The one remaining gate is scholar content confirmation. No final
`paper.pdf` has been created.

The machine-readable receipt is
`notes/stage5_preflight_build_receipt.json`, SHA-256
`3ce4aff0e76f9412c14371e93d967229d1942227f3b9289404976d7383e80c88`.

## Locked inputs and exclusive transform

| Check | Result |
|---|---:|
| accepted TeX SHA-256 | `803d9e7d69c233363d912b4fee25f5915b7f07d48937b794ee11c807ca182ef7` |
| Stage-5 TeX SHA-256 | `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48` |
| standalone block lines removed | 110 |
| non-marker source-byte changes | 0 |
| remaining HTML/ARS markers | 0 |
| bibliography byte identity | PASS; `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981` |
| content-proof byte identity | PASS; `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208` |

The transform was replayed from the accepted input and compared bytewise with
`stage5_finalization/manuscript.tex`; it passes. No scientific, declaration,
bibliographic, subtype, Route, canonical, or result byte was edited.

## Isolated build and hard gates

An isolated temporary directory received only the Stage-5 TeX and
bibliography. The command sequence was:

```text
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
lualatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

All four return codes are `0`. The final pass has zero undefined citations,
undefined references, rerun requests, missing glyphs, overfull boxes, or fatal
errors; BibTeX has zero warnings. The temporary diagnostic PDF is 13 A4 pages
and was not retained in the repository.

The citation profile is unchanged: `natbib[numbers,sort&compress]` with
`plainnat`. All five citation contexts resolve to five unique keys; the
bibliography and generated `.bbl` each contain five entries. Missing cited
keys and uncited bibliography keys are both zero.

The ARS formatter hard gate finds zero unresolved warning/placeholder strings,
zero problematic reference/anchor markers, and zero `HIGH-BLOCK` markers.
All seven required disclosure/boundary headings remain present:

1. Limitations and open obligations
2. Data and Code Availability
3. Ethics Declaration
4. Author Contributions
5. Conflict of Interest
6. Funding
7. AI-Assisted Research Disclosure

The author name, affiliation, postal address, and email remain present.

## Content-proof equivalence

`pdftotext` comparison against
`stage5_finalization/content_proof.pdf` passes in both modes:

- default text SHA-256 on each PDF:
  `75505120c4517dff9d3e273631baad6d268ab550c45524deea5e48d0888d6ecb`;
- `-layout` text SHA-256 on each PDF:
  `5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b`.

The temporary PDF container hash differs from the historical proof container,
but page count, page size, file size, ordinary extracted text, and layout text
agree. The locked content proof remains the confirmation artifact.

## Pandoc lossiness check

`pandoc --from=latex --to=plain --wrap=none manuscript.tex` returns `0`, but
the conversion is **lossy and must not be promoted**. It emits 11 mathematical
conversion warnings; its plain output is not byte-equal to the PDF text, has
no rendered numeric citation markers or References section, and omits
arguments of LaTeX `\path` commands. The LaTeX source and LuaLaTeX proof are
therefore authoritative; no Pandoc-derived manuscript was retained.

## Freeze and next gate

The canonical `paper` tree remains
`c95656aee2c1ba49bf4646f80e6c203047fcb832ed76371ae931a898991594a1`;
the `results` tree remains
`5009c710cf06ef5147ccc392ee09c604b9a5b846b433eacbfc57650957d65761`.
The residual congruence inverse-limit flow, the separate homology-cover
calibrator, their two rejected Route-A tuples, and uninvoked Route B are
unchanged.

**Pending:** one scholar content confirmation of the 13-page proof. Only after
that confirmation may final-PDF generation be authorized.
