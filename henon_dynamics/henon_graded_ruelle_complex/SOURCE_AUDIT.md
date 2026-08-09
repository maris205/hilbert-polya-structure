# Primary-source, theorem-scope, and novelty audit

## Audited status

The primary sources justify the classical ingredients and the corrected
pinning convention.  They do **not** directly supply the full
two-contracting/one-expanding, vector-valued, three-complex-dimensional
Hénon theorem asserted in the earlier release.

Accordingly, this source audit distinguishes:

- exact Hénon domain and finite-dimensional algebra already established;
- classical source theorems that may be used in a future proof;
- analytic gates that remain open and cannot be replaced by code metadata.

## Local source lock

The local dynamical source is the byte-locked Paper 5 manuscript:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`
- SHA-256:
  `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9`

Only its exact recurrence

\[
x_{n+1}=1-ax_n^2-x_{n-1}
\]

and area-preserving Jacobian are inherited.  Its numerical zero-fitting
claims are not used.

The immediate mathematical parent is the HCS-C22 T4/T5 certificate.  It
supplies the common real survivor, exact base disks, projective disk,
right-half-plane logarithm sector, and the local instability weight.  These
data establish the one-step geometry; they do not by themselves prove a
nuclear transfer-operator theorem.

## What the primary sources supply

### Ruelle

Ruelle's analytic construction treats genuinely contracting holomorphic
branches in arbitrary finite complex dimension.  On holomorphic cotangent
forms it supplies pullback operators, order-zero nuclearity, fixed-point
traces, and alternating determinant identities under its stated contraction
and domain hypotheses.

Ruelle's 1990 differentiable extension supplies vector-bundle and exterior-
power bookkeeping in a broader \(C^r\) framework, together with generalized
determinants in a proved spectral domain.  It is not an automatic analytic
nuclear theorem for the present mixed Hénon cross kernel.

- D. Ruelle, *Zeta-functions for expanding maps and Anosov flows*, Invent.
  Math. 34 (1976).  [Primary PDF](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf)
- D. Ruelle, *An extension of the theory of Fredholm determinants*, Publ.
  Math. IHÉS 72 (1990), 175--193.
  [Primary record and PDF](https://www.numdam.org/item/PMIHES_1990__72__175_0/)

These sources make exterior cancellation and holomorphic nuclear restriction
classical.  They do not write the C22G block cross kernel, prove its all-word
composition, or provide its common enlarged domains.

### Rugh and Baladi--Pujals--Sambarino

Rugh's pinning construction and the BPS presentation concern real-analytic
surface maps with one forward-contracting and one forward-expanding complex
coordinate.  BPS Definition 2.2 fixes input contracting data and output
expanding data, solves the input expanding coordinate, and computes the
contracting output.  Equations (2.5)--(2.6) settle the convention relevant
to the present lift.

BPS equation (2.13) includes a real orientation sign, and its trace formula
has an absolute fixed-point denominator.  That scalar surface formula cannot
simply be relabelled as the desired holomorphic, vector-valued \(\mathbb C^3\)
trace theorem.  Removing the real sign and changing dimension requires a new
oriented residue calculation and a word-kernel proof.

- V. Baladi, E. R. Pujals, M. Sambarino, *Dynamical zeta functions for
  analytic surface diffeomorphisms with dominated splitting*,
  [arXiv:math/0307045](https://arxiv.org/abs/math/0307045) and
  [primary preprint PDF](https://www.imj-prg.fr/preprints/350.pdf).
- H. H. Rugh, *Generalized Fredholm determinants and Selberg zeta functions
  for Axiom A dynamical systems*, Ergodic Theory Dynam. Systems 16 (1996),
  805--819.  [DOI](https://doi.org/10.1017/S0143385700009111)

Rugh's 1996 statement treats Axiom-A surface diffeomorphisms and
three-dimensional flows, not the present three-dimensional discrete lifted
map.  Among the audited primary sources, no theorem was found that can be
quoted verbatim to close G2--G5.

The audited BPS PDF SHA-256 was
`384cd555d8da1eff5eee73b5dcd01e89d97dd9387b988b2417bd60cc3c2da833`;
the audited Ruelle 1990 PDF SHA-256 was
`d4889f8d28be195b59a32ccef5526a685da4d0bde9fc0a372efa8a5be70b499b`.

## Exact convention and one-step Hénon data

The preliminary roadmap attempted to prescribe a stable/projective output
and invert the projective map.  That is the wrong BPS mixed boundary-value
problem and creates a spurious pole at output slope zero.

The corrected one-step gate fixes \((x,m)\) at input and \(z\) at expanding
output, then solves

\[
1-ay^2-x=z,
\qquad
y=P_{a,\sigma}(x,z).
\]

The resulting cross identity, strict disk inclusions, pole exclusion, and
Jacobian estimates are exact.  In particular, the three image ratios

\[
\frac{39}{41},\qquad
\frac{250880}{466211},\qquad
\frac{907}{915}
\]

are all below one, and the full and pinning Jacobian lower bounds are

\[
|\det D\widehat F_a|\ge\frac{50176}{3352561},
\qquad
|\det D_{(x,m)}K|\ge\frac{401408}{204506221}.
\]

These are one-step image and injectivity statements.  The third ratio is a
half-inverse image ratio, not automatically the restriction ratio of an
enlarged output-\(z\) Banach space.

## Exact finite algebra and its limit

With physical tangent basis \((e_x,e_y,e_m)\), scalar variable order
\((x,m,u)\), residual order

\[
(x-K_1,m-K_2,u-h),
\]

and product orientation \(dx\wedge dm\wedge du\), the block calculation gives

\[
\det DR=-\partial_z h\,\det(I-DF).
\]

Thus a simple raw Grothendieck residue with numerator \(\partial_z h\) has
the finite algebraic sign

\[
-\frac1{\det(I-DF)}.
\]

The exterior polynomial identity

\[
\sum_{k=0}^3(-1)^k\operatorname{tr}(\wedge^kM)=\det(I-M)
\]

then fixes the candidate parity shift \(k+1\).

These identities are exact.  They do not prove that the canonical trace of
an all-word operator equals this residue.  That requires a valid iterated
kernel, a nuclear trace theorem on the chosen spaces, and fixed-point coding.

## Open theorem gates

The audited sources and current code leave the following points open:

1. **G2 -- vector word kernels:** construct the iterated block pinning maps
   and prove chronological kernel composition with the correct weight,
   derivative point, fibre basis, and contour signs.
2. **G3 -- functional analysis:** give explicit intermediate/enlarged
   domains, including an enlarged output-\(z\) disk; prove a rank-one
   order-zero nuclear factorization, the metric approximation property, and
   locally uniform holomorphy in a fixed \(p\)-nuclear ideal.
3. **G4 -- trace:** prove that the canonical nuclear trace is the diagonal
   contour residue for periods one, two, repetitions, and general \(n\), with
   one-to-one graph/fixed-point coding.
4. **G5 -- determinants:** only after G2--G4 may one assert jointly entire
   Fredholm factors and a quotient defining a meromorphic germ on
   \(\mathbb C^2\).

The existing symbolic certificate checks rational constants, a generic
block determinant identity, exterior algebra, graph counts, and selected
chronology mutations.  It contains no implementation of the infinite-
dimensional Banach spaces, nuclear decomposition, nuclear trace, or
several-variable Fredholm determinant.  Its regression `pass` status cannot
be cited as proof of G2--G5.

## Novelty verdict

The following remain classical and are not novelty claims:

- pinning/cross coordinates;
- Grothendieck nuclear restrictions once their hypotheses are proved;
- exterior-power Lefschetz cancellation;
- alternating Fredholm products in proved analytic-hyperbolic settings;
- projective and Grassmann lifts as general techniques.

The exact Hénon-specific contribution currently retained is narrower:

- common one-step \(\mathbb C^3\) triangular domains for both chronological
  letters and all state edges;
- explicit rational inclusion, pole, and Jacobian constants;
- a correctly oriented candidate vector kernel with a frozen physical fibre
  basis;
- the block determinant sign and exterior parity as finite algebra;
- reproducible algebraic and mutation regressions.

This is useful analytic infrastructure, but not a completed operator theorem
and not a new Hilbert--Pólya mechanism.  C22G therefore closes as a
conditional blueprint rather than as a proved meromorphic-continuation
result.
