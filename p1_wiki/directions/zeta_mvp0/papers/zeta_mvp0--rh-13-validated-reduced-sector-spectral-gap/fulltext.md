---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-13-validated-reduced-sector-spectral-gap"
canonical_tex: "zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/validated-reduced-sector-spectral-gaps.pdf"
source_sha256: "6837b90131b836a118e44577b2220b28f67cf52fecdb42150967c52c350c8291"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Validated Reduced-Sector Spectral Gaps at a Quadratic Band-Merging Map: A Computer-Assisted Proof of Postcritical Zeta Noncancellation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/validated-reduced-sector-spectral-gaps.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the algebraic band-merging parameter of $f_u(x)=1-u x^2$, let $u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0$, put $r=u_{\mathrm c}-1$, and set $\lambda=2u_{\mathrm c}r=1.678573510428\ldots$. A preceding analytic-circle-lift construction proved the exact component-zeta factorization $$\mathcal Z(z)=\frac{D_{2,-}(z)}{D_{1,+}(z)}
   \frac{1-z/\lambda}{1-z/\lambda^2}.$$ After removing the Perron factor $1-z$ from $D_{1,+}$, the only unresolved point was the reduced-sector disk bound $$r_1<\lambda^{-2},\qquad r_2<\lambda^{-2},$$ where $r_1$ is the non-Perron spectral radius in the even $\beta=1$ sector and $r_2$ is the odd $\beta=2$ spectral radius. That bound would prevent cancellation of both explicit postcritical factors. We prove it by a computer-assisted argument with complete analytic tail estimates.

  The two inverse branches have common square $$t(x)=\frac{1-\sqrt{(1-x)/u_{\mathrm c}}}{u_{\mathrm c}}.$$ Deck parity turns the circle operators into coefficient-decimating Wiener--Taylor operators on the disk $|x|<R$, $R=0.7$: $$\begin{aligned}
   (\mathcal T_1v)(x)&=2a(x)\sum_{k\ge0}c_{2k}\frac{t(x)^k}{R^{2k}},\\
   (\mathcal T_2v)(x)&=b(x)\sum_{k\ge0}c_{2k+1}\frac{t(x)^k}{R^{2k+1}},
   \qquad v(x)=\sum_{j\ge0}c_j(x/R)^j,\end{aligned}$$ with explicit analytic weights $a,b$. The exact circle-mean functional removes the Perron mode from $\mathcal T_1$.

  Using dimension $N=50$, 100 Taylor coefficients, a Cauchy radius $0.9$, and 100-decimal Arb ball arithmetic, we certify $$\|\mathcal T_{1,0}^3\|\le0.03582019310742
   <\lambda^{-6}=0.0447051759618781\ldots,$$ $$\|\mathcal T_{2}^2\|\le0.06463843745472
   <\lambda^{-4}=0.125961707473977\ldots.$$ Hence $$r_1\le0.3296420762932<\lambda^{-2},
   \qquad
   r_2\le0.2542409043697<\lambda^{-2}.$$ The inequalities remain certified for dimensions $30,40,50,60,70$.

  It follows unconditionally that the centered weighted zeta function has an uncanceled simple zero at $z=\lambda$, an uncanceled simple pole at $z=\lambda^2$, and a zero-free residual factor on $|z|<3.03359$. Moreover $$q_n=1-\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).$$ Floating-point eigenvalues near $0.20788030$ and $0.15252824$ are reported only as diagnostics; the theorem uses the larger validated norm bounds.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Validated Reduced-Sector Spectral Gaps**\
  **at a Quadratic Band-Merging Map:**\
  A Computer-Assisted Proof of Postcritical Zeta Noncancellation
