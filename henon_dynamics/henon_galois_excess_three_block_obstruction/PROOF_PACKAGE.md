# Proof package

## Theorem 1: cycle-incidence criterion

If `N_r(gamma)` denotes cyclic `r`-block incidence, then a width-`r`
potential `v` has orbit sum

```text
S_gamma(v) = <v, N_r(gamma)>.
```

Hence every integer incidence relation forces the same relation among orbit
sums.  On a finite cycle list, annihilating every row relation is also
sufficient by linear-functional extension.

## Theorem 2: exact three-block no-go

With states `0=--, 1=-+, 2=+-, 3=++`, use

```text
gamma_3  = (0,2,1)
gamma_4a = (0,0,2,1)
gamma_4b = (0,2,3,1)
gamma_5  = (0,0,2,3,1).
```

Their triple multisets give

```text
N_3(gamma_3)+N_3(gamma_5)
=N_3(gamma_4a)+N_3(gamma_4b).
```

Exact algebra gives

```text
E_4b = 0,
E_3  = acosh(21*sqrt(5)-19) > 0,
E_4a = acosh(287-96*sqrt(6)),
E_5  > acosh(195) > E_4a.
```

Therefore `E_3+E_5>E_4a+E_4b`, contradicting the forced identity.  Any local
realization must use at least four consecutive states.

## Exact period-five ledger

The orbit has coordinates `(a,b,c,c,b)` with

```text
b = 1/2 - 3*a^2,
c = -54*a^4 + 18*a^2 - a - 1/2.
```

Its coordinate polynomial is

```text
5832*a^6 - 1944*a^5 - 2268*a^4 + 648*a^3
+ 144*a^2 - 12*a - 1.
```

Eliminating `a` gives the degree-six trace polynomial stored in the
certificate.  Its roots lie one each in

```text
(-7607,-7606), (-711,-710), (-590,-589),
(390,391), (770,771), (4445,4446).
```

The coordinate interval contains exactly one root.  The derivatives of
`b(a)`, `c(a)`, and the reduced trace have no roots there and have midpoint
signs `(+,+,-)`, so the physical symbolic word is `--,--,+-,++,-+` and its
trace decreases strictly into the last trace interval.  The degree-twelve multiplier polynomial is
`z^6 Q_5(z+z^{-1})`, monic, reciprocal and irreducible.

## Theorem 3: quantitative Hölder gate

On the one-sided H6 presentation, if an alpha-Hölder potential realizes all
excesses and

```text
sum_i c_i N_m(gamma_i) = 0,
```

then cylinder approximation gives

```text
|sum_i c_i E_gamma_i|
<= C theta^(alpha*m) sum_i |c_i| |gamma_i|.
```

A one-sided Hölder no-go therefore requires a sequence with increasing `m`
whose normalized discrepancy violates every exponential rate.  This does
not promote to arbitrary two-sided Hölder data without an additional
future-dependent cohomological reduction.

## Finite-data firewall

Every finite family of distinct periodic orbits and arbitrary assigned totals
admits a locally constant interpolation: choose disjoint long cylinders around
one point on each orbit and sum their indicators with the desired weights.
Thus no finite table alone can refute a general Hölder observable.
