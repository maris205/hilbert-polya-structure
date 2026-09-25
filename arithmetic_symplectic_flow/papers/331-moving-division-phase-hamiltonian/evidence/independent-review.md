# Internal independent review — moving division-phase Hamiltonian

Candidate ID: `AHF-20260920-DPH01`.
Paper ID: `331-moving-division-phase-hamiltonian`.
Date: 2026-09-20.
Status reviewed: `OWNED HAMILTONIAN FLOW; ARITHMETIC PACKETS OPEN — STOP / FORK`.
Review standing: all three bounded checkpoints complete; no manuscript correction requested.
Calibration: `NOT_CALIBRATED`; internal same-model/shared-history scrutiny, not external peer review.

## 1. Inputs, access order and independence limits

The only scientific inputs personally read for this review were:

| Input | Actual read scope | SHA-256 |
| --- | --- | --- |
| Frozen candidate card | Original lines 1–192 through the original EOF | `dd6253b6c128fb1b93bb9c109a307ee7df25ea9d9787f44fa09247cac0a0b8c6` |
| First/released/final manuscript | All 366 lines through EOF | `d150f1b49e4b1b0ac0dec10d39c47aa59900dbdd7cfc900003eb0b392dd6d117` |

The ARS router was personally reread completely this round before the scientific
card read. Previously read applicable deep-research workflow, Devil's Advocate,
runtime and fallacy instructions were retained. The three-checkpoint method was
applied within the parent's confirmed mathematical scope, without a venue score.

The actual observable sequence was:

1. Read and hash the original 192-line card; independently derive MAIN and ALL
   three controls while retaining the mathematics privately.
2. Send metadata-only `ALL RAW READY`, before receiving the lock notification.
3. Receive one combined `FIRST LOCK NOTICE + RAW RELEASE` message. Root reported
   its first-draft hash tool had completed before root received READY, and before
   receipt of any raw mathematics; the following clock reading was
   `2026-09-20 09:26:47 UTC`. This is author-reported lock chronology, not a
   reviewer-observed private completion timestamp.
4. Release eight mathematical messages, ending `ALL RAW FINAL`, without opening
   the manuscript or other scientific materials.
5. Receive a separate `PAPER UNLOCK` after all raw messages were acknowledged.
6. Measure the manuscript hash and personally read lines 1–210 and 211–366 to EOF;
   compare its proofs with the previously submitted raw derivations.
7. Complete the final adverse checkpoint and write only this assigned report.

The first and released manuscripts have the same reported hash, matching the
actual bytes read. No manuscript amendment was requested or adopted during this
review. Root's first draft was locked before receiving raw mathematics; this does
not establish absence of shared historical context or error independence.

No card append, scout, ledger, historical scientific source, peer answer or
auxiliary mathematical report was read. No auxiliary agent, web query, scientific
numerical computation, parameter change, or other-file write was used. The same
inherited runtime/model and reasoning setting were retained. This report neither
verifies source-author historical reading claims independently nor borrows their
mathematical conclusions. The final manuscript's provenance statements are read
as disclosures, not additional proof inputs.

## 2. Checkpoint 1 — card-first personal derivation

### 2.1 Smooth full source, inverse and every-Borel IMAGE

Write `v(Q)=exp(-1/Q^2)` off zero and `v(0)=0`. For MAIN, every
mixed derivative off the axis is a finite sum of `v(Q)` times polynomials
in `q,Q^(-1)` and bounded trigonometric factors. On bounded q intervals,
exponential decay dominates each inverse power of Q, uniformly. Extending all
these derivatives by zero proves a jointly smooth potential, flat along Q=0.
The declared axis field is therefore the actual Hamiltonian field, not an
independently glued dynamics. Each control has its own equally smooth extension.

