# Independent Publication-Stage Review — Paper 17

Date: 2026-08-17 (UTC)

## Verdict

PASS. The frozen human-readable publication scope and the strict-canonical
publication lock agree with each other, bind the complete live fifteen-file
source-design record, define exact and nonexpanding stage universes and role
boundaries, and close every downstream lifecycle action that this review is
not allowed to authorize.

This is a publication-governance verdict only. Its sole positive effect is to
make a separately invoked anonymous author eligible to draft exactly
paper/main.tex and paper/references.bib. It does not itself draft sources,
start formal source review, compile, build, revise, finalize, disclose an
identity, release, submit, upload, communicate externally, or create a
project-level main.pdf.

## Independence, temporal fence, and method

- I am a fresh reviewer and authored none of the fifteen inputs, neither
  publication-governance artifact, and neither reviewed lock.
- Before the exact PUBLICATION AUTHOR STOP, I did not open, list, stat, hash,
  inventory, or write the future Paper 17 paths
  notes/PUBLICATION_STAGE_SCOPE.md and
  experiments/publication_lock.json.
- Before that stop I read only the authorized fifteen Paper 17 inputs and the
  three exact Paper 16 files designated as nonbinding templates. The Paper 16
  material supplied format context only and was not used as authority for any
  Paper 17 conclusion.
- After the stop I independently read both Paper 17 governance artifacts in
  full, parsed and replayed the lock, rehashed every bound object, and checked
  the complete allowed Paper 17 inventory. I did not rely on an authorial
  PASS assertion.
- The review remained read-only until every gate below had passed. This file
  is the sole write, made only after the all-pass determination.

The identities announced at the stop and independently recovered from the
live files are:

| Governance artifact | SHA-256 | Bytes | LF |
|---|---:|---:|---:|
| notes/PUBLICATION_STAGE_SCOPE.md | 44e391724f8634a747748e501e576ed8b9ceaada52a14f265fad367d87561943 | 50254 | 1115 |
| experiments/publication_lock.json | 641da77ac8fa8188c585130b11ef00250383aa477d9d876d490a7a3a2f2ecff2 | 62682 | 1 |

Both are regular non-symlink files, strict UTF-8 without a BOM or CR, with
exactly one terminal LF.

## Bounded digest-cell repair replay

I independently replayed the reported bounded pre-stop repair entirely in
memory. For each row below, the final digest occurs in the unique path row of
the scope and in the same path-sorted input-binding row of the lock. Replacing
only that final value by the listed predecessor value gave the predecessor
state:

