# HCS-C26 theorem package: scalar AGY determinants survive, oscillator twists do not

## Material passport

- **Origin:** HCS-C24 discrete metaplectic atom theorem, HCS-C25 exact AGY
  return family, and the HCS-C26 positive-prefix complexification.
- **Mode:** theorem / source lock / exact validation.
- **Date:** 2026-08-10.
- **Status:** theorem text complete; exact certificate and independent replay
  are release gates.
- **Novelty boundary:** HCS-C24's atomic essential-norm theorem and HCS-C25's
  all-length decoder are inputs.  C26 contributes the common complex domain,
  the scalar trace-class realization and algebraic trace atoms, and the
  no-localizer evaluation application to the full AGY family.

## 1. Source-locked notation

The alphabet size and Jacobian exponent are

\[
d=4,
\]

whereas the complex dimension of the projective base is

\[
q=d-1=3.
\]

Keeping these symbols separate prevents a dimension error in the nuclearity
and trace formulas.  Put

\[
\ell(z)=\mathbf 1^Tz,
\qquad
H_{\mathbb C}=\{z\in\mathbb C^d:\ell(z)=1\}\simeq\mathbb C^q,
\qquad
p_M(z)=\frac{Mz}{\ell(Mz)}.
\]

For the fixed strongly positive neat AGY path `gamma_*`, write

\[
P=B_{\gamma_*}^T>0.
\]

The AGY branch grammar in Section 4.1.3 and Lemma 4.4 says that a return is
either `gamma_*` itself or a minimal path of the form
`gamma_* gamma_0 gamma_*`.  Combining that grammar with later-on-the-left
Rauzy multiplication, and then transposing, gives the C26 algebraic
factorization

\[
A_\gamma:=B_\gamma^T=P C_\gamma,
\qquad C_\gamma\ge0,
\qquad
h_\gamma=p_{A_\gamma}=p_P\circ p_{C_\gamma}.
\tag{1.1}
\]

Every `C_gamma` is nonnegative and invertible, so it has no zero row or
column.  The direct
projective formulas are

\[
q_\gamma(x)=\ell(A_\gamma x),
\qquad
r_\gamma(x)=\log q_\gamma(x),
\qquad
j_\gamma(x)=q_\gamma(x)^{-d}=e^{-dr_\gamma(x)}.
\tag{1.2}
\]

Thus the raw scalar weight is

\[
w_{s,\gamma}(x)=q_\gamma(x)^{-(s+d)}.
\tag{1.3}
\]

HCS-C25 proves

\[
\sum_{\gamma\in\Gamma}
\sup_{x\in\Delta}|w_{s,\gamma}(x)|<\infty,
\qquad \operatorname{Re}s>-\sigma _0,
\tag{1.4}
\]

and proves that the projected symplectic matrices `g_gamma` of distinct
fixed-start branches are distinct.  Both statements preserve the complete
chronological word.

## 2. A common complex domain from the fixed positive prefix

Define the canonical complex section of the positive cone by

\[
\mathcal D=
\left\{
z\in H_{\mathbb C}:
\operatorname{Re}(z_i\overline{z_j})>0
\text{ for every }i,j
\right\}.
\tag{2.1}
\]

### Lemma 2.1 -- elementary complex-cone geometry

The set `D` is a bounded connected domain containing the real positive
simplex.  If `C` is an invertible nonnegative matrix, then

\[
p_C(\mathcal D)\subset\mathcal D.
\tag{2.2}
\]

If `P` is strictly positive, then

\[
p_P(\overline{\mathcal D})\Subset\mathcal D.
\tag{2.3}
\]

#### Proof

For `z` in `D`,

\[
\operatorname{Re}z_i
=\sum_j\operatorname{Re}(z_i\overline{z_j})>0.
\]

On the closure,

\[
1=|\ell(z)|^2
=\sum_{i,j}\operatorname{Re}(z_i\overline{z_j})
\ge |z_k|^2,
\]

