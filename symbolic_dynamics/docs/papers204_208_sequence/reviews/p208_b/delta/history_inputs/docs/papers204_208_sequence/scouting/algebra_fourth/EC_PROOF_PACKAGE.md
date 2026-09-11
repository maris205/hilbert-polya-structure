# EC: endpoint-distance feedback — valid author proof, no promotion

Date: 2026-09-05 UTC. Author: algebra scout (`batch197_lzk_gate`).
This is a candidate proof package, not an independent review or admission.
Final author disposition: `PROOF_COMPLETE / NO_PROMOTION_VALUE_TOO_THIN /
OWNER_AMBER / HOLD_EXTERNAL`. The initial proof-complete/value-pending
signal was downgraded after completing the static inverse adapter below.
Only this candidate received a deep proof pass after the six-map pilot.

## 1. Literal carrier and bounded claim contract

For integers n >= 1 and M >= 0, let X = {0,...,M}^n. Define

    E(x)_i = max_{1 <= j <= n} |x_i - x_j|.

Labels and repeated coordinates remain in the state. This is not the
farthest-neighbour point selector, a fixed metric's eccentricity profile,
the complete list of pairwise distances, or cyclic adjacent differences.
Distances are recomputed from the new coordinates at every epoch. The map
is total on X, including n = 1 and constant vectors.

The proved contract is: unique recurrent state; sharp global entrance time;
every labelled one-step inverse set and its cardinality; exact first-image
census; maximum one-step fibre and all equality targets. No all-time inverse
atlas, closed pointwise entrance-time formula, transient-layer census,
higher-dimensional metric extension, or global novelty is asserted.

## 2. Endpoint fold, convergence, and sharp height

Write alpha = min x, beta = max x and R = beta-alpha. For every i,

    E(x)_i = max(x_i-alpha, beta-x_i).                    (2.1)

Indeed every other coordinate lies in [alpha,beta], and both endpoints
occur among the coordinates. Consequently max E(x) = R and

    min E(x) >= ceil(R/2),
    range E(x) <= floor(R/2).                           (2.2)

If x has k > 1 distinct values, (2.1) sends its two distinct endpoints to
the same value R. As all outputs depend only on their input value, the
number of distinct values drops by at least one. Constants map to zero.
Thus every orbit reaches zero in at most k <= n steps, and zero is the
unique recurrent state and unique fixed point. This argument itself works
for any finite real coordinate vector; only the logarithmic bound below
uses integrality.

Let mu(x) = min{t >= 0: E^t(x) = 0}. Iterating (2.2), a nonconstant vector
of diameter R >= 1 becomes constant in at most floor(log_2 R)+1 steps,
then becomes zero one step later. For M >= 1 this gives

    H(n,M) := max_{x in X} mu(x)
           <= min(n, floor(log_2 M)+2).                 (2.3)

All boundary cases and equality are as follows:

    H(n,0) = 0;
    H(n,M) = min(n, floor(log_2 M)+2) for M >= 1.        (2.4)

For n = 1 and M >= 1, (1) is a sharp witness. For n >= 2, put the right
side of (2.4) equal to h >= 2. Use the h distinct coordinates

    S_h = {0,1,2,4,...,2^(h-2)}

and repeat zero to fill the remaining n-h labels. They lie in [0,M].
For h = 2 their first image is the positive constant 1, so their height is
two. For h >= 3 put R = 2^(h-2). The support of the first image is

    {R} union {R-2^j: 0 <= j <= h-3}.

Reflection about R identifies this set with S_(h-1). Translating or
reflecting a nonconstant support does not change its subsequent distance
profile, hence does not change its time to zero. Duplicating coordinates
does not change the support trajectory. Induction proves height h.
The support-drop and diameter bounds are distinct obstructions; (2.4)
gives their exact simultaneous optimum, not just a logarithmic estimate.

## 3. Full labelled one-step inverse sets

For a target b in X write r = max b. If r = 0, its sources are exactly the
M+1 constant vectors. Assume henceforth r > 0. Any source interval must
have width r by max E(x) = range x. Write its minimum as a, where
0 <= a <= M-r. Equation (2.1) gives the complete coordinate solution

    x_i in {a+b_i, a+r-b_i}.                            (3.1)

These choices have a solution in [a,a+r] exactly when every b_i >= ceil(r/2).
Both endpoints a and a+r must occur in the source. They can occur only at
target positions where b_i = r. Thus the full inverse set is the disjoint
union, over a = 0,...,M-r, of the choices (3.1) satisfying both endpoint
requirements. This is a source-set bijection: each decoded source has
minimum a, maximum a+r, and E(x)=b; every source has exactly this encoding.

