# CRC3: cyclic record-count feedback on ternary words

2026-09-05 UTC. Author: root. Status: complete author deductions /
P206 admitted, manuscript gates pending / OWNER_AMBER / HOLD_EXTERNAL.

This paper-local copy changes lifecycle text only. The original author
scouting package and the independent candidate gate remain unchanged.

This fixes a natural three-letter carrier before theorem verification.
It is not an assertion about arbitrary-alphabet maximum fibres. The earlier
CRC exploratory file keeps its more general temporal result and unverified
general-tree inverse route; neither is silently used to prove this package.

## 1. Literal map and exact contract

For n≥1 let X_n={1,2,3}^n with cyclically labelled positions 0,…,n−1.
R(x)_i counts the strict left-to-right record values in the length-n scan
x_i,x_(i+1),…,x_(i+n−1). The first letter is a record. All scans use the
same old word. At most three distinct record values occur, so this is an
autonomous self-map of the full ternary box for every n, not just n≤3.

Put

    D_n={b∈X_n:min b=1, b_i−b_(i+1)≤1 at all cyclic edges},
    C_n={c∈X_n:min c=1, |c_i−c_(i+1)|≤1 at all cyclic edges}.

**Temporal/image theorem.** R(X_n)=D_n and R²(X_n)=C_n. On C_n,
R(c)=(max c+1)·1−c. Thus R⁴=R², the exact recurrent set is C_n,
the sole fixed state is 1^n, and every other recurrent period is two.
The sharp full-carrier tail height is one for n=1,2 and two for n≥3.
Define integer sequences L_0=2,L_1=3,L_n=3L_(n−1)−L_(n−2), and
P_0=2,P_1=2,P_n=2P_(n−1)+P_(n−2). Then

    |D_n|=L_n−2^n,       |C_n|=P_n+1−2^n.

These are equivalent to L_n=((3+√5)/2)^n+((3−√5)/2)^n and
P_n=(1+√2)^n+(1−√2)^n. Strict two-cycle count is (|C_n|−1)/2.
Counts are corollaries, not an additional primitive contribution axis.

For b∈D_n, split its cyclic nonroot positions (b≠1) into runs immediately
before the next position with value one. Empty runs are included: each
one terminates one run. If a run u has length m, define

    g(u)=m+1                         if u has no letter 3;
         length of its final 2-run  if u contains a letter 3.

A run containing 3 necessarily ends in 2 by membership in D_n. Let

    Ψ_n(b)= product_runs g(u) + 1_{b has no 3} + 1_{b=1^n},

and set Ψ_n(b)=0 for b∉D_n.

**Inverse/extremal theorem.** Every target b∈X_n has exactly Ψ_n(b)
one-step sources. The formula arises from a bijective source decoder,
not from brute-force enumeration or a generic unevaluated counting problem.
Let J(n) be the maximum product of positive integers summing to n. Then
the uniform maximum fibre is three for n=1,2, and 1+J(n) for n≥3, where

    J(1)=1;
    J(3a)=3^a                         (a≥1);
    J(3a+1)=4·3^(a−1)                 (a≥1);
    J(3a+2)=2·3^a                     (a≥0).

At n=1 the only maximizing target is 1. At n=2 they are exactly 11,12,21.
For n≥3 every maximizing target uses only letters 1,2, and its cyclic
blocks 2^(s−1)1 have sizes forming a product-maximizing composition of n.
Equivalently, all sizes are 3 when n≡0 mod 3; when n≡1 mod 3 they are
3's and either one 4 or two 2's; when n≡2 mod 3 they are 3's and one 2.
All cyclic placements of these blocks on the labelled positions qualify.
No orbit quotient is taken when stating equality targets.

## 2. First image, two-step dynamics, and sharp boundary cases

For any x, the coordinates of R(x) equal to one are precisely the positions
of the global maximum of x. In particular min R(x)=1. Comparing scans
starting at i and i+1, all record values after the initial x_i in the former
also occur as records in the latter: they exceed x_i and every intervening
value. The former has at most one extra initial record, so
R(x)_i≤R(x)_(i+1)+1. Hence R(X_n)⊆D_n.

Conversely, for b∈D_n set x_i=4−b_i. This word has maximum three and
cyclic upward steps at most one. A scan from x_i visits every integer
level from x_i to three before it can exceed that level. Its strict record
values are exactly those integers, so R(x)_i=4−x_i=b_i. This proves the
exact first image without using the proposed general-tree inverse.

Let b∈D_n and c=R(b). We already know c_i−c_(i+1)≤1. If b_i<b_(i+1),
the next position is the first new record and c_i=c_(i+1)+1. If equal,
c_i=c_(i+1). If b_i>b_(i+1), the D_n condition forces a unit drop.
The scan from the lower value b_(i+1) can therefore have at most one
extra record, the value b_i, before the record values strictly larger than
b_i shared by the two scans. It follows that c_(i+1)−c_i≤1. This includes
the global-maximum case, in which the final scanned b_i supplies that one
possible extra value. Thus R(D_n)⊆C_n.

For c∈C_n put M=max c. Since its upward steps have size at most one, a
scan from c_i has all and only the record values c_i,c_i+1,…,M. Hence
R(c)_i=M+1−c_i. The resulting word has minimum one, maximum M and unit
steps, and applying the reflection twice is identity. Every c is its own
two-step preimage. Therefore R²(X_n)=C_n and R⁴=R². Every periodic state
lies in the second image, proving exact recurrence. A reflection-fixed
word must be constant; minimum one makes it 1^n.

