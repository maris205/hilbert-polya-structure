# SOURCE LOCK — SD-C17

## Identity and scope

```yaml
candidate_id: SD-C17
title: tensor-atom Koszul subset shift
primary_system_family: Symbolic Dynamics
route_b_invocation_allowed: false
status: frozen
```

SD-C17 is a symbolic edge shift and nothing else.  No geometric flow,
Hamiltonian, quantum graph, operator model, Riemann-zero table, Gamma factor,
functional equation, or critical-strip fit is admissible.  An idea that needs
one of those objects is recorded only in `ROUND2_CLUES.md`.

## Tensor source and formal finite restrictions

Let

\[
  \mathcal M=\{F_n:n\ge 1\},\qquad
  F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n,
\]

where \(F_n\) is the full shift on \(n\) symbols.  The tensor atoms of
\(\mathcal M\) are the irreducible objects \(F_p\).  This intrinsic
factorization, rather than an externally supplied prime table, is the
arithmetic source.

For every finite atom set \(A\subset\operatorname{Atom}(\mathcal M)\), attach
one formal variable \(x_a\) to each \(a\in A\).  Write

\[
  x_S=\prod_{a\in S}x_a,
  \qquad
  \epsilon(S)=(-1)^{|S|+1}
\]

for every nonempty subset \(S\subseteq A\).  These finite formal restrictions
are the primary algebraic certificates.  Their compatibility under
inclusions of atom sets defines the countable candidate.

## Phase space, grammar, clock, and scalar potential

The edge alphabet is

\[
  \mathcal E_A=\{S\subseteq A:S\ne\varnothing\}.
\]

SD-C17 is the one-vertex full edge shift on \(\mathcal E_A\), or on all finite
nonempty subsets of the countable tensor-atom set in the countable limit.
Reflection is not an orbit equivalence.  Closed words are identified only
under cyclic rotation.

An edge \(S\) has roof and scalar weight

\[
  T(S)=\sum_{a\in S}h(a),
  \qquad
  w_s(S)=\epsilon(S)e^{-sT(S)}.
\]

The sign \(\epsilon(S)\) is an ordinary scalar edge coefficient.  It is not a
chain degree, orientation line, supertrace sign, or fermionic parity.
Temporal repetition always uses the actual scalar power

\[
  w_s(S)^r=\epsilon(S)^r e^{-rsT(S)}.
\]

## Transfer and determinant convention

The vertex function space is \(\ell^2(\{*\})\cong\mathbb C\).  Put

\[
  \mathcal F_A(x)=
  \sum_{\varnothing\ne S\subseteq A}(-1)^{|S|+1}x_S,
  \qquad
  L_{A,x}c=\mathcal F_A(x)c,
\]

and freeze

\[
  D_A(x,z)=\det_{\mathbb C}(I-zL_{A,x})
           =1-z\mathcal F_A(x).
\]

At \(z=1\), inclusion--exclusion gives

\[
  D_A(x,1)=\prod_{a\in A}(1-x_a).
\]

For the countable tensor specialization \(x_{F_p}=p^{-s}\), the alphabet sum
is absolutely convergent for \(\operatorname{Re}s>1\), since

\[
  \sum_{\varnothing\ne S}|w_s(S)|
  =\prod_p(1+p^{-\operatorname{Re}s})-1<\infty.
\]

In that domain,

\[
  D_{\infty}(s,1)=\prod_p(1-p^{-s})=\zeta(s)^{-1}.
\]

This is the determinant of the frozen one-vertex symbolic adjacency.  It is
not a completed-zeta determinant and makes no claim in the critical strip.

## Koszul interpretation and firewall

For \(A=\{a_1,\ldots,a_k\}\), the polynomial algebra
\(R_A=\Bbbk[x_{a_1},\ldots,x_{a_k}]\) has a Koszul resolution with one basis
line for every subset of \(A\).  The polynomial above is its decategorified
alternating subset inventory.  This observation motivates the name
"Koszul subset shift".

It does **not** identify the scalar shift with the Koszul chain complex.
Exterior orientation, the Koszul differential, chain homotopies, and
supertraces are absent from the frozen candidate.  Any chain-enhanced model
would be a new candidate and must freeze its chain groups, differential,
cyclic action, power maps, and graded determinant before evaluation.

## Primitive and repetition ledger

Whenever \(|z\mathcal F_A(x)|<1\),

\[
  -\log D_A(x,z)
  =\sum_{r\ge1}\frac{z^r}{r}\mathcal F_A(x)^r
  =\sum_{\gamma\ \mathrm{primitive}}
    \sum_{r\ge1}\frac{z^{r|\gamma|}w(\gamma)^r}{r}.
\]

A primitive orbit is a primitive cyclic necklace of subset edges.  Every
report must keep separate:

1. primitive necklaces at the target multidegree;
2. repetitions of primitives from lower multidegrees;
3. their exact \(1/r\) trace-log factors;
4. the aggregated scalar coefficient.

An aggregate zero is not evidence of a primitive-level involution.

## Naturality and no-lift gate

A proposed primitive cancellation or Morse reduction is admissible only if
it is fixed before orbit enumeration and simultaneously:

- preserves tensor content and the entropy roof;
- commutes with cyclic rotation and temporal power maps;
- is equivariant for every finite permutation of the atom set;
- preserves the frozen scalar trace at every repetition order;
- distinguishes scalar signs from chain parity;
- leaves a nontrivial determinant sector if it is advertised as a determinant
  mechanism.

Lexicographic matchings, chosen atom orders, selected cyclic orientations,
and cutoff-dependent pairings are forbidden presentation choices.

## Allowed and forbidden data

Allowed:

- tensor products and intrinsic entropy of finite full shifts;
- finite subsets of intrinsic tensor atoms;
- formal variables and exact integer/rational arithmetic;
- primitive necklaces, cyclic actions, bar/Koszul/Hochschild complexes;
- classical homological and representation-theoretic theorems;
- randomized formal inventories as `PROVES_TOO_MUCH` controls.

Forbidden:

- target Riemann zeros or any fitted spectral data;
- a prime mask, Möbius coefficient, or von Mangoldt weight in the edge rule;
- replacing \((-w)^r\) by \(-w^r\);
- discarding temporal repetitions after inspecting a coefficient;
- a cross-family carrier or Route-B operator.

## Frozen route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The positive result is an exact same-object scalar determinant.  The stopping
result is a primitive-cycle no-lift theorem under the naturality gate above.
Universality over arbitrary formal inventories triggers
`STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.
