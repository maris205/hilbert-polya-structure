# HCS-P74 proof package

## 1. Frozen source and sign convention

Let

    Phi(x)=2x/(1-2x^2),
    c_m=(1/m) product_(p|m,p odd)(1-p),
    rho_m=2^(-1/(2m)).

P72 proves, on the appropriate slit continuation of the punctured unit disk,

    log C_rel(t)
      =H_rel(1-sqrt(2)t)-sum_(m>=2)c_m Phi(t^m),              (1)

where

    H_rel(u)=-(1/2)log(2-u)-3(2u-3)/[4(u-2)].                (2)

The multiplier class in this paper is

    W_(d,G)(t)
      =exp(sum_(m>=2)d_m Phi(t^m)+G(t)).                     (3)

Thus the combined channel coefficient is `d_m-c_m`.  This convention is
fixed throughout: cancellation requires `d_m=c_m`.

Assume

    sum_(m>=2)|d_m| r^m < infinity for every 0<r<1,           (4)

and `G` is holomorphic on the unit disk.  Condition (4) is a direct,
checkable hypothesis ensuring normal convergence away from the locally
finite pole set.  The exact sequence `d_m=c_m` satisfies it because
`|c_m|<=1`.

## 2. Complex pole ledger

For `0<=k<2m`, put

    alpha_(m,k)=rho_m exp(pi i k/m),
    b_(m,k)=c_m (-1)^k/(sqrt(2)m).                            (5)

The weighted root-of-unity filter gives the exact partial fraction identity

    c_m Phi(t^m)
      =sum_(k=0)^(2m-1) b_(m,k)/(1-t/alpha_(m,k)).            (6)

Indeed, after writing `x=t/rho_m`, expand the right side geometrically.  The
inner sum

    sum_(k=0)^(2m-1)(-1)^k exp(-pi i k j/m)

is `2m` when `j` is congruent to `m` modulo `2m` and is zero otherwise.
Since `rho_m^m=1/sqrt(2)`, the surviving terms are precisely

    2c_m t^m+4c_m t^(3m)+8c_m t^(5m)+... .

The radii `rho_m` are strictly increasing.  Hence a pole
`alpha_(m,k)` belongs to channel `m` alone.

## 3. Theorem: coefficientwise cancellation rigidity

Let

    D_2={|t|<1} minus {alpha_(m,k):m>=2, 0<=k<2m}.

Under (4), the series in (3) is normally convergent on compact subsets of
`D_2`.  Suppose that

    W_(d,G)(t) exp(-sum_(m>=2)c_m Phi(t^m))                  (7)

has a meromorphic continuation across every deleted point.  Then

    d_m=c_m for every m>=2.                                  (8)

Consequently (7) is `exp(G(t))`, which is holomorphic and nowhere zero on
the unit disk.

### Proof

Fix `m` and `k`.  Normal convergence makes every channel `j!=m` holomorphic
near `alpha_(m,k)`.  By (6), the logarithm of (7) has principal part

    (d_m-c_m)(-1)^k/
      [sqrt(2)m(1-t/alpha_(m,k))].                            (9)

If `d_m-c_m` is nonzero, exponentiating the nonzero simple pole produces an
essential singularity, contradicting meromorphic removability.  Thus
`d_m=c_m`.  The argument applies independently to every `m>=2`.  Substitution
in (7) leaves `exp(G)`.  This proves the theorem.

Meromorphic removability in the hypothesis is intentionally stronger than
needed: an exponential of a nonzero pole is not even meromorphic.

## 4. Theorem: the negative source pair is rigid

Put

    w=1+sqrt(2)t=2-u.

Equation (2) becomes the exact identity

    H_rel(2-w)=3/(4w)-(1/2)log w-3/2.                        (10)

Choose any local slit and a branch of `log w`.  Let `a,beta` be complex.
After the channels have been cancelled, multiplication by

    w^beta exp(-a/w)                                         (11)

has logarithm

    (3/4-a)/w+(beta-1/2)log w-3/2+G(t).                      (12)

It extends holomorphically and nonvanishingly across `w=0` if and only if

    (a,beta)=(3/4,1/2).                                      (13)

### Proof

A nonzero coefficient of `1/w` gives an exponential essential singularity,
so `a=3/4`.  The remaining factor `w^(beta-1/2)` can extend holomorphically
and nonvanishingly only with exponent zero, so `beta=1/2`.  Conversely these
values reduce (12) to `-3/2+G(t)`, which is holomorphic and finite.  This
proves both necessity and sufficiency.

Thus the forced pair contributes the scalar factor `exp(-3/2)`, while the
full residual in the general gauge is

    exp(-3/2) exp(G(t)) = exp(-3/2) A(t),  A(t):=exp(G(t)).

It is the constant `exp(-3/2)` in the distinguished `G=0` gauge used by the
normalized genus-`m-1` construction below.

If one asks only for a meromorphic, possibly zero or polar extension, the
weaker conclusion is `a=3/4` and `beta-1/2` integral.  The nonvanishing
hypothesis is therefore essential to the exact uniqueness statement.

## 5. Theorem: holomorphic gauge torsor

Let `R_ch=exp(-sum_(m>=2)c_m Phi(t^m))` on `D_2`.  The multipliers of the
form (3) for which `W R_ch` extends holomorphically and nowhere zero to the
unit disk form a torsor under

    O(unit disk)^x,

