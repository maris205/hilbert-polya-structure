# C199 hostile audit

1. **Signed-offset erasure:** both `a>0` and `a<0` families force the correct
   orientation and stable half-axis.
2. **Heading confusion:** blade angle is separated from velocity heading,
   which gains `pi` when `u<0`.
3. **Energy laundering:** scattering angle is proved independent of `H`; state
   energy is independently recomputed.
4. **Smooth-measure overclaim:** `1/|omega|` is restricted to reduced open
   half-planes.  Its Haar lift is an off-line full measure, but the pointwise
   obstruction excludes only reduced/Haar-factor smooth densities, not every
   configuration-dependent full-flow density.
5. **Boundary collapse:** `a=0`, `omega=0`, and `H=0` are stated separately.
6. **Finite-grid overreach:** regression is explicitly not the theorem proof.
7. **Formal-operator promotion:** Poisson structure earns only an A4 hint, not
   a Hilbert–Pólya claim.
8. **Hash-only defense:** semantic mutations repair the hash before checking;
   unknown keys and stale hashes are both rejected.

All tested attacks are closed.  This is an internal hostile audit, not an
external review or acceptance assessment.
