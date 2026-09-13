# Paper 26 Independent Publication-Lock Review R1

## Verdict and finding census

Verdict: PASS.

I independently audited the complete Paper 26 L18 universe and find the
publication lock byte-exact, strict-canonical, scientifically faithful,
publication-complete, namespace-clean, and authority-safe. I did not inherit
or adopt the author, parent, candidate-review, or predecessor-review verdicts.
I read the two current Batch 06 ledgers, all eighteen current Paper 26 files,
and both candidate reviews to physical EOF and reconstructed the conclusions
below from their current bytes.

The final finding census is:

- blocker: 0;
- major: 0;
- minor: 0;
- ambiguity: 0;
- canonical or lexical defect: 0;
- inventory, identity, hygiene, or path defect: 0;
- scientific or proof-boundary defect: 0;
- citation or bibliography defect: 0;
- public-metadata or firewall defect: 0;
- lifecycle, namespace, permission, or authority defect: 0.

The research-review discipline supplied the review structure, but all
measurements, comparisons, parses, and judgments in this artifact are fresh
for this gate. No network, browser, TeX, BibTeX, PDF, CAS, numerical,
scientific, compilation, build, release, or external-effect action was used.
No build root, historical root, future root, temporary artifact, source file,
code file, data file, or PDF was listed, probed, read, created, or changed.

## Opening governance and external records

The current governance records were regular mode-0644/link-one UTF-8 files,
with no BOM, CR, or NUL and one terminal LF:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| BATCH_06_STATUS.md | cd326d2404ae8ebc4b716edd63d1290dcbe09ba3a499404b93c9d22664487c90 | 401075 | 5664 |
| BATCH_06_IDEA_REPORT.md | 6497862441248ab173be2dc3bdb22a610e28a8a979543dc564200d4272d2b334 | 524669 | 9587 |

They open exactly PAPER26_PUBLICATION_LOCK_REVIEW_R1_OPEN and record the
parent-consumed author stop. The publication lock binds the distinct
author-opening ledger snapshots:

| Author-opening record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| BATCH_06_STATUS.md | d2adfe9dc9558b34d42773c3030d7d7837066b5889a2a30a1b41e7bff897b9f2 | 395944 | 5586 |
| BATCH_06_IDEA_REPORT.md | 7fda5432313fb6b9230c0992972bb8bbde432af1504b7255f2b9c2f0403b6b9f | 522839 | 9556 |

The current status ledger records that both author-opening identities remained
exact through the lock write. Their later change is precisely the parent
author-stop consumption and review-gate transition, not an author-side ledger
mutation.

Both candidate records were also read through EOF:

| Candidate review | SHA-256 | Bytes | LF | Unique terminal |
|---|---|---:|---:|---|
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R1.md | cc81cc410d9122bdaf6ebf8b20e57bce3cbe4fcaed17c3cc0ed5f596d9844dbe | 29824 | 611 | PAPER26_CANDIDATE_GATE_PASS_R1 |
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R2.md | 164273106733f611c0d35a60cb693d5ffbf8cf1300ffb658a00abb555fbda2e1 | 26605 | 1112 | PAPER26_CANDIDATE_GATE_PASS_R2 |

I treated their provisional formulations as history. In particular, I did not
carry forward the early upper-carry shortcut or the early bridge-based inverse
recurrence wording. The live source package repairs both issues, and the
publication lock freezes the repaired statements.

## External L18 universe, identities, and hygiene

The project root was an ordinary directory, mode 0755, link count 6, and
directory size 90. Its four children were the complete directory universe:

| Relative directory | Type | Mode | Links | Prewrite directory size |
|---|---|---:|---:|---:|
| experiments | directory | 0755 | 2 | 134 |
| notes | directory | 0755 | 2 | 4096 |
| paper | directory | 0755 | 2 | 67 |
| refine-logs | directory | 0755 | 2 | 99 |

There were exactly eighteen regular files, four child directories, zero
symbolic links, and zero other nodes. Every file below was independently
opened, read to EOF, hashed, and checked as mode 0644/link one, strict UTF-8,
no BOM, no CR, no NUL, and exactly one terminal LF:

