---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-398-exact-lag-endpoint-maximum-and-maximizers"
canonical_tex: "zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/main.pdf"
source_sha256: "96aa193b9fe66b613cf3ba95807e17c02b10e244e1d4a76bdbc5544e4337bdbf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Lag Endpoint Maximum and Maximizers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the fixed-lag centered Möbius capacity of RH-396, let $B_\infty(h)$ be the nonattained endpoint over finite declared phase clocks at a fixed positive integer lag $h$. We determine its exact maximum across fixed lags. Put $d=2h$, let $p_0(h)$ be the least prime not dividing $d$, and set $$t_p(d)=\frac{p^2}{\gcd(d,p^2)},\qquad
   A_m(d)=\prod_p\left(1-\frac{\min(m,t_p(d))}{p^2}\right).$$ The RH-396 Euler--run formula telescopes to $$B_\infty(h)=\sum_{m=1}^{p_0(h)^2-1}(-1)^{m+1}A_m(d).$$ A finite-prime CRT transfer compares the three local valuation levels at each prime. After a common cofinal passage it gives $$\begin{aligned}
   \max_{h\geq1}B_\infty(h)&=B_\infty(1),\\
   B_\infty(h)=B_\infty(1)
   &\Longleftrightarrow
   \mu^2(h)=1\ \text{and}\ \gcd(h,210)=1.\end{aligned}$$ On the complement of this equality class the same value is a supremum but is not attained; the fixed lags $h=p^2$, for primes $p\geq11$, approach it with gap in $(0,p^{-2}]$. If $p_0(h)\geq5$, the gap from the maximum is larger than $2/1334025$. Consequently $\sup_{h\geq1,\,q<\infty}C_h(q)=B_\infty(1)$, with no finite pair attaining it. The previously established infimum $3/\pi^2$ remains unattained. Every analytic limit is a fixed-data terminal logarithmic limit; the finite CRT phase space used in the comparison is bookkeeping, not a random-Möbius model.
author:
- Prime Dynamics Theory Project
bibliography:
- references.bib
date: 'August 13, 2026'
title: Exact Lag Endpoint Maximum and Maximizers
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; fixed lag; squarefree run; Euler product; exact maximizer; nonattainment.

# Fixed-data interface and main results

We first reproduce the interface whose endpoint will be compared. Write $\mathcal T=\{-1,0,+1\}$, and extend the Möbius function by $\mu_0(k)=\mu(k)$ for $k\geq1$ and $\mu_0(k)=0$ for $k\leq0$. An admissible terminal clock satisfies $$1\leq\omega(X)\leq X,
 \qquad \omega(X)\longrightarrow\infty.
 \label{eq:terminal-clock}$$ Fix $h,q\geq1$, the function $\omega$, and an entire family of phase tables $$F_r:\mathcal T^3\longrightarrow\{-1,+1\},\qquad r\in\mathbb Z/q\mathbb Z,$$ before $X\to\infty$. Put $d=2h$. The centered output and scored terminal functional are $$\begin{aligned}
 \varepsilon_F(n)
 &=F_{n\bmod q}\bigl(\mu_0(n-h),\mu(n),\mu(n+h)\bigr),
 \label{eq:centered-output}\\
 L_{h,q,X}(F)
 &=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}\frac{\mu(n)\varepsilon_F(n)}n.
 \label{eq:terminal-functional}\end{aligned}$$ The table is universally distance-$d$ safe when $$\neg\bigl(F_r(a,b,c)=+1\ \text{and}\
 F_{r+d}(c,e,f)=+1\bigr)
 \label{eq:distance-safety}$$ for every $r\in\mathbb Z/q\mathbb Z$ and every $a,b,c,e,f\in\mathcal T$. RH-396 proves that the limit $L_{h,q}(F)=\lim_{X\to\infty}L_{h,q,X}(F)$ exists and is independent of the admissible clock. Only after all fixed-table limits are formed does one take the finite maximum $$C_h(q)=\max_{F\ \mathrm{universally\ distance}\text{-}d\ \mathrm{safe}}
 |L_{h,q}(F)|.
 \label{eq:capacity}$$ Thus $q$ is a finite declared phase clock and $\omega$ is a terminal clock; neither is an endpoint cutoff or an orientation variable.

