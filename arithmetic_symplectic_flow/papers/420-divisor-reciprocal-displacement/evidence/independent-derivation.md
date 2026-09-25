# 420 — card-only independent derivation

Candidate: `ANG-20260923-DRD01`.
Result: all four actual Borel owners and all-point clocks are admitted. MAIN has TWO
distinct fixed packets of primitive `log 2`, violating the necessary multiplicity bound.
Decision: **STOP / FORK**. The prescribed two-step words supply no additional cycle.

## 1. Exact input and access boundary

Sole scientific input: original `candidate-card.md`, lines 1–88 through EOF,
88 lines / 5,107 bytes, personally read at CP1 and reread after raw release.
Original SHA-256: `31ea137041ecd06bee01bbaa421251517285d7c28db722240a1d4145104da88e`.
Preserved `scope-review.md`: 81 lines, SHA-256
`c865ce87f173893ced76baadb3d41d045c3eefb072a266e4a3917d39c8dd659e`.
Root reported fully reading CP1 and separately released this derivation.
No manuscript, README, ledger, outcome appendix, author/peer answer, old scientific source
or external material was read. No auxiliary agent, scientific code, numerical experiment,
web or Git operation was used. Only this report is written at the raw stage.
Applicable ARS router and previously read workflow/DA/runtime guidance are retained.
Same-model shared history and disclosed design expectations remain; NOT_CALIBRATED,
not blinded, error-independent or external peer review. No previous theorem is imported.

## 2. Full sources, complete inverses and exact image tests

For each owner write `F(x,y)=(y,x+delta*y-a/x)` with its OWN card values and permission.
Every a is a positive integer. At a fixed cell/sign let `b=v-delta*u` and
`xi_sigma(b,a)=(b+sigma*sqrt(b^2+4a))/2`, for BOTH signs sigma.
The two roots are nonzero and have opposite signs, since their product is `-a`.
The inverse expression is `theta(u,v)=(xi_sigma(b,a),u)`.
Its actual domain consists exactly of the card's target y-cell condition, reconstructed
x-cell/sign, own arithmetic permission and forward checks. Necessity follows by multiplying
`b=x-a/x` by x; sufficiency follows by substitution with the reconstructed labels.
All signs, axes and half-open cuts are kept. A target need not itself be forward legal.

For clarity, the unrestricted integer atlas admits the following exact finite-per-target
implementation. This is a proved bound/rewriting, not an imposed numerical cutoff.
Set `m=floor u`, `d=|m|`. Define `Gamma_O(u,v)` by retaining the following roots and
returning the corresponding source `(xi,u)` whenever its stated tests pass:

- MAIN or D, d>0: use `a=1+d`; retain each sign iff `d` divides `floor xi`.
  Here MAIN uses `b=v-u`, D uses `b=v`. Permission forces `g=d`, including `floor xi=0`.
- MAIN or D, d=0: only `n=0` is permitted, so use `a=1` and retain the positive root
  iff `0<xi<1`. Equivalently `b<0`; the negative root never has the required source cell.
- C, d>0: use `a=1`, `b=v-u`; retain each sign iff `d` divides `floor xi`.
  For d=0 use the preceding `0<xi<1` condition with `b=v-u`.
- P, d>0: enumerate every positive divisor g of d, use `a=1+g`, `b=v-u`,
  and retain a root exactly when `gcd(|floor xi|,d)=g`.
- P, d=0: enumerate integer n satisfying `|n|<=|b|+4`, use `a=1+|n|`,
  and retain each root exactly when `floor xi=n`.

To prove the last bound, any actual source satisfies `a=1+|floor x|<=|x|+2`.
If `|x|>=1`, then `|b|=|x-a/x|>=|x|-a/|x|>=|x|-3`.
If `|x|<1` the same final bound `|x|<=|b|+3` is immediate.
Thus `|floor x|<=|b|+4` for every candidate. No possible preimage is omitted.
MAIN/C/D have at most two predecessors per target, and at most one when d=0.
P has at most twice the number of positive divisors of d when d>0 and finitely many
under the exact bound when d=0. The complete image is precisely `Gamma_O(w)!=empty`.
This finite radical-and-floor test is a full image description, not a test on selected targets.

