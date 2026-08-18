# P47 writer report

Candidate: `SD-C49` / paper 47 writer overlay

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

This is a writer-side closure record.  It is neither an independent writer
audit nor an installation, publication, or authority-write authorization.

## Outcome

The candidate contains a complete 14-page A4 manuscript on the looped
harmonic-quotient graph operator.  It proves analytically that the
coefficient array is bounded and compact exactly on `Re(s)>0`, is
Hilbert--Schmidt exactly on `Re(s)>1/2`, and is trace class exactly on
`Re(s)>1`.  It derives the legal traces

```text
Tr(E_s)   = 2^(-s) zeta(s),
Tr(E_s^2) = zeta(2s) P(s)
          = zeta(2s) zeta_MT(s,s;2s) / zeta(4s),
```

with ordered edges and no extra factor two.  The complex identity is stated
only as left--right unitary multiplication, not conjugacy.  Ordinary and
regularized determinants remain in their exact trace-class and
Hilbert--Schmidt domains; the local quadratic coefficient is
`-Tr(E_s^2)/2`.  A mixed `15-30-60` triangle and the real negative
`{3,6}` principal minor supply the anti-fiber and sign witnesses.

Canonical finite results are labeled implementation replay only.  The paper
does not turn finite PASS fields into proof, claim priority for Egyptian or
Mordell--Tornheim algebra, or assert an all-Schatten theorem, functional
equation, completed divisor, rational-prime ledger, or Hilbert--Pólya
operator.

## Independent visual-HOLD repair

The prior writer overlay failed its independent visual audit because the
three thick domain bands in Figure 2 crossed their labels and the strict-wall
note collided with the axis ticks and the negative-domain label.  The
repaired vector source, SHA-256
`1da86f01205cb0ea57af2a7dc47bcb5993e1e3374229237cf7464fe320904c52`,
places each label above its band and places the strict-wall explanation in a
separate white callout to the right of the axis.  The thresholds `0,1/2,1`,
open endpoints, band extents, color/domain semantics, and negative-domain
statement are unchanged.

The rejected rendering and its seal are withdrawn permanently:

- withdrawn PDF SHA-256:
  `bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0`;
- withdrawn writer-seal SHA-256:
  `cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0`.

Only the new anchors in this report and its downstream handoff/seal are
valid.  The repair has passed writer-side checks but still requires the same
auditor's fresh independent recheck.

## Paper artifacts and QA

- final `main.pdf` and `main_round2.pdf` SHA-256:
  `b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d`;
- preserved Round-0 PDF SHA-256:
  `3cab9e5f273b584d8759c5b7a88ed8f145046c6402bb651d94d01c21331eeb53`;
- preserved Round-1 PDF SHA-256:
  `5837f352495e0688bc1b0785a031c8cc04f01f5a811adb5332e04cfeb4abc087`;
- final bibliography SHA-256:
  `dd828b408bbe3bb486a8d8ea7fc8794d9c6759ac564176befae50dadf5a235dc`;
- final compile-log SHA-256:
  `23cf89d34d194a01ff9a4c3bcd3611670099f7286bccc121c336dbf89e7973d2`;
- final PDF-QA record SHA-256:
  `e761980bddd67519af3bc6da2e120c088c435a32871b00abe50f11f38b4b8cc1`.

Two clean builds at `SOURCE_DATE_EPOCH=1787011200` reproduced the PDF,
bibliography, and log byte for byte.  The final log is warning-free.  All 14
A4 pages were rasterized at 170 dpi and inspected individually; page 7 now
has white separation between every band and label, and the strict callout is
clear of the three ticks and the negative-domain label.  All 29 font records
are embedded, subsetted, and Unicode mapped, with no Type 3 font.  Default,
layout, and raw text extraction each has zero illegal C0/DEL/C1 and zero
replacement characters.  Both bbox modes report 6,490 words and zero
out-of-page boxes.

## Plan and manuscript reviews

