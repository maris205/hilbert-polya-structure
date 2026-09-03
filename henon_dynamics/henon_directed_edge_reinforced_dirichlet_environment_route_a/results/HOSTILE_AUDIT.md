# Hostile audit

The checker rejected all 79 attacks. Repaired-payload attacks cover identity,
date/source, scope, evaluator and YAML binding, departure reinforcement,
vertex-local normalization, mixture and limit contracts, collision and
nonclaim fields, source tokens, Route-A/Route-B values, parallel-arc ownership,
path counts/probabilities, summaries, moments, stationary flows and enumeration
digests. The frozen nonempty-outgoing-row hypothesis is attacked both by
rewriting and deletion, with repaired payload hashes. Every nested row family
is attacked by extra-key, omission and duplication mutations.

Strict parsing rejects duplicate/nonfinite/non-object JSON and duplicate,
anchor, alias, merge, non-string-key, implicit-timestamp, unknown-field,
type-mutated and non-object YAML. Repaired YAML raw/semantic binding attacks
and a stale-hash control are included.
