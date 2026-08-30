# Compilation report

All three revision artifacts were built in two independent temporary trees,
with two LuaLaTeX passes per tree, `TZ=UTC`, and
`SOURCE_DATE_EPOCH=1788048000`.  The two trees produced identical bytes for
each revision; build sidecars remained outside this package.  The release
PDF is byte-identical to `main_round2.pdf`.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `646fea906b5e6a4b03e4a6d2f2dfc8ef087cf10fb6982624346b5c61805b86b0` | 2 |
| `main_round1.pdf` | `ff5c80a1c833385c575065ca68bbfea4b87c9d4160d07caeab44db2fbf59003b` | 3 |
| `main_round2.pdf` | `05d9c83b204730a79476f468ee9746bcede2e52e69e0df2b33fb371a4e18da4f` | 3 |
| `main.pdf` | `05d9c83b204730a79476f468ee9746bcede2e52e69e0df2b33fb371a4e18da4f` | 3 |

The first pass of each fresh tree emits the expected unresolved-reference
and `rerunfilecheck` notices while auxiliary files are being created.  The
second pass has no `Error`, `Overfull`, `Underfull`, undefined-reference, or
rerun warnings.  `pdfinfo` confirms the page counts; `pdffonts` confirms all
22 listed fonts are embedded and subset; `pdftotext` confirms the required
contracted-rotation, itinerary, half-open-boundary, route-boundary, and
scope-boundary phrases.  No LaTeX sidecars are included in the release.
