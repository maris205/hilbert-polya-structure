# ARS Devil's Advocate — Checkpoint 2 / RCF01

**Date:** 2026-09-21.  
**Candidate:** `ANG-20260921-RCF01`.  
**Reviewer task:** `/root/rcf01_analysis_review`.  
**Verdict:** `PASS` for the bounded Gate1–Gate3 author evidence.  
**Calibration:** `NOT_CALIBRATED`.  
**Portfolio disposition:** ADVANCE at the owned Reeb/clock/packet level;
STOP stronger-naturalness promotion. No formal Route coordinate is assigned.

## 1. Scope, provenance and limitations

This is a separately dispatched AI mathematical evidence audit at ARS
checkpoint 2, not external peer review, checkpoint 3, a literature/novelty
assessment, or an independently calibrated correctness certificate. No
external model, network request, numerical experiment, Git operation or PDF
generation was used. The only new file written by this reviewer is this report.

The scientific evidence was the following two complete author inputs:

| Input | Actual reading | SHA-256 at reading |
| --- | --- | --- |
| [Frozen card](../candidate-card.md) | All 187 lines, including the pre-audit multiplicity target | `9fd564c3a42a09fb38463c860daa4cc451887015e3334485108b1537cba8622a` |
| [Author paper](../paper.md) | All 553 lines; 1–195 are opening history, 196–553 contain the audited continuation | `1264835924f270dc6b021aa56d89cb7431da0105f85fb5bc5db6f20a3394844d` |

No other 348 review, scout, controls, ledger or evidence file was opened.
No 344 proof or other stream proof was opened. Source links in the paper
were not followed. In particular this review did not obtain another
reviewer's answer before reaching its disposition.

Actual instruction/context reading comprised the stream `AGENTS.md`, all
411 lines of `plan.md`, and the following complete selected ARS files under
`/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/3.22.0/skills/academic-research-suite/`:

- `SKILL.md`;
- `ars/deep-research/WORKFLOW.md`;
- `ars/deep-research/agents/devils_advocate_agent.md`;
- `ars/deep-research/references/logical_fallacies.md`;
- `codex/model-runtime-policy.md`.

Read-scope qualification: an initial combined entry-point read of
`AGENTS.md plan.md readme.md` was truncated. It is not a claim to have read
the complete root README. A subsequent `rg` for `348|RCF|Reeb` exposed the
348 workflow entry and several other-candidate summary snippets. These
are disclosed context exposure, not evidence used for any derivation here;
strict isolation from all other-candidate summaries is therefore not claimed.
The mathematical assessment below rests on the two frozen inputs alone.

The served model identifier and effective reasoning setting were not
independently observed and remain `UNKNOWN`. Separate execution does not
establish independent model errors: this is an AI review within the same
working session/family, without cross-model validation or human verification.
No numerical confidence score is assigned. The caller restricted this task
to checkpoint 2 and explicitly rejected an issue quota; the DA template's
all-checkpoints and minimum-one-issue defaults do not enlarge that scope.

## 2. Gate1: independent reconstruction and attacks

### G1 — all words and finite basins

For a word of length d>=1, the stipulated pair rule reduces its length by
one and preserves the gcd of all entries. Its first d−1 pair steps therefore
reach `(gcd(w))`. At a singleton n, the atom factorization is well-defined:
induction on n gives existence, and the Euclidean algorithm gives Bezout
for an atom r coprime to a, hence the atom-divides-product lemma and
uniqueness by cancellation. The sorted empty factorization of 1 is unique.
These arguments use no prime list or finite factorization cutoff.

After factorizing a composite gcd, coalescing the factor word yields its
single atom r if the gcd is a power of r, and 1 otherwise. The next step
from `(1)` is empty. Thus the author's basin alternatives in paper lines
216–232 are exhaustive. They also exclude a composite cycle and infinite
transient: each factor-word stage has finite length and is followed by an
atom fixed word or by `(1)` and empty.

