# P214 ordinary article build plan — not executed

Status: `SOURCE_PLAN_ONLY / BUILD_GRANT_ABSENT / NO_PDF`.
The target is an anonymous 4–6 page article including references. Page count
and all visual conditions are unmeasured until a separately authorized build.

## Fixed local TeX inputs

main.tex, math_commands.tex, references.bib and the six sections:
0_abstract.tex, 1_setup.tex, 2_clock.tex, 3_fibres.tex, 4_controls.tex,
5_scope.tex. These are nine actual source inputs. main.tex requests
article[11pt], amsmath, amssymb, amsthm and bibliography style plain.
No conference class/style, extra font package, external image or generated
scientific table is required. The installed implementation of those tools,
classes, packages, bibliography style and fonts is still a build dependency;
their provenance is not established merely by naming them here.

## Prospective stages

After root accepts the complete source and separately authorizes a build,
the ordinary process would run a first pdfLaTeX pass, BibTeX on main, and
two resolving pdfLaTeX passes. Each pass must retain its complete log,
exit status and source-input evidence. No command in this note is an
executable authorization or a claim that an engine has been queried.

Before execution, root must choose and bind the actual source-only work
directory, interpreter/engine and resource policy, complete input pins,
reproducibility/environment settings, output capture and storage scope.
No shell-escape feature is requested. Do not copy a preexisting PDF or
auxiliary file into a source-only build to simulate a cold build.

After a successful authorized build, inspect all unresolved references and
citations, overfull/underfull and font diagnostics, embedding, page count
and actual rendered pages. A hash or image file's existence is not viewing.
The source draft currently has complete labels/citations by construction,
but only an actual build can verify their TeX resolution and layout.

This initial build plan does not replace the two physical source-only
terminal builds or final all-page viewing required after manuscript A/B.
No build, PDF, page count, diagnostics, rendering or viewing result is
supplied by this source package.
