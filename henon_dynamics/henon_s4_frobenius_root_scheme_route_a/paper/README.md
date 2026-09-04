# Paper build

`main.tex` is a conditional three-round manuscript.  The release gate builds
rounds 0, 1, and 2 twice in fresh directories with LuaLaTeX and fixed epoch
`1788480000`.  `main.pdf` is byte-identical to `main_round2.pdf`.

Build and audit all artifacts from the package root:

```bash
python -B code/c369_release_manifest.py --write --build-pdfs
```
