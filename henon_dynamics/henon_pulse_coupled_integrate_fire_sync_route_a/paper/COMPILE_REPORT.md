# Compilation report

All three revision artifacts were built in two independent temporary trees,
with two LuaLaTeX passes per tree, `TZ=UTC`, and
`SOURCE_DATE_EPOCH=1788048000`.  The two trees produced identical bytes for
each revision; build sidecars remained outside this package.  The release PDF
is byte-identical to `main_round2.pdf`.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `c7cef7cb582f04ea5e9679b077fabd40b7b8d0480e339d82a282f2a5f5daf80d` | 2 |
| `main_round1.pdf` | `9a1ad2c5084089159d945fc65d0b987e82ac0a650d6786889e5805c98936875f` | 2 |
| `main_round2.pdf` | `d618c92d9a47b0221bcd066f388dd72efc003c39ae703028ef402b12d905013d` | 2 |
| `main.pdf` | `d618c92d9a47b0221bcd066f388dd72efc003c39ae703028ef402b12d905013d` | 2 |

The final audit records any first-pass rerun notices separately; the settled
second pass has no undefined references, overfull boxes, or fatal warnings.
Fonts are embedded/subset and extracted text is checked for the event-map and
Route-A boundary phrases.  No LaTeX sidecars are included in the release.
