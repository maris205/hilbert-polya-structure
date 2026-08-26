# Paper 21 Phase-3 relative-conductor theorem

Date: **2026-08-24**

Status: **PROOF PASS / QUANTITATIVE FRAMING REVISED**

The local conductor gate closes exactly.  The resulting
Thorner--Zaman specialization is an unconditional asymptotic improvement
over the stronger exact Kadiri--Wong input `|D_E|^310`, and therefore also
over the Phase-2 envelope `exp(310B)`.  It does not improve the
Bach--Sorenson ERH logarithmic-square bound, and the unpublished numerical
value of Thorner--Zaman's implied constant prevents a named finite cutoff.

## 1. Frozen fields

Fix distinct primes `p,r` and an integer `m>=1`.  Put

```text
E = Q(zeta_(r^(m+1)), p^(1/r)),
F = Q(zeta_r),
H = Gal(E/F).
```

The imported Paper-15 intersection calculation gives

```text
[E:Q] = r^(m+1)(r-1).
```

For odd `r`,

```text
H ~= C_r x C_(r^m).
```

For `r=2`, the cyclotomic group is generally noncyclic and is treated by
Dirichlet characters rather than by a false cyclic replacement.

The selected Paper-15 conjugacy class meets `H` and returns exactly

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.
```

The full exact-condition density and selected-class density remain,
respectively,

```text
(r-1)/r^(m+1),
r^(-(m+1)).
```

## 2. Odd `r`: character-by-character conductors

Write

```text
d = r-1,
lambda = (1-zeta_r),
w = v_r(p^d-1),
epsilon = 2 if w=1, and 0 if w>=2.
```

Fermat gives `w>=1`.  Let `kappa` generate the character group of the
Kummer factor `C_r`, and let `psi` be a cyclotomic character.

### 2.1 Primes over `p`

At every prime `P|p` of `F`, the polynomial `X^r-p` is Eisenstein.  Since
`p!=r`, the resulting degree-`r` extension is totally and tamely ramified.
Thus

```text
a_P(kappa^a psi) = 0 if a=0, and 1 if a!=0.
```

The cyclotomic factor is unramified at `P`.  The global `p`-part of the
conductor is therefore `p O_F` exactly when the Kummer component is
nontrivial, and

```text
Norm_(F/Q)(p O_F)=p^(r-1).
```

### 2.2 The Kummer character at `lambda`

Let `K=F_lambda=Q_r(zeta_r)`, normalized by
`v_K(zeta_r-1)=1`, and let `omega(p)` be the Teichmueller lift of `p mod r`.
The Kummer class is represented by

```text
u=p/omega(p) in 1+r Z_r.
```

The `r`-adic logarithm gives

```text
(1+r Z_r)^r = 1+r^2 Z_r.
```

If `w>=2`, then `p` is already an `r`-th power in `Q_r`; the local Kummer
character is trivial and has exponent zero.

If `w=1`, write `u=1+rc` with `c` an `r`-adic unit and take
`alpha^r=u`.  In `M=K(alpha)`, with its integer-normalized valuation, the
Newton polygon of `(1+X)^r-u` gives

```text
v_M(zeta_r-1)=r,
v_M(alpha-1)=r-1.
```

Hence

```text
varpi=(alpha-1)^(r-1)/(zeta_r-1)^(r-2)
```

is a uniformizer.  For a nontrivial Kummer automorphism
`tau(alpha)=zeta_r alpha`, direct substitution gives

```text
v_M(tau(varpi)-varpi)=2.
```

The unique ramification break is therefore `1`, so every nontrivial local
Kummer character has conductor exponent `2`.

### 2.3 Cyclotomic characters at `lambda`

Let

```text
F_j=Q(zeta_(r^(j+1))),       1<=j<=m.
```

The standard cyclotomic discriminant formula gives

```text
D_(F_j/F)=lambda^[j(r-1)r^j].
```

If `f_j` is the conductor exponent of a character of exact order `r^j`, the
conductor--discriminant formula and subtraction at successive `j` give

```text
phi(r^j) f_j
 = j(r-1)r^j-(j-1)(r-1)r^(j-1),
