# P163 paper plan — Complemented-Shadow Dynamics (CSD)

**Format:** anonymous compact `amsart` theorem paper  
**Inherited gate:** `GREEN_REENTRY_AFTER_CONTRACT_STRENGTHENING`  
**Lifecycle:** `HOLD_EXTERNAL`

## One-sentence contribution

For complementation after the lower shadow on arbitrary set families, the
paper derives exact atomic and mixed-rank dynamics and classifies the whole
maximum-depth phase-space shell by a rigid central-slice condition, endpoint
rank support, and eventual period.

## Claims--evidence map

| Claim | Proof object | Exact pressure | Role in paper |
|---|---|---|---|
| even/odd atomic kernels | two-step Johnson neighbourhood plus dual predecessor distance | literal atomic iteration through `n=9` | forward engine, fully owner-subtracted |
| exact mixed-rank clock | simultaneous even/odd slice saturation and silent-atom boundary | every phase state through `n=4` | dynamics backbone |
| recurrent rank-support involution | connected Johnson layers and `phi(k)=n-k+1` | recurrent/fixed/period census through `n=4` | structural axis |
| complete atomic depth census | explicit singleton radii and parity inversion | every atom through `n=9` | temporal refinement |
| deepest iff and total | central equality rigidity, with all off-central atoms free | full phase spaces through `n=4`; central controls through `n=12` | central residual axis |
| support-refined deepest count | one central atom, nonempty chosen slices, optional silent atom | every support through `n=4` and symbolic product controls | central residual axis |
| eventual period-one/two products | orbit factorization of rank involution | exact `n=2,3,4` splits and products through `n=12` | independent refinement |
| every-target inverse atlas | cover inclusion--exclusion and stable nonempty-slice choices | every audited target through `n=4` | completeness infrastructure only |

## Section architecture

1. **Literal map and main contracts.** Define the two-level powerset carrier,
   atomic kernels, parity radii, rank support, recurrent states, and the full
   deepest-shell theorem.  Place the `n=2` exception directly beside the shell
   statement.
2. **Johnson kernels and mixed-rank clock.** Prove the square identity, even
   and odd kernels, union lift, exact clock, recurrent core, fixed counts, and
   zeta function.
3. **Central equality rigidity.** Separate even and odd ambient dimensions;
   prove the singleton central slice is necessary and sufficient, then count
   the free off-central layers.
4. **Support and period products.** Refine by the labelled endpoint support
   and factor invariant support choices over `phi`-orbits.
5. **Inverse completeness and claim boundary.** Record the target-cover and
   stable-fibre formulas, while assigning their generic mechanism zero value.
6. **Controls, limitations, declarations.** Freeze the exact transcript and
   visible `HOLD_EXTERNAL` posture.

## Boundary contract

- The main ambient domain is `n>=2`; `n=0,1` are verifier-only excluded
  controls because the silent atom changes the height.
- `n=2` has height one and twelve deepest states, split `6/6`; the central
  singleton predicate selects only eight.
- The empty family has tail zero; `{empty}` has tail one.
- The every-target inverse formula starts at `t>=1`; time zero is the identity.
- The empty target has two positive-time sources, and targets containing
  unsupported atoms have zero fibre.
- At `t>=n-1`, the image is exactly the recurrent rank unions, with parity
  retained through `phi^t(R)`.

## Owner and internal subtraction

Zero contribution credit is assigned to lower/upper shadows, Kruskal--Katona
extremality, the Johnson closed-neighbourhood identity, Johnson distances and
covering radii, Boolean-relation powers, generic eventual-period theory,
cover inclusion--exclusion, and zeta bookkeeping after cycle classification.
The bounded owner audit supports no originality or precedence statement.

Internally, P97 subtracts generic union growth, P110/P115 subtract the general
deepest-shell paper format, and P143 subtracts Boolean-relation dynamics.  The
remaining proof obligation is the specific mixed-parity equality rigidity and
its support-resolved free-layer census.

## Verification and build contract

- `code/verify.py` must import no scout or gate code.
- Two fresh runs must be byte-identical to `code/CANONICAL.txt`.
- Build from `main.tex` and `references.bib` only in two clean temporary
  directories.
- Final checks cover logs, citations, page size, fonts, metadata, extracted
  identity tokens, visual rendering, and visible `HOLD_EXTERNAL` status.
- At the Round-0 author-draft stage, hostile review and Git were outside the
  drafting task.  Both hostile reviews are now complete; Git remains a
  batch-level operation.
