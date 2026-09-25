# FRACTRAN PRIMEGAME encodes primes on a wandering universal computation

**Paper ID:** 093-fractran-primegame-boundary  
**Record ID:** ASFS-SCOUT-20260914-63  
**Date / status:** 2026-09-14; EXTERNAL COMPUTATIONAL CONTROL  
**Route state:** No formal ASFS Route-A coordinate; Route B NOT INVOKED.

## Frozen object

A FRACTRAN program is a finite ordered fraction list. At integer state (n), it multiplies by the first listed fraction whose product remains an integer. Conway's PRIMEGAME is one fixed list. Starting from its specified seed, it encounters powers (2^p) exactly for successive prime exponents (p).

Every such output has a different integer state. Since the exponents are unbounded, the prime-coded trajectory cannot be periodic. Selecting an unrelated periodic state would not retain prime-output ownership.

| Obligation | Finding | Status |
| --- | --- | --- |
| Fixed execution rule | finite program list | established |
| Arithmetic relation | prime exponents of outputs | computational control |
| Closed packet/repetitions | prime-coded trajectory is wandering | scoped FAIL |
| Prior-work lineage | no sieve-symbolic deformation or Hénon owner | scoped FAIL |
| Roof/flow/operator | absent | NOT EVALUATED |

FRACTRAN is Turing-complete. This is an adverse control: a universal program can encode arbitrary computable output, so its prime sequence is not a natural project mechanism without an additional owner relation.

## Decision

**Portfolio position: stop/external control.** Do not reversibilize, suspend, or geometrize PRIMEGAME without a new frozen object and direct lineage proof.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Conway/FRACTRAN source record](evidence/README.md)
- [054 prime-time nonrecurrence boundary](../054-prime-time-observation-nonrecurrence/paper.md)
