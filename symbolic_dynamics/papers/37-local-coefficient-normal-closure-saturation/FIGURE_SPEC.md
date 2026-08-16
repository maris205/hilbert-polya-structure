# Paper 37 figure specification — SD-C39

All artwork is writer-owned pure TikZ. No external image, rasterization,
opacity, color-only distinction, or data-driven plotting script is used.
Labels must remain legible at ordinary A4 scale and in grayscale.

## Figure 1 — finite-coefficient saturation fork

File: `figures/coefficient_fork.tex`.

- Common source box: unquotiented affine Hashimoto shift, source damping,
  bounded invertible edge transport, and one unit marker `z`.
- Upper branch: ordinary invertible holonomy; factor deletion requires
  nilpotence; stop badge `cannot delete`.
- Middle branch: graded direct-relator match; arrow to mixed word leakage with
  `-4r^4(r-1)`.
- Lower branch: full normal-closure saturation; arrow to every closed factor
  cancelled and `Z_gr=1`.
- Final shared badge: `no selective primitive sector`.
- Caption must explain all three branches without relying on the body text.

## Figure 2 — direct match versus mixed witness

File: `figures/shear_leakage.tex`.

- Left panel: `A`, `B_r`, and `B_(-r)` feed the direct relator.
- Center badge: equal determinant polynomials, so every direct repetition
  cancels.
- Right panel: the six-segment closed path based at `(r^2,0)` for `M_r`.
- Bottom callout: mixed supertrace `-4r^4(r-1) != 0`.
- Visual distinction must use line style and labels in addition to color.

## Figure 3 — normal-closure saturation funnel

File: `figures/normal_closure_funnel.tex`.

- Top row: translated cells, conjugates, inverses, and repetitions.
- Middle: arbitrary finite mixed products `product a_j R^eps_j a_j^-1`.
- Lower: every cyclically reduced closed Cayley label.
- Bottom: all primitive factor terms vanish, `log Z_gr=0`, `Z_gr=1`.
- A dashed side comparison says direct-cell matching alone does not pass
  through the funnel.

## Shared visual language

- `formalblue`: frozen source, matrices, and definitions.
- `deepgreen`: valid determinant ownership and exact equality.
- `warningamber`: incomplete cancellation or object boundary.
- `stopred`: leakage, erasure, or route stop.
- `softgray`: grouping and normal-closure regions.
- Solid arrows are proved constructions or implications; dashed arrows are
  failed comparisons and are never claimed maps.
