# Source, collision and replay provenance

2026-09-06 UTC. This is author-owned bounded scouting. It does not claim
an external review, global novelty clearance, a paper gate or a specialist
opinion. `HOLD_EXTERNAL` remains unchanged.

## Sources actually used

| Source and status | Actual read scope | What is deducted, and what is not licensed |
|---|---|---|
| Shay Moran, *Shattering Extremal Systems*, Saarland master's thesis (2012), [arXiv:1211.2980](https://arxiv.org/pdf/1211.2980) | Title / contents / introduction; printed pp. 3–6, Definitions 2.7–2.8, Lemma 2.9 and Theorem 3.3 | Owns the shattered / strongly shattered statistics, their duality and the Sandwich framework. It was not read as a theorem about iterating their set difference. |
| Christine Heitsch, *Counting orbits under Kreweras complementation*, preprint (2023), [arXiv:2303.12240](https://arxiv.org/pdf/2303.12240) | PDF pp. 1–3 and printed p. 4 orbit statement; noncrossing definition, rotation identity, tree adapter and orbit-length restrictions | The noncrossing AKC core and its orbit enumeration are owned. This does not prove attraction from every crossing partition under cycle-support canonicalization. |
| Petra Laketa and Stanislav Nagy, *Halfspace depth for general measures: The ray basis theorem and its consequences*, preprint v1 (2021), [arXiv:2106.00616](https://arxiv.org/pdf/2106.00616) | PDF pp. 1–3; depth Definition (1), convex depth regions, intersection identity (2), empirical-measure scope | Owns the static depth-region/median construction. Our finite-grid feedback deduction is only nested convex-region erosion. No smooth-density assumption from the later ray-basis theorem is imported. |
| Khaled Elbassioni and Imran Rauf, *Polynomial-time dualization of r-exact hypergraphs with applications in geometry*, Discrete Mathematics 310 (2010), 2356–2363, [publisher record and introduction](https://doi.org/10.1016/j.disc.2010.05.017) | Publisher-indexed primary title, abstract and opening introduction, not a complete PDF | Supplies the ordinary inclusion-minimal transversal/dual-hypergraph convention. The minimum-cardinality filter is distinguished explicitly; the source is not asserted to own or solve its iterates. |

These primary readings establish occupied primitives, not the novelty of
anything left over. The UPC reduction is written out elementarily in
`PROOF_BOUNDARIES.md`; it does not rely on a named theorem beyond finite
poset closure facts proved there. Negative credit is based on a complete
adapter, not a claim that a keyword search found the exact UPC article.

Literature retrieval followed the symbolic research and research-lit
skills: local history and paper-name relevance first, then targeted web
primary sources. Optional Zotero and Obsidian providers were unavailable;
the prescribed arXiv fetch helper was not found, so arXiv web retrieval
was used. No PDFs were downloaded into the paper library. One attempted
Helsinki PODS97 full-text retrieval timed out, and a direct publisher
open failed; neither is represented as a complete paper reading. An
incorrect guessed publisher PII also failed and supplied no evidence.
The successful publisher-indexed text listed above is the limited
fallback for transversal definitions. Third-party result snippets were
discovery only, not proof inputs.

## Exact local collisions and adapter checks

The following historical files were inspected directly and are pinned in
`INPUT_PINS.sha256` using paths relative to the workspace root:

- `docs/papers187_191_sequence/scouting/graph_lane/replacement/CANDIDATES.md`,
  RX09/UCH: its literal is exactly UZ, including all hypergraphs.
- The accompanying `KILL_LEDGER.md`, RX09: image 1,447, fixed 32,
  periods one/two and height two at ground size four. The current run
  reproduces that collision; it does not reopen the candidate.
- `docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md`,
  section 12/KRC: its carrier is noncrossing partitions only, and its
  ground-size-eight cycle census exactly matches the known AKC core.

The old ledger also distinguishes RX07/E2C (unique two-step witness)
from UPC (unique path across all positive lengths). This distinction
does not save UPC: its full closure-generator adapter independently
deducts both axes. UD is output-complemented old UZ, hence has the
identical inverse problem after relabelling targets, but it is not
asserted to be conjugate in time. MHT is not the ordinary minimal
transversal blocker; it is a rank-filtered probe, and its rank and
unsatisfiable-boundary deductions still earn no independent axis.

The late UZ hit occurred after the original pilot. `INTAKE.md` retains
that correction and separately declares MHT before its own pilot.
Pre-MHT literal search in scouting Markdown used the patterns minimum
transversal, minimum hitting set and minimum blocker, with no exact
literal hit. Searches are finite discovery work, not exhaustive owner
clearance. No failed or duplicate row is removed from the denominator.

## Executable inputs and bounded carriers

`pilot.py` is the original unchanged six-literal, 41-box program.
It is self-contained Python standard-library code. The full-functional-
graph profiler is adapted from the author's earlier scout profilers;
it is not an independent review implementation. All carriers include
the empty case and every state of the declared box. No random samples,
external data, imported scientific modules, approximate geometry or
floating-point calculations are used.

`replacement_pilot.py` imports that exact local `pilot.py` for the
functional-graph profiler and defines only the MHT rule. Therefore both
scripts are scientific dependencies of the replacement output. It is
five separately declared boxes, not an enlargement of an old cutoff.

`proof_checks.py` imports no pilot code. It uses exact, uncapped integer
path counts, independently builds the UPC reachability/interval posets,
enumerates each complete inverse fibre and compares summary facts to
`CANONICAL.json`. The latter file is therefore an explicit input, not
an unmentioned expected table. This is a distinct author audit route,
not an independent person or process-separated paper review.

## Actual replay record

The first baseline execution and then an actual fresh pair each
completed successfully. The fresh baseline pair had child exits
`[0,0]`, empty stderr, 23,335 stdout bytes each, and raw-byte equality.
Its canonical SHA-256 is
`8a6a2ac98ef0a1864406f007c9ddebf7cf7f3f74bdac6b0aed5cf3beb68e19b8`.
The preserved `CANONICAL.json` has that identical physical byte hash.

MHT and UPC author checks each had a first execution followed by an
actual fresh pair. Each pair had child exits `[0,0]`, empty stderr and
raw-byte equality. Their complete stdout is preserved separately:

| Executable | Canonical stdout | Bytes | Assertions per child |
|---|---|---:|---:|
| `pilot.py` | `CANONICAL.json` | 23,335 | 482,974 |
| `replacement_pilot.py` | `REPLACEMENT_CANONICAL.json` | 3,003 | 131,638 |
| `proof_checks.py` | `PROOF_CHECKS_CANONICAL.json` | 1,423 | 288,849 |

The baseline scans 241,420 state/map pairs in 41 boxes. MHT adds
65,814 in five boxes, for 307,234 pairs in 46 executed literal boxes.
The extra UPC proof audit revisits 33,868 original UPC states; it does
not add a candidate, expand a cutoff or increase that pilot denominator.
Assertions are literal executed checks, not a count of distinct theorems.

`audit_replay.py` provides the final reproducible receipt: run from the
workspace with `python3 -B` and the file path. It checks source and
canonical hashes before/after, launches every script twice, compares
each pair as raw bytes and compares both to the physical canonical.
Its saved complete stdout is `REPLAY_CANONICAL.json`. This final gate
is a fresh execution, not merely a hash refresh. Commands, interpreter
version, return codes, stderr sizes, stdout sizes, and dependency hashes
are in that receipt. No canonical is regenerated by the replay auditor.

The package's `ARTIFACT_MANIFEST.sha256` covers every persistent regular
file except itself. Local interpreter `__pycache__` files are generated
caches, excluded explicitly; `-B` prevents new ones during the final
replay. Historical input pins and the complete package manifest are
separate scopes. No central index, previous package, numbered paper,
Git path or external service was written by this lane.
