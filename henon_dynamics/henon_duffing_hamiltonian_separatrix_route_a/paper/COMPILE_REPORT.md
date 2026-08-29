# C232 compile report

- Engine: LuaLaTeX; two passes per revision.
- Fixed environment: `SOURCE_DATE_EPOCH=1787875200`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Two independent fresh build directories were run for each of revisions 0, 1
  and 2; every pair is byte-identical.  Settled logs have zero warnings,
  overfull/underfull boxes, undefined references, missing characters or errors.
- Page counts: round 0 = 2, round 1 = 2, round 2/final = 3; A4.
- Final font audit: 16 entries, every font embedded and subset.
- Extracted-text and visual page audit: PASS; `main.pdf` equals
  `main_round2.pdf` byte-for-byte.
- No LaTeX sidecars are retained in the release directory.

## SHA-256

```text
main_round0_original.pdf  8b29d1b401b99099b8291e80ab60f3da9b2df985234914e35280004adf72e15d
main_round1.pdf           f1acdaaedc0293677c3098920fa06efcb79daea3ca8f4287173182feff4cba28
main_round2.pdf           3846c1d9fd6ffc59249bc886157cc26e5ec335e35633546a22e770e36e23c455
main.pdf                  3846c1d9fd6ffc59249bc886157cc26e5ec335e35633546a22e770e36e23c455
```
