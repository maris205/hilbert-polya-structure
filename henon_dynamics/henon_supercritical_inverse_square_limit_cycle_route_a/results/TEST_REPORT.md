# C391 actual executable test report

All listed lanes completed successfully in this release-write run. Exact and numeric results are regression, not interval certificates. Six code scripts were actually invoked under both -O and -OO: twelve optimized-mode refusals, including this release script.

```
C391 producer PASS d70db5719bfeb0820ad4027e5dd1279ce534f4c6b0518fc5bdd9f2489e44ba43 {'classical': 45, 'boundary': 27, 'scattering_algebra': 15, 'negative_levels': 60, 'continuum': 36}
```

```
C391 independent checker PASS d70db5719bfeb0820ad4027e5dd1279ce534f4c6b0518fc5bdd9f2489e44ba43 45+27+15 exact rows; 60+36 numerical rows
```

```
C391 symbolic/high-precision PASS {"bessel_ode_cells": 12, "boundary_matching_cells": 12, "green_wronskians": 12, "interval_certified": false, "log_period_cells": 36, "normalization_integrals": 3, "stone_jump_cells": 108, "symbolic_identities": 8, "working_digits": 100}
```

```
C391 two-directory replay PASS 069eabac801adf6c6ceabd14f8e9c0aa26ce5f79664f2d2365dc3e54671ae3a8
```

```
C391 hostile PASS {"distinct_mutations": 56, "release_write_yaml": 10, "repaired_hash": 42, "serialization": 4, "strict_yaml": 10, "total_refusals": 66}
```

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.821s

OK
```
