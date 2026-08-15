# Independent Source-Lock Review

## Verdict

**REPAIR_REQUIRED**

`SOURCE_LOCK_PASS` is not issued.  The package is hash-consistent and its
main formulas are correct, but one explicit algebraic characterization is
false.  The defect is local and repairable; it changes neither the four
scalar formulas, the counterexample, nor the low-novelty conclusion.

This review binds the rejected frozen lock

`6df72fae8e80a7bad689e492b71ad216a4fefa7bc107b82f8027832f56b1b334`.

Any source repair changes at least one design-document digest and therefore
requires a regenerated source lock and a fresh independent review.  This
review does not authorize code, a registered execution, a result, or a
manuscript.

## Independence and review boundary

The mathematical and novelty attack was performed blind, before the authored
Paper-11 package was opened.  The authored files were inspected only after
the final lock and its expected SHA-256 were supplied.  The present review
used read-only parsing, hashing, upstream-status inspection, and direct
mathematical checks.  It did not create or inspect Paper-11 code, run a
Paper-11 experiment, alter an upstream paper, add a modulus, or draft a
manuscript.  This review file is the sole new artifact.

Before this file was added, the Paper-11 tree contained exactly the six
bound design documents, `experiments/source_lock.json`, and the one citation
sidecar.  It contained no code, result, registered-run, figure, or manuscript
artifact.

## Reproduced local bindings

All seven bound local/sidecar digests and the lock digest reproduce exactly.

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `notes/RESEARCH_QUESTION.md` | `86262824c80ae6b89943282312b0ce5ee04bed3eb9a2a4cb297e30f8dd0be8ec` | exact |
| `notes/NOVELTY_ASSESSMENT.md` | `9ef3260014f861f5d77a5a5c52070bbed4c82d7061ab52fb99e38848ebc0426b` | exact |
| `notes/PROOF_PACKAGE.md` | `5fc2bfa664e43770b8945292e3b856b57143de8eada398cc95a963450de03790` | exact |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `8c2bfb3061d348154af2e99de9520206157e2a83515188494526851782c50a2c` | exact |
| `experiments/EXPERIMENT_PLAN.md` | `ccf8335474c1ea43a978e81a73c9611b7e6762170cda9aa84a3550c0fbdd551a` | exact |
| `experiments/EXPERIMENT_TRACKER.md` | `63f63b5f80d7dcbf4fc2aa2b712438fe9b584ac9584d360b8aba26a7a621516a` | exact |
| `notes/CITATION_VERIFICATION.md` | `56b55be90e9916cede8d7757b86af90d3d2355e7566ede59c6daf51f6fb41b43` | exact |
| `experiments/source_lock.json` | `6df72fae8e80a7bad689e492b71ad216a4fefa7bc107b82f8027832f56b1b334` | exact |

The Paper-11 lock is strict JSON.  A duplicate-key-rejecting parse found no
duplicate object key.  The bound Paper-9 and Paper-10 JSON locks, the bound
Paper-10 raw result and result manifest, and the bound Paper-10 terminal
pipeline state likewise strict-parse without duplicate keys.

## Reproduced upstream bindings

### Paper 9

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `experiments/source_lock.json` | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` | exact |
| `paper/FINAL_INTEGRITY.md` | `7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712` | exact |
| `paper/paper_final.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` | exact |

The bound final-integrity record states
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`.

### Paper 10

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | exact |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` | exact |
| `results/EXPERIMENT_RESULTS.json` | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` | exact |
| `results/result_manifest.json` | `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658` | exact |
| `results/INDEPENDENT_RESULT_INTEGRITY.md` | `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58` | exact |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e` | exact |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a` | exact |
| `paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | exact |
| `paper/reviews/round2_review.md` | `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae` | exact |
| `paper/FINAL_INTEGRITY.md` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` | exact |
| `paper/PIPELINE_STATE.json` | `dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c` | exact |

