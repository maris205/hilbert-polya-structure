# Independent internal review: Frobenius--Hénon equalizers

Reviewer: coordinating current-team agent, independent of the scout author.
Date: 2026-09-05. This is an AI-assisted internal mathematical review, not
external or human peer review. No favorable author label is taken as evidence.

## Reviewed inputs

All 456 lines of the contract/proof/source handoff and the complete bounded
producer were read. The saved results were inspected for scope; the producer
was not rerun because this review tests the projective proof independently
of its finite Gröbner checks.

| Input, relative to the continuation directory | SHA256 |
|---|---|
| `henon_arithmetic/CONTRACT_SCOUT.md` | `a891beca49be4b1cc2a460a4320596097a22c13a39056e20727db5058b982378` |
| `henon_arithmetic/bounded_check.py` | `330440c3883aeaabb53944c9e3e2101ecdccdc92dfb3d775fdbf8811121668cf` |
| `henon_arithmetic/bounded_results.json` | `9d821a7b787ad0fdbf8fca5b25a5724d7f3d46d792888e17256600136653e79b` |

## Verdict

No blocking mathematical gap found in the theorem for D=d^n != Q=q^r.
The proof justifies distinct geometric point counts, not just scheme lengths,
and the non-p-power degree assumption genuinely supplies all pairs of clocks.
The nonresonant, all-coefficient exact small-twist law is substantial enough
to proceed as ONE paper-level source-arithmetic contract after the classical
ownership subtraction below. No formal Route A grade or novelty guarantee
is conferred by this admission recommendation.

## Load-bearing checks

1. The coordinate degree induction is valid in every characteristic: the
   degrees of f(g_2) and a g_1 differ strictly. The leading homogeneous part
   stays a pure power and cannot cancel. The inverse has the matching
   regularity at the opposite infinity point.
2. The graph's two projections are birational, while its mixed line degree
   is D. Pairing its class with the Frobenius graph class gives
   1+DQ+Q^2, with the two end coefficients in the correct order.
3. An affine solution has invertible Jacobian D(H^n), determinant a^n.
   Over the algebraic closure the finite-type affine intersection is
   zero-dimensional, finite and reduced. This does not presuppose its count.
4. On the Frobenius graph, both coordinates are simultaneously finite or
   infinite. The contraction at infinity and Frobenius's unique geometric
   preimages leave exactly the two displayed boundary points.
5. At I_-, the graph is smooth and the denominator C is a unit. Nonresonance
   makes the second equation a unit times v^min(D,Q). The proof that v is a
   non-zero-divisor modulo B is correct: reduction modulo v forces the other
   factor to be divisible by v, and cancellation takes place in k[[u,v]].
   The filtration therefore has precisely min(D,Q) quotients of length Q.
6. At I_+, the inverse-graph chart is regular. The equation
   Y=Phi_r(g^{-1}(Y)) has identity linear term and gives length one by the
   formal local inverse/Nakayama argument. No unjustified separability of
   Frobenius is used.
7. These local calculations also establish properness of the projective
   intersection. At the intersection points both graphs are smooth, so the
   local complete-intersection lengths are the actual intersection numbers.
   Subtraction gives max(DQ,Q^2) with no uncounted boundary component.
8. The threshold uses positive integer r and is floor(log_q D)+1. There is
   no equality ambiguity when d is not a p-power. The slice and genuine
   diagonal iterate have different clocks and are correctly distinguished.
9. The finite polynomial exponential is transcendental when D>q. The
   finite-dimensional weighted-trace exclusion is independently valid via
   Cayley--Hamilton with nonzero constant coefficient and backward
   propagation of a zero tail; A_i need not commute with F_i.
10. Commutation of H and q-Frobenius follows from the coefficient field.
    Thus (H^{-k}Phi_s)^m=H^{-km}Phi_{sm}; the resulting count is Lambda^m
    and its rational dynamical zeta is correctly derived. It is not the
    fixed-n Frobenius slice or a target Euler factor.

The resonant cubic control was reconstructed directly by hand from the map:
y=x^3 leaves x^6-x=0 in characteristic three, derivative -1, hence six
distinct points. It refutes extending the theorem to D=Q without additional
conditions. This is independent reasoning, not a rerun of the saved producer.

## Closest-source and repository ownership

The reviewer accessed [Shuddhodan's author v2 HTML](https://arxiv.org/html/1803.06461),
read the relevant section 2 definitions/propositions and Example 3.6 plus
the concluding threshold-growth paragraph. Twisted étaleness, eventual
trace agreement, the torus defect example, and the nonuniform-threshold
motivation are prior-owned. They are explicitly excluded from novelty here.
The accessed source does not calculate the two Hénon local lengths or this
all-coefficient small-twist max-law. The claim is limited to that scoped
increment, not a new general trace principle.

The reviewer independently opened the Stacks Project's Gysin/lci framework.
A fresh browser attempt to retrieve Varshavsky's author HTML failed; the
scout's stated access is not recast as a successful independent retrieval.
The proof does not depend on a Varshavsky theorem to obtain the exact count.
Fresh Hénon/Frobenius/equalizer queries produced mostly Perron--Frobenius
noise, not a directly owning primary theorem; this is not exhaustive novelty
clearance.

The reviewer read the actual
[C12A entry](../../henon_frobenius_scheme_obstruction/README.md).
Its fixed finite-period scheme and joint finite-action character are not
the growing equalizer H^n=Phi_r. The distinction in the proposed contract is
necessary and preserved. A fixed-period scheme's rationality is not reused
as the new theorem.

## Minor clarifications for the manuscript

- **A-M1:** call Q^2 the degree of the finite Frobenius morphism, or its
  generic scheme degree, rather than “topological degree” without explanation.
  Frobenius is a homeomorphism on geometric underlying spaces; the Chow
  coefficient uses scheme degree, not the number of geometric points in a fiber.
- **A-M2:** the accessed v2 HTML shows the threshold-growth discussion in the
  paragraph following Example 3.6; it does not display a separate Remark 3.7
  heading. Use that unambiguous locator unless an original numbered version
  is checked. This does not change source ownership or the theorem.

Neither issue requires rerunning mathematical checks. Apply the wording in
the manuscript and record the affected-input check. The original reviewed
handoff is preserved as the input snapshot.

## Claims permitted and withheld

Permitted: a proved source-side nonresonant exact equalizer law, its sharp
boundary defect/threshold, and the stated slice-versus-iteration consequences.
Proceed to a complete manuscript and normal batch gates as one contract.

Withheld: resonance classification, ordinary Hénon periodic zeta, a universal
new trace theorem, global priority, target Euler factors/root number,
automorphy, target zero correspondence, A2/A3 or a Hilbert--Polya operator.
No compile, paper review, formal evaluation, release seal or remote
synchronization was performed by this proof review.
