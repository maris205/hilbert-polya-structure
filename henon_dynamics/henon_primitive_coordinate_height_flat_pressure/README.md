# HCS-P63: primitive-coordinate height and the flat-pressure obstruction

This project tests the first all-period height pressure suggested by HCS-P62
for the area-preserving map

\[
H_6(q,p)=(1-6q^2-p,q).
\]

The test produces an exact negative answer for the pressure as originally
written.  Under the integral scaling `x=6q`, every primitive mixed-axis root
is an algebraic integer and every one of its Galois conjugates is a real
periodic coordinate.  If `M` is the largest absolute coordinate on a
periodic orbit, the recurrence gives

\[
M^2\le 6+2M,
\qquad M\le 1+\sqrt7.
\]

Hence every scaled primitive coordinate has uniformly bounded absolute Weil
height,

\[
0\le h(x)\le \log(1+\sqrt7),
\]

independently of its odd period.  For the reduced primitive polynomial
`tilde_Psi_n` of degree `D_n`, define

\[
Z_n(s)=\sum_{\widetilde\Psi_n(\alpha)=0}e^{-s h(\alpha)}.
\]

Then for every fixed real `s`,

\[
\lim_{n\to\infty,\ n\text{ odd}}\frac1n\log Z_n(s)
=\frac12\log2.
\]

The ordinary coordinate-height pressure is therefore flat: it records only
the unweighted primitive-root entropy.  A nontrivial next pressure must use
an extensive observable, such as `n*h(alpha)`, packet Mahler height, or a
discriminant/ramification height.

This flatness is not an artifact of `x=6q`: every fixed nonzero algebraic
rescaling changes height by at most an additive constant and leaves the
pressure unchanged.

## Strongest status

- **PROVED:** every scaled primitive reflection coordinate is an algebraic
  integer whose conjugates lie in `[-(1+sqrt(7)),1+sqrt(7)]`.
- **PROVED:** the ordinary per-root Weil-height pressure is identically
  `(1/2)log(2)` for every fixed real parameter.
- **COMPUTER_CERTIFIED_EXACT:** scaled primitive polynomials through odd
  period 11 are monic integral and irreducible in the finite ledger.
- **NUMERICAL_DIAGNOSTIC:** 50-digit factor heights and root maxima through
  period 11 satisfy the exact all-period envelope.
- **STOP_SCOPED:** ordinary non-extensive coordinate height cannot supply a
  new pressure pole or distinguish the physical instability pressure.

## Reproduce

```bash
bash code/run_c63.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

## Project contents

- `paper/paper.pdf`: complete manuscript;
- `PROOF_PACKAGE.md`: compact theorem ledger;
- `code/`: primary and independent certificate implementations;
- `results/`: frozen JSON certificates and test report;
- `experiments/`: claim-driven finite validation plan;
- `notes/`: source audit, hostile review, evaluator boundary, and next clue.

## Claim boundary

This paper corrects the specification of one height pressure.  It does not
prove an extensive Galois pressure, rational-prime labels, von Mangoldt
amplitudes, a completed Riemann determinant, a Hilbert--Polya operator, or
the Riemann hypothesis.
