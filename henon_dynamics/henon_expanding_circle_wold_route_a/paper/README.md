# C177 paper build

The released manuscript is `main.pdf`; `main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve the three materially distinct internal drafting rounds.

Final deterministic build:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

Release requires two fresh byte-identical final builds, embedded/subset fonts, and logs free of layout, glyph, reference, citation, and rerun warnings. Build auxiliaries are not released.