| Raw-byte-sorted relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| experiments/EXPERIMENT_PLAN.md | 7b543388f7c12220aee27605b6cef53df48b7c835798a90495b4706b98a8355f | 15201 | 394 |
| experiments/EXPERIMENT_TRACKER.md | c35c8cfba39bf8634e11ee91173b6fb2c313babe347ff30fdf0c5f445b65562d | 7987 | 105 |
| experiments/publication_lock.json | 3e07bea49e0c24c85c5c8e2d7ed04c3a85dc11f314630d6625e8d7f70fe033ea | 40739 | 1 |
| experiments/source_lock.json | 226b90ec7367b73cbd481a67a08a38e5a471c0a9d9ac571e6905292587b59839 | 11556 | 1 |
| notes/CITATION_VERIFICATION.md | 8ebb74149ce7d1eb22151019cd5a868e941df1c78b787ae605794a1c64011d09 | 8311 | 153 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 56853a22b9a89e4599cad40a017d659aa50a6ecbf2cb3d52df080bd14b18d6f4 | 9076 | 75 |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 49844cd40eee7a654f79c8a86f521d31998fbad5b70928204d4cb0621b4b97e6 | 18883 | 417 |
| notes/INDEPENDENT_PUBLICATION_SCOPE_REVIEW.md | 678a9b2dbcaf46add7ef1227677ed1368de40269184eb25f4e7c2c1363a8aa12 | 26084 | 168 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 974bcfea08dff87d359993839452eb271d2cf0edbbe2fb811abc17051aece92e | 17823 | 449 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | c12ea09940a775b97dc7e459b6284858bf076f56b2e13a15b09d95ffe6214e0e | 20397 | 440 |
| notes/NOVELTY_ASSESSMENT.md | 150573d9fe3cbddac7e49bdefc51ca687bd3b7dc51bbd2651f65b8947f1088a3 | 11496 | 185 |
| notes/PROOF_PACKAGE.md | e17c0a801e3b19b0c090e96d69562492465ef96ac39fe3219cdeb193b4cd8f7d | 40986 | 1431 |
| notes/RESEARCH_QUESTION.md | bb539d56e60987180c362d7d4b076785b40def15408aef08bf8b58403ee81bb4 | 9878 | 209 |
| paper/PAPER_PLAN.md | 8f788b1416ec9887a894c103bf0374896f4c4eff50e9fc7ac7124eb67c43ca15 | 56308 | 834 |
| paper/PUBLICATION_SCOPE.md | c74fe2eb363e3e4af8f6cd27d45151da68aaaf9cde0024e492e283c04a64322e | 36215 | 492 |
| refine-logs/FINAL_PROPOSAL.md | 56447f2b98d64dc9c97b70f3731f03aa1c41ed68a459c07a178e1166320611ba | 10528 | 241 |
| refine-logs/INITIAL_PROPOSAL.md | 65d4e90de9a9db2ea652c26c43a8114ef61f658efca14cb23ce9dd9d8a309711 | 6789 | 159 |
| refine-logs/REVIEW_SUMMARY.md | c0f1576dcc3cc3587bc5c726ac6e70fa87f06f3225cf6e6d381e34933f9ff138 | 14062 | 213 |

The paths are normalized project-relative ASCII, and therefore UTF-8, with no
empty component, dot component, parent traversal, separator ambiguity,
control byte, or duplicate. Their order is strict ascending raw UTF-8 byte
order. The seventeen bound file rows and four bound directory rows match the
live identities, types, modes, links, hashes, sizes, LF counts, hygiene fields,
and order exactly.

At prewrite, the review path and all three future source paths were absent:
notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md, paper/main.tex,
paper/math_commands.tex, and paper/references.bib.

## Independent L17, prelock, and L18 reconstruction

I used two genuinely independent implementations. The Python route used
recursive os.scandir entries, nonfollowing stat calls, explicit struct
big-endian unsigned-64 framing, whole-content reads, and hashlib. The Ruby
route independently used Find, File.lstat, File.binread, Q-greater-than
packing, byte-string sorting, and incremental Digest updates.

