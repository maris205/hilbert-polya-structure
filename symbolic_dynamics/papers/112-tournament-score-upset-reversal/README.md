# P112 — Synchronous tournament score-upset reversal

Status: **ANONYMOUS WORKING MANUSCRIPT / EXTERNAL HOLD**.

For a labelled tournament `T`, the update reorients every edge between
unequal-score vertices from the higher-outdegree endpoint to the lower one,
while retaining an edge on a score tie.

The manuscript proves the following map-specific exact conjunction:

1. a simultaneous-incidence formula, strict squared-score Lyapunov identity,
   local fixed criterion, and absence of nontrivial cycles;
2. equal-score ordinal-sum decomposition and recursive factorization of all
   later iterates;
3. pointwise depth equal to score-refinement-tree height and `tau<=n-1`;
4. fixed points equal unique ordered sums of regular tournaments.

The fixed recurrence, EGF `F=1/(1-R)`, regular counts, and zeta
`(1-z)^(-f_n)` are retained only as zero/low-credit standard corollaries.
In the explicitly specified scan by increasing order and then increasing
numeric mask, mask `148` is the least nonidempotent state through `n=6`.
That is a finite regression signal, not a global depth theorem.

The paper does **not** claim a sharp global depth formula or a complete
transient enumerator.  Landau/Moon tournament structure, Rubinstein/Henriet
static score procedures, Bouyssou and Linares Lejarraga--Bodanza iterative
choice procedures, Ryser/Thomassen/ESA 2026 reversal work, McKay
regular-tournament enumeration, generic labelled EGFs, and Artin--Mazur zeta
bookkeeping are all explicitly zero-credit.  P106 is separated by phase
space, update rule, and proof engine.  No novelty, priority, or owner-clearance
claim is made.

## Reproduce the exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The canonical run makes **1,677,508** assertions over all **33,868** labelled
tournaments through order six.  Its stdout is stored in
`code/verification_output.txt`.

## Build the draft

See `BUILD.md` for the exact four-stage LaTeX commands and mechanical result.
Public release, submission, and specialist contact remain **HOLD**.