For the stated form, `i_(X_H) omega=dH`; hence the actual flow preserves omega.
The controls satisfy this identity with their OWN Hamiltonians. All four
potentials lie in `[0,1)`. Conservation of each owner's energy bounds both
momenta by `sqrt(2 H_*)`; positions grow at most linearly over a finite time
interval. A finite-time trajectory stays in a compact box, where the smooth
field permits continuation. This works in both directions and proves

    I_x=R, D_t=X, Phi^t(X)=X,
    (Phi^t)^(-1)=Phi^(-t), Phi^(s+t)=Phi^s Phi^t

for all real s,t and every initial state. A globally bounded force is not needed.
All maps are smooth global diffeomorphisms. The full hypersurface Q=0 is not
claimed invariant: P nonzero takes a point off it. The narrower frozen
`R_axis={Q=0,P=0}` is invariant.

Every owner's vector field has divergence zero. Its variational determinant
therefore equals one at every state and time, including null axes and equilibria.
The global change-of-variables theorem gives

    mu(Phi^t E)=integral_E 1 dmu

for EVERY Borel E, also unbounded E by exhaustion. This is not merely a
whole-space mass statement. The inverse determinant and finite composition laws
hold pointwise. Lebesgue4 is sigma-finite, full-support and nonatomic. The
derivative prescription fixes null-point values; an a.e. measure identity by
itself would not uniquely prescribe them.

### 2.2 Actual time groups, two kernels and complete incoming objects

The action triples are genuinely parametrized by `(t,x)` with their actual
time label. Composition adds time; no free-word or integer-lag replacement occurs.
The physical clock is `c=t`; the separate IMAGE cocycle is `sigma=0`.

| Actual source | Literal source isotropy / physical return group H_x | Kernel of c on isotropy | Kernel of sigma on isotropy |
| --- | --- | --- | --- |
| Stationary | R | 0 | R |
| Nonstationary periodic, least period L | LZ | 0 | LZ |
| Nonperiodic | 0 | 0 | 0 |

These are the closed-subgroup possibilities for a continuous real action.
The stationary orbit is a singleton, but retains ALL real time arrows and has
no least positive return. For a periodic orbit, repetitions are the actual rL
and the physical phase is elapsed time modulo L. For a nonperiodic orbit, a
chosen reference gives its injective elapsed-time parameter. This does not assert
a global transversal or an embedded/subspace-topology classification for unknown
general nonperiodic orbits. No additional height extension is introduced.

All incoming states are exactly the same complete actual orbit. Invertibility
excludes extra finite-time transient ancestors entering an equilibrium or a
periodic core. An asymptotic limit is not an incoming arrow. A plane invariant
for both time directions has no off-plane finite-time incoming states.

Crucially, `sigma=0` does not imply `H_x=0`, and stationary `H_x=R` does not
exclude nonstationary periodic sources elsewhere.

### 2.3 Full critical sets and integer-seed audit

For MAIN, putting `theta=pi q/Q` off the axis gives

    W_q=(pi v/Q) sin(2theta),
    W_Q=v[2 sin^2(theta)/Q^3 - pi q sin(2theta)/Q^2].

The first equation vanishes at integer and half-odd-integer q/Q, but the latter
case has nonzero Q-derivative component `2v/Q^3`. The complete critical
locus is thus p=P=0 with either Q=0 and arbitrary q, or Q nonzero and q=kQ,
k an integer. Each point is a distinct stationary singleton orbit.

The complete control critical loci are:

- A, ARITHMETIC-PHASE-OFF: `p=P=0,Q=0`, arbitrary q.
- D, DIVISOR-FEEDBACK-OFF: `p=P=0` and either Q=0 or q an integer.
- F, FORCE-OFF: `p=P=0`, all q,Q.

All are null continua in full Lebesgue4, with the stationary groups in §2.2.
For every owner, energy zero is precisely its equilibrium set. Here energy
`H_*=0` emphatically does NOT mean return group `H_x=0`: these states have
`H_x=R`.

For integer zero-momentum seeds `(n,d,0,0)`, MAIN is stationary exactly when
d divides n if d is nonzero; all d=0 seeds are stationary without a defined
division readout. A has no stationary seed with d nonzero; D and F make all
integer zero-momentum seeds stationary. These extra control-seed corollaries
were explicit in raw, and follow from the manuscript's complete critical sets;
they need not be repeated as additional manuscript claims.