| Path | Predecessor digest | Final digest |
|---|---|---|
| experiments/EXPERIMENT_PLAN.md | 6d3c765e3a2acc842a11dd4abff349bef11744f6d381e3ca97522bb3b87470f8 | 6d3c765e8d9991ccaccbde358fa4c8119003c27201645ac08654d173a1d470f8 |
| experiments/EXPERIMENT_TRACKER.md | ef600ff69e42dd263c5bed3eb5b0039d1374ae1cd2e996ad29bb3b8ea4e49206 | ef600f790719a402b294bb06229463a62450653f1f662ff635ebcd9ca82d9206 |
| notes/CITATION_VERIFICATION.md | 28e6bc2b3af39af5ea6d61a58ce20178f32ddd763bb7fc0135cd87a10e4d7ddf | 28e6bc4d461a876e326c08e2a2481fd9f3b30ea3192ddc6c576185e88f317ddf |
| notes/CLAIMS_EVIDENCE_MATRIX.md | becba782ef5a5e07a45096cc6fa0b858726a854320bbccaca0cdb5f0a3a8fea9 | becba75688dc6e77c18a301f37daa34a17328cf54968f3707a6b76ad1774fea9 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | aa67cb02db0c2f331921902652e47567ca457407a55389dacd891364f2428260 | aa67cb9c507e244095df86390bcfe5799c8919a1b32b99b84e94ee98b8538260 |
| notes/NOVELTY_ASSESSMENT.md | d67777120313e948612332199863ace9aadd906835d012754bef0cc472545e29 | d67777768a84199c48170a8eada1c61af10652c81e080c7c341b90629b2c5e29 |
| notes/PROOF_PACKAGE.md | a5649b59a345677de04bd58499af16ba9eeae38b8c430def7cb015a33b73cc77 | a5649bdc97d6853ddfe2716dc5531cf3d4a581fd9e55b4296c9cfe6ccadbcc77 |
| notes/RESEARCH_QUESTION.md | 8942591bb800a70811b8ae06675e91b7ab531b174fc2f4018026625045ab82f | 894259da46aa6e886af06741c8798503c5d7e8229295a1c76a8f53e399bdc82f |
| refine-logs/FINAL_PROPOSAL.md | f91e411be7f47f63787bd2f04b057f2e9e069a7e3ee949e76d06730e6e81bc4 | f91e41b0af9bf2ede85516f4362ae3880015b16080326d788e268d359c718bc4 |
| refine-logs/INITIAL_PROPOSAL.md | 7cbf74a6297f91328062022993fabf10f3ae12df35c40f80c7cbba85dd79df14 | 7cbf74c1db067b58184055dba18ff3fd0d467141bb3868005715612d108edf14 |
| refine-logs/REVIEW_SUMMARY.md | af07de40939f610a739bb2b634833374582900a5259b2a38ed02e11654f1aa9 | af07dea511210fa75f48db5d580106fd25d7984c3262d9a1f279b5baeab51aa9 |

I also reversed only the dependent scope binding in the lock: its scope
SHA-256 from the final value to
032f14ab04211a21049d07f1b5670743884a3b3fcdf67cf8741af2f747382010
and its byte count from 50254 to 50251, leaving its 1115-line count
unchanged.

That exact reverse transformation reconstructed:

- the predecessor scope at SHA-256
  032f14ab04211a21049d07f1b5670743884a3b3fcdf67cf8741af2f747382010,
  50251 bytes, and 1115 LF; and
- the predecessor strict-canonical lock at SHA-256
  11072cc7819527bea6b8b484c27c286984d4056c5c39695a463e06b1f23af467,
  62679 bytes, and 1 LF.

Reapplying the same eleven path-bound digest substitutions and the dependent
scope SHA/byte update reproduced both final files byte for byte. Thus the
repair is reversible and bounded to exactly eleven digest cells in each
governance representation plus the lock's dependent scope identity; the
replay found no other drift.

## Strict canonical lock and self-exclusion

The lock passes every canonicality and negative-probe requirement:

- strict UTF-8 decoding, no BOM, LF-only line endings, compact comma/colon
  separators, no insignificant whitespace, and exactly one terminal LF;
- lexicographic Unicode-code-point ordering at every object level;
- byte-exact round-trip through a duplicate-rejecting, nonfinite-rejecting
  parser and recursively sorted compact serializer;
- exact rejection of each mandated synthetic input:
  {"x":1,"x":2}, {"x":NaN}, {"x":Infinity}, and {"x":-Infinity};
- fifteen safe, relative, unique, path-sorted input bindings with no absolute
  path and no parent traversal;
- the final lock's own SHA-256 and byte count are absent from its content;
  its self-record contains only its path, role, and affirmative self-hash and
  self-byte exclusion flags; and
- the scope binding inside the lock matches the final scope's path, SHA-256,
  bytes, and LF count exactly.

Whitespace perturbation and object-order perturbation do not survive the
strict byte round-trip; duplicate and nonfinite probes are rejected rather
than normalized; and a hypothetical self-identity insertion violates the
explicit self-exclusion rule. The lock is therefore both canonical and
non-self-referential.

## Fifteen frozen input bindings

Every bound path is a regular non-symlink UTF-8 file with a terminal LF. The
scope row, lock row, and live file agree exactly for all fifteen bindings:

