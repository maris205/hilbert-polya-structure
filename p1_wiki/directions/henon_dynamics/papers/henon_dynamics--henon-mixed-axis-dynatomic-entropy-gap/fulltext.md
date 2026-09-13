---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mixed-axis-dynatomic-entropy-gap"
canonical_tex: "henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/paper/paper.pdf"
source_sha256: "6280d26bb47b3d1ca7865d4d94e707bee6e82903a37eb5b908fc35f20a0a1b64"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Formal Reflection-Dynatomic Entropy Gap for the Area-Preserving Hénon Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mixed_axis_dynatomic_entropy_gap/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct the odd-period mixed-axis reflection closures of the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$ as a univariate divisibility sequence. If $n=2m+1$, the vertex-to-edge closure polynomial is $F_n(X)=q_{m+1}(X)-q_m(X)$, where the coordinates satisfy the Hénon recurrence. We prove $$\deg F_n=2^{(n+1)/2},\qquad F_d\mid F_n\quad(d\mid n).$$ The associated formal Möbius dynatomic divisor has degree $$D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}
     =2^{(n+1)/2}+O(n2^{n/6}),$$ and hence formal entropy $(1/2)\log2$. This is strictly larger than the physical reflection entropy $(1/2)\log\varphi$ of the certified local H6 survivor. Exact factorization through period fifteen produces reduced irreducible primitive quotients of degrees $2,2,6,14,28,62,126,246$; the period-nine quotient is exactly the previously certified degree-$28$ trace-field coordinate factor. The all-period result is a formal divisor-degree theorem. Effectivity as a reduced minimal-period root divisor remains conditional on a new symmetry-line transversality theorem, and no Galois-height pressure follows from degree alone.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  A Formal Reflection-Dynatomic Entropy Gap\
  for the Area-Preserving Hénon Map
