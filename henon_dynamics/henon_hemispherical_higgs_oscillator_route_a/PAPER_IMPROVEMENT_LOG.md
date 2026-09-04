# Paper improvement log

## Round 0: exact classical action

Froze (omega>0), derived the turning polynomial and exact root integral,
inverted the action, and separated circular, meridional, equilibrium, and
classical zero-coupling faces.

## Round 1: Friedrichs quantum closure

Added the one-hemisphere operator domain, Jacobi eigenfunctions, exact levels
and multiplicities, completeness argument, flat limit, and the distinction
between the Dirichlet hemisphere and full sphere at (omega=0).

## Round 2: identity revival and release boundary

Added the consecutive-gap necessity proof, the sufficient condition, the
(k=1) calculation proving the common phase is exactly one, and the reduced
fraction formula for (M_{min}). Added full evidence, collision, limitation,
and Route-A audits.

Every conditional manuscript round is compiled twice in fresh directories at
the frozen epoch. The release gate requires byte determinism, settled
warning-free logs, embedded/subset fonts, clean extracted text, and full page
rasterization.

## Release hygiene repair

Corrected two missing TeX escapes in the displayed revival criterion.  The
release source gate now rejects literal `quad` or `qquad` commands, the PDF
text gate rejects a leaked `qquad` token, and hostile tests prove that legal
`\quad` and `\qquad` commands are retained.