| Path | SHA-256 | Bytes | LF |
|---|---:|---:|---:|
| experiments/EXPERIMENT_PLAN.md | 6d3c765e8d9991ccaccbde358fa4c8119003c27201645ac08654d173a1d470f8 | 6234 | 140 |
| experiments/EXPERIMENT_TRACKER.md | ef600f790719a402b294bb06229463a62450653f1f662ff635ebcd9ca82d9206 | 2465 | 59 |
| experiments/source_lock.json | 31b7e8d156bfe46f48bbe0fd38fc6d0f7cbd50da1d78eced8eb0d2b9d7ab0c9f | 53476 | 1 |
| notes/CITATION_VERIFICATION.md | 28e6bc4d461a876e326c08e2a2481fd9f3b30ea3192ddc6c576185e88f317ddf | 10066 | 173 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | becba75688dc6e77c18a301f37daa34a17328cf54968f3707a6b76ad1774fea9 | 10963 | 83 |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 99365584ff6e2fc25f5997bf992c64095c3428c2386bf4e9cfa2923dc50d591b | 18822 | 354 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | aa67cb9c507e244095df86390bcfe5799c8919a1b32b99b84e94ee98b8538260 | 22043 | 390 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 97dca62e01f1906c0a9a5042215badfc6db38b521aff8ba6e7ef996fb751b6b2 | 19068 | 332 |
| notes/NOVELTY_ASSESSMENT.md | d67777768a84199c48170a8eada1c61af10652c81e080c7c341b90629b2c5e29 | 10258 | 200 |
| notes/PROOF_PACKAGE.md | a5649bdc97d6853ddfe2716dc5531cf3d4a581fd9e55b4296c9cfe6ccadbcc77 | 30089 | 852 |
| notes/RESEARCH_QUESTION.md | 894259da46aa6e886af06741c8798503c5d7e8229295a1c76a8f53e399bdc82f | 13539 | 368 |
| paper/PAPER_PLAN.md | 904ecde6dd376da9d701d53e5229071c8f543b839180b59f73ea3c4300e6f356 | 46371 | 848 |
| refine-logs/FINAL_PROPOSAL.md | f91e41b0af9bf2ede85516f4362ae3880015b16080326d788e268d359c718bc4 | 8233 | 257 |
| refine-logs/INITIAL_PROPOSAL.md | 7cbf74c1db067b58184055dba18ff3fd0d467141bb3868005715612d108edf14 | 6920 | 185 |
| refine-logs/REVIEW_SUMMARY.md | af07dea511210fa75f48db5d580106fd25d7984c3262d9a1f279b5baeab51aa9 | 10835 | 208 |

The aggregate is exactly 269382 bytes and 4450 LF.

## Author-stop inventory and future absences

Immediately before this review write, the Paper 17 root was exactly U_L17:
17 regular files, the four directories experiments, notes, paper, and
refine-logs, zero symlinks, and zero other entry types. Its file set was
exactly U_G15 plus the publication scope and publication lock.

Accordingly, every later path was absent: this review; paper/main.tex;
paper/references.bib; notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md;
paper/main_round0.pdf; paper/BUILD_RECEIPT_R0.json;
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md;
paper/SOURCE_REVISION_RECEIPT_R1.json; paper/main_round1.pdf;
paper/BUILD_RECEIPT_R1.json; and
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md. Forbidden code, data, figure,
asset, build-intermediate, output, finalization, release, and external-effect
paths were absent as required.

## Scientific theorem and proof contract

The lock preserves one unified proof-first article. Part A is dominant; Part
B is the exact loss-of-anchor boundary of the same character-deficit
mechanism, not a detached note.

### Part A

The anchored theorem is fixed over an algebraically closed characteristic-zero
field with k at least 2, 1 at most nu at most k-1, nonzero a and c, and at
least two collected nonconstant monomials. It uses the exact recurrence
x_(n+k)=P(x_(n+k-nu))+a x_n, the survivor variety V_m, the stated state
windows, the projection bijection to T_m, and the range 0 at most m at most
k. Every connected torus coset contained in V_m has dimension at most k-m;
the same bound passes componentwise to a possibly disconnected subgroup
translate.

