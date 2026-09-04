# Theorem package

Let `gcd(p,q)=1`, `q>=3`, and `lambda>0`.  On `ell^2(Z^2)` fix the
anisotropic Landau-gauge Harper Hamiltonian

```text
(H Psi)_(m,n) = Psi_(m+1,n)+Psi_(m-1,n)
              + lambda exp(2 pi i p m/q) Psi_(m,n+1)
              + lambda exp(-2 pi i p m/q) Psi_(m,n-1).
```

After Fourier transformation in `n`, its magnetic Bloch fiber acts by

```text
(H(k_x,k_y)u)_m = u_(m+1)+u_(m-1)
                 +2 lambda cos(k_y+2 pi p m/q)u_m,
u_(m+q)=exp(i q k_x)u_m.
```

The last line is the phase convention: the stored boundary character is
`X=q k_x`.  Set `D(E;k_x,k_y)=det(EI-H(k_x,k_y))`.

## Main theorem

There is a unique real monic polynomial `P_(p/q,lambda)` of degree `q`
such that, for every real `E,k_x,k_y`,

```text
D(E;k_x,k_y)
 = P_(p/q,lambda)(E)-2 cos(q k_x)-2 lambda^q cos(q k_y).       (1)
```

It has the following complete consequences.

1. **Full two-dimensional spectrum.**  With
   `C_(q,lambda)=2(1+lambda^q)`,

   ```text
   spectrum(H) = {E real: |P_(p/q,lambda)(E)|<=C_(q,lambda)}.  (2)
   ```

2. **Algebraic band edges and contacts.**  The band-edge multiset is the
   real zero multiset of

   ```text
   B(E)=P_(p/q,lambda)(E)^2-C_(q,lambda)^2.                    (3)
   ```

   Its factors are characteristic polynomials of two real symmetric
   endpoint fibers:

   ```text
   P(E)-C=D(E;0,0),
   P(E)+C=D(E;pi/q,pi/q).                                     (4)
   ```

   An edge label is multiple exactly when

   ```text
   P(E)=+C or -C, and P'(E)=0.                                (5)
   ```

   Thus two algebraic edge labels coalesce precisely under (4).  This is
   the closed-gap/contact criterion; it is not a claim that all other gaps
   are open.

3. **Duality and symmetries.**

   ```text
   P_(p/q,lambda)(E)
      =lambda^q P_(p/q,1/lambda)(E/lambda),                   (6)
   P_(p/q,lambda)(E)=P_((q-p)/q,lambda)(E),                    (7)
   P_(p/q,lambda)(-E)=(-1)^q P_(p/q,lambda)(E).                (8)
   ```

4. **Forced even-denominator contact.**  If `q` is even, then

   ```text
   P(0)=2(-1)^(q/2)(1+lambda^q),  P'(0)=0.                    (9)
   ```

   Hence zero is a multiple central edge.  In particular an
   all-gaps-open statement would be false.

5. **Small magnetic cells.**  If coincident periodic neighbors are
   accumulated rather than overwritten, (1) remains valid on the direct
   boundary fibers

   ```text
   q=1, p=0: P(E)=E,
   q=2, p=1: P(E)=E^2-2(1+lambda^2).                         (10)
   ```

   The `q=2` folded bands meet at zero.  As `lambda` tends to zero from
   above, the spectrum tends to the horizontal-chain interval `[-2,2]` and
   the magnetic bands fold together; reciprocal duality is not evaluated
   at `lambda=0`.

## Proof chain

For `zeta=exp(2 pi i/q)` and `y=exp(i k_y)`, put

```text
A_m(E,y) = [[E-lambda(y zeta^(pm)+y^(-1)zeta^(-pm)), -1],
            [1,                                           0]],
M_q=A_(q-1)...A_0.
```

Every `A_m` has determinant one.  The two Floquet multipliers are therefore
`exp(+/- i q k_x)`, and comparison of monic degree-`q` polynomials gives

```text
D(E;k_x,k_y)=tr(M_q(E,y))-2cos(q k_x).                       (10)
```

Replacing `y` by `zeta^p y` cyclically permutes the potential sequence.
The new monodromy is a cyclic conjugate, so its trace is unchanged.  Since
`p` is invertible modulo `q`, `tr M_q`, as a Laurent polynomial of degree at
most `q` in `y`, can have only the powers `-q,0,+q`.  The coefficient of
`y^q` is obtained uniquely by choosing `-lambda y zeta^(pm)` in every
upper-left entry:

```text
(-lambda)^q zeta^(p q(q-1)/2) = -lambda^q.                  (11)
```

The sign is `-1`: if `q` is odd then `q-1` is even, while if `q` is even
then coprimality forces `p` odd.  The `y^(-q)` coefficient is the conjugate
and has the same value.  The remaining coefficient is independent of both
Bloch phases, monic and real; call it `P`.  Equations (10)--(11) prove (1)
and uniqueness.

