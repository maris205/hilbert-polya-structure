# Owner and collision search log — open-fresh P165

**Status:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.  
**Search date:** 2026-09-03.  
**Rule:** a search non-hit is not novelty evidence.  Publisher/DOI metadata
and primary papers control attribution; snippets were used only to discover
sources.

## 1. Search envelope

Bounded queries included the following exact or near-exact strings:

```text
"minimum weight codewords" shortening code support union
"support of all minimum weight codewords" linear code
linear code shorten on support minimum weight codewords
minimum weight codewords support residual code shortening iteration
coding theory shorten coordinates support codewords weight less than twice minimum distance
linear code "weight less than 2d" support shortening
"all minimum weight codewords" shortening linear code hitting set
iterated shortening linear code minimum distance doubles
"principal down-set" inclusion poset weak order operator iteration
poset map ordered by inclusion of strict downsets iteration
```

The internal search covered P1--P164 directory names, recent theorem
contracts/firewalls, all current P162--P166 scout and hostile-gate Markdown,
and explicit terms `code`, `Schur`, `hull`, `shortening`, `minimum distance`,
`poset`, `downset`, `row inclusion`, `shadow`, `closure`, and `peeling`.

## 2. Verified primary/background sources

| source | verified metadata and what it owns | effect on this scout |
|---|---|---|
| M. Grassl and G. White, *New good linear codes by special puncturings*, ISIT 2004, p. 454, [DOI 10.1109/ISIT.2004.1365491](https://doi.org/10.1109/ISIT.2004.1365491) | Crossref resolves the DOI to the IEEE proceedings article and publisher resource.  The paper uses low-weight-word coordinate information for special puncturing. | direct owner of the low-weight-support/puncturing neighborhood; no contribution credit is assigned to that primitive |
| M. Jibril, M. Tomlinson, C. J. Tjhai, M. Z. Ahmed, and S. Bezzateev, *Some new codes from binary Goppa codes and a method of shortening linear codes*, **IET Communications** 7 (2013), 270--277, [DOI 10.1049/iet-com.2011.0693](https://doi.org/10.1049/iet-com.2011.0693) | publisher metadata, abstract, and Sec. 3 were directly inspected.  The paper defines hitting sets of low-weight supports and proves generalized shortening statements that eliminate prescribed low-weight words and increase distance.  Its Corollary 5 explicitly ranges over words of weight at most `d+delta`. | decisive subtraction: taking `delta=d-1` owns the general route “hit all words below `2d`, shorten, and obtain distance at least `2d`.”  The one-step doubling fact is not claimed here |
| F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland Mathematical Library 16 (1977), publisher record [ISBN 978-0-444-85193-2](https://shop.elsevier.com/books/the-theory-of-error-correcting-codes/macwilliams/978-0-444-85193-2) | Elsevier's record verifies authorship, volume, and the standard coding-theory scope. | linear codes, support, Hamming weight, minimum distance, puncturing, shortening, repetition codes, and direct sums are background only |
| A. Vardy, *The intractability of computing the minimum distance of a code*, **IEEE Transactions on Information Theory** 43 (1997), 1757--1766, [DOI 10.1109/18.641542](https://doi.org/10.1109/18.641542) | Crossref resolves the DOI, title, venue, volume, pages, and IEEE publisher. | blocks any implication that the literal map or theorem is an efficient general-code algorithm |
| V. Pilaud and V. Pons, *The weak order on integer posets*, **Algebraic Combinatorics** 1 (2018), [DOI 10.5802/alco.36](https://doi.org/10.5802/alco.36) | journal page and arXiv record describe weak-order/lattice structures on integer relations and posets. | nearby order-theoretic owner, not a direct source for `P ->` inclusion order of its own strict principal downsets |

## 3. Direct-owner adjudication for SDS

### Zero-credit material

- conventional shortening, with deleted coordinates retained as zero padding;
- Hamming support and minimum distance;
- use of a hitting set for low-weight codewords to raise distance;
- the specialization that discarding every word of weight `<2d` leaves
  minimum distance at least `2d`;
- direct sums and full-support one-dimensional repetition lines;
- generic finite-map termination and elementary geometric sums.

### Bounded non-hit, stated correctly

The searches did **not** retrieve a source defining the literal autonomous
map

```text
C -> {c in C : c is zero on the union of supports of all 0<wt(x)<2d(C)}
```

and iterating it on all labelled `q`-ary linear codes.  They also did not
retrieve the every-time target criterion

```text
d(D)>=2^t and z(D)>=2^t-1
```

or the simultaneous minimum-dimension/minimum-support fibre count.  This is
only a bounded non-hit.  It supports the status `OWNER_THIN`; it does not
support “novel,” “first,” or “unpublished.”

### Residual ceiling after subtraction

Only the following conjunction may be credited provisionally:

1. the autonomous recomputation of the entire sub-double-weight support at
   every step;
2. the sharp global depth `floor(log_2(n+1))` from pairwise-disjoint dyadic
   purge layers;
3. the exact all-time image criterion for every prescribed nonzero target;
4. the classification and count of simultaneous dimension/support-minimal
   target preimages.

The proof of item 2 may use the owned one-step distance increase, but cannot
present that increase as the contribution.  A source owning any of items
1, 3, or 4 directly forces a new gate and presumptive kill.

## 4. Internal collision audit

| internal object | overlap | ruling |
|---|---|---|
| killed Schur-square/code-power candidates | same broad code carrier | no product or power appears; no literal collision |
| killed code-hull candidates `C cap C^perp` and `C+C^perp` | subspace output | those are idempotent orthogonality retractions; SDS has nonzero logarithmic tails |
| P100/P115 | coordinate loss and finite algebra | fixed valuation or Cartier coordinate maps versus state-dependent low-weight support recomputation |
| P109 | descending subspace dynamics | one fixed nilpotent image operator versus a new coordinate kernel recomputed from the current code |
| P137 | sharp resource-budget clock plus target inverse | strongest silhouette risk; P137's permanent additive marker parts yield a triangular clock and partition fibres, whereas SDS's multiplicative distance yields dyadic layers and target code extensions.  Generic resource summation is zero credit, but the core recursion and target invariants differ |
| P143 | Boolean row/subset encoding | no row-inclusion residual or relation quotient in SDS |
| P159/P160 | pruning/cropping and rank change | different literal carrier, update, clock, and inverse obstruction; the fixed ambient coordinates in SDS are not deleted |
| P163/P164 | set-family shadows and affine-code fibres | neither complemented shadow kernels nor a cellular-automaton linear tail occurs |

No exact P1--P164 literal map was found.  The P137 comparison is the main
hostile-review risk and is explicitly preserved, not waved away.

## 5. PDI owner and value gate

The principal-downset terminology and weak-order endpoint class are standard.
The bounded search found no primary source for iterating the exact literal
operator.  That does not rescue it: its one-step inverse is a coupled
realization problem for principal-downset families, the fixed census is
classical ordered-Bell material, and its Boolean-row inclusion mechanism lies
next to P143.  It is killed internally as
`KILL_NO_INDEPENDENT_TARGET_AXIS` without relying on a novelty judgment.

## 6. Required next gate

An independent specialist should attack exactly three points before any paper
allocation:

1. whether Jibril's generalized shortening, or citations downstream of it,
   already state the literal union-support iteration;
2. whether equality in the two lower bounds really forces the direct-sum
   expansion in every finite field, including cancellation in lifted cosets;
3. whether the residual after full one-step subtraction is paper-sized rather
   than a concise corollary package.

Until that gate, status is `GREEN_OWNER_THIN / HOLD_EXTERNAL`.
