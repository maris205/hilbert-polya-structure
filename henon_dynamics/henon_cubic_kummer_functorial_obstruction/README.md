# HCS-C38: cubic Kummer functorial obstruction

Status: `PROVED_SCOPED_OBSTRUCTION`.

This project tests the first nonscalar escape selected by C37.  The
homogeneous H\'enon chirp is placed in three \(\mathbf Z/3\)-graded Kummer
channels and every tensor, exterior, dual, and super construction obtained
functorially from those channels is audited.

## Main result

If a group \(G\) acts on \(X\), \(\phi:X\to A\), and

\[
c(g,x)=\phi(gx)\phi(x)^{-1},
\]

then every finite-dimensional representation \(\rho:A\to\mathrm{GL}(V)\)
produces another coboundary

\[
\rho(c(g,x))=\rho(\phi(gx))\rho(\phi(x))^{-1}.
\]

The same identity survives finite tensor operations, exterior powers,
duals, parity shifts, and virtual supertraces.  Consequently the direct
three-channel lift

\[
\operatorname{diag}(1,c,c^2)
\]

has identity holonomy on every closed scaling orbit and every repetition.
Changing representation category without adding nonfunctorial monodromy
does not escape the C37 gauge obstruction.

## Evidence and boundary

- `PROVED`: the functorial coboundary theorem and closed-holonomy identity.
- `NUMERICALLY_CERTIFIED`: two exact finite cyclic models check all cocycle,
  gauge, determinant, and repetition identities.
- `REFUTED`: the direct \(\mathbf Z/3\)-graded Kummer lift as a source of new
  prime weights.
- `OPEN`: a genuinely nonfunctorial channel permutation or central extension
  not induced from the scalar chirp.

## Route evaluation

\[
(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL},A4_{\rm NATURAL}).
\]

Overall: `ROUTE_A_REJECTED_FOR_FUNCTORIAL_KUMMER_LIFTS`.  Route B is not
authorized because no nontrivial determinant or complete operator is
produced.

## Research extraction

- **Strongest positive result:** functorial gauge triviality is stable under
  all finite graded representation operations.
- **Strongest obstruction:** every closed prime-loop holonomy remains the
  identity matrix, not merely determinant one.
- **Open theorem:** classify nonfunctorial monomial channel cocycles over the
  scaling-site prime loops.
- **Reusable structure:** the representation-stable coboundary lemma and its
  type-strict finite certificate.
- **ROUND2_CLUE:** central extensions can survive only through channel
  permutation/projective data not expressible as \(F(gx)F(x)^{-1}\).

## Reproduce

```bash
python -B code/c38_kummer_checker.py
python -B -m unittest code/test_c38.py
```

The compiled paper is [`paper/paper.pdf`](paper/paper.pdf).
