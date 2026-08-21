# Independent proof re-audit

## Scope and method

This is a proof reconstructed from the frozen definitions, not a summary of
the builder's verdict.  The audited object has arity `d>=2`, a positive phase
vector `a=(a_0,...,a_(p-1))`, complete cyclic blocks
`V_j -> V_(j+1 mod p)`, and only the expressly defined transient feeders.
Write `c_j=log a_j` and

```text
|Delta_n|=(d^(n+1)-1)/(d-1),
H_j(c)=(d-1)/(d^p-1) sum_(t=0)^(p-1) d^(p-1-t)c_(j-t).
```

Cross-audit computation is supportive only.  The deductions below carry the
claims for all parameters in the contract.

## C0: cylinder lemma and Frostman bound

Under the frozen metric, two distinct trees that agree on `Delta_n` but not
on `Delta_(n+1)` have distance `exp(-|Delta_n|)`.  Consequently, for

```text
exp(-|Delta_n|) <= r < exp(-|Delta_(n-1)|),
```

a closed `r`-ball meeting the stratum is exactly one depth-`n` cylinder
intersected with that stratum.  This includes the left endpoint; it is the
off-by-one convention used below.

Let `L=liminf log(P_n)/|Delta_n|`.  If `s>L`, choose a subsequence with
`log P_n <= (s-epsilon)|Delta_n|`.  The `P_n` depth cylinders cover the
stratum and have diameter at most `exp(-|Delta_n|)`, so their total
`s`-cost tends to zero.

If `0<=s<L`, then eventually `P_n>=exp(s|Delta_n|)`.  For a ball at the
above scale, equiprobability gives

```text
mu(B) <= P_n^(-1) <= exp(-s|Delta_n|) <= r^s.
```

The last inequality has the correct direction because
`r>=exp(-|Delta_n|)`.  Finitely many large scales are absorbed into a
constant.  The mass-distribution principle yields `dim_H>=s`; taking
`s` upward to `L` proves equality.  A ball centered outside the stratum but
meeting it has the same cylinder intersection as a ball centered at one of
its points, so no center convention changes the argument.  For every frozen
stratum, independent uniform choices within the forced phase give compatible
finite marginals of mass `1/P_n`; no measure existence is being assumed for
an unfrozen model.

## C1: complete cyclic core

With root phase `h`, level `ell` is forced to phase `h+ell` and has `d^ell`
vertices.  Completeness makes all labels within that phase independent, so

```text
P_(n,h)=product_(ell=0)^n a_(h+ell)^(d^ell).
```

For any periodic vector `x`, reverse the weighted sum by `u=n-ell`.  Along
`n=r mod p`,

```text
sum_(ell=0)^n d^ell x_(h+ell) / |Delta_n|
 -> (d-1)/d sum_(u>=0) d^(-u)x_(h+r-u).
```

Writing `u=t+kp` gives the coefficient

```text
(d-1)/d * d^(-t)/(1-d^(-p))
=(d-1)d^(p-1-t)/(d^p-1),
```

and hence the limit `H_(h+r)(x)`.  This checks both index direction and the
`p-1-t` exponent.  C0 makes the dimension of a root-phase stratum the
minimum of its `p` residue limits.  Changing `h` cyclically permutes that
list, and the whole core is a finite union of root-phase strata.  Therefore

```text
dim_H T_C(a)=min_j H_j(c).
```

The argument includes `p=1`, phase sizes equal to one, and zero dimension.

## C2: one transient level and finite unions

Fix the ordered phases of the `d` children of `r`, and let their multiplicity
vector be `m`.  At core-relative level `ell`, phase `s+ell` occurs
`m_s d^ell` times.  Thus, for total depth `n>=1`,

```text
P_(n,m)=product_s product_(ell=0)^(n-1)
        a_(s+ell)^(m_s d^ell).
```

With `b_k=d^(-1)sum_s m_s c_(s+k)`, its logarithm is
`d sum_(ell=0)^(n-1)d^ell b_ell`.  Since

```text
d|Delta_(n-1)|/|Delta_n| -> 1,
```

the residue limits are `H_j(b)`, equivalently
`d^(-1)sum_s m_s H_(s+j)(c)`.  C0 gives `D_1(m;c)`.

There are only `p^d` ordered phase assignments, so the root-`r` set is a
finite union and its dimension is the largest `D_1`.  Adding the finitely
many core-root strata cannot enlarge this maximum: the composition
concentrated in any one phase reproduces the core minimum.  A declared
finite allowed composition set is handled by the same finite-union
argument.  This reasoning uses both complete core blocks and strict
transience; it does not survive a return edge or an undeclared feeder target.

