# IR1: all-parameter integral periodicity — proof and finite-core contract

2026-09-07. Draft theorem proof for independent review. The analytic
reduction below is complete; the finite-core output is now preserved in
`IR1_CORE_SUMMARY.json` and `IR1_CORE_CYCLES.jsonl`.
This document does not claim admission, a C-number, or literature priority.
All points and parameters are integers. The time is one application of
`T_a(x,y,z)=(y,z,yz+a-x)`; no induced clock replaces it.

## 1. Scalar encoding and a parameter-free identity

A periodic point is equivalent to a bi-infinite periodic scalar sequence
with `x_(i+3)=x_(i+1)x_(i+2)+a-x_i`. Write
`d_i=x_(i+2)-x_i` and `D=max |d_i|`. Subtracting the two adjacent
recurrences gives

`d_(i+1)+d_(i-1)=(x_(i+1)+1)d_i`.                         (1)

Consequently `|(x_(i+1)+1)d_i|<=2D`. Two adjacent zero differences
force every difference to vanish, by (1) in both directions.
Reversing a scalar sequence preserves its recurrence and its parameter;
on triples this is the actual reversing involution `(x,y,z)->(z,y,x)`.

If `D=0`, the sequence alternates `u,v` and exactly the equation

`a=u+v-uv=1-(u-1)(v-1)`                                (2)

is required. Its least period is one for `u=v`, otherwise two.
Thus this entire unbounded case is already explicit for every parameter.

## 2. Height versus difference: the four-step channel

Suppose `D>0` and `|x_1+1|>3D`. By integrality in (1), `d_0=0`.
Put `x_0=x_2=b`, `x_1=m`, and `e=d_1=-d_(-1)`.
Then `e!=0`, `|e|<=D`, `x_(-1)=m+e`, `x_3=m+e`.
Both `|x_(-1)+1|` and `|x_3+1|` exceed `2D`, so integrality
forces `d_(-2)=d_2=0`. Applying (1) at `i=1` gives
`(b+1)e=0`, hence `b=-1`. The scalar recurrence now gives exactly

`(-1,t,-1,a+1-t)` repeated.                            (F4)

Conversely this word satisfies the recurrence. Therefore every cycle
not of type F4 obeys `|x_i+1|<=3D` at every phase. The F4 word has
least period four unless `2t=a+1`; in the latter case it has period two,
or period one when also `t=-1` (thus `a=-3`).

## 3. Exhaustion of large differences

Assume `D>100`. Select an extremal difference, reversing if necessary,
so `d_0=D>0`. Put `(x_0,x_1,x_2)=(u,s,v)` with `v-u=D`.
Equation (1) shows `s in {-3,-2,-1,0,1}`. Set

`p=d_(-1)=v-su+s-a`, `q=d_1=sv+a-u-s`.

Then `p+q=(s+1)D`, with `|p|,|q|<=D`.
All deductions below use necessary consequences of the global maximum
`D`; violating one excludes periodicity, not merely one finite sample.

### 3.1 End centers s=1 and s=-3

For `s=1`, `p=q=D`. Equation (1) gives `d_(-2)=uD`
and `d_2=vD`, hence `u,v in [-1,1]` and `D<=2`, impossible.
For `s=-3`, `p=q=-D`, giving `d_(-2)=-(u+2)D`
and `d_2=-(v+2)D`. Thus `u,v in [-3,-1]` and again `D<=2`.

### 3.2 Center s=-1

Let `E=u+v-a-1`, so `p=E`, `q=-E`. Equation (1) gives

`d_(-2)=(u+1)E-D`, `d_2=-(v+1)E-D`.

Their bounds imply `(u+1)E>=0` and `(v+1)E<=0`.
Since `u<v`, `E>0` is impossible. If `E=0`, the word is F4.
Otherwise put `E=-k`, where `k` is a positive integer. Then
`u<=-1<=v`, `k(-u-1)<=2D`, `k(v+1)<=2D`, so `k<=4`.
Both `x_(-1)` and `x_3` equal `k-1`. Another application of (1)
gives `d_(-3)+d_3=k(k-2)D`. Since its absolute value is at most
`2D`, the possibilities `k=3,4` are excluded. Only `k=1,2` remain.

For `k=1`, `a=u+v`, `x_(-1)=x_3=0`, and
`d_(-3)=-v`, `d_3=u`, with both corresponding centers `a+1`.
Thus `|a+2|max(|u|,|v|)<=2D`. As the maximum is at least `D/2`,
`-6<=a<=2`. The forward word begins

`u,-1,v,0,a+1,u,(a+1)u+a,(a+1)u^2+au-1`.

In particular `d_5=(a+1)u^2+(a-1)u-1`. If `a!=-1`,
write `U=|u|`; here `u=(a-D)/2<0`, `U>49`, and `D<=2U+6`.
Then `|d_5|>=U^2-7U-1>2U+6>=D`, a contradiction.
For `a=-1`, the word is exactly

