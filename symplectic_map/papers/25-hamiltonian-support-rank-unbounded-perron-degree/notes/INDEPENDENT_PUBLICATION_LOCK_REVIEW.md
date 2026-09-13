# Paper 25 Fresh Independent Publication-Lock Review

## Verdict, independence, and boundary

Review date: 2026-08-26 UTC.

The complete publication-lock conjunction passes. I found no blocker, major
finding, minor finding, unresolved ambiguity, canonicalization defect,
manifest or inventory defect, source-input defect, resource or toolchain
defect, build-executability defect, metadata or pagination defect, citation
or firewall defect, lifecycle or permission defect, or external-effect
defect.

I am the fresh independent publication-lock reviewer opened by the
parent-controlled `PAPER25_PUBLICATION_LOCK_REVIEW_OPEN` transition. I am
distinct from the publication-lock author and from both candidate reviewers,
the source-design author and reviewer, the source-lock author and reviewer,
both paper-plan authors and reviewers, and the publication-scope author and
reviewer. I authored none of the nineteen reviewed project inputs and used no
delegated reviewer.

I treated the final lock, every prior verdict, and every mathematical,
bibliographic, inventory, and build assertion as unproved. This review is a
nonexecuting publication-lock audit. I did not compile TeX, process a
bibliography, create or inspect a PDF, invoke Ghostscript on a PDF, run a PDF
inspection command on an artifact, access the network, assign a source, or
perform scientific computation. No Paper 23 or Paper 24 temporary root and no
path under `/tmp` was accessed.

## Governing records and complete consumption

I read both current root governance records through physical EOF before the
decision. Their stable review-gate identities are:

| Record | SHA-256 | Bytes | LF | Mode / links |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `40783136e382f56e419a83206a374590a3196129cfceb97a67a70b13721a390f` | 200,771 | 2,895 | `0644` / 1 |
| `BATCH_06_IDEA_REPORT.md` | `dcd6e0b32d7886f0a5751f75c3c9a4f947ae19f655c15cf633be4e84539cab07` | 353,955 | 6,725 | `0644` / 1 |

Both are regular UTF-8 files with terminal LF and no BOM, CR, or NUL. Each
contains the current gate exactly once. The chronologically controlling
idea-report transition authorizes this conditional review path and no other
write. The lock's own author-stop permission fields remain historically
false and do not self-authorize this review.

I also read all nineteen project files completely through EOF, including both
one-line JSON locks, all 1,240 lines of the proof package, both complete paper
plans, all prior independent reviews, the complete publication scope, and all
proposal, citation, claims, novelty, tracker, and research-question records.
I read all 251 lines of the local `paper-compile` skill as the deterministic
build-review standard; it routed to no additional required reference. The
frozen direct-pass contract, rather than an unbound wrapper, controls this
review.

The two root candidate controls also remain unchanged:

| Record | SHA-256 | Bytes | LF | Final control |
|---|---|---:|---:|---|
| `BATCH_06_PAPER25_CANDIDATE_REVIEW_R1.md` | `c8044d3d41573df7d1cd356acaa1e78414e18b3608e76a50553157c556495d0f` | 21,097 | 603 | `PAPER25_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER25_CANDIDATE_REVIEW_R2.md` | `46724d7d3c764d95f8235e6ffc40b40d78c6130ccf9c85a5832bbc4b5ca6b408` | 17,460 | 663 | `PAPER25_CANDIDATE_GATE_PASS_R2` |

## Final lock identity and strict canonical adjudication

The reviewed lock is
`experiments/publication_lock.json`. Its independently measured identity is:

- SHA-256
  `414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081`;
- 69,835 bytes and exactly one LF;
- one physical JSON line followed by exactly one terminal LF;
- regular non-symlink file, mode `0644`, link count one; and
- valid UTF-8 with no BOM, CR, or NUL.

I decoded the raw bytes strictly and parsed them with an object-pairs hook
that rejects a duplicate before dictionary construction. Float tokens and
`NaN`, `Infinity`, and `-Infinity` were rejected at token conversion. A
recursive walk admitted only object, array, string, integer, Boolean, and
null values. Every object's encountered key sequence was already in ascending
Unicode code-point order. Recursive key sorting followed by UTF-8
`ensure_ascii=false` compact encoding with separators comma and colon and one
terminal LF reproduced all 69,835 bytes exactly.

