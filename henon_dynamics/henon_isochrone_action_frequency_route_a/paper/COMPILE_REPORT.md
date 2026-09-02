# Deterministic compile report

## Contract

- Engine: LuaLaTeX.
- Fixed environment: `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Two LuaLaTeX passes per build.
- Two isolated directories for each of three substantive rounds: six fresh builds total.
- Each same-round pair was byte-identical.
- The settled warning regex found no LaTeX/package warning, overfull/underfull box, undefined reference/citation, rerun request, or missing character.
- `pdffonts` reported every font embedded and subset.
- `pdftotext -layout` satisfied round-specific text contracts.
- Every final-round page was rasterized and visually inspected: PASS.

## Artifacts

| Round | Pages | Embedded/subset font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 16 | `959003cf32111953109f9a64875503805f120bf7bdd1310c62269db34a3fcd79` |
| 1 | 3 | 21 | `d81c873e253e1505f316844fc27ad0cb6cd972e60736fe926d0de4f4c2cb691f` |
| 2 | 4 | 22 | `e89f5fa8ba9d9b2148f7d15d2b1d48d6767681278ff6c123fd61f2e673b87f3b` |

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf` and has SHA-256 `e89f5fa8ba9d9b2148f7d15d2b1d48d6767681278ff6c123fd61f2e673b87f3b`.

The substantive progression is visible in the page sequence and text contracts: round 0 closes the core energy/action/period theorem; round 1 adds the apsidal closure proof and boundary atlas; round 2 adds exact evidence, adversarial validation, natural quantization, Route-A interpretation, limitations, and declarations.
