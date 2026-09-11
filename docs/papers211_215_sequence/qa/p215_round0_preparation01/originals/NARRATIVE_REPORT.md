# P215 narrative report — deductive results, no numerical results

The standard drawdown vector becomes a finite dynamical system when its
entire output replaces its input. On X={0,...,q}^n, this iteration always
terminates at zero, but a prefix-length bound misses the statewise answer.
The exact answer is the number of sign runs after zero differences of
(0,x) are discarded and consecutive equal signs are compressed.
The number of runs, not the number of sign changes alone, is the depth.

The identity y_i=max(y_(i-1)-(x_i-x_(i-1)),0) explains why: the first
positive run disappears, every negative input run supplies a positive
output run, and each later positive input run supplies a nonempty negative
one before any saturation. Plateaus are neutral. The maximum depth is n
for positive n,q, attained exactly by strict alternating differences.

The inverse mechanism is independent of orbit enumeration. A positive
target value forbids a new source prefix maximum. Thus each zero-started
target block has a constant source record height L_j, with nondecreasing heights
and explicit block lower barriers. The formula x_i=L_j-y_i reconstructs
every source uniquely. Reverse-complementing the heights gives the
classical upper-barrier enumeration problem. A first-violation decomposition
evaluates it by a finite binomial recurrence. Zero has the unique largest
fibre binom(q+n,n), and the image consists exactly of targets starting at zero.

The classical drawdown statistic, barrier counting, multiset counting and
generic finite-map terminology are deducted. The admitted scope is this
exact autonomous clock and rule-specific inverse reconstruction. Bounded
source/collision work does not establish global priority or absence of
every possible factor. The separate interval-hull-complement scout is not
part of this manuscript or verifier.

The fixed 24 verifier cases are 0<=n<=5, 0<=q<=3. Their prospective total
is 6+63+364+1365=1798 states, by finite geometric sums for q=0,1,2,3.
This calculation is a parameter expectation, not observed coverage.
The draft and verifier are SOURCE only; no run, canonical, replay, build
or manuscript-review result is supplied.
