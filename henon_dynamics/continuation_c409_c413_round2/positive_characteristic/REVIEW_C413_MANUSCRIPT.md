# Independent internal manuscript review: C413 integral trace map

Reviewer: `/root/scout_nonaffine_charp`, not the C413 manuscript author.
Date: 2026-09-06.

## Decision

**The current complete LaTeX manuscript proves its main theorem as stated.**
The classification, all-period exclusion, proper-escape statement and
fixed-level return/zeta laws pass mathematical review. The source attribution
preserves the distinction between classical periodic families and the claimed
integral exhaustiveness theorem. No new mathematical assumption or weakening
of the main statement is required.

There is one minor but worthwhile precision repair in the finite-check prose,
recorded as R1 below. The existing PDF also predates two already disclosed
author-side prose corrections; it must be rebuilt from the reviewed source
before final release (R2). Thus the present decision is
`MANUSCRIPT_PROOF_PASS; MINOR_FINITE_CHECK_CLARIFICATION; FINAL_PDF_BUILD_PENDING`,
not a final artifact release certificate.

This is a new, actual-manuscript review. The coordinator's earlier
[proof review](../REVIEW_TRACE_ROOT.md) is provenance, not my review of this
manuscript. This report is current-team internal review, not human peer review,
an external-model review, a journal decision, a worldwide priority certificate,
or a formal Route-A evaluation.

## Materials actually read

I read all of the following files in full:

- [Main source](../papers/C413_integral_trace/main.tex), all six included
  `sections/*.tex` files, and the complete `references.bib` (759 source lines
  across those files).
- [Paper plan](../papers/C413_integral_trace/PAPER_PLAN.md),
  [citation audit](../papers/C413_integral_trace/CITATION_AUDIT.md), and
  [author build report](../papers/C413_integral_trace/BUILD_REPORT.md).
- The text extracted from all ten pages of the existing
  [initial PDF](../papers/C413_integral_trace/main.pdf). This was a text read,
  not visual final-page QA, and the PDF/source discrepancy is explicitly
  handled below.
- The complete [source ledger](../nonlinear_geometry/SOURCE_LEDGER.md),
  [exact-check receipt](../nonlinear_geometry/VERIFICATION.md), and
  all 175 lines of [the supplementary checker](../nonlinear_geometry/verify_trace_contract.py).
  I also read the existing coordinator proof review as a prior record, after
  reading and checking the complete actual manuscript.
- The primary-source passages in the independent source section below.

No old sealed proof package was changed, no accepted finite census was rerun,
and no author TeX file was edited by this reviewer. The mathematical reasoning
in this receipt comes from checking the current manuscript itself.

## Exact claim, assumptions and dependency map

The object is the bijection
$T(x,y,z)=(y,z,yz-x)$ on $mathbb Z^3$, with inverse
$T^{-1}(x,y,z)=(xy-z,x,y)$ and invariant
$K=x^2+y^2+z^2-xyz$. The clock is the ordinary iterate of this one map.
The theorem classifies every integral periodic point, with no bound on its
period, height or integer level, into the disjoint orbits
$O,E,D,A_m,B_m,C_m$ for $m\geq1$.

Proof status under the strict-proof skill: **PROVABLE AS STATED**.

The proof dependencies are acyclic:

1. The two-sided recurrence, invariant and explicit cyclic words establish
   existence, exact least periods, heights, levels and disjointness.
2. A coordinate of maximal absolute value in an arbitrary periodic word
   supplies the neighbour bound and its equality case.
3. The zero/sign alternatives and unit cube exhaust the remaining possibilities.
4. Injectivity of any nonperiodic two-sided orbit in a lattice yields proper
   escape; no quantitative real escape theorem is invoked.
5. Exact orbit counts on one fixed level yield all-time fixed-point counts
   and the elementary finite orbit product. The factorization of 7 resolves
   the overlap of the two arithmetic supports.

No cited theorem supplies an unproved step in items 1--5.

## Mathematical proof audit

