# C130 experiment plan

## Goal

Turn the all-period symbolic proof into a replayable finite receipt without
mistaking the replay cutoff for a theorem cutoff.

## Frozen inputs

- `B=[[1,1],[1,1]]`;
- roof `(1,sqrt(2))`;
- rational control roof `(1,2)`;
- destination weighting `M=B diag(u,v)`;
- periods `1<=n<=10` for replay only.

## Claim--test matrix

| Claim | Exact test | Failure signal |
|---|---|---|
| mixing base | every entry of `B` is positive | any zero entry |
| bivariate determinant | direct symbolic and standard-library determinant | term other than `1-u-v` |
| all-order trace form | matrix powers versus binomial sectors for each replay period | coefficient mismatch |
| primitive identity | necklace enumeration and Euler product modulo total degree 10 | residual coefficient |
| sector separation | exact algebraic pair labels and distinct-sector rule | forged merged pair |
| within-sector caveat | two explicit primitive period-six necklaces with counts `(3,3)` | nonprimitive/rotational duplicate |
| rational collision | `(2,0)` and `(0,1)` both map to time 2 | unequal time |
| lattice periodicity | `1-q-q^2` and `2*pi*i` period | specialization mismatch |
| strict boundary | exact tuple and false Route-B flag | any promotion |

## Implementations

1. The producer uses SymPy to derive the determinant, traces, and replay rows.
2. The independent checker uses a separate dictionary representation of
   bivariate polynomials, enumerates necklaces from scratch, and does not
   import the producer or SymPy.
3. The SymPy crosscheck reconstructs the matrix rather than importing producer
   functions.
4. Byte replay compares a temporary receipt to the retained evidence.
5. The hostile suite mutates 43 semantic fields and repairs the payload hash
   before checking, plus one deliberately stale-hash mutation.

## Acceptance gates

- all five programs exit zero;
- 2,046 rooted closed words, 226 primitive cycles, and 65 replay clock sectors;
- all 43 repaired-hash mutations and the one stale-hash mutation rejected;
- two isolated fixed-epoch PDF builds byte-identical to the retained final;
- every PDF font embedded and final log free of warnings/bad boxes;
- all rendered pages visually clean;
- exactly 27 payload files plus the manifest itself on disk.

## Conservative fallback

If the irrational roof only separates count vectors, the paper must say so and
must retain a same-sector orbit collision.  If the analytic Euler product is
not globally convergent, state its right-half-plane domain and use the explicit
entire determinant for continuation.  Neither issue may be hidden by wording.