For n=1 every word reaches 1 in one step; the source 2 proves sharpness.
For n=2 the first image is {11,12,21}=C_2 and the source 22 has tail one.
For n≥3, x=1^(n−2)23 has first image 3^(n−2)21. The closing edge from
1 to 3 is not a unit step, so this image is outside C_n and x has tail
two. The general second-image theorem supplies the upper bound.

## 3. Exact image and recurrent populations

For cyclic walks through the ordered alphabet 1,2,3, let A have entry
A_ij=1 if i−j≤1 and zero otherwise. Thus

    A = ((1,1,1),(1,1,1),(0,1,1)).

The number of cyclic labelled words respecting these edge constraints is
tr(A^n). Those avoiding 1 use the all-ones 2×2 matrix and number 2^n.
The characteristic polynomial of A is λ(λ²−3λ+1); for n≥1 its trace
is L_n. Subtraction gives |D_n|. For C_n the analogous matrix is

    B = ((1,1,0),(1,1,1),(0,1,1)).

It has eigenvalues 1,1+√2,1−√2. Its words avoiding 1 again number 2^n.
Thus |C_n|=P_n+1−2^n. This is the ordinary transfer-matrix count with
the minimum constraint subtracted; no new spectral-counting tool is claimed.

## 4. Every-target inverse decoder, by the source maximum

It suffices to treat b∈D_n, as the first-image theorem rejects all other
targets. If the source maximum is one, the only source is 1^n, contributing
the final indicator. If its maximum is two, each source letter two is
an output one and each source letter one has records 1 then 2, giving
output two. Thus there is one such source precisely when b has no 3:
take x_i=3−b_i. The target has a one, so this source really has maximum
two, even for b=1^n. This contributes the middle indicator.

Now the source maximum is three. Its three positions are exactly the
one positions in b. The source on each intervening run uses only 1,2.
A source two yields output two. A source one yields output three exactly
when there is a source two later in that run, before the next three;
otherwise its output is two.

If a target run u has no 3, the source run must be weakly decreasing:
2^a1^(m−a), for exactly m+1 choices a=0,…,m. Conversely all of them
give that target run. This includes an empty run with one choice.

If u contains 3, let its last 3 be followed by a terminal run of t twos.
Here t≥1. Every target three forces source one. Every target two before
the last three forces source two: otherwise it would have a later two
and would itself output three. On the final t positions, the source is
2^a1^(t−a) with 1≤a≤t. A positive a is necessary to trigger the last
target three, and it also triggers all earlier target threes. The forced
prefix and each of these t tails therefore produce exactly the prescribed
run. This reconstructs all sources, with no collisions or omissions.

Distinct runs are independent after their terminating source threes are
fixed. The maximum-three contribution is product g(u). The three distinct
source-maximum cases are disjoint, so their sum is precisely Ψ_n(b).

## 5. Uniform maximum and every equality target

If b has any 3, replace all its threes by twos, obtaining b*. The roots
and run lengths remain the same. For a run of length m containing a 3,
its final two-run length is at most m−1 and therefore strictly smaller
than m+1. All other run factors are unchanged. Consequently

    Ψ_n(b) = product g(u) < product (m(u)+1) < Ψ_n(b*).

Such a target cannot maximize. The all-one target has fibre three.
Every remaining binary target has at least one two. If its consecutive
root-terminated block lengths are s_1,…,s_k, then s_j≥1, sum s_j=n,
and the inverse theorem gives fibre 1+product s_j. Conversely every
composition of n other than all ones is realized by concatenating
2^(s_j−1)1. Therefore the optimization is exactly integer-product
maximization, with the constant target considered separately.

For n≥2 no maximizing product partition has a part one: merging it with
any other part increases the product, including the two-singleton case.
A part s≥5 can be split into 3 and s−3, since 3(s−3)>s. A part four can
be kept or split into two twos without changing the product. Three twos
are inferior to two threes, since 8<9. These replacements prove that
every optimum, after optionally splitting its fours, consists of threes
and at most two twos. Sum modulo three now gives exactly the values J(n)
and the complete part lists stated in §1. Every listed composition has
that product, so the converse equality direction holds as well.

For n≥3, 1+J(n)>3, excluding the constant target and proving all equality
cases. For n=2 the constant target and the two length-two cyclic placements
both give three; the image contains no other target. For n=1 only target
one is in the image and has its three constant sources. QED.

## 6. Exact limits and value questions

Strict record statistics, next-greater/Cartesian encodings, bounded-word
transfer matrices, run factorization, integer products and the 2/3 optimum
are classical primitives and receive zero invention credit. The proved
interaction is specific to recomputing all cyclic record counts and to
recovering ternary source runs, then transporting the sharp product
optimization back to every labelled target. Source/collision review must
determine whether a prior literal result or explicit full adapter removes
that conjunction; none is claimed absent merely because a search had no hit.

There is no every-time fibre formula, maximum-fibre theorem for q>3,
arbitrary-alphabet paper, or global novelty certificate. The general
temporal spike and the NS/P204 review risk are visible controls, not reasons
to relax this candidate's two-axis gate. The standalone author verifier and
independent candidate gate are now real completed inputs; root read the full
gate and actual source contexts, checked its pins and performed two fresh
raw-canonical replays. P206 is admitted on the narrow contract only.
Both independent manuscript reviews, accepted deltas and terminal gates
remain required before any completed-paper claim.