Magnetic Bloch decomposition expresses the full lattice Hamiltonian as the
direct integral of the fibers.  For fixed `E`, (1) vanishes for some fiber
exactly when

```text
P(E)=2cos(q k_x)+2lambda^q cos(q k_y).
```

The two phases are independent and the right side fills precisely
`[-C,C]`, proving (2).  At `(k_x,k_y)=(0,0)` the phase sum is `C`; at
`(pi/q,pi/q)` it is `-C`.  This proves (4).  The corresponding total
horizontal boundary phases are `0` and `pi`, and both fibers have real
diagonal potentials, so they are real symmetric.  Hence both factors in
(3) are real-rooted.  The criterion (5) follows because `B'=2 P P'` and
`P` is nonzero at an edge.

Interchanging the two lattice axes reverses magnetic orientation and swaps
the hopping amplitudes.  After division by `lambda`, magnetic Fourier
duality gives

```text
H_(p/q,lambda) equivalent to lambda H_((q-p)/q,1/lambda)
```

with the two Bloch characters exchanged.  Comparing the phase-independent
monic parts of (1), and then using complex conjugation to identify fluxes
`p/q` and `(q-p)/q`, proves (5)--(6).

The bipartite involution `Gamma Psi_(m,n)=(-1)^(m+n)Psi_(m,n)` conjugates
`H` to `-H` while shifting both Bloch quasimomenta by `pi`.  Substitution in
(1) proves (8).

For the remaining all-denominator constant term, Lamoureux--Mingo,
Theorem 2.5, prove the vanishing of all intermediate cyclic matching sums;
their Corollary 2.6 gives

```text
Delta_(p/q,L)(0)=2(-1)^(q/2)(1+(L/2)^q)  for even q.
```

Their normalization is
`h_(theta,L)=u+u^-1+(L/2)(v+v^-1)`, whereas the present potential is
`2 lambda cos`, so `L=2 lambda`.  The phase-independent monic discriminant
`Delta_(p/q,2lambda)` is exactly `P_(p/q,lambda)` after comparing their
Chambers formula with (1).  This proves the first identity in (9) for every
even denominator.  Since (8) makes `P` even, `P'(0)=0`.  The finite exact
`q<=10` lane is only a regression check of this sourced theorem.  Finally,
direct scalar and two-by-two determinants with accumulated wrap edges give
(10).

## Evidence and independence

The canonical ledger covers all 78 reduced fluxes with `3<=q<=16`, the
anisotropies `1/2,2/3,1,3/2,2`, and a `12 x 16` grid in the two total Bloch
phases.  It contains 390 panels, 74,880 Hermitian fibers, 825,600
eigenvalues, and 224,640 determinant probes.

The producer constructs `P` by transfer-polynomial multiplication.  The
checker never imports it and instead reconstructs `P` from a reference
fiber characteristic polynomial before rebuilding every fiber.  The SymPy
lane works exactly in `Q[zeta_q]/Phi_q` for all 30 reduced fluxes through
`q=10`, retaining lambda as an exponent variable and verifying phase
support, extreme coefficients, duality, reversal, parity, and (8).  These
are regression receipts; the preceding argument proves the continuum
theorem.

## Source, collision, and Route-A boundary

Harper's magnetic equation, Chambers' relation, and Hofstadter's bands are
established mathematics.  Lamoureux--Mingo (Proc. Amer. Math. Soc. 135
(2007), 3205--3215, DOI `10.1090/S0002-9939-07-08830-2`) directly own the
cyclic-matching cancellation and even-`q` constant term.  C371 contributes
a convention-locked reconstruction, the explicit real endpoint-fiber edge
factorization, and an executable atlas; no object or formula priority is
claimed.  The workspace's direct neighbor HCS-C15/HEN-O30 owns a critical
Weyl--Harper block at flux `1/3^m` and its top spectral edge along a
Heisenberg tower.  It does not own the all-rational two-phase identity,
anisotropic duality, or complete algebraic edge atlas proved here.  C293,
C340, and C356 are respectively a magnetic Grushin cylinder, a Lame
Floquet operator, and a QWZ Chern pump; C371 imports none of their owners.

Reduced rational flux supplies a weak cyclotomic relation, but no canonical
rational-prime carrier, prime-power repetition law, isolated primitive
orbit ledger, logarithmic prime clock, target determinant, target divisor,
or target-zero spectrum.  The source Hamiltonian is naturally
self-adjoint, but it is not a Hilbert--Polya realization.  The locked tuple
is

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,
 A4_NATURAL_QUANTIZATION), overall ROUTE_A_REJECTED.
```

Route B remains locked.  The literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
