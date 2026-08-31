# Control results

## Fresh independent verifier

Run on 2026-08-31 UTC from the repository root:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Result: `cmp` status `0`.

```text
PARTITIONS_N_LE_45=540634
PERIODS=1,2
MAX_TAIL=6
FIRST_TAIL_WEIGHTS=0:1,1:2,2:5,3:9,4:15,5:30,6:45
N30_FIXED_CYCLES_RECURRENT=59,139,337
ALL_TARGET_CELLS_N_LE_30=28628
NONZERO_TARGET_CELLS_N_LE_30=5379
WREATH_CASES=18
WREATH_ELEMENTS=1259
TAG_INITIAL_N_LE_30=28628
TAG_REACHABLE=118634
TWO_CLEAN_PAIRS=56961
TOTAL_ASSERTIONS=7130840
EXACT_ARITHMETIC=python_integers_and_tuples
FLOATING_POINT=none
SAMPLING=none
STATUS=PASS
```

## What is checked

- the three-case partition map preserves weight at every tested state;
- complete functional graphs through weight 45, including every period and
  tail, versus the recurrent decoder;
- fixed-point and strict-cycle OGF coefficients through weight 30;
- the multivariate source product versus every one of 28,628 target
  partitions through weight 30, including all zero fibres;
- literal permutation multiplication, commutators, generated derived
  groups, and natural-point orbits in 18 wreath products with 1,259 source
  group elements;
- the whole/split tag invariant, strict tag-count loss exactly on crossing
  merges, and 56,961 instances of the two-clean-step lemma across 118,634
  reachable tagged states.

The maximum observed tail six is not used to sharpen the theorem's safe
`2 ell(lambda) <= 2n` bound.  Finite enumeration is a falsifier only and
does not prove the all-weight theorem or establish novelty/priority.

## Immutable Round-0 pinned hashes

```text
26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a  code/verify.py
be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90  code/verification_output.txt
386b0cbca5cf812599687df39e3db43ee0edb47cb500f7718742b9badf0cb273  main.tex
515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae  references.bib
7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b  main_round0_original.pdf
```

The `386b...` source pin above is historical: it is the source that produced
the immutable Round-0 PDF, not the current repaired manuscript.

## Current Round-1 pinned hashes

```text
cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149  main.tex
515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae  references.bib
26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a  code/verify.py
be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90  code/verification_output.txt
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main.pdf
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main_round1.pdf
```

External status: `HOLD_EXTERNAL`.
