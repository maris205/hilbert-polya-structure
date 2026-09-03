# Paper build

`main.tex` is the sole LaTeX source.  It defaults to revision round two.
The release gate compiles a selected round using

```tex
\def\CRevisionRound{0}\input{main.tex}
```

and analogously for rounds one and two.  Each round is built twice in a
fresh temporary directory with `SOURCE_DATE_EPOCH=1788393600`.  Checked-in
PDF roles are:

- `main_round0_original.pdf`: model, first moment, and sharp energy law;
- `main_round1.pdf`: adds the full second-moment decomposition and evolution;
- `main_round2.pdf`: adds covariance, probability, all boundaries, evidence,
  collision, scope, and disclosure;
- `main.pdf`: byte-identical copy of round two.
