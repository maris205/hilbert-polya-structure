# P165 source and ownership verification

**Status:** `OWNER_THIN / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.  
**Verification date:** 2026-09-03.

## Verified sources

1. M. Jibril, M. Tomlinson, C. J. Tjhai, M. Z. Ahmed, and S. Bezzateev,
   *Some new codes from binary Goppa codes and a method of shortening linear
   codes*, IET Communications 7 (2013), 270--277,
   DOI `10.1049/iet-com.2011.0693`.
   The Wiley/IET publisher page and article section on shortening were
   inspected.  The paper defines hitting sets for low-weight codewords and
   gives distance-increasing shortening results.  Its general route includes
   hitting all words through weight `d+delta`; taking `delta=d-1` reaches the
   sub-double-weight boundary used by the present one-step argument.

2. M. Grassl and G. White, *New Good Linear Codes by Special Puncturings*,
   Proceedings of ISIT 2004, p. 454,
   DOI `10.1109/ISIT.2004.1365491`.
   DOI metadata, the author's publication list, and the KIT institutional
   record agree on title, authors, venue, year, and page.  This source owns
   the neighboring use of low-weight support information for puncturing.

3. A. Vardy, *The Intractability of Computing the Minimum Distance of a
   Code*, IEEE Transactions on Information Theory 43 (1997), 1757--1766,
   DOI `10.1109/18.641542`.
   DOI and DBLP metadata agree.  It supports only the manuscript's explicit
   non-claim of a general efficient implementation.

All three BibTeX records were checked against DOI metadata.  The Grassl--White
year, omitted by one Crossref BibTeX response, was separately confirmed by
the institutional and author records.

## Mandatory subtraction

The following material receives zero contribution credit:

- conventional shortening and puncturing;
- Hamming support, minimum distance, direct sums, and repetition lines;
- choosing hitting coordinates for low-weight words;
- eliminating all words of weight below `2d` to leave distance at least
  `2d` in one step;
- generic finite-map termination and the geometric-series identity.

The manuscript does not claim that distance doubling, by itself, is new.
Its scoped residual starts only with autonomous recomputation across time,
the sharp global clock, the every-time nonzero-target image equivalence, and
the simultaneous lower-bound extremizer classification and count.

## Bounded owner-search statement

The earlier scout searched exact phrases around iterated shortening, unions
of supports of all words below twice the minimum distance, minimum-weight
residual codes, and target preimages, together with the internal P1--P164
code-dynamics ledger.  It found no direct source for the complete literal
iteration or targetwise formulas.  This is a bounded non-hit, not evidence
of novelty, priority, or publication readiness.  Any direct owner of the
literal map, image equivalence, or extremal count reopens the gate.

## Internal collision boundary

The nearest internal silhouettes are P109's iteration of a fixed nilpotent
linear operator, P137's additive rank-feedback resource budget, and P164's
affine cellular-automaton code fibres.  Here the coordinate kernel is
recomputed nonlinearly from the full current code, the clock comes from
multiplicative distance growth, and reachability is controlled jointly by
target distance and target-zero capacity.  These distinctions are bounded
internal noncollisions, not global novelty claims.
