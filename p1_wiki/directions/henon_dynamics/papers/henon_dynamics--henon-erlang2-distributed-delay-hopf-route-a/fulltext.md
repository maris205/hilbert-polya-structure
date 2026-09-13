---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-erlang2-distributed-delay-hopf-route-a"
canonical_tex: "henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a/paper/main.pdf"
source_sha256: "6752439941e1afcc07b94ebda6a8f95316fa93c6b99ecd5d845c4be398da95fa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Stability, Crossing, and Jordan Atlas for Erlang--2 Distributed-Delay Feedback

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_erlang2_distributed_delay_hopf_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve a scalar negative-feedback equation with a normalized Erlang shape-two memory kernel. Compatible histories admit an exact three-dimensional linear-chain realization, whose cubic Routh determinant gives a necessary-and-sufficient stability threshold and a transverse imaginary crossing. \>0 We further exhaust every repeated-root surface, determine all Jordan sizes, count unstable roots, and give closed semigroup formulas on simple, double, and triple-root faces. \>1 Zero damping and feedback, the triple-root point, the excluded zero-rate kernel, the fast-memory limit, source ownership, collision boundaries, and the rejected Route-A decision are closed explicitly. No nonlinear periodic branch is claimed.
author:
- 'Route-A source-local certificate HCS-C343'
date: 3 September 2026
title: |
  An Exact Stability, Crossing, and Jordan Atlas\
  for Erlang--2 Distributed-Delay Feedback