The independent structural census is exactly 228 objects and 67 arrays. The
top level has 23 fields. The schema is exactly
`paper25.publication_lock.v1`, the integer lock version is exactly 1, and the
top-level `lock_status`, top-level `status`, and nested author-stop status all
equal exactly:

`PUBLICATION_LOCK_AUTHOR_STOP / PENDING_PARENT_CONSUMPTION_BEFORE_FRESH_PUBLICATION_LOCK_REVIEW`.

The lock names its own path only as the new regular node in the post-lock
inventory. It contains no field assigning its own digest or octet count. Its
pre-lock aggregate and post-lock content aggregate deliberately exclude only
this lock's own bytes, while every one of the eighteen predecessor files is
fully bound. Thus the self-exclusion is necessary, explicit, and no broader
than its stated self-referential hash/size boundary.

The predecessor `experiments/source_lock.json` separately remains strict
canonical JSON under `paper25.source_lock.v1`, SHA-256
`5aa32ca98f7725b9f627129056250d4c21de0b228b66c8b56644752e5512c5ab`,
34,422 bytes and one LF. Its duplicate-rejecting recursive-sort compact
round trip also reproduced every byte.

## Exact L18 manifest, framed aggregate, and L19 universe

I recomputed SHA-256, byte count, LF count, node type, mode, link count,
UTF-8 validity, terminal LF, BOM, CR, and NUL directly for every manifest
row. All eighteen rows contain a SHA field and every field matches the live
immutable input. Adding the externally measured lock gives the complete L19
binding:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `ab2291ddf6bff7aae632e2b261c58895a9367dc110f15d2c22920cec685a7cc9` | 11,033 | 359 |
| `experiments/EXPERIMENT_TRACKER.md` | `9527dada16fa76c0434e94de028a1635fcab3942cf9bee5a38d5cb577f1a89fb` | 5,405 | 92 |
| `experiments/publication_lock.json` | `414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081` | 69,835 | 1 |
| `experiments/source_lock.json` | `5aa32ca98f7725b9f627129056250d4c21de0b228b66c8b56644752e5512c5ab` | 34,422 | 1 |
| `notes/CITATION_VERIFICATION.md` | `9538e423e5ba9fedf9e9cac3fd8060800d683a935ffba48b8ada69b3b51697af` | 9,001 | 126 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `abb0b13c83fc32c5dbbecd0de6ce18c6a154177f41955deddcfba3bc308b6e7d` | 8,618 | 87 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `2b55e0068348b377d27b982aea3940211a53194e5d41d26e6712eb1053eebbee` | 26,764 | 506 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `413886a5c5c75ce82f2dd3005571ab70241f3f6e9d0bd4102972954260cabe67` | 34,357 | 734 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `feaeb0b5b6c3c6ecb006349e529fcc92355aaea60a969851e20d86312e6e1e5b` | 26,953 | 793 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `e18007da043a38d6099a0d99a55c83d4f590dba79bfb0fe102fab4b118a6e98b` | 25,132 | 515 |
| `notes/NOVELTY_ASSESSMENT.md` | `ecc57ca4ba68375270b04d5be2eff9884d31f81d3fa1acc36d0bc5cd49f2683d` | 8,496 | 136 |
| `notes/PROOF_PACKAGE.md` | `0b957e5519dff5460d819de335782b9ac2b669f42089e0699d03cf0349f5ab93` | 29,750 | 1,240 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `9a60c44aaa308aefce7d0e4f8ea877b381f37386ee7fe88447850e33aa76fca0` | 43,878 | 800 |
| `notes/RESEARCH_QUESTION.md` | `8641c4160fe74ee3925bc2803c90ef139261f48c844c78856b53989e9a8d7098` | 5,839 | 139 |
| `paper/PAPER_PLAN.md` | `ebcd925470e25d53f85bbce861aee68bbefcf4702128e2338969887bb2039be4` | 54,112 | 1,044 |
| `paper/PAPER_PLAN_R1.md` | `422c4e1d4a7810cc6013e1be6ad611ac7c3f4d6d9b70024d389dfc7a2a87c747` | 54,340 | 1,046 |
| `refine-logs/FINAL_PROPOSAL.md` | `13bf8d9bc21a1841b24b9d9308558d6807cba5e218685a03795dfd65d75d4f6d` | 7,426 | 220 |
| `refine-logs/INITIAL_PROPOSAL.md` | `06caba1425c68ac387d3ae618bc1ce1edea02cbf4db547adfb3dea136070f6ba` | 5,788 | 126 |
| `refine-logs/REVIEW_SUMMARY.md` | `69408011fd514f8a5ab54fe81253b960e527c58c0da46090f346e076de931fb7` | 6,190 | 122 |

