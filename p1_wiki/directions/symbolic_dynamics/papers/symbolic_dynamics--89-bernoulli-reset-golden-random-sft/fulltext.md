---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--89-bernoulli-reset-golden-random-sft"
canonical_tex: "symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/main.tex"
canonical_pdf: "symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/main.pdf"
source_sha256: "0526e96d9ebd1cda90f59c9240a84eca7646191f0743e41d1bf65440ea2361e7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fibonacci Regeneration in a Bernoulli-Reset Golden Random Shift: Exact Quenched--Annealed Gap and Gaussian Fluctuations

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/89-bernoulli-reset-golden-random-sft/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At every time, choose independently between the golden-mean adjacency matrix $$A=\begin{pmatrix}1&1\\1&0\end{pmatrix}
   \quad\text{and the reset matrix}\quad
   E=\begin{pmatrix}1&1\\0&0\end{pmatrix},$$ using $E$ with probability $p$. The number $N_n$ of fibre paths through $n$ random constraints is a random matrix product. The rank-one identity $EA^kE=F_{k+2}E$ turns its logarithm into a renewal-reward process. We obtain, for $0<p<1$, $$h_{\mathrm q}(p)=p^2\sum_{k\geq0}(1-p)^k\log F_{k+2},
   \qquad
   h_{\mathrm a}(p)=\log\frac{1+\sqrt{5-4p}}2,$$ and prove the strict disorder gap $h_{\mathrm q}(p)<h_{\mathrm a}(p)$. We also prove $$\frac{\log N_n-nh_{\mathrm q}(p)}{\sqrt n}
   \Longrightarrow \mathcal N(0,\sigma_p^2),$$ where $$\sigma_p^2=p^2\sum_{k\geq0}(1-p)^k
   \bigl(\log F_{k+2}-(k+1)h_{\mathrm q}(p)\bigr)^2>0.$$ The general random-subshift, random-matrix, and regenerative limit theories are established background. This note records an exact two-matrix specialization and makes no absolute novelty or priority claim.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: 'Fibonacci Regeneration in a Bernoulli-Reset Golden Random Shift: Exact Quenched--Annealed Gap and Gaussian Fluctuations'
