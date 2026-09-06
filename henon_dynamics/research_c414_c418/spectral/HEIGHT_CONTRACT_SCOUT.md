# Native Hénon canonical-height counting: candidate, not admission

## Frozen mathematical question

Let $q$ be any prime power, $d\ge2$, $f\in\mathbb F_q[X]$ have
degree $d$, and $a\in\mathbb F_q^\times$. Put
$H(x,y)=(y,f(y)-ax)$ on $\mathbb F_q[t]^2$. The domain is polynomial
points, not all of $\mathbb F_q(t)^2$. Put
$h(x,y)=\max(0,\deg x,\deg y)$, with $\deg0=-\infty$, and
$\widehat h^\pm(P)=\lim_{n\to\infty}d^{-n}h(H^{\pm n}P)$.
The observable is the native **two-sided canonical-height** sum
$\widehat h=\widehat h^++\widehat h^-$ and its counting Dirichlet series
$Z_H(s)=\sum_{P\in\mathbb F_q[t]^2}q^{-s\widehat h(P)}$.
This is a point-height series, not an ordinary periodic-orbit zeta or an
arbitrary reparametrization of the iteration clock.

Question: determine this complete height distribution and its complex
continuation uniformly in $q,d,f,a$. In particular, is the distribution
independent of lower coefficients and Jacobian, and does its continuation
have infinitely many genuine poles accumulating at every point of
$\Re s=0$? This prospective boundary conclusion is NOT proved yet.

## Classical baseline versus proposed increment

Kawaguchi/Ingram supply canonical heights and local escape theory for Hénon
maps. Hsia and Takehira treat dynamical height zeta/counting in other settings;
Takehira's retrieved 2024 arXiv paper and 2025 journal record concern polarized
one-dimensional maps and explicit global-function-field examples. These are
inputs/nearby owners, not claims of new definitions or new general Northcott
theory. Relevant exact source statements still require line-level checking.

The proposed increment is an explicit cancellation-aware orbit decomposition,
an exact universal all-polynomial-point height series, and its true pole and
boundary structure. A parameter table, the mere existence of a canonical
height, or a standard height-count asymptotic alone will not qualify.

## Cheap decisive check and current derivation

Every nonconstant bi-infinite polynomial orbit appears to have exactly one
of two distinguished degree valleys:

1. one edge $(x,y)$ with positive degrees $m,n$ and
   $m<dn$, $n<dm$;
2. one falling-to-rising turn $(x,y)$ with $\deg x=M\ge1$,
   $d\max(0,\deg y)\le M$ and
   $\deg(f(y)-ax)=M$.

The strict edge has height pair $(\widehat h^-,\widehat h^+)=(m,n)$.
The turn has pair $(M,M/d)$ and two adjacent equal minimum total heights.
All orbit iterates scale the pair by $(d^{-k},d^k)$. If this decomposition
is not disjoint/exhaustive, or coefficient-dependent cancellation changes its
cardinality, the proposed universality must be corrected or rejected.

The proposed edge multiplicity is $(q-1)^2q^{m+n}$. Summing admissible
middle degrees, the proposed turn multiplicity for $M=dk+r$ is

$$
D_M=\begin{cases}
(q-1)^2q^{(d+1)k},&r=0,\quad k\ge1,\\
(q-1)q^{(d+1)k+r+1},&1\le r\le d-1,\quad k\ge0.
\end{cases}
$$

First verification will independently compute heights by actual polynomial
iteration until provable escape, and compare the resulting finite exact
distribution to the orbit formula. Symbolic residue analysis must distinguish
true poles from cancellation between adjacent valley sectors; nonzero
summands alone never prove a boundary of their sum.

## Replacement and route boundary

Reject this candidate if the full formula is directly present in a primary
owner, if only the elementary leading height count survives, or if a required
infinite decomposition/continuation cannot be proved. Do not move from
polynomial to rational points silently. Finite tests do not prove the theorem.
The source function field and height are intrinsic, but no target Euler
factors, root number, automorphy, Riemann divisor or Hilbert–Pólya operator
has been constructed. This lane changed from an operator-first screen to
native arithmetic height counting for a concrete reason: the latter supplies
a new exact arithmetic observable without reusing a previously excluded
GCD/LCM or delta-chain operator.

Status: `NOT_CURRENTLY_JUSTIFIED` as a complete paper contract; proof and
source ownership are active. No C-number or formal route grade is assigned.
