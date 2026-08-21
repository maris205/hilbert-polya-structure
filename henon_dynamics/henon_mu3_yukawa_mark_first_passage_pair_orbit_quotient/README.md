# C97: Ordered-pair orbit quotient of finite first-passage laws

C97 lifts the C93 symmetry quotient from single targets to all 400 ordered
target pairs.  The faithful order-1920 label group acts diagonally on pairs;
its ambient C75 lift still has order 11520 and is never substituted for the
effective group.  Exact transport of the complete C90 joint-law payload gives
272 pair orbits: 144 singleton orbits and 128 doubleton orbits.  Orbit--
stabilizer, a finite Burnside count, relation type, and the transpose
involution are all certified.

The canonical evidence SHA-256 is
`099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696`.
The producer, an independent inclusion-column closure decoder, SymPy, clean
replay, and 14 hostile mutations pass.  This is a finite symmetry quotient
under `NO_BAD_EULER_OR_ROOT_NUMBER`, not a full Burnside ring or table of
marks and not an arithmetic or operator claim.

Run from this directory:

```text
python -B code/c97_pair_orbit_quotient.py
python -B code/c97_pair_orbit_quotient_checker.py
python -B code/c97_sympy_crosscheck.py
python -B code/c97_replay_checker.py
python -B code/c97_mutation_test.py
```

Generate the final ledger only after the deterministic PDF is present:
`python -B code/c97_release_manifest.py`.