Each route framed a file as:

u64be(path byte count) || relative UTF-8 path bytes ||
u64be(content byte count) || content bytes.

Both independently obtained:

| Layer | Files | Content bytes | Content LF | Path bytes | Framing bytes | Prefix bytes | Stream bytes | SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Unprefixed L17 | 17 | 321580 | 5966 | 524 | 272 | 0 | 322376 | c78937738859e75a59cc0df37513e68fa31e76c618320008204ef747ab8ac2b9 |
| Publication prelock | 17 | 321580 | 5966 | 524 | 272 | 31 | 322407 | 3540c1034897611dc5691cd1543cf68e96a80ac97ae5060e37a13212d8fe9014 |
| Unprefixed L18 | 18 | 362319 | 5967 | 557 | 288 | 0 | 363164 | d732dfa99afbb3748f24792091618ef7b3a0a13e4717ab6297103cc02a43106c |

The prelock prefix is the exact 30 ASCII bytes
paper26-publication-prelock-v1 followed by one 00 byte. It is applied once
before the complete ordinary L17 stream and nowhere else.

The sole L17-to-L18 delta is experiments/publication_lock.json. Its path is
33 bytes, its frame is 16 bytes, and its content is 40739 bytes / one LF, so
the framed increase is exactly 40788 bytes. The lock excludes itself from the
seventeen-row files binding and from L17. Its self-identity object names only
the externally measured path and the excluded field names byte_count,
lf_count, and sha256; it contains none of those identity values. The live
lock SHA does not occur in the lock bytes.

## Strict-canonical audit

The lock is one physical JSON line plus one LF, exactly 40739 bytes. It has no
BOM, CR, NUL, extra LF, trailing record, or invalid UTF-8. Its schema is
paper26.publication_lock.v1 and its sole logical author terminal is
PAPER26_PUBLICATION_LOCK_AUTHOR_STOP. Each occurs exactly once as a parsed
string value and exactly once in the raw bytes.

I did not rely on a permissive library parse. The first validator was a
handwritten Python recursive-descent parser with decoded-key duplicate
rejection, exact integer grammar, scalar-value restrictions, explicit escape
and surrogate-pair handling, complete-record consumption, and a separate
recursive encoder. The second was an independently written Ruby
recursive-descent parser and encoder with its own token, duplicate, integer,
escape, surrogate, and record logic.

Both accept only object, array, string, integer, and Boolean values. Both sort
object keys recursively by Unicode code-point arrays, preserve array order,
emit compact separators and literal UTF-8 with ensure-ASCII disabled, and add
one LF. Each encoder reproduced all 40739 committed bytes exactly. A
non-BMP discriminator confirmed the required code-point order U+E000 before
U+10000; both implementations distinguish it from JavaScript UTF-16 order.

The duplicate-aware external census agreed exactly:

| Parsed category | Count |
|---|---:|
| Objects | 139 |
| Arrays | 81 |
| String values, excluding object keys | 617 |
| Object keys | 915 |
| Strings when keys are counted | 1532 |
| Integers | 213 |
| Booleans | 209 |
| Boolean true | 95 |
| Boolean false | 114 |

Thus keys are not included in the 617 string-value count; they are reported
separately, and the combined string/key census is 1532. No null, float,
exponent number, nonfinite value, or other value type exists. The permissions
object has exactly thirty keys and all thirty values are real Boolean false;
those thirty are a subset of the 114 false values in the whole object. The
separate authorized_write_paths array is exactly empty.

Both strict validators rejected every required hostile class:

| Hostile class | Python | Ruby |
|---|---|---|
| Duplicate decoded object key | reject | reject |
| Null value | reject | reject |
| Float number | reject | reject |
| Exponent number | reject | reject |
| Nonfinite number token | reject | reject |
| Integer leading zero | reject | reject |
| UTF-8 BOM | reject | reject |
| CR or CRLF | reject | reject |
| Raw NUL | reject | reject |
| Lone Unicode surrogate escape | reject | reject |
| Trailing JSON record | reject | reject |
| Missing terminal LF | reject | reject |
| Extra terminal LF | reject | reject |

