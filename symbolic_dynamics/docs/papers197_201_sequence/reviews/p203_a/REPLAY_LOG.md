# P203 A actual formal replay pair

Both processes ran the unchanged verify_signed_correlations.py after the
physical Round0 intake and original input pin freeze. Its earlier exploratory
run is disclosed in PREPARATION.md and does not count as this pair.

- Replay 1:2026-09-05T08:18:11.169015+00:00 to08:19:00.766407+00:00,
  measured49.597401seconds, subprocess exit0, empty stderr.
- Replay 2:2026-09-05T08:18:12.356415+00:00 to08:19:01.724864+00:00,
  measured49.368458seconds, subprocess exit0, empty stderr.

The actual wrapper captured start/end UTC, monotonic duration, subprocess
status and complete stdout/stderr as JSON. Tool sessions24707/7395 completed
with those observations. The two full stdout strings were byte-identical;
their actual text was saved with apply_patch as REPLAY1/2 and CANONICAL,
then physical cmp checks exited0. Each has1498484 assertions.

Verifier SHA-256:
66a12b737eaa8428389f00ec951e0fb2e844dfa96b3491ef8d8e37138b466d67.
Canonical/replay stdout SHA-256:
0a05cc3f14a56db28afa6084cac6301d06d1b957d1119d387c8dc367df518d9a.

Scope:all33868 labelled states n0..6; full source SET comparison; every
star/four-set certificate; composition-power recurrent discovery and exact
binary-jump entry; sharp witness n3..80; both inverse witnesses and colours
n4..24. No fulln7, random experiment or all-n proof is inferred from these
numbers. The correlation implementation has no file I/O or upstream imports.
The scope-only A-M1 repair changes no literal, theorem, code or canonical.
The final accepted manuscript finding census belongs to the hashed review
report, not the verifier's explicitly finite NOT_A_REVIEW_VERDICT footer.
