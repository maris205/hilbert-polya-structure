---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c430-native-galois-fields"
canonical_tex: "henon_dynamics/research_c429_c433/papers/C430_native_galois_fields/main.tex"
canonical_pdf: "henon_dynamics/research_c429_c433/papers/C430_native_galois_fields/main.pdf"
source_sha256: "64726ac4156c5f58f7012373b0e00497bf36ea3465c7f664d46292749ca39669"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Native Galois fields of small wild cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c429_c433/papers/C430_native_galois_fields>)
- [规范 TeX](<../../../../../henon_dynamics/research_c429_c433/papers/C430_native_galois_fields/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c429_c433/papers/C430_native_galois_fields/main.pdf>)
- [BibTeX](<../../../../../henon_dynamics/research_c429_c433/papers/C430_native_galois_fields/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every odd prime $p$, we determine the Galois action on all canonical small cycles of $P(z)=(1+s)z+z^2$ over $K=\overline{\mathbb F}_p((s))$. The degree-$p^e$ small factor is irreducible for every $e\ge1$; each root generates a totally ramified cyclic splitting field of degree $p^e$, whose distinguished generator is one application of $P$. The common root valuation has denominator only $p$, so it does not establish this degree. We instead prove an exact second-layer contact formula and transfer the native action through a canonical matching of the top clusters. The degree-$p$ Artin--Schreier classes, oriented by translation by $+1$, agree at every level $e\ge2$, whereas the prime-period field intersects every later field trivially over $K$. We compute the common first quotient break $2(p-1)$ and the two upper breaks $2(p-1),2p(p-1)$ of the second-layer field. Finally, using the independently proved compact adding-machine limit of the cycles, we obtain exact eventual agreement of every fixed finite native Galois quotient and a canonical $\mathbb Z_p$-extension. This last tower consists of stabilized quotient fields, not the original sequence of full periodic-point fields.
author:
- Anonymous
bibliography:
- references.bib
title: Native Galois fields of small wild cycles
```

## Markdown 正文

# Introduction

A unique geometric periodic cycle need not be one Galois orbit over the coefficient field. This distinction is particularly pronounced for wild cycles: a single cycle of length $p^e$ permits a proper Galois subgroup of its native rotation group, even when every point has nonintegral valuation. We study this distinction for the marked quadratic multiplier deformation $$k=\overline{\mathbb F_p},\qquad R=k[[s]],\qquad K=k((s)),\qquad
 P(z)=(1+s)z+z^2,$$ where $p$ is an odd prime and $v(s)=1$. All algebraic fields below lie in one fixed separable closure $K^\mathrm{sep}$. The word *native* means that the distinguished action is one application of $P$.

For $e\ge1$, put $$\label{eq:quotient}
 Q_e(z)=
 \frac{P^{\circ p^e}(z)-z}{P^{\circ p^{e-1}}(z)-z}.$$ Here and throughout, the superscript $\circ$ denotes composition. The canonical small factor $M_e\in R[z]$ is the monic degree-$p^e$ Hensel factor of $Q_e$ reducing to $z^{p^e}$. Its roots, denoted $S_e$, form the unique ordinary $p^e$-cycle in the open unit disk. These geometric facts follow from the optimal-cycle theorem of Lindahl--Rivera-Letelier [@lindahl2016optimal Theorem C and Proposition 4.4]; we give the precise factor interface in Section [2](#sec:setup){reference-type="ref" reference="sec:setup"}.

[\[thm:main\]]{#thm:main label="thm:main"} For every odd prime $p$ and every $e\ge1$, $M_e$ is irreducible over $K$. For any $\alpha_e\in S_e$, the field $L_e=K(\alpha_e)=K(S_e)$ is totally ramified cyclic of degree $p^e$. It has a distinguished generator $\sigma_e(\alpha_e)=P(\alpha_e)$.

Let $F_e$ be the unique degree-$p$ subfield of $L_e$. Choose $y_e\in F_e$ with $\sigma_e(y_e)-y_e=1$, and set $a_e=y_e^p-y_e\in K$. Then, for every $e\ge2$, $$\label{eq:main-class}
 [a_e]=[a_2]\ \text{in }K/\wp(K),\qquad
 F_e=F_2,\qquad L_1\cap L_e=K,
 \quad \wp(b)=b^p-b.$$ The equalities concern oriented classes and embedded fields.

The choice of $y_e$ does not affect its class, once the translation by $+1$ is fixed. Section [5](#sec:as){reference-type="ref" reference="sec:as"} supplies a trace resolvent with exactly this convention. Equality in [\[eq:main-class\]](#eq:main-class){reference-type="eqref" reference="eq:main-class"} does not assert equality of its raw Laurent-series representatives.

[\[thm:ramification\]]{#thm:ramification label="thm:ramification"} The unique break of $L_1/K$ is $p-1$. For every $e\ge2$, the unique break of $F_e/K$ is $2(p-1)$. The upper and lower breaks of $L_2/K$ are respectively $$(u_1,u_2)=\bigl(2(p-1),\,2p(p-1)\bigr),\qquad
 (b_1,b_2)=\bigl(2(p-1),\,2(p-1)(p^2-p+1)\bigr).$$ The field different exponent, measured by $v_{L_2}=p^2v$, is $$\label{eq:main-different}
 d_{L_2/K}=(p-1)(2p^3-2p^2+3p-1).$$

The degree proof has two distinct steps. First, the contact with the prime-period cycle has exact denominator $p^2$: $$v(\alpha_e-\beta_1)=\frac{2(p-1)^2}{p^2}
 \qquad(e\ge2).$$ A compositum ramification argument forces degree at least $p^2$. This contact does not acquire denominator $p^e$ at higher levels. Instead, the multiplier of the level-two cycle gives a cross-level contact deeper than the separation of the $p$ top clusters. The resulting canonical matching transfers a nontrivial native quotient action and forces the entire cyclic Galois group. Its native equivariance also proves the oriented class equality. For the precise ramification invariants, we use a controlled cancellation in $L_2L_1$, where the relevant element has valuation divisible by $p$, rather than applying a prime-to-$p$ leading-term rule outside its hypotheses.

## Eventual quotients and their additional dependency {#eventual-quotients-and-their-additional-dependency .unnumbered}

Write $\rho_e:G_K\to\mathbb Z/p^e\mathbb Z$ for the native rotation character, where $G_K=\mathop{\mathrm{Gal}}(K^\mathrm{sep}/K)$. A separate consequence, proved in Section [7](#sec:tower){reference-type="ref" reference="sec:tower"}, is the following.

[\[thm:tower\]]{#thm:tower label="thm:tower"} For every odd prime $p$, there is a unique continuous surjection $\chi_\infty:G_K\to\mathbb Z_p$ such that $$\label{eq:eventual-intro}
 \forall j\ge1\ \exists E_j\ge j\ \forall e\ge E_j\ \forall g\in G_K:
 \quad \rho_e(g)\bmod p^j=\chi_\infty(g)\bmod p^j.$$ The fields $$K_j=(K^\mathrm{sep})^{\ker(\chi_\infty\bmod p^j)}$$ are nested cyclic degree-$p^j$ extensions of $K$. For $e\ge E_j$, $K_j$ is the unique degree-$p^j$ subfield of $L_e$. Their union has Galois group $\mathbb Z_p$ over $K$.

Only Theorem [\[thm:tower\]](#thm:tower){reference-type="ref" reference="thm:tower"} uses the compact adding-machine limit proved in the unpublished companion [@companion2026haar Theorem 1.1]. We state its exact compactness, full-sequence Hausdorff convergence and native conjugacy interface before using it. That theorem is proved independently of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}; conversely, the proofs of Theorems [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} and [\[thm:ramification\]](#thm:ramification){reference-type="ref" reference="thm:ramification"} use no compact-limit input. In particular, [\[eq:eventual-intro\]](#eq:eventual-intro){reference-type="eqref" reference="eq:eventual-intro"} implies neither $E_j=j$ nor $K_j=L_j$, and it does not make the original $L_e$ a nested sequence.

## Relation to earlier work {#relation-to-earlier-work .unnumbered}

Lindahl--Rivera-Letelier own the existence, uniqueness and optimal radius of the small quadratic cycles [@lindahl2016optimal]. The common valuation is $(p-1)/p$, with denominator only $p$, independently of $e$. It therefore does not by itself prove degree $p^e$ over $K$. The arithmetic step here is the uniform second-layer obstruction and the cross-level cluster transfer.

Keating's study of periodic-point fields [@keating2006extensions Theorem 6.1] is a close antecedent: its proof uses commuting Galois actions and a full valuation denominator to establish the degree of a periodic-point extension. Its hypotheses include a finite extension of $\mathbb Q_p$, $p>3$, a ramification bound and a tame base change. His equal-characteristic Proposition 5.1 is also relevant, but compares already cyclic extensions by an isomorphism that may induce a nontrivial automorphism of the base. Neither formulation is an equality of our prescribed characters over the unchanged $k((s))$.

Compatible tower construction through norm fields is also classical; Keating's equivalence [@keating2009wintenberger Theorem 1.1 and Section 3] allows the base field to vary and works with finite residue field. The distinction in Theorem [\[thm:tower\]](#thm:tower){reference-type="ref" reference="thm:tower"} is eventual equality for every fixed quotient of the *prescribed* cycle sequence. The extraction of Galois characters from dynamical torsors has further antecedents; for instance, Debaisieux [@debaisieux2026lubin Propositions 2.1--2.3] uses consistent root sequences for a mixed-characteristic commuting pair. We do not claim the general torsor-to-character step as new. Artin--Schreier theory, ramification filtrations and their quotient compatibility are classical throughout [@elder2025artin].

Our conclusions are local at a fixed multiplier parameter. They do not classify global dynatomic components, compute every higher Witt coordinate, or determine all intersections of full higher periodic-point fields. The comparison with earlier work is bounded to the cited results and makes no universal priority claim.

# Canonical factors and local ramification tools {#sec:setup}

Fix an odd prime $p$, and retain $R,K,P$ from the introduction. The valuation $v$ extends uniquely to an algebraic closure of the complete field $K$. Write $r=(p-1)/p$.

[\[lem:small\]]{#lem:small label="lem:small"} For each $e\ge1$, there is a unique coprime Hensel factorization $$Q_e=M_eV_e,\qquad \overline M_e=z^{p^e},\qquad
 \overline V_e(0)\ne0,$$ with both factors monic in $R[z]$. The roots $S_e\subset K^\mathrm{sep}$ of $M_e$ are $p^e$ distinct points, form one ordinary native $p^e$-cycle, and all have valuation $r$. If $v(x)>0$, then $v(V_e(x))=0$.

We specify the geometric input from [@lindahl2016optimal Theorem C, its $q=1$ case, and Proposition 4.4]. For $g(z)=z+z^2$ in odd characteristic it gives $$\mathop{\mathrm{ord}}_z(g^{\circ p^j}(z)-z)
 =1+\frac{p^{j+1}-1}{p-1}\qquad(j\ge0),$$ and for $P$ it gives the unique cycle of $p^e$ distinct points in the open unit disk, with ordinary least period $p^e$. It applies after passing to a complete algebraic closure; the roots below are already separable algebraic over $K$.

For any polynomial $h$, $h(z)-z$ divides $h^{\circ p}(z)-z$: in the quotient by $h(z)-z$, every iterate of $h$ equals $z$. Monic division over $R$ thus proves $Q_e\in R[z]$. Reducing and subtracting the two displayed orders gives $\overline Q_e=z^{p^e}\overline V_e$, where $\overline V_e(0)\ne0$. Coprime Hensel factorization gives the unique factors. Their coefficients are integral, so $V_e$ evaluates to a unit at every point of positive valuation. Every point of the cited cycle is therefore a root of $M_e$; there are exactly $\deg M_e=p^e$ such distinct points. This proves both separability and identification of its roots.

For completeness, their common valuation can be recovered from the factor. On points of positive valuation, $P(x)=x(1+s+x)$ has the same valuation as $x$. Since the roots form one cycle, their valuations coincide. Differentiating the numerator and denominator of [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"} at the common root $0$, or cancelling their simple factors $z$, gives $$Q_e(0)=
 \frac{(1+s)^{p^e}-1}{(1+s)^{p^{e-1}}-1}
 =s^{p^e-p^{e-1}}.$$ The denominator is nonzero. Since $V_e(0)$ is a unit, the product of all $p^e$ roots has valuation $p^e-p^{e-1}$. Their common valuation is $r$.

[\[lem:rotation\]]{#lem:rotation label="lem:rotation"} For $\alpha\in S_e$, $K(\alpha)$ is the splitting field of $M_e$, with Galois group a subgroup $H_e\le\mathbb Z/p^e\mathbb Z$ of native rotations. Its degree is $p^{h_e}$, where $1\le h_e\le e$, and it is totally ramified. If $h_e<e$, every nonidentity automorphism has native rotation index divisible by $p$. At $e=1$ the degree is $p$.

Every root is an iterate of $\alpha$, so lies in $K(\alpha)$. The factor is separable by Lemma [\[lem:small\]](#lem:small){reference-type="ref" reference="lem:small"}, hence this root field is Galois. Galois commutes with $P$. A permutation commuting with a single cycle is determined by the image of one point and is a rotation of that cycle. Thus the splitting group is a subgroup of the cyclic group of order $p^e$. The valuation $v(\alpha)=r$ forces its ramification degree, and hence its degree, to be divisible by $p$. Every finite extension of $K$ has trivial residue extension because $k$ is algebraically closed; the degree--ramification identity for complete discretely valued fields makes it totally ramified. A proper subgroup of $\mathbb Z/p^e\mathbb Z$ lies in $p\mathbb Z/p^e\mathbb Z$. At $e=1$ the lower and upper degree bounds agree.

[\[lem:displacement\]]{#lem:displacement label="lem:displacement"} For points $x,y$ with $v(x),v(y)\ge r$, the map $P$ is an isometry and, for $a\ge0$ and $x\ne y$, $$\label{eq:isometry}
 \frac{P^{\circ a}(x)-P^{\circ a}(y)}{x-y}
 \in 1+\{u:v(u)\ge r\}.$$ For $x\in S_e$, a step of index prime to $p$ has displacement valuation $2r$; every step of index divisible by $p$ has displacement valuation at least $3r$, with $v(0)=+\infty$.

The disk $v(z)\ge r$ is $P$-invariant, and $$P(x)-P(y)=(x-y)(1+s+x+y).$$ The second factor belongs to the set in [\[eq:isometry\]](#eq:isometry){reference-type="eqref" reference="eq:isometry"}; products of such factors remain in that set. This proves the first assertion by iteration. For $x\in S_e$, $$v(P(x)-x)=v(sx+x^2)=2r$$ because $1+r>2r$. In the telescoping sum of $a$ one-step displacements, each summand divided by the first has residue $1$, by [\[eq:isometry\]](#eq:isometry){reference-type="eqref" reference="eq:isometry"}. If $p\nmid a$, their sum has nonzero residue $a$, giving valuation $2r$. For $a=p$, the residues cancel in characteristic $p$, and every remaining term gains at least $r$. Thus the $p$-step displacement has valuation at least $3r$. Telescoping in blocks of $p$ proves the last assertion.

We use lower and upper ramification groups $G_t,G^u$ with the following convention. For a totally ramified finite Galois extension $D/K$, put $v_D=[D:K]v$, and for $g\ne1$ set $$\ell_D(g)=v_D(g\pi-\pi)-1,
 \qquad
 \psi_D(u)=\int_0^u[G:G^t]\,dt ,$$ where $\pi$ is a uniformizer and $G=\mathop{\mathrm{Gal}}(D/K)$. The first lower and upper breaks coincide. Upper numbering commutes with Galois quotients. Abelian upper breaks are integral; in a cyclic degree-$p^2$ extension, $$\label{eq:herbrand-two}
 b_2-b_1=p(u_2-u_1),\qquad u_2\ge p u_1.$$ A nontrivial degree-$p$ character over $K$ has a reduced Artin--Schreier polar representative whose largest pole is prime to $p$ and equals its break. These classical facts hold for the arbitrary perfect residue field $k$, not just finite residue fields [@elder2025artin Section 2].

[\[lem:prime-value\]]{#lem:prime-value label="lem:prime-value"} Let $D/K$ be a finite totally ramified Galois $p$-extension. If $x\in D$, $a=v_D(x)>0$, and $p\nmid a$, then for every $g\ne1$, $$\label{eq:prime-value}
 v_D(gx-x)=a+\ell_D(g).$$

The given coefficient field $k$ is fixed by $g$, and $\mathcal O_D=k[[\pi]]$. The leading multiplier of $g\pi$ is a $p$-power root of unity in $k^\times$, hence equals $1$. Write $g\pi=\pi(1+u)$, with $v_D(u)=b=\ell_D(g)\ge1$. For each positive integer $j$, characteristic $p$ binomial expansion gives $$\label{eq:monomial-displacement}
 v_D(g(\pi^j)-\pi^j)=j+p^{v_p(j)}b.$$ Indeed, writing $j=p^qj_0$, $p\nmid j_0$, reduces the bracket to $(1+u^{p^q})^{j_0}-1$, whose linear term is nonzero. In $x=c_a\pi^a+\sum_{j>a}c_j\pi^j$, the leading term has displacement order $a+b$, whereas every later term has order at least $j+b>a+b$. These orders tend to infinity, so the complete tail cannot cancel the leading term.

Applying this lemma to $L_1/K$, with $v_{L_1}(\alpha_1)=p-1$, and using Lemma [\[lem:displacement\]](#lem:displacement){reference-type="ref" reference="lem:displacement"}, proves that its unique break is $2(p-1)-(p-1)=p-1$. More generally, [\[eq:prime-value\]](#eq:prime-value){reference-type="eqref" reference="eq:prime-value"} computes the first break of $D/K$ as the minimum nonidentity $x$-displacement minus $v_D(x)$. Any nontrivial Galois quotient has first upper break at least this value, by upper quotient compatibility.

# Exact interlevel contact and the second-layer degree {#sec:second}

The first comparison supplies degree $p^2$ uniformly, without an Artin--Schreier coefficient calculation.

[\[prop:second\]]{#prop:second label="prop:second"} For every $e\ge2$, $\alpha\in S_e$, and $\beta\in S_1$, $$\label{eq:exact-contact}
 v(\alpha-\beta)=d_0:=\frac{2(p-1)^2}{p^2}.$$ Moreover, $$\label{eq:pstep}
 [K(\alpha):K]\ge p^2,\qquad
 v(P^{\circ p}(\alpha)-\alpha)=2(p-1).$$ In particular, $M_2$ is irreducible of degree $p^2$.

The exact first factorization is $$\label{eq:first-factor}
 P^{\circ p}(z)-z=z(z+s)M_1(z)V_1(z).$$ Put $\mu=(P^{\circ p})'(\beta)$. Differentiating at $\beta$ gives $$\mu-1=\beta(\beta+s)M_1'(\beta)V_1(\beta).$$ The first two factors have valuation $r$, the last is a unit, and each of the $p-1$ root differences in $M_1'(\beta)$ has valuation $2r$. Hence $$\label{eq:first-multiplier}
 v(\mu-1)=2r+(p-1)2r=2(p-1)<+\infty .$$

For $e\ge2$, both return polynomials defining $Q_e$ vanish at $\beta$. Differentiate their polynomial quotient identity before evaluation. By the chain rule and [\[eq:first-multiplier\]](#eq:first-multiplier){reference-type="eqref" reference="eq:first-multiplier"}, the derivative of the denominator is nonzero, and $$Q_e(\beta)=
 \frac{\mu^{p^{e-1}}-1}{\mu^{p^{e-2}}-1}
 =(\mu-1)^{(p-1)p^{e-2}} .$$ This is not substitution into an undefined $0/0$ expression. Since $V_e(\beta)$ is a unit, it follows that $$\label{eq:first-average}
 \sum_{\alpha'\in S_e}v(\beta-\alpha')
 =2(p-1)^2p^{e-2}.$$ All contacts are finite, because the ordinary periods differ. Any two level-$e$ points differ by a sum of one-step displacements and thus have difference valuation at least $2r$. The average in [\[eq:first-average\]](#eq:first-average){reference-type="eqref" reference="eq:first-average"} is $d_0<2r$. Some contact is therefore below $2r$; the unequal-valuation triangle rule forces every contact to equal that one. Their average is $d_0$, proving [\[eq:exact-contact\]](#eq:exact-contact){reference-type="eqref" reference="eq:exact-contact"}.

Write $L=K(\alpha)$, $F=K(\beta)=L_1$, and $B=LF$. By Lemma [\[lem:rotation\]](#lem:rotation){reference-type="ref" reference="lem:rotation"}, $[L:K]=p^h$, $1\le h\le e$. Suppose $h=1$. Since $p$ is odd, $d_0$ has exact denominator $p^2$. The element $\eta=\alpha-\beta\in B$ therefore forces $[B:K]\ge p^2$; the opposite inequality follows from the two degrees. Thus $L\cap F=K$, $\mathop{\mathrm{Gal}}(B/K)\simeq C_p\times C_p$, and $v_B=p^2v$. Because $h<e$, each nontrivial automorphism of $L/K$ has a rotation index divisible by $p$, so moves $\alpha$ with valuation at least $3r$. Every nontrivial automorphism of $F/K$ moves $\beta$ with valuation $2r$. The restrictions can be chosen independently in the direct product. Hence the minimum nonidentity displacement of $\eta$ has base valuation exactly $2r$.

But $v_B(\eta)=2(p-1)^2$ is positive and prime to $p$. Lemma [\[lem:prime-value\]](#lem:prime-value){reference-type="ref" reference="lem:prime-value"} makes the first break of $B/K$ $$p^2(2r-d_0)=2(p-1).$$ Its quotient $F/K$ has break $p-1$, contradicting upper quotient compatibility. Consequently $h\ge2$. At $e=2$, the orbit size also bounds the degree by $p^2$, so equality and irreducibility follow. Finally evaluate [\[eq:first-factor\]](#eq:first-factor){reference-type="eqref" reference="eq:first-factor"} at $\alpha$. Both initial factors have valuation $r$, the complementary factor is a unit, and all $p$ contacts equal $d_0$. Thus $$v(P^{\circ p}(\alpha)-\alpha)=2r+p d_0=2(p-1),$$ which proves [\[eq:pstep\]](#eq:pstep){reference-type="eqref" reference="eq:pstep"}.

The contact [\[eq:exact-contact\]](#eq:exact-contact){reference-type="eqref" reference="eq:exact-contact"} has denominator $p^2$ at every higher level. In particular, $p^e d_0$ is divisible by $p$ when $e\ge3$, so the prime-value argument cannot be repeated with this contact to force degree $p^e$. The next section uses level-two clusters instead.

# Cluster transfer and full local inertia {#sec:inertia}

For $j\ge2$, define top clusters in $S_j$ by $$x\sim_j y \quad\Longleftrightarrow\quad
 x=y\ \text{or}\ v(x-y)>2r .$$ The ultrametric inequality makes this an equivalence relation.

[\[lem:clusters\]]{#lem:clusters label="lem:clusters"} There are exactly $p$ top clusters in $S_j$. If $x\in S_j$, they are $$\mathcal C_{j,a}
 =\{P^{\circ(a+bp)}(x):0\le b<p^{j-1}\},
 \qquad a\in\mathbb Z/p\mathbb Z.$$ Different clusters are separated by valuation $2r$, and $P$ acts on the clusters by $a\mapsto a+1$. The Galois action on clusters is the reduction modulo $p$ of its native rotation index.

Indices prime to $p$ give displacement valuation $2r$, by Lemma [\[lem:displacement\]](#lem:displacement){reference-type="ref" reference="lem:displacement"}. An index divisible by $p$ gives a sum of $p$-step displacements. Each has valuation $2(p-1)$, by Proposition [\[prop:second\]](#prop:second){reference-type="ref" reference="prop:second"} and the isometry. Their sum has valuation at least $2(p-1)>2r$. Thus two indices lie in the same cluster exactly when they agree modulo $p$. Galois preserves the root set and the valuation, and its rotation description is Lemma [\[lem:rotation\]](#lem:rotation){reference-type="ref" reference="lem:rotation"}.

Fix $\beta\in S_2$, and let $\mu_2=(P^{\circ p^2})'(\beta)$. Differentiating the exact identity $$P^{\circ p^2}(z)-z
 =(P^{\circ p}(z)-z)M_2(z)V_2(z)$$ at $\beta$ gives $$\mu_2-1=(P^{\circ p}(\beta)-\beta)M_2'(\beta)V_2(\beta).$$ There are $p(p-1)$ differences in the derivative product with rotation index prime to $p$, all of valuation $2r$. The remaining $p-1$ indices are $ap$, $1\le a<p$. Telescoping $a$ $p$-step displacements, and dividing by the first, gives residue $a\ne0$; hence these differences have valuation exactly $2(p-1)$. Consequently $$\label{eq:second-multiplier}
 v(\mu_2-1)
 =2(p-1)+p(p-1)2r+(p-1)2(p-1)
 =2(p-1)(2p-1).$$ In particular $\mu_2\ne1$.

[\[lem:matching\]]{#lem:matching label="lem:matching"} For every $e\ge3$, the $p$ top clusters of $S_e$ are canonically matched with those of $S_2$ by the relation $$C\longleftrightarrow D
 \quad\Longleftrightarrow\quad
 v(x-y)>2r\ \text{for some }x\in C,\ y\in D.$$ The matching is equivariant for both $G_K$ and one application of $P$.

The derivative-ratio argument of Section [3](#sec:second){reference-type="ref" reference="sec:second"}, now at the ordinary period-$p^2$ point $\beta$, is legitimate by [\[eq:second-multiplier\]](#eq:second-multiplier){reference-type="eqref" reference="eq:second-multiplier"}. It gives $$Q_e(\beta)
 =\frac{\mu_2^{p^{e-2}}-1}{\mu_2^{p^{e-3}}-1}
 =(\mu_2-1)^{(p-1)p^{e-3}} .$$ The complementary factor is a unit. Therefore $$\frac1{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
 =\frac{2(p-1)^2(2p-1)}{p^3}>2r.$$ The strict inequality follows from $$\frac{2(p-1)^2(2p-1)}{p^3}-2r
 =\frac{2(p-1)(p^2-3p+1)}{p^3}>0$$ for every integer $p\ge3$. Thus there is a pair $\alpha\in S_e,\beta\in S_2$ with contact deeper than $2r$. Applying $P^{\circ a}$, $0\le a<p$, gives $p$ such pairs meeting all top clusters in both sets.

If one pair $x\in C,y\in D$ has contact deeper than $2r$, then every pair $x'\in C,y'\in D$ does: apply the ultrametric inequality to $x'-x$, $x-y$ and $y-y'$. If $C'\ne C$, its points have contact exactly $2r$ with points of $C$. The unequal-valuation triangle rule then gives contact exactly $2r$ between every point of $C'$ and every point of $D$. Thus $D$ cannot be matched to two clusters; the symmetric argument gives uniqueness for $C$. The $p$ pairs already constructed prove existence everywhere. This matching is characterized by the valuation alone, hence is Galois-equivariant. Since $P$ is an isometry, it carries a matched pair to a matched pair; uniqueness proves native equivariance as well.

At level two, Proposition [\[prop:second\]](#prop:second){reference-type="ref" reference="prop:second"} gives $H_2=C_{p^2}$, so $G_K$ acts transitively on its $p$ top clusters. Lemma [\[lem:matching\]](#lem:matching){reference-type="ref" reference="lem:matching"} transfers that transitivity to the top clusters of $S_e$ for every $e\ge3$. If $H_e$ were a proper subgroup of $C_{p^e}$, all its indices would be divisible by $p$; by Lemma [\[lem:clusters\]](#lem:clusters){reference-type="ref" reference="lem:clusters"}, it would act trivially on those $p>1$ clusters. Hence $H_e=C_{p^e}$. Level one is Lemma [\[lem:rotation\]](#lem:rotation){reference-type="ref" reference="lem:rotation"}. The root action is transitive, giving irreducibility; the same lemma already proves that any root generates the totally ramified splitting field. Fullness of the native rotation subgroup supplies the designated generator $\alpha_e\mapsto P(\alpha_e)$.

# Native-oriented Artin--Schreier classes {#sec:as}

The field result permits a concrete, sign-fixed resolvent. For $n=p^e$ and $\alpha_e\in S_e$, set $$\label{eq:resolvent}
 w_e=\frac{\alpha_e^{n-1}}{M_e'(\alpha_e)},\qquad
 y_e=-\sum_{i=0}^{n-1}\overline i\,\sigma_e^i(w_e),\qquad
 a_e=y_e^p-y_e ,$$ where $\overline i\in\mathbb F_p$ is the residue of $i$.

[\[lem:resolvent\]]{#lem:resolvent label="lem:resolvent"} The elements in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} satisfy $$\mathop{\mathrm{Tr}}_{L_e/K}(w_e)=1,\qquad
 \sigma_e(y_e)-y_e=1,\qquad a_e\in K,\qquad K(y_e)=F_e.$$ The class $[a_e]\in K/\wp(K)$ is independent of the starting root and of the trace-one choice, with this native orientation.

Let $x_0,\ldots,x_{n-1}$ be the distinct roots of $M_e$. The coefficient of $T^{n-1}$ in Lagrange interpolation $$T^{n-1}=\sum_{i=0}^{n-1}
 x_i^{n-1}\frac{M_e(T)}{(T-x_i)M_e'(x_i)}$$ gives $\sum_i x_i^{n-1}/M_e'(x_i)=1$. This is the trace identity. Reindexing the weighted sum in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"}, including its wrapped coefficient $-(n-1)=1$ in characteristic $p$, gives $\sigma_e y_e-y_e=\sum_i\sigma_e^i w_e=1$. Thus $\sigma_e^a y_e=y_e+\overline a$, $a_e$ is invariant, and the stabilizer of $y_e$ is precisely $\langle\sigma_e^p\rangle$. This proves $K(y_e)=F_e$.

Replacing $w_e$ by any trace-one element produces $y'_e$ with the same translation identity. Their difference is fixed by $\sigma_e$, hence lies in $K$, and $a'_e-a_e=\wp(y'_e-y_e)$. Replacing the starting root by $\sigma_e^a\alpha_e$ replaces $y_e$ by $\sigma_e^a y_e=y_e+\overline a$, also preserving the class. No division by $p^e$ has been used.

This is the additive trace-resolvent construction of classical Artin--Schreier theory, written here to specify the native sign. For completeness, every class in $K/\wp(K)$ has a unique reduced polar representative $\sum_{m>0,\ p\nmid m}c_ms^{-m}$ with finite support. The regular part is in $\wp(k[[s]])$: the constant equation is solvable in $k$, and the remaining coefficients are solved successively using the unit derivative $-1$. Subtracting $\wp(c^{1/p}s^{-m})$ eliminates a pole $cs^{-pm}$; starting from the largest pole terminates. A nonzero reduced polar polynomial cannot equal $\wp(b)$: if $v(b)<0$ its largest pole would be divisible by $p$, and if $v(b)\ge0$ it would have no pole. This also proves uniqueness.

[\[prop:as-stable\]]{#prop:as-stable label="prop:as-stable"} For every $e\ge2$, $[a_e]=[a_2]$ and $F_e=F_2$ inside the fixed separable closure.

Let $\rho_e:G_K\to\mathbb Z/p^e\mathbb Z$ be characterized by $$g\alpha_e=P^{\circ\rho_e(g)}(\alpha_e).$$ Commutation with $P$ shows that the index is independent of the starting root; composition adds indices, so it is a continuous character, factoring through $L_e/K$. For $e\ge3$, label the top clusters at each level by $i\in\mathbb Z/p\mathbb Z$, using native iteration. By Lemma [\[lem:matching\]](#lem:matching){reference-type="ref" reference="lem:matching"}, the matching is a map commuting with $i\mapsto i+1$, hence has the form $i\mapsto i+c$. Galois equivariance then gives, for every $g\in G_K$, $$i+\overline{\rho_e(g)}+c
 =i+c+\overline{\rho_2(g)} .$$ Thus $\rho_e\bmod p=\rho_2\bmod p$ on the whole group. The same assertion is tautological at $e=2$. The translation identity in Lemma [\[lem:resolvent\]](#lem:resolvent){reference-type="ref" reference="lem:resolvent"} gives $$g(y_e)-y_e=\overline{\rho_e(g)}
 =\overline{\rho_2(g)}=g(y_2)-y_2.$$ Consequently $b_e=y_e-y_2$ is fixed by $G_K$ and lies in $K$. It follows that $a_e-a_2=\wp(b_e)$, and that $K(y_e)=K(y_2)$. The phase $c$ permits only a translation of cluster labels, not a nontrivial scalar or sign change of the native generator.

[\[prop:separation\]]{#prop:separation label="prop:separation"} For every $e\ge2$, $L_1\cap L_e=K$.

First suppose, for contradiction, $L_1\subset L_2$. Choose $\alpha\in S_2,\beta\in S_1$, and put $\eta=\alpha-\beta\in L_2$. By Proposition [\[prop:second\]](#prop:second){reference-type="ref" reference="prop:second"}, $$v_{L_2}(\eta)=2(p-1)^2,\qquad
 v_{L_2}(\sigma_2^p\eta-\eta)=2p^2(p-1).$$ For the second equation, $\sigma_2^p$ fixes the unique degree-$p$ subfield, hypothetically $L_1$, and the $p$-step displacement of $\alpha$ is [\[eq:pstep\]](#eq:pstep){reference-type="eqref" reference="eq:pstep"}. The first value is prime to $p$, so Lemma [\[lem:prime-value\]](#lem:prime-value){reference-type="ref" reference="lem:prime-value"} gives the second lower break, under this supposition, as $$b_2=2p^2(p-1)-2(p-1)^2
 =2(p-1)(p^2-p+1).$$ The degree-$p$ quotient is hypothetically $L_1/K$, giving first break $b_1=p-1$. But then $$b_2-b_1=(p-1)(2p^2-2p+1)\equiv-1\pmod p,$$ contrary to [\[eq:herbrand-two\]](#eq:herbrand-two){reference-type="eqref" reference="eq:herbrand-two"}. Thus $L_1\not\subset L_2$, and its prime degree gives $L_1\cap L_2=K$.

If $L_1\subset L_e$ at any later level, cyclicity would identify it with $F_e=F_2\subset L_2$, contradicting what was just proved. Again prime degree gives the stated intersection. This completes Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

The second lower-break expression in this contradiction has not yet been proved to be an actual invariant: its paired first break arose from a false containment assumption. Section [6](#sec:ramification){reference-type="ref" reference="sec:ramification"} derives the actual two breaks independently, with first break $2(p-1)$.

# The first quotient and the second-layer different {#sec:ramification}

We now calculate the actual ramification invariants. The element $\alpha_2-\beta_1$ has valuation divisible by $p$ in $L_2L_1$, so Lemma [\[lem:prime-value\]](#lem:prime-value){reference-type="ref" reference="lem:prime-value"} does not apply there. Its replacement tracks the leading cancellation.

[\[lem:cancellation\]]{#lem:cancellation label="lem:cancellation"} Let $D/K$ be a finite totally ramified Galois $p$-extension, with group $G$, first lower break $b_0>0$, and $p\nmid b_0$. Suppose $x\in D$ has $a=v_D(x)>0$, $v_p(a)=1$, and $$\label{eq:cancellation-hyp}
 v_D(gx-x)>a+p b_0\qquad(g\ne1).$$ In any uniformizer expansion of $x$, the first nonzero exponent prime to $p$ is $$n=a+(p-1)b_0.$$ The first graded quotient $G_{b_0}/G_{b_0+1}$ has order $p$. If $g$ has later lower break $c=\ell_D(g)>b_0$, then $$\label{eq:later-rule}
 v_D(gx-x)=n+c.$$

Write $x=\sum_{j\ge a}c_j\pi^j$, with $c_a\ne0$. For an element $g$ of break $b_0$, [\[eq:monomial-displacement\]](#eq:monomial-displacement){reference-type="eqref" reference="eq:monomial-displacement"} says that the leading monomial contributes at exact order $a+p b_0$. Every later monomial with exponent divisible by $p$ contributes at strictly greater order. If the first nonzero exponent $j$ prime to $p$ were less than $a+(p-1)b_0$, its contribution at $j+b_0$ would be uniquely lowest, contradicting [\[eq:cancellation-hyp\]](#eq:cancellation-hyp){reference-type="eqref" reference="eq:cancellation-hyp"}. If no such exponent were present at $n=a+(p-1)b_0$, the leading monomial at order $a+p b_0$ could not cancel. Thus $n$ is the first such exponent, and $p\nmid n$.

To control the entire first grade, not just one automorphism, put $$\theta(g)=\mathop{\mathrm{res}}\left(\frac{g\pi-\pi}{\pi^{b_0+1}}\right),
 \qquad g\in G=G_{b_0}.$$ Composition adds the leading coefficients, since each automorphism fixes $k$ and has linear coefficient $1$. Hence $\theta$ is additive and has kernel $G_{b_0+1}$. The coefficient of order $a+p b_0$ in $gx-x$ is $$c_a\,\overline{(a/p)}\,\theta(g)^p
 +c_n\overline n\,\theta(g).$$ Only these two monomials contribute at that order. By [\[eq:cancellation-hyp\]](#eq:cancellation-hyp){reference-type="eqref" reference="eq:cancellation-hyp"}, the displayed expression vanishes for every $g$. Its leading coefficient is nonzero, so this degree-$p$ polynomial has at most $p$ roots. The image of the nontrivial first graded $p$-group therefore has exactly $p$ elements.

For a later break $c>b_0$, the monomial $c_n\pi^n$ contributes at order $n+c$. Later prime-to-$p$ exponents give larger orders. Every exponent divisible by $p$ gives order at least $a+pc$, and $$a+pc-(n+c)=(p-1)(c-b_0)>0.$$ The contribution at $n+c$ is unique. All tail orders tend to infinity, so no infinite-series cancellation changes it. This proves [\[eq:later-rule\]](#eq:later-rule){reference-type="eqref" reference="eq:later-rule"}.

## Apply the cancellation in the disjoint compositum

Set $B=L_2L_1$, $G=\mathop{\mathrm{Gal}}(B/K)$, and choose $\alpha\in S_2,\beta\in S_1$. By Proposition [\[prop:separation\]](#prop:separation){reference-type="ref" reference="prop:separation"}, $$G\simeq C_{p^2}\times C_p,\qquad v_B=p^3v.$$ Let $\sigma,\gamma\in G$ act by one native step on $\alpha,\beta$, respectively, fixing the other root. For $\eta=\alpha-\beta$, write $$\label{eq:a-A}
 a=v_B(\eta)=2p(p-1)^2,\qquad A=2p^2(p-1).$$ The contact gives the first equality, with $v_p(a)=1$. Both root displacements have base valuation at least $2r$, so $$\label{eq:uniform-displ}
 v_B(g\eta-\eta)\ge A\quad(g\ne1),\qquad
 v_B(\sigma\eta-\eta)=v_B(\gamma\eta-\eta)=A.$$ Infinite valuation is allowed in the inequality.

Let $b_0$ be the first lower, equivalently upper, break of $B/K$. Its quotient $L_1/K$ gives $b_0\le p-1$. The first drop of a finite abelian $p$-extension is detected by a degree-$p$ character: the first graded quotient is elementary abelian (the leading-coefficient injection above shows this), and a nonzero character of that quotient pulls back to such a character of $G$. Its Artin--Schreier break is $b_0$. Thus $b_0$ is positive and prime to $p$. Finally $$A-a=2p(p-1)>p(p-1)\ge p b_0.$$ Lemma [\[lem:cancellation\]](#lem:cancellation){reference-type="ref" reference="lem:cancellation"} applies. In particular the first graded quotient has order $p$, and with $$\label{eq:n-compositum}
 n=a+(p-1)b_0$$ we have $v_B(g\eta-\eta)=n+\ell_B(g)$ whenever $\ell_B(g)>b_0$.

## Exclude all early-conductor orderings

Put $F=F_2$, let $b$ be its unique break, and write $u_2$ for the second upper break of $L_2/K$. Classical cyclic ramification gives $u_2\ge pb\ge p$. Let $$E=FL_1,\qquad N=\mathop{\mathrm{Gal}}(B/E)=\langle\sigma^p\rangle .$$ Then $E/K$ is elementary abelian of degree $p^2$. The subgroup $N$ persists in $G^u$ for $0\le u\le p-1$. Indeed choose $p-1<u'<u_2$. The projection of $G^{u'}$ on $L_1$ is trivial, while its projection on $L_2$ contains $\langle\sigma^p\rangle$. In the direct product these two projections force all of $N$ to lie in $G^{u'}$; monotonicity gives the assertion. It follows that $$\label{eq:index-quotient}
 [G:G^u]=[G/N:(G/N)^u]\qquad(0\le u\le p-1).$$ This is a quotient argument, not an assumed product rule for compositum ramification.

Suppose $b\le p-1$. All degree-$p$ characters of $E/K$ are linear combinations over $\mathbb F_p$ of those for $F/K$ and $L_1/K$. Their reduced polar representatives have largest poles at most $p-1$; a linear combination cannot introduce a larger pole. The $L_1$ character has break exactly $p-1$. Characters separate this elementary abelian group, so its last upper break is $p-1$. By [\[eq:index-quotient\]](#eq:index-quotient){reference-type="eqref" reference="eq:index-quotient"} and the cancellation lemma its first graded quotient has order $p$. Hence $E/K$ has exactly two distinct upper breaks, $b_0<p-1$ and $p-1$, each dropping the group by a factor $p$. This includes the possibility $b=p-1$: possible cancellation of the two leading poles either produces a smaller first break, or gives a single drop of order $p^2$, which the lemma rules out.

The lower value corresponding to the last break of $E/K$ is $$c=\psi_B(p-1)=b_0+p(p-1-b_0)>b_0.$$ There is $h\in G$ with lower break exactly $c$: lift a nontrivial element of the last upper group of $E/K$ inside $G^{p-1}$; its image disappears immediately after that break. By [\[eq:n-compositum\]](#eq:n-compositum){reference-type="eqref" reference="eq:n-compositum"} and [\[eq:later-rule\]](#eq:later-rule){reference-type="eqref" reference="eq:later-rule"}, $$v_B(h\eta-\eta)=n+c=a+p(p-1)<A,$$ contradicting [\[eq:uniform-displ\]](#eq:uniform-displ){reference-type="eqref" reference="eq:uniform-displ"}. Therefore $$\label{eq:b-greater}
 b>p-1.$$

## Read off the exact first quotient break

By [\[eq:b-greater\]](#eq:b-greater){reference-type="eqref" reference="eq:b-greater"}, every nonzero linear combination involving the character of $F/K$ has break $b$: its highest pole cannot cancel with the strictly lower pole of the $L_1$ character. The other nonzero characters have break $p-1$. Thus $E/K$ has upper breaks $p-1,b$, each of rank one. The subgroup $N$ persists through upper $b$: choose $b<u'<u_2$, possible since $u_2\ge pb>b$, and repeat the two-projection argument. Consequently $$b_0=p-1,\qquad n=a+(p-1)^2.$$ For $p-1<u\le b$, the $L_1$ projection is trivial and the $L_2$ projection is full. Hence $G^u=\langle\sigma\rangle$, and immediately after $b$ its $L_2$ projection drops to $\langle\sigma^p\rangle$. The lower break of the native generator $\sigma$ is thus $$\ell_B(\sigma)=\psi_B(b)
 =(p-1)+p(b-(p-1))>b_0 .$$ Its displacement is $A$; the later-break rule yields $$\ell_B(\sigma)=A-n
 =2p^2(p-1)-2p(p-1)^2-(p-1)^2=p^2-1.$$ Comparison gives $$\label{eq:exact-first-break}
 (p-1)+p(b-(p-1))=p^2-1,\qquad b=2(p-1).$$ Since $F_e=F_2$ for $e\ge2$, this proves the asserted first quotient break at every higher level. Equivalently, the largest pole of the native-oriented reduced AS class is $2(p-1)$, with nonzero coefficient. No general formula for all its coefficients has been used or obtained.

## The complete second-layer filtration

The full upper filtration of $B/K$, at this point with the last break $u_2$ still undetermined, is $$\label{eq:compositum-filtration}
 G^u=
 \begin{cases}
 G,&0\le u\le p-1,\\
 \langle\sigma\rangle,&p-1<u\le 2(p-1),\\
 \langle\sigma^p\rangle,&2(p-1)<u\le u_2,\\
 1,&u>u_2.
 \end{cases}$$ The first two lines were proved above. After $p-1$ the $L_1$ projection is trivial, and upper quotient compatibility identifies the $L_2$ projection with its upper group. A subgroup of $C_{p^2}\times C_p$ with trivial second projection is uniquely determined by its first projection. This proves the last two lines without any additional independence assumption.

Let $c_0,c_1,c_2$ be the lower breaks of $B/K$. The first two are $$c_0=p-1,\qquad c_1=(p-1)+p(p-1)=p^2-1.$$ The element $\tau=\sigma^p$ has lower break $c_2$. It fixes $\beta$, so [\[eq:pstep\]](#eq:pstep){reference-type="eqref" reference="eq:pstep"} gives $$v_B(\tau\eta-\eta)=2p^3(p-1).$$ The later-break rule is applicable because $c_2>c_1>b_0$. Subtracting its identity for $\sigma$ from that for $\tau$ gives $$c_2-c_1=2p^3(p-1)-2p^2(p-1)=2p^2(p-1)^2.$$ The index on the last interval of [\[eq:compositum-filtration\]](#eq:compositum-filtration){reference-type="eqref" reference="eq:compositum-filtration"} is $p^2$. Hence Herbrand's formula gives $$u_2-2(p-1)=\frac{c_2-c_1}{p^2}=2(p-1)^2,
 \qquad u_2=2p(p-1).$$ In particular, the upper and lower breaks of $B/K$ are $$\label{eq:compositum-breaks}
 \begin{aligned}
 &(p-1,\ 2(p-1),\ 2p(p-1)),\\
 &(p-1,\ p^2-1,\ p^2-1+2p^2(p-1)^2).
 \end{aligned}$$ Upper quotient compatibility identifies the two upper breaks of $L_2/K$. Its lower breaks are $$b_1=2(p-1),\qquad
 b_2=b_1+p\bigl(2p(p-1)-2(p-1)\bigr)
 =2(p-1)(p^2-p+1).$$ These are actual invariants, derived with the actual first break, independently of the hypothetical calculation in Proposition [\[prop:separation\]](#prop:separation){reference-type="ref" reference="prop:separation"}.

## Different exponents versus the root order

For a finite totally ramified Galois extension $D/K$, the Hilbert different formula in the integer-normalized valuation is $$\label{eq:different-sum}
 d_{D/K}=\sum_{i\ge0}(|\mathop{\mathrm{Gal}}(D/K)_i|-1).$$ One way to check this normalization is to use a uniformizer $\pi$, which generates the integer ring over $R$. Its minimal polynomial is Eisenstein; its derivative generates the different. The valuation of that derivative is $\sum_{g\ne1}v_D(g\pi-\pi)$, and counting each automorphism in its lower groups gives [\[eq:different-sum\]](#eq:different-sum){reference-type="eqref" reference="eq:different-sum"}. The derivative description is the monogenic case of the classical different formula [@stacksdifferent Tags 0BWD and 0BWG].

For $L_2/K$, the successive lower group orders are $p^2,p$, giving $$\begin{aligned}
 d_{L_2/K}
 &=(b_1+1)(p^2-1)+(b_2-b_1)(p-1)\\
 &=(2p-1)(p^2-1)+2p(p-1)^3\\
 &=(p-1)(2p^3-2p^2+3p-1).
 \end{aligned}$$ This proves Theorem [\[thm:ramification\]](#thm:ramification){reference-type="ref" reference="thm:ramification"}. For $B/K$, the three lower group orders are $p^3,p^2,p$, so the additional invariant is $$\begin{aligned}
 d_{B/K}
 &=(c_0+1)(p^3-1)+(c_1-c_0)(p^2-1)
   +(c_2-c_1)(p-1)\\
 &=p(p^3-1)+p(p-1)(p^2-1)+2p^2(p-1)^3\\
 &=p^2(p-1)(2p^2-2p+3).
 \end{aligned}$$

These are field different exponents, not the discriminant of $R[\alpha_2]$. For example, at $p=3$ the proved formulas give upper breaks $(4,12)$, lower breaks $(4,28)$, and $d_{L_2/K}=88$. The root-difference product instead gives $$v(\operatorname{Disc}(M_2))
 =p^2\bigl(p(p-1)2r+(p-1)2(p-1)\bigr)
 =4p^2(p-1)^2,$$ which equals $144$ at $p=3$. This is a direct consequence of the distances already proved, not a numerical input to the field calculation. It must not be substituted for the exponent $88$.

# The eventual native quotient tower {#sec:tower}

This section combines the local Galois fields with an independent compact-limit theorem. We state the imported interface explicitly before proving the Galois continuity and quotient transfer needed for Theorem [\[thm:tower\]](#thm:tower){reference-type="ref" reference="thm:tower"}.

Choose an algebraic closure of $K$ containing $K^\mathrm{sep}$, and let $\mathcal C$ be its completion. It is complete and algebraically closed by the classical completion theorem [@conradcompletion Theorem 1.1]. Fix $0<|s|<1$ and use the associated absolute value. The sets $S_e$ are still the unique small ordinary cycles in $\mathcal C$, by Lemma [\[lem:small\]](#lem:small){reference-type="ref" reference="lem:small"}.

For nonempty compact subsets $E,F\subset\mathcal C$, let $d_H(E,F)$ denote their Hausdorff distance for the ordinary metric $d(x,y)=|x-y|$; explicitly, $$d_H(E,F)=\max\left\{
 \sup_{x\in E}\inf_{y\in F}|x-y|,
 \sup_{y\in F}\inf_{x\in E}|x-y|
 \right\}.$$

[\[thm:compact-input\]]{#thm:compact-input label="thm:compact-input"} For these cycles, the ordinary metric closure $$C=\overline{\bigcup_{e\ge1}S_e}^{\,\mathcal C}$$ is compact. The set $$\label{eq:tail-limit}
 \Omega=\bigcap_{N\ge1}
 \overline{\bigcup_{e\ge N}S_e}^{\,C}$$ is nonempty and compact, $P(\Omega)=\Omega$, and $d_H(S_e,\Omega)\to0$ for the full sequence. There is a homeomorphism $h:\Omega\to\mathbb Z_p$ such that $$\label{eq:native-conjugacy}
 h(Px)=h(x)+1.$$

This is precisely the compactness, Hausdorff and conjugacy part of the unpublished companion [@companion2026haar Theorem 1.1, *Compact adding-machine limit of the optimal cycles*], applied to $\mathcal C$ and $\lambda=1+s$. The companion proves it for every complete algebraically closed nonarchimedean field of characteristic $p$ and every $0<|\lambda-1|<1$. Its proof includes the all-anchor identity $$\frac1{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
 =c_d:=\frac{p-1}{p^{d+1}}
 v\bigl((P^{\circ p^d})'(\beta)-1\bigr)
 \ge d r^3+r^2(1+1/p),\qquad e>d,\quad\beta\in S_d.$$ The finite value of this average excludes the finite-cycle alternative for the compact limit. Thus no unproved isolation assumption, nor merely weak convergence of measures, is being used in [\[eq:native-conjugacy\]](#eq:native-conjugacy){reference-type="eqref" reference="eq:native-conjugacy"}. The companion proves its factor, contact and compactness assertions without using full local inertia or the first AS character. Theorem [\[thm:compact-input\]](#thm:compact-input){reference-type="ref" reference="thm:compact-input"} is the only additional model-specific input in this section; no part of the preceding sections depends on it.

## Continuity of the Galois action on the compact closure

The characters $\rho_e:G_K\to\mathbb Z/p^e\mathbb Z$ were defined in Proposition [\[prop:as-stable\]](#prop:as-stable){reference-type="ref" reference="prop:as-stable"}. By Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} they are continuous and surjective, with one native step labeled $+1$. Every $g\in G_K$ extends uniquely to the algebraic closure: purely inseparable roots have uniquely determined images. The extension of the valuation from complete $K$ is unique, so the resulting action is isometric. It therefore extends to an isometric automorphism of $\mathcal C$, with inverse the extension of $g^{-1}$. Since $gS_e=S_e$ at every level and $g$ commutes with $P$, it preserves $C$, every tail closure in [\[eq:tail-limit\]](#eq:tail-limit){reference-type="eqref" reference="eq:tail-limit"}, and $\Omega$.

We need continuity in $g$, not just individual isometries. Fix $\varepsilon>0$. Compactness of $C$ and density of the algebraic cycle union give a finite set $A_\varepsilon\subset\bigcup_e S_e$ such that every $x\in C$ is within distance strictly less than $\varepsilon$ of some $a\in A_\varepsilon$. Each $a$ is separable algebraic over $K$, so its stabilizer in $G_K$ is open. Let $U_\varepsilon$ be the intersection of these finitely many stabilizers. For $g\in U_\varepsilon$, $$|gx-x|\le
 \max\{|gx-ga|,|ga-a|,|a-x|\}<\varepsilon
 \qquad(x\in C).$$ Thus elements of $G_K$ near the identity move all of $C$ uniformly little. If $g=g_0u$, $u\in U_\varepsilon$, and $|x-x_0|<\varepsilon$, then $$|gx-g_0x_0|=|ux-x_0|
 \le\max\{|ux-x|,|x-x_0|\}<\varepsilon.$$ This proves joint continuity of $G_K\times C\to C$, and of its restriction to $\Omega$. It requires no assertion that a limit point is algebraic.

## A canonical translation character

For a homeomorphism $h$ satisfying [\[eq:native-conjugacy\]](#eq:native-conjugacy){reference-type="eqref" reference="eq:native-conjugacy"}, the continuous map $f_g=h\circ g\circ h^{-1}:\mathbb Z_p\to\mathbb Z_p$ commutes with addition by $1$. Any continuous $f$ with $f(z+1)=f(z)+1$ is a translation: induction gives $f(m)=f(0)+m$ on nonnegative integers, and these integers are dense in $\mathbb Z_p$. Hence there is a unique $\chi_\infty(g)\in\mathbb Z_p$ such that $$\label{eq:translation-character}
 h(gx)=h(x)+\chi_\infty(g)\qquad(x\in\Omega).$$ Composition adds translation amounts, so $\chi_\infty$ is a homomorphism. For a fixed $\omega_0\in\Omega$, $$\chi_\infty(g)=h(g\omega_0)-h(\omega_0),$$ and the joint continuity just proved shows that it is continuous.

The character is independent of the origin and of the chosen native conjugacy: if $h'$ also satisfies [\[eq:native-conjugacy\]](#eq:native-conjugacy){reference-type="eqref" reference="eq:native-conjugacy"}, then $h'\circ h^{-1}$ commutes with addition by $1$, so is itself a translation. Conjugating a translation by a translation does not change its amount. Multiplication of coordinates by a unit $u\in\mathbb Z_p^\times$ would instead change the native step to $+u$, and is compatible with [\[eq:native-conjugacy\]](#eq:native-conjugacy){reference-type="eqref" reference="eq:native-conjugacy"} only if $u=1$. There is therefore no sign or scalar ambiguity at any finite depth.

## Transfer every finite quotient to all late cycles

Fix $j\ge1$ and define the continuous surjection $$q_j:\Omega\longrightarrow\mathbb Z/p^j\mathbb Z,\qquad
 q_j(x)=h(x)\bmod p^j.$$ Its finitely many fibers are compact and clopen. They are permuted natively by $+1$ and by Galois translation by $\chi_\infty(g)\bmod p^j$. This quotient exists at every $j$; there is no assumption that a particular family of metric partitions attains every cardinality $p^j$. Equivalently, a cofinal inverse system of cyclic partitions suffices, since any partition of size $p^k$, $k\ge j$, maps to the quotient modulo $p^j$.

Different fibers of $q_j$ have positive minimum distance: the distance function attains its minimum on their compact product, and disjointness makes that minimum nonzero. Choose $\delta_j>0$ such that $$\label{eq:delta-separation}
 x,y\in\Omega,\ |x-y|<\delta_j
 \quad\Longrightarrow\quad q_j(x)=q_j(y).$$ Full-sequence Hausdorff convergence supplies $E_j\ge j$ with $$\label{eq:uniform-threshold}
 d_H(S_e,\Omega)<\delta_j\qquad(e\ge E_j).$$ This threshold is chosen before, and independently of, $g$.

For each such $e$, define $q_{e,j}:S_e\to\mathbb Z/p^j\mathbb Z$ by choosing $x\in\Omega$ with $|\alpha-x|<\delta_j$ and setting $q_{e,j}(\alpha)=q_j(x)$. Two choices of $x$ are at mutual distance less than $\delta_j$, by the ultrametric inequality; hence [\[eq:delta-separation\]](#eq:delta-separation){reference-type="eqref" reference="eq:delta-separation"} makes the definition independent of the choice. The other directed Hausdorff bound in [\[eq:uniform-threshold\]](#eq:uniform-threshold){reference-type="eqref" reference="eq:uniform-threshold"} proves surjectivity.

All points in $C$ lie on $|z|=|s|^r<1$, by continuity of the norm and Lemma [\[lem:small\]](#lem:small){reference-type="ref" reference="lem:small"}. On the open unit disk, $$P(x)-P(y)=(x-y)(1+s+x+y),\qquad |1+s+x+y|=1.$$ Thus $P$ is an isometry there. If $x$ is an allowed choice for $\alpha$, then $Px$ is an allowed choice for $P\alpha$. Likewise $gx$ is an allowed choice for $g\alpha$, since Galois acts isometrically and preserves $\Omega$. Therefore $$\label{eq:two-equivariances}
 \begin{aligned}
 q_{e,j}(P\alpha)&=q_{e,j}(\alpha)+1,\\
 q_{e,j}(g\alpha)&=q_{e,j}(\alpha)+\chi_\infty(g)\bmod p^j.
 \end{aligned}$$ There is no need to choose nearby points globally consistently; choice independence was proved first. On the other hand, the definition of $\rho_e$ and the first identity give $$q_{e,j}(g\alpha)
 =q_{e,j}(P^{\circ\rho_e(g)}\alpha)
 =q_{e,j}(\alpha)+\rho_e(g)\bmod p^j.$$ Comparison with the second identity in [\[eq:two-equivariances\]](#eq:two-equivariances){reference-type="eqref" reference="eq:two-equivariances"} proves [\[eq:eventual-intro\]](#eq:eventual-intro){reference-type="eqref" reference="eq:eventual-intro"} simultaneously for every $g\in G_K$. It is exact equality of characters, not just an abstract isomorphism of finite cyclic fields or a subsequence limit.

## Surjectivity and the algebraic kernel fields

The image $H=\chi_\infty(G_K)$ is compact and hence closed in $\mathbb Z_p$, since $G_K$ is profinite. Taking $j=1$ and a sufficiently late $e$ in [\[eq:eventual-intro\]](#eq:eventual-intro){reference-type="eqref" reference="eq:eventual-intro"} shows that its reduction modulo $p$ is the nonzero native first character. Thus $H$ contains a $p$-adic unit $u$. It contains all integer multiples of $u$, which are dense in $\mathbb Z_p$, and closedness yields $H=\mathbb Z_p$.

For every $j$, $\chi_\infty\bmod p^j$ is a continuous surjection onto the cyclic group of order $p^j$. Its kernel is open and normal, so Galois correspondence [@stacksgalois Section 9.22] gives $$K_j=(K^\mathrm{sep})^{\ker(\chi_\infty\bmod p^j)},\qquad
 [K_j:K]=p^j.$$ For $e\ge j$, the unique degree-$p^j$ subfield of $L_e$ is $$F_{e,j}=L_e^{\langle\sigma_e^{p^j}\rangle}
 =(K^\mathrm{sep})^{\ker(\rho_e\bmod p^j)}.$$ The proved character equality therefore gives $$K_j=F_{e,j}\qquad(e\ge E_j)$$ as actual subfields of the chosen separable closure. The kernels for $j+1$ lie in the kernels for $j$, so $K_j\subset K_{j+1}$. Restrictions on Galois groups are the ordinary reductions modulo $p^j$, induced by the same character. Consequently $$\mathop{\mathrm{Gal}}\left(\bigcup_{j\ge1}K_j\,/\,K\right)
 \simeq\varprojlim_j\mathbb Z/p^j\mathbb Z=\mathbb Z_p,$$ with quotient map $\chi_\infty$. If a second continuous character satisfied [\[eq:eventual-intro\]](#eq:eventual-intro){reference-type="eqref" reference="eq:eventual-intro"}, choose $e$ beyond both thresholds at each $j$. Their reductions both equal $\rho_e\bmod p^j$; equality at every $j$ gives equality in $\mathbb Z_p$. This proves uniqueness and completes Theorem [\[thm:tower\]](#thm:tower){reference-type="ref" reference="thm:tower"}.

In particular $K_1=F_2$, by choosing $e$ beyond $E_1$ and using Proposition [\[prop:as-stable\]](#prop:as-stable){reference-type="ref" reference="prop:as-stable"}. It is not $L_1$, since $L_1\cap L_2=K$. For larger $j$, the theorem fixes the quotient degree first and only then takes the cycle level sufficiently large. It does not imply containment of a prescribed full $L_j$ in all later fields.

Finally, the points of $\Omega$ are classical elements of the completed algebraic closure, not necessarily algebraic over $K$. No finite Galois correspondence has been applied to such a coordinate, and no theorem identifying fixed fields inside the completion is used. Every field above is defined by a continuous character kernel inside $K^\mathrm{sep}$.

# Scope and further questions

The local arithmetic separates three objects attached to the same native cycles. The full splitting field $L_e$ has degree $p^e$; its first quotient $F_e$ equals $F_2$ for $e\ge2$; and for a fixed $j$ the eventual kernel field $K_j$ is the common degree-$p^j$ quotient of all sufficiently late $L_e$. Only the last collection has a proved nesting relation. The prime-period field $L_1$ is separated from every higher $L_e$, while the common first quotient has twice its ramification break.

The exact higher ramification sequence of $L_e/K$, general-prime coefficients of the reduced first AS representative, effective thresholds $E_j$, and complete pairwise intersections of the full $L_e$ are not determined here. Nor does a theorem about this completed small factor decide transitivity on all global dynatomic cycles. These are distinct questions, rather than consequences of the cyclicity or of the compact-limit construction.

## Preparation and proof provenance {#preparation-and-proof-provenance .unnumbered}

This manuscript was prepared with AI assistance and current-team internal proof checking. These activities are not external peer review or publication acceptance. The arithmetic contact, native cluster-transfer and ramification arguments form one integrated local-field result. The independently proved compact-limit theorem is explicitly credited to the unpublished companion [@companion2026haar], and is used only in Section [7](#sec:tower){reference-type="ref" reference="sec:tower"}. All remaining new arguments used for the conclusions are given in this article. No numerical experiment or computer-assisted mathematical certificate is required by the proofs.
