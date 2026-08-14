# SOURCE LOCK — SD-C18

## Identity and scope

```yaml
candidate_id: SD-C18
title: character-resolved cycle-index determinant of the tensor-atom shift
primary_system_family: Symbolic Dynamics
paper_project: 16-equivariant-cycle-index-determinant
route_b_invocation_allowed: false
status: frozen
```

SD-C18 is a formal equivariant refinement of the one-vertex Koszul-subset
shift.  The primary objects are finite signed symbolic edge shifts, their
primitive cyclic words, and the Burnside/representation/cycle-index ledgers
carried by atom relabelings.  A geometric flow, quantum graph, Hamiltonian,
self-adjoint operator, scattering system, or target-zero table is not part of
the candidate.  Any such continuation is recorded only in
`ROUND2_CLUES.md`.

## Tensor source and arithmetic specialization

Let

\[
  \mathcal M=\{F_n:n\ge 1\},\qquad
  F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n,
\]

where \(F_n\) is the full shift on \(n\) symbols.  Tensor atoms are the
irreducible objects \(F_p\).  For a finite atom set \(P\), attach an
independent formal variable \(x_p\) to every \(p\in P\).  The analytic
specialization is

\[
  x_{F_p}=e^{-s h(F_p)}=p^{-s}.
\]

No prime mask, von Mangoldt coefficient, Riemann-zero datum, or fitted phase
is allowed.  The arithmetic input is confined to intrinsic tensor
factorization and entropy.

## Frozen subset shift

For a finite label set \(P\), define

\[
  E(P)=2^P\setminus\{\varnothing\},\qquad
  x_S=\prod_{p\in S}x_p,\qquad
  \epsilon(S)=(-1)^{|S|+1}.
\]

The phase space is the one-vertex full edge shift on \(E(P)\).  Closed words
are identified under cyclic rotation only; reflection is not an orbit
equivalence.  An edge \(S\) has entropy roof

\[
  T(S)=\sum_{p\in S}h(F_p)
\]

and scalar weight \(\epsilon(S)e^{-sT(S)}\).  Temporal repetition always
uses the actual scalar power \(\epsilon(S)^r e^{-rsT(S)}\).

## Rank-one edge-state transfer

Let \(V_P=\mathbb C[E(P)]\), with basis \(e_S\), and put

\[
  u_P=\sum_{S\ne\varnothing}e_S,
  \qquad
  \ell_x(e_S)=\epsilon(S)x_S,
  \qquad
  A_x=u_P\otimes\ell_x.
\]

Set

\[
  b_P(x)=\ell_x(u_P)
  =\sum_{S\ne\varnothing}\epsilon(S)x_S
  =1-\prod_{p\in P}(1-x_p).
\]

The declared scalar shadow is

\[
  A_x^r=b_P(x)^{r-1}A_x,
  \qquad \operatorname{tr}A_x^r=b_P(x)^r,
  \qquad \det(I-A_x)=\prod_{p\in P}(1-x_p).
\]

This scalar shadow inherits the exact A2 statement of the preceding
candidate.  It is not the character-resolved determinant claimed by SD-C18,
and its A2 status may not be patched into the resolved route tuple.

## Formal equivariant ledger

Let \(S_P\) permute subset edges by \(\rho(g)e_S=e_{gS}\), while acting on
variables by relabeling.  The family is semilinearly covariant:

\[
  \rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
\]

The primary positive object is the multigraded primitive-cycle class in the
completed Burnside/species ledger.  To carry scalar edge signs through power
maps, introduce the nontrivial character line \(\tau\) of \(C_2\).  An edge
\(S\) receives color \(\tau^{|S|+1}\), so that evaluation at the nontrivial
element of \(C_2\) gives \(\epsilon(S)\), while

\[
  \psi^r(\tau^{|S|+1})=\tau^{r(|S|+1)}
\]

reproduces \(\epsilon(S)^r\).  A negative integer coefficient is not an
admissible substitute for this \(C_2\) carrier under Adams operations.

At squarefree content \(pqr\), freeze the Burnside residual

