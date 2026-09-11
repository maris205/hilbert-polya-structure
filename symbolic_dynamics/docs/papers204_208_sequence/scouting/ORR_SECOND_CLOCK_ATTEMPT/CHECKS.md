# Actual documentary checks

2026-09-07 UTC. These are original-file integrity checks, not mathematical
producer runs, pilot replays, byte-identical scientific comparisons or an
independent proof review. No code was added or executed for mathematics.

The seven operative original hashes were first obtained by an explicit
sha256sum command listing exactly the seven paths in INPUTS.sha256. The
list was then written without changing any original, and the following
command was actually run from /root/autodl-tmp/symbolic_dynamics:

```text
sha256sum -c docs/papers204_208_sequence/scouting/ORR_SECOND_CLOCK_ATTEMPT/INPUTS.sha256
```

Observed exit: 0. Complete returned output:

```text
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/INTAKE.md: OK
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/PRECODE_PROOFS.md: OK
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/ORR_FIBRE_PROOF.md: OK
docs/papers204_208_sequence/scouting/ORR_ROOT_CLOCK_BOUNDARY.md: OK
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/SOURCE_AND_HISTORY.md: OK
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/public_sources/flip_sort.pdf: OK
docs/papers204_208_sequence/scouting/finite_systems_twenty_second/public_sources/flip_sort.txt: OK
```

The main agent then reread the entire new PROOF_PACKAGE.md and checked its
literal, odd/even boundary cases, colour definition, lower-bound induction,
cross-parity inversion gain, colour-sorting comparison, capacity inequality
and preserved counterexample. This is author self-checking, not independent
acceptance. The final nonself outer manifest is checked separately after
it is written; its actual result and digest accompany the handoff. This
file does not claim a future command has already passed.
