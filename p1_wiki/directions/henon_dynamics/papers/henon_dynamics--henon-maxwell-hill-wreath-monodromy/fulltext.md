---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-maxwell-hill-wreath-monodromy"
canonical_tex: "henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper/main.pdf"
source_sha256: "19e6bd998c0a700044d6913243733a1ff37b5159bf707059f4d40e36f0d4c3d7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Full Quadratic Wreath Monodromy from a Period-Five Hénon Maxwell--Hill Collision

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_maxwell_hill_wreath_monodromy>)
- [规范 TeX](<../../../../../henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_maxwell_hill_wreath_monodromy/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the complete quadratic arithmetic monodromy carried by an exact period-five equal-action collision in the area-preserving Hénon family. Earlier exact work produced a degree-nine collision field $K$, an $S_9$ splitting field $L$, and an intrinsic element $\beta\in K^\times$: the product of the chronological Hill determinants on the two branches of the collision. It left open whether the nine conjugate classes $[\beta_i]$ are independent in $L^\times/L^{\times2}$. We prove that they are. The decisive local certificate is a $19$-adic Newton edge of slope $-5/2$. It gives one valuation parity row of weight two; the full $S_9$-action propagates that row to every pair of coordinates. Thus a square relation can only be the product of all nine conjugates. Exact square classes of the rational norm and the discriminant differ by $3$, excluding this final relation through the unique sign quadratic subfield of an $S_9$-extension. Kummer theory then gives $$\operatorname{Gal}\bigl(L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})/\mathbb{Q}\bigr)
   \cong C_2^9\rtimes S_9=C_2\mathbin{\wr}S_9,$$ of order $185{,}794{,}560$. Standard Newton, Kummer, and wreath-product machinery is not claimed as new; the result is the explicit Hénon-specific maximality theorem. It remains fixed-period and supplies neither a dynamical zeta function nor a Hilbert--Pólya operator.
author:
- HCS Research Program
bibliography:
- references.bib
date: 12 August 2026
title: |
  Full Quadratic Wreath Monodromy from a\
  Period-Five Hénon Maxwell--Hill Collision
