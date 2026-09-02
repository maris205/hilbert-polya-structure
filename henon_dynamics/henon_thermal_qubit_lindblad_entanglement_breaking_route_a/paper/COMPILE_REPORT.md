# Deterministic compile report

Engine: LuaLaTeX. Frozen environment:
`SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

Each revision round was built for two passes in each of two isolated fresh
directories. The two builds of every round were byte-identical to the archived
artifact. Settled logs contain no LaTeX/package warning, overfull or underfull
box, undefined reference/citation, rerun request, or missing character.

| Round | Pages | Bytes | Embedded/subset font rows | SHA-256 |
|---|---:|---:|---:|---|
| original | 2 | 171487 | 23 | `a76618c30507dbae459d920e98d60e796278de712cea42dc6113e3dee209948a` |
| revision 1 | 3 | 180407 | 23 | `e2a467c3f76a6b77e0eacaa243a664ff0b74b2378e21df7bf8f9f1b1a422576b` |
| revision 2 | 3 | 190391 | 24 | `16c82784cff2f4cbe661938e425c5065dd77ee4de220f9caaa3ff1d7c6a9c544` |

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf`. The three
archive hashes are pairwise distinct. All eight archived pages rasterize to
nonempty PNG files; visual inspection found no clipping, overlap, orphaned
lines, or blank spill page.
