---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-397-odd-lag-half-span-overlap-mobius-capacity"
canonical_tex: "zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/main.pdf"
source_sha256: "a0ded93cfcd46f48b602e3f276a39e01e99ba8c37d3961316540f3925064ec11"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Lag Half-Span Overlap Möbius Capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a lag $h\geq1$. A phase table reads the centered triple $\mu_0(n-h),\mu(n),\mu(n+h)$, and half-span overlap safety forbids two positive outputs at separation $h$ whenever their two shared symbols agree. We determine the exact terminal-log capacity for every finite declared phase clock. The complete three-shift table law first reduces the analytic limit to nonnegative exact-support cell densities. A positive projection then turns universal four-symbol safety into the single binary obstruction $t_rs_{r+h}=0$ on source and target flags. Every flag class saturates to a rectangle. Its value has four terms, and a collision-aware translation identity telescopes the phase costs. The remaining bonus is precisely a maximum-weight independent set on the step-$h$ phase graph: $$C^{\mathrm{hs}}_h(q)=K_1-\frac{\kappa_2(h)}2+
   \frac14\max_{J\cap(J+h)=\varnothing}
   \sum_{r\in J}\Theta_{h,q,r}(LCR).$$ For every fixed odd $h$, the maximum over all finite declared clocks is attained, equals $K_1-\kappa_2(h)/2+\kappa_3(h)/4$, and is attained exactly when the declared clock $q$ is even. The word "declared" is essential: minimal period is not required. The fourth safety symbol is used only in a finite compatibility predicate; no four-shift analytic correlation enters the proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 12, 2026'
title: 'Odd-Lag Half-Span Overlap Möbius Capacity'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; centered local rule; overlap safety; phase clock; weighted independent set; exact attainment.

# Definitions and principal results

Write $\mu_0(k)=\mu(k)$ for integers $k\geq1$, and $\mu_0(k)=0$ for $k\leq0$. A *terminal clock* is a function $$1\leq\omega(X)\leq X,
 \qquad \omega(X)\longrightarrow\infty.
 \label{eq:terminal-clock}$$ Fix integers $h,q\geq1$, fix one table $$F_r:\{-1,0,+1\}^3\longrightarrow\{-1,+1\}
 \qquad(r\in\mathbb Z/q\mathbb Z),$$ and fix the clock $\omega$, all before $X\to\infty$. The visible input order and the scored output are $$\begin{aligned}
 \varepsilon_F(n)
 &=F_{n\bmod q}\bigl(\mu_0(n-h),\mu(n),\mu(n+h)\bigr),
 \label{eq:centered-output}\\
 L_{h,q,X}(F;\omega)
 &=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}
 \frac{\mu(n)\varepsilon_F(n)}n.
 \label{eq:terminal-functional}\end{aligned}$$ The table value $\varepsilon_F(n)$ is the output; multiplication by the center $\mu(n)$ produces the score.

The family is *universally half-span safe* when $$\neg\bigl(F_r(x,z,y)=+1\ \text{and}\
 F_{r+h}(z,y,w)=+1\bigr)
 \label{eq:half-span-safety}$$ for every $r\in\mathbb Z/q\mathbb Z$ and every $x,z,y,w\in\{-1,0,+1\}$, with phases read modulo $q$. Both symbols $z,y$ are shared: $$\begin{array}{c@{\quad}c@{\quad}c}
 x & z\ (\text{center}) & y\\[-2pt]
   & \multicolumn{2}{c}{\underbrace{\hspace{4.6em}}_{\text{overlap}}}\\[-2pt]
   & z & y\ (\text{center})\quad w .
\end{array}$$ The second center is the first right symbol, so the separation is $h$, not $2h$.