Every row is a regular non-symlink file, mode `0644`, link count one, valid
UTF-8, terminal LF, and free of BOM, CR, and NUL. The only four child
directories are `experiments`, `notes`, `paper`, and `refine-logs`; there is
no symbolic link or other node.

For the L18 aggregate I emitted the 31-byte prefix consisting of ASCII
`paper25-publication-prelock-v1` followed by NUL. In ascending bytewise order
of project-relative UTF-8 POSIX paths, I then emitted for each file:

`uint64_be(path-byte-count) || path bytes || uint64_be(content-byte-count) || exact content bytes`.

The eighteen content files total 397,504 bytes and 8,086 LF; their paths
total 552 UTF-8 bytes. The resulting stream is exactly 398,375 bytes with
SHA-256
`78f1a0a41476c33f3d3767001ed301f6b1f0f5c1c2146101b731cc2bddd2861c`.
The live L19 universe is exactly nineteen regular files, four directories,
zero links, zero other nodes, 467,339 content bytes, and 8,087 LF. Removing
only the 69,835-byte, one-LF publication lock restores exact L18. No old
project input changed.

## Bounded repair adjudication

The final author-stop lock, rather than either intermediate repair identity,
is the sole reviewed object. The bounded pre-handoff repair is complete:

1. all eighteen manifest rows contain their reproduced SHA-256 values;
2. the exact environment map contains neither `HOME` nor `CODEX_HOME`, and
   both remain unset under `/usr/bin/env -i`;
3. no pass or inspection command independently assigns either variable;
4. the `.fls` contract identifies only immutable source-origin
   `main.tex` and `math_commands.tex`, separately permits generated reads
   `main.aux`, `main.bbl`, and `main.out`, and classifies all remaining
   records as audited system TeX/font inputs;
5. `references.bib` is a BibTeX-only input and is not misclassified as a
   pdfLaTeX `.fls` input; and
6. BibTeX reads exactly generated `main.aux`, immutable
   `references.bib`, and frozen system `plain.bst`, and writes only
   `main.bbl` and `main.blg`.

The repair creates no source or output expansion. The ledgers state that no
downstream actor consumed an intermediate identity, and every live binding
and final semantic field agrees with that disposition.

## Article identity, effective plan, and mathematical contract

The exact title on every title-bearing surface is:

**Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product
Shears**

The source-visible and rendered author is exactly `Anonymous`; the visible
date and source date are empty. PDF/XMP Author, Subject, Keywords, Creator,
and Producer are semantically empty, while PDF/XMP Title and the outline root
use the exact full title. The visible word `Anonymous` may not propagate to
PDF/XMP Author. Affiliations, author footnotes, acknowledgments, grants,
emails, ORCIDs, personal or repository links, identity clues, and hidden
revision or collaboration data are forbidden.

`paper/PAPER_PLAN_R1.md` is the sole effective plan. Its SHA-256 is
`422c4e1d4a7810cc6013e1be6ad611ac7c3f4d6d9b70024d389dfc7a2a87c747`,
and its terminal `PAPER PLAN R1 AUTHOR STOP` is unique and final.
`paper/PAPER_PLAN.md` is immutable superseded history, not a fallback or an
effective notation source. The bounded R1 delta uses uppercase `N` only for
the abstract Structural-Theorem dimension and lowercase `n` only for the
nonnegative iterate index.

The complete theorem package is internally consistent:

- Theorem H quantifies every `d>=2`, chooses parameters only in the order
  `d -> p,c -> a_1<...<a_d -> b,R_0`, uses the literal positive potentials
  and shears, and fixes `D`, `B_0`, and `C=b 1 a^T-D`.
- Its six retained conclusions are polynomial symplecticity; exact ordinary
  degree `deg(F^n)=e_1^T C^n 1` for every `n>=0`, with a tied seed and unique
  `q_1` only for positive iterates; rational irreducibility and reduction to
  `t^d-c`; forward Perron dynamical degree and algebraic degree exactly `d`;
  minimal rational constant-coefficient scalar recurrence order exactly `d`
  both from the start and eventually; and selected stacked row rank `r=d`.
