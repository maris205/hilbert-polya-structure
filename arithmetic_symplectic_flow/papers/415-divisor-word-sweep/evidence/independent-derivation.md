# 415 — card-only independent derivation

Candidate: `ANG-20260923-DWS01`.
Raw result: all four Borel owners and their prescribed clocks are admitted; the MAIN
fixed packet found in the frozen window has a nonprime primitive length. **STOP / FORK**.
This is an exact bounded obstruction, not a classification of higher cycles or other cells.

## 1. Inputs, stage and notation

Sole scientific input: `candidate-card.md`, original lines 1–90, personally read through EOF
at CP1 and reread after the separate mathematical release; 90 lines, 5,585 bytes.
Original SHA-256: `187e6326ebe494cc581ba1e556c81d8069d0e55d7b8022b464655260a59f7e03`.
CP1 `scope-review.md` is preserved: 84 lines, SHA-256
`7549fe8c9484e755d069569c90edaed58fa53d90f7e754dfe6f6010f2acd3404`.
Root reported reading CP1 completely before releasing this card-only derivation.
No manuscript, support surface, outcome appendix, author/peer answer, old scientific file
or external source was read. No auxiliary agent, scientific code, numerical experiment,
web or Git operation was used. This report alone is written in the raw stage.
ARS router/workflow/DA/runtime guidance is retained from the disclosed scope stage.
Shared model/history and the card's design-stage expectations prevent blindness or
error-independence claims. Internal review is NOT_CALIBRATED, not external peer review.

Write `A_N=dom C_N`, `B_N=dom R_N`, always with literal finite-step permission.
The divisor word is finite for each integer N, including its prescribed empty cases.
For any legal one-dimensional word W, write `d_W(t)=|W'(t)|` on its actual domain.
An empty word has full domain and derivative one.

## 2. Literal word inverses and all four complete sources

Put `b_d=2d^2+1`. Then `h_d(t)=d+b_d/(t-d)`, so
`h_d(t)-d=b_d/(t-d)`, `h_d(h_d(t))=t`, and
`h_d'(t)=-b_d/(t-d)^2` at every legal point.
Thus h_d is a bijection of `R\{d}` onto itself, with the same literal inverse.
Reversing a successful word reverses each of its legal finite intermediate states.
Consequently `C_N:A_N -> B_N` and `R_N:B_N -> A_N` are inverse bijections.
Their domains are open sets obtained by deleting finitely many forbidden preimages of poles;
their derivatives are the products of the displayed nonzero finite factor derivatives.
This proof never restores a missing intermediate state by rational cancellation.

All full two-dimensional domains and images now have exact permission tests:

| Owner | Forward domain and output | Entire inverse-domain test and inverse |
| --- | --- | --- |
| MAIN | `x in A_{N(y)}`; set `u=C_{N(y)}(x)`; require `y in A_{N(u)}`; output `(u,C_{N(u)}(y))` | Require `v in B_{N(u)}`; set `y=R_{N(u)}(v)`; require `u in B_{N(y)}`; inverse `(R_{N(y)}(u),y)` |
| U | `x in A_{N(y)}`; output `(C_{N(y)}(x),y)` | Require `u in B_{N(v)}`; inverse `(R_{N(v)}(u),v)` |
| V | `y in A_{N(x)}`; output `(x,C_{N(x)}(y))` | Require `v in B_{N(u)}`; inverse `(u,R_{N(u)}(v))` |
| R | `x in B_{N(y)}`; set `u=R_{N(y)}(x)`; require `y in B_{N(u)}`; output `(u,R_{N(u)}(y))` | Require `v in A_{N(u)}`; set `y=C_{N(u)}(v)`; require `u in A_{N(y)}`; inverse `(C_{N(y)}(u),y)` |

These tests include ALL signs and indices and all literal intermediate permissions.
Word inversion proves the reconstructed forward test automatically; retaining it is equivalent.
They are necessary as well as sufficient, because the final u first fixes the second word,
and its inverse recovers y before the first word is inverted.
Every target therefore has at most ONE actual predecessor for each owner, not a freely
chosen index-pair family. All four maps are Borel partial bijections of the full plane.
Terminals are their own domain complements and remain objects with their entire incoming.