The equality family is sufficient, not necessary: when a=1 and P(1)=0, the
translated residue set R_m={n-nu mod k:0<=n<m} fixes those initial
coordinates to 1 and imposes x_(k+n)=x_n. Its saturated direct-summand
relation lattice makes H_m connected and isomorphic to G_m^(k-m). For every
prescribed support size at least two, the b_j=1, c=-s, Gamma=<2> family gives
the sharp infinite T_(k-1) clock. At m=k the qualitative Laurent bridge gives
finiteness, and T_m is a subset of T_k for m at least k.

I checked every locked Part A bridge in order:

1. exact definitions, zero-based scalar orientation, transition convention,
   state windows, and projection;
2. scheme sanity by successive monic future-variable elimination and
   localization, establishing integrality of V_m;
3. the nonzero constant singleton forcing
   chi_(k+n-nu)=1;
4. the exact split on whether P(xi_(k+n-nu)) vanishes, yielding either killed
   endpoints or chi_(k+n)=chi_n and xi_(k+n)=a xi_n;
5. the A_n and B_n kernel relations and integral independence via interval
   pivots, disjoint endpoint pairs, and exclusion of a pair wholly inside the
   pivot interval;
6. future-coordinate character generation before reduction to the middle
   residues and the rank bound;
7. the fact that R_m is a translation of m distinct residues, not an orbit
   under subtraction by nu, with no gcd(k,nu) hypothesis;
8. the identity-component passage for disconnected groups without dimension
   loss;
9. direct containment, connectedness, saturation, and dimension for H_m;
10. the exact rational rank-one sharpness family with q=k-1-nu; and
11. Laurent only at the qualitative finiteness step after geometric
    coset exclusion.

### Part B

The zero-anchor theorem fixes k=2, nu=1, c=0 and
x_(n+2)=P(x_(n+1))+a x_n with actual positive-exponent support. Linear
support E={1} is explicitly excluded from nonlinear finiteness and may have
an infinite family in every window. Every nonlinear monomial support, every
binomial support with lower exponent at least two, and every support of size
at least three has no positive-dimensional torus coset in V_2^0. The only
nonlinear two-step resonance is E={1,d}, d at least 2, with
P(X)=beta X+delta X^d and a=-beta^2; its unique connected
positive-dimensional coset is
C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d)}. Every nonlinear support,
including that resonance, has no positive-dimensional coset in V_3^0.

I checked every locked Part B bridge:

1. exact recurrence, first three equations, survivor variety, and scalar
   orientation;
2. the trivial-middle-character split into endpoint killing versus the
   root-copy relation and its next-equation closure;
3. all linear chains with r^2=beta r+a and the compatible infinite rank-one
   example;
4. the nonlinear monomial local relation, its two-equation closure, and the
   preserved one-step example;
5. the actual-support one-step P(1)=0 family for every support size at least
   two;
6. the at-least-three-character comparison and closure of all root-copy
   branches;
7. exhaustive A/B/C labels with their exact character and scalar equations,
   including rejection of endpoint-endpoint pairing;
8. the nine adjacent words, with AA, AB, AC, BA, and CA closing directly;
   BB and CC requiring pq=1, BC requiring q^2=1, CB requiring p^2=1, and only
   CB with p=1 surviving;
9. the {1,d} C-then-B character vector, unique scalar resonance
   a=-beta^2, and exact coordinates of C_d;
10. uniqueness by the cyclic character lattice, dimension one, generation,
    and surjectivity of the nonzero x_1 character;
11. third-step closure after CB, including the A/B/C continuations and the
    all-first-four-characters-trivial branch; and
12. declaration of every other nonlinear support case before Laurent and
    preservation of the compatible resonant arithmetic tuple.

