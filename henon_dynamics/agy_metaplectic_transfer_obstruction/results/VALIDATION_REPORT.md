# HCS-C25 independent validation report

## Material Passport

- Origin: independent implementation; producer import forbidden
- Origin Mode: `validate`
- Origin Date: 2026-08-10
- Verification Status: `VERIFIED`
- Version Label: `c25_independent_validation_v2`

The checker contains its own Rauzy move, graph, matrix, decoder, projective
derivative, state-elimination, and stress-replay implementations.  It does
not import `c25_producer.py`.

All eleven registered checks passed:

```text
literal_seven_state_graph_and_edge_transport                 PASS
statewise_integer_symplectic_trivialization                  PASS
source_locked_AGY_word_closed_and_neat                       PASS
eight_complete_3d_minus_4_strong_positivity                  PASS
later_left_matrix_determinant_positivity_and_form            PASS
projective_x0_y0_roof_and_exp_minus_4r_jacobian              PASS
all_length_decoder_gamma_trace_and_theorem_invariants        PASS
central_first_return_rational_language                       PASS
length_22_nonproof_stress_replay                             PASS
toy_ttt_and_AGY_section_scope_separation                     PASS
operator_claim_boundary_no_averaging_no_smoothing            PASS
```

The independent replay verifies the exact `128 x` arrow chronology,
`det(B)=1`, strict positivity, both transported-form identities, the complete
128-step row-subtraction trace, and the rational points `x0`, `y0`.  It also
rebuilds all seven state frames and all fourteen fixed-fiber edge matrices;
the independently recovered split is six identity and eight nonidentity
edges.  It differentiates the projective branch in three simplex coordinates
and obtains `S(x0)^(-4)` exactly; the exponent is not accepted from metadata.

The optional stress replay independently obtains 35,420 central first-return
words through length 22, 35,420 decoder recoveries, 35,420 distinct matrices,
and the same canonical word-matrix SHA-256 digest.  The checker confirms that
the finite window is labelled as a mutation sentinel rather than the proof.

The validation also enforces the claim boundary: the full-matrix decoder is
promoted to absolute homology only because this four-letter `H(2)` crossing
form has determinant one.  The certificate explicitly disclaims that
promotion in the presence of a relative-homology kernel.

The metaplectic statement is also scoped: the checker proves that every
fixed-fiber integral symplectic edge has two possible lifts and that chosen
edge lifts can be composed along labeled paths.  It does not select central
signs or assert a group-theoretic splitting.
