# Independent Publication-Stage Review

Date: 2026-08-17 UTC

Candidate: `henon_support_size_torus_escape_v1`

Canonical project: `papers/16-henon-support-size-torus-escape`

## Review identity, temporal fence, and scope

This is the fresh independent review of the Paper16 publication-stage
governance pair. I authored or modified none of the fifteen frozen inputs,
neither governance artifact, and no future manuscript, source-review, build,
revision, or review-round artifact. Before the first explicit `PUBLICATION
AUTHOR STOP`, I did not open, list, stat, hash, or inventory either future
governance path.

The first stopped pair contained blockers, so I made no project write and
reported the defects. I did not reopen either artifact during the bounded
repair. After the fresh author stop with new stable identities, I independently
read and rehashed the repaired pair, rehashed all fifteen inputs, reconstructed
the superseded pair in memory by reversing only the authorized repairs, and
replayed the complete publication gate. The reconstruction reproduced both
superseded hashes and byte counts exactly, establishing that no other drift
occurred.

I performed only read-only governance checks before this report: complete
reading, hashing, byte and LF counting, strict JSON validation, exact-set and
inventory comparison, and semantic review. I performed no manuscript drafting,
bibliography authoring, compilation, network access, CAS operation, symbolic or
scientific calculation, experiment, data or result generation, figure work,
submission, upload, release, or external communication. This report is my sole
project write.

## Governance-pair identity and bounded-repair closure

The repaired pair independently matches the fresh author stop exactly:

| Governance artifact | Bytes | LF lines | SHA-256 |
|---|---:|---:|---|
| `notes/PUBLICATION_STAGE_SCOPE.md` | 44,353 | 997 | `26efa57a0fa024b5272117b1e615da63f631967f9506bbf18df3f3b0bafa30a6` |
| `experiments/publication_lock.json` | 55,924 | 1 | `9be9105d43e68ee71c745e9fb8748900bc3605e6918475e393b831f47372449c` |

The reverse reconstruction is exact. Replacing the two repaired boundary
displays by their former malformed text, restoring the former overbroad public-
text paragraph, and reversing only the corresponding lock changes reproduces:

- the superseded 43,850-byte, 989-LF scope with SHA-256
  `30c47dd0c3aa43ea485b9cbaef81810308e63bd998225d95cc372cdf8040715a`;
- the superseded 55,175-byte canonical lock with SHA-256
  `b1ea7d03ff8e5e3d0b262bd14f49fb436f564231d23abe936f81b607a0d3c1ac`.

Thus the repair changed only the authorized items: the missing `\qquad`
commands in the two counterexample displays; the narrowing of the identity and
date ban to manuscript-author identity and manuscript/front-matter dates or
identity-bearing timestamps; the explicit exemption for neutral bibliographic
authors, years, and locked preprint version dates; the consistent activation
of source-level review after a stable draft stop; and the scope identity bound
by the canonical lock.

## Fifteen frozen-input bindings

All fifteen inputs were independently re-read and rehashed after the fresh
stop. Every observed path, byte count, LF count, and SHA-256 value agrees with
both governance artifacts:

| Frozen input | Bytes | LF lines | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5,824 | 129 | `f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6` |
| `experiments/EXPERIMENT_TRACKER.md` | 1,971 | 48 | `4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d` |
| `experiments/source_lock.json` | 31,945 | 1 | `86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd` |
| `notes/CITATION_VERIFICATION.md` | 10,733 | 205 | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 7,659 | 59 | `bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 9,989 | 211 | `d7493502cf05fb489f5dfe88ce48c6b93c549316bc62f95e617aedb255c399d3` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 13,903 | 360 | `046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 14,929 | 298 | `f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c` |
| `notes/NOVELTY_ASSESSMENT.md` | 7,309 | 117 | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `notes/PROOF_PACKAGE.md` | 16,808 | 704 | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `notes/RESEARCH_QUESTION.md` | 8,319 | 318 | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `paper/PAPER_PLAN.md` | 34,681 | 880 | `875d26506ba552c79fe62fe11ac1a70e73e1a00245e8bb1aacc1b5c58753d336` |
| `refine-logs/FINAL_PROPOSAL.md` | 5,387 | 155 | `220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,253 | 98 | `329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2` |
| `refine-logs/REVIEW_SUMMARY.md` | 5,479 | 95 | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |

The earlier independent reviews still end with `SOURCE_LOCK_PASS` and
`PAPER_PLAN_PASS`. They establish frozen provenance and eligibility, not an
independent downstream authorization.

## Strict canonical-lock and self-exclusion gate

The repaired publication lock passes every strict canonical check:

- strict UTF-8 decoding succeeds, with no BOM or carriage return and exactly
  one terminal LF;
- parsing with duplicate-key rejection and nonfinite-number rejection
  succeeds;
- synthetic duplicate-key, `NaN`, `Infinity`, and `-Infinity` objects are all
  rejected;
- recursively Unicode-sorted, compact-separator, `ensure_ascii=false`
  serialization plus one LF reproduces all 55,924 bytes exactly;
- all fifteen binding paths are unique, safe, nonempty relative paths without
  dot or dot-dot components;
- the scope binding gives its exact safe path, repaired SHA-256, bytes, and LF
  count; and
- the lock binds itself only by safe path and authority role. Its own SHA-256
  and byte count are absent, and it is not one of the fifteen content bindings.

No current downstream authorization is true. The only true lifecycle state is
the frozen publication stage pending this independent review; the lock records
no draft, no build, no executed code or science, no finalization, and no
release.

## Exact inventory and future-absence gate

Immediately before this sole pass write, the project universe was exactly the
17-file governance universe. It had exactly four real subdirectories excluding
the root (`experiments`, `notes`, `paper`, and `refine-logs`), zero symlinks,
and zero other entry types. Its files were exactly the fifteen frozen inputs
plus the repaired scope and publication lock.

The present review path was absent. The two public sources, the formal source-
review path, both round PDFs, both build receipts, the Round-1 review, the
revision receipt, the Round-2 review, and `paper/main.pdf` were absent. All
section, macro, style, class, figure, asset, code, data, result, build,
release, source, submission, and output paths forbidden at this stage were
absent. No later-stage artifact was pre-created or inspected.

## Theorem, proof, and quantitative gate

The governance pair preserves the exact title **Support Size and Finite-Rank
Torus Escape for Generalized Hénon Maps** and one dependent support-size phase
transition. It keeps characteristic zero, actual collected support

\[
1\le e_1<\cdots<e_s=d,
\qquad
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\]

with all displayed coefficients nonzero, the map
\(H(x,y)=(P(x)+ay,x)\), an arbitrary finite-rank subgroup
\(\Gamma\le K^*\), no finite-generation assumption, and the exact convention
that \(T_m\) has \(m\) transitions and \(m+1\) states.

The quantitative definitions are exact. Amoroso--Viada supplies

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)},
\]

the sparse-image budget is

\[
\mathcal S_q(d,r)=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\qquad
\mathcal S_*=\max_{2\le q\le s+1}\mathcal S_q(d,r),
\]

and \(\mathcal M(\mathbf e)\) is defined by the two locked subset sums. The
closed expression and crude inequality remain checksums only.

PC1 is dominant and states exactly

\[
\#T_2(H,\Gamma)
\le d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*
\qquad(s\ge2).
\]

PC2 gives the prescribed-support rational rank-one family
\(a=b_j=1\), \(c=-s\), \(\Gamma=\langle2\rangle\), and
\((1,2^n)\mapsto(2^n,1)\), proving that one transition does not suffice.
PC3 is subordinate, fully reproduced, and states

\[
\#T_4(H,\Gamma)\le4d\mathcal A(3,3r)+81d^2,
\]

with the exact rank-one sharpness chain
\(t^d,t,c,-t,(-t)^d\). It receives no renewed support-one novelty credit.

The proof lock is complete. It keeps Amoroso--Viada Theorem 6.2 as the sole
external proof theorem and includes the algebraic-closure injection for an
arbitrary characteristic-zero field, rank preservation or upper bounds, and
no descent or equality claim. Fixed coefficients never enlarge a variable
group.

The sparse-image lemma retains the rank-\(2r\) tuple, degree-\(d\) power
fiber, all \(2^q-q-2\) proper degenerate subsets, and arbitrary torsion. The
PC1 proof retains the fixed \(Z/U/M_j\) normalization, rank \(3r\), all four
GZ/GU/R0/R1 cases, both graph endpoints, coefficient cosets, the exact two
root budgets, second-recurrence closure even after constant cancellation, and
the deliberately overlapping simultaneous-label union. The repaired scope now
typesets both \(c=0\) and \(a=0\) boundary calculations correctly.

The complete PC3 proof retains all A/B/C labels, all nine adjacent words, the
BA and CB continuations, the compatible CBA branch under
\(a=-1\) and \(bc^{d-1}=-1\), the fourth-label closure, and the exact
\(3^4d^2=81d^2\) word union. Appendices may audit these calculations but may
not supply a missing hypothesis or implication.

## Citation, novelty, anti-claim, and absorption gate

The bibliography contract has exactly seven verified primary entries, all and
only actually cited entries. Amoroso--Viada is the sole proof input; ESS is
historical only. The three Krieger-et-al. result roles remain distinct.
Bell--Ghioca remains fixed-orbit and finitely generated, with arithmetic
progressions separated from the finite regular-map residual. Ji--Xie--Zhang
remains non-density, the Mello--Yasufuku epsilon mismatch remains unresolved
and unused, and Kim et al. retains its exact degree and congruence restrictions.

The bounded-search statement is frozen through 2026-08-17 and does not become
priority, a “first” claim, or an absence-of-unpublished-work statement. The
twenty-one mandatory public anti-claims, together with the theorem, citation,
absorption, and lifecycle locks, preserve every semantic boundary of the
twenty-four source-lock anti-claims. No finite-generation, coefficient-
membership, additive-closure, periodic-classification, optimal-constant,
effective-enumeration, height, broader-map, computational-evidence, or global-
priority claim is introduced.

The public-safe overlap paragraph is fixed verbatim, exactly once, in Section
8.3 only. It states that an earlier manuscript by the same authors treated the
one-monomial case, that the present article reproduces and absorbs that theorem
and proof, that the manuscripts will not be submitted in parallel, and that
the present article is the sole intended external version of the overlap. The
predecessor receives no bibliography entry and supplies no black-box proof
step.

## Article, page, table, and public-text gate

The article is a standard self-contained anonymous pure-mathematics `article`,
not a venue or ML-conference template. It has exactly eight numbered main
sections, followed by Appendices A--C and then final References. The
mathematical-content count begins on the first PDF page, includes the abstract,
Sections 1--8, and all three appendices, and ends at Appendix C. It must be
24--26 nonempty pages, with target 25; References are excluded and begin after
a forced page break. There is no total-page cap that could displace a proof.

The abstract is 180--220 words, result-first, citation-free, and provenance-
free. PC1 receives the first theorem display and the largest proof allocation;
PC2 supplies exact sharpness; PC3 is visibly subordinate.

The visual contract is exact: zero figures, figure environments, image files,
included graphics, external assets, experiments, datasets, scans, empirical
results, or empirical tables. Exactly four main-text proof tables are required:
the GZ/GU/R0/R1 ledger, the nine-word A/B/C ledger, the BA continuation ledger,
and the CB/CBA continuation ledger. Every row must also be derived in prose,
and no other table environment is allowed.

The repaired public-text lock is now consistent with the bibliography. It
forbids manuscript-author names, affiliations, email addresses, self-
identifying links, manuscript/front-matter dates, identity-bearing timestamps,
acknowledgments, grants, repository and submission identities, local paths,
hashes, governance terms, verdicts, agent names, operational instructions, and
priority claims. Neutral bibliographic author names, publication years, and
the locked preprint version dates are expressly required and exempt, while
remaining unable to reveal manuscript authorship. PDF metadata dates and
identity-bearing metadata remain forbidden.

## Exact source-review gate, stage universes, and roles

The formal post-draft source gate is unique and closed. Its only path is

`notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md`,

and its only positive final line is `MANUSCRIPT_SOURCE_PASS`. Its reviewer
reads exactly the 20-file draft universe and authors neither public source. A
source blocker has disposition `WRITE NOTHING`. A bounded repair requires a
separate explicit instruction, may touch only the two existing public sources,
and must be followed by a fresh audit and a fresh reviewer. The advisory audit
has no project write and no lifecycle effect; there is no second or advisory
source-review artifact. The repaired lock consistently activates both the
formal and generic source-level review flags only after a stable draft stop.

The nine exact stage universes form the following monotone chain:

| Stage | Regular files | Sole additions from predecessor |
|---|---:|---|
| governance stop | 17 | scope and publication lock over the 15 frozen inputs |
| publication review | 18 | this review |
| anonymous draft | 20 | `paper/main.tex`; `paper/references.bib` |
| formal source PASS | 21 | the unique source-level review |
| Round 0 | 23 | Round-0 PDF and receipt |
| Round-1 review | 24 | independent R1 review |
| bounded revision | 25 | strict revision or no-op receipt |
| Round-1 build | 27 | Round-1 PDF and receipt |
| Round-2 review | 28 | fresh R2 review |

Every path list has exact set equality, the declared count, unique safe
entries, and the exact additions above. At every stage there are only the four
declared directories and zero symlinks. Every role's read allowlist equals its
predecessor universe, and every write universe equals only its declared output.
No role may read a later artifact, expand its universe, review an object it
authored, edit source while building, or self-sign a gate.

An exact final-line `PUBLICATION_STAGE_PASS` activates only the anonymous
manuscript author. Its exact write universe is:

- `paper/main.tex`;
- `paper/references.bib`.

No section file, macro file, style or class file, figure, external asset,
supplementary source, code, data, result, source review, or build artifact is
authorized directly by this verdict. The author performs static checks only
and stops with stable source hashes and byte counts.

## Deterministic builds, validation, cleanup, and review chain

Building remains closed after this publication verdict and after source PASS
alone. Round 0 additionally requires stable exact source bytes, exact 21-file
source-PASS universe, absence of every later path, and a separate explicit
build GO.

Each build round requires exactly two distinct, new, empty, builder-owned,
non-symlink roots under `/tmp`, matching respectively
`^/tmp/p16-paper16-r0-[A-Za-z0-9]{8}$` and
`^/tmp/p16-paper16-r1-[A-Za-z0-9]{8}$`. Both runs in a round use identical
source bytes, the same frozen absolute `pdflatex` and `bibtex` identities, the
exact UTC/C environment with `SOURCE_DATE_EPOCH=1786924800`, and exactly this
four-command sequence:

1. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`;
2. `bibtex main`;
3. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`;
4. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`.

