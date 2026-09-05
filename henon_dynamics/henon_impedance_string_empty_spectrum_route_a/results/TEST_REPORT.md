# C396 actual executable test report

All listed lanes completed successfully in this release-write run. Exact and numeric results are regression, not interval certificates. Six code scripts were actually invoked under both -O and -OO: twelve optimized-mode refusals, including this release script.

```
C396 producer PASS {"boundary": 7, "green": 21, "pseudospectrum": 27, "spectrum": 126, "transport": 588} 015000cea0cbb302ac272b6a935a7f1bcadad585af53f955f8883695854f9fa3
```

```
C396 independent checker PASS caa73f4f09e4c4f45e5bf299df22c467a99dd4ec0d836847ab85795c036ed616 7+588 exact rows; 126+27+21 numerical rows
```

```
C396 symbolic/high-precision PASS {"complex_gauge_actions": 81, "interval_certified": false, "max_residual": "6.4405619e-60", "rayleigh_rows": 27, "singular_modes": 12, "symbolic_identities": 11, "volterra_actions": 81, "working_digits": 100}
```

```
C396 two-directory replay PASS 015000cea0cbb302ac272b6a935a7f1bcadad585af53f955f8883695854f9fa3
```

```
C396 hostile PASS {"authority": 1, "authority_refusals": 2, "distinct_mutations": 62, "physical_write_refusals": 2, "release_write_yaml": 10, "repaired_hash": 45, "serialization": 4, "strict_yaml": 10, "total_refusals": 73}
```

```
...
----------------------------------------------------------------------
Ran 3 tests in 4.302s

OK
```
