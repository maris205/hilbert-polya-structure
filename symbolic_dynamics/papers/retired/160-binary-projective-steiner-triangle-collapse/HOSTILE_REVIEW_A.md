# Hostile Review A — P160 Round 0

## Review status

- **Decision: KILL as a standalone research paper.** The formulas are correct,
  but the claimed residual is substantially owned on the unordered
  three-distinct quotient by Aryapoor (2013). A citation-only repair cannot
  restore a research-level contribution.
- **Finding count:** 1 Critical / 0 Major / 2 Minor.
- **External status:** `HOLD_EXTERNAL`.
- **Role:** reviewer-owned hostile stress test, not an author control and not a
  five-seat ARS panel. Calibration status is `NOT_CALIBRATED`; target/venue
  criteria were not supplied, so no venue-fit claim is made.
- **Read-only boundary:** no pre-existing P160 author file was modified. This
  report and the reviewer artifacts under
  `docs/papers157_161_sequence/reviews/p160_a/` are the only writes.

## Bottom line

The mathematical package survives independent rederivation. The four strata,
cycle and state counts, `N-2` parameterization, all positive-iterate fibres,
`GL(r,2) x S3` orbits, weak components, fibre moments, and rank recovery are
correct, including the degenerate `r=2` coefficient collision. The 2025
Kettinger--Peterson subtraction is also accurate.

The paper nevertheless fails its contribution boundary. Aryapoor's 2013
preprint defines, for a general Steiner quasigroup, the unordered map

```text
{a,b,c} -> {a star b, b star c, c star a}
```

on distinct triples; proves the relevant image and inverse bounds; and, in
Proposition 2.2, identifies the projective `PG(k,2)` equality case, including
exactly `n-3` nonblock preimages of each block and an explicit one-parameter
source set. This is precisely the quotient of P160's distinct-coordinate map
by the free `S3` action. Adding order lifts each unordered source sixfold and
equivariance distributes those lifts one per ordered target. Adding repeated
coordinates supplies only the universal diagonal and elementary
two-equal-three-cycle strata. The remaining components, moments, zeta
function, and rank-recovery formulas are automatic bookkeeping from that
graph. Thus the current paper is a clean ordered reformulation of substantial
prior mathematics, not the required new dynamical-system progress.

## Strongest counter-argument

The manuscript presents the ordered-triple viewpoint as the residual after
subtracting Steiner systems, quasigroup operations, cellular automata, and an
unrelated oriented real product. That subtraction misses the source that is
closest at the level of the actual map. Aryapoor does not merely discuss the
same carrier or the same operation: Section 2.1 writes down the unordered
pair-product transform itself, calls it `phi_S`/`psi_S`, studies its images and
fibres for general Steiner triple systems, and gives the projective equality
case. In that case every distinct input maps to a block, blocks are fixed, and
each block has exactly `n-3` nonblock inverse triples. P160's ordered result is
the free `S3` lift of this statement, plus the fixed block itself. The repeated
coordinate part follows in three lines from the Steiner identities and is not
a compensating contribution. Nor do fibre moments, components, or the zeta
function supply an independent theorem: each follows immediately from the
same census. Therefore the response “Aryapoor treats sets, while we treat
ordered triples” is insufficient. It identifies a change of bookkeeping, not
a new mechanism. Because the paper's own claim ceiling says that the retained
contribution is the complete graph plus target-resolved fibres, the missed
owner occupies the core rather than a related-work margin. Honest subtraction
leaves too little for a standalone research note.

## Independent mathematical rederivation

### 1. Four strata and exact temporal behavior

Let `P=F_2^r\{0}`, `N=2^r-1`, and use `x star x=x`, with
`x star y=x+y` for `x!=y`.

- A diagonal `(x,x,x)` is fixed.
- If `u=x+y` and `x!=y`, then
  `(x,x,y)->(u,u,x)->(y,y,u)->(x,x,y)`. The three states are
  distinct, so the period is exactly three.
- For pairwise-distinct inputs,
  `S(a,b,c)=(b+c,c+a,a+b)`. These outputs are nonzero and distinct,
  and their sum is zero. Thus they form a block. If `a+b+c=0`, the
  input is that same block and is fixed; otherwise it has depth one.

The census is consequently

