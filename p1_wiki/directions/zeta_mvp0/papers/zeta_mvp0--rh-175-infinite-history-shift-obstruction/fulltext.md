---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-175-infinite-history-shift-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/main.pdf"
source_sha256: "087d8b61539792166c212020b517fba47993309e4aae2324d214d1062954c6ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Infinite-History Shift Obstruction Spectral-Disk Pollution, Non-Schatten Powers, and Deceptive Finite Sections

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-175-infinite-history-shift-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The exact rectangular history maps of RH-173 suggest a square completion on an infinite memory space. Freezing the normalized first-block dynamics at $B=rA$ and writing $q=\sqrt\eta>0$, the canonical completion is $$\mathcal L(y_0,y_1,y_2,\ldots)
   =(By_0,qy_0,qy_1,qy_2,\ldots)$$ on $\ell^2(\mathbb N_0;\mathcal Y)$. We determine its spectrum and trace- ideal status exactly.

  If $\mathcal Y$ is finite dimensional, then $$\sigma(\mathcal L)=\sigma(B)\cup\{z:|z|\le q\},
   \qquad
   \sigma_{\mathrm e}(\mathcal L)=\{z:|z|=q\}.$$ The tail is a weighted unilateral shift. Therefore $\mathcal L$ is not compact, belongs to no Schatten class, and no positive power $\mathcal L^m$ is compact or Schatten. The ordinary Fredholm determinants $\det(I-z\mathcal L^m)$ required by the moving-cloud route are consequently undefined.

  Finite truncations conceal this obstruction: their shift tails are nilpotent and have spectrum only at zero. Nevertheless, for $0<|z|<q$ their resolvent satisfies the exact vector lower bound $$\left\|(zI-qS_L)^{-1}e_0\right\|
   =\frac1{|z|}\left(\sum_{k=0}^{L-1}(q/|z|)^{2k}\right)^{1/2},$$ which grows exponentially with $L$. A 15-case audit verifies this formula; at $L=64$ the largest recorded lower bound exceeds $10^{39.9}$ although every finite shift eigenvalue is zero.

  This is a rigorous no-go theorem for the direct canonical infinite-history shift as a Fredholm-determinant operator. It does not reject finite cyclic closures, weighted differences that cancel the shift, scattering objects, or direct transfer-space constructions. The natural next branch is finite cyclic memory.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  The Infinite-History Shift Obstruction\
  Spectral-Disk Pollution, Non-Schatten Powers, and Deceptive Finite Sections
