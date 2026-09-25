# Internal three-checkpoint review — integer-part/remainder matrix division

Candidate: `ANG-20260920-MRD01`.
Status reviewed: `OWNED MATRIX CLOCK; NONINTEGER-LOG FIXED PRIMITIVE — STOP / FORK`.
Verdict: the full owner, complete fixed-locus parameterizations and bounded
fixed-packet gate are supported. No manuscript correction is requested.
Calibration: `NOT_CALIBRATED`. This is inherited-model/shared-history internal
AI scrutiny, not external peer review, cross-model verification or evidence
of independent errors.

## 1. Exact inputs and actual three-checkpoint process

| Input | Actual access | Measured SHA-256 |
| --- | --- | --- |
| [Frozen card](../candidate-card.md) | Complete original 186 lines before any other 316 research file | `e12798b416c0109b50e96f18be02f7c74830e805a6136d5a432072e47bc863ea` |
| [Reviewed manuscript](../paper.md) | Complete final 398 lines after full raw submission and explicit unlock | `60935ac1a41f07313101198ac1a2e820b7492fb9505eabbd3b92e1c1a5e1dc0a` |

The card initially contained exactly those 186 lines. Its original prefix
was checked again with `head -n 186` and SHA-256; no appended
outcome was used as original evidence. The manuscript hash was measured
before the complete read and checked again before this report.

The previously read, unchanged ARS router, deep-research workflow, DA role,
runtime policy and required reasoning references supplied the bounded review
method. No venue calibration or issue quota was invented.

1. **Checkpoint 1:** read only the original card; independently derive the
   main inverse/IMAGE, complete fixed parameterization, full fixed-basin clock
   and all three control results. Send the complete raw findings before
   accessing the manuscript or any peer result.
2. **Checkpoint 2:** after explicit unlock, read all 398 manuscript lines
   and compare the formulas and proofs with those raw conclusions.
   Independently check the manuscript's explicit continuity example and
   four-direct-predecessor list; these were not presented as results of
   the earlier submitted raw checkpoint.
3. **Checkpoint 3:** challenge dimensional Jacobians, null-face ownership,
   completeness versus diagonal restriction, primitive/repetition identity,
   changed controls and higher-period scope. No unresolved correction resulted.

The author reports an initial 392-line draft with hash
`052d10600c706cf6d8f0e51c786e1e7efabb97dab51afdd6a3184fa2bb2445b0`,
completed before receipt of this reviewer's first raw message. That draft
was NOT read by this reviewer; its timing and hash are author-disclosed
provenance. After the complete raw submission, the author checked and
added this reviewer's legal singular-source example, producing the actually
read 398-line version. The final manuscript is therefore not claimed
unaffected by review input or draft-blind.

No auxiliary was delegated or used. No scout, other 316 file,
historical proof or peer calculation was read for this audit. Extensive
inherited history and the same model/runtime remain limitations of the
separate local derivation. No model override, external query, scientific
numerical run, coefficient census or higher-period campaign was performed.

## 2. Checkpoint 1 — exact source, image and four-volume clock

For every permitted integer A, solving `R X=A` gives

    R=A X^(-1), I_A(X)=A+A X^(-1),
    det X!=0, A X^(-1) in [0,1)^4.

Since A and X are invertible, det R is automatically nonzero.
The half-open remainder condition gives the actual floor A even when
its entries are negative. Substitution verifies both inverse identities;
every legal source yields precisely this branch. Distinct A give
different actual predecessors, not extra tags on one arrow.

For a fixed nonsingular target X, every admissible A has rows
of the form rX with r in [0,1)^2. In particular

    |A_ij| <= |X_1j|+|X_2j|.

Thus a finite integer box exhausts all possibilities, after which the
exact half-open and integer-admissibility tests decide the full predecessor
list. This proves finite-to-one ownership rather than assuming or imposing
a numerical cutoff. The exact image is the union of these actual
inverse domains. Singular targets have no incoming branch; for example
X=(1/2)I also shows that even nonsingular targets need not occur.

No incoming branch does NOT mean that a singular real matrix is
terminal. The raw counterexample adopted in the manuscript is

    A=[[-1,2],[-1,1]], R=[[1/2,0],[5/8,1/2]].

Here det A=1, the pivot -1 is permitted, det R=1/4
and floor(A+R)=A, while det(A+R)=0. Its forward step is
legal under the unchanged rule. All integer R=0 states and other
genuine permission failures remain terminal with T^0 but no added loop.

The derivative of the inverse, in the declared matrix order, is

    D I_A(X)[H]=-A X^(-1) H X^(-1).

