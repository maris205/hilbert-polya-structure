# Figure specification: intrinsic grading and duality audit

## Asset contract

- Asset: \`figures/grading_duality_map.tex\`
- Format: pure TikZ source; vector output after LaTeX compilation
- Intended placement: full paper width (\`\linewidth\`)
- Inclusion contract: the asset begins with \`\begin{tikzpicture}\` and ends
  with \`\end{tikzpicture}\`; it contains no float, caption, label, document
  preamble, or internal title

Recommended inclusion:

\`\`\`latex
\begin{figure}[t]
  \centering
  \input{figures/grading_duality_map}
  \caption{...}
  \label{fig:grading-duality-map}
\end{figure}
\`\`\`

Required preamble support:

\`\`\`latex
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}
\`\`\`

The formulas assume the paper's normal AMS math support.

## Logical content

The source node is the already constructed SD-C07 tensor-prime symbolic
system: tensor atoms \(F_p\), entropy lengths \(\log p\), and the diagonal
transfer operator \(\mathcal L_s e_p=p^{-s}e_p\).

Three branches are kept separate.

1. **Koszul/exterior branch.**  After choosing the canonical Koszul functor,
   tensor atoms have homological degree one.  This fixes the Euler
   orientation exactly:
   \[
   \operatorname{Ber}_{V_{\bar 1}}(I-\mathcal L_s)=\zeta(s),\qquad
   \operatorname{Str}\Gamma(\mathcal L_s)
      =\det(I-\mathcal L_s)=\zeta(s)^{-1}
   \]
   for \(\operatorname{Re}s>1\).  The figure labels this as an A2 gain, not
   as analytic continuation.
2. **Stable/unstable branch.**  Natural symbolic reversal returns
   \(\mathcal L_s\oplus\mathcal L_s\): it sends \(s\) to \(s\), not to
   \(1-s\).  Thus it does not intrinsically produce the Riemann duality.
3. **Tensor-group-completion branch.**  In
   \(\mathbb Q_{+}^{\times}\), inversion sends \(s\) to \(-s\), and every
   monoidal \(\mathbb Z/2\)-parity is unchanged by inversion.  A
   \(1/2\)-centering twist is therefore extra structure.

An orange dashed adversarial node grants that extra \(s\leftrightarrow1-s\)
pairing temporarily and records the strongest regularized object:
\[
D_3(s)=\det\nolimits_3(I-\mathcal L_s)
       \det\nolimits_3(I-\mathcal L_{1-s}),\qquad
\tfrac13<\operatorname{Re}s<\tfrac23 .
\]
It is symmetric but zero-free in that strip, and its logarithm starts at
repetition \(r=3\); the prime and prime-square traces \(r=1,2\) have been
removed.  This is an obstruction test, not a candidate promotion.

The footer is the frozen stage verdict:
\[
\textsf{GO A2}\;/\;\textsf{STOP A3}\;/\;\textsf{ROUTE B LOCKED}.
\]

## Visual semantics and accessibility

- Blue solid borders and arrows mean **proved exact symbolic algebra**.
- Orange densely dashed borders and arrows mean **conditional pairing or
  analytic boundary**.
- Gray dotted borders and arrows mean **structural obstruction / locked
  route**.
- Every color class is redundantly named in uppercase text.  Border styles,
  arrow styles, and wording preserve the logic in grayscale.
- There is no color-only legend and no decorative title inside the asset.
- Text is set at footnote size, with compact formulas chosen to remain
  readable at full A4 text width.

## Scope discipline

Only the finite-full-shift tensor family, its atom-loop transfer operator,
Koszul/exterior functors, symbolic reversal, and tensor group completion are
shown.  No other dynamical system family is introduced.  The diagram does
not claim a Gamma factor, intrinsic functional equation, self-adjoint
operator, or zero/divisor correspondence.
