# P211 source, fresh production, runtime and build plan

2026-09-08 UTC. **SOURCE_PREPARATION_ONLY / ROOT_INSPECTION_PENDING.**
No scientific run, canonical production, build or Round0 freeze is
authorized by this file. Root explicitly required this complete source
handoff before approving any of those actions. The unrelated readiness
desk at `docs/papers211_215_sequence/qa/runtime_readiness/PLAN.md` remains
PLAN_ONLY; its suggestions are not an executable approval.

## 1. Exact paper-local scientific inputs

The scientific source set is exactly `verify.py` and `parameters.json`.
There are no local mathematical helpers or imported pilot/review modules.
Direct stdlib roots are exactly `itertools`, `json`, `math`, `sys`.
Imports, a literal parameter dictionary and function definitions are the
only top-level work; mathematical enumeration is guarded by `main`.

The source/parameter interface is fixed in `PARAMETER_SPECIFICATION.md`;
complete output fields and ordering are fixed in `CANONICAL_SCHEMA.md`.
The theorem ceiling is `PROOF_PACKAGE.md` and `CLAIMS_EVIDENCE.md`.
No code here extends it to global fibre maxima or an increased cutoff.

The exact preparation handoff inventory includes all present paper-local
source/plan/proof/source-audit documents and saved source-read evidence.
Its complete nonself manifest is generated only after the sources are
stable, by hashing actual bytes, and is labelled a preparation seal, not
Round0 or a completed-paper seal. It will not be retroactively made to
cover outputs created later. The root must preserve these original source
bytes if later changes alter an already inspected preparation identity.

## 2. Fresh canonical production, separate from replay

The intended paper-local canonical destination is
`papers/211-kernel-image-projection-feedback/CANONICAL.json`.
It does not exist at this handoff. Only a separately recorded successful
initial production may create it exclusively from the complete native
stdout. The old exploratory pilot is neither a dependency nor a candidate
canonical. Its failed prelock and missing launcher environment stay
immutable in the old packet.

Science command template, whose capsule and fresh cache-prefix paths must
be made literal in the root-approved role binding before execution:

```text
/usr/bin/python3.10 -I -S -B -X pycache_prefix=<new-absent-science-prefix> <fresh-capsule>/verify.py --parameters <fresh-capsule>/parameters.json
```

The root-coordinated adapter owns its preparation/execution paths and
records them explicitly. The required science cwd is that fresh capsule.
It contains the registered source/parameter bytes and no old output,
bytecode or cached scientific result. The same immutable source and
parameters define production and both later author replay capsules.
No recorder-mode or production-mode argument is passed to the science.

Initial production records a distinct ATTEMPT before spawn; native
argv/cwd/environment, PID/session/group, start/end/deadline and return;
complete separated stdout/stderr; observer/runtime/input keys; group
settlement; source/capsule byte comparisons; and an actual outer native
return capturing launcher and recorder streams. Success requires the
exact complete output schema, all predicates, native exit 0 and empty
science stderr. Any failure remains a failed attempt, without canonical
adoption, silent retry or posthoc input repair. The initial canonical
bytes/hash and production receipt are not predicted by this plan.

Only after canonical adoption and the complete reuse key is frozen may
the author pair run: two separately recorded executions from fresh
source-only capsules, plus three actual raw comparisons (run1/canonical,
run2/canonical, run1/run2), with complete operand pins. Production and
pair are not the same attempt and are not conflated with a candidate pilot.

## 3. Runtime closure and recorder ownership

`/root/round211_rational_scout` is preparing runtime infrastructure only,
without reading or importing this mathematical implementation. Its
interface coordination is not a proof contribution or manuscript review.
Root must inspect the complete proposed adapter, baselines/diff,
dependency selector, exact role binding, schema checks and manifest.
There is no permission here to execute an uninspected adapter.

