---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--157-newton-hensel-finite-atlas"
canonical_tex: "symbolic_dynamics/papers/157-newton-hensel-finite-atlas/main.tex"
canonical_pdf: "symbolic_dynamics/papers/157-newton-hensel-finite-atlas/main.pdf"
source_sha256: "fd534ee4180dd0575aaff9e9c39dd7d38709029a2ae15f2357e0417f35cca85e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite Dynamics of the Idempotent-Lifting Cubic $3x^2-2x^3$ Modulo Powers of Two

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/157-newton-hensel-finite-atlas>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/157-newton-hensel-finite-atlas/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/157-newton-hensel-finite-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/157-newton-hensel-finite-atlas/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/157-newton-hensel-finite-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Burban and Drozd explicitly record $3x^2-2x^3$ in a known idempotent-lifting construction with quadratic error improvement; the cubic and that mechanism receive no contribution credit here. We instead determine its complete temporal and one-step inverse atlas on $\mathbb Z/2^n\mathbb Z$. A parity-selected endpoint error has a valuation that doubles at every epoch, which gives every pointwise entry time, every temporal shell, the sharp height $\lceil\log_2 n\rceil$, and the two recurrent points. The inverse problem retains information discarded by this clock. In output valuation $2v$, its normalized odd unit lies in one prescribed class modulo eight, with different classes for $v=1$ and $v\geq2$. An exact branchwise bit lift then gives every target fibre, including the separate quotient boundaries $N=n-2v=1,2$, and yields a closed image-size formula. A deterministic audit checks every state and target through $n=17$ and the normalized-unit lanes $1\leq v\leq6$, $1\leq N\leq11$, totaling $2{,}563{,}880$ exact assertions.
author:
- Anonymous
bibliography:
- references.bib
title: 'Finite Dynamics of the Idempotent-Lifting Cubic $3x^2-2x^3$ Modulo Powers of Two'
```

## Markdown 正文

# Prior boundary and the scoped-atlas theorem {#sec:theorem}

Burban and Drozd's Lemma A.4 recalls a known result, with a pointer to classical background, giving integer polynomials that improve an approximate idempotent modulo successive powers of an ideal; it explicitly lists $$G_1(x)=3x^2-2x^3$$ as an example [@BurbanDrozd2004]. We use this as a direct prior record, not as an origination claim. Thus neither the literal cubic, its idempotent-lifting role, nor quadratic error improvement is new here. We ask the narrower finite question: what are all entry-time shells, image classes, and one-step fibres of this fixed map modulo $2^n$?

For $n\geq1$, write $$F_n:\mathbb Z/2^n\mathbb Z\longrightarrow\mathbb Z/2^n\mathbb Z,
 \qquad F_n(x)=3x^2-2x^3.$$ Select the endpoint error by parity, $$\label{eq:error}
 e(x)=\begin{cases}x,&x\equiv0\pmod2,\\1-x,&x\equiv1\pmod2,\end{cases}$$ and use the truncated convention $v_2(0\bmod 2^n)=n$. Let $\tau_n(x)$ be the first entry time into $\{0,1\}$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every $n\geq1$, the following statements hold.

(A) For all $x\in\mathbb Z/2^n\mathbb Z$ and $t\geq0$, $$\label{eq:valuation-clock}
     v_2(e(F_n^t(x)))=\min\{n,2^tv_2(e(x))\}.$$ The reached endpoint is $x\bmod2$, and $$\label{eq:entry-time}
     \tau_n(x)=\min\{t\geq0:2^tv_2(e(x))\geq n\}.$$ For $t\geq0$, $$\label{eq:cdf}
     A_{n,t}:=\#\{x:\tau_n(x)\leq t\}
     =2^{\,n-\lceil n/2^t\rceil+1}.$$ Consequently the exact shell polynomial is $$\label{eq:shell-polynomial}
     D_n(z)=A_{n,0}+\sum_{t=1}^{M_n}(A_{n,t}-A_{n,t-1})z^t,
     \qquad M_n=\lceil\log_2 n\rceil,$$ and $0,1$ are the only recurrent states.

(B) Let $y\notin\{0,1\}$ and reflect it into the even basin by $$y^\flat=\begin{cases}y,&y\equiv0\pmod2,\\1-y,&y\equiv1\pmod2.
     \end{cases}$$ Then $y\in\operatorname{im}F_n$ if and only if $v_2(y^\flat)=2v<n$ for an integer $v\geq1$ and, on putting $N=n-2v$ and $u=y^\flat/2^{2v}$, $$\label{eq:image-condition}
     u\equiv
     \begin{cases}
     1\pmod2,&N=1,\\
     3\pmod4,&N=2,\\
     7\pmod8,&N\geq3\text{ and }v=1,\\
     3\pmod8,&N\geq3\text{ and }v\geq2.
     \end{cases}$$ Every admissible target in this stratum has exactly $$\label{eq:fibre}
     \#F_n^{-1}(y)=2^{\,v+\min(N-1,2)}
     =2^{\,v+\min(n-2v-1,2)}$$ preimages; every inadmissible nonendpoint target has none. The endpoint fibres and total image size are $$\begin{aligned}
     \#F_n^{-1}(0)=\#F_n^{-1}(1)&=2^{\lfloor n/2\rfloor},
     \label{eq:endpoint-fibres}\\
     \#\operatorname{im}F_n&=2+2\sum_{1\leq v<n/2}
     2^{\max(0,n-2v-3)}.\label{eq:image-size}\end{aligned}$$

The two axes in Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"} are not interchangeable. Part (A) keeps only the error valuation. Part (B) needs the normalized odd unit and even distinguishes the first positive valuation stratum from all later ones. Table [1](#tab:subtraction){reference-type="ref" reference="tab:subtraction"} records the claim boundary.

::: {#tab:subtraction}
  Source                                           Zero-credit prior input                                               Residual treated here
  ------------------------------------------------ --------------------------------------------------------------------- ---------------------------------------------------------------
  Burban--Drozd direct record [@BurbanDrozd2004]   cubic, idempotent lifting, and quadratic improvement                  finite temporal census plus normalized-unit image/fibre atlas
  Elementary arithmetic                            error factorizations, odd squares modulo eight, divisibility counts   displayed temporal/inverse conjunction, not the ingredients
  Generic finite dynamics                          orbit, image, and fibre terminology                                   exact formulas only for this map on $\mathbb Z/2^n\mathbb Z$

  : Prior-art subtraction. Every item in the middle column receives zero contribution credit.
:::

# Exact error squaring and the temporal census {#sec:time}

The forward law follows from two identities, but we print the count so that the clock convention and the $n=1$ boundary are explicit.

Direct expansion gives $$\label{eq:factorizations}
 F_n(x)=x^2(3-2x),\qquad
 1-F_n(x)=(1-x)^2(1+2x),\qquad
 F_n(1-x)=1-F_n(x).$$ If $x$ is even, then $3-2x$ is odd. If $x$ is odd, then $1-x$ is even and $1+2x$ is odd. Parity is preserved, and hence $$v_2(e(F_n(x)))=\min\{n,2v_2(e(x))\}.$$ Induction proves [\[eq:valuation-clock\]](#eq:valuation-clock){reference-type="eqref" reference="eq:valuation-clock"}; the first value $n$ is reached at the time in [\[eq:entry-time\]](#eq:entry-time){reference-type="eqref" reference="eq:entry-time"}.

Put $a_t=\lceil n/2^t\rceil$. Entry by time $t$ is equivalent to $2^{a_t}\mid e(x)$. The even basin contains $2^{n-a_t}$ such residues, and reflection $x\mapsto1-x$ gives the same count in the disjoint odd basin. This proves [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. Consecutive differences give [\[eq:shell-polynomial\]](#eq:shell-polynomial){reference-type="eqref" reference="eq:shell-polynomial"}. Every nonendpoint selected error has valuation at least one, so $2^t\geq n$ suffices for absorption; errors of valuation one show that the sharp maximum is $M_n$. All states reach $0$ or $1$, and both are fixed, proving the recurrence assertion. When $n=1$, every state is already an endpoint, $M_1=0$, and the same formulas give $A_{1,0}=2$.

This section is an exact finite specialization of the zero-credit quadratic improvement mechanism; it supplies context for the inverse atlas rather than a claim to a new lifting iteration.

# The normalized-unit lifting law {#sec:lifting}

For a nonzero even source write $x=2^v w$, where $v\geq1$ and $w$ is odd. Then $$\label{eq:hv-factor}
 F_n(x)=2^{2v}h_v(w),\qquad
 h_v(w)=w^2(3-2^{v+1}w).$$ The odd factor $h_v(w)$ retains the information that the temporal valuation forgets.

[\[lem:unit\]]{#lem:unit label="lem:unit"} Fix $v\geq1$ and let $h_v$ act on the odd residues modulo $2^N$. For $N=1$, its image is the unique odd class and that target has one preimage. For $N=2$, its image is $3\pmod4$ and that target has two preimages. For $N\geq3$, the image is $7\pmod8$ if $v=1$ and $3\pmod8$ if $v\geq2$; every target in the displayed class has four preimages.

For odd $w$, $w^2\equiv1\pmod8$. If $v=1$, the second factor in [\[eq:hv-factor\]](#eq:hv-factor){reference-type="eqref" reference="eq:hv-factor"} is $3-4w\equiv7\pmod8$; if $v\geq2$, the cubic term is divisible by eight and $h_v(w)\equiv3\pmod8$. Reduction gives the claimed images and direct fibre counts for $N=1,2$.

Suppose $N\geq3$. Split the odd inputs as $w=r+4z$ with $r\in\{1,3\}$ and define the integer-valued function $$\label{eq:phi}
 \Phi_{v,r}(z)=\frac{h_v(r+4z)-h_v(r)}8.$$ We prove that $\Phi_{v,r}$ is a permutation modulo $2^k$ for every $k\geq0$. For odd $w$, $$\begin{aligned}
 h_v'(w)&=6w(1-2^vw),\\
 h_v''(w)&=6-6\cdot2^{v+1}w,\\
 h_v'''(w)&=-6\cdot2^{v+1}.\end{aligned}$$ Thus $v_2(h_v'(w))=1$, $v_2(h_v''(w))=1$, and $v_2(h_v'''(w))\geq3$. Set $\delta=4\cdot2^j$. The exact cubic Taylor identity, divided by eight, is $$\label{eq:taylor}
 \frac{h_v(w+\delta)-h_v(w)}8
 =\frac{\delta h_v'(w)}8
  +\frac{\delta^2h_v''(w)}{16}
  +\frac{\delta^3h_v'''(w)}{48}.$$ The first term is $2^j$ times an odd integer. The last two terms have valuations at least $2j+1$ and $3j+5$, respectively. Therefore $$\label{eq:bit-toggle}
 \Phi_{v,r}(z+2^j)-\Phi_{v,r}(z)
 \equiv2^j\pmod {2^{j+1}}.$$ Starting with the sole residue modulo one, [\[eq:bit-toggle\]](#eq:bit-toggle){reference-type="eqref" reference="eq:bit-toggle"} says that the two lifts of every input class hit the two lifts of its output class. Induction proves the permutation assertion.

Take $k=N-3$. Within either $r$-branch, $z$ ranges modulo $2^{N-2}$, whereas the output beyond its fixed three low bits depends on $\Phi_{v,r}(z)$ modulo $2^{N-3}$. Each branch therefore covers the required output class twice; the two branches together give four preimages. This proves the lemma.

The separate statements for $N=1$ and $N=2$ are essential: the four-to-one law begins only at $N=3$.

# Every-target fibres and image size {#sec:fibres}

Equation [\[eq:hv-factor\]](#eq:hv-factor){reference-type="eqref" reference="eq:hv-factor"} shows that a nonzero even output has valuation exactly $2v<n$. Conversely, if $2v\geq n$, its output is zero. For $2v<n$, put $N=n-2v$. Lemma [\[lem:unit\]](#lem:unit){reference-type="ref" reference="lem:unit"} gives exactly the normalized unit conditions in [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"}.

The source unit $w$ is specified modulo $2^{n-v}$, but $h_v(w)$ modulo $2^N$ depends only on $w$ modulo $2^N$. Reduction therefore contributes $$2^{(n-v)-N}=2^v$$ high lifts. Lemma [\[lem:unit\]](#lem:unit){reference-type="ref" reference="lem:unit"} contributes $2^{\min(N-1,2)}$ reduced solutions. Their product proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, including $N=1,2$.

The zero fibre consists precisely of residues divisible by $2^{\lceil n/2\rceil}$, and so has $2^{\lfloor n/2\rfloor}$ elements. The reflection in [\[eq:factorizations\]](#eq:factorizations){reference-type="eqref" reference="eq:factorizations"} transfers this entire even-side description to the odd basin and gives the same fibre over one.

Finally, a fixed class modulo eight contains $2^{N-3}$ odd units when $N\geq3$, while the $N=1,2$ image has one unit. Thus a nonzero stratum in one parity basin has $2^{\max(0,N-3)}$ targets. Summing over $1\leq v<n/2$, doubling by reflection, and adding the endpoints proves [\[eq:image-size\]](#eq:image-size){reference-type="eqref" reference="eq:image-size"}.

For orientation, the fibre spectrum is nonuniform even when all targets are viewed at the same modulus. At $n=17$, for example, the exact image contains $10{,}926$ targets and the positive fibre sizes are $8,16,32,64,128,256,512$. This numerical row illustrates the theorem; it is not used in its proof.

# Exact controls and scope {#sec:controls}

The paper-local verifier uses only Python integers. It exhausts every state, orbit, target fibre, and image through $n=17$. Independently, it exhausts the normalized odd-unit maps for $1\leq v\leq6$ and $1\leq N\leq11$, including the one- and two-bit boundaries. The frozen transcript contains $2{,}563{,}880$ exact assertions and has SHA-256

`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

Enumeration supplies counterexample pressure only; Sections [2](#sec:time){reference-type="ref" reference="sec:time"}-- [4](#sec:fibres){reference-type="ref" reference="sec:fibres"} prove the all-$n$ statements.

The result is confined to the single map $3x^2-2x^3$ on $\mathbb Z/2^n\mathbb Z$. It asserts neither an odd-prime analogue nor a general finite-ring theorem. The bounded source screen did not locate the normalized-unit one-step inverse atlas, but that non-hit is not a novelty, priority, ownership-completeness, or release certificate. An earlier source for the residual formulas would require further subtraction.

# Declarations {#declarations .unnumbered}

*Data availability.* No external data were used. The paper-local verifier and frozen transcript contain the deterministic exact controls.

*Ethics.* This mathematical study involved no human participants, animals, personal data, or field intervention.

*Author contributions.* The anonymous author performed the derivations, exact checks, source-boundary audit, and manuscript preparation.

*Conflict of interest and funding.* The author declares no conflict of interest; no external funding is declared.

*External status.* This artifact remains `HOLD_EXTERNAL`; it is not cleared for posting, submission, circulation, or author contact.
