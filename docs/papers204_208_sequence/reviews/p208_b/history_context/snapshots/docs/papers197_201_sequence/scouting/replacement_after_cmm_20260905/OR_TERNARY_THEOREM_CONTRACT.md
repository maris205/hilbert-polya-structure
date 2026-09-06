# Ternary ordered-reset oscillator: all-length theorem spike

Date: 2026-09-05 UTC. Stage1 candidate only, NO PAPER NUMBER, HOLD_EXTERNAL.
This package is not promotion or an external originality claim. Queue,
traffic and coupled-oscillator owners must be subtracted independently.

## 1. Literal finite autonomous system

For every n≥1 the carrier is all cyclic words x in {0,1,2}^n, indexed by
Z/nZ. All comparisons use 0<1<2. Define simultaneous update

```text
F(x)_i = (x_i+1) modulo 3     if x_i ≤ x_(i+1),
         0                    otherwise.
```

Equivalently 0 always goes to1, 2 always goes to0, and 1 goes to0 when
its right neighbor is0 and to2 otherwise. No schedule, auxiliary counter,
external random choice or restricted initial stratum is supplied.

Let C add one modulo3 to every letter and let R shift left by one.

## 2. Entire one-step image and every target inverse

For a target y let e01(y) count its cyclic adjacent occurrences of 01.
Then

```text
y is in im(F) iff y has no cyclic adjacent 21,
|F^(-1)(y)| = 2^e01(y)       when y avoids21,
              0              otherwise.
```

Proof of necessity: output2 at i requires source1 there and a nonzero
right source. Output1 at i+1 would instead require that right source to
be0, a contradiction. For a target avoiding21, start with x_i=y_i−1
modulo3. A target1 forces source0; a target2 forces source1; a target0
permits source2. In addition, exactly at a target occurrence y_i y_(i+1)=01
one may change x_i from2 to1. It then sees source0 on its right and
resets to0 as required. These choices do not interfere. Conversely every
source of output0 is either2 or1 followed by0, and the latter requires
target01. Thus this is a full independent-bit source-set bijection, not
only a cardinality computation. It includes all-zero target (one source)
and n=1 (every target has one source).

The first-image size is trace(J−E_(2,1))^n=L_(2n), where L denotes Lucas
numbers L_0=2,L_1=1. The characteristic polynomial is
lambda(lambda^2−3lambda+1), giving the stated value for n≥1.
The complete positive-fibre size generating polynomial is trace(M(u)^n),
where M has every entry1 except M_(2,1)=0 and M_(0,1)=u. This trace is
standard labelled-word enumeration, not another contribution mechanism.

## 3. Sharp maximum fibre and all maximizers

Occurrences of01 cannot share vertices, so e01≤floor(n/2). For even
n≥2 equality forces one of the two alternating words. For odd n=2m+1≥3,
equality leaves exactly one letter beyond m disjoint01 pairs. The leftover
letter is either0,1,or2; after cyclic placement these give exactly the n
rotations of each of

```text
001(01)^(m−1),    011(01)^(m−1),    012(01)^(m−1).
```

Every such word avoids21. Each has a unique doubled0, doubled1, or sole2,
respectively, so each has n distinct rotations and the three classes are
disjoint. Conversely cut at the leftover letter in any maximizer; the
remaining disjoint01 pairs must alternate, so the list is exhaustive.
Therefore max fibre is 2^floor(n/2), with exactly2 maximizing targets at
even n, exactly3n at odd n≥3, and all3 targets at n=1.

## 4. Run coordinates after two iterations

A nonconstant image word has a unique cyclic decomposition, up to choosing
the first block, into

```text
0^{c_i} 1^{a_i} 2^{b_i},    c_i≥1, a_i,b_i≥0, a_i+b_i≥1,
```

because no positive run can contain21. There are k such blocks. Direct
application of the literal rule gives, with tracked block indices,

```text
c_i' = max(b_(i−1),1),
a_i' = c_i,
b_i' = a_i − 1[b_i=0].
```

When b_i>0 all a_i ones advance to2 and the b_i twos become0. When b_i=0,
the final1 instead resets to0, giving one zero and a_i−1 twos. The c_i
zeros become c_i ones in both cases. The next zero-run comes from the
previous block. These observations prove the equations and preservation
of k. They hold up to cyclic index rotation if one canonically rechooses
the first block; no fixed physical origin is being suppressed in a claim
of full-system conjugacy.

In particular, after two original iterations every nonconstant state has
c_i,a_i≥1 and b_i≥0. Put

```text
z_(c_i)=c_i−1,    z_(a_i)=a_i−1,    z_(b_i)=b_i,
M=sum z = n−2k.
```

The equations become

```text
z_(c_i)' = max(z_(b_(i−1))−1,0),
z_(a_i)' = z_(c_i),
z_(b_i)' = z_(a_i)+min(z_(b_i),1).
```

This is a directed ring of3k bins in the order c_i→a_i→b_i→c_(i+1).
Each b-bin holds one particle permanently once occupied; all other
particles move one bin forward at every step. The c/a bins hold nothing.
This queue/parking description is a proof coordinate system, and generic
one-way transport is explicitly background. It must not be called fresh
merely because it is a different carrier.

## 5. Finite transport lemma with a sharp bound

On a3k-bin directed ring with one parking slot every third bin and M≥1
particles, put one particle in each initially occupied parking slot and
regard all remaining particles as free. A particle arriving at an empty
slot parks there; all others stay free and continue one bin per step.
Parked particles never become free. If several arrive together, choose
any one to park; unlabelled bin counts do not depend on the choice.