Additional adversaries also passed the expected failure boundary: a
textually different escape decoding to a duplicate key, reverse object-key
order, noncompact whitespace, and an ASCII escape for a non-ASCII scalar were
all rejected as duplicate or noncanonical bytes.

## Scientific and proof-contract audit

I compared the lock directly with source_lock.json, PROOF_PACKAGE.md,
RESEARCH_QUESTION.md, the repaired PAPER_PLAN.md, PUBLICATION_SCOPE.md, the
four independent PASS reviews, and both candidate reviews. The exact public
title is:

Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector
Rigidity and Bidirectional Degree Growth

The live contract correctly freezes all of the following:

1. K has characteristic zero; E is finite, nonempty, collected, and contained
   in the coordinatewise-at-least-two lattice; every collected coefficient is
   nonzero with arbitrary signs and no positivity or common-sign premise.
2. W is exactly separated pure power with nonzero alpha and beta and
   derivative exponents e and f at least two. The map is F equals T after S;
   the inverse is S inverse after T inverse, so the subtraction T-inverse
   phase acts first.
3. The entire exposed face is retained at every tie. The unique
   minimal-first-coordinate point isolates the coefficient
   c_(x0,y0)^2 x0 y0 (1-x0-y0), whose nonvanishing gives face-gradient
   algebraic independence in characteristic zero.
4. Injective substitution, nonzero scalars, signs, and separated powers
   propagate leading-pair independence through every forward and inverse
   addition or subtraction phase.
5. The forward state is B after mathcal_A; the inverse state is mathcal_A
   after B. Both lower carries and the repaired cross-coordinate upper
   carries are present, and the final visible blocks are position forward and
   momentum inverse.
6. The bridge is exactly the shifted identity
   u^+_(n+1) = c_star B v^-_n from the ordinary seed. It supplies
   constant-factor vector comparison and equality of exponential rates only,
   not termwise scalar equality and not an inverse scalar recurrence.
7. The forward projective map, branch derivative, positive quadratic gap,
   endpoint decay, finite-support maximum, and continuous wall splitting give
   one uniform logarithmic contraction. The inverse selector is the exact
   scaling conjugate and is evaluated at kappa times s.
8. There is one fixed ray and no nontrivial numerical periodic orbit. An
   interior ray gives an eventually stationary selector; a fixed wall orbit
   uses the full tied face; a strict wall orbit alternates adjacent chamber
   labels while the ratios converge. Extreme adjacent exponents control the
   open sides at a multiple tie.
9. The interior Perron value comes from a positive integral two-by-two
   chamber matrix and has algebraic degree at most two. Adjacent wall matrices
   share a primitive positive integral ray and one rational
   algebraic-integer multiplier, hence a positive integer multiplier equal to
   the one-step dynamical degree.
10. Scalar recurrence arguments are separate in both directions. The inverse
    route uses D_xi = A_xi B = B^(-1) C_xi B, both inverse seed cases, fixed
    and strict walls, both N parity products, their similarities to the
    forward M products, common trace and determinant, and parity-wise visible
    coordinates. Interior orders are at most two, strict interleaved wall
    orders are at most four, and fixed-ray tails are geometric; no minimality
    is claimed.
11. The dependency order is forward-only: symplecticity and inverse order;
    full-face Hessian; Jacobian independence; substitution survival; carries
    and visible blocks; bridge; projective maps; uniform contraction;
    selector classification; spectral arithmetic; separate scalar
    recurrences; then fixtures and boundaries.

The two final proof fixtures match every source:

- Interior: E={(2,2)}, B=diag(3,2), C=[[3,6],[4,2]],
  characteristic polynomial t^2-5t-18, value
  (5+sqrt(97))/2, c_star=3, u_1=(9,6), v_1=(7,8), and
  u_2=(63,48)=3 B v_1.
