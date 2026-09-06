# P207 manuscript A — original proof and source audit

2026-09-06 UTC. Reviewer `/root/batch197_lzk_gate`, not a mathematical
author of P207. Input is the physical `frozen_round0` manuscript, not an
outline or a recovery summary. Root and `/root/batch197_fosp_gate` are
contributors. I previously assessed this candidate and its outline and
reviewed the shared lower-rank inverse proof; that familiarity is explicit.
I supplied no new author lemma or manuscript proof. This is configured-model
process separation, not blind review, human attestation, external review or
a second independent candidate assessor.

## 1. Local certificate and its all-length deduction

The literal carrier is `{0,1,2}^n`, with labelled positions, n >= 3,
two distinct cyclic neighbors, strict comparisons and synchronous updates.
For U, a strict minimum becomes two while each neighbor becomes at most
one; a strict maximum becomes zero while each neighbor becomes at least
one. Hence E(x) is increasing and its sites alternate permanently, with
heights zero/two after the first update. No energy analogy is needed.

Lemma 2.2 has the correct finite domain. Starting with indices -6,...,6,
the time-s row has indices -6+s,...,6-s. A strict extremum at time s
must therefore have |j| <= 5-s. Its original non-extremum test uses the
same j and both time-zero neighbors. The displayed program covers all
177,147 inner words; equality of the two centers uses only their inner
cones, and an inner witness has the stronger |j| <= 4-s domain.
The canonical retains the other 204 words and every one of their nine
extensions. The three classes 158,643 / 18,300 / 204 are exhaustive, not
a sample or a claim that the outer letters are always irrelevant.

For this manuscript review I wrote and executed a new Python producer
that directly enumerates all 1,594,323 thirteen-height words. It uses
literal height inequalities, no 11-word partition or sign-based evolution.
All 166,536 unequal-center cases have a new-extremum witness in the
claimed domain; the other 1,427,787 have equal centers. Separately,
`audit_artifacts.py` actually reads the full author's canonical and
recomputes its entire inner partition and all 1,836 stored witnesses.
No author program is executed or imported by either check.

The all-n passage is deductive: reading thirteen coordinates cyclically
produces an admissible word even when n < 13 and coordinates repeat.
Locality identifies each computed cone entry with the cyclic trajectory.
If E(U^4 a) = E(a), monotonicity forbids a new extremum at any intermediate
time, so the finite lemma forces U^4 a = U^2 a coordinatewise. Among
the n+1 inclusions between E(U^(4q)x), q = 0,...,n+1, one is equality,
with q <= n. The resulting entrance time is 4q+2 <= 4n+2; forward
invariance of Fix(U^2) gives the stated uniform iterate identity.
The manuscript correctly calls this bound nonsharp and computer-assisted.

## 2. Exact core, labels, determinant and seed boundaries

Theorem 2.4 is separate from the finite growth lemma. In a two-time
solution y = Ux, x = Uy, height two forces height zero in the other time.
The possible columns are the five displayed types plus (0,0). A (0,0)
column forces both neighboring columns to be (0,0), then connectedness
forces the all-zero solution.

In a nonzero solution, a neutral (1,1) column needs one height-two
neighbor at each time. These are distinct opposite strong columns.
This rules out a neutral next to a weak column using the neutral site's
own equation. A weak column then has exactly one same-phase weak neighbor
and one opposite-phase strong/weak neighbor; the weak components are unique
dimers. Strong columns have the stated opposite-phase or neutral neighbors.
Substitution in both time equations proves sufficiency. In the emitted
word this is precisely zero runs of length one/two and positive runs
2, 11, 12, 21, 121, with a singleton zero on each neutral side. No zero-free
core is omitted: every U-image has a zero at a source maximum. Only zero
is fixed, because two always maps to zero and, once twos are excluded,
ones map to zero as well.

Each eight-role closed walk emits one nonzero labelled word, and the
proved word language recovers each role, dimer end and neutral orientation
uniquely. Thus no factor n, rotation quotient, or dimer multiplicity is
missing in Proposition 3.1. The phase flip preserves transitions and is
literal U. Eliminating the deterministic intermediate roles has unit
diagonal determinant and yields the displayed two-phase block transfer.
Its determinant is `(1+z^4)^2-(z+2*z^2)^2`, exactly D(z).

The independent producer instead constructs the graph on all four-height
words abcd, with abcd -> bcde precisely when
`u(u(a,b,c),u(b,c,d),u(c,d,e)) = c`.
It has 81 vertices and 137 edges. A labelled closed overlap walk recovers
the cyclic word, including consistent short-period repetitions. Exact
integer Newton identities through the full degree 81 give
`det(I-zR) = (1-z)*D(z)`; all 72 coefficients after degree nine vanish.
This is not a fit to eight initial terms. All sixty author graph traces
were also compared with these independently computed traces. Finite graph
counting itself receives no separate contribution credit.

