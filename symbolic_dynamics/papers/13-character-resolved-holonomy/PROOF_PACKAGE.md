# SD-C15 Proof Package

## Main claim

The positive-cocycle `Z`-skew extension has a single, character-resolved
Fredholm family whose zero Fourier mode is the exact tensor-prime Euler
determinant and whose nonzero modes see recurrent mixed base returns.  This is
a genuine gain over scalar Haar averaging.  It does not solve the RH route:
the response is generic, the entropy-derived twists are gauge or parameter
translations, and inverse time reversal forces a mixed power-two leak into
the target mode.

## Theorem 1 -- lifted periodic ledger

Let the base vertices be `n>=1`, with a loop at every vertex and both arrows
between `n` and `n+1`.  Give loops charge zero and cross edges charge one.
The skew extension has vertices `(n,k)` and maps an edge of charge `q` to an
edge from `(n,k)` to `(m,k+q)`.

Every path containing a cross edge has positive total charge, so it cannot
return to its initial lift coordinate.  Modulo deck translation, the only
primitive periodic lifted paths are the atom loops `gamma_p`; their `r`th
repetitions have roof `r log p` and weight `p^(-rs)`.

## Theorem 2 -- trace-class Bloch family

For `sigma=Re(s)>1`, put

```text
d_n(s)=p_n^(-s),
a_n(s)=(d_n(s)+d_(n+1)(s))/2,
L_s(w)=D_s+w A_s.
```

The diagonal singular values are `|d_n|`.  Each directed weighted shift in
`A_s` has singular values `|a_n|`, and

```text
sum_n |a_n(s)| <= sum_n p_n^(-sigma) < infinity.
```

Thus every Bloch fiber `L_s(w)` is trace class, locally holomorphic in
`(s,w)`, and
`D_SD(s,z,w)=det(I-zL_s(w))` is locally holomorphic in `(s,w)` and entire in
`z`.

The lifted operator
`Ltilde_s=D_s tensor 1+A_s tensor U` is instead an element of the semifinite algebra
`B(l^2(N)) bar-tensor L(Z)` and is trace class for `Tr tensor tau_Z`; ordinary
trace class fails because deck translation has infinite multiplicity.

## Theorem 3 -- exact Euler zero mode

Expand a power trace by closed base words:

```text
Tr L_s(w)^r = sum_(m>=0) c_(r,m)(s) w^m.
```

The exponent `m` is the total cross-edge charge.  A degree-zero closed word
uses no cross edge, so

```text
c_(r,0)(s)=sum_p p^(-rs).
```

On the common trace-log germ,

```text
[w^0] log D_SD(s,z,w)
  = -sum_(r>=1) z^r/r sum_p p^(-rs)
  = sum_p log(1-zp^(-s)).
```

Because every other trace coefficient has positive `w` degree, exponentiation
also gives

```text
[w^0] D_SD(s,z,w)=product_p (1-zp^(-s)).
```

The coefficient can equivalently be read by Haar averaging a consistently
chosen local logarithm over `w=exp(i theta)`.  No global log branch is claimed.

## Theorem 4 -- exact two-atom response

For masses `x,y` and `a=(x+y)/2`,

```text
L(w)=[[x,aw],[aw,y]],
det(I-zL(w))=(1-zx)(1-zy)-z^2 a^2 w^2.
```

Hence the first nonconstant determinant coefficient is nonzero for every
positive inventory, while the constant coefficient remains the pure-loop
factor.  Character visibility is exact, but this formula already predicts
the nonprime controls will move too.

For `N` atoms, the continuant gives the stronger exact coefficient

```text
[w^2]D_N = -z^2 sum_(n=1)^(N-1) a_n^2
            product_(j notin {n,n+1})(1-zd_j).
```

At the frozen real points every factor is positive, so this coefficient is
strictly negative for every positive mass inventory.

## Theorem 5 -- no unified Bloch fiber

For every unitary character `|w|=1`,

```text
Tr L_s(w)^2 = sum_n d_n^2 + 2 w^2 sum_n a_n^2.
```

The second term is nonzero at the frozen real points.  Thus no genuine Bloch
fiber has the exact all-order Euler ledger.  The exact target is the
equivariant coefficient-zero sector; `w=0` recovers it algebraically but is
not a unitary deck character and deletes the cross grammar.

## Theorem 6 -- gauge, translation, and holonomy trilemma

Let a reversed edge pair have integer charges `q` and `qbar`.

1. If `q_e=psi(target)-psi(source)`, then on `|w|=1`
   `L(w)=U_psi(w)L(1)U_psi(w)^(-1)`.  The Fredholm determinant is character
   independent.  Entropy and rank coboundaries therefore give only gauge.
2. If the character is attached to the roof, then
   `p^(-s) exp(i theta log p)=p^(-(s-i theta))`; the family is only a vertical
   reparameterization of the original spectral variable.
3. The adjacent mixed two-cycle has Fourier charge `q+qbar`.  Keeping it out
   of degree zero requires `q+qbar!=0`.  Inverse time reversal requires
   `qbar=-q` and therefore moves the mixed term into degree zero at power two.

Thus recurrent base motion, exact Euler zero mode, and inverse time reversal
cannot coexist in this local character construction.

## Theorem 7 -- no arithmetic selectivity from character resolution alone

The proofs of Theorems 1--4 use only positivity of the cross charges,
summability of the masses, and nonzero cross amplitudes.  They do not use
primality after the atom inventory has been chosen.  Every positive composite
or random mass list, every forward-DAG grammar, and every positive random
charge field has the same structural zero-mode theorem and a nonconstant
two-vertex response.  Consequently character resolution is a same-parent
equivariant analytic improvement but not an arithmetic selector or a unified
scalar determinant.

## Route conclusion

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_EQUIVARIANT_EULER_LEDGER
GO_CHARACTER_RESOLUTION
STOP_UNIFIED_BLOCH_FIBER
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
STOP_INVERSE_TIME_REVERSAL
ROUTE_B_LOCKED
```

The A0 credit belongs only to the tensor-prime source.  A1 and A2 refer to
the periodic ledger modulo deck translation and the same Bloch-resolved
Fredholm object.  A3 fails because the moving fibers do not own the target
ledger and there is no continuation, Gamma factor, functional equation,
Riemann--von Mangoldt law, Weil compression, or target divisor theorem.
