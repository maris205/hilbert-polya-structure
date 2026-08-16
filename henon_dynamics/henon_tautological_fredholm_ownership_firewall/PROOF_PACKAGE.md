# HCS-P77 proof package

## 1. Frozen punctured channel domain

For `q>0`, P75--P76 prove

    log Z_ch(z,q)=sum_(m>=1) h_m(z,q),
    h_m(z,q)=c_m Psi_m(z,q),
    Psi_m(z,q)=2(qz)^m/[1-(1+q^(2m))z^(2m)],

with

    c_m=(1/m)product_(p|m,p odd)(1-p),  0<|c_m|<=1.

Let

    L(q)=min(1,q^(-1)),
    Sigma_q={rho_m(q) exp(pi i k/m):m>=1,0<=k<2m},
    Omega_q={|z|<L(q)}\Sigma_q.

The scalar channel continuation is holomorphic and nonvanishing on
`Omega_q` and has a natural-boundary circle at `|z|=L(q)`.  P77 does not
renormalize or cross that boundary.

## 2. Channel-diagonal trace-class realization

On `ell^2(N)`, define

    A(z,q)=diag(h_1(z,q),h_2(z,q),...).

Let `K` be a compact subset of `Omega_q` and choose `r<L(q)` with `|z|<=r`
on `K`.  Then both `r<1` and `qr<1`.  The finitely many early denominators
are bounded away from zero.  For all sufficiently large `m`,

    |1-(1+q^(2m))z^(2m)|
      >=1-r^(2m)-(qr)^(2m)>=1/2,

so

    |h_m(z,q)|<=4(qr)^m.

Thus `sum_m |h_m|` converges locally uniformly.  It follows that `A` is a
holomorphic trace-class-valued family and

    Tr A(z,q)=sum_m h_m(z,q)=log Z_ch(z,q).

Put

    K_ch(z,q)=exp(A(z,q))-I.

For the tail, `|exp(h_m)-1|<=exp(|h_m|)|h_m|`; hence `K_ch` is also locally
trace class and holomorphic.  The canonical trace-ideal identity gives

    det_F(I+K_ch)
      =det_F(exp A)
      =exp(Tr A)
      =Z_ch(z,q).

This is a valid punctured-domain Fredholm determinant.

## 3. Universal rank-one firewall

Let `U` be any complex domain, let `F` be a nonvanishing holomorphic
function on `U`, and let `P` be any rank-one orthogonal projection.  Define

    K_F(z)=(F(z)-1)P.

Then `K_F` is a holomorphic trace-class family.  Its only possibly nonzero
eigenvalue is `F(z)-1`, so

    det_F(I+K_F(z))=1+(F(z)-1)=F(z).

Therefore the existence of a parameter-dependent trace-class family whose
Fredholm determinant equals a previously known scalar function is universal.
The channel-diagonal construction records the P75 decomposition, but it is
still built from `log Z_ch`; it does not independently derive the scalar
from transport, a fixed generator, or periodic-point traces.  Its ownership
status is `PROVED_TAUTOLOGICAL`, not a genuine transfer theorem.

## 4. Source-native finite cyclic blocks

Let `omega` be a primitive marked reflection word of odd length `n`, and put

    chi_j=chi(sigma^j omega) in {0,1},
    S=sum_(j=0)^(n-1) chi_j.

On `C^n` with cyclic basis `e_0,...,e_(n-1)`, define

    B_omega e_j=q^(chi_j)e_(j+1 mod n).

One full turn gives

    B_omega^n=q^S I.

The characteristic polynomial is `lambda^n-q^S`, and therefore

    det(I-zB_omega)=1-z^n q^S.

Write `D_omega(z)=det(I-zB_omega)`.  This is exactly the physical Euler
denominator polynomial in P70; the corresponding P70 factor is
`D_omega(z)^(-1)`.  Moreover,

    B_omega^* B_omega e_j=q^(2chi_j)e_j,

so the singular values of `B_omega` are precisely the source edge weights
`q^(chi_j)` in `{1,q}`.  In particular,

    min(1,q)||x|| <= ||B_omega x|| <= max(1,q)||x||.

No artificial period damping has been introduced.

## 5. Singleton words and failure of the full direct sum

For every odd `n>=3`, let `omega_n` have one symbol `1` at the reflection
center and zeros elsewhere.  It is reflection fixed.  It is primitive:
if its least period were a proper divisor `d`, repetition would create at
least `n/d>1` symbols equal to one.  Finally,

    S_n chi(omega_n)=n-2,

because exactly the two centers adjacent to the singleton compare unequal
symbols; all other comparisons are equal.  Thus there is at least one
primitive physical block at every odd length.

Let

    B_q=direct_sum_(n odd) direct_sum_(omega in A_n) B_omega

on the Hilbert direct sum of the finite orbit spaces.  The common upper bound
shows that `B_q` is bounded, while the common lower bound gives

    ||B_q x||>=min(1,q)||x||.

The Hilbert space is infinite dimensional by the singleton blocks.  Images
of one unit basis vector from each singleton block are mutually orthogonal
and have norm at least `min(1,q)`.  Therefore `B_q` is not compact.  Hence

    B_q notin S_p for every 0<p<infinity,

and `zB_q` is not trace class for `z!=0`.  Thus the standard determinant
`det_F(I-zB_q)` is not defined.  This does not assert that `I-zB_q` is
never a Fredholm operator.  Reciprocal finite block determinants reproduce
finite P70 Euler products, but the undamped full block sum cannot be
promoted by determinant continuity in trace norm.

## 6. Locally finite graded power ledger

For a single block,

    diagonal_sum(B_omega^r)
      = 0,                         if n does not divide r,
      = n q^((r/n)S),              if n divides r.

For fixed `r`, only the finitely many odd divisors `n|r` contribute, giving
the same finite coefficient ledger as P70.  Since `B_q^r` remains
noncompact, this canonical-basis diagonal sum is not a Hilbert-space trace
and cannot justify a Fredholm determinant.  It is recorded only as a formal
graded trace identity.

## 7. Claim boundary

**PROVED_TAUTOLOGICAL:** the punctured channel-diagonal trace-class family
and its Fredholm determinant.

**PROVED:** the universal rank-one lemma; every source-native finite cyclic
block; its exact determinant, power law, and singular values; the singleton
family; boundedness and noncompactness of the full direct sum.

**REFUTED:** trace-class or Schatten ownership by the undamped source-native
full orbit-block direct sum, and the associated standard trace-class
determinant.

**OPEN:** an independently derived genuine transfer operator that owns the
weighted channels on a source-native state space.

No rational-prime semantics, von-Mangoldt trace, self-adjoint Hilbert--Polya
operator, arithmetic advance, or Route-B authorization follows.
