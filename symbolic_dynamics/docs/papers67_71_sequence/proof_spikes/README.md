# Proof-spike controls

Run from the repository root:

```sh
python3 docs/papers67_71_sequence/proof_spikes/verify_stage1_spikes.py
```

The script performs eight bounded checks:

1. P67 prefix-constraint ranks and `(a,b)`-exponent-rectangle dimensions;
2. P68 three complete-bipartite hom-shift box counts, plus the analytic
   orientation-covariance checksum;
3. P69 Rudin--Shapiro identity `R(n)=max_(m<=n) rho(m)` through length 256,
   including the dyadic factor-range formula through length 256;
4. the surface-flat reserve's direct `S_3` homomorphism counts and a raw `C_2`
   flat-connection count on a concrete two-sheeted cover;
5. P70 full finite-Heisenberg convolution-matrix nullities against the proposed
   cyclotomic/characteristic formula;
6. P71 recovery of one zip fibre profile from fixed-point local degrees and a
   weighted periodic signature through period five;
7. the explicit counterexample that killed the proposed universal torus-coding
   formula `p(M,N)=(M+1)N`;
8. the length-two Dyck-histogram counterexample to
   `N_n(k)=binom(n,k) M^max(k,n-k)`: at `n=2`, `k=1`, the actual count is
   `M+M^2` (six for `M=2`), whereas the formula predicts `2M` (four for
   `M=2`).

Expected final line:

```text
ALL STAGE-1 FINITE CONTROLS PASS
```

These are regression tests and hostile falsifiers.  They do not prove any
infinite theorem, recognizability statement, entropy variational principle,
or novelty/priority claim.
