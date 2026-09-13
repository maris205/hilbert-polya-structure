---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-392-fixed-lag-terminal-log-mobius-capacity-landscape"
canonical_tex: "zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/fixed-lag-terminal-log-mobius-diagonalization-and-square-divisor-capacity-landscape.pdf"
source_sha256: "693f38a69b7f6c35d3a89e98191d0dd27789fd9d14e4057684c942f14bf18112"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fixed-Lag Terminal-Log Möbius Diagonalization and the Square-Divisor Capacity Landscape

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/fixed-lag-terminal-log-mobius-diagonalization-and-square-divisor-capacity-landscape.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-392-fixed-lag-terminal-log-mobius-capacity-landscape/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study terminal logarithmic averages along fixed periodic phases. First, for any two fixed positive-leading affine forms with arbitrary nonzero determinant, we prove full-Möbius cancellation with a fixed periodic mask. The proof inserts finite squarefree cutoffs, combines congruences with an $\mathop{\mathrm{lcm}}$ modulus without assuming the cutoff divisors coprime, extracts contents, and applies Tao's fixed nonparallel Liouville theorem. A determinant-free tail estimate completes the limits in the order: cutoff, terminal limit, then cutoff removal.

  This cancellation diagonalizes every fixed finite collection of distinct Möbius shifts for polynomials of total degree at most two. Separately, for each fixed lag $h\ge1$, it diagonalizes coordinatewise-biquadratic polynomials in $(\mu_0(n-h),\mu(n))$. A local finite-CRT argument gives the exact two-site density $\vartheta^{(h)}_{q,r}$, including collisions modulo $p$ and $p^2$. Projecting $512$ truth tables to eight actions and charging every plus phase to its forced-empty predecessor yields, for all fixed $q,h\ge1$, $$G_{\log}(q,h)=\frac6{\pi^2}-\frac{\kappa_h}{2},\qquad
   \kappa_h=\prod_{p^2\mid h}(1-p^{-2})
            \prod_{p^2\nmid h}(1-2p^{-2}).$$ Thus squarefree lags are exactly the maximizers. The range is $3/\pi^2<G_{\log}(q,h)\le6/\pi^2-\kappa_\star/2$, where $\kappa_\star=\prod_p(1-2p^{-2})$, and its infimum is not attained. Every limit is formed for fixed data before the finite table maximum; no growing period, growing lag, ordinary Cesàro, or multi-lag degree-three claim is made.
author:
- RH research program
bibliography:
- references.bib
date: 'August 10, 2026'
title: 'Fixed-Lag Terminal-Log Möbius Diagonalization and the Square-Divisor Capacity Landscape'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; affine two-point cancellation; squarefree pairs; finite-state capacity.

# Definitions and results

Write $\mu_0(m)=\mu(m)$ for $m\ge1$ and $\mu_0(m)=0$ for $m\le0$. A terminal clock is a function satisfying $$1\le \omega(X)\le X,\qquad \omega(X)\longrightarrow\infty.
 \label{eq:clock}$$ All periods, shifts, affine forms, coefficients, and tables below are fixed before $X\to\infty$.