For Proposition 3.2, the seed's two fronts have disjoint exterior zeros
before meeting. The interior alternating sites, frontier ones, next outer
zeros and untouched zeros give all induction cases; the center alternates
by the permanent-extremum lemma. At the last step, the even cycle's single
remaining zero sees two frontier ones and becomes two. The odd cycle's
two remaining adjacent zeros become the weak 11 dimer. Both profiles lie
in the proved core. At every positive premeeting time a frontier one is
a strict maximum with second iterate two, so entrance has not occurred.
At time zero the zero run has length n-1 >= 3. The source 01^(n-1)
therefore enters exactly one step later, not just at most one step later.
For n=3 the complete equality/multiplicity split yields only 000,
rotations of 110/200 and permutations of 210 as first images, all core;
001 is a noncore witness. H(3)=1 follows. Witness-only n=4,...,64 checks
were kept distinct from full-carrier enumeration n=3,...,10.

## 3. Full decoder and all mixed-kernel inequalities

Equation (2) is U=FJ with Jx=2-x, not JFJ. Its inverse identity is the
full source-set bijection `U^(-1)(b)=J(F^(-1)(b))`; targets and counts
are unchanged. For F, each zero block has one recoverable source height,
and its boundary inequalities must hold even for singleton zero runs.
A positive source letter is nonzero; an interior one in a positive run
would output zero, so all interior letters are two. Length five would
contain three consecutive interior twos. The displayed source strings
therefore exhaust lengths one through four. Distinct strings under
overlapping table conditions are distinct sources, not multiplicities
assigned to one source. This yields all eight kernels exactly.

The cyclic reconstruction retains actual coordinate positions and recovers
all choices from a source. For one block the two outside heights coincide,
as the trace requires. The all-zero target has three sources and a target
without zero has none. These exceptional targets are not put through an
inapplicable nonempty-run trace.

For r factors, the paper's Schatten inequality has valid hypotheses and
exponents. The two-factor theorem in Schatten norm t gives
`||VW||_t <= ||V||_(pt) ||W||_(qt)`. At induction step s use
t=r/s >= 1, p=s/(s-1)>1 and q=s>1, so their reciprocal sum is one,
pt=r/(s-1), and qt=r. Finally `|tr P| <= ||P||_1` follows from the
SVD. Nothing assumes matrix commutation, invertibility or positive
semidefiniteness. Entrywise domination of the five non-A/J0/B0 word
kernels is used only in a nonnegative trace sum.

I checked all product cases, not just alternating products:

- A has positive nonzero eigenvalues lambda and lambda^(-1), and
  `a_r = (lambda^r+lambda^(-r))^(1/r)`.
- J0 has singular values 2,1,1; B0 has Frobenius norm three. Thus
  `||J0||_r <= sqrt(6) < lambda < a_r`, and for r >= 3 the stronger
  `3*cuberoot(10) < lambda^2 <= a_r^2` is valid. The displayed rational
  check follows from lambda > 13/5.
- With k=0, every J0 makes the Holder product strictly smaller than
  `a_r^r`. With k=1 and j=0 the leading 2-by-2 block gives exact equality
  `tr(B0*A^(r-1))=tr(A^r)` for r>=2. With k=1,j>0, r=2 is the explicit
  `tr(B0*J0)=4<7` case; for r>=3 one B0/J0 pair is combined in the
  scalar product of norm bounds, not by moving noncommuting matrices.
- With k>=2, `(a_r/lambda)^r < 10/9` works also when r=k.
  `(10/9)*3^k < lambda^(k+floor(k/2))` has bases 10<lambda^3 and
  30<lambda^4; advancing k by two multiplies the sides by nine and
  lambda^3>nine. This proves strictness for every k>=2.

The cost budget n>=2r+k then supplies the claimed even-index Lucas bound.
The r=0 and r=1 branches are strictly below L4 for n>=4 and give exactly
the seven n=3 attainers. Equality at larger n forces r>=2, k<=1 and
q=n-2r in {0,1}. At q=0 only A survives. At q=1 the extra position is
either a doubled zero or one length-two positive run. The latter is
B0, D0 or D0^T; every J0 is strict and the D0 alternatives are strictly
smaller even with all other factors A, since the leading 2-by-2 block
of A^(r-1) is positive. No length-three positive run fits this budget.
The unique doubled run eliminates nontrivial rotational stabilizers,
and the presence of symbol one distinguishes the two odd families.
Thus the equality list is exhaustive, not merely an attainment list.

## 4. Literal subtraction and original sources

The following source conclusions are bounded comparisons, not global
priority clearance. Raw fresh query/open returns are preserved in
`sources/`. Three spelling/mechanism forms and a recent-six-month query
were run for each rank/temporal, threshold and fibre group. Irrelevant
hits and nonhits are not used as positive novelty evidence.

