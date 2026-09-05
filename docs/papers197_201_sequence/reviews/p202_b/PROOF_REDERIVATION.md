# P202 B: all-length proof reconstruction

Reviewer root; exact frozen Round1. PROVABLE_AS_STATED for the printed
ternary synchronous rule on every nonempty labelled cyclic word. No
q>3, empty-word carrier, all-deepest-source classification or full owner
clearance is inferred. Author and A code were not read/imported to build B.

## Local reconstruction, image and all equality targets

Writing f(a,b)=a+1+[a=1,b=0] modulo3 gives rows111,022,000.
Output1 forces a=0; output2 forces a=1 and b nonzero; output0 permits
a=2, or a=1 when b=0. Two consecutive outputs21 contradict the forced
values at their shared source coordinate. If21 is absent, the baseline
source y-1 modulo3 works at every edge. Its only alternatives change a2
to1 at the first coordinate of a target01 edge. That next source is0;
neither its value nor any other output constraint changes. A target2
before such an optional coordinate still sees a nonzero source neighbor.
Necessity and sufficiency therefore hold independently for all choices,
including the wrap edge. Choices are recovered from the source, so there
are exactly2^e01 distinct sources, and no sources for the forbidden targets.

Different01 edges cannot share a vertex. Consequently e01<=floor(n/2).
An even equality target tiles the circle by01 and is one of its two phases.
An odd equality target leaves one uncovered letter among the tiled pairs.
Removing it leaves all identical01 blocks; according as it is0,1,2 the
word is a rotation of001(01)^(m-1),011(01)^(m-1),012(01)^(m-1).
Conversely every listed word has m pairs and no21. A unique00, unique11
or unique2 distinguishes the three families and prevents a smaller rotation
period, yielding3n distinct odd maximizers. At n=1 the local diagonal
is the colour3-cycle and all three fibres are1. These cover every boundary.

## The run domain really is forward invariant

A nonconstant cyclic word avoiding21 contains0: otherwise changing between
1 and2 around the circle would require21. Starting each block at a zero
run gives0^c_i1^a_i2^b_i with c_i>0 and a_i+b_i>0. Constants have only
constant sources by the decoder; a nonconstant orbit cannot become constant.

Old zeros produce a positive run of ones. If b_i>0, the preceding a_i ones
all become twos and the b_i twos become zeros. If b_i=0, a_i>0 and its last
one becomes zero, leaving a_i-1 twos. Thus the new block lengths are
c'_i=max(b_(i-1),1), a'_i=c_i, b'_i=a_i-[b_i=0]. Their one runs stay
positive and separated, so no omitted merger changes the block count k.
The first-image case a_i=0 is legitimate only with b_i>0 and never creates
a negative length. By the second original step all c_i,a_i>=1.

Subtracting1 from c,a and0 from b gives a nonnegative vector z on3k bins,
mass M=n-2k, with capacities c_j=1 at b bins and0 elsewhere. The local rule
retains the first unit at each capacity-one bin forever and moves all excess
one site each tick. This is exactly existing parking, not a new engine.

## An independent cumulative-flux description

Let U_j(t) be the total number of departures from bin j during the first
t updates, U(0)=0. All particles ever present by the next departure epoch
are z_j+U_(j-1)(t). Of these, one is retained if capacity is1 and the total
is positive; the rest depart. Hence

    U_j(t+1) = max(z_j+U_(j-1)(t)-c_j,0),
    z_j(t) = z_j+U_(j-1)(t)-U_j(t).

This proves the recurrence without giving individual particles paths or
constructing an arrival heap. Equivalently U_j(t) is the nonnegative
maximum of the sums of z-c over backward intervals ending at j of lengths
1,...,t; repeated substitution proves this expression. This auxiliary
max-plus representation is a standard method and earns no contribution
credit. B independently checks cumulative conservation and the synchronous
local recurrence, not an Abelian assertion about unrelated update timing.

The number of occupied slots at time t equals the number of b coordinates
with positive z_j(t). Clearance is exactly that this number is min(k,M):
it means all particles retained if M<=k, or all slots filled if M>=k.

For 1<=M<=k, a still-mobile particle cannot pass k occupied distinct slots:
that would need k+1 particles counting itself. Each slot passed before its
own settlement holds another particle. If it started in a transit bin,
its first slot is at distance at most2 and at most M-1 already occupied
slots can delay it by3 each. Its settling time is at most3M-1. If it
started as excess at an occupied b bin, one other particle was used there;
the bound is3+3(M-2)<=3M-1, and this case requires M>=2.