- Structural Theorem S uses abstract ambient dimension `N` and proves
  `chi_C(t)=(t-1)^(N-r) det((t-1)I_r-T_0X)`. It concludes only unit
  multiplicity at least `N-r` and nonunit characteristic degree at most `r`;
  the reduced monic degree-`r` factor may contain extra unit roots.
- Corollary C uses the exact selected presentations, invertibility of
  `D+I_d`, and irreducibility to prove existential attainment for every
  constructed `r=d>=2`, not universal-presentation sharpness.

The lemma array is exactly L1 through L15 in proof order. It includes full
row-basis factorization, both rank boundaries, noncircular parameters,
literal gradients and symplecticity, broad and fine chambers, both temporal
carries, positive-semiring survival, exact visibility, characteristic
arithmetic, the complete three-part finite-field binomial audit, Perron
degree, reachability/observability and Hankel rank, eventual scalar
minimality, and rank sharpness. Every dependency remains a main-text proof
obligation; no citation, figure, appendix, computation, or finite example
may replace one.

The assumptions and boundaries are exact: characteristic zero, ordinary
total degree, fixed positive supports, `d>=2`, separate `N` and `n`, exact
primitive order of `c`, all strict chamber inequalities, `r=0`, `r=N`,
possible extra unit roots, the `d=2` nonsquare case, the extra condition when
4 divides `d`, the tied identity seed, and positive-iterate-only unique
visibility. The twelve anti-claims remain complete, including no arbitrary
support or sign theorem, no every-Perron realization, no minimal-dimension or
rank-zero/rank-one result, no inverse or higher-degree result, no
positive-characteristic extension, no classification or genericity, no
priority claim, no proof transfer, no computational evidence, and no
universal-presentation sharpness.

## Page, table, figure, and citation contract

The content ledger is exactly 26.00 pages from Abstract through Conclusion:

`0.50 + 2.50 + 2.50 + 2.50 + 3.00 + 6.00 + 3.00 + 3.00 + 3.00 = 26.00`.

Each Section 1--8 subsection sum independently equals its parent allocation.
References are excluded. The source must place a `clearpage` immediately
before the sole bibliography insertion. The extraction algorithm requires
the first standalone normalized `References` heading on physical page 27,
no earlier occurrence, nonempty content pages 1--26, and the Conclusion
heading on page 26. Total PDF pages are at least 27 and references occur only
from page 27 onward. No appendix or supplement may carry a proof obligation.

The manually authored Section 1.5 proof-map table is planned and never
evidence. A notation or context table is conditional; every other table is
default-off and needs a documented exposition purpose. Hero, empirical,
benchmark, ablation, dataset, result, and evidence figures are forbidden. A
cone diagram remains separately authorized, inline-vector, grayscale-safe,
definition-only, and default-off; there is no figure source file.

The contextual public-source universe is exactly eight records with exact
reserved keys, in order:

`BvS, SS, DF, BT, KL, Des, AX, HS`.

Their roles remain contextual and do not transfer a proof. The Berger--Turaev
arXiv title is literally **Generators of groups of Hamitonian maps**, while
the version-of-record title is **Generators of Groups of Hamiltonian Maps**;
the version-of-record-first `BT` rule preserves both manifestations without
creating a ninth contextual work. Any noncollision statement must remain the
exact bounded, nonexhaustive two-sentence pair through 2026-08-26 UTC and may
not imply firstness, uniqueness, or priority.

The authoritative standard-source queue is exactly STD-01 through STD-08:
Sylvester, matrix determinant lemma, Dirichlet, finite-field multiplicative
group cyclicity, Gauss and same-degree modular lifting, Perron--Frobenius,
Cayley--Hamilton, and cyclic reachability/observability/Hankel-rank facts.
Every row remains
`UNASSIGNED_PENDING_SEPARATE_AUTHORITY_AND_PRIMARY_RECORD_VERIFICATION`.
The queue assigns no source, key, theorem number, or metadata, transfers no
proof, and authorizes no bibliography action.

## Exact future source universe and public firewall

The complete possible future manuscript-source universe is exactly:

1. `paper/main.tex` for anonymous front matter, metadata controls, Abstract,
   Sections 1--8, all proofs and authorized tables, limitations, Conclusion,
   and the sole bibliography invocation;
