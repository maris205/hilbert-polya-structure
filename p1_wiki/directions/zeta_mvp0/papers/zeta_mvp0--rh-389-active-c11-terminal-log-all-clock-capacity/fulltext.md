---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-389-active-c11-terminal-log-all-clock-capacity"
canonical_tex: "zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/main.pdf"
source_sha256: "6ab94513dfa12067e397b991485e67b76af3ea96ad6eb766fced35a8c7f1edc8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Active-$c_11$ Terminal-Log All-Clock Capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-389-active-c11-terminal-log-all-clock-capacity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a fixed clock $q$, let $(f_r)_{r\bmod q}$ be a universally distance-two-safe family of lag-two tables $f_r:\{-1,0,+1\}^2\to\{-1,+1\}$. We allow the interpolation coefficient $c_{11}(r)$ of the shift-two Möbius correlation to be active. For every $1\le\omega(X)\le X$ with $\omega(X)\to\infty$, we prove the unconditional terminal logarithmic limit $$\frac1{\log\omega(X)}
   \sum_{X/\omega(X)<n\le X}
   \frac{\mu(n)f_{n\bmod q}(\mu_0(n-2),\mu(n))}{n}
   \longrightarrow
   \sum_{r\bmod q}\{c_{02}(r)\delta_{q,r}+c_{22}(r)\vartheta_{q,r}\}.$$ The active $c_{11}$ channel is closed by the fixed determinant-two theorem of TPC-137; the remaining zero and density channels are transferred from ordinary prefixes by an Abel lemma that also covers bounded lower endpoints $X/\omega(X)$.

  We then project all $512$ truth tables pointwise onto eight actions. A finite compatibility rule and an injective predecessor charge give, for every individually fixed $q$, $$G_{\log}(q)=\max_f|L_q(f)|
   =\frac6{\pi^2}-\frac{\kappa_2}{2},
   \qquad \kappa_2=\prod_p\left(1-\frac2{p^2}\right).$$ The constant action $\{-1,0\}$ attains the positive value for every fixed $q$, and input reflection attains its negative. Thus the supremum over all fixed clocks, taken only after the individual limits, has the same value. This does not prove an ordinary Cesàro limit, growing-clock uniformity, or an unbounded-clock maximum-before-limit theorem. A $602$-row exact artifact reproduces the finite algebra and rejects $24$ semantic mutations; it is not the analytic proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 9, 2026'