so the closure is bounded.  The line segment from any `z` to the real
barycenter stays in `D`: after expanding each pairwise real product, all
terms are positive.  Hence `D` is connected.

For `C>=0`, every row is nonzero and

\[
\operatorname{Re}
\bigl((Cz)_i\overline{(Cz)_j}\bigr)
=\sum_{k,l}C_{ik}C_{jl}
  \operatorname{Re}(z_k\overline{z_l})>0.
\]

Common projective normalization preserves this inequality, proving (2.2).
For `P>0` and `z` in the closure, the same sum is nonnegative and its
diagonal part

\[
\sum_kP_{ik}P_{jk}|z_k|^2
\]

is strictly positive.  The denominator cannot vanish because the squared
modulus of the coordinate sum is the sum of these nonnegative pairwise real
products.  Compactness and continuity then give (2.3).  `square`

### Theorem 2.2 -- uniform AGY holomorphic domain

There is a bounded connected domain `Omega` in `H_C` such that

\[
\boxed{
p_P(\overline{\mathcal D})
\Subset\Omega\Subset\mathcal D
}
\tag{2.4}
\]

and

\[
\boxed{
h_\gamma(\Omega)
\subset p_P(\mathcal D)
\Subset\Omega
\quad\text{for every }\gamma\in\Gamma.
}
\tag{2.5}
\]

#### Proof

Choose a sufficiently small connected Euclidean neighborhood of the compact
connected set `p_P(cl D)` inside `D`.  Equations (1.1), (2.2), and (2.3)
give

\[
h_\gamma(\Omega)
=p_Pp_{C_\gamma}(\Omega)
\subset p_P(\mathcal D)
\subset p_P(\overline{\mathcal D})
\Subset\Omega.
\]

No passage from real Hilbert contraction to complex contraction is used.
The fixed strictly positive prefix is the mechanism that creates the common
complex gap.  `square`

### Scope warning 2.3

One cannot generally replace `Omega` by the natural domain
`p_P(D)`.  The real branch images partition the real AGY base up to measure
zero and approach its boundary; a single compact subset of that same natural
domain cannot contain all of them.  The enlarged intermediate domain in
(2.4) is essential.

## 3. Holomorphic weights and the scalar determinant

### Lemma 3.1 -- common logarithm and complex branch sum

For every fixed `s` with `Re(s)>-sigma_0`, all weights extend holomorphically
to `Omega` by

\[
w_{s,\gamma}(z)
=\exp\bigl(-(s+d)\operatorname{Log}\ell(A_\gamma z)\bigr),
\tag{3.1}
\]

where `Log` is the principal logarithm, and

\[
\boxed{
\sum_\gamma
\|w_{s,\gamma}\|_{H^\infty(\Omega)}<\infty.
}
\tag{3.2}
\]

The convergence is locally uniform for `s` in compact subsets of the source
half-plane.  No uniform bound as `|Im(s)|` tends to infinity is asserted.

#### Proof

Write

\[
q_\gamma(z)=\ell(A_\gamma z)=c_\gamma\cdot z.
\]

The matrix `A_gamma=P C_gamma` is strictly positive because `P>0` and
`C_gamma` has no zero column, so every coordinate of `c_gamma` is positive.
Compact containment `cl Omega subset D` gives constants

\[
\delta_\Omega
=\min_{z\in\overline\Omega,i}\operatorname{Re}z_i>0,
\qquad
M_\Omega
=\max_{z\in\overline\Omega,i}|z_i|<\infty.
\]

Consequently

\[
\operatorname{Re}q_\gamma(z)
\ge\delta_\Omega\sum_i c_{\gamma,i}>0,
\]

which supplies one principal logarithm for every branch.  Fix a real
interior point `x_0` and put

\[
m_0=\min_i(x_0)_i,
\qquad M_0=\max_i(x_0)_i.
\]

Uniformly in `gamma` and `z`,

