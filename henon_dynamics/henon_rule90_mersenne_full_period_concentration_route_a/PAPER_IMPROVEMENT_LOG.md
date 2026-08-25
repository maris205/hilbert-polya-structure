# C155 paper improvement log

No external reviewer transport or numeric score was used.  Both rounds were
genuine internal theorem, boundary, and presentation audits followed by
compilation.

## Round 0 to round 1

Findings:

- The first draft inferred fixed-space dependence from finite rows instead of
  proving it for every `r,j`.
- The degree bound was written for time `j`, which would be useless when `j`
  is large, rather than for `d=gcd(j,L)`.
- “Average period” did not state whether states or cycles were sampled.

Repairs:

- Added the polynomial-gcd/Bézout kernel equality.
- Applied the cleared degree bound only after reduction from `j` to `d`.
- Defined the mean as total periodic states divided by total primitive cycles.

## Round 1 to round 2

Findings:

- The union bound needed an explicit argument that every non-full period is
  represented among times `1,...,L-1`.
- Burnside's identity term was not separated from the proper-time error.
- The early case `L=3` has no full-period state and could be mistaken for a
  contradiction to an asymptotic theorem.
- The release draft lacked a Chinese abstract, bilingual keyword sets, and
  the workflow-required declarations.

Repairs:

- Used the previously proved fact that every realized period divides `L`.
- Isolated the `j=0` term `2^(L-1)` before applying the same exponential
  bound to the remainder.
- Stated the result as a limit with a uniform (possibly trivial at small `L`)
  bound; the exact ledger retains the `L=3` exception transparently.
- Added independently structured English/Chinese abstracts, seven keywords
  in each language, and transparent data, ethics, contribution, conflict,
  funding, and AI-use declarations; switched the final build to LuaLaTeX for
  embedded CJK glyphs.

Final internal audit: no unresolved issue remains inside the frozen scope.

## Final typography cross-review

The release cross-review found that a document-wide `small` declaration made
the theorem page unnecessarily dense and left the declarations page sparse.
The global reduction was removed, and a page break before the finite-size
boundary now distributes boundary/validation text and declarations across the
second page.  No mathematical content changed.
