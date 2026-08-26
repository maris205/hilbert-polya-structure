# C173 paper build

The release paper is `main.pdf`; `main_round2.pdf` is byte-identical to it.
The two earlier snapshots document substantive revisions.

Rebuild from this directory with LuaLaTeX:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The final build uses A4 paper, embedded Latin Modern and Droid Sans Fallback
fonts, English plus Simplified Chinese abstracts, and no bibliography.  The
final PDF has two pages and SHA-256
`74d495da262be5ee425e0a61772553809929249f63a7335d62ca9dc96d442570`.

Auxiliary LuaLaTeX files are build caches and are excluded from the release
manifest.
