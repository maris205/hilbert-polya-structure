# Deterministic manuscript build — C297

The single conditional source was built for rounds 0, 1, and 2.  Each round
was compiled twice in two isolated temporary directories, with two LuaLaTeX
passes per build, under:

```text
SOURCE_DATE_EPOCH=1788307200
FORCE_SOURCE_DATE=1
TZ=UTC
```

Both builds of each round were byte-identical.  The settled-log warning regex
found no LaTeX/package warning, overfull/underfull box, unresolved reference,
rerun request, or missing character.

| artifact | pages | embedded/subset font rows | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 1 | 22 | `e10307506e636527f3296fda541e627b6c17b704c059eb3c2845054beb87ccb2` |
| `main_round1.pdf` | 2 | 21 | `3208737429a4d28a18f399d038271a4b74ea2b7b9851887c627033dade1c337d` |
| `main_round2.pdf` | 3 | 22 | `a6122768fabaa99cfa3ab62ef28384a5360103c029ce4393fe94f16d4537fc82` |

All pages render, all fonts are embedded and subset, and round-specific text
sentinels are present, including `HEN-O281` and `52 hostile` in the release
round.  `main.pdf` is byte-identical to `main_round2.pdf`.
The three hashes are distinct, confirming two substantive revisions.
