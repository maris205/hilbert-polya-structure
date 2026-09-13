---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-line-ramification"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_line_ramification/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_line_ramification/paper/main.pdf"
source_sha256: "62fc92c3c0ad6a6276c833b5a1f063b35b782bb68cd67d02a3ff824a93d5eb4d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Filtered inertia and Artin conductors of the 27 lines on an explicit cubic surface

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_line_ramification>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_line_ramification/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_line_ramification/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_line_ramification/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_yukawa_line_ramification/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the complete lower filtered inertia of the degree-$27$ line field of an explicit smooth cubic surface whose normal closure has Galois group $W(E_6)$. Factor degrees in the $27$-line action do not distinguish the required subgroup embeddings, and the wild primes $3$ and $5$ require higher ramification data. We combine exact maximal-order decompositions with the simultaneous actions on the $27$ lines and the $36$ double-sixes, exhaust the compatible subgroup classes, solve the branch-different equations, and apply Serre's graded tame-action law only after the finite alternatives have been enumerated. At $3$ the filtration has orders $(18,9,3,3,3,3,3,3,1)$, while at $5$ it has orders $(20,5,5,5,1)$; the corresponding Artin conductor pairs on the nontrivial $6$- and $20$-dimensional constituents are $(11,35)$ and $(7,29)$. Writing $A=181\cdot997\cdot2346241$ and $B=283\cdot1801\cdot
  14932047182473291995860108491583652133938007263719$, we obtain $$\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6,\qquad
   \operatorname{Disc}(K)=3^{106560}5^{80352}A^{34560}B^{25920}.$$ Two decomposition groups of orders $18$ and $36$ remain possible at $3$, but they have the same filtered inertia and hence the same stated invariants. No decomposition Frobenius, bad Euler factor, epsilon factor, or root number is determined.