For MAIN, the card's indexed inverse is exactly `(R_N(u),R_M(v))` with
`N(u)=M` and `N(R_M(v))=N`; these conditions make the apparent indices unique.
For R the analogous expressions use C instead of R. Nothing identifies R with MAIN inverse:
the order of the two coordinate sweeps in the macro inverse is itself reversed.

Forward terminals can be actual images. MAIN and U send `(3/2,-6)` to `(2,-6)`,
where their next horizontal literal word hits its first pole. V sends `(-6,3/2)`
to `(-6,2)`. R sends `(43/8,-6)` to `(3,-6)`, where its next first factor has a pole.
The second word in the stated two-sweep examples is empty. These are finite legal
incoming examples, not permissions to continue from the terminal or insert a self-step.

## 3. EVERY-Borel IMAGE and all-point macro clock

On a fixed MAIN inverse piece labelled N,M, the analytic expression is the product map
`theta(u,v)=(R_N(u),R_M(v))`. Its prescribed inverse Jacobian is
`J_M=d_{R_N}(u)d_{R_M}(v)>0`. For U it is `d_{R_{N(v)}}(u)`;
for V it is `d_{R_{N(u)}}(v)` on each fixed readout piece;
for R it is `d_{C_N}(u)d_{C_M}(v)` on its own reconstructed-label piece.
All derivatives are evaluated on literal domains, so every value is finite and positive.
Readout cuts select the fixed-label extension; the readout function is not differentiated.

Each word is a smooth injective map on its finitely punctured actual domain with smooth inverse.
The ordinary real change-of-variables formula on its components, and then on their products,
gives `mu(theta E)=integral_E J dmu` for EVERY Borel subset E of an actual inverse piece.
Restricting to the Borel floor/reconstruction conditions preserves the identity, including
null boundaries and infinite integrals. Countably many index pieces partition the entire
image; injectivity makes their reconstructed images disjoint, so countable additivity
also gives the complete inverse law with the piecewise J.
The unique actual labels give atlas consistency at every retained point.
The value at a null cut is the frozen analytic prescription, not a.e. uniqueness.

Let D_F denote the absolute forward macro Jacobian on its own fixed-label piece.
For MAIN, `D_M(x,y)=d_{C_{N(y)}}(x)d_{C_{N(u)}}(y)` with the actual u.
For R replace both C by R; U and V retain only their own factor.
The chain rule for the legal inverse gives `J_F(Fz)=1/D_F(z)` and
`kappa_F(z)=log D_F(z)`. Internal factors enter this derivative product,
not separate time steps. There is no globally assumed area invariance or positive roof.
At a terminal the next-step clock is undefined, while the empty history has clock zero.

## 4. Actual retained-lag groupoid, complete incoming and phases

Fix one owner F. All of the following use its own domains and D_F.
Let `D_m(z)=product_{i=0}^{m-1} D_F(F^i z)` on legal histories, with `D_0=1`.
Then `S_m=log D_m` and
`c(z,m-n,w)=log(D_m(z)/D_n(w))` whenever `F^m z=F^n w`.
Two witnesses for the same retained triple differ by common legal tail padding;
the extra derivative products cancel. Aligning two composable middle histories proves
additivity without crossing a terminal. A finite-itinerary holonomy `w -> z` has IMAGE
`D_n(w)/D_m(z)=exp(-c)`, by the same branchwise change of variables.
Countably many Borel history graphs give a Borel groupoid and Borel all-point cocycle.

Injectivity strengthens the description. Write `phi^j r` for legal forward iterates
if `j>=0` and legal iterates of the unique partial inverse if `j<0`.
Cancelling the common shorter iterate shows that EVERY incoming arrow to r is exactly
`(r,j,phi^j r)` for an allowed integer j, and every such arrow exists.
This supplies ALL incoming, including negative directions and finite terminal chains,
without a history completion or a free-word quotient. Allowed j form an integer interval;
on a cycle all integers occur, with different lags still different arrows.

