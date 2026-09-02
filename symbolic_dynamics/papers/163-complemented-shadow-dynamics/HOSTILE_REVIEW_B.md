# Hostile Review B — P163 complemented-shadow dynamics

**Reviewer role:** independent Review B; neither author nor Review A  
**Frozen input:** current anonymous Round 1, byte-identical to Round 0  
**Decision:** **ACCEPT**  
**Findings:** **0 Critical / 0 Major / 0 minor**  
**External status:** **HOLD_EXTERNAL**

## Executive verdict

I independently reconstructed the literal set-family map

```text
S_n(F)={ complement(A-{a}) : A in F, a in A }
```

and attacked every theorem axis named in the abstract.  The alternating
atomic kernels, mixed-rank clock, recurrent rank unions, atomic depth census,
central-slice equality case, support- and period-resolved deepest counts, the
`n=2` exception, and the positive-time every-target cover formula all survive.
The paper's claim boundary is disciplined: the Johnson-ball square, ordinary
shadow theory, Boolean-relation machinery, and generic cover
inclusion--exclusion are explicitly zero-credit inputs.  No theorem error,
boundary omission, source defect, build defect, anonymity leak, or
abstract/body mismatch was found.

The independent verifier makes 1,041,401 exact assertions and passed two
fresh byte-identical replays.  Two source-only cold builds settled to the
same 424,998-byte, five-page PDF as the frozen artifact.  All 32 font rows are
embedded/subset/Unicode-mapped, metadata is anonymous, and every page passed
visual inspection.

## Frozen inputs and independence

The Review-B input hashes are recorded in
`docs/papers162_166_sequence/reviews/p163_b/PINNED_INPUTS.sha256`.  In
particular:

- `main.tex`:
  `bb18ae1fbe2f9b7994efc3bdbe69917783e5e5e2acc539bbc8dcb37fbbb79e8f`;
- `references.bib`:
  `27ed70f7cb91a31fc14a6976ed022e9308da457fa3f7739af4a38bc830deb430`;
- `main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf`:
  `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`.

The new control `verify_review_b.py` constructs subsets, families, the
literal update, clocks, kernels, and Möbius inversion from scratch.  It does
not import the author verifier or Review-A evidence.  No Review-A file or
executable was used as a mathematical or control input.

## Independent mathematical findings

### 1. Atomic Johnson-ball iterate — PASS

Two steps from a nonempty `k`-set either restore the set or exchange one
chosen point with one outside point.  Thus the square is the closed-neighbour
operator on `J(n,k)`, and iteration gives the claimed even balls.  A
rank-`n-k+1` target has predecessors `complement(C) union {c}`; minimizing
over `c` gives the odd defect `|A intersect C|-1`.  The empty atom is silent
after time zero exactly as stated.

### 2. Mixed-rank clock — PASS

Every occupied rank slice must saturate at one common parity.  The maxima of
the slice covering defects and the minimum of the even/odd saturation times
give the displayed clock.  The separate empty-family, silent-singleton, and
nonempty-support branches are all necessary and correct.

### 3. Recurrent rank unions and periodic census — PASS

The square is inflationary on each connected Johnson slice, so a periodic
slice is empty or full.  Rank support follows the involution
`phi(k)=n-k+1`.  This proves the `2^n` recurrent states,
`2^ceil(n/2)` fixed states, strict two-cycles otherwise, and the stated zeta
function.

### 4. Atomic exact-depth census — PASS

The independently derived depth is

```text
min(2 min(k,n-k), 2 min(k-1,n-k)+1).
```

For each `d=0,...,n-1`, exactly the manuscript's rank `k_n(d)` realizes `d`,
with `binom(n,ceil(d/2))` atoms.

### 5. Sharp height and deepest equality — PASS

For even `n=2m`, height `2m-1` forces the central Johnson covering radius
`m`; uniqueness of the antipode makes this equivalent to a singleton
rank-`m` slice.  For odd `n=2m+1`, the odd equality can only occur at rank
`m+1`, where an `(m+1)`-set meeting every central member in `m+1` points
forces all members to equal it.  Hence for every `n>=3`, tail `n-1` holds
exactly when the central slice is a singleton.

### 6. Total/support/period deepest counts — PASS

