# P46 paper plan

This writer-side plan is bound to the protected Stage0 and canonical State-A
snapshots. It is not a paper, a publication seal, or an authorization to write
the authority tree. Canonical evaluated evidence is used only for finite
implementation replay; every infinite theorem and endpoint remains
proof-owned.

## Working identity

- Working title: **Dyadic-Sum Hankel Operators: Sharp Ideal Thresholds,
  2-Adic Blocks, and Labeled Cycle Equations**.
- Alternate concise title: **Sharp Ideal Walls and Labeled Cycle Calculus
  for a Dyadic-Sum Hankel Operator**.  Both titles deliberately say
  ``labeled'': the cyclic solver classifies a fixed ordered edge-label
  system and is not advertised as a primitive-orbit enumerator.
- Format: anonymous, self-contained mathematical article; 11pt A4 article,
  not forced into an ICLR/NeurIPS/ICML template.
- Type: theorem paper with exact finite implementation replay.
- Section count: an unnumbered abstract, 8 main sections, and 4 appendices.
- Page budget: no conference-template limit is imposed.  The executable
  budget is 11.25 A4 pages through Section 8, 1.25 pages of references, and
  4.8 pages of appendices, for a target of about 17.3 pages total.  The
  section-level allocation below already includes three vector figures and
  two compact tables.
- One-sentence contribution: For the Dirichlet-weighted adjacency of the
  looped graph `m+n=2^a`, we prove the sharp compact, Hilbert--Schmidt, and
  trace-class walls `0`, `1/2`, and `1`, expose its exact `v_2`-scaled
  bounded-operator direct sum on `Re(s)>0`, and solve every ordered dyadic
  cyclic closure system by a complete odd/even criterion.
- Claim boundary: one frozen operator on `ell^2(N)` with loops retained, the
  real-logarithm branch, and one-edge marker `z`; no all-`S_p` theorem, no
  rational-prime emergence, no completed target divisor, no Hilbert--Polya
  operator, and no priority claim.

## Reader contract

The paper tells one story: the same dyadic additive constraint controls both
the operator's metric phase diagram and the algebra of its closed walks.
Equal 2-adic valuations produce exact self-similar blocks; alternating linear
closure produces the cycle solver. Generic Schur, Schatten, and regularized
determinant machinery is supporting infrastructure and receives no novelty
credit.

The article must distinguish three evidence types at first use:

1. analytic proof establishes every infinite-operator claim and endpoint;
2. canonical finite replay checks two independent implementations;
3. integrity and mutation audits establish reproducibility, not mathematics
   or novelty.

## Main theorem ledger

Let `s in C`, `sigma=Re(s)`, and consider the coefficient array

```text
H_s(m,n) = 1_{m+n=2^a for some a>=1} (mn)^(-s/2)
```

where the real logarithm defines the complex power and loops are retained.
We write `H_s` only for a bounded operator on `ell^2(N)` having these matrix
coefficients; the first assertion characterizes exactly when that bounded
realization exists.  In that region let `A_s` be the compression to odd
positive integers.  The paper will prove, with each legal domain stated
locally:

1. The coefficient array defines a bounded (then automatically compact)
   operator `H_s` iff `sigma>0`; for `sigma<=0` no bounded operator with
   these coefficients exists.
2. `H_s in S_2` iff `sigma>1/2`, and `H_s in S_1` iff `sigma>1`.
3. Every legal edge preserves `v_2`.  If `sigma>0`, so that the matrices
   define bounded operators on the stated Hilbert spaces, then
   `H_s ~= direct_sum_{k>=0} 2^(-ks) A_s` by a basis-reordering unitary.
   No all-`s` equivalence of unbounded operators is asserted.
4. If `sigma>1/2` and `r>=2`, then `H_s^r` and `A_s^r` are trace class and
   `Tr(H_s^r)=Tr(A_s^r)/(1-2^(-rs))`.
5. On `sigma>1/2`,
   `det_2(I-zH_s)=product_{k>=0} det_2(I-z 2^(-ks)A_s)`, locally uniformly
   in `z`. On `sigma>1`, the ordinary trace is
   `Tr(H_s)=1/(1-2^(-s))`; only there is the ordinary Fredholm determinant
   authorized, with its own locally uniform direct-sum product and the
   overlap identity
   `det_2(I-zH_s)=det(I-zH_s) exp(z Tr(H_s))`.