Adversarial unit case: `(1,1,...,1)` reaches empty after exactly its original
length many steps. Its geometric transport is identity on every step, but
its word evolution is terminal rather than cyclic. No source unit loop may
be added in MAIN. Mixed-factor gcds likewise terminate. For example gcd 12
produces `(2,2,3)`, then `(2,3)`, then `(1)`, then empty; gcd 8 instead
produces `(2,2,2)`, then `(2,2)`, then `(2)`. These exact examples test the
general proof; they are not its completeness evidence.

The first-hit coordinate map is `(u,v,z) -> (u−s_w,v,z)` because every valid
step subtracts `log a` from u and fixes v=q xi and z. Hence N_w and s_w are
finite, fixed functions of the whole word. Basin labels and first-hit maps
are not chosen after solving physical returns. **Disposition: PASS.**

### G2 — inverse completeness and branch IMAGE

Every possible source is either a singleton or a word of length at least
two. The first alternative gives exactly the singleton inverse specified
by `fct(n)=w'`; the second gives exactly `(a,b,tail)` with `gcd(a,b)=g`
when the target is `(g,tail)`. No longer-word inverse can hit empty; the
main empty target has the singleton predecessor `(1)`. All positive pair
entries, including units, remain. The two source-length alternatives are
disjoint, so no distinct incoming word is lost by deduplication.

The inverse geometry is `(Q,X,Z) -> (aQ,X/a,Z)` on the entire q>0 target
chart. Both compositions are identity, and its Jacobian is exactly
`a*(1/a)*1=1`. In `(u,v,z)` it is a translation, so the density assertion
holds pointwise on the axes and on `vz=−1` as well. Change of variables
then gives equality for every Borel set, including sets of infinite measure.
The same reasoning applies to each actual arrow translation.

The global many-to-one map has many inverse branches; summing all branches
is a different operation and is not measure preservation of global S.
Paper lines 424 and 509–510 explicitly retain this distinction. The source
negative-log IMAGE cocycle is zero, without identifying it with physical
time. **Disposition: PASS.**

### G3 — retained lag, terminal validity and full quotient topology

Let an arrow have the frozen convention `(y,k,x)`, with `k=m−n`.
If a common future is before the core, applying its remaining identical
steps gives `N_y−m=N_x−n`. In the terminal basin it is impossible to extend
past empty. The necessary and sufficient equations are consequently

```text
k = N_y−N_x,
u_y−u_x = s_y−s_x,   v_y=v_x,   z_y=z_x.
```

In an atom basin put `L=log r`. A common future at the core has the form
`m=N_y+j`, `n=N_x+l`, where j,l are nonnegative. It gives

```text
u_y−u_x = s_y−s_x + (k−N_y+N_x)L,
v_y=v_x, z_y=z_x.
```

Every integer `k−N_y+N_x` can be written j−l with j,l nonnegative, proving
sufficiency for every retained lag. The equations also cover common
futures before the core. Composition adds k and telescopes the N/s
differences; inversion negates them. Multiple witnesses (m,n) for an equal
triple are not extra arrows. This checks the exact groupoid convention.

At equal source and target, MAIN has kL=0 in an atom basin and k=0 in the
terminal basin. Its source isotropy is therefore trivial everywhere.
This does not remove the arrow `(Phi^L x,1,x)` at a periodic core point:
`S(Phi^L x)=x`, while its geometric endpoints in Y are different. This
explicit lag/sign check distinguishes a physical return from source isotropy.

For fixed words and lag, each nonempty arrow component is the graph of one
translation of R^3. Discreteness of the word and lag factors makes these
components open and closed in the prescribed inherited topology. Source and
target restrict to diffeomorphisms, and composition/inversion are continuous
smooth maps on these components. No replacement groupoid topology is needed.

The proposed map to the disjoint union of R^3 and `(R/L_r Z) x R^2` has
exactly these orbits as fibers: equality of quotient coordinates reconstructs
an integer lag in an atom basin and the unique allowed lag in the terminal
basin. On every word chart it is continuous, open and onto its own
component. Core charts provide surjectivity of the whole map. These facts
prove the full quotient homeomorphism, not merely a parametrization of a
chosen subset. A countable disjoint union of those components is Hausdorff
and second countable; the translation charts give its smooth dimension 3.
All incoming charts and all v,z values are accounted for. **Disposition: PASS.**