### 1. Recurrence, reversal and all displayed orbits

The inverse and invariant identities are correct. The scalar recurrence
$x_{i-1}+x_{i+2}=x_ix_{i+1}$ is valid for every integer index, so shifting
to a maximum is legitimate in the original clock. Reversal of the scalar
indices preserves this same recurrence; it is not a quotient by signs or
a replacement of $T$ by a power.

I checked the transitions in the entire twelve-triple table, including the
sign-sensitive transitions through indices 4, 6, 8 and 11 and the last return
to index 0. The current source correctly traverses by numeric index, not by
physical row in the two-column table. The four-letter and six-letter words
also close under the recurrence.

For $m\geq2$ the unique positive occurrence of $m$ excludes repetition of a
shorter scalar word in the four- and twelve-letter families. The source does
not incorrectly apply that argument at $m=1$: it separately checks all four
and twelve triples there. Different heights separate parameters, and exact
least periods separate the three families and the special orbits. The four
modulus-two points with positive product split into the fixed point $E$ and
three-cycle $D$, as claimed. Together with the origin this gives five special
points, not five fixed points.

### 2. Maximum bound and every exceptional branch

The two equations at $|u|=M\geq2$ give $|a|,|b|\leq2$. If $b=2\eta$,
equality in $2\eta u=a+x_2$ forces both summands to be $\eta u$; the
other neighbour relation then gives $M^2\leq M+2$, hence $M=2$.
The four resulting signed triples are exactly $E\sqcup D$. Negative $u$
and the case $|a|=2$ are both covered, the latter by the proved reversal.

After eliminating modulus-two neighbours, integrality is used explicitly to
reduce them to $\{-1,0,1\}$. Two zero neighbours give the axis orbit with
both signs of $u$. With exactly one zero neighbour the displayed recurrence
steps produce $t(1-u^2)$, whose modulus $M^2-1$ exceeds $M$ even when
$M=2$. This eliminates the complete branch.

For nonzero neighbours, $abu<0$ would give $|bu-a|=M+1$; otherwise
$u=abM$. The four surviving triples agree with $B_M$, $C_M$, and the
specified fourth and eighth iterates of $C_M$. No sign quotient merges
the four-cycle and twelve-cycle.

In the unit cube exactly four nonzero triples of negative product are
excluded by an immediate modulus-two entry. The other 23 points partition
as $1+6+12+4$, and the already verified disjoint $B_1,C_1$ together have
the exact 16 points needed in the last two classes. This is a full finite
counting proof, not an invocation of computational output.

### 3. Proper escape and the finite-cube consequence

A nonperiodic two-sided orbit of a bijection is injective, so it visits any
finite bounded subset of the lattice only finitely often. This proves the
two norm limits, a stronger statement than mere unboundedness, without
assuming coordinatewise monotonicity. The manuscript clearly avoids a
quantitative growth-rate claim.

The end of Section 3 correctly counts 49 states **whose whole orbit remains
in** $[-2,2]^3$. Its 125-step first-exit certificate follows because 126
successive states inside a 125-element set repeat; the entire resulting
periodic orbit is then contained in the finite path in that cube.
This is distinct from counting all globally periodic initial points which
happen to be inside the cube. R1 asks Section 5 to retain this exact wording.

### 4. Every level and every ordinary time

The two parameter-to-level maps are injective for positive integer
parameters. The quadratic support condition is exactly the positive odd
square condition on $4k-7$. All exact orbit-count indicators and their
divisibility contributions to $F_k(n)$ agree with the classification.

In the intersection argument the first factor in
$(2r-2m+1)(2r+2m-1)=7$ is indeed positive, because
$r^2=(m-1/2)^2+7/4$ and $r,m\geq1$; the second is strictly larger.
Thus the factors are 1 and 7, so the only intersection is $r=m=2$ and
level 4. The exceptional count is $1+3+6+4+12=26$.

