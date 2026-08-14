# Paper plan — Paper 31 / SD-C33

## Configuration

- **Title:** *Wilson Semiring Verifiers in Symbolic Dynamics: Matched-Clone,
  Pruning, and Clock-Dilution Obstructions*
- **Type:** theorem-led negative/diagnostic paper
- **Field:** symbolic dynamics, operator theory, arithmetic dynamics
- **Target:** field-general research article; no venue-fit claim
- **Citation style:** author-year `plainnat`
- **Output:** modular LaTeX, pure TikZ figures, PDF
- **Review policy:** no manuscript review loop, by explicit user instruction
- **Length target:** approximately 8,000--9,500 words including appendices

## One-sentence contribution

Finite-full-shift alphabet sum genuinely escapes Paper 30's bare
multiplicative-UFD clone, but the resulting Wilson verifier is exactly copied
by a matched semiring clone and yields only a pruning-equivalent transient
determinant or a noncompact recurrent operator under the entropy clock.

## Claims/evidence matrix

| Claim | Evidence | Status | Main section |
|---|---|---|---|
| alphabet sum/product reconstructs \(\mathbb N_0\) | additive-generation theorem plus entropy separation | proved | §3 |
| ordinary polynomial addition breaks the Paper 30 monomial clone | \(\Phi(1+1)=x_2\neq2\) | proved | §3 |
| a matched semiring clone copies all source-natural data | transport induction | proved | §3 |
| the stationary Wilson graph has one primitive cycle per prime | direct proof of Wilson's theorem and deterministic graph census | proved | §4 |
| temporal repetitions give exact prime-power weights | total roof \(r\log p\) | proved | §4 |
| the raw marked product is \(\prod_p(1-z^{p-1}p^{-s})\) | finite periodic diagonal sums and trace-log rearrangement | proved as a formal periodic identity | §5 |
| the primary recurrent adjacency is noncompact for every nonnegative exact-clock allocation | minimum-roof edge and orthogonal-block sequence | proved | §6 |
| uniform allocation has unit-circle essential approximate spectrum | explicit cyclic-block eigenvalues | proved | §6 |
| first return gives an honest determinant but changes time | diagonal trace norm and marker comparison | proved | §6 |
| transient verification prunes to accept loops | acyclic power traces and block-triangular determinant | proved in the declared trace-class model | §7 |
| terminal compilation proves too much | five nonprime computable support families and the general total-decider compiler | theorem plus exact controls | §7--8 |
| Route A fails and the terminal semiring branch closes | ownership table and strict gate evaluation | proved/scoped | §9 |

## Section architecture

### §0 Abstract (190--230 words)

- Lead with the exact post-Paper-30 problem.
- State bare-clone separation and matched-clone failure in the first half.
- Give the Wilson factor \(1-z^{p-1}p^{-s}\).
- State whole-operator noncompactness and the first-return marker change.
- End with the negative branch decision, not a generic promise.

### §1 Introduction (850--1,050 words)

- Motivate the nonmultiplicative escape left open by Paper 30.
- Explain why alphabet sum is source-natural and why Wilson is the smallest
  exact congruence witness.
- Preview the strongest result: genuine bare-clone separation still collapses
  under matched transport, pruning, or clock dilution.
- Give four falsifiable contribution bullets.
- Place Figure 1 after the contribution list.

### §2 Source and literature boundary (750--950 words)

- Define finite full shifts and distinguish alphabet-sum from categorical
  coproduct.
- Position the work relative to symbolic zeta functions, computation in
  dynamics, semirings of dynamical systems, and countable-state thermodynamic
  formalism.
- Name Papers 19 and 20 as the closest internal collisions.
- State the bounded novelty claim and functional-ownership convention.

### §3 Bare-clone separation and matched-clone collapse (900--1,100 words)

- Prove additive reconstruction.
- Give the \(1+1\) contradiction for the old clone.
- Define the matched semiring clone and prove exact transport.
- Use Figure 1 to make the two clone questions visually distinct.

### §4 Stationary Wilson grammar (850--1,050 words)

- Define quotient/remainder and the residue-state graph.
- Prove the exact prime-cycle theorem, including \(n=4\) and square composites.
- Separate primitive prime cycles from temporal prime-power repetitions.
- State explicitly that terminal closure is selector-equivalent.

### §5 Marked periodic ledger (750--950 words)

- Compute the finite periodic diagonal sum.
- Derive the factor \(1-z^{p-1}p^{-s}\).
- Prove normal convergence for \(|z|<1\).
- State the Euler specialization and deny Fredholm ownership.
- Use Figure 2 to expose graph time versus entropy time.

