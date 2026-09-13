# Research Question

## Source-stage identity

- Candidate: henon_primitive_cycle_cover_v1
- Safe title: **Normalized Primitive-Cycle Covers in a Degenerating Hénon Family**
- Date frozen for literature purposes: 2026-08-16
- Lifecycle: `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE / NO_RESULTS`
- Authorization: no code, registered execution, result, figure, or manuscript
- Required next gate: an independent Round-2 `SOURCE_LOCK_PASS`

This file fixes the mathematical question and the boundary of the proposed
paper. It is the corrected v2 source design after the immutable Round-1
`REPAIR_REQUIRED` review; it is not a manuscript and it is not an assertion
that independent Round-2 source review has passed.

## Upstream boundary

Paper 12 is terminal and is used only as batch provenance. Its final PDF,
Round-2 review, terminal-integrity certificate, and independent terminal review
must be hash-bound in experiments/source_lock.json. No Paper-12 code,
experimental artifact, or theorem is an input to the mathematics below.
BATCH_04_STATUS.md and BATCH_04_IDEA_REPORT.md must likewise be bound as the
exact dashboard snapshots at source-lock time.

The selected route was opened only after two alternatives were stopped:

1. a pure period-three properness statement failed on an explicit DVR
   collision arc;
2. an adelic fixed-spectrum conditioning proposal reduced to standard
   finite-multiplier-map consequences;
3. the surviving route is the five-layer normalized primitive-cycle package
   defined here.

## Base, family, and fixed algebra

Fix integers \(d,n\ge 2\). Put

\[
 A=\mathbb Q[a,c],\qquad K=\mathbb Q(a,c),\qquad
 H_{a,c}(x,y)=(a y+x^d+c,x).
\]

All rings and schemes in the theorem are over characteristic zero. Cyclic
indices are taken modulo \(n\). If a periodic orbit is written

\[
 (z_i,z_{i-1})\longmapsto (z_{i+1},z_i),
\]

then its equations are

\[
 g_i=z_i^d+a z_{i-1}+c-z_{i+1}=0.
\]

Define the full fixed algebra

\[
 B_n=A[z_0,\ldots,z_{n-1}]/(g_0,\ldots,g_{n-1}).
\]

This is the coordinate algebra of the full \(H_{a,c}^n\)-fixed scheme in
orbit coordinates. It includes lower periods. It is not called an
exact-period algebra.

Let

\[
 \nu=\nu_d(n)=\sum_{e\mid n}\mu(n/e)d^e,
 \qquad r=r_d(n)=\nu/n.
\]

The shift

\[
 \sigma(z_i)=z_{i+1}
\]

is the time-shift action.

## Generic actual-period block

The generic algebra \(B_n\otimes_AK\) is finite étale. Over an algebraic
closure of \(K\), actual exact-period-\(n\) points form a Galois-stable clopen
subset. Let \(e_n\) be its idempotent and set

\[
 E_n=e_n(B_n\otimes_AK).
\]

The word **actual** is permitted only for this generic clopen block. The
source theorem must prove that \(E_n\) is one field and has \(K\)-dimension
\(\nu\). It must not manufacture an everywhere embedded actual-period
subscheme inside \(\operatorname{Spec}B_n\).

## Relative normalization and quotient

Let \(S\) be the integral closure of \(A\) in the field \(E_n\). Let

\[
 S_0=S^{\langle\sigma\rangle},\qquad
 F=\operatorname{Frac}(S_0)=E_n^{\langle\sigma\rangle}.
\]

The scalar special line is \(a=0\), on which

\[
 f_c(z)=z^d+c.
\]

Let \(\Phi_{d,n}(z,c)\) denote the \(n\)-th scalar dynatomic polynomial and
define

\[
 D_n=\mathbb Q[c,z]/(\Phi_{d,n}(z,c)).
\]

For this source package, the notation

\[
 Y_1(n)=\operatorname{Spec}D_n,
 \qquad
 X_0(n)=X_0^{\mathrm{aff}}(n)
   =\operatorname{Spec}(D_n^{C_n})
\]

always means the **affine** point and orbit dynatomic curves. It does not
mean a smooth projective compactification. This convention prevents a
notation-only identification from replacing the required base-change proof.

## Two observables

Write

\[
 u_i=d z_i^{d-1},\qquad
 M_i=DH_{a,c}(z_i,z_{i-1})=
 \begin{pmatrix}u_i&a\\1&0\end{pmatrix}.
\]

Define the orbit sum and the pointwise derivative trace

\[
 \tau=\sum_{i=0}^{n-1}z_i,
 \qquad
 \rho=\operatorname{tr}(M_{n-1}\cdots M_0).
\]

