# Paper 36 figure specification — SD-C38

All artwork is source-owned TikZ. No external image, rasterization, opacity,
or color-only distinction is permitted. Labels must remain legible at normal
A4 reading scale and after grayscale conversion.

## Figure 1 — relation cell and marker mismatch

File: `figures/relation_clock.tex`.

- Left endpoint `x`, right endpoint `xvu=xu^r v`.
- Upper path: two arrows labeled `v,u`, marker `z^2`.
- Lower path: a compressed chain labeled `u^r,v`, marker `z^(r+1)`.
- A lightly filled cell between them labeled `C_(r,x)`.
- A red/amber callout: `z^2 != z^(r+1), r>=2`.
- Caption explains that filling the relation destroys the unit-step grading.

## Figure 2 — one-source object firewall

File: `figures/object_firewall.tex`.

- Common source box: formal reverse affine Cayley graph and Hashimoto shift.
- Upper branch: source damping, trace-class `T=DHD`, positive relation trace.
- Lower branch: attach every Cayley relation cell, contractible `K_r`, empty
  recurrent quotient.
- A central barrier labeled `not the same ledger / z does not descend`.
- The figure must not suggest that the lower branch is an operator compression.

## Figure 3 — generic chain-superdet control

File: `figures/superdet_generic.tex`.

- Three chain-level boxes `C_2`, `C_1`, `C_0` with multiplicities `+1,-2,+1`.
- Boundary arrows between them.
- Below, the equation `Str(A_tilde^n)=(1-2+1)tau(A^n)=0`.
- A generic-relator input fan shows that the relator word is never read.
- A stop badge says `exact cancellation, zero selectivity`.

## Shared visual language

- `formalblue`: definitions and source objects.
- `deepgreen`: valid operator ownership.
- `warningamber`: marker or object mismatch.
- `stopred`: failed route or generic-control stop.
- `softgray`: cell and background grouping.
- Solid arrows: genuine maps/constructions.
- Dashed arrows: comparisons only, never claimed identifications.
