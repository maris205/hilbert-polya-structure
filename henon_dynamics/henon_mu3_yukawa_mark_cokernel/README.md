# HCS-C66 restricted mark-map Smith invariants

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C66 takes the exact 16-type table-of-marks matrix from C64 and computes its
full integral Smith form.  The restricted map has Smith invariants

```text
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 24, 144]
```

Consequently its cokernel is

```text
(Z/2)^10 + (Z/4)^3 + Z/24 + Z/144
```

with 2-primary part `(Z/2)^10 + (Z/4)^3 + Z/8 + Z/16` and 3-primary part
`Z/3 + Z/9`.  The C65 rank-three mark-image SNFs and relative `Z/2` are
checked only as an upstream compatibility condition.

The result is restricted to the 16 C63/C64 subgroup types.  It does not
classify the full Burnside ring and makes no arithmetic, local, Euler-factor,
root-number, automorphy, or Hilbert--Polya claim.  The literal scope firewall
is `NO_BAD_EULER_OR_ROOT_NUMBER`.

Entry points:

- `code/c66_mark_snf.py`: source-bound producer;
- `code/c66_mark_snf_checker.py`: independent exact checker;
- `code/c66_mark_snf_replay_checker.py`: clean-process replay;
- `code/c66_snf_crosscheck.py`: independent library Smith-form check;
- `code/c66_mutation_test.py`: hostile semantic mutations;
- `results/c66_mark_snf_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.