## C3--C4: mean, constant convolution, and Fourier condition

Every row of the circular operator `H` has weights summing to one, and cyclic
reindexing proves

```text
(1/p)sum_j H_j(x)=(1/p)sum_j x_j.
```

On a `p`th root of unity `z`, the unnormalized kernel multiplier is

```text
sum_(t=0)^(p-1)d^(p-1-t)z^t
=(d^p-z^p)/(d-z)=(d^p-1)/(d-z),
```

which never vanishes for `d>=2`.  Hence `H(x)` is constant exactly when
`x` is constant.

The residue vector for `m` has mean `bar(c)`, so its minimum is at most that
mean.  Equality of minimum and mean holds exactly when every residue equals
the mean, hence exactly when

```text
sum_s m_s c_(s+k)
```

is independent of `k`.  Exponentiation turns this into equality of the
shifted integer products.  This proves the unconditional constant-circular-
convolution criterion.

If `p|d`, the uniform composition `m_s=d/p` is integral and constant, proving
universal sufficiency.  For necessity under the stated extra hypothesis,
the nonzero Fourier modes of the convolution are, up to the harmless index
reversal, `hat(m)(-q)hat(c)(q)/d`.  If every nonzero mode of `c` is nonzero,
constancy forces every nonzero mode of `m` to vanish.  Fourier inversion then
makes `m` uniform, which is integral exactly when `p|d`.  The hypothesis is
essential: for `p=4,d=2,a=(2,3,2,3),m=(1,1,0,0)`, all shifted products are
`6` although `4` does not divide `2`.

## C5: two phases

For `p=2`, direct substitution gives

```text
H_0=(d c_0+c_1)/(d+1),
H_1=(d c_1+c_0)/(d+1).
```

Their mean is `mu`, and their difference has magnitude
`(d-1)Delta/(d+1)`, giving the component penalty
`(d-1)Delta/(2(d+1))`.  For `m=(k,d-k)`, the two entries of `b` differ by
`(2k-d)(c_0-c_1)/d`, so the same calculation gives

```text
D_1=mu-(d-1)|2k-d|Delta/(2d(d+1)).
```

The least value of `|2k-d|` is zero for even `d` and one for odd `d`.
When `Delta=0`, every composition saturates; when `Delta>0`, the optimum
strictly improves on the component and saturates exactly in the even case.

## C6: `L` transient levels

For a fixed assignment of the `N=d^L` core roots at level `L`, the forced
transient levels contribute no choices, and

```text
P_(n,L,m)=product_s product_(ell=0)^(n-L)
           a_(s+ell)^(m_s d^ell).
```

Because `|Delta_(n-L)|/|Delta_n| -> d^(-L)`, C0 and the periodic limit give

```text
D_L(m;c)=min_j N^(-1)sum_s m_s H_(s+j)(c).
```

There are finitely many phase assignments at level `L`.  A root at a later
transient state has a `K<L` optimizer.  If `m` is a composition of `d^K`,
then `dm` is a composition of `d^(K+1)` and has exactly the same residue
vector.  Thus `D_(K+1)^*>=D_K^*`; the top transient stratum dominates all
later transient and core strata.

The mean/constant-convolution proof applies with denominator `N`.  For
convergence, take a balanced composition and write
`m_s=N/p+e_s`, where `sum e_s=0` and `|e_s|<1`.  Since all `H_j(c)>=0`,

```text
|N^(-1)sum_s e_s H_(s+j)(c)|
 <= p max_j H_j(c)/N.
```

The residue mean is `bar(c)`, so the optimized minimum is at most the mean
and at least the balanced minimum.  This yields the stated two-sided error,
monotonicity, and convergence.  Exact saturation at finite `L` remains the
constant-convolution condition; `p|d^L` is sufficient, with necessity only
under the full Fourier-support hypothesis.

## C7: four states

For the displayed matrix, the essential core is the complete two-cycle with
phase sizes `(1,2)`.  C5 gives `log(2)/3`.  The transient row admits one child
in each phase, so the composition `(1,1)` has constant convolution and
dimension `bar(c)=log(2)/2`.  The universal mean bound rules out anything
larger.  Therefore the full four-state shift has dimension `log(2)/2`,
strictly above its cyclic essential SCC.

## Proof conclusion

All C0--C7 quantifiers are supported under the frozen hypotheses.  In
particular, the proof does not extend to incomplete cyclic blocks, feeder
return edges, arbitrary reducible graphs, or unconditional divisibility
necessity.
