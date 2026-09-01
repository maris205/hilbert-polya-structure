# Batch review: HCS-C269--HCS-C273

## Release basis

This review is extracted from the five final release manifests, their bound
physical artifacts, and the final proof audit, not from the earlier idea
report.  Every package is
`RELEASE_COMPLETE`, is bound to source commit
`9cb7483e97ef82fdc06d45ecb3043f183ce22391`, evaluator v0.2.0 SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788134400` (2026-08-31 00:00:00 UTC), and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  Each package closes 27 manifest payloads plus
its self-excluded manifest, retains three substantively different PDF rounds,
uses two fresh two-pass builds per round, and makes the final PDF
byte-identical to round 2.

Across the batch, the producer-independent checkers close 65,525 assertions,
the symbolic reconstructions close 823 checks, and hostile testing rejects
114/114 changes.  The five canonical evidence files contain 2,734,029 bytes.
The final papers total 13 pages and 111 embedded/subset font records.  These
are release-accounting totals; the heterogeneous field vertices, trajectory
samples, network cases, spectral roots and random-walk histories are not
collapsed into a scientifically meaningless single observation count.

After the repairs, a read-only audit reran all thirty producer, checker,
symbolic, replay, mutation and manifest commands in temporary copies.  A
second independent C270 audit also reconstructed its numeric schema and read
the complete cut/conjugate proof.  Fresh deterministic final-PDF builds,
ledger closure, checker independence, source/evaluator/epoch locks and the
claim firewall all passed without modifying the release trees.

## Five theorem-scale advances

### HCS-C269 -- finite-field Chebyshev functional graphs

For every prime power `q` and degree `d`, including characteristic two,
nonprime fields and the separate constant face, the paper reconstructs the
entire normalized Chebyshev/Dickson functional graph from multiplication by
`d` on the two cyclic covers of orders `q-1` and `q+1`, folded by inversion
and glued at the exact ramified intersection.  This closes all fixed and
primitive counts, cycles and finite source zeta factors, tail layers and
height, image ranks, and the full-function Koopman characteristic polynomial
with exact zero-Jordan multiplicities.

Evidence scale: 121 maps over 11 independently validated field models, 1,914
direct vertices, 77 nonprime-field cases, 33 characteristic-two cases, 535
fixed-count cells, 203 cycle cells, 250 tail cells, 371 image-rank cells and
121 zero-Jordan cells.  The evidence is 182,471 bytes.  The checker closes
32,499 assertions, SymPy closes 311 identities, and hostile testing rejects
41/41 attacks.  The final paper has 3 pages and 25 embedded/subset fonts.

Release-integrity repair: an early checker accepted a repaired-hash mutation
that replaced the frozen irreducible modulus for `GF(4)` by a reducible
polynomial.  The final independent checker verifies the characteristic is
prime, the modulus is monic of the declared degree and irreducible over
`GF(p)`, and all degrees for a fixed `q` use the same field model.  The new
mutation is rejected.  The finite, generally nonnormal composition operator
also no longer receives a natural-quantization score.

Route-A verdict: `ROUTE_A_EXPLORATORY`, Route B disabled,
`(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL,
A4_FORMAL_HINT)`.

### HCS-C270 -- standard Heisenberg sub-Riemannian geometry

For the frozen real `H^1` frame and unit-speed Hamiltonian clock, the paper
integrates every normal geodesic, excludes nonconstant abnormal extremals,
computes the exact exponential Jacobian, and proves equality of the first
conjugate, first rotational Maxwell and cut times at `2*pi/|lambda|` for
`lambda!=0`.  The `lambda=0` geodesics are lines with no finite such time.  It
identifies the nonzero vertical axis as both the cut and first-conjugate locus
and proves the complete Carnot--Caratheodory distance formula, including the
horizontal and vertical endpoint faces.

Evidence scale: 800 trajectory rows, 64 regular-distance rows and 12 vertical
rows, with 10,972 numeric cells recounted from an explicit three-family field
schema.  The evidence is 905,104 bytes.  The checker closes 11,139 assertions,
the symbolic reconstruction closes 20 identities, and hostile testing rejects
27/27 attacks.  The final paper has 3 pages and 14 embedded/subset fonts.

Release-integrity repair: the final package does not confuse one horizontal
rotation with a closed geodesic.  Nonzero vertical momentum produces vertical
drift and zero vertical momentum produces a line, so A1 was lowered from weak
to fail throughout the evidence, checker, evaluation, paper and manifest.
The numeric-cell receipt is now derived independently from named fields rather
than accepted as a hard-coded total.  The Dido step states and proves the
unique sub-full-turn arc needed for the global cut argument.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C271 -- irreducible heterogeneous network SIS

For `x'=beta*diag(1-x)Ax-Dx` with irreducible `A>=0` and positive diagonal
`D`, the paper proves the global disease-free/endemic threshold from the
spectral abscissa of `beta*A-D`.  Above threshold it proves the unique
interior equilibrium attracting every nonzero state, a Hurwitz endemic
Jacobian and strict componentwise
transmission monotonicity.  At equality it proves, for every nonzero initial
state, the sharp normalized Perron law
`t*x(t) -> v/[beta*w^T*diag(v)A*v]`.

