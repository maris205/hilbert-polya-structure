# HCS-C59 primary-source and novelty audit

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Search boundary: **2026-08-16 UTC, bounded instance and topic search.**

## 1. Claim/source matrix

| source | exact locator | authorized C59 use | not supplied |
|---|---|---|---|
| Austen A. James, *A Bayesian Approach to Computing Brauer Groups of Cubic Surfaces* (Rice PhD thesis, 2022) | §3.1, printed p. 22 | the 350 subgroup classes of (W(E_6)) yield 339 fractional profiles and exactly 11 Gassmann collisions | no C59 minimum-index extraction, orbit sums, fields, discriminant, or local tables |
| Robert Perlis, “On the equation \(\zeta_K(s)=\zeta_{K'}(s)\),” *J. Number Theory* 9 (1977), 342--360 | Theorem 1; printed p. 351 | Gassmann/arithmetic-equivalence criteria and a classical explicit example | no C59 cubic-surface construction |
| Wieb Bosma and Bart de Smit, “On arithmetically equivalent number fields of small degree,” ANTS V (2002), 67--79 | introduction, pp. 67--68; §3.3 | equality of degree, discriminant, signature, and normal closure; permutation-character computation | no C59 instance |
| D. B. McReynolds, “Geometric Spectra and Commensurability,” *Canad. J. Math.* 67 (2015), 184--197 | proof of Theorem 1.2, pp. 193--194 | explicit common-normal-closure arithmetic equivalence with different ramified local degrees | no (W(E_6)) or cubic-surface realization |
| Guillermo Mantilla-Soler, “On a question of Perlis and Stuart regarding arithmetic equivalence,” *NYJM* 25 (2019), 558--573 | Theorem 1.3, p. 559; Theorem 3.7 and proof, p. 572 | explicit polynomial pairs with equal zeta data and different ramification tuples | no C59 pair |
| Keiichi Komatsu, “On adele rings of arithmetically equivalent fields,” *Acta Arith.* 43 (1984), 93--95 | entire note | distinction between arithmetic and adelic/local equivalence | no C59 computation |
| Richard P. Stauduhar, “The determination of Galois groups,” *Math. Comp.* 27 (1973), 981--996 | abstract and opening sections | classical resolvent construction from ordered roots | no C59 invariant or certificate |
| Claus Fieker and Juergen Klueners, “Computation of Galois groups of rational polynomials,” *LMS J. Comput. Math.* 17 (2014), 141--158 | §1; §2 and Remark 2.1 | Stauduhar method and relative invariants/stabilizers | no C59 product or split witness |
| Elsenhans--Jahnel, “Moduli spaces and the inverse Galois problem for cubic surfaces” | introduction theorem p. 2; Algorithm 5.1; Algorithm A.10 | established program of explicit cubic-surface (W(E_6))-realization | no C59 fields |
| GAP/TomLib documentation and TomLib 1.2.9 `U4(2).2` table | official package documentation and versioned data | table-of-marks fixed-point convention and exact finite computation | no literature novelty or durable embedded field definition |

## 2. Known results that C59 must not rebrand

James's eleven collisions are prior art. The ToM-301/303 pair is not a new
Gassmann discovery. Equality of the induced trivial characters implies equal
Dedekind zeta functions by classical Gassmann/Perlis theory. Common-normal-
closure arithmetically equivalent fields with different ramified local
algebras are classical. Relative invariants and resolvents are established
computational Galois methods.

The phrase “unique minimum-index pair” is restricted to the complete 350-row
subgroup table for this (W(E_6)) model. It is not a minimum degree for
arithmetically equivalent number fields in general.

## 3. Bounded new contribution

The only authorized novelty statement is:

> For the one released cubic-surface line extension, two exact integral
> quadratic orbit sums primitively realize the minimum-index (W(E_6))
> Gassmann pair, and the resulting fields have a complete exact eight-prime
> global arithmetic package and nonisomorphic finite etale
> $\mathbf Q_3$-algebras in both surviving decomposition-group branches.

The bounded search found no primary source containing that exact conjunction.
This is negative search evidence, not proof of absolute priority. No “first”
claim is authorized.

## 4. Explicit-field boundary

The exact fields are defined by embedded subgroup arrays and the scaled sums

\[
\alpha_i=Ld_i,\qquad
\eta_\pm=\sum_{\{i,j\}\in\mathcal S_\pm}\alpha_i\alpha_j.
\]

The name (eta) never denotes an unscaled sum. An unscaled sum is
$\widetilde\eta$, with $\eta=L^2\widetilde\eta$. The exact
characteristic-zero resolvent is the finite product over $G/H_\pm$. This
does not supply expanded characteristic-zero coefficients, a power integral
basis, or a maximal order.

ToM positions are version-sensitive locators. Durable field definitions
require exact 27-point generator arrays and exact support arrays in the
released labelled carrier. A fresh abstract group isomorphism is not release
authority.

## 5. Local wording boundary

For $F=K^H$, the factors of $F\otimes\mathbf Q_3$ are indexed by
$D\backslash G/H$. The local rows `(n,e,f,d)` are obtained from the
corresponding stabilizers and lower filtration. Different degree multisets
are sufficient to prove nonisomorphism of the two finite etale algebras.

The tuple `(n,e,f,d)` does not classify an individual high-degree local field.
Equality of global zeta functions remains compatible with the local
separation because the residue-degree multisets agree branchwise.

## 6. Graph and feasibility boundary

A bounded design computation first enumerated 51,840 graph automorphisms and
found equality with the released faithful (W(E_6)) permutation set. That
historical result supports target selection only and is not theorem
authority. Canonical G1 now reproduces the graph from all four line equations,
and the independent checker proves

\[
\operatorname{Aut}(\text{Schlaefli graph})=W(E_6)
\]

inside the released labelled action as equality of full 51,840-element
permutation sets. Eight sampled graph isomorphisms remain smoke evidence, not
the proof.

## 7. Negative source gates

The formal package and eventual paper must reject:

- “first arithmetically equivalent fields with different completions”;
- “first common-normal-closure example”;
- “first Gassmann collision in (W(E_6))”;
- “new resolvent method”;
- “minimum degree of arithmetically equivalent fields” without the exact
  (W(E_6))-table qualifier;
- “ToM 301/303 canonically define the fields”; and
- any inference from equal zeta functions to integral, local, adelic, or
  idele equivalence.

## 8. Scope and current status

`NO_BAD_EULER_OR_ROOT_NUMBER` remains absolute. No source in this ledger
supplies a C59 bad Euler factor, Frobenius, epsilon factor, root number,
automorphy, rational-point theorem, Brauer--Manin conclusion, motive, RH, or
Hilbert--Polya operator.

The source and salami review supports the bounded novelty statement. The
official project-local tuple contains 13 source files and 8 result files, 21
live entries and 20 self-excluding scoped entries. All G0--G7 gates pass; the
payload has 10,412 scalar leaves; the independent checker rejects 20,894
certificate rebound mutations and 8 evidence mutations; and all 48 tests and
the independent post-refresh machine hostile audit pass.

The principal SHA-256 values are payload
`a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b`,
certificate
`3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a`,
check report
`271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3`,
schema file
`07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4`,
group/resolvent evidence
`0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958`
and
`667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`,
scoped manifest
`c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda`,
payload shape
`788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2`,
and G0 subpayload
`ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d`.

This post-refresh prose has passed its new formal-document hostile audit. The
paper bibliography recheck, paper construction/audit, release provenance,
promotion, and release remain pending.
