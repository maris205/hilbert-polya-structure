# Publication-Stage Scope

## Authority and present lifecycle

This document governs the transition from the frozen Paper 14 source design
and passed paper plan to a possible anonymous proof-first manuscript. It is a
governance artifact, not a draft, build, review, or release.

The current state is exactly:

**PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW / NO_DRAFT / NO_BUILD / NO_RELEASE**

The candidate identifier remains
**henon_four_step_torus_escape_v1**, and the safe title remains exactly:

**Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps**

The date of this governance freeze is 2026-08-16 UTC.

The current authority consists of this scope together with the canonical
publication lock. Historical source-package and plan statuses remain
provenance. They do not independently authorize a manuscript or build.

## Frozen-input gate

The publication-stage author rehashed the following twelve inputs before
writing this scope. Each observed byte count and SHA-256 value matched the
frozen identity.

| Frozen input | Bytes | SHA-256 |
|---|---:|---|
| experiments/source_lock.json | 10,716 | f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 12,934 | ea6d13c1ec74bbad0ac8c6cd850d0f0b8c33992d05b5e428308eef3347a18308 |
| paper/PAPER_PLAN.md | 30,112 | 6a0e16e3688714c43c9e9d87054c501d44989e59a523c6ff084eac4c9db3a88f |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 7,992 | 0d1bbb1104e2f709312e1cfe0b3c449eb3bd706654c58f87eaf5b621a3ea5596 |
| notes/RESEARCH_QUESTION.md | 6,371 | 782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c |
| notes/PROOF_PACKAGE.md | 13,728 | c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 5,902 | d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e |
| notes/CITATION_VERIFICATION.md | 12,919 | 0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af |
| notes/NOVELTY_ASSESSMENT.md | 8,660 | 2fafbef234a7e7cc8fbe10b25e0b920188b3c35472538fcbaf023da8d357bac1 |
| refine-logs/FINAL_PROPOSAL.md | 7,814 | 719214a159f1e36676d059c626dcefab7fe11b012e44146243db8aa500eb38a0 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW_R2.md | 12,836 | 8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0 |
| notes/INDEPENDENT_CITATION_PRECISION_AUDIT.md | 21,470 | 7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17 |

The source-lock verdict is exactly **SOURCE_LOCK_PASS**. The paper-plan
verdict is exactly **PAPER_PLAN_PASS**. Neither verdict by itself authorized
drafting, compilation, finalization, identity disclosure, submission, or
release.

## Current authorization state

All present downstream authorizations are false:

| Authorization flag | Current value |
|---|---|
| anonymous draft | false |
| bibliography authoring | false |
| build | false |
| code | false |
| experiment | false |
| figure | false |
| finalization | false |
| identity disclosure | false |
| manuscript review | false |
| result | false |
| source revision | false |
| submission | false |
| public release | false |

The publication-stage governance is frozen, but freezing governance is not
permission to perform any downstream act. The independent
publication-stage review described below is the sole presently permitted
future project write.

## Exact theorem and contribution lock

Let \(K\) be an arbitrary field of characteristic zero, let \(d\ge2\) be an
integer, let \(a,b,c\in K^\ast\), and let
\(\Gamma\le K^\ast\) be a multiplicative subgroup of finite rank \(r\).
Finite generation is not assumed, and no membership condition on
\(a,b,c\), or \(-1\) is imposed. Define
\[
H(x,y)=(b x^d+a y+c,x)
\]
and
\[
T_m(H,\Gamma)
=
\{P\in\Gamma^2:
H^j(P)\in\Gamma^2\text{ for every integer }j
\text{ with }0\le j\le m\}.
\]
Thus \(T_4\) contains five states and four transitions, while \(T_3\)
contains four states and three transitions.

The dominant primary claim is exactly
\[
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\tag{PC1}
\]

The co-primary sharpness claim is exactly: for every integer \(d\ge2\),
there is a number-field example with
\(\operatorname{rank}\Gamma=1\) and
\[
\#T_3(H,\Gamma)=\infty.
\tag{PC2}
\]
The locked explicit family is
\[
b=1,\quad a=-1,\quad c^{d-1}=-1,\quad
K=\mathbb Q(c),\quad
\Gamma=\langle2,c,-1\rangle,\quad
P_t=(t,t^d),\quad t=2^n.
\]

