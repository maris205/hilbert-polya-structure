---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-fano-threefold-third-moment"
canonical_tex: "henon_dynamics/henon_mu3_fano_threefold_third_moment/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_fano_threefold_third_moment/paper/main.pdf"
source_sha256: "c4a1754b204b052208aec81cd7d938a64afe7b1a5203e2acc3c7985f6fc22abf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fano-Threefold Third Moment for the Fourier--Cubic Hénon Kernel

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_fano_threefold_third_moment>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_fano_threefold_third_moment/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_fano_threefold_third_moment/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_fano_threefold_third_moment/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_fano_threefold_third_moment/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We evaluate the third Galois-normalized chronological moment of the Fourier--cubic Hénon kernel by projective geometry. The six-step zero fibre decomposes into a Fermat cubic fourfold, a split quadric fourfold, and their explicit $(2,3)$ complete-intersection threefold. An exact Jacobi-sum decomposition isolates twenty Tate sectors in the cubic fourfold, while Chevalley--Warning isolates the Tate divisibility in the threefold count. The remaining rank-two and rank-forty pieces give an exact square-root gain after field-degree normalization. This extends the normalized Hénon Euler germ, holomorphically and without zeros, from $\operatorname{Re}s>1/3$ to $\operatorname{Re}s>1/4$. In the inherited normalized semifinite operator category the same function is an eighth-order graded regularized determinant with seven explicit chronological counterterms. This is not a classical Fredholm determinant: the normalized semifinite and ordinary Hilbert Schatten thresholds remain different. No meromorphic continuation through $\operatorname{Re}s=1/4$, functional equation, or Riemann-divisor identification is claimed.
author:
- Hénon Zeta Research Program
bibliography:
- references.bib
date: 14 August 2026
title: 'A Fano-Threefold Third Moment for the Fourier--Cubic Hénon Kernel'
```

## Markdown 正文

# Introduction

The full Fourier--cubic quantization of the homogeneous area-preserving Hénon map produces exact finite-field trace moments. Pairing an additive character with its inverse, then averaging over the maximal real cyclotomic field, gives rational logarithmic moments $c_{p,n}$. Earlier stages of the construction identify the second moment with a genus-four curve, prove normal convergence for $\operatorname{Re}s>1/3$, and realize the Euler germ by a sixth-order determinant relative to a normalized faithful semifinite trace. The first untreated logarithmic term is $n=3$.

The six chronological steps at $n=3$ lead naturally to a cubic fourfold and a $(2,3)$ Fano threefold. Their middle cohomology supplies the next square-root gain.

[\[thm:main\]]{#thm:main label="thm:main"} Let $p>3$ satisfy $p\equiv1\pmod3$, and let $\rho\in\mathbf F_p^\times$ have order three. Outside the finite set of bad reductions of the explicit complete intersection constructed below, the third descended Hénon moment is $$C_{p,3}=-2-\frac{2A_p}{p^2}-\frac{2B_p}{p},
 \qquad
 c_{p,3}=\frac{2C_{p,3}}{p-1},$$ where $A_p$ is the primitive-middle Frobenius trace of a Fermat cubic fourfold and $B_p$ is the middle Frobenius trace of a smooth $(2,3)$ threefold. Their ranks are $22$ and $40$, and hence $$|A_p|\le22p^2,
 \qquad |B_p|\le40p^{3/2},
 \qquad
 |c_{p,3}|\le\frac{92+160\sqrt p}{p-1}.$$ More precisely, $$A_p=20p^2+pa_p,\qquad B_p=pb_p,
 \qquad |a_p|\le2p,\quad |b_p|\le40\sqrt p,$$ and consequently $$C_{p,3}=-42-2b_p-\frac{2a_p}{p}.$$ The finitely many omitted local factors are handled by their unitary-block bound. Consequently the normalized Euler germ is holomorphic and nonzero on $\operatorname{Re}s>1/4$, and there $$\mathcal G(s)=
 \exp\!\left(-\sum_{n=1}^{7}\frac{\ell_n(s)}n\right)
 \operatorname{Det}_{8,\tau,\mathrm{gr}}(I-X_s).$$ Order eight is the least fixed integer order forced by positive $L^q(\mathcal M,\tau)$-membership on the whole half-plane.

All chronology and all prime clocks are retained before the geometric reduction. The theorem is therefore an operator-and-arithmetic advance for the Hénon construction, not a claim that the resulting function already has the Riemann divisor. Purity is used in the precise form proved by Deligne [@Deligne1974 Théorème 1.6]; regularized determinant background is recorded in [@Simon2005 Chapter 9]. Classical context for smooth quadric--cubic Fano threefolds appears in [@BlochMurre1979]. The diagonal-hypersurface calculation uses Weil's Jacobi-sum formula [@Weil1949]; a cohomological formulation is given by Brünjes [@Brunjes2003 Definition 4.4, Proposition 4.5, Theorem 4.6].

# The six-step chronological zero fibre

Fix $\rho\in\mathbf F_p^\times$ of order three. The third moment uses the six-step phase $$\label{eq:phase}
 \Phi_3(x)=2\sum_{i=0}^{5}x_i^3+
 x_0x_1+x_1x_2+x_2x_3+x_3x_4+x_4x_5+\rho x_5x_0.$$ Let $Z_{p,3}=\#\Phi_3^{-1}(0)$. The exact cyclotomic trace normalization inherited from the two-step Hénon kernel is $$\label{eq:moment}
 C_{p,3}=\frac{2Z_{p,3}}{p^2}-2p^3,
 \qquad c_{p,3}=\frac{2C_{p,3}}{p-1}.$$ The factor two is not an averaging convention. If $x_0=\rho^2y_5$ and $x_i=y_{i-1}$ for $1\le i\le5$, direct substitution changes the $\rho$-phase into the $\rho^2$-phase. The two order-three boundary twists therefore have exactly the same zero-fibre count, so their conjugate chronological contributions really are twice the single count in [\[eq:moment\]](#eq:moment){reference-type="ref" reference="eq:moment"}.

Put $$\mathcal C=\sum_{i=0}^{5}x_i^3,
 \qquad
 \mathcal Q=x_0x_1+x_1x_2+x_2x_3+x_3x_4+x_4x_5+\rho x_5x_0,$$ and let $S=V(\mathcal C)$, $R=V(\mathcal Q)$, and $Y=S\cap R$ in $\mathbf P^5$.

[\[prop:direction\]]{#prop:direction label="prop:direction"} One has the exact count $$Z_{p,3}=1+\#\mathbf P^5(\mathbf F_p)-\#S(\mathbf F_p)-\#R(\mathbf F_p)+p\#Y(\mathbf F_p).$$

For a projective direction $[v]$, $$\Phi_3(\lambda v)=\lambda^2
 \bigl(2\lambda\mathcal C(v)+\mathcal Q(v)\bigr).$$ If neither homogeneous value vanishes, exactly one nonzero scalar works. If exactly one vanishes, none works. If both vanish, all $p-1$ nonzero scalars work. Adding the origin proves the formula.

Writing $u=(x_0,x_2,x_4)^t$ and $v=(x_1,x_3,x_5)^t$, the quadratic form is $u^tMv$, where $$M=\begin{pmatrix}1&0&\rho\\1&1&0\\0&1&1\end{pmatrix},
 \qquad \det M=1+\rho=-\rho^2\ne0.$$ Thus $R$ is the split projective quadric fourfold and $$\label{eq:qcount}
 \#R(\mathbf F_p)=1+p+2p^2+p^3+p^4.$$

Write the two remaining point counts as $$\label{eq:traces}
 \#S(\mathbf F_p)=1+p+p^2+p^3+p^4+A_p,
 \qquad
 \#Y(\mathbf F_p)=1+p+p^2+p^3-B_p.$$ Substitution in [\[prop:direction\]](#prop:direction){reference-type="ref" reference="prop:direction"} gives $$\label{eq:zformula}
 Z_{p,3}=p^5-p^2-A_p-pB_p,$$ and then [\[eq:moment\]](#eq:moment){reference-type="ref" reference="eq:moment"} gives the formula in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# The two middle cohomologies

The Fermat cubic $S\subset\mathbf P^5$ is a smooth fourfold in every characteristic different from three. Weak Lefschetz leaves only its middle cohomology outside the projective-space contribution. Its total Chern class is $$c(TS)=\frac{(1+H)^6}{1+3H}
 =1+3H+6H^2+2H^3+9H^4,$$ so $\chi(S)=3\cdot9=27$. Since the four nonmiddle even Betti numbers are one, $b_4(S)=23$, and the primitive rank is $22$. The trace $A_p$ in [\[eq:traces\]](#eq:traces){reference-type="ref" reference="eq:traces"} is therefore pure of weight four, whence $$\label{eq:Abound}
 |A_p|\le22p^2.$$

The Fermat symmetry gives a sharper exact decomposition. Choose a cubic character $\chi$ of $\mathbf F_p^\times$, put $\pi_p=J(\chi,\chi)$, and define $a_p=\pi_p^2+\overline{\pi}_p^{\,2}$. In the six-variable diagonal character sum, the only surviving character multiplicities are $0,3,6$. The twenty mixed choices have three $\chi$'s and three $\overline\chi$'s, and each contributes $p^2$; the two extreme choices contribute $p\pi_p^2$ and $p\overline\pi_p^{\,2}$. Thus $$\label{eq:Aexact}
 A_p=20p^2+pa_p,\qquad a_p\in\mathbf Z,\qquad |a_p|\le2p.$$ This is an exact diagonal-hypersurface identity, not an inference from the finite control ledger.

The intersection $Y=S\cap R$ has type $(2,3)$ in $\mathbf P^5$. At every good reduction it is a smooth threefold. Adjunction gives $$K_Y=\mathcal O_Y(2+3-6)=\mathcal O_Y(-1),$$ so $Y$ is a prime Fano threefold of degree six. Its Chern class is $$c(TY)=\frac{(1+H)^6}{(1+2H)(1+3H)}
 =1+H+4H^2-6H^3,$$ and hence $\chi(Y)=6(-6)=-36$. Weak Lefschetz gives $\chi(Y)=4-b_3(Y)$, so $$\label{eq:b3}
 b_3(Y)=40.$$ The sign in [\[eq:traces\]](#eq:traces){reference-type="ref" reference="eq:traces"} is the odd-cohomology sign in the Lefschetz trace formula. Purity now gives $$\label{eq:Bbound}
 |B_p|\le40p^{3/2}.$$

There is also an exact Tate divisibility. The affine cone over $Y$ is cut out in six variables by equations of degrees two and three. Since $2+3<6$, Chevalley--Warning [@Warning1935] makes its number of $\mathbf F_p$-points divisible by $p$. That number is $1+(p-1)\#Y(\mathbf F_p)$, so $\#Y(\mathbf F_p)\equiv1\pmod p$. From [\[eq:traces\]](#eq:traces){reference-type="ref" reference="eq:traces"} it follows that $$\label{eq:Bexact}
 B_p=pb_p,\qquad b_p\in\mathbf Z,\qquad |b_p|\le40\sqrt p.$$

Combining [\[eq:Aexact,eq:Bexact\]](#eq:Aexact,eq:Bexact){reference-type="ref" reference="eq:Aexact,eq:Bexact"} with the exact moment formula yields $$C_{p,3}=-42-2b_p-\frac{2a_p}{p},$$ and hence $$|C_{p,3}|\le46+80\sqrt p,
 \qquad
 |c_{p,3}|\le\frac{92+160\sqrt p}{p-1}.$$ The finite exact ledger checks these all-prime identities but is not used to promote them to theorems.

# The fourth abscissa and the eighth-order determinant

The logarithm of the normalized Euler product is $$\label{eq:log}
 -\sum_{p\equiv1(3)}\sum_{n\ge1}\frac{c_{p,n}}n p^{-ns}.$$ The inherited first-moment identity $c_{p,1}=-12/(p-1)$ is summable for $\operatorname{Re}s>0$. The genus-four second-moment estimate is $c_{p,2}=O(p^{-1/2})$, so its threshold is $\operatorname{Re}s>1/4$. The new bound $c_{p,3}=O(p^{-1/2})$ has the weaker threshold $\operatorname{Re}s>1/6$. For $n\ge4$, the inherited uniform estimate $$\label{eq:uniform}
 |c_{p,n}|\le4\cdot4^n$$ makes $n=4$ the first remaining wall, again at $\operatorname{Re}s=1/4$.

For completeness, fix a compact set with $\operatorname{Re}s\ge\sigma_0>1/4$ and choose $P_0$ so that $4p^{-\sigma_0}\le1/2$ for $p>P_0$. The large-prime $n\ge4$ tail is bounded by a constant times $\sum_{p>P_0}p^{-4\sigma_0}$. For the finitely many $p\le P_0$, the unitary-block estimate $|c_{p,n}|\le\tau_p(I)=(8p+4)/3$ gives a geometric series because $p^{-\sigma_0}<1$. The finitely many bad reductions are absorbed into this same finite-prime argument. Thus [\[eq:log\]](#eq:log){reference-type="ref" reference="eq:log"} converges locally normally, proving the holomorphic nonvanishing assertion.

Let $(\mathcal M,\tau)$ and $X_s$ be the normalized semifinite product algebra and Galois-sector block inherited from the preceding construction. Exactly $$\tau(|X_s|^q)=
 \sum_{p\equiv1(3)}\frac{8p+4}{3}p^{-q\operatorname{Re}s},
 \qquad
 X_s\in L^q(\mathcal M,\tau)\iff q\operatorname{Re}s>2.$$ Hence $L^8(\mathcal M,\tau)$ is the first fixed integer ideal covering the whole half-plane $\operatorname{Re}s>1/4$. Put $$\ell_n(s)=\sum_pc_{p,n}p^{-ns},\qquad1\le n\le7.$$ The estimates above make each counterterm locally normally convergent there, and the eighth-order trace-associated graded determinant is $$\operatorname{Det}_{8,\tau,\mathrm{gr}}(I-X_s)
 =\exp\!\left(-\sum_{n\ge8}\frac{\operatorname{Str}_\tau(X_s^n)}n\right).$$ Restoring the first seven logarithmic terms gives the factorization in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Order eight is least only among fixed integer orders forced by positive $L^q(\mathcal M,\tau)$-membership; no claim is made about unrelated exotic regularizations.

The ordinary Hilbert direct sum is different: $$X_s\in S^q(\mathcal H)\iff q\operatorname{Re}s>3.$$ It is classically trace class only for $\operatorname{Re}s>3$, and its local supertrace produces the ordinary Galois norm rather than the field-degree-normalized root. The object above is therefore a genuine normalized-semifinite regularized determinant, not a mislabeled classical Fredholm determinant.

# Route-A audit

The formal classification is $$\begin{gathered}
 \mathrm{A1\_WEAK},\qquad
 \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\qquad
 \mathrm{A4\_NATURAL\_QUANTIZATION}.
\end{gathered}$$

The positive result is substantial: an exact six-step Hénon trace has become a Frobenius trace on a Fano threefold, the normalized Euler germ extends farther left of the Riemann critical abscissa, from $\operatorname{Re}s>1/3$ to $\operatorname{Re}s>1/4$, and a canonical eighth-order determinant in the normalized semifinite category realizes it. Nothing was fitted to zeta zeros, no prime clock was shifted, and no chronological transition was averaged.

A1 remains weak because the primes label arithmetic fibres rather than primitive cycles of one real Hénon map. A3 remains partial because the construction has no Gamma factor, functional equation, continuation through the fourth abscissa, zero-counting law, or Riemann-divisor match. A4 is natural at each finite place, but the global object is regularized and no self-adjoint Hilbert--Pólya generator has been constructed. Thus the project remains Route-A exploratory, albeit with a strictly stronger A2 half-plane.

The next mathematical wall is the fourth chronological moment. Its resolution would require another source-derived cohomological decay theorem; the present paper does not infer such a pattern from the first three moments.

# Smoothness scope {#sec:smoothness}

We record the exact scope needed by the analytic theorem. Over $\mathbf Q(\rho)$, $\rho^2+\rho+1=0$, a singular point of $Y=V(\mathcal C,\mathcal Q)$ would satisfy $\nabla\mathcal C=\lambda\nabla\mathcal Q$. The case $\lambda=0$ has no projective solution. After scaling $x_i=\lambda y_i$, the six gradient equations become the quadratic recurrence $$\begin{aligned}
3y_0^2&=y_1+\rho y_5,&
3y_1^2&=y_0+y_2,\\
3y_2^2&=y_1+y_3,&
3y_3^2&=y_2+y_4,\\
3y_4^2&=y_3+y_5,&
3y_5^2&=y_4+\rho y_0.\end{aligned}$$ Eliminating successively from $y_0,y_1$, and adjoining $\mathcal Q(y)=0$, gives the exact characteristic-zero ideal $$\langle y_0,y_1,\rho^2+\rho+1\rangle.$$ Thus the generic fibre is smooth. Clearing the finite set of coefficients in this elimination gives a model smooth away from finitely many rational primes. This generic statement is already sufficient for [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}: finitely many local logarithms are analytic for $|p^{-s}|<1$ and do not affect normal convergence.

The released certificate additionally records exact finite-field Jacobian controls. Any stronger assertion that every split prime is good is made only if its cleared-denominator elimination certificate is included; a finite scan is never promoted to an all-prime theorem.
