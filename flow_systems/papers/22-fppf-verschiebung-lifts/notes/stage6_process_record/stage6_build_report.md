# Paper 22 Stage-6 process-record build report

Date: **2026-08-26**

## Inputs and outputs

- Authoritative human-readable source: `paper_creation_process.md`
- Pandoc-generated LaTeX: `paper_creation_process.tex`
- Chinese PDF: `paper_creation_process_zh.pdf`
- Layout template: `process_record_template.tex`
- Deterministic post-conversion formatter: `format_generated_tex.pl`

## Toolchain substitution

The preferred Stage-6 toolchain (`tectonic` plus the prescribed CJK font) was
not installed. The first LuaLaTeX attempt with `ctexart` stopped because
`luatexja.sty` was unavailable. The successful local substitution used:

1. Pandoc Markdown-to-LaTeX conversion;
2. standard `article` class, LuaLaTeX, Babel's Chinese `onchar` font routing;
3. TeX Gyre Termes for Latin text and AR PL SungtiL GB / Droid Sans Fallback
   for Chinese glyphs;
4. three LuaLaTeX passes after line-break formatting for hashes and two-column
   tables.

Recorded versions: Pandoc `2.9.2.1`; LuaHBTeX/LuaLaTeX `1.14.0`
(TeX Live 2022/dev/Debian); Perl `5.32.1`; Poppler `pdfinfo 22.02.0`.
The resolved font files were `gbsn00lp.ttf` (AR PL SungtiL GB),
`DroidSansFallbackFull.ttf`, and `texgyretermes-regular.otf`.

## Exact successful command sequence

Run from this directory:

```sh
sed '1d' paper_creation_process.md | pandoc \
  -f markdown+tex_math_dollars -t latex \
  --shift-heading-level-by=-1 --template process_record_template.tex \
  -o paper_creation_process.tex
perl -0777 -i format_generated_tex.pl paper_creation_process.tex
lualatex -interaction=nonstopmode -halt-on-error paper_creation_process.tex
lualatex -interaction=nonstopmode -halt-on-error paper_creation_process.tex
lualatex -interaction=nonstopmode -halt-on-error paper_creation_process.tex
cp paper_creation_process.pdf paper_creation_process_zh.pdf
```

The stdout/stderr of the final pass is persisted as
`lualatex_final_stdout.txt`; the manifest binds that file, the template, and
the formatter by SHA-256. The first two pass transcripts are intentionally
ephemeral because the final pass and generated artifacts are the verification
surface.

This substitution changes only the Stage-6 process-record typesetting. It does
not touch the Stage-5 paper source, bibliography, or final paper PDF.

## Verification

- PDF: 14 physical pages (cover, contents, and 12 numbered body pages), A4,
  PDF 1.5, unencrypted.
- All listed PDF fonts are embedded and Unicode-mapped where applicable.
- Persisted final-output search: no `Overfull`, `Missing character`, `Fatal error`,
  `LaTeX Error`, or `Undefined control` match.
- Visual inspection sampled the cover, contents, deliverables, stage table,
  collaboration trajectory, and terminal page; no clipping or unreadable table
  was observed.
- At build time the stage state remained `in_progress`; successful compilation
  was not a terminal acknowledgement.  The later scholar event `确认完成 Paper
  22 Stage 6` and the resulting `completed` state are recorded separately in
  `stage6_completion_receipt.md`; the compiled process-record bytes were not
  changed afterward.