Let

    A = #{i: b_i = r},
    Z = #{i: 2 b_i = r}.

The midpoint set counted by Z is empty when r is odd. If min b < ceil(r/2)
or A < 2, the inverse is empty. Otherwise

    |E^-1(b)| = (M-r+1) (2^A - 2) 2^(n-A-Z).           (3.2)

There are 2^A endpoint assignments, with precisely the two constant
endpoint assignments forbidden. A midpoint has one branch and each
remaining position has two. Different interval minima cannot overlap.
Equation (3.2) covers every target, every parity, and repeated coordinates;
the r=0 constant-source clause is separate because the two branches then
coincide everywhere.

## 4. Image census and all maximum fibres

For each fixed positive r, a target in the image uses the alphabet
{ceil(r/2),...,r} and must contain the top symbol at least twice. If
q = floor(r/2), the number of such targets is

    (q+1)^n - q^n - n q^(n-1).

For n >= 2 this has no 0^0 ambiguity and yields

    |im E| = 1 + sum_(r=1)^M [
                 (floor(r/2)+1)^n - floor(r/2)^n
                 - n floor(r/2)^(n-1)].                (4.1)

For n = 1 the image has size one. The leading 1 in (4.1) is the all-zero
target. This census is an elementary alphabet-occupancy consequence of
the inverse characterization, not a third contribution mechanism.

For n >= 2 and M >= 1 the all-one target has fibre M(2^n-2). For a positive
target, (3.2) is at most (M-r+1)(2^n-2): dropping midpoint restrictions can
only enlarge the binary branch set, and omitting either global endpoint
still forbids at least the two uniform assignments. Equivalently,
(2^A-2)2^(n-A-Z) <= 2^n-2 for A >= 2. Equality in the global bound at a
positive target requires r=1; then every target coordinate is 1. For r>1
the interval factor is strictly smaller than M.

The zero fibre is M+1. Comparing it with M(2^n-2) gives the full statement:

- If M=0, the sole target/source is 0^n and the maximum is one.
- If n=1, the sole image target is 0 and the maximum is M+1.
- If n=2 and M=1, the maximum is two, attained exactly by 00 and 11.
- Otherwise, for n>=2 and M>=1, the maximum is M(2^n-2), attained only by 1^n.

For n>=3, M(2^n-2)-(M+1) >= 5M-1 > 0. For n=2 the difference is M-1.
This accounts for all equality and degeneracy cases.

## 5. Exact subtraction and remaining value question

The static eccentricity transform, the endpoint identity (2.1), reflection
and translation invariance, scalar absolute-value branch inversion,
binary word counting, and finite-support merger arguments all receive zero
primitive novelty credit. In particular, (3.2) is entirely adapted to the
following elementary static experiment: choose an interval of width r,
choose one of two reflected positions per nonmidpoint label, require both
endpoints. The adapter is fully bijective, not an asymptotic analogy.

The remaining temporal signal is the exact autonomous remeasurement clock
(2.4). The endpoint-constrained inverse and its extrema, however, are
entirely supplied by the explicit static branch adapter. Mathematical
separation of the proofs does not establish a materially independent
inverse research contribution. The final author disposition is therefore
NO_PROMOTION_VALUE_TOO_THIN: no second residual axis has been demonstrated.
The image census is not counted as a replacement axis, an exact-literature
non-hit does not prove novelty, and neither M nor the metric dimension is
enlarged to rescue the value gate. This is an author rejection, not a
fabricated independent reviewer verdict or a claim of an exact published
owner for the whole autonomous operator.

Nearest located primary sources and their actual read scope are in
SOURCE_AND_COLLISION_NOTES.md. They establish a pre-existing static
eccentricity surface, not by themselves ownership of this autonomous
one-dimensional feedback system. The current source audit is bounded.

## 6. Evidence and proof authorship

The first intake has 15 EC boxes among six maps and 41 boxes; all one-step
fibre formula and sharp-height controls in pilot.py pass. After the above
deductions, verify_structure.py checks 30 EC parameter boxes, all 15,029
labelled source/target states, full decoded source sets (not merely counts),
diameter and support inequalities, image census, and all maximum targets.
It additionally checks 462 symbolic geometric-support witnesses through
n=33 and M=2^30, without enumerating those large carriers.

The structural script also verifies the CP permutation adapter and OR
tableau-transpose adapter. Its total assertion count is 139,395. It imports
no pilot, prior paper, or candidate verifier. This is a different author
verification representation, NOT an independent reviewer. See the complete
canonical and REPLAY_LOG.md for actual two-process and byte comparisons.
No manuscript, formal paper ID, accepted gate, or external action is created
by this packet. The algebra scout is a proof contributor and cannot review
an eventual EC manuscript.