Define `A_r(j)=S_j(r)` for nonnegative j and
`A_r(j)=-S_{-j}(phi^j r)` for negative j. Then `c(r,j,phi^j r)=A_r(j)`.
The FULL lag kernel is precisely the identity arrows, because equal-depth coalescence
of two objects is impossible under an injective iterate.
The FULL clock kernel is precisely the actual arrows above with `A_r(j)=0`;
its intersection with the lag kernel is again the identities.
This does not assert that the clock kernel consists only of isotropy.

The complete conditional isotropy ledger is as follows, without a higher-cycle census.
On an aperiodic orbit, source isotropy and H are zero, including all terminal chains.
If r belongs to a least macro-period-p cycle, put `K=S_p(r)`.
Its entire source isotropy is `p Z`, `c(kp)=kK`, and `H=K Z`.
There are no strictly preperiodic external ancestors of a cycle: a cycle predecessor
already occupies the unique inverse, so backward induction keeps all ancestors on it.
If `K!=0`, extension isotropy is trivial and the primitive time is `|K|`, with repetitions
`k|K|`; if `K=0`, the whole `p Z` remains ineffective extension isotropy and no positive time exists.

The extension is on ALL `X times R_h`. At `z=phi^j r`, its exact phase relative to r is
`h+A_r(j)` modulo H. Alternative j differ by an actual cycle and hence by H, so this
is well-defined. Height translation is complete on these orbit sets and has stabilizer H.
No smooth or Hausdorff global quotient is inferred. Equal time groups never merge source orbits.

## 5. Exact six-cell fixed classification for all four owners

Set `I_6=[-6,-5)`, `I_8=[-8,-7)`, `I_0=[0,1)`, `I_1=[1,2)`.
The four negative rectangles use `D_6=(2,3)` and `D_8=(2,4)`.
Direct composition, with its literal holes retained, gives

| Word | Rational expression on its literal domain | Excluded real inputs |
| --- | --- | --- |
| C_6 | `(16t-5)/(11-t)` | `2,11` |
| R_6 | `(11t+5)/(t+16)` | `3,-16` |
| C_8 | `(25t-14)/(13-2t)` | `2,13/2` |
| R_8 | `(13t+14)/(2t+25)` | `4,-25/2` |

For example the simplified value of C_6 at 2 does not restore its missing first h_2 step.
All four words are legal on both negative intervals. Their complete fixed equations are
`C_6(t)=t iff t^2+5t-5=0`, and `C_8(t)=t iff (t+7)(t-1)=0`.
Each root is legal for the associated word and its inverse; inverse words have the same fixed set.
Write `rho=(-5-3sqrt(5))/2`, `sigma=(-5+3sqrt(5))/2`.
Since `5<3sqrt(5)<7`, rho lies strictly in I_6, while sigma is positive.
Neither root is in I_8. Of the C_8 roots, -7 is the EXCLUDED right endpoint of I_8,
and 1 is positive; neither is in I_6 or I_8. No floor boundary is rounded or selected away.

A MAIN fixed point first requires `C_{N(y)}(x)=x`; its second word is then selected by
the actual u=x, and requires `C_{N(x)}(y)=y`. R has the identical fixed equations with
the inverse words. U requires only the first equation, V only the second.
This establishes the following COMPLETE sets in the frozen window:

| Rectangle | MAIN | U | V | R |
| --- | --- | --- | --- | --- |
| I_6 x I_6 | `{(rho,rho)}` | `{rho} x I_6` | `I_6 x {rho}` | `{(rho,rho)}` |
| I_6 x I_8 | empty | empty | empty | empty |
| I_8 x I_6 | empty | empty | empty | empty |
| I_8 x I_8 | empty | empty | empty | empty |
| I_0 x I_0 | entire rectangle | entire rectangle | entire rectangle | entire rectangle |
| I_1 x I_1 | entire rectangle | entire rectangle | entire rectangle | entire rectangle |