For a finite set $J\subset\mathbb Z$, define $$D_h(J)=\prod_p\left(
 1-\frac{|\{dj\bmod p^2:j\in J\}|}{p^2}\right).
 \label{eq:Dh}$$ For $\ell\geq1$, put $$\begin{aligned}
 R_{\ell,h}
 &=D_h([0,\ell-1])-D_h(\{-1\}\cup[0,\ell-1])
 \notag\\
 &\quad-D_h([0,\ell])+D_h([-1,\ell]).
 \label{eq:R-def}\end{aligned}$$ This is the density of an exact bracketed positive step-$d$ run, so it is nonnegative. If $$p_0(h)=\min\{p\text{ prime}:p\nmid d\},
 \label{eq:p0}$$ RH-396 defines $$B_\infty(h)=\frac3{\pi^2}
 +\frac12\sum_{\substack{1\leq\ell<p_0(h)^2\\\ell\ \mathrm{odd}}}
 R_{\ell,h}.
 \label{eq:B-run}$$ Its endpoint theorem and lag-infimum corollary are $$\sup_{q<\infty}C_h(q)=B_\infty(h),\qquad
 C_h(q)<B_\infty(h)\quad(q<\infty),
 \label{eq:RH396-endpoint}$$ and $$\inf_{h\geq1}B_\infty(h)=\frac3{\pi^2},
 \qquad B_\infty(h)>\frac3{\pi^2}\quad(h\geq1).
 \label{eq:RH396-infimum}$$ These are definitions (18)--(21), Theorem 1.3, equation (22), and Corollary 1.4, equation (23), on PDF page 3 of the frozen RH-396 release [@RH396].

Our new result supplies the upper landscape that RH-396 explicitly left open.

