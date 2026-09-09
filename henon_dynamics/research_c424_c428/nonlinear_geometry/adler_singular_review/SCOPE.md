# Independent singular-fibre check within NL424-3

2026-09-08 UTC. This is a bounded subproblem of the existing, full Adler
contract, **not a new candidate, manuscript, admission or formal evaluation**.
Only this directory is authored by the singular-fibre reviewer.

The corrected [frozen contract](../FROZEN_SCOUTS.md) and
[scout report](../SCOUT_REPORT.md) were read in full before this work.
The native map, ordered parameters, factorwise two-sided regular domain,
equal-parameter cancellation and the complete invariant map are unchanged:
$$
T_\beta=R_{\beta_1,\beta_3}^{13}\circ R_{\beta_1,\beta_2}^{12},
\qquad
R_{b,c}(x,y)=\left(y-\frac{b-c}{x+y},
x+\frac{b-c}{x+y}\right),
$$
where $R_{b,b}$ is an everywhere-defined swap. One whole $T_\beta$ is
one tick. Parameters stay attached to their sites.

The invariant map is $(S,H_\beta)$ as defined in the parent contract.
On every rational level $(S,H_\beta)=(S_0,h)$ introduce
$$
u=x_1+x_2,\quad v=x_2+x_3,\quad w=x_3+x_1,\quad t=2S_0,
$$
$$
a=\beta_3-\beta_2,\quad b=\beta_1-\beta_2,\quad
\gamma=\beta_2t-h.
$$
The affine cubic is
$$
C:\quad uv(t-u-v)+au+bv+\gamma=0,\qquad w=t-u-v.
$$
All parameters and ordinary points in this review are rational unless a
geometric statement explicitly uses $\overline{\mathbb Q}$.

The assigned checks are:

1. Geometric reducedness, points at infinity and the complete reducibility
   criterion of these level cubics.
2. For every geometrically irreducible singular level, an explicit
   normalization, native Möbius action, exact two-sided regular domain,
   and classification of its ordinary rational periodic points.

The coordinator owns the reducible line/conic dynamics. Another reader
owns smooth-fibre translation and source/pole analysis. Those cases are
not solved or silently imported here. The original all-fibre NL424-3
question therefore is not declared solved by this review.

The previously read proof-writer instructions govern the proof package.
No mathematical program, parameter census, source search, old rerun,
author-document edit, TeX or formal evaluation was used. The analysis is
explicit hand algebra; no elliptic group-law origin or flex is assumed.
