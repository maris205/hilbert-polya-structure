# Hostile review — P86

Audit date: 2026-08-28 UTC

Disposition after revision: **GO for internal short-paper release**

## Bottom line

No core formula blocker remains.  The fiber matrices, forbidden support,
complexity cubic, one-dependence, infinite Markov order, age law, entropy-rate
series, and strict entropy gap all survive independent derivation.  The
original draft had one genuine low-index proof gap in the complexity
recurrence, one under-explained complete-past conditioning step, and several
minor source/control/rounding issues.  All were corrected before the final
build.

## Formula audit

### 1. Cylinder fibers and support — PASS

For a partial lift with endpoint-type counts `(z,r)`, observing zero sends it
to `(z+r,mz)`, while observing a fixed nonzero symbol sends it to `(0,r)`.
This is exactly right multiplication by the displayed matrices `C_0,C_a`.
The initial counts `(1,m)` and terminal sum `(1,1)^T` therefore give every
fiber exactly.

A nonzero--zero--nonzero observed triple is impossible because the middle
hidden vertex forced nonzero by the first edge forces the next hidden vertex
to zero.  Conversely, zero gaps in a legal word have length at least two, so
successive nonzero edge intervals can be divided through independently and
joined with zero hidden endpoints.  This proves the exact image/support
description.  Two inserted zeros bridge arbitrary legal words, proving
mixing.

### 2. Complexity recurrence — PASS after correction

The weighted pair-state matrix and

```text
det(tI-A_q)=t(t^3-qt^2+(q-1)t-(q-1))
```

are correct.  The original proof attributed the cubic recurrence from
`n>=2` directly to Cayley--Hamilton, but the extra factor `t` only gives that
step automatically for `n>=3`.  The manuscript now closes the gap by direct
inclusion--exclusion:

```text
L_3=q^3-m^2,
L_4=q^4-2qm^2,
L_5=q^5-3q^2m^2+m^3.
```

Adjacent forbidden occurrences are incompatible; at length five only the
first and third positions overlap, in `m^3` words.  These values verify the
remaining recurrence cases `n=0,1,2`.

### 3. Genuine context conditional — PASS after clarification

Let an arbitrary compatible earlier word `v` leave row vector
`(1,m)C_v=(z,c)`.  Reading any `a!=0` gives

```text
(z,c)C_a=(0,c).
```

After `r` zeros,

```text
(0,c)C_0^r=c(F_r,mF_{r-1}).
```

The scalar `c`, which contains every dependence on the earlier past, cancels
from the next-symbol ratio.  Hence, for every earlier finite past and then by
martingale convergence for the complete past,

```text
P(Y_0=b | v a 0^r)=mF_{r-1}/(qF_{r+1}),  b!=0, r>=1.
```

The draft's formula was correct but this cancellation was not explicit.  It
is now stated in the context proof and again at the complete-past entropy
step.  The abstract now also records the necessary range `r>=1`.

The decreasing Möbius recurrence
`t_{r+1}=m/(1+t_r)` has fixed point
`(sqrt(4q-3)-1)/2`; injectivity prevents a finite iterate from reaching it.
Thus consecutive prediction values are strictly unequal, and contexts with
the same arbitrarily long zero suffix rule out every finite Markov order.

### 4. Age law and entropy series — PASS

The event `R=r` is the disjoint union over `a!=0` of cylinders `a0^r`.
For fixed `a`, its fiber count is `mF_{r+1}`, so

```text
w_r=P(R=r)=m^2 F_{r+1}/q^(r+2).
```

The generating function
`sum F_j z^j=z/(1-z-mz^2)` normalizes these weights because
`q^2-q-m=(q-1)^2=m^2`.

Given age `r`, the posterior nonzero probability of `U_0` is `alpha_r`; the
independent uniform `U_1` then gives one zero mass `1-s_r` and `m` equal
nonzero masses `s_r/m`.  Its entropy is exactly
`h_b(s_r)+s_r log m`.  Averaging over the age law proves the series.  The
positive root of `x^2=x+m` is below `q`, so the weights and series converge
exponentially.

### 5. Strict entropy gap — PASS

The support is a mixing SFT, so its maximal-entropy measure is unique.  In
the ordered-pair presentation the Parry measure is one-step Markov and hence
has original-symbol Markov order at most two.  The adjacent-product measure
has no finite Markov order, so it is not the Parry measure.  Uniqueness then
gives the strict gap.  This argument is structural; the displayed decimals
are not being used as a proof.

## Nonprime-field and independent controls

The `q=4` implementation is the field
`F_2[x]/(x^2+x+1)`, with `x^2=x+1`, not the ring modulo four.  Its nonzero
elements form the expected order-three multiplicative group, and every proof
uses only bijectivity of multiplication by a nonzero element.

- Package control: PASS over `F_2,F_3,F_4,F_5`.
- Exhaustive discrete scope: 24 block lengths, 14,676 hidden words, 4,258
  candidate observed words.
- Revised label coverage: 199 exact `(a,b,r)` context checks, including 63
  over `F_4`.
- Separate `F_4` implementation: 765 conditionals with arbitrary compatible
  earlier pasts all matched the formula; the age law passed for `r=0,...,5`.
- Independent finite-past conditional entropies for `F_4`, past lengths one
  through five, were
  `1.209007376298, 1.139649626196, 1.135404614435,
  1.134280524399, 1.134116079531`, decreasing toward the series value
  `1.134074691264723`.

The entropy sums and Perron roots in the script are floating-point
diagnostics, despite the script's historical `ALL EXACT CONTROLS PASSED`
banner.  Exactness applies to the discrete identities; the entropy formula
and gap are proved symbolically.  The table's three one-unit last-decimal
rounding discrepancies were corrected against high-precision roots.

## Ownership audit

- Aaronson--Gilat--Keane--de Valk now receive positive ownership for the
  general one-dependent/block-factor landscape (DOI
  `10.1214/aop/1176991499`).
- Blackwell owns the entropy problem for functions of finite-state Markov
  chains; Rissanen and Buehlmann--Wyner own the context/variable-memory line;
  Parry owns the intrinsic Markov measure used in the gap proof.
- The text now describes the process as a hidden Markov process with an
  almost-surely finite but unbounded context tree and avoids asserting
  membership in a finite-context VLMC subclass.
- Bounded searches using the exact formula and combinations of `adjacent
  product`, `finite field`, `one-dependent`, and `hidden Markov` found no
  direct primary owner for this combined exact package.  This remains a
  dated collision firewall, not an absolute priority claim.

## Final release audit

- Four-stage `pdflatex / bibtex / pdflatex / pdflatex`: PASS.
- PDF: **7 A4 pages**, **318,027 bytes**, PDF 1.5.
- Undefined references/citations: **0/0**.
- LaTeX/package warnings and overfull/underfull boxes: **0**.
- Bibliography: **5 cited keys / 5 entries**.
- Fonts: **23/23 embedded, subsetted, and Unicode-mapped**.
- All seven rendered pages visually inspected; no clipping or collisions.
- SHA-256: `d6444b5f31e2a1f77155280b28bc2b0e857cb9ead34dde1645683f8cba77798e`.