The subordinate periodic corollary counts only exact-period-\(n\) orbits
\(\mathcal O\) whose whole orbit satisfies
\(\mathcal O\subseteq\Gamma^2\). If
\(C_n^\Gamma(H)\) denotes their number, then
\[
\sum_{n\ge1} n C_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\tag{COR1}
\]
No larger one-representative periodic-point claim is authorized.

## Exact proof-content lock

The manuscript must contain the complete proof spine in its mathematical
content. It may improve exposition but may not change any assumption,
quantifier, label, index direction, or bound.

1. For \(H^j(P)=(x_j,x_{j-1})\), the recurrence is
   \[
   x_{i+1}=b x_i^d+a x_{i-1}+c.
   \]
   The inverse map proves injectivity of the passage from initial states to
   local states.
2. The ESS equation is the fixed-coefficient equation
   \[
   \frac1c x_{i+1}
   -\frac bc x_i^d
   -\frac ac x_{i-1}
   =1.
   \]
   Its variable triple
   \((x_{i+1},x_i^d,x_{i-1})\) belongs to \(\Gamma^3\), which has rank
   \(3r\). The three scalars are fixed coefficients; they are not absorbed
   into \(\Gamma\).
3. Evertse--Schlickewei--Schmidt, published Theorem 1.1, gives at most
   \[
   E(3,3r)=\exp\!\bigl(18^9(3r+1)\bigr)
   \]
   nondegenerate triples at one local index. Each triple has at most \(d\)
   local states. The four indices \(0,1,2,3\) therefore contribute at most
   \(4dE(3,3r)\).
4. Local degeneracy is exhausted by the fixed labels
   \[
   \begin{aligned}
   A_i&:a x_{i-1}+c=0,\\
   B_i&:b x_i^d+c=0,\\
   C_i&:b x_i^d+a x_{i-1}=0.
   \end{aligned}
   \]
   The first letter labels index \(i\), the next labels \(i+1\), and so on.
5. The complete nine-transition analysis has only two potentially free
   adjacent words: \(BA\) and \(CB\). Every \(BA\) branch closes at the
   third letter with at most \(d^2\) initial states. The only potentially
   free three-letter extension of \(CB\) is \(CBA\), under
   \(a=-1\) and \(bc^{d-1}=-1\), and that branch closes at the fourth
   letter with at most \(d^2\) states.
6. Every word in \(\{A,B,C\}^4\) has at most \(d^2\) initial states.
   Choosing any valid label at an index covers simultaneous degeneracy;
   overlaps may overcount but cannot omit a point. The \(3^4=81\) words
   contribute at most \(81d^2\).
7. Short periodic orbits require no correction because the proof does not
   assume the five indexed states are distinct.
8. The direct rank-one family proves PC2 through exactly the first three
   transitions, and orbit disjointness plus whole-orbit containment proves
   COR1.

Full transition arrays and expanded algebra may appear in appendices, but no
logical implication needed for PC1, PC2, or COR1 may be hidden exclusively
in an appendix.

## Citation and novelty lock

The manuscript may cite only verified primary sources whose roles are
consistent with the frozen citation record. Bibliographic metadata must be
checked against the primary journal, author-posted, DOI, or arXiv record.
No citation may be fabricated, and no unverified marker may remain.

The following boundaries are mandatory:

- Evertse--Schlickewei--Schmidt, published Theorem 1.1, is the sole external
  proof theorem.
- Bell--Ghioca, Theorem 1.1(i), concerns return times for one fixed orbit of
  a rational self-map of a semiabelian variety to a finitely generated
  subgroup. Under the regular-self-map hypothesis, Theorem 1.1(ii) makes
  only the residual set finite; it does not make the entire return-time set
  finite. The present map is generally rational, not regular, on
  \(\mathbb G_m^2\).
- Kim--Krieger--Postolache--Szeto, Theorem A, applies for odd \(d>2\) to a
  rational polynomial of degree at most \(d\) and yields at least
  \((d-4)^2\) rational periodic points in their general-polynomial Henon
  family. Their Theorem B, for \(d\equiv1\pmod6\), gives an integer cycle
  of length \((8d+10)/3\).
- Mello--Yasufuku, Theorems 1.1--1.2 and Corollary 1.3, are conditional on
  \(\mathrm{Hyp}_\epsilon\), with the main results requiring
  \(\epsilon\ge(1+c)/2\). Their Theorem 4.2, under additional divisor
  hypotheses and Vojta's Main Conjecture, supplies the relevant non-density
  only for sufficiently small \(\epsilon\), and does not verify the general
  main hypothesis.

