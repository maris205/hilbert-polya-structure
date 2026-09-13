# Independent Paper16 Manuscript Review — Round 2

Date: 2026-08-17 UTC

Candidate: henon_support_size_torus_escape_v1

Manuscript: *Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps*

## Reviewer independence, temporal activation, and method

I am the fresh Round-2 manuscript reviewer. I authored neither public source,
neither build receipt, neither persisted PDF, the Round-1 review, nor the
no-op source-revision receipt. I began the future-artifact portion of this
review only after the explicit R1 BUILDER STOP / ACTIVATE R2 notice. Before
that notice I did not list, stat, hash, open, or otherwise inspect
paper/main_round1.pdf, paper/BUILD_RECEIPT_R1.json, or this future review
path.

After activation I read every one of the 27 allowed Round-2 inputs. I
independently reconstructed PC1, PC2, PC3, the sparse-image lemma, all four
PC1 incidence types, all nine support-one adjacent words, the BA/CB/CBA
continuations, the exact constants, examples, counterexamples, citation
roles, anti-claims, and absorption rule. I also read the full 1,138-line TeX
source, the full 64-line bibliography, and the extracted text of every PDF
page.

No web access, compilation, source edit, temporary file or directory,
rasterization, CAS, symbolic engine, scientific computation, experiment,
data or figure generation, parameter scan, package installation, submission,
upload, external message, or release action was performed. Read-only
parsing, hashing, byte comparison, Poppler inspection, and in-memory PDF
object/text inspection were used only as review evidence. This report is the
sole project-file write made by this review.

## Exact Round-2 input universe

Immediately before this report was created, the project contained exactly 27
regular files in exactly four real directories: experiments, notes, paper,
and refine-logs. There were zero symlinks and zero other entry types. The
observed file set was exactly the publication lock's after_R1_build universe,
with these independently replayed identities:

| Path | Bytes | SHA-256 |
|---|---:|---|
| experiments/EXPERIMENT_PLAN.md | 5,824 | f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6 |
| experiments/EXPERIMENT_TRACKER.md | 1,971 | 4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d |
| experiments/publication_lock.json | 55,924 | 9be9105d43e68ee71c745e9fb8748900bc3605e6918475e393b831f47372449c |
| experiments/source_lock.json | 31,945 | 86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd |
| notes/CITATION_VERIFICATION.md | 10,733 | 6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 7,659 | bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311 |
| notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md | 21,165 | 437e44da869719ef4c74c7de277a162390b6102fc163d96420f7165507ae8f76 |
| notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md | 16,365 | 4cdc119a1590cf9accdbd9f23767a9ca20c287c316ec34cba2ee283e8ea11e0b |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 9,989 | d7493502cf05fb489f5dfe88ce48c6b93c549316bc62f95e617aedb255c399d3 |
| notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md | 20,503 | e61b2857963ff9a64806bb69f585421b52d1d49537b493dce6d09b24ea3850ea |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 13,903 | 046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 14,929 | f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c |
| notes/NOVELTY_ASSESSMENT.md | 7,309 | 83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b |
| notes/PROOF_PACKAGE.md | 16,808 | b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8 |
| notes/PUBLICATION_STAGE_SCOPE.md | 44,353 | 26efa57a0fa024b5272117b1e615da63f631967f9506bbf18df3f3b0bafa30a6 |
| notes/RESEARCH_QUESTION.md | 8,319 | 43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928 |
| paper/BUILD_RECEIPT_R0.json | 84,479 | 6390def39a7dcd1d6eac57a81fcf4e30889b5e358e550d0022679d74ddc1ccb2 |
| paper/BUILD_RECEIPT_R1.json | 84,163 | 7285916176945eaa1ee70224afa3b37ac65c1712ad3feeb0befcb408b36b5e76 |
| paper/PAPER_PLAN.md | 34,681 | 875d26506ba552c79fe62fe11ac1a70e73e1a00245e8bb1aacc1b5c58753d336 |
| paper/SOURCE_REVISION_RECEIPT_R1.json | 9,333 | cf389ab3e02733b97c6af868a16253141d74417128ed1e262ddd9aafd94e10cb |
| paper/main.tex | 80,488 | 2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9 |
| paper/main_round0.pdf | 442,639 | b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f |
| paper/main_round1.pdf | 442,639 | b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f |
| paper/references.bib | 2,019 | 62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f |
| refine-logs/FINAL_PROPOSAL.md | 5,387 | 220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540 |
| refine-logs/INITIAL_PROPOSAL.md | 4,253 | 329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2 |
| refine-logs/REVIEW_SUMMARY.md | 5,479 | 20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a |

