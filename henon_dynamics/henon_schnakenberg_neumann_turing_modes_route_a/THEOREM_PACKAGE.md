# Proof package: complete linear Schnakenberg--Neumann Turing atlas

## Claim

Let `a,b,d_u,d_v,L>0` and consider the Schnakenberg system on `(0,L)`
with `u_x=v_x=0` at both endpoints.  Put

\[
s=a+b,\qquad (u_*,v_*)=(s,b/s^2),
\]
\[
\tau={b-a\over s}-s^2,qquad
B=d_v{b-a\over s}-d_us^2,qquad
Q=B^2-4d_ud_vs^2.
\]

Then the following statements hold.

1. `(u_*,v_*)` is the unique positive spatially homogeneous equilibrium.
   Its kinetic Jacobian has trace `tau` and determinant `s^2`; hence it is
   asymptotically stable exactly when `tau<0`, neutral with eigenvalues
   `+/- i s` when `tau=0`, and unstable when `tau>0`.
2. The real linearized Neumann operator has compact resolvent and, after
   complexification, decomposes over `mu_n=(n*pi/L)^2`, `n>=0`, into the
   matrices

   \[
   M(\mu)=
   \begin{pmatrix}
   (b-a)/s-d_u\mu&s^2\\
   -2b/s&-s^2-d_v\mu
   \end{pmatrix}.
   \]

   Its two modal eigenvalues are

   \[
   \lambda_{n,\pm}={T_n\pm\sqrt{T_n^2-4D_n}\over2},
   \quad T_n=\tau-(d_u+d_v)\mu_n,
   \quad D_n=d_ud_v\mu_n^2-B\mu_n+s^2.
   \]
3. Assume `tau<0`.  A nonempty continuous positive-wavenumber instability
   window exists exactly when

   \[
   B>0,\qquad Q>0.
   \]

   In that case

   \[
   \mu_\pm={B\pm\sqrt Q\over2d_ud_v},\qquad
   0<\mu_-<\mu_+,
   \]

   and the `n`th Neumann mode is unstable exactly when
   `mu_-<mu_n<mu_+`.  At either endpoint it has one simple zero eigenvalue
   and one strictly negative eigenvalue.
4. The finite interval has a genuine linear Turing instability exactly when
   at least one integer `n>=1` lies in that open window.  With
   `r_+ = (L/pi)sqrt(mu_+)` and `r_-=(L/pi)sqrt(mu_-)`, the unstable dimension
   is

   \[
   N_{\rm unst}=\max\{0,\lceil r_+\rceil-\lfloor r_-\rfloor-1\}.
   \]

   The neutral modes are precisely the positive integers equal to either
   endpoint.  For a fixed `n>=1`, instability occurs exactly for

   \[
   {n\pi\over\sqrt{\mu_+}}<L<
   {n\pi\over\sqrt{\mu_-}}.
   \]
5. If `d_u=d_v`, kinetic stability implies `B=d_u tau<0`, so diffusion cannot
   create a Turing window.  At `Q=0` and `B>0`, the determinant only touches
   zero at `mu_0=B/(2d_ud_v)` and no open unstable window exists.  The
   homogeneous mode `n=0` is exactly the kinetic block.  The faces
   `d_u=0` or `d_v=0` are excluded from this uniformly parabolic theorem and
   are not obtained by dividing the displayed root formula by zero.

## Status

**PROVABLE AS STATED.**  Here “equilibrium” always means the positive
spatially homogeneous equilibrium, and “Turing instability” means linear
instability of that equilibrium to some `n>=1` Neumann mode while `n=0`
remains stable.

## Assumptions and notation

- All five parameters are strictly positive.
- The real linearized operator acts on `L^2((0,L);R^2)` with domain
  `H_N^2(0,L)^2`; all spectral statements are made after its canonical
  complexification.
- Square roots in the modal formula may be complex; instability is determined
  by the real two-by-two trace--determinant test.
- The nonlinear PDE is used only to define the equilibrium and its
  linearization.

## Dependency map

1. The equilibrium calculation gives the exact Jacobian.
2. The Neumann spectral theorem reduces the operator to independent real
   two-dimensional blocks.
3. Kinetic stability makes every modal trace strictly negative.
4. Therefore a spatial mode is unstable exactly when its determinant is
   negative.