On FOUR real coordinates, left and right multiplication contribute squared
2x2 determinants. The resulting density is

    J_A(X)=|det A|^2 / |det X|^4,
    kappa=2 log|det A|-4 log|det R|.

Analytic change of variables establishes IMAGE for every Borel subset
of the exact branch domain, including its null boundary subsets. The
positive analytic formula is the frozen all-point version, not a pointwise
consequence of almost-everywhere uniqueness or a count of predecessors.
It has no inverse-domain value at det X=0 and does not
continue a step through terminal det R=0.

Every legal increment is strictly positive: the nonzero integer determinant
has absolute value at least one, and a nonsingular remainder in
[0,1)^4 has determinant of absolute value strictly below one.
This is a proved local clock sign, not an inserted roof.
An actual forward arrow nevertheless has height increment -kappa, according
to the frozen source/range convention.

Actual finite branch pairs have `J=exp(K_l(w)-K_k(z))` and
`c=K_k(z)-K_l(w)`. For two presentations of the same triple,
the longer legal histories guarantee the common extension exists and
shared future terms cancel pointwise. The same alignment proves composition.
This is the full partial retained-lag Borel owner with countable fibres,
not arbitrary matrix transformations, free words or a germ quotient.
Analytic individual branches do not make the global floor map continuous
or étale; the manuscript's explicit discontinuity example is correct.

## 3. Checkpoint 1 — complete fixed parameterization

The fixed equation resolves as

    R(A+R)=A, (I-R)A=R^2,
    A_R=(I-R)^(-1)R^2, F_R=(I-R)^(-1)R.

Because R is invertible, I-R must be invertible; alternatively a left
null vector of I-R contradicts the displayed equation. Therefore ALL
fixed states are parametrized by the full four-entry R cube with
det R and det(I-R) nonzero, followed by the explicit test that
A_R is integer and belongs to the frozen admissible set.
Conversely each accepted R gives F_R=A_R+R, hence the correct floor,
remainder and legal fixed point. Different R give different F_R.

This eliminates the unknown fixed matrix; it is not a restatement of
T(M)=M and not a restriction to diagonal, symmetric or positive-definite
sources. Commutation is a consequence of the rational solution, not an
assumption on arbitrary source matrices. The raw equivalent formulas, with
tau=tr R, delta=det R and Delta=1-tau+delta, were

    A_R=((tau-delta)R-delta I)/Delta,
    F_R=(R-delta I)/Delta.

They agree with the manuscript by the 2x2 characteristic identity.
Neither representation claims a finite census of every admissible integer cell.

At every such core,

    det A_R=(det R)^2/Delta,
    J_(A_R)(F_R)=Delta^2,
    kappa(F_R)=-2 log|Delta|.

For R=[[a,b],[c,d]] in the remainder cube,
`Delta=(1-a)(1-d)-bc` lies strictly above -1 and at most
one. Equality to one would force a=d=0 and bc=0,
contradicting det R!=0. Excluding Delta=0 therefore gives
`0<|Delta|<1`. No zero-time fixed core is omitted: none exists.

## 4. Full fixed-tail packets and decisive witness

For a fixed F, its entire basin is the union of all
legal finite inverse histories reaching F. The exhaustive inverse rule
retains every predecessor at every depth, including any legal singular
source leaf. A closed-form list of each basin is not required
or asserted. In the main owner each level is finite and the
whole basin at most countable; repeated histories do not duplicate states.

Let d(z) be first entry depth, S(z) its kappa prefix sum,
and a=kappa(F)>0. All integer lags between two basin points
are realized by extending along the fixed core. The exact formula is

    c(z,ell,w)=S(z)-S(w)+(ell-d(z)+d(w))*a.

Every basin point has source isotropy Z, full time group aZ
and trivial extension fixed-object isotropy. Its complete height phase is
`h-S(z) modulo a`. This yields ONE primitive packet per fixed
core, not one per predecessor, inverse word or phase. The phase
circle is abstract R/aZ, not an embedded curve or a proved
Hausdorff coarse quotient. Distinct fixed matrices cannot have a common
future and never merge merely through equal spectrum, determinant or time.

Set phi=(1+sqrt5)/2, r=phi^(-1), R=rI and A=I.
Since r^2+r=1, F=phi I is an actual admissible fixed matrix.
Direct four-dimensional evaluation gives

    J_I(F)=phi^(-8), H_F=(8 log phi)Z.

