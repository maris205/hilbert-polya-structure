# Test report

- producer: `C387_PRODUCER_PASS payload_sha256=367f48652a963b15b8b777afd6e1cd71dbb8a42f7b8060e6c4aed6c0181d270a grid={"fixed_torus_rows": 228, "flow_identity_rows": 171, "gammas": 3, "irrational_rows": 24, "orbit_rows": 1368, "rational_phases": 12, "return_multiplier_cutoff": 12, "signed_block_rows": 126, "slopes": 19}`
- checker: `C387_CHECKER_PASS exact_assertions=278369 independent_integer_lattice_recount=true`
- sympy: `C387_SYMPY_PASS exact_identities=271 signed_modes=true generic_parameters=true`
- replay: `C387_REPLAY_PASS isolated_directories=2 exact_byte_match=true`
- mutation: `C387_MUTATION_PASS rejected=48/48 repaired_hash_json=36 strict_yaml=10 names=least_period_0,displacement_0,least_period_731,displacement_731,least_period_-1,displacement_-1,missing_orbit,order,negative_returns,half_integer,fixed_tori,primitive_tori,return_matrix,isolated,reversal,section,negative_m,chirp_sign,domain,irrational_return,time_one,heat_compact,target_route,clock,baseline,bool_to_zero,unknown_field,flag_claims_automorphy,flag_claims_hilbert_polya_operator,flag_claims_root_number,flag_claims_target_arithmetic_local_data,flag_claims_target_divisor_or_counting_law,flag_claims_target_euler_factors,flag_claims_target_functional_equation,flag_claims_target_zero_match,flag_invokes_route_b,duplicate_json,nonfinite_json,yaml_unknown_field,yaml_bool_zero,yaml_date_timestamp,yaml_duplicate,yaml_anchor,yaml_alias,yaml_merge,yaml_nonstring,yaml_route_promotion,yaml_route_b`
- smoke: `3 tests PASS`

All six script optimized-mode refusal gates, strict source/YAML gates, exact membership and PDF checks passed. Finite evidence is regression, not an infinite proof.
