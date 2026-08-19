# C72 test report

```text
producer: PREFREEZE_G3_PASS
independent integer-lattice/group checker: PASS
GAP abstract subgroup cross-check: GROUP_CROSSCHECK_PASS
clean-process replay: REPLAY_PASS
hostile mutation test: PASS, 28/28 rejected
```

The producer and checker use different subgroup closure recurrences and
different coordinate-validation paths.  Both compare the set of reached
subgroups with an independent enumeration of the complete 54-element core,
not merely the number 20.  Every support-size row independently sums to its
binomial coefficient.