The five common bridges are also present: collected group-algebra character
bases with no nonzero singleton, torsion-free character lattices and separate
identity-component passage, generation by all ambient coordinate characters,
strict separation of geometric coset existence from an infinite intersection
with a specified Gamma, and invocation of Laurent only after the complete
finite-rank bridge.

## Laurent bridge and citation lock

Laurent1984 is the sole external proof input. The bridge does not assume
finite generation or bounded torsion: a rational basis of
Gamma tensor_Q Q generates Gamma_0; each individual element has a suitable
power in Gamma_0 after killing its own finite-order torsion factor; hence
Gamma lies elementwise in Gamma_0^div, including arbitrary infinite torsion.
The characteristic-zero transfer generates a finitely generated coefficient
field over Q, embeds that field in C, extends the embedding only to an
appropriate algebraic closure containing the relevant points, uses Cartesian
powers and geometric preservation, and transfers finiteness back by
injectivity. It does not claim that all of K embeds in C. The imported result
and all consequences remain qualitative.

The bibliography is exact set equality among cited main.tex keys,
references.bib entries, and main.bbl items, with exactly these eight verified
keys:

1. BedfordPambuccian1998;
2. BellGhioca2024;
3. Bera2018;
4. BeraVerma2013;
5. JiXieZhang2026;
6. KarimovKelmendiOuaknineWorrell2024;
7. Laurent1984; and
8. MelloYasufuku2026.

The other seven sources are contextual only. Evertse--Schlickewei--Schmidt,
Kaur, every unverified source, and the predecessor manuscript are excluded.
There are no uncited entries and no wildcard nocite. The Laurent record is
the Inventiones mathematicae 78 (1984), 299--327 journal article, DOI
10.1007/BF01388597, EuDML record 143175; the distinct seminar record is not
substituted.

## Public article, tables, pages, and claim boundaries

The exact title is:

Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors
and the Exact Zero-Constant Boundary

The source is a standard anonymous \documentclass[11pt]{article}. It has no
appendix and exactly these eight main sections:

1. Introduction and anchor-loss question
2. Shift-like recurrences, survivor varieties, and the Laurent bridge
3. Characters on recurrence cosets
4. Sharp anchored torus-coset decay
5. Equality subtori and sharp arithmetic clock
6. Zero-anchor local partition calculus
7. Exact zero-constant phase and third-step closure
8. Assumption boundaries, contextual separation, and conclusion

The abstract must contain 180--220 words under the lock's robust
math-span-as-one-token rule, with its exact snippet identity recorded; it
contains neither citations nor history. Content runs from the first page
through the end of Section 8 and occupies 20--23 nonempty pages. A forced
clear page then begins exactly one final References page, for 21--24 total
nonempty pages and no blank page.

There are exactly three table environments, all proof tables with surrounding
derivation:

1. Section 4: A_n/B_n relation pivots, supports, integral independence, and
   rank consequence;
2. Section 6: A/B/C labels, character patterns, and exact scalar equations;
3. Section 7: all nine adjacent words and the V_3^0 transition/closure
   matrix.

There are zero empirical tables, figures, figure environments,
includegraphics calls, raster/vector assets, external inputs, and empirical
claims.

All fifteen public anti-claims are explicit and preserved:

1. the dimension statement concerns a torus coset in V_m, not T_m;
2. the resonant coset does not force T_2 to be infinite for every Gamma;
3. a=1 and P(1)=0 are sufficient, not necessary, for the equality family;
4. no gcd(k,nu) hypothesis, phase, or conclusion is claimed;
5. killed residues form the stated translation, not a subtraction orbit;
6. nonlinear monomial support is not put in a no-finite-window class at c=0;
7. Laurent yields no effective count, algorithm, height bound, or
   enumeration;
8. standard partition and singleton observations alone are not presented as
   the contribution;
9. there is no theorem in positive characteristic, for a=0, for rational or
   Laurent maps, or for arbitrary polynomial automorphisms;
