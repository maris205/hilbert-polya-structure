# Fresh residual 07 — bounded candidate handoff

Author: /root/round211_fresh_residual_scout. Date: 2026-09-09 UTC.
Disposition: DEDUCTIVE_AUTHOR_CANDIDATE / FRESH_NONCONTRIBUTOR_GATE_REQUIRED.
This is one provisional literal, not a numbered paper, admission, reserve,
independent PASS or global novelty clearance.

## Result and precise carrier

For n>=1, N>=0, let X(n,N) be all labelled cyclic nonnegative integer
n-tuples of total mass N. With all inputs read simultaneously, set

    q_i = min(a_i,a_(i+1)),
    F(a)_i = a_i-q_i+q_(i-1).

There is no hidden scheduler, additional memory, restricted initial class,
moving carrier or quotient by rotation. This is an abstract receiver-limited
conservative flow; chemical implementability is not asserted.

The complete [author proof](PROOF_PACKAGE.md) supplies this conjunction:

1. The minimum is invariant. After subtracting it, each original positive
   run is absorbed at its original right endpoint. All recurrent states
   are fixed; the full-carrier sharp worst entrance time is zero for
   n<=2 or N=0, ceil(log2 N) for n=3,N>=1, and N-1 for n>=4,N>=1.
2. Every target's one-step fibre is an explicit finite sum over uniquely
   assigned weak-ascent/strict-descent words. Dyadic backward recursion
   fixes every descent, and each long ascent leaves one evaluated integer
   interval. The necessity and sufficiency proofs include all ties,
   wraparound, empty fibres and automatic preservation of the mass constraint.
3. At fixed n>=3, the largest fibre has exact growth degree floor(n/3):
   with k=floor(n/3), for N>=2k,

       (N/(2k))^k <= max_y |F^(-1)(y)| <= (2^n-1)(N+1)^k.

   The lower bound uses a proved exact product for every fixed target;
   each long comparison ascent consumes at least three edges for the upper
   bound. Exact finite-N maxima and all maximizers are not claimed.

The time mechanism is original-run endpoint growth. The inverse and degree
mechanisms are eliminated comparison chambers and packing of independently
free peak/prepeak intervals. The gate must assess both correctness and
whether the residual survives ordinary-method and primary-owner deductions.

## Exactly what was executed

The [pre-pilot contract](PREPILOT_CONTRACT.md) and [source](pilot.py) were
fixed and hashed before the single author process:

    python3 -I -S -B docs/papers211_215_sequence/scouting/finite_residual_fresh07/pilot.py

Native chunk 70be95 exited 0. The unchanged domain is n in {3,4,5} and
N in {0,...,6}: 21 complete carriers and 756 states. The actual output
contains every state, successor, path depth, terminal state and one-step
fibre size, plus carrier summaries. Mass/minimum preservation, permanent
zeros, the predicted terminal map, fixed-state characterization and the
stated worst clocks passed the source's assertions on that box.

[The exact native process return](PILOT_NATIVE.json), specifically its
result.output field, is authoritative: 61,482 ASCII bytes of actual
stdout/stderr text returned by the tool, with no tool truncation.
[The plaintext derivative](PILOT_ACTUAL.txt) is 61,483 bytes, namely that
output followed by one additional LF introduced when the file was written.
It is not advertised as raw-byte identical to stdout. Both original files
are preserved, not silently normalized.

Sections 4–5 of the proof (general inverse, fixed-target product and sharp
fibre degree) were completed AFTER the pilot. They are deductive author
claims, not checked by the saved executable. Printing actual indegrees
does not test those formulas. No inverse implementation, scientific replay,
larger cutoff, n=6 run, independent verifier or manuscript review occurred.
The symbolic n=6 example is explicitly a deduction.

## Scope, sources and ownership

Two substantive non-game entrances were considered: discrete midpoint
geometry/half-sharing and nonlinear conservative resource transport.
The former is an old exact adapter and receives no new literal or credit.
Only the latter was instantiated and piloted. Earlier matching/CIS leads
remain bounded subtraction, not additional new maps or failed-pilot counts.

[Source and collision deductions](SOURCE_AND_COLLISION.md) compare the
actual old UUC, MNA, midpoint, LV, matching and current P211/P212 originals.
[Historical identity pins](INPUTS.sha256) bind the twelve selected files;
[the four immutable pilot-file pins](PILOT_PRESERVATION.sha256) bind the
precontract, script, native output and plaintext derivative.
[Read scope and provenance limits](READ_SCOPE.md) distinguish whole originals,
selected sections, failed accesses, truncated navigation and metadata leads.
[Native local returns](NATIVE_READS.json) preserve actual tool objects, and
[primary access metadata](PRIMARY_ACCESS.json) preserve exact requests and
provider references without republishing bulk copyrighted responses.

The bounded searches did not identify an exact owner in the selected read
surface. This is not an absence proof. The full literal, explicit inverse
or growth degree may still have a primary owner; indirect conjugacies have
not been exhausted. Generic conservation, zero permanence, potential
arguments, current reconstruction, ordered linear chambers and interval
counting receive zero independent novelty credit.

The project's symbolic-dynamics-research workflow governed the two-axis
gate and immutable evidence. Idea/literature/proof and novelty skills
informed the bounded search and claim separation. The novelty skill's
requested separate GPT-5.4 review route was unavailable; none is claimed.
The project-authorized fresh noncontributor gate is still a separate task,
not an author self-review or external expert endorsement.

## Handoff boundary

Only this directory was created or edited. Historical manuscripts, sealed
scouts, accepted reviews, snapshots and failures remain unchanged. P211 and
P212 setups were read solely for subtraction; this scout contributed no
proof to or edit of either retained paper. No central index, Git, SSH,
host configuration, protected runtime, manuscript upload or external contact
was changed. Root alone integrates lifecycle counts and any later admission.

The package is ready for a fresh noncontributor candidate gate after its
complete nonself manifest is checked. Review is specifically asked to test
ties, r=1/r=2 chambers, wraparound, n<=2/N=0 boundaries, interval independence,
the fixed-target exhaustiveness argument, degree lower-bound spacing,
direct ownership and value after standard-method deduction.
The author is not eligible to review this candidate independently.