Distinct labels cannot duplicate an actual reconstructed source: its floors and root sign
are unique. Different sources at a common target remain different incoming branches.
Each fixed-a/sign analytic inverse is injective: its output recovers u, then
`v=xi-a/xi+delta*u`. The actual restrictions are Borel; all four full partial maps are Borel.
There is no claim that the entire forward map is injective.

The d=0 convention and terminal incoming are substantive: `(1/2,0)` is legal for all four
owners and maps to `(0,-3/2)`. That target remains an object but its next step is forbidden
by x=0. It is not an absorbing fixed point, and no next-step clock is assigned to it.
P additionally retains sources disallowed by the arithmetic permission; the controls' domains
are not silently identified with MAIN's.

## 3. EVERY-Borel IMAGE and the frozen all-point clock

Implicit differentiation of `b=xi-a/xi` gives
`q_sigma=d xi/db=xi^2/(xi^2+a)=(1+sigma*b/sqrt(b^2+4a))/2`.
It is strictly between zero and one for every finite real b and every a>0.
The inverse derivative matrix is `[[-delta*q_sigma,q_sigma],[1,0]]`, so
`J_theta=q_sigma>0`. This is the prescribed labelled root-germ value even on floor cuts.
The root germ is a global analytic diffeomorphism from the target plane onto the source
half-plane of its sign, with inverse the fixed-a forward formula. Change of variables
therefore proves `mu(theta E)=integral_E J_theta dmu` for EVERY Borel actual-domain E,
including null boundaries and infinite integrals. No finite test or total-mass ratio substitutes for it.
Countably many fixed-label pieces cover the actual atlas; source-unique labels ensure
consistency at each source. Other incoming sources at the same target need not have the same J.
The a.e. density alone would not choose null-point values; the card's analytic prescription does.

At every legal source of each owner,
`j(z)=J_theta_z(Fz)=x^2/(x^2+a)`, and `kappa(z)=log(1+a/x^2)>0`.
The forward absolute branch Jacobian is `1+a/x^2`; its signed determinant is negative.
Delta changes the actual map and inverse domain but not this determinant formula.
For the terminal-incoming example above, j at that source is `1/5` and kappa is `log 5`.
Branchwise IMAGE is not a global invariant-measure claim for a many-to-one map.

## 4. Full retained histories, all kernels and conditional entire H

Fix an owner. On legal histories put `D_s(z)=product_{i<s}(1+a(F^i z)/x_i^2)`;
`D_0=1`, and `S_s=log D_s`. Each factor exceeds one, but no factor is appended after a terminal.
For actual triples define
`c(z,m-n,w)=log(D_m(z)/D_n(w))` when `F^m z=F^n w`.
Different witnesses for the same actual triple differ by common legal future padding.
The additional factors are on the same common tail and cancel. Aligning two witnessed
middle histories proves additivity without continuing through a terminal.
The forward arrow `(Fz,-1,z)` has `c=-kappa(z)`, as frozen.

Each finite inverse itinerary is injective on its own Borel domain. A branch-pair holonomy
from w to z has IMAGE `D_n(w)/D_m(z)=exp(-c)` by the real chain rule and iterated
change of variables, at every retained point. Countably many finite itinerary pieces give
the actual Borel groupoid and descended Borel cocycle. This is not a free history groupoid.

The FULL lag kernel is `{(z,0,w):F^s z=F^s w for some legal s}`.
The FULL clock kernel is the set of actual triples with `D_m(z)=D_n(w)`;
the joint kernel requires both a zero-lag witness and that product equality.
Equal-depth coalescence is possible; these kernels must not be reduced to identities by
confusing branch injectivity with global injectivity. Full-arrow kernels also differ from isotropy kernels.

All incoming arrows to any object r are obtained as follows: choose every legal forward m,
every nonnegative n, and every point w in `Gamma_O^n(F^m r)`; emit `(r,m-n,w)`.
Here `Gamma^0(A)=A` and each subsequent generation applies the finite explicit radical
tests in Section 2 to every preceding point. Deduplicate actual triples only.
This exact untruncated enumeration includes all terminals, all branches and every depth.

