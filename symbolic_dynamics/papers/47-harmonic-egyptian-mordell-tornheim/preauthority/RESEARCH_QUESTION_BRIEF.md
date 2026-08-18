# Research Question Brief — Paper 47

## Narrow question

For the looped graph on positive integers whose endpoints satisfy

$$
m+n\mid mn,
$$

what is the exact operator-ideal phase diagram of its canonical
Dirichlet-weighted adjacency, and does the graph realize a classical multiple
Dirichlet series intrinsically as a same-object trace rather than importing
that series as a fitted analytic decoration?

## Frozen answer

Let

$$
E_s(m,n)=\mathbf 1_{\{m+n\mid mn\}}(mn)^{-s/2},
\qquad \sigma=\Re s.
$$

Then \(E_s\) is bounded and compact exactly for \(\sigma>0\),
Hilbert–Schmidt exactly for \(\sigma>1/2\), and trace class exactly for
\(\sigma>1\).

Every ordered edge has the unique form

$$
m=t\,a(a+b),\qquad n=t\,b(a+b),
\qquad t\ge1,\quad (a,b)=1.
$$

The loops are exactly \(m=n=2t\). Consequently,

$$
\operatorname{Tr}(E_s)=2^{-s}\zeta(s)
\quad(\sigma>1),
$$

and

$$
\operatorname{Tr}(E_s^2)
=\frac{\zeta(2s)}{\zeta(4s)}
 \cdot\zeta_{\rm MT}(s,s;2s)
\quad(\sigma>1/2),
$$

where the Mordell–Tornheim series is

$$
\zeta_{\rm MT}(s,s;2s)
=\sum_{a,b\ge1}a^{-s}b^{-s}(a+b)^{-2s}.
$$

The coprime factor is not an analogy: it is exactly the primitive
Mordell–Tornheim sum produced by the edge parameterization.

## Why this is paper-sized

The elementary Egyptian-fraction parameterization and the classical
Mordell–Tornheim series receive no novelty credit. The indivisible remainder
is the realization theorem: one frozen arithmetic graph simultaneously owns
the unique coprime-scale edge parameterization, sharp ideal walls,
zeta-valued first trace, its \((s,s;2s)\) primitive Mordell–Tornheim second
trace, and genuinely mixed cycles.

If the second-trace identity is demoted to an example, the project becomes a
short repetition of Paper 46's ideal staircase and must stop as salami.

## Non-goals

- no novelty claim for Egyptian fractions or Mordell–Tornheim identities;
- no loop deletion;
- no all-\(S_q\) theorem beyond \(q=1,2\);
- no claim that the operator is positive semidefinite;
- no rational-prime primitive ledger;
- no Riemann-zero fit, completed zeta, or Hilbert–Pólya claim;
- no authority, Git, README, Route-B, or publication authorization.

## Status

PROVABLE AS STATED / PREAUTHORITY THEORY INPUT
