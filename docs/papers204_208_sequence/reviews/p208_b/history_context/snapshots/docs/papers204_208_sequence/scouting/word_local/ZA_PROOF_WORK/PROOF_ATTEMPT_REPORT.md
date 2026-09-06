# ZA proof attempt — PROOF_HOLD / NO_ADMISSION

Date: 2026-09-05 UTC. Assigned mathematical author subtask, not an independent
paper review. Only this subdirectory was written during this assignment.
The root pilot and P134 proof notes were read; none of the root's update or
verification code was imported. The local `zstep` uses exhaustive substring
equality, and the separate `zscan` uses first-mismatch comparisons. They agree
on all 3,279 ternary words through length seven.

## Outcome

No all-parameter proof of eventual two-periodicity, one phase endpoint per
zero mask, or a uniform useful transient clock was obtained. These remain
conjectures despite the strengthened exact image evidence. Three proposed
proof routes were falsified, including both strict and weak prefix contraction
on **valid** Z arrays. The candidate is not admitted or assigned a paper ID.

The proved pieces in `PARTIAL_THEOREMS.md` are closure, zero-mask complementation,
an invariant-sector census and recurrent lower bound, equality of the one-step
image with all realizable Z arrays, and the exact factorial fibre extremum.
The last axis duplicates P134's generic forced/forbidden-letter argument and
does not rescue the absent temporal theorem.

## Exact obstruction to P134-style prefix amplification

All indices below are zero-based and `G=Z²`.

1. Strict prefix improvement fails at length 10 even on valid arrays:

```text
x  = 0010010100
y  = 0010030100
Gx = 0010030100
Gy = 0010050100
```

The zero masks agree and inputs agree before coordinate 5, but outputs still
disagree there. These are members of the complete valid-array enumeration.

2. Even prefix nonexpansion fails at length 12:

```text
x  = 002004020010
y  = 002004020020
Gx = 001007010020
Gy = 001003010020
```

Inputs agree through coordinate 9; outputs already disagree at coordinate 5.
Actual source words satisfying the stated carrier bounds are respectively

```text
020210202201
010120101101
```

Their Z arrays are exactly `x,y`. The independent deterministic search found
a length-16 witness, then shortened it by paired deletions to this length-12
witness. This is deletion-minimal for the executed greedy process, **not** a
claim of globally minimal length. The complete valid-array tests through
length 11 found no such weak counterexample; this was an instructive false
signal, now explicitly superseded.

3. Same-mask lexicographic antitonicity of `Z` already fails at length seven:

```text
x  = 0020010 < 0020020 = y
Zx = 0102101 < 0104101 = Zy
```

Thus an order-reversing-map shortcut to two-periodicity is unavailable.

The exact realizers, outputs, seed and reduction history are retained in
`NONEXPANSION_COUNTEREXAMPLE.json`. The strict-prefix and lexicographic
examples are in `COMPLETE_VALID_PROBE.json` and `ORDER_PROBE.json`.
These counterexamples refute the proposed lemmas, not the two-cycle conjecture.

## Exact finite scope

`probe_complete_valid.py` enumerates all restricted-growth words through
length 11. Every equality pattern has one such representative; Z depends
only on equality. The recoding proof in `PARTIAL_THEOREMS.md` therefore makes
this a **complete valid-Z-array** enumeration, not an arbitrary-alphabet
sample. At length 11 it uses 678,570 equality patterns and obtains 3,701
different valid arrays. Every tested valid array eventually reaches a
two-cycle, and every zero mask has one phase endpoint. Valid-image maximum
tails at lengths 2 through 11 are

```text
0,0,1,1,2,2,2,2,3,3.
```

This is not an enumeration of all `11!` carrier states. Together with the
proved one-step image characterization it determines ambient maximum tails
at lengths 10 and 11 to be four: a deepest valid point has a carrier parent
and its depth increases by one, while every carrier point enters the valid
image in one step. This deduction is finite-size, not an all-size clock.

