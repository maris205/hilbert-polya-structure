# HCS-C18 derivation package

## 1. Frozen objects and conventions

Let

\[
\Gamma=\operatorname{PSL}_2(\mathbb Z),\qquad
P=\operatorname{Stab}_{\Gamma}(\infty),\qquad
C=\mathbb P^1(\mathbb Q).
\]

Matrices are computed with lifts in \(\operatorname{SL}_2(\mathbb Z)\); signs
are removed only after absolute values or projective actions are formed.  An
arrow \((g,x)\) in the action groupoid \(\Gamma\ltimes X\) runs from \(x\)
to \(gx\), and

\[
(g,hx)\circ(h,x)=(gh,x).
\]

For the multi-cusp calculation, \(N\) is squarefree and all cusp scaling
matrices use the standard width/Atkin--Lehner normalization in which the
classical tensor formula holds.

## 2. A genuinely open positive control

Let \(s_q\) be the number of solutions of

\[
r^2\equiv-1\pmod q,
\]

with \(s_1=1\), and let \(T_0>1\) be a sufficiently large geometric cusp
cutoff.  In the unoriented convention of Pujahari--Satpathy, the
number of modular scattering geodesics at denominator \(q\) and their sojourn
time are

\[
n_q=\frac{\varphi(q)+s_q}{2},\qquad
\ell_q=2\log(qT_0).
\]

### Proposition 2.1 (open scattering Dirichlet--Laplace series)

For \(\Re s>1\),

\[
\begin{split}
Z_{\mathrm{sc}}(s;T_0)
&:=\sum_{\gamma}e^{-s\ell_\gamma}\\
&=\frac{T_0^{-2s}}{2}
\left[
\frac{\zeta(2s-1)}{\zeta(2s)}+
\frac{\zeta(2s)L(2s,\chi_{-4})}{\zeta(4s)}
\right].
\end{split}
\]

Consequently this expression is meromorphic on \(\mathbb C\), and

\[
\operatorname*{Res}_{s=1}Z_{\mathrm{sc}}(s;T_0)
=\frac{3}{2\pi^2T_0^2},\qquad
\operatorname*{Res}_{s=1/2}Z_{\mathrm{sc}}(s;T_0)
=\frac{3}{8\pi T_0}.
\]

#### Proof

The totient identity is

\[
\sum_{q\ge1}\frac{\varphi(q)}{q^w}
=\frac{\zeta(w-1)}{\zeta(w)}.
\]

The root count \(s_q\) is multiplicative.  Its local Dirichlet factors are

\[
1+2^{-w},\qquad
\frac{1+p^{-w}}{1-p^{-w}}\quad(p\equiv1\!\!\pmod4),\qquad
1\quad(p\equiv3\!\!\pmod4).
\]

These are exactly the local factors of

\[
\frac{\zeta(w)L(w,\chi_{-4})}{\zeta(2w)}.
\]

Putting \(w=2s\), multiplying by \(T_0^{-2s}/2\), and adding the two
coefficient series proves the formula.  At \(s=1\), only
\(\zeta(2s-1)\) contributes the displayed residue.  At \(s=1/2\), the
pole comes from \(\zeta(2s)\) in the second summand and
\(L(1,\chi_{-4})=\pi/4\).  Direct substitution of
\(\zeta(2)=\pi^2/6\) gives the two constants.  \(\square\)

This series is not an Euler product over primitive closed orbits.  Its role is
to demonstrate that open arithmetic survives before a diagonal trace is
taken.  The machine audit uses \(T_0=1\) only as an analytic normalization of
the coefficient series, not as a positive geometric sojourn cutoff.

## 3. Why double cosets do not form an orbit semigroup

Set

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

### Proposition 3.1 (representative-dependent composition)

The double-coset set \(P\backslash\Gamma/P\) has no multiplication induced by
representative multiplication.

#### Proof

For every integer \(n\), \(S\) and \(ST^n\) represent the same right
\(P\)-coset.  Nevertheless,

\[
SS=-I,qquad
ST^nS=\begin{pmatrix}-1&0\\n&-1\end{pmatrix}.
\]

The first product lies in the identity cell with lower-left entry zero; the
second lies in a big cell with absolute lower-left entry \(|n|\).  For
\(n\ne0\) these are different \(P\)-double cosets.  \(\square\)

Retaining a source endpoint repairs composition, but the resulting clock has
a different obstruction.

## 4. Endpoint action groupoids

Choose a nonzero vector \(v_x\) on every projective line \(x\).  Define the
automorphy factor and its real logarithmic cocycle by

\[
g v_x=j_v(g,x)v_{gx},\qquad
\sigma_v(g,x)=2\log|j_v(g,x)|.
\]

