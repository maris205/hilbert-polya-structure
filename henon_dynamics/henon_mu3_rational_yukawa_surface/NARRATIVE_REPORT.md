# HCS-C55 narrative report

Status: **DOCS_FINAL_NO_MORE_EDITS; exact finite controls, independent hostile
paper audit, and official compilation passed**.

## What this project is trying to finish

The preceding two projects found an unexpectedly small Hodge-theoretic core
inside the middle cohomology of a rationally descended quadric--cubic
fivefold. The core has rank ten and, after one Tate twist, the same Hodge
numbers as the third cohomology of a four-modulus Calabi--Yau threefold.

HCS-C55 asks whether that resemblance persists when the variety moves, and
whether it can be measured by an exact period invariant rather than by Hodge
numbers alone.

## The geometric move

The four invariant tangent directions are not automatically four parameters
in a displayed linear equation. To turn them into a genuine family, the
project works in the Hilbert scheme.

The complete intersection has unobstructed embedded deformations, and all
abstract deformations are induced by embedded ones. The finite rational group
form acts on the ambient projective space, so it acts on the Hilbert scheme.
Its fixed germ is smooth in characteristic zero. That fixed germ is generally
larger than four dimensions because it retains coordinate and equation-gauge
directions. A rational four-dimensional slice is therefore chosen
transversely to the kernel of Kodaira--Spencer.

This distinction is the key algebraization step: the slice has precisely the
four abstract invariant directions, while the restricted Hilbert universal
family supplies an actual algebraic family and an actual fiberwise group
action.

## The relative Hodge core

The nonconstant group scheme has rank \(24\), although only two geometric
elements are rational points. Its relative Reynolds correspondence is
defined intrinsically as the norm of the universal action graph. After
splitting, it is the familiar average of all \(24\) graphs.

The image on fifth cohomology is a rank-\(10\) polarized variation. Exactly
one Tate twist changes its types

\[
(4,1),(3,2),(2,3),(1,4)
\]

to

\[
(3,0),(2,1),(1,2),(0,3).
\]

The four base directions map isomorphically to the four-dimensional
\((2,1)\) piece. In this precise sense the projected period map is locally
maximal. The result is a CY3-type variation, not the cohomology of a
constructed CY3.

## Why the powers of \(y\) matter

The Cayley ring uses \(F=yC+zQ\). Four expressions that look superficially
similar have different mathematical roles:

\[
\begin{array}{c|c}
\text{role}&\text{class}\\ \hline
\text{tangent operator}&[yp]\\
\text{first Hodge variation}&[y^2p]\\
\text{third Gauss--Manin variation}&[y^4p^3]\\
\text{polarized top trace}&[y^5p^3].
\end{array}
\]

The number of Gauss--Manin derivatives is three. The fifth power of \(y\)
does not mean five derivatives: one factor belongs to the original Hodge
generator and another enters through the final pairing.

This ledger prevents two common errors: treating the first image as the
tangent operator, and tracing the third variation before pairing it with the
original Hodge line.

The semilinear auxiliary-variable convention is equally rigid:
\(D(y)=y\) and \(D(z)=\rho z\). This is forced by
\(D(C)=C\) and \(D(Q_\rho)=\rho^2Q_\rho\), so that \(D(yC+zQ)=yC+zQ\).

## The exact fingerprint

In the frozen rational tangent basis, the target calculation produces a
primitive integral cubic with \(20\) nonzero terms. Only its projective class
is intrinsic: changing the tangent basis acts by
\(\operatorname{GL}_4(\mathbf Q)\), and changing the trace normalization
rescales the whole cubic.

The surface cut out by this cubic is geometrically smooth. The rigorous
certificate is the gradient algebra: its exact Hilbert series is

\[
(1+t)^4
\]

and its length is \(16\). That forces the four partial derivatives to
have only the affine origin as common zero, hence the projective surface is
smooth. Smoothness, not factorization over \(\mathbf Q\), then proves
geometric irreducibility.

## What the cubic can and cannot decide

If an honest four-modulus CY3 family carries a polarized rational VHS
isomorphic to this projected core, its Yukawa cubic at the matched point must
be projectively \(\operatorname{GL}_4(\mathbf C)\)-equivalent to the HCS
cubic. A mismatch is therefore a genuine local no-go.

A match is much weaker. It says nothing by itself about higher Yukawa jets,
the full Gauss--Manin connection, monodromy, integral structure, or an
algebraic correspondence. It cannot be promoted to a motive.

The known \((1,4)\) \(\operatorname{Dic}_3\) and \(\mathbf Z_{12}\)
quotients are natural comparators. Their original paper does not compute the
required four-variable tensor, and the later mirror-side one-parameter
special geometry cannot replace it. The current honest label is therefore
NOT-COMPARABLE-WITH-CURRENT-DATA.

A separate future project may study the arithmetic of the cubic surface's
27-line scheme; it is not part of any C55 claim.

## Current state

All theorem-dependent exact and adversarial gates pass: \(R_{1,0}\), the
multiplication-by-\(y\) isomorphism, the four lifted operators, top-line
descent, direct-cube/20-trace agreement, and the complete scalar-leaf rebound
sweep. The exact code/results lane is a release candidate, and the official
paper build, documentation-hash backfill, and verified 47-entry full-project
inventory are complete. The manifest SHA-256 is reported only outside its
covered artifacts to avoid a self-cycle. The implementation commit remains a
later provenance step; the no-CY3/no-motive scope is unchanged.
