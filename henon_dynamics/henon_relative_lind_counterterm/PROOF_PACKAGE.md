# HCS-P71 proof package

## 1. Source lock

Kim--Lee--Park, Example 4.3, gives for the full n-shift with reverse flip

    zeta_(sigma,rho)(t)
      =1/sqrt(1-nt^2)
       exp((nt+(n+n^2)t^2/2)/(1-nt^2)).

For n=2:

    zeta_flip(t)
      =(1-2t^2)^(-1/2)
       exp((2t+3t^2)/(1-2t^2)).

This is the source-defined full infinite-dihedral zeta, not P70's restricted
odd packet product.

## 2. Exact local Lind ledger

Set u=1-sqrt(2)t, so 1-2t^2=u(2-u). The exponential numerator is

    2t+3t^2
      =sqrt(2)(1-u)+(3/2)(1-2u+u^2).

Therefore

    log zeta_flip(t)
      =(1/sqrt(2)+3/4)/u -(1/2)log u + G_L(u),

where G_L is analytic at zero.

## 3. P70 packet ledger and relative mismatch

P70 proves

    log Z_orb(t,1)=1/(sqrt(2)u)+G_orb(u).

Subtracting gives

    log(zeta_flip/Z_orb)
      =3/(4u)-(1/2)log u+G_rel(u).

Thus the odd packet captures the 1/sqrt(2) contribution but leaves a
source-native exponential coefficient 3/4 and a square-root branch.

## 4. Relative extension and uniqueness

Define, on a local branch,

    C_rel(t)=u^(1/2) exp(-3/(4u))
             zeta_flip(t)/Z_orb(t,1).

Its logarithm is G_rel(u), so C_rel extends holomorphically and nonvanishingly
across u=0.

More generally multiply the ratio by u^beta exp(-c/u). Nonzero holomorphic
extension requires cancellation of the essential exponential, hence c=3/4.
It then requires cancellation of the algebraic u^(-1/2), hence beta=1/2.
The pair is unique.

## 5. Claim boundary

PROVED: source formula audit; exact local coefficient comparison; unique
relative counterterm; nonzero local extension.

OPEN: a global single-valued continuation, zeros of the relative germ,
transfer/Fredholm realization, prime semantics, and Route B.
