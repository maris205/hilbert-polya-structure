# Research question

For the pairwise-coprime Brieskorn links

\[
\Sigma(2,p,q)=\{z_0^2+z_1^p+z_2^q=0\}\cap S^5,
\qquad 3\le p<q,
\]

with (p,q) odd, can the standard weighted contact form be normalized so that
the entire Reeb return geometry is explicit: all primitive orbit types, every
fixed-time component, the Morse--Bott kernels, transverse rotations and first
degeneracies, nondegenerate Conley--Zehnder indices, the Seifert quotient, and
the principal Robbin--Salamon index?

The answer proved in this package is yes. The integer weights give a weak
Route-A arithmetic relation, but the two-dimensional principal orbit quotient
prevents a discrete primitive ledger. No target arithmetic or spectral claim
is made.

## Frozen assumptions

- (p,q) are odd, coprime integers with (3\le p<q).
- The sphere has radius one and the contact form includes the factor (1/(4\pi)).
- Exceptional-orbit Conley--Zehnder indices use the ambient missing-coordinate
  complex-line trivialization.
- The principal Robbin--Salamon index uses the standard Milnor-fiber capping
  trivialization from the Brieskorn index formula.
- Finite evidence stops at (q\le101); proofs do not.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
