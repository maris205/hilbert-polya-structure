# Hostile Review B — P164 cyclic equality-feedback dynamics

**Reviewer role:** independent Review B; neither author nor Review A  
**Frozen input:** current anonymous Round 1  
**Decision:** **ACCEPT**  
**Findings:** **0 Critical / 0 Major / 0 minor**  
**External status:** **HOLD_EXTERNAL**

## Executive verdict

I independently reconstructed the literal map

```text
T_q(w)_i = 1{w_i=w_(i+1)}
```

and attacked every theorem axis named in the abstract.  The nonlinear
change-mask multiplicity, affine Rule-102 tail, dyadic one-block
nilpotence, sharp point clock and shell census, all-time image staircase,
every-target q-weighted affine enumerator, time-two complementary-pair
spectrum, and midpoint duplicated-half spectrum all survive.  The repaired
endpoints also survive: at `t=n` the image consists of two targets and the
zero-target fibre is exactly the positive last shell; at `j=n` all sources
collapse to the all-one target.

The independent verifier makes 7,718,087 exact assertions and passed two
fresh byte-identical replays.  Two source-only cold builds settled to the
same 301,337-byte, four-page PDF as the frozen Round-1 artifact.  All 23 font
rows are embedded/subset/Unicode-mapped, identifying metadata is blank, the
visible anonymous/HOLD markers are intact, and every page passed visual
inspection.  No theorem error, proof gap, boundary omission, source defect,
internal collision, build defect, anonymity leak, or abstract/body mismatch
was found.

## Frozen inputs and independence

The complete Review-B input hashes are recorded in
`docs/papers162_166_sequence/reviews/p164_b/PINNED_INPUTS.sha256`.
The principal hashes are:

- `main.tex`:
  `6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218`;
- `references.bib`:
  `9cbcc889eeb5ed72891d70d50150cc1783026edc3aa05d8f2f948a23bbb10ac7`;
- current `main.pdf` and `main_round1.pdf`:
  `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26`;
- author canonical transcript:
  `dddbb6ba053c908fb60321b717867da925bdd2c9af3d723f93175367a180997f`;
- Review-A canonical transcript:
  `5ad48573820c14d20f881dd131eb0b7551024b239fb6eb6868ec003c749e830e`;
- Review-A report:
  `1c1093a906592a3575d8a2a930e84fb9688b0045b37999691f51593c3cf06bea`.

The earlier verifier and canonical artifacts were pinned as immutable inputs
but were not imported, executed, or used to generate Review-B mathematics.
The new control constructs q-ary words, the literal equality update, masks,
the binary difference operator, depths, images, and fibres from scratch using
only the Python standard library.

## Independent mathematical findings

### 1. Literal iterate and mask multiplicity — PASS

With `c_i=1{w_i!=w_(i+1)}`, the first step is `1+c`.  On binary words the
next step is `1+Db`, where `D=I+S` and `D1=0`; hence
`T_q^t(w)=1+D^(t-1)c(w)` for every `t>=1`.

For a fixed mask of weight `r`, contracting equality edges leaves a proper
q-colouring problem on the cyclic change quotient.  Its exact source
multiplicity is

```text
(q-1)^r + (-1)^r(q-1).
```

For `q>=3` this vanishes exactly for unit masks.  The exceptional `r=0` and
the two-edge multigraph case are both covered by the same formula.

### 2. Dyadic repeated root, point clock, and shells — PASS

The cyclic module is `F_2[x]/((x+1)^n)` when `n` is a power of two, and `D`
is multiplication by `x+1`.  Thus `D^n=0`, `dim ker D^j=j`, and
`im D^j=ker D^(n-j)` including both endpoints.  This gives the printed
pointwise depth, unique recurrent all-one state, and the cumulative-kernel
shell differences.

For every dyadic `j<n`, `D^j=I+S^j`; kernel words consist of `j` free bits
repeated `n/j` times.  Evaluating that product enumerator gives the checkpoint
formula exactly.

### 3. Last shell and sharp height — PASS

`ker D^(n-1)` is the even-weight hyperplane, so the final shell is the total
q-weighted mass of odd masks:

```text
(q^n-(q-2)^n)/2 - (q-1)2^(n-1).
```

Writing `x=q-1>=2`, the manuscript's lower bound
`x(nx^(n-2)-2^(n-1)) >= x2^(n-2)(n-2)>0` is valid for every stated
`n>=4`.  Hence the height is sharply `n+1`; this is not merely a nonempty
finite-box observation.

### 4. Image staircase and every-target fibres — PASS

The first image omits precisely the complements of the `n` unit masks.  For
`t>=2`, set `j=min(t-1,n)`.  Every coset of `ker D^j` has a feasible mask:
if a representative is a forbidden unit, adding the all-one kernel vector
produces a feasible mask of weight `n-1>=3`.  This repair is valid through
the capped endpoint `j=n`.  Therefore the stated image and cardinality are
exact.

Summing the independently rederived change-mask multiplicity over
`D^j c=y+1` gives the displayed every-target affine enumerator.  Nonbinary
positive-time targets have zero fibre.  Every all-time source/target mass
check closed exactly.

### 5. Time-two complementary-pair spectrum — PASS

