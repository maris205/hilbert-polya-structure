# Publication-Stage Scope

## Authority and present lifecycle

This document governs the transition from the frozen Paper 15 source package
and independently passed paper plan to a possible anonymous proof-first
manuscript. It is a governance artifact, not a manuscript, bibliography,
build, manuscript review, revision, finalization, or release.

The current state is exactly:

**PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW / NO_DRAFT / NO_BUILD / NO_RELEASE**

The candidate identifier is **henon_quartic_trace_fibers_v1**. The public
title is exactly:

**Low-Period Trace Fibers of Quartic Generalized Hénon Maps**

The governance freeze date is 2026-08-17 UTC. The present authority consists
of this scope together with `experiments/publication_lock.json`. Earlier
source-design, source-lock, and paper-plan statuses are bound provenance; none
of them independently authorizes a downstream artifact.

## Frozen-input gate

Before either governance artifact was written, the publication-stage author
rehashed all fifteen existing project files. Every observed path, byte count,
line count, and SHA-256 identity matched the stable pre-governance snapshot.

| Frozen input | Bytes | LF lines | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 8,354 | 375 | `c30436a0389c88df8f51fe6e226347bfe108aa84b5032841ec0033ffa7a987fb` |
| `experiments/EXPERIMENT_TRACKER.md` | 2,955 | 71 | `d0e46a2c9a691c33e6f6e523f85367f00e8060c124044e2f011016c0a68f9efb` |
| `experiments/source_lock.json` | 26,920 | 1 | `802fc883cde85cd6312e8a31e0728dc01b493c640c8918d9eacc497f44cac7be` |
| `notes/CITATION_VERIFICATION.md` | 13,630 | 339 | `d84f4b523a7fee3e8f5fa8f2c4c898dbf62e3fd9528154fdd991d82c150c3609` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 9,343 | 125 | `928f0923bbfddd9294508a427bfcbcbd259591cac4c136bd4effb15bd86ed109` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 13,961 | 227 | `ce2f6ba64b971d26b2ed472d2417c018461632cb1d54d6db53004f25b2d435ac` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12,529 | 228 | `55789c4a7c62e4577b655399e7fe8247fe641381e50876d6ebad9bce1f0e8b6e` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 12,014 | 211 | `39ef31d1dac337fe9856fd9d8f40f756b30730a683db43c1d9b7e183236c6f63` |
| `notes/NOVELTY_ASSESSMENT.md` | 9,878 | 251 | `c0b7a102d0d63dcb71d58bdbe460e59988fbf303a10f540a0221275fd34c5eb2` |
| `notes/PROOF_PACKAGE.md` | 29,436 | 1,347 | `f99d14bc18bd160e5d55e6254e4a2957dda40adbc2a680970506a6ecca5a42ed` |
| `notes/RESEARCH_QUESTION.md` | 8,641 | 293 | `a287da2bebfa89b02dd7a83d13129e442b51d5780ccbc01c90eca93ad169e082` |
| `paper/PAPER_PLAN.md` | 45,894 | 739 | `1b70ec0c37d9d587aa56b97b175c6da2f44e114d9414bf31c9f70534dd209e08` |
| `refine-logs/FINAL_PROPOSAL.md` | 9,331 | 395 | `97daded29a79a1b19b828c4704187fa9c70bdac7448382a72b1df8c0f773ab21` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,842 | 178 | `043ca69894386ab5040099138780cc6801ba39ff0b088a2ba3f274ef263cb1a0` |
| `refine-logs/REVIEW_SUMMARY.md` | 7,112 | 202 | `ab479b99e6fbf1b8f66b719df01d8abfbc97da30a8feb1c0fb1b77bab16ac0bb` |

The source-lock review ends with the exact verdict **SOURCE_LOCK_PASS**. The
paper-plan review ends with the exact verdict **PAPER_PLAN_PASS**. These
verdicts establish provenance and eligibility only.

## Current authorization state

At governance freeze, every downstream authorization is false.

| Authorization | Current value |
|---|---|
| anonymous manuscript drafting | false |
| bibliography authoring | false |
| build or compilation | false |
| code or scientific execution | false |
| experiment or result | false |
| figure or external asset | false |
| manuscript review | false |
| source revision | false |
| finalization or `paper/main.pdf` | false |
| identity disclosure | false |
| submission or upload | false |
| public release or external messaging | false |