A nonzero isotropy lag exists exactly when the source eventually enters an actual cycle.
For a least-period-p core with `K=sum_cycle kappa`, the source isotropy at every point
in its entire incoming class is `p Z`, with `c(kp)=kK` and ENTIRE `H=K Z`.
Transient factors cancel. In this candidate K is strictly positive because every legal
step has positive kappa. Hence the positive primitive is exactly K, repetitions are kK,
and extension isotropy is trivial. A non-eventually-periodic history has trivial source
isotropy and H=0. Thus no owner has nontrivial zero-clock ISOTROPY, although nonidentity
zero-clock arrows between different objects can and do occur.
These are conditional all-source formulas, not a classification of untested cycles.

The extension retains all `X times R_h`; height translations commute with every actual arrow.
Over a source orbit its complete phase space is the torsor `R/H`, not a selected height.
Transporting to a reference object by any actual arrow supplies the phase; alternative
arrows change it precisely by the entire H. For the found classes, explicit complete
transport formulas appear in Section 6. No nice global quotient topology is inferred.

## 5. Complete fixed sets and exactly the two frozen two-step words

A fixed state requires `x=y=t!=0`. The remaining equation is `delta*t^2=a`.
For MAIN/P, diagonal floors n=m=k give `a=1+|k|` and automatic MAIN permission.
For C, a=1; for D, delta=0 and a>0 exclude fixed states.
The complete six-cell results are:

| Floor cell | MAIN | P | C | D |
| --- | --- | --- | --- | --- |
| (-2,-2) | `{(-sqrt(3),-sqrt(3))}` | same geometric point | empty | empty |
| (-1,-1) | empty | empty | `{(-1,-1)}` | empty |
| (0,0) | empty | empty | empty | empty |
| (1,1) | `{(sqrt(2),sqrt(2))}` | same geometric point | `{(1,1)}` | empty |
| (2,2) | empty | empty | empty | empty |
| (4,2) | empty | empty | empty | empty |

The MAIN/P diagonal equations successively use a=3,2,1,2,3; both square-root signs are
tested in every case. In the (-1,-1) cell, -sqrt(2) is below the lower edge; in (0,0),
the possible +1 is the excluded upper edge; in (2,2), sqrt(3) is below the lower edge.
For C, -1 and +1 lie on included LOWER edges of their displayed cells; they are excluded
from the adjacent earlier cells. The (4,2) rectangle cannot have x=y. The pole t=0 never enters.
Every admitted fixed core has actual least source period one and `kappa=log 2`.

Now consider only the ordered word ((4,2),(2,4)) and its rotation, each owner separately.
At the first (4,2) cell, x is in [4,5), y in [2,3); permission holds and g=2.
For MAIN/P the second output coordinate is `x+y-3/x>=21/4>5`, so the first image
cannot lie in the required (2,4) cell. For C it is `x+y-1/x>=23/4>5`, with the same exclusion.
For D, the first image DOES lie in (2,4) precisely when
`2+sqrt(7)<=x<5`, `2<=y<3`. The lower edge solves `x-3/x=4`; the upper output is below 5.
But every point of (2,4) fails arithmetic permission, since 4 does not divide 2.
Thus this legal D first leg terminates before the required second leg and is not a cycle.

For the rotation starting in (2,4), MAIN/C/D are illegal immediately. P is legal, with
a=3, but `x+y-3/x>=9/2>3`, so its image cannot lie in (4,2).
There are NO admitted two-step returns in either frozen word for any owner, hence
no period-one repeat to relabel as primitive two. No other word has been tested.

## 6. Complete incoming, phases and packets of every found core

Write `a_-=(-sqrt(3),-sqrt(3))`, `a_+=(sqrt(2),sqrt(2))` for MAIN/P,
and `c_-=(-1,-1)`, `c_+=(1,1)` for C. Let `L=log 2`.
For each owner and each of its found cores r, the EXACT entire source orbit is
`B_O(r)=union_{s>=0} Gamma_O^s({r})`, using the explicit tests in Section 2.
Every generation is finite; the union retains ALL depths, not a truncation.
Necessity follows because a tail relation to a fixed r must eventually equal r;
sufficiency follows from the displayed legal inverse history. This is a complete radical
parameterization of all incoming points, including those outside the tested cells.
For P/C no finite-depth closure or finite-cardinality claim is substituted for this union.

