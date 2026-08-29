# Final QA

Status: passed for the post-cross-hostile internal refreeze on 29 August
2026; external release **HOLD**.

## Mathematical closure

- The forward composition convention is stated and guarded by a
  noncommuting two-map example and exact script sentinel.
- The interval/constant normal form includes equality cases and records only
  thresholds through time `n`.
- The distribution-free survival law is scoped to iid atomless thresholds
  independent of iid map types.
- Every formula conditional on `N_n=j` is restricted to cases with
  `P(N_n=j)>0`: all `j` for `0<p<1`, only `j=0` at `p=0`, and only `j=n`
  at `p=1`. The unconditional survival and diameter identities retain their
  full `0<=p<=1` scope.
- The pgf, geometric support convention, mass formula, mean, and variance
  agree algebraically and in exact rational controls.
- Critical, off-critical, and `p=0,1` endpoint statements were checked
  separately.
- The expected-diameter theorem is explicitly restricted to uniform
  thresholds. Its endpoint cases are proved separately from the minimum
  pure-cap and complementary-maximum pure-floor order statistics, without
  conditioning on null events.
- Pathwise finite absorption is not advertised as a conventional finite
  Lyapunov exponent; the signed annealed rate and positive decay exponent
  are separately defined.

## Exact control

Command:

```text
python3 code/verify_cap_floor.py
```

Result: PASS, **6,948,361 exact assertions**. The output was rerun after
each hostile-review repair and is stored verbatim in
`code/verify_cap_floor.out`. No random seed, floating point, third-party
package, or network dependency is present. The final count excludes 305
tautological diameter self-comparisons; the independent fixed-type rank-gap
lane, aggregate law lane, and endpoint lane remain registered.

## LaTeX and bibliography

The required four stages completed with exit status zero:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Final scans of `main.log` and `main.blg` found zero matches for `Warning`,
`Overfull`, `Underfull`, `undefined`, `multiply defined`, or `Error`.
All citations and cross-references resolve. The bibliography contains the
three sources cited in the manuscript, with DOI fields. The official record
for DOI `10.12958/adm1816` confirms the joint authorship of A. Umar and
M. M. Zubairu, now reproduced in the bibliography and owner-subtraction
language.

## PDF mechanics and visual inspection

- `pdfinfo`: five A4 pages, PDF 1.5, 305,010 bytes, unencrypted, no
  JavaScript, no creation-date metadata.
- `pdffonts`: every listed font is embedded and subsetted and has a Unicode
  map.
- `pdftotext -layout`: title, abstract, theorem/proof text, formulas,
  references, and HOLD statements are recoverable in reading order.
- Every page of the final refreeze was rendered independently to a 110-dpi
  PNG and inspected. An earlier 130-dpi repair render exposed a bare `quad`
  token in the endpoint display; the source was fixed, the full four-stage
  build was repeated, and the affected page was also rerendered at 150 dpi.
  The final PDF has no
  clipping, collision, blank page, anomalous margin, broken equation, or
  stranded heading. The theorem proof continuing from page 3 to page 4 is
  a clean sentence-level continuation.

## Scope, anonymity, and release gate

- Author is `Anonymous`; there are no acknowledgements, affiliations, or
  identifying metadata.
- Draft-token scan found no unfinished-work markers.
- Absolute novelty and priority claims are absent. Owner subtraction is
  explicit in the abstract, introduction, scope section, and evidence map.
- The independent internal cross-hostile result was `0 CRITICAL / 1 MAJOR /
  2 MINOR`; the null-event conditioning, incomplete source attribution, and
  tautological evidence-count findings are all closed in this refreeze.
- The artifact is GO only as an internal theorem-bearing short paper.
  External release remains HOLD pending specialist direct-owner review.

## Freeze

`SHA256SUMS` covers the manuscript source, bibliography, verifier and stored
output, all six evidence/QA documents, and `main.pdf`. A final
`sha256sum -c SHA256SUMS` verification is required and recorded as PASS at
handoff.
