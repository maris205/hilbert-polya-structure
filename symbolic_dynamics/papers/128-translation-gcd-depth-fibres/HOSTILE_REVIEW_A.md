# P128 hostile Review A — independent nonauthor, round 0

## Decision

**GO_INTERNAL_AFTER_MINOR_REPAIR.  External release remains HOLD.**

I independently reconstructed the literal iterate, the orbit-exponent clock,
the cyclic transfer trace, the all-depth formal product, the terminal split
and every target-fibre formula.  I found no counterexample and no major
mathematical or ownership defect.  In particular, the trace does **not**
recount a support by its zeros or rotations: coordinates have a fixed cut,
and an admissible labelled support determines one and only one closed state
path.  The invariant factor in the global product also does not double-count
the orbit minima.

Two small repairs are nevertheless required before round-one freeze: make
the fixed-cut uniqueness in the trace proof completely explicit, and add the
transfer-matrix side itself to the canonical mechanical control (the current
verifier independently enumerates residual vectors but never constructs
`M_t`).  A wording repair should call the infinite expression a **formal
orbit Euler product** wherever the term could be read analytically.

Severity count:

- **CRITICAL: 0**
- **MAJOR (mathematics): 0**
- **MAJOR (owner/scope): 0**
- **MINOR: 3**

## Independence and reviewed artifacts

I did not author P128.  I read the complete manuscript, bibliography,
support package, verifier, canonical transcript, current PDF and frozen
round-zero PDF.  I did not edit any manuscript, bibliography, code, PDF or
support file; this review is the only added file.

Reviewed SHA-256 values:

- `main.tex`:
  `be420329b9b14f489536f808448e8c2729462310dac786abbf500a366bddabae`
- `references.bib`:
  `32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c`
- `code/verify.py`:
  `660a85d36a5e0796cc01056f17cf782495a7fd256e8a77201bf10cec8dce0803`
- `code/verification_output.txt`:
  `303f25ecf334d396ecb9c510cc4496d2ce5877387ebcae3661b9ec683b353930`
- `main.pdf` and `main_round0_original.pdf`:
  `e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667`

The two PDF hashes agree, so the reviewed working PDF is exactly the frozen
round-zero artifact.

## 1. Literal iterate, terminal projection and extension-field boundary

Let `sigma f(x)=f(x+1)`.  Since the characteristic is `p`, `sigma^p=1`
even when `q=p^a`; the acting group is the order-`p` prime-subfield
translation subgroup, not the full additive group of `F_q`.  Inducting with
translation as a gcd-preserving automorphism gives

\[
 T^t(f)=\gcd_{0\le j\le t}\sigma^j f.
\]

At `t=p-1` this is the gcd over the full orbit and hence is invariant.  On
an irreducible translation orbit of length `p`, write the exponent vector as
`e=(e_0,...,e_{p-1})`.  Up to reversing the chosen cyclic indexing, the
time-`t` exponents are

\[
 e_i^{(t)}=\min_{0\le j\le t}e_{i+j}.
\]

With `m=min_i e_i` and `c_i=e_i-m`, all windows of length `t+1` contain a
zero exactly when no positive cyclic run has length `t+1`.  Thus the least
terminal time is the longest positive cyclic run `lambda(c)`.  Fixed
irreducibles have no residual coordinate and no transient.  The global depth
is therefore the maximum local run length, and it lies in `0,...,p-1`.

The boundaries are clean:

- `p=2` has only depths 0 and 1; the one-state and two-state local matrices
  reduce to the displayed formulas.
- Degree zero contains only `1`, which is fixed and lies in the unit fibre.
- For a genuine extension `F_{p^a}`, the invariant ring of translation by
  `1` remains `F_q[x^p-x]`; it is not `F_q[x^q-x]`.
- Repeated irreducible factors are fully represented by arbitrary exponent
  heights, not accidentally squarefree data.

## 2. The trace does not recount cyclic supports

For a fixed coordinate cut on the labelled orbit, define the state before
position `j` to be the number of consecutive positive entries immediately
preceding `j`, capped by the admissible bound `t`.  A zero entry takes every
state to 0 with weight 1; a positive entry takes state `i` to `i+1` with
weight

\[
 u=y+y^2+\cdots=\frac{y}{1-y}.
\]

This is exactly the row-to-column matrix in the manuscript.  An admissible
support has a zero because its normalized exponent vector has minimum zero.
Starting from that zero computes the state at **the already fixed cut**; a
different zero computes the same state assignment, not another closed path.
Equivalently, the preceding-run-length formula directly gives the unique
state at every cut.  Conversely a closed path cannot use only positive
transitions, because its state would strictly increase; it therefore contains
a zero and recovers a unique labelled support and its positive heights.
Hence

\[
 R_{p,t}(y)=\operatorname{tr}(M_t(u)^p)
\]

