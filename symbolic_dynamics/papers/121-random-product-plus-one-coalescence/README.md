# P121 — Higher-moment pole ladders in product-plus-one coalescence

Status: **ANONYMOUS OWNER-REWRITE / INTERNAL REVIEW / EXTERNAL HOLD**.

Start with `n` ordered copies of one, repeatedly select a current adjacent
pair uniformly, and replace `(x,y)` by `xy+1`.  The terminal value `X_n` is
not a newly discovered random-tree statistic.  Disanto, Fuchs,
Paningbatan, and Rosenberg (Annals of Applied Probability, 2022,
DOI `10.1214/22-AAP1791`) study the Yule root-configuration count `R_n`, and
the common ordered-history coupling gives, object by object,

```text
X_n = R_n + 1.
```

Their uniform split, finite law, unmarked antichain correspondence, complete
mean analysis, and second-moment/variance neighborhood receive zero
contribution credit.  Andriantiana--Wagner--Wang own the fixed-tree
cardinality marker, while Chang--Fuchs and Rosenberg own the caterpillar
probability neighborhood.

## Residual theorem package

After that subtraction, the paper retains only:

1. the **Yule-averaged** cardinality-marked antichain transform and its
   closed bivariate Euler/logarithmic-derivative form; and
2. beginning at moment order `r=3`, a strict continuation
   `rho_r<rho_(r-1)`, a unit-residue positive pole, and the exact exponential
   `limsup`.

The arbitrary-order moment identity is a mechanical binomial expansion of
the owned exact law and receives zero credit.  The minimum and its exact
mass `2^(n-2)/(n-1)!` are retained only as fully owned controls.

For `r>=3` the paper does **not** claim a unique dominant complex
singularity or a full coefficient asymptotic.  A bounded focused search did
not locate the Yule-averaged transform or a strict `r>=3` continuation of the
owned low-order pole ladder, but a search miss is not novelty, priority, or
owner clearance.

## Exact controls

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The standard-library verifier makes **139,589** exact assertions.  It checks
every boundary order through `n=9`, complete laws through `n=12`, moments
through order six, and coefficient identities through `n=60`.  It also
parses `code/marked_antichain_coefficients.tsv` exactly.  Finite computation
does not prove the pole ladder or any ownership claim.

See `BUILD.md` for the anonymous four-stage PDF build.  The frozen initial
PDF is retained as `main_round0_original.pdf`; repaired snapshots are kept
separately.  Public posting, submission, and specialist contact remain
**HOLD**.
