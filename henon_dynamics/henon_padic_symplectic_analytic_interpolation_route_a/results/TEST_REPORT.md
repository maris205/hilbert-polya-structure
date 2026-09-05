# Actual test report

Fresh commands completed successfully in the release run. These are finite exact checks, not universal theorem proofs.

```text
C394 producer PASS: {"displacements": 2880, "finite_levels": 56, "payload": "7085faf0dba4be3d15fad62c40630cbd19f6ab4e757c7188af71342f2339daae", "polynomial_coefficients": 512, "residue_points": 109876, "tails": 1024}
C394 independent checker PASS: {"assertions": 66481, "displacements": 2880, "finite_levels": 56, "payload": "7085faf0dba4be3d15fad62c40630cbd19f6ab4e757c7188af71342f2339daae", "residue_points": 109876}
C394 exact symbolic PASS: identities=4592
C394 two-directory byte replay PASS: sha256=53df1f26a3ec5586fb3cce0b4d127659afc3ebcf912589714d10a23bc409f039
C394 hostile PASS: {"actual_symlink_write_refusals": 1, "actual_yaml_write_refusals": 10, "names": ["baseline", "epoch_bool", "route_bool_zero", "scope_bool_zero", "scope_bool_float", "route_upgrade", "overall_upgrade", "prime_float", "parameter_bool", "level_bool", "radius_bool", "shell_population", "shell_period", "shell_cycles", "cycle_length_bool", "fixed_iterate_bool", "fixed_count", "displacement_prime_bool", "displacement_radius_bool", "base_time_bool", "end_time", "precision_cap", "observed_valuation", "difference_coordinate", "difference_order_bool", "coefficient_exponent_bool", "coefficient_bool", "coefficient_value", "factorial_valuation_bool", "tail_bound", "dyadic_margin", "zero_parameter_control", "threshold_control", "pointwise_control", "genuine_periodic_control", "origin_derivative", "clock_promotion", "flag_claims_automorphy", "flag_claims_hilbert_polya_operator", "flag_claims_root_number", "flag_claims_target_arithmetic_local_data", "flag_claims_target_divisor_or_counting_law", "flag_claims_target_euler_factors", "flag_claims_target_functional_equation", "flag_claims_target_zero_match", "flag_invokes_route_b", "unknown_root", "unknown_nested", "missing_level", "reordered_displacements", "duplicate_json", "nan_json", "infinity_json", "yaml_write_unknown", "yaml_write_false_to_zero", "yaml_write_unquoted_date", "yaml_write_duplicate", "yaml_write_anchor", "yaml_write_alias", "yaml_write_merge", "yaml_write_nonstring", "yaml_write_promotion", "yaml_write_route_b", "actual_symlink_write_refusal"], "rejected": 64, "repaired_hash": 50, "strict_json": 3, "total": 64}
C394 smoke PASS: 3/3
C394 optimized-mode refusal PASS: six scripts under -O and -OO, 12/12 refusals
```
