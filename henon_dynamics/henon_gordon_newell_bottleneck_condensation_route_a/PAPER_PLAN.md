# Paper plan — HCS-C285

**Working title:** Canonical Flow and Bottleneck Condensation in Finite
Gordon–Newell Networks

**One-sentence contribution:** A self-contained theorem derives finite
canonical equilibrium, all occupancy derivatives, service flows, exact
nonreversible time reversal, and the full unique/tied bottleneck limit from
one complete-homogeneous partition function, with every small and singular
face stated explicitly.

**Type:** exact probability/queueing theory paper with executable regression
certificate. The 28-file source-local release format overrides conference
template and external-figure defaults.

## Claims–evidence matrix

| Claim | Mathematical evidence | Executable evidence | Section |
|---|---|---|---|
| canonical product law for arbitrary irreducible `P` | global-balance proof | generator left nullspaces | §2 |
| complete moment and flow calculus | derivative/decrement identities | 165 factorial cells and 9 flow ledgers | §2–3 |
| exact time reversal and reversibility iff gate | stationary rate-ratio proof | `P*`, involution and current cells | §3 |
| unique/tied condensation | positive coefficient convolution and simplex moments | 28 finite asymptotic cells | §4 |
| zero/equal/small-`N` closure | explicit boundary proofs | 12 boundary cells | §5 |
| strict Route-A failure | evaluator criteria | YAML/checker/manifest | §6 |

## Manuscript structure and revision staging

### Round 0

1. Abstract: finite product form, moments, flows, reversal.
2. Frozen model and classical ownership.
3. Canonical law and derivative calculus with proof.
4. Throughput and exact time reversal with proof.
5. Compact ownership bibliography.

### Round 1 substantive addition

5. Complete unique/tied bottleneck theorem.
6. Positive-coefficient asymptotic proof, total-variation nonbottleneck limit,
   and conditional uniform-composition/Dirichlet proof.

### Round 2 substantive addition

7. Full zero, equal-weight, self-route, gauge, and singular boundary atlas.
8. Executable evidence/proof separation and hostile audit.
9. Registry collision distinctions and strict Route-A tuple/nonclaims.

## Table/figure plan

The paper needs no external plot: the theorem is exact and the frozen package
may contain only 28 files. The most informative visual object is an in-text
two-column boundary table comparing admissible finite faces with excluded
singular faces. Its caption-equivalent lead sentence states what is compared
and prevents a skim reader from confusing zero routing entries with zero
service rates. A second compact in-text display contrasts unique and tied
bottleneck limits. Both are generated directly by LaTeX in `main.tex`, so no
untracked raster or vector artifact is introduced.

## Citation plan

- Introduction/model: Gordon & Newell (1967), verified INFORMS DOI metadata.
- Reversal: Kelly (1979; Cambridge reissue 2011), verified author/Cambridge
  edition metadata.
- Modern context: Kelly & Yudovina (2014), verified Cambridge book DOI and
  ISBN metadata.

Every source is cited for ownership or standard context. The paper explicitly
disclaims literature originality.

## Reverse-outline check

The topic sentences progress from one canonical partition function, to its
finite probabilistic consequences, to its time arrow, to its maximal-weight
limit, then to boundaries and Route-A nonclaims. No section launches an
independent spectral or arithmetic story.