Before the sole write, notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md was absent.
The entire remaining finalization universe was absent as a consequence of the
exact 27-file match. In particular, paper/main.pdf,
paper/main_round2.pdf, paper/BUILD_RECEIPT_R2.json, and
paper/FINAL_RELEASE_MANIFEST.json were absent.

## Six-node canonical JSON graph

The canonical JSON graph has six nodes:

1. experiments/source_lock.json;
2. experiments/publication_lock.json;
3. paper/BUILD_RECEIPT_R0.json;
4. paper/SOURCE_REVISION_RECEIPT_R1.json;
5. paper/BUILD_RECEIPT_R1.json; and
6. the frozen upstream Paper14 FINAL_RELEASE_MANIFEST.json at SHA-256
   e832be91a990d1d1caf7e2b4aba40fa8d9a1196524c815e03b30309df6226e68.

I directly replayed strict canonicalization for the five in-universe JSON
nodes. Each is strict UTF-8 with no BOM or CR, compact separators, recursive
Unicode-code-point key order, exactly one terminal LF, no duplicate object
keys, and no nonfinite number. Parsing and recursively sorted compact
serialization reproduced each file byte-for-byte. Synthetic duplicate-key,
NaN, positive-infinity, and negative-infinity probes were all rejected. Each
node excludes its own byte count and SHA-256 and declares the applicable
self-exclusions.

The sixth node is outside the Round-2 read allowlist, so I did not reopen it.
Instead I verified the allowed, frozen source-lock review at SHA-256
f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c.
That independent review binds the manifest at 32,293 bytes and the SHA-256
above and records its successful strict canonical compact-JSON round trip.
This preserves both the six-node graph and the Round-2 read boundary.

All R1 receipt bindings use unique safe relative paths and match the observed
objects. The R1 all_after_revision_inputs, prebuild, prewrite, and postwrite
universes have their exact declared cardinalities and identities. Receipt
self-exclusion is intact.

## Round-1 findings and no-op revision disposition

The Round-1 review is unchanged at 21,165 bytes and ends exactly with
MANUSCRIPT_R1_PASS. Its required-repair count is zero and its cosmetic-repair
count is zero. It records one accepted transient build observation,
R1-OBS-001, rather than a finding. The conventional Table-4 top-float
placement was explicitly accepted as legible and logically anchored.

The canonical source-revision receipt binds that review and records exactly:

- action NO_OP;
- zero changed paths and an empty change ledger;
- empty-diff SHA-256
  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855;
- no theorem, bibliography, layout, or metadata change;
- one authorized revision window consumed, zero remaining, and zero source
  edits; and
- byte preservation of both public source files.

I independently rehashed paper/main.tex to
2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9
and paper/references.bib to
62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f.
These are the exact pre-R1 identities. The R0 and R1 PDFs are also
byte-for-byte identical, not merely equal in length or extracted content.
Thus the required no-op implication is satisfied.

## Deterministic build and cleanup replay

Both build receipts bind two independent clean builds. Across R0 and R1 this
gives four clean roots, sixteen successful build-command exits, four
byte-identical final PDFs, four clean final logs, and four identical BBLs. The
R1 roots are:

- /tmp/p16-paper16-r1-3T3EwQtl;
- /tmp/p16-paper16-r1-7iCBzHwq.

They are distinct, match the locked R1 regex, have /tmp as resolved parent,
were new empty non-symlink builder-owned directories, received exact source
copies, and ended with exactly the eight allowed regular files. The R0 roots
likewise match their own locked regex and protocol.

Every run used the same four-command sequence:

1. pdflatex with nonstop, halt-on-error, file-line-error, and no-shell-escape;
2. bibtex main;
3. the same pdflatex command;
4. the same pdflatex command.

The deterministic environment is exactly TZ=UTC, LC_ALL=C, LANG=C,
SOURCE_DATE_EPOCH=1786924800, and FORCE_SOURCE_DATE=1. All sixteen command
exit codes across the two receipts are zero. The recorded build, validation,
and orchestration executable identities still match their resolved
executables.

For each run, command warning-event counts are [119, 0, 10, 0]. These are the
fully enumerated clean-directory bootstrap reference, citation, summary,
label, and output-rerun events accepted as R1-OBS-001. The corresponding
command transcripts are identical across A/B and across R0/R1. The combined
transcript is 30,185 bytes at SHA-256
6d4255de4ecd3e667955bd029a974712a66b2242b2fed9ac9f1a3d242fff4dcf.

