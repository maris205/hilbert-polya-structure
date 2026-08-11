# HCS-C30 results

## 1. Exact input identities

The two frozen C25 words and the derived C26 word are raw source-matrix
identities.  For closed C25 paths, source frames telescope between the raw
Rauzy matrices and the fixed-frame symplectic matrices.  The C29 fixed-frame
certificate is SHA-locked, and C30 independently replays the raw products.
The C26 relation is also replayed directly in the source \(A,B,C\) alphabet.

This proves identity **holonomy**.  It does not make the reduced formal word a
unit arrow in the path groupoid.

## 2. Complete cyclic-phase cone census

The exact result is

| Word | Genuine forward length \(B^{-\mathsf T}\) | Contravariant transfer \(B^{\mathsf T}\) |
|---|---:|---:|
| C1 | 6/6 infeasible | 6/6 infeasible |
| C2 | 6/6 infeasible | 6/6 infeasible |
| C26 \(W_{24}\) | 24/24 infeasible | 24/24 infeasible |

Every phase ends at \(I_4\), so failure is not caused by a broken relation.
Every phase has a canonical integer certificate: either one required prefix
row is nonpositive and nonzero, or a positive integer combination of required
rows is zero.

Representative forward-length certificates are

\[
(0,-1,0,1)+(0,1,0,-1)=0
\]

for C1,

\[
(-1,0,0,0)
\]

for C2, and

\[
(-11430,-460520,-3353,-456200)
\]

for C26.  The representative C26 transfer row is

\[
(-984333,-498163,-999116,-479060).
\]

No positive vector can satisfy the corresponding strict inequalities.

## 3. Raw homology convention control

The distinct covariant recurrence \(H_k=B(t_k)H_{k-1}\) has positive integer
witnesses

\[
(1,2,1,1)\quad\text{for C1},
\qquad
(1,1,3,1)\quad\text{for C2}.
\]

Thus the implementation can distinguish a covariant homology zigzag from the
AGY length action.  These witnesses are not positive length or transfer
orbits.  The C26 raw covariant control is infeasible.

## 4. Roof theorem

Every real additive groupoid cocycle satisfies

\[
\tau(g^{-1})=-\tau(g).
\]

Therefore genuine inverse arrows cannot both carry positive elapsed time.
The projective logarithmic normalizer additionally telescopes to zero on a
matrix-identity return wherever all prefixes are defined.  This statement is
not extended to every edge cocycle: C1 and C2 are kernel words, not unit paths.

A symmetric assignment \(L(e)=L(e^{-1})>0\) defines a valid new graph
suspension.  It is not the AGY roof.  This exactly classifies the C29 unit-edge
determinant rather than invalidating it.

## 5. Operator and flat-trace theorem

On one infinite-dimensional fibre, bounded faithful edge inverses cannot be
blocks of a compact or nuclear finite Hashimoto operator.  Coordinate
compression would make every edge block compact/nuclear, and composition with
its bounded inverse would make the identity compact/nuclear.

For a standard geometric fixed-point trace, each C29 witness meets an exact
dichotomy:

- its source positive branch domain is empty; or
- after domain enlargement, the full map is the identity, its fixed set is a
  continuum, \(Dh_W=I\), and \(\det(I-Dh_W)=0\).

The theorem rules out the ordinary nuclear and standard isolated-hyperbolic
flat-trace promotion.  It does not rule out every clean-fixed-set or
distributional regularization.

## 6. Surviving finite determinant

C29's finite edge operator over the group von Neumann algebra still defines

\[
D_\infty(u)
=\exp\!\left[-\sum_{n\ge1}\frac{N_nu^n}{n}\right].
\]

This is a valid nonconstant finite group-trace germ for a symmetric graph
suspension.  It is not an ordinary Hilbert-space Fredholm determinant and not
the natural extension of AGY.

## 7. Route-A outcome

```text
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION
```

Route B is not authorized.  The negative result closes the formal inverse
lane and redirects the program to a genuinely hyperbolic positive-time base.
