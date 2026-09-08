# IR1 non-author review: the analytic finite-core reduction passes

Date: 2026-09-07 UTC. Reviewer: current internal arithmetic-lane agent,
not the author of IR1. Review target:
[IR1_PROOF.md](../integral_return/IR1_PROOF.md), Sections 1–4,
specifically the universal difference/height reduction and the
finite-certification coverage argument. The finite output, code,
classification table, level counts and literature priority are outside
this report's verdict.

## Verdict and provenance

**PASS for the analytic reduction; the one minor request is now closed.**
I independently recomputed the recurrence identities and every large-
difference branch in Sections 1–4. No missing signed branch, invalid
division, or failed numerical escape inequality was found. In particular,
the proof establishes the universal residual bounds `1<=D<=100` and
`-301<=x_i<=299`, once its explicit symbolic channels are removed.
This does not, by itself, certify the computer-assisted classification.

The sole new request was to state closure of the symbolic channel list
under scalar reversal before using the universal conclusion. The closure
is true and is verified below. The author's added Section 3.6 now states
it correctly; the focused follow-up at 09:45:55 UTC verified that repair.
There is no unresolved mathematical correction in this review's scope.

At the audited snapshot the full source SHA-256 was
`985f858919712adaae47797c902705542efad55ac630b6d5f25bd35dded924dd`.
The analytic span from the Section 1 heading through the paragraph
ending “Its code, exact counts and output digest belong alongside this
proof.” had SHA-256
`fdb7081dc45660f10f9d140466bda808ecbf6b3a25aeb3f6a30e4a7e3b688322`.
These hashes identify the reviewed version, not a frozen release.
The full source hash at the focused Section 3.6 recheck was
`5dcc9c6a84e4219a24fa177399ee1e7292e7217d8b83ab3dda4a90ceebd17e5d`.
That follow-up checked the requested new paragraph, not a second full
review of changing finite-output or Section 5 material.

This was a separate non-author derivation, **not a blind review**: the
root reviewer had already reported the Section 2 sign correction and
said its preliminary reading was positive. The version I read already
had the correct `x_(-1)=m+e=x_3`. I did not use a peer review report or
finite output as a substitute for deriving the branches. This is the
current internal Codex team, with no external GPT-5.4 call, human
reviewer, or independently calibrated error process. Calibration status:
`NOT_CALIBRATED`. No venue-fit or admission judgment is made.

No mathematical code or enumeration was run in this review. Only the
submitted text was read and its identification hashes computed. The
author's files and all older evidence were left unchanged.

## Criterion-bound findings

| Criterion from the assigned review contract | Judgment | Evidence anchor | Reason and scope |
|---|---|---|---|
| Correct scalar encoding, reversor and extremal identity | MEETS | equation: Sections 1 and 3.3 | Direct algebra recovers the identity and the signed transformation; both time orientations are retained |
| Exhaustive large-difference case split | MEETS | equation: Sections 3.1–3.5 | The five possible centers, all `k` cases and both `epsilon` signs reduce to the listed channels or a contradiction |
| Universal residual height bound | MEETS | equation: Section 2 and Section 4, first paragraph | The only escape from the height/difference inequality is the exact F4 word |
| Finite seed coverage and termination, as mathematics | MEETS | text: Section 4, “No arbitrary iteration cutoff is allowed.” | Seed parameters are forced by a maximum difference; injectivity rules out a noninitial repeated state |
| Actual finite-certificate completeness and family subtraction | NOT_ASSESSED | dataset: Section 4, finite-run paragraph | Assigned to the independent certificate review; no output totals or terminal list are accepted on this report's authority |

The main positive feature is that the finite box is deduced before
enumeration and is independent of `a`, level and period. This is a
genuine analytic reduction, not a box selected because a sample stopped
producing new cycles. Evidence anchor: equation: Sections 2–4.

### W1 — Make reversal closure of the channel list explicit

**Disposition:** CLOSED. Added Section 3.6 explicitly records the signed
reversor action and the correct F5 parameter involution. This paragraph
was read and compared with the hand derivation below on 2026-09-07 at
09:45:55 UTC.

**Severity:** Minor.

**Evidence Anchor:** text: Section 4, “Every integral periodic orbit is
either one of (2), F3, F4, F5, F6, F8, F12”.

**Confidence:** 5/5 — direct word reversal and cyclic rotation.

Sections 3 and 3.3 use reversal to choose signs or the larger neighbor.
To transfer their conclusions back to the original forward orbit, the
symbolic family list must be reversal-closed. This is true, but the
snapshot leaves it implicit. The minimal remedy is one sentence and
the F5 parameter involution:

`reverse(F5(u))` is a cyclic rotation of `F5(-1-u)`.

Every other listed channel is a cyclic rotation of its own reversal.
For example F12 is palindromic about its `m` entry, and F8 is palindromic
about either entry equal to `1`. The alternating family, F3, F4 and F6
are immediately checked from their displayed words. This check requires
no new computation or change to the claimed families.

This does **not** authorize identifying every reversed cycle with its
forward cycle: generic F5 parameters give distinct orientations.
Section 4 correctly requires either both orientations or an explicit
verified rotation. For instance F5 at `u=50` has a negative extremum
of magnitude 101 but no positive extremum of that magnitude; the
positive-extremum seed naturally lies on its reversed family member.

## Detailed derivation checks

### 1. Scalar recurrence and reversor

The recurrence is equivalently

`x_i+x_(i+3)=x_(i+1)x_(i+2)+a`.

Subtracting its version at `i-1` yields

`x_(i+3)-x_(i-1)=(x_(i+1)+1)(x_(i+2)-x_i)`,

which is exactly Equation (1). Two successive zero `d` values propagate
in both directions without dividing by any coefficient. If all `d`
vanish, substitution into the alternating sequence gives Equation (2).

For `R(x,y,z)=(z,y,x)`, direct composition gives

`R T_a R(x,y,z)=(xy+a-z,x,y)=T_a^(-1)(x,y,z)`.

On a centered scalar seed use `x'_i=x_(2-i)`. Then

`d'_i=-d_(-i)`, hence `(d'_0,p',q')=(-d_0,-q,-p)`.

Thus the initial positive-extremum choice is legitimate, while the
second reversal in Section 3.3 may change that sign. The explicit
`epsilon` in Sections 3.3–3.5 correctly prevents losing this branch.

### 2. High coordinates force F4

From `|x_1+1|>3D`, integrality forces `d_0=0`. With
`e=d_1=-d_(-1)`, the definitions give both neighboring coordinates
equal to `m+e`, not one equal to `m-e`. Since `e=0` would force `D=0`,
we have `0<|e|<=D`. Their heights exceed `2D`, forcing
`d_(-2)=d_2=0`. Equation (1) at `i=1` then implies `b=-1`.
Starting from `(-1,m,-1)` produces `a+1-m,-1,m,...`, exactly F4.
The contrapositive at every phase gives the claimed residual height
bound. The formerly reported sign typo is closed in the reviewed input.

### 3. End centers and the `s=-1` branches

At `d_0=D>0`, Equation (1) forces the integer `s+1` into `[-2,2]`.
The formulas for `p,q` follow by one forward and one backward scalar
step. The endpoint cases `s=1,-3` force both neighbors to saturate the
same bound, so `u,v` lie in an interval of length two. They cannot have
difference `D>100`.

For `s=-1`, setting `E=u+v-a-1` gives the displayed neighbor differences.
Their lower bounds give `(u+1)E>=0` and `(v+1)E<=0`. A positive `E`
would imply `u>=-1>=v`, contradicting `u<v`. At `E=0` the recurrence
gives F4. With `E=-k<0`, summing the two nonnegative inequalities gives
`kD<=4D`. A further use of (1) gives

`d_(-3)=-k^2(u+1)-kD+k`,

`d_3=k^2(v+1)-kD-k`,

whose sum is `k(k-2)D`. This excludes `k=3,4` and no others.

For `k=1`, the centers of `d_(-3)=-v` and `d_3=u` are both `a+1`;
therefore `|a+2|<=4`. If `a!=-1`, the coefficient of `u^2` in `d_5`
is a nonzero integer, while `|a-1|<=7`. For `U>49`,
`U^2-7U-1>2U+6>=D`. The only surviving parameter is `a=-1`,
where the recurrence closes to F5 for every integer `u`.

For `k=2`, the two coefficients multiplying `2a` are `u+a+2` and
`v+a+2`, whose difference is `D`. Their maximum absolute value is at
least `D/2`, yielding `|a|<=2` without dividing by `a`.
The `d_4` expressions exclude `a=1,2,-2` exactly as printed.
At `a=-1`, the seed has `u+v=-2` and closes to a rotation of F8 with
`t=v`. At `a=0`, it has `u=-1-v` and closes to F12 with `m=v+1`;
the large-difference inequalities ensure `m>0`. No new ownership claim
about C413 is needed for this local substitution check.

### 4. Signed `s=0,-2` branches

