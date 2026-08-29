# Author proof and scope self-check — P109

## Claim

For the image map `T(U)=N(U)` of a regular nilpotent endomorphism on the full
subspace lattice of `F_q^d`, prove the exact iterated fibre and transition
formulas, the absorption and periodic census, and the stated rigidity
classification.

## Status

**PROVABLE AS STATED**, with the explicit `d=1` non-rigidity exception.

## Assumptions

- `q` is a prime power.
- `d>=1`.
- `N^d=0` and `N^(d-1)!=0`, equivalently `N` has one nilpotent Jordan block.
- Dynamical conjugacy means a bijection of phase sets intertwining the maps.

## Dependency map

1. The iterate law uses functoriality of linear images.
2. The fibre theorem uses the exact sequence
   `0 -> ker N^t -> (N^t)^(-1)(W) -> W -> 0`.
3. The joint transition formula uses only the fibre theorem and the number of
   `s`-subspaces of `im N^t`.
4. The absorption theorem uses the iterate law and the kernel staircase
   `dim ker N^t=min(t,d)`.
5. Periodic uniqueness uses nilpotency directly and does not depend on the
   fibre count.
6. Rigidity uses the depth theorem, uniqueness of the fixed point, and the
   exact identity `G_2(q)=q+3`.
7. The second proof route derives the intersection count from a hyperplane
   recurrence and Gaussian Pascal, independently of the exact-sequence graph
   parameterization.

## Boundary audit

- `t=0`: identity fibres are recovered.
- `t=d`: every subspace maps to zero and the fibre formula becomes the full
  Gaussian rank count.
- `W` outside `im N^t`: the fibre is empty.
- invalid `r,s`: the Gaussian-zero convention handles them.
- `d=1`: `q` is not recoverable; the theorem says so rather than hiding the
  collision.
- characteristic two and non-prime fields: the proof is characteristic-free,
  and controls include `F_4`, `F_8`, and `F_16`.

## Production self-check

This is an author-side scope and production check, not an independent hostile
review.  Both proof routes were checked against the listed endpoints and the
control was replayed.  The first PDF pass exposed lost leading backslashes in
several cross-reference commands; the final visual pass also exposed one
literal `qquad` in the kernel/image definition.  Those production defects were
repaired, the four-stage build was repeated, and extracted text was rechecked.

## Open risks

- The main residual risk is external ownership: invariant-subspace and
  Gaussian-intersection ingredients are mature, while the exact temporal
  conjunction has only a bounded search record.
- An independent reviewer should rederive the uniform-fibre graph count and
  verify that the hyperplane recurrence is sufficiently independent for the
  stated two-route claim.
- No final QA or public-release decision is made here.
