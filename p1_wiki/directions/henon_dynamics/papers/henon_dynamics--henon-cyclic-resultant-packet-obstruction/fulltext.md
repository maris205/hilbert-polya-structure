---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cyclic-resultant-packet-obstruction"
canonical_tex: "henon_dynamics/henon_cyclic_resultant_packet_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_cyclic_resultant_packet_obstruction/paper/paper.pdf"
source_sha256: "5ff4179fab0262eabf7e9f21b945fb1ba6c149dc5708b5c9591acbc8dac4b7ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclic Resultant Packets and the Norm Trilemma for Hénon Monodromy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cyclic_resultant_packet_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cyclic_resultant_packet_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cyclic_resultant_packet_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cyclic_resultant_packet_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_cyclic_resultant_packet_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Termwise rational-prime labels for a certified area-preserving Hénon survivor are obstructed, leaving cyclic resultants and prime-ideal packets as the smallest collective arithmetic candidates. We prove a norm trilemma for every reciprocal algebraic-unit multiplier. The principal cyclic determinant ideal is an exact square, and its norm from the full multiplier field is an integer square. For every cyclotomic index $n>2$, the full primitive norm is also a square because a unit-normalized cyclotomic value lies in the fixed trace field. In contrast, the minimal trace-field norm and the principal-ideal packet survive; their canonical half norms can be prime or composite. They form repetition-indexed sequences rather than powers of one Euler label. An exact certificate uses the signed primitive H6 multipliers of periods one, three, and four. It verifies 36 resultant rows, including all 30 square-theorem rows, and detects the period-three sign, $n=2$ boundary, nonreciprocal mutation, and false one-scalar power law. A quadratic primitive-divisor theorem gives genuine fresh divisors for the period-four sequence beyond index 12, but no theorem assembles these packets into all rational primes or a Riemann determinant. Thus full-field scalarization is rejected while trace-field and ideal packets remain a precise open route.
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
  Cyclic Resultant Packets and the Norm Trilemma\
  for Hénon Monodromy
