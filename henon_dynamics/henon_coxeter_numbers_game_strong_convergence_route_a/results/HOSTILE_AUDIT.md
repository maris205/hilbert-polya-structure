# Hostile audit

The mutation suite recomputes the canonical payload hash after every semantic,
schema, type, and drop-replace attack, so a checker that validates only JSON
integrity cannot pass.  It also injects raw duplicate keys whose last value
would be accepted by ordinary `json.loads`, and includes one stale-hash attack
to prove the integrity gate is active.  All 84/84 mutations were rejected.

Attack families include:

- candidate, source, evaluator, date, epoch and scope locks;
- theorem headline, root-system scope, coordinate update, legal move and word
  convention;
- every analytic proof obligation, every nonclaim, and every closest-collision
  distinction, including the formerly escaping second nonclaim;
- terminal, cumulative-element, parabolic-length, strict, zero and product
  theorem contracts;
- proof mechanism/status and the finite-evidence role;
- all Route-A axes, overall verdict, Route-B flag, and forbidden scope flags;
- exact case name-to-components/initial-coordinate mapping;
- Cartan transpose and entries, rank, initial position, zero set, strict/zero/
  disconnected flags, terminal, length, branch count and branch digest;
- exact branch case/index/sequence/length/terminal fields and branch ordering;
- exact level case/depth/prefix/state/edge/terminal fields and level ordering;
- every boundary face and complete semantic sentence;
- unknown and missing nested/row fields, strict bool/integer/list/string type
  substitutions, duplicate-replaced grids, and row-family-reordered content;
- raw duplicate top-level, nested, and row keys;
- stale canonical payload hash.

The independent checker rejects duplicate JSON keys before object construction
and duplicate rows before comparison, then locks exact top-level, nested and
row key sets, strict scalar types, and complete unique grids.  The release carrier uses a
custom safe YAML loader that rejects duplicate keys, merge keys, anchors and
aliases, then validates exact top-level, source-lock, A0--A4 and metric key
sets.  Hostile Route-carrier controls must reject a duplicate top-level field,
a duplicate cutoff, a duplicate axis verdict, a tuple/verdict mismatch, and an
anchor injection.

No mutation success was waived.  Affine/indefinite inputs are not simulated as
supporting evidence: they are rejected by the declared finite-type scope.
