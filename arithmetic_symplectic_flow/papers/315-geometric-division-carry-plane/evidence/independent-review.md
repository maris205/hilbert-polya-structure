# Internal three-checkpoint review — geometric division/addition carry

Candidate: `ANG-20260920-GAC01`.
Status reviewed: `OWNED CARRY CLOCK; ALL-INTEGER PRIMITIVE LEDGER — STOP / FORK`.
Verdict: the bounded owner, full main return classification and specified
control results are supported. No manuscript correction is requested.
Calibration: `NOT_CALIBRATED`. This is internal inherited-model/shared-history
AI scrutiny, not external peer review, cross-model verification or evidence
of independent errors.

## 1. Exact inputs, scope and actual access order

| Input | Actual read | Measured SHA-256 |
| --- | --- | --- |
| [Original card](../candidate-card.md) | Complete original 180 lines, before any other 315 research file | `c9184fc0e8062f01800716d82b76ee012c13bf7d0bad2aba0a2d68f88612bbba` |
| [Final manuscript](../paper.md) | Complete 390 lines after the full raw submission and explicit unlock | `56414b8d7e1e209cae77c2e28dd04c12b7a2bb247ce1eb87f8014f26cfa70fd3` |

The card contained exactly its original 180 lines when first read.
Its frozen prefix was checked again with `head -n 180` and SHA-256;
no appended outcome was read as research input. The manuscript hash was
measured before the full read and checked again before this report.
No other 315 file, scout, historical proof or peer calculation was read.
No auxiliary agent was delegated or used in this round.

The previously read, unchanged ARS router, deep-research workflow, DA role,
runtime policy and required reasoning references governed the three bounded
checkpoints. No venue standard or compulsory issue quota was invented.

1. **Checkpoint 1:** read only the original card, independently derive the
   main owner, all returns/basins and all three controls, then send the
   complete raw results before manuscript access.
2. **Checkpoint 2:** after explicit unlock, measure the final manuscript
   hash and read all 390 lines; compare its proofs and all-point/sign
   conventions with the raw conclusions.
3. **Checkpoint 3:** test the strongest counterarguments about null-grid
   clocks, primitive versus repeated times, full predecessor multiplicity,
   lattice restriction, controls and claim scope. No unresolved correction
   was found.

The author reports that the initial 384-line draft, hash
`371029b2c48d45d66b809c842096088b904bbb3fe9814d1ba15ad06bcf213f62`,
was completed before receipt of this reviewer's first raw message. That
version was NOT read by this reviewer; its timing/hash are author-disclosed
provenance, not an independently inspected draft lock.
After the complete raw submission, the author adopted the reviewer's
CARRY-OFF fixed-basin observation and supplied a separate inverse-lattice
reflection and integer-update proof in the final 390-line manuscript.
Accordingly the final draft was influenced by raw review input and is
not claimed draft-blind. The raw derivation itself preceded manuscript access.
Extensive inherited context and a shared model remain limitations even
where local proofs were developed separately.

## 2. Checkpoint 1 — full source, inverse and IMAGE

For x=A+r, y=B+s and A=m*q+j, m=B+1, the formula
is `T=(B+s,B+q+s+r/m)`. Since `0<=s+r/m<2`, the
stated carry epsilon is 0 or 1 and the next floor/fraction
readout follows, including exact wrap boundaries. The map is total on
the complete nonnegative plane; no terminal or negative-coordinate convention
is being supplied implicitly.

At target (u,v), B=floor(u) and m=B+1 are forced. A
predecessor exists exactly when

    delta=v-u>=0, fractional_part(delta)<1/m.

Then q=floor(delta) is unique and all m predecessors are
`(m*delta+j,u)`, j=0,...,m-1. Solving for r proves necessity
and sufficiency, and different j give distinct actual points. The
strict upper boundary is essential. Thus the stated full image and
finite multiplicity are exact, not a selected branch or presumed surjectivity.

The map is Borel but not ordinarily continuous. For example at
y=1 the limit as x approaches 1 from below differs from
T(1,1). Finite/countable branch data do not imply an étale owner
or any Hausdorff quotient result.

Each inverse matrix is `[[-m,m],[1,0]]`, with absolute determinant m.
For every Borel subset of its actual domain, affine substitution gives
the IMAGE factor m. This is not the predecessor count being used
as a measure law, although the two numbers happen to agree.
The frozen full-point branch version gives `kappa=-log m`, including
axes and grid cuts. Almost-everywhere uniqueness alone does not determine
these values on null states.

For a finite forward branch, the absolute determinant is 1/P_k.
Thus an actual arrow from w to z has

    J=P_k(z)/P_l(w),
    c=-log P_k(z)+log P_l(w).

