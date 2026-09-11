# Fourth intake actual execution and integrity record

Date: 2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`.
Author checks only; no independent candidate or manuscript review.

Runtime actually queried with `python -VV`:

    Python 3.12.3 | packaged by Anaconda, Inc. |
    (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]

Both scripts are deterministic standard-library-only CPU programs. They
import no repository code, canonical data or prior verifier. The `-B`
flag prevents bytecode artifacts. No random seed or external data is used.

## Pilot

Executed in two fresh interpreter processes:

    python -B docs/papers204_208_sequence/scouting/algebra_fourth/pilot.py

Both completed with exit 0. The complete output is the 41-row
PILOT_CANONICAL.jsonl, covering 15,089 state instances. Original captured
outputs agreed; later direct byte checks below passed. EC and CP built-in
controls pass; MG's control only verifies cardinality preservation; other
map controls are explicitly labelled not_claimed. The functional graph is
computed from a complete literal successor array by path walking, detecting
cycle entry, and propagating tails backward, without theorem-derived depths.

Two actual additional fresh byte comparisons were run after artifact
creation, each exit 0 with empty stdout:

    cmp docs/papers204_208_sequence/scouting/algebra_fourth/PILOT_CANONICAL.jsonl <(python -B docs/papers204_208_sequence/scouting/algebra_fourth/pilot.py)

Canonical SHA-256:

    f3e0e12d9006272bfa16681e0c6d125bececce045ec602357b9733df5362a3c2

## Structural and collision controls

After the EC deductive proof and CP/OR adapters were obtained, executed:

    python -B docs/papers204_208_sequence/scouting/algebra_fourth/verify_structure.py

The initial development execution passed. Two further fresh interpreters
both exited 0 and produced the complete identical stdout preserved as
STRUCTURE_CANONICAL.json. Total assertions: 139,395. These include complete
source-set equality for EC/CP/OR, not just equal counts; EC endpoint/diameter/
support identities and all extremizers; and exact OR tableau coordinates.
30 EC boxes contain 15,029 target states. The 462 geometric-support checks
are explicit witnesses through n=33 and M=2^30, not those huge full carriers.

Two actual additional fresh raw-byte comparisons each returned exit 0,
empty stdout:

    cmp docs/papers204_208_sequence/scouting/algebra_fourth/STRUCTURE_CANONICAL.json <(python -B docs/papers204_208_sequence/scouting/algebra_fourth/verify_structure.py)

Canonical SHA-256:

    267c1980da1f0bf20d6a2cc65adbabf6005e8bc60e56b6253d8b953caa6ef9d3

## Documentary limits and closure

The package's complete nonself file manifest is SHA256SUMS. It includes
the literal pilot, complete actual output, structural script/output,
EC proof, other-map adapters, source boundaries, scout report and this log.
Only documentary disposition text changed after the successful scripts;
neither executable nor canonical was changed afterward.

The attempted `jq` convenience summary failed because jq is unavailable.
No result relies on it: the complete JSONL was subsequently read and parsed
to obtain the 41/15,089 totals. Several primary browser fetches timed out;
their successful read fallbacks and still-unavailable fulltexts are stated
in SOURCE_AND_COLLISION_NOTES.md, without converting a failed fetch into a
full read. No PDF manuscript build, author/source edit outside this lane,
external reviewer, contact or Git synchronization was performed here.

Final scientific outcome: six author NO_PROMOTION dispositions, zero
reserves/admissions. Valid proofs are preserved despite the adverse value
judgment. The remaining temporal EC theorem is not a two-axis paper.
