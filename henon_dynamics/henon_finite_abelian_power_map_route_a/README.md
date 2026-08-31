# HCS-C264 — finite abelian power-map atlas

This self-contained Route-A package classifies the functional graph and full-function Koopman operator of the map (P_d:g\mapsto g^d) on every finite abelian group. For (d\ge1), a canonical prime-support splitting (G=A_d\times B_d) separates a periodic automorphism from a nilpotent transient map. The package derives every cycle count, fixed-point count, primitive count, finite dynamical zeta factor, tail layer, image rank, and zero-eigenvalue Jordan-block multiplicity. The constant map (d=0) is handled as a separate strict boundary.

The proof is uniform in the group and exponent. The finite corpus is a regression oracle, not the logical basis of the theorem: 34 group types and (d=0,\ldots,18) give 646 maps and 21,280 directly enumerated group elements.

Release boundary: `NO_BAD_EULER_OR_ROOT_NUMBER`. Route tuple: `(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route B is disabled. The certificate claims workspace ownership only, not literature priority.

Run the six scripts in `code/` in producer, checker, SymPy, replay, mutation, manifest order. The paper PDF is `paper/main.pdf`.