The independent publication-stage review below is the sole permitted next
project write. Freezing this governance pair is not permission to draft or
build.

## Exact theorem and contribution lock

The manuscript must present one dependent theorem package, not a naked-cutoff
note. For

\[
f_{a,p}(x,y)=(ay+p(x),x),
\]

with (p) monic centered, the public proof chain is

\[
\operatorname{Trace}_1
\Longrightarrow
\text{finitely many Jacobian candidates}
\Longrightarrow
\text{the exact lower exceptional curve }E
\Longrightarrow
\operatorname{Trace}_3\text{ separates }L^3
\Longrightarrow
P_{\mathcal H^1}(4)=3.
\]

The unified theorem has exactly three dependent parts.

1. **Part A: pure fixed-trace Jacobian bound.** Over an algebraically closed
   field (k) of characteristic zero, for (d\ge2), set
   \[
   s=1-a,\qquad q=p-sx,\qquad
   C_f(T)=\det\!\left(T-M_{p'}\mid k[x]/(q)\right).
   \]
   Pure formal fixed traces determine (C_f), and (C_f'(s)=0). A fixed
   trace multiset therefore leaves at most (d-1) Jacobians and at most
   three in degree four. The Jacobian is an output candidate, never an
   input.
2. **Part B: exact period-at-most-two failure locus.** Over (mathbb C), on
   the single-factor monic-centered space (mathcal H^1_4), the exact
   non-quasi-finite locus of (mathfrak T_{\le2}) is
   \[
   E=\{a=1,\ p(x)=(x^2-L)^2:L\in\mathbb C\}.
   \]
   Its lower trace data is
   (operatorname{Trace}_1=0^{\times4}) and
   (operatorname{Trace}_2=2^{\times12}), and the finite residual quotient
   is (E/\mu_3\simeq\mathbb A^1_{L^3}).
3. **Part C: sharp period-three cutoff.** Over (mathbb C),
   (mathfrak T_{\le3}) is quasi-finite on (mathcal H^1_4) and on its
   finite residual quotient (mathcal M^1_4), while
   (mathfrak T_{\le2}) is not. On (E), the pointwise formal-period-three
   second power sum is
   \[
   -1296000-1572864L^3.
   \]
   The cyclewise value, only after formal subtraction and division by three,
   is (-432000-524288L^3). Thus the sharp pure formal-trace quasi-finite
   cutoff on this normalized single-factor quartic space is three.

The manuscript must credit Cantat--Dujardin immediately for the already known
exceptional family, its period-one/two blindness, general trace rigidity, and
existence of an unspecified finite cutoff. The contribution is the full
dependent chain above.

## Formal-cycle and proof-visibility lock

Every (operatorname{Trace}_n) is the trace multiset on the formal-period-
(n) zero-cycle in the Cantat--Dujardin convention, with scheme-theoretic
multiplicity. The quartic formal lengths are exactly (4,12,60). Symmetric
products must be modeled by elementary symmetric coordinates, and the
conclusion is quasi-finiteness of a finite-type morphism rather than
injectivity.

The mathematical content must retain the complete proof spine.

1. Derive the fixed algebra (k[x]/(p-(1-a)x)) and identify pure fixed
   traces with the characteristic polynomial of multiplication by (p').
2. Prove (C_f'(s)=0) both by the squarefree residue identity and by the
   nonreduced local factor ((T-s)^m); division by (C_f(s)) is forbidden
   in the nonreduced case.
3. Enumerate Jacobians before invoking Cantat--Dujardin Theorem 4.2, and use
   that theorem only over (mathbb C), at fixed Jacobian, with (a\ne1).
4. On (a=1), prove the length-(16) period-two tensor algebra, subtract the
   embedded length-(4) formal fixed cycle scheme-theoretically, and obtain
   formal length (12).
5. Treat all five root partitions ([1111]), ([31]), ([211]), ([22]),
   and ([4]). Sugiyama is permitted only on ([1111]); the other strata,
   all ordering choices, and every boundary are direct proofs.
6. Prove that ([22]\cup[4]) is exactly (E), including the argument from
   (C_f(T)=T^4) that excludes an unseen (a\ne1) component of the common
   lower fiber.
7. For period three, retain rank (64), the cyclic signs, equality of the
   complete-intersection Jacobian with (operatorname{tr}(Df^3)), and the
   exact exponent (operatorname{Tr}(M_{t^2})=operatorname{Res}(t^3)).
8. Prove the two-term support, both independent slope certificates giving
   (-1572864), and the terminating constant ledger giving (-1296000).
9. On the fixed algebra prove the required nilpotence, perform the local
   elimination at multiplicities two and four, subtract length (4) from
   length (64), and divide by three only after the pointwise length (60)
   is established.
10. Separate the two global fiber cases, use the period-three moment only on
    (E), then apply the finite-type finite-fiber criterion and the direct
    finite-quotient argument.

No theorem may be represented by a proof sketch alone. Appendices may expand
finite coefficient ledgers and local substitutions, but every hypothesis and
logical implication needed for Parts A--C must remain in the main content.

## Citation, novelty, and anti-claim lock

Bibliographic metadata must come from the verified primary records bound by
the frozen citation ledger. The controlling Cantat--Dujardin text is the
51-page author PDF dated 2026-05-10, not the earlier byte-distinct arXiv v1.
Its Theorem 3.7 supplies no explicit quartic cutoff; Theorem 4.2 retains its
complex, fixed-Jacobian, (a\ne1) scope; Example 4.3 supplies the known
exceptional curve and lower-period blindness. Sugiyama applies only on the
no-multiple-fixed-point ([1111]) stratum. Friedland--Milnor,
Cattani--Dickenstein--Sturmfels, Hutz, Huguin, and Stacks Tag 02NH retain only
their frozen roles.

The article may describe a bounded primary-source search through 2026-08-17.
It may not claim absolute priority, a first result, a newly discovered
exceptional family, or absence of unpublished work. The following fourteen
anti-claims are mandatory.

1. The Jacobian is not supplied to the pure trace map.
2. The conclusion is not injectivity, global uniqueness, generic degree one,
   or an exact fiber-cardinality statement.
3. No exact map degree, branch divisor, or generic degree is determined.
4. The global theorem covers neither compositions, arbitrary loxodromic
   automorphisms, unnormalized spaces, nor multifactored moduli.
5. Parts B and C are not widened beyond (mathbb C).
6. No positive-characteristic analogue is claimed.
7. Reduced periodic points cannot replace formal-period zero-cycles.
8. Cantat--Dujardin's general rigidity, unspecified cutoff, exceptional
   family, and lower-period blindness are not new here.
9. Classical residue identities, formal dynatomic methods, generalized Hénon
   normal forms, Sugiyama, Huguin, or fixed-point identities are not claimed
   as new methods.
10. The absorbed exceptional-curve classification, subtraction, coefficient
    ledgers, and period-three moment receive no renewed novelty credit.
11. No all-degree cutoff, statement (P(d)=3), effective universal cutoff,
    or universal coefficient nonvanishing is claimed.
12. The period-three second power sum is not a global classifier of
    (mathcal H^1_4); it is used only after the lower fiber is proved to be
    (E).
13. No computation, CAS run, scan, experiment, or numerical check is theorem
    evidence.
14. The article makes no absolute priority or unpublished-work absence claim.

## Paper 12 absorption and public disclosure

The unified Paper 15 article must reproduce and absorb all overlapping
Paper 12 theorem and proof material. Paper 12 is internal provenance, not a
black-box citation and not a parallel external vehicle. The two overlapping
central claims may not be submitted separately.

The public article must express this substantive disclosure without exposing
an internal project number, path, hash, or lifecycle label. Section 8 must
state that the exceptional-curve theorem and calculation in the article
supersede and absorb an earlier non-public development manuscript, that the
earlier artifact receives no separate novelty claim, and that it will not be
submitted in parallel. No public citation may be fabricated for the non-public
artifact. This public-safe wording satisfies the mandatory Paper 12/Paper 15
overlap disclosure while keeping operational metadata out of the article.

## Article format, page, evidence, and visual lock

The manuscript is a standard anonymous proof-first article in complex and
algebraic dynamics, not an ML-conference submission. The title must match the
exact title above. There are exactly eight numbered main sections, with
Section 8 containing limitations, the public-safe overlap disclosure, and the
conclusion, followed by references and exactly five proof appendices A--E.

The mathematical-content count begins on the first PDF page and ends at the
end of Section 8. It must be 24--26 pages inclusive. References and all five
appendices are excluded from that count. A page break must separate Section 8
from the references, and another must separate references from Appendix A, so
the count is auditable. There is no hard total-page cap, because proof
completeness controls. Every PDF page must contain non-whitespace public text
or mathematical content; blank pages are forbidden.

There are zero figures, figure environments, image files, included graphics,
external assets, experiments, datasets, scans, numerical results, empirical
tables, or computational evidence. The figure-generation phase is
intentionally vacuous and closed.

At most one `table` environment may appear, and only as an in-source
five-stratum mathematical roadmap. If used, its caption must have the
substance:

> The five centered quartic root strata. This roadmap records
> parameterizations and proof locations; the complete finiteness and boundary
> arguments are given in Section 5.

The table is non-evidentiary, contains no generated data, and cannot replace
any formula or proof paragraph. Exact coefficient certificates may be
typeset as aligned equations or mathematical arrays, but no second table
float is authorized.

The two public source files and the PDF's public text must contain no local
filesystem path, hash, internal candidate identifier, governance status,
review verdict, agent name, operational instruction, or other lifecycle
jargon. They must also contain no author name, affiliation, email address,
acknowledgment, grant number, repository identity, submission identifier, or
self-identifying link. Public mathematical citations remain neutral.

## Independent publication-stage review gate

The sole next project write is exactly:

`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`

The reviewer must be fresh and independent. The reviewer must have authored
or modified none of the fifteen frozen inputs, neither governance artifact,
and no future manuscript source. The governance author cannot review or sign
its own work.

After an explicit governance-author stop with stable identities, the reviewer
may read only the seventeen governance-stage paths. Before that stop it may
not open, list, stat, or inventory either governance path. It must rehash all
fifteen inputs and both governance artifacts, validate the lock's strict
canonical round trip with duplicate-key and nonfinite-number rejection, bind
the scope by hash/bytes/lines, verify exact inventory and every future
absence, and replay the theorem, proof, citation, page, public-text,
anonymity, role, build, review-chain, cleanup, and lifecycle contracts.

Any mismatch, ambiguity, independence failure, or blocker has disposition
**WRITE NOTHING**. Only if every conjunctive check passes may the reviewer
create its sole review file. Its last nonempty line must be exactly:

**PUBLICATION_STAGE_PASS**

No heading, prose, or approximate wording substitutes for the exact final-line
verdict. A missing review or any other final line leaves every downstream
authorization false. A passing review activates only the anonymous two-file
manuscript-author stage; no build is activated by the review itself.

## Exact stage path universes and role contracts

Let (F) be exactly the fifteen paths in the frozen-input table. Define the
successive exact project path universes:

\[
\begin{aligned}
U_G&=F\cup\{\texttt{notes/PUBLICATION_STAGE_SCOPE.md},
\texttt{experiments/publication_lock.json}\},\\
U_P&=U_G\cup\{\texttt{notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md}\},\\
U_D&=U_P\cup\{\texttt{paper/main.tex},
\texttt{paper/references.bib}\},\\
U_{R0}&=U_D\cup\{\texttt{paper/main_round0.pdf},
\texttt{paper/BUILD_RECEIPT_R0.json}\},\\
U_{V1}&=U_{R0}\cup\{\texttt{notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md}\},\\
U_{S1}&=U_{V1}\cup\{\texttt{paper/SOURCE_REVISION_RECEIPT_R1.json}\},\\
U_{R1}&=U_{S1}\cup\{\texttt{paper/main_round1.pdf},
\texttt{paper/BUILD_RECEIPT_R1.json}\},\\
U_{V2}&=U_{R1}\cup\{\texttt{notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md}\}.
\end{aligned}
\]

Their exact regular-file counts are respectively (17,18,20,22,23,24,26,
27). At every stage the only project directories are `experiments`, `notes`,
`paper`, and `refine-logs`, and the symlink count is zero. A stage may begin
only when its predecessor's exact path universe and required stable identities
hold and every later path is absent.

The roles have exact read and write universes.

| Role | Activation | Exact read universe | Exact project write universe |
|---|---|---|---|
| publication-stage author | present governance task | (F) | scope and publication lock only |
| independent publication reviewer | stable governance-author stop | (U_G) | publication-stage review only |
| anonymous manuscript author | exact final-line `PUBLICATION_STAGE_PASS` | (U_P) | `paper/main.tex`; `paper/references.bib` |
| Round-0 builder | stable manuscript-author stop and exact (U_D) | (U_D) | `paper/main_round0.pdf`; `paper/BUILD_RECEIPT_R0.json` |
| fresh Round-1 reviewer | stable Round-0 builder stop and exact (U_{R0}) | (U_{R0}) | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` |
| bounded revision author | stable Round-1 review and exact (U_{V1}) | (U_{V1}) | `paper/main.tex`; `paper/references.bib`; `paper/SOURCE_REVISION_RECEIPT_R1.json` |
| Round-1 builder | stable revision stop and exact (U_{S1}) | (U_{S1}) | `paper/main_round1.pdf`; `paper/BUILD_RECEIPT_R1.json` |
| fresh Round-2 reviewer | stable Round-1 builder stop and exact (U_{R1}) | (U_{R1}) | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` |

Each read universe is the complete allowlist; a role may not read a later
artifact before its stage. Each write universe is exact and cannot be
expanded. Reviewers author none of the objects they review. Builders do not
edit sources or issue review verdicts. No role may self-sign a gate.

## Anonymous manuscript-author contract

Only after the exact publication-stage pass may one manuscript author write
exactly `paper/main.tex` and `paper/references.bib`. The author may not compile,
access the network, install anything, run code, CAS, symbolic engines,
scientific calculations, parameter scans, or generate data. It may not read
any future build, review, or revision artifact.

The manuscript must:

- use a standard self-contained anonymous `article` layout, with no venue
  style and no shell escape;
- put all eight sections, five appendices, proof arrays, and any single
  allowed table in `paper/main.tex`;
- include only verified, actually cited bibliography entries in
  `paper/references.bib`;
- create no `sections/`, `math_commands.tex`, `figures/`, style file,
  external asset, supplementary source, code, data, or result;
- preserve Parts A--C, all field and normalized-space limits, the formal-cycle
  convention, fourteen anti-claims, exact proof visibility, and public-safe
  Paper 12 absorption disclosure;
- contain no empirical claim or unsupported priority language; and
- include deterministic pdfTeX-compatible controls that suppress dates,
  identity-bearing metadata, and the trailer identifier without disclosing
  internal governance in public text.

The author must verify, without compiling, that exactly the two authorized
paths were added, report stable SHA-256 and byte counts for both, and stop.
That stop activates no build by itself; the Round-0 builder must independently
verify the exact (U_D) precondition.

## Round-0 isolated deterministic build protocol

Round-0 building begins only after the stable source stop and an exact
preflight of (U_D). It performs exactly two clean builds in two distinct,
new, empty, non-symlink directories created with the literal template:

`/tmp/p15-paper15-r0-XXXXXXXX`

Each resolved directory must match
`^/tmp/p15-paper15-r0-[A-Za-z0-9]{8}$`, have `/tmp` as its resolved parent,
be owned by the builder, and contain no entry before the two exact source-byte
copies are placed there. Reusing a directory or selecting a path outside this
pattern is a blocker.

The builder must resolve one absolute `pdflatex` and one absolute `bibtex`
executable before both runs, record each executable's SHA-256 and complete
version text, and use the same two identities in both runs. The environment
for every build command is exactly:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786924800
    FORCE_SOURCE_DATE=1

In each clean root, run exactly and in order:

    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight exit codes must be zero. The builder may not edit source, access the
network, install a package, invoke a rasterizer, execute scientific code or
CAS, use shell escape, or read an undeclared project path. In each temporary
root the only allowed paths are `main.tex`, `references.bib`, `main.aux`,
`main.bbl`, `main.blg`, `main.log`, optional `main.out`, optional `main.toc`,
and `main.pdf`. Every entry must be a regular non-symlink file.

The two `main.pdf` files must be identical in bytes, SHA-256, and byte count;
the two `main.bbl` files must also be byte-identical. A mismatch fails the
round and cannot be resolved by selecting one output.

## Build content and PDF validation contract

Before persistence in either round, both builds must satisfy every check:

- zero TeX, LaTeX, and BibTeX errors;
- zero undefined references and zero undefined citations;
- zero unresolved TODO, FIXME, XXX, VERIFY, placeholder, drafting, or repair
  marker;
- every log warning enumerated; a warning fails unless it is explicitly
  classified as cosmetic, source-independent, incapable of affecting
  mathematics, layout, citations, fonts, anonymity, or reproducibility, and
  accepted by the later independent reviewer;
- zero missing glyphs, missing characters, missing fonts, and overfull boxes;
- every PDF font embedded, subset, and equipped with a Unicode map;
- the exact title, anonymous author presentation, eight main sections,
  references, and appendices A--E;
- 24--26 mathematical-content pages through the end of Section 8, excluding
  references and all appendices, with every page nonempty;
- no image XObject, raster or vector image, attachment, embedded file, form,
  XFA object, JavaScript, launch action, rich-media object, or file annotation;
- anonymous metadata, with no author identity, creation date, modification
  date, submission identifier, local path, or trailer ID; generic producer
  and creator tool names are permitted only when identity-free;
- public source and extracted PDF text free of local paths, hashes, internal
  candidate identifiers, governance labels, verdicts, acknowledgments,
  grants, repositories, and identity-bearing text;
- exact set equality among citation keys used by `main.tex`, entry keys in
  `references.bib`, and `\bibitem` keys in `main.bbl`, with no duplicate key,
  wildcard `\nocite`, uncited entry, or missing entry;
- zero figure environment, `\includegraphics`, image file, external asset,
  empirical claim, or empirical table; and
- at most the one authorized non-evidentiary five-stratum table with the safe
  caption role above, never as a proof substitute.

Checks must use non-raster tools and record their absolute executable paths,
hashes, and versions when their outputs enter a receipt. The source and PDF
must agree on theorem statements, formal lengths, exact coefficients,
limitations, citations, and the overlap disclosure.

## Round-0 persistence and receipt

Only after both clean builds and every validation pass may the Round-0 builder
persist exactly:

- `paper/main_round0.pdf`
- `paper/BUILD_RECEIPT_R0.json`

No `paper/main.pdf`, auxiliary, log, transcript, cache, temporary directory,
or other project artifact may remain. The persisted PDF must be an exact byte
copy of both clean-run PDFs.

`BUILD_RECEIPT_R0.json` must be strict compact canonical JSON: UTF-8, keys
recursively sorted by Unicode code point, no insignificant whitespace, no
duplicate key, no nonfinite number, no carriage return, and exactly one
terminal LF. Its own SHA-256 and byte count are excluded. It must bind:

- all governance and publication-review identities;
- both source paths, hashes, and byte counts before and after building;
- exact temporary-root paths and validation of their pattern, ownership,
  distinctness, emptiness, and non-symlink status;
- build and validation executable paths, executable hashes, and full versions;
- the exact environment and command sequence, all eight exit codes, and
  per-command transcript hashes and byte counts;
- per-run PDF, `main.bbl`, final log, and combined-transcript hashes and bytes;
- PDF and BBL byte-identity booleans;
- every error, warning, undefined-reference, undefined-citation, glyph,
  font, overfull-box, page, nonempty-page, metadata, security, public-text,
  citation-set, table, figure, and external-access check;
- the exact persisted PDF hash and byte count;
- the prewrite and postwrite exact project path universes; and
- explicit temporary cleanup and post-cleanup absence checks.

After all receipt facts needed from a temporary root have been captured, the
builder must validate that the root contains only the allowed regular files,
unlink those files one by one by resolved explicit path, and remove the now
empty root with `rmdir`. Recursive deletion, unresolved variables, globs, and
symlink traversal are forbidden. Both roots must be verified absent before
the builder stops. If validation or cleanup fails, no project output may be
persisted; if persistence already occurred and cleanup then fails, the builder
must report the blocker without adding another project artifact.

## Fresh Round-1 review and one bounded revision

After an exact (U_{R0}) builder stop, a fresh independent reviewer may write
only `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`. A precondition identity or
inventory mismatch has disposition **WRITE NOTHING**. Otherwise the review
must independently rehash every allowed input, validate the R0 receipt and PDF
against both sources, and audit every theorem statement, proof transition,
formal multiplicity, exact coefficient, citation role, bibliography key,
page boundary, nonempty page, limitation, anti-claim, anonymity property,
overlap disclosure, PDF structural property, warning disposition, and visual
layout without rasterization.

Its final disposition is exactly one of `MANUSCRIPT_R1_PASS` or
`MANUSCRIPT_R1_REPAIR_REQUIRED`. Every finding has a stable identifier,
severity, exact location, required bounded repair, and theorem-scope impact.
Neither disposition authorizes finalization or release.

Exactly one bounded revision-author window follows a stable R1 review. The
author may edit only `paper/main.tex` and `paper/references.bib` and must add
the strict canonical `paper/SOURCE_REVISION_RECEIPT_R1.json`. Every source
change must map to an R1 finding and preserve the theorem, proof dependency,
formal convention, citation boundaries, evidence class, page contract,
anonymity, and overlap rule. If R1 requires no repair, both source files remain
byte-identical and the receipt records a no-op with zero changes. No second
revision window exists. A requested theorem or governance expansion is a
blocker rather than a permitted revision.

The revision receipt excludes its own hash and bytes and binds the R1 review,
the pre/post source hashes and bytes, an exact source diff digest and bounded
change ledger, or the explicit no-op identities. It must also bind the exact
prewrite and postwrite path universes.

## Round-1 rebuild and fresh Round-2 review

After an exact (U_{S1}) revision stop, the Round-1 builder repeats the same
two-clean-build protocol and every validation against the revised sources.
Its two distinct clean roots use the literal template
`/tmp/p15-paper15-r1-XXXXXXXX` and must match
`^/tmp/p15-paper15-r1-[A-Za-z0-9]{8}$`. It persists only:

- `paper/main_round1.pdf`
- `paper/BUILD_RECEIPT_R1.json`

The R1 receipt has the same strict canonical and content contract as R0. It
additionally binds the R0 PDF and receipt, the R1 review, the source revision
receipt, and the exact authorized pre/post source identities. It preserves
both R0 artifacts and never writes `paper/main.pdf`. The R0 and R1 PDFs may
differ only if the source revision receipt authorizes the exact source diff;
for a no-op revision, the R1 PDF must be byte-identical to the R0 PDF.

After an exact (U_{R1}) stop, a fresh Round-2 reviewer, distinct from all
authors, builders, and earlier reviewers, may write only
`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`. A precondition mismatch has
disposition **WRITE NOTHING**. The reviewer rehashes the entire allowed chain,
replays every R1 finding and repair, verifies no theorem drift or new defect,
and repeats the theorem, proof, citation, page, PDF, anonymity, warning,
public-text, and inventory audits. The sole positive final-line verdict is
exactly **MANUSCRIPT_R2_PASS**. A repair-required result creates no second
revision authority.

Even an exact R2 pass does not authorize finalization, `paper/main.pdf`, a
camera-ready version, identity disclosure, public release, submission, upload,
venue communication, external messaging, or any other downstream action.
Those actions require a separate future lock and independent review.

## Inventory, safe cleanup, and author stop

Immediately before these governance writes, the project contained exactly
15 regular files, four subdirectories excluding the root, zero symbolic
links, and no other entry type. After this scope and the canonical lock are
written, the required inventory is exactly (U_G): 17 regular files, the
same four subdirectories, zero symbolic links, and no other entry type.

At the governance stop, the publication-stage review path is absent; both
manuscript sources are absent; every R0, R1, revision, and R2 path is absent;
`paper/main.pdf` is absent; and no section source, macro file, figure, asset,
code, data, scientific result, build intermediate, release, submission,
upload, identity, or external-messaging artifact exists.

The publication lock must bind this scope by relative path, SHA-256, byte
count, and LF-line count. It binds itself only by relative path and authority
role; its own SHA-256 and byte count are excluded. The lock must be strict
compact canonical JSON with recursively Unicode-sorted keys, duplicate and
nonfinite rejection, and one terminal LF.

After writing and validating exactly the two governance artifacts, the author
must rehash all fifteen frozen inputs, verify exact (U_G), verify every
future absence, report both governance identities and lock structure, and
stop. No downstream file may be written in the same authoring turn.
