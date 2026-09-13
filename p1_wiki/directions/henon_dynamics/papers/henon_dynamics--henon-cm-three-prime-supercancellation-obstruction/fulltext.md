---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cm-three-prime-supercancellation-obstruction"
canonical_tex: "henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/paper/paper.pdf"
source_sha256: "e7125ab36ef8dbd8bbfbb8a8829ec8c9a31bf3dfff542652d99a7c19973ebc78"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Three Primes Close the Finite Cubic-Cohomology Bridge: A Supercancellation Rigidity Theorem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cm_three_prime_supercancellation_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_cm_three_prime_supercancellation_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The cubic Hénon channel has a natural arithmetic completion in the $j=0$ elliptic curve $E:y^2=x^3+1$, but its degree-two Euler factors are not Riemann factors. We test whether finite graded cohomology can cancel the difference. At each good prime, allow arbitrary integral powers of the degree-zero Tate factor, the $H^1(E)$ factor, and the degree-two Tate factor. We prove that equality with $(1-T)^{-1}$ at the three primes $5,7,11$ forces the exponent vector to be $(1,0,0)$. The coefficient matrix has determinant $-24$; hence the result holds over the rationals, not merely in a finite search box. Exact code recomputes the point counts, exhausts 15,625 integral classes, and checks six holdout primes. Thus every nontrivial use of the cubic CM geometry changes the local Riemann ledger. The theorem closes the finite Tate-plus-CM supercancellation route while leaving infinite-rank complexes and non-Euler scattering constructions outside its scope.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
bibliography:
- references.bib
date: 'Preprint, August 2026'
title: |
  Three Primes Close the Finite Cubic-Cohomology Bridge:\
  A Supercancellation Rigidity Theorem
```

## Markdown 正文

# Introduction

The preceding cubic arithmetic completion provides genuine Frobenius data with intrinsic square-root normalization. Its global object is an elliptic $L$-function rather than the Riemann zeta function. Graded determinants suggest a possible repair: combine the new $H^1$ factor with Tate pieces in a virtual cohomology class, hoping that unwanted local data cancel.

This paper tests the entire smallest such category. The test is local and exact. Equality of Euler factors implies equality of their first logarithmic coefficients. Two inert primes and one split prime produce a nonsingular three-by-three system. Its unique solution removes the elliptic factor itself.

The result illustrates a useful research rule. Before constructing a global operator from a finite cohomological ansatz, compare a minimal set of local traces. A low-rank obstruction can close an infinite global fitting problem without computing a single Riemann zero.

# The finite virtual category

Let $E:y^2=x^3+1$, and for a good prime $p$ set $$a_p=p+1-\#E(\mathbb F_p),
 \qquad P_p(T)=1-a_pT+pT^2.$$ The three basic cohomological local factors are $$(1-T)^{-1},\qquad P_p(T)^{-1},\qquad (1-pT)^{-1}.$$ They correspond formally to $H^0$, $H^1(E)$, and $H^2$; see [@Milne2026; @Serre1965]. For integers $A,B,C$, define $$\label{eq:virtual}
 D_{p;A,B,C}(T)
 =(1-T)^{-A}P_p(T)^{-B}(1-pT)^{-C}.$$ Negative exponents are retained as numerator factors. No absolute values or post-hoc deletion are allowed.

The target local Riemann factor is $$\label{eq:target}
 Z_p(T)=(1-T)^{-1}.$$

# First logarithmic coefficient

Expanding at $T=0$ gives $$\begin{aligned}
 \log D_{p;A,B,C}(T)
 &=\bigl(A+Ba_p+Cp\bigr)T+O(T^2),\\
 \log Z_p(T)&=T+O(T^2).\end{aligned}$$ Therefore local equality implies $$\label{eq:linear}
 A+Ba_p+Cp=1.$$ This condition is only necessary at one prime, but three selected primes make it decisive for the full parameter vector.

Direct point counts give $$a_5=0,qquad a_7=-4,qquad a_{11}=0.$$ The inert-prime zeros at $5$ and $11$ also follow from bijectivity of the cube map modulo primes congruent to two modulo three.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Suppose [\[eq:virtual\]](#eq:virtual){reference-type="eqref" reference="eq:virtual"} equals [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"} at $p=5,7,11$. Then $$(A,B,C)=(1,0,0).$$ The same conclusion holds if the exponents are allowed to be rational.

Equation [\[eq:linear\]](#eq:linear){reference-type="eqref" reference="eq:linear"} at the three primes is $$\begin{pmatrix}
 1&0&5\\
 1&-4&7\\
 1&0&11
 \end{pmatrix}
 \begin{pmatrix}A\\B\\C\end{pmatrix}
 =\begin{pmatrix}1\\1\\1\end{pmatrix}.$$ The coefficient determinant is $-24$, so the solution is unique over $\mathbb Q$. Subtracting the first equation from the third gives $6C=0$, hence $C=0$ and $A=1$. The middle equation then gives $-4B=0$, hence $B=0$.

Within the virtual category [\[eq:virtual\]](#eq:virtual){reference-type="eqref" reference="eq:virtual"}, every nontrivial use of $H^1(E)$ changes at least one of the three frozen local Riemann factors. Exact local matching retains only the undecorated degree-zero zeta factor.

The first logarithmic coefficient is enough because it already yields a full-rank system. No claim is made that first coefficients generally determine arbitrary Euler factors.

# Exact certificate

The code recomputes $a_5,a_7,a_{11}$ from Legendre sums, constructs the matrix in Theorem [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}, and performs exact Gaussian elimination with rational fractions. It then enumerates all $(A,B,C)\in[-12,12]^3$, totaling $15{,}625$ classes, and finds the single match $(1,0,0)$. Finally, primes $13,17,19,23,29,31$ serve as holdouts.

  Item                                             Value
  -------------------------- ---------------------------
  Sentinel primes                               5, 7, 11
  Matrix determinant           $-24$ (absolute value 24)
  Unique rational solution                     $(1,0,0)$
  Integral classes checked                        15,625
  Holdout primes                                       6

  : Rigidity certificate.

The finite enumeration is adversarial validation, not the proof of global uniqueness. The determinant calculation proves the theorem for every rational, hence every integral, exponent vector.

# Scope and evaluator audit

The theorem classifies exactly the finite span generated by the two Tate pieces and $H^1(E)$. It does not classify infinite-rank local complexes, prime-dependent exponents, non-Euler scattering determinants, or a new trace formula derived directly from Hénon periodic orbits. An arbitrary global zero-free factor is also outside the local Euler-equality claim; it cannot be invoked silently to rewrite the frozen local factors.

Route A records weak A1, failed A2, partial analytic A3, and formal A4. The tuple is $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL\ ANALYTIC},A4_{\rm FORMAL\ HINT}).$$ Route B stops at B1 because no operator/domain is defined. Even at the formal B4 level, every nontrivial cubic class has the wrong prime trace.

# Conclusion

The cubic channel can be made arithmetic, but finite cohomological grading cannot make it Riemann without erasing it. Three primes already force the unique local match to be the original zeta factor. This closes the direct Kummer-to-CM-to-superdeterminant bridge in its finite natural category. Future work must introduce a genuinely new prime-trace function outside the span of $1,a_p,p$, and must derive that function from Hénon chronology rather than from a fitted cancellation.
