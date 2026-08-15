# Independent Source-Lock Review R2

## Verdict

**SOURCE_LOCK_PASS**

This bounded rereview binds:

- Paper-11 source-lock v2 SHA-256:
  331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b.
- Immutable Round-1 REPAIR_REQUIRED review SHA-256:
  233da2cb9707f340e7dec588437f694133af63f30bc17c0547dd2a9032a1c17a.

The sole Round-1 blocker is repaired. All local, citation, upstream,
mathematical, ledger, novelty, and inventory gates pass. This source pass
authorizes only the next separately reviewed implementation stage. It does
not authorize a registered execution, result, or manuscript.

## Review boundary and inventory

The rereview used read-only parsing, hashing, terminal-status inspection,
wording scans, and direct mathematical regression. It did not edit a lock or
design document, create or inspect Paper-11 code, run a Paper-11 experiment,
alter an upstream artifact, add a modulus, or draft a manuscript. This R2
review is the sole new artifact.

Before this file was added, the Paper-11 tree contained exactly the six
bound design documents, experiments/source_lock.json, the citation sidecar,
and the immutable Round-1 review. It contained no Paper-11 code,
registered-run, result, figure, or manuscript artifact.

## Local and review-history bindings

Every v2 local binding reproduces exactly.

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| notes/RESEARCH_QUESTION.md | f695dd359e4f965fcf13e7c4550daf9ae90ce6565fbdb61a8c3a39fb2cee174a | exact |
| notes/NOVELTY_ASSESSMENT.md | 1dbd6e4dc07fbc1e126334f6484a71b77852f0583749ba64259bd0e603669c95 | exact |
| notes/PROOF_PACKAGE.md | 3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948 | exact |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490 | exact |
| experiments/EXPERIMENT_PLAN.md | 2e69d035a315061cf0cbc9608fae66cbc2545480b84dabaa6e20b3a40f3409e5 | exact |
| experiments/EXPERIMENT_TRACKER.md | a02e413ba9e493b38588f7809172e03a8b6c07c9d6b102f407b12b829194dc81 | exact |
| notes/CITATION_VERIFICATION.md | 1bfc33598d9ff5e5a8636a9ba5f8365ef9c3176614ba90a2b64ae1eb6dc4154b | exact |
| immutable notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 233da2cb9707f340e7dec588437f694133af63f30bc17c0547dd2a9032a1c17a | exact |
| experiments/source_lock.json | 331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b | exact |

The v2 lock is strict JSON. A duplicate-key-rejecting parse found no
duplicate object key. The bound Paper-9 and Paper-10 source locks, the bound
Paper-10 raw result and result manifest, and the bound Paper-10 terminal
pipeline state also strict-parse without duplicate keys.

## Upstream bindings

### Paper 9

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| experiments/source_lock.json | 662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49 | exact |
| paper/FINAL_INTEGRITY.md | 7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712 | exact |
| paper/paper_final.pdf | 96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6 | exact |

The bound Paper-9 final-integrity record states
COMPLETE_LOCAL_FINAL_REVIEW_PASS.

### Paper 10

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| experiments/source_lock.json | aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2 | exact |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5 | exact |
| results/EXPERIMENT_RESULTS.json | 8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff | exact |
| results/result_manifest.json | db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658 | exact |
| results/INDEPENDENT_RESULT_INTEGRITY.md | 29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58 | exact |
| experiments/OFFICIAL_EXPERIMENT_RESULTS.md | 1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e | exact |
| experiments/OFFICIAL_VALIDATION_REPORT.md | f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a | exact |
| paper/paper_final.pdf | f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378 | exact |
| paper/reviews/round2_review.md | ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae | exact |
| paper/FINAL_INTEGRITY.md | e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce | exact |
| paper/PIPELINE_STATE.json | dc7550b39e42cdeeeacd4ae64f9fb4142b0f2e2e4b315d0e73f1932077e0b09c | exact |

