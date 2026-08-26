# HCS-C182: periodic box--ball action--angle dynamics

This package freezes the periodic binary box--ball system for every `L>=2M`, every soliton content, every KTT/Takagi internal-symmetry sector, and every commuting carrier evolution `T_l`.  Its clear progress is an exact passage from the source action--angle theorem to componentwise and globally aggregated fixed points, primitive cycles, Artin--Mazur zeta factors, and the ordinary determinant of the finite counting-measure Koopman permutation.

The action--angle bijection and invariant-torus decomposition are explicitly attributed prior results, not novelty claims.  The new package-level synthesis is exact and all-parameter, while the finite scan is only a regression sentinel.

The Route-A verdict is

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`,

overall `ROUTE_A_REJECTED`.  Exact integrability and Smith arithmetic do not create an intrinsic prime origin or arithmetic clock.

Run the six release commands from this directory:

```text
python3 code/c182_periodic_bbs_producer.py
python3 code/c182_periodic_bbs_checker.py
python3 code/c182_sympy_crosscheck.py
python3 code/c182_replay.py
python3 code/c182_mutation.py
python3 code/c182_release_manifest.py
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