[\[thm:maximum\]]{#thm:maximum label="thm:maximum"} For every fixed positive integer $h$, $$B_\infty(h)\leq B_\infty(1).
 \label{eq:maximum-bound}$$ Equality holds exactly when $$\mu^2(h)=1\qquad\text{and}\qquad\gcd(h,210)=1.
 \label{eq:maximizer-criterion}$$ In particular, $\max_{h\geq1}B_\infty(h)=B_\infty(1)$, and the maximum is attained at infinitely many fixed lags.

[\[thm:complement\]]{#thm:complement label="thm:complement"} Let $\mathcal N$ be the complement in $\mathbb Z_{\geq1}$ of the set in [\[eq:maximizer-criterion\]](#eq:maximizer-criterion){reference-type="eqref" reference="eq:maximizer-criterion"}. Then $$\sup_{h\in\mathcal N}B_\infty(h)=B_\infty(1),$$ and the supremum is not attained on $\mathcal N$. For every prime $p\geq11$, $$0<B_\infty(1)-B_\infty(p^2)\leq\frac1{p^2}.
 \label{eq:prime-square-gap}$$ If $p_0(h)\geq5$, then $$B_\infty(1)-B_\infty(h)\geq B_\infty(1)-B_\infty(3)
 >\frac1{36750}>\frac2{1334025}.
 \label{eq:p0-gap}$$

[\[cor:joint\]]{#cor:joint label="cor:joint"} One has $$\sup_{\substack{h\geq1\\q<\infty}}C_h(q)=B_\infty(1),
 \label{eq:joint-supremum}$$ and no finite pair $(h,q)$ attains this value. The lower endpoint [\[eq:RH396-infimum\]](#eq:RH396-infimum){reference-type="eqref" reference="eq:RH396-infimum"} remains an unattained infimum.

# Product and telescope

Put $$t_p(d)=\frac{p^2}{\gcd(d,p^2)},\qquad
 A_m(d)=D_h([0,m-1])
 =\prod_p\left(1-\frac{\min(m,t_p(d))}{p^2}\right).
 \label{eq:A-product}$$ The first equality in the product follows because the step $d$ has orbit length $t_p(d)$ modulo $p^2$. Translation of the four sets in [\[eq:R-def\]](#eq:R-def){reference-type="eqref" reference="eq:R-def"} gives $$R_{\ell,h}=A_\ell(d)-2A_{\ell+1}(d)+A_{\ell+2}(d).
 \label{eq:R-second-difference}$$ Since $p_0\nmid d$, the $p_0$-orbit has length $p_0^2$. Consequently $$A_m(d)=0\qquad(m\geq p_0^2).
 \label{eq:A-cutoff}$$

[\[prop:telescope\]]{#prop:telescope label="prop:telescope"} For every fixed $h\geq1$, $$\boxed{\displaystyle
 B_\infty(h)=\sum_{m=1}^{p_0(h)^2-1}(-1)^{m+1}A_m(2h).}
 \label{eq:B-alternating}$$ This is the density, in the square-divisibility phase space, that the positive forward step-$d$ run beginning at a uniformly selected phase has odd length.

The singleton density is $A_1=\prod_p(1-p^{-2})=6/\pi^2$, so the first term of [\[eq:B-run\]](#eq:B-run){reference-type="eqref" reference="eq:B-run"} is $A_1/2$. Write $T=p_0^2$, which is odd. Substituting [\[eq:R-second-difference\]](#eq:R-second-difference){reference-type="eqref" reference="eq:R-second-difference"} into [\[eq:B-run\]](#eq:B-run){reference-type="eqref" reference="eq:B-run"} and collecting terms gives $$\frac{A_1}{2}
 +\frac12\sum_{\substack{1\leq\ell\leq T-2\\\ell\ \mathrm{odd}}}
 (A_\ell-2A_{\ell+1}+A_{\ell+2})
 =A_1-A_2+A_3-\cdots-A_{T-1}+\frac{A_T}{2}.$$ The last term vanishes by [\[eq:A-cutoff\]](#eq:A-cutoff){reference-type="eqref" reference="eq:A-cutoff"}, proving [\[eq:B-alternating\]](#eq:B-alternating){reference-type="eqref" reference="eq:B-alternating"}.

For the event interpretation, first restrict to any finite prime set containing $p_0$. A phase is positive at index $j$ if none of those prime squares divides the corresponding residue plus $dj$. The probability that its first $m$ indices are positive is the finite version of $A_m$. If $L$ denotes the forward positive-run length, then $$\Pr(L\text{ is odd})
 =\sum_{m\geq1}(-1)^{m+1}\Pr(L\geq m).$$ The reset prime $p_0$ forces $L<T$, so the sum is finite. Finite CRT counting followed by the square-divisor union bound gives the infinite product in [\[eq:A-product\]](#eq:A-product){reference-type="eqref" reference="eq:A-product"}. This auxiliary phase probability is not an independence assertion about values of the Möbius function.

# Finite CRT transfer

The comparison of two lags is made at finite prime support and only then passed to a common cofinal limit. For a finite set $\mathcal P$ of primes, let $$\Omega_{\mathcal P}=\prod_{p\in\mathcal P}\mathbb Z/p^2\mathbb Z$$ with uniform counting measure. For $u=(u_p)$, declare the index $j$ positive when $u_p+dj\not\equiv0\pmod{p^2}$ for every $p\in\mathcal P$. Multiplication by the unit part of $d$ is a bijection in each local coordinate. Hence the law depends only on $$e_p(d)=\min(v_p(d),2),\qquad
 t_p(d)=p^{2-e_p(d)}\in\{p^2,p,1\}.
 \label{eq:local-level}$$

Delete one prime coordinate $p$ temporarily. A positive component in the remaining binary cycle is a finite path $P_L$. Its maximum independent-set cardinality, equivalently the number of starting positions with an odd remaining forward run, is $$\alpha(L)=\left\lceil\frac L2\right\rceil.
 \label{eq:alpha}$$ At square support, RH-396 identifies the finite endpoint with this total MWIS cardinality, normalized by the number of positive vertices and multiplied by $K_1=6/\pi^2$. The positive-vertex density $K_1$ is independent of $d$. Thus the expected sums of $\alpha(L)$ below all have the same positive normalization and compare the endpoint in the same direction. For an integer period $T\geq1$, define the total deletion loss $$\Lambda_T(L)=T\alpha(L)-
 \sum_{r=0}^{T-1}
 \alpha\bigl(P_L\setminus\{j:j\equiv r\pmod T\}\bigr),
 \label{eq:Lambda-definition}$$ where $\alpha$ is summed over the path components remaining after deletion.

[\[lem:Lambda\]]{#lem:Lambda label="lem:Lambda"} The loss in [\[eq:Lambda-definition\]](#eq:Lambda-definition){reference-type="eqref" reference="eq:Lambda-definition"} is $$\begin{array}{c|c|c}
 &L\text{ odd}&L\text{ even}\\ \hline
T\text{ odd}&
 \alpha(L)&
 \max\{0,L/2-(T-1)/2\}\\[2pt]
T\text{ even}&
 \min\{\alpha(L),T/2\}&0.
\end{array}
\label{eq:Lambda-branches}$$ The formulas include $T=1,2$ and the thresholds $L<T$, $L=T$, and $L>T$.

Number the vertices $1,\ldots,L$. Let $f\in\{1,\ldots,T\}$ be the first possible deleted vertex for a residue class. If $f>L$, no vertex is deleted and the resulting value is $\alpha(L)$. If $f\leq L$, put $$n_f=1+\left\lfloor\frac{L-f}{T}\right\rfloor,
 \qquad b_f=L-f-(n_f-1)T,
 \qquad 0\leq b_f<T.$$ The surviving component lengths are exactly $$f-1,\quad
 \underbrace{T-1,\ldots,T-1}_{n_f-1\ \mathrm{times}},\quad b_f.$$ Consequently, with $\beta_f=\alpha(L)$ for $f>L$, $$\beta_f=
 \left\lceil\frac{f-1}{2}\right\rceil
 +(n_f-1)\left\lceil\frac{T-1}{2}\right\rceil
 +\left\lceil\frac{b_f}{2}\right\rceil,
 \qquad
 \Lambda_T(L)=\sum_{f=1}^{T}\bigl(\alpha(L)-\beta_f\bigr).
 \label{eq:Lambda-count}$$ Write $L=kT+s$, $0\leq s<T$, and split the sum at $f=s$, with the evident empty part when $k=0$. Substitution in [\[eq:Lambda-count\]](#eq:Lambda-count){reference-type="eqref" reference="eq:Lambda-count"}, using $$\sum_{j=0}^{n-1}\left\lceil\frac j2\right\rceil
 =\left\lfloor\frac{n^2}{4}\right\rfloor,$$ gives, for odd $T$, $$\Lambda_T(L)=
 \begin{cases}
  \alpha(L),&L\text{ odd},\\
  \max\{0,L/2-(T-1)/2\},&L\text{ even},
 \end{cases}$$ and, for even $T$, $$\Lambda_T(L)=
 \begin{cases}
  \min\{\alpha(L),T/2\},&L\text{ odd},\\
  0,&L\text{ even}.
 \end{cases}$$ This proves all four branches, including $T=1,2$ and the cases $L<T,L=T,L>T$.

For a prime $p$ at local level $e\in\{0,1,2\}$, averaging its phase over $\mathbb Z/p^2\mathbb Z$ changes the contribution of a base path to $$V_{p,e}(L)=\alpha(L)-
 \frac{\Lambda_{p^{2-e}}(L)}{p^2}.
 \label{eq:local-V}$$ Indeed, $p^2-p^{2-e}$ phases delete no vertex of the orbit, while the remaining $p^{2-e}$ phases realize once each of the residue deletions in [\[eq:Lambda-definition\]](#eq:Lambda-definition){reference-type="eqref" reference="eq:Lambda-definition"}.

[\[lem:local-order\]]{#lem:local-order label="lem:local-order"} For every odd prime $p$, $$V_{p,0}(L)\geq V_{p,1}(L)\geq V_{p,2}(L).
 \label{eq:odd-local-order}$$ The three quantities are equal for odd $L$. For even $L<p$, $V_{p,0}=V_{p,1}$, while the first strict $0$-to-$1$ comparison occurs at $L=p+1$, with loss $p^{-2}$. The $1$-to-$2$ comparison is strict for every even $L$. At $p=2$, the identity $d=2h$ permits only levels $1$ and $2$, and $$V_{2,1}(L)\geq V_{2,2}(L),
 \qquad V_{2,1}(2)-V_{2,2}(2)=\frac14.$$

For odd $p$, all three periods $p^2,p,1$ are odd. Insert their values in the odd-$T$ rows of [\[eq:Lambda-branches\]](#eq:Lambda-branches){reference-type="eqref" reference="eq:Lambda-branches"}. For odd $L$, all three losses equal $\alpha(L)$. For even $L$, the loss is nondecreasing as the period falls from $p^2$ to $p$ to $1$, which proves [\[eq:odd-local-order\]](#eq:odd-local-order){reference-type="eqref" reference="eq:odd-local-order"}. When $L<p$, both of the first two losses vanish; at $L=p+1$, they are zero and one. The period-one loss is $\alpha(L)=L/2$, strictly exceeding the period-$p$ loss for even $L$. At $p=2$, use the even-period row for $T=2$ and the odd-period row for $T=1$. Level zero would require $2\nmid d$ and is therefore counterfactual; it is never used.

[\[prop:transfer\]]{#prop:transfer label="prop:transfer"} Fix all local coordinates except a prime $p$, and suppose a reset prime other than $p$ makes every positive component a path. Increasing the local level $e_p$ weakly decreases the finite endpoint. Strict local loss on any positive-density exact-run cylinder makes the decrease strict. The comparison survives along one common prime-initial cofinal family.

Condition on the other finite coordinates and decompose their positive cycle into paths. The endpoint numerator is the sum of $\alpha(L)$ over those paths. Averaging the $p$-coordinate replaces each summand by $V_{p,e_p}(L)$. The inequalities in [\[lem:local-order\]](#lem:local-order){reference-type="ref" reference="lem:local-order"} may therefore be summed path by path. This proves the finite comparison.

For strictness, fix an exact path of a length at which the relevant local inequality is strict. Supply its two zero boundaries by two auxiliary prime squares, and require its interior to avoid every other square class. Finite CRT gives a nonempty cylinder. After the finitely many small coordinates are fixed, its remaining density contains a tail $\prod_{r>Y}(1-L/r^2)>0$. Thus the strict loss has positive density.

Finally take the same increasing prime-initial supports on both sides. For each fixed finite set of path indices, the omitted square-divisor density is at most a fixed multiple of $\sum_{r>Y}r^{-2}$, which tends to zero. Hence the finite inequalities pass to the products $D_h$, the run densities, and the finite telescope [\[eq:B-alternating\]](#eq:B-alternating){reference-type="eqref" reference="eq:B-alternating"}. No infinite-prime random mask and no varying-lag terminal limit is introduced.

# Maximum and equality cases

For the base lag $h=1$, the local level is $1$ at $p=2$ and $0$ at every odd prime. For an arbitrary $h$, every local level is at least this canonical level. Fix the reset prime $s=p_0(h)$. Every coordinate that must be changed is $2$ or a prime divisor of $h$, so it is different from $s$; moreover $e_s=0$ at both endpoints of every comparison. Include $s$ in every common prime-initial support. It then cuts all positive components into paths throughout the transfer sequence. Applying [\[prop:transfer\]](#prop:transfer){reference-type="ref" reference="prop:transfer"} one prime at a time and passing along that common cofinal support proves $B_\infty(h)\leq B_\infty(1)$. It remains to determine exactly when all transfers are invisible.

[\[lem:strict-witnesses\]]{#lem:strict-witnesses label="lem:strict-witnesses"} Every lag outside [\[eq:maximizer-criterion\]](#eq:maximizer-criterion){reference-type="eqref" reference="eq:maximizer-criterion"} has one of the following strict local witnesses.

  defect                                 prime   exact path length   local loss
  -------------------------------------- ------- ------------------- ------------
  $2\mid h$, equivalently $4\mid d$      $2$     $2$                 $1/4$
  odd $p^2\mid h$                        $p$     $2$                 positive
  $3\mid h$ after squarefree reduction   $3$     $4$                 $1/9$
  $5\mid h$ after squarefree reduction   $5$     $6$                 $1/25$
  $7\mid h$ after squarefree reduction   $7$     $8$                 $1/49$

Each witness occurs on a positive-density exact-run cylinder after all other local transfers have been made.

The losses are the special cases of [\[lem:local-order\]](#lem:local-order){reference-type="ref" reference="lem:local-order"}. For an odd square factor, level $0$ is replaced by level $2$, and the length-two loss is positive. For a single factor $p=3,5,7$, the first strict level $0$-to-$1$ length is $p+1$.

Order all nonwitness transfers first and the displayed witness last. For each witness of length $L$, choose two fresh auxiliary primes $a,b\nmid 2hp$ with $a,b>L+1$. Their step-$d$ orbit lengths are $a^2,b^2>L+1$. Use the $a^2$-coordinate to force a zero at the left boundary and the $b^2$-coordinate to force a zero at the right boundary; neither class can repeat in the $L$-site interior. CRT chooses these two boundary classes and avoids all interior classes at the remaining finitely many primes. The outside-prime product is positive because $\sum_p p^{-2}<\infty$. Hence the strict finite loss cannot disappear in the cofinal limit.

[\[lem:invisibility\]]{#lem:invisibility label="lem:invisibility"} If $h$ is squarefree and $\gcd(h,210)=1$, then $B_\infty(h)=B_\infty(1)$.

Now $p_0(h)=3$, so every positive run has length at most eight. Every odd prime divisor of $h$ is at least eleven and occurs once, changing its local level from $0$ to $1$. For odd path lengths the two levels are equal; for even $L\leq8<p$, they are again equal by [\[lem:local-order\]](#lem:local-order){reference-type="ref" reference="lem:local-order"}. Thus every such transfer is invisible on every possible path. There are only finitely many prime divisors, so the finite endpoints and then their common cofinal limits agree exactly.

The local transfer order proves the upper bound. The forward implication in the equality statement is the contrapositive of [\[lem:strict-witnesses\]](#lem:strict-witnesses){reference-type="ref" reference="lem:strict-witnesses"}; the reverse implication is [\[lem:invisibility\]](#lem:invisibility){reference-type="ref" reference="lem:invisibility"}. The connector in [\[eq:maximizer-criterion\]](#eq:maximizer-criterion){reference-type="eqref" reference="eq:maximizer-criterion"} is therefore "and", and $210=2\cdot3\cdot5\cdot7$. The equality class is infinite, for example it contains $1,11,13,143$, and $187$.

# Complement and the uniform gap

Let $p\geq11$ be prime and take $h=p^2$. The reset prime is still three, so only path lengths $1,\ldots,8$ occur. Relative to $h=1$, only the $p$-coordinate changes, from level $0$ to level $2$. Odd path lengths have zero loss. At even length $L$, the loss is $\alpha(L)/p^2$ in the phase average. On a finite common support $\mathcal P_Y$, remove the $p$-coordinate, let $N_Y$ be the number of positive vertices in one period of the remaining graph, and define $$\rho_{L,Y}=\frac1{N_Y}
 \#\{\text{positive path components of length }L\}.$$ The count is taken over the complete CRT period, so it already averages all remaining phase coordinates. Exact-run densities and the square-divisor tail show that $\rho_{L,Y}$ has a common cofinal limit $\rho_L$. Summing the local loss over all $p^2$ phases removes the factor $p^{-2}$; the full positive-vertex count gains the common factor $p^2-1$. The square-clock normalization therefore gives $$0<B_\infty(1)-B_\infty(p^2)
 =\frac{K_1}{p^2-1}
 \sum_{\substack{2\leq L\leq8\\L\ \mathrm{even}}}
 \rho_L\alpha(L)
 \leq\frac1{p^2}.$$ The normalization is by component count, not by the density of vertices lying inside a component. In particular, $$\sum_L\rho_L\alpha(L)\leq
 \sum_L\rho_LL\leq1,$$ because the positive path components are disjoint. Strictness follows from the length-two cylinder in [\[lem:strict-witnesses\]](#lem:strict-witnesses){reference-type="ref" reference="lem:strict-witnesses"}. The last displayed upper bound also uses $K_1=6/\pi^2<2/3$, hence $K_1/(p^2-1)<1/p^2$ for $p\geq11$. Each $p^2$ is an individually fixed lag; only after its endpoint has been formed do we let the external scalar prime parameter tend to infinity. This proves [\[eq:prime-square-gap\]](#eq:prime-square-gap){reference-type="eqref" reference="eq:prime-square-gap"}, the complementary supremum, and its nonattainment by [\[thm:maximum\]](#thm:maximum){reference-type="ref" reference="thm:maximum"}.

[\[lem:uniform-gap\]]{#lem:uniform-gap label="lem:uniform-gap"} If $p_0(h)\geq5$, then [\[eq:p0-gap\]](#eq:p0-gap){reference-type="eqref" reference="eq:p0-gap"} holds.

The hypothesis says $3\mid d$, equivalently $3\mid h$. At every odd prime other than $3$, reduce the local level all the way to the canonical level zero, using the two steps $2\to1\to0$ when necessary. At $2$, reduce to the canonical level one and use only the permitted comparison $V_{2,1}\geq V_{2,2}$. At $3$, reduce level two to the level one of the lag $h=3$ when necessary, using $V_{3,1}\geq V_{3,2}$. The local transfer order gives $$B_\infty(h)\leq B_\infty(3).$$

To compare $h=1$ and $h=3$, leave the $3$-coordinate until last and force an exact base path of length four in the other coordinates. Choose the inactive $2$-coset with factor $1/2$, the left boundary from a class modulo $5^2$, and the right boundary from a class modulo $7^2$. At every prime $r\geq11$, avoid the four interior classes. The resulting cylinder has density larger than $$\frac12\cdot\frac1{25}\cdot\frac1{49}
 \prod_{r\geq11}\left(1-\frac4{r^2}\right)
 >\frac12\cdot\frac1{25}\cdot\frac1{49}\cdot\frac35
 =\frac3{12250}.$$ Here $\prod_{r\geq11}(1-4/r^2)>1-4\sum_{n\geq11}n^{-2}>3/5$. The final level $0$-to-$1$ transfer at $p=3$ has local loss $1/9$. Therefore $$B_\infty(1)-B_\infty(h)\geq B_\infty(1)-B_\infty(3)
 >\frac3{12250}\cdot\frac19
 =\frac1{36750}>\frac2{1334025},$$ which is the claimed chain.

The two parts of [\[thm:complement\]](#thm:complement){reference-type="ref" reference="thm:complement"} have now been proved.

# Joint finite-clock endpoint

For each fixed $h$ and each finite declared phase clock $q$, RH-396 gives the strict pointwise inequality $$C_h(q)<B_\infty(h)\leq B_\infty(1).$$ Hence every finite pair lies strictly below $B_\infty(1)$. Conversely, the cofinal square clocks constructed in RH-396 at the single fixed lag $h=1$ have capacities tending to $B_\infty(1)$. This proves [\[eq:joint-supremum\]](#eq:joint-supremum){reference-type="eqref" reference="eq:joint-supremum"} and rules out finite-pair attainment. The retained infimum and its nonattainment are exactly RH-396 Corollary 1.4, [\[eq:RH396-infimum\]](#eq:RH396-infimum){reference-type="eqref" reference="eq:RH396-infimum"}; we import that theorem rather than replacing its proof by an orientation or random-model argument.

# Exact finite reproduction and source roles

The companion certificate reproduces finite identities and attacks implementation drift; it is not an analytic proof. Its immutable partition contains 72 rows:

  group                     rows
  ----------------------- ------
  deletion-loss formula       12
  local order                 12
  product and telescope       12
  strictness cylinders        12
  maximizers                   8
  complement and gap           8
  joint endpoint               4
  firewalls                    4

The canonical certificate has 36,635 bytes and SHA-256

d47de091a8fe5a134ba4bbf8ac4689f53b54786d45dc3bfc7061c99b46bea741

66 named semantic mutations are rejected. The core has 61,751 bytes and SHA-256

ce728df064b2538e49a1f47de5db0ee7e6eabee3d99283be5dc3eb3c122df9da

The frozen source closure has 184 Git members and four ordered remote logical locks, for 188 logical inputs. Its canonical serialization has 64,997 bytes and SHA-256

5cb3a2f4339ba0b2f11654092496bf7caf255d0d0e7ccf23524355d9f3fa97d7

RH-396 at commit `cd57086fa90939d56656c3f952a08ffad9aabefe` is the sole load-bearing theorem and analytic endpoint input. RH-397 at commit `dd63a109dcfa72365c749e0b183820d2611af733` is the direct release and source-closure predecessor only [@RH397]. Earlier sources and all four remote records are inherited transitively; none pays a fresh claim here.

The pretty result has 187,434 bytes and SHA-256

b22bd32fd515cbe98ee1fc946cef7e695273fdffd002cb5e29281ceba7e263f7

its 44 result mutations are rejected. The exact Draft 2020-12 schema has 961,955 pretty bytes, SHA-256

5852ea6e0718185cd063ec56fd5ace000464f95741a2299e15dcd5405d447e8e

and 4,768 recursively closed nodes; 32 schema mutations are rejected. The four Stage-1 test layers pass 45 tests in both normal and `-OO` modes.

# Limitations and declarations

The order of operations is permanent: $$\begin{aligned}
 \text{fix }h,q,F,\omega
 &\longrightarrow X\to\infty
 \longrightarrow \text{finite safe-table maximum}\\
 &\longrightarrow \sup_{q<\infty}
 \longrightarrow \text{fixed-scalar comparison in }h.\end{aligned}$$ There is no $h=h(X)$, $q=q(X)$, growing or adaptive table, moving order, uniform effective rate, prelimit maximum, or ordinary Cesàro assertion. The centered rule reads $\mu(n+h)$, so it is not causal or online. We prove no four-shift or larger-window law, generic-graph theorem, monotonicity in $h$, operator or trace formula, statement about zeros, Riemann hypothesis, or Gates A--E. The finite CRT probability is exact square-divisibility bookkeeping and must not be read as a stochastic law for Möbius values.

#### Data and code availability.

All deterministic certificate, result, schema, source-lock, and release files belong to the frozen repository package. Verification is offline; no remote PDF is redistributed and no network fetch is required.

#### Ethics.

The work uses no human participants, animals, personal data, or intervention.

#### Author contributions and AI use.

The Prime Dynamics Theory Project directed the research, reconstructed and checked the arguments, assigned source roles, and retains responsibility for all claims. AI-assisted tools supported drafting, finite-certificate implementation, formatting, and consistency checks.

#### Competing interests and funding.

The project declares no competing interests and received no external funding.