### G4 — full contact/Reeb equations and both volume owners

Recomputing exterior differentiation gives

```text
d beta = z dv wedge du + v dz wedge du + dv wedge dz;
beta wedge d beta
 = ((1+vz)−vz/2−vz/2) du wedge dv wedge dz
 = du wedge dv wedge dz = dq wedge dxi wedge dz.
```

Thus `vz=−1`, either axis and their intersection are regular contact
points. All arrow translations preserve beta exactly, so local forms
descend to the proven full quotient. Circular u causes no obstruction:
the local one-forms du agree under constant deck translations.

The actual frozen action becomes `(u+t,e^t v,e^(−t)z)`. Its generator R has
`beta(R)=1`, and direct contraction gives

```text
i_R d beta
 = z(v du−dv) + v(−z du−dz) + v dz + z dv = 0.
```

Both identities hold throughout the atlas, and the action commutes with
every arrow translation while preserving the word and lag labels. The
exponential formulas give the group law and all-real-time existence on
the entire domain; no finite-time escape from q>0 occurs.

The physical Jacobian and its inverse are identically 1, separately from
the source-branch Jacobian. Pullback fixes beta, so it also fixes the
descended contact volume. Local volume invariance extends to all Borel
sets by a countable chart partition. Atlas counting measure pushforward
through infinitely many word sheets is not used to define this volume.
Infinite total volume licenses neither finite-measure recurrence nor an
invariant probability claim. **Disposition: PASS.**

## 3. Gate2: full returns and the three controls

### P1 — MAIN

The full quotient equality in the terminal component forces t=0. In an
atom component it forces simultaneously

```text
t in L_r Z,  (e^t−1)v=0,  (e^(−t)−1)z=0.
```

For real nonzero t both exponential factors differ from 1. Thus a nonzero
return exists exactly when v=z=0 in an atom basin; the entire stabilizer
there is `L_r Z`, and it is `{0}` everywhere else. Basin, v and z are
arrow-invariant, so this answer is representative-independent. There are
no stationary or dense-stabilizer states.

Specific attempted counterexamples fail for independent reasons: at
`v=1,z=0`, time L_r changes v to r; at `v=0,z=1`, it changes z to 1/r;
at `vz=−1`, constancy of the product does not give equality of either
coordinate. None can be declared periodic using an invariant product
instead of the complete state. Every such point remains in Q.

The solved periodic set in each atom component is one circle, and u+t
acts transitively on it. Its least positive period is L_r, and all positive
returns are its own integer multiples. The full incoming preimage consists
of every basin-r word with all q>0 and xi=z=0; `[log q−s_w]` exhausts its
phases. Different prime basins cannot be identified by any arrow. Prime
powers enter the same prime basin; mixed-factor gcds enter the terminal
one. This proves exactly one primitive per atom and no extra primitive.

The logarithm comes from the frozen multiplicative source transport and
the frozen physical action; no source IMAGE time, algorithmic time, roof
or subsequent period rescaling enters this deduction. **Disposition: PASS.**

### C1 — FACTOR-OFF

All nonempty words now end at their own singleton gcd n, including n=1;
empty has no incoming source. The control's N/s data therefore differ from
MAIN and must be recomputed, as paper lines 417–419 do. Its singleton
inverse is available only over the same singleton; all pair inverses
remain, with full domains and the same exact Jacobian cancellation.

For n>=2 the core translation has L_n=log n, yielding the author's graph
equations, trivial source isotropy and cylinder quotient. For n=1 that
translation is identity: arbitrary lag can be added after both first hits
without changing geometry. Hence source isotropy is Z at every point of
basin 1, while its coarse quotient is R^3. Empty is a separate R^3
component with trivial isotropy. Equal witness triples remain one arrow;
the nonzero lag arrows of basin 1 remain distinct.

Every arrow is beta-strict, so the control owns its descended contact form
and complete Reeb action. On either R^3 component u+t=u forces t=0.
On each n>=2 cylinder the full return equations again force v=z=0 for
t nonzero, giving precisely one primitive of period log n and its own
repetitions. In particular the n=4 orbit is disjoint from the n=2 orbit;
commensurable lengths do not identify physical orbits. This control
correctly supplies an adverse composite-primitive result. **Disposition: PASS.**

