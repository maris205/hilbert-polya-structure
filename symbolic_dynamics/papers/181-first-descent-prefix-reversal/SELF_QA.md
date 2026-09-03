# P181 author self-QA

**Decision:** `ROUND2_DUAL_REVIEW_ACCEPTED / OWNER_AMBER`  
**External state:** `HOLD_EXTERNAL`

## Mathematical closure

- The first descent uses one-based position `d`, and the reversed prefix has
  length `d+1`; the follower is included.
- The identity is the unique descent-free permutation and is explicitly
  fixed.  No nontrivial prefix reversal can fix a permutation with distinct
  entries.
- Every nonfixed output begins with `pi_(d+1)<pi_d`; the converse image proof
  uses the literal two-prefix predecessor.  The image equality is therefore
  proved in both directions.
- A position-two peak has first descent exactly two, so its action is
  `rho_3`.  Its partner is a distinct peak and returns in one step.
- Every nonidentity image state that is not a peak starts with three
  increasing entries.  Reversing at its later first descent creates a peak
  in the first three output positions.  This excludes hidden cycles.
- The inverse lemma translates the complete first-descent condition, not
  only a necessary inequality.  Different prefix lengths give different
  predecessors.
- The identity's fixed predecessor is added exactly once and is distinct from
  `rho_2(identity)`.
- The depth-two set is proved bijective to `I_n \ R_n`; depth one is then
  obtained by subtraction.  All three populations sum to `n!`.
- For `n>=4`, the identity's fibre two cannot tie the run maximum.  A full run
  forces `n` into position two and leaves exactly `n-1` choices for position
  one.
- The `n=1`, `n=2`, and `n=3` functional graphs and fibres are written out.
  The `n>=4` maximizer statement is not forced onto any small boundary.

## Source and owner closure

- All three bibliography entries were retrieved from DOI/Crossref and
  checked on SIAM, Elsevier/ScienceDirect, DBLP, primary PDF/preprint, or
  author surfaces.  The `.bib` file has no uncited entry and every citation
  resolves.
- The Gates–Papadimitriou DOI is the verified `...90068-2`, not `...90068-X`.
- Generic pancake sorting, arbitrary prefix reversal, binary/ternary string
  reversal, and longest-increasing-prefix cut-and-shuffle maps receive zero
  contribution credit.
- Project Euler Problems 523–524 are official negative controls for the
  follower-to-front First Sort rule.  The example `1324` separates it from
  P181 as `2134` versus `2314`.
- P122's deterministic permutation reversal and inverse-cut proof vocabulary,
  P117's reversal/cycle vocabulary, the killed FDF owner match, and the FAR
  value-complement conjugate are all subtracted or firewalled.
- A bounded owner-search miss is never called novelty, priority, or freedom
  to operate.  `OWNER_AMBER / HOLD_EXTERNAL` is visible in the manuscript and
  all lifecycle documents.

## Artifact closure

- The canonical verifier replay is byte-identical and ends with 6,273,070
  assertions, `status=PASS`, and `external_status=HOLD_EXTERNAL`.
- The settled PDF has three A4 pages and no warning, bad box, unresolved
  reference/citation, rerun request, or fatal error.
- All 28 font rows are embedded, subsetted, and Unicode mapped.  The PDF is
  unencrypted and contains no forms or JavaScript.
- PDF title, author, subject, keywords, creator, and producer metadata are
  blank; the visible author is `Anonymous`.
- All three pages were visually inspected.  The theorem continuation,
  equations, table, footnote, references, and running furniture are legible
  and unclipped.
- `main_round0_original.pdf` preserves the author baseline;
  `main_round1.pdf`, `main_round2.pdf`, and the live repaired PDF are
  byte-identical.
- Two source-only cold builds reproduce the live PDF byte for byte at SHA-256
  `57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861`.
- Source files contain no control byte, TODO, FIXME, placeholder citation,
  email, ORCID, local path, or unauthorized release language.
- Review A's `S_1` boundary finding is repaired and formally accepted with
  `0 Critical / 0 Major / 0 Minor` open after a 17,364,060-assertion replay.
- Process-separated Review B accepted image, recurrence, tails, full incoming
  sets, maximizers, small boundaries, and the First Sort negative control
  with 377,591 assertions and zero open findings.

## Remaining theorem concern

No defect is known in the five frozen claims or the three small boundaries,
and both hostile reviews are closed.
The live risk is external ownership: the mechanism is elementary enough that
an equivalent autonomous rule may exist under different terminology.  The
correct state therefore remains `OWNER_AMBER / HOLD_EXTERNAL`.
