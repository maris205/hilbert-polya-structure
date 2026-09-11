# P214 narrative and evidence status

Date: 2026-09-11 UTC. `AUTHOR_DATA_AND_STRICT_PAIR_ACCEPTED /
REPAIRED_INITIAL_ARTIFACT_ACCEPTED_AND_PDF_ADOPTED / PHYSICAL_ROUND0_PENDING`.
This documentary proposal records the post-adoption cutoff only.

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
The manuscript states this limitation explicitly, without treating a
negative literature search as positive novelty evidence.

For m>=3 there are positive fibres of sizes q and q^(m-1). Every finite-
group endomorphism has constant positive fibre size, so F cannot be
bijectively conjugate to one. This makes the linear comparison mathematically
meaningful without proving absence of arbitrary nonlinear factors.

## Evidence and experiment boundary

All five items of the root's frozen theorem contract have complete accepted
candidate-stage deductions. Manuscript-level reviews are not yet performed.
The accepted author source retains the fixed box q in {2,3,4}, m in {2,3,4};
F4 is the field defined by an irreducible quadratic over F2, not Z/4Z.
The prescribed 84+819+4368=5271 states are now covered by an actual accepted
finite run: all states, literal transitions, orbit-derived depths and all
5271 target predecessor lists, including empty ones, in 10646 records.
[Complete DATA reception](../../docs/papers211_215_sequence/qa/p214_author_data_root01/RECEPTION.md)
records independent and root reconstruction with 381643 assertions and
all 211105 named producer comparisons. The actual full JSONL role is
CANONICAL.json, 10,419,112 bytes, SHA256
4ebeac267f855a1f9b03263ed2517d7a34b6dd0b62639b9fa54129c136763c35.
[Actual canonical adoption](../../docs/papers211_215_sequence/qa/p214_author_data_root01/CANONICAL_ADOPTION.md)
and [two real strict replays](../../docs/papers211_215_sequence/qa/p214_runtime_root01/PAIR_RECEPTION.md)
are separately received; both entire streams match canonical RAW bytes.
Their complete finite semantics are explicitly reused under unchanged
scientific/dependency keys, not reconstructed anew by this task. Finite
checks pressure the formulas; they do not prove the all-q,m theorems.

The [first artifact HOLD](../../docs/papers211_215_sequence/qa/p214_initial_artifact_root01/RECEPTION.md)
preserves the six-page first PDF and six diagnostic occurrences of one
overfull inline-product cause, with original classifications intact.
The [exact two-file display/status repair](../../docs/papers211_215_sequence/qa/p214_display_repair_binding01/SOURCE_RECEPTION.md)
was actually adopted and built at 3a4987/session1244/cf150d, exit zero.
Root [actually viewed all seven new pages](../../docs/papers211_215_sequence/qa/p214_display_repair_binding01/PAGE_VIEWS.md):
the product is fully within the text block and no new visual defect was
observed. The seventh page contains the complete second reference; the
old 4–6 page target was an intention, not a cap. The new 191537-byte PDF
has SHA256 ca77a57c47b81c26a2c7beca37c49b58137196f0a50f5baecb2d2283ff7f3bfd.
[Complete repaired artifact reception](../../docs/papers211_215_sequence/qa/p214_display_repair_artifact_root01/RECEPTION.md)
now accepts both full 952992-byte reports, each with 4367 checks and zero
findings, together with the seven actual root page views. The original visual
Minor cause is CLOSED for this repaired version only; the initial HOLD and
six generic Major diagnostic records are not erased or converted into PASS.
[Actual PDF adoption](../../docs/papers211_215_sequence/qa/p214_display_repair_artifact_root01/PDF_ADOPTION.md)
and its [complete native record](../../docs/papers211_215_sequence/qa/p214_display_repair_artifact_root01/PDF_ADOPTION_NATIVE.json)
record exclusive copy to paper-root main.pdf after absence checks and a full
RAW comparison at 700490, exit zero. The adopted PDF retains the ca77a57c
identity above. These are received artifacts, not another build or page view
by this task; neither supplies manuscript-review or terminal-build credit.

Historical source handoff, proof/source/protocol plans and their original
seals are not rewritten. The latest pre-lifecycle 28-source key is
qa/p214_display_repair_binding01/ADOPTED_SOURCE_INPUTS.sha256, following the
two-file repair; qa/p214_source_root01/ADOPTED_SOURCE_INPUTS.sha256 predates
it. These qa/ paths are relative to docs/papers211_215_sequence/.
After applying these three lifecycle proposals, a new current input
binding is required. Physical Round0 still requires accepted/applied lifecycle
delta, that new binding, actual separately granted copying and root reception. Review
A, accepted delta/Round1, distinct B, accepted delta/Round2, two physical
terminal builds and final paper/batch checks remain unperformed gates.
Runtime, build and physical-freeze grants stay separate from SOURCE preparation.

## Provenance and scope

The admission contract and reception are in
`docs/papers211_215_sequence/qa/fresh55_root_reception01/`. The original
Fresh55 author and noncontributor gate packages remain unchanged.
The scout, root's cancellation challenge/clarification, and the collision
contributor's P/Q adapter are proof authorship. Verifier/source contributors
are listed in README. None is presented as a nonauthor manuscript
reviewer. Anonymous publication text contains no operational agent names.

No theorem beyond R=F_q[t]/(t^m) on the full I² is promised. There is no
all-time inverse theorem, graph-isomorphism classification, general chain-ring
extension, new general contraction principle or global priority claim.
External release and specialist contact remain `HOLD_EXTERNAL`.
