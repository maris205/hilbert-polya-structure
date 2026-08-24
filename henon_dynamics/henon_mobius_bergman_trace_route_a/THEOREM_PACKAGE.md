# Proof package

## Claim

Let `D` be the unit disk, let `A^2(D)` have normalized area measure, and set

\[
\phi_a(z)=\frac1{a+z}\quad(a=3,6),\qquad
\mathcal L=C_{\phi_3}+C_{\phi_6},\quad C_\phi f=f\circ\phi.
\]

Then `L` is trace class and `||L||_1<=89/16`.  If

\[
M_w=M_{a_1}\cdots M_{a_n}=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad M_a=\begin{pmatrix}0&1\\1&a\end{pmatrix},
\]

then `Phi_w=phi_(a_1) o ... o phi_(a_n)` has one fixed point in `D`.  With
`t=tr(M_w)`, `delta=det(M_w)=(-1)^n`, and
`Delta=t^2-4*delta`,

\[
z_w=\frac{A-D+\sqrt\Delta}{2C},\qquad
\lambda_w=\Phi_w'(z_w)=\frac{t-\sqrt\Delta}{t+\sqrt\Delta},
\]

and

\[
\operatorname{Tr}C_{\Phi_w}=\frac1{1-\lambda_w}
=\frac12+\frac{t}{2\sqrt\Delta}.
\]

For every `n>=1`, after relabelling the operator-product reversal,

\[
\operatorname{Tr}\mathcal L^n
=\sum_{|w|=n}\frac1{1-\lambda_w}.
\]

For primitive cyclic words `[p]`, the Fredholm determinant satisfies

\[
\det(I-z\mathcal L)=
\prod_{[p]}\prod_{k\ge0}(1-z^{|p|}\lambda_p^k).
\]

The raw product is absolutely convergent for `|z|<1/2`.  The trace-class
determinant is entire; no global convergence of the displayed raw product is
asserted.

## Status

`PROVABLE AS STATED` for the frozen Möbius--Bergman system.  The determinant
is dynamical, not arithmetic or target-facing.

## Assumptions

- Bergman area measure is normalized so `e_n(z)=sqrt(n+1) z^n` is orthonormal.
- Matrix multiplication represents function composition from left to right:
  `M_(a1)...M_(an)` represents `phi_(a1) o ... o phi_(an)`.
- In `L^n`, composition operators reverse this written word; reversal is a
  bijection on all words and is relabelled in the trace sum.
- The square root of the positive real discriminant is the positive root.

## Proof strategy and dependency map

1. Compute the exact image disks and a derivative contraction bound.
2. Expand each composition operator against the Bergman basis to obtain an
   absolutely summable rank-one decomposition.
3. Read fixed points and multipliers from the integer Möbius matrix.
4. Conjugate the unique fixed point to zero and use triangular monomial action
   to compute the composition trace.
5. Expand `L^n`, then regroup the Fredholm logarithm by primitive cyclic root.
6. Use two non-cyclic same-count words as an exact order-sensitivity control.

## Proof

The image of the closed unit disk under `phi_a` is the disk with center

\[
c_a=\frac{a}{a^2-1},\qquad r_a=\frac1{a^2-1}.
\]

Thus its largest modulus is `1/(a-1)`: respectively `1/2` and `1/5`.
The distance between the two centers minus both radii is

\[
\frac38-\frac6{35}-\frac18-\frac1{35}=\frac1{20},
\]

so the closed images are strictly separated.  Also
`sup_D |phi_a'|<=1/(a-1)^2`, namely `1/4` and `1/25`.  Every finite
composition is therefore a strict contraction of the closed disk and has a
unique fixed point, which lies in its strict interior.

For `f=sum_n <f,e_n> e_n`,

\[
C_{\phi_a}f=\sum_{n\ge0}\langle f,e_n\rangle
\sqrt{n+1}\,\phi_a^n.
\]

Since `||phi_a^n||_(A^2)<=r^n` when `sup |phi_a|<=r`, this is a nuclear
rank-one expansion.  Coarsening `sqrt(n+1)<=n+1` gives

\[
\|\mathcal L\|_1\le
\sum_{n\ge0}(n+1)(1/2)^n+
\sum_{n\ge0}(n+1)(1/5)^n
=4+\frac{25}{16}=\frac{89}{16}.
\]

For `M_w=[[A,B],[C,D]]`, the fixed equation is
`C z^2+(D-A)z-B=0`.  Matrix entries are positive in the required positions,
and contraction already selects the unique root in the disk.  The displayed
positive-radical root follows from the quadratic formula.  At a fixed point,
`Cz_w+D=(t+sqrt(Delta))/2`; since the derivative of the Möbius map is
`delta/(Cz+D)^2` and `delta=(t^2-Delta)/4`, the multiplier formula follows.

Let a disk automorphism send `z_w` to zero.  Its composition operator is
bounded and invertible on Bergman space, so it gives a similarity of
`C_(Phi_w)` to composition by a map `psi` fixing zero.  If
`psi(z)=lambda_w z+O(z^2)`, its matrix on the monomial basis is triangular
with diagonal `1,lambda_w,lambda_w^2,...`.  Trace class therefore gives
`Tr C_(Phi_w)=sum_(k>=0) lambda_w^k=1/(1-lambda_w)`, which simplifies to the
displayed matrix expression.

Expanding `L^n` yields all `2^n` operator words.  The convention for
composition operators reverses each function word, but reversal bijects the
word set, so the all-`n` trace identity follows.  Near zero,

\[
\log\det(I-z\mathcal L)
=-\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}\mathcal L^n.
\]

A repetition `p^r` of a primitive cycle of length `ell` has `ell` rooted
rotations and multiplier `lambda_p^r`.  Substitution and
`1/(1-lambda_p^r)=sum_(k>=0)lambda_p^(rk)` turn its contribution into
`sum_k log(1-z^ell lambda_p^k)`.  Exponentiation proves the product.
The multiplier is well-defined on a cyclic class: cyclically rotating a
matrix product preserves its trace and determinant, hence preserves the
displayed formula for `lambda_p`.
There are at most `2^ell/ell` primitive cycles and
`|lambda_p|<=4^(-ell)`, so absolute convergence follows from `2|z|<1`.
The logarithmic regrouping is first justified in a smaller neighborhood of
zero; the determinant and the convergent product are analytic on `|z|<1/2`,
so the identity theorem extends their equality across that disk.

Finally, `33366` and `33636` have the same digit multiset but are not cyclic
rotations.  Their matrices are

\[
\begin{pmatrix}63&388\\208&1281\end{pmatrix},\qquad
\begin{pmatrix}60&379\\199&1257\end{pmatrix},
\]

with traces `1344` and `1317` and determinant `-1`.  The positive-trace
formula makes both their multipliers and composition traces unequal.  Order
sensitivity is therefore internal to nonlinear composition.

## Corrections or missing assumptions

The raw primitive product is proved only in `|z|<1/2`.  Its left side extends
entirely because `L` is trace class; that continuation does not prove global
absolute convergence of the raw factors.  Also, word order is meaningful
only modulo cyclic rotation for primitive cycles; the control pair was chosen
outside one cyclic class.

## Open risks

- No target divisor or analytic target completion is compared.
- No self-adjoint or antiunitary structure is produced.
- No arithmetic meaning is assigned to the dynamical primitive factors.
- The trace-class bound is explicit but deliberately coarse.

## Strict assessment

The tuple is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and
`route_b_invocation_allowed: false`.
