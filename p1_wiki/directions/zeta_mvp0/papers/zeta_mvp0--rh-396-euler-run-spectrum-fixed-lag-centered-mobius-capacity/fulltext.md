---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity"
canonical_tex: "zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/main.pdf"
source_sha256: "5d9a8c6c9a39436d07a94e082fffc003cfba91ece1d3859c11e2facbd5ffe99d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Euler--Run Spectrum for Fixed-Lag Centered Möbius Capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a lag $h\geq1$. A centered phase table reads $\mu_0(n-h),\mu(n),\mu(n+h)$, and universal safety forbids two positive outputs at separation $2h$ for every ternary word. The complete three-shift terminal-log law converts every fixed-table limit, for every terminal clock, into collision-aware squarefree densities. Positive projection and relation saturation then give an exact tropical trace on all eight subsets of $\{-1,0,+1\}$ for every finite clock. The familiar four-state compression is proved throughout the non-self-loop regime $q\nmid2h$; when $q\mid2h$, the full eight states remain necessary in general.

  On square-support clocks, a phasewise identity for each shared ternary value charges two consecutive transitions by one center weight. Once the base support contains $p_0(h)=\min\{p\text{ prime}:p\nmid2h\}$, the centered capacity equals a raw step-$2h$ path-MWIS normalized by the squarefree density. Exact bracketed-run densities yield the Euler--run endpoint $$B_\infty(h)=\frac{3}{\pi^2}
   +\frac12\sum_{\substack{1\leq\ell<p_0(h)^2\\ \ell\ \mathrm{odd}}}
   R_{\ell,h}.$$ For every fixed $h$, this is the supremum over finite clocks, and no finite clock attains it. Fresh-prime lifts can plateau: strict gain is equivalent to the presence of an even positive run, while a CRT construction guarantees eventual strict gain. Across fixed lags, $\inf_{h\geq1}B_\infty(h)=3/\pi^2$, and the infimum is not attained. No monotonicity, supremum, or maximum in $h$ is claimed.
author:
- RH research program
bibliography:
- references.bib
date: 'August 12, 2026'
title: 'Euler--Run Spectrum for Fixed-Lag Centered Möbius Capacity'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; centered local rule; fixed lag; tropical trace; squarefree run; nonattained supremum.

# Definitions and main results

Write $\mu_0(k)=\mu(k)$ for integers $k\geq1$, and $\mu_0(k)=0$ for $k\leq0$. A *terminal clock* is a function $$1\leq\omega(X)\leq X,
 \qquad \omega(X)\longrightarrow\infty.
 \label{eq:clock}$$ Fix $h,q\geq1$, put $d=2h$, and fix, before $X\to\infty$, one sign table for every phase, $$F_r:\{-1,0,+1\}^3\longrightarrow\{-1,+1\},\qquad r\in\mathbb Z/q\mathbb Z.$$ Its centered output and scored terminal functional are $$\begin{aligned}
 \varepsilon_F(n)
 &=F_{n\bmod q}\bigl(\mu_0(n-h),\mu(n),\mu(n+h)\bigr),
 \label{eq:output}\\
 L_{h,q,X}(F)
 &=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}\frac{\mu(n)\varepsilon_F(n)}n.
 \label{eq:functional}\end{aligned}$$ Thus $\varepsilon_F(n)$ is the output, while $\mu(n)\varepsilon_F(n)$ is the score. The family is *universally distance-$d$ safe* when $$\neg\bigl(F_r(a,b,c)=+1\ \text{and}\
 F_{r+d}(c,e,f)=+1\bigr)
 \label{eq:safety}$$ for every phase $r$ and every $a,b,c,e,f\in\{-1,0,+1\}$. The shared letter is $c=\mu(n+h)=\mu((n+d)-h)$.

The density notation must retain collisions among the three shifts. Let $\mathcal I=\{L,C,R\}$ and $$a_L=h,\qquad a_C=0,\qquad a_R=-h.
 \label{eq:coordinate-shifts}$$ For $S\subseteq\mathcal I$, first deduplicate modulo $p^2$, then set $$B_{p,S}=\{a_i\bmod p^2:i\in S\},\qquad
 \nu_{p,S}=|B_{p,S}|,
 \qquad
 \tau_{p,S}(r)=\#\{b\in B_{p,S}:b\equiv r\pmod p\}.
 \label{eq:local-data}$$ Define $$\begin{aligned}
 \Theta_{h,q,r}(S)
 &=\frac1q
 \prod_{p\nmid q}\left(1-\frac{\nu_{p,S}}{p^2}\right)
 \prod_{p\parallel q}\left(1-\frac{\tau_{p,S}(r)}p\right)
 \prod_{p^2\mid q}
 \mathbf 1_{\{r\bmod p^2\notin B_{p,S}\}},
 \label{eq:theta}\\
 \kappa_h(S)
 &=\prod_p\left(1-\frac{\nu_{p,S}}{p^2}\right).
 \label{eq:kappa}\end{aligned}$$ Then $\Theta_{h,q,r}(\varnothing)=1/q$ and $$\sum_{r\bmod q}\Theta_{h,q,r}(S)=\kappa_h(S).
 \label{eq:phase-sum}$$ Only in a collision-free $j$-site case does this reduce to $$K_j=\prod_p\left(1-\frac{j}{p^2}\right),\qquad
 K_0=1,\qquad K_1=\frac6{\pi^2}.
 \label{eq:Kj}$$ The phase-resolved exact-support density is $$\Pi_{h,q,r}(U)=
 \sum_{W\subseteq\mathcal I\setminus U}(-1)^{|W|}
 \Theta_{h,q,r}(U\cup W).
 \label{eq:Pi}$$ It is nonnegative and has mass $\sum_{U\subseteq\mathcal I}\Pi_{h,q,r}(U)=1/q$.

For $x,y\in\{-1,0,+1\}$, write $$S(x,y)=\{C\}\cup\bigl(\{L\}:x\ne0\bigr)
 \cup\bigl(\{R\}:y\ne0\bigr)
 \label{eq:Sxy}$$ and define the nonnegative cell weight and transition $$\begin{aligned}
 \lambda_{h,q,r}(x,y)
 &=2^{-\mathbf 1_{\{x\ne0\}}-\mathbf 1_{\{y\ne0\}}}
 \Pi_{h,q,r}\bigl(S(x,y)\bigr),
 \label{eq:lambda}\\
 \mathcal K_{h,q,r}(U,V)
 &=\sum_{\substack{x\notin U\\y\in V}}
 \lambda_{h,q,r}(x,y),
 \qquad U,V\subseteq\{-1,0,+1\}.
 \label{eq:transition}\end{aligned}$$

