# Paper build

`main.tex` is a three-round conditional manuscript.  The release gate builds
each round twice in fresh directories with LuaLaTeX and fixed epoch
`1788480000`; final `main.pdf` is byte-identical to round 2.

```bash
python -B code/c372_release_manifest.py --write --build-pdfs
```
