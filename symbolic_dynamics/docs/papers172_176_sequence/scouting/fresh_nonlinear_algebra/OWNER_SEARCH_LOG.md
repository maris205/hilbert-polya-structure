# Primary-source owner search log

**Search date:** 2026-09-03 (UTC).  
**Scope:** the two theorem-strength candidates M01 and V02 only.  
**Status rule:** a search miss is recorded only as a bounded non-hit; it is
not evidence of novelty, priority, or freedom to operate.

## Queries

The search used exact formulas and semantic variants, including:

```text
"[diag(A),A]" matrix
"diagonal-feedback commutator" matrix
matrix self-map [diag(A), A] finite field commutator dynamics
matrix commutator diagonal part proper coloring fibre finite field
"support graph" commutator matrix coloring
commutator map finite field fibres matrices
cyclic map triple vectors pairwise dot products finite field dynamics
triples vectors pairwise dot product 1 finite field counting
"cyclic Gram gate"
```

Internal repository searches additionally used the literal formulas and the
terms `Gram`, `quadratic-state`, `bilinear`, `commutator`, `fixed
commutator`, `Potts`, `chromatic`, `support graph`, and `every-target fibre`
across P1--P171.

## M01: diagonal-feedback additive commutator

### Located primary owner regions

1. Hsu-Wen Vincent Young,
   [*On matrix pairs with diagonal commutators*](https://doi.org/10.1016/j.jalgebra.2020.11.023),
   *Journal of Algebra* 570 (2021), 437--451.  This studies algebraic sets of
   arbitrary pairs whose commutator is diagonal, and also the variety where
   a pair commutator has zero diagonal.  It owns the algebraic-commutator
   variety region, not the finite self-map (A\mapsto[D(A),A]), its image,
   or its fibres.
2. Zhibek Kadyrsizova and Madi Yerlanov,
   [*Algebraic sets defined by the commutator matrix*](https://arxiv.org/abs/2006.13514),
   *Journal of Algebra* 589 (2022), 29--50,
   [journal DOI](https://doi.org/10.1016/j.jalgebra.2021.09.012).  The paper
   studies vanishing diagonal/anti-diagonal equations, complete
   intersections, and positive-characteristic singularity properties for
   arbitrary matrix pairs.  Again, no state-derived diagonal feedback or
   finite functional graph is stated.
3. R. Brandl,
   [*The commutator map*](https://doi.org/10.1017/CBO9780511600647.011), in
   *Groups--St Andrews 1985*, and Robert W. Baddeley,
   [*Images of commutator maps*](https://doi.org/10.1080/00927879408825010),
   *Communications in Algebra* 22 (1994), 3023--3035, own the fixed-element
   **group** commutator programme.  Baddeley's map is
   (g\mapsto g^{-1}\alpha^{-1}g\alpha).  This is relevant vocabulary and
   image prior art, but it is neither an additive matrix bracket nor a
   feedback map.
4. Jason Fulman,
   [*Fixed points of non-uniform permutations and representation theory of
   the symmetric group*](https://arxiv.org/abs/2406.12139) (2024), studies
   fixed points of random commutators, including one fixed permutation.  Its
   statistic and symmetric-group carrier do not supply M01's deterministic
   graph, but all broad “fixed commutator distribution” language is already
   occupied.
5. Michael Larsen and Michael Lu,
   [*Flatness of the commutator map over (SL_n)*](https://arxiv.org/abs/1807.07300),
   *IMRN* 2021, studies fibres of the two-input multiplicative commutator
   morphism.  Generic claims about commutator fibres receive zero credit.
6. Alan D. Sokal,
   [*The multivariate Tutte polynomial (alias Potts model) for graphs and
   matroids*](https://arxiv.org/abs/math/0503607), owns the generic
   Potts/Tutte/chromatic partition-function framework.  Proper-colouring
   sums, occupation refinements, and evaluations of such sums are classical
   input, not an M01 contribution by themselves.

### Exact subtraction

M01 may not claim any of the following as new: zero diagonal of a diagonal
commutator, arbitrary commutator varieties or word-map fibres, generic
fixed-commutator image questions, proper-colouring solvability, or a
Potts/chromatic partition function.

The only residual under review is their literal conjunction:

\[
A\longmapsto[D(A),A],
\]

whose first image is classified by (q)-colourability of the target support
and whose individual fibres are the support-only occupation-weighted sum
proved in `M01_THEOREM_PACKAGE.md`.  Exact-formula searches located no source
stating this self-map, the support criterion, or the weighted every-target
fibre identity.

**Owner verdict:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.  This is a bounded
non-hit with substantial neighboring ownership, not a novelty finding.  A
source giving the same self-map or an equivalent polynomial-map fibre
identity is an immediate kill switch.

## V02: cyclic Gram gate

### Located primary owner regions

1. David Covert and Steven Senger,
   [*Pairs of dot products in finite fields and rings*](https://arxiv.org/abs/1508.02691),
   studies triple counts subject to two prescribed dot products.  It owns a
   central counting problem behind the V02 recurrent core and inverse
   constraints, though its results concern subsets and estimates rather than
   the literal full-space dynamics.
2. David Blevins et al.,
   [*On the number of dot product chains in finite fields and
   rings*](https://arxiv.org/abs/2101.03277), studies chains of prescribed dot
   products.  This is another direct static counting region for V02's Gram
   constraints, not a statement of the cyclic state update.
3. Doowon Koh and Youngjin Pi,
   [*Size of dot product sets determined by pairs of subsets of vector spaces
   over finite fields*](https://arxiv.org/abs/1401.6992), owns broader finite
   dot-product set machinery.  V02's elementary whole-space hyperplane
   counts receive no novelty credit.

Exact and semantic searches found no primary source stating (or obviously
conjugating to) the literal update

\[
(u,v,w)\mapsto((u\cdot v)w,(v\cdot w)u,(w\cdot u)v)
\]

or its functional graph.  That non-hit cannot overcome the internal
collision: P125 already occupies the formed-space state-gate quotient,
hyperplane inverse, shallow functional graph, and zeta architecture, while
the killed `NL03` scout already occupies the three-shared-input bilinear
constraint census.

**Owner verdict:** external `NO_LITERAL_HIT_IN_BOUNDED_SEARCH`, but final
portfolio verdict **`KILL_INTERNAL_P125_NL03`**.  No novelty language is
authorized.

## Final owner-sensitive recommendation

Only M01 remains recommendable, and only for internal hostile development.
V02 is mathematically correct but removed before allocation.  No result in
this lane is cleared for posting, specialist contact, priority claims, or
submission.