### C2 — DRIFT-ONLY

The control explicitly retains identical C,S,G,beta, so reusing their
source and quotient derivations does not change owners. Its separate action
is `(u+t,v,z)` with generator V. Directly,
`beta(V)=1+vz` and `i_V d beta=−z dv−v dz`. Both Reeb equations hold
together only at v=z=0, although translation invariance makes this a global
strict contact, volume-preserving action. Its physical determinant is 1.

Its full return group is `{0}` in the terminal component and `L_r Z`
at every transverse point of each atom component. Distinct (v,z) are
preserved by both source arrows and this physical action, so each pair
gives a distinct circle. There is an R^2 family per atom, not a single
representative packet. The unit and incoming histories remain those of
MAIN, whose source isotropy is trivial. **Disposition: PASS; the control
fails the proposed main Reeb and multiplicity targets, as reported.**

### C3 — UNIT-HOLONOMY

The word source and N data are those of MAIN, but every geometric step
and inverse is now identity on the whole target chart. Its branch IMAGE
density is 1. Terminal arrows have only `k=N_y−N_x`; atom-basin arrows
have arbitrary k. In both cases geometric equality is necessary and
sufficient. Thus source isotropy is trivial in basin 0 and Z in each atom
basin, including every incoming word chart, not only the core word.

Its quotient is one R^3 per basin via the open identity chart maps, with
no u-period identification. Beta descends, and the full frozen Phi owns
the same pointwise Reeb and physical-volume identities on this different
quotient. Equality u+t=u forces t=0 everywhere. Nontrivial source lag
therefore coexists with no physical period and no repetition. The author
does not quotient the Z lag kernel out of G to obtain this conclusion.
**Disposition: PASS.**

## 4. Gate3, findings and dispositions

No Critical, Major or Minor mathematical defect was identified in the
bounded author evidence. The following are adjudicated attacks and
limitations, not a manufactured defect quota:

| Audit question / attempted objection | Evidence and disposition |
| --- | --- |
| Were inconvenient histories or transverse states discarded? | No: the exact quotient fibers and full return equations include every word and every transverse point. CLOSED by G1–G4/P1. |
| Can unit steps or retained lag generate an overlooked packet? | MAIN units terminate; FACTOR-OFF basin 1 and UNIT-HOLONOMY retain Z isotropy but have real u and no physical periods. CLOSED by the own-control equations. |
| Does zero source IMAGE erase physical returns? | No: a return arrow can have distinct endpoints in Y. The explicit core arrow of lag 1 verifies the distinction. CLOSED. |
| Is contact preservation sufficient for normalized Reeb time? | No: DRIFT-ONLY is a counterexample, correctly reported by C2. CLOSED for MAIN through both equations. |
| Do the controls prove canonical arithmetic naturalness? | No. They separate roles within this designed construction. S2 retains this limitation; strong naturalness remains OPEN. |
| Is volume conservation being promoted to typical periodicity or recurrence? | No. The periodic locus has two vanishing transverse coordinates, hence zero contact volume; infinite volume is explicit. CLOSED at the stated scope. |
| Does exact prime indexing establish an operator, Route result or RH statement? | No such conclusion is supported or asserted in the continuation. T3 is NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal A UNASSIGNED; B NOT INVOKED. |

The strongest counter-argument to a stronger interpretation is that the
source computes complete atom factorization as a macro and deliberately
funnels prime powers into atom fixed words, while the geometric translation
and hyperbolic Reeb pair are designed to realize the resulting prime
circles. A rigorous realization of these inputs does not explain why an
independent arithmetic/geometric principle must choose them. FACTOR-OFF
shows the same Reeb construction supports every integer label. Paper
lines 521–528 directly acknowledge this objection, so it limits the
significance rather than contradicting the scoped theorem.

No literature novelty, canonical selection theorem, analytic trace/zeta
owner or natural quantization has been supplied or checked. Those absences
do not invalidate the frozen three-gate result and cannot be turned into
positive credit. The analysis does not inherit any prior candidate theorem.