Evidence scale: 240 exact parameter cases and 720 critical samples.  The
evidence is 445,039 bytes.  The checker closes 8,724 assertions, SymPy closes
33 identities, and hostile testing rejects 11/11 attacks.  The final paper
has 2 pages and 22 embedded/subset fonts.

Proof-integrity repair: the final proof does not assume that a critical orbit
already lies on a center manifold.  With `P=vw^T`, `a=w^Tx`, `y=(I-P)x` and
`z=y/a`, positivity gives `a` comparable to `||x||`, while the stable
variation-of-constants equation on `ker(w^T)` gives `z->0`.  It follows that
`-a'/a^2` tends to the stated positive coefficient and hence the asserted
`1/t` law holds for arbitrary nonzero critical trajectories.  An independent
read-only proof audit confirmed this bridge and its normalization.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

### HCS-C272 -- Erlang age-transport semigroup

For mortality transport on `L1(R_+)` with an Erlang fertility boundary, the
paper computes all `k` algebraic roots of the cleared Euler--Lotka
denominator, but calls a root an `L1` eigenvalue only when it lies strictly to
the right of the mortality-shift essential edge `Re(lambda)=-mu`.  It proves
that the newborn contribution is a compact perturbation of the shift,
separates the isolation threshold `beta=1` from the population threshold
`beta=(1+mu/gamma)^k`, and obtains operator-norm rank-one asynchronous growth
when the dominant pole is isolated.

Evidence scale: 360 parameter cases and 2,340 algebraic-root cells.  The
evidence is 1,152,543 bytes.  The checker closes 12,635 assertions, SymPy
closes 48 identities, and hostile testing rejects 11/11 attacks.  The final
paper has 2 pages and 25 embedded/subset fonts.

Proof-integrity repair: for every fixed positive time, the final proof maps an
`L1` bounded set to an equicontinuous boundary-history family, uses the
Volterra renewal resolver and newborn-triangle map, and obtains compactness by
Arzela--Ascoli.  Therefore the Calkin class is exactly that of the mortality
shift and the essential growth edge is `-mu`.  Simplicity and separation of
the dominant pole then give the claimed quasi-compact operator-norm
asymptotic.  An independent read-only proof audit confirmed both bridges and
the positive-data trichotomy.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C273 -- Sparre--Andersen universal fluctuations

For iid continuous increments symmetric about zero, with strict positivity
and no ties frozen, the paper proves
`q_n=binom(2n,n)/4^n`, its square-root generating function and the exact
first-descent law.  It then proves that both the number of positive partial
sums and the unique maximum time have mass `q_k*q_(n-k)`, and that both
converge after scaling to `Beta(1/2,1/2)`.  A simple symmetric atomic walk
separates strict, nonnegative and tied-maximum conventions exactly.