For $q\ge1$ and $r\in\mathbb Z/q\mathbb Z$, define the one-site and lag-$h$ two-site densities $$\begin{aligned}
 \delta_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}\mu(n)^2,
 \label{eq:delta-def}\\
 \vartheta^{(h)}_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}
  \mu_0(n-h)^2\mu(n)^2.
 \label{eq:theta-def}\end{aligned}$$ Their local formulas will be proved in Section [3](#sec:density){reference-type="ref" reference="sec:density"}.

[\[thm:finite-shift\]]{#thm:finite-shift label="thm:finite-shift"} Fix $q$, distinct integers $a_1,\ldots,a_m$, and phase polynomials $$P_r(x_1,\ldots,x_m)=c_\varnothing(r)+
 \sum_i c_i(r)x_i+\sum_i c_{ii}(r)x_i^2+
 \sum_{i<j}c_{ij}(r)x_ix_j$$ of total degree at most two. For every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, $$\begin{aligned}
 &\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\le X}
 \frac{P_{n\bmod q}(\mu_0(n-a_1),\ldots,\mu_0(n-a_m))}{n}
 \notag\\
 &\hspace{35mm}\longrightarrow
 \sum_{r\bmod q}\left\{\frac{c_\varnothing(r)}q+
 \sum_i c_{ii}(r)\delta_{q,r-a_i}\right\}.
 \label{eq:finite-shift}\end{aligned}$$ Every linear and off-diagonal quadratic channel vanishes.

The next statement is deliberately separate: $x^2z^2$ has total degree four but coordinatewise degree two.

[\[thm:biquadratic\]]{#thm:biquadratic label="thm:biquadratic"} Fix integers $q,h\ge1$ and $P_r(x,z)=\sum_{0\le i,j\le2}c_{ij}(r)x^iz^j$. Then $$\begin{aligned}
 &\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\le X}
 \frac{P_{n\bmod q}(\mu_0(n-h),\mu(n))}{n}
 \notag\\
 &\quad\longrightarrow\sum_{r\bmod q}\left\{
 \frac{c_{00}(r)}q+c_{20}(r)\delta_{q,r-h}
 +c_{02}(r)\delta_{q,r}+c_{22}(r)\vartheta^{(h)}_{q,r}\right\}.
 \label{eq:biquadratic}\end{aligned}$$ The other five coefficient channels vanish.

For a truth-table specialization, let $f_r:\{-1,0,+1\}^2\to\{-1,+1\}$, put $E_r=\{(x,z):f_r(x,z)=+1\}$, and call the phase tuple *lag-$h$ safe* if no $(x,z)\in E_r$ and $(z,w)\in E_{r+h}$ coexist. Denote the finite set of safe tuples by $\mathcal A_{q,h}$, and set $$L_{q,h}(f;\omega)=\lim_{X\to\infty}\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\le X}
 \frac{\mu(n)f_{n\bmod q}(\mu_0(n-h),\mu(n))}{n}.
 \label{eq:score}$$ Theorem [\[thm:biquadratic\]](#thm:biquadratic){reference-type="ref" reference="thm:biquadratic"} will show that this limit exists and is independent of $\omega$. Only after these fixed-table limits are formed, define $$G_{\log}(q,h)=\max_{f\in\mathcal A_{q,h}}|L_{q,h}(f;\omega)|.
 \label{eq:capacity-def}$$

[\[thm:capacity\]]{#thm:capacity label="thm:capacity"} For every pair of fixed integers $q,h\ge1$, $$\boxed{G_{\log}(q,h)=\frac6{\pi^2}-\frac{\kappa_h}{2}},\qquad
 \kappa_h=\prod_{p^2\mid h}(1-p^{-2})
          \prod_{p^2\nmid h}(1-2p^{-2}).
 \label{eq:capacity}$$ The value does not depend on $q$. Constant table $36$ attains the positive sign and its input reflection, table $72$, attains the negative sign. With $\kappa_\star=\prod_p(1-2p^{-2})$, $$\frac3{\pi^2}<G_{\log}(q,h)\le
 \frac6{\pi^2}-\frac{\kappa_\star}{2}.
 \label{eq:range}$$ Equality on the right holds exactly for squarefree $h$; the left endpoint is the unattained infimum over $h\ge1$.

# Terminal analytic tools

[\[lem:abel\]]{#lem:abel label="lem:abel"} Let $(a_n)$ be bounded and $A(t)=\sum_{n\le t}a_n=\alpha t+o(t)$. Then every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} satisfies $$\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\le X}\frac{a_n}{n}
 \longrightarrow\alpha.
 \label{eq:abel}$$

Put $Y=X/\omega(X)$ and $B(t)=A(t)-\alpha t$. Partial summation gives $$\sum_{Y<n\le X}\frac{a_n}{n}
 =\alpha\log(X/Y)+\frac{B(X)}X-\frac{B(Y)}Y
   +\int_Y^X\frac{B(t)}{t^2}\,dt+O(1).$$ For any $\varepsilon>0$, choose $T$ with $|B(t)|\le\varepsilon t$ for $t\ge T$. If $Y\ge T$, the normalized error is at most $\varepsilon+o(1)$. If $Y<T$, the part below $T$ is bounded and $\log X/\log\omega(X)\to1$. The same bound follows. Let $\varepsilon\downarrow0$.

[\[thm:full-mu\]]{#thm:full-mu label="thm:full-mu"} Let $$D(n)=a_1n+b_1,\qquad V(n)=a_2n+b_2,
 \quad a_1,a_2\in\mathbb N,\quad b_1,b_2\in\mathbb Z,$$ and suppose $\Delta=a_1b_2-a_2b_1\ne0$. For every fixed bounded periodic $\rho$ and every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, $$\sum_{X/\omega(X)<n\le X}
 \frac{\mu(D(n))\mu(V(n))\rho(n)}n=o(\log\omega(X)).
 \label{eq:full-mu}$$ Values before both forms become positive are omitted, changing the sum by $O(1)$.

Let $P$ be fixed, larger than every prime divisor of $a_1a_2$, and $$S_P(m)=\prod_{p\le P}(1-\mathbf 1_{p^2\mid m})
 =\sum_{k\mid P\#}\mu(k)\mathbf 1_{k^2\mid m}.$$ Since $\mu(m)=\lambda(m)\mathbf 1_{m\ \mathrm{squarefree}}$, first replace the two Möbius factors by $\lambda(D)\lambda(V)S_P(D)S_P(V)$. Let $M$ be a period of $\rho$. Expanding both cutoffs and the fixed periodic mask leaves finitely many systems $$n\equiv s\pmod M,\qquad k^2\mid D(n),\qquad \ell^2\mid V(n).$$ Each compatible system is a finite disjoint union of residue classes $n=r+Lt$ modulo $L$, where $$L=\mathop{\mathrm{lcm}}(M,k^2,\ell^2)\le M(P\#)^2.
 \label{eq:lcm}$$ No assumption $(k,\ell)=1$ is used.

On such a class, set $$c_D=(a_1L,a_1r+b_1),\qquad c_V=(a_2L,a_2r+b_2).$$ After removing these fixed contents, the two affine forms in $t$ have positive leading coefficients and determinant $$\frac{L\Delta}{c_Dc_V}\ne0.
 \label{eq:reduced-det}$$ Complete multiplicativity gives $$\lambda(D)\lambda(V)=\lambda(c_Dc_V)
 \lambda(D/c_D)\lambda(V/c_V).$$ Tao's Theorem 2, equation (3), printed and PDF page 3, now gives terminal logarithmic cancellation for the reduced fixed nonparallel forms [@Tao2016LogChowla]. Treat the finitely many nonempty classes separately. Replacing $r+Lt$ by $Lt$ changes each weighted sum by $O(1)$. If $X/\omega(X)\to\infty$, the affine endpoint change produces an admissible clock with logarithm $\log\omega(X)+O(1)$. If that lower endpoint stays bounded, apply Tao's theorem with the full-prefix clock $\omega'(X')=X'$ after removing finitely many $t$; then $\log X'\sim\log\omega(X)$. Every subsequence has a further subsequence of one of these two types. Hence the fixed-$P$ approximant is $o(\log\omega(X))$.

It remains to remove $P$. For either fixed affine form $F$, a Boolean union bound and the substitution $F(n)=p^2m$ give $$\sum_{X/\omega(X)<n\le X}
 \frac{|\mathbf 1_{F(n)\ \mathrm{squarefree}}-S_P(F(n))|}{n}
 \ll_F \frac{\log\omega(X)}P+1.
 \label{eq:tail}$$ Indeed, beyond finitely many $n$, one has $n^{-1}\ll_F(p^2m)^{-1}$; the relevant harmonic $m$-interval has length in logarithmic scale at most $\log\omega(X)+O_F(1)$, and $\sum_{p>P}p^{-2}\ll P^{-1}$. The two-coordinate inequality $|uv-UV|\le|u-U|+|v-V|$ for Boolean values makes this estimate determinant-free. Divide by $\log\omega(X)$, first let $X\to\infty$ with $P$ fixed, and then let $P\to\infty$. This proves [\[eq:full-mu\]](#eq:full-mu){reference-type="eqref" reference="eq:full-mu"}.

The Boolean-cutoff and content-extraction architecture follows the TPC-137 template, which treated a frozen determinant-two setting [@TPC137]. The argument above proves the arbitrary-nonzero-determinant form needed here, without claiming historical priority for that level of generality. RH-389 used TPC-137 only at determinant two [@RH389]; it is not being cited as an all-$h$ theorem.

# One-site and two-site local densities {#sec:density}

For each prime $p$, let $$A_p^{(h)}=\{0,h\pmod {p^2}\},\qquad
 \nu_p^{(h)}=|A_p^{(h)}|,\qquad
 \tau_{p,r}^{(h)}=|\{a\in A_p^{(h)}:a\equiv r\pmod p\}|.$$ The braces denote a set of distinct residues modulo $p^2$. Thus a collision modulo $p^2$ is counted once, whereas two distinct residues that collide only modulo $p$ both contribute to $\tau_{p,r}^{(h)}$.

[\[prop:density\]]{#prop:density label="prop:density"} For fixed $q,h\ge1$, $$\begin{aligned}
 \delta_{q,r}={}&\frac1q
 \prod_{p\nmid q}(1-p^{-2})
 \prod_{p\parallel q}\left(1-\frac{\mathbf 1_{p\mid r}}p\right)
 \prod_{p^2\mid q}\mathbf 1_{p^2\nmid r},
 \label{eq:delta-local}\\
 \vartheta^{(h)}_{q,r}={}&\frac1q
 \prod_{p\nmid q}\left(1-\frac{\nu_p^{(h)}}{p^2}\right)
 \prod_{p\parallel q}\left(1-\frac{\tau_{p,r}^{(h)}}p\right)
 \prod_{p^2\mid q}\mathbf 1_{r\bmod p^2\notin A_p^{(h)}}.
 \label{eq:theta-local}\end{aligned}$$ Moreover, $$\begin{gathered}
 0\le\vartheta^{(h)}_{q,r}\le\delta_{q,r},\qquad
 \vartheta^{(h)}_{q,r}\le\delta_{q,r-h},
 \label{eq:cone}\\
 \sum_{r\bmod q}\delta_{q,r}=\frac6{\pi^2},\qquad
 \sum_{r\bmod q}\vartheta^{(h)}_{q,r}=\kappa_h.
 \label{eq:totals}\end{gathered}$$

Impose squarefreeness only at primes $p\le R$, with $R$ containing the prime divisors of $q$. The Chinese remainder theorem gives an exact finite density. If $p\nmid q$, it removes $\nu_p^{(h)}$ residues modulo $p^2$. If $p\parallel q$, the fixed residue modulo $p$ has $p$ lifts, of which $\tau_{p,r}^{(h)}$ are forbidden. If $p^2\mid q$, the phase already fixes the residue modulo $p^2$, giving the last indicator. This proves the finite truncation of [\[eq:theta-local\]](#eq:theta-local){reference-type="eqref" reference="eq:theta-local"}; the one-site computation is identical with the single forbidden residue $0$.

The omitted-prime error is bounded by the density of integers for which $p^2\mid n$ or $p^2\mid n-h$ for some $p>R$. The union bound is $O(\sum_{p>R}p^{-2})+o_N(1)$. First $N\to\infty$, then $R\to\infty$, proving both infinite products. This is a direct finite-CRT-plus-tail proof; Mirsky's squarefree-pattern work is historical context, not a black-box source for the phase formula [@Mirsky1948].

The cone follows by set inclusion of squarefree pairs into each one-site event. Summing phases removes the congruence. At $p$, the two forbidden residues coincide precisely when $p^2\mid h$; hence the total pair density is the product $\kappa_h$ in [\[eq:capacity\]](#eq:capacity){reference-type="eqref" reference="eq:capacity"}.

The collision convention is visible in small cases. For $(h,q,r)=(2,2,0)$, the residues $0,2\pmod4$ are distinct but both are $0\pmod2$, so $\tau_{2,0}^{(2)}=2$ and the $p\parallel q$ factor is zero. For $(6,3,0)$, the analogous factor is $1-2/3=1/3$. In contrast, $(h,q,r)=(4,2,0)$ gives the singleton $A_2^{(4)}=\{0\}$ and factor $1/2$, while $(9,3,0)$ gives factor $2/3$. These examples rule out both loss of a modulo-$p$ collision and double counting of a genuine modulo-$p^2$ collision.

# Diagonalization proofs

For any fixed periodic $\rho$, Davenport cancellation in fixed arithmetic progressions gives $$\sum_{n\le N}\mu(n-a)\rho(n)=o(N).
 \label{eq:one-form}$$ It also gives the masked estimates $$\sum_{n\le N}\mu(n-h)\mu(n)^2\rho(n)=o(N),\qquad
 \sum_{n\le N}\mu(n-h)^2\mu(n)\rho(n)=o(N).
 \label{eq:masked}$$ Indeed, insert $\mu(m)^2=\sum_{d^2\mid m}\mu(d)$, keep $d\le R$, and apply [\[eq:one-form\]](#eq:one-form){reference-type="eqref" reference="eq:one-form"} on the resulting finitely many progressions. The absolute tail is $O(N/R+\sqrt N)$; take $N$ and then $R$ to infinity [@Davenport1937]. Lemma [\[lem:abel\]](#lem:abel){reference-type="ref" reference="lem:abel"} transfers [\[eq:one-form\]](#eq:one-form){reference-type="eqref" reference="eq:one-form"}, [\[eq:masked\]](#eq:masked){reference-type="eqref" reference="eq:masked"}, and Proposition [\[prop:density\]](#prop:density){reference-type="ref" reference="prop:density"} to every terminal clock.

Expand each phase polynomial. The constant has phase density $1/q$, linear monomials vanish by [\[eq:one-form\]](#eq:one-form){reference-type="eqref" reference="eq:one-form"}, and diagonal squares give $\delta_{q,r-a_i}$. For $i\ne j$, apply Theorem [\[thm:full-mu\]](#thm:full-mu){reference-type="ref" reference="thm:full-mu"} to $n-a_i,n-a_j$; their determinant is $a_i-a_j\ne0$. The finite phase sum gives [\[eq:finite-shift\]](#eq:finite-shift){reference-type="eqref" reference="eq:finite-shift"}.

The constant, $x^2$, $z^2$, and $x^2z^2$ channels give respectively $1/q,\delta_{q,r-h},\delta_{q,r}$, and $\vartheta^{(h)}_{q,r}$. The $x,z$ channels vanish by [\[eq:one-form\]](#eq:one-form){reference-type="eqref" reference="eq:one-form"}; $xz^2,x^2z$ vanish by [\[eq:masked\]](#eq:masked){reference-type="eqref" reference="eq:masked"}; and $xz$ vanishes by Theorem [\[thm:full-mu\]](#thm:full-mu){reference-type="ref" reference="thm:full-mu"}, whose determinant is $h\ne0$. Summing phases proves [\[eq:biquadratic\]](#eq:biquadratic){reference-type="eqref" reference="eq:biquadratic"}.

# Truth-table projection and the all-$q,h$ charge

For a phase table, let $Q_r$ be the unique coordinatewise-biquadratic interpolant of $zf_r(x,z)$ on $\{-1,0,+1\}^2$. Since $Q_r(x,0)=0$, its $c_{00},c_{10},c_{20}$ coefficients vanish; the compiler coordinates are $(c_{01},c_{02},c_{11},c_{12},c_{21},c_{22})$. Theorem [\[thm:biquadratic\]](#thm:biquadratic){reference-type="ref" reference="thm:biquadratic"} therefore gives $$L_{q,h}(f;\omega)=\sum_{r\bmod q}
 \{c_{02}(r)\delta_{q,r}+c_{22}(r)\vartheta^{(h)}_{q,r}\},
 \label{eq:table-limit}$$ which is independent of $\omega$.

Replace $E_r$ pointwise by $E_r^+=E_r\cap(\{-1,0,+1\}\times\{+1\})$. At $z=+1$ the score $zf_r$ is unchanged, at $z=0$ it is zero, and at $z=-1$ deleting a plus edge changes the score from $-1$ to $+1$. Projection therefore never decreases a finite signed score and cannot create a composable pair. It maps the $512$ tables onto the eight actions $$A_r=\{x:(x,+1)\in E_r\}\subseteq\{-1,0,+1\},$$ with $64$ preimages per action. Two phases $r,r+h$ are compatible exactly when $$A_r=\varnothing\quad\hbox{or}\quad +1\notin A_{r+h}.
 \label{eq:compatibility}$$

Write $\delta_r=\delta_{q,r}$ and $\vartheta_r=\vartheta^{(h)}_{q,r}$. Exact interpolation gives the eight limiting weights:

    Action $A$     $c_{02}$   $c_{22}$           $w_r(A)$
  --------------- ---------- ---------- --------------------------
   $\varnothing$      0          0                  0
     $\{-1\}$         0        $1/2$         $\vartheta_r/2$
      $\{0\}$         1         $-1$      $\delta_r-\vartheta_r$
    $\{-1,0\}$        1        $-1/2$    $\delta_r-\vartheta_r/2$
     $\{+1\}$         0        $1/2$         $\vartheta_r/2$
    $\{-1,+1\}$       0          1            $\vartheta_r$
    $\{0,+1\}$        1        $-1/2$    $\delta_r-\vartheta_r/2$
   $\{-1,0,+1\}$      1          0              $\delta_r$

The $512$-table lag-two setting originates in RH-378; the positive-current projection and eight-action table are inherited from RH-389 [@RH378; @RH389]. All-$h$ compatibility, density, and charge are proved here.

Use the baseline $B_0=\{-1,0\}$ and $H_r=\delta_r-\vartheta_r/2$. An action without $+1$ has weight at most $H_r$, while an action containing $+1$ gains at most $\vartheta_r/2$ above $H_r$. If $+1\in A_r$, compatibility forces $A_{r-h}=\varnothing$. The loss at that predecessor pays the gain since $$H_{r-h}-\frac{\vartheta_r}{2}
 =\frac{\delta_{r-h}-\vartheta_{r-h}}2+
  \frac{\delta_{r-h}-\vartheta_r}2\ge0.
 \label{eq:charge}$$ Translation $r\mapsto r-h$ is a permutation of $\mathbb Z/q\mathbb Z$, so distinct plus phases have distinct charged predecessors. It has $(q,h)$ cycles, each of length $q/(q,h)$. If $q\mid h$, every cycle is a self-loop and [\[eq:compatibility\]](#eq:compatibility){reference-type="eqref" reference="eq:compatibility"} forces the plus-phase set empty. For example, $(q,h)=(6,4)$ has two cycles of length three; no coprimality of $q,h$ is needed. Summing [\[eq:charge\]](#eq:charge){reference-type="eqref" reference="eq:charge"} and using [\[eq:totals\]](#eq:totals){reference-type="eqref" reference="eq:totals"} yields $$\sum_{r\bmod q}w_r(A_r)\le
 \sum_{r\bmod q}H_r=\frac6{\pi^2}-\frac{\kappa_h}{2}.
 \label{eq:signed-bound}$$ The constant baseline attains equality.

Finally reflect inputs by $f^\rho(x,z)=f(-x,-z)$. Safety is preserved, and the six compiler coefficients transform with signs $(+,-,-,+,+,-)$. The surviving $c_{02},c_{22}$ channels therefore change sign. Baseline table $36$ attains the positive value in [\[eq:signed-bound\]](#eq:signed-bound){reference-type="eqref" reference="eq:signed-bound"}; its reflection is table $72$ and attains the negative value. This proves the absolute maximum in Theorem [\[thm:capacity\]](#thm:capacity){reference-type="ref" reference="thm:capacity"}.

# Square-divisor landscape

If $h$ is squarefree, no local factor in $\kappa_h$ is replaced, so $\kappa_h=\kappa_\star$. If $p^2\mid h$, the factor $1-2p^{-2}$ is replaced by the strictly larger $1-p^{-2}$. Hence $\kappa_h=\kappa_\star$ exactly for squarefree $h$, proving the maximum claim in [\[eq:range\]](#eq:range){reference-type="eqref" reference="eq:range"}.

For every finite $h$, at least one prime-square factor remains strict, and comparison with $\prod_p(1-p^{-2})=6/\pi^2$ gives $\kappa_h<6/\pi^2$. Thus $G_{\log}(q,h)>3/\pi^2$. On the other hand, for $$h_y=\left(\prod_{p\le y}p\right)^2,$$ the factors through $y$ equal those of $6/\pi^2$, while the tail ratio tends to one. Consequently $\kappa_{h_y}\to6/\pi^2$ and $G_{\log}(q,h_y)\to3/\pi^2$. The infimum is therefore not attained.

# Executable artifact and source boundary

The Stage-1 certificate contains $640$ exact rows, $$640=512+8+64+8+9+7+12+8+6+6,$$ covering truth tables, actions, compatibility, charge, monomials, determinant completion, local densities, the lag spectrum, finite shifts, and firewalls. It exhausts all $512^2$ ordered table pairs, finding $3375$ compatible pairs and zero projection, reflection, involution, parity, or interpolation failures. It also rejects $24$ semantic mutations under a builder-independent verifier. The canonical certificate has $220832$ bytes and SHA-256

614297795d4d4dfeadfb5667d3e0d405 d04fbe8e07e9d87a743faed9cb267a96.

These checks reproduce finite algebra; they do not prove Theorem [\[thm:full-mu\]](#thm:full-mu){reference-type="ref" reference="thm:full-mu"} or Proposition [\[prop:density\]](#prop:density){reference-type="ref" reference="prop:density"}.

The immutable closure is rebound to RH-389 release commit

8b1a875b4bbefd955a419593951ce2d09987ac6f.

Its Git groups have sizes $95,8,3$, with ordered group digests

8a674e5d60237b4463e1f68ef79965633ed11a4d098957e5be44e05f471174cb,\
87bbdb455fa5217404d863d1054b4ae408de69da6701ff42ac439ec9bfe1605c,\
a03e4ba7d8b5b054acc95288c70e753bf22b82bb1957f635891b28682c67840e.

The all-$106$ Git digest is

3b32865a14618a605915beb8eab6432b048fca49718b69519697ef861cbe650f,

and adding three remote logical locks gives $109$ objects with digest

39bf8e9030b511e85fdf26a7c71722c3e4be5bc74bc738aa253bbc29c94517f9.

Among the three remote locks, only Tao is an analytic proof input. Its official Cambridge version of record locates Theorem 2, equation (3), on printed/PDF page 3 and is licensed CC BY 4.0; project policy nevertheless does not vendor the PDF. The inherited Johnston--Yang and Maynard locks are closure-only and are not used in the proof. No article-specific redistribution grant is established for either of those two payloads, so both remain remote and unvendored. All three offline verifiers default to zero network requests. The publication tree excludes all five external payload identities (the Johnston--Yang PDF, source archive, and extracted source, the Maynard PDF, and the Tao PDF). No new remote source was added.

Relative to the RH-378/RH-389/TPC-137 templates, the two local proof completions are the arbitrary-nonzero-determinant Boolean cutoff argument and the all-$h$ phasewise CRT formula. This is a package-level provenance statement, not a global priority claim.

# Limitations and declarations

The quantifiers are fixed-data quantifiers. There is no uniform theorem for $q=q(X)$, $h=h(X)$, a growing shift family, or an effective rate. The paper proves terminal logarithmic averages, not ordinary Cesàro averages. The finite-shift theorem stops at total degree two. The coordinatewise-biquadratic compiler concerns one fixed lag and does not assert degree-three multi-coordinate or interacting-multiple-lag truth-table laws. The maximum in [\[eq:capacity-def\]](#eq:capacity-def){reference-type="eqref" reference="eq:capacity-def"} is taken only after each fixed-table limit; no maximum-before-limit or adaptive selector is present. Nothing here constructs an operator, trace formula, zero model, or proof of the Riemann Hypothesis, and all five physical gates remain open.

#### Data availability.

No new empirical data were created or analyzed. The exact certificate, result, recursively closed JSON Schema, source-lock records, and tests are included in the paper package. External PDFs and source archives are not vendored.

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
