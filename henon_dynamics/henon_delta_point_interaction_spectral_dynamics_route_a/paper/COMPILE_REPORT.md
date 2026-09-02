# Compile report

- Engine: LuaLaTeX (two passes per build).
- Reproducibility clock: `SOURCE_DATE_EPOCH=1788307200`, `TZ=UTC`.
- PDF trailer ID: fixed in `main.tex`.
- Fresh builds: two isolated directories for each of Rounds 0, 1, and 2;
  the release manifest itself performs two LuaLaTeX passes per build, and
  every same-round pair is byte-identical to its retained artifact.
- Retained pages: Round 0 = 1, Round 1 = 2, Round 2 = 3.
- Round hashes:
  - `main_round0_original.pdf`: `16c7dd82828c3130602a1ab1d25b91a38c7452c68a4325764a12691d15641eae`
  - `main_round1.pdf`: `5de873c3dbef1500762cf7cdbab0c57cc6667af7bd93eb4335107fc4b1435759`
  - `main_round2.pdf`: `f6d2973ac3523a6b29609820e348f45cddec81135ee36f02d6f6019ad05dae35`
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Fonts: all fonts in all three rounds are embedded and subset.
- Settled second-pass logs are warning-free.  No overfull/underfull boxes, undefined
  references/citations, or rerun requests occur; the log only identifies the
  loaded `rerunfilecheck` package.
- All three round page counts and extracted-text contracts are checked, and
  the final three-page PDF was visually inspected after hardening.