\[
\frac{\delta_\Omega}{M_0}
\le\frac{|q_\gamma(z)|}{q_\gamma(x_0)}
\le\frac{M_\Omega}{m_0},
\qquad
|\arg q_\gamma(z)|<\frac\pi2.
\tag{3.3}
\]

Choose the real comparison point as

\[
x_0\in\Delta\subset p_P(\mathcal D)\subset\Omega.
\]

For fixed `s`, (3.3) bounds the complex weight by a constant times
`q_gamma(x_0)^-(Re(s)+d)`.  The latter is bounded by the corresponding real
branch supremum in (1.4), proving pointwise summability.

For local uniformity, let
`K compactly contained in {Re(s)>-sigma_0}` and choose a real
`a_0` with

\[
-\sigma_0<a_0<\min_{s\in K}\operatorname{Re}s.
\]

The source return satisfies `q_gamma(x_0)=exp(r_gamma(x_0))>=2`.  Hence the
weight magnitudes for `s in K` are bounded, after one `K`-dependent sector
constant from (3.3), by

\[
q_\gamma(x_0)^{-(a_0+d)}.
\]

Equation (1.4) at the real parameter `a_0` supplies a summable majorant.
This proves the claimed compact-parameter uniformity.  `square`

### Theorem 3.2 -- scalar trace-class AGY operator

On the scalar Bergman space

\[
\mathcal H_0=A^2(\Omega),
\]

the operator

\[
(L_sf)(z)=\sum_{\gamma\in\Gamma}
w_{s,\gamma}(z)f(h_\gamma z)
\tag{3.4}
\]

belongs to an exponential singular-value class `E(c,1/q)` for some `c>0`.
In particular, for every `Re(s)>-sigma_0`, it is trace class and has the
ordinary Fredholm determinant

\[
D_s(u)=\det_{\mathcal H_0}(I-uL_s).
\tag{3.5}
\]

#### Proof

Theorems 2.2 and Lemma 3.1 make `(h_gamma,w_s,gamma)` a countable
holomorphic map-weight system whose combined image is compactly contained in
`Omega` and whose weight sup norms are summable.  The Bergman transfer
theorem of Bandtlow--Jenkinson applies in complex dimension `q=3`, giving
the exponential class and hence trace class.  Their nuclear convergence
also justifies the wordwise fixed-point trace formula for every power.
`square`

### Corollary 3.3 -- parameter holomorphy

The map

\[
s\longmapsto L_s
\]

is holomorphic with values in the trace-class ideal throughout
`Re(s)>-sigma_0`, and

\[
\boxed{
D(s,u)=\det(I-uL_s)
}
\]

is jointly holomorphic on

\[
\{\operatorname{Re}s>-\sigma_0\}\times\mathbb C.
\]

Indeed, each branch weight is entire in `s`, while Lemma 3.1 gives locally
uniform summability on compact `s`-sets.  Factoring every branch through one
fixed Bergman restriction between nested domains converts that bound into
locally uniform trace-norm summability.  Banach-valued Weierstrass
convergence gives trace-norm holomorphy, and the standard trace-class
determinant is jointly holomorphic in a trace-class operator and a scalar.
This statement does not assert that the logarithmic orbit series converges
at `u=1`.

This is a statement about the **raw scalar** AGY operator.  The normalized
operator involving the invariant density is not included: AGY proves only
`rho in C_b^1`, not a holomorphic continuation of `rho`.

## 4. Chronological Perron trace atoms

Let

\[
(T_{s,\gamma}f)(z)
=w_{s,\gamma}(z)f(h_\gamma z).
\]

For an ordered word

\[
\boldsymbol\gamma=(\gamma_1,\ldots,\gamma_n),
\]

the operator product
`T_{s,gamma_1} ... T_{s,gamma_n}` has map and matrix

