# Stage-2 proof/implementation bridge report

## Outcome

The frozen theorem is **PROVABLE AS STATED** under the exact contract in
`THEOREM_CONTRACT.md`.

- All integer bases `p>=3` have the exact essential `p^N` skeleton and the
  same high-center pointed-factor rigidity.
- Hosseini--Yassawi constructiveness holds exactly for prime `p`; composite
  bases retain the skeleton but have the smaller common period
  `ell*p^N`.
- Every same-base pointed factor inside the frozen target family is the
  unique surjective 1-block directive-letter quotient.
- Pointed factor classes are the admissible independent-set partitions of
  the cyclic directive-adjacency graph, ordered by refinement.
- Cross-base and nonpointed maps remain explicitly unresolved and out of
  scope.

The fresh nearest-owner verdict is

```text
NO_EXACT_COLLISION_FOUND_IN_BOUNDED_SEARCH
```

DKL (1995), Theorem 1 is credited as the closest general same-period,
over-zero aligned-symbol owner.  Hosseini--Yassawi owns the constructive
pure-power obstruction.  Neither source was found to state the residual
radius-zero collapse and explicit quotient poset for this affine family.
This bounded verdict is not a priority claim.

## Input integrity

The Stage-1 manifest hash was checked against the frozen expected value:

```text
7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8
```

All 13 entries in that manifest rehashed successfully.  Their exact values
are in `evidence/input_hashes.json`; Stage-1 was not modified.

## Deterministic test result

All nine assertion groups passed:

1. direct affine values equal independent nested-hole values;
2. exact unique-hole residues are independently reproduced;
3. the high-center identity holds in sampled prime and composite lanes;
4. every bounded smaller prime-base candidate period has an exact witness;
5. composite counterperiods pass both implementations;
6. directive, partition, and graphical-Stirling enumerators agree;
7. the graphical-Stirling/chromatic identity agrees for the bounded graph
   evaluations;
8. bounded local-rule consistency agrees exactly with letter quotienthood;
9. all typed negative controls are rejected for their intended reason.

Exact evidence counts are:

| Check | Count/result |
|---|---:|
| Independent point-value comparisons | 68,288 |
| Skeleton cases | 32 |
| Skeleton residue classes | 28,764 |
| High-center identities | 1,920 |
| Prime cases | 10 |
| Smaller prime candidate periods rejected | 3,918 |
| Prime next-power sample comparisons | 3,370 |
| Composite counterperiod cases | 18 |
| Composite direct-formula comparisons | 998,025 |
| Composite nested-fill comparisons | 99,519 |
| Canonical directives | 44 |
| Partition checks | 477 |
| Admissible partitions across sources | 112 |
| Chromatic `q=0,...,6` evaluations | 308 |
| Bounded local-rule cases | 972 |
| Consistent local cases | 132 |
| Exact quotient cases | 132 |
| Local false positives / false negatives | 0 / 0 |
| Typed negative controls | 4 |

Local-rule bounds were bases `{3,4,5}`, radii `{0,1,2,3}`, directive period
at most 5, alphabet size at most 3, dense radius 128, plus deterministic high
centers.  These are falsification bounds only; the factor theorem is proved
separately with CHL, high centers, and orbit density.

## Key reproducibility hashes

The following hashes identify the deterministic implementation and evidence
bytes used for this report:

```text
bca735786fefe539ef7749883d2a3e167a28571f4d8b531c05ec6003de705299  impl_formula.py
4818ae7aee9be90ffde1f440833fc8f81b6c48476fb38c02974857aba8b6a9c7  impl_holefill.py
4ff2806825ce4255fdd63b38a50a0587f3bac09f522aaf04ddc34f73b6753528  run_stage2.py
620c53d713d91c74ac1519d7bce259b0728c043d383e5b13adff8cc44dd14bc0  evidence/input_hashes.json
b6e7f69ca360680c21bf3d772d79ceeb543f1cb8a82d236a647206df8781c74b  evidence/canonical_evidence.json
99ee0fb200903772944ec05897af21ae4126bedd1df08fab6cae4bdf46772963  evidence/test_results.json
```

`SHA256SUMS.txt` is the authoritative whole-package content list, excluding
itself to avoid self-reference.  `verify_manifest.py` additionally rejects
missing or extra files, symlinks, nonregular entries, cache/bytecode, and
unexpected modes.

## Negative controls and interpretation

- A declared target letter omitted by the map is rejected as
  nonsurjective.
- Merging an adjacency edge is rejected because the quotient leaves the
  frozen target class.
- Wrong-base and nonpointed declarations are rejected as scope overreach,
  not asserted impossible in broader categories.
- The `p=4` counterperiod is a required falsifier of the tempting but false
  all-base constructiveness statement.

The first pre-freeze integration run exposed two normalization defects:
least-period reduction of quotient directives and cyclic indexing in one
local quotient check.  Both fixes are recorded in `METHODOLOGY.md`; all JSON
evidence was regenerated afterward.

## Cohesion / anti-salami verdict

The skeleton, prime/composite split, high-center lemma, factor rigidity,
partition poset, and graph counts form one dependency chain.  The graph
counts are corollaries of the map classification, not standalone fragments,
and the constructiveness split is required to state the source domain
correctly.  The package is therefore coherent as one theorem program.

This is not a publication-mass authorization.  Source completeness,
terminology, and every proof quantifier still require an auditor who did not
build the package.

## Required next gate

An independent auditor should first verify the manifest, then audit the
proof without consulting the evidence, then reproduce the evidence, and
finally rerun the exact-quantifier source search.  No manuscript or public
write is authorized before that gate.

**Final Stage-2 status: `HOLD_FOR_INDEPENDENT_STAGE2_AUDIT`.**
