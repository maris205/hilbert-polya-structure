# P193 — Mutual-best block refinement

**Round:** `ROUND0_AUTHOR_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

This anonymous short paper studies a simultaneous permutation update.  Each
position nominates its smallest later smaller value; each such value nominates
its earliest earlier larger position; mutually nominating pairs exchange.
The literal update is exactly first--minimum exchange in every current
non-singleton direct-sum indecomposable block.

The paper proves the complete finite functional graph, a pointwise recursive
clock, maximum tail `n-1` with exactly `(n-1)!` deepest states, an exact
ordinary-generating-function recurrence for every depth layer, and a closed
every-target fibre product.  The image is the set of permutations beginning
with `1`, and the identity is the unique maximum-fibre target, with fibre
`2^(n-1)`.

Direct-sum decomposition and the common-master matching interpretation are
zero-credit background.  No external owner clearance or novelty claim is
made.

## Exact replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The complete default range is `S_1,...,S_9`.  The canonical terminal fields
are

```text
transitions=409113
assertions=7985745
transition_digest=28eedb5ba198c502e491d2788354ab2fe6de9785af1852bc3b4dd00f69f33761
status=PASS
```

The verifier performs target-by-target and source-by-source comparisons; the
digest is over all ordered `(n, source, image)` transition records.  Finite
checks are counterexample pressure, not proof or ownership evidence.

## Deterministic Round-0 build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` for the settled artifact record.

## File map

- `main.tex`, `references.bib`: anonymous standalone manuscript and its
  zero-credit background references;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`: story spine and section contract;
- `PROOF_PACKAGE.md`: normalized theorem statements, dependencies, and full
  proof audit;
- `CLAIMS_EVIDENCE.md`: claim-to-proof-to-falsifier traceability;
- `SOURCE_VERIFICATION.md`: citation scope and internal collision firewall;
- `code/verify.py`, `code/CANONICAL.txt`: independent standard-library exact
  control and byte-for-byte replay target;
- `BUILD.md`, `SELF_QA.md`: Round-0 build and author-side handoff records.

Posting, submission, and any other external circulation remain unauthorized.
