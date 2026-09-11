# Bounded read-only helper scope

Date: 2026-09-07 UTC. Helper: `incidence_desk`. It was assigned at most
one genuine constrained-labelled-structure description, with the parent's
current exclusions, no files, no science execution, no further children,
and an instruction to stop promptly to free a manuscript-review slot.
It reported **NO_FRESH_SLATE**, zero new maps, zero pilots, zero files,
and then became idle. It did not author any LBR proof or independent gate.

## Local access reported by the helper

All paths below are relative to the workspace root.

| Original | Actual extent |
|---|---|
| `docs/papers204_208_sequence/scouting/combinatorial/SCOUT_REPORT.md` | Complete, lines 1–74 |
| `docs/papers204_208_sequence/scouting/combinatorial/SOURCE_AND_COLLISION_NOTES.md` | Complete, lines 1–78 |
| `docs/papers204_208_sequence/scouting/combinatorial/PROOF_NOTES.md` | Complete C08 argument, lines 93–103; surrounding 105–110 |
| `docs/papers197_201_sequence/scouting/word_poset_lane/COLLISION_FIREWALL.md` | Lines 33–49 |
| `docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md` | Keyword-match lines 86, 109–110, 113, 117, 248, 301 only |

The first content search used the explicit four-file allowlist consisting
of the first two files, the firewall, and the eighteenth proof file, with
the expression `(tableau|RSK|Knuth|jeu|promotion|matching|uncross|partition)`.
A second search used only the exact `combinatorial/PROOF_NOTES.md` path.
No broad root search, `head` truncation, or review/capsule exposure occurred
in this helper task. An empty `sed 145,230` request against the 110-line
proof file returned no body and was corrected to the C08 range; it was
not treated as a full read. Main separately read the full local C08
proof file, report, source memo and firewall before using their arguments.

## Public source work reported by the helper

Queries were exactly:

- `site.cambridge.org "Bender–Knuth billiards in Coxeter groups"`;
- `site.arxiv.org tableau "rectification" "Knuth" "row reading"`.

Only public terminology was sent. The publisher HTML for the Bender–Knuth
paper failed with a content-length-too-large error. That failed HTML
opening is not counted as a body read. Its successful publisher PDF
supplied the actual source comparison: complete Section 1.1 at extracted
lines 69–122, Theorem 1.22 through Remark 1.26 at 464–503, and the
displayed proofs of 1.22/1.24 at 1215–1230. The underlying separator
machinery was not completely read; no independent verification of all
theorem dependencies is claimed.

Main subsequently retrieved the PDF into this directory with recorded
curl/headers/stdout/stderr/hash receipts, and read the corresponding local
body ranges specified in `SOURCE_AND_HISTORY.md`. The helper did not save
its browser failure as a physical HTTP payload; this reported limitation
is not retroactively relabeled as a raw download receipt.

No P208/P209/FTH/OFS science was read or changed in this line. No helper
result is presented as an independent review or general absence theorem.
