---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--43-squarefree-factor-periodic-rigidity"
canonical_tex: "symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/main.tex"
canonical_pdf: "symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/main.pdf"
source_sha256: "1fef3523cd8fa74c753e788fde78eb260ffdd114fa216fd024ac0670f2f6da79"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Factors Cannot Resurrect Cycles: Periodic-Ledger Rigidity for the Squarefree Admissible Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/43-squarefree-factor-periodic-rigidity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We record a source-specific closure statement for the two-sided squarefree admissible shift. Let $X_{\mathrm{sf}}\subset\{0,1\}^{\mathbb Z}$ consist of the sequences whose support omits at least one residue modulo $p^2$ for every rational prime $p$. For every compact metrizable system $(Y,S)$ and every continuous surjective $\mathbb Z$-equivariant map $\pi:X_{\mathrm{sf}}\to Y$, we prove $$\operatorname{Per}(Y,S)=\{\pi(0^{\mathbb Z})\}.$$ The proof chooses fresh prime-square moduli for the two source points at each coordinate of a finite window. The Chinese remainder theorem synchronizes both translates on an arbitrarily long zero block, proving source proximality. Uniform continuity transports proximality through the factor, and finite-orbit separation excludes every nontrivial target cycle. Hence $\#\operatorname{Fix}(S^m)=1$ for all $m\geq1$, the Artin--Mazur zeta function is $(1-z)^{-1}$, and its inverse determinant is $1-z$.

  The mathematical ingredients are known or elementary: squarefree and $\mathscr B$-free proximality receives zero novelty credit, as do factor permanence and the rank-one determinant. The contribution is only a typed internal closure connecting the arbitrary compact-metrizable factor quantifier to the periodic ledger, marker, operator ownership, sharpness controls, and a rejected Route-A record. In particular, repetitions of the single fixed orbit are not rational-prime primitives. Every finite set of prime-square exclusions admits an explicit periodic witness, including a separate empty-set case. An exact published duplicate triggers `STOP_DUPLICATE`; no standalone novelty claim is made.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  **Factors Cannot Resurrect Cycles:**\
  Periodic-Ledger Rigidity for the Squarefree Admissible Shift