2. `paper/math_commands.tex` for notation and formatting macros only, with
   no prose, claim, proof, bibliography datum, I/O, shell escape, identity,
   or hidden executable behavior; and
3. `paper/references.bib` for the eight freshly verified contextual records
   plus only the minimum freshly verified standard records, with no unused,
   speculative, local, identity-bearing, generated, or hidden field.

The roles are disjoint. There is no section, appendix, copied class or style,
figure, generated TeX/BibTeX/bbl source, hidden include, alternative
bibliography, code, data, notebook, build file, package manifest, or source
archive. All three paths were absent before this review write.

The public firewall covers all source and comments, BibTeX data, rendered
text, headers, footers, bookmarks, anchors, links, PDF information, XMP,
IDs, attachments, annotations, filenames, URIs, archives, release manifests,
forms, README text, and registry fields. It forbids local paths or machine
identities; hashes, counts, modes, inventory labels, internal timestamps, or
build diagnostics; verdict, score, role, gate, lock, or lifecycle data;
private identities or acknowledgments; internal projects and lineage;
unverified bibliography data; hidden/generated prose or traces; and priority
or exhaustive-discovery claims. Only verified public citation metadata and
the three publication-safe source basenames have the narrow stated
exceptions.

## Deterministic build contract and future executability

The date conversion is exact: `2026-08-26T00:00:00Z` equals epoch
`1787702400`. The internal reproducibility date never becomes a visible date,
metadata author field, prose string, filename, or release description.

Every pass starts with `/usr/bin/env -i` and the same exact map:

`BIBINPUTS=.`; `BSTINPUTS=.:/usr/share/texlive/texmf-dist/bibtex/bst/base`;
`FORCE_SOURCE_DATE=1`; `LANG=C`; `LC_ALL=C`; `PATH=/usr/bin:/bin`;
`SOURCE_DATE_EPOCH=1787702400`;
`TEXMFCONFIG=/nonexistent/paper25-texmf-config`;
`TEXMFHOME=/nonexistent/paper25-texmf-home`;
`TEXMFVAR=/nonexistent/paper25-texmf-var`; `TZ=UTC`; `openin_any=p`; and
`openout_any=p`.

`HOME` and `CODEX_HOME` are absent, not assigned an independent value, and
not repurposed. Network access must be administratively disabled throughout.
The exact pass order is:

1. `/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex`;
2. `/usr/bin/bibtex main`;
3. the identical second pdfLaTeX command; and
4. the identical third pdfLaTeX command.

There is no wrapper, retry, extra pass, shell escape, or postprocessor. The
final PDF is the direct third-pdfLaTeX output.

The exact A and B roots are `/var/tmp/paper25-publication-build-A` and
`/var/tmp/paper25-publication-build-B`. Both were absent and not symlinks at
review time, tested only by their exact names. A later authorized build must
fail without reading, cleaning, reusing, or deleting either root if it is
present. Each root is then created once, empty and mode `0700`; the three
identical mode-`0644` sources are staged; no subdirectory is allowed. The
only permitted root basenames are `main.tex`, `math_commands.tex`,
`references.bib`, `main.aux`, `main.bbl`, `main.blg`, `main.fls`, `main.log`,
`main.out`, and `main.pdf`. A and B share no cache, auxiliary, output, or
working directory. No build output enters the project tree.

The source and generated-input distinctions are executable and closed. In
pdfLaTeX `.fls` records, immutable source-origin inputs are exactly
`main.tex` and `math_commands.tex`; generated inputs are restricted to
`main.aux`, `main.bbl`, and `main.out`; every other input must be an audited
system TeX or font dependency. BibTeX alone reads `references.bib`, together
with generated `main.aux` and system `plain.bst`, and writes only `main.bbl`
and `main.blg`. `main.aux` may name only database `references` and style
`plain`. No home, workspace, network, project-local substitute, alternative
database/style, or generated source expansion is allowed.

The warning policy is consistent with the pass order. Pass 1 may report only
initially missing `main.bbl`, unresolved citation/reference, and consequent
rerun diagnostics; pass 2 may report only a rerun diagnostic; all must be
absent on pass 3. BibTeX returns zero with no error or `Warning--` line.
Every missing expected file, unexpected node, nonzero command, source drift,
unlisted input, overfull or underfull box, hard-error pattern, missing glyph,
duplicate destination, or final LaTeX/package/pdfTeX/hyperref/bookmark/
hyperxmp/rerun/font/metadata warning is a hard failure.