[\[thm:fixed-clock\]]{#thm:fixed-clock label="thm:fixed-clock"} For every fixed $h,q,F$, the limit $L_{h,q}(F)=\lim_{X\to\infty}L_{h,q,X}(F)$ exists for every terminal clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} and has the same value for all such clocks. Form the finite maximum only after these fixed-table limits: $$C_h(q)=\max_{F\ {\rm universally\ safe}}|L_{h,q}(F)|.
 \label{eq:capacity}$$ If $\gamma$ runs over the $\gcd(q,d)$ cycles of $r\mapsto r+d$ in $\mathbb Z/q\mathbb Z$, then $$\boxed{
 C_h(q)=\sum_\gamma
 \max_{\substack{Y_r\subseteq\{-1,0,+1\}\\r\in\gamma\ {\rm cyclic}}}
 \sum_{r\in\gamma}\mathcal K_{h,q,r}(Y_{r-d},Y_r).}
 \label{eq:full-eight}$$ Thus the exact formula is a tropical trace on eight states for every finite $q$. Both signs of every nonzero optimum are attained.

[\[thm:compression\]]{#thm:compression label="thm:compression"} If $q\nmid d$, an optimizer in [\[eq:full-eight\]](#eq:full-eight){reference-type="eqref" reference="eq:full-eight"} can be chosen from the four antipodally symmetric subsets of $\{-1,0,+1\}$. If $q\mid d$, every cycle is a self-loop and the theorem retains all eight states; no four-state reduction is asserted. This exception is strict in general: for $h=2,q=4$, the full and four-state-restricted coefficient vectors in the basis $(K_0,K_1,K_2,K_3)$ are respectively $$(0,0,\tfrac12,-\tfrac12)
 \quad\text{and}\quad
 (0,0,1,-2),
 \label{eq:self-loop-obstruction}$$ and the full value is strictly larger.

For the endpoint, let $$p_0(h)=\min\{p\text{ prime}:p\nmid d\}.
 \label{eq:p0}$$ For a finite set $J\subset\mathbb Z$, define the absolutely convergent local product $$D_h(J)=\prod_p\left(
 1-\frac{|\{dj\bmod p^2:j\in J\}|}{p^2}\right),
 \label{eq:Dh}$$ and, for $\ell\geq1$, $$\begin{aligned}
 R_{\ell,h}
 &=D_h([0,\ell-1])-D_h(\{-1\}\cup[0,\ell-1])
 \notag\\
 &\quad-D_h([0,\ell])+D_h([-1,\ell]).
 \label{eq:Rlh}\end{aligned}$$ Intervals here denote sets of integers. The quantity $R_{\ell,h}$ is the density of an exact bracketed squarefree run of length $\ell$ in step-$d$ coordinates, hence is nonnegative. Set $$B_\infty(h)=\frac3{\pi^2}
 +\frac12\sum_{\substack{1\leq\ell<p_0(h)^2\\\ell\ \mathrm{odd}}}
 R_{\ell,h}.
 \label{eq:Binfinity}$$

[\[thm:endpoint\]]{#thm:endpoint label="thm:endpoint"} For every fixed $h\geq1$, $$\boxed{\sup_{q<\infty}C_h(q)=B_\infty(h),\qquad
 C_h(q)<B_\infty(h)\quad(q<\infty).}
 \label{eq:all-clock-endpoint}$$ The supremum is over finite clocks only and is taken after the fixed-table terminal limits and finite safe maxima.

[\[cor:lag-infimum\]]{#cor:lag-infimum label="cor:lag-infimum"} Across fixed positive integer lags, $$\boxed{\inf_{h\geq1}B_\infty(h)=\frac3{\pi^2}.}
 \label{eq:lag-infimum}$$ Every fixed $h$ satisfies $B_\infty(h)>3/\pi^2$, so the infimum is not attained. No supremum, maximum, or monotonicity assertion in $h$ is made.

# Terminal table bridge and relation saturation

RH-394 proves the complete terminal-log table law for any three fixed distinct shifts: Theorem 1.1, equation (8), Theorem 1.2, equations (11)--(14), and Corollary 1.3 (printed/PDF pages 2--3) [@RH394]. We instantiate it at the ordered shifts $(a_L,a_C,a_R)=(h,0,-h)$. They are distinct because $h\geq1$, and all of $h,q,F$ are fixed before the limit. This is the sole analytic terminal-clock input in the present paper.

To state the resulting bridge, put $$H_r(x,z,y)=zF_r(x,z,y)$$ and, for $U\subseteq\mathcal I$, let $$\overline H_{r,U}=2^{-|U|}
 \sum_{\sigma\in\{-1,+1\}^{U}}H_r(\sigma_U,0_{U^c}).$$ The cited law, including the boundary convention $\mu_0$, gives $$L_{h,q}(F)=
 \sum_{r\bmod q}\sum_{U\subseteq\mathcal I}
 \Pi_{h,q,r}(U)\overline H_{r,U}.
 \label{eq:table-bridge}$$ It also gives [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}--[\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"}. The deduplication in [\[eq:local-data\]](#eq:local-data){reference-type="eqref" reference="eq:local-data"} is essential: if, for example, $p^2\mid d$, several coordinate shifts can define the same forbidden class modulo $p^2$. Equation [\[eq:table-bridge\]](#eq:table-bridge){reference-type="eqref" reference="eq:table-bridge"} is qualitative and fixed-data; no rate uniform in $h$ or $q$ is imported. Tao and Tao--Teräväinen are inherited two-point and odd-correlation provenance inside RH-394, not separately strengthened inputs here [@Tao2016LogChowla; @TaoTeravainen2019].

[\[lem:projection\]]{#lem:projection label="lem:projection"} Given a safe family $F$, replace every $+1$ output at a cell whose center $z$ is not $+1$ by $-1$, leaving every other cell unchanged. Call the result $F^+$. Then $F^+$ is safe and $$L_{h,q}(F^+)\geq L_{h,q}(F).$$ If $$A_r=\{(x,y)\in\{-1,0,+1\}^2:F^+_r(x,+1,y)=+1\},
 \label{eq:relation}$$ then $$L_{h,q}(F^+)=
 \sum_{r\bmod q}\sum_{(x,y)\in A_r}\lambda_{h,q,r}(x,y).
 \label{eq:projected-limit}$$

At $z=-1$, changing the output from $+1$ to $-1$ changes the score $zF$ from $-1$ to $+1$; at $z=0$, it does not change the score. Deleting positive outputs cannot create a forbidden pair, so safety is preserved. This establishes the pointwise score comparison before any limit is taken.

Start now from the all-minus table. Its score is $-z$, whose uniform average on every exact-support sign stratum is zero. Turning the center-$+1$ cell $(x,+1,y)$ from minus to plus changes $H$ by two. The density of that specified sign cell is $$2^{-1-\mathbf 1_{\{x\ne0\}}-\mathbf 1_{\{y\ne0\}}}
 \Pi_{h,q,r}(S(x,y)).$$ Multiplication by two gives exactly [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"}. Summing the changed cells proves [\[eq:projected-limit\]](#eq:projected-limit){reference-type="eqref" reference="eq:projected-limit"}.

For a relation $A\subseteq\{-1,0,+1\}^2$, define, before using either symbol, $$\operatorname{Source}(A)=\{x:(x,y)\in A\text{ for some }y\},\qquad
 \operatorname{Target}(A)=\{y:(x,y)\in A\text{ for some }x\}.$$

[\[lem:saturation\]]{#lem:saturation label="lem:saturation"} The projected relation family is safe if and only if $$\operatorname{Target}(A_r)\cap\operatorname{Source}(A_{r+d})=\varnothing
 \qquad(r\bmod q).
 \label{eq:relation-safety}$$ Put $Y_r=\operatorname{Target}(A_r)$. Then $$A_r\subseteq(\{-1,0,+1\}\setminus Y_{r-d})\times Y_r.
 \label{eq:relation-containment}$$ Replacing every $A_r$ by the saturated relation $$\widetilde A_r=(\{-1,0,+1\}\setminus Y_{r-d})\times Y_r
 \label{eq:saturated-relation}$$ preserves safety and weakly increases [\[eq:projected-limit\]](#eq:projected-limit){reference-type="eqref" reference="eq:projected-limit"}. Conversely, every subset profile $(Y_r)_{r\bmod q}$ in [\[eq:saturated-relation\]](#eq:saturated-relation){reference-type="eqref" reference="eq:saturated-relation"} is safe.

An edge $(x,c)\in A_r$ and an edge $(c,y)\in A_{r+d}$ are precisely two positive outputs allowed by a common shared letter $c$. Their absence for every $c\in\{-1,0,+1\}$ is [\[eq:relation-safety\]](#eq:relation-safety){reference-type="eqref" reference="eq:relation-safety"}. It follows that every source of $A_r$ lies outside $\operatorname{Target}(A_{r-d})=Y_{r-d}$, while its targets lie in $Y_r$, proving [\[eq:relation-containment\]](#eq:relation-containment){reference-type="eqref" reference="eq:relation-containment"}. All weights in [\[eq:projected-limit\]](#eq:projected-limit){reference-type="eqref" reference="eq:projected-limit"} are nonnegative, so saturation cannot lower the score. Finally, an edge of $\widetilde A_r$ ends in $Y_r$, while an edge of $\widetilde A_{r+d}$ begins outside $Y_r$; hence the saturated family is safe.

[\[lem:reflection\]]{#lem:reflection label="lem:reflection"} Define $$F^\rho_r(x,z,y)=F_r(-x,-z,-y).$$ This map preserves universal safety and satisfies $$L_{h,q}(F^\rho)=-L_{h,q}(F).
 \label{eq:reflection-sign}$$

Simultaneous negation is a bijection of the ternary words appearing in [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"}, so it preserves safety. Moreover, $$zF^\rho_r(x,z,y)=-H_r(-x,-z,-y).$$ Every exact-support stratum in [\[eq:table-bridge\]](#eq:table-bridge){reference-type="eqref" reference="eq:table-bridge"} is invariant under simultaneous sign negation. Its uniform average therefore changes sign, which proves [\[eq:reflection-sign\]](#eq:reflection-sign){reference-type="eqref" reference="eq:reflection-sign"}. This is a terminal table-law identity; it does not identify the reflected table with a pointwise transformation of the observed Möbius sequence.

# The tropical optimizer and four-state boundary

[\[prop:tropical\]]{#prop:tropical label="prop:tropical"} The right side of [\[eq:full-eight\]](#eq:full-eight){reference-type="eqref" reference="eq:full-eight"} is the maximum positive terminal score over all safe tables.

By Lemmas [\[lem:projection\]](#lem:projection){reference-type="ref" reference="lem:projection"} and [\[lem:saturation\]](#lem:saturation){reference-type="ref" reference="lem:saturation"}, a positive optimum is attained by a saturated subset profile. The phase $r$ contribution is $$\sum_{\substack{x\notin Y_{r-d}\\y\in Y_r}}
 \lambda_{h,q,r}(x,y)
 =\mathcal K_{h,q,r}(Y_{r-d},Y_r).$$ Addition by $d$ decomposes $\mathbb Z/q\mathbb Z$ into $\gcd(q,d)$ cycles, each of length $q/\gcd(q,d)$. Profiles on distinct cycles do not interact, so their maxima add. Cyclic closure of each finite dynamic program is exactly the tropical trace in [\[eq:full-eight\]](#eq:full-eight){reference-type="eqref" reference="eq:full-eight"}. There are eight possible subsets of $\{-1,0,+1\}$, including all singleton states and all self-loops.

The existence and clock independence of every fixed-table limit follow from [\[eq:table-bridge\]](#eq:table-bridge){reference-type="eqref" reference="eq:table-bridge"}. Positive projection, saturation, and Proposition [\[prop:tropical\]](#prop:tropical){reference-type="ref" reference="prop:tropical"} give the displayed positive maximum. Lemma [\[lem:reflection\]](#lem:reflection){reference-type="ref" reference="lem:reflection"} shows that every score has a safe score of the opposite sign, hence the positive maximum equals the absolute capacity and both orientations are attained. This proves every assertion of the theorem, including self-loop clocks.

For an antipodally symmetric set $Y\subseteq\{-1,0,+1\}$, write $$u(Y)=\left(u_0(Y),u_1(Y)\right)
 =\left(\mathbf 1_{\{0\in Y\}},
 \frac{|Y\cap\{-1,+1\}|}{2}\right)\in\{0,1\}^2.$$ Abbreviate $$\alpha_r=\Pi_{h,q,r}(\{C\}),\quad
 \beta_r=\Pi_{h,q,r}(\{L,C\}),\quad
 \gamma_r=\Pi_{h,q,r}(\{C,R\}),\quad
 \eta_r=\Pi_{h,q,r}(\{L,C,R\}).$$ Directly summing [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"} gives, on the four states, $$\begin{aligned}
 \mathcal K_{h,q,r}(U,V)
 &=\alpha_r(1-u_0(U))u_0(V)
 +\beta_r(1-u_1(U))u_0(V)\notag\\
 &\quad+\gamma_r(1-u_0(U))u_1(V)
 +\eta_r(1-u_1(U))u_1(V).
 \label{eq:four-transition}\end{aligned}$$

[\[prop:compression\]]{#prop:compression label="prop:compression"} If $q\nmid d$, the eight-state maximum has a four-state optimizer, and its transitions are given by [\[eq:four-transition\]](#eq:four-transition){reference-type="eqref" reference="eq:four-transition"}.

Fix the membership of zero in every $Y_r$, and set $k_r=|Y_r\cap\{-1,+1\}|\in\{0,1,2\}$. The cell weights depend on a nonzero outer coordinate only through its being nonzero, not through its sign. Consequently the two transition terms in which $Y_r$ occurs are affine in $k_r$ once all other memberships are fixed.

The hypothesis $q\nmid d$ is equivalent to $q/\gcd(q,d)>1$. Thus the occurrence of $Y_r$ as target in the $r$-term and as excluded source in the $r+d$-term belongs to two distinct terms, with no self-identification. An affine function at $k_r=1$ is no larger than at least one endpoint $k_r=0$ or $2$. Round one phase at a time. The objective never decreases, and after finitely many rounds all nonzero memberships are antipodally symmetric. Equation [\[eq:four-transition\]](#eq:four-transition){reference-type="eqref" reference="eq:four-transition"} follows by splitting the sum into the four zero/nonzero support patterns.

Proposition [\[prop:compression\]](#prop:compression){reference-type="ref" reference="prop:compression"} proves the non-self-loop statement. If $q\mid d$, then $r+d=r$ for every phase. A self-loop transition uses the same nonzero count both as an included target and an excluded source; terms proportional to $k_r(2-k_r)$ can occur, so the preceding affine rounding is unavailable.

The obstruction $(h,q)=(2,4)$ can be checked without approximation. At each even phase every self-loop transition is zero: phase $0$ has zero center mass, while at phase $2$ both outer coordinates are forced to be zero and cannot lie simultaneously outside and inside the same state. At either odd phase, substituting [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}--[\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"} for all eight subsets gives

                     $Y$ type                     number of states  self-loop value
  ---------------------------------------------- ------------------ -----------------
            $\varnothing,\{-1,0,+1\}$                   $2$         $0$
   one nonzero sign, or its complement with $0$         $4$         $(K_2-K_3)/4$
              $\{0\}$ or $\{-1,+1\}$                    $2$         $K_2/2-K_3$

Here $$\frac{K_3}{K_2}
 =\frac12\prod_{p\geq3}\left(1-\frac1{p^2-2}\right).$$ The product is less than one. On the other hand, $$\sum_{p\geq3}\frac1{p^2-2}
 <\sum_{\substack{n\geq3\\n\ {\rm odd}}}\frac1{n(n-1)}
 =1-\log2<\frac13,$$ and $\prod(1-x_i)\geq1-\sum x_i$, together with $\log2>2/3$, gives $$\frac13<\frac{K_3}{K_2}<\frac12.
 \label{eq:K3K2-bounds}$$ Thus a one-sign state is the full optimum at each odd phase, whereas the four-state optimum is $\{0\}$ or $\{-1,+1\}$. Adding the two odd phases yields respectively $(K_2-K_3)/2$ and $K_2-2K_3$, which are the coefficient vectors in [\[eq:self-loop-obstruction\]](#eq:self-loop-obstruction){reference-type="eqref" reference="eq:self-loop-obstruction"}; their difference $(3K_3-K_2)/2$ is positive by [\[eq:K3K2-bounds\]](#eq:K3K2-bounds){reference-type="eqref" reference="eq:K3K2-bounds"}.

# Square-support marginal charge

Let $\mathcal P$ be a nonempty finite set of primes and $$q_{\mathcal P}=\prod_{p\in\mathcal P}p^2.$$ More generally, call $Q$ *square-supported* if every prime divisor of $Q$ occurs to exponent at least two. Its positive center phases form $$V_h(Q)=\{r\bmod Q:\Theta_{h,Q,r}(\{C\})>0\}
       =\{r\bmod Q:p^2\nmid r\text{ for every }p\mid Q\}.$$ Write $$\begin{aligned}
 N_h(Q)&=|V_h(Q)|,\label{eq:NQ}\\
 \alpha_h(Q)&=\max_{\substack{I\subseteq V_h(Q)\\
 I\cap(I+d)=\varnothing}}|I|,\label{eq:alphaQ}\\
 M_h(Q)&=K_1\frac{\alpha_h(Q)}{N_h(Q)}.
 \label{eq:MQ}\end{aligned}$$ The normalization is deliberate: $\alpha_h(Q)$ is a raw, unweighted MWIS cardinality, whereas $M_h(Q)$ is a weighted terminal value. Neither [\[eq:MQ\]](#eq:MQ){reference-type="eqref" reference="eq:MQ"} nor the equality with centered capacity below is being asserted for clocks having a prime only to the first power.

[\[lem:clock-divisibility\]]{#lem:clock-divisibility label="lem:clock-divisibility"} If $q\mid Q$, then $C_h(q)\leq C_h(Q)$. On every square-supported $Q$, one also has $M_h(Q)\leq C_h(Q)$.

Regard a $q$-phase table as a $Q$-phase table by literal repetition. It produces the same output word, preserves universal safety, and has the same fixed-table terminal limit. The declared clock need not be a minimal period. Maximizing after the limits gives the first assertion.

For the second, choose an independent set $I$ in [\[eq:alphaQ\]](#eq:alphaQ){reference-type="eqref" reference="eq:alphaQ"}. At $r\in I$, let the projected relation be all of $\{-1,0,+1\}^2$; off $I$, let it be empty. This family is safe, and summing [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"} over both outer coordinates gives $\Theta_{h,Q,r}(\{C\})$. All positive center phases of a square-supported clock have the common weight $$\delta_Q=\frac1Q\prod_{p\nmid Q}\left(1-\frac1{p^2}\right)
 =\frac{K_1}{N_h(Q)}.
 \label{eq:deltaQ}$$ Thus the embedded value is $\delta_Q\alpha_h(Q)=M_h(Q)$.

[\[lem:marginal\]]{#lem:marginal label="lem:marginal"} Let $Q$ be square-supported, and suppose that both $r$ and $r+d$ belong to $V_h(Q)$. For each $t\in\{-1,0,+1\}$, define $$m_r(t)=\sum_{x\in\{-1,0,+1\}}\lambda_{h,Q,r}(x,t),\qquad
 m'_{r+d}(t)=\sum_{y\in\{-1,0,+1\}}\lambda_{h,Q,r+d}(t,y).$$ Then $$\begin{aligned}
 m_r(0)
 &=\Theta_{h,Q,r}(\{C\})-\Theta_{h,Q,r}(\{C,R\})
 \notag\\
 &=\Theta_{h,Q,r+d}(\{C\})
   -\Theta_{h,Q,r+d}(\{L,C\})=m'_{r+d}(0),
 \label{eq:marginal-zero}\\
 m_r(\pm1)
 &=\frac12\Theta_{h,Q,r}(\{C,R\})
 =\frac12\Theta_{h,Q,r+d}(\{L,C\})
 =m'_{r+d}(\pm1).
 \label{eq:marginal-sign}\end{aligned}$$ In particular, $$m_r(t)=m'_{r+d}(t)\quad(t\in\{-1,0,+1\}),\qquad
 \sum_{t\in\{-1,0,+1\}}m_r(t)=\delta_Q.
 \label{eq:marginal-total}$$

Summing exact-support cells with right coordinate zero gives the event that the center is squarefree while the right site is not; this is the difference in the first line of [\[eq:marginal-zero\]](#eq:marginal-zero){reference-type="eqref" reference="eq:marginal-zero"}. If the right coordinate is a specified nonzero sign, uniform sign splitting contributes the factor $1/2$ in [\[eq:marginal-sign\]](#eq:marginal-sign){reference-type="eqref" reference="eq:marginal-sign"}. The same argument at phase $r+d$ uses the left coordinate.

It remains to prove the two phase identities. Outside the prime support of $Q$, the pair of coordinate shifts $\{C,R\}=\{0,-h\}$ is a translate of $\{L,C\}=\{h,0\}$, so the deduplicated local factors are identical even when the two residues collide. At a supported prime square, the first pair requires $r\not\equiv0,-h\pmod{p^2}$, and the second requires $r+d\not\equiv0,h\pmod{p^2}$. Since the endpoint center phases $r$ and $r+d$ are positive, in both cases the only remaining condition is $r+h\not\equiv0\pmod{p^2}$. Hence $$\Theta_{h,Q,r}(\{C,R\})
 =\Theta_{h,Q,r+d}(\{L,C\}).$$ Both singleton center densities equal $\delta_Q$ by [\[eq:deltaQ\]](#eq:deltaQ){reference-type="eqref" reference="eq:deltaQ"}. This proves [\[eq:marginal-zero\]](#eq:marginal-zero){reference-type="eqref" reference="eq:marginal-zero"} and [\[eq:marginal-sign\]](#eq:marginal-sign){reference-type="eqref" reference="eq:marginal-sign"}; adding the three states proves [\[eq:marginal-total\]](#eq:marginal-total){reference-type="eqref" reference="eq:marginal-total"}. The $t=0$ difference is part of the identity, not an omitted zero-weight case.

[\[lem:path-charge\]]{#lem:path-charge label="lem:path-charge"} Under the hypotheses of Lemma [\[lem:marginal\]](#lem:marginal){reference-type="ref" reference="lem:marginal"}, for all $U,V,W\subseteq\{-1,0,+1\}$, $$\mathcal K_{h,Q,r}(U,V)
 +\mathcal K_{h,Q,r+d}(V,W)\leq\delta_Q.
 \label{eq:pair-charge}$$ Consequently a positive step-$d$ path of length $L$ contributes at most $\lceil L/2\rceil\delta_Q$ to [\[eq:full-eight\]](#eq:full-eight){reference-type="eqref" reference="eq:full-eight"}.

Dropping the outer-coordinate restrictions in the two transitions and splitting at the shared state gives $$\begin{aligned}
 \mathcal K_{h,Q,r}(U,V)
 &\leq\sum_{t\in V}m_r(t),\\
 \mathcal K_{h,Q,r+d}(V,W)
 &\leq\sum_{t\notin V}m'_{r+d}(t).\end{aligned}$$ Their sum is $\delta_Q$ by [\[eq:marginal-total\]](#eq:marginal-total){reference-type="eqref" reference="eq:marginal-total"}. Pair successive sites of a path, leaving one unpaired site when $L$ is odd; a single transition is at most its full center mass $\delta_Q$. This gives the path charge.

[\[prop:square-saturation\]]{#prop:square-saturation label="prop:square-saturation"} If $Q$ is square-supported and $p_0(h)\mid Q$, then $$\boxed{C_h(Q)=M_h(Q)
 =K_1\frac{\alpha_h(Q)}{N_h(Q)}.}
 \label{eq:square-saturation}$$

Because $p_0\nmid d$, a step-$d$ orbit modulo $p_0^2$ visits every residue class. The factor $p_0^2\mid Q$ therefore forces at least one zero center phase on every step-$d$ cycle. Deleting the zero phases splits the positive graph into finite paths; there are no all-positive cycles. Lemma [\[lem:path-charge\]](#lem:path-charge){reference-type="ref" reference="lem:path-charge"} bounds the contribution of each path by its ordinary path-MWIS cardinality times $\delta_Q$. Summing paths gives $$C_h(Q)\leq\delta_Q\alpha_h(Q)=M_h(Q).$$ The reverse inequality is the one-site embedding from Lemma [\[lem:clock-divisibility\]](#lem:clock-divisibility){reference-type="ref" reference="lem:clock-divisibility"}.

[\[prop:same-support\]]{#prop:same-support label="prop:same-support"} Suppose $p_0(h)\in\mathcal P$, $q_{\mathcal P}\mid Q$, and $\operatorname{rad}(Q)=\operatorname{rad}(q_{\mathcal P})$. Put $R=Q/q_{\mathcal P}$. No coprimality condition on $R$ and $d$ is required. Then $$\begin{aligned}
 N_h(Q)&=R\,N_h(q_{\mathcal P}),&
 \alpha_h(Q)&=R\,\alpha_h(q_{\mathcal P}),\label{eq:cover-counts}\\
 C_h(Q)&=M_h(Q)=M_h(q_{\mathcal P})=C_h(q_{\mathcal P}).
 \label{eq:cover-capacity}\end{aligned}$$

Reduction modulo $q_{\mathcal P}$ makes the positive support word on $\mathbb Z/Q\mathbb Z$ an $R$-fold cover of the corresponding word on $\mathbb Z/q_{\mathcal P}\mathbb Z$, proving the first count in [\[eq:cover-counts\]](#eq:cover-counts){reference-type="eqref" reference="eq:cover-counts"}. By Proposition [\[prop:square-saturation\]](#prop:square-saturation){reference-type="ref" reference="prop:square-saturation"}, the base positive graph is a disjoint union of paths. The inverse image of a path under any graph cover is $R$ disjoint copies of that path: choose a lift of one endpoint, then lift its unique successive edges. This argument is independent of $\gcd(R,d)$. Hence the path-MWIS cardinality scales by $R$, proving the second count. The ratio in [\[eq:MQ\]](#eq:MQ){reference-type="eqref" reference="eq:MQ"} is unchanged, and Proposition [\[prop:square-saturation\]](#prop:square-saturation){reference-type="ref" reference="prop:square-saturation"} at both clocks proves [\[eq:cover-capacity\]](#eq:cover-capacity){reference-type="eqref" reference="eq:cover-capacity"}.

[\[rem:p0-counterexample\]]{#rem:p0-counterexample label="rem:p0-counterexample"} For $h=6$, one has $d=12$ and $p_0=5$. The same-support lift $36\mid72$ occurs before the support contains $5^2$: $$(\alpha_6(36),N_6(36))=(9,24),\qquad
 (\alpha_6(72),N_6(72))=(24,48).$$ The raw ratios are $3/8$ and $1/2$, so unconditional same-support scaling is false. Once the base includes $p_0^2$, $$(\alpha_6(900),N_6(900))=(291,576),\qquad
 (\alpha_6(1800),N_6(1800))=(582,1152),$$ in agreement with Proposition [\[prop:same-support\]](#prop:same-support){reference-type="ref" reference="prop:same-support"}. These exact counts are finite illustrations of the proved path-cover mechanism, not asymptotic evidence.

The finite MWIS and square-clock viewpoint follows the combinatorial template of RH-375, Theorem 2.2 and Sections 3--5 [@RH375]. The $h=1$ centered marginal argument in RH-395 is the direct finite precedent [@RH395]. Neither predecessor supplies the general distance-$d$, collision-aware proof above, and neither is used as a terminal-clock analytic input.

# Euler--run formula

For a finite prime set $\mathcal P$ and finite $J\subset\mathbb Z$, define $$D_{h,\mathcal P}(J)=
 \prod_{p\in\mathcal P}\left(
 1-\frac{|\{dj\bmod p^2:j\in J\}|}{p^2}\right),
 \label{eq:finite-D}$$ and define $R_{\ell,h,\mathcal P}$ by the same four-term expression as [\[eq:Rlh\]](#eq:Rlh){reference-type="eqref" reference="eq:Rlh"}, with $D_h$ replaced by $D_{h,\mathcal P}$. Thus $$\begin{aligned}
 R_{\ell,h,\mathcal P}
 &=D_{h,\mathcal P}([0,\ell-1])
 -D_{h,\mathcal P}(\{-1\}\cup[0,\ell-1])\notag\\
 &\quad-D_{h,\mathcal P}([0,\ell])
 +D_{h,\mathcal P}([-1,\ell]).
 \label{eq:finite-R}\end{aligned}$$

[\[lem:finite-runs\]]{#lem:finite-runs label="lem:finite-runs"} Suppose $p_0(h)\in\mathcal P$. On $\mathbb Z/q_{\mathcal P}\mathbb Z$, the exact number of bracketed positive step-$d$ runs of length $\ell$ is $$q_{\mathcal P}R_{\ell,h,\mathcal P}.
 \label{eq:run-count}$$ These quantities are nonnegative integers and vanish for $\ell\geq p_0(h)^2$. Moreover, $$\alpha_h(q_{\mathcal P})
 =\frac{N_h(q_{\mathcal P})}{2}
 +\frac{q_{\mathcal P}}2
 \sum_{\substack{1\leq\ell<p_0(h)^2\\\ell\ {\rm odd}}}
 R_{\ell,h,\mathcal P}.
 \label{eq:alpha-run}$$

For $r\bmod q_{\mathcal P}$, all phases $r+dj$, $j\in J$, are positive precisely when, for each $p\in\mathcal P$, the residue $r\pmod{p^2}$ avoids the distinct classes $-dj\pmod{p^2}$. The Chinese remainder theorem therefore gives the exact density [\[eq:finite-D\]](#eq:finite-D){reference-type="eqref" reference="eq:finite-D"}. Inclusion--exclusion on the two endpoint events $r-d$ positive and $r+d\ell$ positive gives [\[eq:finite-R\]](#eq:finite-R){reference-type="eqref" reference="eq:finite-R"}. Its complement interpretation is exactly: zero at index $-1$, positive at indices $0,\ldots,\ell-1$, and zero at index $\ell$. This proves [\[eq:run-count\]](#eq:run-count){reference-type="eqref" reference="eq:run-count"} and nonnegativity.

Because $p_0\nmid d$, the residues $dj\pmod{p_0^2}$ for any $p_0^2$ consecutive indices $j$ cover all classes. Every such block therefore contains a phase divisible by $p_0^2$, proving the run cutoff. There are no all-positive cycles.

Finally, a path of length $\ell$ has MWIS cardinality $$\left\lceil\frac\ell2\right\rceil
 =\frac\ell2+\frac12\mathbf 1_{\{\ell\ {\rm odd}\}}.$$ Summing the first term over all runs gives $N_h/2$, and summing the second counts the odd runs. Equation [\[eq:run-count\]](#eq:run-count){reference-type="eqref" reference="eq:run-count"} now gives [\[eq:alpha-run\]](#eq:alpha-run){reference-type="eqref" reference="eq:alpha-run"}.

[\[prop:finite-endpoint\]]{#prop:finite-endpoint label="prop:finite-endpoint"} If $p_0(h)\in\mathcal P$, then $$\begin{aligned}
 C_h(q_{\mathcal P})
 &=M_h(q_{\mathcal P})=B_{h,\mathcal P},
 \label{eq:finite-B-equality}\\
 B_{h,\mathcal P}
 &=\frac{K_1}{2}
 +\frac{K_1}{2D_{h,\mathcal P}(\{0\})}
 \sum_{\substack{1\leq\ell<p_0(h)^2\\\ell\ {\rm odd}}}
 R_{\ell,h,\mathcal P}.
 \label{eq:finite-B}\end{aligned}$$

The singleton finite density satisfies $$D_{h,\mathcal P}(\{0\})
 =\prod_{p\in\mathcal P}\left(1-\frac1{p^2}\right)
 =\frac{N_h(q_{\mathcal P})}{q_{\mathcal P}}.$$ Insert [\[eq:alpha-run\]](#eq:alpha-run){reference-type="eqref" reference="eq:alpha-run"} into the normalized definition [\[eq:MQ\]](#eq:MQ){reference-type="eqref" reference="eq:MQ"}. This gives [\[eq:finite-B\]](#eq:finite-B){reference-type="eqref" reference="eq:finite-B"}. Proposition [\[prop:square-saturation\]](#prop:square-saturation){reference-type="ref" reference="prop:square-saturation"} gives [\[eq:finite-B-equality\]](#eq:finite-B-equality){reference-type="eqref" reference="eq:finite-B-equality"}.

[\[lem:infinite-density\]]{#lem:infinite-density label="lem:infinite-density"} For every fixed finite $J\subset\mathbb Z$, the products $D_{h,\mathcal P}(J)$ converge to $D_h(J)$ as $\mathcal P$ increases through the primes. The limit is the density of simultaneous squarefreeness at the step-$d$ positions indexed by $J$. Consequently $$R_{\ell,h,\mathcal P}\longrightarrow R_{\ell,h}\geq0
 \qquad(\ell\text{ fixed}).$$

The number of excluded classes at a prime is at most $|J|$, and $$\sum_p\frac{|\{dj\bmod p^2:j\in J\}|}{p^2}
 \leq |J|\sum_p\frac1{p^2}<\infty.$$ Thus the local products converge absolutely in the standard product sense (with a possible zero caused only by a finite local factor). Finite CRT gives every truncated density. Removing the truncation is justified by the square-divisor union bound $$\overline d\{n:p^2\mid n+dj
 \text{ for some }j\in J,\ p>Y\}
 \leq |J|\sum_{p>Y}\frac1{p^2}\longrightarrow0.$$ Hence the product is the claimed density. Applying the same two-endpoint inclusion--exclusion as in Lemma [\[lem:finite-runs\]](#lem:finite-runs){reference-type="ref" reference="lem:finite-runs"} shows that the four-term limit is an exact bracketed-run density, so it is nonnegative.

[\[prop:cofinal\]]{#prop:cofinal label="prop:cofinal"} Let $\mathcal P_y$ be any increasing prime-initial family containing $p_0(h)$ and tending to all primes. Then $$B_{h,\mathcal P_y}\longrightarrow B_\infty(h).
 \label{eq:cofinal-limit}$$

Lemma [\[lem:infinite-density\]](#lem:infinite-density){reference-type="ref" reference="lem:infinite-density"} gives $$D_{h,\mathcal P_y}(\{0\})\longrightarrow
 D_h(\{0\})=\prod_p(1-p^{-2})=K_1.$$ It also gives convergence of every run-density term. The run cutoff $\ell<p_0(h)^2$ is fixed and finite, so the limit can be taken termwise in [\[eq:finite-B\]](#eq:finite-B){reference-type="eqref" reference="eq:finite-B"}. Its first term is $K_1/2=3/\pi^2$, and its run coefficient tends to $1/2$. The result is exactly [\[eq:Binfinity\]](#eq:Binfinity){reference-type="eqref" reference="eq:Binfinity"}.

The exact rational interval oracle in the companion artifact encloses $$B_\infty(1)\in[0.4214,0.4224],\qquad
 B_\infty(2)\in[0.3282,0.3296],\qquad
 B_\infty(3)\in[0.4143,0.4181].$$ These intervals orient the scale of the endpoint. They are not used in any comparison or proof, and they imply no monotonicity in $h$.

# Fresh-prime lifts and strict nonattainment

Fix a finite prime support $\mathcal P$ containing $p_0(h)$, and let $\varpi\notin\mathcal P$ be a prime with $\varpi\nmid d q_{\mathcal P}$. Put $\mathcal P'=\mathcal P\cup\{\varpi\}$. Every old positive run has length less than $p_0^2$, and $$p_0^2<\varpi^2,$$ because $p_0$ is already supported and no smaller prime can be both fresh and coprime to $d$.

[\[lem:path-deletion\]]{#lem:path-deletion label="lem:path-deletion"} Let $P_L$ be a path with vertices $1,\ldots,L$. Deleting vertex $j$ leaves MWIS cardinality $$\left\lceil\frac{j-1}{2}\right\rceil
 +\left\lceil\frac{L-j}{2}\right\rceil.
 \label{eq:deleted-path}$$ If $L$ is odd, this is one less than $\lceil L/2\rceil$ exactly when $j$ is odd. If $L$ is even, it always equals $L/2$.

Deleting $j$ splits $P_L$ into paths of lengths $j-1$ and $L-j$; their MWIS cardinalities add, giving [\[eq:deleted-path\]](#eq:deleted-path){reference-type="eqref" reference="eq:deleted-path"}. Substitution of $L=2m+1$ or $L=2m$ gives the two parity statements.

[\[prop:fresh-recurrence\]]{#prop:fresh-recurrence label="prop:fresh-recurrence"} Let $\mathcal R_{\mathcal P}$ be the multiset of old positive run lengths and set $$E_{\mathcal P}=
 \sum_{\substack{L\in\mathcal R_{\mathcal P}\\L\ {\rm even}}}\frac L2,
 \qquad
 O_{\mathcal P}=
 \sum_{\substack{L\in\mathcal R_{\mathcal P}\\L\ {\rm odd}}}
 \left\lceil\frac L2\right\rceil.$$ Then $$\begin{aligned}
 N_h(q_{\mathcal P'})
 &=(\varpi^2-1)N_h(q_{\mathcal P}),\label{eq:Nprime}\\
 \alpha_h(q_{\mathcal P'})
 &=\varpi^2\alpha_h(q_{\mathcal P})-O_{\mathcal P}\notag\\
 &=(\varpi^2-1)\alpha_h(q_{\mathcal P})+E_{\mathcal P},
 \label{eq:alphaprime}\\
 B_{h,\mathcal P'}-B_{h,\mathcal P}
 &=\frac{K_1E_{\mathcal P}}
 {(\varpi^2-1)N_h(q_{\mathcal P})}.
 \label{eq:normalized-gain}\end{aligned}$$ Thus a fresh-prime step is strict exactly when the old positive graph has an even run. It is not necessarily strict at every step.

Because $\varpi\nmid q_{\mathcal P}$, every old phase has $\varpi^2$ lifts modulo $q_{\mathcal P'}$. Exactly one lift is divisible by $\varpi^2$, proving [\[eq:Nprime\]](#eq:Nprime){reference-type="eqref" reference="eq:Nprime"}.

Consider an old run of length $L<\varpi^2$. Among its $\varpi^2$ lifted copies, $\varpi^2-L$ have no deletion, and for each $j=1,\ldots,L$ exactly one copy has its $j$th vertex deleted. Indeed, the lift parameter runs bijectively modulo $\varpi^2$; two different positions cannot be deleted in the same lift because that would give $\varpi^2\mid d(j_1-j_2)$, while $\varpi\nmid d$ and $0<|j_1-j_2|<\varpi^2$.

Lemma [\[lem:path-deletion\]](#lem:path-deletion){reference-type="ref" reference="lem:path-deletion"} shows that an odd run loses one unit for each odd deletion position, a total loss $\lceil L/2\rceil$, whereas an even run loses nothing. Its total lifted contribution is therefore $$\begin{cases}
  (\varpi^2-1)\lceil L/2\rceil,&L\text{ odd},\\
  \varpi^2L/2,&L\text{ even}.
 \end{cases}$$ Summing runs gives both forms of [\[eq:alphaprime\]](#eq:alphaprime){reference-type="eqref" reference="eq:alphaprime"}. Dividing [\[eq:alphaprime\]](#eq:alphaprime){reference-type="eqref" reference="eq:alphaprime"} by [\[eq:Nprime\]](#eq:Nprime){reference-type="eqref" reference="eq:Nprime"} in [\[eq:MQ\]](#eq:MQ){reference-type="eqref" reference="eq:MQ"} proves [\[eq:normalized-gain\]](#eq:normalized-gain){reference-type="eqref" reference="eq:normalized-gain"}.

[\[rem:plateau\]]{#rem:plateau label="rem:plateau"} For $h=9$, exact raw counts give $$(\alpha_9(36),N_9(36))=(16,24),\qquad
 (\alpha_9(900),N_9(900))=(384,576),$$ and therefore $$M_9(36)=M_9(900)=\frac{2K_1}{3}.$$ The first clock does not yet contain $p_0(9)^2=25$, so this fixture is outside the recurrence's qualified base domain. It nevertheless rules out any blanket claim of strict gain at every square-support prime step. Proposition [\[prop:fresh-recurrence\]](#prop:fresh-recurrence){reference-type="ref" reference="prop:fresh-recurrence"}, rather than stepwise strictness, is the exact statement.

[\[lem:CRT-two-run\]]{#lem:CRT-two-run label="lem:CRT-two-run"} Every finite support containing $p_0(h)$ has a finite extension whose positive graph contains an exact run of length two.

Enlarge the support, if necessary, until it contains two distinct primes $a,b$ with $a\nmid d$ and $b\nmid d$. Seek a starting phase $r$ whose interior phases $r,r+d$ are positive and whose endpoints $r-d,r+2d$ are zero. Impose $$r\equiv d\pmod{a^2},\qquad
 r\equiv-2d\pmod{b^2}.$$ The left endpoint is then divisible by $a^2$, and the right endpoint is divisible by $b^2$. Since neither prime divides $d$, the two interior phases are nonzero modulo both prime squares. At every other supported prime $p$, choose a local residue avoiding the two classes $0,-d\pmod{p^2}$; at least two of the $p^2$ classes remain even for $p=2$. The Chinese remainder theorem combines these choices. The resulting $r$ begins an exact positive run of length two.

[\[prop:eventual-strictness\]]{#prop:eventual-strictness label="prop:eventual-strictness"} For every finite $\mathcal P$ containing $p_0(h)$, some finite extension $\mathcal P^\star$ satisfies $$B_{h,\mathcal P^\star}>B_{h,\mathcal P}.$$ Consequently $B_{h,\mathcal P}<B_\infty(h)$ whenever $\mathcal P$ also contains every prime divisor of $d$.

Add generic primes until Lemma [\[lem:CRT-two-run\]](#lem:CRT-two-run){reference-type="ref" reference="lem:CRT-two-run"} applies. Every such addition is nondecreasing by [\[eq:normalized-gain\]](#eq:normalized-gain){reference-type="eqref" reference="eq:normalized-gain"}. The extended graph now has an even run, so adjoining one further fresh prime is strict, again by [\[eq:normalized-gain\]](#eq:normalized-gain){reference-type="eqref" reference="eq:normalized-gain"}. This proves the first assertion.

For the second, extend $\mathcal P$ through the missing primes in increasing order. Since all prime divisors of $d$ were already included, every newly added prime is coprime to $d$, so the recurrence applies at every step. The values are nondecreasing, some future step is strict, and Proposition [\[prop:cofinal\]](#prop:cofinal){reference-type="ref" reference="prop:cofinal"} identifies their limit as $B_\infty(h)$. Hence the starting value is strictly below that limit.

First let $\mathcal P_y$ be a cofinal prime-initial family containing $p_0(h)$. Proposition [\[prop:finite-endpoint\]](#prop:finite-endpoint){reference-type="ref" reference="prop:finite-endpoint"} and [\[eq:cofinal-limit\]](#eq:cofinal-limit){reference-type="eqref" reference="eq:cofinal-limit"} give $$C_h(q_{\mathcal P_y})=B_{h,\mathcal P_y}
 \longrightarrow B_\infty(h).$$ Therefore $\sup_q C_h(q)\geq B_\infty(h)$.

For the strict upper bound, fix an arbitrary finite $q$. Choose a finite prime set $\mathcal P$ containing $p_0(h)$, every prime divisor of $q$, and every prime divisor of $d$. Set $$Q=\operatorname{lcm}(q,q_{\mathcal P}).$$ Then $q\mid Q$, $q_{\mathcal P}\mid Q$, and $\operatorname{rad}(Q)=\operatorname{rad}(q_{\mathcal P})$. Lemma [\[lem:clock-divisibility\]](#lem:clock-divisibility){reference-type="ref" reference="lem:clock-divisibility"}, Proposition [\[prop:same-support\]](#prop:same-support){reference-type="ref" reference="prop:same-support"}, and Proposition [\[prop:eventual-strictness\]](#prop:eventual-strictness){reference-type="ref" reference="prop:eventual-strictness"} give $$C_h(q)\leq C_h(Q)=M_h(q_{\mathcal P})
 =B_{h,\mathcal P}<B_\infty(h).$$ This proves strict nonattainment at every finite clock and the reverse supremum inequality. At no point is $q$ allowed to depend on $X$; the scalar supremum is taken only after all fixed-table limits and finite maxima.

# The landscape across fixed lags

[\[lem:isolated-positive\]]{#lem:isolated-positive label="lem:isolated-positive"} For every fixed $h\geq1$, $$R_{1,h}>0.$$

Choose distinct primes $a,b$ with $a\nmid d$ and $b\nmid d$. The Chinese remainder theorem gives one residue class modulo $a^2b^2$ satisfying $$r\equiv d\pmod{a^2},\qquad
 r\equiv-d\pmod{b^2}.
 \label{eq:isolated-congruences}$$ Every integer in this class has $a^2\mid r-d$ and $b^2\mid r+d$. Moreover, its center is nonzero modulo both $a^2$ and $b^2$, because neither prime divides $d$. Among these integers, impose for each remaining prime $p$ the local avoidance $r\not\equiv0\pmod{p^2}$. Finite CRT counts followed by the elementary square-divisor tail give this subevent the density $$\frac1{a^2b^2}
 \prod_{p\ne a,b}\left(1-\frac1{p^2}\right)>0.$$ Here the product is positive because $\sum_p p^{-2}<\infty$. On the subevent, the center $r$ is squarefree while the two step-$d$ neighbors $r-d$ and $r+d$ are not. It is therefore contained in the exact bracketed length-one event whose density is $R_{1,h}$.

[\[lem:outside-prime-tail\]]{#lem:outside-prime-tail label="lem:outside-prime-tail"} For every integer $Y\geq2$, put $$d_Y=\prod_{\substack{p\leq Y\\p\ {\rm prime}}}p^2,
 \qquad h_Y=\frac{d_Y}{2}.
 \label{eq:hY}$$ Then $h_Y$ is a positive integer and $$0\leq B_\infty(h_Y)-\frac3{\pi^2}
 \leq\frac12\sum_{p>Y}\frac1{p^2}
 <\frac1{2(Y-1)}.
 \label{eq:outside-tail}$$

The factor $2^2$ occurs in $d_Y$, so $h_Y$ is integral and $2h_Y=d_Y$. Exact positive runs in step-$d_Y$ coordinates partition the run-start event $$\{r:\ r\text{ is squarefree and }r-d_Y\text{ is not squarefree}\}.$$ All runs are finite: the first prime not dividing $d_Y$ supplies the run-length cutoff proved above. Consequently the density of this event is $$\sum_{\ell\geq1}R_{\ell,h_Y}.
 \label{eq:all-run-starts}$$ If $p\leq Y$ and $p^2\mid r-d_Y$, then $p^2\mid d_Y$ forces $p^2\mid r$, contrary to the center being squarefree. Every boundary in [\[eq:all-run-starts\]](#eq:all-run-starts){reference-type="eqref" reference="eq:all-run-starts"} must therefore be supplied by a prime $p>Y$. The union bound and the density $p^{-2}$ of one square divisibility class give $$\sum_{\ell\geq1}R_{\ell,h_Y}
 \leq\sum_{p>Y}\frac1{p^2}.$$ The endpoint bonus uses only odd runs, so nonnegativity of all the $R_{\ell,h_Y}$ and [\[eq:Binfinity\]](#eq:Binfinity){reference-type="eqref" reference="eq:Binfinity"} prove the first inequality in [\[eq:outside-tail\]](#eq:outside-tail){reference-type="eqref" reference="eq:outside-tail"}. Finally, $\sum_{p>Y}p^{-2}\leq\sum_{n>Y}n^{-2}<1/(Y-1)$, which proves the displayed strict bound.

All run densities in [\[eq:Binfinity\]](#eq:Binfinity){reference-type="eqref" reference="eq:Binfinity"} are nonnegative, so $B_\infty(h)\geq3/\pi^2$. Lemma [\[lem:isolated-positive\]](#lem:isolated-positive){reference-type="ref" reference="lem:isolated-positive"} puts the strictly positive term $R_{1,h}/2$ into the endpoint for every fixed $h$, because $1<p_0(h)^2$. Hence equality is impossible at any fixed lag.

On the other hand, Lemma [\[lem:outside-prime-tail\]](#lem:outside-prime-tail){reference-type="ref" reference="lem:outside-prime-tail"} supplies a sequence of individually fixed integer lags $h_Y$ for which the endpoint bonus tends to zero. Thus values approach $3/\pi^2$ from above, proving [\[eq:lag-infimum\]](#eq:lag-infimum){reference-type="eqref" reference="eq:lag-infimum"} and nonattainment. This argument compares scalar endpoints only after their fixed-lag limits; it provides neither a varying-lag terminal limit nor an ordering of endpoints by lag.

# Source roles, reproducibility, and limitations

## Analytic and combinatorial provenance

The sole analytic input is the complete three-shift terminal-log law of RH-394, frozen at repository commit `6b3d616851cd2d7cba66371d0aa9f25b8e8bf2f7` [@RH394]. Section 2 uses precisely its fixed-shift density, phase-average, mass, and terminal-clock conclusions. The present paper supplies every subsequent safety, tropical, square-clock, run-density, strictness, and lag-landscape argument.

RH-395, frozen at commit `20de7202518f4488cbd9c7d63bf94aaa3dc94476`, is cited only as the $h=1$ finite relation-saturation and tropical-optimizer precedent [@RH395]. RH-375, frozen at commit `071fed1b2a5d8488b9d2e35a99a753953b233584`, is cited only as the finite one-site MWIS and square-clock template [@RH375]. Neither provides an analytic terminal-clock input here. The Tao two-point and Tao--Teräväinen odd-correlation papers are inherited provenance through RH-394 [@Tao2016LogChowla; @TaoTeravainen2019]; the Johnston--Yang and Maynard records likewise remain inherited source-closure objects only. No new conclusion in this paper is attributed directly to those four remote records.

## Finite reproduction and source integrity

The companion certificate is an exact finite reproduction artifact, not an analytic proof. Its frozen canonical JSON has $96$ rows, $83{,}309$ bytes, and SHA-256 `7cc0da78ee7e47a22b357d7e8d907bc9d9879caeb82ede30709e8cb1023032ba`. The strict validator rejects all $32$ named single-core mutations. Among its checks, the exhaustive full-eight relation oracle scans $262{,}144$ ordered relation pairs and finds exactly $3{,}375$ universally safe pairs. These checks reproduce finite identities and counterexamples used above; they do not replace the proofs.

The frozen source closure contains $160$ immutable Git objects and four inherited remote records, hence $164$ logical objects. Its canonical SHA-256 is `c16456d58efd74edf1505c430a54459e359b5ba7e1e581773e9a0613b493385b`; the all-Git and logical-source digests are, respectively, `472bf5ce5e352dce0d3a44ad10b22345b98e0e8b9a0cd745be9ecd93dedf0a86` and `72040ab3d7a5d98ce308b91d0748d52a8d4886cf245f5079f14c69ee659cc287`. Reproduction is offline: the release records zero network requests, vendors no external PDF payload, and records no forbidden payload-hash hit. The four remote redistribution flags are $(\mathrm{no},\mathrm{no},\mathrm{yes},\mathrm{no})$; the corresponding PDFs are not redistributed.

## Claim firewall

Every analytic assertion fixes $h$, $q$, and the complete phase table before $X\to\infty$, and it holds for every terminal clock in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. The order is: terminal limit for each fixed table, finite safe maximum, and only then the scalar supremum over finite clocks. The result is not an ordinary Cesàro-average theorem and contains no regime with $h=h(X)$, $q=q(X)$, or growing phase tables; no uniform rate in these parameters is asserted.

The centered rule reads $\mu(n+h)$, so it is not causal or online. The proof concerns exactly three shifts and safety at the single separation $2h$; it does not establish an even four-shift law, a larger-window compiler, or a generic graph theorem. Nothing here is an analytic trace or operator formula, a statement about zeta zeros or the Riemann hypothesis, or a discharge of downstream Gates A--E. Finally, the lag argument proves only the infimum and its nonattainment. It makes no assertion about a supremum, a maximum, or monotonicity in $h$.

# Declarations {#declarations .unnumbered}

**Data availability.** The finite certificate, exact result and schema, source-lock metadata, and offline verification code are included in the accompanying RH-396 package. No new empirical data were generated and no external source PDF is redistributed.

**Ethics declaration.** This mathematical study involved no human participants, animals, personal data, or sensitive datasets; institutional ethics approval was not applicable.

**Author contributions (CRediT).** The RH research program performed conceptualization, formal analysis, methodology, software, validation, and writing (original draft, review, and editing).

**Conflict of interest.** The author declares no conflict of interest.

**Funding.** No external funding was received for this work.

**AI-use statement.** AI-assisted tools supported drafting, finite-certificate implementation, formatting, and consistency checks. The research program directed and reviewed the mathematical arguments, source roles, and release artifacts and retains responsibility for the content.