Once the central member is chosen, every other atom (including the silent
one) is free.  Prescribing nonzero rank support gives the exact nonempty-slice
product and optional-silent factor.  Period one is equivalent to
`phi`-invariant support; factorization over rank orbits yields the stated
`q_O` formula, and subtraction gives period two.  The central two-rank orbit
when `n` is even was specifically checked: its mate is correctly forced in a
fixed support.

### 7. Exceptional `n=2` census — PASS

All sixteen phase states were enumerated.  Four are recurrent; all twelve
others have tail one.  Six enter period one and six enter period two.  The
central-slice predicate selects eight, confirming why the general
central-singleton formula must begin at `n>=3`.

### 8. Every-target cover formula — PASS

For `t>=1`, admissible nonempty source atoms are those whose kernels lie in
the target.  Inclusion--exclusion over target atoms missed by their union
gives the displayed alternating sum; the optional silent source atom gives
the factor two.  Its orientation and signs are correct.  The formula gives
two sources for the empty target, zero for any target containing the silent
atom, and the stated stable nonempty-slice product after `t>=n-1`.  The paper
correctly does not assert this formula at `t=0`.

Full proof details and boundary derivations are frozen in
`docs/papers162_166_sequence/reviews/p163_b/PROOF_REDERIVATION.md`.

## Exact independent control

Files:

- `docs/papers162_166_sequence/reviews/p163_b/verify_review_b.py`;
- `docs/papers162_166_sequence/reviews/p163_b/CANONICAL.txt`.

Frozen control data:

- assertions: **1,041,401**;
- status: **PASS**;
- verifier SHA-256:
  `7c098c5ab552fb2d136716ec7947f57d55ed23612f0bd46bdbb404d846f441fc`;
- transcript SHA-256:
  `9242436ce116ba2664a1a8ab6e5caa13f1ea82d5a08c0886e88b4f142a86eb80`;
- two fresh replays: both byte-identical to the frozen transcript.

The exhaustive boxes cover every family and target for `n=2,3,4`, while
atomic and symbolic/equality sentinels extend through `n=9` and `n=12`.
Enumeration is counterexample pressure, not a substitute for the proof.

## Owner and internal-collision audit

The fresh bounded source search directly confirmed:

- Diego--Serra--Vena's identity
  `B(S)=nabla Delta(S)=Delta nabla(S)` for Johnson balls;
- classical Kruskal--Katona shadow ownership;
- Rosenblatt, Gregory--Kirkland--Pullman, and Akin--Mrozek--Przybylski--Wiseman
  as generic Boolean-relation/power/period owners.

No source was found that directly states the literal complemented-shadow
self-map with the parity clock and central deepest-shell package.  That
bounded non-hit is not a novelty certificate.  All directly owned engines
remain subtracted.

The P1--P165 scan found no second numbered paper with the same literal map.
The closest silhouettes are P97 (sumset union growth), P110 (partition
shift--join deepest shell), P115 (Cartier depth/fibres), and P143 (Boolean
row-inclusion residual).  P162, P164, and P165 are also map-level disjoint.
Details are in `OWNER_AUDIT.md` and `COLLISION_AUDIT.md` in the Review-B
evidence directory.

## Build, anonymity, and visual audit

Two fresh source-only builds, each containing only `main.tex` and
`references.bib`, settled and reproduced the canonical SHA-256 exactly.
There are no actual LaTeX/BibTeX warnings, undefined items, rerun requests,
or bad boxes.  `pdfinfo` reports A4, 5 pages, no encryption/forms/JavaScript,
and blank author/title/subject/keyword metadata.  `pdffonts` reports 32/32
embedded, subset, and Unicode-mapped font resources.  All five 144-dpi page
renders are clean.  The visible anonymous byline and two visible
`HOLD_EXTERNAL` notices are intact.  Full numbers are in
`docs/papers162_166_sequence/reviews/p163_b/BUILD_QA.md`.

## Severity ledger

### Critical

None.

### Major

None.

### minor

None.

## Final recommendation

**ACCEPT** for internal Round-2 freezing.  No mathematical or editorial
repair is requested.  This is an internal review decision only; it does not
authorize posting, submission, circulation, specialist contact, or a novelty
claim.  The artifact remains **HOLD_EXTERNAL**.

