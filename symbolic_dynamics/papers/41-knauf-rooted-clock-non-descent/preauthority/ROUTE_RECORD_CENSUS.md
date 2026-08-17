# Existing Route-record census

## Integrity frame

The authority tree contains 42 path-distinct Route-A YAML records through
terminal Paper 39.  This includes two historical records labeled `SD-C07`
(Papers 4 and 5) and ends at `SD-C41`.  Paper 40 is separately research-sealed
as proposed `SD-C42`; it is not counted as an integrated Route YAML here.

The path-sorted stream was frozen by:

```bash
find AUTHORITY/symbolic_dynamics/papers \
  -path '*/evaluations/route_a/*/*.yaml' -type f -print0 \
| sort -z | xargs -0 sha256sum | sha256sum
```

Result:

```text
record_count = 42
sha256sum_stream_sha256 = 4ae213350dd1aadedea717bd46ebf54e888b7f108a8b6cf35644aece39944d86
path_list_sha256 = 63439d5f3a57e42837edaa4514a922743b98265b96c34dcb19c56ccca3770054
```

The path-list hash uses authority-relative paths, newline terminated and
lexicographically sorted.

## Tuple census

Abbreviations: `AO=ANALYTIC_ARITHMETIC_ORIGIN`, `SA=STRUCTURAL_ARITHMETIC_RELATION`,
`WA=WEAK_ARITHMETIC_RELATION`, `PA=PASS_ANALYTIC`, `AD=ANALYTIC_DETERMINANT`,
`PS=PARTIAL_ANALYTIC_STRUCTURE`, `FH=FORMAL_HINT`, `F=FAIL`, `W=WEAK`.

| Record | Tuple | Overall |
|---|---|---|
| C01 | `(WA,PA,AD,F,F)` | rejected |
| C02 | `(F,F,AD,F,F)` | rejected |
| C03 | `(F,W,F,F,F)` | rejected |
| C04 | `(WA,PA,AD,PS,FH)` | exploratory |
| C05 | `(SA,F,F,F,F)` | exploratory |
| C06 | `(AO,F,F,PS,F)` | exploratory |
| C07 / Paper 4 | `(AO,PA,AD,PS,F)` | analytic candidate |
| C07 / Paper 5 | `(AO,PA,AD,PS,F)` | analytic candidate |
| C08 | `(AO,PA,AD,PS,FH)` | analytic candidate |
| C09 | `(AO,PA,AD,PS,FH)` | analytic candidate |
| C10 | `(AO,PA,AD,PS,FH)` | analytic candidate |
| C11 | `(AO,PA,AD,PS,F)` | exploratory |
| C12 | `(AO,F,AD,F,F)` | rejected |
| C13 | `(AO,F,AD,F,F)` | rejected |
| C14 | `(AO,PA,AD,F,F)` | rejected |
| C15 | `(AO,PA,AD,F,F)` | rejected |
| C16 | `(AO,W,AD,F,F)` | rejected |
| C17 | `(AO,F,AD,F,F)` | rejected |
| C18 | `(AO,W,F,F,F)` | rejected |
| C19 | `(AO,W,AD,PS,F)` | rejected |
| C20 | `(AO,W,AD,F,F)` | rejected |
| C21 | `(SA,PA,AD,F,F)` | rejected |
| C22 | `(SA,PA,F,F,F)` | rejected |
| C23 | `(SA,W,AD,F,F)` | rejected |
| C24 | `(SA,W,AD,F,F)` | rejected |
| C25 | `(SA,W,AD,F,F)` | rejected |
| C26 | `(SA,F,F,F,F)` | rejected |
| C27 | `(SA,F,AD,F,F)` | rejected |
| C28 | `(SA,F,AD,F,F)` | rejected |
| C29 | `(AO,PA,AD,F,F)` | rejected |
| C30 | `(SA,F,AD,F,F)` | rejected |
| C31 | `(SA,F,AD,F,F)` | rejected |
| C32 | `(SA,F,AD,F,F)` | rejected |
| C33 | `(SA,PA,F,F,F)` | rejected |
| C34 | `(SA,F,AD,F,F)` | rejected |
| C35 | `(SA,F,F,F,F)` | rejected |
| C36 | `(SA,F,F,F,F)` | rejected |
| C37 | `(SA,F,F,F,F)` | rejected |
| C38 | `(SA,F,F,F,F)` | rejected |
| C39 | `(SA,F,AD,F,F)` | rejected |
| C40 | `(SA,F,F,F,F)` | rejected |
| C41 | `(F,F,F,F,F)` | rejected |

## Relevance audit, not successor ranking

The census shows three close methodological collisions:

1. `C35` already makes operator descent an explicit ownership obligation;
2. `C37` already separates a diagonal partition trace from a graph
   determinant;
3. the Paper-40 sealed `C42` research package already owns the Gauss/Mayer
   cyclic-pair and projection analysis.

These records narrow Paper 41.  They do not select it.  The six-card Boolean
rule in `SELECTION_AND_PROVENANCE.md` is retrospective over known results and
provides governance-independent uniqueness only, not prospective selection.

## Separately sealed Paper-40 research result

The final research seal records proposed `SD-C42` with tuple

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

and `ROUTE_A_REJECTED`, Route B false.  It is audited only as a collision and
object-boundary record.  Its corrections are not Paper-41 novelty.