the multiplicative group of nowhere-zero holomorphic functions on the disk.
Explicitly, every such multiplier is uniquely

    W=exp(sum_(m>=2)c_m Phi(t^m)) A(t),                       (14)

where `A` belongs to `O(unit disk)^x`.

### Proof

The coefficient theorem forces the singular series in (14).  The quotient
`A=W/exp(sum c_m Phi)` equals the extended product `W R_ch`, so it is
holomorphic and nowhere zero.  Conversely every such `A` gives an admissible
multiplier.  Since the disk is simply connected, every `A` has a holomorphic
logarithm `G`, so (14) is exactly the class (3).  Multiplication by `A`
acts freely and transitively.

The source factor (11) does not remove this gauge.  With the forced pair
(13), the completely source- and channel-renormalized relative object is

    exp(-3/2) A(t).                                          (15)

## 6. Primary factors and exact residuals

The gauge is already visible in two natural order-independent pole products.
For `z=t/alpha_(m,k)` define the relative multiplier factor

    P_(m,k)^[g](t)
      =exp(b_(m,k)[1/(1-z)-sum_(j=0)^g z^j])
      =exp(b_(m,k) z^(g+1)/(1-z)).                           (16)

It has the positive principal exponential needed to cancel the negative
channel in (1).

### Genus `m-1`: channel annihilation

The root filter in Section 2 gives

    sum_(k=0)^(2m-1) log P_(m,k)^[m-1]
      =c_m Phi(t^m).                                         (17)

Therefore

    W_-(t)=product_(m>=2) product_(k<2m) P_(m,k)^[m-1](t)
          =exp(sum_(m>=2)c_m Phi(t^m)),                       (18)

and `W_- R_ch=1`.  Here `G=0`.

### Genus `m`: source-leading preservation

At degree `m`, the root filter instead gives

    sum_(k=0)^(2m-1)b_(m,k)(t/alpha_(m,k))^m=2c_m t^m.

Hence

    sum_k log P_(m,k)^[m]
      =c_m Phi(t^m)-2c_m t^m,                                (19)

and

    W_+(t)=exp(sum_(m>=2)c_m Phi(t^m)
                 -2sum_(m>=2)c_m t^m).                       (20)

The renormalized channel residual is the explicit nonconstant function

    W_+ R_ch=exp(-2sum_(m>=2)c_m t^m).                        (21)

It is holomorphic and nowhere zero for `|t|<1`.  An equivalent product form
is

    exp(2t) product_(d>=1,d odd)(1-t^d)^(2mu(d)),             (22)

where the logarithm of the product converges normally in the unit disk.

### Normal convergence and order independence

Let `K` be compact in `D_2`, and choose `r<q<1` with `|t|<=r` on `K`.
For all sufficiently large `m`, `|t/alpha_(m,k)|<=q`.  Since `|c_m|<=1`,

    sum_(k<2m)|log P_(m,k)^[m-1](t)|
      <=sqrt(2) q^m/(1-q),                                   (23)

and the genus-`m` bound has `q^(m+1)` in place of `q^m`.  Both majorants are
summable in `m`.  Thus both double logarithmic series converge absolutely
and normally on compact subsets.  Their products are independent of every
enumeration of the individual complex poles, not merely of channel order.

Equations (18) and (20) show that two source-ordered, order-independent
regularizations differ by the nontrivial holomorphic gauge (21).  Cancellation
alone therefore does not select an absolute canonical object.

## 7. Normalized trivialization and finite jets

For genus `m-1`, (15) with `A=1` is the constant `exp(-3/2)`.  If the final
normalization requires value one, the scalar `exp(3/2)` is forced and the
fully renormalized relative object is identically one.  This is a proved
trivialization inside the declared normalization, not a statement that all
renormalizations are trivial.

No finite Taylor jet fixes the gauge.  Fix `N>=0` and a base point `t_0` in
the disk.  For every complex `lambda`,

    A_lambda(t)=exp(lambda (t-t_0)^(N+1))                     (24)

is nowhere zero, agrees with `1` through order `N` at `t_0`, and is
nonconstant when `lambda!=0`.  Only an infinite-jet condition, or an
independent axiom such as `G=0`, removes this freedom.

## 8. Monodromy boundary

All factors in (16) are exponentials of single-valued rational functions on
`D_2`; their monodromy is trivial.  On a slit disk one may artificially add
`lambda log(1-t/alpha)` to a counterterm logarithm.  Gluing its exponential
to the punctured disk requires integral `lambda`, and requiring a nowhere-zero
extension forces `lambda=0`.  Nontrivial slit monodromy is therefore extra
regularization data, not information forced by P72.

## 9. Claim boundary

**PROVED:** coefficientwise rigidity in the declared normally convergent
channel-log class; uniqueness of the negative source pair for nonzero
holomorphic extension; holomorphic gauge-torsor classification; normal and
order-independent genus `m-1` and genus `m` products; their exact residuals;
normalized trivialization for `G=0`; finite-jet nonuniqueness.

**NOT PROVED:** that `G=0`, genus `m-1`, genus `m`, or any other gauge is
absolutely canonical without an additional axiom; ownership by a transfer
operator or determinant; rational-prime or von-Mangoldt semantics; a
functional equation; a self-adjoint spectrum; Route B.
