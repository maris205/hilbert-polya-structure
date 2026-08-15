# HCS-C57: minimal 2-primary Brauer jump

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; THEOREM_TARGET_LOCKED; machine
PREFREEZE_CODE_RESULTS_PASS; NOT_RELEASED.**

HCS-C57 studies one fixed object: the smooth Q-defined cubic surface \(Y\)
released by HCS-C55, together with the full \(W(E_6)\) line field proved in
HCS-C56. The locked theorem target identifies the smallest degree of a finite
extension over which the algebraic Brauer quotient acquires 2-torsion, and
constructs a canonical quaternion representative over an attaining field.

The exact project-local machine tuple now passes
`PREFREEZE_CODE_RESULTS_PASS`: 18 code files and 11 result files form an exact
29-file live inventory, with a self-excluding 28-entry scoped manifest. The
certificate, strict schema, independent checker, 33-test suite, and full
semantic rebound are bound below. The official 18-file paper source, 24-page
PDF, compilation report, and independent hostile paper audit also pass.
Implementation/provenance commits, the post-compile formal-document hash,
full-project manifest, archive, and release remain deliberately unset. Phase-1
and `/tmp` artifacts are chronology and transport evidence only; none is
release provenance.

## 1. Locked outcome

Let \(K/\mathbf Q\) be the HCS-C56 common normal line field, with

\[
\operatorname{Gal}(K/\mathbf Q)\cong W(E_6),\qquad |W(E_6)|=51840.
\]

For an unordered double-six \(D=\{\mathcal E,\mathcal G\}\), where
\(\mathcal E\) and \(\mathcal G\) denote the effective sums of its two
sixers, let

\[
U=U_1=\operatorname{Stab}_{W(E_6)}(D)\cong S_6\times C_2,
\qquad |U|=1440,
\qquad F_D=K^U.
\]

Let

\[
U_1^+=\operatorname{Stab}(\mathcal E)\cap
\operatorname{Stab}(\mathcal G)\cong S_6
\]

be the index-two subgroup of \(U_1\) that preserves the two sixers
separately. Then

\[
F_D'=K^{U_1^+}=F_D(\sqrt{\delta_D}).
\]

The central theorem target is

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0
\quad\Longrightarrow\quad
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q]
\]

for every finite extension \(L/\mathbf Q\), with equality attained at
\(F_D\). In particular the minimum possible degree is 36, and

\[
[F_D:\mathbf Q]=36,\qquad
\operatorname{Br}(Y_{F_D})/\operatorname{im}\operatorname{Br}(F_D)
\cong\mathbf Z/2\mathbf Z.
\]

The intended explicit generator is

\[
\mathcal A_D=(\delta_D,Q_D/u_0^4).
\]

Here \(F_D'/F_D\) orients the double-six, and \(Q_D\) is a canonical
determinant-defined quartic whose divisor is the sum of the twelve lines in
the double-six. No expanded 31-by-36 coefficient table for \(Q_D\) is
required.

## 2. Why this is a new theorem-sized step

HCS-C55 produced the Q-defined Yukawa cubic surface. HCS-C56 determined its
connected degree-27 line scheme and full \(W(E_6)\) normal closure. C57 uses
that actual Galois group to prove a sharp arithmetic minimization theorem and
to descend a concrete Brauer class.

The general facts that cubic surfaces have 36 double-sixes, that their
stabilizer has index 36, and that a Galois-invariant double-six can produce
2-torsion are classical. Elsenhans--Jahnel also explicitly precede C57 in
using a degree-36 double-six resolver in general. The search-bounded
instance-specific content is the complete package for this frozen surface:

1. exact double-six and orientation fields inside the certified C56 field;
2. sharp minimality over every finite extension of \(\mathbf Q\);
3. a compact determinant definition of the quartic \(Q_D\);
4. an exact divisor/norm bridge and a nonzero quaternion generator.

## 3. Essential field distinctions

- \(E/\mathbf Q\) is the non-Galois degree-27 HCS-C56 line field.
- \(K/\mathbf Q\) is its Galois closure and the common normal line field.
- \(F_D=K^U\) is the degree-36 double-six field.
- \(F_D'=K^{U_1^+}=F_D(\sqrt{\delta_D})\) is the oriented quadratic extension.

Thus \(E\ne K\), \(F_D\ne E\), and no one of these fields may be substituted
for another.

Two exact degree-36 generators occur in the design:

\[
\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D).
\]

This equality is proved from stabilizers and the Galois correspondence. C57
does **not** claim or require an expanded identity
\(\delta_D=P(\theta_D)\).

## 4. Proof architecture

The written proof has four independent bridges.

1. **Classification bridge.** The complete Swinnerton-Dyer /
   Elsenhans--Jahnel 2-primary theorem has two branches: a
   \(\mathbf Z/2\) quotient places the Galois image in a conjugate of the
   index-36 double-six stabilizer \(U_1\), while a
   \((\mathbf Z/2)^2\) quotient places it in a conjugate of the classical
   index-720 subgroup \(U_3\). A finite list of natural stabilizers is not
   used as a substitute for this theorem.
2. **Degree bridge.** If \(H_L\) is the image of \(G_L\) in \(W(E_6)\), both
   branches give
   \(36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q]\). Equality excludes the
   \(U_3\) branch and forces a conjugate of \(U_1\).
