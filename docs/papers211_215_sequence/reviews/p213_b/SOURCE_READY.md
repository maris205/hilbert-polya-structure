# B source ready for root review — NOT execution authorization

2026-09-11 UTC. Own new-only reviews/p213_b. Source/proof review is complete
at the declared narrow scope; examined mathematical/source defects 0/0/0.
See SOURCE_AND_PROOF.md for actual claim-level reasoning and read limits.
No verifier execution, import, compilation, test, pilot, canonical adoption,
build, page view, host observation, grant, Git, child or external upload
has occurred. Full final review and delta are deliberately not emitted yet.

## Exact requested science scope

verify.py, no imports or external data. All n=1,2,3,4,5,6 and N=0,1,2,3,4:
30 full labelled carriers and 461 states. Complete Boolean words for every
target with n>=3; n<=2 handled directly. No randomization, command-line
parameters, floating point, environment inspection or filesystem operations.
Two-site saturation checks stay within these same carriers and t=0..N.
The checker creates no files. Execution is guarded by __name__ but importing
is NOT authorized as a workaround. Runtime must preserve assertions (no -O).

## Output schema and roles

UTF-8/ASCII line-oriented stdout, LF endings; ordinary print spacing. Order:
header P213_B_OCCUPATION_RELATION_LAYERS_V1; PARAM line; n ascending, N
ascending, states lexicographic. Each STATE line gives n, N, comma vector,
NEXT vector, TIME integer, END vector and PRE semicolon-separated complete
lexicographic predecessor vectors (or '-'). It is followed, for n>=3, by
all CHAMBER lines in increasing bit-code order with bit i encoded at site i:
n, N, target, WORD comma bits, PRE complete source vectors or '-', INTERVALS
semicolon triples (prepeak site, lower, upper), in increasing site order, or
'-'. Empty PRE explicitly means empty chamber; '-' intervals can also mean
a nonempty zero-dimensional chamber. CARRIER lines contain n,N, STATES
count, HEIGHT, LAYERS comma list of new-state counts from depth zero onward,
and MAXFIBRE. Final PASS gives CARRIERS, STATES, CHAMBERS totals.
All complete source lists must be retained, not summarized by count/hash.

Expected successful structural state/carrier counts 461/30 are exact design
requirements, not observed results. Chamber count is computed and emitted;
no hand-filled expected transcript exists. A successful run must exit zero,
have empty stderr and the complete final line; exceptions fail the run.
Canonical role will be canonical_stdout.txt, adopted ONLY from separately
accepted complete actual initial stdout. It is an explicit line-oriented
adapter for inherited CANONICAL.json, never a JSON conversion. Two separately
authorized strict replays and whole raw comparisons must follow. A future
final finding-census adapter may preserve this source-era report unchanged.

## Needed pins and runtime acceptance before any run

INPUT_PINS.sha256 pins all 25 frozen Round1 payloads plus its manifest and
the two internal source originals/A source-read boundary. Freeze payload
digests there originate from the frozen manifest; they must be independently
checked against actual files by root before acceptance. B did freshly read
the manifest hash and selected source hashes, but does not claim it already
ran a complete freeze pin check. The author canonical/PDF are pinned input
roles, not B-adopted results or B-viewed pages.

Root must fully read and accept this source, proof, request and output schema.
Before a new actual initial run, separately resolve and pin exact interpreter,
launch arguments, assertion setting, cwd, relevant ordinary runtime settings,
reviewer source and documentary parameters/schema plus captured launch code.
An ordinary direct-Python trust recipe may be mechanically reused from A
ONLY after acceptance under its unchanged dependencies; do not reuse A
scientific code, results, grants or canonical. No host/proc probing is
authorized by this document. Relevant runtime dependencies/identities remain
unresolved here and are a next-step gate, not missing facts to invent.
Capture complete actual stdout/stderr/exit and before/after relevant keys.
Future source-only build requires separate exact TeX/bib/resource/runtime
pins and actual all-seven-page viewing by B; a PDF hash is not a view.

No general pointwise clock, exact finite maximum/all maximizers, all-time
inverse, global novelty, external endorsement or terminal acceptance claimed.
HOLD_EXTERNAL remains.