Every final log is 25,226 bytes at SHA-256
a2fc5a1655350c39f897fefc70cba9225cdcca5765c9587aa484b570653fcb3e
and has zero errors, warnings, undefined references or citations, overfull or
underfull boxes, and missing glyph events. Every main.bbl is 1,586 bytes at
SHA-256
ded1b190bcef76e90ee59429b7939f87fa87c229df597d926947b8732a7f368b,
and every BibTeX log is semantically clean. No retained warning exists.

Both receipts record explicit per-path unlink operations and rmdir, with no
recursive deletion, glob, unresolved target, or symlink traversal. I
independently verified absence of all four build roots and all sixteen
declared transcript paths. No build intermediate or undeclared project
artifact remains.

## Source structure, citations, public text, and anti-claims

The source has the exact title, visible Anonymous byline, empty date, and
empty author, subject, keyword, creator, producer, creation-date, and
modification-date PDF fields. The deterministic pdfTeX controls suppress
dates, identity-bearing producer information, and trailer ID.

The abstract has 181 words under the locked conservative math-collapsed
count and 190 raw whitespace tokens, both within 180--220. It starts with
PC1 and the exact bound, identifies vanishing proper subsums as the obstacle,
states the graph/root-fiber and second-recurrence mechanism, and ends with
PC2 and the support-one contrast. It has no citation, provenance, publication
history, or priority language.

The source contains exactly eight main sections, Appendices A--C, and final
References in the locked order. There are exactly four proof-table
environments, zero figure environments, zero includegraphics commands, and
zero external assets. All four tables are surrounded by derivations in the
main text. There are 75 unique labels, 108 reference commands, and no
undefined reference target.

The exact cited-key set, bibliography-entry-key set, and generated BBL key set
are equal and have cardinality seven:

- amorosoViada2009;
- bellGhioca2024;
- ess2002;
- jiXieZhang2026;
- kimEtAl2025;
- kriegerEtAl2015;
- melloYasufuku2026.

There is no wildcard nocite, duplicate key, missing entry, uncited entry, or
predecessor bibliography entry. The citation roles remain exact:

- Amoroso--Viada Theorem 6.2 is the sole external proof input, with its
  algebraically closed characteristic-zero and nondegenerate-only scope.
- Evertse--Schlickewei--Schmidt Theorem 1.1 is historical quantitative
  context only.
- Krieger et al. Theorem 1.7 is the monic S-integral image result, Theorem
  1.8 is the exceptional-coefficient valuation statement, and Corollary 1.9
  is its number-field one-orbit consequence.
- Bell--Ghioca Theorem 1.1 remains a fixed-orbit,
  finitely-generated-subgroup result with arithmetic progressions and a
  residual; regularity only makes the residual finite.
- Ji--Xie--Zhang Theorem 1.8 and Corollary 1.9 remain non-density results.
- The Mello--Yasufuku large- and small-epsilon regimes and additional divisor
  assumptions are not merged.
- Kim et al. Theorems A and B retain their odd-degree,
  degree-at-most, congruence, and construction restrictions.

The exact public-safe absorption paragraph occurs once, in Section 8.3, and
nowhere prohibited. It makes the present manuscript the sole intended
external vehicle for the fully reproduced support-one material, forbids
parallel submission of the predecessor, and gives PC3 no renewed novelty
credit.

Section 8 contains all 21 locked anti-claims. It asserts no
positive-characteristic analogue; no PC1 theorem with c=0, a=0, or a zero
displayed b_j; no syntactic support convention; no conjugacy invariance; no
optimal constants; no effective enumeration; no height estimate; no
periodic, rational-periodic, or integral-cycle classification; no
classification of all exceptional coefficient strata; no arbitrary-map,
arbitrary-automorphism, Hénon-composition, or normal-form theorem; no
arbitrary-subgroup extension; no replacement of finite rank by finite
generation; no coefficient membership in Gamma; no additive closure of
Gamma; no priority or absence-of-unpublished-work claim; no strengthening of
Bell--Ghioca, Ji--Xie--Zhang, Mello--Yasufuku, or Kim et al.; no code, CAS,
computation, scan, experiment, data, or numerical theorem evidence; and no
black-box or renewed-novelty treatment of PC3.

No acknowledgment, grant, manuscript-author name, affiliation, email,
self-identifying link, governance status, review verdict, internal candidate
identifier, internal project number, hash, filesystem path, repository
identity, submission identifier, or operational instruction appears in the
public manuscript or rendered PDF. Neutral bibliography names and frozen
version dates appear only in their permitted bibliographic role.

## Independent mathematical reconstruction

### Quantitative input and sparse-image lemma

For q at least two and R nonnegative, the manuscript fixes

