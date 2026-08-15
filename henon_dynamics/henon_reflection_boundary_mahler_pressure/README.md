# HCS-P64: Reflection-boundary equidistribution and extensive packet pressure

P63 proved that ordinary fixed-parameter coordinate height is bounded and
therefore pressure-flat. P64 identifies the correct extensive packet object.
For odd periods, the complete mixed-axis roots are the reflection-fixed
slice of the full two-shift. Their marked-axis empirical measures converge
to a one-sided fair Bernoulli process reflected across the marked axis,
whereas averaging each selected orbit over time converges to the invariant
maximal-entropy Bernoulli measure.

For the monic integral primitive coordinate polynomial
`tilde_Psi_n`, put

```text
a_n = D_n^(-1) log M(tilde_Psi_n).
```

Then `a_n -> kappa_J`, where `kappa_J` is the reflection-boundary average of
`log^+|x|`, and

```text
lim_(odd n) n^(-1) log[D_n exp(-s n a_n)]
  = (1/2)log(2) - s kappa_J
```

for every fixed real `s`. Moreover `0 < kappa_J <= log(1+sqrt(7))`, so this
pressure is genuinely nonconstant. The analogous orbit-averaged packet has
slope `kappa_max`, the maximal-entropy average.

The distinction is essential: on the axis limit, `s[-1]=s[1]` almost surely,
while this event has probability `1/2` under the invariant fair Bernoulli
measure. Finite diagnostics through period 11 suggest the two numerical
slopes differ, but P64 does not promote that observation to a theorem.

## Status

- **PROVED:** reversor-equivariant full-shift coding on the frozen H6
  horseshoe;
- **PROVED:** primitive reflection-axis weak-star convergence;
- **PROVED:** orbit-averaged convergence to maximal entropy;
- **PROVED:** nonconstant linear packet-Mahler pressure;
- **NUMERICAL_OBSERVATION:** finite axis/orbit slope separation;
- **OPEN:** a rigorous nonzero interval separating `kappa_J` and
  `kappa_max`, individual extensive-height pressure, and any prime trace;
- Route A: **EXPLORATORY / A1 strengthened**; Route B: **not authorized**.

## Reproduce

```bash
bash code/run_c64.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The compiled manuscript is [`paper/paper.pdf`](paper/paper.pdf).
