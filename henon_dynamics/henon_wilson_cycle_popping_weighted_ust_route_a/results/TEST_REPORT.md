# Test report

All commands are run from the package root with `PYTHONDONTWRITEBYTECODE=1`
and `TZ=UTC`.

| Lane | Command | Result |
|---|---|---|
| producer | `python -B code/c338_wilson_ust_producer.py` | PASS; 772 graphs, 8,136 graph--tree pairs, 55,895 simple subset events, 12,754 stack tables |
| independent checker | `python -B code/c338_wilson_ust_checker.py` | PASS; 224,424 exact checks |
| symbolic | `python -B code/c338_wilson_ust_sympy_crosscheck.py` | PASS; 85 checks |
| replay | `python -B code/c338_wilson_ust_replay.py` | PASS; 1,844,227 identical bytes |
| mutation | `python -B code/c338_wilson_ust_mutation.py` | PASS; 142/142 rejected |

The checker imports no producer code.  Each script explicitly rejects both
`python -O` and `python -OO`; the release gate verifies the refusal text.
Strict JSON rejects duplicate keys and nonfinite constants.  Strict YAML
rejects duplicates, anchors, aliases, merge keys, non-string keys, implicit
timestamps, unknown fields through exact schema comparison, and type changes.
Raw and semantic evaluator digests, authority path/version/hash, every
evidence section digest, Route-A tuple, nonclaims, collisions, source tokens,
and all coordinate ledgers are directly owned.

The release gate performs two independent fresh two-pass LuaLaTeX builds for
each revision, byte-compares them with the checked-in PDFs, checks extracted
text and all page rasters, enforces embedded/subset fonts, rejects warnings and
build sidecars, and requires the exact 27-payload/28-physical inventory.
