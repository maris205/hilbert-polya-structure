# Improvement log — P148

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Baseline

The initial theorem package proved the divisible-depth dynamics, exact clock,
ordered block-and-gap fibre, exact-size image criterion, and algebraic image
series.  Its proof verifier passed, but the first ownership posture omitted a
direct same-object source.

## Hostile Review A

**Score:** 1 Critical / 0 Major / 2 Minor.

1. **Critical owner hit.**  Soo--Khoussainov--Linz Definition 6.6 directly
   owns the unordered one-step outward-contraction.
2. **Minor proof exposition.**  The every-target fibre proof needed the
   explicit recursive bijection `F_U=A_d product_j F_{U_j}`.
3. **Minor metadata.**  The Höner spelling and 2020/2021 publication
   convention needed correction to the 2021 journal issue record.

The gate was reopened and external status remained `HOLD_EXTERNAL`.

## Implemented repair set

- Added the direct owner citation to the manuscript and source ledgers.
- Added the exact forgetful equivalence
  `For(E(T)) ≅ OutContr(For(T),root(T))` and its quotient-edge proof.
- Assigned the unordered rule, partition-tree interpretation, and bare
  height compression zero contribution credit.
- Screened the full v4 references and bounded later-citation/query lanes;
  recorded every non-hit as bounded and non-certifying.
- Expanded Theorem 3 with the recursive `F_U` bijection, unique block/gap
  recovery, injectivity, surjectivity, no double count, induction, and
  coefficientwise finiteness.
- Corrected `H{\"o}ner zu Siederdissen` and the version-of-record year 2021.
- Rebuilt the manuscript with 5/5 primary references resolved and visually
  inspected the corrected bibliography.

## Hostile Review B

**Score:** 0 Critical / 0 Major / 0 Minor — **ACCEPT**.

Review B independently rederived the owner equivalence and all theorem
interfaces, checked the v4 source and bounded later-citation audit, replayed
the verifier, made an isolated source-only build, and visually inspected all
five pages.  No further source, proof, metadata, build, or layout repair was
required.

Review B imposed the final conservative scoring interpretation: iterating
the direct-owned unordered operator makes its unordered depth-divisibility
and binary clock cheap consequences.  They remain correct supporting
theorems but receive zero contribution credit.

## Final claims subtraction

Zero credit:

- unordered one-step outward-contraction and partition-tree semantics;
- generic ordered child promotion and bare height compression;
- cheap unordered all-rank depth/clock consequences; and
- generic Catalan, parity, transition, and pruning background.

Only this conjunction survives:

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

## Round-2 freeze

- `main.pdf`: 5 A4 pages, 357,397 bytes.
- SHA-256:
  `5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957`.
- Exact control: 216,905 assertions, canonical PASS transcript.
- Bibliography/visual: 5/5 references, 5/5 pages accepted.
- Reproducibility: isolated source-only build byte-identical.

The current PDF is the accepted round-2 artifact.  No change in this closure
log authorizes external release or a Git operation.
