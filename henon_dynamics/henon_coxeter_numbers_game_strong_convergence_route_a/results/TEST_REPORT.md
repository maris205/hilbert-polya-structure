# Test report

All commands were run from the repository root with bytecode disabled:

```bash
python3 -B henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/code/c286_numbers_game_producer.py
python3 -B henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/code/c286_numbers_game_checker.py
python3 -B henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/code/c286_numbers_game_sympy_crosscheck.py
python3 -B henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/code/c286_numbers_game_replay.py
python3 -B henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/code/c286_numbers_game_mutation.py
```

Observed outputs:

```text
C286_PRODUCER_PASS; 23 cases, 3332 branches, 143 levels, 8 boundaries
C286 independent checker: PASS (19056 assertions; positive-root/inversion/coset reconstruction)
C286_SYMPY_PASS (577 symbolic matrix/root checks)
C286 byte replay: PASS (1296292 bytes; two fresh paths)
C286 hostile mutation audit: PASS 84/84
```

The archived evidence SHA-256 is
`e770246fe3d448e684b2adc50465dc715ff0e4008db3c9616a28719a84588081`.
The producer's canonical payload SHA-256 is
`d3b0b4dc922bd445ee3a71e012dd46b037acd0586b889533a41fe0d57dedd65a`.

The checker does not import the producer.  It reconstructs the positive root
set, all Weyl matrices, inversion length, the full and parabolic longest
elements, the minimal right-coset representatives, the target `w_0w_J`, and
all quotient weak-order path words.  An all-depth duplicate-rejecting JSON
loader, strict scalar types, exact nested/row schemas, complete unique case,
branch, level and boundary grids, all analytic/nonclaim/collision values, the
eight boundary semantics, theorem/model/proof contracts, scope flags and Route
disposition are locked.

The release gate additionally checks source/evaluator/date/epoch/scope locks,
duplicate/merge/alias-safe Route YAML, exact 27-payload/28-physical files,
three pairwise-distinct revision PDFs, two fresh byte-identical builds per
round, embedded/subset fonts, text tokens, warning-free logs, visual audit,
and final-equals-round2.  Collision-registry hashes are retained as immutable
read-only snapshot tokens inside the hashed source audit; release replay does
not depend on the subsequently mutable shared registry bytes.