counts every normalized exponent vector exactly once.  The trace is not a
necklace quotient and introduces no factor of `p`; nor does it multiply a
word by its number of zeros.

As a reviewer-side control independent of the package, I constructed
truncated polynomial matrices and compared the trace coefficients with
direct residual-vector enumeration for `p=2,3,5,7`, every
`0<=t<=p-1`, through degree 9 (degree 7 for `p=7`).  All **156 coefficient
assertions passed**.  This control also confirms

\[
 R_{p,0}=1,
 \qquad
 R_{p,p-1}=\frac{1-y^p}{(1-y)^p}.
\]

The manuscript's proof is mathematically correct.  MINOR A1 below requests
one sentence that removes the only possible recounting ambiguity.

## 3. Global formal product: no repeated orbit minima

The translation action on irreducibles has orbit length 1 or `p`.  On each
nonfixed orbit the decomposition

\[
 (e_0,\ldots,e_{p-1})=m(1,\ldots,1)+c,
 \qquad \min_i c_i=0,
\]

is unique.  The common-minimum factor is invariant.  Together with all
fixed irreducible powers, all such minimum factors form one arbitrary monic
element of `F_q[x^p-x]`, with series `(1-qz^p)^{-1}`.  The residual vector
is counted only in its own nonfixed irreducible orbit by `R_{p,t}(z^d)`.
Thus the invariant factor and local factors are disjoint coordinates; the
formula does not count the minima twice.

There are

\[
 a_d=\frac{N_d(q)-b_d}{p}
\]

nonfixed degree-`d` orbits.  Unique factorization and the maximum-of-local-
depths rule therefore give

\[
 H_{q,p,t}(z)=\frac1{1-qz^p}
 \prod_{d\ge1}R_{p,t}(z^d)^{a_d}.
\]

For a fixed coefficient only `d<=n` contributes, so this is a valid formal
power-series product without an analytic convergence hypothesis.  At
`t=0` it is the invariant series; at `t=p-1` it is the all-monic series
`(1-qz)^{-1}`.  Exact layers are the stated consecutive differences.

## 4. Terminal split and target fibres

Valuation by valuation, `Q(f)` keeps the full exponent on every fixed
irreducible and the common minimum on every nonfixed orbit.  Hence it divides
`f`.  Dividing gives a residual with no fixed irreducible and minimum zero on
every nonfixed orbit, so it lies in `Q^{-1}(1)`.  Conversely, for invariant
`h`,

\[
 Q(hr)=hQ(r)
\]

follows from the window gcd.  Thus multiplication is a degree-preserving
**set bijection**

\[
 \{h:\sigma h=h\}\times Q^{-1}(1)\longrightarrow\mathcal M_q,
\]

not a monoid quotient.  Dividing the all-monic series by the invariant series
correctly gives

\[
 U_{q,p}(z)=\frac{1-qz^p}{1-qz},
\quad
 U_{q,p,n}=\begin{cases}q^n,&n<p,\\q^n-q^{n-p+1},&n\ge p.\end{cases}
\]

Multiplication by a fixed invariant target `h` transports this unit fibre
bijectively to `Q^{-1}(h)`, with the advertised degree offset.  Summing the
coefficients gives the displayed capped formula; direct algebra confirms its
second numerator
`q^{L+1}-1-q^{L-p+2}+q`.
Since all `U_{q,p,n}` are nonnegative, the same formula also gives the exact
degree-cap bound without a hidden cancellation: for a cap `D` the fibre over
degree `m` is precisely the prefix sum through `L=D-m` (zero if `L<0`), and
the unit target `m=0` supplies the largest available prefix.

The terminology firewall is effective.  The manuscript never calls
`Q^{-1}(1)` a kernel and explicitly states that `Q` is not multiplicative.
Its counterexample is valid in every characteristic:
`Q(x)=Q((x^p-x)/x)=1`, while `Q(x^p-x)=x^p-x`.

## 5. Owner and internal subtraction

The direct owner boundary is substantially accurate.

The scouting label `P01` was an **old-reserve handle**, not a fresh candidate
or an earlier paper number.  Its prime-field window identity, sharp
`p-1` clock, terminal invariant ring and finite depth tables predate this
manuscript and correctly receive zero credit in the current README, plan,
abstract and Section 1.  The passage from that reserve to P128 is therefore
admissible only on the two residual outputs reviewed here: the all-depth
exponent-layer product and the exact/capped fibre over every invariant
target.  I found no sentence that attempts to reclaim the old P01 material.