3. **Brauer bridge.** Exact integral group cohomology gives
   \(H^1(U,\operatorname{Pic}\overline Y)=\mathbf Z/2\); a separate
   Hochschild--Serre argument over the number field \(F_D\) identifies it
   with the algebraic Brauer quotient.
4. **Divisor bridge.** Let \(H_Y\) be the hyperplane class and put
   \(\mathcal L_0=\operatorname{div}_Y(u_0)\). Exact restriction and rank
   certificates define \(Q_D\), while the written degree and norm bridges
   prove

   \[
   \operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G\sim4H_Y,
   \]

   \[
   \operatorname{div}_{Y_{F_D}}(Q_D/u_0^4)
   =\mathcal E+\mathcal G-4\mathcal L_0
   =\operatorname{Norm}_{F_D'/F_D}
   (\mathcal E-2\mathcal L_0).
   \]

## 5. Package inventory

The C57 root package consists of:

- RESEARCH_QUESTION.md: locked question, FINER screen, and claim boundary;
- THEOREM_PACKAGE.md: exact target theorem suite;
- DERIVATION.md: algebra, field, cohomology, and quartic derivations;
- PROOF_PACKAGE.md: rigorous implication from named exact premises;
- SOURCE_AUDIT.md: primary-source locators and bounded novelty contract;
- METHODOLOGY_BLUEPRINT.md: evidence layers and fail-closed workflow;
- EXPERIMENT_PLAN.md: exact producer/checker plan and kill gates;
- EXPERIMENT_TRACKER.md: machine-prefreeze ledger and unresolved downstream
  gates;
- IMPLEMENTATION_CHECKLIST.md: implementation and hostile-test checklist;
- INTEGRITY_REPORT.md: machine identity, remaining-null, and scope ledger;
- NARRATIVE_REPORT.md: adaptive C55--C57 research narrative;
- PAPER_PLAN.md: implemented manuscript plan and official artifact tuple;
- paper/: 18 bound source files, the official PDF, and the compilation report;
- route_a_evaluation.yaml: `PAPER_COMPILED`/`PAPER_HOSTILE_PASS` Route record
  with the unchanged machine PREFREEZE tuple.

The paper subtree contains exactly 20 files: 18 source files, `main.pdf`, and
`COMPILATION_REPORT.md`; no generated auxiliary remains.

## 6. Hard nonclaims

C57 does not claim:

- a new general construction of a double-six resolver;
- an expanded formula \(\delta=P(\theta)\);
- a printed expanded quartic table;
- a rational point or absence of rational points over \(F_D\);
- a Brauer--Manin obstruction, Hasse failure, or weak-approximation failure;
- a local evaluation, local Picard--Artin package, conductor, Euler factor, or
  root number;
- stable irrationality as a C57 novelty;
- a motive, automorphy, Calabi--Yau realization, or new dynamical theorem.

## 7. Current release boundary

The mathematical architecture is locked and the exact machine handoff is
complete at `PREFREEZE_CODE_RESULTS_PASS`. G0--G7 have stable project-local
identities, with G6 ending at the determinant quartic/rank certificate and G7
covering divisor/quaternion/nonzero-class matching; the separate unnumbered
negative-scope firewall also passes. The producer, independent checker,
official atomic refresh, mandatory nonmutating replay, 33/33 tests, and
535/535 rebound cases pass. The paper source aggregate is
`3c2b0a3a3908368ea5efa35f22fb124796e43f5666328c94d3bee0682fd9c10e`;
the 24-page, 537984-byte PDF digest is
`60bdbcbb1a9ddc03ac6a142d22142821860545026fb9dfa21a8001960c7d0200`;
and the independent paper audit reports `PAPER_HOSTILE_PASS` with zero blocker.
Project status nevertheless remains `NOT_RELEASED` with
`promotion_authorized=false`. The next gates are the post-compile root audit
and formal-package binding, commits, full-project manifest, archive, and final
release promotion.
