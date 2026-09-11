# P192: First-Collision Hurwitz Dynamics

Current internal status: Review-A repair incorporated;
`OWNER_RED_AMBER/HOLD_EXTERNAL`. The immutable Round-0 PDF is retained
separately for provenance.

This directory freezes an internal theorem-note package for a deterministic map on minimal transposition factorizations of the long cycle. It does not assert novelty, priority, completeness of the owner search, or freedom to operate. External circulation is on hold.

## Frozen system

For (n\ge 2), let

\[
\mathcal F_n=\{(\tau_1,\ldots,\tau_{n-1}):
\tau_1\cdots\tau_{n-1}=(1\,2\,\cdots\,n)\},
\]

where products act rightmost first. Write every transposition as ((a,b)) with (a<b), and set \(\ell((a,b))=a\). At a state (f), choose the least (i) for which

\[
\ell(\tau_i)=\ell(\tau_{i+1}),
\]

then apply the right Hurwitz move

\[
H_i(\ldots,x,y,\ldots)=(\ldots,y,yxy,\ldots).
\]

If there is no collision, hold. The long-cycle orientation, right Hurwitz convention, numeric endpoint order, and least-index scheduler are part of the definition.

## Claim boundary

The manuscript proves four axes:

- executed indices increase strictly, so all recurrence is fixed;
- the maximum tail is exactly (n-2);
- the fixed-state count is ((n-1)^{n-2});
- every labelled target has an exact one-step inverse-Hurwitz fibre atlas, with unique maximum indegree (n-1) at the adjacent-transposition chain.

The history-set formula

\[
\#\{f:\operatorname{Hist}(f)=I\}=(n-1)^{n-2-|I|}
\]

is a conjecture only. It is supported by exhaustive local computation for (2\le n\le8) and a separate streaming computation for (n=9). Neither computation is an all-(n) proof. Claims derived from that formula, including a general binomial depth law or unique deepest state, also remain conjectural.

## Reproduce the finite checks

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
g++ -std=c++17 -O3 -Wall -Wextra -pedantic code/verify_n9.cpp -o /tmp/p192_verify_n9
/tmp/p192_verify_n9 | cmp - code/CANONICAL_N9.txt
```

The Python check exhausts all 280,392 states for (2\le n\le8), performs 1,962,920 assertions, and tests the proved theorem package as well as the finite history masks. The C++ program independently streams all (9^7=4,782,969) Prüfer words and checks all 128 history masks at (n=9). Its output explicitly labels the result `n9_verified_not_claimed_all_n`.

See [BUILD.md](BUILD.md) for the deterministic cold-build recipe and exact artefact data.

## Package map

- [main.tex](main.tex) and [main.pdf](main.pdf): current repaired source and four-page canonical PDF (SHA-256 `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57`).
- [main_round0_original.pdf](main_round0_original.pdf): immutable three-page Round-0 review pin (SHA-256 `aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1`), intentionally different from current `main.pdf` after repair.
- [NARRATIVE_REPORT.md](NARRATIVE_REPORT.md): mathematical story, contribution subtraction, and risk posture.
- [PAPER_PLAN.md](PAPER_PLAN.md): section and claim plan.
- [FIGURE_PLAN.md](FIGURE_PLAN.md): deliberately minimal visual plan.
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md): assumptions, dependencies, and expanded proofs.
- [CLAIMS_EVIDENCE.md](CLAIMS_EVIDENCE.md): claim-by-claim proof/source/computation matrix.
- [SOURCE_VERIFICATION.md](SOURCE_VERIFICATION.md): citation metadata audit and owner-search boundary.
- [BUILD.md](BUILD.md): verifier replay, cold compile, PDF data, and bibliography delta.
- [SELF_QA.md](SELF_QA.md): Round-0 checks, accepted-repair addendum, and unresolved defects.
- [code/verify.py](code/verify.py) with [code/CANONICAL.txt](code/CANONICAL.txt): exhaustive (n\le8) controls.
- [code/verify_n9.cpp](code/verify_n9.cpp) with [code/CANONICAL_N9.txt](code/CANONICAL_N9.txt): independent (n=9) stream.
- [main_pre_metadata_audit.pdf](main_pre_metadata_audit.pdf): noncanonical pre-metadata-audit snapshot retained only for provenance; it contains the superseded bibliography metadata.

## Release gate

The classical Hurwitz moves, minimal-factorization counts, parking-function
correspondence, Pollak count, ordinary tree/Prüfer encodings, and Campion
Loth--Rattan conditional Hurwitz-string bijection receive zero contribution
credit. The residual object is the literal adaptive first-collision scheduler
together with its target-resolved inverse atlas. A complete external
exact-scheduler owner search has not been frozen. The package therefore
remains `OWNER_RED_AMBER/HOLD_EXTERNAL`.