6. For an ordered cyclic tuple `q_i=2^(a_i)`, iterating
   `n_(i+1)=q_i-n_i` gives
   `(1-(-1)^r)n_1=sum_i (-1)^(r-i)q_i`. For odd `r` there is one candidate,
   accepted exactly when every derived vertex is positive. For even `r`,
   the alternating label sum must vanish.  With
   `b_1=0`, `b_i=sum_{j<i}(-1)^(i-1-j)q_j`,
   `L=max_{i odd}(-b_i)`, and `U=min_{i even}b_i`, the positive solutions
   are exactly
   `n_1=x in Z intersect (L,U)` and
   `n_i=(-1)^(i-1)x+b_i`.  The interval may be empty and contains
   `max(0,U-L-1)` integers.  The odd block retains exactly the odd `x`.

The main theorem must not say that the cyclic solver counts primitive orbits
by itself. It classifies the vertex solutions for a fixed ordered label
tuple. Primitive reduction and cyclic base-point quotienting remain separate.

## Canonical evidence binding

- Protected authority snapshot: 60 regular files; snapshot TSV SHA-256
  `ca9f33594949f405e3df72404d35ebd4d26d8fd1f314d7be940367709ed905e8`.
- State-A result-ledger SHA-256:
  `fa22dde6ec3a9cbd473528ebb619863ac7beb0d1c9cc807394541501153add37`.
- Writer canonical summary SHA-256:
  `c86887d3e7e9602cfebaec3e0b03e534d243af576166115fd7825f130a8ec774`.
- Mechanically rendered writer ledger SHA-256:
  `a0f669a865382da47776754d0a785d81fd7243fbb4f1d5f270dddeb5acfbe7a6`.
- Canonical comparison: 4 complete support cutoffs, 335,922 ordered label
  tuples, and 36 exact rational trace cases, with zero support, cycle, and
  trace mismatches under strict recursive type-and-value comparison.

## Claims--evidence backbone

The detailed matrix is in `CLAIMS_EVIDENCE.md`. Its current high-level
shape is:

| Claim | Proof owner | Canonical replay owner | State-A status |
|---|---|---|---|
| Bounded/compact iff `sigma>0` | row-sum decay, finite compression, row-one obstruction | proof-contract replay only; finite endpoint fields explicitly infer no theorem | expected audit fields replayed with PASS; infinite result remains analytic-proof-owned |
| `S_2` iff `sigma>1/2` | exact anti-diagonal levels | endpoint-formula and proof-contract replay | expected strict-endpoint fields replayed with PASS; no finite theorem inference |
| `S_1` iff `sigma>1` | entrywise summability and disjoint trace-dual matchings | proof-contract replay | matching-obstruction check recorded as PASS; infinite result remains analytic-proof-owned |
| exact `v_2` bounded-operator direct sum on `Re(s)>0` and legal trace/`det_2` product | valuation lemma plus ideal argument | support/valuation and exact finite trace replay | four cutoffs and 36 traces agree exactly; infinite factor remains proof-owned |
| complete odd/even solver | recurrence and positivity/parity conditions | independent direct-walk versus algebraic-solver exhaustion | 335,922 ordered tuples; zero mismatches |

The pre-output smoke values in `PREOUTPUT_STATIC_SEAL.json` are architecture
evidence only. They must not be quoted as canonical evaluated results.

## Planned section architecture and page allocation

The allocations below total 11.25 pages through the end of Section 8 and
include all main-text figures and tables.  Appendix allocations are stated
separately so that proof completeness cannot silently consume the main-text
budget.

### Abstract (0.35 page; 170--210 words)

- State the frozen operator and the three strict walls in the first two
  sentences.
- Give the bounded-operator `v_2` direct sum, legal trace/regularized-
  determinant domains, and ordered odd/even cycle theorem without implying
  a primitive-orbit count.
- End with the canonical replay counts explicitly labeled finite
  implementation evidence rather than proof.

### 1. Introduction (1.35 pages; includes Fig. 1)