Its least positive time is 8 log phi, whose exponential is
`(47+21 sqrt5)/2`, an irrational number. Thus this primitive is
not log N for any positive integer, in particular not log prime.
It cannot be another packet's repetition: its entire H and full-tail
class were determined, not merely a convenient loop or numerical length.

At checkpoint 2 the manuscript's four direct predecessors were verified:
the inverse condition at phi I forces A entries to be 0
or 1; A11=1 and det A!=0 leave exactly the four
listed matrices. Their predecessors are phi A and all satisfy the
permission. This finite list does not replace the complete deeper basin.
No multiplicity assertion about other fixed cores sharing this time is
needed for the decisive wrong-time gate.

## 5. Separately derived controls

**SCHUR-OFF / SCHUR-SHIFT.** Each uses its own integer list:
respectively the nonzero pivot/determinant conditions alone, or those conditions
and `A11|(det A+1)`. Signed divisibility and determinant -1 remain
included. Solving R X=A again gives that list's exact union
image and finite target enumeration; no equality with the main image
or retained basins is presumed. Its own four-dimensional derivative gives
the same algebraic Jacobian on its own domains.

For each control the full fixed solution is the rational R
parameterization above with that control's integer permission test. The same
explicit Delta bounds prove positivity on every accepted fixed core.
Its own finite histories and prefix sums determine its fixed-basin source
group Z, H=aZ, trivial kernel and phase. Both lists admit I,
so their OWN phi I fixed packet has primitive 8 log phi.
This is a direct control calculation, not transfer of the main orbit.

**INTEGER-DIVIDEND-OFF.** Its exact image is

    V_0={X:det X!=0, X^(-1) in [0,1)^4}.

For every target there, all main-admissible A give distinct predecessors
`A+X^(-1)` with actual floor A. There are countably infinitely
many, since A=diag(n,1), n>=1, already supplies an infinite family.
The main finite count and A X^(-1) inverse test are inapplicable.

Differentiating this inverse gives the own density `|det X|^(-4)`
and increment `-4 log|det R|>0`. The complete fixed equation
resolves as

    R in [0,1)^4, det R!=0,
    A_R^0=R^(-1)-R integer and main-admissible,
    F_R^0=R^(-1).

Necessity and sufficiency follow from F_R^0=A_R^0+R, including all
negative floor cells permitted by the tests. Every accepted core has
source Z, H=`(-4 log|det R|)Z` and trivial extension kernel.
All its countably branching finite predecessors remain in its own basin
and contribute phases of one packet, not additional primitive packets.

At R=rI the integer dividend computed from this new equation is
I and the own clock is again 8 log phi. Its direct
predecessors are ALL A+rI, not the four main predecessors. Equal
clock values at a shared matrix do not identify the changed owners.
All three controls have exact wrong-time fixed witnesses; their other
higher cycles remain UNCLASSIFIED.

## 6. Checkpoints 2/3 — strongest objections and final standing

The entire bound manuscript agrees with the submitted raw conclusions.
The legal singular-source example, the explicit discontinuity values,
the four-predecessor enumeration, the fourth-power determinant law and the
fixed-basin signs/phases were checked directly. No Critical, Major or Minor
manuscript correction is requested.

The strongest completeness challenge would be that the rational parameterization
silently chose a diagonal or commuting subsystem. It does not: its
necessity proof starts with every legal fixed point, excludes singular
I-R by contradiction, and only then derives commutation and the formula.
The diagonal witness decides the gate without replacing that full owner.

The strongest clock limitation is also explicit: the witness lies on
null off-diagonal cell faces, so its clock uses the frozen analytic
all-point version. Almost-everywhere measure data alone do not force that
version or establish stronger naturalness. This is not an unreported
defect in a contract that explicitly froze the version; changing it
would require a changed owner. No inverse value was extended to a
singular target, and no terminal was given a forward loop.

The strongest repetition/multiplicity rescue fails by the full isotropy and
tail argument. Extra finite predecessors do not create or remove the
fixed primitive; unrelated core labels, determinants and spectra cannot merge
it. The control witnesses show only that these three specified changes
do not remove their own wrong-time cores, not a universal impossibility
for matrix dynamics, divisibility mechanisms or all pointwise clocks.

The final standing is **STOP / FORK** for prime-time promotion.
Full fixed-locus and fixed-packet results are retained; higher main/control
periods are not globally classified. Stronger naturalness remains OPEN.
T3 is not supplied/pursued; classical A0/A1/A2 are not applicable,
formal coordinates are UNASSIGNED and Route B is NOT INVOKED.
Only this report was written. No author-owned file, old package or
runtime setting was changed, and no external or numerical campaign occurred.
