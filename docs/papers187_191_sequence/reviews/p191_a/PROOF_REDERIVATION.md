# P191 Review-A proof rederivation

## Reviewer route

The reviewer rederived the manuscript through cut masks rather than part
tuples.

1. A state is a subset of `[N-1]`, encoded as a bit mask of internal cuts.
2. The literal update deletes a cut at prefix `s` unless the incoming gap from
   the previous retained cut divides `s`.
3. Because the image mask is always a subset of the source mask, the functional
   graph is attacked by indegree peeling and reverse breadth-first search
   rather than by forward orbit tracing.
4. A target fibre is reconstructed in two different ways:
   a. a global path dynamic program forbidding jumps across mandatory target
   cuts; and
   b. an interval product whose local automata count deleted intermediate
   vertices and a retained or untested closing step.

## Reopened claims

- Fixed states are exactly the masks whose every retained cut satisfies the
  divisibility predicate.
- The recurrence for fixed counts depends only on the last cut.
- The first cut, when present, is invariant, giving the universal tail bound.
- Equality in the bound forces one part of size two and one leading unit,
  hence the unique deepest source `(1,2,1^(N-3))`.
- Target fibres are path counts; image membership is equivalent to positivity
  of those path counts.

## Boundary handling

- `N=1,2,3` were reopened explicitly and all carriers are fixed.
- One-part targets are represented by the empty cut mask and use only the
  final interval factor.
- The final endpoint `N` is never tested, so the last step in a source path
  is unconstrained by divisibility.

No reviewer step imports the author verifier or relies on its internal carrier
representation.
