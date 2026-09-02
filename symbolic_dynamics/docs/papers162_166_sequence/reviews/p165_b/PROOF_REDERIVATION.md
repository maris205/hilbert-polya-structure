# P165 Review B — independent proof rederivation

**Object:** Round-1 low-weight support-shortening map  
**Review date:** 2026-09-03  
**Lifecycle:** `HOLD_EXTERNAL`

This derivation was made from the literal map and the Round-1 theorem
contract, without adopting the author proof or Review A's derivation.
Computation is used only as counterexample pressure.

## 1. Literal conventions

Let `C <= F_q^n` be a labelled linear subspace.  For nonzero `C`, define

```text
d(C) = min{wt(c): 0 != c in C},
L(C) = {c in C: 0 < wt(c) < 2d(C)},
U(C) = union_{c in L(C)} supp(c),
T(C) = {c in C: c|_{U(C)}=0}.
```

Set `T(0)=0`.  Coordinates are retained, so this is a self-map on the
subspace lattice of one fixed ambient space.  Put `C_i=T^i(C)`, and while
`C_i != 0`, put `d_i=d(C_i)` and `U_i=U(C_i)`.

## 2. Strict descent and distance growth

Choose a word `w` of weight `d(C)`.  Since

```text
0 < d(C) < 2d(C),
```

the word lies in `L(C)`, its support lies in `U(C)`, and it cannot belong to
`T(C)`.  Hence every nonzero step is a strict subspace inclusion.

Now suppose `T(C)` is nonzero.  If a nonzero survivor `x` had
`wt(x)<2d(C)`, then `x` would lie in `L(C)`.  Its support would therefore be
contained in `U(C)`, while survival requires it to be zero on `U(C)`, an
impossibility.  Thus

```text
d(T(C)) >= 2d(C).
```

This is a weak lower bound on the new distance, despite the strict cutoff in
the definition.  Equality is allowed.

## 3. Disjoint purge budget and sharp height

Every later code is a subcode of `C_{i+1}` and is zero on `U_i`; hence
`U_j` is disjoint from `U_i` whenever `j>i`.  A minimum word of `C_i` has
all `d_i` of its supported coordinates inside `U_i`, so

```text
|U_i| >= d_i >= 2^i d_0 >= 2^i.
```

If `tau(C)=r`, the codes `C_0,...,C_{r-1}` are nonzero and

```text
n >= sum_{i=0}^{r-1}|U_i| >= 1+2+...+2^{r-1}=2^r-1.
```

Therefore `r<=floor(log_2(n+1))`.  Strict descent also makes zero the only
periodic state.

For sharpness, let `r=floor(log_2(n+1))`, choose disjoint coordinate blocks
`B_i` of sizes `2^i`, and put on each block a one-dimensional line whose
nonzero vectors have full support.  The direct sum of these lines has, at
stage `i`, distance `2^i`.  The only nonzero words below `2^{i+1}` belong
to the line on `B_i`: a later line has weight at least the strict boundary,
and disjoint supports make mixed weights additive.  Thus precisely `B_i` is
purged and the depth is `r`.  Unused ambient coordinates cause no change.

## 4. Nonzero all-time image: necessity

Suppose `T^t(C)=D != 0`.  All states through time `t` are nonzero.  Repeated
distance growth gives

```text
d(D) >= 2^t d(C) >= 2^t.
```

Moreover, `D` is zero on every pairwise-disjoint purge set
`U_0,...,U_{t-1}`.  Hence, with `z(D)=n-|Supp(D)|`,

```text
z(D) >= sum_{i=0}^{t-1}|U_i| >= 2^t-1.
```

Both target conditions are independently necessary: a large target distance
does not create missing zero coordinates, and abundant zero coordinates do
not repair a small distance.

## 5. Nonzero all-time image: sufficiency

Assume `d(D)>=2^t` and `z(D)>=2^t-1`.  In the zero-coordinate set of `D`,
choose disjoint blocks

```text
B_i, |B_i|=2^i, 0<=i<t,
```

and a full-support line `M_i` on each.  Define

```text
C = D direct_sum M_0 direct_sum ... direct_sum M_{t-1}.
```

At stage `i`, the current code is
`D direct_sum M_i direct_sum ... direct_sum M_{t-1}` and has distance
`2^i`.  Any nonzero word outside `M_i` has weight at least `2^{i+1}`:
this holds for later line components, for a nonzero target component, and
for every mixed word because the supports are disjoint.  The strict cutoff
therefore selects exactly the nonzero words of `M_i`, so `U_i=B_i` and that
line alone disappears.  After `t` steps the state is `D`.

