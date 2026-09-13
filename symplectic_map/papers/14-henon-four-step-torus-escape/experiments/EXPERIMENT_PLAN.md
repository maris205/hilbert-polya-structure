# Experiment Plan

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Execution class

This project is **proof-only**. It authorizes no scientific execution.

The directory name is retained for repository consistency, but the proposed
theorem has no empirical component. No program, computer algebra calculation,
parameter table, numerical approximation, prime search, modulus search, or
data-generation task is part of the evidence.

## Explicit prohibitions

Do not perform:

- numerical experiments;
- symbolic or computer-algebra verification;
- parameter scans over \(a,b,c,d\);
- searches over primes;
- reductions modulo primes or composite moduli;
- finite-field tests;
- orbit enumeration;
- periodic-point searches;
- random sampling;
- benchmark construction;
- code generation;
- result-file creation;
- figure or table generation from computed data;
- use of a computation as evidence for any word-transition identity.

No scientific execution is authorized even if described as a sanity check.

## Proof-review protocol

The only admissible next activity is a read-only independent review of the
source documents. The reviewer should complete the following documentary
checks by hand.

### P1. Statement and quantifiers

Verify:

- \(\operatorname{char}K=0\);
- \(d\ge2\);
- \(abc\ne0\);
- \(\Gamma\le K^\ast\) has finite rank \(r\);
- no coefficient-membership assumption appears;
- \(T_m\) uses every \(0\le j\le m\);
- the main set is \(T_4\), not a periodic-point set.

Acceptance condition: the theorem in every source document is equivalent to

\[
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

### P2. ESS applicability

Independently check the primary source and verify that

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}=1
\]

is an equation with variables in a rank-\(3r\) subgroup and arbitrary fixed
nonzero coefficients.

Acceptance condition: no enlargement of \(\Gamma\) and no hidden membership
of \(a,b,c,-1\) is used.

Mandatory regression check: reject the statement “\(b\) must lie in
\(\Gamma\), or the group must be enlarged to contain \(b\).” The statement
is false for this proof because \(b\) occurs only in the fixed ESS
coefficient \(-b/c\).

### P3. Nondegenerate-state count

Verify that an ESS triple fixes \(x_{i+1}\), \(x_i^d\), and \(x_{i-1}\), and
that at most \(d\) values of \(x_i\) remain. Verify the inverse

\[
H^{-1}(X,Y)=
\left(Y,\frac{X-bY^d-c}{a}\right)
\]

and the four-index union bound.

Acceptance condition:

\[
\#\{\text{nondegenerate part}\}\le4dE(3,3r).
\]

### P4. Degeneracy labels and nine transitions

Re-derive the \(A,B,C\) labels from the three fixed-coefficient summands.
Then re-derive all nine adjacent transitions without consulting a computed
table.

Acceptance conditions:

- only \(BA\) and \(CB\) can be free;
- all other adjacent words have at most \(d^2\) initial states;
- the index direction agrees with
  \(H(x_i,x_{i-1})=(x_{i+1},x_i)\).

### P5. Free-chain closure

Verify:

- \(BAA,BAB,BAC\);
- \(CBB,CBC,CBA\);
- the exceptional conditions \(a=-1\) and \(bc^{d-1}=-1\);
- \(CBAA,CBAB,CBAC\).

Acceptance condition: each four-letter word has at most \(d^2\) initial
states.

### P6. Overlap and short periods

Check simultaneous degeneracy, the three pairwise intersections, the
impossibility of triple degeneracy in characteristic zero, and the use of a
union bound. Check periods \(1,2,3,4\) without assuming distinct states.

Acceptance condition: no omitted state and no additional short-period term.

### P7. Sharpness construction

For each symbolic \(d\ge2\), verify by direct algebra, not by execution, that

\[
b=1,\quad a=-1,\quad c^{d-1}=-1,\quad
\Gamma=\langle2,c,-1\rangle,\quad P_t=(t,t^d)
\]

gives infinitely many points of \(T_3\) and that
\(\operatorname{rank}\Gamma=1\).

Acceptance condition: the example proves only \(T_3\) survival, not
periodicity or a classification of all exceptions.

### P8. Periodic corollary

Verify that \(C_n^\Gamma(H)\) counts exact-period orbits entirely contained
in \(\Gamma^2\), so every orbit contributes \(n\) points to \(T_4\).

Acceptance condition:

\[
\sum_{n\ge1}nC_n^\Gamma(H)\le\#T_4(H,\Gamma).
\]

### P9. Citation and collision review

Open every primary link in CITATION_VERIFICATION.md. Confirm exact version,
scope, and whether it is theorem input or boundary evidence. Repeat targeted
searches for:

- Hénon maps and finite-rank multiplicative groups;
- Hénon \(S\)-unit periodic points;
- finite-window torus survival;
- higher-dimensional orbit multiplicative dependence;
- cyclotomic Hénon periodic points.

Acceptance condition: any newly found direct collision triggers a source
repair before further lifecycle progression.

### P10. Nonclaim and reserve audit

Verify that no document asserts:

- rational/integral periodic-point uniformity;
- one-representative orbit control;
- optimal constants;
- general polynomial Hénon coverage;
- \(d=1\) or positive characteristic;
- a complete \(T_2/T_3\) classification;
- scientific execution;
- any theorem from the quartic Paper 15 reserve.

## Gate

The package may leave the present lifecycle only after an independent
reviewer has completed P1--P10 and issued a separate review artifact under
new authorization. This plan does not authorize creation of that artifact.

## Expected outputs

None at the current stage:

- no code;
- no data;
- no results;
- no figures;
- no manuscript;
- no source lock;
- no review file.