```text
diagonal states       N
two-equal states      3N(N-1)
ordered blocks        N(N-1)
nonblock states       N(N-1)(N-3).
```

Hence there are `N^2` fixed **states**, `N(N-1)` strict three-**cycles**
containing `3N(N-1)` states, and `N(N-1)(N-3)` depth-one states. The
manuscript, table caption, and verifier use these two counting units
consistently.

### 2. Target fibres and positive iterates

For a block target `(x,y,z)`, solving

```text
b+c=x, c+a=y, a+b=z
```

gives `(a,b,c)=(t,t+z,t+y)`. Exactly `t=0,z,y` are forbidden, so
there are `(N+1)-3=N-2` sources. The choice `t=x` is the fixed block;
the other `N-3` sources are nonblocks and have no predecessors. Diagonal and
two-equal targets have the unique predecessor supplied by their permutation
cycles, while nonblocks are not in the image.

For every `k>=1`, a block's `k`-step predecessors remain the block plus the
same source-free leaves; on the diagonal/two-equal locus the map is a
permutation; and nonblocks remain outside the stable image. This proves the
same `1/(N-2)/0` fibre law for every positive iterate.

### 3. Symmetry orbits and components

Every invertible binary-linear map preserves equality and addition, and the
opposite-pair construction commutes with coordinate permutations. The four
classes are respectively: one repeated vector; an ordered independent pair
plus an equality position; an ordered independent pair completed by its sum;
and an ordered independent triple. Transitivity on ordered independent lists
therefore gives the stated `GL(r,2) x S3` orbits. At `r=2`, the last class is
empty.

The weak components are `N` singleton diagonal loops, `N(N-1)` isolated
three-cycles, and `N(N-1)` block-centered stars with `N-3` leaves. Their count
is `2N^2-N`. The fibre histogram is

```text
size 0:   N(N-1)(N-3) targets
size 1:   3N^2-2N targets
size N-2: N(N-1) targets,
```

with equal sizes combined. This gives every moment and the displayed fibre
enumerator. Its maximum is `N-2`, so `max fibre + 3=N+1=2^r`, including
`r=2`.

### 4. The `r=2` coalescence

At `N=3`, the nonblock count is zero and `N-2=1`. The nominal fibre-one and
block terms in `Phi_r` therefore coalesce:

```text
(3N^2-2N)u + N(N-1)u^(N-2) = 21u+6u = 27u.
```

Every one of the 27 targets has fibre one, all states are periodic, the image
probability is one, and `log_2(1+3)=2`. No boundary defect was found.

### 5. General Steiner control and the Pasch mechanism

For any Steiner quasigroup, the diagonal, two-equal three-cycle, and block
fixed-point calculations are universal. For a distinct nonblock input, write
`x=b star c`, `y=c star a`, `z=a star b`. The assertion that `(x,y,z)` is a
block is exactly the assertion that

```text
{b,c,x}, {c,a,y}, {a,b,z}, {x,y,z}
```

is a six-point Pasch configuration. In `PG(r-1,2)` this closure always holds.
Each Pasch is counted by 24 ordered nonblock sources, giving
`N(N-1)(N-3)/24` Pasch configurations, the classical maximum.

The behavior is not true for arbitrary Steiner quasigroups. In the affine
Steiner quasigroup `AG(2,3)`, with `x star y=-x-y`, the distinct nonblock

```text
((0,0),(1,0),(0,1))
```

maps to

```text
((2,2),(0,2),(2,0)),
```

which is again a nonblock and lies in a three-cycle. This independently
confirms that P160's projective restriction is mathematically substantive,
but it also identifies the established Pasch framework that the manuscript
failed to subtract.

## Source audit

### Direct owner collision

