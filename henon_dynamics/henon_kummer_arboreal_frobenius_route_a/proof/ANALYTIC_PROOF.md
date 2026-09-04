# Analytic proof ledger

**Proof status:** complete and unconditional for every `n>=3`.

**External inputs:** Capelli's binomial irreducibility criterion, elementary
cyclotomic Galois theory, and Chebotarev density.

**Finite computation role:** none in the proof.

Write `m=2^n`, `alpha=2^(1/m)`, `zeta=zeta_m`,
`L=Q(alpha)`, `C=Q(zeta)`, and `K=LC`.

## Lemma 1: the shared quadratic field

Since `n>=3`, `zeta_8=zeta^(2^(n-3))` lies in `C`, and

```text
sqrt(2)=zeta_8+zeta_8^(-1) in C.
```

It also equals `alpha^(m/2)`, so `Q(sqrt(2))` lies in `L intersect C`.

## Lemma 2: `sqrt(2)` is not a square in `C`

If `y^2=sqrt(2)` with `y in C`, then `y=+/-2^(1/4)`, hence the real pure
quartic field `Q(2^(1/4))` would be an intermediate field of the abelian
Galois extension `C/Q`.  Every intermediate field of an abelian Galois
extension is Galois over the base.  But `Q(2^(1/4))/Q` is not normal:
`X^4-2` is irreducible by Eisenstein at `2`, and the real field
`Q(2^(1/4))` does not contain the conjugate `i*2^(1/4)`.  Contradiction.

## Lemma 3: relative irreducibility and intersection

Over `C`, `alpha` satisfies

```text
X^(m/2)-sqrt(2).
```

Capelli's binomial criterion says that `X^r-a` in characteristic zero is
irreducible if `a` is not a `q`-th power for any prime `q|r`, together with
the standard fourth-power exception when `4|r`.  Here `r=m/2` is a power
of two and Lemma 2 excludes a square.  The exceptional shape
`sqrt(2)=-4c^4` is also impossible because `i in C` would make
`sqrt(2)=(2ic^2)^2`, again a square.  Therefore the displayed polynomial
is irreducible and

```text
[K:C]=m/2,   [K:Q]=(m/2)*phi(m)=2^(2n-2).
```

Eisenstein gives `[L:Q]=m`.  The compositum degree identity yields

```text
[L:L intersect C]=[K:C]=m/2,
```

so `[L intersect C:Q]=2`.  Lemma 1 supplies a quadratic subfield, proving

```text
L intersect C=Q(sqrt(2)).
```

## Lemma 4: exact finite-level image

`K` is the splitting field of `X^m-2`.  Every automorphism has unique
parameters

```text
sigma(zeta)=zeta^a,   sigma(alpha)=zeta^b alpha,
```

with `a` odd modulo `m` and `b` modulo `m`.  Acting on roots gives the
affine map `j -> a*j+b`.  On the shared element `sqrt(2)` the radical
formula gives

```text
sigma(sqrt(2))=(-1)^b sqrt(2).
```

The cyclotomic formula gives

```text
sigma(sqrt(2))=zeta_8^a+zeta_8^(-a)=chi_2(a)sqrt(2).
```

Thus every automorphism lies in `H_n`.  Conversely, `H_n` has
`phi(m)*(m/2)=2^(2n-2)` elements because the character fixes the parity of
`b`.  This equals `[K:Q]`; the faithful injection is therefore onto.

## Lemma 5: restrictions

Choose compatible radicals and roots of unity with
`alpha_n=alpha_(n+1)^2` and `zeta_(2^n)=zeta_(2^(n+1))^2`.  Direct
substitution shows that restriction reduces both `(a,b)` coordinates
modulo `2^n`.  Every `(a,b) in H_n` has two lifts of `a` and two lifts of
`b`; reduction preserves both `a mod 8` and the parity of `b`, so all four
lifts belong to `H_(n+1)`.  Hence restriction is onto with kernel four.
Taking inverse limits gives the stated closed index-two subgroup.

## Lemma 6: fixed-root distribution

The fixed-index equation is

```text
(a-1)j=-b mod 2^n.
```

It has `g=gcd(a-1,2^n)` solutions exactly when `g|b`, and none otherwise.
Because `a` is odd, `g>=2`, so one fixed root is impossible.

- If `a=7 mod 8`, then `chi_2(a)=1`, `b` is even, and
  `v_2(a-1)=1`.  There are `2^(n-3)` such `a` and `2^(n-1)` allowed `b`,
  giving `2^(2n-4)` elements with two fixed roots.
- If `v_2(a-1)=k` with `3<=k<n`, then `a=1 mod 8`, and there are
  `2^(n-k-1)` choices of `a`.  Exactly `2^(n-k)` values of `b` are
  divisible by `2^k`, giving `2^(2n-2k-1)` elements with `2^k` fixed
  roots.
- For `a=1`, only `b=0` fixes all `2^n` roots.
- The valuation `k=2` forces `a=5 mod 8`, hence `chi_2(a)=-1` and `b`
  odd, so the divisibility condition fails.  Four fixed roots never occur.

All remaining elements have no fixed root, proving the complete law.

## Theorem: density

Every odd prime is unramified in `K_n`; the polynomial has separable
reduction.  It has a root modulo `p` exactly when arithmetic Frobenius fixes
a member of `R_n`.  Fixed-point count is conjugacy invariant, so
Chebotarev gives the fraction of fixed-point-bearing elements of `H_n`.
Dividing Lemma 6 by `|H_n|=2^(2n-2)` gives

```text
delta_n
 = 1/4 + sum_(k=3)^(n-1) 2^(1-2k) + 2^(-2n+2)
 = 7/24 + 1/(3*4^(n-1)).
```

The final term tends to zero, hence `delta_n -> 7/24`.

## Finite Koopman realization and boundary

Each Galois element permutes the orthonormal point basis of `l^2(R_n)`, so
its matrix is unitary.  This canonical finite-level representation neither
produces a self-adjoint global operator nor supplies a target determinant.
The real permutation matrices do not by themselves supply a single
family-wide antiunitary that sends every action to its inverse, and this
package supplies no nontrivial orbit phase/weight preservation law.  Thus
the strict grade is `A4_FORMAL_HINT`, not a quantization pass.