The collision statement remains a bounded primary-source comparison through
2026-08-16. The manuscript may say that the compared theorems do not supply
PC1 or PC2. It may not make an absolute priority claim. The advisory novelty
score of 7.0/10 is governance provenance, not mathematical evidence and not
publication prose.

## Page, evidence, and visual lock

The publication target is:

- 15--17 pages of mathematical content, excluding references;
- approximately 17--20 total pages including references; and
- a proof-first arithmetic-dynamics journal format, not an ML-conference
  template.

Mathematical content includes the abstract, introduction, theorem statements,
proofs, limitations, and proof appendices. The page envelope refines, without
changing, the passed plan: proof content is never removed merely to hit a
cosmetic target.

There are zero computational experiments, numerical scans, CAS checks,
datasets, empirical figures, and empirical evidence tables. No figure file
is required or authorized. Typeset proof devices such as aligned equations,
the \(3\times3\) transition array, and tabular case splits are allowed inside
paper/main.tex because they are symbolic proof, not empirical evidence.

## Locked limitations and nonclaims

The manuscript must state the following limitations accurately:

- the ESS exponential constant is coarse and unoptimized;
- the \(81d^2\) union bound is coarse and unoptimized;
- there is no complete \(T_2/T_3\) coefficient stratification;
- the result does not cover general polynomial Henon maps, compositions of
  Henon maps, or arbitrary polynomial automorphisms;
- the result is a finite-window theorem, not a general return-time
  classification;
- PC2 is sharp only in transition length, not in either numerical constant;
- the periodic corollary requires whole-orbit containment;
- \(d=1\), positive characteristic, and zero coefficients are excluded; and
- no effective enumeration, height bound, rational-point classification,
  integral-point classification, or periodicity of the sharpness family is
  claimed.

No code, experiment, computation, or figure can be presented as verification
of the transition table or as evidence for a theorem.

## Independent publication-stage review gate

The sole next project write is:

**notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md**

The reviewer must be fresh and independent. The reviewer may not have
authored or modified either governance file, any of the twelve frozen inputs,
or any future manuscript source. The governance author may not review or sign
its own work.

The reviewer must:

1. rehash all twelve frozen inputs;
2. bind and rehash this scope and experiments/publication_lock.json;
3. independently validate strict canonical JSON, including duplicate-key and
   nonfinite-number rejection;
4. verify the current 19-file inventory and zero-symlink condition;
5. confirm that no draft, bibliography, build, figure, code, experiment,
   result, review-round artifact, finalization, release, or submission file
   exists;
6. replay the theorem, proof-dependency, citation-boundary, page, evidence,
   limitation, role, and deterministic-build contracts; and
7. verify reviewer independence and the absence of author self-signing.

Only the exact verdict

**PUBLICATION_STAGE_PASS**

activates the conditional anonymous-draft authorization below. Any other
text, a missing review, a hash mismatch, a noncanonical lock, or an altered
input leaves every downstream authorization false.

## Conditional anonymous-draft contract

After, and only after, an independent review at the sole review path returns
the exact verdict **PUBLICATION_STAGE_PASS** and binds the stable lock hash,
one anonymous manuscript drafter may write exactly:

- paper/main.tex
- paper/references.bib

No other manuscript source is authorized. In particular, there is no
authorization for section files, math_commands.tex, a style file, a figure
file, a figure directory, supplementary material, code, experiment, result,
or build artifact during drafting.

The draft must:

- use a standard self-contained article layout suitable for a focused
  arithmetic-dynamics paper;
- remain anonymous, with no names, affiliations, email addresses,
  acknowledgments, repository identifiers, hidden PDF metadata identity, or
  identity-revealing self-citation;
- contain the exact safe title, theorem assumptions, claims, proof spine,
  citation boundaries, limitations, page target, and zero-evidence policy
  locked above;
- keep all article sections and mathematical proof arrays in paper/main.tex;
- include in paper/references.bib only entries actually cited in main.tex;
- use no shell escape and no external generated asset; and
- end with an explicit author stop and stable SHA-256 and byte count for both
  source files.

The exact pass activates only these two source writes. It does not activate a
build, manuscript review, source revision, finalization, identity disclosure,
submission, or release.

## Exact role read allowlists and write universes

