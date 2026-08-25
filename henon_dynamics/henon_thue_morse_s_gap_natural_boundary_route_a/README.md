# HCS-C159: Thue--Morse S-gap natural boundary

This package proves that the Thue--Morse S-gap renewal shift is topologically
mixing with dense periodic points and recurrent transitive points.  Its exact
Artin--Mazur zeta is

```text
zeta_X(z)=2/(2-3z+z(1-z) product_(j>=0)(1-z^(2^j))),
```

and the unit circle is a natural boundary for its source-defined meromorphic
continuation.  This replaces C154's one-pass wandering interface and avoids
repeating C144's periodic vacuum.

Run:

```text
python code/c159_s_gap_producer.py
python code/c159_s_gap_checker.py
python code/c159_sympy_crosscheck.py
python code/c159_replay.py
python code/c159_mutation.py
```

The release includes the exact evidence, proof package, bilingual PDF,
independent checks, hostile audit, Route-A evaluation, and content-addressed
manifest.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
