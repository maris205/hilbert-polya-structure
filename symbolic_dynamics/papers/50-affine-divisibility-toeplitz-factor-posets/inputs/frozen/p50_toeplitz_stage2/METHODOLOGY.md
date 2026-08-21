# Stage-2 methodology

## Purpose and boundary

This directory is a proof/implementation bridge, not a manuscript.  It
turns one frozen Stage-1 candidate into an auditable theorem contract, a
complete proof spine, a bounded deterministic falsification suite, and a
primary-source boundary.  It does not authorize Git, README, mirror,
authority, figure, publication, or submission work.

The immutable input is `/tmp/p49_53_phase1`.  Before producing evidence,
`run_stage2.py` verifies the SHA-256 of the Stage-1 manifest and then every
file named in it.  The expected manifest hash is hard-coded as

```text
7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8.
```

The exact verified entries are written to `evidence/input_hashes.json`.
No Stage-1 file is copied or modified.

## Proof discipline

The written proof is primary.  It follows these lanes in order.

1. Freeze `nu_p` as a divisibility exponent for every integer `p>=3`.
2. Derive the unique hole residue and exact skeleton algebraically.
3. Prove Toeplitzness, essential periods, simple one-hole construction, and
   aperiodicity for all bases.
4. Treat Hosseini--Yassawi constructiveness separately: a modular-inverse
   lower bound only for prime `p`, and a quantified `ell*p^N` counterperiod
   for composite `p`.
5. Invoke Curtis--Hedlund--Lyndon once, combine it with the all-base
   high-center identity, and use orbit density to prove the arbitrary-radius
   pointed factor theorem.
6. Derive partition, preorder/poset, and graph-count consequences only after
   the map theorem.

This ordering prevents finite evidence from substituting for an infinite
proof.  It also makes the single prime-only use of modular invertibility
visible.

## Independent deterministic implementations

The two implementation modules do not import one another.

### `impl_formula.py`

- evaluates `x(k)` from the affine integer `(p-1)k+1` and repeated division
  by `p`;
- computes `r_N` by the closed geometric-sum formula;
- enumerates directives by a Cartesian product followed by canonical
  restricted-growth filtering;
- enumerates set partitions by a Cartesian product of labels followed by
  canonical filtering;
- counts proper graph colorings by a direct Cartesian product;
- samples local rules from direct affine evaluations.

### `impl_holefill.py`

- evaluates `x(k)` by successive one-hole filling, updating the nested
  residue and modulus, without evaluating the affine divisibility exponent;
- computes centers by the recurrence `r_{N+1}=r_N+p^N`;
- recursively grows restricted-growth directives;
- recursively places vertices into set-partition blocks;
- counts proper colorings by recursive vertex assignment;
- samples local rules using the nested-hole evaluator.

Agreement is therefore meaningful for coordinate values, centers,
directive sets, partition sets, graphical Stirling numbers, chromatic
evaluations, skeleton samples, and bounded local constraints.  It is still
not a formal proof of independence or correctness.

## Exhaustive and sampled bounds

All bounds below are serialized in `evidence/canonical_evidence.json`.

### Coordinate and center checks

- integer bases `p=3,...,10`;
- four directives `(0,1)`, `(0,1,2)`, `(0,1,0,2)`, `(0,1,2,1)`;
- dense coordinates `k=-1000,...,1000`;
- centers `r_n`, `n=0,...,18`, with offsets `-3,...,3`;
- total independent point-value comparisons: `68,288`.

### Skeleton and high-center checks

- skeletons: `p=3,...,10`, `N=1,...,4`, totaling 32 cases and
  `28,764` residue classes;
- high centers: `p=3,...,10`, all nonzero `j` in `[-40,40]`, and levels
  `nu_p(j)+1`, `nu_p(j)+2`, `nu_p(j)+5`, totaling `1,920` identities.

### Constructiveness controls

- prime lanes: `(p,max N)=(3,4),(5,3),(7,3)`;
- every candidate `1<=q<p^(N+1)` is rejected by an exact center witness,
  totaling `3,918` candidate periods;
- `p^(N+1)` receives `3,370` sampled common-period comparisons;
- composite lanes: `p in {4,6,8,9,10,12}`, `N=1,2,3`;
- each uses `q=ell*p^N`, with `ell` the least prime divisor;
- direct-formula comparisons: `998,025`;
- independent nested-fill comparisons: `99,519`.