The word **trace** in \(\rho\) means matrix trace of \(DH^n\) at a periodic
point. It does not mean the field trace \(\operatorname{Tr}_{F/K}\). Cyclic
invariance puts \(\tau\) and \(\rho\) in \(S_0\).

## Primary claim PC1

**PC1 — normalized primitive-cycle cover.** For every fixed \(d,n\ge2\):

1. \(B_n\) is a free \(A\)-module of rank \(d^n\), with basis
   \(\prod_i z_i^{e_i}\) for \(0\le e_i<d\).
2. The generic actual-period block \(E_n\) is a field of degree \(\nu\) over
   \(K\).
3. The relative normalization \(S\) is finite locally free of rank \(\nu\)
   over \(A\), and \(\operatorname{Spec}S\) is geometrically integral over
   \(\mathbb Q\).
4. Its scheme-theoretic scalar fiber is exactly
   \[
   S/aS\simeq D_n,
   \]
   including reducedness and excluding hidden nilpotents.
5. \(S_0\) is finite locally free of rank \(r\), invariants commute with the
   scalar base change, and
   \[
   S_0/aS_0\simeq D_n^{C_n}.
   \]
6. On a dense open \(U\subset\operatorname{Spec}A\) where
   \(\operatorname{Spec}S_0\to\operatorname{Spec}A\) is finite étale, the
   geometric monodromy on the \(r\) cycles is \(S_r\). For \(r=1\), this is
   the trivial group \(S_1\).

The scalar-fiber assertion in item 4 must pass through the unique height-one
prime above \((a)\), ramification index \(e=1\), the divisor of \(a\), and a
finite birational normality comparison. A bare statement that normalization
commutes with base change is forbidden.

## Primary claim PC2

**PC2 — two separately primitive cycle coordinates.** With \(F\), \(\tau\),
and \(\rho\) as above,

\[
 K(\tau)=F=K(\rho).
\]

Equivalently, multiplication by either element on the rank-\(r\) algebra
\(S_0\) has a characteristic polynomial

\[
 \chi_s(T)=\det(T\operatorname{id}_{S_0}-m_s)
 \quad(s\in\{\tau,\rho\})
\]

that is irreducible of degree \(r\) over \(K\) (and hence, being monic and
primitive, in \(A[T]\)). The determinant is defined on
\(\bigwedge_A^rS_0\); no global choice of basis is part of the claim.

The proofs for \(\tau\) and \(\rho\) must be separate until the common
\(S_r\)-stabilizer step. Nonconstancy of one observable cannot be used for
the other.

### PC2 prior-art boundary

PC2 is not positioned as the invention of either scalar generator. For the
scalar map \(f(z)=z^d+c\), Morton (1996), Corollary 1 and pp. 322--323,
establishes the relevant all-\(d\) dynatomic and multiplier-polynomial
irreducibility. On p. 336 he identifies the orbit-shift fixed field as

\[
 \operatorname{Frac}(D_n)^{\langle\sigma\rangle}
 =\mathbb Q(c,w),\qquad
 w=\prod_{i=0}^{n-1}f'(z_i)=\rho|_{a=0},
\]

for every \(d,n\) in scope. For \(d=2\), Corollary 3 on p. 335 proves the
orbit-sum polynomial irreducible, and p. 336 likewise gives the same fixed
field as \(\mathbb Q(c,t)\), where \(t=\tau|_{a=0}\). Thus the residual PC2
delta is the two-parameter lift over \(\mathbb Q(a,c)\), a uniform proof for
\(\tau\) in every degree (in particular \(d\ge3\)), and the integral,
basis-free characteristic polynomials in \(A[T]\). The proof package retains
separate infinity-word arguments for both observables as a uniform internal
route; those arguments do not restore novelty to the occupied scalar cases.

Cantat--Dujardin (2026), Section 3.2 and Theorems A and 3.7, are a second
mandatory boundary: their \(\operatorname{Trace}_n\) is the multiset of
pointwise traces over all formal-period-\(n\) points, and finitely many such
period multisets determine a Hénon map up to uniformly finitely many choices
over an algebraically closed characteristic-zero field. That parameter-
reconstruction statement is not the fixed-actual-period, single-cycle-field
primitivity statement in PC2, and PC2 is not presented as an extension of
their rigidity theorem.

## Degree-one boundary

For \((d,n)=(2,2)\),

\[
 \nu=2,\qquad r=1,
\]

and the exact two-cycle equations give

\[
 \tau=z_0+z_1=a-1,
 \qquad z_0z_1=(a-1)^2+c,
\]