```

and hence

```text
f_j=j(r-1)+1.                                      (2.1)
```

The smallest nonzero value is `r>=3`, strictly larger than the possible
Kummer exponent `2`.  Thus a product with a nontrivial cyclotomic character
cannot suffer local cancellation at `lambda`.

### 2.4 Complete ledger and maximum

For `a in Z/rZ`, the conductor ideal is

```text
1                                      if a=0, psi=1;
p O_F lambda^epsilon                   if a!=0, psi=1;
lambda^[j(r-1)+1]                      if a=0, ord(psi)=r^j;
p O_F lambda^[j(r-1)+1]                if a!=0, ord(psi)=r^j.
```

A character with a nontrivial Kummer component and a faithful cyclotomic
component attains both local maxima.  Therefore

```text
Q(E/F)
 = max_chi Norm_(F/Q)(f_chi)
 = p^(r-1) r^[m(r-1)+1].                         (2.2)
```

The Wieferich alternative changes the relative different, but not this
maximum conductor.

## 3. Exact discriminant control for odd `r`

The conductor--discriminant product, together with

```text
sum_(j=1)^m phi(r^j)(j(r-1)+1)=m r^m(r-1),
```

gives

```text
D_(E/F)
 = (p O_F)^[(r-1)r^m]
   lambda^[(r-1)(m r^(m+1)+epsilon)].             (3.1)
```

Consequently

```text
|D_E|
 = p^[(r-1)^2 r^m]
   r^[r^(m+1){r-2+m(r-1)}+(r-1)epsilon].          (3.2)
```

This exact value is the fair input for comparing the two unconditional
theorems; using only the looser Phase-2 majorant would overstate the gain.

## 4. The `r=2` branch

Here `F=Q` and

```text
E=Q(zeta_(2^(m+1)),sqrt(p)).
```

Let `eta` be the quadratic character of `Q(sqrt(p))`.  Its conductor is

```text
p       if p=1 mod 4,
4p      if p=3 mod 4.
```

At `p`, a character has conductor exponent one exactly when it contains
`eta`.  At `2`, a cyclotomic character has exponent in
`{0,2,3,...,m+1}`.  If `p=3 mod 4`, twisting by `eta` multiplies the local
character by the conductor-`4` character `chi_(-4)`:

- exponents above `2` are unchanged;
- exponent `0` and exponent `2` are interchanged;
- for `m=1`, the four global conductor norms are `1,4,4p,p` rather than
  `1,4,p,4p`.

For `m>=2`, a primitive character of conductor `2^(m+1)` remains primitive
under this conductor-`4` twist.  Thus, including the small case separately,

```text
Q(E/Q)=p 2^(m+1)                                  (4.1)
```

for every `m>=1`.  The exact discriminant is

```text
|D_E|=p^(2^m) 2^[m 2^(m+1)].                     (4.2)
```

## 5. Thorner--Zaman specialization

Apply Thorner--Zaman Theorem 1.1 with their `L=E`, ground field `Q`,
abelian subgroup `A=H`, and fixed field `K=F`.  Their theorem states

```text
P(C;E/Q)
 << D_F^694 Q(E/F)^521
    + D_F^232 Q(E/F)^367 [F:Q]^[290[F:Q]],        (5.1)
```

with an absolute effectively computable implied constant.  The selected
target conjugacy class meets `H`, so (5.1) supplies a rational prime in the
exact-order class.

For odd `r`, substitution of (2.2), `D_F=r^(r-2)`, and `[F:Q]=r-1` gives

```text
ell <<
 p^[521(r-1)] r^[694(r-2)+521(m(r-1)+1)]
 +
 p^[367(r-1)] r^[232(r-2)+367(m(r-1)+1)]
 (r-1)^[290(r-1)].                                (5.2)