The dynamical zeta formula has the correct negative exponents and is valid
as a formal series and for $|t|<1$. Its rational continuation follows from
the finite orbit product on each fixed level. The explicit warning that
$\#\operatorname{Fix}(T^6;\mathbb Z^3)=\infty$ correctly prohibits an
unqualified whole-lattice finite-count zeta.

The rational period-two example is correct, and prevents a false extension
from integers to rationals. The ordinary clock and original integer lattice
remain visible in all theorem statements and tables.

## Independent primary-source check

The following is the scope of this reviewer's actual source reading; it does
not inherit a claim that the coordinator read something on my behalf.

| Primary source | Material independently inspected | Result for this manuscript |
|---|---|---|
| [Roberts--Baake 1994](https://web.maths.unsw.edu.au/~jagr/RB94.pdf) | Header and map/invariant normalization, Eq. (29), surrounding text on printed pp. 849--852, and the actual printed p. 850 Table I image | The half-trace scaling is correct. The axis family, four-period family and sign-linked twelve-period family are classical and are explicitly credited |
| [Roberts 1996](https://web.maths.unsw.edu.au/~jagr/R96.pdf) | Theorem 4.1 and Remarks 4.1--4.2; Theorem 4.2 and Corollary 4.1; Theorem 4.3 with proof; Extensions 5.1--5.2 and their surrounding arguments | General real/complex escape and growth theory is correctly subtracted. No such growth theorem is claimed or needed by C413 |
| [Humphries 2016 v1](https://arxiv.org/html/1611.02743v1) | Introduction and definitions, complete Theorem 1, its stated axis exception and proof in Section 3 | The quantifier is the full group, or every group element, not this one map. The non-axis half-trace point $(-1/2,3/2,-1/2)$ on level 2 is outside those alternatives |
| [Ghosh--Sarnak v3](https://arxiv.org/html/1706.06712v3) | Abstract, introduction through the Markoff group definition and Theorem 1.1 | Finite orbit count versus infinite orbit size is explicitly distinguished in the primary text. C413 uses this as context, not as proof of a single-word periodic classification |
| [Vishkautsan v2](https://arxiv.org/pdf/1504.07099v2) | Abstract and Sections 1.1--1.2, including the coefficient normalization, reflection maps and residual-periodicity definition | The map, domain and local/global question differ. The zero-level predecessor is properly deducted instead of promoted as new |

For the Roberts--Baake table, web text extraction was inadequate. I therefore
viewed the existing rendering of printed p. 850 from the actual author-hosted
PDF; the PDF SHA256 is
`524d281026f0c763f6fda829ae63cb892cb7a53291539caa2a435a68f9f5f6ed`.
The period-four representatives are visibly
$(-1/2,a,-1/2)$ and $(-1/2,1/2-a,-1/2)$, agreeing with the
normalization used in the manuscript.

All five bibliography entries are cited. The Humphries item is explicitly
version-pinned, with no invented journal. No uninspected source theorem is
used as a hidden step in the main argument. The manuscript makes no unsupported
first-ever claim. This check supports its narrow ownership statements, not
exhaustive worldwide priority.

## Supplementary evidence scope

I read the verifier and its execution receipt, and checked their relationship
to the source prose; I did not rerun them. The finite partial-permutation
graph identifies cycles entirely contained in the specified cube. It does
not call an unclosed trajectory globally nonperiodic merely because a time
cutoff expired. The 68,921-state graph and its 445 cyclic states have that
finite scope. The layer-return checks are consistency checks against generated
orbits and are not independent proofs of universal exhaustiveness.

The recorded checker and receipt hashes at review time are:

```text
41b4145cf8368e792e0e41d8b08184b711736560be054516609005721efc3106  verify_trace_contract.py
cde600a2c2d8915ca61c91e8d1a3fe50a29966dfb150699f18ab4436d02178a5  VERIFICATION.md
```

No numeric or empirical statement in Section 5 is used to justify a missing
quantifier in the proof. The existing auxiliary variable named `nonperiodic`
in the small-cube checker means outside the cycles contained in that cube;
it must not be interpreted as a new global mathematical classification.

## Requested clarifications and remaining release work

### R1. Preserve the whole-cycle-in-cube qualifier in Section 5.2

At [the current source lines 44--46](../papers/C413_integral_trace/sections/5_scope.tex),
replace the shortened wording about “49 periodic states” and “escape of the
other 76 states” by wording such as:

> On the smaller cube, the checks recover 49 states on cycles wholly contained
> in the cube and verify that each of the other 76 initial states leaves this
> cube in both time directions within nine iterates. Leaving this cube need
> not mean that the initial state is globally nonperiodic.

The reason is concrete: $(-1,-2,-1)$ lies in $[-2,2]^3$ and is in $B_3$,
so it is globally periodic, although
$T(-1,-2,-1)=(-2,-1,3)$ leaves the cube immediately. The main theorem and
Section 3 already have the right quantifiers. This is a precision repair to
the diagnostic description, not a theorem correction or a demand for new tests.

### R2. Rebuild the final reviewed source, not the older initial PDF

The PDF present at review time has ten pages and SHA256
`9f7d55c1484714b51d148b9aa65c05ca3230495aa354d8b680b9d6334af4fc52`.
The author report correctly discloses that it predates two source prose fixes.
The current source corrects (i) the numeric-index traversal of the two-column
table and (ii) the direction of the implication from whole-group finiteness
to one-map periodicity, removing an inaccurate compact-level phrase.
I read and accept those current source corrections; I do not accept the older
PDF prose as the final reviewed artifact.

The coordinator's already required final clean builds and all-page visual QA
should run after adjudicating R1. No extra mathematical census is requested.

## Reviewed source hashes

```text
35eb55a08f71e55971e75c66d6bfc34f55cdb5ecfdd76aa154a724f82ec1e4cc  main.tex
c4d0fd7ebadeb613ffc58cddd6971399a2882af54b336b585584fd4360c68f23  references.bib
dd53b66f78718506b121fd4fb552177978a6afd1340be441ccfd9da677377238  sections/0_abstract.tex
56b1fd707faa58d49997b325f9d089dfd1350c455f66094fd25026d77b86f70b  sections/1_introduction.tex
d90b9727ddd304c5fedea5311ada39f207e01825bf23b787cad9d27906a77ad4  sections/2_itineraries.tex
b9999fb90b7a0531d50922e1a2ffcf778fbd01cf1e6171fbad5780b551de257a  sections/3_exhaustiveness.tex
eb5038ab7fed841e8ac6be601a351980db856613c5873b509b7c58f3c29aa1fc  sections/4_level_arithmetic.tex
386f0472c7bfa35584c82a5ede779f7fa83200863e6488040f6938763bc2b9c8  sections/5_scope.tex
```

Final internal disposition: the complete current mathematical manuscript
survives unchanged in its theorem statements. Credit remains with the
classical orbit constructions and escape inputs; the admitted increment is
the all-integer, unrestricted-period exclusion. No target Euler, root-number,
zero/divisor or Hilbert--Polya conclusion is established.

## Follow-up verification of R1 (2026-09-06)

I read the coordinator's revised Section 5.2 in the actual source. Both
445 and 49 now explicitly count states on cycles wholly contained in the
respective cube. The other 76 small-cube initial states are described only
as leaving that cube in both time directions. The text explicitly warns
that this does not imply global nonperiodicity and gives the correct
counterexample $(-1,-2,-1)\in B_3$, whose image is $(-2,-1,3)$.
R1 is resolved; no theorem or classification change is needed, and no
experiment was rerun for this prose verification.

The revised `sections/5_scope.tex` has SHA256
`141b591d949c70902d9cd1f98be9144e1c5118e27dbc276d1364900d6a62f328`.
This follow-up supersedes R1 only and preserves the earlier source/PDF
snapshot as historical review evidence. R2, the coordinator's final clean
builds and visual QA of the final source, remains a release-stage task.
