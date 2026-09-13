# Independent Manuscript-Source Review — Paper 17

Date: 2026-08-17 UTC

Article: **Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences:
Constant Anchors and the Exact Zero-Constant Boundary**

## Verdict and exact effect

PASS. The repaired anonymous manuscript source and bibliography satisfy the
complete frozen theorem, proof, Laurent, example, citation, article,
anti-claim, predecessor, anonymity, and static-source contracts. The bounded
repair is exactly reversible to the declared predecessor and introduces no
other byte drift. No mathematical, citation, structural, public-text, or
static pdfTeX blocker remains.

This is a source-level verdict only. It creates no PDF, performs no build, and
does not authorize compilation. A build remains conditional on this exact
review, stable exact `U_S21`, and a separate explicit build GO.

## Independence, temporal fence, and method

- I am a fresh formal source reviewer and authored neither `paper/main.tex`
  nor `paper/references.bib`.
- Before the explicit `AUTHOR REPAIR STOP`, I did not open, list, stat, hash,
  or otherwise inspect either source or the future review path.
- Before that stop I read the exact `U_P18` contract and verified the prior
  publication-stage review and its terminal `PUBLICATION_STAGE_PASS`.
- After that stop I independently read exact `U_D20` in full, including both
  repaired sources, and replayed the entire gate rather than reviewing only
  the announced diff.
- The audit used read-only text selection, strict parsing, hashing, byte/LF
  counts, and in-memory reversal. It used no compilation, web access, CAS,
  scientific execution, code artifact, data, result, figure, asset, or
  external input.
- The review remained zero-write until every conjunctive gate below had
  passed. This file is the sole project write.

## Exact inventory and source identities

Immediately before this review write, the project was exactly `U_D20`: 20
regular non-symlink files, exactly the four directories `experiments`,
`notes`, `paper`, and `refine-logs`, zero symlinks, and zero other entry types.
The sorted path set equaled the lock's `U_D20_draft` array. Every later path
was absent, including this review, all build receipts and PDFs, both later
manuscript reviews, and the revision receipt.

The stable source identities independently recovered after the repair stop
were:

| Source | SHA-256 | Bytes | LF |
|---|---:|---:|---:|
| `paper/main.tex` | `9cf03af659631ad7ec4228c05927733c620b111bb3840fa3555b32325cfcc977` | 72701 | 1213 |
| `paper/references.bib` | `e7aab6d2bfcbb1688cfeb5625d490a155820532aba1ba2359433ea7c543417d0` | 1890 | 61 |

Both files are strict UTF-8 without BOM, CR, or NUL, with exactly one
terminal LF and balanced braces. They remained byte-identical through the
entire audit.

## Exact bounded-repair reconstruction

The repair was reconstructed in memory from the live source. The live file
contains exactly:

- one repaired disconnected-group theorem sentence and zero copies of its
  predecessor sentence; and
- four occurrences of `pq\,u_1` and zero occurrences of the malformed
  `pq,u_1`.

Reversing only those five lines does the following:

1. replaces
   `\xi D\subseteq V_m$, every component of $D$ is a translate of $D^0$,
   and hence the same bound holds for $\dim D$.`
   by
   `\xi D\subseteq V_m$, the same bound holds for $\dim D$ by passage to
   every component of $D^0$.`; and
2. replaces the four literal `pq\,u_1` strings by `pq,u_1`.

The reversal produces exactly SHA-256
`d81575674ac40cf7d816e00d53a77d2d4e841f22cbee8cd039d3cbe73eca99b2`,
72678 bytes, and 1213 LF characters. Reapplying precisely those five changes
reproduces the live 72701-byte source byte for byte and returns SHA-256
`9cf03af659631ad7ec4228c05927733c620b111bb3840fa3555b32325cfcc977`.
The bibliography is unchanged. The repair is therefore exact, bounded,
reversible, and free of unannounced drift.

## Governance and predecessor gates

The canonical publication lock is 62682 bytes and one LF at SHA-256
`641da77ac8fa8188c585130b11ef00250383aa477d9d876d490a7a3a2f2ecff2`.
It passes duplicate-key and nonfinite rejection, recursively sorted compact
round-trip, terminal-LF, and self-byte/self-hash exclusion. All fifteen input
bindings and the publication-scope binding match their frozen path, SHA-256,
byte, and LF records.

The exact stage arrays are sorted, unique, and have their declared counts.
`U_D20` differs from `U_P18` only by the two sources, and `U_S21` differs from
`U_D20` only by this review path. The prior reviews retain the exact terminal
tokens `SOURCE_DESIGN_PASS`, `SOURCE_LOCK_PASS`, `PAPER_PLAN_PASS`, and
`PUBLICATION_STAGE_PASS`. The publication review is 31269 bytes and 565 LF at
SHA-256
`30eb09aeb5e41ffd7fe3fb0220c5711fd7827a9ab7ad8a476df5800317709f7f`.

