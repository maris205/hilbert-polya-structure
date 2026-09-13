---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--exact-uc-polar-nuclear-fredholm"
canonical_tex: "logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/main.pdf"
source_sha256: "0efad7ac718371e58105f8a5b942dc9e630c983f29bf30da5b7737ff6eebfdc4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Order-Zero Nuclearity and an Exact Fredholm Ledger for the Exact-$U_c$ Polar Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/README.md>)
- [BibTeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove that a frozen two-component transfer family attached to the exact-$U_c$ polar Logistic map is nuclear of order zero on its natural matching space. The construction uses the intrinsic log-Jacobian roof and a single holomorphic branch germ on fixed radius-$10^{-3}$ stadiums. An explicit Riemann-map Taylor expansion factors every weighted pullback through a compactly nested inner stadium, yielding a canonical Fredholm determinant $\Delta(\lambda,s)$ that is entire in both variables. The matching condition is shown to preserve, rather than alter, the ambient determinant and trace ledger. For every based inverse word the trace term is $\mathrm{e}^{-sT}/(1-\varepsilon\mathrm{e}^{-T})$, with the orientation sign retained in the denominator. A sealed target-free regression checks all 510 words of length at most eight at 100-digit precision. The result is an analytic determinant theorem only: it establishes neither a prime-orbit law nor a Riemann-zero, completed-$\xi$, growth-counting, or quantization result.
author:
- Anonymous
date: August 2026
title: |
  Order-Zero Nuclearity and an Exact Fredholm Ledger\
  for the Exact-$U_c$ Polar Map
```

## Markdown 正文

# Exact polar and matching setup

Let $u=U_c$ be the real root of $$u^3-2u^2+2u-2=0,\qquad \rho=u-1.$$ The inherited real system is the two-full-branch polar map $G=q^{-1}\circ(-f^2)\circ q$, where $f(x)=1-ux^2$ and $q(\theta)=\rho\sin\theta$. Its branch intervals are $I_L=[-\pi/2,0]$ and $I_R=[0,\pi/2]$. The intrinsic determinant clock is $\tau=\log|G'|$; one polar step corresponds to two physical Logistic iterates, but that physical count is not used below.

Let $U_\sigma$ be the radius-$10^{-3}$ stadium around $I_\sigma$. The previous branch construction provides holomorphic inverse branches $\phi_L,\phi_R$, a common holomorphic logarithm $\ell=\operatorname{Log}a$, and $$\phi_L'=a,\qquad \phi_R'=-a,\qquad
 \sup_{U_L\cup U_R}|a|<0.59626<1.$$ On $X=A(U_L)\oplus A(U_R)$, where $A(U)=\mathcal{O}(U)\cap C(\overline U)$, set $$B=\{(v_L,v_R):v_L(0)=v_R(0)\}.$$ The weighted family is $$(\mathcal{L}_s v)_j(z)=\mathrm{e}^{s\ell(z)}
 [v_L(\phi_L(z))+v_R(\phi_R(z))],\qquad j\in\{L,R\}.$$ This setup uses no arithmetic target data. The exact parameter, roof, domains, orientations, and half-open geometric coding are fixed by the mirrored source lock.

# Explicit Riemann-map Taylor nuclear factorization

Let $V_\sigma$ be the radius-$6\cdot10^{-4}$ stadium around $I_\sigma$. The inherited compact inclusion gives $$\phi_\sigma(\overline U_j)\subset V_\sigma\Subset U_\sigma
 \quad (j,\sigma\in\{L,R\}).$$ The inner stadium is a proof device and does not change the operator domain.

Fix a Riemann map $h_\sigma:\mathbb{D}\to U_\sigma$. Compact containment gives $r_\sigma<1$ such that $\sup_{\overline V_\sigma}|h_\sigma^{-1}|\le r_\sigma$. If $f\circ h_\sigma=\sum_{m\ge0}\lambda_{\sigma,m}(f)\zeta^m$, Cauchy estimates give $\|\lambda_{\sigma,m}\|\le1$. Hence the restriction $$R_\sigma=
 \sum_{m\ge0}\lambda_{\sigma,m}\otimes
 \left.(h_\sigma^{-1})^m\right|_{V_\sigma}$$ is $p$-nuclear for every $0<p\le1$, because $\sum_{m\ge0}r_\sigma^{mp}<\infty$. Thus it is nuclear of order zero.

Each branch block factors as $Q_{j\sigma}(s)R_\sigma$, with $$Q_{j\sigma}(s)g=\mathrm{e}^{s\ell}\,(g\circ\phi_\sigma).$$ The latter map is bounded. The nuclear ideal property and the finite block sum prove order-zero nuclearity of $\mathcal{L}_s$. Since $\ell$ is bounded on the frozen closures, $\partial_s^k\mathrm{e}^{s\ell}=\ell^k\mathrm{e}^{s\ell}$ shows that $s\mapsto\mathcal{L}_s$ is entire locally in every $p$-nuclear ideal.

# Complemented matching determinant

Define $\delta(v)=v_L(0)-v_R(0)$ and let $e=(1,0)$. Since $\delta(e)=1$, the map $P_B=I-e\delta$ is a bounded projection and $X=B\oplus\mathbb{C}e$. Both outputs of $\mathcal{L}_s$ are restrictions of the same holomorphic expression. Therefore $\mathcal{L}_s(X)\subset B$, and relative to this decomposition it has the form $$\mathcal{L}_s=\begin{pmatrix}\mathcal{L}_{s,B}&b_s\\0&0\end{pmatrix}.$$ Consequently all power traces, and hence the canonical determinants, agree: $$\operatorname{Tr}_X(\mathcal{L}_s^n)=\operatorname{Tr}_B(\mathcal{L}_{s,B}^n),\qquad
 \operatorname{det}_{\mathrm{Fr}}(I-\lambda\mathcal{L}_s)=\operatorname{det}_{\mathrm{Fr}}(I-\lambda\mathcal{L}_{s,B}).$$ We define $$\Delta(\lambda,s)=\operatorname{det}_{\mathrm{Fr}}(I-\lambda\mathcal{L}_{s,B}),
 \qquad D_{\rm pol}(s)=\Delta(1,s).$$ The order-zero nuclear determinant theorem and the ideal-valued entire dependence from the preceding section make $\Delta$ jointly entire in $(\lambda,s)$. This is a canonical Grothendieck determinant, not a regularized determinant, spectral-zeta determinant, Euler product, or a physical-return determinant.

# Exact based-fixed-point trace

For a word $\omega=(\omega_0,\ldots,\omega_{n-1})$, write $\Phi_\omega=\phi_{\omega_0}\circ\cdots\circ\phi_{\omega_{n-1}}$. For a diagonal block path $(j_0,\ldots,j_{n-1})$, this word is the bijective reverse-order relabelling $\omega=(j_0,j_{n-1},\ldots,j_1)$; a based orbit may subsequently be cyclically relabelled. It contracts its appropriate frozen stadium and has a unique fixed point $p_\omega$. Set $$T_\omega=-\log|\Phi_\omega'(p_\omega)|,
 \qquad \varepsilon_\omega=(-1)^{\#R(\omega)}.$$ The common branch germ gives $$\Phi_\omega'(p_\omega)=\varepsilon_\omega\mathrm{e}^{-T_\omega},
 \qquad W_{\omega,s}(p_\omega)=\mathrm{e}^{-sT_\omega}.$$ The weighted-composition fixed-point trace formula therefore yields $$\operatorname{Tr}(\mathcal{L}_s^n)=
 \sum_{\omega\in\{L,R\}^n}
 \frac{\mathrm{e}^{-sT_\omega}}
 {1-\varepsilon_\omega\mathrm{e}^{-T_\omega}}.$$ This is a based-word formula. Distinct cyclic rotations are retained when they are distinct. A least-period-$d$ orbit repeated to length $n=rd$ contributes its $d$ based points; the $1/n$ factor in the local logarithm of the determinant supplies the usual $1/r$ coefficient.

The only boundary periodic point is the left point $P=-\pi/2$. With $a_P=u^2/4$, its pure-left contribution is $$\frac{a_P^{ns}}{1-a_P^n}.$$ Although $P$ is a real endpoint, it is interior to its complex stadium; there is no half-weight. It also belongs only to the left component, so the matching condition supplies no doubled-copy correction.

# Sealed 510-word target-free certificate

The accompanying regression program enumerates every based word of lengths one through eight, for a total of $$\sum_{n=1}^{8}2^n=510$$ words. At 100 decimal digits it verifies a contraction fixed point, cyclic rotation agreement for the roof and signed inverse derivative, the parity rule $\varepsilon_\omega=(-1)^{\#R(\omega)}$, and the signed denominator. It separately checks the pure-left boundary identities through length eight.

The certificate is sealed as an implementation regression, not as evidence for an all-order theorem; the all-order statements above come from the analytic factorization and fixed-point trace theorem. It uses only the certified $U_c$ bracket and inherited branch formulas. In particular, it contains no prime table, Riemann-zero table, $\zeta$ or $\xi$ evaluation, or Fredholm-zero calculation.

  Quantity                   Sealed value
  -------------------------- --------------------
  Maximum word length        $8$
  Based words checked        $510$
  Complex derivative bound   $<0.59626$
  Precision                  100 decimal digits
  External target data       none

# Limitations and conclusion

The result is deliberately narrow. It gives a genuine same-object analytic Fredholm determinant and a signed dynamical trace ledger, but it does not identify the divisor of $D_{\rm pol}$. There is no theorem relating primitive roof periods to logarithms of primes, no von-Mangoldt amplitude, functional equation, Gamma factor, trivial-zero ledger, completed-$\xi$ identity, or Riemann--von Mangoldt counting law. No Fredholm zero has been computed in this stage.

Accordingly, the analytic Route-A tuple is $$\begin{aligned}
(&\mathrm{A1\_WEAK},\ \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\ \mathrm{A4\_FAIL}),
\end{aligned}$$ while the Riemann-target tuple remains $$(\mathrm{A1\_WEAK},\ \mathrm{A2\_FAIL},\
 \mathrm{A3\_FAIL},\ \mathrm{A4\_FAIL}).$$ There is no Hilbert space lift, self-adjoint operator, or Route-B result. The next smallest target-free task is a growth-order bound or a high-imaginary-height divisor-count regime for $D_{\rm pol}$, before any comparison to a target divisor is considered.

# Proof appendix

## Order-zero restriction

For a bounded Jordan stadium $U$ and $V\Subset U$, choose a Riemann map $h:\mathbb{D}\to U$. Compactness gives $r<1$ with $h^{-1}(\overline V)\subset r\overline\mathbb{D}$. Cauchy coefficients of $f\circ h$ have norm at most $\|f\|_{A(U)}$. The expansion $$f|_V=\sum_{m\ge0}\lambda_m(f)(h^{-1})^m|_V$$ therefore converges in every $p$-nuclear quasi-norm, $0<p\le1$, because $\sum r^{mp}<\infty$. This proves the required restriction theorem with a fixed factorization independent of $s$.

## Entire family and determinant

On a compact set of roof parameters, multiplication by $\ell^k\mathrm{e}^{s\ell}$ is bounded uniformly after division by a suitable factorial. Combining this bound with the preceding fixed nuclear expansion shows local convergence of the Taylor series in every $p$-nuclear ideal. The canonical determinant of an order-zero nuclear operator is entire in its operator argument, which yields joint entireness of $\Delta$.

## Trace and multiplicity

Each diagonal word block is a one-variable weighted composition operator on a stadium. The reverse-order relabelling $\omega=(j_0,j_{n-1},\ldots,j_1)$ is a bijection from diagonal block paths to binary based words and preserves right-branch parity. Its contraction has one isolated fixed point and contributes weight divided by $1-\Phi_\omega'(p_\omega)$. The sign of the derivative is exactly the parity of the right inverse branches. Summing diagonal blocks gives the based-word formula. The complemented block form transfers it from the ambient space to the matching space without any additional multiplicity.

# References {#references .unnumbered}

No external references are cited in this self-contained stage report. The formal source note and source lock are mirrored in the project root.
