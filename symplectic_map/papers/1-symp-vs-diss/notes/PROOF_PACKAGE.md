# Proof Package

## Claim

Let \(f\colon N\to N\) be a \(C^1\) map of a one-dimensional manifold. Let
\(M\) be a two-dimensional manifold, \(\pi\colon M\to N\) a \(C^1\)
submersion, and \(F\colon M\to M\) a \(C^1\) local diffeomorphism satisfying
\(\pi\circ F=f\circ\pi\). Then no point in the image of \(\pi\) is a critical
point of \(f\). In particular, the critical quadratic map
\(f_a(q)=1-aq^2\) cannot be a smooth submersion factor of a planar
symplectomorphism on any domain containing a point over \(q=0\).

## Status

PROVABLE AS STATED

## Assumptions and notation

- A submersion has surjective derivative at every point.
- A local diffeomorphism has invertible derivative at every point.
- A symplectomorphism is a local diffeomorphism.

## Proof strategy

Differentiate the semiconjugacy identity and compare ranks at a critical point.

## Dependency map

1. The chain rule differentiates \(\pi\circ F=f\circ\pi\).
2. Composition of a surjective linear map with an invertible linear map is
   surjective.
3. At a critical point of a one-dimensional map, \(Df\) is the zero linear map.

## Proof

Fix \(z\in M\), and write \(q=\pi(z)\). Differentiating the semiconjugacy
identity at \(z\) gives

\[
D\pi_{F(z)}\circ DF_z = Df_q\circ D\pi_z.
\]

Because \(F\) is a local diffeomorphism, \(DF_z\) is invertible. Because
\(\pi\) is a submersion, \(D\pi_{F(z)}\) is surjective. Therefore the
left-hand side is a surjective map from \(T_zM\) to \(T_{f(q)}N\), and has
rank one.

Suppose that \(q\) is a critical point of \(f\). Since \(N\) is
one-dimensional, \(Df_q=0\). The right-hand side is then the zero map and has
rank zero. This contradicts the equality above. Hence no point in the image of
\(\pi\) can be critical for \(f\).

For \(f_a(q)=1-aq^2\), \(Df_a(0)=0\). If the domain contains any point
\(z\) with \(\pi(z)=0\), the preceding contradiction applies. A planar
symplectomorphism is a local diffeomorphism, so it cannot furnish the stated
smooth submersion factor. \(\square\)

## Embedded-copy corollary

There is a second, independent obstruction if “lift” means an exact invariant
embedded copy.  Suppose (i:N\to M) is injective, (F:M\to M) is injective,
and

\[
F\circ i=i\circ f.
\]

If (f(q_1)=f(q_2)), then
(F(i(q_1))=F(i(q_2))).  Injectivity of (F) and then of (i) implies
(q_1=q_2).  Hence (f) must itself be injective.  The non-injective
quadratic map cannot occur as such an invariant embedded subsystem of a
global symplectomorphism.  This corollary is topological and does not use the
critical derivative; it likewise does not rule out an inverse-limit or
branch-labeled natural extension.

## Corrections and scope

- The claim concerns a smooth submersion factor. It does not exclude a singular
  projection, an inverse-limit model, a branch extension, or an almost-everywhere
  factor avoiding the critical fiber.
- In coordinates with \(F(q,p)=(f(q),P(q,p))\), the same obstruction follows
  from \(1=\det DF=f'(q)P_p(q,p)\).
- The statement is an elementary obstruction and is consistent with prior work
  whose canonical noisy-map extensions become singular on \(f'=0\).

## Open risks

The theorem alone is not a sufficient novelty claim. The research contribution
must come from its consequences for the frozen arithmetic-lift hypothesis and
from the controlled orbit-survival experiment.