- Open with the three sharp walls and exact 2-adic self-similarity, rather
  than generic Hankel history.
- Explain why the endpoint walls require three different witnesses.
- State the cycle solver as the arithmetic counterpart of the block theorem.
- Give three concrete contribution bullets: phase diagram, valuation/block
  product, and complete cyclic closure.
- Preview the finite replay only as an independent implementation check.
- State the novelty and Hilbert--Polya firewalls explicitly.

### 2. Related work and ownership boundaries (0.85 page)

- Synthesize classical Hankel/Schatten theory (Peller), lacunary Schur and
  folding machinery (Fournier--Wagner), finite power-of-two Hankel
  determinants (Guo), finite distinct-label graph systems (Alekseyev), and
  regularized determinants (Simon) by mathematical role rather than as a
  paper-by-paper list.
- State exactly what each source owns and subtract those ingredients from
  the contribution.  Alekseyev is used only for finite distinct-integer
  graph labeling and restricted power-of-two linear (in)equations.
- Phrase the literature result only as a bounded-search absence; make no
  priority claim.

### 3. The dyadic-sum source and operator (1.40 pages)

- Define the looped graph, countable edge shift, one-edge clock, primitive
  vertex-cycle type, marker, branch convention, and `H_s`.
- Verify the identity entrywise and, equivalently, on every finite
  compression:
  `P_N H_s P_N=U_t P_N H_sigma P_N U_t`, with `U_t` restricted to the
  compression.  On `sigma>0`, where the full matrices define bounded
  operators, pass to `H_s=U_t H_sigma U_t`.  For `sigma<=0`, make only the
  coefficient/finite-compression statement and say that the formal matrix
  has no bounded realization.  This left--right factorization
  transfers boundedness, compactness, singular values, ideal membership,
  and corresponding norms only.  It is not unitary conjugacy and does not
  transfer spectra, powers, traces, or determinants; those later claims are
  proved for the actual complex matrix from the valuation direct sum.
- State immediately that for `s!=0` the Dirichlet factors make this a
  diagonally weighted dyadic Hankel support, not a classical Hankel matrix
  whose entries depend only on `m+n`.
- List loop locations and give the exact support/valuation lemma.
- Include a small typed table separating vertices, derived edge labels,
  closed walks, the marker `z`, and valuation weights.

### 4. Boundedness and compactness at the wall `sigma=0` (0.95 page)

- Derive the absolute row sum from neighbors `2^(A+j)-m`.
- Keep the uniform bound and the limit `R_m -> 0` separate.
- Prove norm approximation by finite compressions.
- Use the row `m=1` as an infinite `ell^2` obstruction for `sigma<=0`.
- State that no cutoff singular value proves this endpoint.

### 5. Sharp Hilbert--Schmidt and trace-class thresholds (1.80 pages;
includes Fig. 2 and Table 1)

- Write the exact dyadic anti-diagonal formula for `||H_s||_2^2`.
- Treat `0<sigma<1`, `sigma=1`, and `sigma>1` separately.
- Isolate the central lower bound at `sigma=1/2`.
- Prove trace-class sufficiency from entrywise absolute summability.
- Prove necessity through pairwise disjoint `Q_j=4^j` matchings and a
  uniformly norm-one finite-rank partial isometry.
- Include a compact phase table with strict endpoints.

### 6. 2-adic self-similarity, traces, and legal determinants (2.10 pages)

- Decompose `ell^2(N)` by exact valuation subspaces.  State the unitary
  bounded-operator equivalence only for `sigma>0`; the support calculation
  alone does not create a closed unbounded operator theorem for
  `sigma<=0`.
- Derive the scaled odd block and the trace-power geometric factor.
- Separate the `r=1` ordinary trace-class statement from `r>=2` traces in
  the Hilbert--Schmidt domain.
- Prove the `det_2` direct-sum product in a self-contained Appendix-B lemma:
  combine all block eigenvalues, use the square-summability bound by the
  Hilbert--Schmidt norms, and prove normal convergence of the canonical
  product on compact `z`-sets from
  `log((1-w)e^w)=O(w^2)`.  Simon is cited only for the standard definition
  and background machinery.
