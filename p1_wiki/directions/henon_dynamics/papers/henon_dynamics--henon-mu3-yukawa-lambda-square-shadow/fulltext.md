---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-lambda-square-shadow"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/paper/main.pdf"
source_sha256: "37a8ffa2657f507fb1727e5459dfa88d44139e29e3b27ec83517ff766a811bc8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Lambda-Square Shadows of a \texorpdfstring$W(E_6)$W(E6) Gassmann Pair

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_lambda_square_shadow>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Starting from the released degree-160 Gassmann pair for the Weyl group $G=W(E_6)$, we compute the exterior-square and symmetric-square shadows of the two permutation $G$-sets. Exact finite-group enumeration verifies equal rational characters, complete orbit atlases, core-free stabilizers, normalizer orders, and a fixed-field dictionary grouped by ambient conjugacy. The two shadows have dimensions $51{,}040$ and $51{,}360$. Product-form marker carriers are supplied with a split-prime noncollision witness. These are finite-group and formal marker results only: no arithmetic field resolvent, discriminant, Euler factor, or root-number claim is made.
author:
- C62 computational research note
date: August 2026
title: 'Lambda-Square Shadows of a $W(E_6)$ Gassmann Pair'
```

## Markdown 正文

# Question and scope

Let $H_+$ and $H_-$ be the released nonconjugate order-$162$ subgroups of $G=W(E_6)$, and write $X_\pm=G/H_\pm$. The question is whether applying the degree-two lambda operations can preserve the permutation character while separating the resulting finite $G$-sets and their fixed-field shadows. Throughout, the scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. Thus all conclusions below are finite-group or formal-marker conclusions.

# Lambda identities

For a finite $G$-set $X$ and $g\in G$, the standard formulas are $$\chi_{\Lambda^2 X}(g)=\frac{\chi_X(g)^2-\chi_X(g^2)}2,
 \qquad
 \chi_{\operatorname{Sym}^2X}(g)=\frac{\chi_X(g)^2+\chi_X(g^2)}2.$$ The released C61 equality $\chi_{X_+}=\chi_{X_-}$ therefore implies equality of both degree-two characters. The producer independently evaluates these identities on the complete $W(E_6)$ action and records dimensions $$|\Lambda^2X_\pm|=\binom{320}{2}=51{,}040,
 \qquad |\operatorname{Sym}^2X_\pm|=\binom{321}{2}=51{,}360.$$

# Complete orbit atlases

The exact action enumerates all two-subsets and all size-two multisets. The exterior-square atlas has 10 orbits totaling $51{,}040$ points; the symmetric-square atlas has 11 orbits totaling $51{,}360$ points. For every orbit we store the complete stabilizer element set, its core, its normalizer, and canonical digests. In each row the fixed-field degree is checked by $$[G^{\mathrm{core}(S)}:S]=\frac{|G|}{|S|}=\frac{51{,}840}{|S|},$$ with trivial core in all 42 plus/minus orbit records.

Four matched exterior rows and five matched symmetric rows have nonconjugate plus/minus stabilizers. Hence character equality is not used as an isomorphism test for the actual finite $G$-sets.

# Fixed-field dictionary

The G4 dictionary groups the complete stabilizer sets by conjugacy in the ambient $W(E_6)$, producing 16 explicit type labels. The checker verifies that each label has a consistent subgroup order, normalizer order, core order, and fixed-field degree. The plus and minus type sets differ in both lambda operations. Several subgroup orders split into multiple labels, so subgroup order, orbit-table position, or a hash cannot serve as the field identifier.

  shadow                     orbit count   total degree   matched nonconjugate rows
  ------------------------ ------------- -------------- ---------------------------
  $\Lambda^2$                         10         51,040                           4
  $\operatorname{Sym}^2$              11         51,360                           5

# Marker carriers and arithmetic boundary

For each orbit $\mathcal O$ the reproducibility package stores the formal carrier $$R_{\mathcal O}(T)=\prod_{(i,j)\in\mathcal O}
 \bigl(T-(512X_i+X_j)\bigr).$$ At the released split-prime witness $p=692717$, all evaluated marker values inside each orbit are distinct and below $p$. This certifies a convenient noncollision label for the orbit computation. It does not expand the carrier over characteristic zero and does not identify an arithmetic number field. Consequently no discriminant, different, local extension, Euler factor, ramification, or root-number statement is made here.

# Reproducibility and nonclaims

The code and JSON evidence are deterministic and source-bound to the released C61 group action. The commands are:

    python3 code/c62_lambda.py
    python3 code/c62_atlas.py
    python3 code/c62_resolvent.py
    python3 code/c62_dictionary.py
    python3 code/c62_dictionary_checker.py

All outputs are marked prefreeze until the final audit and manifest closure. The paper deliberately does not claim arithmetic equivalence beyond the finite fixed-field shadow, and it does not claim any bad-prime or root-number result.

# Conclusion

Degree-two lambda operations preserve the rational permutation character of the C61 Gassmann pair while producing complete, explicitly separated finite orbit/stabilizer data. The resulting 16-type fixed-field dictionary and the formal marker carriers constitute the C62 contribution within the stated scope boundary.

9 J.-P. Serre, *Topics in Galois Theory*, Jones and Bartlett, 1992. W. Burnside, *Theory of Groups of Finite Order*, Cambridge University Press, 1911.