Required environment across the enclosing startup, launcher, recorder
and science is the root-approved explicit whitelist
`PATH=/usr/bin:/bin`, `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `TZ=UTC`.
Every process records and checks its actual settings, original argv,
cwd, interpreter/flags/import path/encoding/locale, and its own distinct
new absent `-X pycache_prefix`. `-I -S -B` and optimization zero are
required at each Python layer; `-B` alone does not disable reading caches.

The complete relevant dependency selection must be frozen before
science: every current role helper, source/parameter input, interpreter,
transitive imported Python source/native extension, resolved invoked
utility/library linkage, applicable loader configuration and exact
encoding/locale/gconv membership, plus relevant injection/zip/venv and
cache absence. It must cover all process layers under the same sanitized
startup environment, not only a child probe. In particular, inspect and
bind LC_CTYPE and gconv-modules.cache membership; two hard-coded hashes
alone would not establish complete closure. Import-only discovery may
not run the scientific main routine. The static direct-import list above
is not a claim that all transitive/runtime dependencies have been pinned.

Record before/after input/configuration keys and current capsule-copy
comparisons. Every observed external ordinary file must resolve to a
pre-frozen selected input. Unexpected files/settings cause failure; they
cannot be appended to an old pin list. Keep bounded Python-open and
sampled-map observations honestly labelled, not continuous startup/OS or
escaped-descendant tracing. Settle only the owned process group before
closing streams; unknown writers mean UNCLOSED, even if mathematical
stdout looks successful. Preserve actual original failure outcomes.

If bounded runtime closure is not established, readiness remains HOLD
until root decides the smallest required preparation change. The author
does not write any helper into old sealed desks or modify their receipts.

## 4. Exact TeX source/build design, not yet executed

Root owns a separate build preparation at
`docs/papers211_215_sequence/qa/p211_build_preparation`. The author does
not implement or run a builder. The final exact build environment is the
root-inspected P210-pattern ENV8 binding, without repurposing `HOME`;
the source/date settings below are proposals to be checked within that
binding, not a claim that the earlier six-variable proposal is final ENV8.

Build input files are exactly:

```text
main.tex
math_commands.tex
references.bib
sections/0_abstract.tex
sections/1_introduction.tex
sections/2_image.tex
sections/3_clock.tex
sections/4_inverse.tex
sections/5_scope.tex
```

Format is anonymous `amsart`, 11pt A4, standard T1/Latin Modern fonts,
27mm margins, `amsplain` bibliography, no external figures, no minted,
no shell escape and no project-local style file. The complete style/font/
engine dependencies still require the build's own reviewed provenance.
The Markdown/source-evidence/verification files are not TeX inputs.

Read-only executable lookup found `/usr/bin/pdflatex`, `/usr/bin/bibtex`,
`/usr/bin/pdfinfo`, `/usr/bin/pdftotext`, `/usr/bin/pdffonts` and
`/usr/bin/pdftoppm`. `latexmk` was not found. Therefore the proposed
paper-compile fallback is an explicit four-command build in one new
source-only build directory, each command independently recorded:

```text
/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
```

Proposed fixed date settings are `SOURCE_DATE_EPOCH=1788825600` and
`FORCE_SOURCE_DATE=1` within the root's final explicit ENV8. The main source
omits PDF dates/trailer ID and clears author metadata. Root must inspect
these actual engine/config/source dependencies before accepting any
build identity; their readiness is not asserted here. Never run
`latexmk -C`, clean away a failed build, or overwrite an old output tree.

Every build retains full native stdout/stderr, TeX/BibTeX logs, recorder
input list, engine/configuration/source pins, exit codes and output hashes.
Diagnostics are not required to be empty; unresolved references/citations,
errors, absent glyphs, overfull boxes and other warnings must be inspected
and reported. The next steps after a successful build are actual pdfinfo,
text/reference and font checks, then rendering and viewing every actual
page. A page-count prediction or PNG digest is not a visual review.
Neither a 100KB file threshold nor external conference page padding is
an acceptance rule for this internal mathematical short note.

## 5. Downstream gates and current stopping point

Only after root's source/runtime/production/build reception may physical
Round0 contain the correct current manuscript, actual canonical, proof,
parameters and actual PDF, with a complete nonself manifest. Exactly two
distinct nonauthor manuscript processes A and B follow the inherited
artifact-role contract. A's exact accepted delta precedes Round1; B uses
a materially different route on pinned Round1 and its accepted delta
precedes Round2. No author or later proof contributor self-reviews.

Fresh author/A/B exact replay pairs, two final physical source-only
builds, every-page viewing and final artifact/batch closure remain
obligations, not results of this preparation. All external actions remain
OWNER_AMBER / HOLD_EXTERNAL. This task hands the stable source plan to
root and stops before any scientific or build execution or Round0 freeze.