```

For `r=2`,

```text
ell << (p 2^(m+1))^521+(p 2^(m+1))^367.          (5.3)
```

Both bounds are unconditional.  The symbol `<<` and the unpublished
numerical value of its absolute constant must be retained.

## 6. Honest comparison of bounds

Kadiri--Wong gives the completely numerical unconditional bound

```text
ell <= |D_E|^310.                                 (6.1)
```

For odd `r`, (3.2) makes its `p`-exponent
`310(r-1)^2 r^m`; the leading `p`-exponent in (5.2) is only `521(r-1)`.
The former is larger for every allowed odd `r,m`.  For `r=2`, the two
exponents are `310*2^m` and `521`, and the former is already `620` at
`m=1`.  The `r`- and `2`-exponents likewise favor (5.2)--(5.3).

It follows that for every fixed `r,m`, if `T_TZ(p,r,m)` denotes the displayed
two-term monomial,

```text
|D_E|^310 / T_TZ(p,r,m) -> infinity as p -> infinity.   (6.2)
```

Thus the Thorner--Zaman specialization is strictly stronger on a genuine
infinite unconditional parameter range, whatever its one fixed absolute
constant is.  Because the published theorem does not print that constant,
the proof does **not** justify a named cutoff such as `p>=p_0(r,m)` or a
claim that one particular small triple is numerically improved.

Under the exact ERH hypotheses, Bach--Sorenson gives

```text
ell <= (4 log|D_E|+2.5[E:Q]+5)^2.                (6.3)
```

This logarithmic-square/discriminant-degree bound is far smaller than the
unconditional polynomial (5.2)--(5.3).  Relative conductors do not improve
(6.3); the conditional statement must retain Bach--Sorenson.

## 7. Source ledger

| Source | Load-bearing use | Verification |
|---|---|---|
| Thorner--Zaman, *An explicit bound for the least prime ideal in the Chebotarev density theorem* | definition (1-6), Theorem 1.1, printed p. 1137 | **FULL PUBLISHER PDF VERIFIED** |
| Kadiri--Wong, *Primes in the Chebotarev density theorem for all number fields* | Theorem 1, printed p. 701, `N P<=D_L^310` | **FULL JOURNAL PDF VERIFIED IN PHASE 2** |
| Bach--Sorenson, *Explicit bounds for primes in residue classes* | Theorem 5.1, printed p. 1729 | **FULL AMS PDF VERIFIED IN PHASE 2** |
| conductor--discriminant formula and local ramification | derivations in Sections 2--4 | **SELF-CONTAINED SPECIALIZATION** |

Primary links:

- [Thorner--Zaman publisher PDF](https://msp.org/ant/2017/11-5/ant-v11-n5-p04-p.pdf),
  SHA-256 `504512d24db46f933d52f277d2ad3a14da5ed66e0efcda0407c8aceadd008d4c`;
- [Kadiri--Wong journal PDF](https://www-math.nsysu.edu.tw/~pjwong/stuff/leastprimeALL.pdf);
- [Bach--Sorenson official AMS PDF](https://www.ams.org/journals/mcom/1996-65-216/S0025-5718-96-00763-6/S0025-5718-96-00763-6.pdf).

## 8. Phase-3 verdict

```text
LOCAL_CONDUCTORS=PASS
Q_ODD=p^(r-1) r^[m(r-1)+1]
Q_R2=p 2^(m+1)
RELATIVE_DIFFERENT=PASS
TZ_SPECIALIZATION=PASS
UNCONDITIONAL_IMPROVEMENT_OVER_EXACT_D_E^310=PASS_EVENTUAL
EXPLICIT_NUMERICAL_THRESHOLD=UNRESOLVED_BY_PUBLISHED_CONSTANT
ERH_IMPROVEMENT=NO
STANDALONE_INCREMENT=FOCUSED_SHORT_NOTE
MANUSCRIPT_STAGE=AWAITING_RESEARCH_CHECKPOINT
ROUTE_ADVANCEMENT=NONE
```

This is a genuine unconditional structural improvement, but its honest paper
shape is a focused exact-density/conductor/least-witness note.  It should not
be marketed as a numerically explicit cutoff theorem or as an ERH
improvement.