The Paper-10 independent result review states RESULT_PASS. Its final
integrity and terminal pipeline state state
COMPLETE_LOCAL_FINAL_REVIEW_PASS. The inherited free-transitive
centralizer-torsor theorem and exact nine-row ledger remain upstream inputs,
not Paper-11 reruns.

## Round-1 repair closure

The v1 package incorrectly characterized

\[
\Phi_G:B(G)\longrightarrow\mathbb Z,\qquad
\Phi_G([G/H])=|H|
\]

for abelian \(G\) as a homomorphism of Burnside rings. Every live v2 design
document has removed that positive multiplicativity claim. The only
remaining occurrences of the rejected wording are negative corrections or
the immutable Round-1 review history.

V2 now states exactly that \(\Phi_G\) is an additive homomorphism of abelian
groups on Burnside classes. Its nonmultiplicativity witness is correct. For
a nontrivial finite group \(G\), let \(\mathbf u=[G/\{e\}]\). Under the
diagonal Cartesian product, \(G\times G\) splits into \(|G|\) regular
\(G\)-orbits, so

\[
\mathbf u^2=|G|\mathbf u.
\]

Additivity and \(\Phi_G(\mathbf u)=1\) give

\[
\Phi_G(\mathbf u^2)=|G|
\ne1
=\Phi_G(\mathbf u)^2.
\]

Thus no multiplicativity for the Cartesian Burnside product is available or
used.

For every additive map \(\psi:B(G)\to R\), the package defines only

\[
\psi_*\!\left(\prod_{m\ge1}(1-t^m)^{-s_m/m}\right)
=\prod_{m\ge1}(1-t^m)^{-\psi(s_m)/m}.
\]

It applies \(\Phi_G\) to Lefschetz or exact-period classes before forming the
scalar product. It makes no claim that \(\Phi_G\), arbitrary marks, or
another additive map preserves Burnside multiplication, the
pre-\(\lambda\) structure, or the symmetric-power structure. The Round-1
blocker is closed without changing any support or exponent formula.

## Formula and definition regression

The live v2 package keeps distinct:

1. the 2008 fixed-point/point-order rational Burnside zeta;
2. the 2015 fixed-\(G\)-orbit/orbit-order integral Burnside zeta; and
3. the 2013 \(G\)-permutation invariant determined by the complete twisted
   Lefschetz table and represented by a
   \((\mathbb Z\times G)\)-set.

The 2018 enhanced carrier, two additive exact-period orbifold reductions,
and the Morita quotient-stack boundary remain separately named.

For

\[
X=\coprod_{K\le C}n_K(C/K),\qquad H=\langle a\rangle,
\]

the exact general formulas remain

\[
d_K=[H:H\cap K],\qquad M_K=[C:HK],
\]

\[
\zeta_{X,\phi_a}(t)
=\prod_K(1-t^{d_K})^{-n_K[C:HK]},
\qquad
\zeta_{X/C,\bar\phi_a}(t)=(1-t)^{-\sum_Kn_K},
\]

\[
P_m^C=\sum_{d_K=m}n_K[C/K],
\qquad
\zeta_{\mathrm{pt}}^C(t)
=\prod_m(1-t^m)^{-P_m^C/m},
\]

\[
\widetilde P_1^C=[X],\qquad
\widetilde P_m^C=0\ (m>1),\qquad
\widetilde\zeta_{\mathrm{orbset}}^C(t)=(1-t)^{-[X]}.
\]

The negative signs follow the Artin--Mazur inverse convention. The point
classes depend on \(a\) only through \(H\); orbit-order data have only period
one. Additive exact-period orbifold reduction remains

\[
\Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
=\prod_K(1-t^{d_K})^{-n_K|K|/d_K},
\qquad
\Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)
=(1-t)^{-\sum_Kn_K|K|}.
\]

With the locked left action

\[
(j,c)\cdot xK=ca^jxK,
\]

