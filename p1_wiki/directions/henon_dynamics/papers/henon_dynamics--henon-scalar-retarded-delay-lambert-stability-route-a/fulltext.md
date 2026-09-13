---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-scalar-retarded-delay-lambert-stability-route-a"
canonical_tex: "henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a/paper/main.pdf"
source_sha256: "dbe1f5eacd94d39a3296d34406edda9b559f700ead4b9071e92e112a998adbda"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Lambert--W and Hopf Atlas for a Scalar Retarded Semigroup

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_scalar_retarded_delay_lambert_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the scalar retarded equation $x'(t)=-a x(t)-b x(t-\tau)$ on $C([-\tau,0];\mathbb C)$ for all nonnegative $a,b,\tau$. One theorem package closes the characteristic roots through Lambert $W$, the exact method-of-steps fundamental solution, eventual compactness of the history semigroup, algebraic multiplicities, and the complete stability/Hopf boundary. The result is deliberately source-local: a characteristic function is not renamed a Fredholm determinant, and no arithmetic or target spectral claim is made. The strict Route-A record is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
author:
- 'Route-A dynamics study --- HCS-C210'
date: 28 August 2026
title: 'A Lambert--W and Hopf Atlas for a Scalar Retarded Semigroup'
```

## Markdown 正文

suppressoptionalinfo 611

#### Revision status.

Revision checkpoint: all Hopf crossings and retarded root-continuity proof boundary added.AI-use disclosure: language assistance was used for drafting and code review; all displayed identities and receipts are independently checked.

# Owner, clock, and scope

For $\tau>0$ write $X=C([-\tau,0];\mathbb C)$ with the supremum norm and $x_t(\theta)=x(t+\theta)$. The generator is $$A\phi=\phi',\qquad D(A)=\{\phi\in C^1:\phi'(0)=-a\phi(0)-b\phi(-\tau)\}.$$ The clock is physical elapsed time and the normalization is $r(0)=1$, $r(t)=0$ for $t<0$. The case $\tau=0$ is the scalar ODE. These choices are frozen before any calculation; no fitted parameter or target data is used.

# Characteristic spectrum

For $\tau>0$ and $b>0$, the characteristic function $$\Delta(\lambda)=\lambda+a+b e^{-\lambda\tau}$$ has precisely the roots $$\lambda_k=-a+\tau^{-1}W_k(-b\tau e^{a\tau}),\qquad k\in\mathbb Z,$$ counted with algebraic multiplicity. A multiple root is possible exactly when $b\tau e^{a\tau}=e^{-1}$; it then has multiplicity two and is $\lambda=-a-\tau^{-1}$.

Indeed $W e^W=-b\tau e^{a\tau}$ gives the displayed substitution, while $\Delta'=1-b\tau e^{-\lambda\tau}$ and $\Delta''=b\tau^2e^{-\lambda\tau}$ give the multiplicity assertion. The branch point is not a Hopf boundary in general; the two loci are kept separate in the evidence.

# Method of steps and compactness

For $\tau>0$, $$r(t)=\sum_{n=0}^{\lfloor t/\tau\rfloor}
 \frac{(-b)^n}{n!}e^{-a(t-n\tau)}(t-n\tau)^n,\qquad t\geq0.$$

At the zero-delay face the fundamental solution is instead $r(0)=1$ and $r(t)=e^{-(a+b)t}$ for $t>0$; the delayed formula is not silently continued through $\tau=0$. The Laplace transform is $$\frac1{\Delta(s)}=\frac1{s+a}
 \sum_{n\geq0}\frac{(-b)^n e^{-ns\tau}}{(s+a)^n},$$ and inversion term by term gives the formula. The history solution operators $T(t)$ form a strongly continuous semigroup. For $t>\tau$, a bounded set of histories is mapped into a bounded equicontinuous subset of $C^1$; hence Arzelà--Ascoli makes $T(t)$ compact. The standard eventual-compact spectral mapping statement therefore gives $$\sigma(T(t))\setminus\{0\}=\exp\!\bigl(t\sigma(A)\bigr).$$ At a nonzero semigroup eigenvalue $\mu$, algebraic multiplicity is the sum of the characteristic-root multiplicities over all roots satisfying $e^{t\lambda}=\mu$; exponential collisions are thus aggregated. This is an operator theorem for the delay owner, not a target determinant construction.

# Stability and Hopf surface

If $a\geq b$ and $(a,b)\ne(0,0)$, the semigroup is exponentially stable for every finite $\tau$. If $b>a$, set $$\omega=\sqrt{b^2-a^2},\qquad
 \tau_c=\frac{\arccos(-a/b)}{\omega}.$$ It is exponentially stable exactly when $0\leq\tau<\tau_c$; at $\tau_c$ the only imaginary roots are the simple pair $\pm i\omega$, and for $\tau>\tau_c$ there is a right-half-plane conjugate pair. The crossing is transversal: $$\frac{d\operatorname{Re}\lambda}{d\tau}
 =\frac{\omega^2}{(1+a\tau)^2+(\omega\tau)^2}>0.$$

To see the boundary, substitute $i\omega$ into $\Delta=0$ to obtain $a+b\cos(\omega\tau)=0$ and $\omega=b\sin(\omega\tau)$. A crossing can therefore occur only for $b>a$. Continuity from $\tau=0$ and the positive crossing derivative give the stated regions. More explicitly, all Hopf crossings are at $$\tau_m=\frac{\arccos(-a/b)+2\pi m}{\omega},\qquad m=0,1,2,\ldots,$$ and each pair crosses from left to right; hence stability holds before the first boundary and never returns afterwards. At $a=b>0$ no finite-delay imaginary root occurs, although the spectral gap closes in the limit $\tau\to\infty$. At $\tau=0$ one has $x'=-(a+b)x$; at $b=0$ the delay term is absent; and at $a=b=0$ histories become constant after one delay. The root-count continuation used here is the standard retarded-semigroup argument of Hale and Verduyn Lunel; the finite sentinel grid is not used to prove this all-delay assertion.

# Evidence and independent checks

The receipt contains twelve exact rational parameter cases, thirteen quarter time points per case, and three symbolic Hopf controls. The producer writes only canonical rational strings. A separate checker reconstructs all 156 method-of-steps cells, enforces recursive key closure and locks every scope field. A SymPy program independently verifies the Lambert substitution, $\Delta'$ criterion, the Gamma/Laplace term and the Hopf modulus. Clean replay is byte-identical; 24 repaired-hash mutations (including two unknown-key attacks) and one stale-hash mutation are rejected.

# Route-A boundary

The model has no intrinsic rational-prime carrier and no isolated primitive orbit ledger. Its exact $\Delta$ is a characteristic function, not a Fredholm determinant or target divisor. No global target analytic structure, same-clock self-adjoint lift, Euler factor, root number, automorphy object or Hilbert--Pólya operator is claimed. Thus the evaluator record is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},
\qquad \texttt{ROUTE\_A\_REJECTED},$$ with Route B false and scope literal `NO_BAD_EULER_OR_ROOT_NUMBER`. The internal source theorem is the contribution; the finite ledger is only a reproducibility sentinel.

1 J. K. Hale and S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Applied Mathematical Sciences 99, Springer, 1993, [doi:10.1007/978-1-4612-4342-7](https://doi.org/10.1007/978-1-4612-4342-7).
