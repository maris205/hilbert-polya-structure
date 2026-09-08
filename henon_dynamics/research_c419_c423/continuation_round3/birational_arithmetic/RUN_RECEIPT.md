# Author-run receipt

Completed 2026-09-07, before 11:07 UTC. Python 3.12.3, standard library
only. All writable source/report/output paths are under the present
`continuation_round3/birational_arithmetic/` directory.

## Executed mathematical diagnostics

Working directory: `/root/autodl-tmp/hilbert-polya-structure`.

1. `python henon_dynamics/research_c419_c423/continuation_round3/birational_arithmetic/exact_probe.py`
   exited 0. Its parameter domain had been frozen as $1\le c\le512$.
   Exactly 6,980 potential states, 407 retained edges and 8 native fixed
   cycles were found. No nonfixed cycle was found in that sample.
2. `python henon_dynamics/research_c419_c423/continuation_round3/birational_arithmetic/b2_exact_probe.py`
   exited 0. Its parameter domain had been frozen as the 272 pairs
   $-8\le a,b\le8$, $b\ne0$, with the proved complete periodic-height
   bound. Exactly 229,520 potential states, 34,997 retained edges,
   71 fixed cycles and 16 native two-cycles were found. Six nonfixed
   cycles avoid the proposed unit-denominator section.

Both scripts use exact integer divisibility and complete graph-cycle
extraction, with no iterate/period cutoff. Cyclic words are identified
only up to starting phase, not time reversal. Ordinary domain exclusions
are enforced before edges are created, and every output cycle is checked
against the original recurrence. Each diagnostic was run exactly once;
neither parameter sample was expanded. These are author checks, not
independent verification of the extraction implementation.

The three-cycle family in `SCOUT_REPORT.md` was hand-derived and proved
there by three explicit polynomial identities. No additional parameter
scan generated it. B3 received no mathematical CPU. No old IR1 or other
accepted artifact was rerun.

## Executed-file/output digests

| File | SHA-256 |
|---|---|
| `exact_probe.py` | `f51373a9c41f833b98beb7c88cc6a53b372379159bcef4b5511853faaccf0a15` |
| `B1_EXACT_PROBE_OUTPUT.json` | `5a0f97775f353fcc167a574e1dcce208a721a1b7b09f60e7fe428f285eff5bc9` |
| `b2_exact_probe.py` | `9dcea18cdf2b4bae671f6c4cccdb245a05aaddd0e9fa6831bbda885c90c9e0ec` |
| `B2_EXACT_PROBE_OUTPUT.json` | `82491d73d0f6a3437fe726ea79ec20df2f4ad1da9b99c2628dbeaca54040d8be` |

## Claims and status

The B1 all-parameter fixed-only guess is unproved. The B2 all-parameter
at-most-three hypothesis is unproved. The B2 height bound and displayed
three-cycle family have written elementary proofs, but neither is the
complete frozen question. B3 has not been given a full classification.
The recommended contribution to the batch admission count is zero.

A separate current-team non-author review is pending coordination at
the time of this receipt. No paid/human/external-model review is implied.
No manuscripts, C-numbers, formal evaluations, global-state mutations,
Git writes or GPU jobs were created.
