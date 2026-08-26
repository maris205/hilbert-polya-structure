# Paper 15 replacement candidate lock

Status: `PHASE1_REPLACEMENT_CANDIDATE_UNPROVED`  
Version: `P15R-CAND-v1.0`  
Batch design lock: `sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8`  
Batch amendment v1: `sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802`  
Transverse precheck: `sha256:02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb`

## Candidate owner

For each rational prime `p`, the owner is the bare compact group

```text
B_p = (product_{ell != p} Z_ell^x) / p^{Zhat}.
```

The marked presentation, Paper-9 actual indiscrete `Q_p`, Paper-16
standardized flow, and Paper-18 measured owner are separate records.

## Candidate center

Compute the characteristic pro-primary torsion-closure indices

```text
kappa_r(p)=log_r [B_{p,(r)}:closure(Tor(B_{p,(r)}))]
```

and prove that the full signature is a complete invariant among the groups
`B_p`, with the exact valuation formulas and `B_2 not~ B_3` as an explicit
arithmetic separation.

## Pass/fail disposition

- `FULL_PAPER_PLAUSIBLE` requires the complete height-saturation, Ulm,
  compact torsion-closure, and iff-classification package.
- A single separation or marked conductor formula is `MERGE_OR_STOP`.
- `UNIVERSAL_RECOVER_P=OPEN`; it is not an authorized theorem.
- The old mixed-clock project is historical and merged into Paper 16.

## Hard locks

No transfer from `B_p` to actual `Q_p`; no conductor label promoted to a bare
invariant; no hidden GRH; no erased `r=2` sign; no finite controls promoted
to infinite proof; no Haar/trace/operator/determinant credit; Route B and
Git/public synchronization false.

This lock authorizes independent Phase-1 reviews only.
