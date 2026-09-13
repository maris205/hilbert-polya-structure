---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-373-composite-clock-mobius-capacity-floor"
canonical_tex: "zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/main.pdf"
source_sha256: "2242a03b03e31707f44595930db7a8ff11cee7df1134ac0b575ef12e2d9feba5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Composite-clock phase selectors and an improved Möbius capacity floor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-373-composite-clock-mobius-capacity-floor/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The RH-366 distance-two capacity has an unconditional lower floor $4/\pi^2$ and a squarefree upper ceiling $6/\pi^2$, but its adaptive finite-prefix limit is open. We give a strict, source-locked improvement of the lower floor. A clocked selector with period $q=180$ uses an explicit set of eighty phases having no two elements at distance two modulo $180$. The resulting sign word is admissible for every possible Möbius input. Exact squarefree densities in the $180$ arithmetic progressions and fixed-frequency Möbius cancellation give the correlation $$\frac{97}{24\pi^2}
         =\frac4{\pi^2}+\frac1{24\pi^2}.$$ Consequently $\liminf K_N/N\ge97/(24\pi^2)$. We also give a literal two-state universal-safety completion on the frozen four-state graph and check all $3240$ input-pair rows. This is one explicit lower-bound witness, not an optimization over all clocks or memories; the ordinary capacity limit, intrinsic operators, prime-power traces, Riemann-zero identification, and RH remain outside scope.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: |
  Composite-clock phase selectors and an improved\
  Möbius capacity floor