10. collected support is not claimed affine-conjugacy invariant;
11. finite rank is not replaced by finite generation or bounded torsion;
12. no improvement of the companion's explicit planar nonzero-constant
    cardinality bounds is claimed;
13. the bounded comparison is not global, exhaustive, first-result, or an
    unpublished-work claim;
14. Part A does not classify all equality or maximal cosets; and
15. there is no periodic-point classification or effective enumeration.

Exactly one public-safe predecessor disclosure is required in Section 8 and
forbidden from the abstract, Sections 1--7, theorem statements, proofs,
tables, and References. It says that the earlier companion established
stronger explicit bounds for the planar nonzero-constant problem and subsumed
its support-one precursor, while the present article neither reproduces nor
improves those estimates and instead contributes the all-dimensional
torus-coset decay profile and exact zero-constant boundary. There is no
predecessor bibliography entry, black-box dependency, absorption, or parallel
repackaging.

The public text is anonymous and contains no author identity, grant,
acknowledgment, repository, submission, local-path, hash, governance,
review-verdict, operational, drafting, placeholder, repair, or internal
marker.

## Formal manuscript-source review gate

Drafting does not self-certify. After a separately invoked anonymous author
creates only paper/main.tex and paper/references.bib and issues a stable stop
binding both files by SHA-256 and bytes, a fresh reviewer who authored neither
source must read exact U_D20.

That review has one and only one possible write path:
notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md. It must recheck the title,
11-point article form, anonymity, robust abstract, eight sections, no
appendix, final References, complete Part A and Part B chains, all scalar
orientations and examples, the full Laurent bridge, exactly three proof
tables and zero figures/assets, all fifteen anti-claims, the unique Section 8
predecessor disclosure, exact eight-key citation equality, Laurent's sole
proof role, static pdfTeX compatibility, deterministic controls, and absence
of drafting markers.

On any blocker the reviewer writes nothing. Only an all-pass review may write
the unique file and end with exactly MANUSCRIPT_SOURCE_PASS. A repair needs a
separate explicit instruction, can touch only the two source files, and is
followed by a fresh review at the same review path. Source review is not
automatic after drafting, and even its positive result does not authorize a
build.

## Exact stage universes

The path arrays are sorted, duplicate-free, have the declared count, and each
transition has exactly the stated sole additions:

| Universe | Count | Sole additions from predecessor |
|---|---:|---|
| U_G15_current | 15 | none |
| U_L17_governance | 17 | notes/PUBLICATION_STAGE_SCOPE.md; experiments/publication_lock.json |
| U_P18_publication_pass | 18 | notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md |
| U_D20_draft | 20 | paper/main.tex; paper/references.bib |
| U_S21_source_pass | 21 | notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md |
| U_R0_round_0 | 23 | paper/main_round0.pdf; paper/BUILD_RECEIPT_R0.json |
| U_V1_round_1_review | 24 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md |
| U_S1_revision | 25 | paper/SOURCE_REVISION_RECEIPT_R1.json |
| U_R1_round_1_build | 27 | paper/main_round1.pdf; paper/BUILD_RECEIPT_R1.json |
| U_V2_round_2_review | 28 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md |

U_D20, U_S21, U_R0, U_V1, U_S1, U_R1, and U_V2 have exact set equality with
their predecessors plus only these additions. A revision may change the two
existing source bytes but adds only its receipt path. No role may insert a
path, read a later artifact, or expand its own universe.

## Role separation and write universes

All ten operational roles have exact read counts and exact write sets:

