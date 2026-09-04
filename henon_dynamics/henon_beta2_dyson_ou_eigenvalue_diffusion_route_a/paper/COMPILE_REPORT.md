# Compilation report

- Engine: LuaLaTeX.
- Determinism controls: `SOURCE_DATE_EPOCH=1788480000`,
  `FORCE_SOURCE_DATE=1`, and suppressed optional PDF metadata.
- Each checked-in round wrapper was compiled twice in two fresh directories;
  the two byte strings agreed, and page counts increased strictly by round.
- Settled logs: zero warnings, zero overfull boxes, zero underfull boxes, zero
  undefined references, and zero missing characters.
- Fonts: all font rows embedded and subset, including `Droid Sans Fallback`
  for the Chinese abstract and keywords.
- Every page passed 72-dpi rasterization and text-control-byte checks.
- English/Chinese abstracts and both five-to-seven-keyword lists passed text
  extraction.  Each complete round-specific title was present, every other
  round title was absent, and early rounds contained no later-round theorem
  text.

| round | pages | SHA-256 | theorem increment |
|---|---:|---|---|
| 0 | 2 | `a9645564bd8369569a63ba558e70ac007fc443cdedf4f35bdbc4e580c2cfd7eb` | matrix radialization and ordered GUE law |
| 1 | 3 | `613865808c42c7e127c0a5e46ae60c814dcb825dc6e77da6c16fc526b3dae6b3` | determinant/Doob kernel and noncollision |
| 2 | 4 | `00144e9afe6a77226c7e976b74196e76bf361ab15d13bd494c8e9a076bac407a` | complete partition spectrum, gap, trace, and Route-A closure |

`main.pdf` is byte-identical to round 2 and has SHA-256
`00144e9afe6a77226c7e976b74196e76bf361ab15d13bd494c8e9a076bac407a`.
