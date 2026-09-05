# Frozen exact audit plan

Use p=2,3,5,7. For each prime take two consecutive admissible parameter valuations and two unit coefficients: sixteen parameters total. Finite levels extend respectively to N=5,4,3,2, giving 56 parameter-level cases and 109876 residue vectors. The producer uses the proved shell formulas; the independent checker directly enumerates the expanded polynomial permutation, discovers every cycle, then reconstructs all shell and fixed-iterate rows.

At four radii and five unit-vector seeds, compare three base times and three later times. All 2880 displacement records use modulus p^(predicted valuation+3), so the observed valuation is strictly below the precision cap. There are 512 sparse integer finite-difference coefficients through order three and 1024 ordinary factorial-tail rows through order 64. The checker uses an independent SymPy substitution-difference recurrence for the coefficients, not the producer's binomial combination of iterates.

Controls cover a=0, the dyadic map -x, pointwise versus coefficientwise residue identity, finite versus genuine periods, and target-scope refusal. Two fresh working directories test bytes. Hostile repaired-hash cases test semantics and exact types; ten YAML cases exercise actual release-write refusal before any output. None of these finite lanes replaces a proof.
