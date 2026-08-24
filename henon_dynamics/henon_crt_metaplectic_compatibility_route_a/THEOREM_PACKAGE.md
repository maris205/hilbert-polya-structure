# Theorem package — HCS-C136

## Frozen family

Let `r>=3` be odd, let `c` be a unit modulo `r`, put
`omega_r=exp(2*pi*i/r)`, and let `h_r` be the inverse of two modulo `r`.
On the standard basis of `H_r=C^r`, define

\[
 Q_r|x\rangle=\omega_r^x|x\rangle,\qquad
 P_r|x\rangle=|x+1\rangle,
\]

\[
 W_{r,c}(q,p)=\omega_r^{-c h_rqp}Q_r^{cq}P_r^p,
\]

\[
 (\mathcal F_{r,c})_{xy}=r^{-1/2}\omega_r^{cxy},\qquad
 (C_{r,c})_{xx}=\omega_r^{3c h_rx^2},\qquad
 U_{r,c}=C_{r,c}\mathcal F_{r,c}^{-1}.
\]

Let `K_r` be coefficientwise complex conjugation in that residue basis and set

\[
 \Theta_{r,c}=\mathcal F_{r,c}K_r.
\]

At `c=1` these are exactly the C131 conventions.

## Theorem 1 — generalized-character lift and antiunitary reversal

For every odd `r>=3` and every unit `c mod r`, `U_(r,c)` is unitary and

\[
 U_{r,c}W_{r,c}(q,p)U_{r,c}^{-1}
 =W_{r,c}(3q-p,q).
\]

Thus one application of `U_(r,c)` implements one application of

\[
 A=\begin{pmatrix}3&-1\\1&0\end{pmatrix}
\]

on every generalized Weyl observable.

The same family has a canonical antiunitary involution satisfying

\[
 \Theta_{r,c}^{2}=I,
 \qquad
 \Theta_{r,c}U_{r,c}\Theta_{r,c}^{-1}=U_{r,c}^{-1},
\]

and, for every `(q,p)`,

\[
 \Theta_{r,c}W_{r,c}(q,p)\Theta_{r,c}^{-1}=W_{r,c}(p,q).
\]

### Proof

Because `c` is a unit, `omega_r^c` is primitive.  Fourier orthogonality makes
`F_(r,c)` unitary, while the chirp is diagonal unitary.  Direct conjugation
gives

\[
 \mathcal F_{r,c}^{-1}Q_r^c\mathcal F_{r,c}=P_r,
 \qquad
 \mathcal F_{r,c}^{-1}P_r\mathcal F_{r,c}=Q_r^{-c}.
\]

The chirp fixes `Q_r^c` and sends `P_r` to `W_(r,c)(3,1)`.  Hence `U_(r,c)`
sends the two Weyl generators to `W_(r,c)(3,1)` and `W_(r,c)(-1,0)`.
The symmetric half-phase cancels the product cocycle for a general `(q,p)`,
giving the displayed identity with no scalar.

For the antiunitary assertions, coefficientwise conjugation gives
`bar(F_(r,c))=F_(r,c)^(-1)` and `bar(C_(r,c))=C_(r,c)^(-1)`.  Therefore

\[
 \Theta_{r,c}^{2}=\mathcal F_{r,c}\overline{\mathcal F_{r,c}}=I,
\]

and, since `bar(U_(r,c))=C_(r,c)^(-1) F_(r,c)`,

\[
 \Theta_{r,c}U_{r,c}\Theta_{r,c}^{-1}
 =\mathcal F_{r,c}\overline{U_{r,c}}\mathcal F_{r,c}^{-1}
 =\mathcal F_{r,c}C_{r,c}^{-1}=U_{r,c}^{-1}.
\]

Also `K_r W_(r,c)(q,p) K_r=W_(r,c)(-q,p)`.  The exact Fourier
conjugations

\[
 \mathcal F_{r,c}Q_r^{ca}\mathcal F_{r,c}^{-1}=P_r^{-a},
 \qquad
 \mathcal F_{r,c}P_r^b\mathcal F_{r,c}^{-1}=Q_r^{cb}
\]

then give

\[
 \mathcal F_{r,c}W_{r,c}(-q,p)\mathcal F_{r,c}^{-1}
 =\omega_r^{c h_rqp}P_r^qQ_r^{cp}
 =W_{r,c}(p,q),
\]

where `P_r^q Q_r^(cp)=omega_r^(-cpq) Q_r^(cp)P_r^q` and
`h_r-1=-h_r mod r`.  This proves all three antiunitary identities without a
phase ambiguity.

## Theorem 2 — exact two-factor CRT tensor identity

Let `M,N>1` be odd and coprime, put `L=MN`, and let `c` be a unit modulo
`L`.  Define

\[
 a=N^{-1}\pmod M,\qquad b=M^{-1}\pmod N,
\]

\[
 c_M=(c\bmod M)a\pmod M,\qquad
 c_N=(c\bmod N)b\pmod N.
\]

The canonical unitary

\[
 J_{M,N}|x\bmod L\rangle
 =|x\bmod M\rangle\otimes|x\bmod N\rangle
\]

satisfies

\[
 J_{M,N}\mathcal F_{L,c}J_{M,N}^{-1}
 =\mathcal F_{M,c_M}\otimes\mathcal F_{N,c_N},
\]

\[
 J_{M,N}C_{L,c}J_{M,N}^{-1}
 =C_{M,c_M}\otimes C_{N,c_N},
\]

\[
 J_{M,N}W_{L,c}(q,p)J_{M,N}^{-1}
 =W_{M,c_M}(q_M,p_M)\otimes W_{N,c_N}(q_N,p_N),
\]