Evidence scale: 41 survival rows, 561 arcsine cells, 12 scaling receipts, 8
atomic families and 695,482 complete permutation histories.  The evidence is
48,872 bytes.  The checker closes 528 assertions, SymPy closes 411 identities,
and hostile testing rejects 24/24 attacks.  The final paper has 3 pages and 25
embedded/subset fonts.

The independent proof audit found no repair necessary.  The finite histories
are regression receipts; universality is proved by the permutation/cycle
factorization, and the atomic example is used only to delimit the no-ties
hypothesis.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

## Exact release hashes

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C269 | `e6a19af6b27e300f3ce2c9b20c6ff0eb6d93678c504c991cf427bc483e5aa3c3` | `81b38a2277a4e593a89082ea9a4161d14eeafceea39c3be764b7a33c6ed7432e` | `cee059de35dfb9e0d98f298a08aee59c780343d5228d6f995c6711cf7835e8eb` | `c966e31fe276300869a18ff7460952f850b7810e1cc0d4df3481d62da0fd5e0a` | `c1e0431dc6762a643735007df3239cf536a1f4ca995342d5db0845205edf4888` |
| C270 | `86bbae2b0610357cf6fba54a5334e5225c135b8255fd760d4c6f967e9e99dcaa` | `3345dd19e8302eda8557682dbaba555aa5091188e1baed69ea54482794dad9ca` | `8032e0ac5ed5f68b366b254813fd28bb76c26c3aa94312a396a9e929a1209cfa` | `21134aa7aa51475bb686a9ceae9ebe83414aee6ebd38f2b8277f8f14db694cfa` | `a00a6a39482d00a3996deee3496ecd37ec0686a33ce7c10720b90c975429add3` |
| C271 | `5e034383f5469286d8cbb4d877786cca6c68908ed8f31a7678b043364c1209a1` | `dc5784b015d69721c60033708b5bd03fcd8d1a631bf4e18506d8ccc67d86a0fa` | `58faff18875db3e3b916dff5bf2275654985d6e4c7c5b4244f866e3f97252928` | `666b0e3e62cef878a88caf0305d9cdc6e6331e1ddab42c76369f1e9973c0c03e` | `b30551942eab5a957de2eb60165f8dfcf680baba0be6daf1346c5833b650cc39` |
| C272 | `0afd59cf1df3feaf278dba7c74e7b82b6f96422fbca2d4ea51e697163b782dbe` | `34695190fa613ff2f163c03c150892adf513fb884e5993addfb12b0f70d75df8` | `df472f2578a0dbf724cbd31a274122dc168af6742e4df2ba4a5f381262e21a18` | `06bb70f11ddb1e3dbcdf72a89896b88feb843c354c29a4eac5640dfc9bc350de` | `67f5dbfc0d69c383f2c7a9a0a570cd7a26b139a8203bc4417141ab1da7b681cd` |
| C273 | `8aa9827fd90be07158c08cc6a72d2b55cb479daf2c025079ecca6d787d0618b7` | `802b6d4d4eefa87e5d47f48b937030cc25528b402e032d9623609e66a9a0d825` | `0aa02262c71052c5765aa4ae2ad9b2acef5faeced00e0bb91071093eb264468f` | `0f81c47565325f0a1fd296f8de0af7468638bc9981f197b9ed08d4cacda80b52` | `935b20cd372e6236c33b6c369707c220b8eb8ddd0a2a428833a94ab8688c93ba` |

For every row, the three retained revision hashes are distinct and the final
PDF hash equals the round-2 hash.  The five manifests and their hash-bound
compile reports record deterministic fresh builds, embedded/subset fonts,
settled logs, extractable text, visual inspection, byte replay, semantic
mutation rejection and manifest closure as `PASS`.  The
target-operator/Route-B gate is explicitly `NOT_CLAIMED`.

## Citation, proof and reproducibility integrity