For M>=k, an empty slot remaining after3k-1 ticks implies a mobile particle
still exists. A particle never restarts after parking, so that particle
moved every tick. These3k-1 destinations visit every bin except its initial
one. The alleged empty slot is not its initial bin, since otherwise it
would already be occupied at time0. It was therefore encountered, a
contradiction. M=0 has clearance0, not a negative formula. All M units in
one c bin fill successive slots at2,5,8,..., attaining3min(k,M)-1 for
every positive pair (k,M). This proves both bounds and all parameterwise
equality examples without finite extrapolation.

## Original-word recurrence and exact first entry

Let A allow edges00,01,11,12,22,20. On each the local output is current+1,
and colour advance preserves the edge set. Thus F is global colour advance
on A, with exact period3 at every nonempty word. Let B allow01,10,12,20.
On each the output is the next letter; hence F is literal left rotation
on B and has exactly the word's spatial period. Intersecting the edge sets
leaves the directed3-cycle: exactly three intersection words if3 divides n,
otherwise none. These statements use original positions, not run phases.

Inside the twice-image domain, all slots occupied means every b_i>=1,
equivalently membership in A. All particles retained means c_i=a_i=1 and
b_i in{0,1}, equivalently membership in B. Before clearance, a missing slot
and a moving surplus exclude both conditions. Since every nonconstant
word eventually clears and constants already lie in A, A union B is the
entire recurrent set and clearance is exactly the remaining entry time.
For any original x, explicitly handle x already recurrent and F(x) already
recurrent; otherwise h(x)=2+clearance(F^2x). No quotient origin determines
a temporal period in this argument.

For n>=3, min(k,n-2k)<=floor(n/3), so the two preliminary steps give
H<=3floor(n/3)+1; M=0 gives at most2. If n=3k+r, k>=1,0<=r<=2,
the literal first two images of1^(k+r+1)2(12)^(k-1) are
2^(k+r+1)0(20)^(k-1) and0^(k+r+1)1(01)^(k-1). The last has all k+r
surplus units in a single c bin and k empty slots, so exactly3k-1 further
steps are needed. Its two predecessors cannot be recurrent because their
future point is not. Hence H=3k+1. At n=1 all three states are recurrent;
at n=2 the upper2 is attained by12->20->01, followed by the two-cycle.

## Labelled cyclic counts and fixed iterates

An adjacency trace counts closed walks with distinguished coordinate0,
therefore labelled words rather than necklaces. The no21 matrix V(1)
has determinant0, trace3 and sum of principal two-minors1, giving
lambda(lambda^2-3lambda+1). Its two nonzero roots are the squares of the
Fibonacci characteristic roots; for positive n their power sum is L_(2n).
Weighting01 by u gives exactly the entire fibre-exponent polynomial.
Evaluating at2 recovers3^n by the complete source partition.

For A, I+P3 has eigenvalues2, exp(i*pi/3),exp(-i*pi/3); its trace is
2^n+(2,1,-1,-2,-1,1)_(n mod6). For B the adjacency Q has characteristic
polynomial lambda^3-lambda-1, hence b_0=3,b_1=0,b_2=2 and
b_n=b_(n-2)+b_(n-3). The b_0 convention is not an empty carrier claim.
Subtracting the actual three-word overlap gives the recurrent count.
F^t fixes A iff3 divides t. A B word is fixed iff it repeats a closed
word of length d=gcd(n,t), giving b_d. The intersection contributes twice
exactly when3 divides d, giving the stated subtraction. This proves every
printed n,t formula and requires no enumeration of finite examples.

## Independent finite controls and limits

B represents words as byte strings and discovers true recurrence using
the composition power F^(3n). It first checks this power is idempotent on
the entire finite carrier, proving in that box that its fixed set is the
true recurrent set. Binary first-entry searches then use this discovered
set, not the claimed language or height. Sparse rank decrements produce
actual full source sets. The entire coefficient polynomial, all maximum
targets, F^t-fixed counts for1<=t<=6n, original C/R actions, and the flux
entry are checked for all797160 words n=1..12. Separate flux controls cover
8708 complete configurations k=1..4,M=0..5; sharp words extend through210.
Two actual fresh processes each pass8456463 assertions with identical
stdout. These are falsifiers, not the all-length proof or novelty evidence.
