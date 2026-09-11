# Actual paper-local author replay pair

2026-09-05 UTC; root executions, Python 3.12.3, standard library only.
The local verify.py is a byte-identical copy of the original standalone
author implementation. It imports no pilot, reviewer, historical or local
research module and reads no canonical/data file. No random seed or network
input is used; -B disables bytecode output.

Working directory: `/root/autodl-tmp/symbolic_dynamics`. Actual sequence:

```sh
python -B papers/205-conflict-triggered-cyclic-increments/verify.py > papers/205-conflict-triggered-cyclic-increments/author_replay/run1.stdout
cmp papers/205-conflict-triggered-cyclic-increments/CANONICAL.json papers/205-conflict-triggered-cyclic-increments/author_replay/run1.stdout
python -B papers/205-conflict-triggered-cyclic-increments/verify.py > papers/205-conflict-triggered-cyclic-increments/author_replay/run2.stdout
cmp papers/205-conflict-triggered-cyclic-increments/CANONICAL.json papers/205-conflict-triggered-cyclic-increments/author_replay/run2.stdout
```

The commands were chained with success conditions. Both Python producers
and both raw-byte comparisons exited zero, combined exit zero. Each output
has 1,029,769 assertions PASS and the complete recorded finite boxes.
Both complete stdout files remain in author_replay/, not just their digests.

- verify.py SHA256: `329b2c8bf19bdfd77cfbb5e3f16d6bfc78aa90f557444cf45d5e35d44868afe9`.
- CANONICAL.json and each run SHA256: `41ca0312bd5115fc0343310ebfbd493c44ee927d267de7ca438328af92bae2f7`.

These fresh executions are author proof pressure, not independent reviewer
evidence, all-parameter proofs, cold builds or page-view attestations.
