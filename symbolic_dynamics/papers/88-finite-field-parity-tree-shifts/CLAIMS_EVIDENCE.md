# Claims–Evidence Map

| Claim | Proof location | Independent control |
|---|---|---|
| The local rule defines a free-semigroup tree SFT | Definition 2.1 and following paragraph | Every generated block is checked against every local star |
| Terminal restriction is a bijection | Theorem 2.2 | Exhaustive leaf-to-block generation; brute legal-block comparison in three cases; extension-matrix rank |
| Exact block count `q^(d^h)` | Theorem 2.2 | 8,315 enumerated legal blocks, including 256 over `F_4`; constraint rank/nullity certificates |
| Root reconstruction coefficient is the product along each path | Theorem 2.2 | Direct evaluation on every enumerated block; extension-matrix root row |
| Each fixed root has `q^(d^h-1)` blocks | Theorem 2.2 | Nonzero reconstruction row and affine-hyperplane rank |
| Root-refined SNRE collapses to `A_(h+1)=q^(d-1) A_h^d` | Equation (2.7) | Exact block counts at successive heights |
| Boundary-normalized complexity is `log q` | Theorem 3.1 | Substitution of exact block count |
| Site-normalized complexity tends to `(d-1) log(q)/d` | Theorem 3.1 | Exact finite-height volume formula |
| Double-log rate is `log d` | Theorem 3.1 | Exact finite-height double-log formula |
| Uniform finite-block laws are compatible | Proposition 4.1 | Exhaustive restriction tables with constant fibers; restriction-map rank |
| The projective law is invariant under every subtree shift | Proposition 4.1 | Uniform terminal-coordinate argument at arbitrary rooted subtrees |
| The law has the displayed joint-offspring block-Markov factorization | Equation (4.4), for `h >= 1`, with the root-only `h=0` case stated separately | Product exponent equals exact cylinder mass |
| Every proper sibling subset is iid uniform conditional on the parent | Lemma 4.2 | Exact affine-hyperplane fiber count |
| Every deterministic ray is iid uniform | Theorem 4.3 | Exhaustive distribution of every tested ray; independent observation-rank controls |
| The complete level reconstructs the root | Theorem 5.1 | Exact reconstruction on all enumerated blocks |
| Every proper level subset is independent of the root | Theorem 5.1 | 811 complete joint-table enumerations, including all 15 proper subsets in the `F_4` case; 567 observation-rank certificates |
| Proper/full mutual information is exactly `0`/`log q` | Theorem 5.1 | Joint-table uniformity plus deterministic full reconstruction |
| `d >= 2` and all `c_j != 0` are needed for the combined package | Remark 5.2 | Explicit `d=1` ray-degeneracy and zero-coefficient deletion-leak controls |
| Results hold for every prime power | All algebraic proofs | Proof uses only finite-field linear algebra; one exhaustive `F_4` lane checks a non-prime field without extrapolating universal scope |

The program is a regression control, not a replacement for the proofs.  In
particular, a single implemented extension field and finite rank sampling at
larger boundary sizes do not prove the all-parameter statements.
