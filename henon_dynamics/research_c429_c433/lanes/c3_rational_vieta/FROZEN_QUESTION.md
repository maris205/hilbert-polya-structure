# C3 frozen rational arithmetic question

2026-09-09 UTC. Initial theorem-first investigation; no mathematical program,
old certification, build, or external-model upload is authorized or run.

## Object and full question

For every $n\ge3$ and $a\in\mathbb Z$, retain the original polynomial
automorphism
$$
F_{n,a}(x_1,\ldots,x_n)
=(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1)
$$
on **all** $\mathbb Q^n$, including zero coordinates and every level of
$$
K=\sum x_i^2-\prod x_i-a\sum x_i.
$$
One application of $F_{n,a}$ is the native time step. Does the rational
periodic set admit a finite affine-linear atlas, independent of the level,
whose pieces carry exact native least periods?

To avoid the trivial bounded-denominator obstruction to replacing
$\mathbb Z$ by $\mathbb Q$ in an integer linear set, allow each proposed
piece to be the rational points of a rational polyhedron, allowing strict
and non-strict rational linear inequalities and equations, followed by a
rational affine map. Parameters are free rational parameters subject only
to those linear conditions. A finite union of such pieces includes finite
affine spaces, rays, segments, and their rational linear cuts. Arbitrary
nonlinear equations or an unspecified elliptic rational-point oracle are
not an affine-linear atlas.

## Success / decisive counterexample boundary

A positive result must exhaust all rational periodic points, with finitely
many pieces for each fixed $(n,a)$, not finitely many denominator strata or
one invariant level. A decisive negative result is one fixed $(n,a)$ for
which one exact least-period stratum is not a finite union of the allowed
pieces. This refutes this full atlas claim, not rational periodic
decidability or all conceivable nonlinear classification methods.

The proposed discriminator is $(n,a)=(5,-1)$ and native period two:
$$
(u,v,u,v,u)\longmapsto(v,u,v,u,v),\qquad
u+v=u^2v^2-1.
$$
The proof will test whether this locus is infinite with unbounded
denominators and contains no affine line. No census is needed.

## Source subtraction and proof dependencies

- C427's actual theorem is an integral semilinear atlas; its nonzero-block
  proof uses $|x|\ge1$ for nonzero integers and integrality of a product
  of absolute value below two. Neither fact is assumed over $\mathbb Q$.
- C427's mixed-zero channels and C421's complete $n=3$ integer table are
  inherited; neither counts as this new rational obstruction.
- The proposed $n=5$ zero-free two-period elliptic locus, its explicit
  denominator growth, and its incompatibility with any finite rational
  affine-linear atlas are the increment to be proved.
- Elliptic group-law identities and rational polynomial/linear algebra
  are classical inputs. Any external source collision will be recorded.
- C424 normalization and C426 all-affine good-model results may only be
  imported after matching their two-dimensional Hénon hypotheses, not
  because the present map is also a polynomial automorphism.

## Initial status

Full positive atlas claim: **NOT CURRENTLY JUSTIFIED**, with the displayed
candidate obstruction under proof. Broader nonlinear rational arithmetic
classification remains separate and is not silently substituted.
