# Figure specification: periodic-clock obstruction map

## Purpose

The figure is a theorem map, not empirical evidence.  It makes the assumption
boundary of the periodic-clock obstruction visible in one glance:

1. an exact, single-valued, autonomous clock decoder forbids periodic points
   in the direct image;
2. erasing the clock permits periodic quotients but destroys arithmetic
   inheritance;
3. recovering the clock from a lift, visit counter, or traversal time is a
   nonautonomous construction and therefore not the claimed factor model;
4. passage from the direct image to its closure is valid only with a total
   continuous decoder and lag-pair separation from the clock diagonal;
5. discontinuous decoders or compactified clocks may admit periodic boundary
   points, which are explicitly labelled arithmetic-sterile.

The layout is deliberately a three-way classification followed by a separate
closure test.  It must not be read as saying that every conceivable symbolic
recoding falls into one of the three boxes; it classifies the clock semantics
used by the theorem and its controls.

## Mathematical objects encoded

- Source: `X = \bigsqcup_{k\geq0} X_k` with
  `\sigma(X_k)\subseteq X_{k+1}`.
- Exact clock: `\kappa(x)=q_{k+1}` for `x\in X_k`; the logarithmic clock is
  `\tau=\log\kappa`.
- Direct image: `\pi(X)` for a shift-commuting recoding `\pi`.
- Exact autonomous decoder: a single-valued state map `d` satisfying
  `d(\pi x)=\kappa(x)`.
- Orbit closure: `Y_0=\overline{\pi(X)}`.
- Lag-pair set:
  `E_m=\{(\kappa(x),\kappa(\sigma^m x)):x\in X\}`.
- Closure condition: `\overline{E_m}\cap\Delta_C=\varnothing` for every
  positive lag `m`.

For the ordinary uncompactified clock spaces used in the paper, the relevant
choices are `C=\mathbb N_{\mathrm{disc}}` for the exact prime clock and
`C=\mathbb R` for finite logarithmic clock values.  A compactification that
adds an infinite value is intentionally placed in the countercontrol branch.

## Visual grammar and accessibility

| Semantic class | Color | Shape / border | Explicit text tag |
|---|---|---|---|
| Valid obstruction theorem | muted blue | solid rounded rectangle / solid arrow | `THEOREM` |
| Sharp control or assumption failure | muted orange | dashed rounded rectangle / dashed arrow | `CONTROL` or `COUNTERCONTROL` |
| Nonautonomous or invalid decoder model | gray | dotted rounded rectangle / dotted arrow | `INVALID MODEL` |

Thus color is redundant: line style, box labels, and outcome text preserve all
meaning in grayscale.  The figure has no internal title, decorative imagery,
legend-only semantics, or rasterized text.  Mathematical notation is typeset
by the parent LaTeX document.

## Integration contract

The manuscript should load:

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric}
```

The input file contains only the `tikzpicture`; the manuscript owns the float,
centering, caption, and label.  Include it as follows:

```latex
\begin{figure}[t]
  \centering
  \input{figures/obstruction_map}
  \caption{...}
  \label{fig:periodic-clock-obstruction}
\end{figure}
```

The file is pure TikZ and has no external image, data, generated cache, or
shell-escape dependency.  A direct TeX box measurement gives a natural width
of 419.43 pt (approximately 14.74 cm, including node padding), so it fits the
443.86 pt (15.60 cm) text block produced by A4 paper with 27 mm left and right
margins without scaling.

## Caption claim discipline

The caption supplied by the manuscript should distinguish four logically
different statements:

- direct-image no-cycle theorem under exact autonomous decoding;
- periodic clock-erasing quotient as a sharp control, not a valid arithmetic
  inheritance result;
- external/lift/traversal clocks as model failures, not counterexamples;
- closure no-cycle theorem under continuity and lag-pair separation, together
  with a compactification/discontinuity boundary control.

It does not claim a prime determinant, a periodic-orbit trace formula, a
Route-B candidate, or evidence beyond symbolic dynamics.