- Wall: E={(2,8),(4,5),(5,3)}, B=diag(24,11), walls
  3/2 and 2, ratios 24/11, 1548/781, and 51294/25619,
  selector word low, high, middle, high, middle, and so on, common direction
  (2,1), multiplier 132, ordered monodromy C_high C_middle with matrix
  [[10080,14688],[4928,7568]], trace 17648, determinant 3902976, and
  eigenvalues 17424 and 224. The lock labels this a hand-checkable selector
  alternation converging to the wall, not numerical evidence or a two-cycle.

## Anti-claims, collision subtraction, and novelty

The twenty-one lock anti-claims jointly preserve every source boundary: no
axis support; exponent one; zero, duplicate, ghost, or uncollected support;
mixed or nonseparated W; positive characteristic; dimension at least three;
infinite support; altered phase order or bridge seed; termwise
forward/inverse equality; scalar transfer through the bridge; numerical
two-cycles or other numerical periodic orbits; recurrence minimality; higher
dynamical degrees; a new entropy conclusion; compactification; integrability
or nonintegrability; periodic, Diophantine, or other arithmetic point-orbit
conclusions; classification or nonconjugacy; a genericity substitute;
support optimality, support-rank novelty, or global Hamiltonian quadratic
sharpness; and exhaustive coverage, global novelty, priority, firstness,
uniqueness, or no-related-theorem language.

The Paper 24 ownership subtraction reserves the special two-term wall
criterion, forced selector period two, parity/monodromy mechanics, and
interleaved-recurrence framing; Paper 26 uses two-step products only as late
consequences. The Paper 25 subtraction reserves support-rank bounds,
stationary sharp constructions, unbounded higher-dimensional Perron degree,
and scalar minimality. Paper 26 is expressly a narrower planar rigidity
theorem and claims neither ownership set. Public expression is limited to
assumption-and-mechanism differences without project numbers or unpublished
identifiers.

Global claim-level novelty and venue selection remain unresolved. The lock
claims neither exhaustive literature coverage, global noncollision,
priority, nor firstness.

## Publication architecture, table, and metadata

The design ledger is exactly:

| Component | Designed pages |
|---|---:|
| Front matter and Abstract | 0.75 |
| Section 1 | 2.25 |
| Section 2 | 1.50 |
| Section 3 | 3.00 |
| Section 4 | 4.25 |
| Section 5 | 3.75 |
| Section 6 | 3.50 |
| Section 7 | 4.00 |
| Section 8 | 2.50 |
| Section 9 | 0.50 |

The sum is exactly 26.0 designed body pages excluding references, and
Sections 4 through 7 total exactly 15.5. The 22-through-30 rendered range is
explicitly future acceptance, not a claim that an unbuilt PDF already has
that pagination. The body is an Abstract plus exactly Sections 1 through 9.
There is no appendix, supplement, empirical section, or theorem-critical
external material.

There are zero figures and zero assets. The sole table is a hand-typeset
qualitative structural table in Section 6.7, with exactly the three columns
Mechanism, Consequence, and Boundary and exactly five body rows. The rows are
the full-face certificate, strict carries/separated powers, finite-envelope
contraction, interior/common-wall spectral mechanism, and stable
visibility/Cayley-Hamilton. There is no second table, generated table,
numerical result, benchmark, score, page ledger, literature table, claims
matrix, fixture table, or notation table in the future article.

The visible author is exactly Anonymous and the visible date is empty. The
PDF and XMP Title values equal the exact title. PDF and XMP Author, Creator,
Producer, Subject, and Keywords are all empty. The firewall covers rendered
text, source comments, bookmarks, links, PDF/XMP metadata, attachments,
PDF-exposed filenames, and bibliography fields. It excludes identity,
affiliation, acknowledgments, grants, identity links, local paths, hashes,
reviews, gates, workflow roles, candidate IDs, paper numbers, unpublished
predecessors, repository data, and internal collision labels.

## Seven-entry bibliography audit

Exactly seven article records are admitted. Each has citation_count one,
proof_transfer false, one frozen Section 1 slot, and the exact fields below:

