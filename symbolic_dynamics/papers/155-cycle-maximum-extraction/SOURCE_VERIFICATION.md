# P155 primary-source verification and subtraction

**Checked:** 2026-09-02 UTC.  **External status:** `HOLD_EXTERNAL`.

Only primary preprints, official journal pages, and DOI/arXiv records were
used for claim decisions.  This is a bounded owner audit; a non-hit is not
novelty, priority, or clearance evidence.

## Closest verified primary sources

1. **Chen, Deng, Du, Stanley, and Yan, “Crossings and Nestings of Matchings
   and Partitions.”**  Primary preprint:
   <https://arxiv.org/abs/math/0501230>.  It fixes minimal and maximal block
   elements and proves crossing/nesting symmetry.

   **Subtracted:** block endpoints, set-partition supports, and any
   crossing/nesting statement with endpoint sets fixed.

2. **Rubey and Stump, “Crossings and Nestings in Set Partitions of Classical
   Types.”**  Primary preprint: <https://arxiv.org/abs/0904.1097>.  It uses
   opener/closer configurations and bijections preserving them.

   **Subtracted:** opener, closer, singleton, transient, endpoint-feasibility,
   and preserved-endpoint language.

3. **Mongelli, “Combinatorial Interpretations of Particular Evaluations of
   Complete and Elementary Symmetric Functions,” EJC 19(1), P60 (2012).**
   Official journal record and DOI:
   <https://doi.org/10.37236/2131>.

   **Subtracted:** writing cycles with their minima first and ordering cycles
   by increasing minima.

4. **Andrews, Egge, Gawronski, and Littlejohn, “The Jacobi–Stirling
   Numbers.”**  Primary preprint: <https://arxiv.org/abs/1112.6111>.

   **Subtracted:** cycle maxima and enumerations with prescribed sets of cycle
   maxima.

All four entries in `references.bib` were checked against these primary
records and are cited in `main.tex`.

## Literal-map query families

```text
"cycle maxima" permutation "standardize"
permutation cycles ordered by minimum sequence of cycle maxima
"cycles are ordered by their minima" permutation
set partitions openers closers minima maxima blocks
iterated cycle maxima permutation
cycle maximum extraction permutation dynamics
```

The bounded search did not retrieve the exact map

```text
cycles ordered by minima -> standardized word of support maxima
```

together with its rank-varying iteration, threshold, or every-target weighted
fibres.  This records only a bounded non-hit.

## Internal mechanism firewall

- Fixed-rank cycle pruning by arrow surgery is not used: P155 forgets cyclic
  order immediately and changes rank to the number of cycles.
- Endpoint-local peak extraction is not used: P155's inverse problem is an
  opener/closer schedule on disjoint supports.
- Weak-excedance extraction is not used: P155's obstruction is singleton
  capacity `rlmin`, and its fibres are factorially weighted support partitions.

No source decision authorizes external posting, contact, submission, or
release.

