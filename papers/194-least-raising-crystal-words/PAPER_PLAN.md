# Paper plan — P194 least-colour raising crystal words

## Frozen title

**Least-Colour Raising Dynamics on Finite Type-A Crystal Words**

Anonymous A4 short paper.  Round 0 is an author-side freeze only; no external
release while ownership remains amber.

## One-sentence residual

After assigning crystal, RSK, tableau, Schur, and hook machinery zero credit,
the paper retains the autonomous least-colour raising scheduler together with
its exact clock and complete labelled inverse atlas, including a sharp stable
fibre threshold.

## Section architecture

1. **Literal scheduler and subtraction boundary.** Freeze the sign,
   cancellation, edited occurrence, and least-colour conventions; give one
   orbit; state zero-credit background and the external hold.
2. **Components, recurrence, and clock.** Identify fixed words with ballot
   words, prove one highest sink per component, derive the pointwise clock,
   and prove the unique global extremizer.
3. **Component and global layers.** Derive the normalized principal Schur
   specialization, shape multiplicity `f^lambda`, global layer polynomial,
   fixed-word sum, and bounded-height involution interpretation.
4. **Every-target inverse atlas.** Prove the scheduler admissibility rule,
   the uniform bound `k`, the exact stability threshold, and the staircase
   witness.
5. **Finite control and claim ceiling.** Describe independent checks, state
   their exact range, and preserve `OWNER_AMBER/HOLD_EXTERNAL`.

## Claims–evidence matrix

| claim | deductive engine | finite falsifier |
|---|---|---|
| fixed iff highest iff ballot | signature prefix criterion | every word in the complete grid |
| unique highest sink in each component | type-A highest-weight decomposition plus strict energy drop | explicit undirected component construction |
| pointwise depth `sum(w)-sum_i i lambda_i` | one-unit letter-sum drop and endpoint baseline | orbit-by-orbit comparison |
| sharp maximum `n(k-1)`, uniquely at `k^n` | upper-bound equality conditions | complete deepest-set comparison |
| one-component depth polynomial | SSYT weight enumerator and principal specialization | independent SSYT enumeration and polynomial product |
| shape multiplicity `f^lambda` | recording-tableau index under reverse RSK | constructed components versus hook count |
| global layer polynomial | sum over components | complete source depth histogram |
| fixed census and involution interpretation | one highest per component and RSK involutions | permutation inversion/shape census through `S_8` |
| every-target predecessor set | crystal-string inverse plus least-colour admissibility | literal versus predicted source sets for every target |
| uniform fibre bound `k` | at most one candidate per colour plus possible self | complete indegrees |
| equality iff `n>=binom(k,2)` | strict padded-weight staircase and explicit witness | direct stable witnesses through `k=9` |

## Figure and table decision

No figure or table is needed in Round 0.  The orbit example, Schur product,
and set-valued inverse formula carry the argument more precisely than a
diagram.  `FIGURE_PLAN.md` records one optional post-owner-gate crystal panel,
but it is deliberately excluded from the current manuscript.

## Citation policy

Use verified sources for crystal bases, type-A word crystals, RSK/tableaux,
Schur/hook identities, and the nearest deterministic crystal-dynamics
subtraction. Defant--Williams crystal pop-stack sorting receives zero credit
and is distinguished at the literal update level. No citation is treated as support
for a P194 scheduler theorem.  No bounded non-hit may be rewritten as a claim
of novelty, priority, completeness, or freedom to operate.

## Acceptance boundary

The Round-0 source is internally complete only after:

- all four signature choices are identical in the paper and verifier;
- the reverse-word RSK convention is explicit;
- `n=1` and `k=1` boundaries are covered;
- the exact fibre theorem compares predecessor sets, including empty fibres,
  rather than indegrees alone;
- stable equality is proved in both directions;
- two verifier processes agree byte for byte with `code/CANONICAL.txt`;
- LaTeX has no unresolved references, unresolved citations, fatal errors, or
  material bad boxes;
- anonymity and `OWNER_AMBER/HOLD_EXTERNAL` survive PDF-text inspection;
- no hostile or process-separated review is represented as part of Round 0.
