# Build and verification

## Current frozen snapshot

- Workflow snapshot: official GPT-5.4/xhigh Round 2 package synchronization.
- Authoritative PDF: `main_gpt54_round2.pdf`; `main.pdf` is byte-identical.
- Result: 10 A4 pages, 371,616 bytes.
- SHA-256:
  `09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08`.
- Manuscript source was unchanged in Round 2; the deterministic PDF is also
  byte-identical to `main_gpt54_round1.pdf`.

## Requirements

- `python3` 3.10 or newer
- `pdflatex`
- `bibtex`
- standard TeX Live packages used by `amsart`, `natbib`, `booktabs`,
  `tabularx`, `microtype`, `hyperref`, and `cleveref`

## Re-run the finite controls

From the package directory:

```bash
python3 code/verify_surface_flat_sft.py
```

The final line must be `ALL CHECKS PASS`.  The output is a regression receipt,
not a proof premise.

## Compile the manuscript

```bash
export SOURCE_DATE_EPOCH=1787616000
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` was unavailable in the frozen environment, so the manual sequence
is authoritative.  The reproducibility settings in `main.tex` omit volatile
PDF dates and trailer identifiers.

## QA commands

```bash
pdftotext -layout main.pdf qa/final_text.txt
cp qa/final_text.txt qa/final_text.new.txt
pdfinfo main.pdf > qa/pdfinfo.txt
pdffonts main.pdf > qa/pdffonts.txt
python3 code/verify_surface_flat_sft.py > qa/control_replay.txt
diff -u code/verify_surface_flat_sft.out qa/control_replay.txt
rg -n -i '\bcha''ins?\b|子群''链|非定向''链|定向''链' . \
  --glob '!reviews/**' --glob '!*.pdf' --glob '!*.png'
rg -n -F '^{,' sections *.tex *.md code --glob '!qa/**'
rg -n 'Warning|undefined|multiply defined|Overfull|Underfull|Error' main.log
sha256sum -c SHA256SUMS
```

The three `rg` commands are zero-match gates, so exit status 1 from `rg` alone
means the check passed. Historical review files under `reviews/` are immutable
and intentionally excluded only from the terminology gate. `qa/final_text.txt`,
`qa/pdfinfo.txt`, `qa/pdffonts.txt`, `qa/control_replay.txt`, and the Round-2
visual receipt are current generated artifacts from the frozen PDF.

## Round-2 gate state

- Core mathematics: **PASS** (official Round-2 proof audit).
- Package-wide Round-2 synchronization: **PASS** after the recorded replay.
- Stage 2.5 specialist/collision review: **PENDING**.
- Specialist and priority clearance: **NOT GRANTED**.
- External release: **HOLD**.

The external-release status is **HOLD** even when all build and mathematical
checks pass.

## Stage 2.5 corrected artifact

Correction round 1 repaired the Klug pinpoint and integrated the located
lattice-TQFT, representation-zeta, and finite-group Markov-shift owners. No
theorem or proof was changed. The current canonical `main.pdf` is 11 A4
pages, 377,379 bytes, SHA-256
`93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766`.
The official-review PDFs remain historical pre-Stage-2.5 snapshots. The
source, citation, control, and deterministic rebuild receipt is
`stage2_5/CORRECTION_ROUND_1.md`. External release remains **HOLD**.
