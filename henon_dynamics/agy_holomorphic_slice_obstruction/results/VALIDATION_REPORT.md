# HCS-C26 independent validation report

## Material Passport

- Origin: independent implementation; producer import forbidden
- Origin Mode: `validate`
- Origin Date: 2026-08-10
- Verification Status: `VERIFIED`
- Version Label: `c26_independent_check_v1`

The independent checker rebuilds every elementary Rauzy move and does not
import `c26_producer.py`.  All fourteen registered checks pass:

```text
literal_seven_state_fourteen_edge_graph                         PASS
state4_gamma_star_later_left_B_and_transposed_R                 PASS
finite_gamma_star_decoder_application_witness_only              PASS
exact_x0_normalizer_and_dimension_four_jacobian                 PASS
positive_prefix_column_hull_margin_and_birkhoff_ratio           PASS
complex_dimension_three_principal_right_half_plane_metadata     PASS
one_two_and_spectral_three_return_characteristic_polynomials    PASS
perron_projective_denominator_and_trace_atom_simplification     PASS
sigma_zero_and_one_single_branch_coefficient_floors             PASS
conditional_slice_assumption_chain_complete                     PASS
external_C24_C25_theorems_not_claimed_reproved                  PASS
no_collision_or_central_sign_averaging                          PASS
finite_length_20_sentinel_replayed_as_nonproof                  PASS
claim_scope_firewall                                            PASS
```

The checker independently recovers

```text
states                     7
edges                      14
AGY base state             4
gamma_star length          128
S_gamma_star(x0)           15076979616018/8999921
J_gamma_star(x0)           S^(-4)
complex-cone delta         14783/1642663
Birkhoff theta             12206150825/12121793906
Birkhoff q bound           0.00173375049763643206391704653769
periodic trace examples    3
two-return word length     391
three-return word length   650
sentinel first returns     13528
sentinel matrix collisions 0
sentinel digest            8dfa54831399b1b528df41e47c6ebe99a8032b0e6ab9529250bb1de2e67c29fa
```

The projective Jacobian is recomputed from a direct three-coordinate affine
derivative; the checker does not accept the exponent from certificate
metadata.  The exact `sigma=0` coefficient equals that Jacobian, and the
`sigma=1` coefficient equals the Jacobian divided by `S`.

The checker recomputes the normalized-column hull, scans all positive-prefix
cross ratios exactly, and independently verifies the rational enclosure of
the Birkhoff contraction coefficient.  It also rebuilds the one-, two-, and
three-return matrices and characteristic polynomials.  It confirms that the
two-return AB/BA pair is spectrally cyclic while the three-return noncyclic
reversal has a different reciprocal polynomial.  Starting from a
different Perron vector, it uses a centered finite difference rather than
the producer's analytic derivative to verify
`det(I-Dp_A)=chi_A'(lambda)/lambda^3`.

Validation of the theorem block means that every necessary assumption and
external dependency is present with the correct evidence status.  It does
not mean that an unspecified holomorphic space has been constructed or that
the external theorems were re-established computationally.