The proof in `PROOF_PACKAGE.md` quantifies over all integer translates `t`;
these finite ranges are negative controls, not the source of that
quantifier.

### Directive, partition, and graph checks

- canonical frozen directives: least period at most 6, alphabet size at
  most 4;
- 44 directives generated independently;
- 477 partition admissibility checks;
- 112 admissible partitions in total across those sources;
- graphical Stirling counts compared between implementations;
- proper labeled colorings evaluated independently for `q=0,...,6` and
  compared with `sum_k S_G(k)(q)_k`, totaling 308 directive/`q` evaluations.

### Bounded local-rule falsification

- all nine frozen canonical directives with period at most 5 and alphabet
  size at most 3;
- every ordered source/target pair;
- bases `p in {3,4,5}`;
- radii `R=0,1,2,3`;
- dense coordinates `[-128,128]` plus high centers to a deterministic depth
  depending on the two directive periods and `R`;
- 972 source/target/base/radius cases;
- 132 consistent cases and 132 exact surjective letter quotients;
- zero observed false positives and zero observed false negatives;
- at most 18 distinct observed windows in a case.

This search only tries to expose a counterexample inside its finite bounds.
The CHL/high-center/orbit-density argument is the all-radius theorem.

## Typed negative controls

The generator rejects four deliberately out-of-contract declarations before
they can be misread as theorem evidence.

1. A letter map that omits a declared target letter:
   `REJECT_LETTER_MAP_NOT_SURJECTIVE`.
2. A kernel merging cyclically adjacent letters:
   `REJECT_QUOTIENT_NOT_CYCLIC_NEIGHBOR_DISTINCT`.
3. A source and target with different bases:
   `REJECT_WRONG_BASE_OUT_OF_SCOPE`.
4. A map that does not preserve the distinguished point:
   `REJECT_NONPOINTED_OUT_OF_SCOPE`.

Composite-base constructiveness is controlled separately and more strongly:
the evidence records the explicit counterperiod `ell*p^N` in 18 cases, and
the proof handles all composite bases, all levels, and all translates.

The wrong-base and nonpointed controls are scope guards, not claims that
such maps can never exist in broader categories.

## Determinism and serialization

- No randomness, wall-clock values, locale-dependent sorting, network data,
  or hash-table iteration order enters the evidence.
- JSON is emitted with sorted keys, two-space indentation, UTF-8, and a
  final newline.
- Canonical directive and partition representatives are restricted-growth
  label strings and are explicitly sorted.
- The run date is the frozen audit date `2026-08-20`, not a runtime clock.
- The tested environment was Python 3.12.3 on Linux x86_64; only the Python
  standard library is required.
- `PYTHONDONTWRITEBYTECODE=1` is used for the frozen run.  Bytecode caches are
  forbidden from the manifest.

## Pre-freeze defect log

The first integration run usefully failed twice before evidence was frozen.

1. The image of `(0,1,0,2)` under the admissible merge of letters `1` and
   `2` was initially retained as `(0,1,0,1)`.  That word is valid but its
   least directive period is 2, not 4.  `quotient_directive` was changed to
   reduce every image to its least period.
2. The direct-formula local quotient check initially failed to reduce both
   directive indices cyclically across the least-common-multiple horizon.
   The index normalization was corrected.

Both were implementation/normalization defects, not failures of the theorem
statement.  After the fixes, every evidence file was regenerated from
scratch by the deterministic runner and all nine assertion groups passed.
Recording these failures prevents a clean final run from erasing useful
audit history.

## Source-search method

The nearest-owner search used exact formula/phrase queries, title and author
queries, primary journal pages, primary PDFs, arXiv abstracts, and arXiv full
text.  Each source was compared by object class, map quantifier, pointedness,
base relation, and conclusion.  Search-engine snippets were never treated
as proof of a source claim.  `SOURCE_LOCK.md` records the exact nearest
owners and the bounded negative verdict.

## Reproduction

From `/tmp/p50_toeplitz_stage2`, run

```text
PYTHONDONTWRITEBYTECODE=1 python3 run_stage2.py \
  --stage1 /tmp/p49_53_phase1 \
  --output /tmp/p50_toeplitz_stage2
```

Then run

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_manifest.py
```

The first command must report `PASS` and reproduce the canonical JSON bytes.
The second must reject any missing, added, nonregular, mode-changed, or
content-changed package file.
