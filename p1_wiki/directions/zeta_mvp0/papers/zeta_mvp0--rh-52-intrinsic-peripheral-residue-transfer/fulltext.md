---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-52-intrinsic-peripheral-residue-transfer"
canonical_tex: "zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/main.pdf"
source_sha256: "4e218afbe13241db1f90afefba3ba75b00c794ec1c876bab18f4ee1504371255"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Intrinsic Peripheral Residue Transfer from Weak Finite Factors Direct Haar-Range Bounds and a Sharp Half-Power Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The two-pole Hardy reduction for the noisy quadratic transfer operator left a finite-factor premise: the intrinsic Perron and parity residues must not regain a power-law loss on the adjacent Haar coupling ranges. The previous proposed route asked the finite left eigenfactors to inherit the sharp rounded-spike detail estimate $\left\lVert \ell_d\right\rVert_2=O(h\sigma^{-1})$, which would make the fine residues $O(\sqrt{\sigma})$. We prove that this sharp transfer is unnecessary.

  The strong/weak Ulam stability inherited from the postcritical tower/spike space gives finite peripheral normalizations satisfying $$|\lambda_{n,-}|\ge\frac12,\qquad
   \left\lVert r_{n,\pm}\right\rVert_\infty+\left\lVert \ell_{n,\pm}\right\rVert_1\le C$$ on every $h=o(\sigma^2)$ schedule. Direct Gaussian smoothing gives $$\left\lVert (E_{2n}-E_n)\mathcal P_\sigma\right\rVert_{L^1\to L^2}
   \le Ch\sigma^{-3/2},$$ $$\left\lVert (E_{2n}-E_n)\mathcal K_\sigma\right\rVert_{L^\infty\to L^2}
   \le Ch\sigma^{-1},\qquad
   \left\lVert \mathcal P_\sigma\right\rVert_{L^1\to L^2}\le C\sigma^{-1/2}.$$ We also prove $\left\lVert B\right\rVert_{\mathfrak S_2},\left\lVert C\right\rVert_{\mathfrak S_2}=\Theta(h\sigma^{-3/2})$. The exact block eigenvector identities then yield $$\frac{\left\lVert U^*P_{f,\pm}UB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}=O(1),
   \qquad
   \frac{\left\lVert CP_{c,-}\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert_{\mathfrak S_2}}=O(1),$$ while $CP_{c,+}=0$ exactly. Hence the sufficient residue premise in RH-50 closes without a sharp finite-detail theorem and without a polylogarithmic bound for the complete finite parity projector.

  There is a precise reason not to demand more from weak factor information: when $h/\sigma$ is small, $$\left\lVert (E_{2n}-E_n)\mathcal P_\sigma\right\rVert_{L^1\to L^2}
   =\Theta(h\sigma^{-3/2}).$$ Thus uniform left $L^1$ control alone cannot produce $O(h\sigma^{-1})$; the missing half power requires the actual postcritical spike geometry.

  A five-scale binary64 audit with $N\sigma=20.48$ reaches $N=40960$. The parity weak condition product decreases from $1.0968$ to $1.0385$, and the observed parity detail divided by $h\sigma^{-1}$ stays between $0.0465$ and $0.0553$. Fine Perron, fine parity, and right parity residues have fitted vanishing powers $0.5275$, $0.5500$, and $0.9362$. These stronger laws are floating evidence, not analytic claims. The remaining Stage A gates are the growing-horizon Hardy-energy budget and infinite-tail/cutoff validation. No arithmetic trace formula, zeta-zero identity, self-adjoint realization, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Intrinsic Peripheral Residue Transfer from Weak Finite Factors\
  Direct Haar-Range Bounds and a Sharp Half-Power Barrier
