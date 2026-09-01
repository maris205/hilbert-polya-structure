# Focused owner and claim-subtraction audit: ARC

**Candidate:** adjacent-run consolidation on positive integer compositions.
**Audit date:** 2026-09-01.  **External status:** `HOLD_EXTERNAL`.

## Outcome

The static recurrent class and general run vocabulary are directly owned:
ARC fixed points are Carlitz compositions, and maximal equal runs in integer
compositions have a substantial enumerative and probabilistic literature.
Those facts receive zero credit.

No primary source was located in the bounded search for the literal
weight-preserving iteration `s^r -> rs`, the sharp all-`n` absorption clock,
or the adjacent-divisor every-target fibre polynomial.  That non-hit is not a
novelty claim.  After subtraction, the clock-plus-inverse conjunction remains
paper-sized and uses a proof engine not present in the static sources.

**Internal recommendation:** `GO_INTERNAL_OWNER_THIN`.

## Query ledger

Queries were run in literal, structural, and terminology variants, including:

- `integer composition dynamics merge maximal runs of equal parts multiply
  run length`;
- `integer composition operator replace a run by its sum`;
- `adjacent equal parts composition merge dynamics`;
- `run-length encoding integer compositions iteration`;
- `composition map r equal parts one part sum iteration`; and
- `Carlitz compositions dynamics map`.

The queries returned static run enumeration, longest-run asymptotics,
locally restricted compositions, and ordinary run-length encoding.  They did
not return a matching self-map.  Indexing and terminology gaps remain a real
limitation.

## Primary-source ledger

| class | primary source | owned content and boundary |
|---|---|---|
| **DIRECT STATIC** | A. Knopfmacher and H. Prodinger, [*On Carlitz Compositions*](https://mathweb.ucsd.edu/~ebender/comp.papers/119-Carlitz_plus.pdf), *European Journal of Combinatorics* 19 (1998), 579--589 | Directly owns the adjacent-unequal fixed class and its generating-function treatment.  It does not define ARC or iterate run consolidation. |
| **DIRECT STATIC/RUN** | H. S. Wilf, [*The Distribution of Run Lengths in Integer Compositions*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i2p23/pdf), *Electronic Journal of Combinatorics* 18(2) (2011), P23, [DOI 10.37236/2019](https://doi.org/10.37236/2019) | Defines maximal constant runs and gives generating functions for bounded run lengths, generalizing Carlitz compositions.  It owns the run statistic, not a self-map that replaces each run by its sum. |
| **NEAREST PROBABILISTIC** | A. Gafni, [*Longest run of equal parts in a random integer composition*](https://arxiv.org/abs/0907.5553), *Discrete Mathematics* 338 (2015), 236--247, [DOI 10.1016/j.disc.2014.10.003](https://doi.org/10.1016/j.disc.2014.10.003) | Owns asymptotics/distribution for the longest equal run of a random composition.  ARC depth is not the initial longest-run statistic and can be created by later value collisions. |
| **NEAREST LOCAL RESTRICTION** | E. A. Bender and E. R. Canfield, [*Locally Restricted Compositions II. General Restrictions and Infinite Matrices*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r108/pdf), *Electronic Journal of Combinatorics* 16 (2009), R108 | Develops general local restrictions and run-length asymptotics.  It supplies vocabulary and static counting context, not ARC's functional graph. |

Ordinary run-length encoding is a standard algorithm rather than a plausible
mathematical owner of this map: it records `(value,count)`, whereas ARC takes
their product, preserves the total, and iterates inside a fixed finite
composition carrier.

## Claim subtraction

The following receive zero credit:

1. the definition and enumeration of Carlitz compositions;
2. the fact that a composition has maximal equal runs;
3. generating functions for bounded or longest run lengths;
4. the `2^(n-1)` census of all compositions of `n`; and
5. ordinary run-length encoding as an algorithmic primitive.

The surviving conjunction is:

1. the literal simultaneous weight-preserving self-map on `Comp(n)`;
2. the sharp equality `max tau=floor(log_2 n)` for every `n`, with an explicit
   witness for every carrier size and a dependency-chain proof of the upper
   bound; and
3. the complete length-refined one-step fibre polynomial

   `Phi_beta(u)=sum u^(sum b_i/s_i)`

   over adjacent-unequal divisor choices, including the exact image test.

Neither the static Carlitz count nor an initial-run statistic implies the
sharp iterative clock.  Likewise, none of the screened sources yields the
divisor-path inverse.

## Internal firewall

P126 is the closest carrier match.  Its refinement map, logarithmic mechanism,
and suffix/codeword inverse are literal and proof-engine distinct from ARC's
maximal-run coarsening, weight-doubling ancestry, and divisor path.  P144's
Dyck reassociation has a component merge, but it is scheduled one pair at a
time and preserves a Catalan opener geometry; ARC is simultaneous and its
inverse is arithmetic on target parts.  The proposed main conjunction does not
transfer from either paper.

## Limit and verdict

A bounded search cannot exclude an unindexed theorem, a result hidden under
data-compression terminology, or a short observation inside the composition
literature.  Accordingly the candidate may not claim external novelty or
priority.  The positive decision is only an internal value judgment after
known static ownership has been subtracted.

Final status: **`GO_INTERNAL_OWNER_THIN`; `HOLD_EXTERNAL`.**
