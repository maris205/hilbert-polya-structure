# Exact Experiment Plan — SD-C28

## Frozen question

For each finite color alphabet, audit the cyclic coefficient that is one on
every nonempty monochromatic word and zero on every mixed word. Determine
whether finite recognizable or finite graded trace memory can realize it
without semisimplifying to one supplied color sector per label.

## Exact blocks

| Block | Independent variable | Exact observable | Decisive condition |
|---|---|---|---|
| P | colors 1–7; word length 1–5 | projector word trace | equals selector word by word |
| R | colors 1–6; word length 1–5 | triangular-extension trace | radical changes no trace |
| G | colors 1–5; word length 1–4 | even-minus-odd trace | common sector cancels |
| H | colors 1–8 | Hankel rank | rank is m or m+1 by empty convention |
| A | four scalar pencils; powers 1–8 | aggregate supertrace | aggregate passes but oriented words fail |
| S | support size 1–12 | exterior superdimension | one only at singleton support |
| B | color algebra size 1–12 | idempotent/separability checks | HH0 survivor is m color lines |
| D | degrees 2–5; powers 1–6 | de Rham chain, traces, determinant | analytic tensor preserves selector |
| C | seven inventories; three cutoffs | exact l1 sums/products | identical compiler proves too much |
| M | labels 2–512 | digit/return marker | selector preserves but does not derive marker |

All arithmetic is exact. No training/validation split, stochastic seed
statistics, or target-root metrics apply. The aggregate adversary is a
falsification control, not a failed implementation.

## Route freeze

The required tuple is

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`.

Overall verdict is `ROUTE_A_REJECTED`; Route B and target-zero data remain
forbidden.