\[
h_{\boldsymbol\gamma}
=h_{\gamma_n}\circ\cdots\circ h_{\gamma_1},
\qquad
A_{\boldsymbol\gamma}
=A_{\gamma_n}\cdots A_{\gamma_1}.
\tag{4.1}
\]

Equivalently,

\[
A_{\boldsymbol\gamma}
=(B_{\gamma_1}\cdots B_{\gamma_n})^T.
\]

Later branches multiply on the left.  This is the literal transfer-iterate
order, not a commutative or averaged surrogate.  Every matrix in this
section is the raw integral determinant-one matrix.  No total-entry
normalization used for numerical bounds may be substituted here.

There is a contravariant bookkeeping point.  If
`(beta_1,...,beta_n)` instead denotes the **forward Rauzy-path order**, then

\[
B_{\rm fwd}=B_{\beta_n}\cdots B_{\beta_1},
\qquad
p_{B_{\rm fwd}^T}
=h_{\beta_1}\circ\cdots\circ h_{\beta_n},
\]

and the corresponding operator-factor order is
`(beta_n,...,beta_1)`.  The theorem uses operator-factor order in (4.1);
the exact two- and three-return certificates label forward order separately.
Neither ordering is averaged or silently identified with the other.

Every `A_word` is a positive matrix in `SL(d,Z)`.  Let

\[
\lambda_{\boldsymbol\gamma}>0
\]

be its simple Perron root and let

\[
\chi_{\boldsymbol\gamma}(t)
=\det(tI-A_{\boldsymbol\gamma})\in\mathbb Z[t].
\]

### Theorem 4.1 -- algebraic scalar trace formula

The unique fixed point of `h_word` in `Omega` is the normalized positive
Perron vector.  The branch trace is

\[
\boxed{
\operatorname{tr}
\bigl(T_{s,\gamma_1}\cdots T_{s,\gamma_n}\bigr)
=
\frac{\lambda_{\boldsymbol\gamma}^{-(s+1)}}
     {\chi_{\boldsymbol\gamma}'
       (\lambda_{\boldsymbol\gamma})}.
}
\tag{4.2}
\]

Consequently

\[
\boxed{
\operatorname{tr}L_s^n
=\sum_{\boldsymbol\gamma\in\Gamma^n}
\frac{\lambda_{\boldsymbol\gamma}^{-(s+1)}}
     {\chi_{\boldsymbol\gamma}'
       (\lambda_{\boldsymbol\gamma})},
}
\tag{4.3}
\]

with the convergence supplied by the holomorphic nuclear trace theorem, and

\[
-\log D_s(u)
=\sum_{n\ge1}\frac{u^n}{n}
  \sum_{\boldsymbol\gamma\in\Gamma^n}
  \frac{\lambda_{\boldsymbol\gamma}^{-(s+1)}}
       {\chi_{\boldsymbol\gamma}'
         (\lambda_{\boldsymbol\gamma})}
\tag{4.4}
\]

for sufficiently small `|u|`.  The determinant in (3.5), rather than the
orbit-log series in (4.4), then supplies the entire continuation in `u`.

#### Proof

Every word map sends `Omega` into the same relatively compact subset.
The Earle--Hamilton fixed-point principle therefore gives a unique fixed
point in `Omega`.  The normalized positive Perron vector is a fixed point
and lies in the real positive-prefix image, so it is that unique point.

The projective normalizers telescope in the true order:

\[
\prod_{k=1}^n
q_{\gamma_k}
\bigl(h_{\gamma_{k-1}}\cdots h_{\gamma_1}x\bigr)
=\ell(A_{\boldsymbol\gamma}x).
\tag{4.5}
\]

At the normalized Perron fixed point, (4.5) equals
`lambda_word`, so the product weight is

\[
\lambda_{\boldsymbol\gamma}^{-(s+d)}.
\tag{4.6}
\]

All intermediate normalizers are positive real numbers at this fixed point,
so (4.6) has no principal-log wrapping ambiguity.