`(u,-1,-1-u,0,0)` repeated.                            (F5)

For `k=2`, `a=u+v+1`, `d_(-3)=-2a`, `d_3=2a`, and their
centers are `u+a+1`, `v+a+1`. Since these differ by `D`, their
bounds imply `|a|<=2` (also valid when `a=0`). The forward word begins

`u,-1,v,1,v+a+1,2a+1,(v+a+1)(2a+1)+a-1`.

Thus `d_4=2a(v+a+1)+a-1`, while `D=2v-a+1` and `v>48`.
For `a=1`, `d_4=D+4`; for `a=2`, `d_4=4v+13>D`;
for `a=-2`, `|d_4|=4v-1>D=2v+3`. Those cases are impossible.
For `a=-1`, direct iteration gives

`(-1,t,1,t,-1,-t-2,1,-t-2)` repeated.                  (F8)

For `a=0`, the surviving triple is `(u,-1,-1-u)`; direct iteration
gives the already classified unforced twelve-step family

`(1,m,1,m-1,-1,-m,1,1-m,1,-m,-1,m-1)` repeated.        (F12)

For the present large-D phase take `m=v+1>0` and rotate this word.
The full unforced classification belongs to C413 and is not claimed new.

### 3.3 Centers s=0 and s=-2: orientation convention

For either center, at least one of `|p|,|q|` is at least `D/2`.
Reverse the scalar word if needed to arrange `|p|>=D/2`.
After that reversal put `d_0=epsilon L`, where `L=D>100`
and `epsilon in {1,-1}`; it is not legitimate to assume the sign
remains positive. Write `v=u+epsilon L`.
The bound at `p` gives `|u+1|<=4`, thus `-5<=u<=3`.
The bound at `q`, using `|v+1|>=L-6`, gives `|q|<3`.

### 3.4 Center s=0

Here `p+q=epsilon L`, so `p,q` both have sign `epsilon` or are
zero. Write `q=epsilon r`, with `r in {0,1,2}`. Then
`a=u+epsilon r`, `x_3=epsilon r`, and

`d_2=(v+1)epsilon r-epsilon L`.

If `epsilon=-1` and `r>=1`, this equals
`(r+1)L-r(u+1)>L`, impossible. If `epsilon=1,r=2`, it equals
`L+2u+2>=L-8`; its center is `x_3=2`, so (1) would require
`3(L-8)<=2L`, impossible. For `epsilon=1,r=1`, put `a=u+1`.
Then `-4<=a<=4`, `d_2=a`, `d_3=2a-1`, and the latter center
is `x_4=L+2a-1`. Hence `|(L+2a)(2a-1)|<=2L`.
If `a` is an integer outside `{0,1}`, the left side is at least
`3(L-8)>2L`. For `a=1`, starting `(0,0,L)` gives
`x_4=L+1`, `x_6=2L+2`, so `d_4=L+1`, impossible.
For `a=0`, starting `(-1,0,L-1)` gives
`x_7=1-L`, `x_9=1-(L-1)^2`, so
`d_7=-L^2+3L-1`, again of magnitude greater than `L`.

Only `r=0` remains. Then `a=u`, `x_3=0`, `x_4=u`,
`x_5=-epsilon L`, `d_2=d_3=-epsilon L`.
The bound at `d_3` gives `-3<=u<=1`, and
`d_4=-u epsilon L`. Its center is `x_5=-epsilon L`;
the bound forces `u=0`. Thus `a=0` and the word is the axis family

`(0,0,t,0,0,-t)` repeated.                            (F6)

### 3.5 Center s=-2

Here `p+q=-epsilon L`, so write `q=-epsilon r`, `r in {0,1,2}`.
Then `d_2=-rL-epsilon(r(u+1)+L)`.
For `epsilon=1,r>=1`, this is at most `-(r+1)L+4r<-L`.
Consider `epsilon=-1`. Then `q=r`, `v=u-L`,
`a=2v+u+r-2`, `x_3=r-2`, and `x_4=rv+u+r`.

If `r=2`, `x_4=2v+u+2`, `x_5=v+u`, `a=2v+u`, and
`d_4=x_4*x_5+a-x_4`. Since `|u|<=5`,

`|d_4| >= (2L-17)(L-10)-4L-32 > L` for `L>100`.

If `r=1`, direct iteration gives

`x_3=-1, x_4=v+u+1, x_5=-2, x_6=-u-2,`
`x_7=v+2u+2, x_8=-uv-2u^2-5u-3`.