- Put the determinant statement in the main text as a proposition with a
  3--5 line proof sketch: the valuation unitary gives the block union, the
  squared Hilbert--Schmidt block norms are summable, and the canonical
  factors therefore converge normally on compact `z`-sets.  Appendix B
  supplies the detailed zero/eigenvalue bookkeeping and compact-uniform
  tail bound.
- State local uniform convergence in `z` and prohibit every determinant
  outside its ideal domain.
- Separate the entire identity from its logarithm: the factors and product
  are entire in `z` and converge uniformly on compact sets, whereas
  `log det_2(I-zH_s)=-sum_{r>=2} (z^r/r)
  Tr(A_s^r)/(1-2^(-rs))` is asserted only on the zero-free disk
  `|z| ||H_s||<1`, using the branch normalized to zero at `z=0`.
- In the trace-class overlap `sigma>1`, also give
  `det(I-zH_s)=product_k det(I-z2^(-ks)A_s)` locally uniformly and
  `det_2(I-zH_s)=det(I-zH_s) exp(z Tr(H_s))`; neither identity is inferred
  from the left--right phase factorization.

### 7. Complete labeled cyclic closure calculus (1.55 pages; includes
Fig. 3)

- Derive the recurrence and closing equation before giving examples.
- Odd length: unique candidate, then positivity; integrality is automatic.
- Even length: put `b_1=0` and
  `b_i=sum_{j<i}(-1)^(i-1-j)q_j`, so
  `n_i=(-1)^(i-1)x+b_i`.  After the alternating compatibility condition,
  define
  `L=max_{i odd}(-b_i)` and `U=min_{i even}b_i`; the positive solutions are
  exactly `x in Z intersect (L,U)`.  The interval is allowed to be empty;
  because `L,U` are integers, its unrestricted count is
  `max(0,U-L-1)`.  For `A_s`, retain only odd `x`.
- State the ranges locally: the ordered cycle solver permits `r>=1` because
  loops are retained, while trace powers in the Hilbert--Schmidt-only strip
  use `r>=2`.
- Verify the frozen examples `(2,4,4)`, `(4,8,8,4)`, and `(4,4,8,4)`.
- Explain precisely how the solver yields a matrix-independent trace
  evaluator without retyping label tuples as primitive temporal orbits.

### 8. Independent replay, limitations, and conclusion (0.90 page; includes
Table 2)

- Report only canonical State-A facts extracted from sealed JSON.
- Separate finite support/cycle/trace agreement from the proof audit.
- Give the consumer/mutation summary only as reproducibility metadata.
- Preserve Fournier--Wagner ownership of Schur/reflection/folding/
  alternating lacunary machinery and make no priority claim.
- Subsection 8.1 (0.50 page) reports replay and ownership only.
- Subsection 8.2, **Conclusion** (0.40 page), restates only the proved
  package, gives the exact non-goals (no all-`S_p`, rational-prime,
  completed divisor, functional equation, or fixed self-adjoint lift), and
  identifies one precise open question: determine the intermediate
  Schatten behavior of this same frozen operator without extrapolating from
  the `p=1,2` endpoints.

### Appendices

- A. Endpoint estimates and disjoint trace-dual matching details.
- B. Hilbert--Carleman direct sums and local-uniform product convergence.
- C. Explicit positivity interval for even cyclic systems and orbit-type
  bookkeeping.
- D. Canonical State-A result ledger and reproducibility hashes, generated
  mechanically from the now-open, hash-verified State-A output snapshot.

Appendix allocation: A (endpoint/matching details), 1.4 pages; B
(self-contained determinant direct sums), 1.6 pages; C (cycle interval and
orbit typing), 1.1 pages; D (canonical evidence ledger), 0.7 page.

## Figure and table plan

State A is now available.  No numerical plot is nevertheless justified:
the evaluated replay is exact and discrete, so a mechanically generated
table is more faithful.  The mathematical figures are vector TikZ/TeX and
contain no hard-coded experimental result.

