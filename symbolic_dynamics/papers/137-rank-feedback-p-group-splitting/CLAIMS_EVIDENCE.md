# Claims and evidence

External status: `HOLD_EXTERNAL`.  Finite enumeration is never used as the
proof of an all-weight statement.

| ID | Claim | Formal support | Executable support | Status |
|---|---|---|---|---|
| C1 | `F(G)=p^d(G)G direct_sum G[p^d(G)]` preserves order and induces the displayed keep/split rule on partition types. | Proposition 2.1 | 176 literal cyclic factor cells and factorwise equality on all 1,295,970 enumerated types | proved |
| C2 | Recurrent types are exactly fixed types `lambda_1<=ell(lambda)`. | Proposition 3.1 | complete functional graphs through weight 50 | proved |
| C3 | The fixed-type OGF is `1+sum_(r>=1) z^r [2r-1 choose r]_z`. | Ferrers-rectangle proof after Proposition 3.1 | coefficients 0--50 from an independent q-Pascal recurrence | proved |
| C4 | A type of initial rank `r0` and entry time `d` obeys `n>=r0(d+1)+binom(d,2)`; the exact maximum is the displayed triangular clock and `(n)` is its unique maximizer with the stated full orbit. | Lemma 4.1 and Theorem 4.2 | pointwise budget, maximum, deepest-count, unique witness, and explicit orbit for every state/weight through 50 | proved and sharp |
| C5 | The bounded-choice coefficient sum is the fibre over every target, and the marker/high-remainder condition is equivalent to image membership. | Theorem 5.1 | all 81,155 targets through weight 35, including 30,923 zero-fibre targets | proved |

## Zero-credit inputs

- classification of finite abelian `p`-groups by partitions;
- `d(G)=dim_(F_p)(G/pG)` and the minimal-generator interpretation;
- the cyclic types of `p^r C_(p^a)` and `C_(p^a)[p^r]`;
- the multiplication-by-`p^r` kernel/image order identity;
- `p^ell`-torsion language and existing partition-indexed finite-group
  statistics;
- Ferrers diagrams, rectangle partitions, Gaussian polynomials, and the
  q-Pascal recurrence;
- generic finite-map recurrence, monotone potentials, and formal coefficient
  extraction;
- generic partition-dynamics vocabulary.

## Scope sentinels

- The map is on **isomorphism classes of finite abelian `p`-groups**, not on
  arbitrary finite `p`-groups.
- The direct sum in the literal map is external; no internal splitting of
  the multiplication exact sequence is asserted.
- The type dynamics is independent of `p`, but the group carrier and literal
  subgroups still depend on the fixed prime.
- The OGF counts fixed **types**, not labeled groups or group elements.
- `D(n)` is an exact maximum over partitions of weight `n`; the stronger
  pointwise inequality depends on the initial length.
- The fibre theorem is one-step and counts source types, not homomorphisms,
  subgroup embeddings, or labeled decompositions.
- Marker copies and residual copies are counted by multiplicity, so no
  spurious binomial choice among identical target parts is introduced.
- Search-result absence is not novelty, priority, or ownership evidence.
- No posting, submission, authorship decision, owner contact, or external
  release is authorized.

## Internal firewall

- P126: ordered balanced composition refinement, fixed split threshold,
  nearly-halving rule, and all-iterate code geometry.
- P135: derived-centralizer multiplicity rule with mergers and two-cycles.
- P115: linear Cartier/Frobenius coefficient dynamics.

None contains the literal group operator, rank-feedback subtraction,
pointwise marker budget, unique triangular clock, or the present every-target
rank-summed fibre decoder.