The Paper-10 independent result review states `RESULT_PASS`; its terminal
pipeline and final-integrity record state
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`.  Its exact nine-row table confirms the
inherited theorem and ledger: $G_q=R_q[A]^\times$ is the full finite
abelian centralizer, $\mathrm{CV}_q$ is its free transitive torsor,
translation by $A$ has order $r_q$, and the full quotient is one fixed
point.

## Mathematical gates that pass

### General finite abelian \(C\)-set formulas

For

\[
X=\coprod_{K\le C}n_K(C/K),\qquad H=\langle a\rangle,
\]

the locked quantities

\[
d_K=[H:H\cap K],\qquad M_K=[C:HK]
\]

are exact.  Translation by \(a\) has point period \(d_K\) on \(C/K\), and
\([C:K]/d_K=[C:HK]\) cycles.  Consequently the signs and exponents in

\[
\zeta_{X,\phi_a}(t)
=\prod_K(1-t^{d_K})^{-n_K[C:HK]},\qquad
\zeta_{X/C}(t)=(1-t)^{-\sum_Kn_K}
\]

follow the Artin--Mazur inverse convention.

The exact-period classes are also correct:

\[
P_m^C=\sum_{d_K=m}n_K[C/K],
\quad
\widetilde P_1^C=[X],
\quad
\widetilde P_m^C=0\ (m>1).
\]

Thus the point-order and orbit-order products are respectively

\[
\prod_m(1-t^m)^{-P_m^C/m}
\quad\hbox{and}\quad
(1-t)^{-[X]}.
\]

The first depends on \(a\) only through \(H=\langle a\rangle\); the second
has only orbit period one.

### Separation of the three zeta constructions

The package correctly keeps separate:

1. the 2008 fixed-point/point-order rational Burnside zeta;
2. the 2015 fixed-\(G\)-orbit/orbit-order integral Burnside zeta; and
3. the 2013 \(G\)-permutation invariant represented by a
   \((\mathbb Z\times G)\)-set and determined by all twisted Lefschetz
   classes.

No formula silently identifies these constructions.  The direct prior-art
collisions are accurately scoped, and the 2018 enhanced carrier is kept
separate as well.

### Exponent reduction, marks, and signs

The exact-period reduction rule

\[
\psi_*\!\left(\prod_m(1-t^m)^{-s_m/m}\right)
=\prod_m(1-t^m)^{-\psi(s_m)/m}
\]

is safe for additive \(\psi\).  The package explicitly forbids naive
coefficientwise application of a mark, cardinality, or orbifold map to a
Burnside power series and does not assert preservation of the Burnside
pre-\(\lambda\) or power structure.  On exact classes, the mark of the
regular orbit is \(n_q\) at the trivial subgroup and zero at every
nontrivial subgroup.  The four locked regular-torsor reductions are correct:

\[
(1-t^{r_q})^{-m_q},\quad
(1-t^{r_q})^{-1/r_q},\quad
(1-t)^{-n_q},\quad
(1-t)^{-1}.
\]

### Inverse convention and action-kernel recovery

With the locked left action

\[
(j,c)\cdot xK=ca^jxK,
\]

the stabilizer is exactly

\[
\widehat K_a
=\langle\{0\}\times K,(1,a^{-1})\rangle.
\]

It records \(a^{-1}K\).  Across the represented orbit types it recovers
exactly \(a\) modulo

\[
N=\bigcap_{n_K>0}K,
\]

the action kernel; exact labelled recovery is equivalent to effectivity.
For the regular Paper-10 torsor the 2013 triple is therefore
\((1,1,a_q^{-1})\), whereas the enhanced return twist is \(a_q\).  The signs
are consistent throughout the six design documents and the lock.

### Stack and inertia statements presently made

The existing assertions

\[
[X/C]\simeq\coprod_Kn_KBK
\]

and \(I(BK)\simeq\coprod_{k\in K}BK\) for abelian \(K\) are correct.
Translation by central \(a\) is \(2\)-isomorphic to identity, so these
inertia components have static period-one dynamics.  In the regular torsor,
all point stabilizers are trivial, the action groupoid is equivalent to a
point, all nonidentity fixed sectors are empty, and the natural
transformation from identity to \(F_a\) has components labelled \(a\).

These facts support only Morita- and \(2\)-isomorphism-invariant conclusions;
the package correctly excludes presentation-sensitive carriers from that
statement.

### \(C_6\) counterexample

For \(C=C_6\), generator \(a\), and
\(X=C_6/C_2\sqcup C_6/C_3\), the action kernel is
\(C_2\cap C_3=1\), while the point periods are \(3\) and \(2\).  The locked
data are exact:

\[
\zeta_X=(1-t^3)^{-1}(1-t^2)^{-1},\qquad
\zeta_{X/C}=(1-t)^{-2},
\]

\[
\Phi_*(\zeta_{\rm pt})
=(1-t^3)^{-2/3}(1-t^2)^{-3/2},\qquad
\Phi_*(\widetilde\zeta_{\rm orbset})=(1-t)^{-5}.
\]

The stack is \(BC_2\sqcup BC_3\) with five static inertia sectors.  Hence
effectivity and an order-six translating element do not force a period-six
factor.

### Paper-10 specialization and frozen controls

Specializing \(K=1\), \(X_q\simeq G_q\), and \(a_q=A\bmod q\) gives
\(d_1=r_q\), \([G_q:H]=m_q\), and every locked torsor formula.  The ordered
modulus tuple is exactly

\[
(2,3,5,7,11,4,6,9,10),
\]

with no tenth modulus.  The rows

\[
(n_q,r_q,m_q)=
(3,3,1),(8,4,2),(20,10,2),(48,8,6),(100,5,20),
(12,3,4),(24,12,2),(72,12,6),(60,30,2)
\]

reproduce Paper 10.  The collisions \(r_2=r_4=3\) and
\(r_6=r_9=12\), together with the four composite controls, prove that the
retained period is not an intrinsic modulus or prime label.  The abstract
\(C_6\) control is correctly isolated from the modulus namespace.

### Novelty and nonclaims

The score \(2/10\) is appropriately conservative.  The 2008, 2013, 2015,
and 2018 papers directly predate every constituent carrier; Zegowitz
predates the shortening/gluing language.  Miles and Walton are correctly
used as scope boundaries, while the 2024--2026 records are context rather
than evidence of priority.  The package makes no absence or priority claim,
does not claim a new zeta or stack theorem, and does not universalize its
negative conclusion to unexamined analytic, weighted,
representation-valued, or transfer constructions.

## Blocking correction 1: Φ is not a Burnside-ring homomorphism

`notes/RESEARCH_QUESTION.md` calls

\[
\Phi_q:B(G_q)\longrightarrow\mathbb Z,
\qquad \Phi_q([G_q/H])=|H|
\]

an "orbifold ring homomorphism."  This is false for the ordinary Burnside
ring product, even for a nontrivial finite abelian group.

Let \(\mathbf u=[G/1]\).  Diagonal multiplication gives

\[
\mathbf u^2=|G|\mathbf u
\]

because \(G\times G\) is the disjoint union of \(|G|\) regular diagonal
orbits.  Yet

\[
\Phi_G(\mathbf u)=1,
\quad
\Phi_G(\mathbf u^2)=|G|,
\quad
\Phi_G(\mathbf u)^2=1.
\]

Thus \(\Phi_G\) is the additive orbifold homomorphism used on Lefschetz or
exact-period classes, not a ring homomorphism under Cartesian
multiplication.  This is exactly why the package's exponent-reduction guard
is necessary.

Required correction: replace "orbifold ring homomorphism" by "additive
orbifold homomorphism" (or "homomorphism of abelian groups") and state that
no multiplicativity is asserted.  Keep the exponentwise definition and all
four scalar formulas unchanged.  Audit the regenerated package for any new
claim that \(\Phi\) preserves Burnside multiplication or a power structure.

## Nonblocking scope note: rigidification and residual \(C/H\)

The existing quotient-stack and inertia formulas are correct, but the
package does not claim or use an inertia-rigidification construction.
Accordingly, the absence of a rigidification theorem is not a second repair
gate.  For any later discussion, however, the roles of
\(H=\langle a\rangle\), a point stabilizer \(K\), and a residual group must
not be conflated.

The safe boundary is:

- On the orbit \(C/K\), the stack component is \(BK\).  A subgroup can be
  rigidified from that component only when it lies in the inertia group
  \(K\); for \(J\le K\) in this abelian setting, rigidifying \(BK\) by \(J\)
  gives \(B(K/J)\).
- The dynamical subgroup \(H=\langle a\rangle\) is not generally a point
  stabilizer.  It may be rigidified from \(BK\) only in the special case
  \(H\le K\), equivalently when translation by \(a\) is already trivial on
  \(C/K\).  Even then the residual stabilizer is \(K/H\), not \(C/H\) in
  general.
- For the regular Paper-10 torsor \(K=1\), the \(C\)-action is free, so there
  is no nontrivial inertia subgroup and no nontrivial rigidification of
  \([X/C]\simeq *\).  In particular \(H=\langle a\rangle\) must not be called
  a stabilizer of the regular \(C\)-action.
- Quotienting the regular set by the free action of \(H\) first is a
  different intermediate construction: \(X/H\) is an ordinary set of
  \([C:H]\) points with a regular residual \(C/H\)-action, and translation by
  \(a\) is identity on it.  It is not an inertia sector or a rigidification
  of \([X/C]\), and it supplies no intrinsic modulus/prime clock.

This boundary may be added as a short nonclaim paragraph, but it is not
required to repair the presently frozen claims and need not expand the
registered audit.

## Required re-review

After correcting the characterization of \(\Phi\):

1. recompute the modified local-document hashes;
2. regenerate `experiments/source_lock.json` with those hashes and a new
   final lock digest;
3. preserve the exact upstream bindings, nine-modulus tuple, formulas,
   novelty score, and no-code/no-run/no-manuscript state; and
4. request a fresh final-hash-bound independent source review.

Until then the exact disposition is:

`REPAIR_REQUIRED`