The metadata source requirements are mutually compatible: PDF/XMP title and
empty metadata are set in the preamble; visible title, `Anonymous`, and empty
date are declared only after `begin-document` and immediately before
`maketitle`. Before PDF objects, `pdfinfoomitdate=1`, an empty trailer ID, and
`pdfsuppressptexinfo=-1` are required. The exact system
`glyphtounicode.tex` is input and `pdfgentounicode=1` is set. Under the frozen
`hyperxmp.sty`, the XMP basic temporal and media-management ID schemas are
suppressed while the exact Dublin Core title remains. Creation/modify/XMP
dates, trailer/document/instance IDs, source paths, and diagnostic data must
be absent.

Per build, Ghostscript performs only a `-dSAFER` null-page structural check.
`pdfinfo` inspects custom information, XMP, destinations, URLs, JavaScript,
and structure; `pdftotext` performs layout and raw UTF-8 extraction;
`pdffonts` and `pdfimages -list` inspect fonts and images; PyMuPDF emits the
canonical sorted metadata/XMP/outline/attachment/link/annotation/page-text
manifest; and `sha256sum` digests the PDF. All fonts must be embedded and
subset, non-Type-3, nonbitmap, nonsubstitute, and text-usable with ToUnicode.
No raster image, attachment, encryption, JavaScript, launch action, private
annotation, file link, local URI, revision data, or hidden collaboration data
may occur. Bookmarks must contain the exact root title, Sections 1--8 in
order, and References, with public text and correct hierarchy.

The A/B acceptance test requires byte-identical final PDFs by SHA-256 and
`/usr/bin/cmp -s`, plus byte-identical outputs for every `pdfinfo`, text,
font, image, and canonical PyMuPDF inspection. No normalization, optimizer,
linearizer, metadata editor, timestamp fixer, or PDF rewrite is allowed.

## Frozen system resources

Using `/usr/bin/kpsewhich` under the exact clean map, I independently
resolved every listed basename from the system installation and hashed the
resolved bytes. All nineteen identities match:

| Resource | SHA-256 |
|---|---|
| `article.cls` | `988fb3e599df7e5b545e4253829dab11f0c7bd7827b79d32c2aaadfb52db6f6c` |
| `size11.clo` | `efc946da03cfa55c75be27d73012ab866fcc935fd47ac4a674026bbdbdcfa9f1` |
| `inputenc.sty` | `16dffe967174f21dbd52ef849bcb74741109f3ce5bc68b881f1ce4aef3133b2a` |
| `fontenc.sty` | `d088c75e16c3c9f6b979a59571b96e5dd9e487a720bc74591580878388b82918` |
| `lmodern.sty` | `e1cdd137ae86b4e860f0b0bcfc4c1a90cae3ff1f9c651cb21bd86c15bb83b916` |
| `geometry.sty` | `d5d36ad74051ad36288242b51438e2d9a5db2bd6c063b9b5704d0931fbc9f439` |
| `microtype.sty` | `a23ca4bacbb60ff7b5aa1052e2a3281cebfcd06ea2e615ad14d12c1786204b4d` |
| `amsmath.sty` | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` |
| `amssymb.sty` | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| `amsthm.sty` | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` |
| `mathtools.sty` | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` |
| `array.sty` | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` |
| `booktabs.sty` | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| `enumitem.sty` | `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3` |
| `hyperref.sty` | `77e7c2421a06900f158416e090665069dd724a6e0c605cd2a1838c7d3b7944d2` |
| `hyperxmp.sty` | `2cfcad062c321ea5b036d119b936ce227cd9d228a2ad0002e3912a5fda39848a` |
| `bookmark.sty` | `d0f20a8d678f8236e2fa0bf85f1885231f478b481b3577230b2f75d4ff136d0f` |
| `plain.bst` | `19f2cf88686b86aaa8e65d5f0313a92499815761e04b42e84ea2c3dc3685ada9` |
| `glyphtounicode.tex` | `395e568c1f4db5e89013e6aa4aac22a668b543256a20b4349436070356870851` |