For the mixed rectangles, the relevant cross-interval root test already fails; in I_8 x I_8
the only negative word root is the excluded endpoint. The last two rows follow from the
specified empty words at BOTH actual readouts, with no intermediate pole at any retained boundary.
All listed fixed points have least SOURCE macro-period one, even when their clock is zero.
No other cell or higher period has been classified.

## 6. Entire fixed-core groups, incoming, phases and multiplicity

For ANY listed fixed point of ANY owner, its only direct predecessor is itself, by global
injectivity. Induction gives its full finite incoming basin as that singleton. A tail relation
to the fixed point also forces finite hitting, so its entire source orbit is the singleton.
Its arrows are exactly `(z,k,z)` for ALL integers k. There are no unexamined external ancestors.
Thus distinct listed points never merge through arbitrarily long histories.

At rho, differentiation of C_6 gives
`lambda=C_6'(rho)=171/(11-rho)^2=(9-sqrt(5))/(9+sqrt(5))`, strictly between zero and one.
Put `mu=1/lambda=(43+9sqrt(5))/38>1`; R_6'(rho)=mu by actual inversion.
The complete fixed-core ledger is therefore:

| Owner and fixed family | kappa and c(k) | Entire H / primitive length | Extension isotropy / phase |
| --- | --- | --- | --- |
| MAIN at `(rho,rho)` | `kappa=-2log mu`, `c(k)=-2k log mu` | `2log(mu) Z`; `L=2log mu` | `0`; `R/(2log(mu) Z)` |
| R at `(rho,rho)` | `kappa=2log mu`, `c(k)=2k log mu` | `2log(mu) Z`; `L=2log mu` | `0`; `R/(2log(mu) Z)` |
| U at `(rho,y)`, all `y in I_6` | `kappa=-log mu`, `c(k)=-k log mu` | `log(mu) Z`; `L=log mu` | `0`; `R/(log(mu) Z)` |
| V at `(x,rho)`, all `x in I_6` | `kappa=-log mu`, `c(k)=-k log mu` | `log(mu) Z`; `L=log mu` | `0`; `R/(log(mu) Z)` |
| Each owner on the two empty-word rectangles | `kappa=0`, `c(k)=0` | `H=0`; no positive primitive | `Z`; `R` |

Every row retains source isotropy Z. On each positive row the clock and lag kernels are
both identities; on each zero row the clock kernel contains all integer isotropy while the
lag kernel and their intersection remain identities. These are the full restrictions to
these singleton source classes, not claims that the global clock kernel has no other arrows.
The MAIN window has one positive primitive packet, as does R separately. U and V each have
continuum many distinct positive packets of their own length. All zero rectangles retain
continuum many source packets and free height phases, but no positive closed-time packet.
The fixed point/lines are area-null; the frozen all-point clock and full source prohibit removing them.

Conjugating sqrt(5) to -sqrt(5) sends mu to mu^{-1}. If any positive integer power mu^j
were rational, it would equal its conjugate mu^{-j}, contradicting mu>1.
In particular `mu^2` is irrational, so the MAIN primitive `log(mu^2)` is NOT log of an
ordinary integer prime. The same argument applies to the U/V length and to all integer repetitions;
a selected repeated loop cannot replace the least positive generator.

## 7. Gate disposition and remaining scope

The MAIN wrong primitive is established on its own admitted full source and measure, without
borrowing U/V/R. Hence the frozen necessary prime-only target FAILS and the decision is STOP / FORK.
Positive nonemptiness is demonstrated, not absent; no claim about all-prime coverage is needed.
Arithmetic-order reversal changes the signed clock here while retaining the positive primitive
of its own isolated core; one-sweep controls display their own continuum multiplicity.
These diagnoses do not identify the different owners or promote a control into MAIN.

The mechanism genuinely executes the complete proper-divisor word read from the current state,
then uses its output in the next readout. This does not prove strong naturalness of the chosen
fractional formula, order or macrostep. Those design/encoding risks remain OPEN.
All four source/clock ledgers above are intact, including literal holes and ineffective isotropy.
No global cycle census, trace, operator, formal Route evaluation or classical lift is supplied.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
This raw derivation is frozen before any manuscript access. CP2/CP3 await a separate PAPER UNLOCK.
