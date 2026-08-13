# Test report

The frozen release must satisfy:

- byte-identical producer replay;
- independent checker pass on all 10 gates;
- all 31 unit/mutation tests pass;
- source hashes, phase values, p-adic fractional parts, cubic sums, rank
  bounds, Poisson-defect scope, Route-A status, and scope mutations are
  rejected;
- booleans cannot impersonate integers;
- unknown payload keys are rejected;
- released results remain unchanged under the default read-only runner;
- the artifact manifest covers every required source, result, evaluation,
  and paper-roadmap file.

The explicit refresh mode is the only operation allowed to replace released
JSON or refresh hashes.