```

## Markdown 正文

# Introduction

The pressure-normalized instability roof of the certified H6 Hénon survivor has the dynamical prime-orbit law $\Pi(T)\sim e^T/T$. That counting law does not make the local orbit labels rational primes. The preceding scalar audit proves more: no common real power of the intrinsic multipliers can turn every primitive orbit into a rational prime. Any remaining arithmetic bridge must therefore carry several repetitions or several Galois conjugates at once.

Cyclic resultants are the first natural collective object. For a monic polynomial $f$, the sequence $$R_r(f)=\mathop{\mathrm{Res}}(f,X^r-1)$$ records the interaction of its roots with all $r$-th roots of unity. These sequences determine reciprocal polynomials under broad hypotheses and obey polynomial recurrences [@hillar2005cyclic; @hillar2004recurrences]. For a determinant-one return map with eigenvalues $\lambda,\lambda^{-1}$, the same sequence is generated directly by $1-\lambda^r$. It is not fitted to prime data.

This paper asks whether taking ideals or norms of that object repairs the failed scalar label. The answer has three parts.

1.  We prove that the cyclic determinant ideal and its full multiplier-field norm are exact squares. The same full-field square obstruction holds for every primitive cyclotomic norm after level two.

2.  We isolate the canonical trace-field half norm. It is an integer, can be prime, and retains nontrivial arithmetic information, but it depends on the repetition index and fails the one-label Euler power law in all three exact H6 controls.

3.  We retain the principal cyclotomic ideals as a source-native collective packet. A primitive-divisor theorem applies to the period-four quadratic sequence, but no available result assembles the varying H6 packets into an all-prime von Mangoldt trace.

The distinction between full and minimal norm is essential. The cyclic determinant already belongs to the fixed trace field. Taking its norm from the larger multiplier field counts the inversion pair twice and creates the square. Figure [\[fig:trilemma\]](#fig:trilemma){reference-type="ref" reference="fig:trilemma"} displays the three resulting lanes.

# Signed H6 monodromy and packet definitions

The map is $$H_6(q,p)=(1-6q^2-p,q),
\qquad
J(q)=\begin{pmatrix}-12q&-1\\1&0\end{pmatrix}.$$ Every chronological return matrix belongs to $SL_2$ over the corresponding periodic-point ring. If $M_\gamma$ is one such matrix, write $\lambda$ for its signed unstable eigenvalue. The other eigenvalue is $\lambda^{-1}$. The sign matters: the exact period-three trace is negative, so the actual unstable eigenvalue is $-L_3$, not its positive modulus $L_3$.

The three source-locked primitive examples have signed minimal polynomials $$\begin{aligned}
f_1(X)&=X^4-4X^3-22X^2-4X+1,\label{eq:f1}\\
f_3^-(X)&=X^4+76X^3-7374X^2+76X+1,\label{eq:f3}\\
f_4(X)&=X^2-578X+1.\label{eq:f4}\end{aligned}$$ They are monic reciprocal polynomials with constant term one. Hence their roots are algebraic units of norm one, and the substitution $\iota(\lambda)=\lambda^{-1}$ defines a nontrivial automorphism of $K=\mathbb Q(\lambda)$. Let $K^+=K^{\langle\iota\rangle}$ be its fixed trace field.

For $r,n\ge1$, define $$\mathfrak A_r=(1-\lambda^r),
\qquad
\mathfrak C_n=(\Phi_n(\lambda))$$ as principal ideals of $\mathcal O_K$. Define the cyclic determinant $$D_r=\det(I-M_\gamma^r)
=(1-\lambda^r)(1-\lambda^{-r})\in\mathcal O_{K^+}.$$ Whenever $(D_r)$ is compared with $\mathfrak A_r$, its principal ideal in $\mathcal O_{K^+}$ is extended to $\mathcal O_K$. The minimal rational cyclic norm is $$a_r=\left|\mathop{\mathrm{N}}_{K^+/\mathbb Q}(D_r)\right|.$$ For $n>2$, define $$\beta_n=\lambda^{-\varphi(n)/2}\Phi_n(\lambda),
\qquad
b_n=\left|\mathop{\mathrm{N}}_{K^+/\mathbb Q}(\beta_n)\right|.$$

Because $f_\lambda$ is monic, $$\label{eq:resultants}
a_r=\left|\mathop{\mathrm{Res}}(f_\lambda,X^r-1)\right|,
\qquad
\left|\mathop{\mathrm{N}}_{K/\mathbb Q}\Phi_n(\lambda)\right|
=\left|\mathop{\mathrm{Res}}(f_\lambda,\Phi_n)\right|.$$

# The norm trilemma

[\[lem:canonical\]]{#lem:canonical label="lem:canonical"} The ideals $\mathfrak A_r$ and $\mathfrak C_n$ do not depend on choosing $\lambda$ or $\lambda^{-1}$. Moreover, $$\label{eq:ideal-product}
\mathfrak A_r=\prod_{n\mid r}\mathfrak C_n.$$

The identity $1-\lambda^{-r}=-\lambda^{-r}(1-\lambda^r)$ shows that the two generators of $\mathfrak A_r$ are associates. For $n>1$, cyclotomic reciprocity gives $\Phi_n(X)=X^{\varphi(n)}\Phi_n(X^{-1})$, so inversion changes $\Phi_n(\lambda)$ by a unit. The same assertion for $n=1$ follows from $\Phi_1(\lambda^{-1})=-\lambda^{-1}\Phi_1(\lambda)$. Finally, $1-\lambda^r=-\prod_{n\mid r}\Phi_n(\lambda)$, which proves [\[eq:ideal-product\]](#eq:ideal-product){reference-type="eqref" reference="eq:ideal-product"} after passing to ideals.

[\[thm:square\]]{#thm:square label="thm:square"} For every $r\ge1$, $$\label{eq:det-square}
(D_r)=\mathfrak A_r^2,
\qquad
\left|\mathop{\mathrm{N}}_{K/\mathbb Q}(D_r)\right|=a_r^2.$$ where the ideal equality is in $\mathcal O_K$. For every $n>2$, $\beta_n\in\mathcal O_{K^+}$ and $$\label{eq:primitive-square}
\left|\mathop{\mathrm{N}}_{K/\mathbb Q}\Phi_n(\lambda)\right|=b_n^2.$$ In contrast, $a_r$ and $b_n$ themselves are not forced to be squares.

The eigenvalue formula gives $$D_r=-\lambda^{-r}(1-\lambda^r)^2.$$ The prefactor is a unit, proving the ideal identity. Since $D_r$ is fixed by $\iota$, it belongs to $K^+$. Norm transitivity gives $$\mathop{\mathrm{N}}_{K^+/\mathbb Q}(D_r)
=\mathop{\mathrm{N}}_{K/\mathbb Q}(1-\lambda^r),$$ while $[K:K^+]=2$ gives $\mathop{\mathrm{N}}_{K/\mathbb Q}(D_r)=\mathop{\mathrm{N}}_{K^+/\mathbb Q}(D_r)^2$. This proves [\[eq:det-square\]](#eq:det-square){reference-type="eqref" reference="eq:det-square"} and identifies the non-doubled norm $a_r$.

For $n>2$, $\varphi(n)$ is even. The factor $\lambda^{-\varphi(n)/2}$ is integral because $\lambda$ is a unit, so $\beta_n\in\mathcal O_K$. Cyclotomic reciprocity gives $$\iota(\beta_n)
=\lambda^{\varphi(n)/2}\Phi_n(\lambda^{-1})
=\lambda^{-\varphi(n)/2}\Phi_n(\lambda)=\beta_n.$$ Thus $\beta_n\in\mathcal O_{K^+}$. Since $\Phi_n(\lambda)=\lambda^{\varphi(n)/2}\beta_n$ and $\mathop{\mathrm{N}}_{K/\mathbb Q}(\lambda)=1$, taking norms proves [\[eq:primitive-square\]](#eq:primitive-square){reference-type="eqref" reference="eq:primitive-square"}.

[\[cor:obstruction\]]{#cor:obstruction label="cor:obstruction"} Neither $|\mathop{\mathrm{N}}_{K/\mathbb Q}(D_r)|$ nor $|\mathop{\mathrm{N}}_{K/\mathbb Q}\Phi_n(\lambda)|$ for $n>2$ can be a rational prime. This corollary does not reject $a_r$, $b_n$, or the ideals $\mathfrak C_n$.

The displayed full-field norms are nonzero integer squares. They are nonzero because $\lambda$ is not a root of unity. A nonzero integer square is not a rational prime. The final sentence follows because Theorem [\[thm:square\]](#thm:square){reference-type="ref" reference="thm:square"} does not force its square roots or underlying ideals to be trivial.

The three lanes are now mathematically distinct. Full-field norm promotion is stopped by Corollary [\[cor:obstruction\]](#cor:obstruction){reference-type="ref" reference="cor:obstruction"}. The trace-field sequence is a valid collective scalar sequence, but it supplies one integer per repetition index. The ideal packet retains the splitting and residue-degree data that both norm maps forget.

# Exact H6 certificate

The certificate evaluates [\[eq:resultants\]](#eq:resultants){reference-type="eqref" reference="eq:resultants"} for the three signed polynomials [\[eq:f1\]](#eq:f1){reference-type="eqref" reference="eq:f1"}--[\[eq:f4\]](#eq:f4){reference-type="eqref" reference="eq:f4"} and indices $1\le n\le12$. Every cyclic resultant equals the product of its primitive cyclotomic resultants. All 30 rows with $n>2$ satisfy [\[eq:primitive-square\]](#eq:primitive-square){reference-type="eqref" reference="eq:primitive-square"}. Table [\[tab:ledger\]](#tab:ledger){reference-type="ref" reference="tab:ledger"} shows selected rows.

The canonical core-certificate digest is

`3bb27b0da0d23743e65629f5293a6e3166a8a2fe09e9822cfced763a496a05e7`.

The half norms are not uniformly prime or composite. For period one, $b_3=19$ is prime but $b_4=24$ is composite. For the signed period-three orbit, $b_3=7451$ is prime; replacing the signed eigenvalue by its positive modulus mutates this value to $7299$. For period four, $b_6=577$ is prime. Across all 30 theorem rows, six half norms are prime.

Nor does the surviving cyclic sequence come from one fixed Euler label. The first two values are $$\begin{array}{c|rrr}
\text{primitive period}&1&3&4\\\hline
a_1&28&7220&576\\
a_2&336&54323280&334080
\end{array}$$ and $a_2\ne a_1^2$ in every column. This finite calculation does not reject all generalized determinant uses of $(a_r)$; it rejects the specific repair that would replace one primitive-orbit Euler label $q$ by $q^r$ at every repetition.

The theorem's range and assumptions are executable. At $n=2$, the three primitive norms $12$, $7524$, and $580$ are nonsquares. For the nonreciprocal polynomial $X^2-2X+2$, the primitive index-three resultant is $13$, also a nonsquare. These controls prevent the proof from silently dropping the even-totient or reciprocal-unit hypotheses.

# Primitive divisors: a positive boundary

Primitive-divisor theory explains why the surviving packet should not be discarded. Postnikova and Schinzel developed primitive divisors for $a^n-b^n$ over algebraic number fields [@postnikova1968primitive]. Flatters studies the Lehmer--Pierce sequence $$\Delta_r=\mathop{\mathrm{N}}_{K/\mathbb Q}(u^r-1)$$ for a positive unit in a real quadratic field [@flatters2007primitive]. For norm-one units, his Theorem 1.4 gives a primitive rational prime divisor for every term beyond the twelfth. Here a primitive divisor of $a_r$ means a rational prime dividing $a_r$ that divides no earlier nonzero $a_m$ with $1\le m<r$.

This theorem applies directly to the period-four multiplier $L_4=289+24\sqrt{145}$: it is positive, lies in the real quadratic field $\mathbb Q(\sqrt{145})$, and has norm one. Therefore the period-four sequence $a_r$ has a fresh rational prime divisor for every $r>12$. This is a genuine source-backed arithmetic advance. It says that new primes occur inside the collective packets; it does not say that $a_r$ itself is prime or that the packets enumerate all rational primes with von Mangoldt multiplicity.

The two quartic H6 multiplier fields are outside Flatters' exact quadratic scope. General algebraic primitive-divisor results motivate a prime-ideal analysis, but a usable H6 bridge would still have to control orbit-to-orbit variation, residue degrees, repeated factors, and the pressure clock. We do not import a theorem across those missing interfaces.

# Route-A evaluation and limitations

The collective packet candidate has exact local provenance but no global Riemann object. Its strict Route-A tuple is $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FORMAL}),$$ with overall status `ROUTE_A_EXPLORATORY`. The full-field rational-prime scalarization is separately `STOP_SCOPED_SQUARE_NORM`. The positive coordinate is the exact trace-field/ideal packet, including eventual primitive divisors for the period-four sequence.

The present paper does not construct an Euler product over all primitive H6 orbits, a trace-class transfer operator, analytic continuation, a functional equation, a Riemann--von Mangoldt law, or a quantum operator. Route B is therefore not authorized. An all-prime claim would require a new packet assembly theorem that keeps prime ideals, residue degrees, repetition indices, and signed H6 orbit weights on the same ledger.

# Conclusion

Cyclic resultants do not restore the failed one-rational-prime-per-orbit picture. Full multiplier-field norms are forced squares, while the minimal trace-field norm and principal ideals retain genuine arithmetic information only as repetition-indexed packets. The period-four sequence even contains eventual primitive rational divisors, so the collective lane is nonempty. The next natural problem is no longer to invent another scalar label. It is to decide whether prime-ideal packets from many primitive H6 orbits admit a single signed, pressure-compatible trace with controlled multiplicities.

# Reproducibility and disclosure {#reproducibility-and-disclosure .unnumbered}

The exact SymPy certificate, adversarial unit tests, generated table, source audit, and hash-locked dependencies accompany the paper. The computations use integer resultants and symbolic identities; decimal root approximations are unnecessary. An AI coding and writing assistant was used to help organize the derivation and implementation. Every formal claim is restated in the proof package and independently checked by exact tests where finite verification is possible.