The same-object ledger remains intact for `ANG-20260921-RCF01`: all MAIN
source, beta, physical action and orbit-equivalence formulas agree with the
187-line card. Each control is separately owned and has the reported
adverse result. The decisive positive reason is the exact full-quotient
return equation, which leaves one circle per intrinsic atom and excludes
all other nonzero returns without deleting any state.

Checkpoint 2 therefore returns `PASS` to the parent for integration and
the separately assigned checkpoint 3. This reviewer neither performs that
later checkpoint nor authorizes a new research route. Mathematical model
review remains `NOT_CALIBRATED`, with the execution and exposure limits
recorded above.

At handoff the parent reported append-only additions to the card and paper.
Byte checks of the original first 187 and first 553 lines still match the
input hashes above. The appended material was not read or adjudicated here.
Both relative Markdown links in this report resolve to existing files.

EOF — bounded checkpoint-2 report; author inputs were not modified.

## ARS Devil's Advocate — separately authorized Checkpoint 3

**Date:** 2026-09-21.  
**Candidate:** `ANG-20260921-RCF01`.  
**Verdict:** `PASS` for the complete supplied final manuscript and status surfaces.  
**Calibration:** `NOT_CALIBRATED`.

The parent separately authorized this final vulnerability/significance review
after checkpoint 2 was frozen. The preceding 339 lines are retained unchanged,
with SHA-256
`0237d7cb568b37be92d2ad3dd11620ae17f2638d3938d95f92d9961c32729e5a`.
This is the same reviewer continuing a new checkpoint, not a new blind seat
or an independent replication of checkpoint 2. The model identity and
execution limitations in the first report remain applicable.

### Final-input read scope

The original card 1–187 and paper 1–553 remain the already-read inputs.
For checkpoint 3 the reviewer personally read paper 554–603, all 46 lines
of the package README, all 78 lines of the claim ledger, and card 188–219.
The resulting full version boundaries are:

| Final surface | Full lines | SHA-256 at this checkpoint |
| --- | --- | --- |
| [Paper](../paper.md) | 603 | `6ebce46d764aa9455349ff7d859eec5a4439aa4df7eb81a4d8d4e64b34045cff` |
| [Package README](../README.md) | 46 | `f9300b22fc6cab4c5485f418717873b3f61bad5f7e04d2cb8e613b997cf6f43e` |
| [Claim ledger](../claim-ledger.md) | 78 | `1077c014ffab4945e0014bb45f39c5b319e60b611d9d655381ecfdb639a6c463` |
| [Candidate card](../candidate-card.md) | 219 | `062f1ac4c797f9f0562f4236cd7e738420129120a41d111bcfc3c697ca186f25` |

No root overview, other review, controls/scout/verification file or linked
external source was opened during this checkpoint. The reviewer did not
read other agents' reports or infer their contents from navigation labels.
Workflow statements about Git/external actions in the package are not
independently verified by this mathematical review; no Git or external
operation was performed. The write scope remains this report alone.

### F1 — the actual first-return map and hyperbolicity

On the atom-r component, the complete quotient is
`(R/L_r Z) x R^2` and the frozen physical action is
`([u],v,z) -> ([u+t],e^t v,e^(−t)z)`. Thus the entire section `[u]=0`
is transverse because the u component of the generator is 1. Starting
on this section, its first positive section return satisfies
`t in L_r Z`, hence occurs at exactly L_r at every transverse point.
Substitution gives `(v,z) -> (r v,z/r)` on the whole plane, with derivative
`diag(r,1/r)`.

Section return is not a full-state return: nonzero transverse points
generally come back to a different point of that section. The map's unique
fixed point is `(0,0)`, exactly the already-solved periodic locus. At this
point the tangent section is also the contact plane, since beta is du
there. Its two transverse multipliers r and 1/r have modulus different
from 1 because r>1. They therefore establish hyperbolicity and exclude
the multiplier 1 required for a degenerate closed Reeb orbit. These are
the actual physical return multipliers, not an independently inserted
matrix, trace formula or operator.

