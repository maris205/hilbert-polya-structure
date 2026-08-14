# SOURCE LOCK — SD-C21

**Title:** *A Semiring Sieve Shift: Exact Euler Determinant, Recurrent-Core
Collapse, and a Factorial-Monoid Compiler No-Go*
**Freeze date:** 2026-08-14
**Primary family:** Symbolic Dynamics
**Object:** one-sided countable deterministic Markov shift and a weighted
vertex-adjacency operator
**Status:** exact construction plus scoped obstruction

## 1. Full-shift semiring skeleton

Choose an $n$-element alphabet $A_n$ and write
$F_n=A_n^{\mathbb Z}$, up to topological conjugacy.  Freeze

\[
F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},\qquad
F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n}.
\]

The symbol $\boxplus$ means **alphabet-sum**, equivalently alphabet
coproduct followed by the full-shift functor.  It is not called a categorical
coproduct of subshifts: the full shift on $A_m\sqcup A_n$ contains mixed
sequences and is not the topological disjoint union of $F_m$ and $F_n$.

The frozen intrinsic data are

\[
h(F_n)=\log n,\quad
S(F_d)=F_d\boxplus F_1=F_{d+1},\quad
F_a<F_b\Longleftrightarrow
F_a\boxplus F_c=F_b\text{ for some }c\ge1.
\]

The two operations are invariant under alphabet relabeling.  On this chosen
skeleton they reproduce the positive-integer semiring; this is a structural
source relation, not a new universal property of Symbolic Dynamics.

## 2. Expanded deterministic graph

For every $n\ge2$, the forward orbit starts at $I_n$.  Its states are

- $I_n$: input;
- $T_{n,d}$: divisor/square-test, beginning at $d=2$;
- $Q_{n,d,q}$: explicit quotient search, beginning at $q=2$;
- $A_n$: accept;
- $R_{n,k}$, $k\ge1$: one-way cemetery.

The transitions are

\[
I_n\longrightarrow T_{n,2},
\]

\[
T_{n,d}\longrightarrow
\begin{cases}
A_n,&d^2>n,\\
Q_{n,d,2},&d^2\le n,
\end{cases}
\]

and

\[
Q_{n,d,q}\longrightarrow
\begin{cases}
Q_{n,d,q+1},&dq<n,\\
R_{n,1},&dq=n,\\
T_{n,d+1},&dq>n.
\end{cases}
\]

Finally,

\[
A_n\to A_n,\qquad R_{n,k}\to R_{n,k+1}.
\]

All comparisons are implemented using $\boxtimes$, successor, and the
alphabet-sum order.  The square test occurs before quotient search, so
$n=2,3$ are accepted.  The graph is the union of the unique forward orbits
of all seeds $I_n$, together with the infinite cemetery continuations.
The cemetery is never an absorbing loop.

An edge rule of the form “reject iff $d\mid n$” is forbidden in the source
definition.  It may be used later only as a proved macro for the expanded
$Q_{n,d,q}$ search.

## 3. One-sided phase space

Let $G$ be the frozen graph and $X_G^+$ its one-sided edge shift.  The
verifier is not presented as a two-sided shift: source states without an
infinite legal past would disappear from that phase space.  All operator
statements use the vertex space $\ell^2(V(G))$.

## 4. Frozen roofs

The prototype-consistent roof convention is

\[
\tau(I_n,T_{n,2})=\log(2n),
\]

\[
\tau(T_{n,d},A_n)=\log(nd),\qquad
\tau(T_{n,d},Q_{n,d,2})=\log(2nd),
\]

\[
\tau(Q_{n,d,q},\mathrm{next})=\log(ndq),
\]

\[
\tau(R_{n,k},R_{n,k+1})=\log(n(k+1)),\qquad
\tau(A_n,A_n)=\log n.
\]

Each value is an entropy of a tensor product of source objects.  The extra
factor $2$ on $T\to Q_{n,d,2}$ records the first explicit quotient state.

The accept-loop roof $h(F_n)=\log n$ is canonical on the full-shift
skeleton after the program accepts $n$.  Every transient roof is a frozen
`MODELING_CHOICE`, not a canonical consequence of trial division.  It is
chosen to make the raw adjacency trace class.  Any locally uniformly
summable replacement on transient edges leaves all power traces and
Fredholm determinants unchanged.

## 5. Operator and determinant

On $\mathcal H=\ell^2(V(G))$, with basis $\delta_v$, freeze the
arrival-weighted vertex adjacency

\[
L_s\delta_u=\sum_{e:u\to v}e^{-s\tau(e)}\delta_v,
\qquad \operatorname{Re}s>1.
\]

The graph has one outgoing edge at every vertex.  The operator is called a
**weighted vertex-adjacency** or **graph transfer**.  It is not called a
Ruelle operator: no Banach space of potentials or thermodynamic-formalism
theorem is being invoked.

Freeze

\[
D_{\mathrm{SV}}(s,z)=\det_{\mathcal H}(I-zL_s),\qquad
D_{\mathrm{SV}}(s)=D_{\mathrm{SV}}(s,1).
\]

## 6. Primitive and repetition ledger

The only primitive directed cycles are

\[
\gamma_p=[A_p],\qquad p\text{ prime}.
\]

Their $r$-fold temporal repetitions have weight $p^{-rs}$, multiplicity
one.  There are no mixed cycles.  Reject rays and all verifier states are
acyclic and contribute to no diagonal coefficient of $L_s^r$.

## 7. Controls and forbidden data

Forbidden inputs are prime tables, zero tables, logarithmic-prime tables,
fitted phases, post-hoc accepted-loop insertion, and any hidden
factor-existence guard.  An independent sieve is allowed only in the sealed
finite validation path.

Mandatory controls are alphabet relabeling, bounded trial depth, shifted
factorization, polynomial UFDs, matched random supports, and universal total
deciders.  Exact agreement for these controls is evidence of implementation
correctness and of the `PROVES_TOO_MUCH` obstruction, not evidence for RH.

## 8. Frozen verdict

~~~text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED

GO_SOURCE_INTRINSIC_SEMIRING_VERIFIER
GO_EXACT_PRIMITIVE_REPETITION_LEDGER
GO_WHOLE_OPERATOR_TRACE_CLASS_RE_GT_1
GO_SAME_OBJECT_EULER_FREDHOLM_IDENTITY

STOP_RECURRENT_ARITHMETIC_ADVANCE
STOP_GLOBAL_ANALYTIC_STRUCTURE
STOP_ARITHMETIC_SELECTIVITY
SELECTOR_TAUTOLOGICAL
PRUNING_EQUIVALENT
PROVES_TOO_MUCH
~~~