and therefore

\[
 J_{M,N}U_{L,c}J_{M,N}^{-1}
 =U_{M,c_M}\otimes U_{N,c_N}.
\]

It also satisfies the exact antiunitary identity

\[
 J_{M,N}\Theta_{L,c}J_{M,N}^{-1}
 =\Theta_{M,c_M}\mathbin{\widehat\otimes}\Theta_{N,c_N}.
\]

Here the hat denotes the canonical conjugate-linear product map in the
ordered residue bases: its matrix part is the Kronecker product of the two
Fourier matrices and it conjugates coefficients in the product basis.  Define
it first on pure tensors by sending `v tensor w` to
`Theta_(M,c_M)(v) tensor Theta_(N,c_N)(w)`, then extend conjugate-linearly to
the full tensor product.  No tensor product of unspecified anti-linear
structures is being invoked.

Every identity is exact; there is no projective scalar.

### Proof

Put `e_M=Na` and `e_N=Mb` modulo `L`.  They are orthogonal idempotents,
sum to one, and reconstruct

\[
 x=e_Mx_M+e_Nx_N\pmod L.
\]

The cross term in `xy` is divisible by `L`, while

\[
 \frac{e_M^2}{L}=\frac{Na^2}{M}\equiv\frac aM\pmod1,
 \qquad
 \frac{e_N^2}{L}=\frac{Mb^2}{N}\equiv\frac bN\pmod1.
\]

Consequently

\[
 \frac{cxy}{L}\equiv
 \frac{c_Mx_My_M}{M}+\frac{c_Nx_Ny_N}{N}\pmod1.
\]

Also `h_L` reduces to `h_M` and `h_N`.  These facts prove the Fourier and
chirp identities entry by entry.  The same character decomposition sends
`Q_L^{cq}` to `Q_M^{c_Mq_M} tensor Q_N^{c_Nq_N}`, while `P_L^p` shifts both
residue coordinates, proving the Weyl identity.  Multiplying the chirp and
inverse-Fourier identities proves the unitary identity.  The positive real
normalization obeys `L^(-1/2)=M^(-1/2)N^(-1/2)`, so no phase remains hidden.
Finally, `J_(M,N)` is a real basis permutation, so it intertwines `K_L` with
coefficientwise conjugation in the ordered product basis.  Combining this
fact with the Fourier identity proves the displayed antiunitary factorization.

## Theorem 3 — exact finite-factor coherence

Fix an ordered list `r_1,...,r_k>1` of pairwise-coprime odd integers,
`L=product_j r_j`, and let `c` be a unit modulo `L`.  Under the canonical
residue-basis unitary, define

\[
 c_j=(c\bmod r_j)(L/r_j)^{-1}\pmod{r_j}.
\]

Then

\[
 J U_{L,c}J^{-1}=\bigotimes_{j=1}^k U_{r_j,c_j}.
\]

With the iterated ordered-basis meaning of the hat tensor, one also has

\[
 J\Theta_{L,c}J^{-1}
 =\mathbin{\widehat\bigotimes}_{j=1}^k\Theta_{r_j,c_j}.
\]

For these fixed ordered leaves, the resulting local characters and both
operator identities are independent of the binary split schedule and its
parenthesization, after the canonical associator of finite tensor products.
No invariance under permuting the leaves, and no symmetric-monoidal or
braiding theorem, is asserted.

### Proof

The n-ary phase identity follows from the CRT idempotents

\[
 e_j=(L/r_j)(L/r_j)^{-1}\pmod{r_j}.
\]

Alternatively, split a product `RS` first.  A factor `r|R` receives

\[
 c\,S^{-1}\,(R/r)^{-1}
 =c\,(L/r)^{-1}\pmod r.
\]

Thus a second split produces the direct n-ary coefficient.  Induction proves
bracket independence, and Theorem 2 at every node proves both operator
identities.  The induction never permutes the fixed ordered leaves.

## Proposition — naive standard-family obstruction

For nontrivial coprime odd `M,N`, the canonical `J_(M,N)` does not satisfy

\[
 J_{M,N}U_{MN,1}J_{M,N}^{-1}
 =\zeta\,(U_{M,1}\otimes U_{N,1})
\]

for any scalar `zeta`.

### Proof

The output row `(x_M,x_N)=(0,0)` has every kernel entry equal to
`(MN)^(-1/2)` on both sides, forcing `zeta=1`.  In the output row `(1,0)`,
the ratio between input columns `(1,0)` and `(0,0)` is `omega_M^(-a)` for
the induced factor and `omega_M^(-1)` for the standard factor.  Equality
therefore forces `a=1 mod M`; the analogous `N` ratio forces `b=1 mod N`.
But `a=b=1` would require both `N=1 mod M` and `M=1 mod N`, impossible for
`M,N>1`.

At `(M,N)=(3,5)`, `a=b=2`.  Already at Fourier entry `x=y=1`, the global
exponent modulo 15 is `1`; the naive standard tensor exponent is `5+3=8`,
while the inverse-scaled exponent is `5*2+3*2=16=1 mod 15`.

## Scope and strict assessment

The coherence theorem belongs to the induced additive-character family.  It
does not construct or classify local corrections back to the standard
`c=1` factors.  It does not address noncoprime factors or an even-level
replacement for the frozen half-phase convention.  Its multifactor coherence
is associativity for fixed ordered leaves only, not permutation coherence.

The strict tuple is

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.

Route B is unauthorized.  No target divisor, analytic completion,
semiclassical trace law, Euler factor, root number, automorphy, or
Hilbert--Polya operator is claimed.
