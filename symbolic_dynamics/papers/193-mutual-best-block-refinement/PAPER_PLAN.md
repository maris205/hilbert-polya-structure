# Paper plan — P193 mutual-best block refinement

## Frozen title

**Mutual-Best Block Refinement on Permutations: Recursive Clocks, Depth
Layers, and Exact Fibres**

Anonymous A4 short paper; no external release while ownership is amber.

## Section architecture

1. **Literal map and subtraction boundary.** Define the two-sided nomination
   rule before any matching interpretation.  Define direct-sum cuts and give
   one example.  Assign matching and direct-sum basics zero credit.
2. **Block surgery and exact clock.** Prove active pairs are precisely
   first--minimum pairs in indecomposable blocks.  Establish strict component
   refinement, unique absorption, the pointwise recursive height, maximum
   `n-1`, and `(n-1)!` deepest states.
3. **All transient layers.** Derive `A_t=1/(1-B_t)` and
   `B_(t+1)=x+x^2 A_t B_t'`, then identify exact layers by coefficient
   difference.
4. **Complete one-step inverse atlas.** Prove the last-component parent lemma,
   group target components, derive the every-target product, image support,
   mass, and the unique `2^(n-1)` fibre maximum.
5. **Exact controls, internal separation, limitations.** State verifier scope,
   selected exact boxes, and explicit differences from P105, P122, P155,
   P156, and especially P181.  Preserve `OWNER_AMBER/HOLD_EXTERNAL`.

## Claims–evidence matrix

| claim | deductive engine | finite falsifier |
|---|---|---|
| literal nominations equal block surgery | forbidden internal sum cut | active-pair equality for every source through `S_9` |
| unique absorber and no cycles | strict increase of component count | complete orbit checks |
| pointwise tail equals recursive height | direct-sum independence plus size recursion | source-by-source equality |
| max tail `n-1`; deepest count `(n-1)!` | induction and last-component parent lemma | full depth histograms |
| all depth layers | sequence construction plus marked last component | all `A_t/B_t` coefficients in the box |
| image iff first entry is `1` | compatible grouping of target components | every target |
| complete fibre product | optional-boundary factorization | every labelled indegree |
| unique maximum fibre `2^(n-1)` | component-size exponent budget | full maximizing set |
| fibre mass `n!` | fibres partition `S_n` | summed predicted and literal indegrees |

## Figure and table decision

No figure is needed.  The two recursions and the inverse grouping are clearer
as formulas and proof text.  One compact table reports selected exhaustive
boxes; it is labelled author-side control rather than experimental evidence.

## Citation policy

Use only standard background citations for permutations/direct sums and
stable matching.  No citation supports a P193 theorem.  Round 0 performs no
external novelty or direct-owner search, and the prose must not turn a local
noncollision into novelty, priority, or clearance.

## Acceptance boundary

The source is ready for internal review only after:

- all theorem statements include `n=1` boundaries;
- the parent lemma is proved before being used for deepest-state counting or
  clearly forward-referenced;
- the verifier passes twice with identical stdout and digest;
- LaTeX compiles without unresolved references, citations, fatal errors, or
  material bad boxes;
- anonymity and `HOLD_EXTERNAL` survive PDF-text inspection.