A(q,R) = (8q)^(4q^4(q+R+1)).

It uses Amoroso--Viada only after embedding K and Gamma into an algebraic
closure. This inclusion preserves the abstract rank of Gamma, every monomial
tuple group has rank no larger than its source, and every K-solution injects
into the algebraic-closure solution set. No descent or equality of the two
solution sets is claimed. Coefficients remain fixed coefficients of the
linear equation and are never adjoined to the variable group.

For a q-term sparse polynomial F and lambda nonzero, the normalized variables
(t^m_1 u^-1, ..., t^m_q u^-1) form an image of Gamma^2 of rank at most 2r.
The nondegenerate contribution is at most d A(q,2r): a coordinate ratio fixes
a positive power of t of degree at most d, and the original equation then
fixes u. A degenerate witness has size 2 through q-1. There are exactly
2^q-q-2 such subsets; each gives a nonzero polynomial of degree at most d,
and each root fixes u. This proves

S_q(d,r) = d(A(q,2r)+2^q-q-2).

The reasoning remains valid with arbitrary, including infinite, torsion
because every residual fiber is bounded by polynomial degree rather than
group size.

### PC1: support at least two

With Q=(v,u), H(Q)=(z,v), and H^2(Q)=(w,z), the first recurrence is normalized
as

Z + U + sum_j M_j = 1,

where Z=z/c, U=-au/c, and M_j=-b_j v^(e_j)/c. The variable tuple
(z,u,v^(e_1),...,v^(e_s)) is an image of Gamma^3 of rank at most 3r. Its
nondegenerate locus contributes at most d A(s+2,3r).

For a vanishing proper subsum, membership of Z and U gives exactly four
types:

- GZ: z=B_J(v) and -au=c+B_(J^c)(v);
- GU: au=-B_J(v) and z=c+B_(J^c)(v);
- R0: B_J(v)=0 for |J| at least two;
- R1: c+B_J(v)=0 for a nonempty complementary J.

For GZ and GU, J=[s] leaves the all-monomial side with s terms, while |J|=1
leaves the complementary constant-plus-monomial side with s terms. Thus one
side always has at least two terms and costs at most S_*; the fixed multiplier
a is a coefficient, not a group-membership assumption. Each graph family has
2^s-1 labels.

For R0, factoring the least power gives at most
e_max(J)-e_min(J) nonzero roots. For R1, c+B_J has at most e_max(J) roots.
For each root v=rho, the second recurrence is

w = (c+a rho) + sum_j b_j z^(e_j).

It has s+1 terms unless the constant cancels, and exactly s at least two terms
if it does. The sparse-image lemma therefore closes every vertical fiber, and
the first recurrence uniquely recovers u. Unioning all labels deliberately
overcounts simultaneous witnesses and omits none.

The resulting component budget is exactly

M(e) = 2(2^s-1)
       + sum_(|J|>=2)(e_max(J)-e_min(J))
       + sum_(J nonempty)e_max(J),

so

#T_2 <= d A(s+2,3r) + M(e) S_*.

The maximum and spread subset counts independently reproduce both checksum
formulas in the source. They are checksums, not replacement definitions.

### PC2 and essential hypotheses

For every prescribed support with s at least two, the choice K=Q,
a=b_j=1, c=-s, and Gamma generated by 2 has P(1)=0 and

(1,2^n) -> (2^n,1).

The distinct initial states give infinite T_1 in rank one, so the PC1 window
is sharp. The c=0 example

(t,t^d) -> (t,t) -> (t^d,t)

for P=X^d+X and a=-1 gives infinite T_2. The a=0 example for
P=-1+X+X^2 sends

(1,t) -> (1,1) -> (1,1),

so the triangular map forgets its free coordinate. These are exact
coefficient-uniform boundary failures, not extensions or classifications.

### PC3: support one

For P(X)=c+bX^d, each of the four local equations for T_4 has a rank-at-most
3r variable triple. Unioning a nondegenerate local equation over the four
indices contributes 4d A(3,3r).

On the all-degenerate locus, the three pair-cancellation labels are exactly

- A_i: x_(i-1)=-c/a and x_(i+1)=b x_i^d;
- B_i: b x_i^d=-c and x_(i+1)=a x_(i-1);
- C_i: b x_i^d=-a x_(i-1) and x_(i+1)=c.

Direct substitution reproduces all nine adjacent words. Only BA and CB can
remain free after two labels. BA has chain

t, alpha, at, b a^d t^d

and each of BAA, BAB, BAC gives a nonzero equation of degree at most d^2.
CB requires b c^(d-1)=-1 and has chain

-b t^d/a, t, c, at.

