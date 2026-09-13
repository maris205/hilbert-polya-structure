---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-376-shift-two-chowla-run-density-boundary"
canonical_tex: "zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/main.pdf"
source_sha256: "414728a8ac2e29add0ec9a4e11fc4d2dd3991be8c5de696c3bd2d5ebbd25b70e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The shift-two Chowla boundary for two-site Möbius run intervals

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-376-shift-two-chowla-run-density-boundary/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate the first correlation-hard component of the exact RH-371 eight-run formula. For either sign $\sigma$, let $C_{\sigma,2}(N)$ count odd starts $1\le n\le N-2$ for which $\mu(n)=\mu(n+2)=\sigma$. With all sums taken over that common endpoint, put $$Q_2=\sum\mu(n)^2\mu(n+2)^2,\quad
   U_2=\sum\mu(n)\mu(n+2)^2,$$ $$V_2=\sum\mu(n)^2\mu(n+2),\quad
   D_2=\sum\mu(n)\mu(n+2).$$ Even starts vanish identically, and Boolean expansion gives the exact all-prefix identity $$4C_{\sigma,2}=Q_2+\sigma U_2+\sigma V_2+D_2.$$ We prove unconditionally that $Q_2/N\to\kappa_2:=\prod_p(1-2/p^2)$ and $U_2,V_2=o(N)$. The latter proof fixes a square-divisor cutoff, applies Davenport cancellation only in finitely many fixed progressions, and then removes the cutoff. The frozen Teräväinen--Walker fixed-affine logarithmic theorem and Abel summation show that any Cesàro limit of $D_2/N$ must be zero. Consequently, existence of either signed two-site interval density is equivalent to ordinary shift-two Cesàro Chowla, and the density is then $\kappa_2/4$ for both signs. This is a scoped hardness equivalence: it neither proves shift-two Chowla nor settles higher run densities, the alternating eight-run envelope, or the adaptive capacity limit. No operator, trace, Riemann-zero identification, Hilbert--Polya construction, or proof of RH is claimed.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: 'The shift-two Chowla boundary for two-site Möbius run intervals'