the \((\mathbb Z\times C)\)-stabilizer remains

\[
\widehat K_a
=\langle\{0\}\times K,(1,a^{-1})\rangle.
\]

It records \(a^{-1}K\), and all represented orbit types recover exactly
\(a\) modulo \(N=\bigcap_{n_K>0}K\). Exact labelled recovery is equivalent
to effectivity. The regular 2013 triple is \((1,1,a_q^{-1})\), while the
enhanced return twist is \(a_q\).

The stack formula

\[
[X/C]\simeq\coprod_Kn_KBK
\]

and the \(\sum_Kn_K|K|\) static inertia-sector count remain correct.
Translation by \(a\) is \(2\)-isomorphic to identity. In the free regular
torsor, the action groupoid is equivalent to a point and has no nonidentity
inertia sector. The statement remains limited to Morita- and
\(2\)-isomorphism-invariant data.

For the structural control

\[
C=C_6,\qquad X=C_6/C_2\sqcup C_6/C_3,
\]

the kernel is \(C_2\cap C_3=1\), while point periods are \(3\) and \(2\).
The exact records remain

\[
\zeta_X=(1-t^3)^{-1}(1-t^2)^{-1},\qquad
\zeta_{X/C}=(1-t)^{-2},
\]

\[
\Phi_*(\zeta_{\mathrm{pt}})
=(1-t^3)^{-2/3}(1-t^2)^{-3/2},\qquad
\Phi_*(\widetilde\zeta_{\mathrm{orbset}})=(1-t)^{-5}.
\]

The quotient stack is \(BC_2\sqcup BC_3\) with five static sectors. This
control remains outside the modulus namespace.

## Paper-10 specialization and fixed ledger

For \(X_q\simeq G_q\), \(K=1\), and \(a_q=A\bmod q\), let
\(n_q=|G_q|\), \(r_q=\operatorname{ord}_{G_q}(a_q)\), and
\(m_q=n_q/r_q\). The regular orbit \(\mathbf u_q=[G_q/1]\) gives

\[
\zeta_{\mathrm{pt},q}^{G_q}
=(1-t^{r_q})^{-\mathbf u_q/r_q},
\qquad
\widetilde\zeta_{\mathrm{orbset},q}^{G_q}
=(1-t)^{-\mathbf u_q},
\]

with four reductions

\[
(1-t^{r_q})^{-m_q},\quad
(1-t^{r_q})^{-1/r_q},\quad
(1-t)^{-n_q},\quad
(1-t)^{-1}.
\]

The ordered tuple remains exactly

\[
(2,3,5,7,11,4,6,9,10)
\]

with rows

\[
\begin{aligned}
(n_q,r_q,m_q)=\;&(3,3,1),(8,4,2),(20,10,2),\\
&(48,8,6),(100,5,20),(12,3,4),\\
&(24,12,2),(72,12,6),(60,30,2).
\end{aligned}
\]

There is no tenth modulus or extra scan. The collisions
\(r_2=r_4=3\) and \(r_6=r_9=12\), plus composite controls
\(4,6,9,10\), show that the retained period is neither a modulus identifier
nor a prime selector.

## Novelty and nonclaim regression

The novelty score remains \(2/10\). The 2008, 2013, 2015, and 2018
constructions remain direct prior art; Zegowitz remains the
shortening/gluing collision; Miles and Walton remain scope boundaries; and
the 2024--2026 screen remains context rather than priority evidence.

V2 claims no new equivariant, Burnside, orbifold, enhanced, or stacky zeta;
historical priority; universal no-go theorem; canonical cross-\(q\)
coefficient ring; extension of Miles or Walton; intrinsic prime clock;
Riemann Euler product; prime/zero correspondence; or Route-B authorization.

## Source-stage disposition

The v2 package is internally consistent, proof-complete for its frozen
scope, byte-bound to all local and upstream evidence, and ready for the
separate implementation/deployment-review stage.

SOURCE_LOCK_PASS
