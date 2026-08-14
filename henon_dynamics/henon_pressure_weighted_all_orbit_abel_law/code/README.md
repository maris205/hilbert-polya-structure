# HCS-P53 code

`c53_all_orbit_abel.py` produces the exact/finite certificate for the
pressure-weighted all-orbit Abel theorem.  It reconstructs half-cyclotomic
trace polynomials, exact trace-field norms, Mahler spectral heights, four
per-orbit Abel sentinels, and a three-orbit pressure-weighted joint profile.

`abstract_salem_stress` is deliberately marked `source_native_h6=false`.
It exercises the unit-circle-conjugate branch of the proof and is never
promoted to an H6 periodic orbit.

`independent_check.py` recomputes dependency hashes, Mahler heights, unit
circle counts, exact norm sentinels, Abel constants, Gamma targets, and the
claim firewall by a separate code path.  `test_c53.py` adds unit and
adversarial tests.

Run the complete finite suite with:

```bash
bash code/run_c53.sh
```