```

## Markdown 正文

# Frozen interval count and scope

RH-371 writes the distance-two adaptive Möbius capacity in terms of eight overlapping run-interval counts. Its definition for the second count is $$C_{\sigma,2}(N)
 =\#\{1\le n\le N-2:n\text{ odd},\
        \mu(n)=\mu(n+2)=\sigma\},
 \qquad \sigma\in\{-1,+1\}.
 \label{eq:C-definition}$$ The starts are allowed to overlap. Thus $C_{\sigma,2}$ counts two-site same-sign intervals; it is not the number of maximal runs having exact length two. RH-371 proves an exact finite-prefix capacity formula but does not prove density convergence for these intervals or for its alternating eight-run envelope [@RH371]. RH-375 closes a separate fixed-clock one-site class without changing this adaptive correlation question [@RH375].

Every sum below uses the single endpoint $$1\le n\le N-2.
 \label{eq:common-endpoint}$$ Empty sums are zero when $N<3$. Define $$\begin{aligned}
 Q_2(N)&=\sum_{n\le N-2}\mu(n)^2\mu(n+2)^2,
 &U_2(N)&=\sum_{n\le N-2}\mu(n)\mu(n+2)^2,
 \label{eq:masked-one}\\
 V_2(N)&=\sum_{n\le N-2}\mu(n)^2\mu(n+2),
 &D_2(N)&=\sum_{n\le N-2}\mu(n)\mu(n+2).
 \label{eq:masked-two}\end{aligned}$$ Here $D_2(N)=o(N)$ is the ordinary shift-two Cesàro Chowla statement. It remains open in the present source corpus.

The theorem below is an equivalence with that open statement, not a proof of it. No failure of convergence is established. A conclusion about one two-site count does not by itself determine the seven remaining RH-371 run levels or their alternating capacity envelope.

# The exact Boolean identity

For $x\in\{-1,0,+1\}$ and $\sigma\in\{-1,+1\}$, $$\mathbf 1_{\{x=\sigma\}}=\frac{x^2+\sigma x}{2}.
 \label{eq:boolean}$$ There is one small endpoint issue: equation [\[eq:C-definition\]](#eq:C-definition){reference-type="eqref" reference="eq:C-definition"} uses odd starts, whereas [\[eq:masked-one\]](#eq:masked-one){reference-type="eqref" reference="eq:masked-one"}--[\[eq:masked-two\]](#eq:masked-two){reference-type="eqref" reference="eq:masked-two"} sum over all starts. The distinction vanishes exactly.

For every even $n$, both same-sign indicators and all four product terms in [\[eq:masked-one\]](#eq:masked-one){reference-type="eqref" reference="eq:masked-one"}--[\[eq:masked-two\]](#eq:masked-two){reference-type="eqref" reference="eq:masked-two"} are zero.

If $n\equiv0\pmod4$, then $\mu(n)=0$. If $n\equiv2\pmod4$, then $\mu(n+2)=0$. Every listed summand contains both sites, either as a sign indicator or as a product, and therefore vanishes.

For every $N\ge1$ and $\sigma\in\{-1,+1\}$, $$\boxed{\displaystyle
 4C_{\sigma,2}(N)
 =Q_2(N)+\sigma U_2(N)+\sigma V_2(N)+D_2(N).}
 \label{eq:master-identity}$$

The preceding lemma permits summation over all starts in [\[eq:common-endpoint\]](#eq:common-endpoint){reference-type="eqref" reference="eq:common-endpoint"}. Apply [\[eq:boolean\]](#eq:boolean){reference-type="eqref" reference="eq:boolean"} at $\mu(n)$ and $\mu(n+2)$ and multiply: $$4\mathbf 1_{\{\mu(n)=\sigma\}}\mathbf 1_{\{\mu(n+2)=\sigma\}}
 =\bigl(\mu(n)^2+\sigma\mu(n)\bigr)
  \bigl(\mu(n+2)^2+\sigma\mu(n+2)\bigr).$$ Since $\sigma^2=1$, expansion and summation give [\[eq:master-identity\]](#eq:master-identity){reference-type="eqref" reference="eq:master-identity"}.

The identity is pointwise before summation. It introduces no probability, independence, or finite-to-asymptotic inference.

# The three unconditional terms

## The squarefree-pair density

Put $$\kappa_2=\prod_p\left(1-\frac2{p^2}\right).
 \label{eq:kappa}$$ The two forbidden classes $0$ and $-2$ modulo $p^2$ are distinct for every prime, including $p=2$. Thus the local factor at $2$ is $1/2$; there is no additional parity factor.

$$\frac{Q_2(N)}N\longrightarrow\kappa_2.
 \label{eq:Q-limit}$$

Fix $R\ge2$ and first forbid only the prime squares $p^2$ with $p\le R$. The Chinese remainder theorem gives the density $$\prod_{p\le R}(1-2/p^2)$$ for the remaining residue classes. A number accepted by this finite sieve but not counted by $Q_2$ has $p^2\mid n$ or $p^2\mid n+2$ for some $p>R$. The union bound gives, uniformly in the common endpoint, $$\#\{\text{such starts}\}
 \le 2\sum_{R<p\le\sqrt{N+2}}
       \left(\frac{N}{p^2}+1\right)
 =O\!\left(\frac NR+\sqrt N\right).$$ First let $N\to\infty$ at fixed $R$, and only then let $R\to\infty$. The finite products converge to [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}, proving [\[eq:Q-limit\]](#eq:Q-limit){reference-type="eqref" reference="eq:Q-limit"}. This is the classical squarefree-pattern sieve in the scope recorded by Mirsky [@Mirsky1948].

## The one-sign squarefree masks

Davenport's fixed-frequency bound, followed by finite Fourier inversion, implies that for every fixed modulus $q$ and residue $a$, $$\sum_{\substack{m\le X\\m\equiv a\ (q)}}\mu(m)=o(X).
 \label{eq:fixed-ap}$$ Only fixed progressions will be used [@Davenport1937].

$$U_2(N)=o(N),\qquad V_2(N)=o(N).
 \label{eq:UV-limit}$$

Use the exact identity $$\mu(m)^2=\sum_{d^2\mid m}\mu(d).$$ Fix an integer cutoff $R$. Expanding the mask at $n+2$ gives $$U_2(N)=\sum_{d\le R}\mu(d)
       \sum_{\substack{n\le N-2\\n\equiv-2\ (d^2)}}\mu(n)
       +O\!\left(\frac NR+\sqrt N\right).
 \label{eq:U-cutoff}$$ Indeed, the absolute tail is at most $$\sum_{R<d\le\sqrt{N+2}}\left(\frac{N}{d^2}+1\right)
 =O(N/R+\sqrt N).$$ For every fixed $d$, the inner sum in [\[eq:U-cutoff\]](#eq:U-cutoff){reference-type="eqref" reference="eq:U-cutoff"} is $o(N)$ by [\[eq:fixed-ap\]](#eq:fixed-ap){reference-type="eqref" reference="eq:fixed-ap"}. The sum over $d\le R$ is finite, so after division by $N$ and passage to the limit, $$\limsup_{N\to\infty}\frac{|U_2(N)|}{N}
                         \ll\frac1R.$$ Now send $R\to\infty$.

For $V_2$, expand $\mu(n)^2$ instead. At fixed $d$, the inner sum is $\sum_{n\equiv0\ (d^2)}\mu(n+2)$; after the translation $m=n+2$ this is again a fixed arithmetic progression. The same tail estimate and the same order of limits prove $V_2=o(N)$.

The proof fixes $R$, takes $N\to\infty$ in finitely many moduli $d^2$, and then removes $R$. It does not apply Davenport with a modulus growing with $N$ and supplies no uniform growing-clock theorem.

Combining [\[eq:master-identity\]](#eq:master-identity){reference-type="eqref" reference="eq:master-identity"}, [\[eq:Q-limit\]](#eq:Q-limit){reference-type="eqref" reference="eq:Q-limit"}, and [\[eq:UV-limit\]](#eq:UV-limit){reference-type="eqref" reference="eq:UV-limit"} gives the unconditional reduction $$\frac{4C_{\sigma,2}(N)}N
 =\kappa_2+\frac{D_2(N)}N+o(1),
 \qquad \sigma\in\{-1,+1\}.
 \label{eq:reduction}$$ The only unresolved term is the unmasked shift-two correlation.

# Logarithmic input and Cesàro rigidity

The frozen source theorem applies to fixed nonparallel positive affine forms and a fixed additive twist. Specializing Teräväinen--Walker to $f_1=f_2=\mu$, the forms $m+1,m+3$, and twist $\gamma=0$ gives $$\lim_{X\to\infty}\frac1{\log X}
 \sum_{m\le X}\frac{\mu(m+1)\mu(m+3)}m=0.
 \label{eq:TW}$$ The affine determinant is $1\cdot3-1\cdot1=2$. This exact specialization and its qualitative logarithmic normalization are locked in TPC-193 [@TeravainenWalker2025; @TPC193]. No natural-average conclusion is read directly from [\[eq:TW\]](#eq:TW){reference-type="eqref" reference="eq:TW"}.

Let $a_n=\mu(n)\mu(n+2)$ and $A(X)=\sum_{n\le X}a_n$. Reindexing [\[eq:TW\]](#eq:TW){reference-type="eqref" reference="eq:TW"} replaces $1/(n-1)$ by $1/n$. The total error is bounded by $$\sum_{n\ge2}\left|\frac1{n-1}-\frac1n\right|\le1,$$ and changing finitely many endpoints costs $O(1)$. Hence $$\frac1{\log X}\sum_{n\le X}\frac{a_n}{n}\longrightarrow0.
 \label{eq:log-D}$$

If $A(X)/X\to L$, then $$\frac1{\log X}\sum_{n\le X}\frac{a_n}{n}\longrightarrow L.
 \label{eq:abel-limit}$$

Partial summation gives $$\sum_{n\le X}\frac{a_n}{n}
 =\frac{A(X)}X+\int_1^X\frac{A(t)}{t^2}\,dt.
 \label{eq:abel}$$ Write $A(t)=Lt+o(t)$. The first term in [\[eq:abel\]](#eq:abel){reference-type="eqref" reference="eq:abel"}, divided by $\log X$, tends to zero. The integral equals $L\log X+o(\log X)$: for any $\varepsilon>0$, the tail error is bounded by $\varepsilon\int_T^Xdt/t$, while the initial interval contributes $O_T(1)$. This proves [\[eq:abel-limit\]](#eq:abel-limit){reference-type="eqref" reference="eq:abel-limit"}.

If $D_2(N)/N$ has a limit, then that limit is zero.

Since $D_2(N)=A(N-2)$, existence of $D_2(N)/N\to L$ is equivalent to $A(X)/X\to L$. The Abel lemma says that the logarithmic average in [\[eq:log-D\]](#eq:log-D){reference-type="eqref" reference="eq:log-D"} tends to $L$, while the frozen affine theorem says it tends to zero. Therefore $L=0$.

The argument uses logarithmic cancellation only as a rigidity statement after a natural Cesàro limit is assumed to exist. It does not invert Abel summation and does not promote a logarithmic theorem to unconditional natural cancellation.

# The shift-two hardness equivalence

Fix either $\sigma\in\{-1,+1\}$. The following are equivalent:

1.  $C_{\sigma,2}(N)/N$ has a limit;

2.  $D_2(N)/N$ has a limit;

3.  $D_2(N)=o(N)$, the ordinary shift-two Cesàro Chowla statement;

4.  both $C_{+1,2}(N)/N$ and $C_{-1,2}(N)/N$ converge.

Whenever these conditions hold, $$\boxed{\displaystyle
 \lim_{N\to\infty}\frac{C_{+1,2}(N)}N
 =\lim_{N\to\infty}\frac{C_{-1,2}(N)}N
 =\frac{\kappa_2}{4}.}
 \label{eq:final-density}$$

Equation [\[eq:reduction\]](#eq:reduction){reference-type="eqref" reference="eq:reduction"} shows that, for either fixed sign, the signed interval density has a limit if and only if $D_2(N)/N$ has a limit. The rigidity proposition forces any such limit to be zero, proving (i)$\Rightarrow$(ii)$\Rightarrow$(iii). Conversely, (iii) inserted into [\[eq:reduction\]](#eq:reduction){reference-type="eqref" reference="eq:reduction"} proves [\[eq:final-density\]](#eq:final-density){reference-type="eqref" reference="eq:final-density"} for both signs, hence (iii)$\Rightarrow$(iv)$\Rightarrow$(i).

Thus one signed density cannot converge to an unknown biased constant: its existence already forces the open unweighted correlation to cancel and forces both signs to have the same density. The result proves neither that the equivalent conditions hold nor that they fail.

# Exact executable protocol

The artifact uses a linear integer Möbius sieve and one streaming pass. For every start $1\le n\le2^{20}-2$, it verifies both pointwise Boolean identities. For every prefix $1\le N\le2^{20}$, it independently verifies their cumulative forms under the common endpoint [\[eq:common-endpoint\]](#eq:common-endpoint){reference-type="eqref" reference="eq:common-endpoint"}. It also checks all $524287$ even starts, aligns both signs with the locked RH-371 definition at every endpoint $N\le1024$, and freezes the following rows:

          $N$   $C_{+,2}$   $C_{-,2}$      $Q_2$   $U_2$   $V_2$    $D_2$
  ----------- ----------- ----------- ---------- ------- ------- --------
       $1024$        $66$        $82$      $330$   $-18$   $-14$    $-34$
      $65536$      $5293$      $5301$    $21155$   $-51$    $35$     $33$
    $1048576$     $84630$     $84346$   $338334$   $130$   $438$   $-382$

All entries are exact integer reproduction. In particular, their apparent small correlations are not used to infer $D_2=o(N)$, a limit, or any asymptotic rate. The source-lock manifest and closed result schema are checked separately.

# Route verdict, boundaries, and Gates

Route A is `GO`. The all-prefix identity, unconditional masked-term asymptotics, and exact equivalence with shift-two Cesàro Chowla form a standalone theorem edge. Route B is `STOP_SCOPED`. The two-site count is a scalar arithmetic statistic extracted from an adaptive capacity, not an intrinsic dynamical trace, and the required natural correlation remains open.

The scope is strict:

-   $C_{\sigma,2}$ is not a maximal exact-length-two run count;

-   neither convergence nor nonconvergence is proved unconditionally;

-   run levels $k\ge3$ require additional mixed-exponent correlations;

-   no conclusion follows for the alternating eight-run envelope or for convergence of $K_N/N$;

-   no growing-modulus, growing-clock, or uniform-in-clock Davenport theorem is used.

Gates A--E remain false/open. This paper does not construct a canonical intrinsic spectral determinant, a time-oriented scattering completion, a self-adjoint generator with an intrinsic $T\log T$ law, a von Mangoldt-weighted prime-power trace, or equality with the completed-zeta divisor. It does not identify Riemann zeros, construct a Hilbert--Polya operator, or prove the Riemann Hypothesis.

# Conclusion

The first nontrivial RH-371 run interval has an exact boundary. Its squarefree support and one-mask terms are unconditional; the only remaining quantity is the ordinary shift-two Möbius correlation. A logarithmic affine theorem does not by itself prove that natural cancellation, but it rules out any nonzero Cesàro limit. Consequently even the existence of one signed two-site density is precisely as hard as shift-two Cesàro Chowla. The next family-level step must track the genuinely mixed moments for run lengths $3$ through $8$, rather than replace them by naked distinct-shift correlations.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

**Data availability.** All source, exact outputs, tests, schema, and SHA-256 manifests are contained in the RH-376 repository directory.

**Ethics.** The study uses no human participants, animals, or personal data. No ethics approval was required.

**Author contributions.** The RH research program performed conceptualization, formal analysis, software, validation, and writing.

**Funding and conflicts.** No external funding or conflict of interest is declared.

**AI-assisted workflow.** Drafting and executable checking used the repository's documented multi-agent workflow. Mathematical claims are limited by the source locks, proofs, independent audits, and reproducible artifacts recorded here.