`im D` is the even-weight hyperplane and `ker D={0,1}`.  Each supported
syndrome therefore has one complementary solution pair.  Summing the two
mask multiplicities yields the printed function of the smaller weight
`rho`.  There are `binom(n,r)` parameter classes for `r<n/2` and half the
central binomial coefficient at `r=n/2`.

The paper correctly distinguishes these parameter counts from aggregated
numerical values.  In the advertised `n=4,q=4` sentinel, the `r=1` and `r=2`
fibre values both equal 24 and merge to seven supported targets.

### 6. Midpoint spectrum — PASS

At `j=n/2`, `D^j=I+S^(n/2)`, so supported syndromes are exactly duplicated
half-words `(u,u)`.  Opposite coordinate pairs contribute `1+a^2` when the
syndrome bit is zero and `2a` when it is one.  This gives

```text
W_(n/2,d)(a)=(1+a^2)^(n/2-h)(2a)^h,
```

and evaluation at `a=q-1,-1` gives the printed formula and
`binom(n/2,h)` parameter multiplicity.  Spectrum aggregation and total mass
also pass independently.

### 7. Endpoint and exclusion attacks — PASS

- At `t=n`, `j=n-1`, the image is `{0,1}` and the all-zero target has the
  exact last-shell fibre.
- At `t=n+1`, `j=n`, all `q^n` sources map to the all-one word; later times
  remain there.
- At `q=2`, feasible masks are the even-weight masks, so the printed q-ary
  support and first-image theorem must be excluded.
- At `n=2`, complementary repair maps a unit to the other unit, and the
  claimed image staircase fails exactly as the limitations section says.
- At nondyadic `n=6`, `D^n` is nonzero and feasible masks need not absorb in
  the claimed window.
- At nondyadic exponent `j=3` for `n=8`, `D^j` is not `I+S^j`; the paper
  correctly limits its closed checkpoint formula to dyadic `j`.

Full line-by-line derivations are frozen in
`docs/papers162_166_sequence/reviews/p164_b/PROOF_REDERIVATION.md`.

## Exact independent control

Files:

- `docs/papers162_166_sequence/reviews/p164_b/verify_review_b.py`;
- `docs/papers162_166_sequence/reviews/p164_b/CANONICAL.txt`.

Frozen control data:

- assertions: **7,718,087**;
- status: **PASS**;
- verifier SHA-256:
  `b4a591e4f9a69c31debf00753ae443efde5445a06508ddc9b5e8e0ee79b47c31`;
- transcript SHA-256:
  `843ded22172b6ea0abe5b3fd29243b0a6c66b8a412c9795112763cfcf1072007`;
- two fresh replays: both byte-identical to the frozen transcript.

The literal boxes cover all words, all positive iterates through the stable
cap, and every binary target for `(n,q)=(4,3),(4,4),(4,5),(4,6),(8,3),(8,4)`,
totalling 74,355 sources.  The two special spectra are independently checked
for `n=4,8,16` and `q=3,4,5,7`; dyadic rank/last-shell sentinels extend to
`n=32`.  Enumeration is counterexample pressure, not a replacement for the
all-parameter derivation.

## Owner and internal-collision audit

Fresh primary-record checks confirmed Martin--Odlyzko--Wolfram as generic
algebraic CA background, Kim as the direct periodic Rule-102 matrix-power
owner, Zhao--Li--Yang--Fu--Shum v3 as a current repeated-root weight-
distribution owner, and Bolognesi--Ciancia as an equality-pattern CA
neighbour on a different carrier.  The manuscript assigns all of those
engines zero contribution credit.

No inspected primary record directly stated the literal finite q-ary map
together with its q-weighted affine target atlas and the time-two/midpoint
spectra.  This is only a bounded non-hit and does not establish novelty.

The P1--P165 audit found no second numbered paper with the same literal map.
The closest internal silhouettes are P57, P63, P90, P98, P109, P115, P117,
P127, P138, and the same-batch P162/P163/P165.  Each differs at the literal
carrier and update; P63/P98 share only already-subtracted binary derivative
or repeated-root machinery.  Detailed source and collision ledgers are in
`OWNER_AUDIT.md` and `COLLISION_AUDIT.md` in the Review-B evidence directory.

## Build, anonymity, and visual audit

Two fresh source-only builds, each containing only `main.tex` and
`references.bib`, settled and reproduced the canonical PDF byte for byte.
Both final logs have zero warnings, undefined references/citations, rerun
requests, bad boxes, or errors; both BibTeX runs have zero warnings.

`pdfinfo` reports A4, 4 pages, no encryption/forms/JavaScript/custom metadata,
and blank author/title/subject/keyword fields.  `pdffonts` reports 23/23
embedded, subset, and Unicode-mapped font resources.  Text scanning found no
identity, affiliation, email, local path, TODO/FIXME, or review-edit leakage.
The visible `ANONYMOUS` and `HOLD_EXTERNAL` tokens remain intact.  All four
144-dpi page renders are clean.  Full numbers are in
`docs/papers162_166_sequence/reviews/p164_b/BUILD_QA.md`.

## Severity ledger

### Critical

None.

### Major

None.

### minor

None.

## Final recommendation

**ACCEPT** for internal Round-2 freezing.  No mathematical, source,
editorial, or build repair is requested.  This review decision does not
authorize posting, submission, circulation, specialist contact, novelty, or
priority claims.  The artifact remains **HOLD_EXTERNAL**.

