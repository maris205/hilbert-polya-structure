---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--exact-uc-polar-growth-order"
canonical_tex: "logistic_dynamics/projects/exact_uc_polar_growth_order/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/exact_uc_polar_growth_order/paper/main.pdf"
source_sha256: "b0044b64bfafa33dd49d3601ae37722e426a04486ac65ae5bbee47018d013d2b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Quadratic Growth and a Zero-Free Half-Plane for the Exact-$U_c$ Polar Fredholm Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/exact_uc_polar_growth_order>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_growth_order/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/exact_uc_polar_growth_order/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/exact_uc_polar_growth_order/README.md>)
- [BibTeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_growth_order/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the unchanged Fredholm determinant of the frozen exact-$U_c$ polar Logistic transfer family, we prove a global quadratic exponential bound in the roof parameter. The proof keeps the matching-space operator and its canonical determinant fixed. A Riemann-map Taylor factorization organizes the operator into two geometric rank-one streams. Hadamard's minor bound and the elementary symmetric-function identity for a geometric sequence then give a determinant coefficient majorant that is Gaussian in the rank. As a result, $|D_{\mathrm{pol}}(s)|\le
   \exp(C_0+C_1(1+|s|)^2)$, so the classical entire-function order is at most two. Jensen's formula, anchored at a point where the determinant is nonzero, yields an $O(R^2)$ disk-count upper bound and hence an $O(T^2)$ upper bound in every fixed real strip. Independently, the exact signed trace ledger and the one-step roof lower bound prove that $D_{\mathrm{pol}}$ has no zeros when $$\Re s>\frac{\log 2}{\log(4/U_c^2)}
   =1.3382657903899534\ldots.$$ All statements concern the same dynamical determinant: no exact growth order, sharp divisor asymptotic, determinant-root computation, or external divisor comparison is claimed.
author:
- Anonymous
date: August 2026
title: |
  Quadratic Growth and a Zero-Free Half-Plane\
  for the Exact-$U_c$ Polar Fredholm Determinant
```

## Markdown 正文

# Frozen determinant and main result

Let $u=U_c$ be the real root of $$u^3-2u^2+2u-2=0,
 \qquad \rho=u-1.$$ The underlying real system is the inherited two-full-branch polar map on $I_L=[-\pi/2,0]$ and $I_R=[0,\pi/2]$. Its inverse branches $\phi_L,\phi_R$ extend holomorphically to the fixed radius-$10^{-3}$ stadiums $U_L,U_R$. They share a holomorphic logarithm $\ell=\operatorname{Log}a$, with $\phi_L'=a$ and $\phi_R'=-a$.

On $$X=A(U_L)\oplus A(U_R),
 \qquad
 B=\{(v_L,v_R):v_L(0)=v_R(0)\},$$ the frozen transfer family is $$(\mathcal{L}_s v)_j(z)=\mathrm{e}^{s\ell(z)}
 \bigl[v_L(\phi_L(z))+v_R(\phi_R(z))\bigr].
 \tag{1}$$ Both outputs of (1) are restrictions of one holomorphic expression, so $\mathcal{L}_s(B)\subset B$. The preceding analytic stage establishes that $\mathcal{L}_{s,B}:=\mathcal{L}_s|_B$ is nuclear of order zero and that $$D_{\mathrm{pol}}(s):=\operatorname{det}_{\mathrm{Fr}}(I-\mathcal{L}_{s,B})
 \tag{2}$$ is entire. Equation (2) is retained throughout; neither the operator nor the determinant convention is replaced.

There exist constants $C_0,C_1<\infty$, depending only on the frozen stadiums and $\ell$, such that $$|D_{\mathrm{pol}}(s)|\le
 \exp\!\bigl(C_0+C_1(1+|s|)^2\bigr)
 \qquad(s\in\mathbb{C}).
 \tag{3}$$ Consequently $\operatorname{ord}(D_{\mathrm{pol}})\le2$. Its zero count, with multiplicity, satisfies $$N_D(2;R)=O(R^2)
 \tag{4}$$ in disks $|s-2|\le R$, and for every fixed real interval $[a,b]$, $$N_D([a,b];T)=O_{a,b}(T^2)
 \tag{5}$$ in $a\le\Re s\le b$, $|\Im s|\le T$. Finally, $D_{\mathrm{pol}}$ has no zeros in $$\Re s>\sigma_*:=\frac{\log2}{\log(4/U_c^2)}
 =1.3382657903899534\ldots.
 \tag{6}$$

The theorem gives only upper information. In particular, $\operatorname{ord}(D_{\mathrm{pol}})\le2$ is not an equality assertion, and (4)--(5) are not sharp counting asymptotics.

# Two geometric rank-one streams

Let $V_\sigma\Subset U_\sigma$ be the proof-only radius- $6\cdot10^{-4}$ stadium around $I_\sigma$. Normalize Riemann maps $h_\sigma:\mathbb{D}\to U_\sigma$ by $$h_L(0)=-\frac\pi4,
 \qquad h_R(0)=\frac\pi4,
 \qquad h_\sigma'(0)>0.$$ Compact containment defines fixed constants $$r_\sigma=\max_{z\in\overline V_\sigma}
 |h_\sigma^{-1}(z)|<1,
 \qquad r=\max(r_L,r_R)<1.
 \tag{7}$$ These conformal quantities are proof coordinates; they do not change the domains in (1).

For $f\in A(U_\sigma)$, expand $$f\circ h_\sigma(\zeta)
 =\sum_{m\ge0}\lambda_{\sigma,m}(f)\zeta^m,
 \qquad \|\lambda_{\sigma,m}\|\le1.
 \tag{8}$$ For $v\in B$, set $$u_{\sigma,m}(v)=\lambda_{\sigma,m}(v_\sigma),$$ and define $x_{\sigma,m}(s)\in B$ by $$\bigl(x_{\sigma,m}(s)\bigr)_j(z)
 =\mathrm{e}^{s\ell(z)}
 \bigl(h_\sigma^{-1}(\phi_\sigma(z))\bigr)^m.
 \tag{9}$$ The matching condition holds because the two components in (9) are restrictions of the same holomorphic function. Hence the full matching-space operator has the two-stream representation $$\mathcal{L}_{s,B}
 =\sum_{\sigma\in\{L,R\}}\sum_{m\ge0}
 x_{\sigma,m}(s)\otimes u_{\sigma,m}.
 \tag{10}$$

Put $$W(s)=\max_{j\in\{L,R\}}
 \|\mathrm{e}^{s\ell}\|_{A(U_j)},
 \qquad L_\ell=\|\ell\|_{A(U_L\cup U_R)}.$$ Then $$W(s)\le\mathrm{e}^{L_\ell|s|},
 \qquad
 \|u_{\sigma,m}\|\,\|x_{\sigma,m}(s)\|
 \le W(s)r_\sigma^m.
 \tag{11}$$ The inherited complex enclosure supplies the convenient safe value $L_\ell<0.824$, although the growth proof needs only finiteness.

The grouping in (10) is essential. There are two streams, indexed by the input branch. Splitting both output components would give four ambient blocks, but a vector supported on only one output component need not belong to $B$.

# Quadratic determinant growth

The two geometric streams force a negative quadratic exponent in the Fredholm coefficients. To see this, truncate (10) and write the resulting finite-rank operator as $T=X\Phi$. Sylvester's identity reduces $\det_B(I-T)$ to a finite matrix determinant. For a principal minor using $q$ rank-one terms, Hadamard's inequality gives $$\left|\det[u_i(x_j)]_{i,j\in I}\right|
 \le q^{q/2}\prod_{i\in I}\|u_i\|\,\|x_i\|.
 \tag{12}$$

Let $e_q(s)$ be the $q$-th elementary symmetric sum of $$\{W(s)r_L^m:m\ge0\}
 \quad\text{and}\quad
 \{W(s)r_R^m:m\ge0\}.$$ For a single geometric sequence, $$\sum_{0\le m_1<\cdots<m_k}r^{m_1+\cdots+m_k}
 =\frac{r^{k(k-1)/2}}{\prod_{h=1}^k(1-r^h)}.
 \tag{13}$$ Set $C_r=\prod_{h\ge1}(1-r^h)^{-1}<\infty$. Splitting $q=k+(q-k)$ terms between the two streams and using $$\frac{k(k-1)}2+
 \frac{(q-k)(q-k-1)}2
 \ge \frac{q^2}{4}-\frac q2
 \tag{14}$$ yields $$e_q(s)\le C_r^2(q+1)W(s)^q
 r^{q^2/4-q/2}.
 \tag{15}$$ Combining (12) and (15), and then passing from the finite truncations to the canonical determinant, gives $$|D_{\mathrm{pol}}(s)|
 \le 1+C_r^2\sum_{q\ge1}
 q^{q/2}(q+1)W(s)^q r^{q^2/4-q/2}.
 \tag{16}$$

Write $\beta=-\log r>0$. After inserting $W(s)\le\mathrm{e}^{L_\ell|s|}$, the logarithm of the $q$-th summand in (16) is at most $$-\frac\beta4q^2
 +\left(L_\ell|s|+\frac\beta2\right)q
 +\frac q2\log q+\log(q+1)+O_r(1).
 \tag{17}$$ The subquadratic terms in $q$ can be absorbed into half of the negative quadratic term. Completing the square in the remaining Gaussian sum proves (3). Equivalently, $$\log M_D(R)=O(R^2),
 \qquad
 M_D(R)=\max_{|s|\le R}|D_{\mathrm{pol}}(s)|,$$ and therefore $\operatorname{ord}(D_{\mathrm{pol}})\le2$.

# Explicit zero-free right half-plane

The zero-free region comes from the exact trace ledger, not from the absolute determinant majorant. Define $$\alpha_0=\frac{U_c^2}{4},
 \qquad
 \tau_*=-\log\alpha_0=\log\frac4{U_c^2}>0.
 \tag{18}$$ The real roof obeys $\tau\ge\tau_*$. Thus every based word $\omega$ of length $n$ satisfies $$T_\omega\ge n\tau_*,
 \qquad \mathrm{e}^{-T_\omega}\le\alpha_0^n.
 \tag{19}$$

The unchanged signed trace identity is $$\operatorname{Tr}\mathcal{L}_s^n
 =\sum_{\omega\in\{L,R\}^n}
 \frac{\mathrm{e}^{-sT_\omega}}
 {1-\varepsilon_\omega\mathrm{e}^{-T_\omega}},
 \qquad
 \varepsilon_\omega=(-1)^{\#R(\omega)}.
 \tag{20}$$ For $\sigma=\Re s\ge0$, equations (19)--(20) give the absolute majorant $$|\operatorname{Tr}\mathcal{L}_s^n|
 \le \frac{(2\alpha_0^\sigma)^n}{1-\alpha_0^n}.
 \tag{21}$$ The sign in (20) remains part of the determinant formula; (21) is used only to prove absolute convergence.

When $$\sigma>\sigma_*:=\frac{\log2}{-\log\alpha_0},
 \qquad q_\sigma:=2\alpha_0^\sigma<1,$$ we have $$\sum_{n\ge1}\frac{|\operatorname{Tr}\mathcal{L}_s^n|}{n}
 \le
 \frac{-\log(1-q_\sigma)}{1-\alpha_0}
 =:B(\sigma).
 \tag{22}$$ Keeping the auxiliary Fredholm variable $\lambda$ distinct from $s$, the same estimate converges for $|\lambda|q_\sigma<1$. Its disk therefore contains $\lambda=1$, and analytic continuation from a neighborhood of zero gives $$D_{\mathrm{pol}}(s)=
 \exp\left(-\sum_{n\ge1}\frac{\operatorname{Tr}\mathcal{L}_s^n}{n}\right).
 \tag{23}$$ It follows that $$D_{\mathrm{pol}}(s)\ne0
 \qquad\left(\Re s>
 \frac{\log2}{\log(4/U_c^2)}\right).
 \tag{24}$$ This is precisely the zero-free half-plane in (6).

# Jensen divisor upper bound

Equation (24) supplies the nonzero anchor $D_{\mathrm{pol}}(2)\ne0$. Apply Jensen's formula to $$F(z)=D_{\mathrm{pol}}(2+z)$$ on $|z|=2R$ and count zeros in $|z|\le R$. The global envelope (3) controls the boundary mean of $\log|F|$, while $F(0)\ne0$ fixes the Jensen anchor. Consequently, counting multiplicity, $$N_D(2;R)=O(R^2).
 \tag{25}$$

For any fixed $[a,b]\subset\mathbb R$, the rectangle $$\{s:a\le\Re s\le b,\ |\Im s|\le T\}$$ lies in a disk centered at $2$ of radius $T+O_{a,b}(1)$. Equation (25) therefore implies $$N_D([a,b];T)=O_{a,b}(T^2).
 \tag{26}$$

The implication is one-way: quadratic entire-function growth gives a quadratic zero-count upper bound. It supplies neither a matching lower bound nor a sharp strip asymptotic.

# Limitations and conclusion

The same exact-$U_c$ polar Fredholm determinant now has a global growth envelope and an explicit zero-free region. Its two geometric rank-one streams yield classical order at most two, Jensen gives an $O(T^2)$ fixed-strip zero-count upper bound, and the positive roof lower bound makes the signed trace logarithm converge at $\lambda=1$ throughout the stated right half-plane.

The conclusion is deliberately one-sided. The proof does not show that the order equals two, does not give lower growth or a sharp divisor asymptotic, and does not evaluate a determinant zero. No comparison with an external divisor is made. The next intrinsic refinement is to certify numerical upper bounds for the normalized conformal ratios $r_L,r_R$, which would make the quadratic-type constant in (3) explicit without changing the object or searching for roots.

# Proof appendix

## Passage from finite truncations

For a cutoff $M$, retain in (10) only $m\le M$. This gives a finite-rank operator $T_M$. For every $0<p\le1$, equation (11) gives $$\sum_{\sigma\in\{L,R\}}\sum_{m>M}
 \bigl(\|u_{\sigma,m}\|\,\|x_{\sigma,m}(s)\|\bigr)^p
 \le W(s)^p\sum_\sigma\frac{r_\sigma^{p(M+1)}}{1-r_\sigma^p}.$$ On compact $s$-sets the right side tends uniformly to zero. Choose $p<2/3$. The canonical Grothendieck determinant is continuous in this ideal, so $\det(I-T_M)\to D_{\mathrm{pol}}(s)$ locally uniformly. The finite-rank minor estimate therefore passes to (16) without changing the determinant convention.

## Elementary symmetric bound

For one stream, expanding $\prod_{m\ge0}(1+tr^m)$ and using the finite geometric $q$-binomial identity gives (13). If $k$ indices come from the left stream and $q-k$ from the right stream, replacing both ratios by $r=\max(r_L,r_R)$ bounds that allocation by $$C_r^2W(s)^q
 r^{k(k-1)/2+(q-k)(q-k-1)/2}.$$ The exponent is minimized by a balanced split. Inequality (14) is its uniform quadratic lower bound, and summing the $q+1$ possible allocations proves (15).

## Gaussian summation

Let $S_q(s)$ denote the $q$-th summand of (16). For fixed $\beta>0$, there is a constant $c_\beta$ such that $$\frac q2\log q+\log(q+1)
 \le\frac\beta8q^2+c_\beta q
 \qquad(q\ge1).$$ Thus, with $A(s)=L_\ell|s|+\beta/2+c_\beta$, $$\log S_q(s)\le
 -\frac\beta8q^2+A(s)q+O_r(1).$$ Completing the square gives $$-\frac\beta8q^2+A(s)q
 =-\frac\beta8\left(q-\frac{4A(s)}\beta\right)^2
 +\frac{2A(s)^2}{\beta}.$$ The translated Gaussian sum is bounded by a constant depending only on $\beta$. Since $A(s)=O(1+|s|)$, equation (3) follows.

## Jensen count

Apply Jensen's formula to $F(z)=D_{\mathrm{pol}}(2+z)$ between radii $R$ and $2R$. Every zero in $|z|\le R$ contributes at least $\log2$ to the Jensen sum at radius $2R$. Therefore $$N_D(2;R)\log2
 \le \frac1{2\pi}\int_0^{2\pi}
 \log|F(2R\mathrm{e}^{i\theta})|\,d\theta-\log|F(0)|.$$ The first term is $O(R^2)$ by (3), and the second is finite by (24). This proves (25), from which the fixed-strip bound (26) follows by geometric containment.

# References {#references .unnumbered}

No external references are cited in this self-contained stage report. The proof depends only on the frozen determinant established in the preceding project stage and on standard complex-analysis inequalities.
