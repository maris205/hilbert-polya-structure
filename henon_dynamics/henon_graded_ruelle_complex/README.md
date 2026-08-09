# HCS-C22G: conditional graded Hénon Ruelle blueprint

## Audited outcome

This directory is a **conditional analytic blueprint and closure note**, not
a completed nuclear-operator theorem.

For the two chronological Hénon letters

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad a\in\{59/10,61/10\},
\]

the projective lift has an explicit three-complex-dimensional cross-map
candidate on common disks.  The following pieces are exact:

- the correct BPS mixed-data convention: fix contracting input
  \((x,m)\) and expanding output \(z\), then solve the expanding input;
- the rational disk clearances, projective pole exclusion, and one-step
  pinning Jacobian bounds;
- the block determinant identity giving a raw residue minus sign when the
  product contour is oriented as \(dx\wedge dm\wedge du\);
- the exterior identity and the resulting candidate parity \(k+1\).

The previous stronger wording has been withdrawn.  The present files do not
prove:

- the all-word vector-kernel composition and nuclear trace formula;
- an enlarged output-\(z\) domain and explicit order-zero nuclear
  factorization;
- the metric approximation property for every mixed space used;
- locally uniform holomorphy in a fixed nuclear ideal;
- jointly entire Fredholm factors or a joint meromorphic continuation of
  the instability determinant.

## Frozen kernel conventions

Scalar function arguments are ordered as

\[
(x,m,u),
\]

while tangent fibres use the physical basis

\[
(e_x,e_y,e_m).
\]

Thus \(D\widehat F_a(x,u,m)\) is always the physical derivative.  Anyone
using the cross-ordered fibre basis \((e_x,e_m,e_y)\) must conjugate it by
the corresponding permutation matrix.

The candidate branch kernel uses

\[
g_{a,\sigma,s}(u,m)\,\wedge^kD\widehat F_a(x,u,m)
\]

at the source integration variable.  The \(u\)-residue then evaluates this
factor at \(u=P_{a,\sigma}(x,z)\).  The product-contour differential order is

\[
\frac{dx}{2\pi i}\frac{dm}{2\pi i}\frac{du}{2\pi i};
\]

changing it can change the raw residue sign.

Every graph block remains the sum of its two parameter-letter kernels, never
an averaged transition, and later matrices act on the left.

## Conditional consequence

If the open iterated-pinning, word-kernel, nuclear-trace, enlarged-domain,
order-zero, approximation-property, and parameter-holomorphy gates are all
proved, then the candidate trace would satisfy

\[
\operatorname{tr}\mathcal L_{s,k}^n
=-
\sum_x
\frac{g_s^{(n)}(x)
\operatorname{tr}(\wedge^kD\widetilde{\mathcal F}^n_x)}
{\det(I-D\widetilde{\mathcal F}^n_x)},
\]

and the corrected parity would give

\[
D_{\rm inst}(z,s)
\stackrel{\rm conditional}{=}
\frac{D_1(z,s)D_3(z,s)}{D_0(z,s)D_2(z,s)}.
\]

Only under those hypotheses would the right side define a meromorphic germ
on \(\mathbb C^2\).  No unconditional joint-entire or joint-meromorphic
claim is made in this release.

## Research decision

The exact domains, constants, pinning correction, fibre convention, and
residue algebra are useful infrastructure.  The missing gates are genuine
functional analysis, not details that can be certified by symbolic mutation
tests.  Even if they are later closed, the mechanism is classical
Ruelle--Rugh/Grothendieck--Lefschetz machinery and supplies no arithmetic
primitive law, Riemann divisor, functional equation, or self-adjoint
Hilbert--Pólya operator.

HCS-C22G is therefore retained as a corrected closure blueprint, not
promoted as a positive operator paper.

## Files

- [`THEOREM_PACKAGE.md`](THEOREM_PACKAGE.md) separates proved algebraic and
  domain statements from the open theorem gates.
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) records the primary-source boundary;
  its historical theorem-language should be read subject to this README and
  the downgraded theorem package.
- [`CLOSURE_AND_PIVOT.md`](CLOSURE_AND_PIVOT.md) records the research pivot;
  it is not an independent proof of the open analytic gates.
- [`paper/`](paper/) contains the matching conditional technical note.
- [`code/`](code/) checks exact constants, finite-dimensional identities,
  graph metadata, and mutations.  It does not prove nuclearity or all-word
  kernel composition.
- [`results/`](results/) contains legacy algebraic certificates and test
  reports.  Their `pass` fields must not be interpreted as certification of
  the open functional-analytic gates.

## Reproduce the algebraic checks

```bash
python -m pip install -r requirements.txt
./code/run_c22g.sh
```

These commands reproduce the exact arithmetic and symbolic regressions only.
They do not upgrade the conditional blueprint to a theorem.

After the audited PDF and release manifest are rebuilt, verify the frozen
artifacts with:

```bash
sha256sum -c results/ARTIFACT_HASHES.sha256
```