The six registered references are used only for model or theorem lineage:
Qureshi--Panario and Gassert for finite-field Chebyshev graphs, Gaveau for the
standard Heisenberg model, Lajmanovich--Yorke for deterministic network
epidemics, M'Kendrick for age-structured population transport, and Sparre
Andersen for the classical fluctuation identity.  Author, title, venue, year,
pages and DOI were checked against publisher records, every bibliography item
is cited in its declared context, and no displayed theorem is outsourced to a
reference.  The Cambridge record dates M'Kendrick's volume to 1925, while the
original paper carries a 1926 read/received history; the package records that
metadata convention explicitly.  Workspace ownership is not a
literature-priority claim.

For a separate originality control, a Pandoc-AST count found 63 substantive
prose paragraphs after excluding headings, pure display blocks, tables and
bibliographies: 13/16/9/11/14 in C269--C273.  The audit sampled
8/9/6/6/7 distinct paragraphs respectively, 36/63 or 57.14 percent overall,
with every paper at or above 50 percent.  Forty-two quoted searches of
distinctive phrases returned no exact external match.  This is a heuristic
collision screen, not a plagiarism detector or a literature-priority proof;
unindexed and paywalled text, poor OCR, translations, paraphrases, formulas
and code can escape exact-phrase search.

The final integrity audit explicitly considered the seven recurrent
AI-research failure modes:

1. **Implementation bug -- clear.**  Each evidence producer has a
   producer-independent semantic checker, independent symbolic
   reconstruction, fresh-path byte replay and repaired-hash mutation tests.
   The C269 field-model hole was found by this audit and repaired before
   release.
2. **Citation hallucination -- clear.**  All six records passed existence,
   metadata, context and ghost-citation checks.
3. **Hallucinated result -- clear.**  Every reported finite count and hash is
   bound into canonical evidence and a 27-payload manifest; arbitrary-model
   theorems are supported by written proofs rather than extrapolated grids.
4. **Shortcut or hidden singularity -- clear.**  Characteristic two,
   reducible-modulus attacks, zero momentum, vertical endpoints, arbitrary
   critical SIS trajectories, the `L1` essential edge, strict/no-ties and
   atomic boundaries are explicit.
5. **Bug reframed as insight -- clear.**  A1 and A4 downgrades and the two
   proof repairs were completed before the narrative, evaluations and
   manifests were frozen.
6. **Methodology fabrication -- clear.**  Assertion, symbolic, mutation,
   evidence-byte, page and font totals agree with the executable receipts and
   physical files.
7. **Frame lock -- clear.**  The collision audit tested alternative
   subtypes, rejected near-duplicate owners and retained five different state
   spaces, clocks and proof technologies.

Automated text search and finite regression cannot certify semantic
completeness by themselves.  They are used as adversarial controls around the
independent mathematical proof audit, not as replacements for it.

## Claim firewall and batch verdict

The firewall is common and literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package
claims a target arithmetic local datum, bad Euler factor, root number,
automorphy statement, target divisor/counting law, target functional equation,
target zero match or Hilbert--Polya identification.  In particular:

- C269's zeta and Koopman data are finite **source dynamical** invariants;
  field indices are not rational-prime orbit labels.
- C270's Maxwell/conjugate phase is not a closed complete geodesic, and its
  Hamiltonian is not promoted to a target operator.
- C271's Perron threshold and equilibria are continuous network data, not
  arithmetic primitive cycles.
- C272's renewal poles are population-semigroup data, and roots left of the
  essential edge are not even `L1` eigenvalues.
- C273's probability generating functions and arcsine laws are stochastic
  source transforms, not Euler products or deterministic orbit determinants.

Finite enumeration and high-precision evaluation are explicitly bounded
regression receipts.  Route B is disabled in all five manifests.  The batch
therefore records one exploratory Route-A result, C269, because it has weak
finite-field arithmetic and complete analytic source-cycle structure while
still failing target-data and target-divisor matching.  C270--C273 remain
conservatively `ROUTE_A_REJECTED`; no source zeta, Hamiltonian, Perron law,
renewal pole or probability transform upgrades those verdicts.