Thus `d_5=-L+3u+4` is centered at `-u-2`.
For `u in [-5,3]` outside `[-3,1]`,
`|(u+1)d_5|>=3(L-13)>2L`, impossible. For `u in [-3,1]`,
`d_6=uL-3u^2-4u-1` is centered at `x_7=-L+3u+2`.
The bound gives `|d_6|<=2L/(L-6)<3`. If `u!=0`,
`|d_6|>=L-16>2`; hence `u=0`. But then
`d_7=2L-7>L`, again impossible.

Only `r=0` remains (for either orientation). Now
`a=2v+u-2`, `x_3=-2`, `x_4=u`, `x_5=epsilon L-2`,
`d_2=-epsilon L`, `d_3=epsilon L`,
`d_4=(u+2)epsilon L`. The bound at center `x_5` forces
`u=-2`, giving the all-parameter family

`(-2,-2,t)` repeated, with `a=2t-4`.                   (F3)

### 3.6 Restoring the time orientation

The actual reversor satisfies `R T_a R=T_a^(-1)`. At the centered
scalar triple it sends `(d_0,p,q)` to `(-d_0,-q,-p)`; this is the
sign rule used in Section 3.3. Reversing F3, F4, F6, F8 or F12 gives
a cyclic rotation of the same word. For the Section 3.2 form
`F5(u)=(u,-1,-1-u,0,0)`, reversal is a cyclic rotation of
`F5(-1-u)`, also in the stated all-integer parameter family.
Alternating words are likewise reversal-closed. Hence large-difference
classification of a normalized reversed sequence really classifies
the original oriented orbit; it does not lose an inverse-time branch.

## 4. Consequence: a universal, finite and complete residual core

Every integral periodic orbit is either one of (2), F3, F4, F5, F6,
F8, F12, or has `1<=D<=100`. Every orbit outside F4 in the latter
case obeys `|x_i+1|<=3D` by Section 2. In particular
`-301<=x_i<=299`. This is an analytic universal exhaustion, independent
of the parameter, level and period; it is not an empirically chosen box.

For a finite certification, every residual orbit has a phase, possibly
after reversal, of the form `(u,s,u+D)` with
`1<=D<=100`, `s in {-3,-2,-1,0,1}` and
`-3D-1<=u<u+D<=3D-1`. Its parameter is uniquely recovered from
an integer `p in [-D,D]` by `a=(u+D)-su+s-p`.
Retain only `q=(s+1)D-p in [-D,D]` and the necessary neighbor
bounds `|(u+1)p|<=2D`, `|(u+D+1)q|<=2D`.
These finite loops cover every residual orbit, including either time
orientation, without any parameter cutoff or period cutoff.

For each retained seed iterate the exact integer map until it returns
to its starting triple, or violates `|x_i+1|<=3D` or `|d_i|<=D`.
No arbitrary iteration cutoff is allowed. The process terminates:
the admissible triples form a finite set and the map is injective,
with inverse `(x,y,z)->(xy+a-z,x,y)`; an earlier repeated state must
therefore be the starting state. An exit proves that this seed cannot
belong to the residual periodic core. For a return record the *first*
return scalar word, canonicalized by cyclic rotation only. Reversal is
not used to merge cycles; both orientations must be present in the final
classification, or explicitly identified by a verified cyclic rotation.

The complete finite output must be compared with explicit symbolic
families, leaving an explicit list of all exceptional terminal words.
Its code, exact counts and output digest belong alongside this proof.
The first complete run returned 74,866 admissible seeds, 25,907 returning
seeds, 30,335 difference exits and 18,624 height exits. After adding both
orientations it produced 25,851 distinct cycles. The only unlisted
terminal words are `(-4,-2,-3,-3,-2)` at `a=-13` and
`(-2,-1,0,0,-1,-2,0,-1,0)` at `a=-2`, of least periods 5 and 9.
The complete disjoint theorem statement, return times and exact level
counts are in `IR1_CLASSIFICATION.md`. This is a computer-assisted
classification, not merely a sampled period table; independent review
of both the analytic reduction and finite certificate remains required.

## 5. Native first returns and arithmetic observables

F3 has least period three except `t=-2`, when it is fixed.
F5 has least period five for every integer `u`: a constant word would
require both zero and minus one to be equal.
F6 has least period six except `t=0`, when it is fixed.
F8 has least period eight except `t=-1`, when it is four.
F12 has least period twelve for the standard parameter range `m>=1`;
this assertion is owned and proved in C413, and can also be checked
directly against its proper divisors. The completed finite core, exact
representative ranges and all overlaps with F4/(2) are resolved in
`IR1_CLASSIFICATION.md`, which also proves the least-period claims
directly. Its disjoint table gives the exact counts on each `K_a` level
and native dynamical zeta factors.

The polynomial `K_a=x^2+y^2+z^2-xyz-a(x+y+z)` is invariant by
direct substitution. Ordinary singular points have never been removed.
Source arithmetic remains distinct from target arithmetic;
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.
