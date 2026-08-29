# Principal-hook regrouping dynamics on integer partitions

Anonymous compact `amsart` note for the self-map that sends an integer
partition to its partition of principal diagonal-hook lengths.

Status: **internal draft**. External dissemination, novelty, and priority are
all **HOLD**. A bounded owner search is collision control only; a missing hit
is not originality evidence.

## Result hierarchy

The paper has one main theorem:

- for `g(lambda)=lambda_1-lambda_2` (with terminal one-row padding), the exact
  increment is `2+m_1(lambda)` in Durfee size at least two and `b+1` for a
  nonterminal hook `(a,1^b)`;
- consequently
  `tau(lambda) <= floor((n-g(lambda))/2) <= floor(n/2)`;
- the maximum is exactly `floor(n/2)`. For `n>=2`, the balanced two-row state
  uses `(a,b) -> (a+1,b-1)` `b-1` times, followed by the final hook step
  `(n-1,1) -> (n)`, for `b=floor(n/2)` total steps. At `n=1`, `(1)` is
  already terminal.

Everything else is explicitly an owned input or a low-credit corollary:

- the owned first-hook identity implies that `(n)` is a globally absorbing
  fixed point (defined as finite-time capture of every state), the unique
  fixed point, and the unique periodic point;
- the owned fibre weights give a depth-state-weighted layer transport
  identity, not a closed scalar recurrence in `A_t(n)` alone;
- `H(lambda)=H(lambda')`, with the sole entrance-time exception
  `(n),(1^n)` for `n>1`;
- for each fixed `n>=1`, `#Fix(H_n^m)=1`, so
  `zeta_{H_n}(z)=(1-z)^(-1)`. No all-weights zeta is asserted.

## Itemized ownership subtraction

The following facts receive zero credit:

1. **Gutschwager:** the principal-hook length partition as a standard object
   and the identity `hl_1(lambda)=lambda_1+ell(lambda)-1`.
2. **Goupil:** the adjacent-gap one-step image and the exact fibre product
   `h_r * product_i(h_i-h_{i+1}-1)`.
3. **Chern--Yee:** prior diagonal-hook data and an involution preserving all
   diagonal-hook lengths; standard one-step diagonal-hook symmetries are not
   counted as temporal credit.
4. **Andrews and standard partition theory:** Ferrers, Durfee, and Frobenius
   setup.

The owned image/fibre result is reproved only so the low-credit layer
transport can be checked without an external lemma.

## P110 firewall

P113 uses unlabelled integer partitions, Ferrers diagrams, and diagonal-hook
regrouping. P110 uses labelled set partitions of a cyclic set and a
shift-join operation in the set-partition lattice. No cyclic action, lattice
join, Bell-number basin, or Möbius-lattice engine is imported here.

## Reproduction

From this directory:

```bash
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The verifier uses only the Python standard library, exhausts every partition
of every `n` from 1 through 40, and reports **10,110,035 exact assertions**.
Its committed transcript is `code/verification_output.txt`.

The LaTeX source uses T1 encoding, Latin Modern fonts, and pdfTeX metadata
controls (`\pdfinfoomitdate`, an empty trailer ID, and suppressed pTeX info)
for a deterministic author-stage PDF.

## Files

- `main.tex`, `references.bib`: manuscript sources.
- `main.pdf`: compiled draft.
- `PAPER_PLAN.md`: theorem contracts and section plan.
- `NARRATIVE_REPORT.md`: result-level narrative.
- `CLAIMS_EVIDENCE.md`: claim/proof/computation/ownership ledger.
- `CONTROL_RESULTS.md`: exact verification and killed-overclaim record.
- `BUILD.md`: deterministic build and diagnostic record.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`: independent review inputs.
- `HOSTILE_REVIEW.md`: repair-resolution ledger; not a final-QA artifact.
- `code/verify.py`, `code/verification_output.txt`: executable controls and
  stored output.