Common extensions of two presentations append identical future factors;
they cancel pointwise. Aligning the middle histories proves composition.
Actual finite branch pairs, not arbitrary affine maps or free histories,
cover the full retained-lag Borel groupoid. The forward-step arrow has
lag -1 and adds `-kappa=log m` to height. No positive roof
has been inferred from a negative local inverse-arrow clock.

## 3. Checkpoint 1 — all main returns and full packet ledger

The second coordinate satisfies `y_next-y=q+r/m>=0`. Any source
cycle forces every such increment to vanish, and x_next=y then forces
a constant diagonal point. On that diagonal the fixed equation forces
the fractional part to vanish. Therefore every periodic point is exactly
`f_n=(n,n)`, n>=0, with least source period one.

Integer states are invariant. Conversely T(x,y) being an integer pair
forces y=B integer and then r/m integer; its range [0,1)
forces r=0. Thus the whole integer lattice is inverse-reflecting too.
For an integer pair (A,B), set `n=B+floor(A/(B+1))`. Direct
iteration gives `(A,B)->(B,n)->(n,n)`. Hence the complete eventual
periodic locus is the integer lattice, not a selected recurrent subsystem.
No noninteger point can arrive in it after finitely many steps.
No assertion about convergence or growth of noninteger histories is needed.

The full basin of f_n is precisely

    B_n={((B+1)*(n-B)+j,B): 0<=B<=n, 0<=j<=B}.

It has `(n+1)*(n+2)/2` states and includes every depth-zero,
one and two predecessor. Inverse reflection excludes all additional real
tails. Distinct fixed cores have no common future, so their basins
cannot be merged by actual arrows.

Every state in B_n has source isotropy Z; every noninteger state
has trivial source isotropy. For z in B_n write d(z) for
its first entry depth and K(z) for its prefix kappa sum.
All integer lags between two points of B_n are realized by
extending their histories inside the fixed core. The exact clock is

    c(z,ell,w)=K(z)-K(w)
              -(ell-d(z)+d(w))*log(n+1).

This verifies the manuscript's signs and entry-depth terms. Its complete
time/extension classification follows:

* n>=1: H=`log(n+1) Z`, with trivial extension fixed-object isotropy;
* origin: H=0, but source and extension isotropy remain Z;
* noninteger states: source isotropy, H and extension isotropy are trivial.

The core-height phase is `h-K(z)` modulo `log(n+1)` when
n>=1. It gives one packet for the WHOLE basin, not one
per finite predecessor. The origin has a free real phase with
residual source/extension isotropy Z. Distinct n cannot merge through time
translation because no source arrow connects their basins.
The phase circle here means the abstract `R/log(n+1)Z` model;
no ambient embedded-circle or quotient-topology theorem is being asserted.

Consequently the global positive primitive ledger is one packet for each
integer N>=2, of least time log N. In particular f_3 has
entire H=`log 4 Z`, not a group containing log 2. Its
packet is distinct from f_1's log 2 packet. Numerical equality
`log 4=2 log 2` does not identify a primitive with a
repeat belonging to a different packet.
The decisive failure is the EXTRA composite primitive ledger. Each prime
time itself still occurs once; the main result is not a failure
of finite multiplicity or multiple same-prime cores.

## 4. Checkpoint 1 — independently checked controls

**UNIT-DIVISOR.** The exact image is `0<=u<=v`; the unique
inverse `(v-u,u)` has J=1 on all its actual domain, including
its boundaries. Thus the whole clock is zero. Its own order
test gives only the origin as a periodic point, and the unique
origin preimage is itself. There are no other eventual periods.
At origin source/extension isotropy is Z with H=0; elsewhere all
three groups are trivial. Source recurrence at origin has not vanished
merely because its clock is zero.

**SHEAR-OFF.** Its own exact image is u,v>=0 with
`fractional_part(v)<1/(floor(u)+1)`. The m inverses `(m*v+j,u)`
on the stated half-open domains are exhaustive and have J=m.
Its local kappa therefore equals -log m, but its source/returns
are not thereby identified with the main owner.

All fixed states are `(t,t)`, 0<=t<1. On the whole unit
square the map is the swap and its inverse is uniquely the
same swap, with no outside predecessor. The complete tail classes there
are unordered pairs of coordinates; their extension classes also require
equal height. Diagonal and off-diagonal source groups are Z and 2Z
respectively, H=0, and extension isotropy equals the source group.

On the full axes, `(t,0)<->(0,t)` for each t>0 has
least source period two. With M=floor(t)+1 its two increments
sum to `-log M`. Therefore H=`log M Z`; when t>=1
the extension kernel is trivial and the primitive time is log M.
When 0<t<1, H=0 and the extension group is 2Z. Origin
has source/extension Z and H=0, consistently with the unit square.

