# Verification report

108 complex rational terms; 16 exact action rows; 12 tail/derivative controls. Symbolic receipt: 3 identities, 9 series/ODE cases, 3 direct K integrals, 12 roots, 3 norm identities and 1 full resolvent trace.

Producer and independent checker were actually executed; symbolic/high-precision lane also passed. The exact payload lives in c398_wall_evidence.json. Replay, hostile and smoke receipts are reconstructed by the release script rather than trusted from this prose. Finite evidence is not an infinite theorem.

Initial checker left cosh(log(r)) unevaluated for a rational r and Rational conversion failed. Rewriting cosh through exponentials fixed the representation, without changing evidence or theorem. The first full trace quadrature at E=-1 passed but was slow; the final regression uses the same full kernel at E=-1/4, where half-integer Bessel identities reduce it to a fast elementary integral, independently compared with the determinant derivative.