The saved primary Zabih–Woodfill PDF was read in full again in this
review, including Section 3's strict-lower rank and census definitions.
Reversing input order does not make the rank primitive original.
[Author-hosted original](https://www.cs.cornell.edu/~rdz/Papers/ZW-ECCV94.pdf).

Mukherjee's newly returned publisher preview defines rank by strictly
lower values and announces iterative convergence; its convergence theorem
and proof remain inaccessible. A direct open supplied no body. The paper
does not attribute a sharp theorem or an upper-rank extension to that
unread material. The example 0202 distinguishes U's displayed two-cycle
from F's fixed state; U=FJ is not itself a conjugacy. No complete alternate
encoding was established, and none is claimed impossible. The missing
body remains an access limitation, not a blanket blocker for all related
maps, and the separate directly matching LNR-S1 hold is unchanged.
[Publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0167865511000420).

The original internal TCSD contract and complete gap proof were reread.
Let D(x)_i=sign(x_(i+1)-x_i), and
`G(s)_i=[s_(i-1)=-1]+[s_i=+1]`. Then U=GD, and the **entire** labelled
inverse is the disjoint union of D-fibres over all s with G(s)=b.
Its source inverse leaves the original labels unchanged and recovers the
unique sign stratum from a source. TCSD evaluates every stratum: deleting
equality edges yields zero for infeasible strict skeletons, a Lucas value
for alternation, or a product of Fibonacci gap factors between doubled
runs. Thus the whole static source decoder, not just alternating counts,
is deducted. The independent producer recomputes this formula for every
sign word and checks the complete union source set for every target in
the declared full boxes.

The old TCSD maximum is a maximum of a *single* sign fibre. It does not
give the new maximum merely because the final Lucas values agree. For
b=0101 at n=4, the two feasible strata (-,0,0,+) and (0,+,-,0) have
three sources each, and the whole fibre has six. Their complete source
lists are in the independent canonical. The old gap-merging proof compares
one product; it provides no all-target inequality for this sum or the
rank-target equality cases. A full union-bound adapter would reopen the
retained residual, but the inspected old proof is not one.

The alternating and both odd attainer source sets are fully classical:
marked height-one sites form an independent set of the labelled alternating
cycle, with inverse heights zero/one on valleys and one/two on peaks.
Doubling the appropriate valley or peak and deleting that repeated position
give both odd families. In the doubled-peak case boundary valleys are
zero/one, so the only strings are 11/22, not 12/21. These are complete
source-set bijections with zero new counting credit. Currie–Visentin's
primary publisher page confirms earlier fence/crown order-map enumeration
and June 1991 metadata; its body was not read or assigned an unseen theorem.
[Publisher source](https://link.springer.com/article/10.1007/BF00383399).

For the standard inequality I reread Tropp's saved primary notes,
Definition 6.15, Example 6.18 and Theorem 6.32 with surrounding proof
context on printed pp.49–53. These establish exactly the UI/Schatten
norm hypotheses used above. No new inequality credit is claimed.
[Author-hosted notes](https://www.tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf).

Goles–Olivos's actual primary abstract covers symmetric binary threshold
maps with period at most two. The 1981 multithreshold body remains
unavailable. I also reread the actual binary state space, linear neighbor
sum and explicit tie convention in Goles et al.'s version-pinned 2023
primary Sections 1–2. Those are not automatically this ternary comparison
count. Even the obvious equal-neighbor-weight scalar representation fails:
triples (0,1,2) and (1,1,1) have the same center and neighbor sum but U
values one and zero. This excludes only that representation, not arbitrary
lifts; no full threshold adapter was obtained. A shared period-two
conclusion alone earns no new generic-mechanism credit.
[1980 primary abstract](https://www.sciencedirect.com/science/article/pii/0012365X80901211),
[2023 primary model](https://arxiv.org/html/2309.01854v1).

## 5. Residual and disposition

After these deductions, the P207 conjunction retains its specific exact
temporal/core theorem, explicit nonsharp local-certificate clock and exact
seed, together with the once-counted rank-family whole-target extremal
comparison and every equality case. Core traces, static inversion,
independent-set counts, input complement, generic finite-set termination
and Holder are not separate axes. This narrow conjunction survives the
inspected adapters; no all-time inverse, basin theorem, larger alphabet,
sharp global clock for n>=4, or global novelty claim is admitted.

No open mathematical, source-applicability, execution or value blocker was
found in this initial manuscript A. This supports a no-change response;
an accepted delta still requires root's exact response and this reviewer's
separate after-pin check. Historical author/gate failures and the rejected
preclosure source-HOLD draft remain intact in their original packages.
`OWNER_AMBER / HOLD_EXTERNAL` remains throughout.