The first time either all M particles are parked or all k slots are
occupied is at most

```text
3 min(k,M) − 1.
```

For M≤k, consider any free particle until it parks. Every parking slot
passed without stopping is occupied by another particle, so it can pass
at most M−1 such slots before reaching an empty one. These visited slots
are distinct: while a free particle remains, M≤k guarantees an empty slot,
which stops it within its first full circuit. If it starts outside a parking slot, the first
slot is at distance at most2, giving distance at most2+3(M−1)=3M−1.
If it starts in an occupied parking slot, that slot already accounts for
another parked particle; the next slot is at distance3 and at most M−2
future occupied slots can precede its destination. The resulting bound
is3+3(M−2)≤3M−1. This covers all initial free particles.

For M≥k, suppose a slot remained empty after3k−1 steps. Since there are
at least k particles but fewer than k parked particles, some particle is
still free. It has been free from time zero and has moved every step.
Its path of3k−1 steps visits every bin except possibly its starting bin.
Thus it passed the proposed empty slot and would have parked there. If
the empty slot were its starting bin, the particle could not initially
have been free there: an initial particle occupies an empty slot at once.
This contradiction proves the bound.

The bound is sharp for all k,M≥1: place all M particles in one c-bin,
immediately after a parking b-bin. They reach successive parking slots
at times2,5,8,...; the last required slot fills at
2+3(min(k,M)−1). For M=0 the clearance time is zero.

## 6. Complete recurrence, not merely sufficient recurrent examples

Define two explicit word sets:

```text
A_n = {x : x_(i+1)−x_i modulo3 is0 or1 for every i},
B_n = {x : every adjacent pair lies in {01,10,12,20}}.
```

B_n is precisely the set of circular concatenations of ramps01 and012.
On A_n, every iterate is global colour advance C, and all points have
exact period3. On B_n, F=R, and each point's period is its least spatial
rotation period. These two statements follow by checking the indicated
allowed adjacent pairs and their invariance under the respective action.

In the run coordinates of Section4, all parking slots filled means all
b_i≥1, exactly A_n among nonconstant run states. All particles parked
means c_i=a_i=1 and b_i in{0,1}, exactly B_n. The transport lemma proves
that every nonconstant orbit enters A_n union B_n; constant words already
belong to A_n. Conversely both sets consist of recurrent points by the
explicit actions. Thus

```text
Rec(F)=A_n union B_n.
```

This proves necessity as well as sufficiency. Moreover, in the twice-image
run stratum, entry to Rec(F) is exactly the first transport epoch at which
all particles are parked or all slots filled. Before that epoch there
is both a free particle and an empty slot, excluding both core criteria.
This is an exact pointwise first-entry criterion, not just an upper bound.

## 7. Sharp all-length maximal tail

Let H(n) be the largest tail to recurrence over all3^n states. Then

```text
H(1)=0,       H(2)=2,
H(n)=3 floor(n/3)+1             for n≥3.
```

For a nonconstant twice-image, k≥1,M=n−2k≥0. If M>0, Section5 gives
tail at most2+3min(k,M)−1. Since min(k,n−2k)≤floor(n/3), this proves
the upper bound. If M=0 the state is already in B_n after two steps.
Constant twice-images also give tail at most two. For n=1 every word
is constant. At n=2 the same argument gives bound2, and12 attains it.

For n=3k+r≥3 with r in{0,1,2}, use the explicit word

```text
x = 1^{k+r+1} 2 (12)^{k−1}.
```

Its first two outputs are

```text
2^{k+r+1} 0 (20)^{k−1},
0^{k+r+1} 1 (01)^{k−1}.
```

The second output has k blocks, M=k+r particles, all in one c-bin,
and all parking slots empty. Section5's sharp configuration takes3k−1
further steps to enter the recurrent core. Therefore x has tail3k+1.
No earlier iterate can be recurrent since the recurrent set is invariant.

## 8. Exact recurrent census

Let a_n=|A_n|=trace(I+P_3)^n, where P_3 is the three-colour cyclic
permutation matrix. Explicitly a_n=2^n+epsilon_n, with epsilon periodic
modulo6 equal to2,1,−1,−2,−1,1. Let

```text
Q = [[0,1,0],[1,0,1],[1,0,0]],      b_n=trace(Q^n).
```

Then b_0=3,b_1=0,b_2=2 and b_n=b_(n−2)+b_(n−3) for n≥3.
The intersection A_n cap B_n consists exactly of the3 rotations of
(012)^(n/3) when3 divides n, and is empty otherwise. Hence

```text
|Rec(F)| = a_n+b_n−3·1[3 divides n].
```

For every t≥1 and d=gcd(n,t),

```text
|Fix(F^t)| = 1[3 divides t] a_n + b_d −3·1[3 divides d].
```

The two actions and their intersection prove this directly. Standard
trace/Burnside/Möbius consequences are zero independent contribution credit.

## 9. Claim and source boundary

The candidate needs an independent exact-history and external owner gate.
The current proof uses one-way finite transport, local-source decoding and
finite adjacency traces, all of which are generic tools and not innovations
in themselves. The proposed residual is the completely specified reset
oscillator with its full A/B recurrent exhaustion, sharp all-length tail,
first-entry transport criterion and independent targetwise source atlas.

The full ordered-reset alphabet family q>3 was piloted but is NOT covered
by this ternary theorem; its irregular sharp-tail pattern is not extended
by analogy. No candidate is promoted on the basis of these exploratory
boxes, and no killed P198/P201 artifact or disposition is rewritten.