Define the frozen base set \(F\) as the twelve paths in the frozen-input table
above.

Define the governance set \(G\) as
\[
G=F\cup
\{\text{notes/PUBLICATION_STAGE_SCOPE.md},
\text{experiments/publication_lock.json}\}.
\]

Define the passed-governance set \(G^+\) as
\[
G^+=G\cup
\{\text{notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md}\}.
\]

The role contracts are exact:

| Role | Activation | Read allowlist | Project write universe |
|---|---|---|---|
| publication-stage author | present task only | \(F\) | notes/PUBLICATION_STAGE_SCOPE.md; experiments/publication_lock.json |
| independent publication reviewer | stable author stop | \(G\) | notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md only |
| anonymous manuscript drafter | exact PUBLICATION_STAGE_PASS | \(G^+\) | paper/main.tex; paper/references.bib only |
| Round-0 builder | stable draft-source stop plus independent gate check | \(G^+\), paper/main.tex, paper/references.bib | paper/main_round0.pdf; paper/BUILD_RECEIPT_R0.json only |
| Round-1 manuscript reviewer | stable Round-0 build stop | \(G^+\), both draft sources, both Round-0 outputs | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md only |
| bounded revision author | stable Round-1 review stop | prior role inputs plus notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md | paper/main.tex; paper/references.bib; paper/SOURCE_REVISION_RECEIPT_R1.json only |
| Round-1 builder | stable revision stop | \(G^+\), revised sources, both Round-0 outputs, Round-1 review, revision receipt | paper/main_round1.pdf; paper/BUILD_RECEIPT_R1.json only |
| fresh Round-2 manuscript reviewer | stable Round-1 build stop | all frozen governance, source, review, revision, receipt, and Round-0/Round-1 PDF artifacts | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md only |

No role may add a path to its own read or write universe. A reviewer may not
author or revise the object it reviews. A drafter, revision author, or builder
may not issue a review verdict. No author may self-sign a gate.

## Round-0 clean deterministic build protocol

Round-0 building remains unauthorized until the anonymous drafter stops and a
separate gate confirms that only the two authorized sources were written.
When activated, the builder must use the following exact protocol.

### Reproducible environment

Use the same absolute pdflatex and bibtex executables for both runs. Record
their absolute paths, executable SHA-256 values, and full version strings.
For every command, set:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786838400
    FORCE_SOURCE_DATE=1

Use no shell escape, network access, downloaded package, figure, generated
asset, or source mutation. The draft should include pdfTeX-compatible
deterministic metadata controls; the byte-equality gate remains decisive.

### Two clean builds

Create two independent empty temporary directories outside the Paper 14
project. Copy the exact bytes of paper/main.tex and paper/references.bib into
each temporary directory. In each directory, run exactly:

    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight process exit codes must be zero. Each temporary directory may
contain only:

- main.tex
- references.bib
- main.aux
- main.bbl
- main.blg
- main.log
- main.out, if emitted
- main.toc, if emitted
- main.pdf

No other generated path is permitted. Both clean-build PDFs must have
identical bytes, SHA-256 values, and byte counts. Both main.bbl files must
also be byte-identical. A mismatch is a build failure; the builder may not
select one PDF and continue.

### Round-0 validation

Before persistence, both runs must show:

- zero LaTeX errors and zero BibTeX errors;
- zero undefined references and zero undefined citations;
- zero unresolved placeholder, verification, repair, or drafting markers;
- zero author identity or hidden identity metadata;
- zero missing-glyph and missing-font errors;
- all PDF fonts embedded;
- no shell-escape or external-file access;
- no empirical figure or evidence table;
- a mathematical-content page count of 15--17 excluding references;
- a total page count approximately 17--20; and
- exact theorem, bibliography, limitation, and anonymity preservation.

A cosmetic warning may be recorded only if it cannot affect mathematics,
layout integrity, references, fonts, anonymity, or reproducibility. An
overfull box exceeding 10 pt is a failure. The source may not be silently
edited by the builder.

### Persistent Round-0 outputs

Only after byte identity and all checks pass may the builder persist:

- paper/main_round0.pdf
- paper/BUILD_RECEIPT_R0.json

No temporary auxiliary file, main.pdf, log, transcript, cache, or build
directory may remain in the project. Temporary directories are removed only
after their transcript hashes and output hashes have been recorded in the
receipt.