| Role | Read universe/count | Exact write universe |
|---|---:|---|
| publication-stage author | U_G15 / 15 | scope, then lock |
| independent publication reviewer | U_L17 / 17 | this review only |
| anonymous manuscript author | U_P18 / 18 | paper/main.tex; paper/references.bib |
| formal source reviewer | U_D20 / 20 | notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md only |
| bounded pre-source repair author | U_D20 / 20 | paper/main.tex; paper/references.bib |
| round-0 builder | U_S21 / 21 | paper/main_round0.pdf; paper/BUILD_RECEIPT_R0.json |
| round-1 manuscript reviewer | U_R0 / 23 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md only |
| sole bounded revision author | U_V1 / 24 | the two sources and paper/SOURCE_REVISION_RECEIPT_R1.json |
| round-1 builder | U_S1 / 25 | paper/main_round1.pdf; paper/BUILD_RECEIPT_R1.json |
| fresh round-2 reviewer | U_R1 / 27 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md only |

The roles are temporally disjoint; reviewers may not author reviewed objects;
self-signing is forbidden. Round-0 additionally requires stable exact U_S21,
the source-review positive token, absence of all later paths, and a separate
explicit build GO. Round-1 review requires stable U_R0; revision requires
stable U_V1; round-1 build requires stable U_S1; and fresh round-2 review
requires stable U_R1.

## Frozen deterministic two-root build protocol

Both rounds use exactly two distinct, new, initially empty, builder-owned,
non-symlink roots under resolved /tmp. Round 0 roots match
/tmp/p17-paper17-r0-XXXXXXXX and the exact eight-character regex; round 1
roots analogously match /tmp/p17-paper17-r1-XXXXXXXX. Only main.tex and
references.bib are copied into each root.

Each root runs the same absolute four-command sequence:

    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/bibtex main
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

Thus each round records exactly eight exit values, all zero. The deterministic
environment is exactly FORCE_SOURCE_DATE=1, LANG=C, LC_ALL=C,
SOURCE_DATE_EPOCH=1786924800, and TZ=UTC; no extension may alter TeX,
bibliography, locale, clock, metadata, path lookup, or source discovery.

The allowed root files are exactly main.aux, main.bbl, main.blg, main.log,
main.out, main.pdf, main.tex, main.toc, and references.bib. CAS, network
access, package installation, shell escape, rasterization, scientific
execution, source edits, undeclared project reads, and project intermediates
are forbidden.

I independently resolved and hashed all thirteen frozen executables. Every
invocation path, resolved target, SHA-256, and declared version identity
matches:

| Invocation | Resolved target | SHA-256 |
|---|---|---|
| /root/miniconda3/bin/python3.12 | /root/miniconda3/bin/python3.12 | 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101 |
| /usr/bin/bibtex | /usr/bin/bibtex.original | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f |
| /usr/bin/cmp | /usr/bin/cmp | b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791 |
| /usr/bin/file | /usr/bin/file | ffa64f607f77d57cb3e2b650825868367a06eb91cdc5959c4e2f62ceb885b18a |
| /usr/bin/pdfdetach | /usr/bin/pdfdetach | e0c04f35fc5b0c4096199ff11d70e49db2b1952b4110f96f5f9ef0a3a4135b2d |
| /usr/bin/pdffonts | /usr/bin/pdffonts | 257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e |
| /usr/bin/pdfimages | /usr/bin/pdfimages | cdac55daf2eaacbaf9f80cf8371e935c8686cb4fd7e84c42bba9706c1f10c87d |
| /usr/bin/pdfinfo | /usr/bin/pdfinfo | 8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e |
| /usr/bin/pdflatex | /usr/bin/pdftex | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 |
| /usr/bin/pdfsig | /usr/bin/pdfsig | 0c50615f466e45cc0309a68bdb8c4ad53778529ec77ab14e521e9c8d765eff09 |
| /usr/bin/pdftotext | /usr/bin/pdftotext | 7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d |
| /usr/bin/sha256sum | /usr/bin/sha256sum | 7645c8e76d75515ccb75c9086bdcf0d4071f2985f380f249253ead7d7c6810b3 |
| /usr/bin/x86_64-linux-gnu-strings | /usr/bin/x86_64-linux-gnu-strings | 6ff5cfaddaf8dbc67614f535530465c890e83498509a6c8ffacc3798b6f1126f |

