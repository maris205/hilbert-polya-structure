# P194 — least-colour raising on crystal words

**Round:** `ROUND0_PRESERVED / REVIEW_B_SOURCE_REPAIR_INSTALLED`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

For words in `[k]^n`, this anonymous short paper applies the Kashiwara
raising operator of the least currently available colour and otherwise
holds.  The signature convention is frozen literally: write `+` for `i` and
`-` for `i+1`, delete `+-` pairs, let `e_i` change the rightmost unpaired
`i+1`, and let `f_i` change the leftmost unpaired `i`.

The paper proves that each crystal component flows to its unique highest
word and that the exact tail is

```text
sum of the letters - sum_i i lambda_i,
```

where `lambda` is the component shape.  The global maximum is `n(k-1)`,
uniquely at `k^n`.  Normalized principal Schur specializations give all depth
layers, with shape multiplicity `f^lambda`; fixed words are counted by
bounded-height involutions.  The scheduler-specific result is a complete
labelled one-step inverse atlas.  Every fibre has size at most `k`, and size
`k` occurs exactly when `n >= binom(k,2)`.

Crystal theory, RSK, Schur specialization, tableau and hook formulas, and the
general idea of a deterministic least/leftmost scheduler receive zero
contribution credit.  The residual is only the literal least-colour schedule
coupled to the clock and every-target fibre theorem. Defant--Williams crystal
pop-stack sorting is also zero-credit: its macrostep resolves the component
restricted to all starting descent colours, rather than taking one least
currently available raising edge. Round 0 and the accepted source repair make no novelty
or priority claim and authorize no external circulation.

## Exact replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The default complete word grid is `1 <= k <= 4`, `1 <= n <= 7`.  Independent
bounded-height involution checks run through `S_8`, and direct staircase-fibre
checks cover `1 <= k <= 9` with four nearby lengths.  The canonical terminal
fields are

```text
words=25384
assertions=618419
transition_digest=15eae7619f324f7730af7dddb103820cb72434ebf897ee8ec4fde1c611e8df49
status=PASS
```

The digest records literal transitions, reverse-RSK shapes, depths, complete
predicted fibres, involution shape data, and stable witnesses in deterministic
order.  Finite checks are counterexample pressure, not proof or ownership
evidence.

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

- `main.tex`, `references.bib`: anonymous standalone paper and verified
  zero-credit background bibliography;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`: story spine and frozen claim plan;
- `PROOF_PACKAGE.md`: theorem normalization, proof dependencies, and boundary
  audit;
- `CLAIMS_EVIDENCE.md`: claim-to-proof-to-falsifier ledger;
- `SOURCE_VERIFICATION.md`: source scope and internal collision firewall;
- `FIGURE_PLAN.md`: explicit no-figure decision and optional post-gate visual;
- `code/verify.py`, `code/CANONICAL.txt`: paper-local exact control and exact
  replay target;
- `BUILD.md`, `SELF_QA.md`: immutable Round-0 records plus the current
  source-repair build/addendum.

Posting, submission, and any other external release remain unauthorized.