| ID | Type | Content | Source | Gate |
|---|---|---|---|---|
| Fig. 1 | hero schematic | Dyadic anti-diagonals on the integer grid, with sample edges partitioned into `v_2=0,1,2` blocks; show the cross-valuation candidate only as a visibly crossed-out non-edge | theorem/source lock | may draft after plan review |
| Fig. 2 | phase diagram | Horizontal `sigma` axis with walls `0`, `1/2`, `1`: unbounded; compact but not `S_2`; `S_2` but not `S_1`; trace class | proved theorem | may draft after plan review |
| Fig. 3 | cycle schematic | Odd closure fixes `n_1`; even closure imposes an alternating constraint and leaves a positivity interval | cycle theorem | may draft after plan review |
| Table 1 | theorem table | exact domains, boundary witnesses, determinant legality | proof package | may draft after plan review |
| Table 2 | canonical replay | support cutoffs, ordered tuples, exact trace cases, mismatch counts | canonical State-A JSON | ready; generate mechanically from bound summary |

Hero caption draft: “The support `m+n=2^a` lies on dyadic
anti-diagonals, but every edge preserves `v_2`. Reordering the basis by
valuation therefore turns the weighted adjacency into scaled copies of one
odd block in its bounded half-plane; the highlighted edges illustrate the
exact scale law.”

The figure-quality pass must check: vector output, no title inside the
figure, readable 10pt-equivalent labels, grayscale-safe line styles, and a
self-contained caption. `Table 2` must be generated from hash-verified
canonical JSON rather than hard-coded values.

## Citation plan

- Introduction/related work: Peller (1985, 2003) for general Hankel/Schatten
  context; Fournier--Wagner (2015) for Schur-test lacunary Hankel machinery;
  Guo (2019) for the finite Hankel-determinant sequence attached to powers
  of two; Alekseyev (2026) for finite power-of-two graph labeling and
  restricted systems.
- Determinants: Simon (2005), Chapter 9, for standard regularized determinant
  machinery; reproduce the exact direct-sum argument used here.
- Every source receives a narrow ownership statement. Search absence is
  phrased as “we did not find an exact combined theorem,” never “first” or
  “novel.”
- Bibliographic metadata and claim-level verification are tracked in
  `evidence/SOURCE_VERIFICATION.md`; no entry enters `references.bib` until its
  metadata and manuscript use are both verified.

### Exact source-use map

| Source | Manuscript location | Permitted use | Imported proof dependency |
|---|---|---|---|
| Peller (1985, 2003) | Sections 1--2 | classical Hankel/Schatten context and terminology | none; all three thresholds are proved directly |
| Fournier--Wagner (2015), Sections 2--4 and 6 | Section 2 | ownership of lacunary Schur, reflection/folding, and alternating machinery | none; the row estimate used here is reproduced |
| Guo (2019) | Section 2 | finite power-of-two Hankel-determinant context | none |
| Alekseyev (2026), DOI record and full arXiv version | Section 2 | finite distinct-integer labeling and restricted power-of-two linear systems only | none |
| Simon (2005), Chapter 9 | Section 6 and Appendix B | standard definition/background for regularized determinants | only standard terminology; the specialized direct-sum product and convergence proof are reproduced |

## Reverse-outline target

The topic-sentence sequence should read: dyadic support creates three sharp
operator walls; valuation explains exact self-similarity; the same support
also makes cyclic closure explicitly solvable; independent replay checks the
implementation without replacing proof. Any paragraph that does not advance
one of those four statements should be deleted or moved to an appendix.

## Hard release gates

1. [complete] Canonical authority State-A output namespace exists, passed
   its 16/16 integrity audit, and is bound into a read-only writer snapshot;
   this plan makes no State-B or publication-seal claim.
2. [complete] Protected Stage0 replay remains byte-for-byte exact.
3. [complete] `CLAIMS_EVIDENCE.md` and the canonical summary were regenerated
   against hash-verified canonical JSON.
4. [in progress] `PAPER_PLAN.md` received an independent `REVISE` review;
   every critical and major issue is being repaired and must pass the same
   reviewer's recheck before `PLAN_READY`.
5. Only then may the paper-figure and paper-write phases create formal
   manuscript artifacts.
6. Compilation must succeed with zero undefined references/citations, all
   fonts embedded, no forbidden markers, and fresh visual inspection.
7. Two writing-improvement rounds may edit only writer-candidate bytes and
   must preserve round-zero/round-one/final PDFs and raw reviews.
8. No final writer manifest or seal is started during this preflight.
