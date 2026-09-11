# P213 A independent source handoff — no execution authority

2026-09-11. Reviewer /root/p213_manuscript_review_a is a fresh nonauthor
process, with no prior candidate/proof/verifier contribution or familiarity.
Current-model/reasoning inheritance is used; this is not blind, cross-model,
external or specialist review. Ownership is only this review directory.

The source verify.py is newly written and has NOT been imported, executed,
compiled or AST-parsed. No canonical, replay PASS, build PASS or accepted
manuscript delta exists in this package at this milestone.

## Exact method and parameters

Fixed full box n=1..6, N=0..4, all labelled weak compositions, no rotation
quotient; expected 30 carriers and 461 states. Base-(N+1) digit enumeration
generates the cube and filters its mass-N layer, unlike the author's recursive
composition generator. The direct update uses positive-part retention plus
incoming minimum, evaluated from old coordinates. Indegree peeling isolates
all recurrent vertices, then reverse peel order assigns terminal labels and
depths to the whole forest. No per-start orbit stopping assumption supplies
the recurrent classification.

The independent inverse enumerates the bounded current cube 0<=c_i<=N and
sets a_i=y_i+c_i-c_(i-1). It accepts nonnegative a exactly when both slacks
a_i-c_i and a_(i+1)-c_i are nonnegative and their product is zero. These
conditions are equivalent to c_i=min(a_i,a_(i+1)); each source has one such
current. Telescoping gives the mass without a source-composition filter.
This is deliberately a different representation from the author atlas;
no author function, pilot, canonical or candidate implementation is imported
or copied. It is not advertised as an O(n2^n) algorithm. The interval-atlas
formula itself is checked deductively in SOURCE_AND_PROOF.md, while this
independent numerical lane reconstructs every exact inverse set from fluxes.

Checks cover all vertices/arrows, recurrent=fixed, minimum and residual zeros,
terminal formula, exact full-carrier height, n<=2 identity, n=3 doubled
two-site trajectory including one post-fixation step, fixed fibre products,
upper bounds and all applicable lower witnesses. No all-parameter proof is
inferred from this box. No new larger experiment is requested.

## Output and dependencies

Only verify.py is scientific executable source. It imports nothing and reads
no input files, canonical, parameters, command arguments, environment, clock,
randomness, network or processes. Integer/tuple/list/dict operations, sorted,
generators, builtin exceptions and print are required. Documentary parameters
are fixed above and hard-coded in source. Interpreter/startup/native/transport
identities and launch contract remain for root to bind explicitly, with an
ordinary trusted-runtime boundary; zero imports does not close runtime.

Proposed isolated invocation after acceptance: resolved Python 3 with -I -S -B,
exact pinned verify.py and no script arguments, in a root-selected directory.
No concrete interpreter path or successful runtime claim is invented here.
Root must receive source/parameters/dependencies before any such invocation.

Success stdout is ASCII LF-delimited, final LF, no blank lines: header
P213_A_CURRENT_FOREST_V1; PARAM n=1..6 N=0..4; 461 STATE records ordered by
n then N then lexicographic state; one CARRIER after each carrier's states;
TOTAL; PASS. Each STATE prints full state, successor, tau, terminal and sorted
complete sources. Vectors are comma-separated decimals, source lists use
semicolon, empty list is '-'. CARRIER prints states, height, maximum indegree
and recurrent count. All computations finish before print. Any exception,
nonzero exit, stderr or truncated capture fails. No numerical expected table
or output bytes are prefilled. Prospective canonical role is CANONICAL.json
under the inherited A-review contract, storing exact actual stdout bytes
despite its basename; root should explicitly accept that role or choose the
line-oriented canonical_stdout.txt adapter before adoption, never convert.

Scientific initial run, raw reception, canonical adoption, separate strict
pair, actual manuscript/build review and accepted delta remain future gates.
OWNER_AMBER / HOLD_EXTERNAL; current round only.
