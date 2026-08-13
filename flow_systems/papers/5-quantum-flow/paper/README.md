# Paper

The release manuscript is [paper.pdf](paper.pdf). It contains an English
article, an independently composed simplified-Chinese abstract, full proofs,
two source-native TikZ figures, operator and Route ledgers, limitations,
declarations, and a reproducibility appendix.

Build from this directory with the required XeLaTeX/BibTeX sequence:

```bash
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
cp manuscript.pdf paper.pdf
```

`manuscript.pdf` is the build target; `paper.pdf` is the release copy.
