# P22 Stage-2.5 originality and AI-failure-mode audit

Date: **2026-08-24**  
Final audited manuscript SHA-256:
`5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc`

## Originality sample

**No blocking originality signal within the required sample.**

| Metric | Result |
|---|---:|
| eligible body paragraphs | 71 |
| sampled paragraphs | 22 |
| sampling rate | 30.99% |
| major numbered sections covered | 7/7 |
| ORIGINAL | 15 |
| COMMON_KNOWLEDGE | 1 |
| PARAPHRASE | 6 |
| CLOSE_MATCH | 0 |
| VERBATIM | 0 |

The sample consists of the fixed priority set plus a deterministic SHA-bound
top-up: `P01, P02, P10, P11, P13, P17, P32, P41, P44, P48, P54, P58,
P60, P61, P62, P63, P66, P67, P68, P69, P70, P71`.  Every major section has
at least one sampled paragraph.  Each paragraph was checked with an exact
8--12-word characteristic phrase and a broader semantic search, then compared
against the primary Deninger, Deninger--Mellit, and Stacks sources where
applicable.

Both Stage-2.5 citation corrections received an extra 100% delta check.  The
new Frobenius/Verschiebung attribution and the narrowed equation-(20)
description are accurate paraphrases with citations; neither is a close or
verbatim match.  The revisions improve source precision without changing the
originality verdict.

Self-plagiarism status is **NOT EXECUTED — AUTHOR UNKNOWN**.  The manuscript
still says `AUTHOR TO CONFIRM`, so no reliable author-publication corpus can
be constructed.  Public exact-phrase searches found no duplicate draft, but
that is not a substitute for author-aware D2 checking.

AI-writing heuristic signals: **0/6 triggered** (excessive smoothness, lack of
specificity, formulaic transitions, excessive parallelism, hedge overload,
and citation--argument gap all remained below their trigger conditions).

## Seven AI research failure modes

| Mode | Verdict | Evidence boundary |
|---|---|---|
| 1. Implementation bug passing self-review | CLEAR | No code-, data-, simulation-, or run-derived result; conclusions are explicit algebraic derivations.  This does not certify the absence of an ordinary proof error. |
| 2. Hallucinated citation | CLEAR | 3/3 sources and 18/18 contexts verified from official/primary records; both initial wording deviations were corrected and rechecked. |
| 3. Hallucinated experimental result | CLEAR | No metrics, seeds, datasets, logs, tables, runs, or observational-result language; all intended evidence is theoretical. |
| 4. Shortcut reliance | CLEAR | The proof handles every `N>1`, retains the `N=1` control, and treats fppf and finite-flat separately; there is no model/dataset shortcut surface. |
| 5. Bug reframed as novel insight | CLEAR | No implementation layer or anomaly narrative; the result is derived from the root cover, injectivity, and overlap calculation. |
| 6. Methodology fabrication | CLEAR | The declared proof method is visibly executed in the manuscript; no unrun experimental procedure or hyperparameter block is asserted. |
| 7. Early frame-lock | CLEAR | The RQ first isolated the `N=2` gate and site distinction, then expanded only after proof evidence; scope, topology, Frobenius, novelty, and Route boundaries remain explicit. |

No mode is `SUSPECTED` or `INSUFFICIENT EVIDENCE`; the seven-mode checklist
therefore adds no block.  D7 experiment-intake is a separate fail-closed
passport requirement and is not silently waived by these mode verdicts.

This is a public-Web/primary-source heuristic screen, not Turnitin or
iThenticate.  It cannot exhaust paid full text, unindexed or unpublished
work, translation reuse, or an unknown author's prior corpus.  A professional
full-text and author-aware check remains advisable before dissemination.
