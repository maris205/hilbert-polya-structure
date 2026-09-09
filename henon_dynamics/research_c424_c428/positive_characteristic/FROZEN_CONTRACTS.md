# Initial positive-characteristic scout: two frozen questions

Frozen on 2026-09-08 UTC, before any new mathematical program or
nontrivial candidate calculation. This is a bounded research contract,
not an admission, theorem announcement or manuscript assignment.
Only two of the allowed three envelopes are used. All claims below are
questions generated in this scout unless explicitly attributed in the
subsequent source audit.

## PC424-D — native p-power dynatomic components

- Map and family: $f_c(x)=x^2+c$, every odd prime $p$, over
  $k=\overline{\mathbb F}_p$, with the entire parameter line $c\in k$.
- Native clock: one application of $f_c$; the selected infinite tower is
  $n=p^e$, for **every** integer $e\geq1$. This is not a Frobenius clock,
  an inverse-tree height or a fixed finite-field point census.
- Domain and object: the full affine plane with coordinates $(x,c)$,
  and the reduced geometric curve cut out by the reduction modulo $p$
  of the integral dynatomic polynomial
  \[
  \Phi_{p^e}(x,c)=
  \frac{f_c^{\circ p^e}(x)-x}{f_c^{\circ p^{e-1}}(x)-x}.
  \]
  Reduction of this polynomial and taking the reduced curve are explicit
  operations; a singularity or nonreduced scheme structure is not itself
  a geometric component count. Formal period is not automatically exact
  period on parabolic parameter fibres.
- Complete question: classify the geometric irreducible components of
  this reduced curve for all odd $p$ and all $e\geq1$. In particular,
  determine whether the entire tower is geometrically irreducible, and
  if not give a uniform component mechanism and the full exceptions.
- Intended arithmetic carrier: the native cyclic action
  $(x,c)\mapsto(f_c(x),c)$ on formal periodic-point moduli in the wild
  case $p\mid n$, not an imported prime labeling of a known spectrum.
- Closest inputs to subtract: the bad-reduction criteria and conditional
  irreducibility results of Doyle–Krieger–Obus–Pries–Rubinstein-Salzedo–West;
  Doyle–Poonen's theorem about geometric irreducibility of already
  irreducible factors; local C12/C23 dynatomic/Frobenius/discriminant work.
  All good-reduction or componentwise conclusions retain their original
  hypotheses and cannot silently imply irreducibility of \(\Phi_{p^e}\).
- Residual required increment: an all-$(p,e)$ connectedness/component
  theorem across the wild native-period tower. A new small-prime factor
  table, one parabolic germ, or one good-reduction criterion is insufficient.
- Cheap decisive test: inspect the closest source hypotheses specifically
  at $p\mid n$, and test whether their monodromy or local special-fibre
  argument actually supplies global connectedness. No large polynomial
  factorization census is authorized by this contract.
- Replacement boundary: if the all-tower component step is absent, mark
  UNCLOSED. Do not replace this question by a single $e=1$ calculation,
  a local cusp, or a finite list of primes while keeping its identity.

## PC424-L — polynomial additive cocycles over the quadratic family

- Map and family: $T_{c,h}(x,y)=(x^2+c,y+h(x))$ on **all** of
  $\mathbb A^2(k)$, for every odd prime $p$, every $c\in k$,
  and every $h\in k[x]$, with $k=\overline{\mathbb F}_p$.
  Any finite-field specialization must contain all coefficients and be
  distinguished from the geometric quantifier over all finite extensions.
- Native clock: one forward application of $T_{c,h}$, whose base is
  $f_c=x^2+c$; there is no Frobenius in the fibre update.
- Observable: for each **ordinary geometric primitive periodic orbit**
  $O$ of $f_c$, the additive sum $S_h(O)=\sum_{a\in O}h(a)\in k$.
  Each distinct orbit point is counted once. This is not an intersection
  multiplicity or scheme length, and not a sum over an $n$-fold repeated
  orbit, which could vanish merely because $p\mid n$.
- Complete question: classify the kernel
  \[
  K_c=\{h\in k[x]:S_h(O)=0\text{ for every primitive periodic orbit }O\}
  \]
  relative to polynomial vertical-shear coboundaries
  \[
  B_c=\{Q\circ f_c-Q:Q\in k[x]\}.
  \]
  Is $K_c=B_c$ for the entire family? If not, a retained paper-level
  contract must classify the extra classes or supply a complete uniform
  obstruction mechanism, not just one low-degree counterexample.
- Intended arithmetic carrier: additive monodromy along the native
  nonlinear base cycles. The elementary return translation by $S_h(O)$
  and its order $1$ or $p$ are background, not the proposed theorem.
- Closest local mechanisms to subtract: old PC414-S has
  $(x^2,y^p+P(x))$ and asks inverse identifiability of joint ledgers; its
  radicial $P/P^p$ ambiguity is not this map or kernel. Old NC2 has a
  Frobenius base and quadratic Artin–Schreier trace sums. Carlitz/rank-two
  additive module classifications, C401/C404 semilinear Hénon, C410 inverse
  trees, and C415/C418/C423 binomial/periodic-parameter mechanisms are
  excluded. Merely changing their exponent or scalar does not reopen them.
- Residual required increment: a polynomial-regularity theorem or complete
  defect classification converting all ordinary orbit-sum data into the
  algebraic quotient $k[x]/B_c$, uniformly in $(p,c)$.
- Cheap decisive test: compare the tautological orbitwise transfer
  solution with polynomial degree constraints. Verify whether a uniform
  transfer-degree bound, rather than finite-field interpolation alone,
  can be justified; distinguish finite-level solvability from global
  polynomial solvability. Only short hand arguments are planned initially.
- Replacement boundary: if the passage from every finite orbit to a
  single polynomial transfer remains unsupported, mark UNCLOSED.
  Do not advertise the elementary period-$p$ lift, bounded-degree
  interpolation, or the old radicial ambiguity as a solution.

## Admission and audit boundary

The subsequent SOURCE_AUDIT is source-role work; the SCOUT_REPORT is
mathematical disposition. No source search certifies worldwide novelty.
No new manuscript, formal evaluation, target Euler factor, root number,
automorphy, divisor/zero correspondence or Hilbert–Pólya realization is
claimed. Only the coordinator may admit a surviving full contract.
