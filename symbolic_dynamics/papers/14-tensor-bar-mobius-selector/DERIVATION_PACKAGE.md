# DERIVATION PACKAGE — Reduced Tensor Bar Code

## 1. Tensor inventory

The symbolic inventory is the monoid of finite full shifts

\[
F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n.
\]

The equality `h(F_m tensor F_n)=h(F_m)+h(F_n)` turns the topological entropy
into a tensor-additive roof without importing an arithmetic weight.

## 2. Why abelian characters cannot be the selector

The Grothendieck group of the free commutative tensor monoid is

\[
K=M^{\mathrm{gp}}\cong\bigoplus_p\mathbb Z e_p,
\qquad
v(F_n)=\sum_pv_p(n)e_p.
\]

Every abelian monoidal charge factors through `v`.  A proposed selector that
vanishes on every composite must in particular satisfy

\[
q(F_{p^2})=2q(F_p)=0,
\qquad
q(F_{p^3})=3q(F_p)=0,
\]

and hence `q(F_p)=0`.  This closes all cyclic-torsion and roots-of-unity
variants at once.

For a coherent thin-divisor cocycle, the initial object gives

\[
\kappa(d,n)=\kappa(1,n)-\kappa(1,d),
\]

so a character twist is a vertex gauge.  If the character instead comes
regularly from entropy, its only effect is

\[
n^{-s}\exp(i\theta t\log n)=n^{-(s-i\theta t)}.
\]

Thus the positive construction must use higher ordered chains, not a
one-cocycle.

## 3. Reduced ordered tensor words

Let

\[
B(s)=\sum_{n\ge2}e^{-s h(F_n)}=\sum_{n\ge2}n^{-s}=\zeta(s)-1.
\]

An internal word of length `k` is an ordered list
`(F_{a_1},...,F_{a_k})`, all `a_j>=2`.  Its roof and reduced-bar sign are

\[
T=\sum_{j=1}^k\log a_j,
\qquad \epsilon=(-1)^{k+1}.
\]

Summing all length-`k` code edges gives `(-1)^(k+1)B(s)^k`, hence

\[
F_{\mathrm{bar}}(s)
=B(s)-B(s)^2+B(s)^3-\cdots.
\]

Absolute convergence requires

\[
\sum_{k\ge1}|B(\sigma)|^k<\infty.
\]

Since `B(sigma)` is positive and strictly decreasing on the real axis, the
raw boundary is the unique solution of

\[
B(\sigma_{\mathrm{bar}})=1,
\quad\text{equivalently}\quad
\zeta(\sigma_{\mathrm{bar}})=2,
\]

namely

\[
\sigma_{\mathrm{bar}}=1.7286472389981836181\ldots.
\]

For `Re(s)>sigma_bar`, geometric summation is legitimate:

\[
F_{\mathrm{bar}}(s)=\frac{B(s)}{1+B(s)}
=1-\frac1{\zeta(s)}.
\]

## 4. Same-object transfer and determinant

The code shift has one vertex and countably many return edges.  After the
edge sum converges, its weighted vertex adjacency acts on
`ell^2({*})=C` as multiplication by `F_bar(s)`.  Therefore

\[
D_{\mathrm{bar}}(s,z)
=\det_{\mathbb C}(I-zL_{\mathrm{bar},s})
=1-zF_{\mathrm{bar}}(s).
\]

At `z=1`,

\[
D_{\mathrm{bar}}(s,1)
=1-F_{\mathrm{bar}}(s)
=\frac1{1+B(s)}
=\frac1{\zeta(s)}.
\]

This is an honest determinant of the frozen weighted symbolic adjacency.  It
is not obtained by applying a determinant label to a previously known
Dirichlet series.

## 5. Finite endpoint cancellation

Fix an endpoint `n`.  The coefficient of `n^{-s}` in `B(s)^k` is the number
of ordered factorizations `a_1...a_k=n` with every `a_j>=2`.  Thus

\[
c(n)=\sum_{k\ge1}\sum_{a_1\cdots a_k=n}(-1)^{k+1}.
\]

Every endpoint sum is finite.  Since

\[
1-F_{\mathrm{bar}}=(1+B)^{-1}
\]

as a formal Dirichlet series, its coefficient is the tensor-divisor
incidence inverse of the constant-one function.  Hence

\[
c(n)=-\mu_\otimes(n)\quad(n\ge2).
\]

The endpoint-first completion is

\[
F^{\mathrm{inc}}_{\mathrm{bar}}(s)
=-\sum_{n\ge2}\mu_\otimes(n)n^{-s}.
\]

It is absolutely convergent for `Re(s)>1` because

\[
\sum_{n\ge1}|\mu_\otimes(n)|n^{-\sigma}
=\prod_p(1+p^{-\sigma})
=\frac{\zeta(\sigma)}{\zeta(2\sigma)}.
\]

The order of operations is essential: raw word summation has the narrower
domain `Re(s)>sigma_bar`; only the finite endpoint cancellation is admitted
in the wider half-plane.

## 6. Entropy innovation and logarithmic derivative

Define intrinsically

\[
\mu_\otimes*\mathbf 1=\delta_1,
\qquad
\Lambda_\otimes=\mu_\otimes*h.
\]

Convolution inversion gives

\[
h(F_n)=\sum_{d\mid n}\Lambda_\otimes(d).
\]

For `n=prod_j p_j^{a_j}`, the terms supported on prime powers sum to
`sum_j a_j log p_j=log n`, yielding

\[
\Lambda_\otimes(p^r)=\log p,
\qquad
\Lambda_\otimes(n)=0
\quad\text{for mixed-factor }n.
\]

The same coefficient arises from the frozen determinant:

\[
\frac{d}{ds}\log D_{\mathrm{bar}}(s,1)
=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\Lambda_\otimes(n)n^{-s}.
\]

No von Mangoldt weight is inserted.  The derivative inserts the entropy roof
`T`, while Möbius cancellation is supplied by the bar grammar.

## 7. Repetition and primitive-cycle audit

For `|zF_bar(s)|<1`,

\[
\log D_{\mathrm{bar}}(s,z)
=-\sum_{r\ge1}\frac{z^r}{r}F_{\mathrm{bar}}(s)^r.
\]

The `r` here is temporal repetition of code edges.  It is not the
tensor-divisor exponent in `mu_tensor`, and the primitive objects are cyclic
necklaces in the code alphabet.  Signed endpoint grouping recovers the Euler
coefficient ledger, but there is no pre-grouping orbitwise map from an atom
to one primitive code orbit.

The bar sign is an ordinary scalar edge weight: repetition of one edge gives
`epsilon(a)^r exp(-rsT(a))`.  It is not an odd supertrace grading, which would
retain one fixed negative sign at every repetition order.  Nothing in this
derivation supplies a chain contraction or a homological contractible-pair
cancellation.

## 8. Universal-inventory derivation

Let any weighted nonunit inventory have partition sum `B_X`.  Repeating the
same ordered-word construction gives

\[
F_X=B_X-B_X^2+B_X^3-\cdots=\frac{B_X}{1+B_X},
\qquad
D_X=1-F_X=\frac1{1+B_X}.
\]

Unique factorization and tensor entropy do not enter this algebraic step.
The mechanism therefore proves the reciprocal-partition identity for
arithmetic and nonarithmetic inventories alike.  This is exactly the
`PROVES_TOO_MUCH` obstruction.
