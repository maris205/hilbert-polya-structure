# Exact theorem package — HCS-C303

Status: **PROVABLE AS STATED**.

## Model and convention

Let `|0>` be the ground state, `|1>` the excited state,
`sigma_z=|1><1|-|0><0|`, `sigma_-=|0><1|`, and
`sigma_+=|1><0|`.  For nonnegative rates and real `omega`, set

\[
\mathcal L(\rho)=-i[(\omega/2)\sigma_z,\rho]
+\gamma_\downarrow D[\sigma_-]\rho
+\gamma_\uparrow D[\sigma_+]\rho
+\frac{\gamma_\phi}{2}(\sigma_z\rho\sigma_z-\rho),
\]

where `D[L]rho=L rho L^*-(L^*L rho+rho L^*L)/2`.  The last coefficient is
not negotiable: isolated pure dephasing damps `rho_01` at rate `gamma_phi`.

Write `Gamma1=gamma_down+gamma_up` and
`Gamma2=Gamma1/2+gamma_phi`.

## Theorem

If `Gamma1>0`, define

`p=gamma_up/Gamma1`, `eta=exp(-Gamma1 t)`,
`c=exp((-Gamma2+i omega)t)`, and `q=2Gamma2/Gamma1>=1`.
Then for every initial density matrix and every `t>=0`,

\[
 \rho_{11}(t)=p+\eta(\rho_{11}(0)-p),\qquad
 \rho_{01}(t)=c\rho_{01}(0).
\]

The Liouvillian characteristic polynomial, with convention
`det(lambda I-L)`, is

\[
 \lambda(\lambda+\Gamma_1)
 [ (\lambda+\Gamma_2)^2+\omega^2],
\]

and the generator is diagonalizable on every parameter face.  Its eigenvalues
are `0`, `-Gamma1`, and `-Gamma2 +/- i omega`.

The exact trace-norm contraction coefficient on differences of density
matrices is

\[
 \eta_{\rm tr}(\Phi_t)=
 \max\{e^{-\Gamma_1t},e^{-\Gamma_2t}\}.
\]

The normalized Choi state in the ordered basis
`|00>,|01>,|10>,|11>` is

\[
J_t=\frac12\begin{pmatrix}
a&0&0&c\\0&b&0&0\\0&0&d&0\\\bar c&0&0&e
\end{pmatrix},
\]

where

\[
a=1-p(1-\eta),\ b=p(1-\eta),\quad
d=(1-p)(1-\eta),\ e=\eta+p(1-\eta).
\]

The channel is entanglement breaking if and only if

\[
 p(1-p)(1-\eta)^2\ge \eta^q. \tag{EB}
\]

For `0<p<1`, there is a unique finite threshold.  Its `eta_*` is the unique
root in `(0,1)` of

\[
 p(1-p)(1-\eta_*)^2=\eta_*^q,
 \qquad t_{\rm EB}=-\log(\eta_*)/\Gamma_1,
\]

and `(EB)` holds exactly for `t>=t_EB`.  If `gamma_phi=0`, then `q=1` and,
with `r=p(1-p)`,

\[
 \eta_*={1+2r-\sqrt{1+4r}\over 2r};
\]

at `p=1/2`, this is `3-2sqrt(2)`.

If `p=0` or `p=1`, no finite-time channel is entanglement breaking, while the
infinite-time constant pure-state preparation is.  If `Gamma1=0` and
`gamma_phi>0`, no finite-time pure-dephasing channel is EB, while complete
dephasing at infinity is.  If also `gamma_phi=0`, the dynamics is a unitary
phase rotation of period `2pi/|omega|` when `omega!=0`, and the identity when
`omega=0`.

For `Gamma1>0` the stationary state `diag(1-p,p)` is unique and strict
contraction excludes every nonconstant recurrent orbit.  On the pure-dephasing
face the fixed states are precisely the diagonal states and there is no
nonconstant recurrence.  On the unitary face diagonal states are fixed and
states with coherence are periodic.  The Liouvillian kernel dimension is one
for `Gamma1>0`, two for `Gamma1=0` except at the zero generator, and four at
`Gamma1=gamma_phi=omega=0`.

## Proof

In the matrix-unit basis `(E00,E01,E10,E11)`, direct substitution gives

\[
L=\begin{pmatrix}
-\gamma_\uparrow&0&0&\gamma_\downarrow\\
0&-\Gamma_2+i\omega&0&0\\
0&0&-\Gamma_2-i\omega&0\\
\gamma_\uparrow&0&0&-\gamma_\downarrow
\end{pmatrix}.
\]

The two scalar ODEs yield the stated channel.  The population block has
eigenvalues zero and `-Gamma1`; each coherence matrix unit is already an
eigenoperator.  These invariant subspaces remain independent even when
eigenvalues collide.  At `Gamma1=0`, nonnegativity forces both population
rates to vanish; the same decomposition proves the stated kernel dimensions.

Applying the channel to the four matrix units in the normalized maximally
entangled state gives `J_t`.  Its trace is one.  Positivity is also visible
directly: `a,b,d,e>=0`, and

\[
 ae-|c|^2=p(1-p)(1-\eta)^2+\eta-\eta^q\ge0,
\]

because `q>=1` and `0<=eta<=1`.  Partial transpose moves `c` to the middle
two-by-two block, whose determinant is

\[
 {bd-|c|^2\over4}
 ={p(1-p)(1-\eta)^2-\eta^q\over4}.
\]

For two qubits, PPT is equivalent to separability, and a channel is EB exactly
when its normalized Choi state is separable.  This proves `(EB)`.  For
`r=p(1-p)>0`, the function `F(eta)=r(1-eta)^2-eta^q` has
`F(0)=r`, `F(1)=-1`, and
`F'(eta)=-2r(1-eta)-q eta^(q-1)<0` in `(0,1)`, proving threshold uniqueness.
The endpoint and `Gamma1=0` claims follow directly from the same determinant.

For a traceless Hermitian difference, the trace norm is the Euclidean length
of its Bloch vector.  The translation cancels, and the linear Bloch map is a
rotation composed with `diag(exp(-Gamma2 t),exp(-Gamma2 t),exp(-Gamma1 t))`.
Its operator norm is the claimed maximum, attained along a corresponding
axis.  This proves sharpness and the recurrence statements.

## Route-A classification

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
overall `ROUTE_A_REJECTED`; Route B is not invoked.

HEN-O287: a finite phase-covariant GKSL/Choi/Liouvillian calculation cannot be
promoted to an arithmetic determinant.  Strict contraction removes
nonconstant recurrence when `Gamma1>0`; the unitary boundary supplies only one
continuously tunable frequency and a continuum of fixed diagonal states;
finite Choi and characteristic polynomials have no prime-power clock or target
global divisor.  A nonunique Stinespring dilation is not a same-clock
self-adjoint realization of a target zero set.

No target arithmetic local data, Euler factors, root numbers, automorphy,
target divisor/counting law, functional equation, zero match, Hilbert–Pólya
operator, or Route B claim is made.
