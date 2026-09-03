# C327 test report

## Exact and numerical lanes

```text
C327_PRODUCER_PASS 216 5428 06519837503bc7159bc2786865d0f51f59666b1a70b735715eeff2f5f89618d1
C327 independent Kronig--Penney checker: PASS 5607 checks
C327 SymPy cross-check: PASS 295 exact identities
C327 byte replay: PASS (f784ba21ff52c4cabd438e1321cce892a77fe6d506567128b88f74c85db2878b)
C327 hostile mutation suite: PASS 55/55
```

The producer payload digest is the self-excluding canonical-JSON digest; the
replay digest is the SHA-256 of the complete pretty-printed evidence file.

## Fail-closed controls

- Producer, independent checker, SymPy, replay, mutation, and release scripts
  explicitly refuse optimized Python.
- JSON rejects duplicate keys, nonfinite constants, and non-object roots.
- YAML rejects duplicate/non-string keys, merge keys, aliases/anchors, wrong
  roots, raw-byte drift, and semantic drift.
- Raw and semantic evaluator hashes, full evaluator authority path, v0.2.0
  version/hash, all five verdict/evidence-status pairs, scope flags, and Route-B
  denial are exact-locked.
- Every top-level and row-level evidence key is owned; repaired payload hashes
  do not allow semantic mutations to pass.

## Paper and release controls

Three substantively distinct revisions are compiled twice each from isolated
directories with LuaLaTeX, fixed epoch `1788393600`, and `TZ=UTC`.  Release
requires byte identity, no warning/layout/reference/citation/glyph issue,
embedded/subset fonts, extractable revision tokens, successful rasterization
of every page, `main.pdf == main_round2.pdf`, and exactly 27 payload files plus
the self-excluded manifest.