| Key; slot | Canonical substantive fields | Narrow role |
|---|---|---|
| BellonViallet1999AlgebraicEntropy; 1.1/S1.1-D1 | Bellon, M. P. and Viallet, C.-M.; Algebraic Entropy; Communications in Mathematical Physics; 1999; 204(2); 425--437; DOI 10.1007/s002200050652 | Degree-growth and algebraic-entropy motivation only |
| DangFavre2021SpectralInterpretations; 1.1/S1.1-D2 | Dang, Nguyen-Bac and Favre, Charles; Spectral interpretations of dynamical degrees and applications; Annals of Mathematics; 2021; 194(1); 299--359; DOI 10.4007/annals.2021.194.1.5 | General spectral context only |
| FordyHone2011SymplecticMaps; 1.3/S1.3-T1 | Fordy, Allan P. and Hone, Andrew; Symplectic Maps from Cluster Algebras; Symmetry, Integrability and Geometry: Methods and Applications; 2011; volume 7; article 091; DOI 10.3842/SIGMA.2011.091; no issue | Separate symplectic/tropical-recurrence context; no integrability inference |
| IshibashiKano2021AlgebraicEntropy; 1.3/S1.3-T2 | Ishibashi, Tsukasa and Kano, Shunsuke; Algebraic entropy of sign-stable mutation loops; Geometriae Dedicata; 2021; 214(1); 79--118; DOI 10.1007/s10711-021-00606-1 | Conceptual mutation-loop comparison only |
| JaneczkoJelonek2008PolynomialSymplectomorphisms; 1.3/S1.3-S1 | Janeczko, Stanisław and Jelonek, Zbigniew; Polynomial symplectomorphisms; Bulletin of the London Mathematical Society; 2008; 40(1); 108--116; DOI 10.1112/blms/bdm112 | Ambient family background only; no classification |
| BergerTuraev2025GeneratorsHamiltonianMaps; 1.3/S1.3-S2 | Berger, Pierre and Turaev, Dmitry; Generators of groups of {Hamiltonian} maps; Israel Journal of Mathematics; 2025; 267(1); 237--252; DOI 10.1007/s11856-024-2709-7 | Position-only/momentum-only shear-generator context only |
| BlancVanSanten2022DynamicalDegrees; 1.3/S1.3-A1 | Blanc, Jérémy and van Santen, Immanuel; Dynamical degrees of affine-triangular automorphisms of affine spaces; Ergodic Theory and Dynamical Systems; 2022; 42(12); 3551--3592; DOI 10.1017/etds.2021.90 | Adjacent affine-triangular comparison only; no class inclusion |

The Abstract has zero citations, Section 1 has exactly seven, and Sections 2
through 9 have zero. No citation appears in a theorem, proof step, fixture,
collision subtraction, or Conclusion. No standard theorem is outsourced, no
entry is unused, and there is no eighth entry.

Fordy--Hone 2014 is fully identified but withheld as redundant and an
integrability-drift risk. Koch--Lomelí 2014 is fully identified but excluded
for insufficient claim fit, with Berger--Turaev already supplying the
narrower useful context. Neither boundary record has a final key, slot, or
bibliography entry. The lock imports the passed primary-record scope; this
review performed no new web lookup and makes no broader novelty inference.

## Source handoff, acceptance, stop, and build-policy split

The future source universe is exactly three disjoint regular UTF-8 text roles:

1. paper/main.tex owns the entire article, exact metadata, Abstract,
   Sections 1--9, all proofs, both fixtures, the sole table, and bibliography
   call; it may input only math_commands.tex and use only references.bib.
2. paper/math_commands.tex owns notation and formatting macros only, with no
   prose, proof, citation, file I/O, executable behavior, identity, external
   input, or hidden source.
3. paper/references.bib owns exactly the seven once-used canonical entries and
   no alternate or unused record.

There is no fourth, hidden, generated, section, style, visual, data, code,
notebook, script, auxiliary, alternate-bibliography, build, or temporary
source. Source creation is currently unauthorized.

