# Route-A independent cross-subtype batch plan: C224--C228

Status: **completed; five theorem owners released**.

Date: 2026-08-29

Source commit: `489672bd36abd3a4f6da92d1446a0af575917959`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Frozen sequence

1. **C224:** Landau--Zener--Weber nonautonomous two-level crossing: exact
   asymptotic scattering law and Stokes phase, plus controlled finite-window
   propagators.
2. **C225:** finite M/M/1/K birth--death queue: stationary law, complete finite
   spectrum/kernel/mixing certificate, and finite-to-infinite capacity faces.
3. **C226:** one-phase Stefan free boundary: unique Neumann similarity root,
   endpoint asymptotics, flux partition, energy ledger, and singular faces.
4. **C227:** Lorenz-63: global absorbing ellipsoid and complete
   equilibrium/local-stability/Hopf/zero-rate atlas.
5. **C228:** product-kernel Smoluchowski gelation: exact pregel/critical law and
   a source-explicit Stockmayer versus Flory postgel closure boundary.

Collision decisions and rejected alternatives are frozen in
`IDEA_REPORT_C224_C228.md`.

## Uniform paper contract

Each candidate must release exactly 28 physical files: 27 content-addressed
payloads and one self-excluded release manifest.  The payload set contains the
theorem and research documents, executable producer/checker/symbolic/replay/
mutation/manifest code, evaluator YAML, three content-distinct revision PDFs
and the final PDF, together with the result and evidence artifacts.

Every package must pass a deterministic producer, a producer-independent
checker with recursive exact-schema closure, an independent symbolic or
algebraic reconstruction, canonical byte replay, repaired-hash/semantic/
unknown-key and stale-hash mutation tests, and manifest-ledger closure.  Each
paper receives two substantive revisions.  The final PDF must reproduce byte
for byte in two fresh fixed-epoch LuaLaTeX builds, embed and subset every
reported font, have clean settled logs and extractable text, and survive
page-by-page visual inspection.  Internal checks are artifact validation, not
external peer review.

## Proof and evidence contract

- C224 must keep the exact infinite-time Weber connection formula distinct from
  the finite RK4 window and report its nonzero Gram residual; no finite-time
  exactness is inferred.
- C225 must retain endpoint-rate and `K=0` conventions, distinguish finite
  reversible spectra from capacity-limit recurrence/mass escape, and avoid an
  unproved infinite continuous-spectrum statement.
- C226 must use corrected, source-audited bibliography metadata and keep the
  zero-superheat/zero-diffusivity/zero-latent faces as singular rescalings.
- C227 must distinguish a global absorbing bound and local Hurwitz/Hopf data
  from global chaos, nonlinear Hopf direction, or an orbit determinant.
- C228 must distinguish pregel conservation from postgel loss conventions and
  must not call the Flory continuation a general Smoluchowski solution or infer
  weak-solution uniqueness.

## Integrity and stopping gates

The ARS implementation-integrity and seven-mode failure audit covers source
ownership, citation existence/context, implementation bugs, hallucinated
results, shortcut reliance, bug-as-insight risk, methodology fabrication, and
frame lock.  No paper may introduce target-zero or prime tables, arithmetic
local data, Euler factors, root numbers, automorphy, a target
divisor/counting-law or functional equation, a Hilbert--Pólya operator, or
Route-B input.  The strict tuples are source-local decisions and do not become
positive arithmetic claims merely because a model has a spectrum or a
generating function.

## Completion condition

The batch closes only after all five executable suites, corrected citations,
three-round paper builds, fresh PDF reproducibility/font/log/text/visual
checks, manifests, cross-package theorem review, registries and README pass.
The scoped commit must then be pushed and verified equal to the remote head.
`BATCH_REVIEW_C224_C228.md` will freeze the final counts and hashes before the
next user checkpoint.
