# Independent Paper 25 post-ledger final source review

Date: 2026-08-26

Role: a fresh final full-source reviewer after the bounded status-ledger repair, distinct from the Paper 25 authors, all earlier source reviewers, both order auditors, and the ledger-repair author.

Gate consumed: `PAPER25_SOURCE_R2_POST_LEDGER_REVIEW_OPEN`.

Disposition: finding-free.  The blocker, major, minor, ambiguity, theorem, citation, metadata, page, inventory, firewall, permission, and lifecycle finding counts are each zero.  No build was run.  This review file is the sole write made by this review and does not authorize a TeX/BibTeX/PDF build, release, repository action, Paper 26 action, or external effect.

## Complete read set and stable inputs

I read `BATCH_06_STATUS.md` and `BATCH_06_IDEA_REPORT.md` from their first physical bytes through their terminal newlines.  Their identities at both the substantive review and the final pre-write stability check were:

- `BATCH_06_STATUS.md`: SHA-256 `f3628ce8ad3df0dc29b7cb766cd5c55b4b5ee3015cc5802b408649934ad820a8`, 222087 bytes, 3184 LF;
- `BATCH_06_IDEA_REPORT.md`: SHA-256 `09e32d05b666908d5597059c0242742d5db1fec748c1c8f7d8c9d53661b2e1f8`, 390829 bytes, 7330 LF.

Both are regular 0644, one-link, valid UTF-8 files with a terminal LF and without a BOM, CR, or NUL.

Before reviewing the paper I read the complete paper-write skill (`/root/.codex/skills/paper-write/SKILL.md`, 363 lines) and every reference it routed for this task: `references/writing-principles.md` (525 lines), `references/venue-checklists.md` (73 lines), and `references/citation-discipline.md` (431 lines).  I then read every one of the following 23 Paper 25 project files to physical EOF:

