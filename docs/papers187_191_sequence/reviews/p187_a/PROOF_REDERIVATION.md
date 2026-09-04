# P187 proof rederivation and counterexample audit

## 1. Arithmetic reduction and carrier closure

For `p^a || N`, write `e_i=nu_p(x_i)`.  Because

```text
nu_p(x_i/gcd(x_i,x_(i+1))) = e_i-min(e_i,e_(i+1))
                            = (e_i-e_(i+1))_+,
```

the divisor carrier is closed and the full map is the direct product of the
prime-height maps `D_a`.  No dependence between primes is hidden in either
the forward orbit or a labelled inverse.  If `N=1`, the index set of primes
is empty and both products are one, as required by the singleton carrier.

## 2. Frozen peaks, collars, and the all-time clock

Let `h=max e`, `z=D_a(e)`, and suppose `z_i=h`.  Equality in
`(e_i-e_(i+1))_+ <= h` forces `(e_i,e_(i+1))=(h,0)`.  Consequently

```text
z_(i-1)=(e_(i-1)-h)_+=0,
z_(i+1)=(0-e_(i+2))_+=0.
```

This remains true on `m=1` and `m=2` under their actual cyclic indexing; the
lemma's nontrivial decomposition is used for the longer cycles.  Let `S` be
the set of such output peaks, put `f_i=h` on `S` and zero elsewhere, and
write `z=f+w`.  The zero collars make `w` vanish on `S` and on both
neighbours of every `S`-site.  Checking an edge by whether neither, its left,
or its right endpoint lies in a peak collar yields

```text
D_a(f+w)=f+D_a(w).
```

The same collar zeros persist in `D_a(w)`, so induction on time yields
`D_a^r(z)=f+D_a^r(w)` for every `r>=0`.  Overlapping collars from peaks at
cyclic distance two cause no exception: their common site is already zero.
All nonpeak values of `z` are at most `h-1`.  Induction on `h` therefore
fixes the residual within `h-1` more steps and fixes every height-`h` source
within `h` steps.

For `m>=3`, the word `(0,...,0,h,1)` evolves by lowering the `h` entry once
per step until the final `1` is isolated, so its tail is exactly `h`.  At
`m=1`, every exponent maps to zero in one step.  At `m=2`, `(u,v)` maps to
`((u-v)_+,(v-u)_+)`, already fixed.  Nonconstant pairs attain tail one when
`a>0`.  Taking the maximum of the primewise tails gives exactly the stated
piecewise height, including `N=1`.

No counterexample was found in the 82,200 reviewer exponent states.  More
importantly, the collar identity supplies the missing uniform step; the
finite boxes are not used to extrapolate it.

## 3. Fixed supports and the weighted cyclic polynomial

The equality `(e_i-e_(i+1))_+=e_i` is automatic for `e_i=0`, and for
`e_i>0` is equivalent to `e_(i+1)=0`.  Thus a fixed prime plane is a cyclic
independent support, with `a` choices of positive height per occupied site.
This proves `I_m(a)` directly.  The reviewer separately enumerated cyclic
supports and checked:

- self-neighbouring `m=1`: only the empty support, hence `I_1=1`;
- `m=2`: the empty support and either singleton, hence `I_2=1+2a`;
- `m>=2`: coefficient of `a^k` equal to
  `m/(m-k) * binom(m-k,k)`;
- `m>=3`: `I_m=I_(m-1)+a I_(m-2)`.

Independent prime supports multiply, so the fixed divisor census and the
absence of nonfixed recurrence follow from the already established global
stabilization.

## 4. Oriented cyclic fibres and matrix direction

Fix one prime and a target height word `b`.  A source is precisely a closed
oriented walk

```text
u_0 -> u_1 -> ... -> u_(m-1) -> u_0
```

whose edge at position `i` obeys `(u_i-u_(i+1))_+=b_i`.  Therefore rows of
`L_b` are current heights and columns are next heights.  Multiplying in the
displayed target order and closing by a trace counts exactly these walks.
The reviewer first counted the oriented walks without matrix multiplication,
then compared every result with the trace.  The test also exhibits
`L_0 L_1 != L_1 L_0` at `a=1`, so the product order is not being excused by
a false commutativity assumption.

For any fixed edge `(u,v)`, exactly one `b` satisfies the constraint.  Thus
the entrywise sum of all `L_b` is `J`, not an upper- or lower-triangular
matrix.  Summing independently over each target coordinate gives
`tr(J^m)=(a+1)^m`; multiplying prime planes gives `|Div(N)|^m`.  The reviewer
checked every target in every exponent box and in composite boxes on
`N=1,8,12,20,72`.

The dangerous short cases reduce as follows:

- `m=1`: closure forces `(u-u)_+=0`, so only the all-one divisor target is in
  the image and its fibre is `|Div(N)|`.
- `m=2`: the two positive-part differences cannot both be positive.  Fibres
  are `a+1` at `(0,0)`, `a-b+1` at `(b,0)` or `(0,b)`, and zero otherwise,
  prime by prime.
- An all-zero prime target forces a weak cyclic chain and hence a constant
  prime exponent.  A target positive in every coordinate would force a
  strict cyclic chain and is empty.

## 5. Counterexample pressure and disposition

The fresh control uses packed base-`q` state generation and closed edge-walk
lifting; it imports no author code.  Its 1,444,819 assertions reopen frozen
peaks, cyclic collars, exact tails, fixed supports, polynomial conventions,
matrix direction, every labelled target, composite multiplicativity, and
mass conservation.

| severity | count | rationale |
|---|---:|---|
| Critical | 0 | no false theorem, invalid quantifier, or broken boundary |
| Major | 0 | no missing proof step or materially unsupported claim |
| Minor | 0 | no correction needed for notation, wording, or reproducibility |

Verdict: `PROVABLE AS STATED`.  Finite passage is not a proof, source search,
or novelty certificate.