The analytic density notation follows the ordered shifts $$a_L=h,\qquad a_C=0,\qquad a_R=-h.
 \label{eq:coordinate-shifts}$$ For $S\subseteq\{L,C,R\}$, deduplicate modulo $p^2$ before any count and set $$B_{p,S}=\{a_i\bmod p^2:i\in S\},\qquad
 \nu_{p,S}=|B_{p,S}|,
 \qquad
 \tau_{p,S}(r)=\#\{b\in B_{p,S}:b\equiv r\pmod p\}.
 \label{eq:local-data}$$ Define $$\begin{aligned}
 \Theta_{h,q,r}(S)
 &=\frac1q
 \prod_{p\nmid q}\left(1-\frac{\nu_{p,S}}{p^2}\right)
 \prod_{p\parallel q}\left(1-\frac{\tau_{p,S}(r)}p\right)
 \prod_{p^2\mid q}\mathbf 1_{\{r\bmod p^2\notin B_{p,S}\}},
 \label{eq:phase-density}\\
 \kappa_h(S)
 &=\prod_p\left(1-\frac{\nu_{p,S}}{p^2}\right).
 \label{eq:kappa-density}\end{aligned}$$ Then $\Theta_{h,q,r}(\varnothing)=1/q$ and $$\sum_{r\bmod q}\Theta_{h,q,r}(S)=\kappa_h(S).
 \label{eq:phase-sum}$$ We shall use $$K_1=\prod_p(1-p^{-2})=\frac6{\pi^2},\qquad
 \kappa_2(h)=\kappa_h(LC)=\kappa_h(CR),\qquad
 \kappa_3(h)=\kappa_h(LCR).
 \label{eq:kappa23}$$ These are collision-aware products. They must not be replaced unconditionally by the collision-free products $\prod_p(1-2p^{-2})$ and $\prod_p(1-3p^{-2})$.

The fixed-table limit below exists for every admissible clock and is clock-independent; write it as $L_{h,q}(F)$. The half-span capacity is formed only afterward: $$C^{\mathrm{hs}}_h(q)=
 \max_{F\ \mathrm{universally\ half\text{-}span\ safe}}
 |L_{h,q}(F)|.
 \label{eq:half-span-capacity}$$

[\[thm:fixed-clock-half-span\]]{#thm:fixed-clock-half-span label="thm:fixed-clock-half-span"} For every fixed integer $h\geq1$, every finite integer $q\geq1$, every phase family $F$, and every terminal clock [\[eq:terminal-clock\]](#eq:terminal-clock){reference-type="eqref" reference="eq:terminal-clock"}, the limit $$L_{h,q}(F)=\lim_{X\to\infty}L_{h,q,X}(F;\omega)$$ exists and has the same value for all such $\omega$. Moreover, $$\boxed{
 C^{\mathrm{hs}}_h(q)=K_1-\frac{\kappa_2(h)}2
 +\frac14
 \max_{\substack{J\subseteq\mathbb Z/q\mathbb Z\\J\cap(J+h)=\varnothing}}
 \sum_{r\in J}\Theta_{h,q,r}(LCR).}
 \label{eq:fixed-clock-formula}$$ The maximum is a weighted step-$h$ independent-set problem. If $q\mid h$, every vertex has a self-loop and only $J=\varnothing$ is admissible. Both signs of every nonzero optimal value are attained by safe tables.

[\[thm:odd-lag-clock-maximum\]]{#thm:odd-lag-clock-maximum label="thm:odd-lag-clock-maximum"} For every fixed odd integer $h\geq1$, $$\boxed{
 \max_{q\geq1}C^{\mathrm{hs}}_h(q)=C^{\mathrm{hs}}_h(2)
 =K_1-\frac{\kappa_2(h)}2+\frac{\kappa_3(h)}4.}
 \label{eq:odd-clock-maximum}$$ For a declared finite clock $q$, equality with the right side holds if and only if $q$ is even: $$C^{\mathrm{hs}}_h(q)=K_1-\frac{\kappa_2(h)}2+\frac{\kappa_3(h)}4
 \quad\Longleftrightarrow\quad 2\mid q.
 \label{eq:attainment-parity}$$ The declared period need not be the minimal period of an optimizing table. Every odd $q$, including $q=1$, is strictly suboptimal.