```

## Markdown 正文

# Introduction {#sec:introduction}

An aperiodic source need not have aperiodic factors. A quotient may forget the information that prevented a source cycle and thereby create a periodic target. Consequently, the source-only statement $\operatorname{Per}(X,T)=\varnothing$ does not by itself control periodic ledgers after factorization. This note closes that loophole for one exact arithmetic source: the two-sided squarefree admissible shift. The operative property is not merely source aperiodicity but proximality, witnessed directly by a prime-square Chinese-remainder construction.

Let $\mathbb P$ denote the rational primes and set $$X_{\mathrm{sf}}=
  \left\{x\in\{0,1\}^{\mathbb Z}:
  \operatorname{supp}(x)\bmod p^2\neq \mathbb Z/p^2\mathbb Z
  \text{ for every }p\in\mathbb P\right\}.
  \label{eq:source-definition-intro}$$ The left shift is $(\sigma x)_j=x_{j+1}$. The prime squares in [\[eq:source-definition-intro\]](#eq:source-definition-intro){reference-type="ref" reference="eq:source-definition-intro"} are explicit grammar inputs. Their arithmetic origin is therefore a modeling choice, not an emergent feature. The zero sequence is a fixed source point.

Our target category is intentionally broad. The space $Y$ may be any compact metrizable space, $S:Y\to Y$ any homeomorphism, and $\pi:X_{\mathrm{sf}}\twoheadrightarrow Y$ any continuous surjection satisfying $\pi\circ\sigma^n=S^n\circ\pi$ for every $n\in\mathbb Z$. We impose no finite alphabet, symbolic presentation, expansivity, soficity, finite sliding-block radius, or bound on factor fibers.

[\[thm:intro-main\]]{#thm:intro-main label="thm:intro-main"} For every factor $(Y,S,\pi)$ in the preceding category, $$\operatorname{Per}(Y,S)=\{y_0\},
  \qquad y_0:=\pi(0^{\mathbb Z}).$$ Thus, for every integer $m\geq1$, $$\#\operatorname{Fix}(S^m)=1,
  \qquad
  \zeta_{\mathrm{AM},Y}(z)=\frac{1}{1-z},
  \qquad
  D_{\mathrm{AM},Y}(z)=1-z.$$

The proof has five exact arrows, summarized in [\[fig:proof-chain\]](#fig:proof-chain){reference-type="ref" reference="fig:proof-chain"}. For each of two source points and each coordinate in a desired window, admissibility supplies a missing residue modulo a fresh prime square. Pairwise coprimality lets the Chinese remainder theorem choose one time at which both translated points vanish throughout the window. This proves source proximality. Surjective lifts, uniform continuity on the compact source, and equivariance pass proximality to the factor. Finally, a finite periodic orbit has a positive separation scale, contradicting proximality unless it is the fixed image of the zero point. Fixed-point counts then determine the Artin--Mazur series.

The theorem is not presented as a new squarefree or $\mathscr B$-free proximality result. Squarefree admissibility and proximality are already present in Sarnak's lecture notes [@sarnak2011mobius]; the broader $\mathscr B$-free literature develops the same source family and general proximality criteria [@elabdalaoui2015bfree; @bartnicka2018bfree; @kasjan2019window]. Passing proximality through a compact factor and separating a finite periodic orbit are elementary. The determinant $1-z$ is likewise an immediate Artin--Mazur calculation. We assign zero novelty credit to each ingredient.

The narrower value of the note is organizational and typed. It freezes the arbitrary compact-metrizable factor quantifier; connects the source proof to the target primitive-orbit ledger; identifies exactly what the marker $z$ counts; limits the one-dimensional matrix $[1]$ to the periodic core; and classifies apparent repairs that change the source, direction, time, or observable. This is an internal exact closure with a standalone novelty assessment of $1/10$. A bounded literature search did not locate the exact all-factor sentence, but absence from a search is not evidence of priority. An exact primary-source collision activates `STOP_DUPLICATE`.

The rest of the paper is organized as follows. separates prior ownership from the retrospective candidate selector. proves compactness and source proximality. proves the arbitrary-factor theorem. derives the zeta, determinant, and primitive-type firewall. proves the finite-exclusion sharpness statement and records the rejected Route-A tuple. Detailed exact checks and the object/marker/operator ledger appear in the appendices.

# Prior ownership, scoped claim, and retrospective selection {#sec:prior-scope}

The distinction between a proved statement and a novel statement is load-bearing here. Nearly all mathematical content belongs to established squarefree dynamics or to elementary topological dynamics. We therefore begin with ownership rather than with a novelty narrative.

## Primary-source chronology

The periodic-point exponential used below is the Artin--Mazur convention introduced in [@artin1965periodic]. That reference owns the determinant framework, not any squarefree-factor theorem. Sarnak's institutional lecture notes identify the squarefree flow through admissible supports and state proximality together with the zero system as the unique minimal subsystem [@sarnak2011mobius]. The present source is two-sided; we give a complete two-sided CRT proof rather than transporting the one-sided presentation by assertion.

El Abdalaoui, Lemańczyk, and de la Rue place squarefree dynamics in the broader setting of pairwise-coprime $\mathscr B$-free integers [@elabdalaoui2015bfree]. Bartnicka, Kasjan, Kułaga-Przymus, and Lemańczyk give a general two-sided proximality classification for $\mathscr B$-free systems [@bartnicka2018bfree]. For $\mathscr B=\{p^2:p\in\mathbb P\}$, their coprimality hypothesis is immediate, so this is the strongest direct collision with the central source property. Kasjan, Keller, and Lemańczyk provide an independent window-based characterization of proximality [@kasjan2019window]. These sources jointly force zero novelty credit for source proximality.

Recent work of Gundlach and Klüners studies symmetries, morphisms, and factor systems of power-free admissible shifts, as well as a broader sieve framework [@gundlach2024powerfree]. Its factor target remains another structured admissible shift with a compatible acting-group morphism, whereas [\[thm:factor-rigidity\]](#thm:factor-rigidity){reference-type="ref" reference="thm:factor-rigidity"} quantifies over an arbitrary compact metrizable $\mathbb Z$-factor and concludes only its periodic ledger. This is a real scope difference, but it is not a novelty proof. The exact sentence could still occur elsewhere.

## Known ingredients and the local closure

::: {#tab:ownership}
  Component                                                       Status                                                  Novelty credit
  --------------------------------------------------------------- ------------------------------------------------------- ----------------
  Squarefree admissible source and its proximality                Known primary-source content; locally replayed by CRT
  Proximality preserved by a continuous onto factor               Elementary permanence; locally proved
  Periodic-orbit separation in a proximal compact system          Elementary finite-set argument
  Singleton Artin--Mazur series and matrix $[1]$                  Direct calculation
  Typed source-to-factor-to-ledger closure with repair taxonomy   Internal program assembly                               /10 internal
  Standalone publication novelty                                  Exact duplicate remains plausible                       /10

  : Ownership and novelty accounting. "Local" means proved in this note for auditability, not claimed as mathematically new.
:::

The only permitted contribution sentence is therefore the following:

> For the exact all-prime-square two-sided source, this note assembles a fully typed proof from explicit CRT proximality through every continuous surjective equivariant compact metrizable factor to the unchanged singleton Artin--Mazur ledger, and it records the sharp source-change controls and strict Route consequence.

The sentence does not claim a new proximality theorem, a general factor theorem, or an arithmetic determinant. It also does not infer novelty from a negative keyword search.

## Retrospective selection

The commissioned remaining candidate universe was $\{\mathrm{SD\text{-}C02},\mathrm{SD\text{-}C03},
\mathrm{SD\text{-}C05}\}$. A Boolean rule was written only after the three historical cards, the primary literature, and the present proof were known. It required the historical statuses $\mathrm{A0\_FAIL}$ with modeling-choice evidence, $\mathrm{A1\_FAIL}$ proved, $\mathrm{A2\_ANALYTIC\_DETERMINANT}$ proved, and $\mathrm{A3\_FAIL}$ proved, together with a compact two-sided arithmetic subshift whose exact determinant comes from a singleton fixed-point ledger.

::: {#tab:selector}
  Card     Historical obstruction                                                      Rule result
  -------- --------------------------------------------------------------------------- -------------
  SD-C02   compact squarefree source; proved singleton ledger and exact $(1-z)^{-1}$   pass
  SD-C03   weak A1, failed A2, nonmatching source and ledger                           fail
  SD-C05   structural A0, failed A2, graded nonstationary source                       fail

  : Application of the retrospective rule. Uniqueness here carries no prospective, ranking, priority, or authorization credit.
:::

Thus the rule returns SD-C02 uniquely, but it is an explicitly retrospective description of a known outcome. It was not frozen before results, does not make the choice outcome independent, and supplies no novelty or priority. Earlier papers are used only as collision and chronology boundaries; none is a ranking or authorization source.

## Exact scope and live duplicate stop

The claim includes all and only maps $$\pi:(X_{\mathrm{sf}},\sigma)\twoheadrightarrow(Y,S)$$ that are continuous, surjective, and equivariant for the full $\mathbb Z$-actions, with $Y$ compact metrizable and $S$ a homeomorphism. It excludes extensions, products, induced systems, changed observables, nononto maps, and finite-modulus replacements. The bounded audit did not locate an exact primary source with the same source, target quantifier, periodic conclusion, and Artin--Mazur packaging. Because every ingredient is known or elementary, an exact collision remains plausible. Discovery of one changes the external disposition to `STOP_DUPLICATE`; the proof may remain as an internal audit record.

# The squarefree source and an exact proximality certificate {#sec:source-proximality}

We now prove the source property used by the factor argument. Keeping this proof local serves two purposes: it fixes the two-sided indexing convention, and it exposes exactly where the infinitely many pairwise-coprime prime-square exclusions enter.

## Topological source

For a fixed rational prime $p$, let $F_p$ consist of those binary sequences whose support meets every residue class modulo $p^2$. If $x\in F_p$, choose one occupied coordinate from each of the finitely many residue classes. The cylinder that keeps those coordinates equal to one is contained in $F_p$. Hence $F_p$ is open and $$X_{\mathrm{sf}}=\bigcap_{p\in\mathbb P}
  \bigl(\{0,1\}^{\mathbb Z}\setminus F_p\bigr)$$ is closed in the compact full shift. Translation permutes the residue classes modulo every $p^2$, so $X_{\mathrm{sf}}$ is shift invariant. It is therefore a compact metrizable $\mathbb Z$-system. The point $0^{\mathbb Z}$ lies in $X_{\mathrm{sf}}$ and is fixed.

For later use, define the nonempty missing-residue set $$M_p(x):=
  \left(\mathbb Z/p^2\mathbb Z\right)
  \setminus\bigl(\operatorname{supp}(x)\bmod p^2\bigr).
  \label{eq:missing-residue}$$ Choosing an element of $M_p(x)$ is a proof witness after $x$ and $p$ have been fixed. It is not a fitted parameter.

For a compact metrizable system $(X,T)$, a pair $(x,y)$ is proximal if, for one (equivalently every) compatible metric, $$\inf_{n\geq0}d(T^n x,T^n y)=0.$$ The system is proximal if every pair is proximal.

## Fresh-prime CRT construction

[\[prop:window-synchronization\]]{#prop:window-synchronization label="prop:window-synchronization"} For every $x^{(1)},x^{(2)}\in X_{\mathrm{sf}}$ and every integer $L\geq0$, there is an integer $n_L\geq0$ such that $$x^{(1)}_{n_L+j}=x^{(2)}_{n_L+j}=0
  \qquad(-L\leq j\leq L).$$

For every $j\in\{-L,\ldots,L\}$ and $i\in\{1,2\}$, choose a rational prime $p_{j,i}$, with all $2(2L+1)$ chosen primes distinct. By [\[eq:missing-residue\]](#eq:missing-residue){reference-type="ref" reference="eq:missing-residue"}, choose $$a_{j,i}\in M_{p_{j,i}}(x^{(i)}).$$ The moduli $p_{j,i}^2$ are pairwise coprime. The Chinese remainder theorem therefore gives an integer $n$, unique modulo their product, satisfying $$n+j\equiv a_{j,i}\pmod{p_{j,i}^2}
  \qquad(j\in[-L,L],\ i\in\{1,2\}).
  \label{eq:crt-system}$$ Choose the nonnegative representative $n_L$. Because $a_{j,i}$ is absent from the support of $x^{(i)}$ modulo $p_{j,i}^2$, [\[eq:crt-system\]](#eq:crt-system){reference-type="ref" reference="eq:crt-system"} forces $x^{(i)}_{n_L+j}=0$ for every requested pair $(j,i)$.

Distinct primes are chosen for point-coordinate pairs, not merely for coordinates. This prevents two unrelated missing residues from being imposed modulo the same prime square. The construction uses arbitrarily large primes as $L$ grows; this is precisely why a finite collection of exclusions cannot support the proof.

## Metric conclusion

Use the compatible product metric $$d_X(x,y)=\frac13\sum_{k\in\mathbb Z}
  2^{-|k|}|x_k-y_k|.
  \label{eq:product-metric}$$ If two points agree on $[-L,L]$, then $$\begin{aligned}
  d_X(x,y)
  &\leq \frac13\sum_{|k|>L}2^{-|k|}
   =\frac13\left(2\sum_{k=L+1}^{\infty}2^{-k}\right)
   =\frac{2^{1-L}}{3}.
  \label{eq:metric-tail}\end{aligned}$$ Combining [\[prop:window-synchronization,eq:metric-tail\]](#prop:window-synchronization,eq:metric-tail){reference-type="ref" reference="prop:window-synchronization,eq:metric-tail"} and letting $L\to\infty$ proves the following.

[\[cor:source-proximal\]]{#cor:source-proximal label="cor:source-proximal"} The two-sided system $(X_{\mathrm{sf}},\sigma)$ is proximal.

This local proof earns no novelty credit: source proximality is known from the squarefree and general $\mathscr B$-free literature discussed in [2](#sec:prior-scope){reference-type="ref" reference="sec:prior-scope"}. Its role is exact source control. In particular, it exhibits the all-prime-square quantifier needed later for the sharpness statement; no finite census is substituted for the theorem.

# Arbitrary-factor periodic rigidity {#sec:factor-rigidity}

Source proximality becomes useful only after its quantifiers survive the factor map. We therefore separate factor permanence from periodic-orbit separation. This also makes clear that the target need not be symbolic.

## Proximality passes to every lawful factor

Fix a compact metrizable space $Y$, a homeomorphism $S:Y\to Y$, and a continuous surjection $\pi:X_{\mathrm{sf}}\twoheadrightarrow Y$ satisfying $$\pi\circ\sigma^n=S^n\circ\pi
  \qquad(n\in\mathbb Z).
  \label{eq:factor-equivariance}$$

[\[lem:factor-proximal\]]{#lem:factor-proximal label="lem:factor-proximal"} The target system $(Y,S)$ is proximal.

Let $y_1,y_2\in Y$. Surjectivity supplies lifts $x_1,x_2\in X_{\mathrm{sf}}$ with $\pi(x_i)=y_i$. Because $X_{\mathrm{sf}}$ is compact, continuity of $\pi$ is uniform: for every $\varepsilon>0$, some $\delta>0$ satisfies $$d_X(u,v)<\delta
  \Longrightarrow
  d_Y(\pi u,\pi v)<\varepsilon.$$ By [\[cor:source-proximal\]](#cor:source-proximal){reference-type="ref" reference="cor:source-proximal"}, choose $n\geq0$ with $d_X(\sigma^n x_1,\sigma^n x_2)<\delta$. Equivariance gives $$d_Y(S^n y_1,S^n y_2)
  =d_Y(\pi\sigma^n x_1,\pi\sigma^n x_2)<\varepsilon.$$ As $\varepsilon$ is arbitrary, $(y_1,y_2)$ is proximal.

Each hypothesis has a distinct role. Surjectivity lifts arbitrary target pairs. Continuity and source compactness yield uniform control. Equivariance compares the same time in source and target. The theorem does not extend by wordplay to a map missing any of these properties.

## Finite-orbit separation

Equivariance anchors the fixed point $$y_0:=\pi(0^{\mathbb Z}),
  \qquad Sy_0=y_0.
  \label{eq:fixed-anchor}$$

[\[lem:periodic-separation\]]{#lem:periodic-separation label="lem:periodic-separation"} Let $(Y,S)$ be a proximal metrizable $\mathbb Z$-system with a fixed point $y_0$. Then $y_0$ is the only periodic point.

Suppose $y$ has least period $r$. If $r=1$ and $y\neq y_0$, then $$d_Y(S^n y,S^n y_0)=d_Y(y,y_0)>0
  \qquad(n\geq0),$$ so the pair $(y,y_0)$ is not proximal.

Now suppose $r>1$. The points $S^k y$ and $S^{k+1}y$ are distinct for every $0\leq k<r$. The finite minimum $$\delta_r:=\min_{0\leq k<r}
  d_Y(S^k y,S^{k+1}y)
  \label{eq:periodic-gap}$$ is therefore positive. Reducing $n$ modulo $r$ shows $$d_Y(S^n y,S^n(Sy))\geq\delta_r
  \qquad(n\geq0).$$ Thus $(y,Sy)$ is not proximal. Both cases contradict proximality unless $y=y_0$.

## The theorem

[\[thm:factor-rigidity\]]{#thm:factor-rigidity label="thm:factor-rigidity"} Let $X_{\mathrm{sf}}$ be the exact source in [\[eq:source-definition-intro\]](#eq:source-definition-intro){reference-type="ref" reference="eq:source-definition-intro"}. For every compact metrizable $\mathbb Z$-system $(Y,S)$ and every continuous surjective equivariant map $\pi:X_{\mathrm{sf}}\twoheadrightarrow Y$, $$\operatorname{Per}(Y,S)=\{\pi(0^{\mathbb Z})\}.$$

By [\[eq:fixed-anchor\]](#eq:fixed-anchor){reference-type="ref" reference="eq:fixed-anchor"}, $y_0=\pi(0^{\mathbb Z})$ is fixed. make $(Y,S)$ proximal, and [\[lem:periodic-separation\]](#lem:periodic-separation){reference-type="ref" reference="lem:periodic-separation"} excludes every periodic point other than $y_0$.

The word "every" in [\[thm:factor-rigidity\]](#thm:factor-rigidity){reference-type="ref" reference="thm:factor-rigidity"} refers to the entire lawful factor category, not to a finite list of symbolic quotients. The proof never examines a target alphabet or a coding radius. Conversely, the theorem is not a universal statement that factors of aperiodic systems are aperiodic. It succeeds because the frozen source is proximal; deleting that property invalidates the finite-orbit contradiction.

## Assumption ledger

::: {#tab:factor-assumptions}
  Assumption                        Use in the proof                                    What deletion permits
  --------------------------------- --------------------------------------------------- ------------------------------------------------------------------
  all prime-square exclusions       fresh coprime moduli for every window               finite approximants with cycles
  continuity                        small source distance gives small target distance   arbitrary observations need not preserve proximality
  surjectivity                      lifts every target pair                             a partial image says nothing about all target points
  equivariance                      aligns source and target time                       time-varying or unrelated maps
  compact metric source             uniform continuity                                  merely pointwise control is insufficient for the stated argument
  homeomorphic $\mathbb Z$-action   exact two-sided factor category                     changed semigroup/induced dynamics

  : Where the factor assumptions enter.
:::

# Periodic ledger, determinant, and ownership firewalls {#sec:periodic-ledger}

The topological theorem has an immediate generating-function consequence, but its typing matters. A fixed-point count, a primitive orbit, a temporal traversal, a rational prime, and an operator acting only on the periodic core are different objects.

## Fixed counts and the Artin--Mazur determinant

By [\[thm:factor-rigidity\]](#thm:factor-rigidity){reference-type="ref" reference="thm:factor-rigidity"}, the point $y_0$ is fixed and is the only periodic point. Hence $$\operatorname{Fix}(S^m)=\{y_0\},
  \qquad \#\operatorname{Fix}(S^m)=1
  \qquad(m\geq1).
  \label{eq:fixed-counts}$$ Using the Artin--Mazur convention [@artin1965periodic], $$\begin{aligned}
  \zeta_{\mathrm{AM},Y}(z)
  &:=\exp\left(
    \sum_{m\geq1}\frac{\#\operatorname{Fix}(S^m)}{m}z^m
  \right) \notag\\
  &=\exp\left(\sum_{m\geq1}\frac{z^m}{m}\right)
   =\exp\bigl(-\log(1-z)\bigr)
   =\frac{1}{1-z}.
  \label{eq:am-zeta}\end{aligned}$$ This is a formal-power-series identity and an analytic identity for $|z|<1$. With the frozen inverse convention, $$D_{\mathrm{AM},Y}(z):=\zeta_{\mathrm{AM},Y}(z)^{-1}=1-z.
  \label{eq:am-determinant}$$ No regularization or analytic continuation is required to obtain the polynomial in [\[eq:am-determinant\]](#eq:am-determinant){reference-type="ref" reference="eq:am-determinant"}.

## Primitive orbit versus repetition

Let $\mathcal O_0=\{y_0\}$ denote the sole primitive periodic orbit. Its least period is one and its primitive Euler factor is $$(1-z)^{-1}.$$ The logarithmic term $z^r/r$ is the contribution of the $r$-fold traversal of this same orbit. It is not a new primitive orbit. Equivalently, $$\operatorname{Prim}(Y,S)=\{\mathcal O_0\},
  \qquad
  \log\zeta_{\mathrm{AM},Y}(z)=\sum_{r\geq1}\frac{z^r}{r}.$$ This distinction prevents a common bookkeeping error: an infinite list of repetition exponents does not constitute infinite primitive support.

The marker $z$ has one meaning throughout the note: one application of the original factor dynamics. Thus $\mathcal O_0$ carries $z$, and its $r$-fold traversal carries $z^r$. No period-dependent regrading is allowed under the frozen contract.

## The periodic-core operator

Let $\mathcal H_{\rm per}=\mathbb C e_0$ and define $K_{\mathrm{per}}e_0=e_0$. Then for every $m\geq1$, $$\operatorname{tr}(K_{\mathrm{per}}^m)=1,
  \qquad
  \det(I-zK_{\mathrm{per}})=1-z.
  \label{eq:rank-one-owner}$$ The identity in [\[eq:rank-one-owner\]](#eq:rank-one-owner){reference-type="ref" reference="eq:rank-one-owner"} is an exact realization of the already proved periodic ledger. It does not elevate $K_{\mathrm{per}}$ to a transfer operator on $X_{\mathrm{sf}}$ or on $C(Y)$. The matrix does not generate the source language, encode aperiodic points, form an analytic family, or define a self-adjoint Hilbert--Polya operator. Calling it a full-state operator would reverse the proof's ownership direction: the theorem proves the ledger first, and $[1]$ merely packages it afterward.

## Rational-prime comparator

If one writes the external formal comparator $$Z_{\mathbb P}(s,u)=
  \prod_{p\in\mathbb P}(1-u p^{-s})^{-1},
  \label{eq:prime-comparator}$$ then $u$ is an independent marker and each $p$ is a distinct object of type `RationalPrimeAtom`. By contrast, the factor ledger contains one object of type `PeriodicOrbit(Y,S)`. Its primitive support has cardinality one, whereas the support in [\[eq:prime-comparator\]](#eq:prime-comparator){reference-type="ref" reference="eq:prime-comparator"} is countably infinite. No same-type bijection exists. Specializing $u=z$ would only identify symbols; it would not repair primitive support, ownership, or repetition.

[\[prop:primitive-obstruction\]]{#prop:primitive-obstruction label="prop:primitive-obstruction"} Under the frozen object, marker, and repetition types, no lawful factor ledger is bijectively identifiable with the rational-prime primitive ledger.

The factor side has the single primitive object $\mathcal O_0$. Every $z^r$ is a traversal of $\mathcal O_0$. The prime side has one distinct primitive atom for each $p\in\mathbb P$. A bijection cannot map a singleton to an infinite set while preserving primitive type. The obstruction occurs before weights, clocks, or analytic divisors are compared.

The conclusion is deliberately negative and local. It does not say that no externally constructed prime diagonal operator exists. It says that such an operator is not owned by the periodic ledger of a factor of $X_{\mathrm{sf}}$.

# Sharpness, repair taxonomy, and strict Route verdict {#sec:sharpness-route}

The all-prime-square quantifier is not decorative. Every finite truncation admits an exact periodic witness, and the empty truncation requires a separate argument. These controls delimit the theorem and prevent a finite computation from being promoted to an all-prime statement.

## Every finite prime-square source has periodic points

Let $P_0\subset\mathbb P$ be finite and define $$Q=\prod_{p\in P_0}p^2.
  \label{eq:finite-Q}$$

[\[prop:finite-sharpness\]]{#prop:finite-sharpness label="prop:finite-sharpness"} The subshift obtained by enforcing admissibility only for the primes in $P_0$ fails the full source's periodic-collapse and proximality conclusions.

Assume first that $P_0\neq\varnothing$. Define $$x_n=1
  \quad\Longleftrightarrow\quad
  n\equiv1\pmod Q.
  \label{eq:finite-witness}$$ For every $p\in P_0$, divisibility $p^2\mid Q$ gives $$\operatorname{supp}(x)\bmod p^2=\{1\bmod p^2\},$$ so $x$ satisfies every retained admissibility constraint. It is nonzero and $Q$-periodic. Moreover, its least positive period is $Q$: if $d>0$ is a period, then $x_1=1$ forces $x_{1+d}=1$, hence $Q\mid d$. Since a nonempty $P_0$ gives $Q\geq4$, this is a nontrivial periodic orbit.

If $P_0=\varnothing$, then $Q=1$ and the constraints are vacuous. The points $0^{\mathbb Z}$ and $1^{\mathbb Z}$ are distinct fixed points, so the system is not proximal and does not have a singleton periodic ledger. This separate empty-set case is essential: one cannot call the period-one all-ones point a nontrivial $Q$-cycle.

For the concrete singleton $P_0=\{2\}$, the point $(0111)^{\mathbb Z}$ supplies an additional least-period-four witness. Its support modulo four is $\{1,2,3\}$, so it omits residue zero. This example is illustrative only; [\[prop:finite-sharpness\]](#prop:finite-sharpness){reference-type="ref" reference="prop:finite-sharpness"} is proved for every finite $P_0$, including the empty set.

## Apparent repairs and their type changes

::: {#tab:repairs}
  Proposed repair                                              Mathematical effect                                                                                                                               Verdict
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------
  Retain finitely many prime-square exclusions                 admits the exact periodic points in [\[prop:finite-sharpness\]](#prop:finite-sharpness){reference-type="ref" reference="prop:finite-sharpness"}   source change
  Take a product with a periodic system                        imports an external periodic ledger through an extension                                                                                          direction error
  Induce on or return to a subset                              changes time, marker, and primitive orbit type                                                                                                    clock change
  Use a noncontinuous, nononto, or nonequivariant map          leaves the factor category used by the proof                                                                                                      scope deletion
  Replace fixed-point counts by an aperiodic or measure zeta   changes the determinant owner                                                                                                                     observable change
  Call the powers $z^r$ new rational-prime primitives          converts traversals into atoms                                                                                                                    repetition/type error
  Call $[1]$ a full source transfer operator                   assigns a ledger package to an unsupported state space                                                                                            ownership error

  : Why common repairs do not remain in the frozen contract.
:::

The one-point factor and the identity factor are lawful positive controls. The former realizes the theorem in its most collapsed form; the latter retains the exact source. Neither creates a nontrivial primitive ledger.

## Strict Route-A record

The exact factor theorem does not promote the candidate through the broader arithmetic program. Its strict Route-A tuple is $$\begin{gathered}
  (\mathrm{A0\_FAIL},\ \mathrm{A1\_FAIL},\
   \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
   \mathrm{A3\_FAIL},\ \mathrm{A4\_FAIL}).
\end{gathered}$$ The coordinates have distinct meanings:

-   **A0 fails.** Every rational-prime-square exclusion is explicitly inserted into the source grammar. No rational-prime primitives emerge endogenously.

-   **A1 fails.** The primitive ledger is proved exactly, including temporal repetition, but contains only one trivial fixed orbit and has no rational-prime primitive support.

-   **A2 passes only at the analytic-determinant label.** The exact inverse determinant $1-z$ is a polynomial and is realized by $[1]$, but it records only the singleton ledger.

-   **A3 fails.** There is no completed arithmetic divisor, gamma factor, functional equation, $T\log T$ growth, explicit formula, or natural same-ledger Weil compression.

-   **A4 fails.** No full-state transfer family, fixed self-adjoint Hilbert--Polya operator, same-clock prime trace identity, or completed target divisor is defined.

Thus the overall verdict is `ROUTE_A_REJECTED`. Route B invocation is false because the same-object primitive ledger and completed analytic structure already fail. The frozen terminal mapping has four keyed entries: three mathematical stop codes and one literature disposition. A reader-facing projection appears in the canonical table below; the exact literal key--value mapping is retained in the source serialization. These conclusions are retrospective renderings of the proved theorem and frozen contract, not prospective predictions.

## Canonical retrospective integration replay

After independent post-output release, a bounded renderer read only the sealed authority artifacts. Source comments retain every exact field/value pair; the compact reader-facing projection is:

  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Evaluators**        Main $17/17$, independent $13/13$; science SHA-256 `ae57c6ffb38eb86d43912677eda19574db0ef50f05c25d964d1fcf261fb2422d`.
  **Proof controls**    CRT $16/16$; factor separation $6/6$; finite-$P_0$ $5/5$, both branches; fixed counts $8/8$; theorem and ledger failures zero.
  **Resolution**        Frozen sources $40/40$; retrospective selector survivor `SD-C02`.
  **Strict Route**      Main $23/23$, independent $24/24$; tuple exactly as displayed in the preceding subsection; `ROUTE_A_REJECTED`; Route B false.
  **Four terminals**    determinant: `STOP_TRIVIAL_ONE_MINUS_Z_DIVISOR`; factor: `STOP_PROXIMAL_PERIODIC_RIGIDITY`; literature: `PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE`; prime type: `STOP_SINGLETON_PRIMITIVE_SUPPORT`.
  **Adversarial**       registry classes, 893 negative instances, zero survivors; exact class map and ID/registry hashes are bound in the source serialization.
  **Reproducibility**   A/B/C artifacts identical; relocated C equals A; State-A/State-B normalized science identical; rerun changed paths $=\varnothing$.
  **Seal**              Integrity $16/16$; 53 exact output paths; 49-entry result ledger, SHA-256 `51cd6900505984e0eec391fcd0ff77aedd7747eedd114ec95d2ddf4d273e8a5f`.
  **Chronology**        Parent `FINAL`; `RETROSPECTIVE_KNOWN_MATHEMATICS_V6_AUTHORITY_OVERLAY_REPAIR`; `STOP_DUPLICATE` remains `LIVE_CONDITIONAL` outside Route.
  **State A**           The three provenance fields retain `PENDING_FIRST_ARTIFACT_COMMIT`; no paper manifest is present.
  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finite rows replay proof obligations, not universal claims by enumeration. This post-output rendering supplies no novelty, priority, ranking, authorization, selector-independence, preregistration, blindness, or prospective credit. The State-A sentinel is a required provenance boundary.

# Limitations and conclusion {#sec:limitations-conclusion}

The theorem is exact but deliberately narrow. It applies to continuous surjective equivariant factors of one fixed two-sided source with all rational-prime-square exclusions. It does not cover an arbitrary aperiodic system, a general $\mathscr B$-free system without the needed proximality, an extension, a product, an induced map, or a changed statistical observable. It makes no claim about aperiodic target structure, invariant measures, entropy, mixing, or spectral type.

The determinant conclusion is equally limited. The polynomial $1-z$ contains one zero and exactly packages one fixed orbit. It has no rational-prime Euler support, completed factor, gamma term, nontrivial divisor growth, or same-object spectral lift. The rank-one matrix $[1]$ is a periodic-core realization, not a transfer operator for the full state space. Nothing here advances a Hilbert--Polya construction.

Within those boundaries, the logic is complete. Prime-square admissibility provides missing residues. Fresh coprime moduli synchronize two translates on arbitrary zero windows. Proximality passes through every lawful compact metrizable factor. A finite periodic orbit cannot survive in a proximal target except for the fixed image of $0^{\mathbb Z}$. The resulting fixed counts force the Artin--Mazur zeta $(1-z)^{-1}$ and inverse determinant $1-z$, while primitive typing prevents the traversals $z^r$ from being relabeled as rational primes.

The finite-exclusion theorem is the sharpest source control in the note. A nonempty finite set $P_0$ admits the least-period $Q=\prod_{p\in P_0}p^2$ witness in [\[eq:finite-witness\]](#eq:finite-witness){reference-type="ref" reference="eq:finite-witness"}; the empty set admits two fixed points. Hence no bounded modulus experiment can replace the all-prime theorem. Other apparent repairs change the source, direction, clock, category, or observable.

Finally, the novelty accounting remains conservative. Known proximality receives zero credit, as do its elementary factor and periodic consequences. The note records an internal typed closure, scored $2/10$ for that program role and $1/10$ as a standalone publication claim. The retrospective selector receives no evidentiary credit. If an exact primary source is found with the same all-prime-square source, arbitrary compact-metrizable factor quantifier, singleton periodic conclusion, and Artin--Mazur packaging, the proper action is `STOP_DUPLICATE`, not rhetorical narrowing.

# Exact proof certificates and edge cases {#app:proof-details}

This appendix expands the finite calculations used in the main proof. The purpose is auditability: none of these computations depends on a numerical search or on a finite surrogate for an all-prime statement.

## Source-only periodic collapse

There is also a direct source-only proof that $0^{\mathbb Z}$ is the sole periodic source point. Suppose $x\in X_{\mathrm{sf}}$ has period $n\geq1$ and some $x_a=1$. Choose a rational prime $p\nmid n$. Periodicity gives $$a+n\mathbb Z\subseteq\operatorname{supp}(x).$$ Because $n$ is invertible modulo $p^2$, the progression $a+n\mathbb Z$ meets every residue class modulo $p^2$. Therefore $\operatorname{supp}(x)\bmod p^2=\mathbb Z/p^2\mathbb Z$, contradicting admissibility. Thus $x=0^{\mathbb Z}$.

This argument alone is not enough for [\[thm:factor-rigidity\]](#thm:factor-rigidity){reference-type="ref" reference="thm:factor-rigidity"}: source aperiodicity need not descend to a factor. The CRT proof supplies the stronger proximality property that does descend.

## CRT certificate for a finite window

For fixed $L$, enumerate the index set $$I_L=[-L,L]\times\{1,2\}.$$ Choose an injective map $(j,i)\mapsto p_{j,i}$ from $I_L$ into the rational primes. The exact congruence packet is $$n\equiv a_{j,i}-j\pmod{p_{j,i}^2}
  \qquad((j,i)\in I_L),$$ where $a_{j,i}\in M_{p_{j,i}}(x^{(i)})$. Since distinct primes have coprime squares, the Chinese remainder theorem gives one class $$n\pmod{\prod_{(j,i)\in I_L}p_{j,i}^2}.$$ No compatibility condition between the residues is needed. Selecting the least nonnegative representative produces a forward time $n_L\geq0$. For each $(j,i)$, the congruence says that $n_L+j$ lies in a residue missing from $\operatorname{supp}(x^{(i)})$, and hence the indicated coordinate is zero.

The smallest-window case $L=0$ uses two distinct primes $p_x,p_y$ and two congruences $$n\equiv a_x\pmod{p_x^2},
  \qquad
  n\equiv a_y\pmod{p_y^2}.$$ It synchronizes the central symbols. Larger windows use the same argument with fresh primes, not an induction that reuses potentially incompatible moduli.

## Product-metric normalization

For the metric in [\[eq:product-metric\]](#eq:product-metric){reference-type="ref" reference="eq:product-metric"}, the total mass is $$\frac13\sum_{k\in\mathbb Z}2^{-|k|}
  =\frac13\left(1+2\sum_{k=1}^{\infty}2^{-k}\right)=1.$$ If $x_k=y_k$ for $|k|\leq L$, then $|x_k-y_k|\leq1$ outside the window and $$d_X(x,y)
  \leq\frac13\left(2\sum_{k=L+1}^{\infty}2^{-k}\right)
  =\frac{2^{1-L}}{3}.$$ The right-hand side tends to zero. This supplies an explicit convergence rate, although the theorem needs only convergence.

## Why a periodic orbit has a positive gap

Let $y$ have least period $r>1$. If $S^k y=S^{k+1}y$ for some $k$, applying $S^{-k}$ gives $y=Sy$, contradicting least period $r>1$. Thus every one of the finitely many numbers $$d_Y(S^k y,S^{k+1}y),\qquad 0\leq k<r,$$ is positive. Their minimum $\delta_r$ is positive. For $n=qr+k$, periodicity gives $$d_Y(S^n y,S^n(Sy))
  =d_Y(S^k y,S^{k+1}y)\geq\delta_r.$$ This proves nonproximality of the pair $(y,Sy)$ without any expansivity or symbolic structure.

For a second fixed point $y\neq y_0$, the constant distance $d_Y(y,y_0)>0$ gives the analogous contradiction. Both cases are needed: the adjacent-orbit argument degenerates when $r=1$.

## Fixed-point exponential and primitive accounting

Substituting $\#\operatorname{Fix}(S^m)=1$ into the definition yields $$\log\zeta_{\mathrm{AM},Y}(z)=\sum_{m=1}^{\infty}\frac{z^m}{m}.$$ Formal differentiation gives $$\frac{d}{dz}\log\zeta_{\mathrm{AM},Y}(z)
  =\sum_{m=1}^{\infty}z^{m-1}=\frac{1}{1-z},$$ and the constant term is zero, so $\log\zeta_{\mathrm{AM},Y}(z)=-\log(1-z)$. Exponentiating yields $(1-z)^{-1}$. Analytically the same calculation holds for $|z|<1$.

The primitive Euler form has one factor because the only primitive orbit is $\mathcal O_0$: $$\prod_{\mathcal O\in\operatorname{Prim}(Y,S)}
  (1-z^{|\mathcal O|})^{-1}
  =(1-z)^{-1}.$$ Expanding the logarithm of this one factor produces all powers $z^r$. The expansion changes traversal number, not primitive identity.

## Finite-P0 witness, including the empty case

For nonempty finite $P_0$, [\[eq:finite-witness\]](#eq:finite-witness){reference-type="ref" reference="eq:finite-witness"} has support $1+Q\mathbb Z$. Modulo any $p^2\mid Q$, this support is exactly the single residue $1$, so every other residue is missing. If $d>0$ is a period, the implication $$x_1=1\Longrightarrow x_{1+d}=1$$ forces $1+d\equiv1\pmod Q$, hence $Q\mid d$. Since $Q$ itself is a period, the least period is exactly $Q$.

When $P_0=\varnothing$, the empty product is $Q=1$ and admissibility places no restriction on the full binary shift. The all-zero and all-one points are two distinct fixed points. This is the correct edge-case certificate; describing it as a nontrivial period-one orbit would be false.

# Typed contract, falsifiers, and provenance {#app:types-provenance}

## Object, marker, and operator types

::: {#tab:type-ledger}
  Symbol               Type and owner                                             Permitted role
  -------------------- ---------------------------------------------------------- -----------------------------------
  $x$                  `SquarefreeAdmissiblePoint`, owned by $X_{\mathrm{sf}}$    source coordinate state
  $\sigma$             `TwoSidedShiftHomeomorphism`, owned by $X_{\mathrm{sf}}$   unit source time
  $y$                  `TopologicalFactorState`, owned by $Y$                     target state
  $S$                  `FactorHomeomorphism`, owned by $Y$                        unit target time
  $\pi$                `ContinuousOntoZFactorMap`                                 source-to-target morphism
  $\mathcal O_0$       `PeriodicOrbit(Y,S)`                                       sole primitive factor orbit
  $p$                  `RationalPrimeAtom`, external                              comparator primitive only
  $K_{\mathrm{per}}$   `FiniteRankLedgerOperator`, periodic core                  packages fixed counts after proof

  : Typed ownership ledger.
:::

The marker $z$ is owned by the target's unit-time dynamics. The marker $u$, if used in the rational-prime comparator, is independently owned. Neither a symbol specialization nor equality of a scalar expression creates an objectwise correspondence. In particular, $$\mathcal O_0\not\equiv p,
  \qquad
  \mathcal O_0^r\not\equiv p_r,
  \qquad
  K_{\mathrm{per}}\not\equiv\text{a full-state transfer operator}.$$

## Proof-dependency and falsifier matrix

::: {#tab:falsifiers}
  Claim                 Falsifier                                                                                                                                         Required response
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------
  source compactness    exhibit a failed-admissibility point without a finite cylinder witness                                                                            reject topology lemma
  CRT synchronization   reuse a modulus with inconsistent missing residues or produce a nonzero requested coordinate                                                      reject proximality proof
  metric convergence    violate the tail bound in [\[eq:metric-tail\]](#eq:metric-tail){reference-type="ref" reference="eq:metric-tail"}                                  reject proximality conclusion
  factor permanence     remove a lift, uniform continuity, or equivariance                                                                                                mark the map outside scope
  periodic rigidity     exhibit a lawful periodic orbit with zero adjacent-orbit minimum                                                                                  reject separation lemma
  zeta identity         derive a fixed count other than one                                                                                                               reject determinant formula
  primitive firewall    count $z^r$ as a distinct primitive                                                                                                               flag repetition error
  finite-P0 sharpness   find a retained modulus met in every residue by [\[eq:finite-witness\]](#eq:finite-witness){reference-type="ref" reference="eq:finite-witness"}   reject the witness
  literature boundary   locate the exact theorem in a primary source                                                                                                      `STOP_DUPLICATE`

  : Independent failure tests for the theorem chain.
:::

## Chronology and decision boundary

The candidate selector was retrospective. All three commissioned card outcomes, the source literature, and the local proof chain were known before the rule identifying SD-C02 was written. Its unique return therefore gives no prospective, outcome-independent, ranking, authorization, novelty, or priority evidence.

The same limitation applies to the Route rendering. The tuple $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_ANALYTIC\_DETERMINANT},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$$ summarizes the proved source and typed ledger after the fact. The overall status is `ROUTE_A_REJECTED`, and `route_b_invocation_allowed=false`. No earlier paper authorizes or ranks this candidate; predecessor records are collision and chronology inputs only.

## Literature and metadata caveats

The bibliography contains only records whose author, title, date, and identifier were checked against the frozen literature audit and its cited institutional, DOI, or arXiv record. The Gundlach--Klüners entry is kept as an arXiv record because the frozen audit binds version 2 and does not freeze final journal volume or page metadata. The Sarnak item is an institutional lecture-note record rather than a journal article. These choices avoid inventing publication fields.

The bounded audit found no exact duplicate with the full source and target quantifiers. That negative result is not exhaustive and is not a basis for priority. Any later exact collision supersedes the external framing while leaving the proof and internal audit trail intact.
