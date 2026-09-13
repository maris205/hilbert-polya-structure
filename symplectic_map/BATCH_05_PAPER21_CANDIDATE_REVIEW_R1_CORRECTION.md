# Paper21 R1 correction — third-selector gap

This correction supersedes exactly the third-selector expansion in
BATCH_05_PAPER21_CANDIDATE_REVIEW_R1.md; no other R1 conclusion changes.

For
\[
v=Au,\qquad u_1=1,\qquad
v_1=g-1,\quad v_2=2+x+2y,\quad v_3=2+2x+y,
\]
the third component of \(\nabla W\) is
\[
2p_1^2p_2^2p_3+g p_3^{g-1}.
\]
Therefore the pure-minus-mixed degree gap is
\[
\begin{aligned}
 (g-1)v_3-(2v_1+2v_2+v_3)
 &= (g-2)v_3-2v_1-2v_2\\
 &= (2g-6)x+(g-6)y-6.
\end{aligned}
\]
\[
(2g-6)x+(g-6)y-6\ge 6
\]
for \(g\ge8\) and \(x,y\ge1\), with equality at \(g=8,x=y=1\).
Thus the third selector remains strict on the full declared cone, and all
subsequent matrix, cone, visibility, no-cancellation, Perron, and row-sum
arguments remain valid. The R1 PASS verdict and scores \(8.2/8.4/9.1\) are
unchanged.

PAPER21_CANDIDATE_GATE_PASS_R1_CORRECTED
