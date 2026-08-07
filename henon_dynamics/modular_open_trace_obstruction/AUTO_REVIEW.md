# HCS-C18 adversarial review record

**Review date:** 2026-08-07

**Review type:** two independent internal, read-only adversarial reviews

**Initial verdict:** major revision; no critical mathematical error

**Post-revision disposition:** all critical/major scope findings addressed

## Claims independently recomputed

Both reviewers confirmed:

- the open coefficient formula and its residues at \(s=1\) and \(s=1/2\);
- the sign of the primitive/affine projective-section cocycle;
- the failure of representative multiplication on
  \(P\backslash\mathrm{PSL}_2(\mathbb Z)/P\);
- the rational-parabolic versus quadratic-hyperbolic fixed-point
  classification and the signs \(\pm\ell(g)\);
- the single global factor
  \(\Lambda(2s-1)/\Lambda(2s)\) in the squarefree scattering tensor formula;
- the Walsh eigenchannels and determinant exponents;
- fixed-basis commutativity;
- the projector trace identity
  \(\operatorname{tr}(P_aAP_bBP_cC)=A_{ab}B_{bc}C_{ca}\).

No critical error requiring withdrawal of the mathematical spine was found.

## Major finding 1: cohomology category

The primitive rational section proves a coboundary only after topology is
forgotten.  The primitive section and denominator transfer function are
discontinuous and unbounded in the topology inherited from
\(\mathbb P^1(\mathbb R)\).  The initial wording could be read as a
continuous/Hölder/Livšic statement or as a bounded transfer-operator
conjugacy.

**Resolution:** the theorem is now explicitly an
algebraic/set-theoretic groupoid-coboundary theorem.  The paper states that no
analytic conjugacy or Fredholm-determinant invariance follows.  The only
trace-level consequence used is zero rational-loop period.

## Major finding 2: period support is not a determinant

The full-boundary theorem classifies automorphy periods.  It does not supply
coding multiplicities, fixed-point Jacobians, branch orientation, parabolic
acceleration, or nuclearity, so it cannot alone prove that an arbitrary trace
or determinant equals Selberg zeta.

**Resolution:** all strong “full trace is Selberg” wording was replaced by a
period-support statement.  Established Selberg transfer operators are cited
as consistent context, not deduced from the elementary theorem.

## Major finding 3: spectral parameter is not time

The fixed Walsh basis proves

\[
\Phi_N(s_i)\Phi_N(s_j)=\Phi_N(s_j)\Phi_N(s_i),
\]

but scattering theory does not make \(s_i,s_j\) successive time events.
Calling the product “actual chronology” over-promoted a conditional modeling
test.

**Resolution:** the result is now named permutation invariance of frozen
spectral-parameter products.  It rules out order recovery only for a proposal
that chooses bare \(\Phi_N(s_j)\) factors as steps.

## Major finding 4: projector witness scope

The finite level-six tests show:

1. sensitivity to reassigning spectral parameters to fixed edges;
2. sensitivity to changing the endpoint path.

They do not establish a source-derived legal reordering of the same dynamical
events.

**Resolution:** all machine fields and prose now say
parameter-to-edge assignment sensitivity and path sensitivity.  The artifacts
also store intrinsic_chronology_claimed as false.

## Major finding 5: Route-A objects were mixed

The initial Route-A table combined rational endpoints, full real boundary,
bare scattering products, and projected paths.  It also used matrix
commutativity as an A2 determinant failure, although commutativity does not
forbid a determinant.

**Resolution:** the paper and YAML now evaluate the four objects separately.
The full boundary passes A1 only in the classical hyperbolic sense; its
determinant is not tested.  The bare and projected branches lack a
source-derived primitive law and Fredholm kernel.  Commutativity is retained
only as the conditional product-order diagnosis.

## Major finding 6: trace-power cancellation

Channelwise noncancellation cannot be promoted to traces of powers, since a
finite sum of nonzero channel factors may vanish.  An explicit warning
example is \(N=7\), \(k=2\): if \(7^s=i(3-\sqrt2)\), then for
\(M_7=aI+bX\) one has \(b=ia\) and
\(\operatorname{tr}M_7(s)^2=2(a^2+b^2)=0\).

**Resolution:** the divisor theorem is asserted channel by channel and for
the determinant, not for traces of powers.

## Major finding 7: normalization and preregistration

The fixed Walsh basis depends on one common Huxley--Hejhal
width/Atkin--Lehner cusp normalization.  An arbitrary \(s\)-dependent cusp
renormalization need not preserve it.  The initial computation also executed
only one of the two preregistered off-line points.

**Resolution:** the theorem now freezes scaling matrices, divisor ordering,
and tensor-bit identification.  A second off-line point,
\(s=0.83+1.7i\), was added to both producer and independent checker, so all
three physical-line and two off-line points are present.

## Additional corrections

- The title no longer calls an already commutative family an
  “abelianization.”
- The geometric cutoff is stated as sufficiently large \(T_0>1\);
  \(T_0=1\) in code is labelled an analytic normalization.
- \(\Lambda(w)\) is defined on first use.
- The proof treats \(x=\infty\) explicitly.
- Level six is described as the smallest squarefree level with two independent
  cusp bits and three nontrivial flip types, not the smallest informative
  projected test.
- Appendix artifact names now match the release.
- External theorem novelty is rated low; synthesis value is rated moderate.

## Final review ruling

The corrected package is suitable as a scoped negative
compatibility/reproducibility paper.  It is not a positive Hilbert--Pólya
candidate, a new scattering formula, a general analytic groupoid-coboundary
theorem, or a projector-path determinant.
