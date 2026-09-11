# P187 Review B — proof rederivation note

## Reviewer-owned route

Review B does not import the author verifier or Review-A transfer controls.
Instead it rewrites the fibre law prime by prime through cyclic
difference-constraint propagation:

- exponent targets are attacked by solving `(u_i-u_{i+1})_+=b_i` around the
  cycle for each start value `u_0`;
- composite targets are reconstructed from the product of the primewise fibre
  counts;
- fixed states, the sharp clock, the all-one target, the `m=1,2` edge cases,
  and the common-prime image obstruction are rechecked directly from this
  representation.

## Verified control surface

- exponent boxes: every `(a,m)` with `1 <= a <= 4`, `1 <= m <= 6`;
- composite boxes: every `(N,m)` with
  `N in {1,2,4,6,12,18,36,60}` and `1 <= m <= 4`;
- exact reviewer assertions: `219556`.

The successful finite checks are regression evidence for the frozen theorem
package only. They do not convert bounded computation into proof and do not
change the owner boundary.