All finite predecessors of an axial cycle remain in the union of
its actual inverse iterates. Directly, `(t,0)` has predecessors `(j,t)`
for j=0,...,floor(t), whereas `(0,t)` has only `(t,0)`.
Deeper predecessors are enumerated with the complete inverse rule, not
discarded or replaced by a selected cross-section. Finite prefixes cancel
in loop times; choosing any actual hit of `(t,0)` gives its
phase by subtracting that prefix sum modulo H. Distinct t give
disjoint actual cycles and cannot tail-merge. Thus each interval
`t in [n,n+1)`, n>=1, gives continuum many distinct primitive
axis packets of time log(n+1). This is a tested control
family, not the complete higher-cycle ledger outside the square/axes.

**CARRY-OFF.** Write u=B+s and v=C+t with s,t in [0,1).
Its exact image is `C>=B` and `fractional_part(t-s)<1/(B+1)`.
Then q=C-B is unique, epsilon is 0 for t>=s and 1
otherwise, and all m values of j give distinct predecessors. The
half-open r condition excludes empty/duplicate epsilon domains. The image
can contain v<u; the main image cannot be reused. Each actual
inverse is affine with absolute determinant m and own kappa -log m.

All fixed states are `(n,n)`: fixedness forces r/(n+1) to be
an integer in [0,1), hence r=0. The positive and zero
fixed-core isotropy/time groups are those stated in the manuscript.
Separately in this control, an integer output forces s=0 and r=0;
its own integer update is `(A,B)->(B,B+floor(A/(B+1)))`.
These facts independently prove its complete fixed-core triangular basins.
This was included in the raw submission and then incorporated into the
final manuscript with the author's separate proof; it is not a borrowed
main groupoid theorem or an exclusion of other off-lattice control cycles.

On the full unit square, its exact map is the integer matrix
`M=[[0,1],[1,1]]` modulo one. The unique inverse remains in
that square, so no outside finite predecessor enters. Rational coordinate
pairs are periodic because M permutes each finite denominator grid.
Conversely `M^k-I` is an invertible rational matrix for every k>0,
so any periodic pair is rational. This proves all periods and
eventual periods there; the bijection creates no additional eventual ones.

The full square's tail classes are the two-sided M-orbits in the
literal half-open representatives. Their extension classes additionally require
equal height because kappa is zero throughout. A rational point of
least period P has source/extension group PZ and H=0. A
pair not both rational has all three groups trivial. The displayed
source 3-cycle has zero closed time, including its wrap point.
No topological torus substitution or classification of higher cycles outside
the square is needed or claimed.

## 5. Checkpoints 2/3 — final adverse assessment

The entire bound manuscript agrees with the raw owner and return
calculations. Equations (7), (12) and (14) have the correct IMAGE,
lag and phase directions. The added CARRY-OFF basin paragraph provides
the requisite own-source proof. No mathematical correction is requested.

The strongest limitation is real but already disclosed: every positive
main core lies on a Lebesgue-null integer grid. Its clock therefore
uses the explicitly frozen affine all-point version, not a uniqueness
claim derived from an almost-everywhere Radon–Nikodym class. Changing that
prescription would change the owner; the present audit neither silently
does so nor promotes it to a naturalness theorem.

The strongest proposed rescue of the prime-only target, reinterpreting a
composite primitive as a prime repeat or merging its finite basin with
a prime basin, is ruled out by the full groups and actual
tail identity. Conversely the negative result does not erase the owned
clock, genuine feedback or the one-per-prime part of the ledger.
The lattice was proved to be the entire eventual-return locus; it was
not imposed as a selected carrier. All noninteger states remain.

Control statements remain attached to their own sources. The SHEAR-OFF
axis continuum does not imply main prime-time multiplicity, and the
CARRY-OFF square's rational recurrence does not create positive square
times. Unexamined higher cycles of those controls stay UNCLASSIFIED.
No universal carry/divisor-geometry impossibility, trace, operator or spectral
claim follows. Historical lineage/priority records were not independently
reread; the directly checked interface is the current identity m|A iff j=0.

The final standing is **STOP / FORK** for the main prime-only
primitive target, with its positive ownership and complete all-integer
return theorem retained. Stronger naturalness remains OPEN; T3 is not
supplied/pursued. Classical A0/A1/A2 are not applicable, formal coordinates
are UNASSIGNED and Route B is NOT INVOKED.
Only this report was written; no other file, prior package or model
setting was changed. No external query, scientific numerical run or
auxiliary review was used.
