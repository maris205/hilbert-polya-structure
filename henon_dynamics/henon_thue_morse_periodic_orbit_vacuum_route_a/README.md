# HCS-C144: Thue--Morse periodic-orbit vacuum

This package proves that the two-sided Thue--Morse substitution subshift is
nonempty, minimal, uniformly recurrent, and has no periodic points.  Therefore
all positive Artin--Mazur fixed-point counts and primitive-cycle counts vanish
and `zeta_TM=1`.

The package also freezes exact circulated substitution approximants.  They
have finite cycles and increasingly accurate local languages, but they are not
points of the limiting subshift.  The strict Route-A verdict is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_REJECTED`, Route B false.

Run:

```bash
python3 code/c144_thue_morse_producer.py
python3 code/c144_thue_morse_checker.py
python3 code/c144_sympy_crosscheck.py
python3 code/c144_replay.py
python3 code/c144_mutation.py
python3 code/c144_release_manifest.py
```

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