```

## Markdown 正文

# Introduction

A reversible map permits a periodic orbit to be reconstructed from a path between two symmetry lines. For the area-preserving Hénon map this turns an odd periodic-orbit system into one polynomial equation. The purpose of this paper is to understand the all-period algebra of those equations rather than to factor one more isolated closure.

The preceding physical calculation proved that primitive reflection cycles in a certified four-state H6 survivor have entropy $(1/2)\log\varphi$, exactly half the ambient symbolic entropy. Meanwhile, explicit period-seven and period-nine reflection closures had degrees $14$ and $28$. These observations suggest a different exponential scale, but a finite degree sequence alone cannot justify a primitive algebraic count.

We make the distinction exact. Our first theorem proves that every odd mixed-axis closure has degree $2^{(n+1)/2}$ and that the closures form a divisibility sequence. Our second theorem forms the associated *virtual* Möbius divisor and proves that its degree has entropy $(1/2)\log2$. Exact factorization through period fifteen then shows that the virtual subtraction is an actual reduced irreducible quotient in that range.

Dynatomic polynomials for one-variable maps are classical [@MortonSilverman1994]. Effectivity can be proved much more generally for nondegenerate morphisms of nonsingular projective varieties by graph--diagonal intersection theory [@Hutz2010]. We do not invoke that theorem: the polynomial Hénon automorphism has a birational projective extension, and our object is an additional symmetry-line slice. Symmetric Hénon periodic orbits have an established geometric literature [@YamaguchiTanikawa2005]; the degree, divisibility and entropy formulas below are derived directly from the frozen recurrence.

The distinction between formal and effective is the main claim firewall. The paper proves a new algebraic scale and isolates transversality as the next gate. It does not prove an all-period root census, Galois-height pressure, prime trace or operator theorem.

# Two reversors and one closure polynomial

Put $f(q)=1-6q^2$ and $$H(q,p)=(f(q)-p,q),\qquad R(q,p)=(p,q),\qquad J=RH.$$ Then $R^2=J^2=1$ and $RHR=H^{-1}$. Parameterize $\operatorname{Fix}(J)$ by $$\label{eq:start}
q_0=X,\qquad q_{-1}=q_1=\frac{1-6X^2}{2},$$ and continue with $$\label{eq:recurrence}
q_{j+1}=1-6q_j^2-q_{j-1}.$$

For odd $n=2m+1$, define $$\label{eq:closure}
F_n(X)=q_{m+1}(X)-q_m(X)\in\mathbb Q[X].$$

[\[prop:mixed\]]{#prop:mixed label="prop:mixed"} A root of $F_n$ gives a point in $\operatorname{Fix}(J)$ whose $(m+1)$st iterate lies in $\operatorname{Fix}(R)$, and therefore a periodic point of period dividing $n$. Conversely, an $n$-periodic point on $\operatorname{Fix}(J)$ satisfies [\[eq:closure\]](#eq:closure){reference-type="eqref" reference="eq:closure"}.

Let $z=(q_0,q_{-1})$. Equation [\[eq:start\]](#eq:start){reference-type="eqref" reference="eq:start"} is exactly $Jz=z$, while $F_n=0$ says $H^{m+1}z\in\operatorname{Fix}(R)$. Since $RH^k=H^{-k}R$ and $Rz=Hz$, the latter condition gives $H^{-m}z=H^{m+1}z$, hence $H^nz=z$. Reversing the argument proves the converse.

This is the vertex-to-edge, or mixed-axis, closure. It contains points of proper odd period and may carry intersection multiplicity; both are handled explicitly below.

# Degree and divisibility

[\[thm:degree\]]{#thm:degree label="thm:degree"} For every odd $n$, $$\label{eq:degree}
\deg F_n=2^{(n+1)/2}.$$

For $j\ge1$, induction in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} gives $\deg q_j=2^j$. Its leading coefficient is nonzero because the next one is $-6$ times its square. In [\[eq:closure\]](#eq:closure){reference-type="eqref" reference="eq:closure"}, $q_m$ has strictly smaller degree than $q_{m+1}$.

[\[thm:divisibility\]]{#thm:divisibility label="thm:divisibility"} If $d\mid n$ and $d,n$ are odd, then $$\label{eq:divisibility}
F_d\mid F_n\quad\text{in }\mathbb Q[X].$$

Write $d=2r+1$ and work in the quotient ring $\mathbb Q[X]/(F_d)$. The two boundary equalities are $$q_{-1}=q_1,\qquad q_r=q_{r+1}.$$ Because [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} determines the chain in both directions, the first equality reflects it about index $0$, the second about the half-index $r+1/2$, and their composition gives $$\label{eq:periodic-mod}
q_{j+d}=q_j\quad(j\in\mathbb Z).$$ Now $n/d$ is odd, say $n/d=2s+1$, and $(n-1)/2=sd+r$. Equation [\[eq:periodic-mod\]](#eq:periodic-mod){reference-type="eqref" reference="eq:periodic-mod"} therefore gives $q_{(n+1)/2}=q_{r+1}=q_r=q_{(n-1)/2}$ in the quotient ring. Thus the remainder of $F_n$ on division by $F_d$ is zero.

The quotient-ring proof is stronger than setwise containment of roots: it does not assume that $F_d$ is squarefree.

# The formal primitive divisor

Define the virtual zero-divisor $$\label{eq:formal-divisor}
\mathfrak D_n^{\mathrm{form}}
=\sum_{d\mid n}\mu(n/d)\,[F_d=0]$$ for odd $n$. This definition is unconditional in the divisor group; it does not assert that every coefficient is nonnegative.

[\[thm:formal\]]{#thm:formal label="thm:formal"} The degree of [\[eq:formal-divisor\]](#eq:formal-divisor){reference-type="eqref" reference="eq:formal-divisor"} is $$\label{eq:Dn}
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2},$$ and $$\label{eq:Dn-asymptotic}
D_n=2^{(n+1)/2}+O(n2^{n/6+1/2}).$$ In particular $D_n>0$ and $$\label{eq:formal-entropy}
\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}\frac1n\log D_n
=\frac12\log2.$$

Equation [\[eq:Dn\]](#eq:Dn){reference-type="eqref" reference="eq:Dn"} follows from Theorem [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}. Every proper divisor of an odd $n$ is at most $n/3$, and there are at most $n$ divisors, which proves [\[eq:Dn-asymptotic\]](#eq:Dn-asymptotic){reference-type="eqref" reference="eq:Dn-asymptotic"}. The leading term dominates for $n\ge11$ since $n2^{-n/3}<1$; direct substitution handles the smaller odd periods. Taking logarithms proves [\[eq:formal-entropy\]](#eq:formal-entropy){reference-type="eqref" reference="eq:formal-entropy"}.

The adjective *formal* is essential. A point of smaller minimal period can appear in a dynatomic divisor with positive excess multiplicity at a degeneracy. Standard dynatomic terminology makes precisely this distinction [@MortonSilverman1994; @Hutz2010].

# Exact reduced quotients through period fifteen

For each odd $n\le15$, exact division succeeds in $$\label{eq:Psi}
\Psi_n=F_n\bigg/\prod_{d\mid n,\ d<n}\Psi_d.$$ Table [1](#tab:factor){reference-type="ref" reference="tab:factor"} records the complete result.

::: {#tab:factor}
    $n$   $\deg F_n$   $\deg\Psi_n$   $D_n$  $F_n$ squarefree   $\Psi_n$ irreducible
  ----- ------------ -------------- ------- ------------------ ----------------------
      1            2              2       2        yes                  yes
      3            4              2       2        yes                  yes
      5            8              6       6        yes                  yes
      7           16             14      14        yes                  yes
      9           32             28      28        yes                  yes
     11           64             62      62        yes                  yes
     13          128            126     126        yes                  yes
     15          256            246     246        yes                  yes

  : Exact rational factorization and squarefreeness.
:::

Thus [\[eq:formal-divisor\]](#eq:formal-divisor){reference-type="eqref" reference="eq:formal-divisor"} is represented by one reduced irreducible polynomial at each audited period. The coefficient-list SHA-256 of $\Psi_9$ is

b0e55d474c54eba2a0bd8b8e742a11ebfae94380bf4c6c4d5253c7d89cbef9dd,

exactly the degree-$28$ mixed-axis coordinate factor used in the period-nine trace-field certificate. This is a coefficient identity, not merely a degree coincidence.

The table is a finite exact theorem and an adversarial test of the formal compiler. It is not evidence by extrapolation for all-period irreducibility or reducedness.

# The algebraic--physical entropy interface

Let $R_n^{\mathrm{phys}}$ be the primitive reversible-necklace count in the certified local H6 survivor. The predecessor theorem gives $$R_n^{\mathrm{phys}}=\Theta(\varphi^{n/2}).$$ Combining it with Theorem [\[thm:formal\]](#thm:formal){reference-type="ref" reference="thm:formal"} yields the strict formal gap $$\label{eq:gap}
h_{\mathrm{alg}}^{\mathrm{form}}-h_{\mathrm{refl}}^{\mathrm{phys}}
=\frac12\log\frac{2}{\varphi}>0.$$

Equation [\[eq:gap\]](#eq:gap){reference-type="eqref" reference="eq:gap"} identifies a genuine exponential reservoir missing from a reflection-only physical pressure. It does not yet provide the required compensating weight. The two populations have different scopes: $R_n^{\mathrm{phys}}$ counts necklaces in one certified local survivor, whereas $F_n$ records every ambient algebraic intersection of the two symmetry lines, including roots outside that survivor and complex roots.

Therefore no termwise Galois compiler follows from the entropy comparison. A valid bridge must prove effectivity, identify which primitive roots lie in the physical survivor, organize the remaining roots into trace fields, and control their instability heights. Degree alone supplies none of the last three steps.

# Why effectivity remains a theorem, not a convention

For a morphism of a nonsingular projective variety, dynatomic effectivity can be formulated through graph--diagonal intersection multiplicities and proved under nondegeneracy hypotheses [@Hutz2010]. The present object is not a direct instance of that statement. The polynomial Hénon automorphism of the affine plane extends birationally, rather than morphically, to the projective plane, and $F_n$ is a further intersection with $\operatorname{Fix}(J)$ followed by a mixed-axis condition.

The exact missing statement is concrete.

> For every odd $n$, the intersection $\operatorname{Fix}(J)\cap H^{-(n+1)/2}\operatorname{Fix}(R)$ is transverse after lower minimal periods are removed, or its local intersection multiplicities have nonnegative Möbius transform.

A repeated root of $F_n$ is the natural finite falsifier. Differentiating the symmetry-line shooting equation should translate it into tangency of the two lines, equivalently a constrained monodromy degeneracy. The certified local hyperbolicity may exclude that degeneracy for survivor roots, but it cannot silently certify ambient algebraic roots. This monodromy/tangency theorem is the next minimal project.

Even after effectivity, a Galois-height pressure would remain separate: it must weight all embeddings and prove a uniform asymptotic, not simply count them.

# Reproducibility and hostile controls

The primary checker locks seven predecessor artifacts, generates all odd closures through period fifteen, computes every divisor remainder, constructs the quotient chain, runs squarefree gcds and exact rational factorizations, and rejects twenty claim mutations. A second implementation imports no primary research code and reconstructs the recurrence, quotient degrees and coefficient hashes. Eight unit tests lock the degree sequence, P58 match, formal/effective boundary and Route-A/Route-B scope. Run

    bash code/run_c60.sh

from the project directory. Exact factorization of the degree-$246$ quotient is the slow step. No floating-point root, prime table or Riemann-zero data is used.

# Conclusion

The odd mixed-axis H6 closures are not a disconnected list of high-degree polynomials. They form an exact divisibility sequence whose virtual primitive divisor has entropy $(1/2)\log2$. This strictly exceeds the physical local-survivor reflection entropy, while exact quotients through period fifteen show that the formal construction is nonvacuous.

The advance is deliberately bounded. Formal degree is not effective root count, ambient algebraic roots are not local symbolic necklaces, and degree is not Galois height. The next bridge is now one sharp theorem: symmetry-line transversality and effectivity, preferably expressed through the chronological monodromy.

# Exact certificate ledger

The primitive quotient coefficient hashes are:

    $n$ $\deg\Psi_n$   SHA-256
  ----- -------------- ---------------------
      1 2              1059cb82bad4fb30...
      3 2              49db94e74c3bf30a...
      5 6              f5fc5a650ff7a6dd...
      7 14             346b1ceca90c7f03...
      9 28             b0e55d474c54eba2...
     11 62             0aceb09f176f6695...
     13 126            4ecd46c06e092d98...
     15 246            66b36bfe8778ca6a...

The full hashes are stored in `results/c60_certificate.json`; abbreviated rows here are not independent proof inputs. The canonical core digest is

27b530feb63bf02408acaeff6a9b0ebd737b98e865a4b10852fa87e3ec41431a.

The independent result digest is

06eddc3a27aad028b813be1c91e21b1b96b7bd286d1512c086cabc59e04bbc41.