```

## Markdown 正文

# Introduction

A periodic orbit can carry arithmetic data that are invisible after its parameter or action coordinate has been eliminated. The HCS-C33 construction made this phenomenon exact for a period-five collision in an area-preserving Hénon family: two distinct chronological orbits have the same generating action, while the product of their two Hill determinants descends to a nontrivial square class over the collision field [@hcs2026c33note; @hcs2026c33certificate]. That theorem produced one quadratic extension. It did not decide what happens when all nine Galois conjugate collision parameters are placed in a common splitting field.

The missing question is a rank problem rather than another orbit search. Let $P_9$ be the degree-nine collision polynomial, let $K=\mathbb{Q}[A]/(P_9)$, and let $L$ be its splitting field. C33 proves $\operatorname{Gal}(L/\mathbb{Q})=S_9$. If $\beta\in K^\times$ is the symmetric two-branch Hill product and $\beta_1,\ldots,\beta_9$ are its conjugates in $L$, define $$V=\langle[\beta_1],\ldots,[\beta_9]\rangle
 \subset L^\times/L^{\times2}.$$ C33 proves only $V\ne0$. Hidden products of conjugates could still make $\dim_{\mathbb{F}_2}V$ any of several smaller values. Irreducibility of one degree-eighteen polynomial would not, by itself, exclude those products.

This note closes the rank problem at its maximal value.

[\[thm:intro-main\]]{#thm:intro-main label="thm:intro-main"} For the exact C33 period-five Maxwell--Hill object, $$\dim_{\mathbb{F}_2}\langle[\beta_1],\ldots,[\beta_9]\rangle=9.$$ Consequently, with $M=L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})$, $$\operatorname{Gal}(M/\mathbb{Q})\cong C_2\mathbin{\wr}S_9,
 \qquad |\operatorname{Gal}(M/\mathbb{Q})|=2^9 9!=185{,}794{,}560.$$

The proof has three short layers. First, a translation $A=1802+T$ exposes a lower $19$-adic Newton edge from $(0,5)$ to $(2,0)$. The two roots in that cluster both give odd, integer-normalized valuation $5$ to $\beta$; the other seven Hill values are units. This produces the parity vector $e_1+e_2$. Second, conjugation by $S_9$ produces every vector $e_i+e_j$, forcing a square relation to have all coordinates equal. Third, the all-ones relation would make the rational norm of $\beta$ a square in $L$. Its square-free class is $3\cdot13\cdot19\cdot41\cdot59$, whereas the sign quadratic subfield has class $13\cdot19\cdot41\cdot59$. Their quotient has class $3$, so the last relation is impossible.

The concrete contributions are therefore:

1.  an exact local weight-two parity certificate for the intrinsic Hénon Hill product;

2.  a proof that the resulting nine-dimensional Kummer module has no hidden relation in the common $S_9$ splitting field;

3.  an order-sharp upgrade of the standard quadratic wreath embedding to equality; and

4.  a reproducible exact certificate that separates these statements from all-period zeta and Hilbert--Pólya claims.

The result is a substantial finite arithmetic structure, but its scope is narrow. No prime is fitted to a Riemann-zero target: $19$ is forced by the exact norm/discriminant ledger and used only as a local proof place. No Euler product, analytic continuation, functional equation, critical-line law, or self-adjoint operator follows from the finite Galois group.

# The locked Maxwell--Hill object and the claim boundary

## Dynamical source

The foundational local manuscript studies the area-preserving recurrence $$x_{n+1}=1-Ax_n^2-x_{n-1},                                 \label{eq:recurrence}$$ equivalently the map $$H_A(q,p)=(1-Aq^2-p,q),                                    \label{eq:henon}$$ whose Jacobian determinant is one [@wang2026henonmodel]. That source motivates the Hénon direction through numerical spectral comparisons. We retain only the exact conservative recurrence. None of its numerical Riemann-zero fits, continuum approximations, or near-critical parameter claims is an assumption in the present theorem.

C33 applied the cyclic period-five generating action to [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}, isolated a transverse equal-action node of two exact period-five points, and descended the product of their chronological Hill determinants [@hcs2026c33note]. The resulting collision polynomial is $$\begin{aligned}
P_9(A)={}&110592A^9-294912A^8+159744A^7+225792A^6\notag\\
&-162816A^5-51520A^4+50672A^3+736A^2-6032A+1037. \label{eq:p9}\end{aligned}$$ It is irreducible, and C33 certifies $$\operatorname{Gal}(P_9/\mathbb{Q})=S_9.                                         \label{eq:s9}$$

Put $K=\mathbb{Q}[A]/(P_9)$. The two node branches have Hill values $h_1,h_2$ in a quadratic algebra over $K$. Their product $$\beta=N_H=h_1h_2=\frac{B_8(A)}{4827099043}\in K^\times    \label{eq:beta}$$ is fixed by branch exchange. A common Hill normalization $h_i\mapsto\mu(A)h_i$ multiplies $\beta$ by $\mu(A)^2$, so $[\beta]$ is intrinsic under the permitted gauge. The polynomial $B_8$ is recorded in Appendix [8](#app:ledgers){reference-type="ref" reference="app:ledgers"}. Exact resultant arithmetic gives $$N:=\operatorname{N}_{K/\mathbb{Q}}(\beta)
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.             \label{eq:norm}$$ C33 used the nonsquare rational norm to prove $\beta\notin K^{\times2}$, and explicitly left the all-conjugate rank and full wreath group unclaimed.

Let $\alpha_1,\ldots,\alpha_9$ be the roots of $P_9$ in its splitting field $L$, and write $\beta_i=\beta(\alpha_i)$. We study the relation kernel $$R=\left\{r\in\mathbb{F}_2^9:
       \prod_{i=1}^{9}\beta_i^{r_i}\in L^{\times2}\right\}. \label{eq:R}$$ The Kummer rank is $9-\dim R$.

## Two different meanings of monodromy

Arai constructs monodromies of loops in the complex Hénon hyperbolic horseshoe locus and studies their action on symbolic dynamics [@arai2007loops]. That is topological continuation in a complex parameter locus. Here "monodromy" means the arithmetic Galois group of the normal closure of a quadratic extension over the number field cut out by $P_9$. The base points, acting objects, and representations are different; the present result is not an extension of Arai's symbolic monodromy theorem.

For a tower $\mathbb{Q}\subset K\subset K(\sqrt\beta)$, embedding the Galois group of the normal closure in a permutation wreath product is standard. The quadratic and Kummer cases are made explicit, for example, by @barquero2023wreath [Theorem 1.11 and Corollary 1.14]. Newton polygons and valuation parity in square-class questions are likewise standard local number theory [@serre1979localfields]. We use these results without a novelty claim.

::: {#tab:boundary}
  ----------------------------------------------------------------------------------------------
  Object                    Prior or inherited input     Hénon-specific increment here
  ------------------------- ---------------------------- ---------------------------------------
  Conservative recurrence   foundational Paper-5 model   no new map claim

  Degree-nine action node   exact C33 theorem            source locked, not rederived

  One Hill square class     exact C33 theorem            upgraded to nine independent classes

  Newton/Kummer theory      standard                     exact $p=19$ parity row

  Wreath embedding          standard                     proof that the embedding is full

  Horseshoe monodromy       Arai's symbolic object       explicitly distinct arithmetic object
  ----------------------------------------------------------------------------------------------

  : Claim boundary. Novelty is restricted to maximality for the locked period-five Hénon Maxwell--Hill invariant.
:::

# The local weight-two parity certificate

The prime $19$ divides both the discriminant of $P_9$ and the norm in [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}. A repeated residue factor alone would be insufficient: the power-basis order may have nontrivial index at this prime. We therefore use the roots in $\overline{\mathbb{Q}}_{19}$ and the Newton polygon directly, without invoking Dedekind factorization.

Set $$c=-3+5\cdot19^2=1802,
 \qquad A=c+T.                                              \label{eq:shift}$$ Write $$P_9(c+T)=\sum_{i=0}^{9}a_iT^i,
 \qquad B_8(c+T)=\sum_{i=0}^{8}b_iT^i.$$ Exact integer division gives the data in Table [2](#tab:newton){reference-type="ref" reference="tab:newton"}. A unit residue means the residue after dividing the coefficient by the displayed power of $19$.

::: {#tab:newton}
   polynomial  valuations, low degree to high   unit residues modulo $19$
  ------------ -------------------------------- ------------------------------
   $P_9(c+T)$  $(5,3,0,0,0,0,0,0,0,0)$          $(18,6,5,6,13,7,15,12,5,12)$
   $B_8(c+T)$  $(3,0,0,0,0,0,0,0,0)$            $(18,6,10,13,14,11,9,8,9)$

  : Exact $19$-adic coefficient ledger at the translated collision cluster.
:::

[\[lem:cluster\]]{#lem:cluster label="lem:cluster"} The polynomial $P_9$ has a degree-two local factor whose two roots satisfy $v_{19}(T)=5/2$. Its splitting field is totally ramified of degree two. The other seven roots lie in unramified extensions and satisfy $v_{19}(T)=0$.

The lower Newton polygon has one negative-slope edge $$(0,5)\longrightarrow(2,0),\qquad \text{slope}=-\frac52.$$ Indeed, $(1,3)$ lies strictly above that segment; every subsequent coefficient is a unit. The edge has horizontal length two and slope denominator two. Its residual polynomial is $$18+5Y\in\mathbb{F}_{19}[Y],$$ which is linear and separable. The Newton polygon theorem therefore gives one degree-two, ramification-index-two cluster and two roots of valuation $5/2$ [@serre1979localfields].

For completeness, exact factorization of the residue polynomial is $$\begin{aligned}
 P_9(A)\equiv -7(A+3)^2
 &(A^2+A-7)\\
 &\cdot(A^5+3A^4+2A^3+A^2+4A-2)\pmod {19}.\end{aligned}$$ The quadratic and quintic factors are distinct and separable. Their roots therefore generate only unramified extensions. The local splitting field has ramification index two, contributed by the displayed Newton cluster, and the remaining Newton edge is horizontal.

We normalize the valuation $v$ on this local splitting field by $v(19)=2$. Thus the two cluster parameters satisfy $v(T)=5$.

[\[prop:odd-hill\]]{#prop:odd-hill label="prop:odd-hill"} After labelling the two cluster roots first, one valuation of $L$ above $19$ satisfies $$\bigl(v(\beta_1),\ldots,v(\beta_9)\bigr)\bmod2
   =(1,1,0,0,0,0,0,0,0).                                  \label{eq:parity}$$

For either cluster root, Table [2](#tab:newton){reference-type="ref" reference="tab:newton"} gives $$v(b_0)=6,\qquad v(b_1T)=5,\qquad v(b_iT^i)\ge10\quad(i\ge2).$$ The minimum is unique, so no cancellation is possible and $v(B_8(c+T))=5$. The denominator in [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"} satisfies $4827099043\equiv7\pmod {19}$, hence it is a unit. Both cluster values of $\beta$ therefore have valuation five.

It remains to rule out positive valuation at another root. Exact residue factorization gives $$B_8(A)\equiv9(A+1)(A+3)
 (A^6+4A^5-7A^4+A^3-4A^2-6A+6)\pmod {19},$$ and consequently $$\gcd(P_9,B_8)\bmod19=A+3.                                  \label{eq:gcd19}$$ Every noncluster root reduces to one of the other, coprime residue factors, so its $B_8$-value is a unit. The valuation row is exactly [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"}.

The translation by $5\cdot19^2$ is not a numerical fit. It separates the two-adic-depth structure of the repeated residue root sufficiently to exhibit the primitive edge $-5/2$. Every coefficient and residue in Table [2](#tab:newton){reference-type="ref" reference="tab:newton"} is reconstructed from [\[eq:p9\]](#eq:p9){reference-type="eqref" reference="eq:p9"} and Appendix [8](#app:ledgers){reference-type="ref" reference="app:ledgers"} by exact integer arithmetic.

# Eliminating every square relation

The local row becomes global because the collision parameters have the full permutation group. We record the elementary binary linear algebra so that the rank conclusion does not rest on a black-box module computation.

[\[lem:pair-annihilator\]]{#lem:pair-annihilator label="lem:pair-annihilator"} Let $W\subset\mathbb{F}_2^9$ be the span of the vectors $e_i+e_j$ with $i\ne j$. Then $W$ is the even-weight subspace, $\dim W=8$, and $$W^\perp=\langle\mathbf{1}\rangle,
 \qquad \mathbf{1}=(1,\ldots,1).$$

Every pair vector has even weight, so $W$ lies in the codimension-one even-weight subspace. The eight vectors $e_1+e_j$, $2\le j\le9$, are independent, proving equality and $\dim W=8$. A vector orthogonal to every $e_i+e_j$ satisfies $r_i+r_j=0$ for all pairs, hence all its coordinates agree.

[\[prop:one-relation\]]{#prop:one-relation label="prop:one-relation"} For the square-relation kernel $R$ in [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}, $$R\subseteq\{0,\mathbf{1}\}.$$

If $r\in R$, then the valuation of $\prod_i\beta_i^{r_i}$ is even at every discrete valuation of $L$. Applying Proposition [\[prop:odd-hill\]](#prop:odd-hill){reference-type="ref" reference="prop:odd-hill"} gives $r_1+r_2=0$. The subspace $R$ is invariant under $\operatorname{Gal}(L/\mathbb{Q})=S_9$. Conjugating both the valuation and its labels supplies $r_i+r_j=0$ for every unordered pair. Equivalently, $R\subseteq
W^\perp$, and Lemma [\[lem:pair-annihilator\]](#lem:pair-annihilator){reference-type="ref" reference="lem:pair-annihilator"} finishes the proof.

To exclude $\mathbf{1}$, we need one standard fact about symmetric splitting fields.

[\[lem:sign-field\]]{#lem:sign-field label="lem:sign-field"} Let $L/\mathbb{Q}$ be the splitting field of a separable polynomial $f$ with $\operatorname{Gal}(L/\mathbb{Q})=S_n$, $n\ge3$. For $c\in\mathbb{Q}^\times$, if $c\in L^{\times2}$, then either $c\in\mathbb{Q}^{\times2}$, or $\left[c\right]=\left[\operatorname{Disc}f\right]$ in $\mathbb{Q}^\times/\mathbb{Q}^{\times2}$.

If $c$ is not a rational square but becomes a square in $L$, then $\mathbb{Q}(\sqrt c)$ is a quadratic subfield of $L$. Quadratic subfields correspond to normal index-two subgroups of $S_n$. The unique such subgroup is $A_n$, because the abelianization of $S_n$ is $C_2$. Its fixed field is the sign field, generated by the alternating Vandermonde, and its square class is $\operatorname{Disc}f$. This argument depends only on the discriminant square class and therefore also applies to a nonmonic defining polynomial.

The exact discriminant factorization is $$D:=\operatorname{Disc}(P_9)
=2^{96}3^{12}13^3 19^5 41^3 59^5 9056471^2.                \label{eq:disc}$$ Combining [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"} and [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"} gives $$\begin{aligned}
 \left[N\right]_{\mathbb{Q}^\times/\mathbb{Q}^{\times2}}
   &=\left[3\cdot 13\cdot 19\cdot 41\cdot 59\right],              \label{eq:nclass}\\
 \left[D\right]_{\mathbb{Q}^\times/\mathbb{Q}^{\times2}}
   &=\left[13\cdot 19\cdot 41\cdot 59\right],                    \label{eq:dclass}\\
 \left[N/D\right]_{\mathbb{Q}^\times/\mathbb{Q}^{\times2}}&=\left[3\right].        \label{eq:ratio3}\end{aligned}$$ In particular, $N$ is neither a rational square nor in the sign-field class.

[\[thm:rank-nine\]]{#thm:rank-nine label="thm:rank-nine"} The nine conjugates $\beta_1,\ldots,\beta_9$ are linearly independent in $L^\times/L^{\times2}$. Equivalently, $R=0$.

Proposition [\[prop:one-relation\]](#prop:one-relation){reference-type="ref" reference="prop:one-relation"} leaves only $\mathbf{1}$. If $\mathbf{1}\in R$, then $$\prod_{i=1}^{9}\beta_i=\operatorname{N}_{K/\mathbb{Q}}(\beta)=N$$ would be a square in $L$. Lemma [\[lem:sign-field\]](#lem:sign-field){reference-type="ref" reference="lem:sign-field"} and [\[eq:nclass\]](#eq:nclass){reference-type="eqref" reference="eq:nclass"}--[\[eq:ratio3\]](#eq:ratio3){reference-type="eqref" reference="eq:ratio3"} rule this out. Hence $\mathbf{1}\notin R$, and $R=0$.

This proof uses one local row, not a class-group computation or a search over all $2^9$ possible products. The full $S_9$ symmetry is what turns a weight-two local observation into a rank-nine global theorem.

# Full wreath monodromy

Let $$M=L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9}).                 \label{eq:M}$$ Because the $S_9$-action permutes the $\beta_i$, this field is normal over $\mathbb{Q}$. It is the normal closure of the tower $\mathbb{Q}\subset K\subset K(\sqrt\beta)$: any normal extension containing $K(\sqrt\beta)$ contains every conjugate of $K$, hence $L$, and then every $\sqrt{\beta_i}$.

[\[thm:wreath\]]{#thm:wreath label="thm:wreath"} There are isomorphisms $$\operatorname{Gal}(M/L)\cong C_2^9,
 \qquad
 \operatorname{Gal}(M/\mathbb{Q})\cong C_2^9\rtimes S_9=C_2\mathbin{\wr}S_9.$$ In particular, $|\operatorname{Gal}(M/\mathbb{Q})|=185{,}794{,}560$.

Characteristic-zero Kummer theory identifies $\operatorname{Gal}(M/L)$ with the dual of the span of the square classes $[\beta_i]$. Theorem [\[thm:rank-nine\]](#thm:rank-nine){reference-type="ref" reference="thm:rank-nine"} therefore gives $\operatorname{Gal}(M/L)\cong C_2^9$.

Restriction to $L$ gives an exact sequence $$1\longrightarrow C_2^9
 \longrightarrow\operatorname{Gal}(M/\mathbb{Q})
 \longrightarrow S_9\longrightarrow1.                     \label{eq:exact}$$ The standard quadratic normal-closure theorem embeds the middle group into the imprimitive wreath product $C_2\mathbin{\wr}S_9$, acting on the signed set $\{\pm\sqrt{\beta_i}:1\le i\le9\}$ [@barquero2023wreath]. No splitting of [\[eq:exact\]](#eq:exact){reference-type="eqref" reference="eq:exact"} is assumed. The exact sequence gives $$|\operatorname{Gal}(M/\mathbb{Q})|=2^9 9!=|C_2\mathbin{\wr}S_9|.$$ An embedded subgroup with the full ambient order is the entire wreath product. Equality supplies the semidirect-product description afterward.

The associated norm polynomial is $$F_{18}(U)=\operatorname{N}_{K/\mathbb{Q}}(U^2-\beta)
          =\prod_{i=1}^{9}(U^2-\beta_i),                   \label{eq:f18}$$ up to primitive integral scaling. The full wreath group is transitive on its eighteen signed roots, so $F_{18}$ is irreducible over $\mathbb{Q}$. The released certificate also verifies this independently modulo $7$: Rabin's test has gcd degrees zero for the prime divisors $2,3$ of $18$, and the $7^{18}$-Frobenius remainder is zero. The primitive coefficient ledger appears in Appendix [8](#app:ledgers){reference-type="ref" reference="app:ledgers"}.

The signed set should not be misread as eighteen independent branchwise Hill classes. Each $\beta_i$ is already the exchange-invariant product of the two branch Hill determinants above one Maxwell node. The Kummer base has rank nine, not eighteen.

# Reproducibility, novelty, and the Route-A decision

## Exact certificate contract

The computational artifact separates production from verification. The producer reads the hash-locked C33 certificate and reconstructs the norm polynomial, rational norm, discriminant, Newton data, finite-field rows, and binary relation-module census. The checker imports no producer code. It reconstructs those objects from the locked $P_9$ and $B_8$ coefficient lists, enforces exact schema and types, and evaluates nine semantic gates: source identity, norm polynomial, rational square classes, local Newton row, permutation module, relation elimination, wreath order, and scope are all checked separately.

Five input files are frozen by SHA-256: the foundational Paper-5 PDF, the C33 JSON certificate, the C33 theorem package, and the independent C33 producer and checker. In particular, the inherited statements $\operatorname{Gal}(L/\mathbb{Q})=S_9$, [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}, and the dynamical meaning of $\beta$ cannot drift silently. The local note and machine artifact are cited separately because the former fixes semantic scope while the latter fixes exact coefficients [@hcs2026c33note; @hcs2026c33certificate].

From the C34 project directory, the core replay is

    python3 code/c34_producer.py --output /tmp/c34.json
    python3 code/c34_checker.py \
      --certificate /tmp/c34.json --output /tmp/c34-check.json
    C34_TEST_CERTIFICATE=/tmp/c34.json python3 code/test_c34.py

The test suite contains six regression tests, including byte determinism and a batch of twenty-seven adversarial mutations. Mutations alter source hashes, polynomial coefficients, Newton slopes and valuations, module ranks, group order, scope flags, and Route-A status. The checker distinguishes an expected mathematical rejection from an unexpected execution error.

The certificate is not presented as a formal proof assistant. Its role is to make the large integer arithmetic replayable and to prevent a weaker finite computation from being substituted for the argument. In particular:

-   irreducibility of $F_{18}$ modulo $7$ is an independent control, not the proof of rank nine;

-   the repeated factor modulo $19$ is not interpreted through an unchecked power-basis factorization;

-   the integer $19$ is a local proof place, not an arithmetic label assigned to a Hénon orbit; and

-   the $2^9$-case census checks the elementary module lemma but does not replace it.

## What the theorem adds

The general embedding $\operatorname{Gal}(M/\mathbb{Q})\hookrightarrow C_2\mathbin{\wr}S_9$ is standard prior art [@barquero2023wreath]. So are Newton polygons and the use of odd valuations to separate square classes. The Hénon-specific content is the simultaneous occurrence of the following exact facts for the locked Maxwell--Hill invariant: the slope $-5/2$, the unique Hill linear term on that cluster, the weight-two support, the full $S_9$ propagation, and the norm/sign-field class mismatch. Their conjunction makes the standard embedding sharp.

This arithmetic monodromy also remains distinct from symbolic continuation in the complex Hénon horseshoe locus [@arai2007loops]. No statement about loops in that locus, pruning automorphisms, or hyperbolic coding is used in Theorem [\[thm:wreath\]](#thm:wreath){reference-type="ref" reference="thm:wreath"}.

## Route-A evaluation

The Hilbert--Pólya motivation in the foundational manuscript asks for a spectral structure connected to the Riemann zeros [@wang2026henonmodel]. A maximal finite Galois group is not such a structure. The formal evaluation is shown in Table [3](#tab:route-a){reference-type="ref" reference="tab:route-a"}.

::: {#tab:route-a}
  gate   decision        reason
  ------ --------------- --------------------------------------------------------
  A1     `WEAK`          genuine chronological period-five Hénon invariant
  A2     `FAIL`          no all-period determinant or analytic continuation
  A3     `FAIL`          no prime law, zero law, or critical-line theorem
  A4     `FORMAL_HINT`   finite signed representation, no self-adjoint operator

  : Route-A assessment. The overall decision remains `ROUTE_A_REJECTED`; Route B is not invoked.
:::

An all-period advance would require compatible Maxwell divisors and Hill Kummer modules across infinitely many periods, together with a chronological trace or determinant law. The present computation gives no such tower and does not imply that one exists.

# Conclusion

The period-five Hénon action collision carries the largest quadratic arithmetic decoration allowed by its nine parameter conjugates. One exact $19$-adic cluster supplies odd Hill valuation on precisely two conjugates; $S_9$ symmetry expands that local row into all pair constraints; and a rational square-class comparison removes the sole surviving global relation. The resulting Kummer rank is nine, so the normal closure has the full signed permutation group $C_2\mathbin{\wr}S_9$.

The proof closes the specific large gate that C33 left open: one nonsquare Hill product has become a maximal all-conjugate module. It does not close the larger Hilbert--Pólya route. The next mathematically distinct gate is compatibility across periods, not a longer computation at period five. Any such continuation must preserve the genuine chronological Hill data and must produce an all-period trace object before spectral or arithmetic-zero claims become available.

# Exact coefficient ledgers {#app:ledgers}

The numerator in [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"}, written in descending degree, is $$\begin{aligned}
B_8(A)={}&-4397149235773440A^8+8210379350937600A^7\\
&+1123467639484416A^6-9885570146248192A^5\\
&-1438653142203648A^4+2906695726100864A^3\\
&+399558302240736A^2-299296418917388A\\
&-24722338005452.\end{aligned}$$ The denominator factors as $$4827099043=13\cdot41\cdot9056471.$$ The nonmonic norm formula used by the exact certificate is $$\operatorname{N}_{K/\mathbb{Q}}(\beta)
 =\frac{\operatorname{Res}(P_9,B_8)}
 {110592^8\,4827099043^9},$$ which reduces to [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}.

The primitive integral form of [\[eq:f18\]](#eq:f18){reference-type="eqref" reference="eq:f18"} is $$\begin{aligned}
F_{18}(U)={}&14348907U^{18}+24092228196U^{16}
 +42361338123648U^{14}\\
&-2093800403587605048U^{12}
 +16196898778074472140000U^{10}\\
&-40251914025500856031607696U^8\\
&+43433412093144215015946065712U^6\\
&-14526376288686830006975254862016U^4\\
&+13331315635008942100786892977536U^2\\
&-113947752632453884225287526761792.\end{aligned}$$ Only even powers occur, as required by the signed-root construction. Modulo $7$, this degree-eighteen polynomial is irreducible.

# Source-lock ledger

The C34 producer verifies the following SHA-256 digests before accepting the inherited object:

  ---------------------------------------------------------------------------------
  source                               SHA-256
  ------------------------------------ --------------------------------------------
  Paper-5 PDF

  `4c00614a70d0f5877d425c68d0c726b9`

  C33 certificate

  `b9edc4281d107fbd0889d79121e1fe7`

  C33 theorem package

  `10c6a79c13a757b6dd60fa8551710b4`

  C33 producer

  `ec387987622cb86b02e1489b75210437`

  C33 checker

  `ea63248c012a5903e31a3fae6e23ae4e`
  ---------------------------------------------------------------------------------

The full relative paths are stored in the JSON certificate. The Paper-5 source is the local manuscript cited as @wang2026henonmodel; the C33 semantic and computational sources are cited as @hcs2026c33note [@hcs2026c33certificate].

#### Scope of the exact computation.

All promoted identities are over $\mathbb{Q}$, finite quotient algebras over $\mathbb{Q}$, finite fields, or the exact Newton valuation ledger. The producer uses no floating-point root finder, Riemann-zero table, or prime-fitting objective. The finite primes $7$ and $19$ certify irreducibility and a local square-class row, respectively; they are not assigned to primitive Hénon orbits. The certificate concerns the nine symmetric two-branch products $\beta_i$, not eighteen independently normalized Hill values.
