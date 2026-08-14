# Compilation Report — Paper23 / SD-C25

**Artifact:** main.pdf  
**Final build date:** 2026-08-14  
**Engine:** pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022)  
**Bibliography:** BibTeX 0.99d with plainnat  
**Paper size:** A4, \(595.276\times841.89\) pt  
**Page count:** 21  
**File size:** 564,519 bytes
**SHA-256:** 38cc9ee9bbd76fedee168caa969d076510ed22416d0c00ac8132a23c3247a765

## Clean build sequence

All pre-existing build products were moved to a recoverable temporary
directory before the final sequence.  The final source was then built with:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

This is a four-pass LaTeX build with BibTeX between passes one and two.
The final two PDFs had identical size, and the final log was stable.

## Automated audit

- Final main.log: zero LaTeX/package warnings, zero overfull or underfull
  boxes, zero undefined references, and zero multiply-defined labels.
- Final main.blg: zero BibTeX warnings.
- Text extraction: no unresolved-reference marker or drafting placeholder.
- Fonts: every font reported by pdffonts is embedded, subsetted, and has a
  Unicode map.
- Metadata: title, subject, keywords, and anonymous author are present.
- PDF properties: unencrypted, no JavaScript, no suspicious form content,
  and A4 page geometry.

## Visual audit

Raster inspections were made at 110 dpi for:

- page 3, the ordered-word rigidity hero diagram;
- page 15, the memory/roof decision diagram and its surrounding proof;
- page 17, the strict Route-A table, theorem, tuple, and verdict.

The two figures are pure TikZ.  Node text, connectors, captions, equations,
table rules, and page margins are legible with no clipping or overlap.

## Scientific consistency audit

The compiled manuscript and source packages consistently distinguish:

1. the full block factor
   \(\det_{\mathbb C^d}(I-w_kBA^{k-1})\);
2. its first trace-log term
   \(w_k\operatorname{tr}(BA^{k-1})\);
3. the separately marked bilinear observable;
4. the separately assumed one-dimensional oracle deletion control.

They also freeze the Paper19/Paper20-only countable-wrapper scope, the
\(\mathbb F\)/\(\mathbb C\) algebraic–Hilbert firewall, cutoff \(N\), DFA
action direction, de Jong nonapplicability boundary, and the distinction
between theorem-level A3 failure and evaluation-level A4 failure.

## Integrated exact evidence

The manuscript reports the finalized 32/32 exact test result, 4,095-cycle
and 8,390,655-edge source census, the
\(\operatorname{tr}(P)=0\), \(\operatorname{tr}(P^2)=2\),
\(\det(I-wP)=1-w^2\) regression, and the byte-identical 31-artifact
double-run certificate.  These are presented as implementation audits, not
as substitutes for the infinite proofs.

## Cleanup

After this audit, auxiliary LaTeX products are moved out of the authority
directory.  The retained build artifacts are main.tex, the modular
sources, references.bib, the TikZ sources, and main.pdf.