```

## Markdown 正文

# Introduction

The topological entropy of a deterministic shift of finite type is the logarithm of a Perron eigenvalue. In a random shift, the corresponding path count is a product of adjacency matrices, and two distinct growth rates appear: the almost-sure, or quenched, exponent of the path count and the annealed exponent of its expectation. Products of random matrices have a classical general theory beginning with Furstenberg and Kesten [@FurstenbergKesten1960]; random subshifts and their thermodynamic formalism are developed, at much greater generality, by Kifer and by Denker--Kifer--Stadlbauer [@Kifer2008; @DenkerKiferStadlbauer2008].

This note isolates a degenerate but exactly solvable Bernoulli model. One matrix is the familiar presentation of the golden-mean shift [@LindMarcus1995]. The other deletes its second row and acts as a rank-one reset. A block of ordinary golden constraints between two resets contributes exactly one Fibonacci number. Reset gaps are geometric, so the entire cocycle becomes regenerative rather than merely subadditive.

The resulting calculation has three features. First, it gives a closed series for the quenched fibre entropy. Second, the annealed exponent remains a quadratic Perron root, and a cycle-normalized strict Jensen argument proves that the two exponents differ at every nontrivial reset probability. Third, the same cycles yield a central limit theorem with an explicit positive variance. No perturbation, irreducibility theorem for random operators, or numerical Lyapunov-exponent approximation is required.

All logarithms are natural. We use the classical Fibonacci normalization $F_0=0$, $F_1=1$, and $F_{j+2}=F_{j+1}+F_j$, and write $\varphi=(1+\sqrt5)/2$. The external-release status of this internal manuscript is **HOLD**: the broad mechanisms have clear owners, and the exact conjunction of formulas below is presented without a claim that it has not appeared elsewhere.

# The random nearest-neighbor shift {#sec:model}

Let $\Omega=\{0,1\}^{\mathbb Z}$ and let $\nu_p$ be the Bernoulli measure for which $\nu_p\{\omega:\omega_i=1\}=p$. The symbol $1$ marks a reset. Put $$\label{eq:matrices}
 A=\begin{pmatrix}1&1\\1&0\end{pmatrix},
 \qquad
 E=\begin{pmatrix}1&1\\0&0\end{pmatrix},
 \qquad
 M_i(\omega)=\begin{cases}A,&\omega_i=0,\\E,&\omega_i=1.\end{cases}$$ For a fixed environment $\omega$, define the fibre $$\label{eq:fibre}
 X_\omega=\left\{x\in\{0,1\}^{\mathbb Z}:
 M_i(\omega)_{x_i,x_{i+1}}=1\text{ for every }i\in\mathbb Z\right\}.$$ The all-zero point belongs to every fibre, so no exceptional empty fibre arises. The number of paths across the constraints at times $0,\ldots,n-1$ is $$\label{eq:path-count}
 N_n(\omega)=\mathbf 1^{\mathsf T}M_0(\omega)M_1(\omega)\cdots
 M_{n-1}(\omega)\mathbf 1,
 \qquad \mathbf 1=\binom11.$$ Thus $N_n$ counts words $x_0\cdots x_n$, not words of length $n$; this one-symbol convention does not affect any exponential rate.

When the limits exist, define $$\label{eq:two-entropies}
 h_{\mathrm q}(p)=\lim_{n\to\infty}\frac1n\log N_n(\omega)
 \quad(\nu_p\text{-a.s.}),
 \qquad
 h_{\mathrm a}(p)=\lim_{n\to\infty}\frac1n\log\mathbb E_{\nu_p}N_n.$$ The first is the fibre topological entropy along a typical environment; the second averages path counts before taking the logarithm.

# Fibonacci regeneration and quenched entropy {#sec:quenched}

The exact solvability is contained in one matrix identity.

[\[lem:fibonacci-reset\]]{#lem:fibonacci-reset label="lem:fibonacci-reset"} For every $k\geq0$, $$\label{eq:reset-identity}
 EA^kE=F_{k+2}E.$$ More precisely, if the reset positions in $\{0,\ldots,n-1\}$ are $r_1<\cdots<r_m$, put $$\ell=r_1,\qquad q=n-1-r_m,
 \qquad k_j=r_{j+1}-r_j-1\quad(1\leq j<m).$$ Then $$\label{eq:factorization}
 N_n(\omega)=B_{\ell,q}\prod_{j=1}^{m-1}F_{k_j+2},
 \qquad
 B_{\ell,q}=\mathbf 1^{\mathsf T}A^\ell EA^q\mathbf 1.$$ The boundary factor satisfies $$\label{eq:boundary-bound}
 1\leq B_{\ell,q}\leq2^{\ell+q+2}.$$

For $k\geq1$, induction gives $$A^k=\begin{pmatrix}F_{k+1}&F_k\\F_k&F_{k-1}\end{pmatrix}.$$ Multiplication on the left and right by $E$ gives $EA^kE=F_{k+2}E$. At $k=0$, the same statement is $E^2=E=F_2E$. Repeatedly applying this identity to $$A^\ell EA^{k_1}E\cdots EA^{k_{m-1}}EA^q$$ proves [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"}. At least the all-zero state path is counted by $B_{\ell,q}$, while there are at most $2^{\ell+q+2}$ binary state words of the required length. This proves [\[eq:boundary-bound\]](#eq:boundary-bound){reference-type="eqref" reference="eq:boundary-bound"}.

Let $r=1-p$. For $0<p<1$, start with the first reset at or after time zero and enumerate later reset times. The numbers $K_j$ of ordinary $A$-steps strictly between consecutive resets are independent and satisfy $$\label{eq:gap-law}
 \mathbb P(K_j=k)=p r^k,
 \qquad k\geq0.$$ The cycle length and logarithmic reward are $$\label{eq:cycle-pair}
 L_j=K_j+1,
 \qquad
 R_j=\log F_{K_j+2}.$$ They obey $\mathbb EL_j=1/p$ and have moments of every order.

[\[thm:quenched\]]{#thm:quenched label="thm:quenched"} For $0<p<1$, the first limit in [\[eq:two-entropies\]](#eq:two-entropies){reference-type="eqref" reference="eq:two-entropies"} exists almost surely and in $L^1(\nu_p)$, and $$\label{eq:quenched-formula}
 \boxed{\displaystyle
 h_{\mathrm q}(p)=p^2\sum_{k=0}^{\infty}r^k\log F_{k+2}.}$$ At the deterministic endpoints, $$\label{eq:quenched-endpoints}
 h_{\mathrm q}(0)=\log\frac{1+\sqrt5}{2},
 \qquad h_{\mathrm q}(1)=0.$$

The renewal-reward strong law applied to [\[eq:gap-law\]](#eq:gap-law){reference-type="eqref" reference="eq:gap-law"}--[\[eq:cycle-pair\]](#eq:cycle-pair){reference-type="eqref" reference="eq:cycle-pair"} gives $$\label{eq:reward-rate}
 \frac{\sum_{j<J(n)}R_j}{n}
 \longrightarrow
 \frac{\mathbb ER_0}{\mathbb EL_0}
 =p^2\sum_{k\geq0}r^k\log F_{k+2}
 \quad\text{almost surely},$$ where $J(n)$ is the number of completed reset-to-reset cycles seen by time $n$. The series converges because $\log F_{k+2}=O(k+1)$.

It remains to compare the reward sum with the exact path count. Let $H_n$ be the longest reset-free run inside the environment word $\omega_0\cdots\omega_{n-1}$. For any $c>2/|\log r|$, a union bound gives $$\mathbb P(H_n\geq c\log n)\leq n r^{c\log n},$$ and the right side is summable. The Borel--Cantelli lemma therefore gives $H_n=O(\log n)$ almost surely. In [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"}, the initial reset delay is almost surely finite and the terminal reset-free length is at most $H_n$. Hence [\[eq:boundary-bound\]](#eq:boundary-bound){reference-type="eqref" reference="eq:boundary-bound"} shows that $$\label{eq:boundary-negligible}
 \log N_n-\sum_{j<J(n)}R_j=O(\log n)
 \quad\text{almost surely}.$$ Combining [\[eq:reward-rate\]](#eq:reward-rate){reference-type="eqref" reference="eq:reward-rate"} and [\[eq:boundary-negligible\]](#eq:boundary-negligible){reference-type="eqref" reference="eq:boundary-negligible"} proves the almost-sure formula. Since $0\leq n^{-1}\log N_n\leq(1+n^{-1})\log2$, dominated convergence gives $L^1$ convergence.

If $p=0$, then $N_n=\mathbf 1^{\mathsf T}A^n\mathbf 1=F_{n+3}$, whose rate is the logarithm of the golden ratio. If $p=1$, then $E^n=E$ and $N_n=2$, so the rate is zero.

# Annealed exponent and the strict disorder gap {#sec:annealed}

Independence of the environment matrices gives an exact finite-time annealed formula despite their noncommutativity: $$\label{eq:annealed-finite}
 \mathbb EN_n
 =\mathbf 1^{\mathsf T}\overline M_p^{\,n}\mathbf 1,
 \qquad
 \overline M_p=(1-p)A+pE
 =\begin{pmatrix}1&1\\r&0\end{pmatrix}.$$ Indeed, successively integrating the last independent factor replaces it by its mean, and iteration yields the displayed product.

[\[thm:gap\]]{#thm:gap label="thm:gap"} For every $0\leq p\leq1$, $$\label{eq:annealed-formula}
 \boxed{\displaystyle
 h_{\mathrm a}(p)=\log\lambda_p,
 \qquad
 \lambda_p=\frac{1+\sqrt{5-4p}}2.}$$ For every nontrivial disorder parameter, $$\label{eq:strict-gap}
 h_{\mathrm q}(p)<h_{\mathrm a}(p),\qquad 0<p<1.$$ Equality holds at $p=0$ and $p=1$.

The characteristic polynomial of $\overline M_p$ is $t^2-t-r$. For $p<1$, the matrix is primitive and its Perron root is $\lambda_p$ in [\[eq:annealed-formula\]](#eq:annealed-formula){reference-type="eqref" reference="eq:annealed-formula"}; [\[eq:annealed-finite\]](#eq:annealed-finite){reference-type="eqref" reference="eq:annealed-finite"} and Perron--Frobenius theory give the exponent. At $p=1$, the mean matrix is the idempotent $E$, and the same formula gives $\lambda_1=1$.

For strictness, take a gap $K$ with law [\[eq:gap-law\]](#eq:gap-law){reference-type="eqref" reference="eq:gap-law"} and define the positive cycle-normalized gain $$\label{eq:normalized-gain}
 Z=\frac{F_{K+2}}{\lambda_p^{K+1}}.$$ The Fibonacci generating function is $$\label{eq:fib-generating}
 \sum_{k\geq0}F_{k+2}z^k=\frac{1+z}{1-z-z^2}.$$ Because $\lambda_p^2=\lambda_p+r$, one has $r/\lambda_p=\lambda_p-1<\varphi-1=\varphi^{-1}$, so substitution of $z=r/\lambda_p$ into the convergent series [\[eq:fib-generating\]](#eq:fib-generating){reference-type="eqref" reference="eq:fib-generating"} gives $$\begin{aligned}
 \mathbb EZ
 &=\frac p{\lambda_p}
   \frac{1+r/\lambda_p}{1-r/\lambda_p-r^2/\lambda_p^2}=1.\label{eq:gain-mean}\end{aligned}$$ For the last equality, after multiplication by $\lambda_p^2$ the denominator is $\lambda_p^2-r\lambda_p-r^2=p(\lambda_p+r)$, exactly the corresponding numerator. Moreover, $Z$ is not constant: its values at $K=0$ and $K=1$ are $\lambda_p^{-1}$ and $2\lambda_p^{-2}$, respectively, and $1<\lambda_p<2$. Strict concavity of the logarithm and [\[eq:gain-mean\]](#eq:gain-mean){reference-type="eqref" reference="eq:gain-mean"} now yield $$h_{\mathrm q}(p)-\log\lambda_p
 =\frac{\mathbb E\log F_{K+2}-(\mathbb EL)\log\lambda_p}{\mathbb EL}
 =p\,\mathbb E\log Z
 <p\log\mathbb EZ=0.$$ The endpoint equalities follow from [\[thm:quenched\]](#thm:quenched){reference-type="ref" reference="thm:quenched"} and [\[eq:annealed-formula\]](#eq:annealed-formula){reference-type="eqref" reference="eq:annealed-formula"}.

The proof identifies the strict gap with within-cycle variability. It is stronger than applying Jensen's inequality separately at finite $n$, since it exhibits a nonconstant normalized gain whose strictness survives after division by time.

# A renewal central limit theorem {#sec:clt}

The same exact cycles determine the fluctuations. Regenerative central limit theorems in the required form are classical; see, for example, the renewal and regenerative chapters of Asmussen [@Asmussen2003]. We state all moments and the boundary transfer explicitly for this model.

[\[thm:clt\]]{#thm:clt label="thm:clt"} For every $0<p<1$, $$\label{eq:clt}
 \frac{\log N_n-nh_{\mathrm q}(p)}{\sqrt n}
 \xrightarrow{\mathrm d}\mathcal N(0,\sigma_p^2),$$ where $$\label{eq:variance}
 \boxed{\displaystyle
 \sigma_p^2=p^2\sum_{k=0}^{\infty}r^k
 \left(\log F_{k+2}-(k+1)h_{\mathrm q}(p)\right)^2>0.}$$ The series converges exponentially.

Write $h=h_{\mathrm q}(p)$ and center one cycle by $$W_j=R_j-hL_j.$$ The pairs $(L_j,R_j)$ are independent and identically distributed, $\mathbb EW_j=0$, and $|W_j|=O(L_j)$. The geometric tail of $L_j$ therefore gives $\mathbb EW_j^2<\infty$. To keep the delayed initial cycle explicit, let $\tau=\min\{t\geq0:\omega_t=1\}$, put $S_m=\sum_{j<m}L_j$, and for $n>\tau$ set $$J_n=\max\{m\geq0:\tau+S_m\leq n-1\}.$$ Thus $J_n$ counts reset-to-reset cycles completed inside the observation window. Conditional on the almost-surely finite $\tau$, the future cycle pairs are iid with the law in [\[eq:gap-law\]](#eq:gap-law){reference-type="eqref" reference="eq:gap-law"}--[\[eq:cycle-pair\]](#eq:cycle-pair){reference-type="eqref" reference="eq:cycle-pair"}. The delayed renewal-reward central limit theorem therefore gives $$\label{eq:regenerative-clt}
 \frac{\sum_{j<J_n}R_j-h(n-1-\tau)}{\sqrt n}
 \xrightarrow{\mathrm d}
 \mathcal N\left(0,\frac{\mathbb EW_0^2}{\mathbb EL_0}\right).$$ Replacing $h(n-1-\tau)$ by $hn$ changes the numerator by the fixed random quantity $h(\tau+1)=o(\sqrt n)$ almost surely. The terminal unfinished cycle is bounded by the longest reset-free block $H_n$, and the exact matrix boundary in [\[eq:boundary-negligible\]](#eq:boundary-negligible){reference-type="eqref" reference="eq:boundary-negligible"} is $O(\log n)$ almost surely. Both are $o(\sqrt n)$, so [\[eq:regenerative-clt\]](#eq:regenerative-clt){reference-type="eqref" reference="eq:regenerative-clt"} transfers to $\log N_n$.

Finally, using [\[eq:gap-law\]](#eq:gap-law){reference-type="eqref" reference="eq:gap-law"} and $\mathbb EL_0=1/p$, $$\frac{\mathbb EW_0^2}{\mathbb EL_0}
 =p^2\sum_{k\geq0}r^k
  \left(\log F_{k+2}-(k+1)h\right)^2,$$ which is [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. Exponential convergence follows because the squared term is $O((k+1)^2)$. Positivity is also exact: if the variance vanished, the positive-probability cases $K=0$ and $K=1$ would give $0=W(0)=-h$ and $0=W(1)=\log2-2h$ simultaneously, a contradiction.

# Exact controls, scope, and ownership boundary {#sec:controls}

The accompanying standard-library program is independent of the proofs at the definition level. It enumerates state paths and environments rather than inserting the theorem formulas. Its discrete layer performs 66,787 integer or rational assertions:

-   $EA^kE=F_{k+2}E$ and the Fibonacci form of $A^k$ through $k=50$;

-   matrix counts against direct enumeration of every state path for every environment of lengths $0\leq n\leq9$;

-   the full renewal factorization for every environment of lengths $0\leq n\leq15$;

-   the exact identity [\[eq:annealed-finite\]](#eq:annealed-finite){reference-type="eqref" reference="eq:annealed-finite"} for three rational values of $p$ and all $0\leq n\leq16$;

-   the rational generating-function reductions used in the strict-gap proof.

Floating-point evaluations are diagnostics only. Representative values are

    $p$     $h_{\mathrm q}(p)$   $h_{\mathrm a}(p)$     $\sigma_p^2$
  -------- -------------------- -------------------- ------------------
   $0.10$    $0.447641693679$     $0.452590731810$    $0.011161475035$
   $0.25$    $0.392429805910$     $0.405465108108$    $0.029582718017$
   $0.50$    $0.285678394376$     $0.311905358182$    $0.057612583213$
   $0.75$    $0.156807280841$     $0.188226406460$    $0.062358024158$
   $0.90$    $0.066539324973$     $0.087651818647$    $0.037293341513$

The ownership boundary is deliberate. Furstenberg--Kesten own the general random-matrix-product setting [@FurstenbergKesten1960]; Kifer and Denker--Kifer--Stadlbauer own broad random-subshift thermodynamic frameworks [@Kifer2008; @DenkerKiferStadlbauer2008]; and the renewal-reward strong law and central limit theorem are classical regenerative probability [@Asmussen2003]. The golden-mean matrix itself is standard [@LindMarcus1995]. The residual content of this note is the exact Fibonacci-reset specialization that ties those mechanisms together.

A bounded search through 28 August 2026 using combinations of *random golden mean shift*, *Bernoulli reset*, *quenched entropy*, and the exact matrix identity did not identify a direct source for the entire displayed package. That negative search is a collision firewall, not evidence of absolute novelty. In particular, randomness here acts on time-dependent transition constraints, not on substitution images, and the note does not claim a general theorem for random substitutions or arbitrary matrix pairs. External dissemination remains on HOLD pending a separate expert literature and priority review.