## Front matter, abstract, and article structure

The source has the exact class line `\documentclass[11pt]{article}`, the
exact locked title, `\author{Anonymous}`, an empty date, and anonymous blank
PDF author/subject/keyword/creator/producer fields.

The abstract is citation-free, history-free, result-first, and anonymous. I
replayed the robust counter by stripping comments, isolating the abstract,
replacing maximal math spans by separate `MATH` tokens, preserving ordinary
argument text, removing formatting commands/braces, normalizing ties and
whitespace, and counting maximal word tokens with internal apostrophes or
hyphens plus each math token. The result is:

- robust word count: **197**;
- math-token count: **8**;
- normalized counter-snippet bytes: **1353**; and
- normalized counter-snippet SHA-256:
  `d490ee03925391d88ff944890ac2e7c361ac7ec24f89d238ebea2637fb7c821c`.

The count lies within the locked 180--220 range.

There are exactly eight numbered main sections, in the required order:

1. Introduction and anchor-loss question;
2. Shift-like recurrences, survivor varieties, and the Laurent bridge;
3. Characters on recurrence cosets;
4. Sharp anchored torus-coset decay;
5. Equality subtori and sharp arithmetic clock;
6. Zero-anchor local partition calculus;
7. Exact zero-constant phase and third-step closure; and
8. Assumption boundaries, contextual separation, and conclusion.

There is no appendix or starred main section. Exactly one `\clearpage`
occurs after Section 8 and before the single final bibliography invocation;
`\end{document}` follows the bibliography with no public content after it.
Part A remains dominant in theorem order, common setup, proof length, equality
construction, arithmetic endpoint, and conclusion. Part B reads as the exact
loss-of-anchor boundary of the same character-deficit mechanism.

## Part A theorem and proof audit

The anchored theorem and every mandatory bridge pass:

1. The type-`nu` map, inverse, one-based map coordinate, zero-based scalar
   recurrence, `m`-transition convention, survivor variety, arithmetic
   window, and projection bijection all have the frozen orientation.
2. Successive monic future-variable elimination gives
   `A_{n+1}=A_n[g_n^{-1}]`. The source proves the ring isomorphism, the
   nonvanishing of `g_n`, integrality, and the absence of hidden components.
3. On a connected coset, ambient coordinates restrict to nonzero scalars
   times characters; group-algebra characters are a basis; and a nonzero
   singleton is impossible after collection.
4. With nonzero constant and at least two actual nonconstant powers, the
   constant/power list has at least three distinct characters against only
   two endpoints. The middle character is therefore trivial.
5. The aggregated equation is split exhaustively. If `P(xi_t)` is nonzero,
   both endpoints are trivial. If it is zero, the proof obtains both
   `chi_(n+k)=chi_n` and `xi_(n+k)=a xi_n`.
6. Every equation supplies the kernel relations
   `A_n=epsilon_(k+n-nu)` and
   `B_n=epsilon_(k+n)-epsilon_n`.
7. All `2m` relations are integrally independent: the `A_n` pivots form the
   length-`m` interval, the endpoint pairs are disjoint, and each pair has a
   coordinate outside that interval occurring in no other relation. The
   endpoint cases `m=0` and `m=k` are explicit.
8. The ambient-character restriction map is surjective. Rank subtraction in
   the full `k+m` lattice gives `dim H<=k-m`; no future character is omitted.
9. The copy relations reduce every future character before middle indices are
   reduced to initial residues. The killed set is exactly the translation
   `{n-nu mod k:0<=n<m}`, with `m` distinct residues, not a subtraction
   orbit. No gcd hypothesis, phase, or conclusion occurs.
10. The repaired theorem now states correctly that, for
    `xi D subseteq V_m`, every component of `D` is a translate of `D^0`;
    the later proof applies the connected theorem to the corresponding
    contained translates and uses `dim D=dim D^0`.
11. Under the sufficient conditions `a=1` and `P(1)=0`, the source verifies
    every recurrence on `H_m`, constructs the free quotient lattice, proves
    its relation lattice is a direct summand and saturated, and obtains
    `H_m` isomorphic to `G_m^(k-m)`.
12. At `m=k`, geometric coset exclusion precedes the Laurent bridge and gives
    qualitative `T_k` finiteness; longer windows are subsets of `T_k`.
13. For arbitrary prescribed support, the rational coefficients
    `a=b_j=1,c=-s`, free residue `q=k-1-nu`, and `Gamma=<2>` give the exact
    infinite `T_(k-1)` family. The source does not universalize this example.

