# C76 hostile audit

The hostile audit mutates semantic fields in the canonical evidence and
requires the independent checker to reject every mutation.  The mutation
families include:

```text
C75 authority hashes and schema id
scope firewall and C6-kernel boundary
effective group order and generator cycles
element-order distribution
support count, orbit count, and orbit-size spectrum
orbit counts by support cardinality
closure-minimal counts and cardinalities
full-core minimal counts and representative masks
```

The audit is deliberately semantic: changing a number while preserving JSON
syntax is expected to fail, as is replacing the effective label group with
the 11520-element ambient lift.  The run rejected all 16 mutations and is
reported as `MUTATION_TEST_PASS` in `results/TEST_REPORT.md`.
