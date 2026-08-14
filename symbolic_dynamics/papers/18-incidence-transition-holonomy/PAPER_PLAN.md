# PAPER PLAN — SD-C20

## Title

*Transition Holonomy on the Tensor-Subset Shift: Noncommutative Artin Blocks
and an Arithmetic Selectivity No-Go*

## Central thesis

Transition-dependent finite-group cocycles escape the cyclic one-letter
classification and produce genuine noncommutative same-object Artin blocks,
but the cleanest intrinsic \(S_3\) example exposes rather than removes mixed
tensor-subset primitives.

## Claim--evidence matrix

| ID | claim | status | decisive evidence |
|---|---|---|---|
| C1 | natural local transition data depend only on \((u,v,w)\) | theorem | relabeling orbit classification |
| C2 | the natural counting gauge orbit has an explicit form | theorem | block-diagonal gauge conjugacy |
| C3 | the frozen \(S_3\) cocycle is not one-letter plus coboundary | theorem | singleton loop plus \([p,pq]\) holonomy |
| C4 | regular-representation Artin factorization is same-object | theorem/classical | right regular decomposition |
| C5 | the two-atom blocks have the stated exact formulas | exact computation | symbolic determinant |
| C6 | mixed terms leak at degrees 3 and 4 | exact computation | trace-log expansion |
| C7 | the commutator is cancellation-proof in an edge-marked ledger | theorem | unique connected traversal of four distinct directed edges |
| C8 | all-irrep-clean tables found in three groups are gauge/count | finite evidence only | exhaustive \(S_3,D_4,Q_8\) enumeration |
| C9 | nontrivial infinite blocks are trace class for \(\Re s>2\) | theorem | nuclear decomposition and Euler-product bound |
| C10 | the candidate satisfies Route A | refuted | A3/A4 failure and mixed-prime leakage |

## Section architecture

1. **Introduction.** State the loophole inherited from the parity fiber and
   give the construction/no-go result up front.
2. **Classical boundary.** Separate standard twisted-zeta, cohomology, and
   switching machinery from the model-specific calculation.
3. **Frozen system.** Define the tensor-subset full shift, two-block edge
   presentation, right cocycle, weights, twisted matrices, and function
   space.
4. **Incidence grammar and gauge.** Classify natural local data, count types,
   and derive the natural counting-gauge orbit.
5. **Primitive holonomy and leakage.** Fix primitive/repetition conventions
   and prove the marked-cycle separation statement.
6. **The \(S_3\) certificate.** Prove genuine nonabelianity; compute the
   trivial, sign, and standard determinants and the exact leak.
7. **Finite evidence and controls.** Report exhaustive tables with an
   evidence firewall and run formal/composite/shuffle/random controls.
8. **Fredholm boundary.** Give the symmetric operator, trace-norm estimate,
   cutoff convergence, and the \(\Re s>2\) limitation.
9. **Route evaluation and limitations.** Apply the strict Route-A tuple and
   keep Route B locked.
10. **Conclusion.** Move the next search toward a different symbolic
    language rather than a richer fiber.
11. **Appendices.** Collect full proofs and a scope/anti-claim ledger.

## Figure plan

One vector figure summarizes the logical fork:

```text
same tensor-subset edge shift
        |
 incidence cocycle in S3
   /          |          \
1D blocks   commutator   standard block
clean        genuine     mixed leakage
   \          |          /
       same inventory reproduced
                 |
        Route-A selectivity fails
```

The figure must label the exact determinant and the first coefficients; it
must not imply a critical-zero result.

## Citation plan

- shift determinants: Bowen--Lanford;
- cocycle periodic data: Livšic, Parry--Pollicott, Kalinin;
- twisted factors and finite extensions: Adachi--Sunada, Pollicott,
  Boyle--Schmieding;
- switching/voltage presentation: Gross--Tucker, Zaslavsky;
- graph Artin factors and non-uniqueness warning: Stark--Terras and recent
  gain/voltage cospectral literature;
- trace-class determinant: Simon.

## Writing controls

- Use “we prove” only for statements in `PROOF_PACKAGE.md`.
- Use “the enumeration found” for the finite tables.
- Never identify an unmarked monomial coefficient with one primitive orbit.
- Keep the group generator \(t=(23)\) distinct from the spectral variable
  \(s\).
- State the skew-product side and the commuting deck-action side explicitly.
- State that the two-block presentation is the same shift.
- Put every cross-family idea only in `ROUND2_CLUES.md`.
