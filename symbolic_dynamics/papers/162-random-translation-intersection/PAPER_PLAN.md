# P162 paper plan — Random Translation Intersection (RTI)

**Format:** anonymous `amsart`, compact theorem paper  
**Lifecycle:** `HOLD_EXTERNAL`  
**Gate inherited:** `GREEN_AFTER_REQUIRED_MINOR_REPAIR`; the required `s=0`
one-step boundary is incorporated explicitly.

## Central question

For the random process on subsets of `V=F_2^d`,

```text
A <- A intersection (A+v),       v uniform in V,
```

what information about the whole history controls the current state, how
long can a non-full source survive, and how many source/history pairs reach
an arbitrary prescribed target?

## Theorem spine

1. **History-span identity.** A history acts as erosion by its generated
   subspace: `A_t=E_{H_t}(A_0)`.
2. **Rank law and sharp clock.** Count ordered histories spanning each fixed
   subspace, derive the full rank distribution and mean full-span time, and
   prove sharpness with `A*=V\{0}` via `E_H(A*)=V\H`.
3. **Every-target weighted inverse atlas.** For target `B`, histories can
   reach it only through subspaces of `Stab(B)`.  Conditional on such a
   subspace, each outside affine coset contributes an independent proper
   subset.  Summing over subspace ranks gives the complete source-size
   polynomial at every time.
4. **Boundary and recovery.** State the one-step unweighted formula in two
   branches (`s=0` and `s>=1`), cover `d=0`, `t=0`, empty/full targets, and
   recover `d` from phase size and `s` from target size plus one-step inverse
   mass.

## Proof dependency map

```text
erosion composition -> history-span identity -> forward state
finite-field spanning histories -> rank law -> full-span clock
fixed-span affine-coset lemma -> every-target polynomial -> fibre recovery
sharp witness V\{0} -> equality in the universal absorption bound
```

The inverse polynomial does not follow from the rank law: it additionally
uses the target restriction `H <= Stab(B)` and proper-subset choices on each
outside affine coset.

## Section plan

1. Process, notation, and combined main theorem.
2. History spans and sharp absorption clock.
3. Stabilizer-weighted inverse fibres and boundary-safe recovery.
4. Owner subtraction, deterministic controls, limitations, and declarations.

## Ownership and claim boundary

Zero contribution credit is assigned to:

- erosion/intersection-of-translates algebra (Heijmans--Ronse);
- generic morphological iteration (Heijmans--Serra);
- stochastic morphology (Sivakumar--Goutsias); and
- finite-field random-rank laws (Balakin).

The paper evaluates only their exact conjunction with the sharp witness,
arbitrary-target source/history polynomial, and phase/fibre recovery.  The
bounded source non-hit is not a novelty or priority assertion.  External use
requires a new literature review of the final wording.

## Verification and build contract

- The verifier must not import scout or hostile-gate code.
- Literal iteration is compared with an independently computed span erosion.
- Every coefficient for every target is checked in exhaustive small boxes.
- Rank, clock, sharp witness, stabilizer, `t=0`, `d=0`, empty/full, odd-cardinality,
  and post-cap boundaries are explicit.
- Two fresh runs must produce byte-identical output before `CANONICAL.txt` is
  frozen.
- The PDF is built from `main.tex` and `references.bib`, then checked for
  unresolved references, boxes, fonts, metadata, anonymity, and visible
  `HOLD_EXTERNAL` status.
