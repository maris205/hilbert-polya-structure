# Test Report

All commands are run from the package root with
PYTHONDONTWRITEBYTECODE=1.

| Lane | Result |
|---|---|
| evidence producer | PASS; deterministic canonical JSON |
| independent checker | PASS; 4,542 assertions, 70 evaluator leaves |
| SymPy cross-check | PASS; 409 exact identities |
| isolated replay | PASS; two temporary directories byte-identical |
| hostile mutation | PASS; 137/137 attacks rejected |
| optimized mode | PASS; all six scripts reject Python -OO |
| PDF rounds | PASS; 1, 2, and 3 pages; byte-distinct and deterministic |
| release closure | PASS; 27 payload files and 28 physical files |

The checker contains its own constants, rational arithmetic, schema, and
row reconstruction.  It neither imports nor names the producer module.
