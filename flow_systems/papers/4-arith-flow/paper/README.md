# Paper

The review-ready manuscript is [paper.pdf](paper.pdf).  It contains an English
abstract, a simplified-Chinese abstract, four theorem-level results, three
source-native TikZ figures, target-separated Route-A conclusions,
limitations, declarations, and an artifact map.

Build with:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

`manuscript.pdf` is the build target; `paper.pdf` is the release copy.