All eight exits must be zero. Within a round, both PDFs and both `main.bbl`
files must be byte-identical; a mismatch cannot be resolved by selecting one
run. Builders may not edit source, access the network, install software,
rasterize, invoke shell escape, run CAS or science, or persist intermediates.

Both rounds require strict checks for errors, warnings, undefined references
or citations, repair markers, missing glyphs or fonts, overfull boxes, exact
title and structure, page boundaries and nonempty pages, the four proof tables,
zero figures and images, exact seven-key citation-set equality, theorem and
proof content, public-text hygiene, anonymity, metadata, embedded/subset fonts
with Unicode maps, and forbidden PDF forms, attachments, scripts, launch
actions, rich media, and annotations. Every validation executable entering a
receipt is bound by absolute path, hash, and complete version.

Round 0 may persist only `paper/main_round0.pdf` and the strict canonical
`paper/BUILD_RECEIPT_R0.json`. Round 1 may persist only
`paper/main_round1.pdf` and `paper/BUILD_RECEIPT_R1.json`. Each receipt binds
the complete input chain, tool identities, roots, commands, environments,
transcripts, outputs, validation facts, stage universes, and cleanup. Its own
hash and byte count are excluded.

Cleanup is explicitly and recoverably scoped. After all receipt facts are
captured, the builder validates each resolved root and its exact regular-file
allowlist, unlinks every allowed file individually by explicit resolved path,
and removes the empty root with `rmdir`. Recursive deletion, globs, unresolved
variables, and symlink traversal are forbidden. Both roots must be verified
absent before the builder stops.

