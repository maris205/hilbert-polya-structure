# Paper 22 research-question brief

Date: **2026-08-24**
Status: **PHASE-2 REVISED — EXACT-SITE `N=2` OBSTRUCTION GATE**

## Primary question

On a universe-small version, in Deninger's sense, of the absolute site
`NoethAffSch_fppf`, with no additional relative base, consider the
source-defined sheaf epimorphism

```text
omega: underline Z(O)^sharp -> W_rat(O)^sharp,
```

What is the necessary-and-sufficient obstruction to lifting the additive
big-Witt endomorphism `V_N` naturally through `omega`?  The first nontrivial
test is `N=2`; only after that case is decided may the question be enlarged
to a family of indices and to Frobenius/Verschiebung relations.

The fppf site is the primary branch.  Here the source abbreviation `fp`
means **finite-flat**; that branch is a later comparator and must not be
blended into the first theorem.

## Subquestions

1. Bind the exact base, site, sheaves, morphism `omega`, and source convention
   before defining any lift.
2. Compute `K=ker(omega)` and the extension
   `e:0->K->underline Z(O)^sharp->W_rat(O)^sharp->0` in the abelian category
   of fppf sheaves.
3. For a candidate induced map `u:K->K`, decide the exact criterion
   `u_*e=V_N^*e` in `Ext^1(W_rat(O)^sharp,K)` and classify the lift torsor.
4. Decide this obstruction for `N=2`; `N=1` is a control only.
5. In the positive branch, prove naturality, additivity, independence of local
   choices, and every claimed `F/V` identity; in the negative branch, give a
   concrete obstruction witness.

## FINER screen

| Criterion | Score / 5 | Reason |
|---|---:|---|
| Feasible | 3 | the source poses an exact problem, but the kernel/descent calculation is not yet known |
| Interesting | 4 | it isolates a concrete missing Witt-operation lift |
| Novel | 5 | the repository's maximum-prior audit found no existing answer for this exact sheaf epimorphism |
| Ethical | 5 | pure mathematics with a clear positive/negative outcome |
| Relevant | 4 | it is an owner-ready algebraic successor, though not a Route bridge |

Mean score: **4.2/5**.

## Owner and nonclaims

- Proof is blocked until the exact source site and notation are bound.
- A generic quotient-sheaf lifting lemma is not the desired arithmetic
  computation.
- No rational-Witt packet realization, groupoid, dynamics, trace, operator,
  determinant, or Route implication is claimed.
- No fp conclusion follows automatically from an fppf theorem.

## Decisions

- **Promote:** exact obstruction group/criterion plus a decided nontrivial
  `N`-family.
- **Narrow:** one fixed `N` is acceptable if it reveals a reusable arithmetic
  mechanism.
- **Stop:** the source-defined owner remains ambiguous, or only an abstract
  noncomputed obstruction can be stated.
