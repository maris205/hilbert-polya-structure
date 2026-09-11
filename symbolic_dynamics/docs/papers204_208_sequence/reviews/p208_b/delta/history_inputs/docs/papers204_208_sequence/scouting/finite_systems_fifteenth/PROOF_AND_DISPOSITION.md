# Fifteenth lane: proof boundaries and bounded no-promotion disposition

2026-09-06 UTC. Proofs and author checker: `batch197_lzk_gate`.
`fifteenth_history_desk` supplied historical formula/reading evidence only.
No independent candidate or manuscript review has occurred. All proofs
below are author deductions, not admissions. The bibliography correction
in `SOURCE_ERRATUM.md` controls over the frozen source input's wrong initial.

## 1. Arithmetic derivative maps: what is actually proved

Fix squarefree N with prime set P, and identify d with its prime subset S.
Leibniz gives d'=sum_(q in S) d/q, with the empty sum zero. For p in S,
every term but d/p is divisible by p, while d/p is not. Consequently
gcd(d,d')=1. This is the old squarefree primitive, not a new result.

**LPG.** The output is always 1. If N=1 the sole state is fixed. If N>1,
1 is the sole fixed state, all other states have depth one, and the fibre
at 1 has 2^|P| elements; all other target fibres are zero. This is a desk
kill, not a third executed map or a candidate contribution.

**ADG.** Adjacent supports are disjoint. T_N(1)=N, T_N(N)=1. For N>1
there are no fixed points: a fixed d must divide both itself and d', hence
d=1, but T_N(1)=N>1. This proves the displayed two-cycle only, not that
it is the whole recurrent set. For p outside S, divide d' modulo p by
the unit d to obtain

    p divides T_N(d) iff sum_(q in S) q^(-1)=0 in F_p.

Thus a target subset R has precisely the input subsets S disjoint from R
for which every p in P minus S satisfies the displayed zero test exactly
when p lies in R. This is a finite congruence predicate, **not** an
evaluated all-target inverse formula or a sharp extremal theorem.

The executed 256 carriers all have only the {1,N} cycle (the N=1 boundary
is a fixed point), with finite maximum depths at most four. This is not
an all-squarefree-N assertion. An actual witness in the box is

    N=3990: 38 -> 21 -> 10 -> 7 -> 1 -> 3990 -> 1.

Indeed 38'=21, 21'=10, 10'=7, 7'=1. The same four-arrow tail holds
analytically for every squarefree multiple N of 3990, since 21,10,7
divide N and none of 38,21,10,7 is 1 or N. This is a lower witness, not
a global upper clock. No added parameter box is run to establish it.

Within the fixed box, 1 is a maximum-fibre target for every N and the
unique such target except for the eight prime N (where both divisors
have fibre one). This finite fact is not promoted to a universal maximum
classification. ADG lacks the requested full temporal theorem and the
materially separate evaluated inverse/extremum; **CLOSE_NO_PROMOTION**.

## 2. Distinct-pair intersection on antichains: old erosion deducted

An antichain with at least two members contains neither the full ground
set nor two comparable sets. Every distinct-pair intersection is strictly
smaller than both participating sets; discarding nonmaximal intersections
cannot create a larger member. Thus, while at least two members remain,
the maximum member size decreases by at least one. A singleton goes to
the empty family on the next arrow, and the empty family is fixed.

For n>=2 a nonsingleton input has largest size at most n-1; after at most
n-1 arrows it is empty or the singleton containing the empty subset,
and one more arrow gives the empty family. The maximum depth is exactly
n: if L_(n,k) denotes all k-subsets, then

    L_(n,n-1) -> L_(n,n-2) -> ... -> L_(n,0) -> empty family.

For 1<=k<=n-1 each (k-1)-subset extends to two distinct k-subsets and
all smaller intersections are dominated by such a (k-1)-subset, proving
each equality. For n=0,1 every antichain has at most one member, so the
height is one. This tight antichain boundary remains the old DI
maximal-layer erosion mechanism. **FID is desk-killed with zero credit**;
no numerical FID evaluation was executed.

## 3. Maximal symmetric differences: a general obstruction, not promotion

For a nonsingleton family C, a ground element belongs to some pairwise
difference exactly when it belongs to some but not all old members.
Every member of the raw difference family is contained in a maximal
member, so maximalization preserves its union. Therefore

    union T(C) = (union C) minus (intersection C).

This shadow need not determine the antichain, its time, or its inverse.
At n=4 the full singleton layer maps to the full two-subset layer, then
to the singleton family containing the whole ground set, then to empty.
Thus first-image inclusion fails even with four original members; this
is not the two-input boundary failure already present in unrestricted SX.
The old SX first-image closure proof cannot be transferred through Max.

### Uniform-layer identity, proved for all n rather than extrapolated

For 1<=k<=n-1 write u=min(k,n-k). The distinct-pair differences of
L_(n,k) are exactly the subsets of every even size 2,4,...,2u. Necessity
follows from |A triangle B|=2(k-|A intersection B|) and the ground-size
bound. For sufficiency, given D of size 2s with 1<=s<=u, split D into
two s-subsets and choose a common (k-s)-subset outside D. Such a common
subset exists because n-2s>=k-s. The resulting k-subsets differ exactly
on D. Every smaller even subset extends to a 2u-subset, so

    T(L_(n,k)) = L_(n, 2 min(k,n-k)).

The endpoint layers k=0,n are singleton families and go to the empty
family. This is a one-dimensional folded doubling rule on this special
layer family, not a classification of all antichain dynamics.

It supplies a decisive barrier against inferring periods <=2 from n<=5.
For every integer r>=3, take n=2^r-1. The following distinct layers form
an exact cycle of length r:

    L_(n,2), L_(n,4), ..., L_(n,2^(r-1)), L_(n,2^r-2).

Successive powers double; 2^(r-1) maps to 2^r-2; that final size n-1
maps back to 2. All sizes are distinct for r>=3. For example the theorem
gives a three-cycle of sizes 2,4,6 at n=7. **No n=7 or larger carrier was
enumerated**: this is a symbolic proof inside the same map, not a raised
pilot cutoff. These unbounded periods are not a complete rigid temporal
classification and do not create a second independent mechanism axis.

### Only simple inverse slices are evaluated

T(C) is the empty family exactly when C has at most one member: distinct
members always produce a nonempty family of differences, and a finite
nonempty family has a maximal member. Thus the empty-family target has
fibre 2^n+1 for every n, counting the empty family plus all singletons.

For n>=1 the target consisting only of the full ground set is reached
exactly when C contains a complementary pair A, A^c. Necessity: that
ground set must itself occur as a difference. Sufficiency: once present,
it dominates every other difference. Antichain incomparability rules out
the endpoint pair empty/full; at n=1 this fibre is consequently zero.
For n=0 the family containing the empty subset cannot occur as a distinct
pair difference, so its fibre is also zero.

This characterizes one fibre as a constrained-antichain counting problem;
it is not a closed count for all targets or a maximum classification.
In the executed box, the empty target is maximal for n<=3, whereas the
full-ground singleton is uniquely maximal at n=4,5, with counts 41,2580.
The finite switch itself prevents assuming a single early extremizer.
FSD has no complete temporal classification or evaluated all-target
inverse/extremum beyond these elementary slices. **CLOSE_NO_PROMOTION**.

## 4. Truncated unit series: generic inverse mechanisms already complete

All statements use the finite carrier in `INTAKE.md`, with truncation
modulo x^(m+1), constant coefficient 1, prime p and m>=0.

**USS.** Write T(f)=1+sum_(k=1)^m b_k x^k. The term a_k x^k f(x)^k
contributes a_k at degree k, and a term with index j<k uses coefficients
at most k-j<k. Therefore b_k=a_k+P_k(a_1,...,a_(k-1)). Solve successively
for every a_k to invert every target. This proves a permutation, zero
tails and fibre one at every target, including the m=0 singleton case.
Its possible cycle census does not turn the singleton inverse into a
materially separate structure. **Desk kill; no executed USS pilot.**

**WCF.** The identity

    T(f)-T(g) = -x(f-g)/((1+xf)(1+xg))

has a unit denominator. Until truncation kills it, a nonzero difference
has x-adic order raised exactly by one. The fixed equation is h+xh^2=1;
its coefficient recurrence determines one and only one unit h, over any
field, without dividing by an integer. The recurrence is the signed
Catalan recurrence, so h_k=(-1)^k C_k reduced modulo p; this is compatible
with the classical generating-function primitive identified in the source.

If f=h its depth is zero. Otherwise, with v=ord_x(f-h) in {1,...,m}, its
exact depth is m+1-v. Hence for m>=1 the height is exactly m (choose a_1
different from h_1=-1); the sole recurrent state is h.

For m>=1 a unit target y is in the one-step image exactly when its first
coefficient is -1. Indeed, from y^(-1)=1+xf one recovers f modulo x^m
as (y^(-1)-1)/x. The constant coefficient is 1 precisely under that
condition, and the degree-m coefficient of f is arbitrary. Consequently
each nonempty fibre has p members, there are p^(m-1) image targets, all
of them attain the maximum p, and all other target fibres vanish. For
m=0 there is one fixed state and one fibre of size one. These exact
results are the generic precision/forgotten-coefficient mechanism already
deducted before code. **Desk kill; no WCF pilot or new candidate credit.**

## Final boundary

Six literals on three carrier neighbourhoods were genuinely screened;
only ADG/FSD were executed within the original full boxes. The source
search is bounded and the mathematical deductions are author work.
Neither surviving pilot supplies the required conjunction after the old
primitives and generic encodings are deducted. Status is
**BOUNDED_CLOSE_NO_PROMOTION**, not a claim of impossibility or global
prior-art absence. No reserve, paper number, independent PASS, central
index/Git change, external action or automatic further lane is authorized.
