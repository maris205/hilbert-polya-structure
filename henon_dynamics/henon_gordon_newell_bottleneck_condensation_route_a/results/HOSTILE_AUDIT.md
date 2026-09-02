# Hostile audit — HCS-C285

## Mathematical attacks closed

1. **Nonreversible global balance.** The checker uses an explicitly
   nonreversible self-loop matrix and a dense nonreversible matrix. It computes
   `Q^T` nullspaces rather than accepting the product weights as input.
2. **Self-event ambiguity.** Self routes contribute to throughput and edge
   event flow but never to off-diagonal state changes. Separate exact ledgers
   enforce both meanings.
3. **Empty-chain reversibility.** `N=0` is recorded as a trivial singleton,
   not evidence that a nonreversible routing matrix satisfies detailed
   balance.
4. **Equal-weight singularity.** All partition calculations use direct sums,
   convolution, or Newton recurrence; no `1/(w_i-w_j)` appears. Two-tied,
   three-tied and all-equal limits are explicit.
5. **False equal split.** The tied sector is conditionally uniform on weak
   compositions and converges to a random Dirichlet vector. The paper never
   replaces that law with deterministic `1/r` shares.
6. **Asymptotic overreach.** Exact finite rows stop at `N=32`; the paper’s
   positive-coefficient convolution and simplex moment proof owns the
   thermodynamic theorem.
7. **Zero-face substitution.** Zero routing entries are admissible under
   irreducibility; zero service rates and zero canonical weights are singular
   excluded faces. Mutations that merge these semantics fail.
8. **Classical ownership.** The publisher-verified 1967 Gordon–Newell source
   is named as owner. No originality language remains.

## Integrity attacks closed

- exact top-level and nested key sets;
- exact JSON-decoded types at every scalar, object, list, and tagged union;
- Boolean-as-integer rejection, including state and index arrays;
- canonical reduced rational-string syntax rather than merely parseable values;
- raw top-level and nested duplicate JSON key rejection;
- duplicate and row-count-preserving drop/replace rejection;
- truncated/empty states, routing rows, moment vectors, covariance matrices,
  flow matrices and reversal matrices;
- repaired payload hashes after false scientific semantics;
- stale payload hash;
- boundary, collision, citation, nonclaim and Route-A tampering;
- unique YAML mapping keys, no merge keys, no anchors or aliases;
- YAML axis/tuple/overall/Route-B coherence.

The mutation result is 64/64 rejected. It includes all four previously
reproduced type-confusion escapes, further top-level/nested type probes, and a
noncanonical rational specimen. Passing a canonical payload is not
sufficient by itself: the checker reconstructs all mathematical values.

## PDF and release attacks closed

- three substantive revision sources selected by an integer macro;
- two independent fresh builds per round, two LuaLaTeX passes per build;
- fixed epoch, timezone, optional-metadata suppression and trailer ID;
- byte equality to archived PDFs and final-equals-round-2;
- distinct round hashes and page counts `2,3,4`;
- zero LaTeX/package/layout/reference/citation/missing-character warnings;
- every font embedded and subset (`22/22`, `23/23`, `24/24`);
- extracted-text checks for ownership, condensation, boundary and Route-A
  nonclaims, plus positive/negative sentinels for the state-space glyph and
  zero-population abstract spacing;
- rendered inspection of all nine pages;
- exact 27-payload/28-physical file-set closure with manifest self-exclusion.

## Remaining nonclaims

No result is asserted for reducible routing, zero service rates, open or
multiclass networks, state-dependent or multiserver service, literature
novelty, arithmetic local data, Euler factors, root numbers, target zeros,
formal quantization, a Hilbert–Pólya operator, or Route B.