After Round 0, a fresh R1 reviewer issues either `MANUSCRIPT_R1_PASS` or
`MANUSCRIPT_R1_REPAIR_REQUIRED`. Exactly one bounded revision window follows,
with a mandatory strict canonical `SOURCE_REVISION_RECEIPT_R1.json`; a PASS
produces a byte-identical no-op receipt, while every repair must map to an R1
finding. Round 1 repeats the two-clean-build protocol. A no-op requires the R1
PDF to equal R0 byte for byte. A fresh R2 reviewer then audits the complete
chain; its sole positive final line is `MANUSCRIPT_R2_PASS`, and there is no
second revision window.

Even an exact R2 pass leaves `paper/main.pdf`, finalization, camera-ready
changes, identity disclosure, submission, upload, public release, venue
communication, external messaging, and parallel use of the absorbed
predecessor false. Each requires a separate future lock and fresh independent
review.

## Final disposition and exact effect

All conjunctive publication-stage gates now pass: reviewer independence and
temporal separation; exact repaired-pair identity and bounded no-other-drift
reconstruction; fifteen frozen bindings; strict canonical JSON and self-
exclusion; exact inventory and future absences; theorem, proof, citation,
anti-claim, and absorption fidelity; the eight-section and three-appendix page
contract; zero figures and four proof tables; coherent public-text anonymity;
the unique formal source gate; exact role and stage universes; isolated
deterministic R0 and R1 builds; full validation and safe cleanup; one bounded
revision; fresh R2 closure; and continued finalization and release prohibition.

The sole effect of this review is to authorize anonymous drafting of exactly
`paper/main.tex` and `paper/references.bib` under the repaired frozen contract.
It authorizes no source-level review, build, compilation, finalization,
identity disclosure, submission, upload, release, or external communication in
this turn.

PUBLICATION_STAGE_PASS
