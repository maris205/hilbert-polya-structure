# SD-C22 Obstruction Registry

## O22.1 — clock dilution

**Status:** proved for every nonnegative exact-clock allocation.

If a cycle has length \(\ell(p)\) and total roof \(\log p\), some edge has
roof at most \(\log p/\ell(p)\to0\). Orthogonal source vectors on different
prime cycles have image norms tending to one. Thus the natural whole adjacency
has essential norm one and is noncompact.

## O22.2 — all finite Schatten classes fail

**Status:** proved.

The cycle singular values are the edge magnitudes. For every \(q>0\), Jensen
gives a block lower bound
\(\ell(p)p^{-q\sigma/\ell(p)}\), which does not tend to zero. Hence the
accepted restriction is outside every finite Schatten class, including trace
class and Hilbert--Schmidt.

## O22.3 — essential unit circle

**Status:** proved.

The \(\ell(p)\) block eigenvalues have radius
\(p^{-\sigma/\ell(p)}\to1\) and asymptotically dense phases. Singular Weyl
sequences from disjoint blocks put the unit circle in the essential
approximate spectrum. Consequently \(I-zL_s\) is non-Fredholm for
\(|z|=1\).

## O22.4 — Poincare collapse

**Status:** proved as an operator/ledger equivalence.

The raw graph-step factor is \(1-z^{\ell(p)}p^{-s}\). First return to one
input vertex per cycle yields \(1-zp^{-s}\) and the Paper 04 diagonal
operator. The factors agree at \(z=1\), but ordinary first return erases the
verification clock. This is not a conjugacy of the full phase spaces.

## O22.5 — universal-decider presentation control

**Status:** proved.

Any total decider can be padded without changing its language. Closing its
accepted computations with total roof \(\log n\) reproduces clock dilution
for squares, powers of two, Fibonacci values, hashes, or arbitrary infinite
decidable supports. The obstruction is a state-subdivision/runtime effect,
not a prime-selective dynamical law.

## Open boundary

No theorem here excludes overlapping recurrent grammars, signed or
matrix-valued cancellation, homological supertraces, nonordinary determinants,
or spaces that deliberately remove finite-cycle modes. The universal claim
that every exact recurrent verifier must create extra cycles or collapse to a
diagonal remains open.

## Next smallest obligation

Freeze an overlapping semiring-local recurrent grammar and prove or refute
primitive-cycle separation before adding any roof, character, determinant,
or zero comparison.