`probe_prefix.py` separately enumerates every carrier through length eight
and preserves the earlier ambient and valid-prefix counterexamples.
`probe_triangular.py` tested the weaker nonexpansion/scalar-monotonicity route
on every valid array through length 11; zero failures there cannot be cited
as a general lemma after the length-12 counterexample.

`probe_order.py` also compares 16,000 seeded mutated source pairs at sizes
16,32,64,128. Only 3,871 pairs give distinct Z images; nonexpansion failures
number `3,3,7,10` by size. They were used to find a counterexample, not to
infer a theorem from random coverage.

### Vacuous comparison explicitly excluded

`probe_valid_coupling.py` examines binary-source images through length 15.
Because zero masks flip and a binary word is determined by its zero mask,
that collection has **exactly one image per mask**. Hence its zero
same-mask coupling-failure count is vacuous and gives no coupling evidence.
Its orbit-height data remain valid; they are labelled binary-source-only.
This diagnostic is preserved rather than silently discarded.

## Files and replay

Each `.json` is actual stdout from the matching local program:

| Program | Canonical stdout | Purpose |
|---|---|---|
| `probe_prefix.py` | `PREFIX_PROBE.json` | Full small ambient/valid prefix tests |
| `probe_valid_coupling.py` | `VALID_COUPLING_PROBE.json` | Binary orbit data; coupling comparison vacuous |
| `probe_complete_valid.py` | `COMPLETE_VALID_PROBE.json` | Complete valid-image recurrence and strict-prefix pressure |
| `probe_triangular.py` | `TRIANGULAR_PROBE.json` | Weaker route, subsequently falsified at length 12 |
| `probe_order.py` | `ORDER_PROBE.json` | Lex-order failure and directed nonexpansion pressure |
| `nonexpansion_counterexample.py` | `NONEXPANSION_COUNTEREXAMPLE.json` | Exact bounded realizers and witness minimization |
| `verify_partial_claims.py` | `PARTIAL_CLAIMS_CANONICAL.json` | Checks only the proved partial theorems |

Run any program from the repository root with `python` and this directory's
relative path; no external dependency, GPU or network is needed for replay.
One initial run of `probe_valid_coupling.py` had an extra closing parenthesis
in its witness dictionary and exited with `SyntaxError` before testing data;
that typing error was corrected before the recorded successful stdout.
No failed mathematical assertion was erased or described as successful.

## P134 and literature boundary

P134 recomputes Morris–Pratt border arrays on inversion sequences. It has
`n−1` recurrent two-cycles and a proved canonical-prefix mismatch automaton.
ZA's observed `2^(n−2)` cycles, invariant complementary-mask sectors, and
failed prefix lemmas are materially different facts; **no literal conjugacy
to P134 is asserted**. But equality-pattern recoding, valid-array image
recognition, and the two factorial-maximizing targets are the same generic
static proof axis and are zero credit here. A newly discovered temporal
proof would still require an independent value/collision gate.

The primary static owner is Julien Clément, Maxime Crochemore and Giuseppina
Rindone, [*Reverse Engineering Prefix Tables*, STACS 2009, 289–300](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2009.1825).
Its Definition 2.1 is the same suffix-start LCP statistic away from coordinate
zero; it uses table value `n` at zero, whereas the present feedback fixes
zero there. The paper proves table validation and realizing-word construction.
Those are background, not ownership evidence for iterating this `Z_0=0` map.
The official metadata and primary PDF were opened. Searches for `Z-array
iterating`, `Z-function two-cycle`, and literal recurrence phrases found no
exact iteration source in this bounded pass; non-hit is not novelty.

**Handoff:** retain `PROOF_HOLD / NO_ADMISSION`. A future attempt must supply
a different invariant or coupling proof that survives the above examples.
Increasing the cutoff or quoting the factorial extremum does not close this
task's missing theorem. No public release, external upload, independent
review certification, central-state edit or Git operation occurred.
