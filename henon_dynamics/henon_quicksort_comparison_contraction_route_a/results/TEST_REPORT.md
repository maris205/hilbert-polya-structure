# Test report — HCS-C302

## Independent exact checker

```text
C302 independent checker PASS (8377 assertions)
payload_sha256=8f1092fa6172e1199583e8ef942cc7d5713102eef96fe9991a2af4f34f057a6b
route_tuple=A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL
```

This includes full permutation enumeration through `n=9` and a separate
integer-count convolution through `n=12`; the checker imports no producer code.

## SymPy cross-check

```text
C302 SymPy exact cross-check PASS (2424 symbolic/cell assertions)
verified: PGFs, mean/variance recurrences, n+1 centering, contraction integral,
beta derivatives, m3=16*zeta(3)-19
```

## Replay and hostile mutations

```text
C302 deterministic replay PASS (two fresh runs and archived bytes identical)
evidence_sha256=0ceba774a464fa86ffa9cb20c44b4b7c57aafb3c6d5aec5a63f1417f92e788fc
C302 mutation suite PASS (72/72 semantic/parser mutations killed)
classes=model,PGF,moments,n+1-centering,contraction,m3,route,scope,JSON,YAML
```

The release script additionally requires two fresh deterministic builds of
each substantive PDF round, no layout/reference warnings, embedded/subset
fonts, complete rasterization, exact YAML semantics, scope flags all false,
and exact 27-payload/28-physical-file closure.