After arranging `|p|>=L/2`, its bound gives `|u+1|<=4`.
The other coordinate has `|v+1|>=L-4`, so the paper's weaker
`L-6` estimate is safe and gives the integer restriction `|q|<3`.
Because `p+q` equals either `epsilon L` or `-epsilon L`, two numbers
bounded in absolute value by `L` must share that sum's sign or be zero.
The restrictions `r in {0,1,2}` therefore exhaust all possibilities.

| Branch | Independently checked decisive consequence |
|---|---|
| `s=0`, `epsilon=-1`, `r>=1` | `d_2=(r+1)L-r(u+1)>L` |
| `s=0`, `epsilon=1`, `r=2` | `d_2>=L-8`, with coefficient 3, contradicts `3(L-8)>2L` |
| `s=0`, `epsilon=1`, `r=1` | The coefficient bound forces `a in {0,1}`; `a=1` gives `d_4=L+1`, and `a=0` gives `d_7=-L^2+3L-1` |
| `s=0`, `r=0`, either sign | `d_4=-u epsilon L` has coefficient `1-epsilon L`, forcing `u=a=0` and F6 |
| `s=-2`, `epsilon=1`, `r>=1` | `d_2<=-(r+1)L+4r<-L` |
| `s=-2`, `epsilon=-1`, `r=2` | The displayed product lower bound equals `2L^2-41L+138`, exceeding `L` throughout `L>100` |
| `s=-2`, `epsilon=-1`, `r=1` | The `d_5` bound reduces `u` to `[-3,1]`; `|d_6|<3` then forces `u=0`, which gives `d_7=2L-7>L` |
| `s=-2`, `r=0`, either sign | `d_4=(u+2)epsilon L` has coefficient `epsilon L-1`, forcing `u=-2`, `a=2v-4` and F3 |

For the most delicate `s=-2,epsilon=-1,r=1` row, I recomputed

`d_5=-L+3u+4`,

`d_6=uL-3u^2-4u-1`.

The excluded `u` values are exactly `-5,-4,2,3`, where the coefficient
has magnitude at least 3 and `|d_5|>=L-13`. For the surviving nonzero
values `-3,-2,-1,1`, the constant in `d_6` has absolute value at most
16, so `|d_6|>=L-16>2`, contrary to its integer upper bound 2.
At `u=0`, direct continuation gives `x_7=2-L`, `x_8=-3`,
`x_9=L-5`, and hence the final contradiction. The strict inequalities
all hold at the first possible integer `L=101` and strengthen thereafter.

### 5. Universal finite-core coverage and termination

After removing the channels, every nonzero difference maximum satisfies
`D<=100`. Section 2 then gives `-3D-1<=x_i<=3D-1` at all phases.
Choosing an extremum and possibly reversing produces the seed
`(u,s,u+D)` in precisely the printed finite ranges. The parameter

`a=(u+D)-su+s-p`

is recovered algebraically; it is not an independently imposed cutoff.
The two neighbor inequalities are necessary consequences of the same
global maximum. Thus retaining their solutions cannot discard a true
residual cycle in its chosen orientation.

At fixed seed and `a`, an orbit which never leaves these bounds occupies
a finite set of triples. If a state repeated before returning to the
initial state, injectivity of `T_a` would pull that equality backwards
to an earlier return to the initial state, a contradiction. The stated
exit-or-first-return algorithm therefore terminates without a guessed
period limit. Reversing the recovered cycles is necessary for complete
forward-orbit enumeration when the positive maximum only occurs on the
reversed orbit. The text explicitly requires this and prohibits merging
cycles by reversal.

I did not validate whether the implementation actually follows those
conditions, whether its output totals are correct, or whether its
symbolic subtraction leaves exactly the printed terminal words. Those
are separate certificate obligations, not weaknesses in this analytic
reduction and not covered by this PASS.

## Handoff boundary

The research-review and ARS theoretical-methodology guidance was used to
keep the report source-anchored, non-author, read-only with respect to
the proof, and separate from editorial or venue judgments. The caller's
bounded current-team contract overrides legacy external-model and full-
panel defaults. The existing Section 2 repair is verified, and the only
new addition requested in W1 is now verified closed. No other correction is required
by this review of Sections 1–4.

The next gate is the separately assigned independent finite-certificate
check and root integration, not another run of the arithmetic ED1
diagnostic. This report does not confer a C-number, paper admission,
target arithmetic, or Route-B authority.

## Arithmetic Receipts

no_recomputable_statistics: This is an exact theoretical recurrence proof; it reports no p-values, sample moments or degrees of freedom covered by the statistical receipt procedures. All algebra checked by hand is recorded above and is not presented as executed code.
