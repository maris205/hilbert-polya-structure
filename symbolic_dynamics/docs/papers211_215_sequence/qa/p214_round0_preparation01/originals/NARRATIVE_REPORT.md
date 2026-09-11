# P214 narrative and evidence status

Date: 2026-09-11 UTC. `ADMITTED / SOURCE_PREPARATION / NO_SCI_OR_BUILD`.

## The technical story

Let R=F_q[t]/(t^m), I=tR, m>=2. The map F(x,y)=(y,x(t+y)) is nonlinear
when m>=3. Both registers lie in a nilpotent ideal, so decay is plausible,
but that observation alone neither determines the exact full-state deadline
nor handles cancellation in t+y. The initial condition (t,-t) kills one
chain immediately. It does not shorten the total deadline because the other
chain is the last one to survive.

Writing F^n(x,y)=(x_n,x_(n+1)) reveals the decisive fact: every x_n with
n>=2 lies in t²R. Every multiplier t+x_n from that point on has valuation
one. If v(y)>=2, both parity chains have exact valuation increments. If
v(y)=1, the odd chain has exact increments and dominates the potentially
accelerated even chain. The resulting first hitting time is

    max{2(m-v(y)), 2(m-v(x))-1},     with v(0)=m.

The maximum is 2m-2, with equality exactly at v(y)=1. The number of states
at depth at most h is q^h for 0<=h<=2m-2. These are one theorem and its
counting corollaries, not several unrelated contributions.

The inverse question is different but elementary. A target (u,w) fixes the
second source register at u and leaves x(t+u)=w in the ideal I. If
d=min(v(t+u),m-1), its image is t^(d+1)R and its kernel has q^d elements.
The saturated d=m-1 branch must be counted inside I; using the full-ring
annihilator would overcount when t+u=0. This gives every target fibre and
the complete distribution, including the q maximizing targets.

## What is and is not advanced

The map L(x,y)=(y,tx) already has the identical pointwise valuation clock
and depth distribution. Their numerical shapes are not new. The contribution
is a proof that the explicit nonlinear feedback retains them despite the
initial cancellation branch. At m=2 the nonlinear term vanishes, so this
entire boundary subfamily is only the linear control.

The inverse mechanism is entirely deducted. On I² take M(a,b)=(b,ab),
P(x,y)=(x,y+t), Q(u,w)=(u-t,w). The identity F=QMP transfers every one-step
fibre from multiplication. Q is not P^-1, so this does not transfer iterates.
The manuscript will state this limitation explicitly, without treating a
negative literature search as positive novelty evidence.

For m>=3 there are positive fibres of sizes q and q^(m-1). Every finite-
group endomorphism has constant positive fibre size, so F cannot be
bijectively conjugate to one. This makes the linear comparison mathematically
meaningful without proving absence of arbitrary nonlinear factors.

## Evidence and experiment boundary

All five items of the root's frozen theorem contract have complete accepted
candidate-stage deductions. Manuscript-level reviews are not yet performed.
The author verifier is being prepared only as SOURCE. Its fixed box is
q in {2,3,4}, m in {2,3,4}; F4 must be the field defined by an irreducible
quadratic over F2, not Z/4Z. The prescribed carriers contain deductively
84+819+4368=5271 states in total. This is a parameter count, not a measured
run. The verifier must emit all states, literal transitions, orbit-derived
depths and all target predecessor lists, not merely aggregate totals.

No scientific import/run, canonical output, build, PDF, page measurement or
visual review exists for this initial source handoff. Finite checks, once
authorized, will pressure the formulas; they will not prove the all-q,m
theorems. Runtime and build grants remain separate from source acceptance.

## Provenance and scope

The admission contract and reception are in
`docs/papers211_215_sequence/qa/fresh55_root_reception01/`. The original
Fresh55 author and noncontributor gate packages remain unchanged.
The scout, root's cancellation challenge/clarification, and the collision
contributor's P/Q adapter are proof authorship. Verifier/source contributors
will be listed in README. None is presented as a nonauthor manuscript
reviewer. Anonymous publication text contains no operational agent names.

No theorem beyond R=F_q[t]/(t^m) on the full I² is promised. There is no
all-time inverse theorem, graph-isomorphism classification, general chain-ring
extension, new general contraction principle or global priority claim.
External release and specialist contact remain `HOLD_EXTERNAL`.