The derivative of the projective map at that point is induced by
`A_word/lambda_word` on the quotient of `C^d` by the Perron line.  Therefore

\[
\det_{\mathbb C}
\bigl(I-Dh_{\boldsymbol\gamma}\bigr)
=\prod_{j=2}^d
  \left(1-\frac{\lambda_j}{\lambda_{\boldsymbol\gamma}}\right)
=\frac{\chi_{\boldsymbol\gamma}'
       (\lambda_{\boldsymbol\gamma})}
      {\lambda_{\boldsymbol\gamma}^{d-1}}.
\tag{4.7}
\]

The holomorphic fixed-point trace formula divides (4.6) by (4.7), producing
the dimension cancellation and exponent `s+1` in (4.2).  Nuclear word
summability gives (4.3): choose nested domains containing the common branch
image compactly.  The Bergman restriction between them is trace class, each
branch factors through that restriction, and its trace norm is bounded by a
common constant times `||w_s,gamma||_infinity`.  Hence

\[
\sum_\gamma\|T_{s,\gamma}\|_1<\infty
\]

locally uniformly in `s`, and the `n`-word expansion converges absolutely in
trace norm with bound

\[
\sum_{\boldsymbol\gamma\in\Gamma^n}
\|T_{s,\gamma_1}\cdots T_{s,\gamma_n}\|_1
\le
\left(\sum_\gamma\|T_{s,\gamma}\|_1\right)^n.
\]

This justifies the trace interchange in (4.3).  The trace-class determinant
identity gives (4.4) only near zero.  `square`

Because `A_word` lies in `SL(d,Z)`, its Perron root is an algebraic unit.
Thus (4.2) is a genuine arithmetic encoding by a chronological integer
matrix, its algebraic unit, and the derivative of its characteristic
polynomial.  The phrase “discriminant-like” may be used heuristically for
the denominator, but no equality with a field discriminant is claimed when
the characteristic polynomial is reducible or nonminimal.  For general
complex `s`, the value `lambda_word^(-(s+1))` is not claimed to be algebraic.

Theorem 4.1 is entirely scalar.  It contains no metaplectic lift, central
sign, or Maslov phase.  A characteristic polynomial cannot distinguish the
two lifts of a symplectic matrix and must not be used as an ordinary trace of
the oscillator representation.

### Corollary 4.2 -- reciprocal four-dimensional form

In the present full-rank `H(2)` model, every closed word matrix is conjugate
to a four-dimensional symplectic matrix.  Hence

\[
\chi_{\boldsymbol\gamma}(t)
=t^4-a_{\boldsymbol\gamma}t^3
 +b_{\boldsymbol\gamma}t^2
 -a_{\boldsymbol\gamma}t+1,
\qquad a_{\boldsymbol\gamma},b_{\boldsymbol\gamma}\in\mathbb Z,
\]

and its scalar trace atom is

\[
\frac{\lambda_{\boldsymbol\gamma}^{-(s+1)}}
{4\lambda_{\boldsymbol\gamma}^3
 -3a_{\boldsymbol\gamma}\lambda_{\boldsymbol\gamma}^2
 +2b_{\boldsymbol\gamma}\lambda_{\boldsymbol\gamma}
 -a_{\boldsymbol\gamma}}.
\]

Distinct words with the same reciprocal polynomial still occur separately
in (4.3); no spectral quotient replaces their dynamical multiplicity.

## 5. The evaluation-slice obstruction

Let

\[
\mathscr F=L^2(\mathbb R^2)
\]

and let `U_gamma` be the pathwise oscillator representation of the HCS-C25
metaplectic lift.

### Theorem 5.1 -- point-evaluative function spaces

Let `X` be a Banach space of `F`-valued functions on a set containing a real
interior point `x_0`.  Assume:

1. the constant embedding
   \[
   J:\mathscr F\to X,\qquad (Jv)(x)=v,
   \]
   is bounded;
