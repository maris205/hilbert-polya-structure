# Research question and theorem contract

For every finite integer \(d\ge1\), constant \(W\in\mathbb R^d\), and
control cap \(c\ge0\), solve the minimum-time problem
\[
\dot x(t)=W+u(t),\qquad |u(t)|\le c,\qquad x(0)=0,
\]
for every target displacement \(y\in\mathbb R^d\).

The required theorem must not be a weak-wind slice. It must give:

1. exact-time reachable sets and every attainable-time set;
2. full reachability conditions and exact \(T(y)\) in weak, critical, and
   strong wind;
3. the correct smaller-root choice in strong wind;
4. uniqueness and explicit form of the time-optimal control;
5. positive homogeneity, rotations, common velocity scaling, HJB, and
   regularity at the critical half-space and strong Mach cone;
6. separate handling of \(W=0\), \(c=0\), and \(y=0\), including the
   degenerate \(W=c=0\) corner.

The contract excludes variable winds, obstacles, state constraints, and
manifold navigation. In particular, the strong-wind finite-value cone is not
promoted to a global Finsler norm.
