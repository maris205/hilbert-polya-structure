# Evidence boundary

- FLINT's ECPP documentation specifies a certificate chain
  (n_i, a_i, b_i, m_i, q_i, P_i), its conditional primality step, the bound on
  q_i, and the transition n_(i+1) = q_i.
- This record uses that documentation only to classify ownership and the
  elementary strict descent q_i <= n_i/2. It makes no claim about ECPP
  complexity, completeness, curve-search behavior, or a new primality theorem.
- No target integer, prime table, curve computation, point computation, numerical
  orbit, roof, determinant, or Route evaluation was used.