For FACTOR-OFF the same calculation on its own integer-n cylinder gives
`diag(n,1/n)`, n>=2. DRIFT-ONLY returns the full transverse plane by the
identity, consistent with its continuum family. UNIT-HOLONOMY has real u
and no circular section return. The supplement does not conflate those
different owners or replace the full-state classification with stability
data. **Disposition: PASS.**

### F2 — volume invariance versus measure-theoretic conservativity

The supplement's box W is a legitimate measurable subset of an atom
component. The interval `0<u<L_r` parametrizes the circle with one point
removed, so its contact volume is exactly
`nu(W)=L_r*(exp(1)−1)`, finite and strictly positive. For any integer k,
its image under `Phi^k` has

```text
v in (exp(k),exp(k+1)),
z in (0,exp(−k)),
u shifted by k modulo L_r.
```

For distinct integers k the open v intervals are disjoint, including
adjacent intervals whose common endpoint is excluded. Possible wrapping
of u on the circle cannot create an intersection. The same argument
covers negative as well as positive iterates. Hence W is a positive-volume
wandering set for the invertible time-one map. This directly disproves
measure-theoretic conservativity of `Phi^1`.

It does not contradict preservation of nu: each image has the same volume,
and the ambient component has infinite volume. Nor does it invalidate
the Reeb equations or the existence of the zero-volume periodic circles.
The final text restricts the adverse conclusion to the actual time-one
map, while explicitly explaining that its earlier use of
"conservative-contact" meant volume-preserving. This removes the possible
terminological overstatement without changing the candidate or claiming a
new research mechanism. **Disposition: PASS.**

### F3 — final status, exposure and significance across all four surfaces

| Check | Evidence and disposition |
| --- | --- |
| One candidate and current result | All four surfaces name `ANG-20260921-RCF01` and the current `OWNED REEB PRIME PACKETS — SCOPED ADVANCE; NATURALNESS OPEN` status. PASS. |
| Historical OPEN not presented as the current conclusion | Paper 199–203 identifies the first 195 lines as history; card 191–195 separates the original 187 lines and current outcome; ledger 40–43 and 63–64 explicitly supersede its first 38 lines. The README presents the current result directly. PASS. |
| No stronger naturalness promotion | Paper S2, card 212–215, ledger 59–67 and README 20–24 retain designed factorization/scheduling/geometry and strong naturalness OPEN. PASS. |
| No Route/operator promotion | T3 remains NOT AUDITED, classical A0/A1/A2 NOT APPLICABLE, formal coordinates UNASSIGNED, and B NOT INVOKED. Stability multipliers are not presented as a quantum operator. PASS. |
| Conservation qualification propagated | Paper 576–591 supplies the counterexample; README 26–28 and ledger 71–78 state its adverse implication. The card asserts only preservation of contact volume, so it makes no contradictory recurrence claim. PASS. |
| AI and human verification disclosed | Paper 593–597 names Codex/internal agents, records user plan approval and explicitly says human proof verification is NOT attested. It disclaims external peer review and cross-family verification. PASS. |
| No model-review inflation | Package/card/ledger distinguish internal review from external peer review. This report's two checkpoints remain NOT_CALIBRATED and cannot establish independent model errors or human validation. PASS. |

No Critical, Major or Minor issue was identified in the supplied final
delta or its integration with the previously audited mathematics. No
rebuttal or unsupported concession was needed.

The strongest objection remains one of significance: exact prime packets
can be produced by deliberately chosen arithmetic macros and geometric
holonomy, so the construction alone is not a canonical explanation of
prime geometry. The final manuscript addresses this objection directly
and leaves the relevant naturalness question OPEN. Its defensible advance
is the explicit complete Reeb/volume/clock/packet owner and exhaustive
controls; the wandering-box counterexample further prevents a stronger
recurrence interpretation. Missing analytic/Route claims remain missing,
rather than being inferred from the successful local geometry.

Checkpoint 3 therefore returns `PASS`. The same-object ledger is intact;
the portfolio decision remains ADVANCE at the Reeb/clock/packet level and
STOP stronger-naturalness promotion. This ends the authorized final review.
No new scientific branch, experiment, operator work, Route evaluation or
external release is performed or authorized by this verdict.

EOF — checkpoint 3 complete; checkpoint-2 prefix preserved; reviewer stops writing.