\[
 \rho=4z_0z_1+2a=4a^2-6a+4+4c.
\]

These are degree-one primitive-element statements. They are not evidence
for nontrivial monodromy. For general \(d\) and \(n=2\), the matrix identity
is

\[
 \operatorname{tr}(M_1M_0)=u_0u_1+2a.
\]

## Exact research questions

### Q1. Finite full fixed scheme

Can the cyclic equations be certified by a monic Gröbner basis over \(A\),
so that finiteness and rank are integral statements rather than generic
point counts?

### Q2. Actual-period field

Can the actual-period idempotent be isolated only after passing to the
generic finite-étale algebra, and can a Henselian connected-lift argument at
\(a=0\) prove that this block is one field?

### Q3. Relative normalization

Can excellence, the Cohen–Macaulay property of a normal surface, and miracle
flatness prove that \(S/A\) is finite locally free?

### Q4. Exact scalar fiber

Can the \(a\)-adic valuation ledger prove a unique height-one prime over
\((a)\), \(e=1\), and residue field \(\mathbb Q(Y_1(n))\), and hence prove
\(S/aS=D_n\) without nilpotents?

### Q5. Quotient and monodromy

Can Reynolds averaging justify arbitrary base change for \(S^{C_n}\), and can
the scalar full-wreath theorem be transferred in the correct direction to
give \(S_r\) on global cycles?

### Q6. Primitive coordinates

Can primitive words at \(c=\infty\) separately show
\(\tau\notin K\) and \(\rho\notin K\), after which maximality of
\(S_{r-1}<S_r\) yields both field-generation statements and the top-wedge
characteristic polynomials?

## Required proof bridges

The proof is incomplete unless it contains all of the following:

- monic Gröbner reduction over the coefficient ring;
- generic étaleness and the actual-period idempotent;
- Henselian lifting of the scalar exact-period factor;
- excellent/Nagata finiteness of normalization;
- normal-surface Cohen–Macaulayness and miracle flatness;
- unique \(a\)-adic prime, \(e=1\), a single multiplicity-one divisor, and
  flat/CM exclusion of special-fiber nilpotents;
- finite birational comparison with the normal Gao–Ou algebra;
- a constants argument proving geometric integrality;
- Reynolds splitting and invariants/base-change compatibility;
- the restriction-specialization monodromy inclusion in the correct
  direction;
- primitive infinity words for both \(\tau\) and \(\rho\);
- the \(S_{r-1}\) maximal-stabilizer step;
- the determinant construction on \(\bigwedge_A^rS_0\).

## Frozen nonclaims

The project does **not** claim:

- an everywhere embedded actual-exact-period subscheme of
  \(\operatorname{Spec}B_n\);
- a free \(C_n\)-action on every fiber;
- that every fiber of \(S\) or \(S_0\) is smooth, reduced, or étale;
- that formal period equals actual period at every scalar parameter;
- a projective compactification theorem;
- a theorem for arbitrary generalized Hénon maps or arbitrary polynomial
  automorphisms;
- novelty of Gröbner bases, normalization, Reynolds operators, dynatomic
  curves, wreath monodromy, orbit sums, or trace coordinates as methods;
- invention of the scalar multiplier generator \(\rho|_{a=0}\), or of the
  quadratic scalar orbit-sum generator \(\tau|_{a=0}\);
- invention of Hénon orbit-sum carriers, cyclic-polynomial elimination, or
  low-period stability polynomials;
- parameter reconstruction from formal-period trace spectra;
- historical priority from a bounded no-hit search;
- fiberwise irreducibility of specialized characteristic polynomials;
- a result, code, figure, or manuscript before source review.

## Decision lock

The adjudicated project decision is GO_SOURCE_DESIGN_ONLY, with historical
candidate scores novelty \(6.8/10\), standalone size \(7.4/10\), and proof
confidence \(0.74\). A dissenting audit scored novelty \(4.5/10\) and size
\(3.9/10\), which is retained rather than averaged away. After the direct
low-period Hénon precedents, Morton's direct scalar fixed-field generators,
and Cantat--Dujardin's trace-spectrum rigidity were fully disclosed, the
corrected conservative author-side ranges are novelty \(4.8\)--\(5.5/10\)
and standalone size \(4.5\)--\(5.5/10\). They are risk estimates informed by
the Round-1 review, not a consensus and not replacement gate verdicts. The
reason to preserve the candidate is the strengthened five-layer package,
with PC1 carrying most of the residual contribution; it is not a claim that
every layer, or the scalar generators in PC2, is individually new. The v2
package remains `PENDING_INDEPENDENT_R2`.