The independent formal-plan gate returned `PLAN_READY`, C0/M0, and its
historical reviewed plan hash is
`a8b9c848b659e5a3a4bfeb74b9f28565b3c1dc461768e43a9695421932ab7a1f`.
During manuscript Round 1, the reviewer correctly required the plan's
quadratic-coefficient wording to be normalized by `-1/2`.  The current plan
therefore has SHA-256
`13f9516230a6c90718f8ea9894c24567e8ea81eff51b87672b8a655b423017ac`;
Round 2 explicitly verified this synchronization.  The historical plan
reviews remain unmodified.

The same GPT-5.4 xhigh manuscript reviewer performed both rounds:

- Round 1: `C0 / M2 / m3`, `ROUND1_FIX`;
- Round 2 after all five fixes: `C0 / M0 / m0`, `ROUND2_READY`.

Raw reviews are retained in full.  Their SHA-256 values are
`f9a4440721be6a44d4c80534b3e2c11878194f23064e99f428aea6cbb3e9d1c6`
and
`fd4b76ffc052a67e393b8cab165afe09bef16571d5a965abede2a8294c628eb9`.
`PAPER_IMPROVEMENT_LOG.md` embeds both raw reviews verbatim, records the
later visual-HOLD repair and withdrawn anchors, and has SHA-256
`6825db382c5f9497a01043f4d8d0d051782e64ab0a8604c7ca4e67103ba90680`.

## Protected State-A replay

`PROTECTED_STATEA_TREE.tsv` covers exactly 91 live protected nodes: 67
regular files and 24 directories.  This is the exact 62-node sealed Stage0
tree plus the 29-node State-A `outputs/` tree, whose 20 regular files have
tree SHA-256
`328527680d533e34ce3aabc17f2cf5688759b0674b7fc8740d0c2df332b64c42`.

Two final repeated invocations, each internally taking two live captures,
matched all protected bytes and metadata.  There were zero missing, extra,
kind, mode, size, or hash mismatches and zero authority mutations.

- portable protected manifest SHA-256:
  `30a79c4be4bc9b9333cb2a9f809d2039430cebc86686a054765734a782eea473`;
- protected replay JSON SHA-256:
  `bd172e5a1f7523211f8784a4384c6e885f33d681b6bc8dc728bbd96ea378f4c3`;
- static 47-file sums SHA-256:
  `1524fa69a7c429a7483ec4153368a2da4269ed81d70d9d6abcbcc196e9bd4406`;
- canonical State-A result-ledger SHA-256:
  `dba161719ef85dee433a13aa14505ab6b0f5ff0fef8c627ea39ddb4bf81bfe47`.

No authority or Stage0-candidate path was written.

## Canonical replay and evidence boundary

The candidate-local summary has SHA-256
`45185ea8750dec4557b055f0381137076df5d1615c51c482fa96e623f8ed1d7f`.
It records exact support counts `(N, ordered edges, loops)` of
`(16,16,8)`, `(32,40,16)`, `(64,96,32)`, and `(128,228,64)`, with all 12
comparison keys PASS.  The mutation suites contain 39 theorem/governance,
35 expanded, and 15 external-auditor instances with zero survivors.  Route
A remains rejected and Route B remains forbidden.  These are finite and
provenance statements, not premises for the infinite theorem.

## Exact writer overlay

`PAPER_MANIFEST.tsv` has 51 sorted content rows and SHA-256
`10bc900a80497637ec397bbc7c7d43c5be736845dee413129252fa07920a98cf`.
It deliberately excludes exactly itself, `WRITER_REPORT.md`, `HANDOFF.md`,
and `WRITER_SEAL.json`.  After closure the overlay contains 55 regular
files, all mode 0644, and nine directories including the root, all mode
0755.  It contains no symlink, cache, LaTeX auxiliary, `outputs/**`,
`evidence/publication_gate/**`, protected snapshot copy, Git path, README,
or mirror path.

The dependency direction is content to manifest to report to handoff to
seal.  No manifest-covered artifact contains the writer-seal hash.