Thus MAIN genuinely retains the divisibility predicate in its force/critical
equations. This is not a prime-to-primitive correspondence, a lossless symbolic
conjugacy, or a finite-packet-preserving lift. No stationary seed receives an
arbitrarily selected positive period.

### 2.4 MAIN invariant-plane test and free axis

For the FULL `S_alpha={q=alpha,p=0}`, MAIN is invariant only when alpha=0
among the frozen half-integers. If alpha is nonzero, Q=4alpha gives
`sin(2pi alpha/Q)=1` and a nonzero q-force, disproving tangency of the whole
plane. No restricted oscillator is legitimate on such a noninvariant plane.

On S_0 the actual trajectory is `(0,Q_0+Pt,0,P)`. At P=0 it is stationary;
at P nonzero it is the full free Q-line with zero return group. Its complete
incoming orbit stays on that line. Every owner's R_axis similarly has
`(q_0+pt,0,p,0)`: singleton at p=0, full nonperiodic q-line otherwise.
Intersections are counted as actual states, not separate copies of a family.

These tests supply no MAIN nonstationary primitive. They do NOT classify or
exclude general MAIN periodic orbits outside the frozen invariant planes.

### 2.5 A — full four-dimensional source classification

Independently, A has `q=q_0+pt`, constant p, and transverse energy
`e=P^2/2+v(Q)`. If p is nonzero, the complete full-state trajectory is
nonperiodic even when its Q component oscillates. For p=0, q is fixed and:

- e=0 gives the stationary point Q=P=0.
- `0<e<1` gives one connected regular compact oval at that q and e.
- e at least one gives fixed nonzero sign of P and a nonperiodic monotone
  Q trajectory; completeness includes the threshold e=1.

For the middle case, `a(e)=1/sqrt(log(1/e))` and the least period is

    L(e)=4 integral_0^a(e) dQ / sqrt(2(e-v(Q))).

The integrand is regular at zero and has an integrable inverse-square-root
singularity at the simple turning point a. Four monotone quarter traversals
return the complete `(Q,P)` state; no earlier traversal does. This proves the
least period, full LZ isotropy and repetitions, not just one return time.
At a fixed e, all real q give continuum many different equal-period orbits.
They are retained despite the periodic family lying in the null set p=0.

Every S_alpha is invariant for A, indeed for any real alpha. Incoming orbits
are exactly these complete curves. The raw derivation additionally gave an
explicit phase: if `I(Q)=integral_0^Q [2(e-v)]^(-1/2)`, use `I(Q)` on the
rising arc and `L/2-I(Q)` on the falling arc, modulo L. Both turning points
match. For drifting q, q itself supplies an affine time parameter; for unbounded
Q trajectories a signed time integral does so. These optional phase formulas
were not required to be copied into the manuscript.

### 2.6 D — all frozen planes, with general off-plane returns OPEN

Here `W_q=pi v sin(2pi q)` and `W_Q=2v sin^2(pi q)/Q^3` off the axis.
Every frozen S_alpha is invariant. Integer alpha gives a free Q-line system;
P=0 is stationary, and P nonzero is nonperiodic. Half-odd-integer alpha gives
exactly the OWN restricted potential v(Q), with the same derived oscillator
equation and period integral as §2.5.

Consequently each such plane has stationary e=0, genuine primitive periodic
ovals for `0<e<1`, and nonperiodic trajectories for e at least one. All phases,
turning points and time/kernel groups remain. Invertibility excludes off-plane
incoming objects. At fixed e the half-odd-integer planes give countably infinitely
many distinct equal-period orbits; allowing e to vary gives a continuum family.
The equality of reduced equations justifies the equal integral; it is not an
unlicensed control-to-MAIN transfer. General off-plane D periodicity remains OPEN.

### 2.7 F — full classification and own inverse

