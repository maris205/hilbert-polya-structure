---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c431-optimal-cycle-measures"
canonical_tex: "henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures/main.tex"
canonical_pdf: "henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures/main.pdf"
source_sha256: "665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Haar limits of optimal wild cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures>)
- [规范 TeX](<../../../../../henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures/main.pdf>)
- [BibTeX](<../../../../../henon_dynamics/research_c429_c433/papers/C431_optimal_cycle_measures/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a complete algebraically closed ultrametric field of odd characteristic $p$, we prove that the uniform measures on the small cycles of $P_\lambda(z)=\lambda z+z^2$ converge whenever $0<|\lambda-1|<1$. The conclusion concerns the entire sequence of cycles of least periods $p^e$, over every field and multiplier in this range. Their union has compact closure in the classical field, and their Hausdorff limit is a compact invariant set on which $P_\lambda$ is conjugate to addition by one on $\mathbb Z_p$. The limiting probability is the corresponding nonatomic Haar measure, with support consisting entirely of type-I points. The main estimate is an exact average-contact identity between any fixed cycle and every higher cycle. With $s=\lambda-1$ and $r=(p-1)/p$, its normalized average $c_d$ satisfies $c_d\ge d r^3+r^2(1+1/p)$; the Hausdorff and essential-supremum transport errors are at most $|s|^{c_d}$. A finite upper bound on contacts with each old cycle excludes periodic points from the limit. The proof answers the selected-cycle convergence question posed by Lindahl and Rivera-Letelier without a discrete-valuation or field-nesting assumption.
author:
- Anonymous Authors
bibliography:
- references.bib
title: Haar limits of optimal wild cycles
```

## Markdown 正文

# Introduction and main theorem {#sec:introduction}

The location of a periodic orbit does not determine how a sequence of such orbits is distributed. This distinction is particularly concrete for the polynomial $P_\lambda(z)=\lambda z+z^2$ in positive characteristic: its small cycles occupy one sphere, although their ordinary periods tend to infinity. We prove that these cycles converge to a classical compact adding-machine system, and give a quantitative estimate for their supports and uniform probability measures.

Throughout the article, $p$ is an odd prime, $(K,|\cdot|)$ is a complete algebraically closed ultrametric field of characteristic $p$, and $$\label{eq:setup}
  s=\lambda-1,\qquad 0<|s|<1,\qquad
  P(z)=(1+s)z+z^2,\qquad r=\frac{p-1}{p}.$$ We normalize the real valuation by $v(x)=\log|x|/\log|s|$ for $x\ne0$ and $v(0)=+\infty$. For a positive integer $a$, $v_p(a)$ denotes the exponent of $p$ dividing $a$, distinct from the field valuation $v$. We write $\mathbb Z_p=\varprojlim_{n\ge1}\mathbb Z/p^n\mathbb Z$ with its usual inverse-limit topology. For $e\ge1$, let $\Pi_e$ be the unique cycle in the open unit disk of ordinary least period $p^e$, and put $$\label{eq:cycle-measures}
  \mu_e=p^{-e}\sum_{\alpha\in\Pi_e}\delta_\alpha.$$ The existence, uniqueness, distinctness, and common radius $|\alpha|=|s|^r$ are the optimal-cycle results of Lindahl--Rivera-Letelier [@lindahl2016optimal Theorem C and the $q=1$ discussion]. All masses in [\[eq:cycle-measures\]](#eq:cycle-measures){reference-type="eqref" reference="eq:cycle-measures"} are real numbers.

Distances between classical points are $d(x,y)=|x-y|$. For nonempty compact sets $E,F$ we use the Hausdorff distance $$d_H(E,F)=\max\left\{\sup_{x\in E}\inf_{y\in F}d(x,y),
                         \sup_{y\in F}\inf_{x\in E}d(x,y)\right\}.$$ A coupling of probabilities $\sigma,\tau$ is a probability on the product with those marginals. Write $W_1(\sigma,\tau)$ for the infimum of $\int d(x,y)\,d\pi$ over couplings, and $W_\infty(\sigma,\tau)$ for the infimum of their essential supremum of $d(x,y)$. All measures used in these distances below are carried by a common compact metric space. Weak convergence on $\mathbb P^{1,\mathrm{an}}_K$ means convergence against every continuous real-valued function there.

[\[thm:compact-adding-machine\]]{#thm:compact-adding-machine label="thm:compact-adding-machine"} Under [\[eq:setup\]](#eq:setup){reference-type="eqref" reference="eq:setup"}, the following conclusions hold.

1.  The classical closure $$C=\operatorname{cl}_K\!\left(\bigcup_{e\ge1}\Pi_e\right)$$ is compact. The entire sequence $\Pi_e$ has a nonempty Hausdorff limit $\mathcal A\subset C$, with $P(\mathcal A)=\mathcal A$ and $|a|=|s|^r$ for $a\in\mathcal A$.

2.  For $d\ge1$ and any $\beta\in\Pi_d$, the number $$\label{eq:main-cd}
     c_d=\frac{p-1}{p^{d+1}}
           v\!\left((P^{\circ p^d})'(\beta)-1\right)$$ is finite and independent of $\beta$. For every $e>d$, $$\label{eq:main-contact}
     \frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
     =c_d\ge d r^3+r^2\left(1+\frac1p\right).$$

3.  The entire sequence $\mu_e$ converges weakly on $\mathbb P^{1,\mathrm{an}}_K$ to a probability $\mu$ supported exactly on $\mathcal A$. For each $d\ge1$, $$\label{eq:main-rate}
     d_H(\Pi_d,\mathcal A)\le |s|^{c_d},\qquad
     W_1(\mu_d,\mu)\le W_\infty(\mu_d,\mu)\le |s|^{c_d}.$$

4.  There is a homeomorphism $\theta:\mathbb Z_p\to\mathcal A$ such that $P(\theta(t))=\theta(t+1)$. The measure $\mu$ is the pushforward of Haar probability under $\theta$, is nonatomic, and is the unique $P$-invariant probability on $\mathcal A$. In particular $\mathcal A$ has no periodic points and consists entirely of type-I points of $\mathbb P^{1,\mathrm{an}}_K$.

This answers Problem 1.3 in the 26 May 2015 version of Lindahl--Rivera-Letelier [@lindahl2016optimal], with its original field and multiplier quantifiers. The assertion concerns each fixed allowed $\lambda$; it does not give convergence uniform as $|\lambda-1|\to1$. The set $C$ contains the old finite cycles and their invariant atomic measures. Unique ergodicity in the theorem is asserted only on $\mathcal A$, not on $C$.

The main arithmetic step is [\[eq:main-contact\]](#eq:main-contact){reference-type="eqref" reference="eq:main-contact"}. Differentiating a small-cycle factorization at a level-$d$ anchor expresses its multiplier through within-cycle distances. Differentiating every higher return quotient at the same anchor then gives its mean contact with $\Pi_e$. A characteristic-$p$ displacement estimate makes that mean diverge as $d$ grows. Because $P$ is isometric on the relevant disk, a single close pair couples the complete cycles. The finite value of the same mean also separates every fixed old cycle from the limit, which is the additional input needed for aperiodicity.

#### Relation to other measures and classical inputs.

Jacobs proves convergence of Rumely's crucial measures to the canonical dynamical measure [@jacobs2017crucial Theorem 2]. His reduction-dependent weights are supported at type-II points; they are not the uniform measures [\[eq:cycle-measures\]](#eq:cycle-measures){reference-type="eqref" reference="eq:cycle-measures"}. This distinction is one of measures, not of characteristic. The periodic-point norm bounds of Nordqvist--Rivera-Letelier [@nordqvist2020residue Theorem 3] concern ramified multiplier-one series and do not provide the cross-level estimate used here. We use classical seminorm topology for the Berkovich line [@baker2007berkovich]. The finite-quotient inverse-limit description and invariant measure of minimal equicontinuous Cantor systems are classical; see Hurder--Lukina [@hurder2025essential author version, Sections 2.2--2.3]. We give the required cyclic-partition proof, including the finite alternative, in full.

The argument is independent of any full-inertia theorem for local periodic fields, of Artin--Schreier character stabilization, or of a nested sequence of splitting fields. The coefficient-field construction in Section [2](#sec:coefficients){reference-type="ref" reference="sec:coefficients"} is a proof device inside arbitrary $K$, not a restriction of the theorem to a Laurent-series field. Sections [3](#sec:displacements){reference-type="ref" reference="sec:displacements"}--[4](#sec:contacts){reference-type="ref" reference="sec:contacts"} prove the contact estimate; Sections [5](#sec:compact){reference-type="ref" reference="sec:compact"}--[6](#sec:adding-machine){reference-type="ref" reference="sec:adding-machine"} prove the compact, measure, and adding-machine conclusions.

# Small factors over an arbitrary complete field {#sec:coefficients}

We first construct the factorization used in the contact calculation without assuming irreducibility or local inertia. Write $$\label{eq:returns}
 F_e(z)=P^{\circ p^e}(z)-z\quad(e\ge0),\qquad
 Q_e(z)=F_e(z)/F_{e-1}(z)\quad(e\ge1).$$ These indices label $p$-power returns; the superscript $\circ$ always denotes ordinary iteration. The minimal ramification of $g(z)=z+z^2$ gives the source input $$\label{eq:minimal-ramification}
 \operatorname{ord}_z\bigl(g^{\circ p^e}(z)-z\bigr)
 =1+\frac{p^{e+1}-1}{p-1}\qquad(e\ge0).$$ This is the $q=1$ reduction underlying the optimal-cycle theorem [@lindahl2016optimal Theorem C and the $q=1$ discussion]. The other input is the already established set of $p^e$ distinct points $\Pi_e$, each of valuation $r$. We will use degree to identify the whole small factor, so no further separability premise is needed.

[\[lem:coefficient-field\]]{#lem:coefficient-field label="lem:coefficient-field"} Let $k_0\subset K$ be the subfield of elements algebraic over $\mathbb F_p$. There is an isometric embedding $$\iota:k_0((t))\longrightarrow K,\qquad t\longmapsto s,$$ where $k_0((t))$ has norm $|s|^{\operatorname{ord}_t}$.

Algebraic closedness of $K$ makes $k_0$ an algebraic closure of $\mathbb F_p$. Every nonzero element of $k_0$ lies in a finite field and has norm one, since it is a root of unity. For a Laurent series $a(t)=\sum_{n\ge n_0}a_nt^n$, set $$\iota(a)=\sum_{n\ge n_0}a_ns^n.$$ Its terms tend to zero, so the ultrametric inequality and completeness of $K$ give convergence. If $n_*$ is its first nonzero coefficient index, the leading term has norm $|s|^{n_*}$ and the remaining tail has norm at most $|s|^{n_*+1}$. Thus $$\label{eq:embedding-norm}
 |\iota(a)|=|s|^{n_*}\qquad(a\ne0).$$ Addition and multiplication are preserved on finite Laurent polynomials. Approximating arbitrary series by finite truncations and using continuity of both operations proves the same for series. Equation [\[eq:embedding-norm\]](#eq:embedding-norm){reference-type="eqref" reference="eq:embedding-norm"} gives injectivity, and preservation of $1$ and multiplication gives preservation of inverses. The norm identity proves the isometry. No equality between the residue field of $K$ and $k_0$ is assumed.

[\[lem:small-factor\]]{#lem:small-factor label="lem:small-factor"} For every $e\ge1$ there are monic $M_e,V_e\in K[z]$ with integral coefficients such that $$\label{eq:small-factor}
 F_e=F_{e-1}M_eV_e,\qquad
 M_e(z)=\prod_{\alpha\in\Pi_e}(z-\alpha),\qquad
 v(V_e(x))=0\quad\text{if }v(x)>0.$$

Work first over the complete discrete valuation ring $R=k_0[[t]]$ with $P_t(z)=(1+t)z+z^2$, and attach a subscript $t$ to the returns in [\[eq:returns\]](#eq:returns){reference-type="eqref" reference="eq:returns"}. For a polynomial $h$, the relation $h(z)=z$ in the quotient by $h(z)-z$ implies $h^{\circ p}(z)=z$ there. Taking $h=P_t^{\circ p^{e-1}}$ proves divisibility of $F_{e,t}$ by $F_{e-1,t}$. Monic division gives a monic quotient $Q_{e,t}$ in $R[z]$, and reduction commutes with this division.

Successive orders in [\[eq:minimal-ramification\]](#eq:minimal-ramification){reference-type="eqref" reference="eq:minimal-ramification"} differ by $p^e$. Consequently $$\overline Q_{e,t}(z)=z^{p^e}\overline V_e(z),
 \qquad \overline V_e(0)\ne0.$$ The displayed monic factors are coprime. Coprime Hensel factorization over $R$ gives monic polynomials $M_{e,t},V_{e,t}\in R[z]$ with $$Q_{e,t}=M_{e,t}V_{e,t},\qquad
 \deg M_{e,t}=p^e,\qquad
 \overline M_{e,t}=z^{p^e},\qquad
 \overline V_{e,t}(0)\ne0.$$ Apply Lemma [\[lem:coefficient-field\]](#lem:coefficient-field){reference-type="ref" reference="lem:coefficient-field"} coefficientwise. The resulting $M_e,V_e$ have integral coefficients, and $V_e(0)$ is a unit. At an input of positive valuation, every positive-degree term of $V_e$ has positive valuation. Hence $v(V_e(x))=0$ there.

For $\alpha\in\Pi_e$, its least period implies $F_{e-1}(\alpha)\ne0$. The transported factorization therefore forces $M_e(\alpha)=0$. There are $p^e$ distinct such points and $M_e$ is monic of degree $p^e$. This proves its exact root product in [\[eq:small-factor\]](#eq:small-factor){reference-type="eqref" reference="eq:small-factor"} and completes the argument.

The construction takes place over one coefficient field that embeds in every allowed $K$. It uses neither a generic-specialization argument nor any conclusion about the Galois group of $M_e$.

# Native isometry and displacement bounds {#sec:displacements}

Set $\mathcal D=\{x\in K:v(x)\ge r\}$, a complete closed disk. It contains every $\Pi_e$. Since $|1+s|=1$ and $|x|<1$ on this disk, $P(\mathcal D)\subseteq\mathcal D$. The identity $$\label{eq:difference}
 P(x)-P(y)=(x-y)(1+s+x+y)$$ contains slightly more information than isometry: the unit factor has residue one.

[\[lem:isometry\]]{#lem:isometry label="lem:isometry"} For $x,y\in\mathcal D$ and every integer $a\ge0$, $$|P^{\circ a}(x)-P^{\circ a}(y)|=|x-y|.$$ If $x\ne y$, then $$\label{eq:residue-one}
 \frac{P^{\circ a}(x)-P^{\circ a}(y)}{x-y}
 \in 1+\{u\in K:v(u)\ge r\}.$$

In [\[eq:difference\]](#eq:difference){reference-type="eqref" reference="eq:difference"}, $v(s)=1>r$ and $v(x),v(y)\ge r$. Thus the second factor lies in the set on the right of [\[eq:residue-one\]](#eq:residue-one){reference-type="eqref" reference="eq:residue-one"} and has norm one. Products of elements of that set remain in the set. Iteration proves both assertions.

Fix $d\ge1$ and $\beta\in\Pi_d$. For $0\le j<d$, define the finite quantities $$\label{eq:deltas}
 \delta_j= v(P^{\circ p^j}(\beta)-\beta).$$

[\[lem:index\]]{#lem:index label="lem:index"} For $1\le a<p^d$, $$\label{eq:index}
 v(P^{\circ a}(\beta)-\beta)=\delta_{v_p(a)}.$$ There are $(p-1)p^{d-j-1}$ indices contributing the value $\delta_j$ in this formula. Distinct $j$ need not give distinct valuation values.

Write $a=kp^j$ with $p\nmid k$ and set $G=P^{\circ p^j}$. The telescoping identity $$G^{\circ k}(\beta)-\beta
 =\sum_{i=0}^{k-1}
   \bigl(G^{\circ(i+1)}(\beta)-G^{\circ i}(\beta)\bigr)$$ may be divided by $G(\beta)-\beta\ne0$. By [\[eq:residue-one\]](#eq:residue-one){reference-type="eqref" reference="eq:residue-one"}, each resulting summand has residue one. Their sum has residue $k\ne0$, so it has valuation zero. This proves [\[eq:index\]](#eq:index){reference-type="eqref" reference="eq:index"}. The count is the number of integers in $\{1,\ldots,p^d-1\}$ divisible by $p^j$ but not by $p^{j+1}$.

[\[lem:displacement\]]{#lem:displacement label="lem:displacement"} For all $d\ge1$, $\beta\in\Pi_d$, and $0\le j<d$, $$\label{eq:displacement}
 \delta_j\ge(p^j+1)r.$$

For $H(z)=\sum_i h_i z^i\in K[z]$, define the weighted Gauss valuation $$w_r(H)=\min_{h_i\ne0}\{v(h_i)+ir\},\qquad w_r(0)=+\infty.$$ Let $U$ be the $K$-linear operator $UH=H\circ P$, and put $\Delta=U-I$. For every integer $i\ge1$, $$\Delta(z^i)=z^i\bigl((1+s+z)^i-1\bigr).$$ The constant coefficient in the bracket has valuation at least one if nonzero. Every positive-degree term has weighted valuation at least $r$, since its coefficient is integral. Because $1>r$, the bracket has weight at least $r$. Constants have zero image under $\Delta$, and the ultrametric inequality gives $$\label{eq:delta-weight}
 w_r(\Delta H)\ge w_r(H)+r.$$ It follows by induction that $w_r(\Delta^N z)\ge(N+1)r$ for all positive integers $N$. The operators $U$ and $I$ commute, and their coefficient field has characteristic $p$. Thus $$\Delta^{p^j}=U^{p^j}-I.$$ Evaluation at $\beta$, whose valuation is $r$, cannot decrease the weighted lower bound. This gives [\[eq:displacement\]](#eq:displacement){reference-type="eqref" reference="eq:displacement"}. The argument applies to real, possibly nondiscrete valuations.

# The all-higher-level contact identity {#sec:contacts}

The key estimate is obtained by keeping the anchor fixed while the higher return level varies. Write $$m_d=(P^{\circ p^d})'(\beta),\qquad A_d=v(m_d-1),
 \qquad \beta\in\Pi_d.$$ We first prove that $m_d-1$ is nonzero, before using it as a denominator.

[\[prop:contacts\]]{#prop:contacts label="prop:contacts"} For every $d\ge1$ and $\beta\in\Pi_d$, $$\label{eq:multiplier-sum}
 A_d=\delta_{d-1}+
       \sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j<\infty.$$ The value $A_d$ is independent of $\beta$. For every $e>d$, $$\label{eq:contact-equality}
 \frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
 =c_d:=\frac{p-1}{p^{d+1}}A_d
 \ge b_d:=d r^3+r^2\left(1+\frac1p\right).$$

Differentiate the factorization of Lemma [\[lem:small-factor\]](#lem:small-factor){reference-type="ref" reference="lem:small-factor"} at level $d$ and evaluate at $\beta$. Since $M_d(\beta)=0$, $$\label{eq:multiplier-product}
 m_d-1=F_{d-1}(\beta)M_d'(\beta)V_d(\beta).$$ The first factor on the right is nonzero by the least-period condition, the second by the simple root product for $M_d$, and the third because it is a unit. Hence $m_d\ne1$. Taking valuations and using Lemma [\[lem:index\]](#lem:index){reference-type="ref" reference="lem:index"} gives $$\begin{aligned}
 A_d
 &=v(F_{d-1}(\beta))+
      \sum_{\gamma\in\Pi_d\setminus\{\beta\}}v(\beta-\gamma)\\
 &=\delta_{d-1}+\sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j.\end{aligned}$$ The chain-rule expression for $m_d$ is the product of $P'$ over all points of the cycle. A different anchor only permutes its factors, proving independence of $A_d$.

Now let $e>d$. Both $F_e$ and $F_{e-1}$ vanish at $\beta$. Differentiating $F_e=F_{e-1}Q_e$ there gives $$\label{eq:derivative-quotient}
 F_e'(\beta)=F_{e-1}'(\beta)Q_e(\beta).$$ Because $P^{\circ p^d}$ fixes $\beta$, the chain rule and characteristic $p$ yield $$F_e'(\beta)=m_d^{p^{e-d}}-1=(m_d-1)^{p^{e-d}},\qquad
 F_{e-1}'(\beta)=(m_d-1)^{p^{e-d-1}}\ne0.$$ The last exponent is one when $e=d+1$, so that boundary case also allows division in [\[eq:derivative-quotient\]](#eq:derivative-quotient){reference-type="eqref" reference="eq:derivative-quotient"}. We obtain $$\label{eq:higher-quotient}
 Q_e(\beta)=(m_d-1)^{(p-1)p^{e-d-1}}.$$ Distinct least periods make $\Pi_d$ and $\Pi_e$ disjoint. Using $Q_e=M_eV_e$, the unit value of $V_e(\beta)$ and the exact root product for $M_e$, equation [\[eq:higher-quotient\]](#eq:higher-quotient){reference-type="eqref" reference="eq:higher-quotient"} becomes $$\label{eq:contact-total}
 \sum_{\alpha\in\Pi_e}v(\beta-\alpha)
 =(p-1)p^{e-d-1}A_d.$$ All summands are finite. Division by the real number $p^e$ proves the equality in [\[eq:contact-equality\]](#eq:contact-equality){reference-type="eqref" reference="eq:contact-equality"}.

Finally Lemma [\[lem:displacement\]](#lem:displacement){reference-type="ref" reference="lem:displacement"} and [\[eq:multiplier-sum\]](#eq:multiplier-sum){reference-type="eqref" reference="eq:multiplier-sum"} give $$\begin{aligned}
 \frac{A_d}{p^d}
 &\ge \frac{r(p^{d-1}+1)}{p^d}
     +\frac r{p^d}\sum_{j=0}^{d-1}
        (p-1)p^{d-j-1}(p^j+1)\\
 &=r\left(1+\frac1p+d\frac{p-1}{p}\right).\end{aligned}$$ Multiplication by $(p-1)/p=r$ proves the lower bound in [\[eq:contact-equality\]](#eq:contact-equality){reference-type="eqref" reference="eq:contact-equality"}. In particular $c_d\to+\infty$.

[\[cor:coupling\]]{#cor:coupling label="cor:coupling"} For every $e>d$, there is a coupling of $\mu_e$ and $\mu_d$ all of whose support pairs have distance at most $|s|^{c_d}$. Moreover $d_H(\Pi_e,\Pi_d)\le|s|^{c_d}$.

Fix $\beta\in\Pi_d$. One contact in [\[eq:contact-equality\]](#eq:contact-equality){reference-type="eqref" reference="eq:contact-equality"} is at least its real average. Choose $\alpha\in\Pi_e$ realizing such a contact. Lemma [\[lem:isometry\]](#lem:isometry){reference-type="ref" reference="lem:isometry"} gives $$|P^{\circ i}(\alpha)-P^{\circ i}(\beta)|
 =|\alpha-\beta|\le |s|^{c_d}\qquad(i\ge0).$$ The real probability $$\label{eq:aligned-coupling}
 \pi_{e,d}=p^{-e}\sum_{i=0}^{p^e-1}
    \delta_{(P^{\circ i}(\alpha),P^{\circ i}(\beta))}$$ has first marginal $\mu_e$. Each point of $\Pi_d$ appears $p^{e-d}$ times in the second coordinate, giving marginal $\mu_d$. The same matched iterates cover both cycle sets and prove the Hausdorff bound. No compatible phases across different pairs of levels are required.

# Compact supports and convergence of measures {#sec:compact}

We record the metric argument at the generality used here. It does not require local compactness of the ambient space, and it separates the closure containing every old cycle from the limiting support.

[\[lem:exact-distances\]]{#lem:exact-distances label="lem:exact-distances"} Let $T$ be an isometry of a metric space. For finite single $T$-cycles $E,F$ with uniform probabilities $\sigma_E,\sigma_F$, put $a=\min_{x\in E,y\in F}d(x,y)$. Then $$\label{eq:exact-distances}
 d_H(E,F)=W_1(\sigma_E,\sigma_F)
        =W_\infty(\sigma_E,\sigma_F)=a.$$

Choose a nearest pair $x,y$, let the cycle lengths be $m,n$, and put $L=\mathop{\mathrm{lcm}}(m,n)$. The probability $$\pi=\frac1L\sum_{j=0}^{L-1}\delta_{(T^jx,T^jy)}$$ has the required marginals, since each coordinate point occurs $L/m$ or $L/n$ times. Isometry makes every paired distance equal to $a$. Every pair in $E\times F$ has distance at least $a$, so no coupling has smaller mean or essential-supremum cost. The iterates also cover both finite sets, proving both directed Hausdorff distances equal to $a$.

[\[prop:compact-limit\]]{#prop:compact-limit label="prop:compact-limit"} Let $(X,d)$ be a complete ultrametric space, let $T:X\to X$ be an isometry, and let $C_e$ be a nonempty finite single $T$-cycle for each $e\ge1$. Let $\sigma_e$ be its uniform probability, and suppose $$\label{eq:contact-criterion}
 a_{d,e}=\min_{x\in C_d,y\in C_e}d(x,y),\qquad
 \varepsilon_d=\sup_{e>d}a_{d,e}\longrightarrow0.$$ Then $B=\operatorname{cl}_X\bigl(\bigcup_e C_e\bigr)$ is compact and $T(B)=B$. There is a nonempty compact set $A\subset B$ with $T(A)=A$ such that $C_e\to A$ in Hausdorff distance. The probabilities $\sigma_e$ converge weakly on $B$ to an invariant probability $\sigma$ with $\operatorname{supp}\sigma\subset A$. For every $d\ge1$, $$\label{eq:general-limit-bound}
 d_H(C_d,A)\le\varepsilon_d,\qquad
 W_1(\sigma_d,\sigma)\le W_\infty(\sigma_d,\sigma)
 \le\varepsilon_d.$$

Fix $\eta>0$ and choose $d$ with $\varepsilon_d<\eta$. Lemma [\[lem:exact-distances\]](#lem:exact-distances){reference-type="ref" reference="lem:exact-distances"} makes $C_d$ a finite $\eta$-net for every later cycle. Adding all earlier cycle points gives a finite net for the entire union. That union is totally bounded, as is its closure $B$. The latter is complete because it is closed in $X$. A complete totally bounded metric space is compact: successive finite covers of radii tending to zero provide a Cauchy subsequence of any sequence, and completeness supplies its limit. Thus $B$ is compact.

The map $T$ sends the union of cycles onto itself. By continuity it maps $B$ into $B$, and its compact image is closed and contains the dense union. Hence $T(B)=B$. No surjectivity on $X$ was assumed.

By [\[eq:exact-distances\]](#eq:exact-distances){reference-type="eqref" reference="eq:exact-distances"}, the cycle sets are Hausdorff-Cauchy. Define their nonempty compact tail intersection by $$\label{eq:tail-set}
 A=\bigcap_{N\ge1}\operatorname{cl}_B\!\left(\bigcup_{e\ge N}C_e\right).$$ We verify Hausdorff convergence directly. Given $\eta>0$, choose $N$ so that $d_H(C_e,C_f)<\eta/2$ whenever $e,f\ge N$. Fix $e\ge N$ and $x\in C_e$. Points in arbitrarily late $C_f$ can be chosen within $\eta/2$ of $x$; a subsequence converges in $B$ to a point of $A$ at distance at most $\eta/2$ from $x$. Conversely, each $y\in A$ is the limit of points in cycles with indices tending to infinity. Choose nearby points of the fixed compact set $C_e$ and pass to a convergent subsequence there. This gives a point of $C_e$ within $\eta/2$ of $y$. Both bounds are uniform, proving $d_H(C_e,A)\to0$. The same argument with $d$ fixed and $d_H(C_d,C_e)\le\varepsilon_d$ for all $e>d$ gives the first inequality in [\[eq:general-limit-bound\]](#eq:general-limit-bound){reference-type="eqref" reference="eq:general-limit-bound"}.

Continuity implies $T(A)\subset A$. For the reverse inclusion, write $y\in A$ as a limit of $y_j\in C_{e_j}$, $e_j\to\infty$. Choose a predecessor $x_j\in C_{e_j}$ with $T(x_j)=y_j$. A convergent subsequence of $x_j$ has limit $x\in A$, and $T(x)=y$. Therefore $T(A)=A$.

For $\varphi\in C(B,\mathbb R)$ let $$\omega_\varphi(t)=\sup\{|\varphi(x)-\varphi(y)|:
                      x,y\in B,\ d(x,y)\le t\}.$$ Compactness gives uniform continuity, so $\omega_\varphi(t)\to0$ as $t\downarrow0$. The coupling in Lemma [\[lem:exact-distances\]](#lem:exact-distances){reference-type="ref" reference="lem:exact-distances"} yields $$\label{eq:modulus-bound}
 \left|\int\varphi\,d\sigma_e-\int\varphi\,d\sigma_d\right|
 \le\omega_\varphi(\varepsilon_d)\qquad(e>d).$$ Thus the integrals converge for every such $\varphi$. Their limits define a positive norm-one linear functional taking the constant one to one. The Riesz representation theorem on the compact Hausdorff space $B$ gives a regular Borel probability $\sigma$. This is convergence of the full sequence. Applying it to $\varphi\circ T$ proves invariance. The continuous nonnegative function $x\mapsto d(x,A)$ has integrals tending to zero by Hausdorff convergence; hence $\operatorname{supp}\sigma\subset A$.

For the transport bound, fix $d$ and consider the finite-cycle couplings with $\sigma_e$ for $e>d$. Probabilities on the compact metric space $B\times B$ admit a weakly convergent subsequence. One proof takes a countable uniformly dense subset of continuous functions, extracts a diagonal subsequence of their integrals, and uses Riesz representation for the resulting positive functional. The limiting coupling has marginals $\sigma_d,\sigma$. The nonnegative continuous function $(x,y)\mapsto
\max\{d(x,y)-\varepsilon_d,0\}$ has integral zero along these couplings and in their limit. The limit is therefore supported on $d(x,y)\le\varepsilon_d$. This proves the remaining inequalities in [\[eq:general-limit-bound\]](#eq:general-limit-bound){reference-type="eqref" reference="eq:general-limit-bound"}.

## Application to the optimal cycles

Apply Proposition [\[prop:compact-limit\]](#prop:compact-limit){reference-type="ref" reference="prop:compact-limit"} to the complete disk $\mathcal D$, the isometry $P$, and the cycles $\Pi_e$. Corollary [\[cor:coupling\]](#cor:coupling){reference-type="ref" reference="cor:coupling"} gives $$\varepsilon_d\le |s|^{c_d}
 \le |s|^{d r^3+r^2(1+1/p)}\longrightarrow0.$$ It follows that $C=\operatorname{cl}_K\bigl(\bigcup_e\Pi_e\bigr)$ is compact, that the full sequence has Hausdorff limit $\mathcal A$, and that $\mu_e$ has an invariant weak limit $\mu$ on $C$ with $\operatorname{supp}\mu\subset\mathcal A$. The norm is continuous, so $C$ and $\mathcal A$ remain on $|z|=|s|^r$. The inequalities [\[eq:main-rate\]](#eq:main-rate){reference-type="eqref" reference="eq:main-rate"} have also been proved.

To interpret the limit on $\mathbb P^{1,\mathrm{an}}_K$, send $a\in K$ to the evaluation seminorm at $a$. This map is continuous: each defining coordinate $a\mapsto|H(a)|$, $H\in K[z]$, is continuous. The Berkovich projective line is Hausdorff; see the seminorm and analytification background in [@baker2007berkovich Sections 2.3--2.4]. The restriction to compact $C$ is therefore a homeomorphism onto a closed compact image. Pushing $\mu$ forward gives a Radon probability on $\mathbb P^{1,\mathrm{an}}_K$. Every continuous real test function on $\mathbb P^{1,\mathrm{an}}_K$ restricts to one on $C$, so convergence on $C$ proves the required weak convergence on $\mathbb P^{1,\mathrm{an}}_K$. Neither compactness of an ambient classical disk nor metrizability of the entire Berkovich line has been used.

# Aperiodicity and the Haar adding-machine limit {#sec:adding-machine}

We first establish the general structure of the compact limit. The polynomial contact identity will then exclude the finite possibilities in that structure theorem.

[\[prop:odometer\]]{#prop:odometer label="prop:odometer"} Under the hypotheses of Proposition [\[prop:compact-limit\]](#prop:compact-limit){reference-type="ref" reference="prop:compact-limit"}, $T|_A$ is minimal and uniquely ergodic, and $\operatorname{supp}\sigma=A$. If $|C_e|=p^e$ for a prime $p$, the system is conjugate either to addition by one on $\mathbb Z/p^k\mathbb Z$ for some $k\ge0$, or to addition by one on $\mathbb Z_p$. Its invariant probability is the corresponding Haar probability.

Fix $x,y\in A$ and $\eta>0$. Choose a cycle $C_e$ with $d_H(C_e,A)<\eta$ and points $u,v\in C_e$ satisfying $d(u,x),d(v,y)<\eta$. Some $j\ge0$ has $T^ju=v$. Isometry and the ultrametric inequality give $$d(T^jx,y)\le\max\{d(T^jx,T^ju),d(v,y)\}<\eta.$$ Every forward orbit in $A$ is dense. The support of the invariant probability is a nonempty closed forward-invariant subset of $A$, so it equals $A$.

Choose a decreasing sequence $\eta_j>0$ tending to zero. On $A$ define $x\sim_j y$ by $d(x,y)<\eta_j$. The ultrametric inequality makes this an equivalence relation. Its classes are clopen and, by compactness, form a finite quotient $Q_j$. Since $T(A)=A$ and $T$ is an isometry, it induces a permutation of $Q_j$. Minimality forces this permutation to be one cycle. Put $q_j=|Q_j|$.

Any invariant probability on $A$ must assign each cell mass $1/q_j$. These partitions refine and have mesh tending to zero. Functions constant on their cells approximate every continuous function uniformly. Hence those masses determine all continuous-function integrals, proving uniqueness of the invariant probability.

Assume now $|C_e|=p^e$. For a fixed $j$, choose $e$ with $d_H(C_e,A)<\eta_j$. Map $u\in C_e$ to the class of a nearby $x\in A$ with $d(u,x)<\eta_j$. Two choices of $x$ have distance less than $\eta_j$, so the map is well-defined. The other directed Hausdorff bound makes it onto, and isometry makes it equivariant. It maps a $p^e$-cycle onto a $q_j$-cycle, so $q_j\mid p^e$. Thus $q_j=p^{k_j}$ for some integer $k_j\ge0$.

Choose a basepoint $a\in A$ and label the cell containing $T^ma$ by $m\bmod q_j$. Transitivity makes this a well-defined labeling of every cell. Refinement is then the reduction map $$\mathbb Z/q_{j+1}\mathbb Z\longrightarrow
 \mathbb Z/q_j\mathbb Z,
 \qquad q_j\mid q_{j+1}.$$ The resulting coding map $$\label{eq:inverse-limit}
 A\longrightarrow\varprojlim_j\mathbb Z/q_j\mathbb Z$$ is continuous and injective because the cell diameters tend to zero. A compatible sequence of cells is nested, nonempty, and compact; its intersection is nonempty by compactness and is a singleton by vanishing diameter. This proves surjectivity. The map is a homeomorphism and conjugates $T$ to addition by one.

If $k_j$ is bounded, it eventually stabilizes and the inverse limit is one finite $p$-power cycle, including a singleton. Otherwise $p^{k_j}$ is cofinal among all powers of $p$, and [\[eq:inverse-limit\]](#eq:inverse-limit){reference-type="eqref" reference="eq:inverse-limit"} is $\mathbb Z_p$. In each case the invariant probability is uniform on every finite quotient and hence is Haar probability. In the infinite case, the mass of a point is at most $p^{-k_j}$ for every $j$, proving non-atomicity.

[\[prop:aperiodicity\]]{#prop:aperiodicity label="prop:aperiodicity"} For every $d\ge1$, define $$\label{eq:old-cycle-contact-bound}
 U_d=p^d c_d-(p^d-1)r<\infty.$$ For $e>d$, $\beta\in\Pi_d$, and $\alpha\in\Pi_e$, $$\label{eq:old-cycle-separation}
 v(\beta-\alpha)\le U_d,\qquad
 |\beta-\alpha|\ge |s|^{U_d}>0.$$ Consequently $\mathcal A\cap\Pi_d=\varnothing$ for every $d$, and $P|_\mathcal A$ is the infinite $p$-adic adding machine.

Put $h=v(\beta-\alpha)$. The $p^{e-d}$ distinct points $$P^{\circ jp^d}(\alpha),\qquad 0\le j<p^{e-d},$$ all have contact $h$ with $\beta$: the iterate fixes $\beta$ and is an isometry. Every remaining point of $\Pi_e$ has contact at least $r$, since both points lie on the sphere of radius $|s|^r$. The exact mean identity [\[eq:contact-equality\]](#eq:contact-equality){reference-type="eqref" reference="eq:contact-equality"} therefore gives $$c_d\ge p^{-d}h+(1-p^{-d})r.$$ Rearranging proves [\[eq:old-cycle-separation\]](#eq:old-cycle-separation){reference-type="eqref" reference="eq:old-cycle-separation"}. Its distance bound is uniform in every $e>d$ and every point of the two cycles. Pass to the Hausdorff limit of the higher cycles to obtain $\mathcal A\cap\Pi_d=\varnothing$.

Proposition [\[prop:odometer\]](#prop:odometer){reference-type="ref" reference="prop:odometer"} leaves only a finite $p^k$-cycle or the $p$-adic adding machine. A finite alternative with $k\ge1$ would lie in the open unit disk and, by uniqueness of the cycle of that period, equal $\Pi_k$. This contradicts the separation just proved. A singleton alternative would be a fixed point of $P$. The fixed points are $0$ and $-s$, and neither lies on $|z|=|s|^r$, since $0<|s|<|s|^r$. The finite alternatives are therefore excluded.

Proposition [\[prop:contacts\]](#prop:contacts){reference-type="ref" reference="prop:contacts"} gives the finite, anchor-independent contact identity and its growing lower bound. Proposition [\[prop:compact-limit\]](#prop:compact-limit){reference-type="ref" reference="prop:compact-limit"} and its quadratic application give compactness, Hausdorff convergence, the entire weakly convergent measure sequence, and [\[eq:main-rate\]](#eq:main-rate){reference-type="eqref" reference="eq:main-rate"}. Propositions [\[prop:odometer\]](#prop:odometer){reference-type="ref" reference="prop:odometer"} and [\[prop:aperiodicity\]](#prop:aperiodicity){reference-type="ref" reference="prop:aperiodicity"} identify the limit system with $(\mathbb Z_p,+1)$ and its measure with nonatomic Haar probability. The support equals $\mathcal A$ by minimality. Its embedding in $\mathbb P^{1,\mathrm{an}}_K$ is compact and consists of classical points, so the Berkovich support is exactly that same type-I set.

The finite upper bound [\[eq:old-cycle-contact-bound\]](#eq:old-cycle-contact-bound){reference-type="eqref" reference="eq:old-cycle-contact-bound"} plays a different role from the growing lower bound for $c_d$. The latter makes high cycles uniformly close; the former keeps their limit away from each fixed old cycle. Growing approximating periods alone would not exclude a finite limit.

# Consequences and scope {#sec:scope}

The theorem describes two distinct compact invariant sets and their associated measures. Keeping them separate prevents a false unique-ergodicity assertion on a space containing finite cycles.

::: {#tab:objects}
  Object                                  Established structure                                                           Role of the estimate
  --------------------------------------- ------------------------------------------------------------------------------- ----------------------------------------------------------------------
  $C=\operatorname{cl}_K\bigcup_e\Pi_e$   Compact classical invariant set containing all old cycles                       Uniform high-level contacts give finite nets at every scale
  $\mathcal A=\lim_e\Pi_e$                Hausdorff limit, disjoint from every old cycle, conjugate to $\mathbb Z_p$      Lower contacts give convergence; the finite average gives separation
  $\mu_e$ and $\mu$                       Full-sequence convergence to the unique invariant probability on $\mathcal A$   Aligned orbit couplings give $W_\infty(\mu_d,\mu)\le|s|^{c_d}$

  : Exact implications for the containing closure, the limiting system, and the cycle measures. Unique ergodicity belongs to $\mathcal A$, not to $C$. All distances are classical absolute-value distances.
:::

For any real continuous function $\varphi$ on $C$, the proof also gives the explicit modulus-of-continuity estimate $$\left|\int\varphi\,d\mu_d-\int\varphi\,d\mu\right|
 \le \omega_\varphi\bigl(|s|^{c_d}\bigr).$$ In particular a Lipschitz test function of constant $L$ has error at most $L|s|^{c_d}$. The bound is for each fixed allowed multiplier; neither its optimality nor uniformity near the boundary $|s|=1$ is asserted.

The proof uses the source's optimal-cycle geometry, coprime Hensel factorization, derivative products, and the elementary characteristic-$p$ substitution identity. Its specific distribution step is the all-anchor contact average with a bound diverging in the anchor level. Compactness and the cyclic inverse-limit argument then identify the resulting measure. No Galois irreducibility, oriented character, or splitting-field nesting conclusion is needed or obtained here. The adding-machine conjugacy is topological, not an asserted analytic linearization.

The theorem does not address characteristic zero, characteristic two, all normalized germs, or counting all periodic points of a polynomial. The comparison with existing measure and ramification results is bounded to the specified sources and does not certify worldwide priority or the present status of every later or unpublished work. The assertion proved here is the positive answer to the explicitly identified version of the selected-cycle question.

#### Preparation and verification statement.

This anonymous manuscript was prepared with AI assistance. The underlying proof arguments received nonauthor review within the same research team; this is internal verification, not external peer review or journal acceptance. No numerical experiment is used as evidence for the theorem. All substantive contact, compactness, and aperiodicity arguments used in the article are included above.