2. evaluation
   \[
   E_{x_0}:X\to\mathscr F,\qquad E_{x_0}F=F(x_0),
   \]
   is bounded;
3. the literal pointwise AGY formula defines a bounded operator
   \[
   (\mathcal L_s^{\rm Mp}F)(x)
   =\sum_\gamma w_{s,\gamma}(x)
      U_\gamma F(h_\gamma x).
   \]

Then, throughout `Re(s)>-sigma_0`,

\[
\boxed{
\|\mathcal L_s^{\rm Mp}\|_{\rm ess}
\ge
\frac{
\left(\sum_\gamma
|w_{s,\gamma}(x_0)|^2\right)^{1/2}}
{\|E_{x_0}\|\,\|J\|}>0.
}
\tag{5.1}
\]

In particular, the operator is noncompact.

#### Proof

Absolute coefficient summability follows from (1.4), and pointwise
evaluation gives the exact full-family slice

\[
E_{x_0}\mathcal L_s^{\rm Mp}J
=\sum_\gamma w_{s,\gamma}(x_0)U_\gamma.
\tag{5.2}
\]

Every coefficient is nonzero.  HCS-C25's decoder and full-rank `H(2)`
symplectic conjugation make the projected metaplectic atoms pairwise
distinct.  HCS-C24 Theorem 3 therefore gives

\[
\left\|E_{x_0}\mathcal L_s^{\rm Mp}J\right\|_{\rm ess}
\ge
\left(\sum_\gamma|w_{s,\gamma}(x_0)|^2\right)^{1/2}.
\]

For every compact `K:X->X`, the compression `E_x0 K J` is compact and

\[
\|E_{x_0}\mathcal L_s^{\rm Mp}J-E_{x_0}KJ\|
\le\|E_{x_0}\|\,\|J\|\,
   \|\mathcal L_s^{\rm Mp}-K\|.
\]

Taking infima over compact `K` proves (5.1).  `square`

This theorem needs no branch-supported holomorphic function and no branch
localizer.  It applies to every bounded literal realization on standard
point-evaluative `H^infinity`, Hardy, Bergman, or reproducing-kernel spaces
that contains constants.  It does **not** claim to cover an anisotropic
distribution space with no bounded point or fibre slice.

### Theorem 5.2 -- same-domain scalar/twisted dichotomy

On

\[
\mathcal H_{\mathscr F}
=A^2(\Omega;\mathscr F)
\simeq A^2(\Omega)\widehat\otimes\mathscr F,
\]

the literal series

\[
(\mathcal L_s^{\rm Mp}F)(z)
=\sum_\gamma w_{s,\gamma}(z)
  U_\gamma F(h_\gamma z)
\tag{5.3}
\]

converges absolutely in operator norm but is noncompact for every
`Re(s)>-sigma_0`.  Hence

\[
\boxed{
L_s:A^2(\Omega)\to A^2(\Omega)
\text{ is trace class,}
\qquad
\mathcal L_s^{\rm Mp}
\text{ is noncompact.}
}
\tag{5.4}
\]

#### Proof

Let `K_P=p_P(cl D)`, a compact subset of `Omega`.  Point evaluations on
the scalar or vector-valued Bergman space are uniformly bounded on `K_P`.
Since every branch image lies in `K_P`,

\[
\|w_{s,\gamma}U_\gamma(F\circ h_\gamma)\|_{A^2}
\le C_{\Omega,P}
\|w_{s,\gamma}\|_\infty\|F\|_{A^2}.
\]

Lemma 3.1 yields absolute operator-norm convergence.  Constants and interior
evaluation are bounded on Bergman space, so Theorem 5.1 proves
noncompactness.  The scalar statement is Theorem 3.2.  `square`

For the usual volume normalization,

\[
\|J\|=\operatorname{vol}(\Omega)^{1/2},
\qquad
\|E_{x_0}\|=K_\Omega(x_0,x_0)^{1/2},
\]