```

## Markdown 正文

# Frozen capacity and claim boundary

The RH-366 scalar capacity is $$K_N=\max_{\substack{\varepsilon_1,\ldots,\varepsilon_N\in\{-1,+1\}\\
 \text{not }(\varepsilon_n,\varepsilon_{n+2})=(+1,+1)}}
 \left|\sum_{n\le N}\mu(n)\varepsilon_n\right|.
 \label{eq:capacity}$$ The optimizer may read the complete prefix and may change with $N$. RH-366 proves $$\frac4{\pi^2}\le\liminf_{N\to\infty}\frac{K_N}{N}
 \le\limsup_{N\to\infty}\frac{K_N}{N}\le\frac6{\pi^2},
 \label{eq:old-bracket}$$ without asserting convergence [@RH366]. RH-371 reduces each finite value to eight odd-run frequencies but leaves their ordinary Möbius convergence open [@RH371].

All statements here remain in the scalar adaptive-capacity data type. The selector is a prescribed arithmetic observable depending only on the phase and current Möbius value. It is not a canonical dynamical coupling, a trace, a determinant, or a model of Riemann zeros.

# A general phase-selector lemma

Let $q\ge1$ and let $I\subset\mathbb Z/q\mathbb Z$ satisfy $$I\cap(I+2)=\varnothing .
\label{eq:independent}$$ Define the one-site selector $$e_r(a)=
 \begin{cases}
 +1,&r\in I\text{ and }a=+1,\\
 -1,&\text{otherwise},
 \end{cases}
 \qquad
 \varepsilon_n=e_{n\bmod q}(\mu(n)).
 \label{eq:selector}$$

The sign word in [\[eq:selector\]](#eq:selector){reference-type="eqref" reference="eq:selector"} obeys the RH-366 distance-two rule for every ternary input word $a_n\in\{-1,0,+1\}$.

If $\varepsilon_n=+1$ and $\varepsilon_{n+2}=+1$, then both residues $n$ and $n+2$ belong to $I$, contradicting [\[eq:independent\]](#eq:independent){reference-type="eqref" reference="eq:independent"}. No arithmetic property of the input is used.

For a residue $r\pmod q$, write $$\delta_{q,r}=\lim_{N\to\infty}\frac1N
 \#\{n\le N:n\equiv r\pmod q,\ \mu(n)^2=1\}.
 \label{eq:delta-def}$$

For every finite $q$ and $I$ satisfying [\[eq:independent\]](#eq:independent){reference-type="eqref" reference="eq:independent"}, $$\lim_{N\to\infty}\frac1N\sum_{n\le N}\mu(n)\varepsilon_n
   =\sum_{r\in I}\delta_{q,r}.
 \label{eq:selector-limit}$$ Consequently $$\sum_{r\in I}\delta_{q,r}
 \le \liminf_{N\to\infty}\frac{K_N}{N}.
 \label{eq:selector-floor}$$

Put $M_r(N)=\sum_{n\le N,\ n\equiv r\ (q)}\mu(n)$ and $Q_r(N)=\sum_{n\le N,\ n\equiv r\ (q)}\mu(n)^2$. On the selected residue classes, $$\mu(n)e_r(\mu(n))
 =-\mu(n)+2\mathbf 1_{\{\mu(n)=1\}}
 =-\mu(n)+\mu(n)^2+\mu(n).$$ Thus the total sum equals $$-\sum_{n\le N}\mu(n)+\sum_{r\in I}Q_r(N)+\sum_{r\in I}M_r(N).$$ Fixed-frequency Davenport cancellation, followed by finite Fourier inversion in the fixed arithmetic progressions, gives $M_r(N)=o(N)$, and the squarefree progression sieve gives $Q_r(N)/N\to\delta_{q,r}$ [@Davenport1937; @Mirsky1948]. The global Möbius sum is also $o(N)$, proving [\[eq:selector-limit\]](#eq:selector-limit){reference-type="eqref" reference="eq:selector-limit"}. The lemma makes the selector admissible, so its absolute correlation is bounded by $K_N$ for every $N$; taking the liminf gives [\[eq:selector-floor\]](#eq:selector-floor){reference-type="eqref" reference="eq:selector-floor"}.

The theorem applies to every fixed finite clock, but it does not say that the best $I$ for a given $q$ has been found, nor that the supremum over $q$ equals the adaptive capacity limit. A finite selector is a lower certificate only.

# The composite clock $q=180$

Take $q=180=2^2\,3^2\,5$. The squarefree progression density has the exact piecewise form $$\pi^2\delta_{180,r}=
 \begin{cases}
 0,&4\mid r\text{ or }9\mid r,\\
 5/96,&4\nmid r,\ 9\nmid r,\ 5\nmid r,\\
 1/24,&4\nmid r,\ 9\nmid r,\ 5\mid r.
 \end{cases}
 \label{eq:180-density}$$

The congruence class is empty of squarefree integers when it is forced to be zero modulo $4$ or $9$. Otherwise, the unrestricted primes contribute $$\frac1{180}\prod_{p\nmid180}(1-p^{-2})
 =\frac1{180}\frac{6/\pi^2}
 {(1-2^{-2})(1-3^{-2})(1-5^{-2})}
 =\frac5{96\pi^2}.$$ When $5\mid r$, the class is zero modulo $5$ and one of the five lifts modulo $25$ is forbidden, multiplying by $1-1/5=4/5$ and giving $1/(24\pi^2)$.

Use the following explicit phase set: $$\begin{aligned}
 I_{\rm even}&=\{r\in\mathbb Z/180\mathbb Z:r\equiv2\pmod4,\ 9\nmid r\},\\
 I_{\rm odd}&=\{3,7,11,15,19,23,29,33,37,41,47,51,57,61,65,69,\\
 &\qquad 73,77,83,87,91,97,101,105,109,113,119,123,127,131,\\
 &\qquad 137,141,147,151,155,159,163,167,173,177\},\\
 I&=I_{\rm even}\cup I_{\rm odd}.\end{aligned}$$ The even set has $40$ elements and the displayed odd list has $40$ elements. Direct reduction modulo $180$ gives $$I\cap(I+2)=\varnothing.
\label{eq:I-safe}$$ Among the selected phases, $68$ have density coefficient $5/96$ and $12$ have coefficient $1/24$; none has coefficient zero. Therefore $$\sum_{r\in I}\delta_{180,r}
 =\frac{68\cdot5+12\cdot4}{96\pi^2}
 =\frac{97}{24\pi^2}.
 \label{eq:180-floor}$$

For the RH-366 distance-two capacity, $$\boxed{\displaystyle
 \liminf_{N\to\infty}\frac{K_N}{N}\ge\frac{97}{24\pi^2}}
 \label{eq:main-floor}$$ and hence $$\frac{97}{24\pi^2}=\frac4{\pi^2}+\frac1{24\pi^2}>
 \frac4{\pi^2}.$$

Apply Theorem 2.2 to the set $I$ in [\[eq:I-safe\]](#eq:I-safe){reference-type="eqref" reference="eq:I-safe"} and use [\[eq:180-floor\]](#eq:180-floor){reference-type="eqref" reference="eq:180-floor"}.

# Literal graph completion

For completeness, the selector can be represented by a universally safe finite-memory table on the frozen RH-366 graph. Its state set is $\{M,P\}$, and the graph vertices are ordered as $$(--),\quad(-+),\quad(+-),\quad(++),$$ with observable $(-1,-1,+1,+1)$ and the six frozen edges from RH-366. For $r\in\mathbb Z/180\mathbb Z$ put $$b_M(r)=-1,\qquad
 b_P(r)=\begin{cases}+1,&r-1\in I,\\-1,&r-1\notin I,\end{cases}$$ and let $$e_r(a)=\begin{cases}+1,&r\in I,\ a=+1,\\-1,&\text{otherwise}.\end{cases}$$ The output in state $s$ is the pair $(e_r(a),b_s(r))$, and the next state is $P$ exactly when $e_r(a)=+1$ (otherwise it is $M$).

The table above is universally safe and has the one-site observable $e_r(a)$.

If $e_r(a)=-1$, the next state is $M$ and its previous-sign coordinate at phase $r+1$ is $-1=e_r(a)$. If $e_r(a)=+1$, then $r\in I$, the next state is $P$, and $b_P(r+1)=+1=e_r(a)$. Thus the pair coordinates shift correctly. The only forbidden edge would have current previous sign $+1$ and next current sign $+1$. The former implies $r-1\in I$ and the latter implies $r+1\in I$, contradicting $I\cap(I+2)=\varnothing$. The first coordinate of every output is $e_r(a)$, so the one-site condition is literal for both states.

This completion is a finite certificate, not a new operator. It merely embeds the explicit sign word in the already frozen graph language.

# Executable audit

The exact artifact uses an integer Möbius sieve, rational density coefficients, and the table construction above. Its principal rows are:

  --------------------------------------- ------------
  selected phases                                 $80$
  distance-two conflicts                           $0$
  coefficient-$5/96$ phases                       $68$
  coefficient-$1/24$ phases                       $12$
  universal state/phase/input-pair rows         $3240$
  prefix witness rows ($1\le N\le2048$)         $2048$
  endpoint                                  $N=2^{16}$
  endpoint selector score                      $26852$
  endpoint capacity                            $32320$
  --------------------------------------- ------------

The endpoint rows and all prefix rows are finite reproducibility checks, not asymptotic evidence. Source hashes for RH-366, RH-371, RH-372, the arithmetic source, and the four-volume archive are stored in `results/result.json`.

# Route verdict and Gate ledger

Route A is `GO` narrowly: the phase-selector theorem and the explicit $q=180$ density calculation are unconditional and independent. Route B is `STOP_SCOPED`. This paper does not prove convergence of $K_N/N$, does not optimize over all clocks or memory budgets, and does not supply the higher-order Möbius correlations needed for the unrestricted genuinely memory-dependent class.

Gates A--E remain false/open. In particular, the selector uses an externally prescribed phase and current Möbius input and has no canonical operator, Fredholm determinant, von-Mangoldt prime-power trace, self-adjoint generator, zero identification, Hilbert--Polya construction, or implication for the Riemann Hypothesis.

# Conclusion

A composite clock can exploit squarefree residue-class defects without violating the distance-two sign rule. The explicit $q=180$ witness raises the rigorous capacity floor by $1/(24\pi^2)$. The remaining gap to the squarefree ceiling is still a nonlinear adaptive problem: the new certificate does not turn a finite selector family into an asymptotic capacity theorem. The next mathematical edge must address that distinction rather than extrapolate from the finite endpoint.
