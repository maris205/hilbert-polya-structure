# Paper plan

**Working title:** Leftmost Reassociation of Dyck Components: Exact Transient
Layers and Terminal Depth Fibres
**One-sentence residual:** After subtracting deterministic leftmost rotations,
ground-level comb covers, and the plane-tree graft/lift model, retain only the
owner-unresolved conjunction of the literal selector's closed all-time orbit
with one specified target preimage at every feasible depth.
**Format:** anonymous `amsart` short theorem note
**Status:** **OWNER-THIN / HOLD_EXTERNAL**
**Date:** 2026-09-01
**Target length:** 5--6 pages including references
**Figures:** none; the factorisation formulas carry the complete mechanism.

## Claim--evidence matrix

| Claim | Formal evidence | Exact control | Credit boundary |
|---|---|---|---|
| Every nonfixed step removes exactly one primitive factor and `tau(P)=k(P)-1`. | Closed iterate formula proved by induction. | Every iterate for every path through `n=12`. | Root-degree clock under the plane-tree graft model is zero standalone credit. |
| Fixed paths are primitive; their count is `Cat_(n-1)`; the unique deepest path is `(UD)^n`. | Factor monotonicity, outer-step deletion, and positive component sizes. | Fixed census and unique sharp source through `n=12`. | Catalan enumeration is zero credit. |
| Depth layer `k-1` has `k/(2n-k) binom(2n-k,n)` paths. | `(zC(z))^k` and an explicit Lagrange-inversion calculation. | Every layer through `n=12`. | Ballot enumeration and generic coefficient extraction are zero credit. |
| A fixed target with `r` interior primitive factors has exactly one basin state at each depth `0,...,r`. | Explicit suffix-cut construction and converse from unique factorisation. | Every fixed target and every feasible depth through `n=12`. | Suffix lift is zero as a representation; only its exact conjunction with the full temporal law remains owner-unresolved. |
| The unique largest terminal fibre has size `n` at `U(UD)^(n-1)D`. | Fibre size `r+1` and `r<=n-1`, with equality classification. | Unique maximizer through `n=12`. | No extremal originality or priority claim. |

## Section structure

### Abstract (180--220 words)

- State the literal repeated-leftmost rule immediately.
- Give the exact clock, unique deepest source, layer formula, and pointwise
  terminal fibre in compact form.
- State the zero-credit boundary and owner-thin/HOLD_EXTERNAL status.
- Do not cite sources in the abstract.

### 1. Introduction (about 1 page)

- Motivate the distinction between an atomic cover and the dynamics induced by
  a deterministic selector.
- State the technical story without claiming literature priority.
- List four falsifiable results matching the matrix.
- Explain that standard Tamari, Catalan, ballot, and primitive-factor facts are
  inputs rather than contributions.
- State why no figure is needed: the exact iterate formula is the mechanism.

### 2. Dyck factors, the map, and the complete theorem (about 1.25 pages)

- Define Dyck paths, semilength, primitive paths, unique factorisation,
  factor count, entry time, endpoint, and the update.
- Prove closure/well-definedness.
- Give the standard ordered-plane-tree contour conjugacy: graft the second
  root child to the first as rightmost child; inverses lift a child suffix.
- State one theorem with clauses for recurrence, clock, layers, terminal
  depth-fibres, and the unique largest fibre.

### 3. The factor-count clock (about 1.25 pages)

- Prove the closed form for every iterate by induction.
- Derive exact factor drop and absence of nontrivial recurrence.
- Count fixed paths by deleting outer steps.
- Prove `k<=n` and equality only for `(UD)^n`.

### 4. Complete temporal layers (about 1 page)

- Introduce the Catalan series only after the dynamical depth has been reduced
  to component count.
- Derive `(zC(z))^k`.
- Include the Lagrange-inversion algebra, including the `n=k` boundary case.
- State the temporal polynomial and bivariate generating function as
  consequences, while assigning generic extraction zero credit.

### 5. Terminal depth-fibre atlas (about 1.5 pages)

- Prove the endpoint formula.
- For `T=UQ D`, cut the primitive factorisation of `Q` before its last `d`
  factors and construct the unique depth-`d` source.
- Prove the converse by return positions and uniqueness of factorisation.
- Derive the geometric depth-fibre polynomial and unique maximum fibre.
- Include small textual examples for boundary cases `r=0` and `d=r`.

### 6. Exact finite controls (about 0.75 page)

- Describe the independent tuple implementation of the literal update.
- Report complete coverage through `n=12`, 290,511 states, 82,500 fixed
  targets, and 6,005,502 assertions.
- Include a compact selected-size table.
- State that computation is not proof or owner evidence.

### 7. Ownership boundary and conclusion (about 1 page)

- Synthesize sources by role: associativity lattice, path cover, primitive
  component enumeration, Catalan background.
- Compare `Phi_n` explicitly with Pallo's distinct deterministic leftmost
  rotation and with the Pallo/Chapoton ground-level comb covers.
- Use the fixed-root count to exclude equality and mirror/reversal conjugacy
  with Pallo (2006).
- Explicitly subtract deterministic leftmost scheduling, comb/height-zero
  covers, the plane-tree graft/lift model, root-degree clock, and component
  census.
- Restrict the residual to the exact all-time/target-fibre conjunction only.
- Record owner-thin limitations and HOLD_EXTERNAL.

## Citation plan

- Introduction and ownership boundary:
  `HuangTamari1972Associativity`,
  `BousquetMelouFusyPrevilleRatelle2012Intervals`,
  `Pallo2006Rotational`, `Pallo2003RightArm`,
  `Chapoton2020DyckOrder`.
- Primitive factorisation and component census:
  `PanayotopoulosSapounakis2002Prime`.
- Catalan/Dyck/plane-tree conventions:
  `Stanley2015Catalan`.
- Every cited item is verified in `SOURCE_VERIFICATION.md`; the bibliography
  contains only these seven entries.

## Figure plan

No figure is planned or needed.  The requested package is a short exact note,
and the formula

```text
Phi^t(P)=U A C_2...C_(t+1) D C_(t+2)...C_k
```

already exposes the state change, clock, and endpoint without a visual layer.

## Author-side checks

- Every theorem claim is at or below the frozen contract ceiling.
- Full proofs remain in the main text; there is no proof appendix.
- No author names, affiliations, acknowledgements, self-citations, or external
  release language appear.
- Round-1 changes are restricted to owner/source and planning repairs; the
  independent round-2 review accepted the package after one abstract-range
  clarification, without changing the theorem contract.
- Compilation, citation, font, metadata, and exact-control checks are recorded
  in `BUILD.md` and `CONTROL_RESULTS.md`.