title: 'Active-$c_{11}$ Terminal-Log All-Clock Capacity'
```

## Markdown 正文

**Keywords:** Möbius function; logarithmically averaged Chowla theorem; active lag-two memory; fixed finite clocks; exact capacity.

# Setting and main theorem

Put $\mu_0(m)=\mu(m)$ for $m\ge1$ and $\mu_0(m)=0$ for $m\le0$. Throughout, every later shifted value $\mu(n-2)$ with $n\le2$ is understood as $\mu_0(n-2)$; for $n>2$ the two notations agree. Fix an integer $q\ge1$. For each $r\in\mathbb Z/q\mathbb Z$, let $$f_r:\{-1,0,+1\}^2\longrightarrow\{-1,+1\},
 \qquad E_r=\{(x,z)\in\{-1,0,+1\}^2:f_r(x,z)=+1\}.$$ The family is *universally distance-two-safe* when no $x,z,w\in\{-1,0,+1\}$ and $r\in\mathbb Z/q\mathbb Z$ satisfy simultaneously $$(x,z)\in E_r,
 \qquad (z,w)\in E_{r+2}.
 \label{eq:safety}$$ This finite compatibility condition is equivalent to forbidding two output $+1$ symbols at distance two for every ternary input. Denote the finite set of such $q$-periodic families by $\mathcal A_q$.

The unique current-zero interpolation from RH-378 is $$\begin{aligned}
 zf_r(x,z)={}&c_{01}(r)z+c_{02}(r)z^2+c_{11}(r)xz
  +c_{12}(r)xz^2 \notag\\
 &+c_{21}(r)x^2z+c_{22}(r)x^2z^2.
 \label{eq:interpolation}\end{aligned}$$ Unlike RH-379, we impose no condition $c_{11}(r)=0$. Define the phase densities $$\begin{aligned}
 \delta_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}\mu(n)^2,
 \label{eq:delta}\\
 \vartheta_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}
  \mu(n-2)^2\mu(n)^2.
 \label{eq:theta}\end{aligned}$$ Finite initial terms are immaterial in [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}. The standard squarefree progression sieve gives $$0\le\vartheta_{q,r}\le\delta_{q,r},
 \qquad
 \vartheta_{q,r}\le\delta_{q,r-2},
 \label{eq:density-cone}$$ and the totals $$\sum_{r\bmod q}\delta_{q,r}=\frac6{\pi^2},
 \qquad
 \sum_{r\bmod q}\vartheta_{q,r}=\kappa_2
 :=\prod_p\left(1-\frac2{p^2}\right).
 \label{eq:density-totals}$$ These facts, including the phasewise formulas, are recorded in RH-379 and ultimately follow from the squarefree-pattern sieve [@Mirsky1948; @RH379].

For an admissible clock function $$1\le\omega(X)\le X,
 \qquad \omega(X)\longrightarrow\infty,
 \label{eq:omega}$$ set $$S_X^\omega(q,f)=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\le X}
 \frac{\mu(n)f_{n\bmod q}(\mu_0(n-2),\mu(n))}{n}.
 \label{eq:terminal-score}$$ Here $q$, the entire table family $f$, and hence every periodic coefficient are fixed before $X\to\infty$.

[\[thm:limit\]]{#thm:limit label="thm:limit"} For every fixed $q\ge1$, every $f\in\mathcal A_q$, and every $\omega$ satisfying [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}, $$\lim_{X\to\infty}S_X^\omega(q,f)=L_q(f),
 \qquad
 L_q(f)=\sum_{r\bmod q}
 \bigl(c_{02}(r)\delta_{q,r}+c_{22}(r)\vartheta_{q,r}\bigr).
 \label{eq:limit-formula}$$ In particular, active phasewise $c_{11}(r)$ is allowed.

[\[def:capacity\]]{#def:capacity label="def:capacity"} After the limits in Theorem [\[thm:limit\]](#thm:limit){reference-type="ref" reference="thm:limit"} have been formed, define $$G_{\log}(q)=\max_{f\in\mathcal A_q}|L_q(f)|,
 \qquad
 A_{\infty}^{\log}=\frac6{\pi^2}-\frac{\kappa_2}{2}.
 \label{eq:Glog}$$

[\[thm:capacity\]]{#thm:capacity label="thm:capacity"} For every individually fixed integer $q\ge1$, $$\boxed{G_{\log}(q)=A_{\infty}^{\log}.}
 \label{eq:fixed-capacity}$$ The constant projected action $\{-1,0\}$ attains $+A_{\infty}^{\log}$ for every such $q$. Its reflected table attains $-A_{\infty}^{\log}$. Consequently $$\boxed{\sup_{q\in\mathbb N}G_{\log}(q)=A_{\infty}^{\log},}
 \label{eq:all-clock}$$ where the supremum is taken only over already-established fixed-$q$ limits; $q=1$ already attains it.

The numerical constant and the table $\{-1,0\}$ are not first discovered here. RH-378 obtained the same value for the unphased $q=1$ table under the unproved ordinary-average hypothesis $D_2(N)=o(N)$ [@RH378]. The new theorem is the unconditional terminal-log closure of active periodic $c_{11}$, followed by an all-$q$ charge showing that every fixed clock has exactly the same capacity. Equation [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"} is not a claim about $\lim_X\sup_q$, and neither theorem is uniform over $q=q(X)$.

# The analytic fixed-table limit

The first lemma keeps the endpoint $X/\omega(X)$ honest. It is not enough to prove only the case in which that endpoint tends to infinity.

[\[lem:abel\]]{#lem:abel label="lem:abel"} Let $(a_n)$ be a bounded sequence and $A(t)=\sum_{n\le t}a_n$. If $$A(t)=\alpha t+o(t),
 \label{eq:prefix-alpha}$$ then every admissible $\omega$ satisfies $$\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\le X}\frac{a_n}{n}
 \longrightarrow\alpha.
 \label{eq:abel-conclusion}$$

Put $Y=X/\omega(X)$ and $B(t)=A(t)-\alpha t$. Stieltjes summation gives $$\sum_{Y<n\le X}\frac{a_n}{n}
 =\alpha\log\frac XY
 +\frac{B(X)}X-\frac{B(Y)}Y
 +\int_Y^X\frac{B(t)}{t^2}\,dt,
 \label{eq:abel-identity}$$ with an immaterial bounded endpoint convention. Fix $\varepsilon>0$ and choose $T$ so that $|B(t)|\le\varepsilon t$ for $t\ge T$.

If $Y\ge T$, the last three terms in [\[eq:abel-identity\]](#eq:abel-identity){reference-type="eqref" reference="eq:abel-identity"} have absolute value at most $2\varepsilon+\varepsilon\log\omega(X)$. If $Y<T$, split the sum at $T$. The part below $T$ is bounded, whereas the part above $T$ has error at most $O_T(1)+\varepsilon\log(X/T)$. In this second case $$\log X-\log T<\log\omega(X)\le\log X,
 \qquad
 \frac{\log X}{\log\omega(X)}\longrightarrow1.$$ Thus both cases give normalized limsup error at most $\varepsilon$. Letting $\varepsilon\downarrow0$ proves the result.

[\[prop:five-channels\]]{#prop:five-channels label="prop:five-channels"} For every fixed $q$, the following statements hold with any fixed bounded $q$-periodic coefficient in front of the displayed sequence: $$\begin{aligned}
 \sum_{n\le N}\mu(n)&=o(N),
 \label{eq:c01-prefix}\\
 \sum_{n\le N}\mu(n-2)\mu(n)^2&=o(N),
 \qquad
 \sum_{n\le N}\mu(n-2)^2\mu(n)=o(N),
 \label{eq:masked-prefix}\end{aligned}$$ while the phase-restricted prefixes of $\mu(n)^2$ and $\mu(n-2)^2\mu(n)^2$ have slopes [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} and [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}.

Finite Fourier inversion reduces [\[eq:c01-prefix\]](#eq:c01-prefix){reference-type="eqref" reference="eq:c01-prefix"} to Möbius sums in fixed arithmetic progressions, which are $o(N)$ by Davenport cancellation [@Davenport1937]. For the first masked sum, insert $$\mu(n)^2=\sum_{d^2\mid n}\mu(d).$$ With $d\le R$ fixed, the phase congruence and $d^2\mid n$ leave finitely many progressions for the remaining factor $\mu(n-2)$, so Davenport again applies. The absolute $d>R$ tail is $$O\left(\sum_{R<d\le\sqrt N}\left(\frac N{d^2}+1\right)\right)
 =O(N/R+\sqrt N).$$ First let $N\to\infty$ with $q,R$ fixed, then let $R\to\infty$. Expanding $\mu(n-2)^2$ proves the second masked estimate in the same way. The two density statements are their defining squarefree progression limits.

This is precisely the three zero-channel argument inside the proof of RH-379's phase-limit proposition, extracted independently of that proposition's declared $c_{11}=0$ domain. No statement about the $c_{11}$ channel has been used.

[\[prop:c11\]]{#prop:c11 label="prop:c11"} For every fixed $q$ and fixed $q$-periodic coefficient $\rho$, $$\sum_{X/\omega(X)<n\le X}
 \frac{\mu_0(n-2)\mu(n)\rho(n)}n
 =o(\log\omega(X)).
 \label{eq:c11-terminal}$$

Use the affine forms $$D(n)=n-2,
 \qquad V(n)=n,
 \qquad
 \det\begin{pmatrix}1&-2\\1&0\end{pmatrix}=2.$$ TPC-137 proves full-Möbius terminal logarithmic cancellation under the primitive determinant-two hypotheses $$(d,s)=(u,a)=(a,s)=1,
 \qquad su-ad=2,$$ for $D(n)=d+sn$, $V(n)=u+an$, and every fixed bounded periodic mask [@TPC137]. Here $(d,s,u,a)=(-2,1,0,1)$ satisfies all three gcd conditions and the determinant identity, while $D(n),V(n)>0$ for $n>2$. The theorem therefore applies after deleting $n\le2$. Those finitely many terms, and the difference between $\mu$ and $\mu_0$ there, contribute $O(1)/\log\omega(X)=o(1)$ after normalization.

TPC-137 is the full-Möbius source used here. Tao's Theorem 2, equation (3), printed page 3, is its upstream fixed-affine Liouville input [@Tao2016LogChowla]; we do not substitute Tao's Liouville theorem directly for the squarefree-completed statement.

Insert [\[eq:interpolation\]](#eq:interpolation){reference-type="eqref" reference="eq:interpolation"} with $x=\mu_0(n-2)$ and $z=\mu(n)$. Proposition [\[prop:c11\]](#prop:c11){reference-type="ref" reference="prop:c11"} makes the $c_{11}$ term zero after terminal-log normalization. Apply Lemma [\[lem:abel\]](#lem:abel){reference-type="ref" reference="lem:abel"} to Proposition [\[prop:five-channels\]](#prop:five-channels){reference-type="ref" reference="prop:five-channels"}: the $c_{01},c_{12},c_{21}$ channels tend to zero, and the $c_{02},c_{22}$ channels tend to $\delta_{q,r},\vartheta_{q,r}$ phase by phase. There are only finitely many phases. Summing them yields [\[eq:limit-formula\]](#eq:limit-formula){reference-type="eqref" reference="eq:limit-formula"}.

# Pointwise projection from 512 tables to eight actions

For a truth table $f$ with plus-edge set $E$, define its *positive-current projection* $f^+$ by $$E^+=E\cap(\{-1,0,+1\}\times\{+1\}).
 \label{eq:projection}$$

[\[lem:projection\]]{#lem:projection label="lem:projection"} For every $(x,z)\in\{-1,0,+1\}^2$, $$zf^+(x,z)-zf(x,z)\ge0.
 \label{eq:pointwise-gain}$$ Moreover $E^+\subseteq E$, so applying the projection phase by phase preserves universal safety. The $512$ input tables project onto exactly eight actions, each with $64$ preimages.

At $z=+1$ the projection changes nothing, and at $z=0$ both scores vanish. At $z=-1$, the only change is $f=+1$ to $f^+=-1$, which changes $zf$ from $-1$ to $+1$. This proves [\[eq:pointwise-gain\]](#eq:pointwise-gain){reference-type="eqref" reference="eq:pointwise-gain"}. Removing plus edges cannot create a composable pair in [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"}. Finally, the action is the subset $$A=\{x\in\{-1,0,+1\}:(x,+1)\in E\}\subseteq\{-1,0,+1\}.$$ There are $2^3=8$ choices for $A$. The six discarded truth values, at $z=-1$ and $z=0$, are free, giving $2^6=64$ preimages of every action.

The interpolation and limiting weight of the eight projected actions are shown below. Only $c_{02}$ and $c_{22}$ survive in Theorem [\[thm:limit\]](#thm:limit){reference-type="ref" reference="thm:limit"}; $c_{11}$ is displayed to make the active channel visible.

        $A$        $c_{02}$   $c_{11}$   $c_{22}$           $w_r(A)$
  --------------- ---------- ---------- ---------- --------------------------
   $\varnothing$     $0$        $0$        $0$                $0$
     $\{-1\}$        $0$       $-1/2$     $1/2$         $\vartheta_r/2$
      $\{0\}$        $1$        $0$        $-1$      $\delta_r-\vartheta_r$
    $\{-1,0\}$       $1$       $-1/2$     $-1/2$    $\delta_r-\vartheta_r/2$
     $\{+1\}$        $0$       $1/2$      $1/2$         $\vartheta_r/2$
    $\{-1,+1\}$      $0$        $0$        $1$           $\vartheta_r$
    $\{0,+1\}$       $1$       $1/2$      $-1/2$    $\delta_r-\vartheta_r/2$
   $\{-1,0,+1\}$     $1$        $0$        $0$             $\delta_r$

Here and below $\delta_r=\delta_{q,r}$ and $\vartheta_r=\vartheta_{q,r}$. The table is an eight-case substitution into [\[eq:interpolation\]](#eq:interpolation){reference-type="eqref" reference="eq:interpolation"}, not an asymptotic inference from the finite certificate.

[\[lem:action-compatibility\]]{#lem:action-compatibility label="lem:action-compatibility"} Let $A$ be the projected action at phase $r$ and $B$ the action at phase $r+2$. They are compatible if and only if $$A=\varnothing\quad\text{or}\quad +1\notin B.
 \label{eq:action-compatibility}$$ Thus the empty left action admits all eight targets, while every nonempty left action admits exactly the four targets that exclude $+1$.

A composable pair of projected edges must have the form $(x,+1)\in E_A$ and $(+1,w)\in E_B$. Such a pair exists precisely when $A$ is nonempty and $+1\in B$.

Since every summand in [\[eq:terminal-score\]](#eq:terminal-score){reference-type="eqref" reference="eq:terminal-score"} has positive weight $1/n$, Lemma [\[lem:projection\]](#lem:projection){reference-type="ref" reference="lem:projection"} shows directly, at finite $X$, that the maximum signed score is no smaller after projection. Conversely every projected action is itself a truth table. The signed capacity problem is therefore exactly the eight-action problem, not merely bounded by it.

# The all-$q$ predecessor charge

Use the constant baseline action $$B_0=\{-1,0\},
 \qquad
 H_r=w_r(B_0)=\delta_r-\frac{\vartheta_r}{2}.
 \label{eq:baseline}$$ For actions not containing $+1$, the action table and [\[eq:density-cone\]](#eq:density-cone){reference-type="eqref" reference="eq:density-cone"} give $w_r(A)\le H_r$. For every action containing $+1$, they give the uniform local cap $$w_r(A)-H_r\le\frac{\vartheta_r}{2}.
 \label{eq:plus-gain}$$ Indeed the eight differences, in the order of the table, are $$-\delta_r+\frac{\vartheta_r}{2},\quad
 -\delta_r+\vartheta_r,\quad
 -\frac{\vartheta_r}{2},\quad0,\quad
 -\delta_r+\vartheta_r,\quad
 -\delta_r+\frac{3\vartheta_r}{2},\quad0,\quad
 \frac{\vartheta_r}{2}.$$

[\[prop:charge\]]{#prop:charge label="prop:charge"} Every compatible $q$-periodic projected action family satisfies $$\sum_{r\bmod q}w_r(A_r)
 \le\sum_{r\bmod q}H_r
 =\frac6{\pi^2}-\frac{\kappa_2}{2}.
 \label{eq:charge-upper}$$

Let $$P=\{r\in\mathbb Z/q\mathbb Z:+1\in A_r\}.$$ For $r\in P$, compatibility [\[eq:action-compatibility\]](#eq:action-compatibility){reference-type="eqref" reference="eq:action-compatibility"} forces the predecessor action $A_{r-2}$ to be empty. The map $r\mapsto r-2$ is a bijection of $\mathbb Z/q\mathbb Z$, with inverse $s\mapsto s+2$. Compatibility also gives $P\cap(P-2)=\varnothing$. In the self-loop cases $q=1,2$, translation by $-2$ is the identity, so this assertion says directly that $P=\varnothing$; there is no exceptional small clock.

The empty predecessor loses $H_{r-2}$ relative to the baseline, and this loss pays the cap in [\[eq:plus-gain\]](#eq:plus-gain){reference-type="eqref" reference="eq:plus-gain"}. More precisely, $$\begin{aligned}
 H_{r-2}-\frac{\vartheta_r}{2}
 &=\frac12(\delta_{r-2}-\vartheta_{r-2})
   +\frac12(\delta_{r-2}-\vartheta_r)\ge0.
 \label{eq:charge-identity}\end{aligned}$$ The first nonnegative term uses the pair inclusion at phase $r-2$; the second uses the fact that a squarefree pair counted by $\vartheta_r$ has a squarefree predecessor in residue $r-2$. Since the predecessor map is injective, distinct plus phases are charged to distinct empty phases. All remaining phases have actions not containing $+1$ and hence weight at most $H_r$. Summing proves the inequality, and [\[eq:density-totals\]](#eq:density-totals){reference-type="eqref" reference="eq:density-totals"} evaluates the baseline total.

[\[cor:signed\]]{#cor:signed label="cor:signed"} For every fixed $q$, $$\max_{f\in\mathcal A_q}L_q(f)=A_{\infty}^{\log}.
 \label{eq:signed-optimum}$$

Projection cannot decrease a finite signed score, so Proposition [\[prop:charge\]](#prop:charge){reference-type="ref" reference="prop:charge"} bounds every original family as well. The constant action $A_r=B_0$ is compatible because it excludes $+1$ at every phase, and its total weight is the right side of [\[eq:charge-upper\]](#eq:charge-upper){reference-type="eqref" reference="eq:charge-upper"}. It therefore attains the bound for every fixed $q$. Notice also that $A_{\infty}^{\log}\ge3/\pi^2>0$ by $\sum_r\vartheta_r\le\sum_r\delta_r$.

# Input reflection and absolute capacity

For a table $f$, define its input reflection by $$f^\rho(x,z)=f(-x,-z).
 \label{eq:reflection}$$

[\[lem:reflection\]]{#lem:reflection label="lem:reflection"} Simultaneously reflecting every phase preserves compatibility and universal safety. Under [\[eq:reflection\]](#eq:reflection){reference-type="eqref" reference="eq:reflection"}, the six coefficients in the order $(c_{01},c_{02},c_{11},c_{12},c_{21},c_{22})$ transform with signs $$(+,-,-,+,+,-).
 \label{eq:reflection-parity}$$ Consequently $L_q(f^\rho)=-L_q(f)$.

Negating a composable triple $(x,z,w)$ gives a composable triple $(-x,-z,-w)$, and conversely. If $g(x,z)=zf(x,z)$, then $$zf^\rho(x,z)=-g(-x,-z).$$ A monomial $x^az^b$ therefore acquires the factor $-(-1)^{a+b}$, which gives [\[eq:reflection-parity\]](#eq:reflection-parity){reference-type="eqref" reference="eq:reflection-parity"}. In particular $c_{02},c_{11},c_{22}$ change sign, whereas $c_{01},c_{12},c_{21}$ do not. This is not an all-six sign reversal. Theorem [\[thm:limit\]](#thm:limit){reference-type="ref" reference="thm:limit"} kills $c_{11}$ as well as the three unchanged zero channels and retains only $c_{02},c_{22}$, so the limiting score negates.

The baseline table has truth-table identifier $36$ and full coefficient vector $$(0,1,-1/2,-1/2,-1/2,-1/2).$$ Its input reflection is table $72$, with vector $$(0,-1,+1/2,-1/2,-1/2,+1/2).$$ The latter is safe and attains $-A_{\infty}^{\log}$ for every fixed $q$; it is not the output complement of table $36$.

Corollary [\[cor:signed\]](#cor:signed){reference-type="ref" reference="cor:signed"} gives $L_q(f)\le A_{\infty}^{\log}$ for every family. Apply the same bound to $f^\rho$ and use Lemma [\[lem:reflection\]](#lem:reflection){reference-type="ref" reference="lem:reflection"} to get $-L_q(f)\le A_{\infty}^{\log}$. Hence $|L_q(f)|\le A_{\infty}^{\log}$. Tables $36$ and $72$ attain the two signs, proving [\[eq:fixed-capacity\]](#eq:fixed-capacity){reference-type="eqref" reference="eq:fixed-capacity"}. Since the equality holds for every individually fixed $q$, its post-limit supremum is [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"}; no interchange of a supremum with $X\to\infty$ has occurred.

# Executable artifact and source integrity

The exact artifact contains $602$ rows: $$\begin{aligned}
 602={}&512\ \text{truth rows}+8\ \text{projected actions}
       +64\ \text{compatibility rows}\\
      &+8\ \text{charge rows}+6\ \text{analytic interfaces}
       +4\ \text{scope rows}.
 \end{aligned}$$ It enumerates all $512^2$ ordered table pairs when checking global projection and reflection compatibility, recomputes the eight interpolation vectors with exact rational arithmetic, verifies the all-$q$ translation and small-clock contracts, and rejects $24$ genuine semantic mutations by an independent field-level verifier. The canonical certificate has $208648$ bytes and SHA-256

b31187db4ea284152b0c1cb895439e29 cfa80a4e564c87814ee182f87be0a020.

These finite checks reproduce the algebraic interfaces in Sections 3--5. They do not prove the analytic cancellation in Section 2.

The immutable source closure has $95$ Git rows and three remote logical objects, for $98$ logical sources. The first $87$ Git rows are rebound to RH-388 release commit

8e6f89ee1e58e67c53c5f4719c05e881107113ac,

and the eight TPC-137 rows are rebound to commit

0a67723ee2d0dd3171ee294816b8902b6e65285d.

The ordered Git digest is

b7ff5b520d5e926f19346a1ac6e49fbc cf07c5fe24de60758179e9959e673353,

and the ordered $98$-source logical digest is

99a9e6d4372a081b028c28acba7de539 850b4092b64063d9553ca261809e3e74.

TPC-137 is the proof dependency for the full-Möbius active channel. The Tao remote lock records the official Cambridge version of record, Theorem 2, equation (3), printed/PDF page 3, and its CC BY 4.0 license. The release policy nevertheless does not vendor that PDF. The opt-in verifier checks the exact fixed PDF URL and final URL, HTTP status, PDF MIME type, $534086$ bytes, $36$ pages, and SHA-256; its default mode makes zero network requests. The publisher article page, DOI, and license are sealed semantic metadata, not claims that the PDF retrieval command live-refetches those separate pages.

The inherited Johnston--Yang and Maynard lock copies are closure-only. They are not RH-389 proof inputs. Their nonredistributable payloads remain remote and unvendored. All external payload files are excluded from the publication tree. The compact JSON lock records retain their auditable hashes and metadata; verifier code duplicates only the constants needed for fail-closed checking.

# Limitations and claim boundary

The theorem has deliberately frozen quantifiers. It proves a terminal logarithmic limit for each fixed $q$, fixed family, and admissible $\omega$. It proves neither an ordinary Cesàro limit nor an effective rate or an all-prefix power saving. There is no uniform theorem for $q=q(X)$, no unrestricted simultaneous clock, and no selector $K_N$. The maximum in [\[eq:Glog\]](#eq:Glog){reference-type="eqref" reference="eq:Glog"} is defined after each fixed-table limit exists. For one fixed $q$, the set $\mathcal A_q$ is finite, so its finite maximum can also be interchanged with the established limits. This automatic fixed-$q$ observation supplies no maximum-before-limit theorem over unbounded or growing clocks and no adaptive or $K_N$ selector.

The active $c_{11}$ channel is closed only in the fixed periodic determinant-two setting supplied by TPC-137. The result does not activate an operator, a trace identity, a zero correspondence, the Riemann Hypothesis, or any of Gates A--E. Every such gate remains false/open.

# Declarations {#declarations .unnumbered}

#### Data availability.

No new empirical data were created or analyzed. The exact certificate, closed JSON Schema, source-lock records, and tests are included with the paper package; external source PDFs are not vendored.

#### Ethics declaration.

This theoretical and computational study involved no human participants, animals, personal data, or clinical intervention. Institutional ethics approval was not applicable.

#### Author contributions.

RH research program: Conceptualization, Methodology, Formal analysis, Software, Validation, Writing--original draft, and Writing--review and editing.

#### Conflict of interest.

The author declares no conflict of interest.

#### Funding.

No external funding was received for this work.

#### AI-use disclosure.

AI-assisted research tools were used for symbolic enumeration, proof and source-audit orchestration, manuscript drafting, and formatting. The theorem statements, computations, citations, and claim boundaries were checked against the frozen sources and executable artifacts. The author takes responsibility for the accuracy and integrity of the work.
