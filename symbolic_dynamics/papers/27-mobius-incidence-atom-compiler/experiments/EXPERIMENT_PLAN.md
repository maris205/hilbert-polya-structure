# Exact Experiment Plan — SD-C29

## Frozen question

Starting only from the fixed positive-integer divisibility relation, determine
whether incidence Möbius inversion can compile covers of \(1\) into exact
necklace-resolved atom idempotents without a supplied prime/color projector
table, and whether the resulting oblique family has cyclic determinants beyond
those of coordinate atom projectors.

## Exact blocks

| Block | Independent variable | Exact observable | Decisive condition |
|---|---|---|---|
| I | cutoffs 6, 12, 18, 30 | \(Z\mu\), \(\mu Z\) | both equal identity |
| Q | labels 1–30; all pairs | rank, trace, \(q_nq_m\), entry formula | complete primitive system |
| C | labels 1–256 | covers of \(1\) | agrees with separated trial evaluator |
| N | four atoms; lengths 1–6 | cyclic word trace | only monochromatic atom classes survive |
| M | ten atoms; repetitions 1–8 | gamma digit exponent | equals \(r\ell(p)\) |
| F | \(s=2,u=1/2,z=1/3\) | power traces and finite determinant | exact atom sum/product |
| D | source cutoff 10; degree 3 | chain maps and two determinants | graded ratio equals atom product |
| H | \(\eta=3/5,3/4,1,5/4\) | rank-one trace norm | exact formula and uniform bound |
| S | \(\eta=5/4,3/2,2\) | zeta/Möbius operator bounds | bounded global similarity certificate |
| X | mutated source, relabeling, cutoff | source equivariance | stable but PROVES_TOO_MUCH |
| A | scalar Möbius, zeta-only, unfiltered | falsification witnesses | each proposed shortcut fails |

All claim-bearing finite arithmetic is exact. Displayed \(H_\eta\) values are
nongating high-precision evaluations of a proved formula. No stochastic
training split, seed statistic, or target-root metric applies.

## Route freeze

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_PASS_ANALYTIC,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

The exact source-derived orbit ledger earns A1. The finite and \(\eta>1\)
similarity theorem prevents ordinary incidence traces from earning A3 or A4.