```

## Markdown 正文

**Keywords:** Ulam approximation; peripheral eigenfactor; Riesz residue; Haar detail; Gaussian smoothing; strong--weak stability; small-noise transfer operator.

**MSC 2020:** 37M25; 47A55; 47B65; 65R20; 37A30.

# Introduction

RH-49 and RH-50 reduced the remaining intrinsic-identification problem to two-pole Hilbert--Schmidt Hardy energies and explicit peripheral residues [@WangDirectional2026; @WangHardy2026]. Once the Perron and negative-parity poles are removed, the bulk range actions can be studied by Stein/Gramian certificates. RH-51 then showed that exact fixed-rank Stein factors are obstructed, but growing-horizon block certificates remain viable [@WangStructuredStein2026].

The present paper addresses the other premise in RH-50. Let $V_{2n}=V_n\oplus W_n$ be the adjacent Haar split and $$T=\begin{pmatrix}A&B\\C&D\end{pmatrix}$$ the fine finite Markov matrix. If $P_{f,s}=r_{f,s}\otimes\ell_{f,s}$, the normalized fine residue is $$\frac{\left\lVert U^*P_{f,s}UB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}.$$ The original route sought $\left\lVert \ell_{f,s,d}\right\rVert_2=O(h\sigma^{-1})$, because $\left\lVert B\right\rVert_{\mathfrak S_2}=\Theta(h\sigma^{-3/2})$ then gives $O(\sqrt{\sigma})$.

That target is true in the stored data, but it is stronger than the program needs. We instead use the weak norms naturally controlled by Keller--Liverani stability: right $L^\infty$ and left $L^1$. The resulting factor-detail bound is only $O(h\sigma^{-3/2})$, yet its power exactly cancels the Hilbert--Schmidt coupling denominator. The coarse right parity residue has a symmetric direct estimate. Both are uniform $O(1)$, already better than the polylogarithmic RH-50 premise.

The distinction is structural. We prove that the $L^1\to L^2$ target-detail norm really has scale $h\sigma^{-3/2}$. No proof based only on a uniform $L^1$ bound can recover the rounded-spike half power. The stronger result must use where the physical eigenfactor places its mass, not merely its total variation.

# Finite factors and adjacent Haar channels

Let $I=[0,1]$, $f(x)=1-u_{\rm c}x^2$, and $$k_\sigma(x,y)=
 \frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {Z_\sigma(x)}.$$ The observable and density operators are $$(\mathcal K_\sigma v)(x)=\int_I k_\sigma(x,y)v(y)\,dy,\qquad
 (\mathcal P_\sigma q)(y)=\int_I k_\sigma(x,y)q(x)\,dx.$$ For equal-cell averaging $E_n$, let $$G_{n,\sigma}=E_n\mathcal K_\sigma E_n\big|_{V_n}.$$ Its density matrix adjoint is the restriction to $V_n$ of $$\mathcal P_{n,\sigma}=E_n\mathcal P_\sigma.
 \label{eq:density-extension}$$ The source projection is unnecessary because each finite eigendensity already belongs to $V_n$.

For $V_{2n}=V_n\oplus W_n$, write $$G_{2n,\sigma}=\begin{pmatrix}A&B\\C&D\end{pmatrix}.$$ The coarse cell width is $h=1/n$. For $s\in\{+,-\}$, $$G_{m,\sigma}r_{m,s}=\lambda_{m,s}r_{m,s},\qquad
 G_{m,\sigma}^*\ell_{m,s}
 =\overline{\lambda_{m,s}}\ell_{m,s},\qquad
 \langle\ell_{m,s},r_{m,s}\rangle=1.$$ Right vectors are cell values and left vectors are cell masses. Thus $$\left\lVert \ell\right\rVert_1=\sum_j|\ell_j|,\quad
 \left\lVert \ell\right\rVert_2=\sqrt m\,\left\lVert \ell\right\rVert_{\ell^2},\quad
 \left\lVert r\right\rVert_\infty=\max_j|r_j|,\quad
 \left\lVert r\right\rVert_2=m^{-1/2}\left\lVert r\right\rVert_{\ell^2}.$$

# Uniform weak finite factors

The continuum spectral stability was established on the postcritical tower/spike space $\mathcal B$, with $L^1$ as weak norm [@WangBoundaryLayer2026; @WangLogConditioning2026]. The deterministic peripheral eigenvalues $1$ and $-1$ are simple and uniformly isolated from the remaining strong-space spectrum.

[\[lem:cell-spike\]]{#lem:cell-spike label="lem:cell-spike"} There is $C<\infty$ such that $$\left\lVert E_nq-q\right\rVert_{L^1}\le C\sqrt h\,\left\lVert q\right\rVert_{\mathcal B}.
 \label{eq:spike-cell-error}$$ On the regular bounded-variation component this improves to $Ch\left\lVert q\right\rVert_{\rm BV}$. Conditional expectation is $L^1$-contractive and variation diminishing after a density transfer step.

The regular estimate is the standard cellwise bounded-variation bound [@Li1976; @BoyarskyGora1997]. For a normalized one-sided square-root atom $a(t-s)_+^{-1/2}\chi(t-s)$, the cell containing $s$ has $L^1$ mass $O(\sqrt h)$. Away from it, summing the derivative bound gives $$h\int_h^\delta t^{-3/2}\,dt=O(\sqrt h).$$ There are finitely many postcritical atoms, with coefficients controlled by the $\mathcal B$-norm. Conditional expectation is an $L^1$ contraction and does not increase variation of the regular representative.

[\[thm:weak-factors\]]{#thm:weak-factors label="thm:weak-factors"} Let $\sigma\downarrow0$ and $h=h(\sigma)$ satisfy $$h=o(\sigma^2).
 \label{eq:proof-schedule}$$ For sufficiently small $\sigma$, the finite operators have exactly two simple peripheral branches near $1$ and $-1$. They can be normalized so that $$\begin{aligned}
 r_{n,+}&=\mathbf1,&\left\lVert \ell_{n,+}\right\rVert_1&=1,\\
 |\lambda_{n,-}|&\ge\frac12,&
 \left\lVert r_{n,-}\right\rVert_\infty+\left\lVert \ell_{n,-}\right\rVert_1&\le C.
 \label{eq:weak-factors}\end{aligned}$$

RH-14 gives uniform Lasota--Yorke estimates on $\mathcal B$, compact strong-to-weak embedding, and $$\left\lVert \mathcal P_\sigma-\mathcal P_0\right\rVert_{\mathcal B\to L^1}=o(1).$$ By [\[lem:cell-spike\]](#lem:cell-spike){reference-type="ref" reference="lem:cell-spike"} and [\[eq:density-extension\]](#eq:density-extension){reference-type="eqref" reference="eq:density-extension"}, $$\left\lVert \mathcal P_{n,\sigma}-\mathcal P_\sigma\right\rVert_{\mathcal B\to L^1}
 \le C\sqrt h.$$ The variation-diminishing property preserves the same Lasota--Yorke ledger for $E_n\mathcal P_\sigma$. Therefore $\mathcal P_{n,\sigma}\to\mathcal P_0$ strongly-to-weakly along [\[eq:proof-schedule\]](#eq:proof-schedule){reference-type="eqref" reference="eq:proof-schedule"}. Keller--Liverani stability preserves the ranks of the two isolated projectors and gives weak convergence of their ranges [@KellerLiverani1999]. The dual statement applied to the bounded component-sign observable controls the right eigenfunctional. The deterministic left component densities have finite $L^1$ norm and pair nontrivially with that sign. Biorthogonal normalization gives [\[eq:weak-factors\]](#eq:weak-factors){reference-type="eqref" reference="eq:weak-factors"}. Perron normalization follows exactly from stochasticity and positivity.

The schedule is precisely $n\sigma^2\to\infty$, already adopted for the intrinsic small-noise limit. No $L^2$ contour-resolvent upper enters the proof. Weak factors stay bounded while their $L^2$ projector norms may grow logarithmically.

# Direct smoothing and coupling scales

Put $Q_n=E_{2n}-E_n$.

[\[lem:smoothing\]]{#lem:smoothing label="lem:smoothing"} For $h/\sigma$ sufficiently small, $$\begin{aligned}
 \left\lVert Q_n\mathcal P_\sigma\right\rVert_{L^1\to L^2}
 &\le C h\sigma^{-3/2},\label{eq:target-detail}\\
 \left\lVert Q_n\mathcal K_\sigma\right\rVert_{L^\infty\to L^2}
 &\le C h\sigma^{-1},\label{eq:source-detail}\\
 \left\lVert \mathcal P_\sigma\right\rVert_{L^1\to L^2}
 &\le C\sigma^{-1/2}.\label{eq:l1-l2}\end{aligned}$$

For each $x$, target-cell Poincaré gives $$\left\lVert Q_n k_\sigma(x,\cdot)\right\rVert_2
 \le\frac h\pi\left\lVert \partial_yk_\sigma(x,\cdot)\right\rVert_2
 \le Ch\sigma^{-3/2}.$$ Minkowski proves [\[eq:target-detail\]](#eq:target-detail){reference-type="eqref" reference="eq:target-detail"}. For $\left\lVert v\right\rVert_\infty\le1$, $$|\partial_x\mathcal K_\sigma v(x)|
 \le\int_I|\partial_xk_\sigma(x,y)|\,dy
 \le C\sigma^{-1}.$$ Source-cell Poincaré proves [\[eq:source-detail\]](#eq:source-detail){reference-type="eqref" reference="eq:source-detail"}. Finally, $$\left\lVert \mathcal P_\sigma q\right\rVert_2
 \le\int_I|q(x)|\left\lVert k_\sigma(x,\cdot)\right\rVert_2\,dx
 \le C\sigma^{-1/2}\left\lVert q\right\rVert_1.$$

[\[prop:couplings\]]{#prop:couplings label="prop:couplings"} There are $c,C,a_0,\sigma_0>0$ such that $$c h\sigma^{-3/2}
 \le\left\lVert B\right\rVert_{\mathfrak S_2},\left\lVert C\right\rVert_{\mathfrak S_2}
 \le C h\sigma^{-3/2}
 \label{eq:coupling-scales}$$ when $0<\sigma<\sigma_0$ and $h/\sigma<a_0$.

The upper bounds are the target/source Poincaré estimates. RH-50 proved the $B$ lower bound. For $C$, choose an interior source rectangle on which $|f'|$ is bounded below and the row normalizer is exponentially close to one. There $$\iint|\partial_xk_\sigma(x,y)|^2\,dx\,dy\ge c\sigma^{-3}.$$ The leading source-Haar coefficient is a fixed nonzero first moment times $h\partial_xk_\sigma$. Summing its square gives $c h^2\sigma^{-3}$; the remainder is relative $O(h/\sigma)$.

# Direct closure of the peripheral residues

For a fine branch write $$r_f=\begin{pmatrix}r_c\\r_d\end{pmatrix},\qquad
 \ell_f=\begin{pmatrix}\ell_c\\\ell_d\end{pmatrix}.$$ The left block eigenvector equation gives $$B^*\ell_c=(\overline\lambda-D^*)\ell_d,
 \qquad
 U^*P_fUB
 =r_c\otimes((\overline\lambda-D^*)\ell_d).
 \label{eq:fine-residue}$$

[\[thm:residue-closure\]]{#thm:residue-closure label="thm:residue-closure"} Along every schedule [\[eq:proof-schedule\]](#eq:proof-schedule){reference-type="eqref" reference="eq:proof-schedule"}, $$\boxed{
 \frac{\left\lVert U^*P_{f,s}UB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}
 =O(1),\qquad s\in\{+,-\}.}
 \label{eq:fine-O1}$$ On the coarse right, $$\boxed{
 CP_{c,+}=0,\qquad
 \frac{\left\lVert CP_{c,-}\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert_{\mathfrak S_2}}=O(1).}
 \label{eq:right-O1}$$

The finite density eigenrelation and [\[lem:smoothing\]](#lem:smoothing){reference-type="ref" reference="lem:smoothing"} give $$\left\lVert \ell_d\right\rVert_2
 =
 |\lambda|^{-1}\left\lVert Q_n\mathcal P_\sigma\ell_f\right\rVert_2
 \le C h\sigma^{-3/2}\left\lVert \ell_f\right\rVert_1.$$ The last factor, $\left\lVert r_c\right\rVert_2$, $|\lambda|$, and $\left\lVert D\right\rVert$ are uniformly bounded by [\[thm:weak-factors\]](#thm:weak-factors){reference-type="ref" reference="thm:weak-factors"}. Insert this estimate into [\[eq:fine-residue\]](#eq:fine-residue){reference-type="eqref" reference="eq:fine-residue"} and divide by the $B$ lower bound.

The Perron right vector is constant and $C\mathbf1=0$. For parity, $$\left\lVert Cr_{c,-}\right\rVert_2
 \le C h\sigma^{-1}\left\lVert r_{c,-}\right\rVert_\infty$$ by [\[eq:source-detail\]](#eq:source-detail){reference-type="eqref" reference="eq:source-detail"}, while $$\left\lVert \ell_{c,-}\right\rVert_2
 \le C\sigma^{-1/2}\left\lVert \ell_{c,-}\right\rVert_1$$ by the finite eigenrelation and [\[eq:l1-l2\]](#eq:l1-l2){reference-type="eqref" reference="eq:l1-l2"}. Hence $$\left\lVert CP_{c,-}\right\rVert_{\mathfrak S_2}
 =\left\lVert Cr_{c,-}\right\rVert_2\left\lVert \ell_{c,-}\right\rVert_2
 \le C h\sigma^{-3/2}.$$ Divide by the $C$ lower bound.

The explicit Perron/parity residue part of the RH-50 dyadic Hardy-control condition is uniformly bounded. Neither $\left\lVert \ell_d\right\rVert=O(h\sigma^{-1})$ nor a polylogarithmic upper for the complete finite projector is required for this range-restricted result.

Multiplying the separate weak-factor smoothing bounds gives only $\left\lVert P_{n,-}\right\rVert_{L^2\to L^2}=O(\sigma^{-1/2})$. The theorem avoids this coarse global estimate: each range action gains a complementary power before the factors are multiplied.

# A sharp half-power barrier

[\[thm:barrier\]]{#thm:barrier label="thm:barrier"} There are $c,C,a_0,\sigma_0>0$ such that $$c h\sigma^{-3/2}
 \le\left\lVert Q_n\mathcal P_\sigma\right\rVert_{L^1\to L^2}
 \le C h\sigma^{-3/2}
 \label{eq:barrier}$$ when $0<\sigma<\sigma_0$ and $h/\sigma<a_0$. Therefore uniform left $L^1$ information alone cannot yield $\left\lVert \ell_d\right\rVert=O(h\sigma^{-1})$.

The upper bound is [\[eq:target-detail\]](#eq:target-detail){reference-type="eqref" reference="eq:target-detail"}. Choose an interior source point $x_0$ and approximate a unit point mass there by $L^1$ densities. Their images converge in $L^2$ to the Gaussian row $k_\sigma(x_0,\cdot)$. On an interior target window, $$\left\lVert \partial_yk_\sigma(x_0,\cdot)\right\rVert_2\ge c\sigma^{-3/2}.$$ The adjacent Haar Taylor expansion, summed over cells in that window, gives $$\left\lVert Q_nk_\sigma(x_0,\cdot)\right\rVert_2
 \ge c h\sigma^{-3/2}$$ when $h/\sigma$ is small. Taking the operator supremum proves the lower bound.

The physical factors are not arbitrary $L^1$ inputs. Their postcritical weights produce structure that this operator norm cannot see. RH-50 proved the continuum rounded-spike derivative scale $\Theta(\sigma^{-1})$. Transferring it to intrinsic finite factors may recover the optional $O(\sqrt\sigma)$ residue law, but [\[thm:barrier\]](#thm:barrier){reference-type="ref" reference="thm:barrier"} identifies the extra information required.

# Five-scale intrinsic-factor audit

The experiment uses the sparse eight-sigma-cutoff family and exact Haar nesting of RH-49 and RH-50. The fine resolution is $$N\sigma=20.48,$$ and the largest dimension is $40960$. This fixed resolution is a production diagnostic, not a realization of $n\sigma^2\to\infty$.

::: {#tab:audit}
    $\sigma$     $N$   weak cond.   Perron detail   parity detail   fine $+$   fine $-$   right $-$
  ---------- ------- ------------ --------------- --------------- ---------- ---------- -----------
      0.0100    2048       1.0968          0.0441          0.0553     0.0462     0.0574      0.0315
      0.0040    5120       1.0765          0.0422          0.0511     0.0281     0.0339      0.0130
      0.0020   10240       1.0604          0.0411          0.0489     0.0195     0.0230     0.00675
      0.0010   20480       1.0485          0.0405          0.0475     0.0136     0.0159     0.00356
      0.0005   40960       1.0385          0.0401          0.0465    0.00951     0.0110     0.00191

  : Five-scale audit. The weak condition is $\left\lVert r\right\rVert_\infty\left\lVert \ell\right\rVert_1$ for parity. Detail columns are normalized by $h\sigma^{-1}$; the final columns are residue actions.
:::

The parity weak products are $$1.0968,\ 1.0765,\ 1.0604,\ 1.0485,\ 1.0385,$$ while the Perron products equal one to rounding. The parity values of $\left\lVert P\right\rVert_-^2/\log(1/\sigma)$ decrease from $0.272$ to $0.208$.

The finite detail is much sharper than the weak theorem: $$0.0401\le
 \frac{\left\lVert \ell_{f,+,d}\right\rVert_2}{h\sigma^{-1}}\le0.0441,
\qquad
 0.0465\le
 \frac{\left\lVert \ell_{f,-,d}\right\rVert_2}{h\sigma^{-1}}\le0.0553.$$ The fitted powers of these ratios are slightly positive, so no growth is observed.

The direct residue fits are $$\begin{aligned}
 \text{fine Perron}&:\ \sigma^{0.52752},&
 \text{fine parity}&:\ \sigma^{0.55003},\\
 \text{right parity}&:\ \sigma^{0.93624}.\end{aligned}$$ The right Perron action is below $2.6\times10^{-15}$ at every scale. The normalized coupling constants are nearly fixed: $$0.0941\le\frac{\left\lVert B\right\rVert_{\mathfrak S_2}}{h\sigma^{-3/2}}\le0.0955,
\qquad
 0.16714\le\frac{\left\lVert C\right\rVert_{\mathfrak S_2}}{h\sigma^{-3/2}}\le0.16715.$$ One-level parity comparisons have maximum left $L^1$ error $8.21\times10^{-5}$, right $L^\infty$ error $2.90\times10^{-4}$, and relative projector defect $1.46\times10^{-4}$.

![Intrinsic peripheral transfer audit. (a) Weak factors remain conditioned. (b) Actual details follow $h\sigma^{-1}$, while both couplings follow $h\sigma^{-3/2}$. (c) All residues vanish, stronger than the analytic $O(1)$ theorem. (d) Adjacent intrinsic factors remain stable across one Haar level.](<../../../../../zeta_mvp0/papers/RH-52-intrinsic-peripheral-residue-transfer/figures/factor_residue_transfer.pdf>){#fig:audit width="\\textwidth"}

# Roadmap consequence

The original A2 milestone requested sharp finite-detail transfer and a polylogarithmic coarse parity projector. replaces both with weaker factor information and a stronger targeted conclusion: every residue action entering RH-50 is $O(1)$.

Sufficient A2 residue gate

:   Closed analytically on the adopted $n\sigma^2\to\infty$ schedule.

Original $O(\sqrt\sigma)$ target

:   Not closed analytically. It is supported by the audit but blocked from weak-norm-only proofs by [\[thm:barrier\]](#thm:barrier){reference-type="ref" reference="thm:barrier"}.

Complete finite projector

:   No longer required for the range-restricted RH-50 residue ledger.

Remaining Stage A work

:   A1 still needs a growing-horizon Hardy/Stein trace budget. A3 still needs deterministic or interval infinite-tail and sparse-cutoff validation.

The next scheduled paper is RH-53, focused on the infinite Hardy tail and the sparse/full Gaussian cutoff bridge.

## No arithmetic or Hilbert--Pólya conclusion

The TPC series remains an independent twin-prime and prime-correlation program and is not an assumption here. Nothing in this paper constructs a prime-power trace formula, identifies a zeta zero, builds a self-adjoint Hilbert--Pólya operator, derives a $T\log T$ law, proves the Riemann hypothesis, or proves a twin-prime statement.

# Reproducibility and theorem boundary

The archive contains the algebra in , the pilot and certificate builders in , the figure, tests, result ledgers, dependency hashes, and archive verification. Principal commands:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q
    OPENBLAS_NUM_THREADS=16 OMP_NUM_THREADS=16 \
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_factor_transfer_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_factor_transfer_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py

The weak-factor theorem, direct kernel bounds, two-sided coupling scales, uniform residue closure, and half-power barrier are analytic. The sharper intrinsic $h\sigma^{-1}$ detail law, vanishing residue powers, and adjacent defects are floating binary64 evidence. No interval constant is claimed for the stored matrices.