The order is class and 11-point option, UTF-8/T1/Latin Modern, geometry and
microtype, mathematics, manual table/list packages, `hyperref`, `hyperxmp`,
`bookmark`, then system `plain.bst` and `glyphtounicode.tex`. Only
system-owned transitive dependencies reached from this list are permitted,
and future `.fls` review must audit them completely and identically in A and
B.

## Frozen toolchain

I independently hashed every command binary and the exact `fitz` module file,
then reproduced each read-only version fingerprint. All identities match:

| Tool | SHA-256 | Version fingerprint |
|---|---|---|
| `/usr/bin/bash` | `59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4` | `GNU bash 5.1.16(1)-release (x86_64-pc-linux-gnu)` |
| `/usr/bin/pdflatex` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | `pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian); kpathsea 6.3.4/dev` |
| `/usr/bin/bibtex` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | `BibTeX 0.99d (TeX Live 2022/dev/Debian); kpathsea 6.3.4/dev` |
| `/usr/bin/kpsewhich` | `ae30057832d4870b13d3abcbf10187b538dc3439afff15d624a65b920dc7911b` | `kpathsea 6.3.4/dev` |
| `/usr/bin/env` | `85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0` | `GNU coreutils 8.32` |
| `/usr/bin/gs` | `7354a9e165d960a4d55e2af5e7af3203777054dfd50228d99814860263ec09ff` | `GPL Ghostscript 9.55.0` |
| `/usr/bin/pdfinfo` | `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` | `Poppler 22.02.0` |
| `/usr/bin/pdftotext` | `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` | `Poppler 22.02.0` |
| `/usr/bin/pdffonts` | `257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e` | `Poppler 22.02.0` |
| `/usr/bin/pdfimages` | `cdac55daf2eaacbaf9f80cf8371e935c8686cb4fd7e84c42bba9706c1f10c87d` | `Poppler 22.02.0` |
| `/usr/bin/sha256sum` | `7645c8e76d75515ccb75c9086bdcf0d4071f2985f380f249253ead7d7c6810b3` | `GNU coreutils 8.32` |
| `/usr/bin/cmp` | `b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791` | `GNU diffutils 3.8` |
| `/root/miniconda3/bin/python3` | `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` | `Python 3.12.3` |
| `fitz/__init__.py` | `23dae7eac8bbdcae7fc175de7fa168b849c25b6fec1a7196a7a9e9f6141a372f` | `PyMuPDF 1.27.2.3; MuPDF 1.27.2` |

Only version calls, exact resource resolution, byte hashing, and exact path
existence checks were executed. Neither pdfLaTeX nor BibTeX processed an
input, and no build or inspection artifact was created.

## Lifecycle, permissions, and finding ledger

Immediately before this review write, the review path, all three future
source paths, and both exact A/B build roots were absent as files, links, and
directories. The project had exact L19. Every permission in the lock was
false and `authorized_write_paths` was empty: no manuscript, TeX, BibTeX,
standard-source verification or assignment, table, figure, code, data,
experiment, CAS, build, PDF, archive, release, submission, upload, hosting,
repository, README, registry, message, network, identity disclosure, Paper
26, or external effect was open.

This passing review makes only the three paths `paper/main.tex`,
`paper/math_commands.tex`, and `paper/references.bib` jointly eligible for a
later parent decision, including any separately authorized primary-record
verification. Eligibility is not authority: this review creates or
authorizes none of those files, no verification, no build, no PDF, no
release, no Paper 26 work, and no external effect.

| Finding class | Count | Disposition |
|---|---:|---|
| blocker | 0 | none |
| major or minor mathematical finding | 0 | none |
| unresolved ambiguity | 0 | none |
| canonicalization or self-exclusion finding | 0 | none |
| manifest, framing, inventory, identity, or encoding finding | 0 | none |
| article, theorem, proof, page, table, or figure finding | 0 | none |
| citation, key, source-queue, or proof-transfer finding | 0 | none |
| future-source or public-firewall finding | 0 | none |
| environment, source-input, build, metadata, or inspection finding | 0 | none |
| system-resource, binary, module, or version finding | 0 | none |
| lifecycle, permission, or external-effect finding | 0 | none |

This file is the sole filesystem delta made by this reviewer. No existing
project file, root ledger, source path, or build root was modified or
created. Its own SHA-256, byte count, LF count, mode, link count, encoding,
terminal uniqueness, and exact L19-to-L20 delta are intentionally measured
externally after creation rather than embedded self-referentially here.

PUBLICATION_LOCK_PASS
