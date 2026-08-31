# P26 Stage 5 content preflight — 2026-08-31

## Outcome

**PASS PREFLIGHT / STAGE 5 `in_progress`.** The format-only payload builds
cleanly and reproduces the accepted Stage-4.5 content proof at the extracted
text level. The one remaining gate is scholar content confirmation. No final
`paper.pdf` has been created.

The machine-readable receipt is
`notes/stage5_preflight_build_receipt.json`, SHA-256
`bbf9f6a6d92dc9602548921e7ca8dcfa4594e7e4dab2b535624803e94d72fa12`.

## Locked inputs and exclusive transform

| Check | Result |
|---|---:|
| accepted TeX SHA-256 | `345c258b5a1097c67d4f7777167b90eee208d6b2d36b23655990269a4de42203` |
| Stage-5 TeX SHA-256 | `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3` |
| standalone block lines removed | 125 |
| non-marker source-byte changes | 0 |
| remaining HTML/ARS markers | 0 |
| bibliography byte identity | PASS; `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f` |
| content-proof byte identity | PASS; `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da` |

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
errors; BibTeX has zero warnings. The temporary diagnostic PDF is 16 A4 pages
and was not retained in the repository.

The citation profile is unchanged: `natbib[numbers,sort&compress]` with
`plainnat`. All eight citation contexts resolve to seven unique keys; the
bibliography and generated `.bbl` each contain seven entries. Missing cited
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
  `c65222378bba501f5bb96e5a5fe2ece4bda3fdb148a8695aa47264c9cac3bc01`;
- `-layout` text SHA-256 on each PDF:
  `67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444`.

The temporary PDF container hash differs from the historical proof container,
but page count, page size, file size, ordinary extracted text, and layout text
agree. The locked content proof remains the confirmation artifact.

## Pandoc lossiness check

`pandoc --from=latex --to=plain --wrap=none manuscript.tex` returns `0`, but
the conversion is **lossy and must not be promoted**. It emits 16 mathematical
conversion warnings; its plain output is not byte-equal to the PDF text, has
no rendered numeric citation markers or References section, and omits
arguments of LaTeX `\path` commands. The LaTeX source and LuaLaTeX proof are
therefore authoritative; no Pandoc-derived manuscript was retained.

## Freeze and next gate

The canonical `paper` tree remains
`71e7fb6184cfa7ee958745b81f078fdba8f7c930140a1f4bc4cafd1f520d943f`;
the `results` tree remains
`67e503425d253f2907cc85ecdedf6843c00ab84c048de34dd2c6cc722b409713`.
The initial dynamical object, subtype, Route-A tuple, and uninvoked Route B are
unchanged.

**Pending:** one scholar content confirmation of the 16-page proof. Only after
that confirmation may final-PDF generation be authorized.