5. The determinant is one upward quadratic, so its signs give the continuous
   window, the discrete count, and every wall.

## Proof

### Step 1: homogeneous equilibrium and kinetic chamber

At a positive constant equilibrium the second reaction equation gives
`u^2 v=b`.  Substitution in the first gives `a-u+b=0`, hence `u=s=a+b`
and `v=b/s^2`.  This proves uniqueness among positive constant equilibria.

For

\[
f(u,v)=a-u+u^2v,\qquad g(u,v)=b-u^2v,
\]

the Jacobian at the equilibrium is

\[
J=\begin{pmatrix}
-1+2b/s&s^2\\
-2b/s&-s^2
\end{pmatrix}
=\begin{pmatrix}
(b-a)/s&s^2\\
-2b/s&-s^2
\end{pmatrix}.
\]

Thus `tr J=tau` and

\[
\det J=-s(b-a)+2bs=s(a+b)=s^2>0.
\]

The real two-dimensional Routh criterion gives asymptotic stability exactly
for `tau<0`.  At `tau=0`, the characteristic polynomial is
`lambda^2+s^2`, while `tau>0` gives positive spectral abscissa.

### Step 2: exact Neumann spectral decomposition

The normalized cosine functions form an orthonormal eigenbasis for the
Neumann Laplacian, with eigenvalues `-mu_n`.  The diagonal diffusion operator
has compact resolvent, and adding the bounded constant matrix `J` preserves
compact resolvent.  After canonical complexification, the cosine basis gives
the direct modal decomposition.  On the `n`th cosine coefficient the
generator is `M(mu_n)` above.  Direct expansion gives

\[
\operatorname{tr}M(\mu)=\tau-(d_u+d_v)\mu
\]

and

\[
\det M(\mu)=s^2-
\left(d_v{b-a\over s}-d_us^2\right)\mu+d_ud_v\mu^2.
\]

The quadratic formula gives the stated modal eigenvalues and exhausts the
linearized spectrum.

### Step 3: continuous instability window

Assume `tau<0`.  Then `tr M(mu)<0` for every `mu>=0`.  A real two-by-two
matrix with negative trace has an eigenvalue with positive real part exactly
when its determinant is negative: negative determinant gives two real roots
of opposite signs, while positive determinant places both real parts below
zero.  At determinant zero the eigenvalues are zero and the negative trace.

The determinant polynomial has positive leading coefficient and positive
constant term.  It is negative at some positive `mu` exactly when its vertex
lies on the positive axis and its minimum is negative.  These conditions are
`B>0` and `Q>0`.  Its roots are `mu_-` and `mu_+`; their sum and product are
positive, so both roots are positive.  The determinant is negative exactly
between them.

### Step 4: finite-domain selection and exact count

The interval supplies only `mu_n=(n*pi/L)^2`.  Since `n=0` is the already
stable kinetic block, diffusion-driven instability requires a positive
integer `n` with `mu_-<mu_n<mu_+`.  Taking positive square roots is order
preserving and gives `r_-<n<r_+`.

The number of positive integers in this strict interval is
`max(0,ceil(r_+)-floor(r_-)-1)`.  This formula removes an integer endpoint on
either side and therefore has the required neutral-wall convention.  Solving
the strict inequalities for `L` gives the displayed entry and exit lengths.

### Step 5: degeneracies

If the diffusivities are equal to `d`, then
`B=d((b-a)/s-s^2)=d tau`, which is negative in the kinetic chamber.  If
`Q=0` and `B>0`, the upward determinant quadratic is nonnegative and has one
double wavenumber root; the modal matrix at that root has zero and negative
eigenvalues, so there is neutral contact but no instability interval.
The remaining boundary statements follow directly from `mu_0=0` and the
strict positive-diffusion assumptions.  This completes the proof.  ∎

## Corrections and claim boundary

- “Unique equilibrium” has been normalized to “unique positive spatially
  homogeneous equilibrium”; nonconstant nonlinear steady states are not
  classified.
- The theorem proves linear spectral instability only.  It does not invoke a
  nonlinear Turing bifurcation theorem.
- Exact finite rows do not prove the all-parameter statement.

## Open risks

No mathematical gap remains in the frozen linear theorem.  A future nonlinear
branch theorem would require transversality, kernel simplicity, and nonlinear
functional-analytic hypotheses not present here.
