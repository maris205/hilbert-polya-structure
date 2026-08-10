# Exact C25 code

`c25_producer.py` rebuilds the literal seven-state labeled Rauzy graph and
emits two exact source-locked certificates:

- the all-length fixed-start matrix decoder, with the complete 128-step
  row-dominance and row-subtraction trace for `gamma_star`;
- the AGY section witness at state 4 with
  `eta=tbttbtbb` and `gamma_star=t^64 eta^8`.

The producer preserves the elementary chronology
`B_word=B_last*...*B_first`.  It verifies eight-completeness, the AGY
`3d-4=8` strong-positivity gate, neatness/no proper border, determinant,
entrywise positivity, intersection-form transport, exact projective witness
points, and `J_gamma=exp(-4 r_gamma)`.  The maximal initial constant run is
computed from the released word and is 65, because `eta` begins with `t`.

`c25_independent_check.py` does not import the producer.  It independently
reconstructs every graph edge, matrix, decoder step, rational point, and
three-coordinate projective Jacobian.  It separately rebuilds the
deterministic state-4 spanning-tree frames, checks
`S_pi^T J_pi S_pi=J0`, and reconstructs all fourteen fixed-fiber matrices
`g_e=S_dst^(-1) B_e S_src`.  It also independently replays the length-22
first-return stress window.  That finite replay is a mutation sentinel, not
the proof of injectivity.

`test_c25.py` rejects reversed chronology, edge transposition, confusion of
`B` with `B^T`, move-word-only state loss, a Jacobian exponent of three,
bordered section words, and promotion of the toy `ttt` branch to the AGY
section.  It rejects a reversed frame direction and a source/target-swapped
edge trivialization, and checks the full-rank `H(2)` qualification on the
projected matrix conclusion.

Run the complete release from the project directory with:

```bash
./code/run_c25.sh
```

No length-13 periodic ledger, averaged transition matrix, prime/zero table,
oscillator truncation, heat kernel, or fitted branch is used.