- `experiments/EXPERIMENT_PLAN.md`, `EXPERIMENT_TRACKER.md`, `publication_lock.json`, and `source_lock.json`;
- `notes/CITATION_VERIFICATION.md`, `CLAIMS_EVIDENCE_MATRIX.md`, `INDEPENDENT_PAPER_PLAN_REVIEW.md`, `INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`, `INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`, `INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, `INDEPENDENT_SOURCE_LOCK_REVIEW.md`, `NOVELTY_ASSESSMENT.md`, `PROOF_PACKAGE.md`, `PUBLICATION_STAGE_SCOPE.md`, and `RESEARCH_QUESTION.md`;
- `paper/PAPER_PLAN.md`, `PAPER_PLAN_R1.md`, `main.tex`, `math_commands.tex`, and `references.bib`;
- `refine-logs/FINAL_PROPOSAL.md`, `INITIAL_PROPOSAL.md`, and `REVIEW_SUMMARY.md`.

The independent final census was exactly 23 regular files, four directories, no symlink, and no other node, totaling 550367 bytes and 9543 LF.  Every file was mode 0644, link count one, valid UTF-8, terminal-LF terminated, and free of BOM, CR, and NUL; the four directories were mode 0755.  Removing the three source files gives the locked L20 census of 20 files, 497097 bytes, and 8587 LF.  The three source files contribute exactly 53270 bytes and 956 LF.

The current source trio independently rehashed as:

| file | SHA-256 | bytes | LF |
|---|---:|---:|---:|
| `paper/main.tex` | `a8f045c5243c3614ada39d01664b833c4057abb566e3da7e44d285ce7973cd63` | 49427 | 827 |
| `paper/math_commands.tex` | `c748e0cde8aadef85c5de9e1fa20efb7770d07fb3fde58dfe0f4fe738720edf0` | 393 | 11 |
| `paper/references.bib` | `159acd5633b19f3f91c203d4f85375cfe5ddaaee6337fd5297c673ac1b9ad99d` | 3450 | 118 |

Each is a regular 0644, one-link, ASCII-subset-of-UTF-8 file with byte `0a` at physical EOF and no BOM, CR, or NUL.

## Lock and aggregate recomputation

I did not accept either JSON lock as self-authenticating.  A Python parser rejecting duplicate keys, nonfinite constants, and floats and an independent Ruby parser using duplicate-rejecting hashes plus recursive no-Float and key-order checks both accepted the live locks.  In each case compact sorted-key reserialization plus one terminal LF reproduced the original bytes exactly.  Hostile duplicate-key, NaN, positive-Infinity, negative-Infinity, and floating-number fixtures were rejected.

The source lock has 24 top-level keys, 66 JSON objects, and 23 arrays.  Its ten locked rows matched independently read file size, LF count, SHA-256, node type, mode, link count, terminal LF, UTF-8, BOM, CR, and NUL properties.  The T10 set is exactly ten files, 97546 bytes, 2647 LF, and 288 path bytes.  Sorting by bytewise path and framing each row as

    uint64be(path_bytes) || path || uint64be(file_bytes) || file

produced 97994 bytes and SHA-256 `e92a6133694e5868e47525981f07e7335617a8f7e5bf84fd8b205743be3e2902`.  The independently rendered sorted text ledger was 1039 bytes with SHA-256 `675e62edf7ddaf74c7a16a845039ef9140a69cd2b28937e8c2294f9368ba83e4`.

The publication lock has 23 top-level keys, 228 JSON objects, and 67 arrays.  All 18 publication rows matched their live files.  L18 is exactly 18 files, 397504 bytes, 8086 LF, and 552 path bytes.  Prefixing `paper25-publication-prelock-v1` plus NUL to the same explicit framing yielded 398375 bytes and SHA-256 `78f1a0a41476c33f3d3767001ed301f6b1f0f5c1c2146101b731cc2bddd2861c`.  Adding the publication-lock file gives L19 = 19 files, 467339 bytes, and 8087 LF.  Thus the source lock, publication lock, their framed aggregates, and the live L23 census agree without relying on a stored report.

## Exact R2 and R1 byte-chain audit

Starting from the current `main.tex`, I reversed the five R2 substitutions in memory.  Every old/new context occurred exactly once:

1. `Choose $v_\rho,\ell>0$ with` back to `Choose $r,\ell>0$ with`;
2. `Cv_\rho=\rho v_\rho` back to `Cr=\rho r`;
3. `\ell^{\trans}v_\rho=1` back to `\ell^{\trans}r=1`;
4. `e_1^{\trans}v_\rho` back to `e_1^{\trans}r`;
5. `n\geq n_0` back to `n\geq N_0`.

The result was exactly SHA-256 `167039b8d6e0199821558b424f0941a1d1dd886310a96b7cd3869151a7e19330`, 49402 bytes, 827 LF.

I then reversed the five R1 changes, again with unique complete contexts: `spectral prediction` to `spectral candidate`; `proposed fresh momentum vector` to `candidate fresh momentum vector`; `proposed fresh position vector` to `candidate fresh position vector`; `these proposed vectors` to `these candidates`; and removal of `, and its reduction modulo $p$ is $t^d-c$` from Theorem H(iii).  This yielded exactly SHA-256 `597323ad7e613f13d7646dfab568cbf1b47b156e9e31df475c52fab79d791f76`, 49356 bytes, 827 LF.

Applying those same five R1 edits forward recovered the R2-preimage byte for byte; applying the five R2 edits forward then recovered the live source byte for byte.  A full diff of each adjacent state contained precisely those five intended changes and no sixth change.

A case-insensitive whole-word scan of the source trio found zero occurrence of `candidate` or `candidates`.  The retired Perron-vector use of `r` and the retired threshold `N_0` are absent.  Current `r` is used only for stacked row rank, `N` only for the structural ambient dimension, and lowercase `n` only for iteration.  The Perron vector is consistently `v_\rho` and the eventual threshold is consistently `n_0`.  Theorem H(iii) explicitly states both irreducibility over `\mathbb Q` and reduction modulo `p` equal to `t^d-c`.

## Independent mathematical review

The hypotheses, quantifiers, boundary cases, selectors, carries, visibility, noncancellation arguments, arithmetic construction, Perron argument, scalar recurrence, and sharpness claim were checked directly against `main.tex`, not inferred from the proof package.

- Structural Theorem S is algebraically exact.  From `C-I=[RSP-P,-R][Q;S]`, the row-basis factorization `Y=LT_0` and `X=UL` give the rectangular Sylvester identity and
  `\chi_C(t)=(t-1)^{N-r}\det((t-1)I_r-T_0X)`.  The reduced factor is monic of degree `r`.  The text correctly permits extra unit roots and handles `r=0` and `r=N` without claiming exact unit multiplicity or a rank-only spectral profile.
- The parameter order is noncircular: choose `d`, then `p,c`, then ordered integer lifts `a_i`, and only then a common sufficiently large `b`.  The literal gradients, subtraction inverses, symplecticity, selected matrices `D` and `B_0`, and strict positivity of `C=B_0D` are correct.
- The broad-cone spike selector and its strict invariance follow from the displayed ratio inequalities.  The fine chamber uses the correct coordinate, ratio, and weighted walls.  Both temporal carries are bounded, the global cross-block comparison is strict, and positive-coefficient semiring propagation prevents top-form cancellation.  The fixed `q_1` visibility statement therefore supports the exact degree formula for every `n\geq0`, including the tie at `n=0` and uniqueness for `n\geq1`.
- The determinant-lemma characteristic-polynomial formula and all modular signs are correct.  The full finite-field binomial irreducibility criterion is applied with all prime-divisor conditions, the `d=2` boundary, and the additional condition when `4\mid d`; it is not shortened to an invalid one-condition test.
- Strict positivity supplies a simple Perron root and spectral gap.  The claimed `\rho>1` needs no hidden assumption: `C` has positive integer entries and `d\geq2`, so for a positive left Perron vector `\ell`, `\ell^\trans C\one\geq d\,\ell^\trans\one>\ell^\trans\one` and hence `\rho\geq d>1`.  Irreducibility of the degree-`d` characteristic polynomial makes the Perron algebraic degree exactly `d`.
- Reachability and observability are both proved by the relevant Bezout/cyclic-vector argument.  Their product gives a nonsingular size-`d` Hankel block.  Cayley--Hamilton supplies an order-`d` recurrence, while Hankel rank excludes every smaller rational recurrence both from `n=0` and on any eventual tail.
- Corollary C uses `D=-I+I(D+I)` and `B_0=-I+(b\one)\one^\trans`.  Since `D+I` is invertible, the selected stacked row rank is `d`; irreducibility excludes the factor `t-1`.  This proves existential sharpness exactly for the constructed ranks and does not claim ranks zero or one.

The fifteen labeled proof units were separately checked in their stated dependency order:

1. L1: full-row-basis factorization and rectangular Sylvester identity;
2. L2: common-kernel sector and both rank boundaries;
3. L3: ordered residue lifts and one simultaneous large-`b` choice;
4. L4: literal gradients, inverses, symplecticity, and selected matrices;
5. L5: broad-cone strict spike selection;
6. L6: strict broad-cone invariance and global cross-block domination;
7. L7: fine visibility-chamber invariance;
8. L8: both temporal carries;
9. L9: positive-semiring top-form survival;
10. L10: exact ordinary-degree visibility;
11. L11: characteristic-polynomial formula;
12. L12: modular reduction and the full binomial check;
13. L13: Perron dynamical and algebraic degree;
14. L14: reachability, observability, Hankel rank, and scalar order;
15. L15: selected rank-`d` sharpness.

The paper's anti-claims are accurate and effective: it does not claim realization of all Perron or weak-Perron numbers, classification, minimal dimension, optimal sparsity, ranks zero or one, inverse or higher dynamical degrees, compactification, entropy, integrability, orbit classification, a positive-characteristic theorem, genericity, nonconjugacy, priority, or proof transfer.  The construction and sharpness claims remain existential.

## Bibliography, citations, and locators

The bibliography contains exactly 12 distinct entries (`BvS`, `SS`, `DF`, `BT`, `KL`, `Des`, `AX`, `HS`, and the four `Std...` books).  The source contains 26 citation commands and 32 cited-key mentions, covers all 12 keys, and has no missing, unused, or duplicate key.  Every factual use remains contextual; no external proof is imported.

The BT record preserves both manifestations: the 2025 Israel Journal of Mathematics version-of-record title `Generators of Groups of Hamiltonian Maps`, volume 267, issue 1, pages 237--252, with DOI, and the arXiv manifestation's literal title `Generators of groups of Hamitonian maps`.  They are one bibliographic work, not two silently merged works.

The eight standard-source locator records were checked against the four locked books:

1. Kailath, Appendix A.12, page 651;
2. Ireland--Rosen, Chapter 16, Section 1, Theorem 1, page 251;
3. Ireland--Rosen, Chapter 4, Section 1, pages 39--41;
4. Kailath, A.12 and A.26(2), pages 651 and 658;
5. Dummit--Foote, Chapter 9, Sections 9.3--9.4, pages 303--308;
6. Meyer, Section 8.2, page 667;
7. Kailath, Appendix Section 8, pages 658--659;
8. Kailath, Sections 2.2--2.4, 5.1, and 6.5.

The separate HS citation points to Section 2.1, Lemma 6, page 4 and states the full three-clause binomial criterion, including the `4\mid d` clause.  The source verification ledger independently closes the eight contextual records and STD01--STD08 to these four standard works; titles, authors, years, journal data, DOI/arXiv information, and locators agree with `references.bib`.

## Static TeX, metadata, and page contract

No TeX engine, BibTeX, PDF tool, or build root was invoked.  Static inspection gives:

- exact class `article` with options `11pt,letterpaper`;
- exactly the 15 packages `inputenc`, `fontenc`, `lmodern`, `geometry`, `microtype`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `array`, `booktabs`, `enumitem`, `hyperref`, `hyperxmp`, and `bookmark`;
- exactly one system input, `glyphtounicode.tex`, and one local input, `math_commands.tex`;
- bibliography style `plain` and database `references`;
- eight sections in the locked order, 39 subsections, one table, zero figures, and no appendix;
- exactly the 18 theorem-like statements H, S, C, and L1--L15; balanced environments and braces; 12 balanced explicit proof environments, with the remaining proof units presented in the immediately following prose;
- no TeX comment, shell escape, file-write primitive, external read, undeclared local import, style file, private path, identity, hash, gate, lock token, project inventory, or governance prose in any publication source.

The title is exactly `Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears`, the visible author is exactly `Anonymous`, and the date is empty.  The hyperref/XMP title agrees exactly; author, subject, keywords, creator, and producer are empty; XMP basic/mm fields and the PDF trailer ID are suppressed; `\pdfgentounicode=1` is present; and the root bookmark agrees with the title.  A `\clearpage` immediately precedes the level-one `References` bookmark, `\bibliographystyle{plain}`, and `\bibliography{references}`.  The locked contract of 26 content pages followed by References on page 27 is statically credible, but remains explicitly unbuilt and therefore is not misreported as an observed PDF.

`math_commands.tex` consists of exactly 11 macro/operator declaration lines and no prose or I/O.  `references.bib` has no comment, preamble, string macro, private field, or uncited entry.  The source/publication firewalls are therefore intact.

## Global lifecycle and permission audit

In the current status ledger the dependency order is now correct and unique:

- review authorization at line 2379 precedes the builder/blocker record at 2415, which precedes the terminal close/discovery block at 2457--2485 and the Paper 25 candidate at 2486;
- the scope author at 2768 precedes the publication-stage pass at 2802, which precedes the lock-author block at 2845--2895, the lock-pass block at 2896--2933, and the source-verification/source-trio record beginning at 2934.

The three relocated status blocks each occur exactly once.  Their independently delimited identities are:

| block | bytes | LF | SHA-256 |
|---|---:|---:|---|
| authorization/builder-close block | 2129 | 29 | `e34247ff20b248ea7f1a91abd1a80e0e78197c9cfe9856e0c4e39ab8ce63a785` |
| scope/stage block | 3651 | 51 | `84a8feda0066b937c7ee9b18c34481a94d17e00f041cca67af57c25bdec386b5` |
| lock/source block | 2782 | 38 | `8ff965c06b5b86ed0070656382932a1250e80675d10a65c1fd62ab3376649827` |

To distinguish a pure move from a rewrite, I reconstructed the immediate pre-repair status bytes in memory.  I removed the unique EOF event beginning `- 2026-08-26: The bounded status-order repair author consumed the corrected`, restored the top gate to

    - Current gate: `PAPER25_ROOT_LEDGER_ORDER_REPAIR_OPEN`

and restored the historical Paper 25 queue row to

    | 4 / Paper 25 | `papers/25-hamiltonian-support-rank-unbounded-perron-degree` | **Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears**; final R2 source review passed every source, mathematics, citation, lock, and static class but correctly made zero writes because three older status-log blocks remain out of dependency order; a status-only mechanical reorder is open, while every project input and compilation remain closed | SOURCE_R2_REVIEW_ZERO_WRITE_LEDGER_ORDER_FINDING_REPAIR_OPEN |

That reconstruction is exactly SHA-256 `ffd69c9daf261680134a81b45ca083faf52a60df201427ad0364a6620041589c`, 219623 bytes, 3150 LF.  Removing the three unique blocks leaves 211061 bytes, 3032 LF, and SHA-256 `e9818588281992d9d87ac392fd213aac605b680db66e2d30b47326a31c769f99`.  The block totals are 8562 bytes and 118 LF, exactly accounting for the pre-repair file.  Reinsertion in current dependency positions, plus only the explicitly recorded current gate/queue/event transition, accounts for the live 222087-byte status ledger.  Thus no block content was changed and no fourth move is hidden.

The IDEA ledger independently has the same lifecycle: Paper 24 terminal close before Paper 25 candidacy; source design before source lock; plan before scope; scope before publication-stage pass; lock author before lock pass/source trio; then the R1 and R2 repairs, the ledger-order finding, and the bounded repair stop.  Its gate-count narrative records that the initially conflated old 216297-byte/3107-LF counts were immediately corrected to the true post-gate 219623-byte/3150-LF identity before the repair author consumed the gate.  The later unsupported numeric-hunk attempt was rejected and had zero filesystem effect; the recorded bare-header patch was the sole effective repair edit.  Current STATUS and IDEA identities therefore agree with both the ordered lifecycle and the no-extra-effect history.

Both JSON locks close their historical action permissions and have empty authorized-write-path sets.  The subsequent serial ledger gate opens only this one conditional review artifact; it does not retroactively open the locks.  The candidate review path was absent at the final pre-write check.  All build, PDF, release, repository, Paper 26, permission-expansion, and external-effect paths remain closed.

I did not access, list, stat, glob, or touch any Paper 23 or Paper 24 historical temporary root.  I did not use the network, a TeX/BibTeX/PDF tool, an A/B build root, the repository, Paper 26, or any external service.

## Read-only diagnostic disclosure

All diagnostic mistakes were read-only and had zero filesystem or external effect:

1. an initial ripgrep NUL expression warned that NUL cannot match in its default text mode; a raw-byte Ruby scan replaced it;
2. the first Ruby canonical-JSON equality compared UTF-8-tagged and ASCII-8BIT-tagged strings and printed false even though their bytes and SHA agreed; byte-normalized equality then passed;
3. an initial Ruby no-Float guard used an always-truthy `tap` result and raised after parsing; the corrected recursive guard passed;
4. an initial publication-row type check compared with `regular` instead of the lock's `regular_file` and emitted 18 false mismatches; the corrected mode/type check passed all 18;
5. the first inverse-chain harness called `count` on an empty replacement and stopped after correctly producing the R2 preimage; a context-counting harness then produced the exact R1 and R2 chain;
6. the first forward-chain harness chose the nonunique phrase `is irreducible over \mathbb Q` and stopped on its three occurrences; the complete two-line theorem context then recovered the current bytes exactly;
7. an initial citation regex contained a closing-class typo and falsely returned zero citations; the corrected parser obtained 26 commands, 32 key mentions, and all 12 keys;
8. one exploratory `FNM_DOTMATCH` directory display included synthetic `.` entries; the census implementation explicitly excluded basename `.` and `..` and returned the exact 23/4/0/0 inventory;
9. one exploratory Ruby aggregate trial produced no validation output and was discarded, and one overbroad one-line-JSON display was truncated; the two complete independent aggregate implementations and full-file reads supplied every reported result;
10. two exploratory theorem/lemma ripgrep expressions returned no match because the paper uses custom environment names; exact `theoremH`, `theoremS`, `corollaryC`, and `lemL...` scans plus the full-source read supplied the stated counts.

None of these diagnostics changed an input, weakened a check, or supplied evidence after it failed; each affected conclusion was recomputed with a corrected independent check.

## Final finding ledger and authorization boundary

| class | count |
|---|---:|
| blocker | 0 |
| major | 0 |
| minor | 0 |
| ambiguity | 0 |
| theorem or proof | 0 |
| citation or locator | 0 |
| metadata or anonymity | 0 |
| page-contract credibility | 0 |
| inventory, identity, or canonicalization | 0 |
| firewall or permission | 0 |
| lifecycle or ledger order | 0 |

The live sources, locks, ledgers, and 23-file inventory remained unchanged at the final stability check.  Creation of this note is the only authorized mutation.  It makes a later parent-controlled dual build eligible; it does not itself authorize or perform that build.

PAPER_SOURCE_R2_NOTATION_REPAIR_PASS