Theorem [\[thm:fixed-clock-half-span\]](#thm:fixed-clock-half-span){reference-type="ref" reference="thm:fixed-clock-half-span"} holds for even and odd $h$. Parity enters only in Theorem [\[thm:odd-lag-clock-maximum\]](#thm:odd-lag-clock-maximum){reference-type="ref" reference="thm:odd-lag-clock-maximum"}; no all-clock classification for even $h$ is asserted.

The first input to the proof is analytic: the complete fixed three-shift terminal table law. Everything after that input is finite. The new finite geometry differs from the distance-$2h$ relation geometry of RH-396: two adjacent radius-$h$ windows now share two symbols, and this overlap collapses an arbitrary ternary relation to two Boolean flags. The collapse, the exact rectangle value, and the odd-clock attainment classification are the new steps of this paper.

# The fixed three-shift bridge and its boundary

Let $I=\{L,C,R\}$. Inclusion--exclusion turns the phase masses into exact-support masses $$\Pi_{h,q,r}(U)=
 \sum_{W\subseteq I\setminus U}(-1)^{|W|}
 \Theta_{h,q,r}(U\cup W),
 \qquad U\subseteq I.
 \label{eq:pi-definition}$$ For a table $G_r:\{-1,0,+1\}^3\to\mathbb R$, write $$\overline G_{r,U}=2^{-|U|}
 \sum_{\sigma\in\{-1,+1\}^{U}}
 G_r(\sigma_U,0_{I\setminus U}).
 \label{eq:stratum-average}$$ The RH-394 compiler gives, for every fixed phase family and every terminal clock, $$\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}
 \frac{G_{n\bmod q}
 (\mu_0(n-h),\mu(n),\mu(n+h))}{n}
 \longrightarrow
 \sum_{r\bmod q}\sum_{U\subseteq I}
 \Pi_{h,q,r}(U)\overline G_{r,U}.
 \label{eq:three-shift-bridge}$$ Moreover, $$\Pi_{h,q,r}(U)\geq0,\qquad
 \sum_{U\subseteq I}\Pi_{h,q,r}(U)=\frac1q.
 \label{eq:pi-mass}$$ These statements are Theorem 1.1, equations (8)--(9), Theorem 1.2, equations (11)--(14), and Corollary 1.3, equation (15), of the frozen RH-394 release, on printed and PDF pages 2--3 [@RH394]. They also give [\[eq:phase-density\]](#eq:phase-density){reference-type="eqref" reference="eq:phase-density"}--[\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"}. The result is qualitative and fixed-data; it supplies no rate uniform in $h$ or $q$.

For our score use the single table $$H_r(x,z,y)=zF_r(x,z,y).
 \label{eq:score-table}$$ Then [\[eq:three-shift-bridge\]](#eq:three-shift-bridge){reference-type="eqref" reference="eq:three-shift-bridge"} is exactly the limit in [\[eq:terminal-functional\]](#eq:terminal-functional){reference-type="eqref" reference="eq:terminal-functional"}.

[\[lem:three-shift-firewall\]]{#lem:three-shift-firewall label="lem:three-shift-firewall"} The safety condition [\[eq:half-span-safety\]](#eq:half-span-safety){reference-type="eqref" reference="eq:half-span-safety"} does not require a four-shift table law or the four-odd coefficient $c_{1111}$.

For each fixed $F$, the averaged summand is the one three-variable table $H_{n\bmod q}(\mu_0(n-h),\mu(n),\mu(n+h))$. The letter $w$ appears only when the finite set of phase tables is tested for universal safety, before any average is formed. The safe family is finite, so we first take the limit of each fixed table and only then maximize those existing limits. We never average a product of two outputs, form a four-variable table, or exchange a maximum with the limit. Thus the sole missing four-shift channel identified in RH-394 is untouched.

RH-396 supplies useful finite precedents for positive projection, input reflection, collision-aware phase densities, and literal repetition of a declared phase table [@RH396]. Its safety step is $2h$, however, and its optimizer is a full relation-composition problem. It does not imply the step-$h$ flag collapse proved below.

# Positive projection, exact cells, and reflection

For $x,y\in\{-1,0,+1\}$, set $$\begin{aligned}
 S(x,y)&=\{C\}\cup(\{L\}:x\ne0)\cup(\{R\}:y\ne0),
 \label{eq:cell-support}\\
 \lambda_{h,q,r}(x,y)
 &=2^{-\mathbf 1_{\{x\ne0\}}-\mathbf 1_{\{y\ne0\}}}
 \Pi_{h,q,r}(S(x,y)).
 \label{eq:lambda}\end{aligned}$$ By [\[eq:pi-mass\]](#eq:pi-mass){reference-type="eqref" reference="eq:pi-mass"}, every $\lambda_{h,q,r}(x,y)$ is nonnegative. It is an event density; no claim is made that its coordinates in a signed Euler-product basis are nonnegative.

[\[lem:positive-projection\]]{#lem:positive-projection label="lem:positive-projection"} Given a safe family $F$, replace every $+1$ output at a cell whose center $z$ is not $+1$ by $-1$, leaving all other cells unchanged. Call the result $F^+$. Then $F^+$ is safe and $L_{h,q}(F^+)\geq L_{h,q}(F)$. If $$A_r=\{(x,y)\in\{-1,0,+1\}^2:F^+_r(x,+1,y)=+1\},
 \label{eq:positive-relation}$$ then $$L_{h,q}(F^+)=
 \sum_{r\bmod q}\sum_{(x,y)\in A_r}
 \lambda_{h,q,r}(x,y).
 \label{eq:projected-cell-sum}$$

At $z=-1$, changing the output from plus to minus changes the score $zF$ from $-1$ to $+1$; at $z=0$, the score stays zero. Deleting positive outputs cannot create a forbidden pair, so the comparison is pointwise and safety is preserved.

Start from the all-minus table, whose score is $-z$. Its average on every exact-support sign stratum is zero. Flipping the center-$+1$ cell $(x,+1,y)$ changes the score by two. The density of that specified sign cell is $$2^{-1-\mathbf 1_{\{x\ne0\}}-\mathbf 1_{\{y\ne0\}}}
 \Pi_{h,q,r}(S(x,y)).$$ The factor two cancels the center-sign half and gives exactly [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"}. Summing the flipped cells proves [\[eq:projected-cell-sum\]](#eq:projected-cell-sum){reference-type="eqref" reference="eq:projected-cell-sum"}.

[\[lem:input-reflection\]]{#lem:input-reflection label="lem:input-reflection"} Define $$F^\rho_r(x,z,y)=F_r(-x,-z,-y).$$ This map preserves universal half-span safety and satisfies $$L_{h,q}(F^\rho)=-L_{h,q}(F).
 \label{eq:reflection-sign}$$

Simultaneous negation is a bijection of the four-letter words in [\[eq:half-span-safety\]](#eq:half-span-safety){reference-type="eqref" reference="eq:half-span-safety"}. For the scored table, $$zF^\rho_r(x,z,y)=-H_r(-x,-z,-y).$$ Every exact-support stratum in [\[eq:three-shift-bridge\]](#eq:three-shift-bridge){reference-type="eqref" reference="eq:three-shift-bridge"} is invariant under simultaneous sign negation, so its uniform average changes sign. This proves [\[eq:reflection-sign\]](#eq:reflection-sign){reference-type="eqref" reference="eq:reflection-sign"}. Consequently the positive maximum equals the absolute capacity and both signs are attained whenever the value is nonzero.

# The overlap flags and their exact rectangles

For a relation $A\subseteq\{-1,0,+1\}^2$, define $$\operatorname{Source}(A)=\{x:(x,y)\in A\text{ for some }y\},\qquad
 \operatorname{Target}(A)=\{y:(x,y)\in A\text{ for some }x\}.$$ For the relation [\[eq:positive-relation\]](#eq:positive-relation){reference-type="eqref" reference="eq:positive-relation"}, put $$s_r=\mathbf 1_{\{+1\in\operatorname{Source}(A_r)\}},\qquad
 t_r=\mathbf 1_{\{+1\in\operatorname{Target}(A_r)\}}.
 \label{eq:source-target-flags}$$

[\[lem:flag-obstruction\]]{#lem:flag-obstruction label="lem:flag-obstruction"} The projected family is safe if and only if $$t_rs_{r+h}=0\qquad(r\bmod q).
 \label{eq:flag-safety}$$

If $t_r=s_{r+h}=1$, choose $(x,+1)\in A_r$ and $(+1,w)\in A_{r+h}$. The concrete word $(x,+1,+1,w)$ violates [\[eq:half-span-safety\]](#eq:half-span-safety){reference-type="eqref" reference="eq:half-span-safety"}. Conversely, every forbidden projected pair has precisely these two relation cells, so it forces the two flags to be one.

There are $2^9=512$ ternary relations. A source-zero relation omits the three cells with first coordinate $+1$, so there are $2^6=64$; the same count holds for target zero, and their intersection has $2^4=16$ members. Thus the four flag classes have counts $16,48,48,400$ in the order $00,10,01,11$. Of all $512^2=262144$ ordered relation pairs, exactly $448^2=200704$ violate [\[eq:flag-safety\]](#eq:flag-safety){reference-type="eqref" reference="eq:flag-safety"}; hence $61440$ are safe.

Set $$X_0=Y_0=\{-1,0,+1\}\setminus\{+1\},\qquad X_1=Y_1=\{-1,0,+1\},
 \qquad \mathcal R(s,t)=X_s\times Y_t.$$ The four rectangles are summarized below.

   flags $(s,t)$      rectangle      size
  --------------- ----------------- ------
       $00$        $X_0\times Y_0$    4
       $10$        $X_1\times Y_0$    6
       $01$        $X_0\times Y_1$    6
       $11$        $X_1\times Y_1$    9

[\[tab:flag-rectangles\]]{#tab:flag-rectangles label="tab:flag-rectangles"}

[\[lem:flag-rectangle-saturation\]]{#lem:flag-rectangle-saturation label="lem:flag-rectangle-saturation"} Every relation with flags $(s,t)$ is contained in $\mathcal R(s,t)$, and that rectangle has exactly the same flags. Replacing each $A_r$ by its flag rectangle preserves safety and weakly increases [\[eq:projected-cell-sum\]](#eq:projected-cell-sum){reference-type="eqref" reference="eq:projected-cell-sum"}.

If $s=0$, no cell has first coordinate $+1$; if $t=0$, no cell has second coordinate $+1$. This proves containment. Each of the four rectangles is nonempty and visibly has the stated flags. Lemma [\[lem:flag-obstruction\]](#lem:flag-obstruction){reference-type="ref" reference="lem:flag-obstruction"} depends only on those flags, while every newly added cell has nonnegative weight $\lambda$.

# Rectangle weights and collision-aware translation

For each phase abbreviate $$M_r=\Theta_{h,q,r}(C),\quad
 U_r=\frac12\Theta_{h,q,r}(LC),\quad
 V_r=\frac12\Theta_{h,q,r}(CR),\quad
 W_r=\frac14\Theta_{h,q,r}(LCR).
 \label{eq:MUVW}$$ Row--column inclusion--exclusion gives the rectangle value $$R_r(s,t)=M_r-(1-s)U_r-(1-t)V_r+(1-s)(1-t)W_r.
 \label{eq:rectangle-value}$$ In particular the corner sign is plus. Event containment gives $$0\leq W_r\leq\frac{U_r}{2},\qquad
 0\leq W_r\leq\frac{V_r}{2}.
 \label{eq:weight-bounds}$$

[\[lem:phase-translation\]]{#lem:phase-translation label="lem:phase-translation"} For every fixed $h,q,r$, including every collision branch, $$V_r=U_{r+h}.
 \label{eq:phase-translation}$$ Moreover, $$\sum_rM_r=K_1,\qquad
 \sum_rU_r=\sum_rV_r=\frac{\kappa_2(h)}2,\qquad
 \sum_rW_r=\frac{\kappa_3(h)}4.
 \label{eq:phase-weight-sums}$$

The residue sets for $CR$ and $LC$ are respectively $\{0,-h\}$ and $\{h,0\}$, after deduplication modulo $p^2$. Translation by $h$ carries the first set to the second. If $p\nmid q$, their $\nu$-counts agree. If $p\parallel q$, deduplication is performed modulo $p^2$ before reduction modulo $p$, and $\tau_{p,CR}(r)=\tau_{p,LC}(r+h)$. If $p^2\mid q$, the indicators $\mathbf 1_{\{r\notin B_{p,CR}\}}$ and $\mathbf 1_{\{r+h\notin B_{p,LC}\}}$ agree. All local factors and the common $1/q$ therefore agree, proving [\[eq:phase-translation\]](#eq:phase-translation){reference-type="eqref" reference="eq:phase-translation"}. The sums follow from [\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"} and [\[eq:MUVW\]](#eq:MUVW){reference-type="eqref" reference="eq:MUVW"}.

# Edge filling and the rising-set optimizer

By Lemma [\[lem:flag-obstruction\]](#lem:flag-obstruction){reference-type="ref" reference="lem:flag-obstruction"}, the flag constraint is $$t_r+s_{r+h}\leq1.
 \label{eq:binary-edge-safety}$$ Suppose an edge is unsaturated: $(t_r,s_{r+h})=(0,0)$. Change only $s_{r+h}$ to one. No other safety edge uses that source flag, and the gain at phase $r+h$ is exactly $$\Delta=U_{r+h}-(1-t_{r+h})W_{r+h}
 \geq U_{r+h}-W_{r+h}\geq0.
 \label{eq:edge-gain}$$ Repeated filling terminates with $$t_r=1-s_{r+h}\qquad(r\bmod q).
 \label{eq:edge-saturation}$$ The gain need not be strict.

Substitute [\[eq:edge-saturation\]](#eq:edge-saturation){reference-type="eqref" reference="eq:edge-saturation"} in [\[eq:rectangle-value\]](#eq:rectangle-value){reference-type="eqref" reference="eq:rectangle-value"} and use [\[eq:phase-translation\]](#eq:phase-translation){reference-type="eqref" reference="eq:phase-translation"}. The two linear costs telescope: $$-\sum_r(1-s_r)U_r-\sum_rs_{r+h}V_r=-\sum_rU_r.$$ The surviving corner bonus is $$\sum_r(1-s_r)s_{r+h}W_r.
 \label{eq:rising-bonus}$$ Define the rising set $$J=\{r:s_r=0,\ s_{r+h}=1\}.
 \label{eq:rising-set}$$ Then $J\cap(J+h)=\varnothing$, including when addition by $h$ is a self-loop.

[\[lem:rising-set-realization\]]{#lem:rising-set-realization label="lem:rising-set-realization"} For every $J\subseteq\mathbb Z/q\mathbb Z$ satisfying $J\cap(J+h)=\varnothing$, there is a saturated flag profile whose rising set is exactly $J$. The empty set and self-loop clocks are included.

Define $s_{r+h}=\mathbf 1_{\{r\in J\}}$, equivalently $s_u=\mathbf 1_{\{u-h\in J\}}$, and put $t_r=1-s_{r+h}$. If $r\in J$, independence implies $r-h\notin J$; hence $(1-s_r)s_{r+h}=1$. If $r\notin J$, that product is zero. Thus the rising set is exactly $J$, and the saturated rectangles realize it. When addition by $h$ is a self-loop, independence forces $J$ empty.

Combining [\[eq:phase-weight-sums\]](#eq:phase-weight-sums){reference-type="eqref" reference="eq:phase-weight-sums"}, [\[eq:rising-bonus\]](#eq:rising-bonus){reference-type="eqref" reference="eq:rising-bonus"}, and Lemma [\[lem:rising-set-realization\]](#lem:rising-set-realization){reference-type="ref" reference="lem:rising-set-realization"} gives $$K_1-\frac{\kappa_2(h)}2+\max_J\sum_{r\in J}W_r,$$ which is exactly [\[eq:fixed-clock-formula\]](#eq:fixed-clock-formula){reference-type="eqref" reference="eq:fixed-clock-formula"}. The fixed-table limits come from [\[eq:three-shift-bridge\]](#eq:three-shift-bridge){reference-type="eqref" reference="eq:three-shift-bridge"}, while Lemma [\[lem:input-reflection\]](#lem:input-reflection){reference-type="ref" reference="lem:input-reflection"} turns the positive maximum into the absolute capacity and supplies both signs. This proves Theorem [\[thm:fixed-clock-half-span\]](#thm:fixed-clock-half-span){reference-type="ref" reference="thm:fixed-clock-half-span"}.

# Odd lags: exact finite-clock attainment

Since $W_r\geq0$, every independent-set bonus is at most $$\sum_rW_r=\frac{\kappa_3(h)}4.
 \label{eq:odd-upper-bound}$$

[\[lem:q-two-attainment\]]{#lem:q-two-attainment label="lem:q-two-attainment"} If $h$ is odd, clock $q=2$ attains [\[eq:odd-upper-bound\]](#eq:odd-upper-bound){reference-type="eqref" reference="eq:odd-upper-bound"}.

Modulo four, $B_{2,LCR}=\{h,0,-h\}=\{1,0,3\}$. In the $2\parallel q$ branch, $\tau$ is one on the even phase and two on the odd phase. The odd triple mass is therefore zero, while the even phase carries the entire phase sum $\kappa_3(h)$. The singleton even phase is step-$h$ independent, so it captures all weight.

If $q$ is any declared even clock, literally repeat the two-phase optimizing table modulo $q$. Because odd $h$ reverses parity, the same safety pattern holds and the output word, hence the terminal value, is unchanged. No minimal-period hypothesis is imposed.

[\[lem:odd-clock-strictness\]]{#lem:odd-clock-strictness label="lem:odd-clock-strictness"} For fixed odd $h$ and odd $q$, there is a phase $r$ for which both $\Theta_{h,q,r}(LCR)$ and $\Theta_{h,q,r+h}(LCR)$ are positive. Consequently the bound [\[eq:odd-upper-bound\]](#eq:odd-upper-bound){reference-type="eqref" reference="eq:odd-upper-bound"} is strict.

We choose $r$ locally at each prime power dividing $q$. If $p\parallel q$ and $p\geq5$, every $\tau$-count is at most three, so both local factors are positive for every class. For $p=3$, there are exactly three cases after deduplication modulo nine. If $3\nmid h$, the three residues occupy the three classes modulo three and each $\tau$-count is one. If $3\mid h$ but $9\nmid h$, the set is $\{0,3,6\}$ modulo nine; choose either nonzero class modulo three, which is preserved by adding $h$. If $9\mid h$, the residue set deduplicates to $\{0\}$, so every $\tau$-count is at most one.

If $p^2\mid q$, choose $r\bmod p^2$ outside $$B_{p,LCR}\cup(B_{p,LCR}-h)=\{h,0,-h,-2h\}.
 \label{eq:four-class-avoidance}$$ There are at most four forbidden classes and $p^2\geq9$, since $q$ is odd. Lift the choice to the full power of $p$ in $q$. The Chinese remainder theorem combines all choices.

For primes outside $q$, every Euler factor is positive: for odd primes, $\nu\leq3<p^2$; at $p=2$, odd $h$ gives exactly three distinct classes modulo four. Thus both adjacent weights are positive. A step- $h$ independent set cannot contain both; if they are the same vertex, the self-loop excludes it. Hence at least one positive weight is omitted, and the upper bound is strict.

Lemma [\[lem:q-two-attainment\]](#lem:q-two-attainment){reference-type="ref" reference="lem:q-two-attainment"}, literal even-clock repetition, and Lemma [\[lem:odd-clock-strictness\]](#lem:odd-clock-strictness){reference-type="ref" reference="lem:odd-clock-strictness"} prove both [\[eq:odd-clock-maximum\]](#eq:odd-clock-maximum){reference-type="eqref" reference="eq:odd-clock-maximum"} and [\[eq:attainment-parity\]](#eq:attainment-parity){reference-type="eqref" reference="eq:attainment-parity"}, hence Theorem [\[thm:odd-lag-clock-maximum\]](#thm:odd-lag-clock-maximum){reference-type="ref" reference="thm:odd-lag-clock-maximum"}.

# Exact finite reproduction

The executable certificate reproduces finite identities and attacks implementation drift; it is not an analytic proof. Its 72 rows are divided as follows: 10 domain/source rows, 10 terminal-bridge/projection/reflection rows, 12 flag/rectangle rows, 12 weight/translation rows, 12 saturation and rising-set rows, 12 odd-clock rows, and 4 claim-firewall rows. Dynamic checks enumerate all 512 relations and all 262144 ordered pairs, recover the 61440 safe pairs, verify all four rectangle classes, exercise all three translation branches, and compare the flag optimizer with an independent weighted-set dynamic program.

The formal $(K_0,K_1,K_2,K_3)$-coefficient controls are

   $(h,q)$    capacity vector
  --------- -------------------
   $(1,1)$    $(0,1,-1/2,0)$
   $(1,2)$   $(0,1,-1/2,1/4)$
   $(1,3)$   $(0,1,-1/2,1/12)$
   $(4,4)$    $(0,1,-3/4,0)$
   $(9,2)$   $(0,1,-4/7,1/3)$

[\[tab:exact-controls\]]{#tab:exact-controls label="tab:exact-controls"}

The $h=4$ row is an even-lag negative control, not an extension of the odd-lag theorem; $h=9$ tests collisions.

The frozen core has 75206 bytes and SHA-256 =0mu plus 1mu`4b247c0a580c06cfaeb22f29d5b9f80d52bee44fcb44ebd978153bc79e04bcd0`. Its canonical certificate has 24297 bytes, 72 rows, and SHA-256 =0mu plus 1mu`23f714236b53c2b89caa72b53f8139cfeab74cd07132082061c3ab0dfc048697`. All 60 named core mutations, 78 result mutations, and 32 schema mutations are distinct and rejected. The stored result has canonical SHA-256 =0mu plus 1mu`d2445cc883371ccfd96eeb09f908d62d232fcb5cde5ea9170aa2029956047c2a`; the recursively closed schema has canonical SHA-256 =0mu plus 1mu`c3a5b2a02b027cc18b67e63b32f0a238990a4754fe4f2f2ce3c8d1acf756b910`. The latter contains 568 object nodes, 140 array nodes, and 3484 nodes in total and passes the official Draft 2020--12 validator.

# Source roles, limitations, and declarations

The sole analytic input is the complete fixed three-shift terminal table law of RH-394 [@RH394]. RH-396 is the direct finite predecessor [@RH396]. Its Section 2, Lemmas 2.1 and 2.3 (PDF pages 4--5), provide the projection and reflection templates, while Lemma 4.1 (PDF page 7) provides literal declared-clock repetition. RH-396 also supplies the collision-aware density notation. The new step-$h$ flag theorem, four rectangles, MUVW identity, edge filling, rising-set surjection, and parity attainment theorem are proved locally. RH-375, RH-392, RH-395, and four remote source records remain transitive comparison or provenance entries, not strengthened analytic inputs.

The exact source closure freezes 172 Git blobs in groups of 160, 8, and 4, plus four ordered remote logical records, for 176 logical inputs. Its all-Git digest is =0mu plus 1mu`b3f5688380762a4e3c27d512311f4c0d22173c434cc40459fc77bb3eb87fb5c4`; its logical digest is =0mu plus 1mu`e9588b58f75e02e31ba5ffb279aea267074ec72f717afa84670f320d6c1030e0`. All remote verification is offline; no remote PDF is vendored, and the redistribution flags are false, false, true, false in their frozen order.

The claims are deliberately fixed-data. We do not treat $h,q$, the phase tables, or the terminal clock as growing or adaptive data; provide an effective rate uniform in those objects; address ordinary Cesàro averages; move the maximum before the limit; or claim a causal rule, since the centered table reads $\mu(n+h)$. We prove no four-shift or even-four correlation, no larger-window compiler, and no generic graph-capacity theorem. No operator, trace formula, zero model, Riemann Hypothesis statement, or Gate A--E upgrade follows.

#### Data and code availability.

The finite certificate, strict result, recursively closed schema, source locks, tests, and release-verification scripts accompany this manuscript. No external payload is included, and reproduction requires no network request.

#### Author contributions.

The RH research program directed the question, proof architecture, source roles, adversarial checks, manuscript review, and release decision. The program also retains responsibility for all mathematical and archival claims.

#### Use of AI-assisted tools.

AI-assisted tools supported drafting, finite-certificate implementation, formatting, and consistency checks. The research program directed and reviewed the arguments, source assignments, and release artifacts and retains responsibility for the final work.

#### Competing interests, funding, and ethics.

The authors declare no competing interests and no external funding. This theoretical and computational work used no human participants, animals, or personal data, so institutional ethics approval and informed consent were not applicable.
