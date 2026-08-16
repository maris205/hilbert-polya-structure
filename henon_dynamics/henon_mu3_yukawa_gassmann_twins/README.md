# HCS-C59: primitive Gassmann twins from the 27 lines

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Locked object

HCS-C59 starts from the released cubic-surface line extension

\[
K/\mathbf Q,\qquad
G=\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |G|=51840,
\]

and constructs two new degree-(320) fields from exact quadratic orbit sums
in the labelled roots of the degree-(27) line eliminant. The defining
subgroups $H_+,H_-\leq G$ have order $162$, index $320$, trivial core,
SmallGroup identifiers `[162,11]` and `[162,19]`, and equal full rational
transitive permutation characters. Their frozen-version TomLib locators are
301 and 303, but those numbers do not define the fields.

If (d_i) are the labelled eliminant roots, (L) is the eliminant leading
coefficient, and (alpha_i=Ld_i), define

\[
\mathcal S_+=H_+\!\cdot\!\{1,2\}\sqcup
H_+\!\cdot\!\{1,9\},\qquad |\mathcal S_+|=27+27,
\]
\[
\mathcal S_-=H_-\!\cdot\!\{1,2\},\qquad |\mathcal S_-|=81,
\]

and the integral quadratic sums

\[
\eta_\pm=\sum_{\{i,j\}\in\mathcal S_\pm}\alpha_i\alpha_j.
\]

`eta` always denotes this scaled integral object. If the unscaled sum is
mentioned, it is $\widetilde\eta_\pm$, with
$\eta_\pm=L^2\widetilde\eta_\pm$.

## 2. Integrated theorem

The certified exact premises C59-EXACT-0 through C59-EXACT-7 prove

\[
F_+=\mathbf Q(\eta_+)=K^{H_+},\qquad
F_-=\mathbf Q(\eta_-)=K^{H_-}.
\]

The fields are nonisomorphic, have common normal closure (K), and satisfy

\[
\zeta_{F_+}(s)=\zeta_{F_-}(s).
\]

Their common signature and signed discriminant are

\[
(r_1,r_2)=(16,152),
\]
\[
\operatorname{Disc}(F_+)=\operatorname{Disc}(F_-)
=+3^{624}5^{496}A^{192}B^{160},
\]

where

\[
A=181\cdot997\cdot2346241=423395612137,
\]
\[
B=283\cdot1801\cdot
14932047182473291995860108491583652133938007263719.
\]

At (3), the complete local-factor tables differ for both C58-permitted
decomposition groups, ToM 140 and ToM 206. Thus the fields are arithmetically
equivalent but not locally equivalent and their adele rings are not
isomorphic. No decomposition-group branch is selected.

## 3. Why this is one paper-sized step

James already reports the 350-to-339 profile collapse and all eleven
(W(E_6)) Gassmann collisions. Perlis/Gassmann theory already supplies the
character/zeta bridge; explicit arithmetically equivalent fields with
different ramified local algebras are classical; relative resolvents are an
established method. C59 claims none of those general facts as new.

The locked contribution is the conjunction of:

1. exact primitive quadratic generators tied to the labelled 27 lines;
2. the unique minimum-index collision inside the complete (W(E_6)) table;
3. exact eight-prime global arithmetic; and
4. complete branch-independent $\mathbf Q_3$-algebra separation.

Removing the primitive realization or either local branch kills the paper.

## 4. Canonical G0--G7 map

- G0: released-authority rebind;
- G1: primitive integral orbit-sum resolvents and graph-label independence;
- G2: complete Gassmann/minimality certificate;
- G3: fixed-field, common-normal-closure, nonisomorphism, and zeta bridge;
- G4: signed discriminant, signature, and exact support;
- G5: complete ToM-140 local algebra;
- G6: complete ToM-206 local algebra and branch independence;
- G7: independent checker, mutation/rebound envelope, novelty, scope, and
  release discipline.

All eight gates are `PREFREEZE_CODE_RESULTS_PASS`. G1 reconstructs every line
and all four chart equations, then proves
`Aut(Schlaefli graph)=W(E6)` as equality of the full 51,840-element
permutation sets. The earlier bounded graph enumeration remains historical
design-feasibility evidence and is not used as project authority.

## 5. Formal-root inventory

The formal-root inventory contains exactly 13 project-root Markdown files:

```text
DERIVATION.md
EXPERIMENT_PLAN.md
EXPERIMENT_TRACKER.md
IMPLEMENTATION_CHECKLIST.md
INTEGRITY_REPORT.md
METHODOLOGY_BLUEPRINT.md
NARRATIVE_REPORT.md
PAPER_PLAN.md
PROOF_PACKAGE.md
README.md
RESEARCH_QUESTION.md
SOURCE_AUDIT.md
THEOREM_PACKAGE.md
```

The post-refresh project also contains exactly 13 source files and 8 result
files: 21 live code/result entries, of which the self-excluding scoped
manifest binds 20. This documentation handoff changes formal-root bytes after
the machine tuple was frozen, so its new 13-file aggregate and Route binding
required—and have now passed—a fresh formal-document hostile audit. Paper,
archive, compilation, promotion, and release artifacts remain absent.

## 6. Official machine evidence

All G0--G7 gates pass. The 15-key payload has 10,412 scalar leaves; the
checker rejects 20,894 certificate rebound mutations and 8 evidence-carrier
mutations; and all 48 tests pass. The mandatory nonmutating replay and
independent post-refresh machine hostile audit pass.

| artifact | SHA-256 |
|---|---|
| canonical payload | `a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b` |
| `results/c59_certificate.json` | `3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a` |
| `results/c59_check_report.json` | `271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3` |
| `results/c59_schema.json` | `07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4` |
| `results/c59_group_evidence.json` | `0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958` |
| `results/c59_resolvent_evidence.json` | `667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6` |
| `results/scoped_hash_manifest.json` | `c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda` |
| payload shape | `788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2` |
| G0 subpayload | `ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d` |

`run_all.sh` replays the frozen pre-documentation machine layer. Once formal
roots or Route change, its historical source/result tuple remains valid, but
the command does not claim that the changed documentation has passed its
separate formal audit.

By layered-lock policy, machine-bound `results/RESULTS.md` and
`results/TEST_REPORT.md` deliberately preserve their source-stable
pre-promotion wording. Rewriting those leaves after promotion would change the
certified tuple. Current machine status is governed by the certificate, check
report, scoped manifest, and independent `POSTREFRESH_PASS` verdict; the
historical prose banners do not downgrade that authority.

## 7. Hard scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER`: C59 claims no decomposition Frobenius, bad
Artin Euler polynomial or factor, local epsilon factor, local/global root
number, Artin holomorphy, or automorphy. It claims no expanded
characteristic-zero coefficient list, integral basis, monogenicity, maximal
order, equality of polynomial and field discriminants, integral permutation
equivalence, equal class numbers, local or adelic equivalence, individually
classified high-degree completions, rational point, Hasse principle, weak
approximation, Brauer--Manin obstruction, motive, RH, or Hilbert--Polya
operator.

“Primitive” means only that each displayed $\eta_\pm$ generates its fixed
field. It does not mean that the degree-(320) field has no intermediate
fields or that the coset action is primitive.

## 8. Current boundary

The code/results tier is `PREFREEZE_CODE_RESULTS_PASS`; the independent
post-refresh machine hostile audit is `POSTREFRESH_PASS`, and the current
formal roots have `FORMAL_DOCS_PASS`. Paper construction, paper hostile
review, compilation, release provenance, archive, promotion, and release
remain pending. Status is therefore `PAPER_PENDING / NOT_RELEASED`.