\[
  \mathcal R_3=[S_3/S_3]+[S_3/C_3]-[S_3/C_2].
\]

Its subgroup marks in the order \((1,C_2,C_3,S_3)\) are

\[
  (0,0,3,1),
\]

and its permutation-representation image is

\[
  R_3=\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std},
  \qquad \chi_{R_3}(e,(12),(123))=(0,0,3).
\]

The class is nonzero although its scalar dimension is zero.  No Adams power
\(r>1\) reaches squarefree multidegree \((1,1,1)\).

## Canonical analytic comparison lift

The only canonical representation-preserving analytic comparison studied in
this paper is the diagonal subset operator

\[
  D_xe_S=x_Se_S.
\]

The sign \(\epsilon(S)\) is used as a supertrace readout, giving

\[
  \operatorname{str}D_x^r=b_P(x_1^r,\ldots,x_n^r),
\]

and, where trace class is available,

\[
  \operatorname{sdet}(I-D_x)
  =\prod_{S\ne\varnothing}(1-x_S)^{\epsilon(S)}.
\]

This object must not be conflated with the rank-one shadow, whose traces are
\(b_P(x)^r\).  For \(n\ge2\) the two power ledgers and their determinants are
different.

## Finite-to-infinite conventions

For \(P\subset Q\), the formal transition is the variable specialization
\(x_q=0\) for \(q\in Q\setminus P\).  It deletes edges containing new labels
and defines a projective multigraded species/cycle-index family.  It is not
an inductive system of fixed edge-state operators.

On \(\mathcal H=\ell^2(E(\mathcal P))\), where \(\mathcal P\) is the set of
tensor atoms, define

\[
  D_se_S=\prod_{p\in S}p^{-s}e_S.
\]

For \(q\ge1\), the frozen analytic criterion is

\[
  D_s\in\mathcal S_q
  \quad\Longleftrightarrow\quad q\operatorname{Re}s>1.
\]

Even in the trace-class half-plane, this diagonal operator has the mixed
subset superdeterminant above, not the pure Euler determinant.

## Naturality and readout gate

A character-resolved Fredholm claim is admissible only if one fixed operator
commutes with the group action defining its character projectors.  Semilinear
covariance of a variable family is not fixed-fiber symmetry.  For distinct
arithmetic weights \(p^{-s}\), \(\operatorname{Re}s>0\), the stabilizer is
trivial.  Equalizing all weights restores \(S_P\)-equivariance, but the
rank-one image is the trivial line and all nontrivial isotype determinants
are one.

At squarefree degree \(pqr\), any linear character/mark readout detecting
\(R_3\) inserts a mixed term in the primitive trace-log ledger.  The pure
Euler trace-log has no such mixed term.  A readout preserving the pure Euler
ledger must therefore kill \(R_3\).  This statement is scoped to the isolated
SD-C18 residual and the canonical lifts frozen here.

## Allowed and forbidden evidence

Allowed:

- tensor products and entropy of finite full shifts;
- finite nonempty subset shifts and primitive cyclic words;
- exact Burnside marks, representation characters, cycle indices, and
  \(C_2\)-colored Adams operations;
- formal variable specializations and exact algebra;
- standard Schatten/Fredholm theory in its natural half-plane;
- composite, shuffled, random, and free-commutative inventories as controls.

Forbidden:

- Riemann-zero tables or zero fitting;
- treating atom relabeling of distinct weights as a commuting symmetry;
- identifying \(b(x)^r\) with \(b(x^r)\);
- replacing scalar sign powers by integer Adams signs;
- calling a completed cycle index an analytic fixed-operator determinant;
- assembling route coordinates from incompatible scalar and resolved
  objects;
- leaving Symbolic Dynamics except as a `ROUND2_CLUE`.

## Frozen route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED

GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
STOP_STANDARD_SUPERTRACE_INTERPRETATION
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
```

The no-go claims are restricted to the canonical rank-one and diagonal
realizations, their standard finite-label actions, and their natural raw
edge-state limit.  No universal impossibility claim is made for every
conceivable group extension or symmetric-monoidal symbolic construction.
