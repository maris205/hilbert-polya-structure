# HCS-C45: pressure-normalized Hénon prime-orbit bridge

Let (\tau=\log J^u) be the positive non-lattice instability roof on the
certified mixing (H_6) survivor, and let (h_*) be the unique root

\[
P(-h_*\tau)=0,
\qquad 0.277980<h_*<0.277987.
\]

The normalized roof (\widehat\tau=h_*\tau) has suspension entropy exactly
one and remains non-lattice.  The Parry--Pollicott prime orbit theorem gives

\[
\#\{\gamma:\widehat\ell_\gamma\le T\}
\sim e^T/T.
\]

This is a genuine positive all-period bridge: it repairs C44's raw-clock
overconvergence using an intrinsic pressure normalization.  Each orbit has a
real label

\[
P_\gamma=e^{\widehat\ell_\gamma}
=|\Lambda_\gamma|^{h_*},
\]

and its Euler factor generates the exact prime-power syntax.  The unresolved
gate is arithmetic: (P_\gamma) is not proved to be a rational prime.

## Reproduce

```bash
bash code/run_c45.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Route A remains exploratory; Route B is not authorized.
