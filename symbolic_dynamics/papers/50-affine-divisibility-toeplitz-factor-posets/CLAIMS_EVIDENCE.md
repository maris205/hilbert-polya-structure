# Claims--evidence matrix

## Frozen object

Fix an integer `p>=3`.  For nonzero `m`, define

```text
nu_p(m)=max{e>=0:p^e divides m}.
```

For composite `p`, this is only the `p`-divisibility exponent.  Let `u` be a
bi-infinite periodic directive on a finite alphabet `A` with exact support,
least period `h>=2`, and unequal cyclic neighbors.  Set

```text
L_p(k)=(p-1)k+1,
x_{p,u}(k)=u_{nu_p(L_p(k))},
X_{p,u}=closure(orbit(x_{p,u})),
T_{p,u}=(X_{p,u},sigma,x_{p,u}).
```

A morphism is continuous, onto, shift commuting, same-base, and pointed.
These quantifiers must appear before the main results.

## Matrix

| ID | Exact manuscript claim | Deductive evidence | Independent/audit evidence | Source boundary | Status and planned location |
|---|---|---|---|---|---|
| C1 | For `r_N=(p^N-1)/(p-1)`, `Per_{p^N}(x)=Z\(r_N+p^N Z)` for every `N>=1`; every `p^N` is essential; `x` is normal simple Toeplitz and aperiodic. | `p50_toeplitz_stage2/PROOF_PACKAGE.md`, Lemmas 1--2 and Proposition 3; independently reconstructed in `p50_toeplitz_independent_audit/INDEPENDENT_PROOF.md`, Sections 1--2. | Root audit: 984,576 skeleton-position checks. Reciprocal checker: 24,024 independent evaluator comparisons and 1,519 residue checks. | Classical Toeplitz/simple-Toeplitz context is credited; the explicit affine skeleton is proved directly. | Proved; Sections 3--4, Figure 1(a). |
| C2 | If `B_N=x[0,p^N-1]` and finite-block essential period means the least common period of all its positions, then it equals `p^(N+1)` for every `N` iff `p` is prime. For composite `p`, every prime divisor `ell|p` gives the strict common period `ell p^N`. | Stage-2 Proposition 4; reciprocal proof Section 3, including every integer translate and the literal omitted-zero convention. | Root audit: 200,988 prime subperiods rejected and 426,088 composite shifts; reciprocal audit: 19,766 prime witnesses and 80,563 composite progression equalities. | Hosseini--Yassawi own the constructive terminology and cross-base obstruction; this manuscript explicitly states its all-coordinate convention and proves the family-specific split. | Proved; Section 4, Figure 2. |
| C3 | For `c_n=r_n`, every nonzero `j` and `n>nu_p(j)` satisfy `nu_p(L_p(c_n+j))=nu_p(j)`, including composite bases and negative offsets. | Stage-2 Lemma 5; reciprocal proof Section 4. | Root audit: 3,744 checks; reciprocal audit: 7,200 identities and 1,120 high-window normal forms. | Elementary family-specific identity; no unit assumption for composite `p`. | Proved; Section 5, Figure 1(b). |
| C4 | A pointed factor `T_{p,u}->T_{p,v}` exists iff there is a surjective letter map `lambda:A->B` with `v_n=lambda(u_n)` for all `n`; both map and letter quotient are unique, and conjugacy is exactly bijective relabeling. | Stage-2 Theorem 6 and Corollary 7; reciprocal proof Section 5. CHL is the only imported theorem. | Candidate bounded local-rule census: 972 cases, 132 consistent and 132 quotient cases, zero false positives/negatives. Negative controls reject wrong-base and nonpointed mutations. | DKL95 already owns the general same-period, over-zero, aligned-symbol criterion. The residual theorem is the high-center collapse to radius zero in this explicit family. | Proved; Section 5, with an explicit all-radius proof. |
| C5 | Pointed target classes within the frozen family are admissible partitions of `A` whose blocks are independent in the cyclic adjacency graph `G_u`; arrows are exactly refinement and unique. | Stage-2 Theorem 8; reciprocal proof Section 6. | Root audit: 728 directives, 9,874 partition checks, 2,216 admissible partitions. Reciprocal audit: 135 directives, 1,632 partition tests, 871 refinement pairs. | No lattice claim. Counts concern pointed-conjugacy classes, not labeled maps. | Proved; Section 6, Figure 3. |
| C6 | The number of `k`-letter target classes is the graphical Stirling number `S_G(k)`; the minimum target alphabet is `chi(G)`; a binary target exists iff `G` is bipartite; `P_G(q)=sum_k S_G(k)(q)_k`. | Stage-2 graph corollaries; reciprocal proof Section 6. | Candidate: 308 chromatic evaluations. Reciprocal checker: 945 chromatic identities. | These are direct finite-graph consequences of C5; no independent novelty claim is needed. | Proved; Section 6 and the `C_4` worked example. |
| C7 | Two independently implemented evaluators and multiple bounded enumerations reproduce the exact formulas and reject typed mutations. | Frozen candidate evidence, reciprocal `REPRODUCTION.md`, and root audit receipts. | Two candidate reruns are byte-identical; all three manifests/verifiers pass. | Falsification and reproducibility evidence only; never a proof of the unbounded theorems. | Audited evidence; Section 7 and reproducibility appendix. |

## Evidence-to-claim constraints

1. Every theorem statement must cite its exact assumptions locally rather
   than relying on the introduction.
2. Computation may illustrate C1--C6 but may not be used to close an
   infinite quantifier.
3. Source comparison must use “specializes,” “collapses in this family,” or
   other scope language; it may not say “first,” “new,” or make priority
   claims.
4. The Hosseini--Yassawi indexing inconsistency is handled by explicitly
   defining the finite-block convention.  If discussed, the paper records
   only that the conclusion is invariant under the alternative reading.
5. Surjectivity, pointedness, same-base scope, exact directive support,
   cyclic-neighbor distinctness, and least-period reduction are not optional
   prose details; each is a theorem dependency.

## Explicit nonclaims

- no classification of different-base factors;
- no classification of nonpointed maps or maps over nonzero odometer
  elements;
- no statement for arbitrary simple Toeplitz systems;
- no classification of target systems outside the frozen affine family;
- no lattice structure on admissible partitions;
- no absolute novelty, priority, or exhaustive literature claim;
- no empirical claim beyond deterministic proof-diagnostic counts.