The definitions immediately give

\[
j_v(gh,x)=j_v(g,hx)j_v(h,x),
\]

and hence

\[
\sigma_v(gh,x)=\sigma_v(g,hx)+\sigma_v(h,x).
\tag{4.1}
\]

If \(v'_x=r(x)v_x\), then

\[
\sigma_{v'}(g,x)=\sigma_v(g,x)
+2\log|r(x)|-2\log|r(gx)|.
\tag{4.2}
\]

### Theorem 4.1 (rational cusp algebraic coboundary theorem)

After forgetting topology, every section-induced absolute projective
automorphy cocycle of the displayed form on

\[
\Gamma\ltimes\mathbb P^1(\mathbb Q)
\]

is a set-theoretic groupoid coboundary.  In particular, the affine denominator
cocycle is

\[
\sigma_{\mathrm{aff}}(g,x)
=2\log q(gx)-2\log q(x),
\tag{4.3}
\]

where \(q(p/q)=q>0\) in lowest terms and \(q(\infty)=1\).  If
\(g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) and
\(c\ne0\), then

\[
\sigma_{\mathrm{aff}}(g,\infty)=2\log|c|.
\tag{4.4}
\]

#### Proof

For \(x=p/q\) in lowest terms, choose a primitive integral vector

\[
\widehat v_x=(p,q)^T,qquad \widehat v_\infty=(1,0)^T,
\]

with any fixed sign convention.  An \(\operatorname{SL}_2(\mathbb Z)\)
matrix maps primitive integral vectors to primitive integral vectors.  Thus

\[
g\widehat v_x=\pm\widehat v_{gx},
\]

so \(|j_{\widehat v}(g,x)|=1\) and
\(\sigma_{\widehat v}\equiv0\).

Every other projective section is a nonzero scalar multiple of
\(\widehat v\), so (4.2) proves the first statement.  For finite rational
\(x\), the affine section is

\[
v_x^{\mathrm{aff}}=(x,1)^T=q(x)^{-1}\widehat v_x.
\]

Equation (4.2) yields (4.3).  Starting at infinity, the endpoint
\(g\infty=a/c\) has denominator \(|c|\), which proves (4.4).  \(\square\)

Thus the entire rational-endpoint class is zero in algebraic/set-theoretic
groupoid cohomology.  This is not a continuous, H\"older, or Liv\v{s}ic
coboundary statement.  The primitive section and transfer function (q(x))
are discontinuous and unbounded in the topology inherited from
\(\mathbb P^1(\mathbb R)\).  No bounded conjugacy of analytic transfer
operators or determinant invariance is inferred.  The trace-level consequence
used below is only that the coboundary period vanishes on rational loops.

### Proposition 4.2 (time-reversal parity obstruction)

A positive, reversal-invariant sojourn time cannot itself be a real-valued
groupoid 1-cocycle.

#### Proof

The inverse of \((g,x)\) is \((g^{-1},gx)\).  Applying (4.1) to the identity
arrow gives

\[
\sigma(g^{-1},gx)=-\sigma(g,x).
\]

A physical sojourn time instead assigns the same positive value to the two
orientations of one geodesic.  The only real function with both parities is
zero.  \(\square\)

Thus the additive object is necessarily a signed Busemann-type lift, not the
positive physical time itself.

## 5. Full-boundary automorphy-period classification

### Theorem 5.1 (cusp-trivial/full-boundary-Selberg dichotomy)

Let \((g,x)\) be a nonidentity loop in
\(\Gamma\ltimes\mathbb P^1(\mathbb R)\).  Exactly one of the following holds.

1. The point \(x\) is rational, \(g\) is parabolic, and
   \(\sigma_v(g,x)=0\).
2. The point \(x\) is a real quadratic irrational, \(g\) is hyperbolic, and
   at the attracting and repelling fixed points respectively,
   \[
   \sigma_v(g,x_+)=\ell(g),\qquad
   \sigma_v(g,x_-)=-\ell(g),
   \]
   where
   \[
   \ell(g)=2\operatorname{arcosh}\frac{|\operatorname{tr}g|}{2}.
   \]

The value on a loop is independent of the projective section.

#### Proof

A loop at \(x=\infty\) has \(c=0\); a nonidentity element of its stabilizer
in \(\Gamma\) is parabolic and has period zero.  A finite fixed point of
\(g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) satisfies

\[
cx^2+(d-a)x-b=0.
\]

An elliptic nonidentity element has no real fixed point.  A parabolic element
has one rational eigenline and eigenvalue of absolute value one, so its
cocycle period is zero.  A hyperbolic element has two real eigenlines.  They
cannot be rational: a primitive integral eigenvector would force a rational
algebraic-unit eigenvalue, hence \(\pm1\), contradicting hyperbolicity.  The
two fixed points are therefore quadratic irrationals.

Let \(\lambda>1\) be the modulus of the expanding eigenvalue.  On the two
eigenlines the automorphy factors have moduli \(\lambda\) and
\(\lambda^{-1}\).  Therefore their cocycle periods are \(\pm2\log\lambda\).
Cayley--Hamilton gives

\[
2\log\lambda
=2\operatorname{arcosh}\frac{|\operatorname{tr}g|}{2}
=\ell(g).
\]

Finally, a section change contributes the coboundary term in (4.2), which
vanishes when \(gx=x\).  \(\square\)

### Corollary 5.2 (period-support consequence)

Any standard trace expansion whose diagonal terms are precisely loops of the
frozen endpoint action groupoid sees no nonzero period on the rational cusp
orbit.  If its unit space is enlarged to the full real boundary, its nonzero
period set is the signed Selberg translation-length set.

This corollary concerns loop-supported ordinary traces.  It does not discard
off-diagonal kernels or traces with additional internal/projector state.  It
does not by itself construct a determinant or determine coding multiplicity,
fixed-point Jacobians, branch orientation, or nuclearity.

## 6. Squarefree multi-cusp scattering

Define the completed zeta and modular scattering coefficient by

\[
\Lambda(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w),\qquad
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]

For a prime \(p\), set

\[
M_p(s)=\frac1{p^{2s}-1}
\begin{pmatrix}
p-1&p^s-p^{1-s}\\
p^s-p^{1-s}&p-1
\end{pmatrix}.
\tag{6.1}
\]

The classical squarefree formula, in the frozen Huxley--Hejhal
width/Atkin--Lehner cusp basis, is

\[
\Phi_N(s)=\phi(s)\bigotimes_{p\mid N}M_p(s).
\tag{6.2}
\]

### Theorem 6.1 (fixed Walsh diagonalization)

Let \(N=\prod_{p\mid N}p\) be squarefree and \(r=\omega(N)\).  Fix the
standard width-normalized scaling matrices, order the divisor-labelled cusps
by their prime-incidence bits, and use that identification at every spectral
parameter.  Let
\(H_2=2^{-1/2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\).
Then the matrix

\[
H_N=\bigotimes_{p\mid N}H_2
\]

is independent of \(s\) and diagonalizes \(\Phi_N(s)\) for every regular
\(s\).  Its eigenchannels, indexed by
\(\varepsilon=(\varepsilon_p)_{p\mid N}\in\{\pm1\}^r\), are

\[
\phi_\varepsilon(s)=\phi(s)
\prod_{p\mid N}
\frac{1+\varepsilon_p p^{1-s}}
     {1+\varepsilon_p p^s}.
\tag{6.3}
\]

Moreover,

\[
\det\Phi_N(s)=\phi(s)^{2^r}
\prod_{p\mid N}
\left(\frac{1-p^{2-2s}}{1-p^{2s}}\right)^{2^{r-1}}.
\tag{6.4}
\]

#### Proof

Each local block is \(a_p(s)I+b_p(s)X\), with \(X\) the coordinate swap.
The two columns of \(H_2\) are its fixed eigenvectors.  Direct factorization
gives the local eigenvalues

\[
a_p(s)+\varepsilon b_p(s)
=\frac{1+\varepsilon p^{1-s}}
       {1+\varepsilon p^s}.
\]

Tensoring the local diagonalizations proves (6.3).  The local determinant is

\[
\prod_{\varepsilon=\pm1}
\frac{1+\varepsilon p^{1-s}}
     {1+\varepsilon p^s}
=\frac{1-p^{2-2s}}{1-p^{2s}}.
\]

In a tensor product, each local determinant appears with exponent
\(2^{r-1}\); the scalar \(\phi\) appears in all \(2^r\) channels.  This gives
(6.4).  \(\square\)

### Corollary 6.2 (permutation invariance of spectral-parameter products)

For any regular parameters \(s_1,\ldots,s_m\) and any permutation \(\pi\),

\[
\Phi_N(s_m)\cdots\Phi_N(s_1)
=\Phi_N(s_{\pi(m)})\cdots\Phi_N(s_{\pi(1)}).
\tag{6.5}
\]

#### Proof

All matrices in (6.2) share the fixed eigenbasis \(H_N\).  In that basis the
ordered product is

\[
\operatorname{diag}_{\varepsilon}
\left(\prod_{j=1}^m\phi_\varepsilon(s_j)\right),
\]

which is invariant under permutation.  \(\square\)

Equation (6.5) is obtained from the frozen matrix product; no transition
average or histogram is substituted.  The \(s_j\) are spectral parameters,
not source-derived time steps.  Thus (6.5) is a conditional modeling
diagnostic: if a proposal encodes successive events by bare factors
\(\Phi_N(s_j)\), their order cannot be recovered from the product.  An
\(s\)-dependent cusp renormalization is outside the frozen normalization and
is not claimed to preserve the fixed Walsh basis.

### Corollary 6.3 (functional equation and physical-line unitarity)

Away from singularities,

\[
\Phi_N(s)\Phi_N(1-s)=I.
\]

On \(\Re s=1/2\), the normalized matrix is unitary.

#### Proof

The completed-zeta functional equation gives
\(\phi(s)\phi(1-s)=1\).  Every factor in (6.3) is inverted by
\(s\mapsto1-s\).  On the physical line, \(1-s=\bar s\), so every
eigenchannel has modulus one.  \(\square\)

## 7. Projector-resolved assignment and path sensitivity

Let \(P_a=e_ae_a^T\) be a rank-one cusp projector.  For three cusp labels,

\[
\operatorname{tr}\bigl(P_a\Phi(s_1)P_b\Phi(s_2)P_c\Phi(s_3)\bigr)
=\Phi(s_1)_{ab}\Phi(s_2)_{bc}\Phi(s_3)_{ca}.
\tag{7.1}
\]

Although the \(\Phi(s_j)\) commute, the projectors need not commute with
them.  Level \(N=6\) is the smallest squarefree level with two independent
cusp bits and three distinct nontrivial flip types.  The itinerary

\[
00\longrightarrow10\longrightarrow11\longrightarrow00
\]

uses respectively a \(2\)-flip, a \(3\)-flip, and a simultaneous flip.  For
generic distinct \(s_1,s_2,s_3\), changing the parameter-to-edge assignment
changes (7.1).  Changing the endpoint path also changes the recorded
amplitude.  The frozen computation records both high-precision witnesses.

This positive result proves only that off-diagonal endpoint resolution can
retain edge labels and path information after leaving the bare commutative
algebra.  It is not a proof of intrinsic chronology: no source identifies
\(s\) with time or defines legal event reorderings.  It supplies neither a
canonical primitive path monoid nor a nuclear determinant.

## 8. Divisor persistence

### Theorem 8.1 (no eigenchannel repair of the shifted quotient divisor)

Let \(\rho\) be a nontrivial zero of \(\zeta\).  Every squarefree scattering
eigenchannel (6.3) has the transported completed-zeta pole at \(s=\rho/2\)
and zero at \(s=(1+\rho)/2\), with the multiplicity inherited from \(\rho\).
No finite local factor in (6.3) cancels either divisor.

#### Proof

The numerator of a local factor vanishes only when

\[
1+\varepsilon p^{1-s}=0,
\]

which forces \(\Re s=1\).  Its denominator vanishes only on \(\Re s=0\).
For a nontrivial zeta zero, \(0<\Re\rho<1\), so

\[
0<\Re(\rho/2)<1/2,
\qquad
1/2<\Re((1+\rho)/2)<1.
\]

All local factors are finite and nonzero at both points.  The scalar
\(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) has the stated pole and zero there.
\(\square\)

The theorem applies channel by channel and hence to the determinant.  It is
not asserted for traces of powers: finite sums of nonzero channel factors can
cancel.  A compensating factor that itself carries a zeta divisor also lies
outside the claim.

## 9. Object-wise Route-A consequence

1. **Rational endpoint ordinary trace.** A1 fails because every
   section-induced rational loop period is zero; A2 fails because no target
   primitive trace law remains; A3 fails for the shifted open quotient; A4 is
   not testable because no same-object operator is defined.
2. **Full real-boundary enlargement.** A1 passes only in the classical sense:
   primitive hyperbolic classes exist.  The theorem identifies their signed
   automorphy-period set but does not construct a determinant, so A2 is not
   tested here.  This recovers no new RH-target period structure, and no new
   operator is defined.
3. **Bare squarefree \(\Phi_N(s_j)\) products.** A1 and A2 are not testable
   because the spectral parameters have no source-derived evolution,
   primitive law, or orbit determinant.  A3 fails channel by channel because
   the shifted completed-zeta quotient persists.  A4 is not testable.
4. **Projector-resolved paths.** The finite assignment/path-sensitivity
   witness escapes the bare commutative algebra, but A1--A4 are all not
   testable until a primitive path law, Fredholm kernel, global divisor, and
   operator are constructed.

The frozen ordinary closures are therefore Route-A rejected, while the
scoped obstruction is retained.  Projector-resolved open paths remain an
explicitly documented escape rather than being silently included in the
no-go.
