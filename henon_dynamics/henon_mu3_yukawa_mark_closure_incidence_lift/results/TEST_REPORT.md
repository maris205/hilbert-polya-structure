# C75 test report

The following checks pass in the clean project directory:

```text
producer: PREFREEZE_G3_PASS
independent checker: PASS
GAP cross-check: GROUP_CROSSCHECK_PASS
clean replay: REPLAY_PASS
hostile mutations: PASS
```

The checker validates source hashes, canonical JSON, all 20 ambient subgroups,
all nine closure fibers, the 12-element weighted stabilizer, all 11,520 direct
lifted pairs, the exact order distribution, the center count, and the 18/6
lattice image/kernel boundary.
