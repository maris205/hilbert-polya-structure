# SOURCE LOCK — SD-C16

## Identity and scope

```yaml
candidate_id: SD-C16
title: reduced tensor bar-code shift
primary_system_family: Symbolic Dynamics
route_b_invocation_allowed: false
status: frozen
```

No other dynamical system family is used as a carrier, analogy, or repair.
No Riemann-zero data, Gamma factor, functional equation, critical-strip fit,
or external spectral operator is admissible.

## Arithmetic symbolic object

Let `F_n` be the full shift on `n` symbols.  Freeze

\[
F_m\otimes F_n=F_{mn},\qquad F_1=\mathbf 1,\qquad
h(F_n)=\log n.
\]

On isomorphism classes this is the free commutative tensor monoid
`M = {F_n : n >= 1}`.  Its nonunit atoms are exactly the `F_p`.  Entropy is
intrinsic and tensor-additive.

## Phase space and local grammar

The code alphabet is

\[
\mathcal C=\coprod_{k\ge1}M_+^k,
\qquad M_+=\{F_n:n\ge2\}.
\]

A symbol `a=(F_{a_1},...,F_{a_k})` is a nonempty ordered reduced tensor word.
Equivalently it is the strict cumulative divisor chain

\[
F_1<F_{a_1}<F_{a_1a_2}<\cdots<F_{a_1\cdots a_k}.
\]

The dynamical object is the one-vertex countable edge shift with one return
edge for every code symbol.  A symbolic orbit is a bi-infinite sequence of
such code edges.  The one-vertex presentation is part of the frozen object.

## Clock, potential, and function space

For a code edge of internal length `k`, freeze

\[
T(\mathbf a)=\sum_{j=1}^k h(F_{a_j})
             =\log(a_1\cdots a_k),
\qquad
\epsilon(\mathbf a)=(-1)^{k+1},
\]

and

\[
\phi_s(\mathbf a)=\epsilon(\mathbf a)e^{-sT(\mathbf a)}.
\]

The parity is the reduced-bar convention.  Choosing this bar grammar is a
`MODELING_CHOICE`; it earns no separate arithmetic credit.  The vertex
function space is `ell^2({*}) = C`, and the weighted vertex adjacency is

\[
L_{\mathrm{bar},s}c=F_{\mathrm{bar}}(s)c,
\qquad
F_{\mathrm{bar}}(s)=\sum_{\mathbf a\in\mathcal C}\phi_s(\mathbf a).
\]

This is a scalar Fredholm operator only after the edge-alphabet sum is
defined in the stated domain.

## Raw domain and determinant

Put `B(s)=sum_{n>=2} n^{-s}=zeta(s)-1`, and let

\[
\sigma_{\mathrm{bar}}=1.7286472389981836181\ldots,
\qquad \zeta(\sigma_{\mathrm{bar}})=2.
\]

The raw sum over individual ordered words is absolutely convergent only for
`Re(s)>sigma_bar`, where

\[
F_{\mathrm{bar}}(s)
=\sum_{k\ge1}(-1)^{k+1}B(s)^k
=\frac{B(s)}{1+B(s)}.
\]

The determinant is not declared after the fact.  It is the one-dimensional
Fredholm determinant

\[
D_{\mathrm{bar}}(s,z)
=\det_{\mathbb C}(I-zL_{\mathrm{bar},s})
=1-zF_{\mathrm{bar}}(s).
\]

At the frozen specialization `z=1`,

\[
D_{\mathrm{bar}}(s,1)=\frac1{\zeta(s)}
\qquad(\Re s>\sigma_{\mathrm{bar}}).
\]

## Endpoint-first incidence completion

For each endpoint `n`, there are finitely many ordered factorizations into
integers at least two, and

\[
\sum_{k\ge1}\ \sum_{a_1\cdots a_k=n}(-1)^{k+1}
=-\mu_\otimes(n).
\]

Here `mu_tensor` is defined intrinsically as the convolution inverse of the
constant-one function on the tensor-divisor poset.  Thus

\[
F^{\mathrm{inc}}_{\mathrm{bar}}(s)
=-\sum_{n\ge2}\mu_\otimes(n)n^{-s}
\]

converges absolutely for `Re(s)>1`.  This is an endpoint-first grouped
incidence completion.  It is **not** raw absolute convergence of the
countable edge alphabet in `1<Re(s)<=sigma_bar`.

## Canonical observable

The only differentiated observable is the already-frozen entropy roof:

\[
\frac{d}{ds}\log D_{\mathrm{bar}}(s,1)
=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\Lambda_\otimes(n)n^{-s},
\qquad
\Lambda_\otimes=\mu_\otimes*h.
\]

Consequently

\[
\Lambda_\otimes(p^r)=\log p,
\qquad
\Lambda_\otimes(n)=0
\quad\text{if }n\text{ has at least two distinct tensor atoms}.
\]

`Lambda_tensor` is neither additive nor a local cocycle.  In particular,
`Lambda_tensor(pq)=0` while `Lambda_tensor(p)+Lambda_tensor(q)>0` for
distinct atoms.  Multiplying a completed closed word by a precomputed
`Lambda_tensor(total mass)` is forbidden and would not be the source-locked
one-object Fredholm realization.

## Primitive and repetition semantics

Where `|z F_bar(s)|<1`,

\[
\log D_{\mathrm{bar}}(s,z)
=-\sum_{r\ge1}\frac{z^r}{r}F_{\mathrm{bar}}(s)^r.
\]

The primitive cycles of the actual code shift are cyclic necklaces of
ordered factorization words.  They are not individual atoms `F_p`.  The
prime-power ledger appears only after signed aggregation.  No orbitwise
statement `p <-> gamma_p` is claimed.

### Scalar-sign firewall

The frozen parity `epsilon(a)=(-1)^(k+1)` is an ordinary scalar edge weight.
If one code edge `a` is repeated temporally `r` times, its weight is

\[
\epsilon(\mathbf a)^r e^{-rsT(\mathbf a)}.
\]

It is **not** a chain grading or supertrace parity.  An odd supertrace sector
would contribute a fixed minus sign at every repetition order, whereas a
negative scalar edge alternates with `r`.  SD-C16 claims no chain complex,
contractible-pair cancellation, homological quotient, or bar-to-Koszul
reduction.  Establishing or refuting such a structure is reserved for the
Paper 15 obligation.

## Data discipline

Allowed inputs:

- tensor product of finite full shifts;
- intrinsic topological entropy;
- nonempty ordered reduced words and finite cumulative divisor chains;
- fixed reduced-bar parity;
- exact finite incidence algebra;
- scalar Fredholm determinants and structural control inventories.

Forbidden inputs:

- a prime table used as a coefficient or mask;
- precomputed `mu_tensor` or `Lambda_tensor` used in the transfer;
- independent fitted per-atom characters or signs;
- Riemann zeros or target spectra;
- cross-family repairs.

## Universal control and route lock

For every weighted nonunit inventory with partition sum `B_X`, the identical
grammar gives

\[
F_X=\frac{B_X}{1+B_X},\qquad D_X=\frac1{1+B_X}.
\]

Therefore the mechanism is `PROVES_TOO_MUCH`: it has a genuine same-object
determinant but no arithmetic selectivity or new analytic information.

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