CBB and CBC close with degree d. Only CBA remains free, and only when a=-1.
Under both compatibilities its chain is

b t^d, t, c, -t, b(-t)^d.

Each fourth label CBAA, CBAB, or CBAC closes it with degree at most d^2.
Consequently every one of the 3^4=81 words has at most d^2 initial states.
The word union covers simultaneous labels without a disjointness assumption,
giving

#T_4 <= 4d A(3,3r) + 81d^2.

For sharpness, choose c^(d-1)=-1, K=Q(c), b=1, a=-1, and Gamma generated by
2, c, and -1. The last two generators are torsion, so the group has rank one.
For t=2^n the scalar order is

t^d, t, c, -t, (-t)^d.

All four states through H^3 lie in Gamma^2 and the initial states are
distinct, proving infinite T_3. PC3 is complete internally and remains
subordinate to PC1.

## PDF content, pagination, layout, fonts, and security

The persisted R1 PDF is 442,639 bytes at SHA-256
b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f.
It is byte-identical to the R0 PDF.

The PDF has 27 nonempty letter-size pages with zero rotation. Pages 1--26 are
mathematical content, including Appendices A--C, and page 27 alone contains
References. This satisfies the locked 24--26 content-page interval. The
nonwhitespace character counts by page are:

[1821, 1868, 2831, 3564, 2964, 2278, 2556, 1262, 2240, 2322, 1123, 1338,
2603, 2363, 2252, 1865, 1086, 1147, 2530, 2547, 2736, 1765, 2166, 1804,
2004, 1721, 1050].

The main headings begin on pages 1, 4, 6, 8, 10, 15, 16, and 21. Appendices
A, B, and C begin on pages 23, 24, and 26. References begins on page 27.
Table 1 is on page 11, Table 2 on page 17, and Tables 3--4 on page 18. The
page-18 float placement remains readable and correctly anchored to the
surrounding continuation argument.

I read the layout-preserving extraction of every page. An independent text
block audit found every nonempty block within its 612-by-792 page rectangle;
there is no clipped or out-of-page block. All pages are nonempty, no proof
step is lost at a break, and all four proof tables remain legible in the
extracted reading order. This was a non-raster audit.

The PDF has exactly 24 font rows. Every row is embedded, subset, and equipped
with a Unicode map. There are zero images and zero image XObjects, zero
figures, zero embedded files, zero file-attachment annotations, zero forms or
XFA, zero widgets, zero JavaScript or JS actions, zero Launch actions, zero
RichMedia objects, and zero URI, file, or other external/dangerous links.
All 116 links are internal destinations and resolve to valid pages. The
document is unencrypted.

The visible title is exact and the visible byline is Anonymous. Author,
subject, keywords, creator, producer, creation date, and modification date are
empty. There is no custom metadata stream, identity-bearing metadata, trailer
ID, manuscript-author disclosure, or forbidden public text.

## Findings and Round-2 disposition

### Required findings

There is no critical, major, minor, mathematical, citation, structural,
layout, anonymity, reproducibility, security, governance, inventory, or
lifecycle finding. The required-finding count is zero.

### Cosmetic findings

There is no cosmetic defect warranting an edit. The cosmetic-finding count is
zero. R1-OBS-001 remains a fully resolved transient build observation, not a
finding, and the no-op revision was correct.

### Final conjunctive gate

Every Round-2 conjunct passes:

- exact temporal activation and reviewer independence;
- exact U_R1 = 27 regular files / 4 directories / 0 symlinks / 0 other
  entries;
- exact identities for all 27 allowed inputs;
- strict six-node canonical JSON graph and self-exclusion;
- zero-finding Round-1 review and exact canonical no-op revision;
- preserved source identities and byte-exact R0/R1 PDFs;
- two deterministic clean R1 builds, with the R0 baseline independently
  consistent;
- clean final logs, exact BBL/citation closure, accepted bootstrap events,
  safe cleanup, and absent roots/transcripts;
- complete PC1, PC2, and PC3 proofs with the exact constants, examples,
  counterexamples, four proof tables, citations, anti-claims, and absorption;
- 27 total pages with 26 content pages and References last;
- exact anonymity, fonts, links, metadata, public text, layout, and PDF
  security; and
- no prohibited action or undeclared artifact.

The sole addition of this report yields the locked U_V2 universe of 28 regular
files in the same four directories, with zero symlinks and zero other entry
types.

This PASS authorizes no further source revision, paper/main.pdf, finalization,
release, submission, upload, identity disclosure, or external distribution.
Any later lifecycle action requires its own separately authorized stage.

MANUSCRIPT_R2_PASS