The lock has exactly eighteen source-acceptance criteria. In order they close:
public identity; PDF/XMP metadata; the firewall; exact source trio; exact body
structure; 26.0/15.5 design and future 22--30 range; zero visuals and sole
table; cancellation before transport; complete dependency-ordered theorem;
all forward/inverse carries; the bounded bridge; complete global contraction;
scaled inverse selector and wall cases; quadratic/integer spectrum; separate
bidirectional recurrences; exact hand fixtures; the seven-entry once-only
citation contract; and all anti-claims/collision subtractions with global
novelty unresolved and no priority wording.

The lock has exactly thirteen mandatory stop rules. They cover: failure of
the face certificate or independence; any carry/visibility/order/bridge
failure; failure of one global contraction constant; an unclassified selector
tail; a numerical cycle, nonintegral wall multiplier, or degree above two;
any defective inverse-recurrence route; need for minimality or another
anti-claim; either fixture failing; any primary field, citation sentence, or
claim-fit failure; need for an extra citation/source/appendix/supplement/table/
visual/computation/generated source/format trick; firewall or metadata
failure; discovery of the same complete theorem without a claim-preserving
narrowing; or repackaging either predecessor headline. These are stop
conditions, not silently repairable exceptions.

The permanent base lock freezes only invariant future build principles:

- exactly two mutually isolated A and B builds;
- a fixed reproducible environment invoked directly through
  /usr/bin/env -i;
- HOME and CODEX_HOME absent and never reassigned;
- direct order pdfLaTeX pass 1, BibTeX, pdfLaTeX pass 2, pdfLaTeX pass 3;
- network, shell escape, wrapper, postprocessor, and retry disabled;
- direct pass-3 PDFs only, with no copied, normalized, or postprocessed
  substitute;
- exact metadata, page/reference, font, text, link/attachment/firewall, and
  byte-identical A/B verification principles.

No future root path is allocated, created, or probed. A first probe belongs
only to a separately authorized builder, and any attempted roots are retained
permanently. This review did not probe any root.

The source-bound profile is eligible only after a valid source PASS and a
separate parent gate. It must later bind, from realized evidence: exact source
trio identities; realized pagination; exact warnings and transient grammar;
raw per-pass logs and exits; tool, binary, version, environment, font, and
resource identities; the precise reachable final inventory; build receipt and
independent evidence; and exact authorized roots and direct final-PDF
identities. The base lock contains no operative placeholder, null, guessed
warning, guessed artifact, prototype digest, or synthetic log fixture.

## Namespace, lifecycle, permissions, and final authority

The active namespace is exactly Batch06/Paper26 at
papers/26-hamiltonian-newton-envelope-contraction. The root-control snapshot
matches the author-opening state ACTIVE_LOCAL_PAPER26_5_OF_5,
PAPER26_PUBLICATION_LOCK_AUTHOR_OPEN, and
PUBLICATION_SCOPE_REVIEW_R1_PASS_PUBLICATION_LOCK_AUTHOR_OPEN, with completed
papers 2, terminal dispositions 4, and no external effect. The only paper24
and paper25 tokens are the two explicitly scoped collision-ownership keys;
they are not active namespace or lifecycle values. No stale Paper23, Paper35,
other batch, root, source, review, or build namespace occurs.

The lock cannot open its own review. Its author stop sets
author_stop_opens_review false, successor_gate_opened false, and the possible
review authorized false. Parent consumption is required. The later valid
review can make the trio eligible only; it cannot authorize source writing.
The current review authority comes solely from the later parent ledger gate.

All thirty action permissions are Boolean false, including publication-lock
review, source trio, source repair, manuscript, bibliography, code, data,
figures/assets, scientific execution, CAS, numerics, browse/network, compile,
build, PDF, root probing or cleanup, temporary artifacts, repository or root
ledger mutation, archive, release, submission, upload, messaging, identity
disclosure, external effect, and successor gate. authorized_write_paths is
empty. All eleven scientific-execution counters are zero.

The lock therefore freezes invariant principles and eligibility conditions
without granting authority. The author-stop terminal occurs exactly once,
self identity is externally bound, the review and trio were absent at
opening, all predecessors and ledgers were stable at the prewrite boundary,
and no finding remains.

PAPER26_PUBLICATION_LOCK_PASS