F has the exact global solution `(q+tp,Q+tP,p,P)`, inverse at negative time,
determinant one and its own every-Borel IMAGE law. Zero momentum gives a
stationary singleton with full real isotropy. Every nonzero velocity gives an
injectively traversed affine line, zero isotropy and no nonstationary period.
Each S_alpha and R_axis is invariant and fully classified by that formula.
Incoming states have the same velocity and lie on the same line, never on a
different equal-energy line. This is a direct solution proof, not an inference
from vanishing sigma.

## 3. Checkpoint 2 — full-manuscript synthesis

The entire 366-line manuscript was read only after ALL RAW FINAL and PAPER
UNLOCK. Its actual hash agrees with the first/released lock in §1. All stated
proofs were checked against the preceding raw derivations, not merely its abstract
or verdict. In particular:

- The flat-extension estimate is locally uniform in q, which is the required
  joint smoothness statement; no invalid global force bound is used.
- Compact-box continuation works for every energy and both time directions,
  including all axes and controls, so the inverse and time domains are complete.
- The determinant argument is all-point, and change of variables supplies the
  full Borel law. Physical time and IMAGE remain separate throughout.
- The half-integer MAIN critical exclusion uses BOTH force components. All
  critical continua, integer signs and zero-denominator axis states remain.
- MAIN's Q=4alpha noninvariance witness is valid for either sign of alpha.
- The oscillator turning amplitude, factor four, endpoint integrability and
  least-period argument are correct. The e=1 case is nonperiodic, not an
  additional closed orbit at infinity.
- A's drifting coordinate excludes full-state returns even when its transverse
  component is periodic. Its classification is global; D's classification is
  limited to the stated planes, while F is globally solved.
- The stated multiplicities, nullness and no-extra-incoming conclusions follow
  from the actual full source and complete inverses, not a selected section.
- The final table and prose retain general MAIN and off-plane D periodicity
  as OPEN. No operator, trace, suspension, or formal Route credit is asserted.

No manuscript correction was found. Raw had additional explicit phase formulas
and integer-control corollaries; their omission is not a proof gap. The first
draft remains unchanged and is not represented as having adopted those extras.

## 4. Checkpoint 3 — strongest positive case and adverse conclusion

The strongest positive case survives: MAIN is a genuine complete smooth
Hamiltonian/symplectic flow on its full declared phase space. Both coordinates
are dynamical, and the division phase supplies an exact arithmetic critical-seed
test. The physical clock is intrinsically the parameter of that actual flow,
not a subsequently inserted roof. Its ownership is not refuted by volume
preservation or by the existence of stationary continua.

The frozen audit nevertheless establishes no MAIN prime-to-nonstationary-primitive
chain. The verified arithmetic witnesses are stationary and have no least
positive return. The bounded invariant-plane follow-up supplies only stationary
or free MAIN trajectories. Neither fact proves that other MAIN periodic orbits
do not exist; no such absence theorem is claimed or needed for the frozen stop.

The controls provide a decisive protection against overstatement: A and selected
D planes have genuine positive physical periods while their IMAGE cocycles are
zero. Their full multiplicities are retained. These positive results cannot be
borrowed as MAIN arithmetic packets, and generic oscillator existence is not
evidence of prime selectivity. Conversely, control oscillations do not establish
a universal impossibility theorem for arithmetic Hamiltonian proposals.

Energy H and return group H_x must stay distinct; in particular the zero-energy
equilibria have H_x=R. Null-state deletion, selecting one energy/q/plane, replacing
physical c by sigma, or assigning a primitive to a stationary source would
change the frozen audit. None is done in the manuscript.

Final standing: no blocking or nonblocking manuscript amendment requested.
The same-object ledger remains intact. `STOP / FORK` is justified by the
precommitted bounded OPEN arithmetic/primitive chain, not a failed Hamiltonian
construction or a global no-periodic-orbit result. Stronger naturalness and
general MAIN periodicity remain OPEN; T3 is not supplied/pursued, classical
ASFS suspension fields are not applicable, formal Routes are UNASSIGNED and B
is NOT INVOKED. No additional cycle census or external verification was performed.
