---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--107-annihilator-power-ideal-dynamics"
canonical_tex: "symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/main.pdf"
source_sha256: "7a2da5b6e0c05fd898bd17e3885b5eac89abdb5e8231b7b6fb5da697cefb419a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Annihilator--Power Dynamics on Ideals of Residue Rings: Resonant Fixed Points, Two-Cycles, and Exact Transients

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/107-annihilator-power-ideal-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $r\geq2$. On the ideal lattice of $\mathbb Z/N\mathbb Z$ we study $T_r(I)=\operatorname{Ann}(I)^r$. For a prime-power component $p^a$, the valuation coordinate is the clipped reflection $$f_{a,r}(e)=\min\{a,r(a-e)\},\qquad 0\leq e\leq a.$$ The endpoints form a two-cycle, while an interior fixed point exists exactly when $r+1$ divides $a$. Before clipping, the centered deviation $\Delta(e)=(r+1)e-ra$ is multiplied by $-r$ at every step. This gives an exact hitting-time formula, a closed transient cumulative distribution, and a sharp logarithmic maximum depth. Chinese remaindering then yields the complete recurrent set, all fixed and two-cycle counts, and the Artin--Mazur zeta function for arbitrary $N$. Literal ideal arithmetic for every $N\leq1000$ independently checks the valuation proof.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Annihilator--Power Dynamics on Ideals of Residue Rings: Resonant Fixed Points, Two-Cycles, and Exact Transients'
```

## Markdown 正文

# Map and ownership boundary

Let $N\geq2$, $R_N=\mathbb Z/N\mathbb Z$, and let $\mathcal I_N$ be its finite set of ideals. For a fixed integer $r\geq2$, define $$\label{eq:map}
 T_r\colon\mathcal I_N\longrightarrow\mathcal I_N,
 \qquad T_r(I)=\operatorname{Ann}_{R_N}(I)^r.$$ Ideal annihilators, ideal powers, and the Chinese remainder theorem are standard commutative-algebra ingredients; see @AtiyahMacdonald1969. Annihilating-ideal graphs and their residue-ring specializations are also an established topic [@BehboodiRakeei2011; @AfkhamiEtAl2016]. We assign these ingredients no novelty credit. More directly, Schwiebert treats the radical and annihilator as operators on the ideal poset, studies their generated monoid, and analyzes finite-product behavior [@Schwiebert2017]. That operator-dynamics viewpoint, the bare annihilator iteration, and its product-decomposition framework are owned background here. Our bounded target is only the temporal package for the specific power-after-annihilator self-map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}: the clipped-reflection normal form, the divisibility-controlled fixed-point anomaly, exact transient layers, and the full one/two-cycle census. A targeted search completed on 29 August 2026 did not locate that conjunction. This is not an exhaustive owner certificate; external circulation and every priority claim remain on **HOLD**.

Factor $N$ as $$\label{eq:factor}
 N=\prod_{i=1}^{s}p_i^{a_i}.$$ The Chinese remainder theorem identifies $\mathcal I_N$ with $\prod_i\{0,1,\ldots,a_i\}$: the coordinate $e_i$ denotes the ideal $(p_i^{e_i})$ in $\mathbb Z/p_i^{a_i}\mathbb Z$. The first proof route works entirely in these valuation coordinates. The control route instead represents an ideal of $R_N$ by its unique divisor generator $(d)$, computes $$\label{eq:literal}
 T_r((d))=\left(\gcd\!\left(N,(N/d)^r\right)\right),$$ and only then compares with the coordinate formulas.

# Prime-power normal form

Fix $a\geq1$ and abbreviate $f=f_{a,r}$. Since $\operatorname{Ann}((p^e))=(p^{a-e})$ and $(p^b)^r=(p^{\min(a,rb)})$, we have the following exact model.

[\[prop:normal\]]{#prop:normal label="prop:normal"} On $\mathcal I_{p^a}$, the map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is conjugate to $$\label{eq:f}
 f(e)=\min\{a,r(a-e)\},\qquad 0\leq e\leq a.$$ Put $\Delta(e)=(r+1)e-ra$. Whenever $f(e)<a$, $$\label{eq:deviation}
 \Delta(f(e))=-r\Delta(e).$$ Clipping occurs precisely when $\Delta(e)\leq-a/r$.

Only the deviation statements require verification. In the unclipped branch $f(e)=r(a-e)$, whence $$(r+1)f(e)-ra
 =r\bigl((r+1)(a-e)-a\bigr)=-r\Delta(e).$$ The inequality $r(a-e)\geq a$ is equivalent to $(r+1)e-ra\leq-a/r$.

The endpoints satisfy $0\leftrightarrow a$. An interior point is fixed if and only if $e=r(a-e)$, which already exposes the arithmetic anomaly.

[\[thm:recurrent-coordinate\]]{#thm:recurrent-coordinate label="thm:recurrent-coordinate"} The recurrent set of $f_{a,r}$ is $$\label{eq:rec-coordinate}
 \{0,a\}\ \cup\
 \left\{\frac{ra}{r+1}:\ (r+1)\mid a\right\}.$$ The endpoints form one two-cycle. The displayed interior state, when it exists, is fixed. There are no other cycles.

The endpoint statements and the fixed-point equation follow from [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"}. Suppose $\Delta(e)\neq0$ and the orbit has not clipped. By [\[eq:deviation\]](#eq:deviation){reference-type="eqref" reference="eq:deviation"}, its deviation alternates sign and its absolute value is multiplied by $r>1$. It therefore eventually enters the clipping region. The next state is $a$, hence belongs to the endpoint two-cycle. Thus every nonfixed interior state is transient.

# Exact transient layers

For a state $e$, let $\operatorname{depth}(e)$ be the first time its orbit is recurrent. The deviation gives a closed hitting-time clock rather than only an upper bound.

[\[thm:depth-coordinate\]]{#thm:depth-coordinate label="thm:depth-coordinate"} For $e$ in [\[eq:rec-coordinate\]](#eq:rec-coordinate){reference-type="eqref" reference="eq:rec-coordinate"}, $\operatorname{depth}(e)=0$. For every other state, put $D=\Delta(e)$. If $D<0$, let $$k_- =\min\{k\geq0:r^{2k+1}|D|\geq a\};$$ if $D>0$, let $$k_+ =\min\{k\geq0:r^{2k+2}D\geq a\}.$$ Then $$\label{eq:depth-coordinate}
 \operatorname{depth}(e)=
 \begin{cases}
  2k_-+1,&D<0,\\
  2k_++2,&D>0.
 \end{cases}$$ Consequently, on each sign side that contains transient states, the largest depth occurs at the smallest available value of $|D|$. The global maximum is the larger of those sidewise values, or zero when there are no transient states. In particular it is $O(\log_r a)$, and [\[eq:depth-coordinate\]](#eq:depth-coordinate){reference-type="eqref" reference="eq:depth-coordinate"} is a sharp formula for every $(a,r)$, including $a=1$.

Before clipping, the deviation at time $j$ is $(-r)^jD$. A negative deviation clips on the following update exactly when its magnitude times $r$ is at least $a$. If $D<0$, negative signs occur at times $2k$; if $D>0$, they occur at times $2k+1$. The two displayed threshold conditions and the additional clipping update give [\[eq:depth-coordinate\]](#eq:depth-coordinate){reference-type="eqref" reference="eq:depth-coordinate"}. Monotonicity in $|D|$ proves the sharp maximum statement.

For completeness, the whole transient distribution also has a floor/ceiling form. Put $\varepsilon_{a,r}=\mathbf1_{(r+1)\mid a}$ and, for $L\geq1$, $$\begin{aligned}
 M_-(L)&=\max\left\{0,
  \min\left(a-1,\left\lfloor\frac{ra-L}{r+1}\right\rfloor\right)\right\},
 \label{eq:Mminus}\\
 M_+(L)&=\max\left\{0,
  a-\max\left(1,\left\lceil\frac{ra+L}{r+1}\right\rceil\right)\right\}.
 \label{eq:Mplus}\end{aligned}$$ These count interior states with $\Delta\leq-L$ and $\Delta\geq L$, respectively.

[\[cor:cdf\]]{#cor:cdf label="cor:cdf"} Let $C_{a,r}(t)=\#\{e:\operatorname{depth}(e)\leq t\}$. Then $C_{a,r}(0)=2+\varepsilon_{a,r}$. For $t\geq1$, set $$j_-(t)=2\left\lfloor\frac{t-1}{2}\right\rfloor,
 \qquad L_-(t)=\left\lceil\frac{a}{r^{j_-(t)+1}}\right\rceil.$$ For $t\geq2$, also set $$j_+(t)=2\left\lfloor\frac{t-2}{2}\right\rfloor+1,
 \qquad L_+(t)=\left\lceil\frac{a}{r^{j_+(t)+1}}\right\rceil.$$ Then $$\label{eq:cdf}
 C_{a,r}(t)=2+\varepsilon_{a,r}+M_-(L_-(t))
 +\mathbf1_{t\geq2}M_+(L_+(t)).$$ Thus the exact depth-$t$ shell is $C_{a,r}(t)-C_{a,r}(t-1)$.

Among negative starting deviations, the largest even exponent available by time $t-1$ is $j_-(t)$; among positive ones, the largest admissible odd exponent is $j_+(t)$, which exists only for $t\geq2$. The clipping test in [\[prop:normal\]](#prop:normal){reference-type="ref" reference="prop:normal"} becomes $|D|\geq L_-(t)$ or $D\geq L_+(t)$. Counting the arithmetic progression $D=(r+1)e-ra$ over $1\leq e\leq a-1$ gives [\[eq:Mminus\]](#eq:Mminus){reference-type="eqref" reference="eq:Mminus"}--[\[eq:Mplus\]](#eq:Mplus){reference-type="eqref" reference="eq:Mplus"}. The endpoints and possible resonant fixed point contribute $2+\varepsilon_{a,r}$.

# Chinese products, cycles, and zeta

Return to [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} and put $$\label{eq:AB}
 A=\prod_{i=1}^{s}\varepsilon_{a_i,r},
 \qquad B=\prod_{i=1}^{s}(2+\varepsilon_{a_i,r}).$$

[\[thm:global\]]{#thm:global label="thm:global"} Under Chinese remaindering, $T_r$ is the product of the maps $f_{a_i,r}$. Its recurrent set has size $B$, its maximum transient depth is $$\label{eq:global-depth}
 \max_{1\leq i\leq s}\ \max_{0\leq e\leq a_i}\operatorname{depth}_{a_i,r}(e),$$ and the number of states of depth at most $t$ is $$\label{eq:global-cdf}
 \prod_{i=1}^{s}C_{a_i,r}(t).$$ For every $k\geq1$, $$\label{eq:fixed-global}
 \#\operatorname{Fix}(T_r^k)=
 \begin{cases}
  A,&k\text{ odd},\\
  B,&k\text{ even}.
 \end{cases}$$ Hence there are $A$ fixed points and $(B-A)/2$ two-cycles, and the Artin--Mazur zeta function [@ArtinMazur1965] is $$\label{eq:zeta}
 \zeta_{T_r}(z)=(1-z)^{-A}(1-z^2)^{-(B-A)/2}.$$ No period greater than two occurs.

Annihilators, products, and powers commute with the finite product decomposition of $R_N$, giving the coordinate product. A product point is recurrent exactly when each coordinate is recurrent; every such coordinate has period one or two, so the product period also divides two. Depth is the maximum coordinate depth, proving [\[eq:global-depth\]](#eq:global-depth){reference-type="eqref" reference="eq:global-depth"}, while independent coordinate choices give [\[eq:global-cdf\]](#eq:global-cdf){reference-type="eqref" reference="eq:global-cdf"}. An odd iterate fixes only the resonant fixed coordinate in every component, producing $A$. An even iterate fixes every recurrent coordinate, producing $B$. Subtracting the fixed points from the points fixed by the square and dividing by two gives the cycle counts and [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The dynamics depends on the prime exponents and not on the primes themselves: moduli with the same exponent multiset have conjugate systems. This is a nonrigidity statement, not a claim that the phase portrait always recovers that multiset.

The internal collision boundary is also explicit. P100 uses least-valuation digit erasure on residue classes and reconstructs prime data from a transient profile; it does not act on the ideal lattice or alternate an annihilator with an ideal power. P102 uses an involution--norm map in a cyclic group algebra; its orbit structure comes from polynomial factorization rather than the clipped expanding reflection [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"}. Shared valuation, CRT, and zeta bookkeeping receive no contribution credit.

# Independent exact control

The accompanying standard-library verifier implements two independent lanes. The first enumerates $e=0,\ldots,a$, checks the deviation clock, the cumulative formula, and all iterate-fixed counts. The second enumerates actual divisor ideals $(d)$ for every $N\leq1000$, applies the literal gcd rule [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}, and compares trajectories, depths, recurrent sets, and fixed counts with the CRT prediction. These finite computations are falsification controls, not proofs of the quantified theorems.

# Conclusion

Annihilation followed by an ideal power becomes a clipped expanding reflection on each prime exponent. Its sign alternation forces a universal two-cycle, while the single equation $(r+1)e=ra$ creates a sharp divisibility resonance. The same normal form supplies every transient layer and, after Chinese remaindering, the complete cycle and zeta data. Specialist owner review remains necessary before any external use.