```

## Markdown 正文

trailerid \[\<C3432026090300000000000000000000\>\<C3432026090300000000000000000000\>\]

# Frozen memory owner

Fix $$a,b\geq0,\qquad r>0,\qquad
 K_r(s)=r^2s\mathrm e^{-rs}\quad(s\geq0),$$ and consider $$\label{eq:delay}
 \dot x(t)=-a x(t)-b\int_0^\infty K_r(s)x(t-s)\,ds .$$ The kernel is normalized; it has mean $2/r$, variance $2/r^2$, and Laplace transform $r^2/(\lambda+r)^2$. A compatible fading-memory history is one for which the following integrals exist and permit the standard differentiation under the integral: $$z_1(t)=\int_0^\infty r\mathrm e^{-rs}x(t-s)\,ds,\qquad
 z_2(t)=\int_0^\infty K_r(s)x(t-s)\,ds.$$

[\[lem:chain\]]{#lem:chain label="lem:chain"} For compatible initialization, equation [\[eq:delay\]](#eq:delay){reference-type="eqref" reference="eq:delay"} is equivalent to $$\label{eq:chain}
 \dot x=-ax-bz_2,\qquad
 \dot z_1=r(x-z_1),\qquad
 \dot z_2=r(z_1-z_2).$$ It is not asserted that arbitrary values of $(z_1,z_2)$ encode a prescribed prehistory.

Integration by parts gives the two filter equations in [\[eq:chain\]](#eq:chain){reference-type="eqref" reference="eq:chain"}; the first equation is [\[eq:delay\]](#eq:delay){reference-type="eqref" reference="eq:delay"}. Conversely, subtract the displayed convolutions from a solution of the two stable filter equations. The differences solve homogeneous first-order equations and vanish initially, so they vanish for all later times. Thus compatible chain solutions recover the delay equation exactly.

Put $X=(x,z_1,z_2)^{\mathsf T}$. Then $\dot X=\mathsf MX$, where $$\mathsf M=\begin{pmatrix}-a&0&-b\\ r&-r&0\\0&r&-r\end{pmatrix},$$ and direct expansion gives $$\begin{aligned}
 p(\lambda)&=\det(\lambda I-\mathsf M)
 =(\lambda+a)(\lambda+r)^2+br^2 \label{eq:poly}\\
 &=\lambda^3+c_2\lambda^2+c_1\lambda+c_0,\nonumber\\
 c_2&=a+2r,\qquad c_1=r(r+2a),\qquad c_0=r^2(a+b).\nonumber\end{aligned}$$

[\[thm:routh\]]{#thm:routh label="thm:routh"} For $b>0$, the zero solution is exponentially stable if and only if $$\label{eq:bh}
 0<b<b_H,\qquad b_H=\frac{2(a+r)^2}{r}.$$ At $b=b_H$, $$\label{eq:hopf-factor}
 p(\lambda)=(\lambda+a+2r)
 (\lambda^2+r(r+2a)),$$ so the roots are $-a-2r$ and $\lambda_\pm=\pm\mathrm i\omega_H$, with $\omega_H=\sqrt{r(r+2a)}$. The conjugate pair is simple and crosses from left to right: $$\label{eq:crossing}
 \operatorname{Re}\lambda_+'(b_H)
 =\frac{r^2}{2\{r(r+2a)+(a+2r)^2\}}>0.$$ For $b>b_H$, exactly two roots lie in the open right half-plane.

For $b>0$, all $c_j$ are positive. The remaining cubic Routh--Hurwitz minor is $$c_2c_1-c_0=r\{2(a+r)^2-br\}.$$ This proves the equivalence in [\[eq:bh\]](#eq:bh){reference-type="eqref" reference="eq:bh"}. At equality, multiplication verifies [\[eq:hopf-factor\]](#eq:hopf-factor){reference-type="eqref" reference="eq:hopf-factor"}. Implicit differentiation of $p(\lambda,b)=0$ at $\lambda=\mathrm i\omega_H$ yields [\[eq:crossing\]](#eq:crossing){reference-type="eqref" reference="eq:crossing"}. Above the threshold the first Routh column has signs $+,+,-,+$, hence two sign changes and exactly two open-right-half-plane roots.

The phrase *chain equivalence owner* records the first manuscript round: this is an all-parameter analytic theorem, not stability inferred from sampled roots.

\>0

# Complete degeneracy and propagator atlas

[\[thm:jordan\]]{#thm:jordan label="thm:jordan"} In the domain $a,b\geq0$, $r>0$, all repeated-root cases are precisely:

1.  $b=0$. The root $-r$ has one size-two Jordan block when $a\ne r$, and at $a=r$ the root $-r$ has one size-three block.

2.  $0\leq a<r$ and $$\label{eq:bd}
     b=b_D=\frac{4(r-a)^3}{27r^2}>0.$$ Here $$p(\lambda)=(\lambda-\mu)^2(\lambda-\nu),\qquad
     \mu=-\frac{r+2a}{3},\quad \nu=-\frac{4r-a}{3},$$ and the Jordan sizes are two and one.

The positive-$b$ defective face lies strictly inside the stable region.

Differentiating [\[eq:poly\]](#eq:poly){reference-type="eqref" reference="eq:poly"} and taking the discriminant gives $$\label{eq:disc}
 p'(\lambda)=(\lambda+r)(3\lambda+r+2a),\qquad
 \operatorname{disc}p=br^2\{4(r-a)^3-27br^2\}.$$ The first critical root belongs to $p$ exactly when $b=0$. The second belongs to $p$ exactly on [\[eq:bd\]](#eq:bd){reference-type="eqref" reference="eq:bd"}; it has positive $b$ precisely when $a<r$. These observations exhaust [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}, and substitution gives the factorization. Moreover, $$\det[e_1,\mathsf Me_1,\mathsf M^2e_1]=r^3\ne0.$$ Thus $\mathsf M$ is cyclic and its minimal polynomial equals $p$: each repeated root has one Jordan block of its algebraic multiplicity. Finally $$\frac{b_D}{b_H}
 =\frac{2(r-a)^3}{27r(a+r)^2}<1,$$ so the positive defective face is stable.

For distinct roots $\lambda_1,\lambda_2,\lambda_3$, Lagrange interpolation modulo $p$ gives $$\label{eq:simple-flow}
 \mathrm e^{t\mathsf M}=\sum_{j=1}^3\mathrm e^{t\lambda_j}
 \prod_{k\ne j}\frac{\mathsf M-\lambda_kI}{\lambda_j-\lambda_k}.$$ On a double face, write $p=(\lambda-\mu)^2(\lambda-\nu)$ and set $$P_\nu=\frac{(\mathsf M-\mu I)^2}{(\nu-\mu)^2},\qquad
 P_\mu=I-P_\nu,\qquad N_\mu=(\mathsf M-\mu I)P_\mu.$$ Hermite interpolation yields $$\label{eq:double-flow}
 \mathrm e^{t\mathsf M}=\mathrm e^{\mu t}(P_\mu+tN_\mu)+\mathrm e^{\nu t}P_\nu,
 \qquad N_\mu^2=0.$$ At $a=r,b=0$, $N=\mathsf M+rI$ satisfies $N^3=0$ and $$\label{eq:triple-flow}
 \mathrm e^{t\mathsf M}=\mathrm e^{-rt}(I+tN+t^2N^2/2).$$ Equations [\[eq:simple-flow\]](#eq:simple-flow){reference-type="eqref" reference="eq:simple-flow"}--[\[eq:triple-flow\]](#eq:triple-flow){reference-type="eqref" reference="eq:triple-flow"} close the flow on every spectral stratum.

The phrase *Routh Hopf atlas owner* marks the substantive first revision: transversality, unstable-root count, discriminant exhaustion, Jordan sizes, and defective semigroups have all been added.

\>1

# Boundaries and claim discipline

At $b=0$, $p=(\lambda+a)(\lambda+r)^2$. Hence $a>0$ is exponentially stable despite the defective $-r$ block. At $a=b=0$, the simple zero root is a constant $x$-mode and the memory transient contains $t\mathrm e^{-rt}$. For $a=0,b>0$, Theorem [\[thm:routh\]](#thm:routh){reference-type="ref" reference="thm:routh"} specializes to stability for $0<b<2r$, an imaginary pair at $b=2r$, and two right-half-plane roots above it. The point $a=r,b=0$ is the triple block in [\[eq:triple-flow\]](#eq:triple-flow){reference-type="eqref" reference="eq:triple-flow"}.

The value $r=0$ is excluded: the displayed expression ceases to be a normalized Erlang density. For fixed bounded $\lambda$, $r^2/(\lambda+r)^2\to1$ as $r\to\infty$, so the bounded slow root tends to $-(a+b)$ while two memory modes are fast. This limiting observation is not substituted for any finite-$r$ theorem.

Theorem [\[thm:routh\]](#thm:routh){reference-type="ref" reference="thm:routh"} proves a simple transverse imaginary *linear spectral crossing*. A nonlinear vector field, its nondegeneracy coefficient, and its center-manifold reduction have not been specified. Therefore neither existence nor stability of a nonlinear periodic branch is claimed.

# Evidence, sources, and collisions

The certificate carries six exact kernel rows, 120 rational Routh faces, 20 Hopf-factorization rows, and 30 repeated-root rows, totaling 2,017 audited scalar leaves. The independent checker, independent SymPy lane, two-directory byte replay, and repaired-hash hostile suite are executable receipts. Sampling does not prove the continuum theorem; the displayed Routh, discriminant, and cyclicity arguments do.

The Erlang linear-chain lineage is documented by Hurtado and Kirosingh [@Hurtado2019] and MacDonald [@MacDonald1978]; Boese supplies primary gamma-delay stability context [@Boese1989]. These records support provenance, not a priority claim for our formulas or assembly.

The nearest workspace owners are C210, a scalar *discrete* retarded delay with an infinite Lambert--$W$ root ladder; C218, a Kelvin--Voigt wave PDE; and C272, an Erlang age-transport renewal PDE. None owns this normalized distributed-memory scalar feedback, its finite Markov realization, and complete cubic Hopf/Jordan atlas. This is a workspace collision statement only.

# Route-A decision

The phrase *Jordan boundary and route firewall* marks the final revision. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ There is no arithmetic origin or prime-power clock; linear modes are not an arithmetic primitive-orbit ledger; no dynamical Euler product, target determinant, functional equation, Weil compression, natural target-zero quantization, target-zero match, or Hilbert--Polya operator is supplied. Route A is rejected and Route B remains locked. No target arithmetic local data, Euler factor, root number, automorphy, divisor, or functional equation is asserted.

#### AI use.

A generative language model assisted proof organization, code scaffolding, and manuscript drafting. The analytic derivation, independent checker, symbolic lane, hostile tests, and deterministic artifacts define the audit record.

\>1

9 P. J. Hurtado and A. S. Kirosingh, *Generalizations of the Linear Chain Trick: incorporating more flexible dwell time distributions into mean field ODE models*, *Journal of Mathematical Biology* 79 (2019), 1831--1883. DOI: [10.1007/s00285-019-01412-w](https://doi.org/10.1007/s00285-019-01412-w).

F. G. Boese, *The stability chart for the linearized Cushing equation with a discrete delay and with gamma-distributed delays*, *Journal of Mathematical Analysis and Applications* 140 (1989), 510--536. DOI: [10.1016/0022-247X(89)90081-4](https://doi.org/10.1016/0022-247X(89)90081-4).

N. MacDonald, *Time Lags in Biological Models*, Lecture Notes in Biomathematics 27, Springer, 1978. DOI: [10.1007/978-3-642-93107-9](https://doi.org/10.1007/978-3-642-93107-9).
