# Figure specification: Route-A chain

## Asset

- File: `figures/route_a_chain.tex`
- Format: pure TikZ, vector output after LaTeX compilation
- Intended size: one paper column (`\linewidth`)
- Inclusion: the asset contains no `figure` float, caption, or label

Recommended inclusion:

```latex
\begin{figure}[t]
  \centering
  \input{figures/route_a_chain}
  \caption{...}
  \label{fig:route-a-chain}
\end{figure}
```

Required preamble support:

```latex
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}
```

The equations also assume the paper's normal AMS math support.

## Mathematical content

The main vertical chain records five logically distinct links:

1. finite full shifts with the actual Cartesian product,
   `F_m tensor F_n` conjugate to `F_mn`;
2. tensor atoms and the entropy norm, giving atoms `F_p` and roof `log p`;
3. the diagonal countable atom-loop shift, with one primitive loop per atom,
   no mixed loops, and repetition length `r log p`;
4. the diagonal trace-class operator and its Fredholm determinant, only for
   `Re(s) > 1`;
5. the exact Euler/Dirichlet identity `Z_tensor(s) = zeta(s)` and its von
   Mangoldt logarithmic derivative in that half-plane.

The right-hand rail is a claim boundary, not another forward implication:

- **A3 BLOCK:** the construction currently supplies no intrinsic analytic
  continuation, Gamma factor, or functional equation;
- **ROUTE B LOCKED:** it supplies neither a self-adjoint operator nor a
  zero/divisor correspondence.

In particular, the figure does not identify the half-plane Fredholm
determinant with a completed `zeta` or `xi` determinant.

## Visual semantics and accessibility

- Blue solid boxes/arrows are exact algebraic identities.
- Orange boxes/arrows mark the modeling bridge and the `Re(s) > 1`
  analytic domain; the orange dashed box marks the A3 stopping boundary.
- Gray short-dashed styling marks the locked operator route.
- Every color class is redundantly labeled in text (`EXACT`, `CONSTRUCTION`,
  `HALF-PLANE`, `A3 BLOCK`, `ROUTE B LOCKED`). Border and line patterns
  remain distinct in grayscale, so the logical status does not depend on
  color perception.
- There is no decorative title inside the asset; the surrounding paper owns
  the caption and cross-reference.

## Deliberate scope limits

The diagram uses only the finite-full-shift tensor family and the derived
diagonal symbolic system. It does not invoke another dynamical system family,
does not claim an intrinsic critical-strip continuation, and does not unlock
Route B.