Consequently, for every nonzero target,

```text
D in im(T^t) iff d(D)>=2^t and z(D)>=2^t-1.
```

## 6. Dimension and new-support lower bounds

If `T^t(C)=D != 0`, the `t` strict inclusions from `C` to `D` have total
codimension at least `t`.  Also each `U_i` is supported by `C`, is zero in
`D`, and the `U_i` are disjoint.  Thus

```text
dim(C)-dim(D) >= t,
|Supp(C)\Supp(D)| >= sum_i |U_i| >= 2^t-1.
```

These are separate lower bounds; the paper claims a classification only for
sources attaining both simultaneously, not either one separately and not
the whole fibre.

## 7. Rigidity under simultaneous equality

Assume both bounds are equalities.  Since each transition has positive
codimension and their sum is `t`, every transition has codimension one.
Since each `|U_i|>=d_i>=2^i` and the total new support is `2^t-1`, all
inequalities are equalities:

```text
|U_i|=d_i=2^i.
```

Choose a minimum word `w_i in C_i`.  Its support lies in `U_i` and has the
same cardinality, so `supp(w_i)=U_i`.  In particular, this is an actual word
supported only on the purge block; no choice of a quotient lift is being
silently made.  Since

```text
C_{i+1}=ker(C_i -> F_q^{U_i})
```

has codimension one and `w_i` is not in that kernel,

```text
C_i=C_{i+1} direct_sum span(w_i).
```

Descending from time `t-1` to zero gives exactly

```text
C=D direct_sum M_0 direct_sum ... direct_sum M_{t-1},
```

where the `M_i` are full-support lines on pairwise-disjoint blocks of sizes
`2^i` outside `Supp(D)`.  Section 5 proves the converse, so this is an iff
classification.  It also rules out a hidden cancellation or extension
class over nonbinary fields.

## 8. Exact count over every prime-power field

The block sizes are assigned to times, so the blocks are ordered by their
distinct dyadic sizes.  Selecting them from the `z=z(D)` labelled zero
coordinates gives

```text
z! / ((z-(2^t-1))! product_{i=0}^{t-1}(2^i)!).
```

On a labelled block of size `m`, there are `(q-1)^m` full-support vectors.
Each one-dimensional line has `q-1` nonzero representatives, hence the
number of full-support lines is `(q-1)^{m-1}`.  Multiplying across the `t`
blocks gives exponent

```text
sum_i(2^i-1)=(2^t-1)-t.
```

The simultaneous-extremizer count is therefore

```text
z(D)! / ((z(D)-(2^t-1))! product_i(2^i)!)
    * (q-1)^{2^t-1-t}.
```

Nothing in this argument assumes that `q` is prime.  The reviewer verifier
uses a native `GF(4)=GF(2)[a]/(a^2+a+1)` implementation and checks the
formula literally.

## 9. Mandatory boundary audit

- **`D=0`.** Zero is in every time image using itself.  Its full fibre is
  `{C:tau(C)<=t}`, not the displayed nonzero-target extremal formula.  On
  the exact-depth-`t` slice, the same proof gives minimum dimension `t`,
  minimum support `2^t-1`, and the same dyadic-line minimizers with `n` in
  place of `z(D)`.
- **`t=0`.** `T^0` is the identity.  Every nonzero `D` meets the conditions
  `d(D)>=1` and `z(D)>=0`; both lower bounds are zero; the empty block/line
  product gives exactly the single source `D`.
- **`n=0`.** The only state is zero, its depth is zero, and
  `floor(log_2(1))=0`.
- **Full-support target.** If `D!=0` has `z(D)=0`, the target has no
  positive-time source, independently of how large `d(D)` is.
- **Post-cap time.** If `2^t-1>n`, no nonzero target has enough zero
  coordinates.  Zero still belongs to the image.
- **Strict `<2d`.** For the direct sum of full-support lines of sizes one
  and two, the strict map retains the second line after one step; replacing
  `<` by `<=` purges it immediately.  The theorem belongs to the strict map.
- **Labelled coordinates.** Blocks are selected from labelled zero
  coordinates; no monomial-equivalence quotient or automorphism divisor is
  present.

## 10. Result

No counterexample or proof gap was found.  The principal theorem and every
stated boundary survive the independent derivation.  The direct one-step
distance-increasing shortening mechanism remains mandatory zero-credit
background; the residual begins with its autonomous recomputation and the
all-time/inverse conclusions.
