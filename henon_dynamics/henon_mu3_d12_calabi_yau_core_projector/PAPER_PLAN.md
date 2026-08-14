# HCS-C52 paper plan

Status: **amber narrative locked; release manuscript compiled**

## Working title

**A Dihedral Chow Projector and the Extreme Hodge Gate for the Hénon
\(\mu_3\) Fivefold**

## One-sentence contribution

The exact projective monomial source symmetries of the fourth Hénon moment
cut its middle cohomology into a rank-10 summand that becomes
Calabi--Yau-threefold Hodge type after one Tate twist and a rank-158
complement that becomes level one after the C51 twist by two, while the
same graph algebra provably cannot isolate the desired rank-two extreme
pair.

## Main theorem architecture

The released main theorem has four clauses and no Frobenius or incidence
upgrade:

1. \(G_{\mathrm{mon}}\cong\operatorname{Dih}(C_{12})\), of order \(24\).
2. The explicit middle Reynolds correspondences
   \(\pi_{\mathrm{core}}\) and \(\pi_{\mathrm{lev}}\) are mutually
   orthogonal \(K\)-rational Chow projectors.
3. Their middle Hodge ledgers are \((1,4,4,1)\) and \((0,79,79,0)\),
   hence their ranks are \(10\) and \(158\).
4. No idempotent in \(\mathbf Q[G_{\mathrm{mon}}]\) refines the first
   projector to the rank-two extreme pair.

Clause 4 is explicitly scoped to the graph algebra.  Full projected
Frobenius polynomials, local irreducibility, and non-graph correspondences
are C53 material.

## Proposed section map

1. **Introduction and C51 gate.**  Explain why a Hodge split is not yet an
   algebraic projector and state the graph-algebra question.
2. **The source fivefold.**  Lock \(K,C,Q,X\), smoothness, degree, Hodge
   normalization, and the closing edge.
3. **Projective monomial stabilizer.**  Derive the 24 maps, multiplication
   table, generators, and dihedral presentation.
4. **Middle Chow--Künneth decomposition.**  Remove ambient Tate classes and
   prove graph/Reynolds idempotence in the Chow category.
5. **Equivariant Cayley ring.**  Define the bigraded Jacobian quotient and
   derive the residue-twisted character.
6. **Rank-10 core and rank-158 complement.**  Compute the Hodge ledgers
   and explain the Calabi--Yau-type terminology.
7. **Optimality of the graph algebra.**  Prove the augmentation lemma and
   the scoped rank-two no-go.
8. **Route-A interpretation and C53 handoff.**  Record the structural gain
   without claiming a new analytic continuation or functional equation.
9. **Limitations, reproducibility, and declarations.**  State all category,
   coefficient, automorphism, and novelty boundaries.
10. **Appendix.**  Exact group table summaries, character table convention,
    and independent-replay details.

## Claim-to-evidence map

| Claim | Required evidence | Forbidden substitute |
|---|---|---|
| order-24 dihedral source group | complete exact enumeration and group table | order histogram alone |
| middle Chow projectors | correspondence identities modulo rational equivalence | action on one cohomology theory |
| character multiplicities | exact \(\mathbf Q(\rho)\) Cayley-ring computation plus independent checker | modular reconnaissance alone |
| rank \(10+158\) | Hodge character plus middle projector | Reynolds average on total cohomology |
| graph-algebra no-go | augmentation lemma for arbitrary group-algebra element | testing central idempotents only |
| same-projector realizations | one \(K\)-rational Chow idempotent acts in each realization; no computed strict compatible system | prime-dependent projectors |

## Required wording firewalls

- “Projective monomial source stabilizer” is not “full automorphism group.”
- “Calabi--Yau-type Hodge summand” is not “Calabi--Yau threefold.”
- “No graph-algebra rank-two projector” is not “no algebraic projector.”
- A Hodge decomposition alone is not an algebraic decomposition.
- Cohomological idempotence alone is not Chow idempotence.
- C52 proves no automorphy, global continuation, functional equation, RH,
  or Hilbert--Pólya operator.
- B3/B4 evidence must not be back-projected into the C52 theorem.

## Prior-work and citation audit

SOURCE_AUDIT.md records verified primary locators for the Cayley-ring
Hodge formula, ordinary versus multiplicative Chow--Künneth projectors,
graph-character projectors and their extra hypotheses, monodromy and
Hodge-locus barriers, and recent symmetry/motivic neighbors.  The
novelty statement is intentionally a targeted-search report rather than
an absolute priority assertion.

## Tables and figures

No decorative figure is required.  Three compact tables should suffice:

1. group conjugacy classes and element orders;
2. Cayley character values and irreducible multiplicities;
3. core/complement Hodge ledgers before and after the C51 Tate twist.

## Release decision

The release paper records the independently certified B0--B2 theorem.  Its
narrative remains
**AMBER_DIHEDRAL_CHOW_DECOMPOSITION_AND_GRAPH_ALGEBRA_OPTIMUM**.
A green rank-two or red local-Frobenius theorem, if obtained later, belongs
to HCS-C53 rather than being appended to this manuscript.
