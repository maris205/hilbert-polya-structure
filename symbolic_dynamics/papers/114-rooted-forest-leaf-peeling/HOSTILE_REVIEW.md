# Consolidated hostile-review resolution — P114

Resolution date: 2026-08-29 UTC  
Internal verdict: **GO_INTERNAL**  
External posting, submission, novelty, and priority: **HOLD**

## Independence and outcome

`HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md` were produced by two
independent nonauthors.  Review B did not read Review A.  Both reviewers
rebuilt the parent-map update, height clock, endpoint basins, bounded-height
EGF, local fibres, periodic census, and deepest layer.  Neither found a
counterexample to the theorem package once the empty and small-`n`
conventions were made explicit.

The reviews did find one release-blocking presentation defect, three boundary
gaps, and a material owner-scope deficit.  All local repairs below are present
in the current tree.  No mathematical CRITICAL or MAJOR item remains open.

## Resolution ledger

| review finding | repair in the final source | status |
|---|---|---|
| Empty forest had an undefined maximum-distance clock | Defined `H(empty)=0`; edgeless forests have height zero; threaded the convention through Theorem 1 and Lemma 2 | resolved |
| Abstract/proof overextended `n-1` and `n!` to `n=0,1` | Restricted the sharp statement to `n>=2`; stated the one and two depth-zero states at `n=0,1` | resolved |
| Exact shell used undefined `B^(-1)` at `h=0` | Declared `B_(n,r)^(-1)=0` and quantified shells for `h>=0` | resolved |
| Matrix-tree proof silently invoked its eigenspace argument at `k=0` | Split off the unique edgeless `k=0` state before the determinant argument | resolved |
| Empty local target relied on an implicit `0^0` convention | Split off `m=0` and proved that only the empty state maps to it | resolved |
| Direct pruning and leaf-stripping owners were absent | Added Miller--Reif `RAKE`, Kovchegov--Zaliapin pruning, and Addario-Berry et al. leaf stripping; assigned the removal primitive and height clock zero credit | resolved |
| Height-enumeration chain was incomplete | Added Riordan and Rényi--Szekeres; assigned bounded height counts and the nested EGF zero credit | resolved |
| Named all-minors theorem lacked its direct source and orientation check | Added Chaiken; stated the edge-reversal bijection from the common away-from-root convention to parent maps toward roots | resolved |
| Cayley, absorption, zeta, inclusion--exclusion, and Hamilton extremality were over-dense as contribution language | Explicitly assigned every generic ingredient zero credit; residual scope is only the endpoint-indexed assembly and elementary `(m,s)` fibre calculation | resolved |
| “Ordered product” could suggest an extra `r!` | Replaced it by “root-indexed product” | resolved |
| Abstract compressed basin and fibre proofs into two engines | Named peeling, determinant/species, and separate target-leaf inclusion--exclusion routes | resolved |
| Empty phase term was implicit | Stated that the `m=0` term equals the unique empty state | resolved |
| Negative bounded search risked sounding like priority evidence | Stated that neither residual item has a priority determination and that search absence supports no inference | resolved |

## Retained theorem boundary

The current short paper proves, for the specified finite map, the endpoint
and exact height clock, every root-set basin, every bounded-depth CDF and
shell, the local predecessor number from `(m,s)`, the fixed/periodic census,
zeta, parameter recovery, and the correctly qualified deepest layer.  The two
substantive finite-map outputs retained after owner subtraction are their
endpoint-indexed assembly and the compact two-parameter fibre formula.

Parallel `RAKE`, tree erasure and height clocks, Cayley/all-minors counts,
labelled height recurrences, generic inclusion--exclusion, absorption/zeta
bookkeeping, and Hamilton-path extremality carry zero novelty or priority
credit.  A bounded audit did not locate the identical full assembly, but that
negative result is not novelty evidence.

## Post-repair controls

- fresh verifier exit: `0`;
- canonical stdout comparison: byte-for-byte equal;
- exact assertions: **400,105** through `n=6`;
- build sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX, all exit `0`;
- settled LaTeX/BibTeX warnings, undefined references, and over/underfull
  boxes: `0`;
- current PDF: 3 A4 pages, 318,137 bytes, anonymous/date-free metadata;
- fonts: 24/24 embedded, subsetted, and Unicode-mapped.

This closes the internal hostile-review gate only.  Final batch QA and hashes
are separate, and external release remains **HOLD**.