author:
- Anonymous Authors
bibliography:
- references.bib
title: Filtered inertia and Artin conductors of the 27 lines on an explicit cubic surface
```

## Markdown 正文

# Introduction {#sec:introduction}

The $27$ lines on a smooth cubic surface carry a rigid $W(E_6)$ configuration, but a global identification of the line-field Galois group does not determine how that group ramifies. A bad-prime list records where ramification may occur, and a field discriminant records a weighted total. Neither datum identifies the embedded inertia subgroup, its higher ramification groups, or the Artin conductors of the irreducible constituents of the line permutation representation.

This paper resolves that local problem for the explicit surface [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"}. Its degree-$27$ line field $E$ has normal closure $K$ with $\operatorname{Gal}(K/\mathbf{Q})=W(E_6)$. We determine the complete lower filtration at every finite ramified prime, including the wild primes $3$ and $5$, and then compute the Artin and Swan conductors on $$\mathbf{Q}[27]=\mathbf{1}\oplus V_6\oplus V_{20}.$$ The calculation closes globally with exact factorizations of $\operatorname{Disc}(E)$ and $\operatorname{Disc}(K)$ and with the archimedean plus/minus multiplicities of $(V_6,V_{20})$.

The main obstruction is subgroup ambiguity. At a rational prime, factor degrees of the line polynomial describe the orbits of a decomposition group on $27$ points. Several nonconjugate subgroups of $W(E_6)$ can have the same orbit partition. Even after a second $36$-point action on the double-sixes is introduced, the prime $3$ leaves three raw subgroup hits. Higher differents and the action of tame inertia on the last wild grade are needed to finish the classification. We therefore use the two actions asymmetrically: the $27$-line action carries the representations of interest, while the $36$-double-six action separates embeddings. Only one frozen degree-$36$ polynomial certifies the local double-six partitions; the other is explicitly a bounded nonresult and is never corroborating evidence.

The decisive $3$-adic step is finite and exhaustive. The simultaneous action scan gives subgroup classes $140,142,206$. Normality and cyclic residue quotients leave four ordered $(D,I)$ pairs. Across those pairs, every possible deep $C_3$ has Table-of-Marks profile $6$, $7$, or $8$, with profile $6$ occurring twice. Exact branch-different equations give formal layer solutions $$(7,-18),\qquad(1,6),\qquad(7,-18).$$ Only profile $7$ is nonnegative. Serre's graded conjugation formula at the last, odd grade then forces inversion, selecting inertia class $140$ and excluding the central class $142$. Two decomposition overgroups remain: $$(D,I)=(140,140)\quad\text{or}\quad(206,140).$$ They have the same filtered inertia and therefore the same conductor and discriminant consequences.

The complete output is summarized in [\[tab:hero-local,fig:wild-filtrations\]](#tab:hero-local,fig:wild-filtrations){reference-type="ref" reference="tab:hero-local,fig:wild-filtrations"}. In particular, the wild lower-order sequences are $$p=3:(18,9,3,3,3,3,3,3,1),\qquad
 p=5:(20,5,5,5,1),$$ and their Artin pairs on $(V_6,V_{20})$ are $(11,35)$ and $(7,29)$. If $$\begin{aligned}
 q&=14932047182473291995860108491583652133938007263719,\\
 A&=181\cdot997\cdot2346241,\\
 B&=283\cdot1801\cdot q.
\end{aligned}$$ then $$\operatorname{Disc}(E)=3^{46}5^{36}A^{18}B^6,\qquad
 \operatorname{Disc}(K)=3^{106560}5^{80352}A^{34560}B^{25920}.$$

#### Contributions.

The paper makes four instance-specific claims.

1.  We separate the nine-prime surface divided-discriminant envelope from the exact eight-prime ramified support of both $E$ and $K$, and give every maximal-order local row that is used.

2.  We exhaust all $p=3$ and $p=5$ decomposition/inertia candidates. At $3$, the complete deep-$C_3$ rational calculation and Serre's odd-grade action determine one filtered inertia while preserving the two possible decomposition overgroups.

3.  We identify the tame $C_3$ and root-reflection classes, compute every local fixed space and Artin--Swan pair on $(V_6,V_{20})$, and derive the exact representation conductors and both field discriminants.

4.  We determine the real signature and distinguish the Table-of-Marks subgroup index from the character-table element index at infinity.

These claims are bounded to the displayed surface. We do not claim a first result for arbitrary cubic surfaces, and the finite-group and local-field tools themselves are classical.

## Context and closest precedent

Serre's treatment of ramification groups supplies three universal ingredients used here: Krasner--Hensel factor stability, the conjugation action on $G_i/G_{i+1}$, and the conductor--discriminant identity [@serre1979local]. Our use of the graded action is narrow: Chapter IV, §2, Proposition 9 forces inversion at grade $7$, but it supplies neither the subgroup scan nor any local data for the frozen surface. Similarly, the conductor formulas convert proved fixed spaces and filtrations into exponents; they do not determine those inputs.

For cubic surfaces, Elsenhans and Jahnel give the closest explicit precedent. Their experiments include full-$W(E_6)$ examples, ramification-support calculations, and $p$-adic factor patterns [@elsenhansjahnel2009experiments Propositions 21--22, pp. 651--652]. The present paper does not rebrand the computation of ramified primes as new. It adds, for a different frozen surface, the complete higher inertia at both wild primes, the local Artin--Swan data of $(V_6,V_{20})$, and the normal-closure discriminant. Their separate study of the cubic-surface discriminant provides determinant-character context [@elsenhansjahnel2012discriminant Theorem 2.12], while the explicit maximal-order and higher-group calculations here are independent instance data.

The geometric reflection step belongs to the Picard--Lefschetz framework of SGA 7 II [@sga7ii1973]. Saito's divided-discriminant and determinant formulas make the hypersurface specialization precise [@saito2012discriminant]. Neither source identifies our three singular fibers. We verify the unique singular point, Hessian unit, critical Hensel lift, critical-value congruence, and valuation-one smoothing separately at each prime before invoking the universal reflection theorem. Published $W(E_6)$ trace conventions, including the corrected finite-field table of Banwait, Fité, and Loughran [@banwaitfite2019delpezzo], are used only to keep group labels aligned; every relevant orbit and fixed space is reconstructed from the labelled actions.

::: {#tab:precedent-boundary}
  question                                    explicit precedent                         this paper
  ------------------------------------------- ------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------
  bad-prime and $p$-adic factor information   present for other full-$W(E_6)$ examples   exact surface envelope, maximal-order rows, and field support for [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"}
  higher wild filtration                      not supplied by the cited precedent        complete lower groups at $3$ and $5$
  constituent conductors                      not supplied by the cited precedent        all local Swan/Artin pairs on $(V_6,V_{20})$
  field discriminants                         cubic discriminant context                 exact $\operatorname{Disc}(E)$ and normal-closure $\operatorname{Disc}(K)$

  : Boundary with the closest explicit cubic-surface precedent. The table compares mathematical scope, not software implementations.
:::

## Scope and organization

The decomposition ambiguity at $3$ is recorded rather than guessed. Accordingly, the paper proves no decomposition Frobenius, bad Euler polynomial or factor, epsilon factor, or root number; it also makes no holomorphy, automorphy, analytic-continuation, or functional-equation claim. This firewall appears formally in [\[rem:main-firewall\]](#rem:main-firewall){reference-type="ref" reference="rem:main-firewall"} and again in [7](#sec:infinity-scope){reference-type="ref" reference="sec:infinity-scope"}.

fixes the surface, representations, and theorem. establishes the local arithmetic and the two carrier roles. Sections [4](#sec:wild-three){reference-type="ref" reference="sec:wild-three"} and [5](#sec:five-and-tame){reference-type="ref" reference="sec:five-and-tame"} classify the wild and tame inertia. derives the conductors and discriminants, and [7](#sec:infinity-scope){reference-type="ref" reference="sec:infinity-scope"} treats infinity and the exact nonclaims. The appendices contain full arithmetic summaries, group tables, reflection witnesses, the validation map, and a source-use ledger.

# The surface, its line field, and the main theorem {#sec:setup-theorem}

## The frozen cubic and its two fields

In homogeneous coordinates $(u_0,u_1,u_2,u_3)$, let $Y=V(F)\subset\mathbf{P}^3_\mathbf{Q}$, where $$\begin{aligned}
F={}&75081586157u_0^3-28576620789u_0^2u_1
-122000922135u_0^2u_2-5364921951u_0^2u_3\notag\\
&+164150208636u_0u_1^2-415458334296u_0u_1u_2
+151070718312u_0u_1u_3\notag\\
&+1158143874300u_0u_2^2+114691988016u_0u_2u_3
+113572676646u_0u_3^2\notag\\
&+6898957820u_1^3+1132596902196u_1^2u_2
-30413540316u_1^2u_3\notag\\
&-2054867641020u_1u_2^2+151980984216u_1u_2u_3
+36794420832u_1u_3^2\notag\\
&+2646295985484u_2^3+560186573940u_2^2u_3
+706181383584u_2u_3^2+1884468968u_3^3.
\label{eq:frozen-cubic}\end{aligned}$$ The coefficients have content one and the leading coefficient is positive, so [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"} fixes the scalar convention. Exact Jacobian elimination shows that $Y$ is smooth. On the standard Grassmann chart $U_{01}$, a line is the row span of $$\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.$$ Restricting $F$ to this line gives four equations. Their quotient is a field of degree $27$, presented by a primitive irreducible eliminant $g(d)\in\mathbf{Z}[d]$. We write $$E=\mathbf{Q}[d]/(g),\qquad K=\text{the normal closure of }E.$$ The full coefficient vector of $g$, the rational back-substitutions for $a,b,c$, and the oriented field identity used by the maximal-order calculation are bound in the exact input record described in [9](#app:local){reference-type="ref" reference="app:local"}. Printing the several-page coefficient vector here would add no local argument; [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"} and the exact chart construction specify the geometric object.

The line-incidence pairing embeds the Galois action into the Weyl group of the $E_6$ root lattice. An irreducibility certificate for $g$, a modular order-five class, and an exact Picard-lattice enumeration give the frozen input $$=27,\qquad \operatorname{Gal}(K/\mathbf{Q})=W(E_6),\qquad |W(E_6)|=51840.
\label{eq:frozen-galois-input}$$ This paper does not recompute the group from ramification; instead, it determines the ramification inside the already identified group. The rational permutation module of the lines decomposes as $$\mathbf{Q}[27]=\mathbf{1}\oplus V_6\oplus V_{20}.
\label{eq:perm-decomposition}$$ The $27$-point carrier is where the two nontrivial representations live. A second permutation carrier, the $36$ double-sixes on $Y_{\overline{\mathbf{Q}}}$, separates subgroup classes that have the same line-orbit data.

## Ramification notation

Fix a finite prime $p$, an embedding $K\hookrightarrow\overline{\mathbf{Q}}_p$, a decomposition group $D_p\leq W(E_6)$, and inertia $I_p\trianglelefteq D_p$. We use the lower numbering $$I_0=I_p\supseteq I_1\supseteq I_2\supseteq\cdots.$$ For a rational representation $V$ of $W(E_6)$, put $$\begin{aligned}
 \operatorname{Sw}_p(V)&=\sum_{i\geq1}\frac{|I_i|}{|I_0|}
       \operatorname{codim}V^{I_i},\label{eq:swan-definition}\\
 a_p(V)&=\operatorname{codim}V^{I_0}+\operatorname{Sw}_p(V).
\label{eq:artin-definition}\end{aligned}$$ These formulas use inertia only. In contrast, a bad Euler polynomial would require decomposition data beyond the filtered groups determined below.

Set $$\begin{split}
 q&=14932047182473291995860108491583652133938007263719,\\
 A&=181\cdot997\cdot2346241=423395612137,\\
 B&=283\cdot1801\cdot q.
\end{split}
\label{eq:qAB}$$ Table-of-Marks labels always refer to the $350$ subgroup classes in the GAP table of marks for `U4(2).2`. They are reproducible identifiers rather than intrinsic group names.

## Main theorem

[\[thm:main\]]{#thm:main label="thm:main"} For the cubic surface [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"}, the degree-$27$ line field $E$, and its normal closure $K$, the following statements hold.

1.  The nine-prime surface divided-discriminant envelope is $$\mathcal{B}_Y=\{2,3,5,181,283,997,1801,2346241,q\},$$ whereas the finite ramified support of both $E$ and $K$ is exactly $$\mathcal{R}_{E,K}=\{3,5,181,283,997,1801,2346241,q\}.$$ In the displayed order on $\mathcal{B}_Y$, $$\bigl(v_p(\operatorname{Disc}E)\bigr)_p=(0,46,36,18,6,18,6,18,6).$$

2.  At $p=3$, inertia is subgroup $\mathrm{ToM}\,140$, with $$I_0\cong(C_3^2):C_2,\quad I_1=C_3^2,\quad
     I_2=\cdots=I_7=C_3,\quad I_8=1,$$ and the deep $C_3$ is $\mathrm{ToM}\,7$. The two and only two surviving ordered pairs are $$(D,I)=(140,140)\quad\text{or}\quad(206,140).$$ Thus $|D_3|\in\{18,36\}$ is unresolved, and $\mathrm{ToM}\,206$ is a decomposition overgroup only. At $p=5$, $$D=I_0=\ensuremath{\mathrm{ToM}\,147}\cong C_5:C_4,\qquad
     I_1=I_2=I_3=C_5,\qquad I_4=1.$$ At $181,997,2346241$, inertia is tame $\ensuremath{\mathrm{ToM}\,6}\cong C_3$. At $283,1801,q$, inertia is the tame root-reflection subgroup $\ensuremath{\mathrm{ToM}\,2}\cong C_2$.

3.  The local Swan and Artin pairs are $$\begin{array}{c|cc}
    p&\operatorname{Sw}_p(V_6,V_{20})&a_p(V_6,V_{20})\\ \hline
    3&(5,18)&(11,35)\\
    5&(3,12)&(7,29)\\
    181,997,2346241&(0,0)&(6,12)\\
    283,1801,q&(0,0)&(1,5).
    \end{array}$$ Consequently $$N(V_6)=3^{11}5^7A^6B,\qquad
     N(V_{20})=3^{35}5^{29}A^{12}B^5.$$

4.  The field discriminants are $$\operatorname{Disc}E=3^{46}5^{36}A^{18}B^6,\qquad
     \operatorname{Disc}K=3^{106560}5^{80352}A^{34560}B^{25920},$$ and $N(V_6)N(V_{20})=\operatorname{Disc}E$.

5.  The signature of $E$ is $(r_1,r_2)=(3,12)$. The subgroup generated by complex conjugation is the Table-of-Marks subgroup $\mathrm{ToM}\,5$; separately, complex conjugation belongs to character-table element-class index $17$ in `CharacterTable("U4(2).2")` under CTblLib $1.3.1$. The class has size $540$ and centralizer order $96$, and $$V_6:(d^+,d^-)=(3,3),\qquad
     V_{20}:(d^+,d^-)=(11,9).$$

The proof is local-to-global. supply exact local arithmetic and the two action carriers. prove the wild $3$-adic classification, while [\[prop:p5-pair,prop:p5-filtration,prop:tame-c3,prop:reflection\]](#prop:p5-pair,prop:p5-filtration,prop:tame-c3,prop:reflection){reference-type="ref" reference="prop:p5-pair,prop:p5-filtration,prop:tame-c3,prop:reflection"} treat the remaining ramified primes. The character calculation and both discriminants appear in [6](#sec:conductors){reference-type="ref" reference="sec:conductors"}; infinity is handled in [7](#sec:infinity-scope){reference-type="ref" reference="sec:infinity-scope"}.

[\[rem:d3-boundary\]]{#rem:d3-boundary label="rem:d3-boundary"} The notation $(D,I)$ is essential. The alternatives are $(140,140)$ and $(206,140)$, and neither alternative makes ToM $206$ an inertia group. Every invariant in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} depends on the common filtered inertia. No argument below selects between the two decomposition groups.

[\[rem:main-firewall\]]{#rem:main-firewall label="rem:main-firewall"} [No-Bad-Euler-or-Root-Number]{.smallcaps}: the theorem determines no decomposition Frobenius, bad Euler polynomial or factor, local epsilon factor, local or global root number, Artin holomorphy, automorphy, analytic continuation, or functional equation. Even a later resolution of $D_3$ would not by itself establish any of these independent assertions.

::: {#tab:hero-local}
          $p$         local arithmetic or geometric input                       lower orders $(|I_i|)_i$          inertia
  ------------------- --------------------------------------------------------- -------------------------- ---------------------
          $2$         surface envelope only; field unramified                   $(1)$                               $1$
          $3$         $(3,1,3),(6,1,7),(9,1,18)^2$                              $(18,9,3,3,3,3,3,3,1)$      $\mathrm{ToM}\,140$
          $5$         $(1,1,0)^2,(5,1,7)^3,(10,1,15)$                           $(20,5,5,5,1)$              $\mathrm{ToM}\,147$
   $181,997,2346241$  $(3,1,2),(3,2,2),(3,6,2)$ at each $p$                     $(3,1)$                      $\mathrm{ToM}\,6$
     $283,1801,q$     ordinary double point/Picard--Lefschetz; no $(e,f)$ row   $(2,1)$                      $\mathrm{ToM}\,2$

  : Complete local theorem for the frozen line field. The $p=3$ entry has two possible decomposition overgroups but one filtered inertia. Reflection-prime input is an ordinary-double-point/Picard--Lefschetz certification; no $(e,f)$ decomposition row is claimed.
:::

::: {#tab:hero-local}
          $p$          $\operatorname{Sw}(V_6,V_{20})$   $a(V_6,V_{20})$   $(v_p\operatorname{Disc}E,v_p\operatorname{Disc}K)$
  ------------------- --------------------------------- ----------------- -----------------------------------------------------
          $2$                      $(0,0)$                   $(0,0)$                             $(0,0)$
          $3$                     $(5,18)$                  $(11,35)$                         $(46,106560)$
          $5$                     $(3,12)$                  $(7,29)$                          $(36,80352)$
   $181,997,2346241$               $(0,0)$                  $(6,12)$                          $(18,34560)$
     $283,1801,q$                  $(0,0)$                   $(1,5)$                           $(6,25920)$

  : Complete local theorem for the frozen line field. The $p=3$ entry has two possible decomposition overgroups but one filtered inertia. Reflection-prime input is an ordinary-double-point/Picard--Lefschetz certification; no $(e,f)$ decomposition row is claimed.
:::

At $3$, $(D,I)=(140,140)$ or $(206,140)$; see [4](#sec:wild-three){reference-type="ref" reference="sec:wild-three"}.

# Exact local arithmetic and the two permutation carriers {#sec:local-arithmetic}

## The surface envelope and field support

An exact Macaulay resultant calculation for the four partial derivatives of $F$, divided by the standard extraneous factor, gives $$\begin{split}
\Delta_Y={}&2^{64}\cdot3^{43}\cdot5^7\cdot181^{24}\cdot283
\cdot997^{24}\cdot1801\\
&\hspace{18mm}\cdot2346241^{24}\cdot
14932047182473291995860108491583652133938007263719.
\end{split}
\label{eq:surface-divided-discriminant}$$ The determinant was evaluated by two exact engines, one using fraction-free elimination and one using exact polynomial arithmetic. Their complete matrices and determinant guards are summarized in [9](#app:local){reference-type="ref" reference="app:local"}. The factorization in [\[eq:surface-divided-discriminant\]](#eq:surface-divided-discriminant){reference-type="ref" reference="eq:surface-divided-discriminant"} is a bad-reduction envelope for the integral surface model; it is not a field discriminant.

The global maximal order $\mathcal{O}_E$ has rank $27$. Its exact discriminant has valuations $$\begin{array}{c|rrrrrrrrr}
p&2&3&5&181&283&997&1801&2346241&q\\ \hline
v_p(\operatorname{Disc}E)&0&46&36&18&6&18&6&18&6.
\end{array}
\label{eq:discE-valuation-vector}$$

[\[prop:support\]]{#prop:support label="prop:support"} The sets $\mathcal{B}_Y$ and $\mathcal{R}_{E,K}$ in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} are respectively the nine-prime set supported by [\[eq:surface-divided-discriminant\]](#eq:surface-divided-discriminant){reference-type="ref" reference="eq:surface-divided-discriminant"} and the eight-prime set obtained by deleting $2$.

Away from the support of the divided discriminant, the integral cubic has smooth reduction. The finite line scheme then extends as a finite étale scheme, so the Galois action on its geometric points is unramified. shows that all eight displayed odd primes ramify in $E$, while $2$ does not.

It remains to pass from the non-Galois field $E$ to its normal closure. At $2$, the zero permutation conductor says that inertia fixes all $27$ cosets of a line stabilizer $H\leq W(E_6)$. The kernel of this action is $\operatorname{Core}_{W(E_6)}(H)$. Since the line action in [\[eq:frozen-galois-input\]](#eq:frozen-galois-input){reference-type="ref" reference="eq:frozen-galois-input"} is faithful, this core is trivial. Thus inertia at $2$ is trivial in $K$. The same faithfulness shows that nontrivial inertia at any of the eight odd primes cannot act trivially on all $27$ lines. Hence $E$ and $K$ have the same stated support.

## Local maximal-order rows

For a prime $\mathfrak p\mid p$ of $E$, write $$e=e(\mathfrak p/p),\qquad f=f(\mathfrak p/p),\qquad
 d=v_{\mathfrak p}(\mathfrak D_{E_{\mathfrak p}/\mathbf{Q}_p}).$$ Its contribution to $v_p(\operatorname{Disc}E)$ is $fd$. Exact prime-ideal decomposition in the maximal order gives the following complete rows.

::: {#tab:local-rows}
          $p$         multiset of $(e,f,d)$              $\sum fd$   local degrees $ef$
  ------------------- --------------------------------- ----------- --------------------
          $3$         $(3,1,3),(6,1,7),(9,1,18)^2$         $46$         $(3,6,9,9)$
          $5$         $(1,1,0)^2,(5,1,7)^3,(10,1,15)$      $36$       $(1,1,5,5,5,10)$
   $181,997,2346241$  $(3,1,2),(3,2,2),(3,6,2)$            $18$          $(3,6,18)$

  : Maximal-order local rows. Every row in the last line occurs at each of the three rational primes, rather than being assigned one row per prime.
:::

The equalities $$3+7+18+18=46,\qquad 0+0+7+7+7+15=36,\qquad
2+2\cdot2+6\cdot2=18$$ are direct different calculations, made before the representation-theoretic conductor computation and used later as checks. No constituent conductor is obtained by splitting a global sum.

At the reflection primes $283,1801,q$, we deliberately do not list an $(e,f,d)$ decomposition. Their inertia is obtained by the geometric ordinary-double-point argument in [5.4](#sec:reflection){reference-type="ref" reference="sec:reflection"}. The six transpositions of a root reflection then give $v_p(\operatorname{Disc}E)=6$, consistently with [\[eq:discE-valuation-vector\]](#eq:discE-valuation-vector){reference-type="ref" reference="eq:discE-valuation-vector"}.

## The 36-point authority and its boundary

Let $\theta_{36}\in\mathbf{Z}[T]$ be the frozen degree-$36$ polynomial whose roots label the double-sixes. A second frozen polynomial $\delta_{36}$ has the same global splitting field but is not a local authority in this paper. The distinction matters because a stable-looking finite-precision factorization does not by itself identify the factors over $\mathbf{Q}_p$.

The factor-stability step uses the Krasner--Hensel criterion in the form localized in @serre1979local [Chapter II, §2, Exercises 1--2, p. 30]. For each asserted factorization, the working precision exceeds both the valuation of the global polynomial discriminant and twice the largest factor-polynomial discriminant valuation; the monic factors are simple and multiply back to the original polynomial at the same precision. The source supplies the criterion, while all exponents, factors, and inequalities below are computations for [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"}.

[\[prop:theta-authority\]]{#prop:theta-authority label="prop:theta-authority"} The polynomial $\theta_{36}$ is a certified local authority with the records in [5](#tab:theta-authority){reference-type="ref" reference="tab:theta-authority"}. No theorem assertion depends on $\delta_{36}$, and no apparent $\delta_{36}$ factorization is used as corroboration.

::: {#tab:theta-authority}
          $p$          certified precisions    factor degrees      bounds     conclusion
  ------------------- ---------------------- ------------------ ------------- ---------------------------------
          $3$            $(900,950,1000)$      $(3,3,3,9,18)$    $(886,538)$  all three precisions clear both
          $5$            $(900,950,1000)$     $(1,5,10,10,10)$   $(746,246)$  all three precisions clear both
   $181,997,2346241$       $(20,30,40)$         $(3,6,9,18)$      $(24,24)$   precision $40$ clears both

  : Certified $\theta_{36}$ factor degrees and strict precision bounds. The two bounds in the fourth column are the global polynomial-discriminant valuation and twice the largest factor-polynomial discriminant valuation.
:::

For comparison only, at the tame $C_3$ primes the global polynomial-discriminant valuation of $\delta_{36}$ is $840$, and twice its largest factor-polynomial discriminant valuation is $408$. Precision $40$ is below both values. We therefore assign $\delta_{36}$ the formal role *bounded nonresult and nondependency*. It supplies neither a premise nor a cross-check, at the tame or wild primes. Polynomial discriminants appear nowhere else in the proof: they are separation bounds, not substitutes for the field discriminants of $E$ or $K$.

## Why two actions are needed

For $D\leq W(E_6)$, its orbits on the $27$ lines have sizes equal to the local factor degrees of $g$. Its orbits on the $36$ double-sixes similarly match the certified factor degrees of $\theta_{36}$. Thus the wild targets are $$\begin{array}{c|cc}
&27\text{-line carrier}&36\text{-double-six carrier}\\ \hline
p=3&(3,6,9,9)&(3,3,3,9,18)\\
p=5&(1,1,5,5,5,10)&(1,5,10,10,10).
\end{array}
\label{eq:wild-carrier-targets}$$ The line carrier alone leaves multiple subgroup embeddings. The double-six carrier removes most of this ambiguity, but at $3$ three raw decomposition classes still have the same simultaneous orbit targets. Normality, tame-quotient structure, branchwise differents, and the graded tame action are therefore genuine proof steps, not database decoration.

The tame order-three case illustrates the same asymmetry. Two $C_3$ classes have compatible line behavior, but on double-sixes they have types $3^{12}$ and $1^3 3^{11}$. The certified $\theta_{36}$ type $3^{12}$ selects $\mathrm{ToM}\,6$; see [\[prop:tame-c3\]](#prop:tame-c3){reference-type="ref" reference="prop:tame-c3"}. The $27$-line action then supplies the $(V_6,V_{20})$ fixed spaces used for conductors.

# Wild inertia at $p=3$ {#sec:wild-three}

The prime $3$ is the only place where the filtered inertia is unique but the decomposition group is not. We retain every finite alternative until it is removed by an explicit local-field condition. This order is important: Serre's conjugation law distinguishes the last two inertia embeddings, but it does not produce the candidate list.

## Complete decomposition and inertia inventory

The local degrees in the line field and the certified double-six degrees are $$27:(3,6,9,9),\qquad 36:(3,3,3,9,18).$$ We enumerate all $350$ conjugacy classes of subgroups in the table of marks for `U4(2).2`, reconstruct their actions on both labelled carriers, and retain precisely those with the two displayed orbit partitions.

[\[prop:p3-hits\]]{#prop:p3-hits label="prop:p3-hits"} The simultaneous orbit targets have exactly three subgroup hits: $$\begin{array}{c|c|c|c}
\text{ToM index}&|H|&\operatorname{IdGroup}(H)&\text{initial role}\\ \hline
140&18&(18,4)&D\text{ or }I\\
142&18&(18,3)&D\text{ or }I\\
206&36&(36,10)&D\text{ only}.
\end{array}$$ The complete list compatible with inertia normality and a cyclic residue quotient is $$(D,I,|D/I|)=(140,140,1),(142,142,1),(206,140,2),(206,142,2).
\label{eq:p3-all-di}$$

The simultaneous orbit scan is exhaustive over the $350$ classes, so it gives the three raw hits without a subgroup-name guess. Their $3$-Sylow subgroup has order $9$. If $\mathrm{ToM}\,206$ were inertia, the quotient of order $4$ by wild inertia would be $V_4$, whereas $I_0/I_1$ must be cyclic of order prime to $3$. Hence $\mathrm{ToM}\,206$ cannot be $I_0$. It contains normal subgroups in each of the two order-$18$ classes, both with cyclic quotient of order $2$. Testing normality and the residue quotient for every ordered containment gives exactly [\[eq:p3-all-di\]](#eq:p3-all-di){reference-type="ref" reference="eq:p3-all-di"}.

The abstract group structures clarify the remaining ambiguity: $$\ensuremath{\mathrm{ToM}\,140}\cong(C_3^2):C_2,\qquad
 \ensuremath{\mathrm{ToM}\,142}\cong C_3\times S_3.$$ Both contain the required wild group $P=C_3^2$; they differ in how the tame involution acts on the eventual deep subgroup. The order-$36$ class has no role as inertia anywhere below.

## Exhausting the deep $C_3$

The four branches of $E\otimes\mathbf{Q}_3$ have target different vector $$\mathbf d=(3,7,18,18).
\label{eq:p3-target-different}$$ The tame $I_0$ contribution is $\mathbf b=(2,5,8,8)$. One lower layer equal to $P=C_3^2$ contributes $\mathbf u=(1,2,4,4)$. Let $r$ be the number of $P$ layers and $s$ the number of layers equal to a chosen deep $Q\cong C_3$. For every candidate $Q$, the branch equations are $$\mathbf b+r\mathbf u+s\mathbf w_Q=\mathbf d,\qquad
 r,s\in\mathbf{Z}_{\geq0}.
\label{eq:p3-branch-equation}$$

The deep group is not chosen by abstract isomorphism type: three different $C_3$ embeddings occur in the valid pairs. Their complete profile multiset is $\mathrm{ToM}\,6$ twice, $\mathrm{ToM}\,7$ once, and $\mathrm{ToM}\,8$ once. The two occurrences of $\mathrm{ToM}\,6$ come from distinct ordered $(D,I)$ containments; neither is suppressed before the different equation is solved.

[\[prop:p3-deep\]]{#prop:p3-deep label="prop:p3-deep"} has a nonnegative integral solution only for $Q=\ensuremath{\mathrm{ToM}\,7}$, and that solution is $(r,s)=(1,6)$. Consequently $$I_1=C_3^2,\qquad I_2=\cdots=I_7=\ensuremath{\mathrm{ToM}\,7}\cong C_3,\qquad I_8=1.$$

For $\mathrm{ToM}\,6$ and $\mathrm{ToM}\,8$, the first and third components of [\[eq:p3-branch-equation\]](#eq:p3-branch-equation){reference-type="ref" reference="eq:p3-branch-equation"} give $$r+\frac{s}{3}=1,\qquad 4r+s=10,$$ whose unique formal integral solution is $(7,-18)$. It cannot be a filtration length. For $\mathrm{ToM}\,7$, the first component gives $r=1$, and the third gives $8+4+s=18$, hence $s=6$. The second and fourth components agree. The candidate list in [\[tab:p3-deep-exhaustion\]](#tab:p3-deep-exhaustion){reference-type="ref" reference="tab:p3-deep-exhaustion"} is exhaustive, so no fourth profile remains.

The fractional entries in [\[tab:p3-deep-exhaustion\]](#tab:p3-deep-exhaustion){reference-type="ref" reference="tab:p3-deep-exhaustion"} are not rounded orbit heuristics. They are the exact normalized contributions $|Q|/|I_0|$ to the four branch permutation conductors. The negative solution therefore rejects an embedding, not merely a proposed break number.

## The odd-grade tame action

After [\[prop:p3-deep\]](#prop:p3-deep){reference-type="ref" reference="prop:p3-deep"}, the only remaining choice is how the tame quotient $C_2=I_0/I_1$ acts on the selected $Q=G_7/G_8\cong C_3$. Serre's graded action law states that, for $s\in G_0$ and $\tau\in G_i/G_{i+1}$, $$\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau).
\label{eq:serre-graded-action}$$ Here $\theta_0(s)=-1$ for the nontrivial tame involution. The precise source is @serre1979local [Chapter IV, §2, Proposition 9, pp. 69--70]. It supplies [\[eq:serre-graded-action\]](#eq:serre-graded-action){reference-type="ref" reference="eq:serre-graded-action"}; it does not identify any Table-of-Marks class for the present surface.

[\[prop:p3-serre\]]{#prop:p3-serre label="prop:p3-serre"} The inertia subgroup is $\mathrm{ToM}\,140$. The central embedding $\mathrm{ToM}\,142$ is impossible, and the final ordered pairs are exactly $$(D,I)=(140,140),\qquad(206,140).
\label{eq:p3-final-di}$$

The last nonzero grade is $i=7$. Substitution in [\[eq:serre-graded-action\]](#eq:serre-graded-action){reference-type="ref" reference="eq:serre-graded-action"} gives $$\theta_7(s\tau s^{-1})=(-1)^7\theta_7(\tau)=-\theta_7(\tau),$$ so the tame involution acts by inversion on $Q\cong C_3$. In $\mathrm{ToM}\,140$, the selected normal $\mathrm{ToM}\,7$ is inverted. In $\mathrm{ToM}\,142$, it is centralized. The latter contradicts the graded action law. Removing the two rows with inertia $142$ from [\[eq:p3-all-di\]](#eq:p3-all-di){reference-type="ref" reference="eq:p3-all-di"} leaves precisely [\[eq:p3-final-di\]](#eq:p3-final-di){reference-type="ref" reference="eq:p3-final-di"}. The selected deep subgroup is normal in each surviving decomposition group.

Serre's proposition acts only after the $350$-class scan, the four valid pairs, and the three exact deep-profile equations have been exhausted; it does not by itself select class $140$.

## Character consequences and the unresolved overgroup

The fixed dimensions for the three nontrivial layers are $$\begin{array}{c|ccc}
H&I_0=\ensuremath{\mathrm{ToM}\,140}&P=C_3^2&Q=\ensuremath{\mathrm{ToM}\,7}\\ \hline
\dim V_6^H&0&0&4\\
\dim V_{20}^H&3&4&10.
\end{array}
\label{eq:p3-fixed-dimensions}$$ Thus the tame codimensions are $(6,17)$, the $P$ codimensions are $(6,16)$, and the $Q$ codimensions are $(2,10)$. Direct substitution into [\[eq:swan-definition\]](#eq:swan-definition){reference-type="ref" reference="eq:swan-definition"} yields $$\begin{aligned}
 \operatorname{Sw}_3(V_6,V_{20})
 &=\frac9{18}(6,16)+6\frac3{18}(2,10)=(5,18),
\label{eq:p3-swan}\\
 a_3(V_6,V_{20})&=(6,17)+(5,18)=(11,35).
\label{eq:p3-artin}\end{aligned}$$ Their sum $46$ equals the direct different exponent in [4](#tab:local-rows){reference-type="ref" reference="tab:local-rows"}; [6](#sec:conductors){reference-type="ref" reference="sec:conductors"} gives the general conductor argument and branchwise checks.

The two possibilities in [\[eq:p3-final-di\]](#eq:p3-final-di){reference-type="ref" reference="eq:p3-final-di"} have orders $18$ and $36$. Both contain the same filtered inertia and the same labelled fixed spaces, so [\[eq:p3-swan,eq:p3-artin\]](#eq:p3-swan,eq:p3-artin){reference-type="ref" reference="eq:p3-swan,eq:p3-artin"} and both field discriminants are independent of this choice. A decomposition Frobenius or a bad Euler polynomial would not be independent of decomposition data. We make no such inference here, and resolving $|D_3|$ alone would still not provide epsilon factors or root numbers.

# Wild $p=5$ and the six tame primes {#sec:five-and-tame}

## The $p=5$ decomposition pair

At $5$, the two carrier partitions are $$27:(1,1,5,5,5,10),\qquad 36:(1,5,10,10,10).$$ The simultaneous scan again begins with every subgroup class rather than a presumed Frobenius group.

[\[prop:p5-pair\]]{#prop:p5-pair label="prop:p5-pair"} The raw simultaneous hits and their exact small-group identifiers are $$\begin{array}{c|c|c|c}
\text{ToM index}&|H|&\operatorname{IdGroup}(H)&\text{Sylow-}5\text{ normal?}\\ \hline
147&20&(20,3)&\text{yes}\\
247&60&(60,5)&\text{no}\\
295&120&(120,34)&\text{no}.
\end{array}$$ The only valid ordered triple is $$(D,I,|D/I|)=(147,147,1),\qquad I_0\cong C_5:C_4.$$

The three rows are the complete $350$-class simultaneous orbit scan. The first ramification group $I_1$ is the unique wild Sylow-$5$ subgroup of inertia and must be normal in $I_0$. The Sylow-$5$ subgroups of $\mathrm{ToM}\,247$ and $\mathrm{ToM}\,295$ are not normal, so neither class can be inertia. Normality and the cyclic residue-quotient test leave $\mathrm{ToM}\,147$; the orbit sizes already force $D=I$ for this class.

## The $p=5$ break equation

The six local branches have target different vector $$\mathbf d_5=(0,0,7,7,7,15).$$ The $I_0=C_5:C_4$ base contribution is $\mathbf b_5=(0,0,4,4,4,9)$. Each positive layer $C_5$ contributes $\mathbf w_5=(0,0,1,1,1,2)$. Hence the only unknown layer count $s$ satisfies $$\mathbf b_5+s\mathbf w_5=\mathbf d_5.
\label{eq:p5-layer-equation}$$

[\[prop:p5-filtration\]]{#prop:p5-filtration label="prop:p5-filtration"} has the unique nonnegative integral solution $s=3$. Thus $$I_0=C_5:C_4,\qquad I_1=I_2=I_3=C_5,\qquad I_4=1.$$

Any of the three degree-$5$ branches gives $4+s=7$, and the degree-$10$ branch gives $9+2s=15$. Both equations give $s=3$; the two unramified branches remain zero. Since [\[prop:p5-pair\]](#prop:p5-pair){reference-type="ref" reference="prop:p5-pair"} left only one inertia embedding, no competing filtration remains.

The fixed dimensions are $$\begin{array}{c|cc}
H&I_0=C_5:C_4&C_5\\ \hline
\dim V_6^H&2&2\\
\dim V_{20}^H&3&4.
\end{array}
\label{eq:p5-fixed-dimensions}$$ Therefore $$\begin{aligned}
 \operatorname{Sw}_5(V_6,V_{20})
 &=3\frac5{20}(4,16)=(3,12),\label{eq:p5-swan}\\
 a_5(V_6,V_{20})&=(4,17)+(3,12)=(7,29).
\label{eq:p5-artin}\end{aligned}$$ The sum $7+29=36$ recovers the direct different.

## Tame order-three primes

At each of $181,997,2346241$, the line carrier has inertia type $3^9$, which by itself is shared by more than one $C_3$ embedding. The double-six local rows are decisive. For $\mathrm{ToM}\,6$, they have degrees $(3,6,9,18)$, all with $e=3$, and total different exponent $24$; for the degree-only competitor, three double-sixes are fixed and the corresponding exponent is $22$. Proposition [\[prop:theta-authority\]](#prop:theta-authority){reference-type="ref" reference="prop:theta-authority"} certifies the first set of rows from $\theta_{36}$, with no use of $\delta_{36}$.

[\[prop:tame-c3\]]{#prop:tame-c3 label="prop:tame-c3"} At $p=181,997,2346241$, inertia is $\ensuremath{\mathrm{ToM}\,6}\cong C_3$. Its line type is $3^9$, its double-six type is $3^{12}$, and $$\dim(V_6^{C_3},V_{20}^{C_3})=(0,8),\qquad
 a_p(V_6,V_{20})=(6,12).$$

The line decomposition rows permit two $C_3$ classes. The certified $\theta_{36}$ rows have double-six type $3^{12}$, selecting $\mathrm{ToM}\,6$ over the class with type $1^3 3^{11}$. Since the place is tame, the conductor is the codimension of the invariant space. The labelled line matrices give fixed dimensions $(0,8)$, hence codimensions $(6,12)$.

## Reflection primes {#sec:reflection}

The primes $283,1801,q$ are treated geometrically. For each $p$, reduce the integral surface equation modulo $p$ and split projective space into the four disjoint pivot strata $$u_0=\cdots=u_{j-1}=0,\qquad u_j=1\qquad(0\leq j\leq3).$$ On each stratum, eliminate the four specialized homogeneous partial derivatives in the remaining coordinates. The calculation produces one reduced point on pivot stratum $0$ and a unit ideal on strata $1,2,3$. (Euler's identity, with $p\ne3$, puts every common gradient zero on the surface.) At the unique point the three-by-three affine Hessian is invertible.

The invertible Hessian does two jobs. First, it proves that the special-fiber singularity is an ordinary quadratic singularity. Second, Hensel's lemma applied to the affine gradient gives a unique critical-point lift modulo $p^2$. Direct substitution shows that the lifted critical value is congruent modulo $p^2$ to the value at the integer representative, and that $F(P)/p$ is nonzero modulo $p$. Thus the smoothing parameter has valuation exactly one. The total space is regular and meets the discriminant transversely.

For odd residue characteristic, the Picard--Lefschetz formula identifies the tame monodromy around such a transverse ordinary quadratic singularity with reflection in the vanishing root; see SGA 7 II, Exposé XV [@sga7ii1973], and the cubic-surface determinant specialization in @saito2012discriminant [Proposition 2.3, p. 858; Theorem 3.5, pp. 864--866; cubic-surface specialization, p. 870]. These sources provide the universal implication. The singular points, Hessians, lifts, and valuation-one assertions are the exact instance calculations recorded in [11](#app:reflection){reference-type="ref" reference="app:reflection"}.

The finite-group side is also exhaustive. There are four classes of subgroups generated by an involution, and their two carrier types are as follows.

[\[prop:reflection\]]{#prop:reflection label="prop:reflection"} At each of $283,1801,q$, inertia is the tame root-reflection subgroup $\mathrm{ToM}\,2$. Its Swan pair is $(0,0)$, and its Artin pair is $(1,5)$. This is geometric ordinary-double-point/Picard--Lefschetz certification; no $(e,f)$ decomposition row is claimed.

The exact chart, Hessian, Hensel, critical-value, and valuation computation proves the hypotheses of the odd-characteristic Picard--Lefschetz formula, so a tame generator acts as an $E_6$ root reflection. On the $27$ lines, a root reflection has type $1^{15}2^6$; on the $36$ double-sixes it has type $1^{16}2^{10}$. The exhaustive comparison in [\[tab:order-two-profiles\]](#tab:order-two-profiles){reference-type="ref" reference="tab:order-two-profiles"} uniquely identifies $\mathrm{ToM}\,2$. The fixed dimensions $(5,15)$ give tame codimensions $(1,5)$, and tame inertia has zero Swan conductor.

It is tempting to reverse the argument and infer a local factor row from the six transpositions. We do not do so. The geometry determines the inertia conjugacy class and hence the permutation conductor $6$; it does not determine the decomposition or residue degrees of the primes of $E$ above a reflection prime.

# Artin--Swan conductors and the two discriminants {#sec:conductors}

## Layerwise character calculation

The Artin formula [\[eq:artin-definition\]](#eq:artin-definition){reference-type="ref" reference="eq:artin-definition"} separates the tame codimension at $I_0$ from the positive layers. All fixed spaces are computed from the labelled $27$-line action, not reconstructed from the total discriminant exponent. The data needed for every ramified type fit in one table.

At $3$, the positive-layer contribution is $$\frac12(6,16)+6\frac16(2,10)=(5,18),$$ and adding the $I_0$ codimensions gives $(11,35)$. At $5$, $$3\frac14(4,16)=(3,12),$$ and adding $(4,17)$ gives $(7,29)$. The tame rows have no positive lower group, so their Swan conductors vanish and their Artin conductors are the final codimension column.

[\[prop:local-conductors\]]{#prop:local-conductors label="prop:local-conductors"} The local pairs are exactly those in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(c). In particular, every Swan conductor and every Artin conductor is a nonnegative integer obtained layer by layer.

The wild calculations are the exact weighted sums above. At each tame $C_3$ prime, [\[prop:tame-c3\]](#prop:tame-c3){reference-type="ref" reference="prop:tame-c3"} supplies fixed dimensions $(0,8)$, hence codimensions $(6,12)$. At each reflection prime, [\[prop:reflection\]](#prop:reflection){reference-type="ref" reference="prop:reflection"} supplies $(5,15)$, hence $(1,5)$. Outside the eight-prime support inertia is trivial. These cases exhaust all finite primes by [\[prop:support\]](#prop:support){reference-type="ref" reference="prop:support"}.

## Branchwise conductor--different closure

For a finite separable extension, the Artin conductor of its permutation representation is the discriminant exponent; see @serre1979local [Chapter VI, §2, Corollary $1'$, pp. 100--101, and §3, Proposition 6 and Corollary 1, pp. 103--104]. Applied locally to each orbit of $D_p$ on the $27$ embeddings, this identifies the branch permutation conductor with $f_{\mathfrak p}d_{\mathfrak p}$.

[\[prop:branchwise-closure\]]{#prop:branchwise-closure label="prop:branchwise-closure"} For every local branch at $3,5,181,997,2346241$, the permutation conductor computed from the proved lower filtration equals the direct maximal-order different contribution. Summing the branches gives $46$, $36$, and $18$ for the three prime types. At a reflection prime, the six transpositions give conductor $6$, equal to the global maximal-order valuation.

For the maximal-order primes, restrict the $27$-point permutation action to each $D_p$ orbit and apply the local conductor--different identity. The orbit refinements used in [\[eq:p3-branch-equation,eq:p5-layer-equation\]](#eq:p3-branch-equation,eq:p5-layer-equation){reference-type="ref" reference="eq:p3-branch-equation,eq:p5-layer-equation"} give the direct rows in [4](#tab:local-rows){reference-type="ref" reference="tab:local-rows"}, rather than merely their totals. For a tame reflection the Artin conductor of a permutation is the codimension of its fixed subspace: six disjoint transpositions have $21$ orbits on $27$ points, so the codimension is $27-21=6$. supplies the independent global-order value.

The decomposition [\[eq:perm-decomposition\]](#eq:perm-decomposition){reference-type="ref" reference="eq:perm-decomposition"} now gives $$a_p(V_6)+a_p(V_{20})=v_p(\operatorname{Disc}E)
\label{eq:local-conductor-disc-check}$$ at every $p$. We emphasize the direction of use: the fixed-space calculation proves the two summands, and [\[eq:local-conductor-disc-check\]](#eq:local-conductor-disc-check){reference-type="ref" reference="eq:local-conductor-disc-check"} checks them. The equality is not used to guess one constituent from the other.

## Global representation conductors and $\operatorname{Disc}E$

Multiplying the local powers in [\[prop:local-conductors\]](#prop:local-conductors){reference-type="ref" reference="prop:local-conductors"} yields:

[\[cor:global-conductors\]]{#cor:global-conductors label="cor:global-conductors"} With $A,B$ as in [\[eq:qAB\]](#eq:qAB){reference-type="ref" reference="eq:qAB"}, $$N(V_6)=3^{11}5^7A^6B,\qquad
 N(V_{20})=3^{35}5^{29}A^{12}B^5.$$ Moreover, $$N(V_6)N(V_{20})
 =3^{46}5^{36}A^{18}B^6
 =\operatorname{Disc}E.
\label{eq:global-conductor-disc}$$

At $3$ and $5$ use the exponents $(11,35)$ and $(7,29)$. Each of the three factors of $A$ carries exponents $(6,12)$; each of the three factors of $B$ carries exponents $(1,5)$. Addition of the two exponent vectors gives $46,36,18,6$ by prime type. The maximal-order discriminant has exactly these valuations and is positive, proving [\[eq:global-conductor-disc\]](#eq:global-conductor-disc){reference-type="ref" reference="eq:global-conductor-disc"}.

The exact field discriminant also closes the support argument. No finite prime outside the displayed eight can act nontrivially on the $27$ roots. Because the $W(E_6)$ action on those roots is faithful, no hidden inertia can survive in $K$ while disappearing from $E$.

## The normal-closure discriminant

For a Galois extension with group $G$ and lower inertia $I_i$, the exponent of the regular permutation discriminant is $$v_p(\operatorname{Disc}K)=\frac{|G|}{|I_0|}
 \sum_{i\geq0}(|I_i|-1).
\label{eq:regular-disc-formula}$$ The factor $|G|/|I_0|$ accounts for the regular representation, while the sum is the local different of the completed Galois extension. In particular, $D_p$ does not occur.

::: {#tab:discK-exponents}
         type              $(|I_i|)_i$         $\sum_i(|I_i|-1)$   $51840/|I_0|$   $v_p(\operatorname{Disc}K)$
  ------------------ ------------------------ ------------------- --------------- -----------------------------
        $p=3$         $(18,9,3,3,3,3,3,3,1)$          37               2880                  106560
        $p=5$             $(20,5,5,5,1)$              31               2592                   80352
      tame $C_3$             $(3,1)$                   2               17280                  34560
   reflection $C_2$          $(2,1)$                   1               25920                  25920

  : Regular-representation discriminant calculation by inertia type.
:::

For example, at $3$ the sum is $$(18-1)+(9-1)+6(3-1)=37,$$ and $2880\cdot37=106560$. At $5$, $(20-1)+3(5-1)=31$, and $2592\cdot31=80352$.

[\[prop:discK\]]{#prop:discK label="prop:discK"} One has $$\operatorname{Disc}K=3^{106560}5^{80352}A^{34560}B^{25920}.$$ This formula is independent of the alternatives $(D,I)=(140,140)$ and $(206,140)$ at $3$.

Insert the four proved filtration types in [\[eq:regular-disc-formula\]](#eq:regular-disc-formula){reference-type="ref" reference="eq:regular-disc-formula"}; [6](#tab:discK-exponents){reference-type="ref" reference="tab:discK-exponents"} lists every arithmetic step. The eight-prime support is exact by [\[prop:support\]](#prop:support){reference-type="ref" reference="prop:support"}. Since only $I_i$ appears in [\[eq:regular-disc-formula\]](#eq:regular-disc-formula){reference-type="ref" reference="eq:regular-disc-formula"}, the order of the decomposition overgroup at $3$ is irrelevant. These calculations first give $|\operatorname{Disc}K|$. Because $K/\mathbf{Q}$ is Galois of degree $51840$, it is either totally real or totally imaginary; in the latter case $r_2(K)=25920$ is even. Hence $\operatorname{sgn}(\operatorname{Disc}K)=(-1)^{r_2(K)}=1$, proving the displayed positive formula.

The prime-power formulas, rather than expanded decimal integers, are the mathematical statements. For transport checking, the decimal value of $\operatorname{Disc}E$ has $586$ digits and that of $\operatorname{Disc}K$ has $1{,}931{,}353$ digits; their byte guards are recorded only in [12](#app:certificate){reference-type="ref" reference="app:certificate"}.

# Infinity, exact scope, and validation boundary {#sec:infinity-scope}

## Archimedean type

The maximal-order field computation gives $$(r_1(E),r_2(E))=(3,12).
\label{eq:E-signature}$$ Thus complex conjugation fixes three of the $27$ embeddings and exchanges the remaining $24$ in pairs: its line type is $1^3 2^{12}$. Independently, exact Sturm counting gives four real roots of $\theta_{36}$, hence double-six type $1^4 2^{16}$.

The simultaneous order-two table is [\[tab:order-two-profiles\]](#tab:order-two-profiles){reference-type="ref" reference="tab:order-two-profiles"}. The line type alone would permit both $\mathrm{ToM}\,3$ and $\mathrm{ToM}\,5$; the double-six type selects $\mathrm{ToM}\,5$. The finite-field class conventions in @banwaitfite2019delpezzo [Table 7.1] provide useful context for $W(E_6)$ labels, but the match here comes from the two exact real-root counts and the reconstructed actions.

[\[prop:infinity\]]{#prop:infinity label="prop:infinity"} The subgroup generated by complex conjugation is the Table-of-Marks subgroup $\mathrm{ToM}\,5$. Under CTblLib $1.3.1$, complex conjugation itself lies in element-class index $17$ of `CharacterTable("U4(2).2")`; that class has size $540$ and centralizer order $96$. Its plus/minus dimensions are $$V_6:(d^+,d^-)=(3,3),\qquad
 V_{20}:(d^+,d^-)=(11,9).$$

Among the four order-two subgroup profiles, only $\mathrm{ToM}\,5$ has the pair of carrier types $1^3 2^{12}$ and $1^4 2^{16}$. Its fixed dimensions on $(V_6,V_{20})$ are $(3,11)$. Since complex conjugation has order two, these are the plus dimensions; subtracting from $6$ and $20$ gives the minus dimensions. A separate reconstruction in the character table finds one order-two element class with size $540$ and centralizer $96$, namely index $17$.

The first-use convention is therefore: *Table-of-Marks subgroup $\mathrm{ToM}\,5$ / character-table element-class index $17$ (CTblLib $1.3.1$)*. The integers $5$ and $17$ belong to different indexing systems. Neither is a root number.

## What the theorem does not determine

The firewall is a mathematical dependency statement. use only the filtration $I_i$, so the two possible $D_3$ overgroups are irrelevant to every quantity computed here. A bad Euler factor instead depends on a lift of residue Frobenius through $D_3/I_0$, and epsilon factors require additional representation-theoretic and additive-character data. None of these inputs is reconstructed by the present calculations.

Two other boundaries prevent local evidence from being silently enlarged. First, $\theta_{36}$ is the only certified degree-$36$ local authority; $\delta_{36}$ is a bounded nonresult and contributes neither a premise nor corroboration. Second, the reflection primes have geometric ordinary-double-point/Picard--Lefschetz certification; no $(e,f)$ decomposition row is claimed. The paper also proves no rational-point, local-point, weak-approximation, Hasse-principle, or Brauer--Manin assertion for $Y$, and no theorem for all cubic surfaces or all line fields.

## Auxiliary exact validation

The finite calculations entering the propositions above admit an independent successful reconstruction from two immutable evidence carriers under a strict schema. The claim-to-artifact map, software versions, digest guards, and semantic perturbations are given in [12](#app:certificate){reference-type="ref" reference="app:certificate"}. Those operational records validate the exact inputs; they are not a separate mathematical contribution and do not replace any written bridge in [\[sec:local-arithmetic,sec:wild-three,sec:five-and-tame,sec:conductors\]](#sec:local-arithmetic,sec:wild-three,sec:five-and-tame,sec:conductors){reference-type="ref" reference="sec:local-arithmetic,sec:wild-three,sec:five-and-tame,sec:conductors"}.

# Conclusion {#sec:conclusion}

For the explicit cubic surface [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"}, the ramification of the $27$-line field is now determined at the level of lower inertia groups rather than only by its support or total discriminant. The key local fact is the $3$-adic classification: a complete decomposition/inertia inventory, the $\mathrm{ToM}\,6$$\times2$, $\mathrm{ToM}\,7$, and $\mathrm{ToM}\,8$ branch-different exhaustion, and Serre's odd-grade conjugation law leave one filtered inertia. The analogous normality and layer equations settle $5$, while certified double-six partitions distinguish the tame $C_3$ class and exact ordinary-double-point geometry gives root reflections at the remaining primes.

These filtrations determine all local Swan and Artin conductors of $(V_6,V_{20})$. Their products recover the degree-$27$ discriminant, and the regular representation gives the $1{,}931{,}353$-digit normal-closure discriminant in a compact prime-power factorization. The same two permutation carriers distinguish complex conjugation and yield the archimedean plus/minus dimensions.

One local question remains deliberately open: the decomposition group at $3$ has order $18$ or $36$. Both options contain the same filtered inertia $\mathrm{ToM}\,140$, so they change none of the results proved here. They also do not furnish bad Euler, epsilon, or root-number data. Resolving that overgroup would require new local evidence, and any analytic consequence would require further independent input.

Two natural continuations are therefore separate from the present theorem. One is to recover the missing decomposition information at $3$ without weakening the exact local-field standard used here. The other is to compute equally complete filtered-inertia packages for additional explicit full-$W(E_6)$ cubic surfaces, allowing genuine comparison of wild embeddings rather than comparison of bad-prime lists alone.

# Frozen inputs, local orders, and authority bounds {#app:local}

## Exact algebraic input

The primitive coefficient array of [\[eq:frozen-cubic\]](#eq:frozen-cubic){reference-type="ref" reference="eq:frozen-cubic"} has $20$ entries. The four Grassmann-chart equations are obtained by the direct substitution $$(u_0,u_1,u_2,u_3)=(s,t,as+ct,bs+dt)$$ and equating the coefficients of $s^3,s^2t,st^2,t^3$. A degree-order basis has Hilbert counts $(1,4,10,12,0)$; lexicographic conversion produces an eliminant $g(d)$ of degree $27$ and rational back-substitutions for $a,b,c$. Substituting those expressions into all four chart equations, clearing denominators, and reducing modulo $g$ gives four zero remainders. The complement of the chart is empty by five independent unit-ideal calculations.

The maximal-order calculation uses a transformed monic degree-$27$ polynomial together with an oriented isomorphism back to the original class of $d$. The orientation is part of the input: the original eliminant generator maps to a rational polynomial in the transformed generator. The full numerator vector is too large for print, so the following canonical guards identify it and the integral basis without abbreviation at the data layer.

::: {#tab:field-input-guards}
  object                                  SHA-256 or exact property
  --------------------------------------- ---------------------------------------------
  oriented original-generator image       ``
  transformed monic polynomial            ``
  canonical $27$-element integral basis   ``
  PARI textual basis carrier              ``; $4{,}549{,}955$ bytes
  maximality certification                no unresolved prime returned by `nfcertify`

  : Compact guards for the exact field presentation.
:::

The semantics of `nfbasis`, `nfinit`, `idealprimedec`, `nfcertify`, and `polsturm` are those of the PARI/GP user's guide [@parigroup2021]. The software reference does not certify any displayed output; exact carriers and independent reconstruction do.

## Divided discriminant engines

The Macaulay construction uses a $56\times56$ matrix and a $24\times24$ extraneous block. Fraction-free determinant evaluation and an independent exact polynomial engine give the same quotient. Its decimal-newline guard is $$\texttt{2be931285c05779d59f6d7f9f7006bd87a3c36e72c4d57dab7315413a3672ed9},$$ and its prime factorization is exactly [\[eq:surface-divided-discriminant\]](#eq:surface-divided-discriminant){reference-type="ref" reference="eq:surface-divided-discriminant"}. The field discriminant, computed from the integral basis rather than this resultant, is positive with $586$ digits and guard $$\texttt{7548db5eb3f1c5549d80f6125521e9f3c7f965fb39b7198a8d28f93e8f78d6ca}.$$ The different origin of these two integers is why the nine-prime surface envelope and eight-prime field support remain separate throughout the paper.

## Complete local-row summary

For readability, repeated rows are compressed only by their multiplicity.

::: {#tab:appendix-local-rows}
      $p$       multiplicity   degree $ef$   $e$   $f$   $d$   $fd$
  ----------- -------------- ------------- ----- ----- ----- ------
      $p$       multiplicity   degree $ef$   $e$   $f$   $d$   $fd$
      $3$                  1             3     3     1     3      3
                           1             6     6     1     7      7
                           2             9     9     1    18     18
      $5$                  2             1     1     1     0      0
                           3             5     5     1     7      7
                           1            10    10     1    15     15
     $181$                 1             3     3     1     2      2
                           1             6     3     2     2      4
                           1            18     3     6     2     12
     $997$                 1             3     3     1     2      2
                           1             6     3     2     2      4
                           1            18     3     6     2     12
   $2346241$               1             3     3     1     2      2
                           1             6     3     2     2      4
                           1            18     3     6     2     12

  : All maximal-order local rows used in the theorem.
:::

The prime-ideal HNF carriers and prime-vector complements are retained in the arithmetic evidence rather than typeset: they occupy several megabytes and do not shorten any proof. Their canonical aggregate guard is $$\texttt{ee43a97eb36fdfb21565b339da78b7b2a4e73ef226e34b49223f127a1617ae4a}.$$

## All certified $\theta_{36}$ factor rows

At $3$ and $5$, the factor rows remain identical at precisions $900,950,1000$, every factor is monic and simple, and the minimum coefficientwise multiply-back valuations are exactly $900,950,1000$. The compressed rows are:

::: {#tab:wild-theta-factor-rows}
   $p$   count   factor degree   mod-$p$ exponent   residual degree   factor poldisc exponent
  ----- ------- --------------- ------------------ ----------------- -------------------------
   $3$     3           3                3                  1                    11
           1           9                9                  1                    62
           1          18                18                 1                    269
   $5$     1           1                1                  1                     0
           1           5                5                  1                    27
           3          10                10                 1                    123

  : Wild $\theta_{36}$ factor rows. The last column is the polynomial-discriminant valuation of one factor.
:::

Thus the global/twice-largest bounds are $886/538$ at $3$ and $746/246$ at $5$. All three precisions exceed both numbers.

At each of $181,997,2346241$, the $\theta_{36}$ rows are $$\begin{array}{c|rrrr}
\text{factor degree}&3&6&9&18\\ \hline
e&3&3&3&3\\
f&1&2&3&6\\
d&2&2&2&2\\
\text{factor poldisc exponent}&2&4&6&12.
\end{array}
\label{eq:tame-theta-rows}$$ Their field-different contributions sum to $24$, the global polynomial-discriminant exponent is $24$, and twice the largest factor exponent is $24$. Precision $40$ clears both bounds, and factor multiplication is verified at $20,30,40$.

For $\delta_{36}$, the same apparent factor degrees at tame precision have factor polynomial-discriminant exponents $4,20,48,204$. Hence the twice-largest bound is $408$, while the global exponent is $840$. Precision $40$ clears neither. No $\delta_{36}$ row, at any prime, is used to prove or corroborate a local partition. This negative authority statement is part of the premise graph, not an observation omitted from the successful lane.

# Exhaustive subgroup and fixed-space ledgers {#app:groups}

This appendix records the finite-group part of the proof independently of the local-arithmetic carriers in [9](#app:local){reference-type="ref" reference="app:local"}. Throughout, "ToM" means the fixed ordering of the $350$ conjugacy classes in `TableOfMarks("U4(2).2")`. A label is therefore a reproducibility coordinate, not an intrinsic name for a subgroup. Every retained class was reconstructed as a permutation subgroup on the labelled sets of $27$ lines and $36$ double-sixes. The GAP, TomLib, and CTblLib conventions are those recorded in [@gap2021; @tomlib2019; @ctbllib2020]; none of those software references supplies an instance calculation for the surface.

## Search predicate and branch contributions

For a subgroup $H\leq W(E_6)$, write $$\lambda_{27}(H)=\bigl(|\Omega|:\Omega\in H\backslash\{1,\ldots,27\}\bigr),
 \qquad
 \lambda_{36}(H)=\bigl(|\Xi|:\Xi\in H\backslash\{1,\ldots,36\}\bigr),$$ with each tuple sorted increasingly. The first pass compares these tuples with the exact local degrees. A proposed ordered pair $(D,I)$ is then kept only when $I\trianglelefteq D$, the prescribed wild Sylow subgroup is normal in $I$, and $D/I$ is cyclic. At $p=3$ we additionally require $I/P$ to be cyclic of order prime to $3$, where $P$ is the wild Sylow subgroup. These tests are run over all ordered containments between the $350$ reconstructed classes; no abstract subgroup name is used as a search seed.

The branch-different calculation can be stated directly on the line action. Let $\Omega_1,\ldots,\Omega_t$ be the $I_0$-orbits. For $H\leq I_0$, put $$c_j(H)=\frac{|H|}{|I_0|}
 \left(|\Omega_j|-\#(H\backslash\Omega_j)\right).
 \label{eq:branch-layer-contribution}$$ Thus one lower layer equal to $H$ contributes $(c_1(H),\ldots,c_t(H))$ to the branch different vector. Formula [\[eq:branch-layer-contribution\]](#eq:branch-layer-contribution){reference-type="ref" reference="eq:branch-layer-contribution"} is simply the Artin conductor formula for the permutation module, separated over the $I_0$-orbits. In particular its entries are rational before the complete filtration is assembled; they must not be rounded.

## The complete $p=3$ ledger

The simultaneous target is $$\lambda_{27}=(3,6,9,9),\qquad
 \lambda_{36}=(3,3,3,9,18).$$ The raw and containment passes give exactly the following data.

::: {#tab:app-p3-pairs}
   $D$ ToM   $|D|$   $\operatorname{IdGroup}(D)$   $I$ ToM   $|D/I|$   status before deep scan
  --------- ------- ----------------------------- --------- --------- -------------------------
     140      18              $(18,4)$               140        1               valid
     142      18              $(18,3)$               142        1               valid
     206      36              $(36,10)$              140        2          valid; $D$ only
     206      36              $(36,10)$              142        2          valid; $D$ only

  : All $p=3$ simultaneous hits and all valid ordered pairs.
:::

There are no other raw hits: they are ToM $140$, $142$, and $206$ only. The last class cannot be inertia because its quotient by its order-$9$ wild subgroup has order $4$ and is not cyclic. It is retained in [10](#tab:app-p3-pairs){reference-type="ref" reference="tab:app-p3-pairs"} solely as a decomposition overgroup.

For every occurrence of a normal order-$3$ subgroup compatible with one of these four pairs, [\[eq:branch-layer-contribution\]](#eq:branch-layer-contribution){reference-type="ref" reference="eq:branch-layer-contribution"} gives the following complete multiset. Keeping the multiplicity two for ToM $6$ is necessary: the two entries come from different ordered containments.

Here the target is $(3,7,18,18)$ and one $P=C_3^2$ layer contributes $(1,2,4,4)$. Solving $$(2,5,8,8)+r(1,2,4,4)+s\mathbf c(Q)=(3,7,18,18)$$ over exact fractions produces the last column. Only ToM $7$ gives a nonnegative integral solution. It gives one $P$ layer and six $Q$ layers. The grade-$7$ inversion test of [\[prop:p3-serre\]](#prop:p3-serre){reference-type="ref" reference="prop:p3-serre"} then removes the two rows with inertia ToM $142$, leaving $(D,I)=(140,140)$ and $(206,140)$. This last test changes neither the deep profile nor the unresolved order of $D$.

## The complete $p=5$ and involution ledgers

At $p=5$ the target pair is $$(1,1,5,5,5,10),\qquad (1,5,10,10,10).$$ All raw simultaneous hits and the normal-Sylow test are reproduced below.

::: {#tab:app-p5-hits}
   ToM   order   $\operatorname{IdGroup}$   Sylow $5$ normal?          conclusion
  ----- ------- -------------------------- ------------------- ---------------------------
   147    20             $(20,3)$                  yes          $(D,I,|D/I|)=(147,147,1)$
   247    60             $(60,5)$                  no              excluded as inertia
   295    120           $(120,34)$                 no              excluded as inertia

  : All $p=5$ hits; the first row is the unique valid inertia class.
:::

The base branch vector is $(0,0,4,4,4,9)$, one $C_5$ layer contributes $(0,0,1,1,1,2)$, and the target is $(0,0,7,7,7,15)$. Hence precisely three positive layers occur. This recovers the lower orders $(20,5,5,5,1)$ without importing a break from the abstract group.

For completeness, the exhaustive order-two scan contains four classes. The two permutation profiles, rather than order alone, distinguish a root reflection from complex conjugation.

For a subgroup of order two, its normalizer equals its centralizer. The reflection geometry selects subgroup ToM $2$. At infinity the simultaneous line/double-six profile selects subgroup ToM $5$; only after this subgroup selection does the character table identify element-class index $17$.

## Fixed spaces and conductor arithmetic

The fixed spaces were computed from the labelled rational matrices for $V_6$ and $V_{20}$, not inferred from subgroup order. The complete list used in the paper is $$\begin{array}{c|c|c|c}
\text{place or role}&H&\dim(V_6^H,V_{20}^H)&
\operatorname{codim}(V_6^H,V_{20}^H)\\ \hline
p=3,\ I_0&\ensuremath{\mathrm{ToM}\,140}&(0,3)&(6,17)\\
p=3,\ I_1&C_3^2&(0,4)&(6,16)\\
p=3,\ I_2=\cdots=I_7&\ensuremath{\mathrm{ToM}\,7}&(4,10)&(2,10)\\
p=5,\ I_0&\ensuremath{\mathrm{ToM}\,147}&(2,3)&(4,17)\\
p=5,\ I_1=I_2=I_3&C_5&(2,4)&(4,16)\\
\text{tame }C_3&\ensuremath{\mathrm{ToM}\,6}&(0,8)&(6,12)\\
\text{reflection}&\ensuremath{\mathrm{ToM}\,2}&(5,15)&(1,5)\\
\text{complex conjugation}&\ensuremath{\mathrm{ToM}\,5}&(3,11)&(3,9)
\end{array}
\label{eq:app-fixed-space-ledger}$$ Substitution into the lower-numbering formula gives, with no omitted layer, $$\begin{aligned}
 \operatorname{Sw}_3&=\frac9{18}(6,16)+6\frac3{18}(2,10)=(5,18),\\
 \operatorname{Sw}_5&=3\frac5{20}(4,16)=(3,12).
\end{aligned}$$ Adding the $I_0$ codimensions gives $(11,35)$ and $(7,29)$, respectively. For the tame rows the Swan term is zero and the final column of [\[eq:app-fixed-space-ledger\]](#eq:app-fixed-space-ledger){reference-type="ref" reference="eq:app-fixed-space-ledger"} is already the Artin pair.

Finally, the normal-closure exponents provide a group-order check that is manifestly independent of $D_3$. For a Galois extension with group $G$ and lower inertia groups $I_i$, $$v_p(\operatorname{Disc}K)=\frac{|G|}{|I_0|}\sum_{i\geq0}(|I_i|-1).
 \label{eq:galois-disc-local}$$ With $|G|=51840$, the four local sums and multipliers are $$\begin{array}{c|c|c|c}
p&\sum_i(|I_i|-1)&|G|/|I_0|&v_p(\operatorname{Disc}K)\\ \hline
3&37&2880&106560\\
5&31&2592&80352\\
181,997,2346241&2&17280&34560\\
283,1801,q&1&25920&25920.
\end{array}$$ This calculation uses $I_0$ and its filtration only; the two possible decomposition-group orders at $3$ therefore give the same result.

# Exact reflection geometry at the three large-support primes {#app:reflection}

We give the instance part of the ordinary-double-point argument used in [5.4](#sec:reflection){reference-type="ref" reference="sec:reflection"}. This appendix deliberately contains no local factorization or $(e,f)$ row: the output is an inertia class obtained from geometry.

## Singular loci on four disjoint pivot strata

For $j=0,1,2,3$, let the $j$th pivot stratum be $$u_0=\cdots=u_{j-1}=0,\qquad u_j=1,$$ with $u_{j+1},\ldots,u_3$ as its remaining coordinates. These strata are disjoint and exhaust projective space. Over $\mathbf{F}_p$ we specialize the four homogeneous first derivatives of $F$ to each stratum and compute their reduced Gröbner basis. Since $p\ne3$, Euler's identity implies that a common gradient zero also lies on $F=0$. In every case below, the stratum-$0$ ideal has the displayed reduced linear basis, whereas the ideals on strata $1,2,3$ reduce to the unit ideal. Thus the projective singular locus consists of exactly one reduced point.

::: {#tab:reflection-singular-points}
  $p$      reduced stratum-$0$ basis         unique projective point $P_p$
  -------- --------------------------------- -------------------------------
  $p$      reduced stratum-$0$ basis         unique projective point $P_p$
  $283$    $x_1+217,\ x_2+128,\ x_3+158$     $[1,66,155,125]$
  $1801$   $x_1+364,\ x_2+1263,\ x_3+1290$   $[1,1437,538,511]$
  $q$      $x_1+$``, $x_2+$``, $x_3+$``      $[1,$ ``, ``, ``$]$

  : Exact pivot-stratum-$0$ singular-locus carriers.
:::

The coordinates in the third row are reduced to the interval $[0,q-1]$; the linear-basis constants are their negatives modulo $q$. The unit-ideal outcomes on the other three pivot strata complete the projective exhaustion; they are not overlapping affine-chart tests of the same point.

## Hessians and first Hensel corrections

Put $f=f_0=F(1,x_1,x_2,x_3)$. The affine Hessian matrices at the points of [12](#tab:reflection-singular-points){reference-type="ref" reference="tab:reflection-singular-points"}, reduced modulo $p$, are $$\begin{aligned}
H_{283}&=
\begin{pmatrix}
146&136&91\\136&13&203\\91&203&263
\end{pmatrix},\\[3pt]
H_{1801}&=
\begin{pmatrix}
276&326&379\\326&700&902\\379&902&1796
\end{pmatrix},\\[3pt]\end{aligned}$$ Write $H_q=(h_{ij})_{1\leq i,j\leq3}$, with $h_{ij}=h_{ji}$. Its six independent entries are $$\begin{aligned}
h_{11}&=1311544089871005361766843220403139014755424019851,\\
h_{12}&=9978936465940142019654684549662337052767937590180,\\
h_{13}&=8612858348525205055038179080298823074941248581837,\\
h_{22}&=2137397871150289173057311598746005216526412381550,\\
h_{23}&=253346114695653176136051595749839977708789738244,\\
h_{33}&=14594568215694396621068754907779675489233126539611.\end{aligned}$$ Their determinants modulo $p$ are respectively $$228,\qquad 1387,\qquad
 6136116089260018682592250996037036352166217747437,
 \label{eq:reflection-hessian-dets}$$ and are nonzero. Consequently each singularity is an ordinary quadratic singularity, and the gradient map has a unique zero lifting $P_p$ modulo $p^2$.

For transparency, write $$\mathbf g_p=\frac{\nabla f(P_p)}p\pmod p,\qquad
 H_p\mathbf c_p=-\mathbf g_p\pmod p.$$ The exact reduced vectors are $$\begin{aligned}
\mathbf g_{283}&=(141,174,163),&
\mathbf c_{283}&=(222,71,239),\\
\mathbf g_{1801}&=(508,508,1167),&
\mathbf c_{1801}&=(495,192,1792).\end{aligned}$$ For the large prime, the two triples are $$\begin{aligned}
\mathbf g_q={}&\bigl(
3555487038157581200031692877049198796770382105104,\\[-2pt]
&\quad 8802808374986467697053812449802016955221345926655,\\[-2pt]
&\quad 14062402405382925912884193140669738406166578327338\bigr),\\
\mathbf c_q={}&\bigl(
2425745955169956924323135015855316312606784196721,\\[-2pt]
&\quad 10534474137669716049158008564147639826733568383236,\\[-2pt]
&\quad 14797023225454273436443782496570083367866547475252\bigr).\end{aligned}$$ The critical lift is the exact residue class $$\widetilde P_p=[1,\mathbf x(P_p)+p\mathbf c_p]\pmod {p^2}.
 \label{eq:critical-lift-formula}$$ For the two smaller primes this gives $$\widetilde P_{283}=[1,62892,20248,67762],\qquad
 \widetilde P_{1801}=[1,892932,346330,3227903].$$ , together with the fully printed $P_q$ and $\mathbf c_q$, is an exact (and more legible) carrier for the $q^2$ lift than its three expanded $98$-digit coordinates.

## Critical value and transversality

Direct integer evaluation gives the following unit residues: $$\begin{gathered}
\begin{array}{c|c|c}
p&F(P_p)/p\pmod p&\det H_p\pmod p\\ \hline
283&212&228\\
1801&818&1387
\end{array}\\[4pt]
\begin{aligned}
F(P_q)/q&\equiv
11651769163508833344099877335703302197941640200357\pmod q,\\
\det H_q&\equiv
6136116089260018682592250996037036352166217747437\pmod q.
\end{aligned}
\end{gathered}
\label{eq:reflection-critical-values}$$ Because $\nabla f(P_p)$ is divisible by $p$, Taylor expansion and [\[eq:critical-lift-formula\]](#eq:critical-lift-formula){reference-type="ref" reference="eq:critical-lift-formula"} give $$f(\widetilde P_p)\equiv f(P_p)\pmod {p^2}.$$ The critical-value column of [\[eq:reflection-critical-values\]](#eq:reflection-critical-values){reference-type="ref" reference="eq:reflection-critical-values"} is nonzero, hence $v_p(f(\widetilde P_p))=1$. After the unique critical-point translation, the completed local equation has a nondegenerate quadratic term and a smoothing parameter equal to $p$ times a unit. It follows that the total space is regular at the critical point and that the base trait meets the discriminant divisor transversely.

All three residue characteristics are odd. The Picard--Lefschetz formula of SGA 7 II, Exposé XV [@sga7ii1973], together with the divided-discriminant bridge for cubic surfaces in @saito2012discriminant [Proposition 2.3, p. 858; Theorem 3.5, pp. 864--866; cubic-surface specialization, p. 870], therefore makes tame inertia act by a single root reflection. The exhaustive action comparison in [\[tab:app-order-two\]](#tab:app-order-two){reference-type="ref" reference="tab:app-order-two"} identifies its subgroup as ToM $2$, with line type $1^{15}2^6$, double-six type $1^{16}2^{10}$, fixed dimensions $(5,15)$, and Artin pair $(1,5)$. This conclusion uses no residue-degree assertion.

# Exact certificate and artifact map {#app:certificate}

This is the only artifact map in the paper. Its purpose is to make the large exact carriers addressable without confusing a machine record with a mathematical authority. The universal implications used in the proofs are cited from the literature; the records below bind the arithmetic and group computations for this one surface.

## Claim-to-carrier map

The certificate payload is divided into eight semantic gates, G0--G7. For the reader, the following coarser map C1--C7 groups each mathematical claim with the carrier that permits an independent reconstruction.

::: {#tab:artifact-map}
  map   mathematical content                                                                                                                                                          independent reconstruction carrier
  ----- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  map   mathematical content                                                                                                                                                          independent reconstruction carrier
  C1    frozen cubic, Grassmann elimination, smoothness, degree-$27$ field, and oriented field presentation                                                                           canonical surface and exact-field leaves in `c58_arithmetic_evidence.json.gz`; independent surface and field reconstruction in the checker
  C2    divided discriminant, maximal order, local prime ideals, differents, $\operatorname{Disc}(E)$, and the nine-versus-eight support distinction                                  arithmetic evidence, strict local-row schema, prime-vector complements, and independent PARI reconstruction
  C3    the certified $\theta_{36}$ partitions at precisions $20,30,40$ and $900,950,1000$, including separation bounds and multiply-back; $\delta_{36}$ nondependency                arithmetic evidence plus the named authority and nonresult leaves in the certificate; both lanes are rebound independently
  C4    the $350$-class subgroup scan, every $p=3$ and $p=5$ raw hit and valid $(D,I)$ pair, the ToM $6\times2,7,8$ rational ledger, normality, and the grade-$7$ action              `c58_group_evidence.json`, reconstructed labelled actions, exact rational arithmetic, and a separate GAP checker
  C5    four-stratum reflection geometry, Hessians, Hensel corrections, critical values, transversality, and the ToM-$2$ selection                                                    arithmetic reflection witnesses together with the complete order-two profile map in the group evidence
  C6    fixed spaces, all Swan and Artin conductors, $N(V_6)$, $N(V_{20})$, $\operatorname{Disc}(E)$, $\operatorname{Disc}(K)$, signature, subgroup ToM $5$, and element index $17$   independent character, product, signature, and CTblLib reconstruction leaves
  C7    strict parsing, schema closure, source/result inventory, checker independence, hostile scalar rebound, and scope firewalls                                                    certificate, schema, independent check report, self-excluding scoped manifest, and the project-local test report

  : The complete C58 artifact map.
:::

The complete payload has $1149$ scalar leaves. The checker reconstructs all semantic leaves without importing or calling the producer's theorem helpers, and rejects $1199$ systematic rebound mutations. Gates G0--G7 all pass; the project-local scaffold suite contains $45$ passing tests. These are integrity statements about the frozen computation, not statistical evidence.

## Exact identities

The principal SHA-256 identities are

::: {#tab:certificate-hashes}
  object                                   SHA-256
  ---------------------------------------- ---------
  object                                   SHA-256
                                           ``
  canonical payload                        ``
                                           ``
                                           ``
  independent replay summary               ``
                                           ``
  decompressed canonical arithmetic JSON   ``
                                           ``
                                           ``

  : Principal certificate identities.
:::

The scoped tree contains exactly the following $14$ source files:

> , , , , , , , , , , , , , and .

Its eight result files are

> , , , , , , , and .

Thus the live code/results inventory has $22$ entries. The manifest is self-excluding and contains the other $21$ entries, so its own digest is not circularly embedded in its contents.

## Backend and replay contract

The bound backend versions are $$\begin{array}{c|l}
\text{backend}&\text{versions}\\ \hline
\text{PARI lane}&\text{Python }3.10.12,\ \text{cypari2 }2.1.2,\
                   \text{PARI }2.13.3\\
\text{finite-group lane}&\text{GAP }4.11.1,\ \text{TomLib }1.2.9,\\
&\text{SmallGrp }1.4.1,\ \text{CTblLib }1.3.1\\
\text{exact-polynomial lane}&\text{Python }3.12.3,\ \text{FLINT }0.9.0,\\
&\text{SymPy }1.14.0,\ \text{jsonschema }4.25.0.
\end{array}$$ In particular, a CTblLib version change invalidates the numeric character-table labels until a fresh rebinding is performed.

From the project-local `code` directory, the unique nonmutating command is

    /usr/bin/bash -p ./run_all.sh

invoked by a trusted parent after unsetting loader, shell-startup, Python optimization, and Python import-path variables. The trust contract excludes a concurrent same-UID pathname mutator during the external-child launch window. A deliberate refresh is a different maintainer operation and is not needed to check the theorem. It promotes exactly six generated targets as a rollback-safe group and then requires a second clean default replay.

The canonical JSON parser rejects duplicate keys and noncanonical integer encodings; deterministic gzip binds the compressed and decompressed arithmetic records. The independent checker redoes local decompositions, different exponents, subgroup filters, filtrations, conductors, and global identities. Raw exploratory transcripts and undocumented temporary outputs are outside the premise graph.

Finally, the payload includes the exact scope leaf [No-Bad-Euler-or-Root-Number]{.smallcaps}. It rejects any output asserting a decomposition Frobenius, bad Euler polynomial or factor, epsilon factor, local or global root number, Artin holomorphy, automorphy, analytic continuation, or functional equation. The unresolved order of $D_3$ does not weaken any result in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, and resolving it would not by itself authorize any of those excluded statements.

# Source-use ledger and theorem boundaries {#app:sources}

The proof separates general theorems from computations for the frozen surface. The exact source locator, the implication used, and the assertion that remains instance-specific are recorded in [15](#tab:source-ledger){reference-type="ref" reference="tab:source-ledger"}. This prevents a citation to a general theorem from being read as a citation for one of the large exact outputs.

::: {#tab:source-ledger}
  source and locator                                                                                                                                   authorized use here                                                                                           not supplied by the source
  ---------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------
  source and locator                                                                                                                                   authorized use here                                                                                           not supplied by the source
  Serre, *Local Fields*, Chapter II, §2, Exercises 1--2, printed p. 30 [@serre1979local]                                                               Krasner--Hensel factor stability once the separation and precision inequalities have been proved              the local factors, polynomial-discriminant exponents, precision bounds, or multiply-back identities for $\theta_{36}$
  Serre, Chapter IV, §2, Proposition 9, printed pp. 69--70 [@serre1979local]                                                                           the graded tame action $\theta_i(s\tau s^{-1})=\theta_0(s)^i\theta_i(\tau)$                                   the $350$-class search, the ToM $6\times2,7,8$ profile inventory, or the identification of ToM $140$ before the grade-$7$ test
  Serre, Chapter VI, §2, Corollary $1'$, printed pp. 100--101; Chapter VI, §3, Proposition 6 and Corollary 1, printed pp. 103--104 [@serre1979local]   Artin conductors; conductor--discriminant identity                                                            any local fixed space, Swan value, conductor exponent, or field discriminant for this instance
  SGA 7 II, Exposé XV [@sga7ii1973]                                                                                                                    Picard--Lefschetz reflection monodromy for a transverse ordinary quadratic singularity                        the singular points, Hessians, Hensel lifts, transversality checks, or the ToM label at $283,1801,q$
  Saito, Proposition 2.3, p. 858; Theorem 3.5, pp. 864--866; cubic-surface specialization, p. 870 [@saito2012discriminant]                             the divided discriminant, determinant character, and Picard--Lefschetz bridge for cubic surfaces              the frozen divided discriminant, the three local witnesses, higher ramification groups, or either field discriminant
  Elsenhans--Jahnel, Propositions 21--22, pp. 651--652 [@elsenhansjahnel2009experiments]                                                               precedent for explicit full-$W(E_6)$ cubic surfaces, ramification envelopes, and $p$-adic factor patterns     the filtered wild inertia, Swan conductors, maximal-order discriminant, or normal-closure discriminant of the present surface
  Elsenhans--Jahnel, Theorem 2.12 [@elsenhansjahnel2012discriminant]                                                                                   the cubic discriminant and its index-two determinant character                                                the complete local representation or any frozen local calculation
  Banwait--Fité--Loughran, Table 7.1 [@banwaitfite2019delpezzo]                                                                                        the corrected finite-field $W(E_6)$ class/trace convention                                                    number-field inertia, filtration, or conductor data for the present surface
  PARI/GP user's guide sections for `nfbasis`, `nfinit`, `idealprimedec`, `nfcertify`, and `polsturm` [@parigroup2021]                                 semantics of maximal orders, prime decompositions, differents, certification, and real-root counting          proof that any particular displayed output was generated or independently reconstructed correctly
  GAP/TomLib and CTblLib package records [@gap2021; @tomlib2019; @ctbllib2020]                                                                         the reproducible `U4(2).2` Table-of-Marks and character-table naming convention, including package versions   the frozen-instance subgroup classification, or permission to identify subgroup ToM $5$ with element-class index $17$

  : Complete source-use ledger.
:::

The closest published precedent therefore prevents a novelty claim of the form "the first ramification calculation for an explicit cubic surface." The bounded contribution proved here is the complete filtered-inertia and Artin-conductor package for this explicit full-$W(E_6)$ surface, including both wild primes and the exact line-field and normal-closure discriminants. It is not a claim about all cubic surfaces.

Nor does the paper address rational or local points, weak approximation, the Hasse principle, or a Brauer--Manin obstruction for $Y$. Those questions are logically separate from the permutation ramification theorem. The analytic nonclaims are the stronger named firewall stated in [\[rem:main-firewall\]](#rem:main-firewall){reference-type="ref" reference="rem:main-firewall"} and repeated in [12](#app:certificate){reference-type="ref" reference="app:certificate"}.