The theorem statement now matches what the proof establishes. No hidden
assumption, quantifier reversal, inequality-direction error, or unproved
Part A lemma remains.

## Part B support phase and proof audit

The exact zero-anchor theorem and every branch of its classification pass:

1. The source fixes `k=2`, `nu=1`, `c=0`, `a` nonzero, finite collected
   positive-exponent support, and the exact first three scalar equations.
2. A trivial middle character is split into nonroot endpoint killing and the
   root-copy relations `u_(n+2)=u_n`, `xi_(n+2)=a xi_n`; later equations
   explicitly close every copy branch.
3. Linear support has the direct all-window chain
   `(t,rt,...,r^(m+1)t)` with `r^2=beta r+a`, and the compatible
   `beta=2,a=-1,r=1,Gamma=<2>` family is kept outside nonlinear finiteness.
4. A nonlinear monomial has only the nontrivial local relation
   `u_(n+2)=u_n=d u_(n+1)`; two equations give `(d^2-1)u_1=0`.
5. For support size at least three, at least one middle power is a singleton;
   the second equation closes both the nonroot and root-copy scalar branches.
6. For binomial support, `A`, `B`, and `C` exhaust the trivial-middle case and
   the two endpoint-to-power orientations. Endpoint-endpoint pairing leaves
   two singleton powers and gives no fourth label.
7. The scalar signs and orientations in the `B` and `C` rows agree with the
   signed restricted recurrence. No coefficient is divided out unless it is
   a nonzero actual coefficient or torus coordinate.
8. All nine adjacent words are derived. `AA,AB,AC,BA,CA` close directly;
   `BB` and `CC` require `pq=1`; `BC` requires `q^2=1`; and `CB` requires
   `p^2=1`. The repaired four products now render unambiguously as
   `pq\,u_1`. Only `CB` with `p=1` survives.
9. For support `{1,d}`, the surviving vector is `(du,u,u,du)`. The first
   `C` and second `B` scalar equations force exactly `a=-beta^2` and the
   displayed coordinates of `C_d` with the correct signs.
10. Both recurrence equations are verified directly on `C_d`. Ambient
    characters generate a cyclic lattice; positive dimension is one; and the
    nonzero `x_1` character is surjective over the algebraically closed field.
    Hence the coset equals all of `C_d` and is unique as a geometric subset.
11. A third `A`, `B`, or `C` label is impossible after `CB`; the latter two
    give `(d-1)u=0` and `(d^2-1)u=0`. If the first four characters are
    trivial, the third recurrence forces the fifth character trivial. Thus
    every nonlinear support has no positive-dimensional coset in `V_3^0`.
12. Only after every support case is declared does the source invoke the
    finite-rank bridge to obtain qualitative `T_2` or `T_3` finiteness.

The support list is exhaustive, the exceptional locus is necessary and
sufficient, and the theorem excludes the linear phase from nonlinear
finiteness. No unclosed root-copy, scalar, character, or fifth-coordinate
branch remains.

## Laurent bridge and arithmetic quantifiers

`Laurent1984` is the sole external proof input. The manuscript states only the
qualitative complex-torus division-group consequence needed here and invokes
it only after geometric positive-dimensional-coset exclusion.

The internal bridge is complete. A rational basis of finite-rank `Gamma`
generates a finitely generated `Gamma_0`; for each element, denominator
clearing and an element-dependent torsion-killing exponent put a positive
power in `Gamma_0`. This includes arbitrary infinite torsion and assumes
neither finite generation nor bounded torsion. The coefficient/generator
field is finitely generated over `Q` and embeds in `C`; only the relevant
algebraic extension is embedded, never all of the original field. Cartesian
powers and injective transfer are explicit.

The conclusions remain qualitative. No effective count, exceptional-locus
algorithm, height estimate, enumeration, or second Diophantine theorem is
introduced.

## Sharp examples and geometric/arithmetic separation

Every locked example has the correct recurrence orientation and compatible
group quantifier:

- anchored equality: `a=b_j=1`, `c=-s`, free residue `k-1-nu`, and
  `Gamma=<2>` give infinite `T_(k-1)`;
- linear zero-anchor: `beta=2`, `a=-1`, `r=1`, and `Gamma=<2>` give an
  infinite family in every window;
- nonlinear monomial: `(x_0,x_1,x_2)=(t^e,t,2t^e)` for `P=X^e,a=1`;
- arbitrary multisupport: the displayed nonzero coefficients give `P(1)=0`
  and `(x_0,x_1,x_2)=(t,1,t)`; and
