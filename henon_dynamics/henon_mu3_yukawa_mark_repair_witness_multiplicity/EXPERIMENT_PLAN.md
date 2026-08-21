# C79 experiment plan

1. Lock the C73, C75, C76, C77, and C78 evidence/manifests by raw-byte SHA-256.
2. Reconstruct the finite point-set closure table independently and enumerate
   every deletion mask and every minimum restoration witness.
3. Derive the block-state witness formula and the complete
   `x,rho,W` coefficient table.
4. Run the independent checker, symbolic cross-check, clean replay, and
   hostile semantic mutations.
5. Build and inspect the paper twice in isolated directories and freeze a
   manifest that excludes itself and transient LaTeX/cache files.

No arithmetic/local, Euler-factor, root-number, automorphy, Burnside-ring,
table-of-marks, or Hilbert--Polya claim is in scope.