Every version command's complete transcript, as well as every validation
executable and receipt-entering validation snippet, must be bound by command,
SHA-256, and bytes.

Within each round the two PDFs, BBLs, final logs, corresponding command
transcripts, combined transcripts, and discovered font tables must be byte
identical. Combined transcripts contain exact combined stdout/stderr bytes
without root labels, timestamps, or wrapper prefixes. Selection after a
mismatch is forbidden.

Validation requires exact source identities before and after each build; the
article, proof, citation, table, anti-claim, predecessor, page, abstract, and
anonymity gates above; zero errors, warnings, undefined references or
citations, multiply defined labels, missing characters/glyphs/fonts,
overfull boxes, and underfull boxes; and decoded-PDF scans. Every discovered
font must be embedded, subset, and Unicode-mapped. Images, attachments,
embedded files, signatures, forms, XFA, JavaScript, launch/external-file
actions, RichMedia, trailer IDs, dates, identity metadata, local paths, and
submission identifiers must all be absent.

## Receipts, cleanup, revision, and final review

Build receipts use the same strict canonical JSON rules and exclude their own
hashes and bytes. A receipt is persisted only after all checks. It binds all
governance/review/source inputs, prebuild and postbuild source identities,
both root identities and safety facts, frozen tools and complete versions,
validation snippets, environment, commands, eight exits, transcripts, all
per-run artifacts and equality checks, the discovered complete font table,
the persisted PDF, exact prewrite/postwrite universes, and cleanup.

Only main_round0.pdf plus BUILD_RECEIPT_R0.json, and later main_round1.pdf
plus BUILD_RECEIPT_R1.json, persist. A project paper/main.pdf is forbidden.
Before cleanup every fact is captured; each root is re-resolved and its exact
regular-file allowlist revalidated; each allowed file is unlinked
individually by explicit resolved path; and the empty root is removed with
rmdir. Globs, recursive deletion, symlink traversal, unresolved variables,
and broad targets are forbidden. Both roots must be verified absent before
the stop.

Fresh round-1 review audits the entire theorem/proof/citation/page/table/
anti-claim/PDF/receipt/cleanup record and writes only
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md. A blocker writes nothing; a written
review ends in exactly MANUSCRIPT_R1_PASS or
MANUSCRIPT_R1_REPAIR_REQUIRED and gives each finding a stable identifier,
severity, source/PDF location, required bounded repair, and theorem-scope
impact.

There is exactly one bounded revision window, including the possibility of a
no-op. It may address only R1 findings, may write only the two sources and the
strict-canonical SOURCE_REVISION_RECEIPT_R1.json, and may not expand theorem,
bibliography, evidence, or scope. A no-op requires byte-identical sources,
and after the no-op the R0 and R1 PDFs must be byte identical. There is no
second revision window.

Round 1 repeats the same two-clean-root deterministic protocol. A fresh and
distinct round-2 reviewer then reads exact U_R1 and may write only
notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md. A blocker writes nothing; a
positive review ends with exactly MANUSCRIPT_R2_PASS and authorizes no
further revision.

## Lifecycle closure and exact effect of this verdict

The current stage records zero manuscript sources, code, data, experiments,
figures/assets, scientific runs, compilations, builds, releases, and external
effects. This verdict changes only publication-stage review status and adds
this one review path, producing exact U_P18.

Under a separate invocation, the anonymous manuscript author may now draft
only paper/main.tex and paper/references.bib. Formal source review remains a
fresh separate gate after a stable source stop. Compilation remains false
until that source review passes and a separate explicit build GO is given.

Even after a positive round-2 manuscript review, camera-ready production,
paper/main.pdf, finalization, public release, repository push, submission,
upload, external messaging, and identity disclosure all remain false.
Finalization requires a separate future lock and a fresh independent review.

All required publication-stage checks pass. No blocker exists.

PUBLICATION_STAGE_PASS
