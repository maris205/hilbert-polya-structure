# Paper build

`main.tex` is a conditional LuaLaTeX manuscript. The three frozen rounds are:

- round 0: normalized contact system and primitive-period theorem;
- round 1: arbitrary-time fixed sets, Morse--Bott kernels, transverse return,
  degeneracy, and exceptional CZ formulas;
- round 2: Seifert quotient, explicit principal RS derivation and sign theorem,
  evidence audit, limitations, and Route-A closure.

Build and audit all rounds twice in fresh directories with:

```bash
python ../code/c370_release_manifest.py --build-pdfs
```

The command freezes `SOURCE_DATE_EPOCH=1788480000`. `main.pdf` must be
byte-identical to `main_round2.pdf`. The final release gate additionally checks
warning-free settled logs, embedded/subset fonts, extracted text, rasterized
pages, round-specific tokens, and byte-identical fresh rebuilds.