BUILD_RECEIPT_R0.json must be strict canonical compact JSON with UTF-8
encoding, recursive Unicode-code-point key ordering, no insignificant
whitespace, exactly one terminal LF, duplicate keys forbidden, nonfinite
numbers forbidden, and its own hash and byte count excluded. It must bind:

- this scope, the publication lock, and the exact publication-stage review;
- the exact source hashes and byte counts;
- executable paths, executable hashes, version strings, environment, and
  command sequence;
- all command exit codes;
- per-run PDF, main.bbl, and transcript hashes and byte counts;
- explicit byte-identity booleans;
- warning and error counts;
- undefined-reference and undefined-citation counts;
- font-embedding and identity checks;
- mathematical-content, reference, and total page counts;
- the persisted main_round0.pdf hash and byte count; and
- the exact persistent-output inventory.

The builder records facts but may not issue a manuscript-pass verdict.

## Round-1 independent review and one bounded revision

After Round 0, a fresh independent reviewer receives an author-and-builder
stop with stable source, PDF, and receipt hashes. The reviewer's sole write is:

**notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md**

The review must rehash all inputs; compare the PDF with the source and build
receipt; review every theorem and proof transition; check bibliography
accuracy, anonymity, prose, page allocation, limitations, warnings, and
visual integrity; and assign stable finding identifiers. The reviewer may
return **MANUSCRIPT_R1_PASS** or **MANUSCRIPT_R1_REPAIR_REQUIRED**. Neither
verdict authorizes finalization or release.

Exactly one bounded revision stage follows the stable Round-1 review. The
revision author may alter only paper/main.tex and paper/references.bib, and
only to resolve identified Round-1 findings without changing the frozen
theorem or evidence scope. If the review passes without requested changes,
the revision stage is a recorded no-op. If any requested change would alter
the theorem, proof dependency, citation boundary, evidence class, or
governance contract, revision stops and a new upstream governance decision is
required.

The revision stage must also write:

**paper/SOURCE_REVISION_RECEIPT_R1.json**

This receipt follows the same strict canonical JSON rules and excludes its
own hash and byte count. It binds the Round-1 review and the pre/post hashes
and bytes of both source files. Every change must map to a Round-1 finding
identifier and record its bounded semantic role. A no-op receipt records
identical pre/post identities and zero changes. After this receipt is frozen,
no second source-revision window is authorized.

## Round-1 rebuild and fresh Round-2 review

The Round-1 builder repeats the exact two-clean-build protocol, toolchain
recording, byte-identity test, validations, and persistent-output discipline
against the revised source. The only new build writes are:

- paper/main_round1.pdf
- paper/BUILD_RECEIPT_R1.json

BUILD_RECEIPT_R1.json uses the same canonical contract as Round 0 and
additionally binds the Round-0 receipt and PDF, the Round-1 review, and
SOURCE_REVISION_RECEIPT_R1.json. It must show that main_round1.pdf is exactly
the byte-identical output of both clean Round-1 builds.

A fresh reviewer, distinct from the governance author, manuscript drafter,
Round-0 builder, Round-1 reviewer, revision author, and Round-1 builder, then
performs a new review. Its sole project write is:

**notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md**

The R2 reviewer must independently rehash the entire authorized chain and
verify that every R1 finding is resolved or explicitly inapplicable, with no
theorem drift or new defect. The only positive verdict is
**MANUSCRIPT_R2_PASS**. A repair-required R2 verdict authorizes no further
revision under this lock.

Even an exact **MANUSCRIPT_R2_PASS** does not authorize finalization,
identity disclosure, camera-ready changes, public release, submission, or
communication with a venue. Those actions require a separate future lock and
independent review that are outside this publication-stage scope.

## Inventory and stop condition

Immediately before these two governance writes, Paper 14 contained exactly
17 regular files and zero symbolic links. After this scope and the canonical
publication lock are written, the expected inventory is exactly 19 regular
files and zero symbolic links. Both new files are governance artifacts; the
publication lock binds this scope by exact hash and byte count and binds
itself by canonical path and role while excluding its own hash and byte count.

At governance freeze:

- notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md is absent;
- paper/main.tex and paper/references.bib are absent;
- all Round-0, Round-1, revision, and R2-review artifacts are absent; and
- no build, release, finalization, submission, identity, figure, code,
  experiment, or result output exists.

After the canonical publication lock is written and verified, the
publication-stage author must stop. No downstream file may be created in the
same authoring turn.