```

## Markdown 正文

# Why square the rectangular cocycle?

RH-173 constructs exact maps $T_t:\mathcal K_t\to\mathcal K_{t+1}$, but a standard operator determinant requires a square operator on one fixed Hilbert space [@WangRH173]. The most literal square completion stores the entire past in $$\mathcal H=\ell^2(\mathbb N_0;\mathcal Y)
 =\mathcal Y\oplus\mathcal Y\oplus\cdots.$$ If the time-dependent normalization ratio is frozen at $r>0$, the current block evolves by $B=rA$ and every older block shifts one position with weight $q=\sqrt\eta$. The resulting operator is $$\label{eq:L}
 \mathcal L(y_0,y_1,y_2,\ldots)
 =(By_0,qy_0,qy_1,qy_2,\ldots).$$

The frozen model is already sufficient to decide the determinant question. If even one positive constant $q$ forces a noncompact shift tail, changing $B$ or fitting a finite packet cannot make the literal completion trace class.

# Block form and invariant tail

Let $S$ be the unilateral shift on $\ell^2(\mathbb N;\mathcal Y)$, $$S(y_1,y_2,\ldots)=(0,y_1,y_2,\ldots),$$ and let $E:\mathcal Y\to\ell^2(\mathbb N;\mathcal Y)$ inject into the first tail coordinate. Relative to $\mathcal H=\mathcal Y\oplus\ell^2(\mathbb N;\mathcal Y)$, $$\label{eq:block}
 \mathcal L=
 \begin{pmatrix}
 B&0\\
 qE&qS
 \end{pmatrix}.$$ The tail subspace $\{0\}\oplus\ell^2(\mathbb N;\mathcal Y)$ is invariant and the restriction is $qS$. The coupling $qE$ has rank $\dim\mathcal Y$.

# Exact spectrum

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} Suppose $\dim\mathcal Y<\infty$ and $q>0$. Then $$\label{eq:spectrum}
 \sigma(\mathcal L)=\sigma(B)\cup\overline{D(0,q)}.$$

If $z\notin\sigma(B)\cup\overline{D(0,q)}$, both $z-B$ and $z-qS$ are invertible. The triangular inverse formula applied to [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"} shows that $z-\mathcal L$ is invertible. This proves one inclusion.

Let $|z|=q$. The unilateral shift has approximate eigenvectors at every point of its boundary circle. Embedding those vectors in the invariant tail gives approximate eigenvectors for $\mathcal L$, so $z\in\sigma(\mathcal L)$.

Now let $|z|<q$. If $z-B$ is not surjective, neither is $z-\mathcal L$, because the first output coordinate is $(z-B)y_0$. If $z-B$ is invertible, use the adjoint. For any nonzero $v\in\mathcal Y$, the tail vector $$h_v=(v,(\overline z/q)v,(\overline z/q)^2v,\ldots)$$ belongs to $\ell^2$ and satisfies $qS^*h_v=\overline z h_v$. Choose $x\in\mathcal Y$ solving $$(B^*-\overline z)x=-qv.$$ Then $(x,h_v)$ is a nonzero eigenvector of $\mathcal L^*$ with eigenvalue $\overline z$. Hence $z\in\sigma(\mathcal L)$. Finally, every point of $\sigma(B)$ makes the first-coordinate equation nonsurjective in finite dimension, so it also belongs to the spectrum.

The disk is independent of the detailed prime-dynamics block $B$. Its radius is fixed solely by the memory parameter. For the archived value $\eta=1/512$, $$q=\frac1{\sqrt{512}}=0.0441941738\ldots.$$ Small radius does not mean trace class: infinitely many directions carry the same nonzero shift weight.

# Essential spectrum and Schatten obstruction

[\[thm:schatten\]]{#thm:schatten label="thm:schatten"} For $q>0$, $$\label{eq:essential}
 \sigma_{\mathrm e}(\mathcal L)=\{z:|z|=q\}.$$ Moreover, for every integer $m\ge1$, $\mathcal L^m$ is not compact and does not belong to $\mathcal S_p$ for any $1\le p<\infty$.

The difference between $\mathcal L$ and $B\oplus qS$ is the finite-rank operator with only block $qE$. Essential spectrum is invariant under compact perturbations, the finite matrix $B$ has empty essential spectrum, and the Fredholm essential spectrum of the unilateral shift is the unit circle [@Conway1990]. This proves [\[eq:essential\]](#eq:essential){reference-type="eqref" reference="eq:essential"}.

The invariant tail restriction of $\mathcal L^m$ is $q^mS^m$. The vectors $q^mS^me_n$ form an orthogonal sequence of constant norm $q^m$, so the image of the unit ball is not relatively compact. Thus $\mathcal L^m$ is not compact. Every Schatten operator is compact, completing the proof [@Simon2005].

# Which memory weights could evade the obstruction?

The failure is caused by a constant tail weight, not by the mere existence of history coordinates. This can be stated exactly for general weighted shifts. Let $(q_n)_{n\ge0}$ be nonnegative and define $$W(y_0,y_1,\ldots)=(0,q_0y_0,q_1y_1,\ldots)$$ on $\ell^2(\mathbb N_0;\mathcal Y)$, where $d=\dim\mathcal Y<\infty$.

[\[thm:weighted\]]{#thm:weighted label="thm:weighted"} The weighted history shift $W$ is compact if and only if $q_n\to0$. For $1\le p<\infty$, $$\label{eq:weighted-schatten}
 W\in\mathcal S_p
 \quad\Longleftrightarrow\quad
 \sum_{n\ge0}q_n^p<\infty,$$ and in that case $$\label{eq:weighted-norm}
 \left\lVert W\right\rVert_p^p=d\sum_{n\ge0}q_n^p.$$

The positive operator $W^*W$ is block diagonal with blocks $q_n^2I_\mathcal Y$. Hence the singular values of $W$ are precisely the numbers $q_n$, each repeated $d$ times. They tend to zero exactly when $W$ is compact, and their $p$th powers are summable exactly under [\[eq:weighted-schatten\]](#eq:weighted-schatten){reference-type="eqref" reference="eq:weighted-schatten"}.

The archived memory recursion has the same shift factor $q_n\equiv\sqrt\eta$, so it lies at the opposite extreme: none of the singular values decays with age. A trace-class redesign would require, for example, age weights in $\ell^1$; a Hilbert--Schmidt redesign would require weights in $\ell^2$. Such a redesign changes the original recursive memory and must be justified physically rather than inserted after the fact.

# Explicit exterior resolvent

Outside the spectral union in Theorem [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"}, the triangular inverse is $$\label{eq:triangular-inverse}
 (z-\mathcal L)^{-1}=
 \begin{pmatrix}
 (z-B)^{-1}&0\\
 (z-qS)^{-1}qE(z-B)^{-1}&(z-qS)^{-1}
 \end{pmatrix}.$$ Consequently, with $b(z)=\left\lVert(z-B)^{-1}\right\rVert$ and $s(z)=\left\lVert(z-qS)^{-1}\right\rVert$, a simple block-row estimate gives $$\label{eq:exterior-bound}
 \left\lVert(z-\mathcal L)^{-1}\right\rVert
 \le b(z)+s(z)+q\,b(z)s(z).$$ For $|z|>q$, $s(z)\le(|z|-q)^{-1}$. Formula [\[eq:triangular-inverse\]](#eq:triangular-inverse){reference-type="eqref" reference="eq:triangular-inverse"} makes clear that the first-block spectrum and the shift circle are the only exterior singularities; the finite-rank coupling creates no additional spectral component outside their union.

Neither $\det(I-z\mathcal L)$ nor $\det(I-z\mathcal L^m)$ is an ordinary Fredholm determinant for any $m\ge1$. In particular, squaring does not remove the history-tail obstruction.

One could seek a relative determinant against the shift background, but that would be a scattering construction with a specified reference operator. It is not the direct moving-cloud determinant required in RH-80 [@WangRH80].

# Why finite spectra are misleading

Let $S_L$ be the nilpotent unilateral shift on $\mathbb C^L$, $S_Le_j=e_{j+1}$ for $j<L-1$ and $S_Le_{L-1}=0$. Its spectrum is $\{0\}$ for every $L$, so eigenvalue plots cannot reveal the limiting disk.

[\[prop:resolvent\]]{#prop:resolvent label="prop:resolvent"} For $z\ne0$, $$\label{eq:finite-resolvent}
 (zI-qS_L)^{-1}e_0
 =\sum_{k=0}^{L-1}\frac{q^k}{z^{k+1}}e_k,$$ and hence $$\label{eq:lower-bound}
 \left\lVert(zI-qS_L)^{-1}\right\rVert
 \ge\frac1{|z|}
 \left(\sum_{k=0}^{L-1}(q/|z|)^{2k}\right)^{1/2}.$$ For every fixed $0<|z|<q$, the right side grows exponentially in $L$.

Because $S_L^L=0$, the finite Neumann expansion is exact: $$(zI-qS_L)^{-1}
 =z^{-1}\sum_{k=0}^{L-1}(qS_L/z)^k.$$ Applying it to $e_0$ gives [\[eq:finite-resolvent\]](#eq:finite-resolvent){reference-type="eqref" reference="eq:finite-resolvent"}. The basis vectors are orthonormal, so taking the norm gives the displayed lower bound.

This is a standard finite-section manifestation of nonnormal spectral pollution: the eigenvalues remain at zero while the pseudospectrum expands toward the shift disk [@TrefethenEmbree2005].

# Finite-section audit

The audit uses $L=4,8,16,32,64$ and points $|z|/q=0.25,0.50,0.75$, for 15 resolvent cases. Direct triangular solves agree with [\[eq:lower-bound\]](#eq:lower-bound){reference-type="eqref" reference="eq:lower-bound"} to relative error below $10^{-12}$. Every finite shift spectrum is exactly zero. At $L=64$ the largest recorded resolvent-vector lower bound has $$\log_{10}\left\lVert(zI-qS_L)^{-1}e_0\right\rVert=39.9005.$$

The same audit forms square block truncations of [\[eq:L\]](#eq:L){reference-type="eqref" reference="eq:L"} with $B=0.8\operatorname{diag}(0.25,-0.40)$. Exactly $2(L-1)$ singular values remain at least $q$ in every truncation, matching the growing shift multiplicity. This finite singular floor is the trace- ideal obstruction in elementary matrix form.

# Scope of the no-go theorem

Theorem [\[thm:schatten\]](#thm:schatten){reference-type="ref" reference="thm:schatten"} rejects one precise branch: $$\text{literal infinite normalized history shift}
 \Longrightarrow
 \text{direct trace-ideal determinant}.$$ It does not reject:

1.  a finite cyclic closure, whose wrap edge replaces the unilateral tail;

2.  a relative or scattering determinant with $qS$ as reference;

3.  a difference of two histories in which the shift cancels;

4.  a compactly weighted memory with weights tending to zero by age;

5.  a direct physical transfer-space Riesz construction.

The next paper develops the finite cyclic branch because it preserves a direct finite determinant and, unexpectedly, reproduces the geometric cloud polynomial exactly.

No physical cycle identification, all-level Riesz projection, complement limit, self-adjoint operator, zeta divisor identity, or Riemann Hypothesis is proved.