### §6 Clock dilution and first return (950--1,150 words)

- Prove noncompactness for arbitrary nonnegative allocations.
- State the inherited exact disjoint-cycle criterion and the
  \(o(\log p)\) successor obligation.
- Prove the uniform essential approximate spectrum statement.
- Derive the trace-class first-return diagonal and marker mismatch.

### §7 Transient pruning and universal controls (750--950 words)

- Define a trace-class regulated DAG compiler.
- Avoid the false claim that the countable DAG direct sum is globally
  nilpotent; use acyclicity and zero power traces.
- Prove determinant pruning.
- Compile squares, powers of two, Fibonacci numbers, seeded support, and
  arbitrary total deciders.
- Use Figure 3 to compare the three ownership outcomes.

### §8 Exact audit (650--850 words)

- Report the final frozen cutoff-4096 research numbers, then synchronize with
  integrator-owned canonical results if they differ.
- Include composite, pseudoprime, bare/matched clone, arbitrary semiring,
  random table, marker, dilution, and universal-wrapper controls.
- Keep theorem proof independent of finite computation.

### §9 Route closure (550--750 words)

- Print the strict Route-A tuple.
- Explain A0 and A1 as scoped passes and A2--A4 as failures.
- State `ROUTE_A_REJECTED`, Route B locked, and
  `CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH`.
- List unsupported claims that remain forbidden.

### §10 Conclusion (250--350 words)

- Restate the narrow success and decisive failure without copying the
  Introduction.
- Give the Paper 32 obligation in one concrete sentence.

### Appendix A — detailed proofs

- Full proofs and operator lemmas not kept in the main text.
- Explicit normal-convergence and essential-spectrum details.
- Trace-class transient block factorization.

### Appendix B — scope and declarations

- Allowed/forbidden information table.
- Object-ownership table.
- Limitations.
- Data/code availability, ethics, CRediT, conflicts, funding, and AI-use
  statements.

## Figure plan

| ID | Type | Description | Data source | Priority |
|---|---|---|---|---|
| Figure 1 | pure TikZ theorem map | bare UFD clone breaks at addition, while matched semiring transport copies the whole Wilson construction | theorem/manual | high |
| Figure 2 | pure TikZ cycle/clock diagram | Wilson cycle of length \(p-1\), total roof \(\log p\), raw factor, first-return contraction, and changed marker | theorem/manual | high |
| Figure 3 | pure TikZ ownership trichotomy | matched clone, transient pruning, and recurrent clock dilution with exact GO/STOP consequences | theorem/manual | high |

**Hero Figure 1 caption plan.**  Compare the same finite-full-shift source
against two controls.  The upper lane shows the contradiction
\(x_2\neq1+1\) for ordinary polynomial addition.  The lower lane shows an
isomorphism to the transported semiring clone and equality of Wilson paths,
cycles, roofs, and ledgers.  A skim reader should see that “addition escapes
Paper 30” and “addition gives a clone-proof arithmetic selector” are different
claims.

All figures are native vector TikZ.  No raster data, target zero, prime table,
or empirical effect-size chart appears.

## Citation plan

- **§1:** Bowen--Lanford; Hartmanis--Shank; Naquin--Gadouleau; Paper 30 as
  internal motivation.
- **§2:** Salo--Törmä; Kopra; Shepherdson--Sturgis; Kůrka;
  Gurevich--Savchenko; Sarig; Parry--Sullivan; Simon; recent semiring and
  state-complexity boundary sources.
- **§3:** Salo--Törmä and Naquin--Gadouleau for context; the actual algebraic
  statements are proved in the paper.
- **§4:** Hartmanis--Shank and Kůrka for computation/recognition context;
  Wilson classification is proved directly.
- **§5--7:** Bowen--Lanford, Parry--Sullivan, Gurevich--Savchenko, Sarig, Hong,
  and Simon for the classical analytic boundary.
- **§8--10:** own exact results and internal Paper 19/20 theorem lineage; no
  new external claim requires a citation.

Every cited external source has verified primary metadata.  The bibliography
contains only keys actually cited in the LaTeX source.

## Review status

No GPT or human-simulated manuscript review is scheduled.  This is an explicit
user override.  Objective formula, source, citation-key, compilation, font,
page, vector-figure, and PDF visual audits remain mandatory.

## Next steps

- [x] freeze source and preregistration
- [x] write proof and derivation packages
- [x] write literature and narrative packages
- [x] create pure TikZ figures
- [x] draft modular LaTeX
- [x] synchronize canonical final experiment numbers
- [x] compile and audit `main.pdf`
