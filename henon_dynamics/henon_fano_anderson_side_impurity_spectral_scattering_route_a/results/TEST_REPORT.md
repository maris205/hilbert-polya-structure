# Test report

## Final lane results

```text
C345_PRODUCER_PASS 126 spectral 315 scattering
  payload ae6529dccfec8b2b686b8d87a2c29e708e1361158e158577ebf7c0fbf94d70ff
C345 independent Fano--Anderson checker: PASS
  13734 assertions, 70 evaluator leaves
C345 SymPy cross-check: PASS 1467 exact identities
C345 byte replay: PASS
  809e130153863cb1327be31599c854a001f140576363753b590bf8049c4226b5
C345 hostile mutation suite: PASS 154/154
C345 release: PASS
```

The checker audits the raw and semantic evaluator hashes, every fixed evaluator
field and leaf, the sign/completeness proof lock, all evidence schemas and
rows, all scope flags, and the self-excluding evidence payload hash.  The
release lane tests both `-O` and `-OO` refusal for all five subordinate scripts
and itself refuses optimized execution.

PDF rounds contain 2, 3, and 4 pages, respectively; all are byte-distinct and
each is byte-identical across independent fresh builds.  The final PDF hash is
`4c1c2e075f60d1a5bd8273d6a89575db86355dd713ad033226c182f52c037962`.
