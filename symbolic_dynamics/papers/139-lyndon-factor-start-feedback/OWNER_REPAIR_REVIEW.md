# Independent owner-repair review — P139 Round 3

**Review date:** 2026-09-01 UTC  
**Reviewer posture:** independent internal hostile reviewer; not an author of this manuscript  
**Scope:** finalized owner-repair delta only; source/evidence audit, attribution-boundary reconstruction, canonical verifier replay, isolated source-only build, PDF/hash preservation, and historical-round check  
**Disposition:** **PASS**  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, PDF, or evidence file was edited during
this review. The only paper-local output is this file.

## 1. Severity-indexed findings

### Critical

**C-R3-01 — controlling owner citation and zero-credit gate: PASS.**  
The missing controlling owner is now closed correctly. `references.bib` and
`main.bbl` contain the four-author journal citation

```text
Sabrina Mantaci, Antonio Restivo, Giovanna Rosone, Marinella Sciortino.
Suffix Array and Lyndon Factorization of a Text.
Journal of Discrete Algorithms 28 (2014), 2--8.
DOI 10.1016/j.jda.2014.06.001.
```

The manuscript now cites Mantaci et al. exactly at the first ownership
boundary in section 1 and labels the suffix-record proposition in section 2 as
`owned input`. The reproduced proof is explicitly marked background, and the
ordered-tail comparison is explicitly marked classical static machinery with
zero contribution credit.

**C-R3-02 — residual package narrowed correctly, with no surviving attribution overclaim: PASS.**  
I checked `main.tex`, `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`,
`CLAIMS_EVIDENCE.md`, `OWNER_REPAIR_LOG.md`, and `BUILD.md` against the owner
audit requirement. Everywhere the static suffix-record/factor-start theorem
and the ordered-tail comparison are treated as owned input, zero-credit
background, or integration-check material only. The residual package is stated
consistently as only:

1. the iterated start-mask dynamics with unique recurrent state `1^n`;
2. the sharp depth-`n` theorem with unique alternating source;
3. the ordered-Lyndon fibre atlas, including its matrix form and special cells
   after subtracting the classical binary Lyndon census and generic matrix
   multiplication.

I found no remaining place where the repaired package tries to reclaim the
static theorem as part of the paper's novelty.

### Major

**M-R3-01 — owner subtraction does not mask a mathematical gap: PASS.**  
The repaired draft still reconstructs coherently after subtracting the static
owner material.

- The leading-one amplifier remains self-contained: every leading `1` is a
  singleton Lyndon factor, so the leading-one prefix grows at every nonfixed
  step and forces the unique recurrent state `1^n`.
- The sharp-depth argument remains self-contained: the alternating word factors
  into `(01)^m` or `(01)^m0`, giving `L_n(a_n)=1a_{n-1}`, and the reverse
  uniqueness argument from the forced mask still pins down the unique deepest
  source.
- The fibre theorem remains self-contained: a target mask prescribes factor
  lengths, and CFL uniqueness gives a bijection with nonincreasing chains of
  binary Lyndon words of those lengths.

As an independent control, I ran a standalone brute-force checker that did not
import the paper-local verifier. It confirmed for every binary word up to
`n=8` that `1^n` is the only recurrent state, the maximum depth is exactly
`n`, the unique depth-`n` state is the alternating word, and the hostile
outside-image mask `10110` has empty fibre.

**M-R3-02 — canonical verifier replay and isolated repaired build: PASS.**  
The canonical verifier replay still matches the frozen transcript exactly:

```text
TOTAL_EXHAUSTIVE_STATES=524286
ORDERED_FIBRES_EXHAUSTIVE_THROUGH=14
SPECIAL_FIBRES_CHECKED_THROUGH=18
EXACT_ASSERTIONS=2654300
STATUS=PASS
```

An isolated build using only `main.tex` and `references.bib`
(`pdflatex -> bibtex -> pdflatex -> pdflatex`) produced a PDF byte-identical
to the working `main.pdf`. The first two passes had only the expected
transient unresolved-citation/cross-reference notices; the settled final pass
and BibTeX log were clean.

### Minor

**N-R3-01 — repaired PDF identity and historical-round preservation: PASS.**  
`main.pdf` and `main_round3.pdf` are byte-identical and share the same
SHA-256. `main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf`
remain byte-identical to one another and retain the pre-repair SHA-256
recorded in the repair log. The repaired PDF differs from `main_round2.pdf`,
which is the expected artifact effect of the owner-language repair.

Only `main_round0_original.pdf` and `main_round3.pdf` are currently mode
`0444`; `main_round1.pdf` and `main_round2.pdf` are mode `0644` but unchanged
bytewise. That is a preservation note, not a repair item under the stated
scope.

## 2. Hash ledger

```text
code/verify.py
01d10e3ffde5cfe675665e0cdfb1d2fc5e411c864ef83a82e93ca3d7d23e6b75

code/verification_output.txt
801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe

main.tex
97299a0a7b211a8434e3bf96612969d4cad8013796820181b2c723d3130e0af3

references.bib
1a5a5ff6b8c006bf797c258090ee2911af27d374c5d8d54a36213cf08ee6650f

main_round0_original.pdf
3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0

main_round1.pdf
3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0

main_round2.pdf
3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0

main.pdf
3c4b474a05290223a1ea70a050cab1b7b46043b0ca3c67f88327d9f71ceb76e3

main_round3.pdf
3c4b474a05290223a1ea70a050cab1b7b46043b0ca3c67f88327d9f71ceb76e3
```

## 3. QA record

- `cmp -s main.pdf main_round3.pdf`: identical
- `cmp -s main_round0_original.pdf main_round1.pdf`: identical
- `cmp -s main_round1.pdf main_round2.pdf`: identical
- `cmp -s main_round2.pdf main_round3.pdf`: different, as expected after the
  repair
- `stat` modes:

```text
444 main_round0_original.pdf
644 main_round1.pdf
644 main_round2.pdf
444 main_round3.pdf
```

- `pdfinfo main_round3.pdf`: 4 A4 pages, 326430 bytes, no metadata stream,
  no forms, no JavaScript, no encryption
- `pdffonts main_round3.pdf`: 25 font rows, all embedded and subsetted
- extracted text check: the abstract, section 1 owner gate, section 2 title,
  proposition label, and limitations section all reflect the narrowed
  zero-credit boundary

## 4. Repair disposition

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. No manuscript, source, or evidence-file change is
required by this review. Exact locations to change: none.

The finalized owner repair is internally coherent, preserves the intended
credit subtraction, introduces no new mathematical overclaim, preserves the
historical Round-0/1/2 artifacts bytewise, and keeps the package
**HOLD_EXTERNAL**.
