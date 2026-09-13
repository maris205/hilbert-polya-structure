# Independent Paper20 Expanded-Source R2 Review

**Review ID:** `PAPER_SOURCE_R2_EXPANDED_AUDITOR_2026_08_22`

**Scope:** read-only audit of the expanded `paper/main.tex`, the frozen source
lock, `BUILD_METADATA_R1.json`, and `SOURCE_REVISION_RECEIPT_R1.json`.  No
compile, CAS/symbolic run, experiment, transport operation, or source edit was
performed.

## Verdict

`PAPER_SOURCE_R2_EXPANDED_BLOCK`

The mathematical source is acceptable under the frozen theorem scope, but the
revision identity is not closed.  The live manuscript and both R1 identity
records disagree on the bound `main.tex` bytes/hash.  A new authorized revision
receipt (or an explicitly authorized replacement of the R1 receipt/metadata)
must bind the live source before this source can receive a PASS.

## Live source identity

The current read-only `sha256sum`/byte readback is:

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 58,951 | 1,552 | `a4a12679acaad9dd258178a417f70c0fa3626266d5cd10b0f527c8e197f41779` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 | 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 | 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 | 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

The manuscript is UTF-8, LF-only, with no BOM, CR, or NUL.  The source-lock
ten-file author aggregate was independently recomputed as
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90` over
45,416 bytes and 873 LF; all ten allowlist rows match their frozen bytes and
hashes.

## Identity blocker

Both R1 records still bind the predecessor manuscript, not the live expanded
source:

| record | stale declaration | live value |
|---|---|---|
| `SOURCE_REVISION_RECEIPT_R1.json`, `/source_files/0` | 58,433 B, 1,545 LF, SHA `3fce1641f04f0dc8a91a47ca9f1f57aae0bb92976af51f8cef50887feea428` | 58,951 B, 1,552 LF, SHA `a4a12679acaad9dd258178a417f70c0fa3626266d5cd10b0f527c8e197f41779` |
| `BUILD_METADATA_R1.json`, `/source_files/0` | 58,433 B, 1,545 LF, SHA `3fce1641f04f0dc8a91a47ca9f1f57aae0bb92976af51f8cef50887feea428` | 58,951 B, 1,552 LF, SHA `a4a12679acaad9dd258178a417f70c0fa3626266d5cd10b0f527c8e197f41779` |

The receipt's `source_identity_transition/main_tex.after` repeats the stale
3fce… identity.  Consequently the `author_stop`/`source_editing:false`
boundary is not bound to the bytes currently under review.  The fix is
bookkeeping only: regenerate an authorized revision receipt and corresponding
R1 metadata (or issue a new R2 revision record) with the live size/LF/hash,
then request a fresh source review.  This reviewer did not alter either record.

## Mathematical/source checks — PASS

The expanded source remains faithful to the frozen `source_lock.json` theorem
and proof contract:

- (K) is algebraically closed of characteristic zero, (ginmathbb Z),
  (gge5), and the displayed (V,W,S,T,F=Tcirc S) are unchanged.
- The explicit triangular inverses, symmetric-Hessian pullback, block
  Jacobians, determinant check, and inverse-Jacobian factorization are
  correct for the stated coordinate order.
- The complete potential/gradient support ledger contains every derivative
  row and separates carried coordinates from gradient rows.
- The (S)-selector and (T)-selector inequalities, including the
  intermediate ratio (v_2/v_1=(2+u_2/u_1)/(g-1)), are algebraically correct
  for (gge5).
- The half-open cone (1le u_2/u_1<(g-2)/2), fractional-linear ratio map,
  endpoint margins, and componentwise growth are correct.
- The (n=0) base case and simultaneous carried-term induction are explicit;
  (v_{n+1}=A_gu_n) is kept as a phase equality rather than incorrectly
  converted into a strict cross-phase cone inequality.
- The positive-semiring/characteristic-zero no-cancellation argument is
  sufficient for the fixed positive-coefficient family.
- (C_g=B_gA_g=[[g+3,2],[2(g-1),g-1]]), the (C_g-A_g) visibility check,
  the (q_2) total-degree functional, Perron eigenvectors/pairings, scalar
  recurrence, and ((\sqrt g+1)^2<(g-1)^2) calculation are correct.
- The (g=5) hand audit agrees with the symbolic phase recurrence.

No generic Newton-fan theorem, arbitrary-potential claim, universal
non-conjugacy claim, priority/firstness claim, numerical/CAS certificate,
periodic-point/trace/torus theorem, or external proof attribution was found.
The seven bibliography keys resolve to `references.bib`, and citation roles
remain context-only as required by the citation lock.

## Static labels and source hygiene — PASS

There are 60 unique `\\label` identifiers, all 54 `\\ref`/`\\eqref`
targets resolve, and no duplicate labels or duplicate explicit tags were
found.  `\\begin`/`\\end` environment counts balance (102/102), braces
balance, and no forbidden draft markers occur.  The source contains no CR,
BOM, or NUL bytes.

## Minor content correction (non-decisive)

At the support-ledger paragraph around current lines 486--493, the sentence
“The first, fourth, and fifth expressions are face comparisons” is inaccurate.
Reading the six displayed margins literally, the face comparisons are the
first and fifth individual expressions; the other four compare a selected
gradient term with a carried identity term.  This does not change any equation
or induction step, but should be corrected in the next authorized source
revision.  The phrase “Every monomial selected in `eq:phase`” in the
no-cancellation subsection is also better stated as “every selected leading
term,” since `eq:phase` is a degree-vector recurrence rather than a monomial
identity.

## Permission and downstream status

The frozen permissions still show build/CAS/experiment/publication/transport
disabled, and no downstream authority is granted by this review.  Because the
live `main.tex` is not the source bound by the R1 receipt/metadata, the
expanded source cannot be promoted to a source PASS until the identity records
are regenerated and reviewed again.

PAPER_SOURCE_R2_EXPANDED_BLOCK