```

## Markdown 正文

**Keywords:** computer-assisted proof; dynamical zeta function; transfer operator; Wiener algebra; Taylor approximation; interval arithmetic; postcritical orbit; quadratic map.

**MSC 2020:** 37E10; 37C30; 37D20; 47A10; 65G20.

# Introduction {#sec:introduction}

An explicit factor in a meromorphic identity is not automatically an actual zero or pole. A zero of the remaining denominator can cancel a proposed numerator, and a zero of the remaining numerator can cancel a proposed pole. For a dynamical zeta function this distinction is spectral: cancellation is equivalent to a transfer-operator eigenvalue at one prescribed reciprocal location.

The preceding postcritical-factorization paper studied the central component of the square of the quadratic map $f_u(x)=1-u x^2$ at an algebraic band-merging parameter [@WangPostcritical2026]. A two-sheeted cosine cover removed the critical point and produced an analytic expanding circle map. Ordinary and deck-twisted flat traces gave the exact identity $$\label{eq:prior-trace}
 q_n=E_{1,n}-O_{2,n}-\lambda^{-n}+\lambda^{-2n},$$ and hence $$\label{eq:prior-factorization}
 \mathcal Z(z)=\frac{D_{2,-}(z)}{D_{1,+}(z)}
 \frac{1-z/\lambda}{1-z/\lambda^2}.$$ The odd second-order determinant was proved nonzero at $z=\lambda$ by a strict pressure estimate. Thus the claim that the centered zeta has a simple zero at $\lambda$ was reduced to excluding the single non-Perron eigenvalue $\lambda^{-1}$ from the even first-order operator.

Numerically, the situation looked much stronger. The leading reduced resonances stabilized near $$\label{eq:numerical-resonances-intro}
 0.20788030,
 \qquad
 0.15252824,$$ both far below $$\label{eq:target-intro}
 \lambda^{-2}=0.3549108444\ldots.$$ The open conjecture was therefore the disk bound $$\label{eq:conjecture-intro}
 r_1<\lambda^{-2},
 \qquad
 r_2<\lambda^{-2}.$$ Unlike exclusion at one point, this stronger statement simultaneously controls the numerator at $\lambda$, the denominator at $\lambda^2$, and the remainder in the periodic coefficient expansion.

The aim here is to prove [\[eq:conjecture-intro\]](#eq:conjecture-intro){reference-type="eqref" reference="eq:conjecture-intro"}. The argument is computer-assisted, but its infinite-dimensional part is not delegated to a black-box eigensolver. We derive exact Taylor formulas for both transfer sectors, choose a concrete Wiener algebra, remove the Perron mode by an exact linear functional, and bound the omitted rows and columns by geometric and Cauchy estimates. Arb ball arithmetic is used only for the finite matrices, the algebraic parameter, and directed evaluation of explicit inequalities [@Johansson2017].

## Main results and logical status {#main-results-and-logical-status .unnumbered}

1.  The even $\beta=1$ and odd $\beta=2$ circle operators are conjugated to two explicit coefficient-decimating operators on a Wiener--Taylor space.

2.  The normalized circle mean is an exact left eigenfunctional of the first operator. Eliminating the constant Taylor coefficient gives a concrete realization $\mathcal T_{1,0}$ of the entire non-Perron sector.

3.  A finite-rank projection at dimension $50$ has rigorously bounded operator errors $$\varepsilon_1\le5.237746723\times10^{-4},
      \qquad
      \varepsilon_2\le2.407483932\times10^{-4}.$$

4.  Arb interval matrix products and analytic tails prove $$\|\mathcal T_{1,0}^3\|<\lambda^{-6},
      \qquad
      \|\mathcal T_2^2\|<\lambda^{-4}.$$ This is the computer-assisted theorem. The stored certificate contains every interval, software version, parameter, and source hash.

5.  The reduced-sector conjecture is therefore unconditional. The residual Fredholm quotient is holomorphic and nonzero on a certified disk of radius $3.03359>\lambda^2$.

6.  Consequently $z=\lambda$ is an actual simple zero, $z=\lambda^2$ is an actual simple pole, and $$q_n=1-\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).$$

7.  The floating-point resonance estimates in [\[eq:numerical-resonances-intro\]](#eq:numerical-resonances-intro){reference-type="eqref" reference="eq:numerical-resonances-intro"} are not used in any certified inequality. They only cross-check the operator representation and explain why the validated bounds have a comfortable margin.

# The lifted dynamics and the remaining spectral problem {#sec:background}

Let $u_{\mathrm c}$ be the real root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and set $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r.$$ Numerically, $$\label{eq:constants-numerical}
 u_{\mathrm c}=1.54368901269207636157\ldots,
 \qquad
 \lambda=1.67857351042832226510\ldots.$$ Let $$\label{eq:S}
 S=f_{u_{\mathrm c}}^2|_{[-r,r]},
 \qquad
 S(x)=-r+2u_{\mathrm c}^2x^2-u_{\mathrm c}^3x^4.$$ The two half intervals are full branches onto $[-r,r]$.

The cosine cover $$\label{eq:cover}
 \pi(\theta)=-r\cos\theta,
 \qquad
 \pi:\mathbb T\to[-r,r]$$ lifts $S$ to an analytic, orientation-preserving degree-two expanding circle map $F$ satisfying $$\label{eq:semiconjugacy}
 \pi\circ F=S\circ\pi,
 \qquad
 F(\theta+\pi)=F(\theta),
 \qquad
 \min F'=\lambda.$$ The equality in the middle is on the circle; a real lift gains $2\pi$.

For $\beta=1,2$, let $$\label{eq:circle-transfer}
 (\mathcal L_\beta\varphi)(\theta)
 =\sum_{F(\eta)=\theta}\frac{\varphi(\eta)}{F'(\eta)^\beta}.$$ The deck involution $\theta\mapsto-\theta$ commutes with $F$ and splits each operator into even and odd sectors. Denote their Fredholm determinants by $D_{\beta,+}$ and $D_{\beta,-}$. Standard analytic expanding-map theory identifies their zeros with reciprocals of the corresponding Ruelle resonances [@Ruelle1976; @Baladi2000; @Baladi2018].

The $\beta=1$ even sector has a simple Perron eigenvalue one. Write $$\label{eq:perron-removal}
 D_{1,+}(z)=(1-z)\widetilde D_{1,+}(z).$$ Let $r_1$ be the spectral radius after this Perron mode is removed, and let $r_2$ be the spectral radius of $\mathcal L_{2,-}$. The factorization [\[eq:prior-factorization\]](#eq:prior-factorization){reference-type="eqref" reference="eq:prior-factorization"} can then be written $$\label{eq:centered-factorization}
 H(z):=(1-z)\mathcal Z(z)
 =\frac{1-z/\lambda}{1-z/\lambda^2}G(z),
 \qquad
 G(z)=\frac{D_{2,-}(z)}{\widetilde D_{1,+}(z)}.$$ Proving [\[eq:conjecture-intro\]](#eq:conjecture-intro){reference-type="eqref" reference="eq:conjecture-intro"} makes both determinants in $G$ zero-free on a disk strictly larger than $|z|\le\lambda^2$.

# Exact Wiener--Taylor sector representations {#sec:taylor-representation}

The full-branch symmetry makes the transfer operators much simpler than the piecewise arccosine formula for $F$ suggests. Define $$\label{eq:s-t}
 s(x)=\sqrt{\frac{1-x}{u_{\mathrm c}}},
 \qquad
 t(x)=\frac{1-s(x)}{u_{\mathrm c}}.$$ For real $x\in[-r,r]$, the two inverse branches of $S$ are $$\label{eq:inverse-branches}
 g_\pm(x)=\pm\sqrt{t(x)}.$$ The function $t=g_+^2=g_-^2$ is analytic on $|x|<1$ even though the individual square roots branch at the endpoint preimage.

Put $$\begin{aligned}
 a(x)
 &=\frac{\sqrt{(1+s(x))(r+s(x))}}{4s(x)},
 \label{eq:a-weight}\\
 b(x)
 &=\frac{a(x)}{2u_{\mathrm c}^2s(x)}.
 \label{eq:b-weight}\end{aligned}$$ For $|x|<1$, the quantity $1-x$ lies in the right half-plane and the chosen square root has positive real part. Hence $s$, $a$, and $b$ are analytic on that disk; in particular none of the displayed denominators vanishes there. The derivative formula for the circle lift gives $$\label{eq:a-derivative}
 a(x)=\frac1{F'(\eta)}
 =\frac{\sqrt{u_{\mathrm c}(2-u_{\mathrm c}t(x))(1-t(x))}}
 {4(1-u_{\mathrm c}t(x))}$$ at either lift preimage $\eta$ over $g_+(x)$ or $g_-(x)$.

## Parity conjugacies

Every analytic even deck function can be written $$\label{eq:even-coordinate}
 \varphi_+(\theta)=v(-r\cos\theta),$$ while every analytic odd deck function can be written $$\label{eq:odd-coordinate}
 \varphi_-(\theta)=\sin\theta\,v(-r\cos\theta).$$ The division by $\sin\theta$ in the odd case is analytic at $0$ and $\pi$. Indeed, deck oddness gives locally $\varphi_-(\theta)=\theta h(\theta^2)$ at $0$ and the analogous expansion in $\theta-\pi$ at $\pi$. Dividing by the corresponding expansion of $\sin\theta$ leaves an even analytic germ, hence an analytic germ in $x=-r\cos\theta$ at each branch value.

[\[prop:sector-operators\]]{#prop:sector-operators label="prop:sector-operators"} Under [\[eq:even-coordinate\]](#eq:even-coordinate){reference-type="eqref" reference="eq:even-coordinate"}, the even $\beta=1$ operator is conjugate to $$\label{eq:T1-branches}
 (\mathcal T_1v)(x)=a(x)\bigl[v(\sqrt{t(x)})+v(-\sqrt{t(x)})\bigr].$$ Under [\[eq:odd-coordinate\]](#eq:odd-coordinate){reference-type="eqref" reference="eq:odd-coordinate"}, the odd $\beta=2$ operator is conjugate to $$\label{eq:T2-branches}
 (\mathcal T_2v)(x)=
 \frac{v(\sqrt{t(x)})-v(-\sqrt{t(x)})}
 {S'(\sqrt{t(x)})F'(\eta)}.$$ At $t(x)=0$, the quotient is understood by its removable analytic continuation. If $v(x)=\sum_{j\ge0}v_jx^j$, these formulas become $$\begin{aligned}
 (\mathcal T_1v)(x)
 &=2a(x)\sum_{k\ge0}v_{2k}t(x)^k,
 \label{eq:T1-series}\\
 (\mathcal T_2v)(x)
 &=b(x)\sum_{k\ge0}v_{2k+1}t(x)^k.
 \label{eq:T2-series}\end{aligned}$$

For a target lift $\theta$, the two $F$-preimages project to $\pm\sqrt{t(x)}$. Their circle derivatives are equal because $F'(\eta)^2$ depends only on the square of the interval coordinate. Thus [\[eq:T1-branches\]](#eq:T1-branches){reference-type="eqref" reference="eq:T1-branches"} follows immediately from [\[eq:circle-transfer\]](#eq:circle-transfer){reference-type="eqref" reference="eq:circle-transfer"}.

For the odd sector, differentiating the semiconjugacy gives the signed identity $$\label{eq:sine-derivative}
 F'(\eta)=S'(y)\frac{\sin\eta}{\sin\theta},
 \qquad y=\pi(\eta).$$ After dividing the output by $\sin\theta$, each $\beta=2$ term becomes $v(y)/[S'(y)F'(\eta)]$. Since $S'$ is odd and $F'$ is equal on the two preimages, their sum is [\[eq:T2-branches\]](#eq:T2-branches){reference-type="eqref" reference="eq:T2-branches"}. Finally $$\label{eq:Sprime-g}
 S'(\sqrt t)=4u_{\mathrm c}^2\sqrt t(1-u_{\mathrm c}t)$$ and the odd Taylor difference contributes a factor $2\sqrt t$. This gives the weight [\[eq:b-weight\]](#eq:b-weight){reference-type="eqref" reference="eq:b-weight"} and proves [\[eq:T1-series\]](#eq:T1-series){reference-type="eqref" reference="eq:T1-series"} and [\[eq:T2-series\]](#eq:T2-series){reference-type="eqref" reference="eq:T2-series"}.

## The Wiener algebra and Perron removal

Fix $$\label{eq:R-choice}
 R=\frac7{10}>r$$ and let $\mathcal A_R$ be the Wiener algebra $$\label{eq:wiener-space}
 \mathcal A_R=\left\{
 v(x)=\sum_{j\ge0}c_j(x/R)^j:
 \|v\|_R:=\sum_{j\ge0}|c_j|<\infty
 \right\}.$$ In these scaled coefficients, $$\begin{aligned}
 (\mathcal T_1v)(x)
 &=2a(x)\sum_{k\ge0}c_{2k}\frac{t(x)^k}{R^{2k}},
 \label{eq:T1-scaled}\\
 (\mathcal T_2v)(x)
 &=b(x)\sum_{k\ge0}c_{2k+1}\frac{t(x)^k}{R^{2k+1}}.
 \label{eq:T2-scaled}\end{aligned}$$

The Taylor coefficients of $t$ are nonnegative. Indeed, $$\label{eq:t-positive}
 t(x)=\frac1u_{\mathrm c}-u_{\mathrm c}^{-3/2}\sqrt{1-x},$$ its constant coefficient is positive, and every nonconstant coefficient of $-\sqrt{1-x}$ is positive. Therefore $$\label{eq:t-norm}
 \|t\|_R=t(R)=0.362223396291970\ldots,
 \qquad
 \tau:=\frac{\|t\|_R}{R^2}
 =0.739231421004020\ldots<1.$$ It follows directly from [\[eq:T1-scaled\]](#eq:T1-scaled){reference-type="eqref" reference="eq:T1-scaled"} and [\[eq:T2-scaled\]](#eq:T2-scaled){reference-type="eqref" reference="eq:T2-scaled"} that the operators are nuclear on $\mathcal A_R$, not merely compact. In fact their nonzero column norms are bounded respectively by $$\label{eq:full-column-decay}
 2\|a\|_R\tau^k,
 \qquad
 \frac{\|b\|_R}{R}\tau^k,
 \qquad k\ge0,$$ and these bounds are summable because $\tau<1$.

The normalized circle mean of the even lift is the explicit functional $$\label{eq:mean-functional}
 \ell(v)=\frac1{2\pi}\int_0^{2\pi}v(-r\cos\theta)\,d\theta
 =\sum_{k\ge0}m_{2k}c_{2k},$$ where $$\label{eq:moments}
 m_{2k}=\binom{2k}{k}\left(\frac{r}{2R}\right)^{2k},
 \qquad m_{2k+1}=0.$$ Since $\mathcal L_1$ preserves Lebesgue integral, $$\label{eq:mean-invariance}
 \ell(\mathcal T_1v)=\ell(v).$$ Every eigenfunction with eigenvalue different from one therefore belongs to $\ker\ell$.

Parameterize $\ker\ell$ by $d=(c_1,c_2,\ldots)\in\ell^1$ and eliminate $$\label{eq:c0-elimination}
 c_0=-\sum_{j\ge1}m_jd_j.$$ The resulting reduced operator $\mathcal T_{1,0}$ has columns $$\label{eq:T10-columns}
 C^{(1)}_{2k}(x)
 =2a(x)\left[\frac{t(x)^k}{R^{2k}}-m_{2k}\right],
 \qquad k\ge1,$$ and $C^{(1)}_{2k+1}=0$. Output coordinates are the nonconstant scaled Taylor coefficients. The odd second-order operator has columns $$\label{eq:T2-columns}
 C^{(2)}_{2k+1}(x)=b(x)\frac{t(x)^k}{R^{2k+1}},
 \qquad
 C^{(2)}_{2k}=0.$$ The reduced first-sector columns are summable as well, since $m_{2k}\le(r/R)^{2k}$ and $r/R<1$.

[\[cor:spectral-identification\]]{#cor:spectral-identification label="cor:spectral-identification"} The nonzero spectrum of $\mathcal T_{1,0}$ is the non-Perron even $\beta=1$ spectrum, and the nonzero spectrum of $\mathcal T_2$ is the odd $\beta=2$ spectrum. Moreover $$\label{eq:det-identification}
 \det(I-z\mathcal T_{1,0})=\widetilde D_{1,+}(z),
 \qquad
 \det(I-z\mathcal T_2)=D_{2,-}(z).$$

Because $R>r$, the maps $$J_+v(\theta)=v(-r\cos\theta),
 \qquad
 J_-v(\theta)=\sin\theta\,v(-r\cos\theta)$$ send $\mathcal A_R$ continuously and injectively into functions holomorphic on a complex strip about the circle. The endpoint argument preceding [\[prop:sector-operators\]](#prop:sector-operators){reference-type="ref" reference="prop:sector-operators"} shows that these are precisely the two local parity coordinates, and that proposition gives the intertwining identities $J_+\mathcal T_1=\mathcal L_{1,+}J_+$ and $J_-\mathcal T_2=\mathcal L_{2,-}J_-$.

The summable geometric column estimates [\[eq:full-column-decay\]](#eq:full-column-decay){reference-type="eqref" reference="eq:full-column-decay"} make both Wiener operators nuclear of order zero. The analytic transfer-operator trace theorem applied to these admissible holomorphic realizations identifies every nuclear trace with the same local inverse-branch fixed-point sum as in the circle realization. Equivalently, this is the usual independence of the analytic Ruelle determinant from the admissible holomorphic realization [@Ruelle1976; @Baladi2000; @Baladi2018]. Thus the two realizations have the same Fredholm determinants and the same nonzero spectra, including algebraic multiplicity.

For the first sector, define the bounded isomorphism $$I_0:\ell^1(\{1,2,\ldots\})\longrightarrow\ker\ell,
 \qquad
 I_0d=\left(-\sum_{j\ge1}m_jd_j,d_1,d_2,\ldots\right).$$ Its inverse drops the constant coordinate. Mean invariance implies $\mathcal T_1I_0=I_0\mathcal T_{1,0}$. The Perron eigenvalue is simple, so this similarity removes exactly its one-dimensional factor and gives [\[eq:det-identification\]](#eq:det-identification){reference-type="eqref" reference="eq:det-identification"}.

# Finite matrices and analytic tail bounds {#sec:certificate-method}

Let $P_N$ retain the first $N$ reduced coordinates. For $\mathcal T_{1,0}$ these are $d_1,\ldots,d_N$; for $\mathcal T_2$ these are $c_0,\ldots,c_{N-1}$. Define $$\label{eq:finite-matrices}
 M_{1,N}=P_N\mathcal T_{1,0}P_N,
 \qquad
 M_{2,N}=P_N\mathcal T_2P_N,$$ extended by zero on the omitted coordinates.

The proof needs a rigorous operator-norm estimate for $\mathcal T_{j}-M_{j,N}$. Choose the larger Cauchy radius $$\label{eq:cauchy-radius}
 \rho=\frac9{10},
 \qquad
 q=\frac R\rho=\frac79.$$ If $f$ is analytic on $|x|\le\rho$ with $|f|\le M_\rho$, Cauchy's estimate gives $$\label{eq:cauchy-tail}
 \sum_{j\ge K}|f_j|R^j
 \le M_\rho\frac{q^K}{1-q}.$$

At $\rho$, the same positive-coefficient argument gives $$\label{eq:sigma}
 t(\rho)=0.482921793913694\ldots,
 \qquad
 \sigma:=\frac{t(\rho)}{R^2}
 =0.985554681456517\ldots<1.$$ For $|x|\le\rho$, put $$\label{eq:s-bounds}
 s_{\min}=\sqrt{\frac{1-\rho}{u_{\mathrm c}}},
 \qquad
 s_{\max}=\sqrt{\frac{1+\rho}{u_{\mathrm c}}}.$$ Equations [\[eq:a-weight\]](#eq:a-weight){reference-type="eqref" reference="eq:a-weight"} and [\[eq:b-weight\]](#eq:b-weight){reference-type="eqref" reference="eq:b-weight"} imply the explicit sup bounds $$\begin{aligned}
 A_\rho
 &=\frac{\sqrt{u_{\mathrm c}(1+s_{\max})(1+t(\rho))}}
 {4s_{\min}}
 \ge\sup_{|x|\le\rho}|a(x)|,
 \label{eq:A-rho}\\
 B_\rho
 &=\frac{A_\rho}{2u_{\mathrm c}^2s_{\min}}
 \ge\sup_{|x|\le\rho}|b(x)|.
 \label{eq:B-rho}\end{aligned}$$ The certified values are $$\label{eq:cauchy-values}
 A_\rho\le2.15844363868010,
 \qquad
 B_\rho\le1.77938939382276.$$

The first $K=100$ Taylor coefficients, enclosed by Arb, together with [\[eq:cauchy-tail\]](#eq:cauchy-tail){reference-type="eqref" reference="eq:cauchy-tail"}, give $$\label{eq:weight-norms}
 \|a\|_R\le0.675431518461580,
 \qquad
 \|b\|_R\le0.321477794530791.$$ The omitted portions of these two weight norms are below $1.19\times10^{-10}$ and $9.76\times10^{-11}$, respectively.

[\[lem:finite-rank-errors\]]{#lem:finite-rank-errors label="lem:finite-rank-errors"} For even $N$, define $$\begin{aligned}
 \varepsilon_{1,N}
 =\max\Bigg\{&
 2A_\rho(\sigma+m_2)\frac{q^{N+1}}{1-q},\nonumber\\[-0.2em]
 &2\|a\|_R\left(\tau^{N/2+1}+m_{N+2}\right)
 \Bigg\},
 \label{eq:epsilon-one}\\
 \varepsilon_{2,N}
 =\max\Bigg\{&
 \frac{B_\rho}{R}\frac{q^N}{1-q},
 \frac{\|b\|_R}{R}\tau^{N/2}
 \Bigg\}.
 \label{eq:epsilon-two}\end{aligned}$$ Then $$\label{eq:operator-errors}
 \|\mathcal T_{1,0}-M_{1,N}\|_1\le\varepsilon_{1,N},
 \qquad
 \|\mathcal T_2-M_{2,N}\|_1\le\varepsilon_{2,N}.$$ For $N=50$, $$\label{eq:error-values}
 \varepsilon_{1,50}\le0.000523774672228,
 \qquad
 \varepsilon_{2,50}\le0.000240748393117.$$

For a retained column, the finite matrix omits only Taylor rows above the projection. In the first sector, every nonzero retained column has index $2k$, $k\ge1$. Its supremum on the Cauchy disk is bounded by $$\label{eq:low-column-one}
 2A_\rho(\sigma^k+m_{2k})
 \le2A_\rho(\sigma+m_2),$$ because $\sigma<1$ and $m_{2k}$ decreases. Apply [\[eq:cauchy-tail\]](#eq:cauchy-tail){reference-type="eqref" reference="eq:cauchy-tail"} starting at row $N+1$. In the second sector, the largest retained-column Cauchy bound occurs at $k=0$ and is $B_\rho/R$; the omitted rows start at $N$.

For an omitted input column, use the Wiener algebra inequality. The first nonzero omitted first-sector column is $N+2$, hence $k=N/2+1$, and $$\label{eq:high-column-one}
 \|C^{(1)}_{2k}\|_1
 \le2\|a\|_R(\tau^k+m_{2k}).$$ Both terms decrease with $k$. The first nonzero omitted second-sector column is $N+1$, giving $$\label{eq:high-column-two}
 \|C^{(2)}_{2k+1}\|_1
 \le\frac{\|b\|_R}{R}\tau^k,
 \qquad k=N/2.$$ Taking the larger of the retained-row tail and omitted-column bound proves the formulas. Arb evaluates every endpoint outward.

# The validated spectral-gap theorem {#sec:main-theorem}

All numbers in this section are interval enclosures, although only outward decimal endpoints are displayed. The cubic root is isolated directly from the integer polynomial [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"}. Taylor coefficients, matrix products, absolute column sums, and the scalar inequalities in [\[lem:finite-rank-errors\]](#lem:finite-rank-errors){reference-type="ref" reference="lem:finite-rank-errors"} are evaluated at 100 decimal places with python-flint/Arb [@Johansson2017; @PythonFlint2026].

For $N=50$, the finite matrix bounds are

::: {#tab:certificate}
  quantity          reduced even $\beta=1$         odd $\beta=2$
  --------------- ------------------------ ---------------------
  $\|M\|_1$            $0.633441090679032$   $0.459253986479389$
  $\|M^2\|_1$          $0.173686165268463$   $0.064417250176370$
  $\|M^3\|_1$          $0.035427563462424$                   ---
  $\varepsilon$        $0.000523774672228$   $0.000240748393117$

  : Certified finite-matrix and truncation bounds.
:::

Write $\mathcal T=M+E$ with $\|E\|\le\varepsilon$. For the first sector, the exact noncommutative expansion gives $$\begin{aligned}
 \|\mathcal T^3\|
 \le{}&\|M^3\|
 +\varepsilon\left(2\|M^2\|+\|M\|^2\right)\nonumber\\
 &+3\|M\|\varepsilon^2+\varepsilon^3.
 \label{eq:cube-perturbation}\end{aligned}$$ For the second sector, $$\label{eq:square-perturbation}
 \|\mathcal T^2\|
 \le\|M^2\|+2\|M\|\varepsilon+\varepsilon^2.$$

[\[thm:validated-gap\]]{#thm:validated-gap label="thm:validated-gap"} For the postcritical circle lift at [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"}, $$\begin{aligned}
 \|\mathcal T_{1,0}^3\|_1
 &\le0.035820193107412
 <\lambda^{-6}=0.0447051759618781\ldots,
 \label{eq:certified-one}\\
 \|\mathcal T_2^2\|_1
 &\le0.064638437454714
 <\lambda^{-4}=0.125961707473977\ldots.
 \label{eq:certified-two}\end{aligned}$$ Consequently $$\label{eq:radius-bounds}
 \boxed{
 r_1\le0.329642076293171<\lambda^{-2},
 \qquad
 r_2\le0.254240904369682<\lambda^{-2}.}$$ In fact both radii are strictly smaller than $1/3$.

Insert [1](#tab:certificate){reference-type="ref" reference="tab:certificate"} and [\[eq:error-values\]](#eq:error-values){reference-type="eqref" reference="eq:error-values"} into [\[eq:cube-perturbation\]](#eq:cube-perturbation){reference-type="eqref" reference="eq:cube-perturbation"} and [\[eq:square-perturbation\]](#eq:square-perturbation){reference-type="eqref" reference="eq:square-perturbation"}. Arb returns the upper endpoints in [\[eq:certified-one\]](#eq:certified-one){reference-type="eqref" reference="eq:certified-one"} and [\[eq:certified-two\]](#eq:certified-two){reference-type="eqref" reference="eq:certified-two"}; the lower threshold endpoints are computed from the isolated algebraic interval for $\lambda$. The spectral-radius formula gives $$\label{eq:power-radius}
 r(\mathcal T_{1,0})\le\|\mathcal T_{1,0}^3\|^{1/3},
 \qquad
 r(\mathcal T_2)\le\|\mathcal T_2^2\|^{1/2}.$$ Taking outward roots yields [\[eq:radius-bounds\]](#eq:radius-bounds){reference-type="eqref" reference="eq:radius-bounds"}. Direct interval comparison also gives $0.329642076293171<1/3$.

This proves the reduced-sector disk-bound conjecture posed in the preceding paper. The argument uses power norms, not approximate eigenvalues. In particular, no spectral diagonalization or assumption of normality enters the proof.

# Consequences for the weighted zeta function {#sec:consequences}

Let $$\label{eq:certified-disk-radius}
 R_{\mathrm{cert}}
 =\frac1{0.329642076293171}
 =3.0335933180\ldots.$$ Since $$\label{eq:lambda-square}
 \lambda^2=2.8176090299\ldots<R_{\mathrm{cert}},$$ [\[thm:validated-gap,cor:spectral-identification\]](#thm:validated-gap,cor:spectral-identification){reference-type="ref" reference="thm:validated-gap,cor:spectral-identification"} show that both $\widetilde D_{1,+}$ and $D_{2,-}$ are zero-free throughout $|z|<R_{\mathrm{cert}}$.

[\[cor:zero-pole\]]{#cor:zero-pole label="cor:zero-pole"} The residual quotient $$\label{eq:G-again}
 G(z)=\frac{D_{2,-}(z)}{\widetilde D_{1,+}(z)}$$ is holomorphic and nonzero for $|z|<R_{\mathrm{cert}}$. Therefore $$\label{eq:H-final}
 H(z)=\frac{1-z/\lambda}{1-z/\lambda^2}G(z)$$ has an actual simple zero at $z=\lambda$ and an actual simple pole at $z=\lambda^2$.

Fredholm zeros are reciprocals of nonzero eigenvalues. The certified spectral radii therefore make both determinants zero-free on the stated disk. Equation [\[eq:H-final\]](#eq:H-final){reference-type="eqref" reference="eq:H-final"} is the exact factorization [\[eq:centered-factorization\]](#eq:centered-factorization){reference-type="eqref" reference="eq:centered-factorization"}; nonvanishing of $G$ prevents either explicit factor from canceling.

The periodic coefficient remainder is $$\label{eq:e-n}
 e_n=q_n-1+\lambda^{-n}-\lambda^{-2n}
 =\operatorname{tr}(\mathcal T_{1,0}^n)-\operatorname{tr}(\mathcal T_2^n).$$ Both operators are nuclear. Since their spectral radii are strictly below $1/3$, the logarithmic derivative of their residual determinant quotient is analytic on a disk of radius strictly greater than $3$.

[\[cor:sharp-law\]]{#cor:sharp-law label="cor:sharp-law"} The component Perron periodic weight satisfies $$\label{eq:sharp-law}
 \boxed{
 q_n=1-\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).}$$ For the standard weighted trace $Q_m$ of the original quadratic map, $$\begin{aligned}
 Q_{2n}
 &=2-2\lambda^{-n}+\lambda^{-2n}+O(3^{-n}),
 \label{eq:Q-even-sharp}\\
 Q_{2n+1}
 &=\lambda^{-(2n+1)}.
 \label{eq:Q-odd-exact}\end{aligned}$$

By the Fredholm trace expansion, $$z\frac{G'(z)}{G(z)}=\sum_{n\ge1}e_nz^n.$$ Choose any $\rho_0$ with $3<\rho_0<R_{\mathrm{cert}}$. The left-hand side is holomorphic on $|z|\le\rho_0$, so Cauchy's coefficient estimate gives $e_n=O(\rho_0^{-n})=O(3^{-n})$. Substitution into [\[eq:e-n\]](#eq:e-n){reference-type="eqref" reference="eq:e-n"} proves the first formula. The exact component-pairing identity from the flat-trace completion theorem is $Q_{2n}=2q_n-\lambda^{-2n}$, while odd iterates fix only the shared endpoint [@WangFlatTrace2026]. Substitution gives the result.

# Certificate audit and independent diagnostics {#sec:audit}

The primary proof uses dimension $50$, but the same code was run at dimensions $30,40,50,60,70$, always with 50 additional Taylor coefficients for the weight-norm tail. reports outward upper bounds. Even the dimension-30 first-sector bound clears $\lambda^{-6}$, although the dimension-50 certificate has a much wider margin.

::: {#tab:stability}
    $N$   $\|\mathcal T_{1,0}^3\|$     $r_1$ bound   $\|\mathcal T_2^2\|$     $r_2$ bound
  ----- -------------------------- --------------- ---------------------- ---------------
     30              $0.043735693$   $0.352326521$          $0.070039026$   $0.264648873$
     40              $0.037216596$   $0.333871140$          $0.065420112$   $0.255773556$
     50              $0.035820194$   $0.329642077$          $0.064638438$   $0.254240905$
     60              $0.035514115$   $0.328700475$          $0.064466069$   $0.253901691$
     70              $0.035446664$   $0.328492244$          $0.064428028$   $0.253826767$

  : Dimension stability of the validated bounds.
:::

![Certificate audit. Top left: validated power norms remain below their exact algebraic thresholds. Top right: the induced spectral-radius bounds remain below $\lambda^{-2}$. Bottom left: finite matrices dominate the final bounds, while analytic-tail corrections are small. Bottom right: the Taylor and independent circle flat traces agree to floating-point accuracy; this panel is a cross-check, not an input to the proof.](<../../../../../zeta_mvp0/papers/RH-13-validated-reduced-sector-spectral-gap/figures/validated_reduced_sector_gap.pdf>){#fig:certificate width="\\textwidth"}

As an independent representation check, floating-point Taylor traces through $n=10$ were compared with the ordinary/twisted circle fixed-point traces from the preceding paper. The maximum discrepancy is $2.7\times10^{-13}$ at the first trace and below $1.2\times10^{-14}$ for $2\le n\le10$. This check is not part of the interval proof; it tests the parity conjugacies and matrix indexing against a separately implemented periodic-point calculation.

The leading floating-point eigenvalues of the dimension-100 matrices are $$\begin{aligned}
 \mu_{1,\mathrm{lead}}
 &=0.20788029772254\ldots,
 \label{eq:diagnostic-one}\\
 \mu_{2,\mathrm{lead}}
 &=0.15252823980512\ldots.
 \label{eq:diagnostic-two}\end{aligned}$$ They agree with the Fredholm-truncation diagnostics but are much smaller than the certified bounds [\[eq:radius-bounds\]](#eq:radius-bounds){reference-type="eqref" reference="eq:radius-bounds"}. This difference is expected: an induced operator norm must control nonnormality and the entire omitted tail, not only the leading apparent eigenpair.

## Reproducibility and proof status

The machine-readable certificate records:

1.  the 100-decimal interval enclosing the algebraic root $u_{\mathrm c}$;

2.  every scalar Wiener, Cauchy, matrix, truncation, and threshold bound;

3.  the python-flint, Python, NumPy, and platform versions;

4.  SHA-256 hashes of the two modules that construct the operators and certificate;

5.  Boolean comparisons for $\|\mathcal T_{1,0}^3\|<\lambda^{-6}$ and $\|\mathcal T_2^2\|<\lambda^{-4}$.

The primary calculation takes less than one second on the reported machine. All interval decisions are repeated by the test suite at independently chosen precision. The exact analytic estimates [\[eq:cauchy-tail\]](#eq:cauchy-tail){reference-type="eqref" reference="eq:cauchy-tail"}, [\[eq:epsilon-one\]](#eq:epsilon-one){reference-type="eqref" reference="eq:epsilon-one"}, and [\[eq:epsilon-two\]](#eq:epsilon-two){reference-type="eqref" reference="eq:epsilon-two"} are stated in the paper so that the finite computation has a transparent mathematical interface.

This is a computer-assisted proof: its theorem depends on the correctness of Arb's directed ball arithmetic and the archived source. It is not merely a high-precision numerical experiment. Conversely, the approximate eigenvalues [\[eq:diagnostic-one\]](#eq:diagnostic-one){reference-type="eqref" reference="eq:diagnostic-one"} and [\[eq:diagnostic-two\]](#eq:diagnostic-two){reference-type="eqref" reference="eq:diagnostic-two"} are explicitly not certified and are unnecessary for the theorem.

# Conclusion

The deck symmetry of the analytic circle lift does more than split a determinant. It decimates Taylor coefficients: the even first-order sector uses only even input coefficients, while the odd second-order sector uses only odd ones. After the exact Perron mean is removed, both operators become nuclear on a concrete Wiener algebra. This structure permits a small finite matrix and an elementary analytic tail bound to control the full infinite-dimensional spectrum.

The resulting validated inequalities resolve the sole noncancellation condition left by the postcritical factorization. The algebraic factors at $\lambda$ and $\lambda^2$ are now actual, respectively a simple zero and a simple pole, and the observed three-term periodic law is a theorem with the explicit remainder $O(3^{-n})$. No unproved spectral assumption remains in these conclusions.

# Data and code availability {#data-and-code-availability .unnumbered}

The complete source, tests, interval certificate, stability table, trace cross-check, figures, and manuscript are archived with this paper [@WangValidatedGapCode2026]. The repository also contains the preceding factorization paper and its independent periodic-orbit implementation.
