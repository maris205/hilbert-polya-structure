# P156 primary-source verification and subtraction

**Checked:** 2026-09-02 UTC.  **External status:** `HOLD_EXTERNAL`.

Only primary papers, official journal pages, DOI metadata, and arXiv records
were used for source-role decisions.  The audit is bounded and cannot establish
novelty, priority, ownership completeness, or external clearance.

## Verified static owners

| source | verified record | zero-credit role |
|---|---|---|
| Ehrenborg–Steingrímsson, *The Excedance Set of a Permutation* | [DOI 10.1006/aama.1999.0671](https://doi.org/10.1006/aama.1999.0671) | excedance-set enumeration and recurrences |
| Chung–Claesson–Dukes–Graham, *Descent Polynomials for Permutations with Bounded Drop Size* | [DOI 10.1016/j.ejc.2010.01.011](https://doi.org/10.1016/j.ejc.2010.01.011), [arXiv:0908.2456](https://arxiv.org/abs/0908.2456) | maximum drop, bounded-drop enumeration, bubble-sort/juggling motivation |
| Chen–Chen, *On Permutations with Bounded Drop Size* | [DOI 10.1016/j.ejc.2015.12.008](https://doi.org/10.1016/j.ejc.2015.12.008), [arXiv:1306.5428](https://arxiv.org/abs/1306.5428) | bounded-drop bijections and unimodality |
| Steingrímsson–Williams, *Permutation Tableaux and Permutation Patterns* | [arXiv:math/0507149](https://arxiv.org/abs/math/0507149) | weak-excedance tableau and pattern structure |
| Bergeron–Gagnon, *The Excedance Quotient of the Bruhat Order...* | [arXiv:2302.10814](https://arxiv.org/abs/2302.10814) | weak-excedance position/value equivalence classes and Bruhat interfaces |

## Exact identity-basin collision

Fufa Beyene, Jörgen Backelin, Roberto Mantaci, and Samuel A. Fufa,
*Set Partitions and Other Bell Number Enumerated Objects*, Journal of Integer
Sequences 26 (2023), Article 23.1.8:

- official article: <https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.html>;
- primary preprint: <https://arxiv.org/abs/2101.07074>.

Their Theorem 27 proves that permutations whose weak-excedance-letter subword
is increasing are counted by the Bell number.  In P156 notation it owns

```text
sum_m |W_n^{-1}(id_m)| = B_n.
```

That aggregate and its proof are fully subtracted.  Their citation chain uses
Baril's transposition-array papers, verified at
[DOI 10.1016/j.ipl.2012.10.003](https://doi.org/10.1016/j.ipl.2012.10.003)
and
[DOI 10.1016/j.disc.2006.09.007](https://doi.org/10.1016/j.disc.2006.09.007).
Those coding facts are also zero credit.

## Exact-map query families

```text
"weak excedance subword" permutation map iteration
"retain" weak excedance letters permutation standardization
"standardized" "weak excedance" subword
weak excedance deletion permutation standardization
iterated weak excedances permutation transform
permutation weak excedance subword map
```

The bounded audit did not retrieve the exact iterated standardized map, its
all-rank image theorem, target-resolved fibre formula, or canonical Fibonacci
right-inverse tower.  This non-hit is not positive evidence.

## Mechanism firewall

Endpoint-local peak extraction uses alternating peak packing and zigzag
fibres.  P156 instead uses the absolute diagonal predicate, the target
obstruction `d(sigma)`, a high-shift/low-tail section, and deficient Ferrers
completions.  Cycle-maximum extraction instead uses right-to-left-minimum
singleton capacity and factorially weighted support partitions.  The shared
rank-varying permutation/standardization carrier receives zero credit.

No source decision authorizes external posting, contact, submission, or
release.

