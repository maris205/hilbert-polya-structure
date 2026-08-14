# Figure specification — Paper 32 / SD-C34

All manuscript figures are pure TikZ vector graphics.  They visualize proved
structural relationships rather than sampled data, so no rasterization,
interpolation, or statistical summary is involved.  Captions carry the
interpretive claim; no figure contains a decorative title.

## Shared visual grammar

| Semantic role | Color | Redundant encoding |
|---|---|---|
| source/projective object | `formalblue` | rounded rectangle, solid border |
| valid analytic ownership | `deepgreen` | double border or thick solid arrow |
| obstruction/universal flood | `warningamber` | diamond/hexagon, densely dashed arrow |
| forbidden terminal repair | `stopred` | octagon, crossed/dashed connector |
| neutral transport/control | `charcoal`/gray | thin dotted connector |

The palette avoids red--green as the sole distinction.  Shape, border style,
arrow pattern, and textual labels remain legible in grayscale.  Minimum text
size is the surrounding LaTeX `\small`; line width is at least 0.7 pt.

## Figure 1 — universal shared-state recurrence

**File:** `figures/projective_recurrence.tex`

**Placement:** Section 4, immediately after the modular-relations theorem.

**Composition:** Two projective blocks labelled “prime \(p\)” and “composite
\(m\)” contain representative shared states.  Each state has an \(S\)-marked
order-two orbit and an \(R\)-marked order-three orbit.  A central relation box
\(S^2=R^3=1\) points to both blocks.  The prime block uses blue and the
composite block amber, but identical orbit shapes make the crucial point:
both inherit the same recurrence.

**Caption claim:** Projective modular relations create marker-distinct,
shared-state recurrence for every modulus; the mechanism therefore cannot
separate primes from prime powers or mixed composites before weighting.

## Figure 2 — cusp-diamond obstruction

**File:** `figures/cusp_diamond.tex`

**Placement:** Section 5.

**Composition:** The primary square has vertices \(c_n,c_{2n},c_{6n},c_{3n}\)
and directional edge labels \(\times2,\times3,\div2,\div3\).  The vertex
\(c_{6n}\) is an amber hexagon labelled “composite”.  A lighter adjacent
diamond based at \(2n\) shares \(c_{2n}\) and \(c_{6n}\), visually proving
overlap.  A side annotation contrasts downward-only arrows (“transient”) with
bidirectional arrows (“primitive cycle”).

**Caption claim:** Bidirectional source-natural cusp correspondences create a
simple nonbacktracking primitive four-cycle for every base modulus, and
neighboring diamonds share recurrent states; orienting the maps only downward
removes all such cycles by making modulus monotone.

## Figure 3 — obstruction trilemma and route result

**File:** `figures/route_trilemma.tex`

**Placement:** Section 9.

**Composition:** Three large nodes show (i) the static field criterion
\(|X_n|=n+1\), (ii) universal recurrent flood, and (iii) same-object
trace-class Fredholm ownership.  The static criterion has a dashed red edge
to a crossed octagonal “block projector” node.  The recurrence and analytic
nodes feed the exact route tuple below.  A green border marks the A2 success;
an amber border marks A1 failure.

**Caption claim:** Static prime recognition, universal composite recurrence,
and honest analytic ownership coexist.  The only immediate connection from
static recognition to prime-only recurrence is the forbidden terminal block
projector, so A2 passes while A1 fails.

## Figure QA checklist

- [x] Pure vector TikZ source retained beside the manuscript.
- [x] No external image, hidden data, or target-zero information.
- [x] Captions are self-contained and state what the reader should notice.
- [x] Every color has a shape or line-style backup.
- [x] No red--green-only contrast.
- [x] No title inside the figure.
- [x] All mathematical labels use manuscript notation.
- [x] Figure widths fit `0.96\textwidth` and remain readable on A4 paper.
- [x] The diagrams make theorem-backed claims only.

## Figure/table trace

| Artifact | Source | Transformation | Supported manuscript claim | Limitation |
|---|---|---|---|---|
| Figure 1 | Theorem 4.1 / Proposition 5 | manual TikZ transcription of \(S^2=R^3=1\) | universal shared-state recurrence | schematic representative states, not a full finite graph |
| Figure 2 | Proposition 6 | manual TikZ transcription of the explicit cusp word | composite-diamond flood and overlap | displays two members of an infinite proved family |
| Figure 3 | strict Route-A record | manual TikZ synthesis of proved gates | A1 failure, A2 analytic success, terminal-gate prohibition | route summary, not an independent proof |
