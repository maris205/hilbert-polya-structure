# Hostile audit

## Mathematical attacks

**Attack: the transition probability ignores unequal block sizes.**
For a fixed attainable target, each source block has exactly two constant-bit
orientations regardless of its size.  Multiplying gives `2^{|pi|}` successful
bit vectors out of `2^n`.  Unattainable targets are explicitly zero.

**Attack: diagonal entries do not imply diagonalizability.**
Accepted.  The proof therefore uses the invariant rank flag and the lowering
relations `(K-lambda_k I)V_k subset V_{k-1}`.  Their product is a squarefree
annihilator.  No conclusion is drawn from triangularity alone.

**Attack: the critical limit ignores rounding of `t`.**
Accepted.  The theorem assumes convergence of `n^2/2^t`; it does not claim a
phase-free law after blindly flooring `2 log_2 n+c`.

**Attack: `n=0` makes the formula ambiguous.**
The contract is uniformly `n>=1`.  The empty-set extension and `0^0`
convention are excluded rather than silently mixed into evidence.

## Model attacks

Shared bits per block would never split a block.  Biased bits replace uniform
word injections by weighted allocations.  Persistent bits stop creating new
word coordinates.  Quotienting by block sizes removes labels and changes
multiplicities.  None is claimed by this theorem.

## Novelty and collision attacks

Binary breaking, occupancy, and absorption are classical and the
Diaconis–Pang–Ram Hopf-power paper is a close owner.  C301 claims a closed
labelled-set-partition derivation and reproducible package, not priority for the
general mechanism.  C194, C215, and C276 remain separately owned models.

## Route-A attacks

`det(I-zK_n)` is a finite Markov polynomial.  Calling it a “spectral
determinant” does not create a target Euler product.  Monotone refinement has
no nonconstant directed cycles, `2^t` is not a prime norm, no target functional
equation/divisor law is built, and rational diagonalizability is not a
Hilbert–Pólya lift.  All five rungs fail and Route B stays locked.
