# HCS-C143: inhomogeneous coined quantum walk

This package constructs a rational, spatially inhomogeneous coined walk on a
five-cycle.  It proves exact unitarity, antiunitary reversal, signed primitive
path ownership, and a nonzero secular-polynomial difference between two
equal-population coin arrangements.

## Entry points

- `THEOREM_PACKAGE.md` — definitions and complete proofs;
- `results/c143_quantum_walk_evidence.json` — canonical exact receipt;
- `code/` — producer, independent checker, SymPy reconstruction, replay,
  hostile mutation suite, and manifest builder;
- `paper/main.pdf` — final paper.

Strict tuple:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.
The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false.
