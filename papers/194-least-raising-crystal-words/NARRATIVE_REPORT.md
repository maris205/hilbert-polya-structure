# Narrative report — P194 least-colour raising crystal words

## Status and scope

`PASS_INTERNAL / OWNER_AMBER / HOLD_EXTERNAL`

The carrier is the full labelled word set `[k]^n`.  At each epoch the map
recomputes all type-A raising operators and applies exactly one: the operator
`e_i` with the least available colour.  If none exists, it holds.  The map is
neither random nor asynchronous, and the scheduler is part of the literal
definition.

## Problem anchor

The crystal graph already supplies partial inverses, connected components,
and unique highest vertices.  Those facts do not determine a finite
functional graph: a deterministic rule must choose one outgoing raising edge
whenever several colours are available.  P194 fixes the least-colour rule and
asks four complete questions.

1. Where does every word terminate, and after exactly how many steps?
2. How many labelled words occur in each transient layer, both inside one
   component and globally?
3. Which words are recurrent, and how are they counted?
4. For an arbitrary labelled target, what is the complete predecessor set?

## Literal convention

For colour `i`, ignore all letters except `i` and `i+1`, encode them as `+`
and `-`, and cancel `+-` pairs.  The raising operator changes the rightmost
unpaired `i+1` to `i`; the lowering operator changes the leftmost unpaired
`i` to `i+1`.  These choices are deliberately repeated in the manuscript,
verifier, and canonical output.  Under this convention the convenient RSK
shape is the insertion shape of the reversed word.

## Main deductive spine

### Unique component sink and exact clock

Every nontrivial move changes one letter `i+1` to `i`; the letter sum drops
by exactly one.  Crystal edges preserve the component, so an orbit cannot
cycle and must stop at its component's unique highest word.  If the component
shape is `lambda`, its highest word has content `lambda` and letter sum
`sum_i i lambda_i`.  Therefore the exact tail is the starting letter sum
minus this baseline.

The global bound follows from `sum(w) <= nk` and the baseline at least `n`.
Equality forces every source letter to be `k`, so the unique deepest state is
`k^n`, with depth `n(k-1)`.

### Complete depth layers

Reverse-word RSK identifies a component of shape `lambda` with the
semistandard tableaux of that shape over `[k]`; its recording tableau is
fixed.  Weight above the highest tableau's row baseline is exactly orbit
depth.  Hence one component has normalized principal specialization

```text
q^(-sum_i i lambda_i) s_lambda(q,q^2,...,q^k)
 = product over cells x of (1-q^(k+ct(x)))/(1-q^(h(x))).
```

There are `f^lambda` recording tableaux and thus that many components.
Summing the component polynomial with these multiplicities gives every global
depth layer.

### Fixed and involution census

Highest words are exactly ballot/Yamanouchi words.  There is one per
component, so their number is `sum f^lambda` over shapes with at most `k`
rows.  RSK identifies the same sum with involutions of bounded shape height.
For `k >= n`, this is the telephone number with exponential generating
function `exp(z+z^2/2)`.

### Every-target inverse atlas

If a nonfixed source reaches `y` using colour `i`, partial invertibility
forces the source to be `f_i(y)`.  That candidate is genuine exactly when all
lower-colour raisings `e_j`, `j<i`, are absent at `f_i(y)`.  A highest target
also contributes itself; a nonhighest target does not.  This gives an actual
set identity, not only an indegree formula.

There are at most `k-1` lowering candidates and at most one self-source, so
every fibre has size at most `k`.  Equality requires a highest target with a
strict drop at every adjacent pair of its padded weight.  Such a partition
has size at least `binom(k,2)`.  The staircase word

```text
1^(k-1+s) 2^(k-2) ... (k-1),  s=n-binom(k,2),
```

meets the threshold and admits every lowering candidate.

## What is and is not residual

The following are completely subtracted:

- finite type-A crystals and Kashiwara operators;
- tensor signatures, highest-weight components, and ballot words;
- RSK, tableaux, Schur functions, principal specialization, hook content,
  hook length, and the involution correspondence;
- generic descent-by-a-Lyapunov-function reasoning;
- the abstract idea of choosing the least or leftmost available local move.
- Defant--Williams crystal pop-stack sorting, including its noninvertible
  orbit-to-highest and sharp maximum-orbit surface.

The retained conjunction is the literal least-colour scheduler, its exact
word-level clock, and especially the target-resolved admissibility atlas with
the sharp stable fibre bound.  The classical layer formulas support the
dynamical accounting but carry no independent contribution claim.

The closest located deterministic crystal map is not the same update. Its
macrostep takes the unique source of a component restricted to all descent
colours of the starting vertex; P194 takes one least-colour raising edge and
recomputes after every edge. Its orbit theorem does not supply P194's depth
layers or targetwise inverse atlas. This separation earns no novelty credit.

## Evidence discipline

The paper-local verifier exhausts 25,384 words, checks 25,384 target fibres,
builds every crystal component in the grid, and independently enumerates
semistandard tableaux.  It also checks the hook formula by a separate
corner-removal recurrence, verifies involution shape counts through `S_8`,
and tests staircase fibres without ambient enumeration through `k=9`.

These controls test implementation and theorem boundaries only.  They are
not proofs, process-separated review, or novelty evidence.

## Open boundary

No all-time predecessor formula beyond one step is claimed.  No closed scalar
formula replacing the Schur sum is claimed.  No asymptotic limit law is
claimed.  Most importantly, the bounded owner search has not cleared the
least-colour crystal scheduler against all specialist literature.  A literal
owner or an equivalence transferring both the schedule and inverse atlas
would require withdrawal or repositioning.  External circulation remains on
hold.
