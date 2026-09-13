# Orbit-linear gauge proof: literal parameter-symbol erratum

Date: 2026-09-06. Author correction to one text encoding error. The frozen
190-line input `PAPER30_ORBIT_LINEAR_GAUGE_PROOF_20260906.md`, SHA256
`2f6e4e603fef5ca331e0f829c4493d426c0e57bf62e930c17e1ac3b965e7a183`,
is preserved unchanged.

At line 28, the second occurrence of the LaTeX parameter command contains
a vertical-tab control character instead of its initial backslash-v pair.
The intended complete formula is

$$
C_\varepsilon=
\exp\!\left(\operatorname{ad}_{\varepsilon h+
\varepsilon^2h_2+\cdots}\right).
$$

Both occurrences refer to the same formal parameter $\varepsilon$. This
matches the later proof's definition of $H_\varepsilon$ and its BCH
calculation; no assumption, coefficient, order, or conclusion is changed.

The issue was identified by the fresh structural mathematical reviewer.
This record acknowledges and corrects the literal error; the independent
mathematical conclusion is recorded separately in that reviewer's report.