MAIN admits a stronger exact closure. At a_-, m=-2 forces a=3 and inverse roots
`+sqrt(3),-sqrt(3)`; only the negative root has floor divisible by 2.
Thus `Gamma_M(a_-)={a_-}` and `B_M(a_-)={a_-}`.
At a_+, m=1 gives both signs of sqrt(2), so
`Gamma_M(a_+)={a_+,q}`, where `q=(-sqrt(2),sqrt(2))`.
To invert q, m=-2 forces a=3, b=2sqrt(2), and the only roots are
`sqrt(2)+sqrt(5)` in (3,4) and `sqrt(2)-sqrt(5)` in (-1,0).
Both have odd floors and fail divisibility by 2. Hence `Gamma_M(q)=empty` and
`B_M(a_+)={a_+,q}`. These statements concern full inverse domains, not the six-cell restriction.
The bounds follow from `1<sqrt(2)<3/2`, `2<sqrt(5)<5/2`, and `sqrt(5)<1+sqrt(2)`.

The changed controls must retain their different incoming. For example
`Gamma_P(a_-)={a_-,(sqrt(2),-sqrt(3))}`, while
`Gamma_P(a_+)={a_+,q}` and `Gamma_P(q)={(sqrt(2)+2,-sqrt(2)),(sqrt(2)-2,-sqrt(2))}`.
These follow by separately testing g=1 and g=2; MAIN's finite closure is not transferred to P.
For C, `Gamma_C(c_-)={c_-,(1,-1)}` and `Gamma_C(c_+)={c_+,(-1,1)}`.
All later P/C generations are specified by the same complete finite radical rules, without pruning.

For ANY point z of any B_O(r), let `R_z=min{s:F^s z=r}` and
`A_z=S_{R_z}(z)`, `E_z=A_z-R_z L`. These are finite, own-clock, first-hit quantities.
Padding histories at the fixed core shows that every pair z,w in this class supports
EVERY integer lag k, and the full arrow formula is
`c(z,k,w)=E_z-E_w+kL`.
Therefore the full lag kernel on this class imposes k=0, the full clock kernel imposes
`E_z-E_w+kL=0`, and their intersection imposes k=0 and `E_z=E_w`.
At each object the source isotropy is Z, its entire image is `L Z`, and extension isotropy is trivial.
An incoming ancestor need not itself be F-periodic; its groupoid isotropy still has this entire image.
The COMPLETE height phase is `h-E_z mod L`, equivalently `h-A_z mod L`.
Equality of these phases is also sufficient for an extension arrow, by the formula for c.

In both MAIN classes E is identically zero: at q, a=2 and x^2=2 give kappa=L,
so its first-hit A=L and R=1. Hence MAIN's full clock kernel on each found class equals
its zero-lag pair relation. On the two-object class this includes nonidentity arrows;
source/extension isotropy must not be confused with this full-arrow kernel.
For P/C the general E formula retains all transient clock contributions, without assuming they vanish.

Different fixed cores of one owner have disjoint entire source orbits: an object cannot
eventually hit two different fixed values, and any tail relation between the basins would
force those fixed values equal. Thus MAIN has EXACTLY TWO found packets of primitive log 2,
as do P and C separately. D has no discovered core. Each packet retains its entire phase
torsor `R/(log 2)Z`; selecting one height or merging equal times is not permitted.

## 7. Gate decision and scope limits

MAIN demonstrates positive nonemptiness, and its found primitive times are ordinary-prime
times. Nevertheless two genuinely different full packets have the same prime-2 time.
This violates the frozen at-most-one-packet-per-prime condition on MAIN itself: STOP / FORK.
No control failure, putative two-step return, numerical approximation or incomplete loop
was used to decide MAIN. Enlarging the census cannot remove the existing duplicate.

On the stated integer seeds the real floors are exactly the input integers and r=0 iff d divides n;
the gcd coefficient then enters the actual update. This verifies the interface, not a strong
naturalness theorem. The designed gate/coefficient, arithmetic T1 and PROVES_TOO_MUCH questions
are not promoted; arithmetic T1 remains NOT PASSED as frozen.
Other cells, other two-step words, higher cycles, global prime-only support and all-prime coverage
remain unclassified. General groupoid formulas above are not an exhaustive periodic census.
Same-object source/measure/version integrity is retained. T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; Route B NOT INVOKED. No owner, measure or null-point repair is proposed.
This raw report freezes before manuscript access; HOLD for a separate PAPER UNLOCK and CP2/CP3.