- resonance: `beta=delta=1,a=-1,Gamma=<2>` gives
  `(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d)`.

The source consistently separates a geometric coset from its intersection
with a specified arithmetic group. It never turns geometric resonance into
universal arithmetic infinitude.

## Three proof tables and zero visual assets

There are exactly three `table` environments and exactly three `tabularx`
environments:

1. the Section 4 relation/pivot audit;
2. the Section 6 exhaustive `A/B/C` character/scalar table; and
3. the Section 7 nine-word and third-step closure matrix.

Every row is derived in adjacent prose. There is no fourth table, empirical
table, figure environment, `includegraphics`, external source input, raster or
vector asset, code, data, or empirical claim.

## Fifteen public anti-claims

All fifteen boundaries are explicit in mathematically natural locations:

1. dimension is assigned to cosets in `V_m`, not to `T_m`;
2. resonance does not make `T_2` infinite for every fixed `Gamma`;
3. `a=1,P(1)=0` is sufficient, not asserted necessary, for the equality
   family;
4. no gcd hypothesis or phase occurs;
5. killed residues are a translated interval, not an iterated orbit;
6. nonlinear monomials close after two steps and are not in a no-window
   class;
7. Laurent yields no effective count, algorithm, height estimate, or
   enumeration;
8. the standard singleton/character observation alone is not claimed as the
   contribution;
9. positive characteristic, `a=0`, rational/Laurent maps, and arbitrary
   polynomial automorphisms are outside the theorem;
10. actual support is not asserted affine-conjugacy invariant;
11. finite rank is not replaced by finite generation or bounded torsion;
12. no improvement of the companion's explicit planar anchored bounds is
    claimed;
13. the bounded comparison is not global, exhaustive, a first-result claim,
    or a statement about unpublished work;
14. Part A does not classify all equality or maximal cosets; and
15. no periodic-point classification or effective enumeration is claimed.

The exact public-safe predecessor paragraph occurs once, in Section 8 only.
It is absent from the abstract, Sections 1--7, theorem statements, proofs,
tables, and bibliography. The predecessor is not cited or imported as a
black-box proof dependency.

## Citation and bibliography equality

The cited key set and bibliography-entry key set are equal, with exactly
eight unique keys and no wildcard `nocite`, duplicate, missing, or uncited
entry:

1. `BedfordPambuccian1998`;
2. `BellGhioca2024`;
3. `Bera2018`;
4. `BeraVerma2013`;
5. `JiXieZhang2026`;
6. `KarimovKelmendiOuaknineWorrell2024`;
7. `Laurent1984`; and
8. `MelloYasufuku2026`.

The Laurent entry has the locked Inventiones identity, volume 78, pages
299--327, year 1984, and DOI `10.1007/BF01388597`. The distinct Bordeaux
seminar record is not substituted. Bedford--Pambuccian and Bera/Bera--Verma
are used only for shift-like provenance and complex-dynamical context. The
four remaining current sources occur only in the Section 8 comparison. The
source explicitly says that none is a proof dependency. Kaur,
Evertse--Schlickewei--Schmidt, unverified sources, and the predecessor are
absent from the bibliography.

## Static pdfTeX and source closure

The static source gate passes:

- begin/end environment multisets and nesting are exact;
- 79 labels are unique, and all 96 `ref`/`eqref` uses resolve to defined
  labels;
- all braces balance in both source files;
- the three table environments are balanced;
- title, abstract, section, clear-page, bibliography, and document-end order
  are exact;
- there is no `input`, `include`, `includegraphics`, shell escape, file-write,
  external-document, minted, or external-bibliography command;
- deterministic pdfTeX controls occur exactly once:
  `\pdfinfoomitdate=1`, `\pdftrailerid{}`, and
  `\pdfsuppressptexinfo=-1`;
- hyperref metadata explicitly blanks author, subject, keywords, creator, and
  producer while retaining the exact public title;
- the package and command set is monolithic and pdfTeX-compatible; and
- both sources contain zero TODO, FIXME, XXX, VERIFY, placeholder, draft,
  repair, governance, review-verdict, internal path/hash/number, identity,
  grant, acknowledgment, repository, submission, or operational marker.

No build was performed. Page count, final warning logs, font embedding,
decoded-PDF security, and two-clean-root byte determinism remain the separate
builder's gates; this positive source verdict does not prejudge or authorize
that stage.

## Postwrite universe and closure

All required source-level checks pass. Creating this sole review path changes
the exact project file set from `U_D20` to `U_S21` and adds no other path.
Every later artifact remains unauthorized and absent. No source revision,
compilation, finalization, release, submission, upload, external message, or
identity disclosure follows from this verdict.

MANUSCRIPT_SOURCE_PASS
