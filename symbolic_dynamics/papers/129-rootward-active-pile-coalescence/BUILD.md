# Build record — P129 round 2

## Isolated build

- Date: 2026-08-31 UTC.
- Only `main.tex`, `math_commands.tex`, `references.bib`, and `sections/*.tex`
  were copied to a fresh `/tmp/p129-round1-final3-build.*` directory; no
  paper-directory auxiliary file entered the build.
- Required sequence:

  ```text
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  ```

- Result: **PASS** at all four stages.
- Settled LaTeX errors: 0.
- Undefined citations/references: 0.
- LaTeX/package warning messages: 0.
- Overfull/underfull boxes: 0.
- Bibliography: 8 cited entries; the three Review-A owner additions have
  visible DOI or arXiv locators.
- The isolated PDF, `main.pdf`, and `main_round1.pdf` are byte-identical.

## Round-one PDF

- Format: PDF 1.5, A4.
- Pages: 6.
- Bytes: 342,879.
- SHA-256:
  `5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2`.
- `main.pdf` and `main_round1.pdf` are byte-identical.
- PDF metadata title, author, subject, and keywords are blank; date and
  trailer identifiers are suppressed.
- No metadata stream, form, JavaScript, or encryption is present.
- All 25 listed font entries are embedded, subsetted, and Unicode-mapped.
- All six pages were rasterized and inspected.  The repaired optional-
  stopping proof, equation (16), bibliography, and `PILOT_ONLY` exclusion
  render cleanly; there is no clipping, collision, missing glyph, or orphan
  heading.

## Preserved round zero

- `main_round0_original.pdf` remains unchanged at 330,389 bytes.
- Its SHA-256 remains
  `404b21a8beb9f9691326262544fc797cd1b62bf69b36ad2b5b65f693495dc05d`.
- It is intentionally distinct from round one.

## Repaired-source hashes

```text
main.tex                  6f187199a00764f23faf40cf8efec56dfb989cdf4771ee5a3316f7b631d111dd
math_commands.tex         4994d5e68b4c06585fe2fc358808303a02621b6ee6ffae1af0e609cbb9632b6d
references.bib            e39d4fba872c07b352c754dbcba8f32e6f66482774aeac28b6f074c56e98f42f
sections/0_abstract.tex   e0f736febc69ac58028c69be0a9abdae2f4041fd5f949022fc77eb9bcc36b2f6
sections/1_model.tex      d6c87de197fb5c28f94ab6afdf79e4231f0257b9b94dd81b875da0e03fbb5108
sections/2_finite_law.tex f92e80a450164d4903f8c512e1d8d7d303e86cb2801793e9c1c13882e0f3fdd4
sections/3_interfaces.tex 20c0e6e0a0329b5e0ffed4d70fb5aee771ebd26f481116fe2f5c26a2f040bbf9
sections/4_ballot.tex      015b5be981210ba803c7bb6c49476d0e148160beedf5774db0f036c7e8527745
sections/5_control.tex     7f5098942961c3bc4c33bb4ae148607ce935f29d359c2a7a90413d5c01d97ce9
sections/6_conclusion.tex  0677d753788611b041329d141fa5273f43b3d5419c8db8af0a99899238e79d2d
```

Independent Review B reproduced the same six-page PDF, canonical verifier,
8/8 bibliography, 25/25 font audit, anonymous metadata, and all-page visual
check with zero blocking finding.  `main_round2.pdf` is byte-identical to
`main_round1.pdf` and `main.pdf`, SHA-256
`5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2`.
It is not an external release artifact; `HOLD_EXTERNAL` remains binding.

## Paper-local final QA

Final QA on 2026-08-31 UTC reran the canonical verifier and obtained a
byte-identical 477-byte transcript with **506,663 assertions**.  A fresh
isolated four-stage build from `main.tex`, `math_commands.tex`,
`references.bib`, and `sections/*.tex` reproduced `main.pdf` byte for byte;
its settled log and BLG have no error, warning, undefined item, bad box, or
actionable rerun request, and all 8 bibliography items close.

The final `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` remain
byte-identical at 6 A4 pages and 342,879 bytes.  The reviewed PDF hash is
unchanged, so the all-page visual, 25-font, and anonymous-metadata evidence
from the two independent reviews applies exactly to the frozen artifact.
`FINAL_QA.md` records the terminal checks and `SHA256SUMS` freezes the
paper-local package.  Internal status is `GO_INTERNAL`; external status is
`HOLD_EXTERNAL`.