where `K_Omega` is the Bergman kernel.  Formula (5.1) is therefore a
concrete positive lower bound on the same domain where the scalar determinant
exists.

## 6. Exact length-128 lower bound

For the HCS-C25 witness

\[
\gamma_*=t^{64}(tbttbtbb)^8,
\]

the exact point and normalizer are

\[
x_0=
\frac{(131596,8592543,81363,194419)}{8999921},
\qquad
S_*(x_0)=
\frac{15076979616018}{8999921}.
\tag{6.1}
\]

Thus

\[
|w_{s,\gamma_*}(x_0)|
=S_*(x_0)^{-(\operatorname{Re}s+4)},
\tag{6.2}
\]

and Theorem 5.1 implies the completely explicit one-branch estimate

\[
\boxed{
\|\mathcal L_s^{\rm Mp}\|_{\rm ess}
\ge
\frac{S_*(x_0)^{-(\operatorname{Re}s+4)}}
{\|E_{x_0}\|\,\|J\|}.
}
\tag{6.3}
\]

At `Re(s)=0`, the numerator equals the exact HCS-C25 Jacobian

\[
\frac{6560769639033108250634950081}
{51672252134321473356696529937672668896230786946152976}.
\tag{6.4}
\]

The C26 certificate independently reconstructs (6.1)--(6.4); it does not
import the C25 producer.

## 7. Tensor-slice extension and exact boundary

The same argument works without point evaluation whenever bounded input and
output slices expose the fibre.  Suppose a base realization has bounded maps

\[
I_f:\mathscr F\to X_0,
\qquad
R_\ell:X_1\to\mathscr F
\]

such that

\[
R_\ell\mathcal TI_f
=\sum_\gamma b_\gamma U_\gamma,
\qquad (b_\gamma)\in\ell^1,
\]

with at least one nonzero signed aggregate after equal projected atoms are
combined.  HCS-C24 then gives

\[
\|\mathcal T\|_{\rm ess}
\ge
\frac{\|(b_g)\|_{\ell^2}}
     {\|R_\ell\|\,\|I_f\|}>0.
\]

This covers natural tensor-type anisotropic spaces when those slices are
proved bounded.  A non-tensor completion that deliberately correlates base
and oscillator modes and destroys every bounded fibre slice remains a
different, open operator model.

Other boundaries are equally sharp:

- Bargmann--Fock is unitary equivalent to the Schrödinger oscillator model,
  so it does not remove noncompactness.
- A heat factor or Hermite damping changes the fibre cocycle unless the
  dynamics forces it and an exact cocycle law is proved.
- The infinite-dimensional Weil character is distributional, not the
  ordinary Hilbert trace used in (3.5).
- Noncompactness rules out trace class, every finite Schatten ideal, and
  ordinary Hilbert/Banach nuclear determinant theory.  It does not say that
  `I-u L` is never Fredholm, and it does not rule out a separately defined
  flat or distributional determinant.

## 8. Route-A decision and next large door

The target metaplectic Hilbert--Pólya candidate receives

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\qquad
\mathrm{ROUTE\_A\_REJECTED}.
\]

The scalar determinant and the algebraic-unit trace formula are meaningful
positive structures, but they provide neither a self-adjoint operator nor a
Riemann-zero correspondence.  The literal infinite oscillator twist has now
failed on `C_b^1`, normalized `L^2`, and a source-faithful holomorphic
Bergman realization.

The next large door should therefore change the fibre rather than the base:

\[
g_\gamma\bmod p\in\operatorname{Sp}(4,\mathbb F_p),
\qquad
\rho_p(g_\gamma)\in U(p^2),
\]

for odd primes `p`.  A finite Weil fibre preserves chronology, has a genuine
finite character expressed by Gauss sums, and can twist the scalar trace-class
operator without infinite multiplicity.  It is a new arithmetic model, not a
claim that `p` tending to infinity recovers an ordinary trace of the
infinite oscillator representation.
