# C239 compile report

Build contract: LuaLaTeX (LuaHBTeX 1.14.0), fixed
`SOURCE_DATE_EPOCH=1788048000`, two settled passes in each of two independent
fresh directories per revision.  Settled logs were scanned for errors,
undefined references/citations, overfull or underfull boxes, duplicate
destinations, and missing characters; all scans were empty.  The final PDF
fonts are embedded and subset.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `8d4ddf0cd25703eabbb245dde84198209eb058d7cd8309f75dcc6dc83532d356` |
| `main_round1.pdf` | 2 | `8d7bf23de5422540f28796cd6e0a26f843f10157122c7690a9afd020fe63b823` |
| `main_round2.pdf` | 2 | `f84034336987de2f5c6889528d9fd845ebac8a722622127568db616c36529130` |
| `main.pdf` | 2 | `f84034336987de2f5c6889528d9fd845ebac8a722622127568db616c36529130` |

The three round hashes are distinct and `main.pdf` is byte-identical to
`main_round2.pdf`.  Round 1 adds literal packet/gcd evidence; round 2 adds
the independent receipt and explicit A0/A2 boundary.  Both fresh builds per
round were byte-identical.  No build sidecars are retained in the release
directory.
