# Manuscript builds

`main.tex` is a conditional three-round manuscript. The checked-in
`main_round0.tex`, `main_round1.tex`, and `main_round2.tex` wrappers freeze
`\CRevisionRound`; the release builder compiles each wrapper twice in fresh
directories.

- `main_round0_original.pdf`: matrix radialization and invariant law.
- `main_round1.pdf`: adds exact killed/Doob kernel and no-collision theorem.
- `main_round2.pdf`: adds complete partition spectrum and Route-A closure.
- `main.pdf`: byte-identical to round 2.

The PDFs are release artifacts, not external submissions; the author line is
the candidate identifier rather than a personal identity.
Each round has a non-leaking English abstract, an independently written
Chinese abstract, and five to seven English and Chinese keywords. Chinese text
uses the embedded `Droid Sans Fallback` font, and page counts must increase by
round.
