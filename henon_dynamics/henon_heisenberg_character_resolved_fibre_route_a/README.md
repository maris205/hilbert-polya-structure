# HCS-C151: central-rotation-resolved Heisenberg fixed fibres

C151 completes the fixed-component question deliberately left open by C146.
For the frozen Heisenberg lattice automorphism, horizontal fixed classes at
iterate `n` form `Z^2/(A^n-I)Z^2`.  A class represented by
`m=(A^n-I)v` lifts to a clean fixed central circle exactly when the exact
rotation

```text
rho_n(v)=sum_(j=0)^(n-1) q(A^j v)-m_1 v_2  (mod 1)
```

vanishes.  The proof establishes invariance under changing the lift `v` by
an integer vector.  Since every rotation has denominator dividing
`Q_n=2|det(A^n-I)|^2`, finite root-of-unity orthogonality gives an all-iterate
component-count projector.

Exact histograms through `n=12` distinguish horizontal classes from actual
fixed circles.  At `n=12`, 103,680 horizontal classes produce only 144 fixed
circles.  Early Lucas/parity guesses fail (already at `n=10` and `n=12`) and
are explicitly rejected rather than extrapolated.

The package contains proofs, exact evidence, independent direct-cocycle and
SymPy reconstructions, byte replay, semantic mutations, two internal review
rounds, retained PDFs, and a self-excluded manifest.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_EXPLORATORY`; Route B is not authorized.