- Garefalakis's primary paper explicitly treats irreducibles invariant under
  `x -> x+b`: [author PDF](https://users.math.uoc.gr/~tgaref/content/static/publications/special-irreducibles.pdf),
  DOI [10.1016/j.jpaa.2010.10.015](https://doi.org/10.1016/j.jpaa.2010.10.015).
- Reis's primary preprint and journal paper characterize translation-fixed
  irreducibles for an `F_p`-subspace:
  [arXiv:1608.03915](https://arxiv.org/abs/1608.03915), DOI
  [10.1016/j.jpaa.2017.06.008](https://doi.org/10.1016/j.jpaa.2017.06.008).
  Theorem 2(c) states
  `(p-1)/(pm) sum_{d|m,(d,p)=1} q^{m/d} mu(d)`; writing
  `m=p^v s` and substituting `e=s/d` gives exactly the manuscript's
  displayed `b_(pm)`.  That formula and the orbit quotient `a_d` correctly
  receive zero credit.
- Gerhard--Giesbrecht--Storjohann--Zima own the shifted-gcd/shiftless
  factorization interface in characteristic zero:
  [primary paper](https://bohr.wlu.ca/ezima/papers/ISSAC03_p119-gerhard.pdf),
  DOI [10.1145/860854.860887](https://doi.org/10.1145/860854.860887).
  It is a neighboring algorithmic mechanism, not a direct owner of the
  finite order-`p` depth product.
- Internally, P110 already owns the consecutive translate fold, invariant
  endpoint, finite clock and recurrent/fixed mechanism on a cyclically acted
  lattice.  P128 explicitly zero-credits this order-dual meet layer.  Its
  residual begins only at the irreducible-orbit exponent census and target-
  refined graded fibres.

The audit used literal variants of `gcd(f(x),f(x+1))`, translated/shifted
gcd iteration, cyclic exponent runs, terminal fibres and irreducible-orbit
Euler products, including 2025--2026 queries, on 2026-08-31.  I found no
primary source stating the all-depth product together with the target-
refined split.  This is a bounded non-hit only; the manuscript correctly
does not convert it into novelty or priority language.

## 6. Fresh reproducibility and presentation audit

I fresh-ran

```sh
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > /tmp/p128_verify_fresh.txt
cmp -s /tmp/p128_verify_fresh.txt code/verification_output.txt
```

The comparison passed.  Fresh and canonical stdout both have SHA-256
`303f25ecf334d396ecb9c510cc4496d2ce5877387ebcae3661b9ec683b353930`.
The run reports **180,403 assertions** over 17,523 states in explicit
`F_4`, `F_8` and `F_9` models.  It covers characteristic 2, odd
characteristic, genuine extensions, repeated factors, every enumerated
target, fixed irreducible counts and every depth-CDF coefficient in scope.

I also copied only `main.tex` and `references.bib` to a fresh temporary
directory and ran

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All stages exited 0.  The isolated PDF is byte-identical to `main.pdf` with
SHA-256
`e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667`.
The settled log/BLG scan has no warnings, undefined citations/references or
bad boxes.  The PDF has 4 A4 pages, 362,516 bytes, blank author/title/date
metadata, rotation 0, no form, JavaScript or encryption.  Every listed font
is embedded, subsetted and Unicode-mapped.  I rasterized and visually checked
all four pages; no clipping, collision, missing glyph, malformed formula or
orphan bibliography was found.

## 7. Severity-ranked required repairs

### CRITICAL

None.

### MAJOR (mathematics)

None.

### MAJOR (owner/scope)

None.  External release nevertheless remains `HOLD_EXTERNAL`; the bounded
search is not specialist novelty clearance.

### MINOR

1. **A1 — remove the last trace-recount ambiguity.**  In the proof of the
   cyclic-transfer lemma, replace “Starting just after any zero” by an
   explicit fixed-cut statement: the state before coordinate `j` is the
   length of the positive run immediately preceding `j`; choosing a zero is
   only a way to compute this unique cyclic state assignment.  State directly
   that trace counts labelled vectors, not rotations.
2. **A2 — put `M_t` into the canonical verifier.**  The present verifier
   independently enumerates residual vectors and successfully tests the
   global product, but it never constructs the displayed matrix.  Add a
   truncated polynomial-matrix trace and compare its coefficients with the
   existing direct `residual_vector_series` for every tested characteristic
   and threshold.  Record the new assertion count and canonical hash.
3. **A3 — tighten the product terminology.**  At first use and in the title
   of Theorem 3.2, say “formal orbit Euler product” (or equivalent), retaining
   the coefficientwise-well-defined sentence.  This avoids suggesting an
   analytic Euler product or multiplicativity of `Q`; no formula changes.

## Provisional verdict

**GO_INTERNAL_AFTER_MINOR_REPAIR / HOLD_EXTERNAL.**  The lead all-depth
formula and the second target-fibre package survive hostile reconstruction,
including `p=2`, extension fields and degree-zero boundaries.  Repairs A1--A3
are local and do not require a theorem rewrite.  A round-one reviewer should
verify the new trace-control count and ensure that “formal orbit” wording did
not expand the ownership claim.