Masood Aryapoor, [*The pasch configuration and Steiner triple
systems*](https://arxiv.org/abs/1306.1257), arXiv:1306.1257v1 (2013):

- Section 2.1 defines `A(S)` and `B(S)` using the unordered images
  `{a star b,b star c,c star a}` and defines the maps `phi_S` and `psi_S`.
- It notes that `psi_S(T)=T` exactly for blocks.
- Theorem 2.1 proves the general at-most-`n-3` inverse bound.
- Proposition 2.2 characterizes the projective equality case, states exactly
  `n-3` nonblock preimages per block, gives the explicit source family, and
  derives the projective pair-sum image.

This is not a title-level neighbor. It is the unordered quotient of the
P160 map on the stratum carrying the depth-one collapse and nontrivial block
fibres. The older extremal background is also explicit in D. R. Stinson and
Y. J. Wei, [*Some results on quadrilaterals in Steiner triple
systems*](https://doi.org/10.1016/0012-365X(92)90143-4), *Discrete
Mathematics* 105 (1992), 207--219: the maximum Pasch count is attained
precisely by projective `PG(d,2)` systems.

The author already cites Falcone--Figula--Galici, [*Extensions of Steiner
Triple Systems*](https://doi.org/10.1002/jcd.21964), whose Definition 3.5 and
Theorem 3.6 discuss Pasch configurations, Veblen points, and the
characterization of projective Steiner triple systems. The current citation uses that source only
for the carrier and therefore does not repair the missing map-level
subtraction.

### Kettinger--Peterson comparison

The manuscript's distinction from Jake Kettinger and Chris Peterson,
[*Oriented Steiner Triple Systems, Steiner Products, and
Dynamics*](https://arxiv.org/abs/2507.09396), arXiv:2507.09396v1 (2025), is
accurate. Their Definitions 3--5 require an orientation, define a
skew-symmetric/anticommutative bilinear product on the real vector space
`R^S`, and their dynamics fixes `w` and iterates the linear map
`L_w(v)=w cross v` (Definitions 10--11 and Section 4). P160 instead uses the
unoriented, idempotent, finite quasigroup on points and simultaneously updates
three coordinates. The state space, multiplication, and iteration scheme all
differ.

### Metadata and read-integrity notes

- Crossref/publisher metadata matched all four DOI-bearing bibliography rows;
  the arXiv API matched both preprints.
- Primary PDFs of Aryapoor and Kettinger--Peterson were downloaded and read
  via `pdftotext`. Their SHA-256 values in this review session were
  `1020387925ee2e163ba20474631c0103d36916ab8ce0b67794b0975d74743ca3`
  and `fb902ffab00553060a1661370ee67362bb0d72bef2428cc55ad055366dba66e4`.
- ARS structural PDF preflight returned `UNAVAILABLE` because `pypdf` was not
  installed. Consequently this report uses section/definition anchors, not
  locally inferred PDF page anchors. Both files were unencrypted and were
  also checked against their primary arXiv records.
- The search remains bounded. No novelty or comprehensive-absence conclusion
  is inferred.

## Build and executable audit

### Author verifier

The author verifier cold-replayed byte-identically:

```text
assertions:        4,836,144
status:            PASS
transcript SHA256: 38b12108ba9440d2acfc2c0f0abde61f7d1daaf18f7c705f9eefd0ca6071efec
verifier SHA256:   e7066b7d3fb96d7905835675793d664a53ec2ce3aec2ffaaaf5d527f3e60cb46
```

### Independent reviewer verifier

`docs/papers157_161_sequence/reviews/p160_a/verify_p160_review_a.py` imports
and calls no author code. It checks ranks 2 through 6, explicitly computes all
fibres of `S^k` for `1<=k<=8`, constructs the `GL(r,2) x S3` orbits from
generators through rank five, verifies component shapes, fibre histograms and
moments, counts Pasch configurations with multiplicity 24, and runs the
`AG(2,3)` control.

```text
assertions:         3,166,113
status:             PASS
two cold runs:      byte-identical
canonical SHA256:   c886731fd14a260c3fab7c6318932c26624db5e93ab8913cb7804bbc68ef7104
reviewer-code SHA:  cdec78341182149d3716a50534bd71867d065314c7330618a16a78754aca0610
```

The independent edge-table hashes agree with the author transcript at every
rank; this is cross-implementation consistency, not proof of independence of
errors.

### Cold PDF build

Two source-only temporary directories, each containing only `main.tex` and
`references.bib`, were built with the documented four commands. The two PDFs,
`main.pdf`, and `main_round0_original.pdf` were byte-identical.

```text
pages / stock:  4 / A4
bytes:          355,500
PDF SHA256:     a988139ec5b9cd600ced9f7eeffdeb42e5b8f8268c1161670661cdc3d0cc84b5
encryption:     none
metadata:       identifying title/author/subject/keywords blank
fonts:          27/27 embedded, subset, Unicode-mapped
warnings:       0 unresolved refs/cites, boxes, rerun requests, or BibTeX warnings
visual QA:      all four rasterized pages legible; no clipping or overlap
```

The occurrences of `rerunfilecheck` in the log are package-loading and an
unchanged-checksum information line, not a rerun warning. BibTeX reports
`warning$ -- 0`.

## Findings

### CRITICAL C1 — The core distinct-triple map and inverse law have a direct unordered owner

- **Dimension:** contribution / ownership / literature integration.
- **Location:** Abstract lines 37--52; source-subtraction Table 1; Theorem 1(i,
  iii); the sentence declaring the retained result; `SOURCE_VERIFICATION.md`
  lines 3 and 21--23.
- **Evidence anchor:** text: “complete functional graph of the ordered-triple
  map”; text: “bounded owner non-hit for the exact coordinate map”. Aryapoor
  Section 2.1 and Proposition 2.2 define the exact unordered quotient and its
  projective inverse count/family.
- **Confidence:** 5/5 — exact primary-source formula-to-formula comparison.
- **Why Critical:** once the prior map, projective collapse, and `n-3`
  nonblock inverse family are subtracted, the retained theorem consists of a
  free ordered lift, universal equality-pattern cycles, and automatic graph
  statistics. That invalidates the paper's core claim to be a standalone
  research advance. This finding alone blocks acceptance in the present
  series, whose requirement is a paper-level new dynamical result.
- **Minimum executable action:** retire P160 as a standalone research paper or
  explicitly reclassify it as an expository/computational note. Add Aryapoor
  2013 and Stinson--Wei 1992 to any retained exposition, identify `S/S3` with
  `psi_S`, and state exactly which claims are unordered prior art.
- **Only credible salvage path:** prove a genuinely new theorem not implied by
  Aryapoor's invariants—for example, a target-resolved/iterated functional
  graph theorem for a nonprojective family of Steiner quasigroups, with a new
  owner search and exact controls. This is a new research stage, not a Round-0
  wording repair.

### MINOR M1 — Positive-iterate fibres are proved but not directly regression-tested by the author verifier

- **Dimension:** executable evidence coverage.
- **Location:** `verify_p160.py` lines 140--148 versus Theorem 1(iii), line 145.
- **Evidence anchor:** code: the exponent loop checks only whether
  `iterate == state`; it does not form the target indegree table of `S^k`.
- **Confidence:** 5/5 — direct code inspection and independent replacement
  check.
- **Impact:** no mathematical error; the one-step graph checks plus proof imply
  the claim. The gap concerns advertised executable coverage.
- **Executable fix if the paper is retained:** for each tested exponent,
  compute `Counter(S^k(state) for state in states)` and compare every target
  with the `1/(N-2)/0` law. The reviewer verifier demonstrates this check.

### MINOR M2 — One rank-recovery proof sentence is syntactically broken

- **Dimension:** writing precision.
- **Location:** `main.tex` lines 310--314.
- **Evidence anchor:** text: “When Theorem 1(iii) gives maximum fibre”.
- **Confidence:** 5/5 — direct text inspection.
- **Impact:** the intended algebra is correct and unambiguous.
- **Executable fix if the paper is retained:** delete “When” and explicitly
  note that at `r=2` the maximum `N-2=1` is attained by every target, not only
  blocks.

## Explicit non-findings

- No algebraic or counting defect was found in the four-stratum theorem.
- `r=2` does not break the fibre enumerator or rank recovery; equal exponents
  combine exactly as stated.
- `N(N-1)` consistently counts strict three-cycles, while `3N(N-1)` counts
  their states.
- The positive-iterate fibre statement is true.
- The `GL(r,2) x S3` orbit statement and component census are true.
- The fibre moments, Garden-of-Eden ratio, image probability, and zeta function
  are true.
- The distinction from Kettinger--Peterson 2025 is exact, not rhetorical.
- The author verifier is deterministic and the build is reproducible.

## Final recommendation

**KILL the current P160 research-paper slot / `HOLD_EXTERNAL`.** The result is
mathematically sound, but the Aryapoor owner collision occupies the core
distinct-triple map and inverse mechanism. A citation patch would make the
paper honest but would not make it a new paper. Continue this slot only after
a new, source-aware theorem is obtained outside the projective case (or after
an equivalently substantive change of dynamics).
