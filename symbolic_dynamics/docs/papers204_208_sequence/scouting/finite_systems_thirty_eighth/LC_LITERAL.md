# LC: least-positive collector — exact desk literal, no pilot authorization

2026-09-07 UTC. This is the lane's first new exact literal. Author:
`/root/thirty_third_finite_scout`. No mathematical or source review is claimed.

Parameters: integers $m\geq1$ and $N\geq0$. The finite carrier is

$$X_{m,N}=\{x\in\mathbb Z_{\geq0}^m:\sum_{i=1}^m x_i=N\}.$$

For $x$, let $S=\{i:x_i>0\}$ and $k=|S|$. If $k=0$, hold the zero
vector. Otherwise let $p$ minimize $(x_i,i)$ lexicographically over $S$,
and update simultaneously by

$$F(x)_p=x_p+k-1,\qquad
F(x)_i=x_i-1\ (i\in S\setminus\{p\}),\qquad
F(x)_i=0\ (i\notin S).$$

There is no graph parameter, threshold cap, post-update sorting, hidden
phase flag or repaired negative coordinate. Only currently positive bins
donate, and exactly one least-positive bin is selected, with the least-label
tie rule. A one-bin support is fixed. The carrier is closed since all donors
were positive, the collector stays positive, and total mass is preserved.

Known mechanisms to deduct before any pilot:

- For fixed support size $k$, the affine change $z_i(t)=x_i(t)+t$
  leaves unselected priorities fixed and adds $k$ to the least priority.
  This is a greedy equal-step priority queue, also the sign-reversed
  complete-graph chip-firing increment. No full-carrier conjugacy to one
  fixed graph is asserted, because supports may shrink.
- Earlier graph/resource GLD sends only from strictly higher loads, and
  RMA sends whole piles to a closed-neighbourhood maximum. Neither is
  this literal. Their occupied resource-transfer and selector boundaries
  are relevant; an altered tie rule is not itself a new contribution.
- Extinct donor bins must have old load one. Undoing a proposed collector
  and choosing those erased unit bins is the expected inverse mechanism.
  A binomial implementation of that ordinary selector inversion does not
  automatically supply a material independent second residual.

Current source priority: Li–Propp, *A Greedy Chip-firing Game*, arXiv
2102.00346 / published RSA 62(3) (2023), 645–666. Its actual primary
definition/proof must be inspected before transferring a theorem or
claiming exact identity. Search snippets alone are not clearance.

No pilot box is declared or executed. The proof/source subtraction may
close this literal negatively before any numerical work. Do not enlarge
the map to another allocation rule or re-label old NED/other proof holds.
