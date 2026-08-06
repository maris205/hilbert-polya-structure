# Superseded R401-VAL-L1-MG V1 release

This directory preserves the original V1 derived archive byte-for-byte for
audit history.  It is **non-licensing** and must not be cited as the current
`PASS_LOCAL_MONODROMY_GAP` release.  The authoritative replacement is
`results/r401_val_l1_monodromy_gap/`, protocol `R401-VAL-L1-MG-V2`.

## What remains valid

The V1 `summary.json` retains exact numerator/denominator endpoints obtained
from all 202 frozen monodromy transcripts.  Those exact fractions still give

\[
 4-\operatorname{tr}M>3
\]

on the already certified local fast branch.  The supersession does not
declare the exact-fraction core false.

## Why V1 is non-licensing

V1 produced its human-readable `decimal_18` values by converting exact
fractions to binary `float` and applying nearest formatting.  The report then
presented those approximations as lower bounds or interval widths without a
directed-rounding certificate.  In particular:

- the displayed 256-bit lower value `3.8507419689457949` lies above its exact
  rational endpoint and therefore is not a rigorous lower bound;
- the displayed 128-bit width `0.054493101512001145` lies below its exact
  rational width and therefore is not a rigorous upper display.

V2 retains every exact numerator and denominator, generates fixed 18-place
floors for lower bounds and ceilings for upper bounds, and independently
replays all 815 decimal payloads.  No V1 internal `PASS` field overrides this
supersession notice.

The complete old hash chain—including the old protocol, analyzer, checker
source, summary, manifest, checker result, postcheck, report, release record,
and freeze—is recorded in `AUDIT_RECORD.json`.  Some old source texts were
not duplicated in this directory; their hashes remain bound by the original
release/manifest/postcheck chain, and the audit record states that limitation
explicitly.
