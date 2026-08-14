# HCS-P50: tagged prime-ideal packets and the rational pushforward obstruction

HCS-P49 left two source-native survivors after the full multiplier-field norm
collapsed to a square: the inversion-fixed trace-field half packets and their
prime-ideal divisors.  HCS-P50 assembles those divisors without erasing the
orbit, cyclotomic index, signed branch, or trace-field prime ideal.

For a finite set of signed primitive H6 controls and indices, write

\[
\beta_{\gamma,n}
=\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
\in\mathcal O_{F_\gamma},
\qquad n>2,
\]

where \(F_\gamma\) is the inversion-fixed trace field.  The project proves
that the divisor

\[
\mathscr D_S=
\sum_{(\gamma,n)\in S}\sum_{\mathfrak q\mid(\beta_{\gamma,n})}
v_{\mathfrak q}(\beta_{\gamma,n})
[\gamma,n,\mathfrak q]
\]

is a canonical lossless **finite-cutoff** ledger relative to the signed H6
source data.  Its rational norm pushforward is exact:

\[
[\gamma,n,\mathfrak q]\longmapsto
f(\mathfrak q/p)[p],
\qquad
\operatorname{div}_{\mathbb Z}|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}|
=\sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
f(\mathfrak q/p)[p].
\]

If \(p\nmid n\), every multiplier-field prime above
\(\mathfrak q\mid(\beta_{\gamma,n})\) sees the reduction of
\(\lambda_\gamma\) with exact multiplicative order \(n\).  The statement is
deliberately not made at bad characteristic \(p\mid n\).

The exact H6 certificate uses primitive periods 1, 3, and 4 and indices
3--20.  It contains 125 tagged atoms but only 95 distinct rational primes.
Consequently the free rational-prime pushforward has kernel rank 30.  The
same rational prime can carry incompatible clocks: for example \(p=29\)
carries certified orders 7, 14, and 15.  At \(p=109,n=11\), two different
split prime ideals occur in the period-one trace field, while a third occurs
for period three.  Thus a rational-prime-only ledger is noninjective and
cannot be called a lossless source-native H6 Euler clock.

## Status

- Tagged finite-cutoff assembly: `PROVED_TAGGED_FINITE_CUTOFF_LEDGER`.
- Untagged rational-prime pushforward: `STOP_SCOPED_NONINJECTIVE` / HEN-O90.
- Pressure-weighted all-orbit limit: `OPEN`.
- Route A: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and
  `ROUTE_A_EXPLORATORY`.
- Route B: not authorized.

The obstruction is scoped.  It does not say that rational norms are useless,
nor that no weighted statistic can be pushed forward.  It says only that the
untagged pushforward forgets genuine source data and is not an injective
identification of H6 packets with rational primes.

## Reproduce

```bash
bash code/run_c50.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The final paper is [`paper/paper.pdf`](paper/paper.pdf).  The next large-road
problem is not another scalarization: it is a pressure-weighted all-primitive-
orbit limit of the vector-valued tagged divisor ledger, with convergence and
the rational pushforward treated as separate theorems.
