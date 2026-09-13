---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-impedance-string-empty-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_impedance_string_empty_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_impedance_string_empty_spectrum_route_a/paper/main.pdf"
source_sha256: "1d220385a00e2d3571ae3d95b436caeacf0a4b24db394bd925fcc3c638b80da7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Impedance String in Physical Time: Complete Spectrum and Transparent Extinction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_impedance_string_empty_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_impedance_string_empty_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_impedance_string_empty_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_impedance_string_empty_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We reconstruct the full energy-space dynamics of a homogeneous string with one fixed endpoint and one finite nonnegative impedance. A unitary characteristic unfolding preserves physical time and transforms the wave generator into a derivative with one scalar boundary condition. For every nonzero signed round-trip coefficient, the entire spectrum is a simple bilateral arithmetic ladder with a complete Riesz basis. The semigroup norm is an exact staircase, including all round-trip endpoints. At transparent impedance the generator spectrum is empty, yet the semigroup has norm one until precisely twice the length divided by the wave speed; after that time it vanishes. An explicit all-plane resolvent verifies that empty spectrum is an operator theorem, not a failed eigenvalue search. Reciprocal positive impedances give the same norm and different spectral ladders. The classical absorbing-wave mechanism retains its literature ownership. This draft closes the domain, clock, complete spectrum and all-time law, while a finite exact and high-precision ledger audits their constants. We give an exact transparent resolvent analysis for the homogeneous impedance string, retaining its complete energy-space domain and physical clock. The generator has empty spectrum at perfect absorption, although its semigroup remains norm one up to the sharp round-trip extinction time. The resolvent norm is reduced to the lowest eigenvalue of a separated Sturm--Liouville problem with a parameter-dependent Robin condition. Positive interior eigenfunctions select the correct trigonometric, critical and hyperbolic branches without relying on sampled singular values. The resulting norm decreases strictly with the real part of the spectral parameter, so every transparent pseudospectrum is an exactly specified left half-plane. At zero spectral parameter its norm is twice the round-trip time divided by pi. Independent Green-kernel, Rayleigh quotient and complex gauge integrals test the formulas. These finite checks do not replace the infinite-dimensional proof, and no new ownership of the classical absorbing-wave spectral mechanism is asserted. We assemble a domain-complete theorem for a finite homogeneous string with a fixed endpoint and a nonnegative finite impedance at the other endpoint. Exact unitary unfolding gives the complete nontransparent spectrum, a Riesz basis and the physical-time semigroup norm. At transparency the spectrum is empty, but the evolution remains norm one until the sharp round-trip extinction time. A separated singular-value problem gives every transparent pseudospectrum through a three-branch scalar formula. We then distinguish compact resolvent from trace-class resolvent: the transparent inverse has half-integer singular values, is Hilbert--Schmidt but not trace class, and is quasinilpotent. Its explicitly named order-two regularized determinant is identically one. Before extinction the semigroup is noncompact, so it has no ordinary trace. Reciprocal impedances further separate decay norm from spectral location. The classical formulas are attributed; independent exact and numerical lanes, strict typed gates and repaired-hash attacks delimit the package's reproducible contribution. No target arithmetic or target self-adjoint operator is inferred from the native wave generator.
author:
- 'HCS-C396 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  An Impedance String in Physical Time:\
  Complete Spectrum and Transparent Extinction
- |
  An Impedance String in Physical Time:\
  Empty Spectrum and Exact Transparent Pseudospectra
- |
  An Impedance String in Physical Time:\
  Empty Spectrum, Exact Pseudospectra and Determinant Boundaries
```

## Markdown 正文

=2em

**Keywords:** impedance string; physical-time semigroup; empty spectrum; exact pseudospectrum; Volterra resolvent; determinant boundary.

# One source, three different spectral questions

Perfect absorption separates three quantities that are often conflated: the spectrum of an unbounded generator, the norm of its evolution, and the norm of its resolvent. Our source is the homogeneous wave equation $$u_{tt}=c^2u_{xx},\quad 0<x<L,\qquad
 u(0,t)=0,\quad u_x(L,t)+(\eta/c)u_t(L,t)=0,
 \label{eq:pde}$$ where $L,c>0$ and $0\leq\eta<\infty$. The time in this equation is never replaced by a spectral or target-dependent clock. Define $$\ell=L/c,\qquad \tau=2L/c,\qquad q=(\eta-1)/(\eta+1)\in[-1,1).
 \label{eq:q}$$ The signed coefficient $q$ includes the reflection at the fixed endpoint; it is the negative of the right-end reflection coefficient alone.

Driscoll and Trefethen [@driscoll1996] established the classical absorbing-wave mechanism, the exact decay staircase and the empty-spectrum transparent case. Their Theorem 1 gives resolvent bounds and invariances. We retain that ownership. The package contribution is a self-contained domain-and-clock reconstruction joined to independently executable evidence and explicit operator-category limitations, not a claim of literature priority. The source theorem is substantially different from free-wave observability: there is no boundary control input, observation inequality or control cost.

# The physical domain and its unitary unfolding

Put $v=u_t$ and $p=cu_x$. On the complex Hilbert space $$\mathcal H=\{u\in H^1(0,L):u(0)=0\}\times L^2(0,L),\qquad
 \|(u,v)\|_E^2=\int_0^L(|p|^2+|v|^2)\,\mathrm dx,$$ the generator is $G_\eta(u,v)=(v,c^2u_{xx})$. Its domain consists exactly of $u\in H^2$, $v\in H^1$, with $u(0)=v(0)=0$ and the right boundary in [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"}. Physical energy is one half of the squared norm.

The following map is unitary from $\mathcal H$ to $L^2(0,\tau)$: $$U(u,v)(s)=\sqrt{c/2}
 \begin{cases}
 (p-v)(L-cs),&0<s<\ell,\\
 (p+v)(c(s-\ell)),&\ell<s<\tau.
 \end{cases}
 \label{eq:unfold}$$ It sends the entire physical generator, including its domain, to $$A_qw=w',\qquad \mathop{\mathrm{Dom}}(A_q)=\{w\in H^1(0,\tau):w(\tau)=qw(0)\}.
 \label{eq:domain}$$

The two changes of variables in [\[eq:unfold\]](#eq:unfold){reference-type="eqref" reference="eq:unfold"}, and $|p-v|^2+|p+v|^2=2(|p|^2+|v|^2)$, prove the isometry. For arbitrary $w$, the inverse is $$\begin{aligned}
 p(x)&=\frac{w(\ell+x/c)+w(\ell-x/c)}{\sqrt{2c}},&
 v(x)&=\frac{w(\ell+x/c)-w(\ell-x/c)}{\sqrt{2c}},\\
 u(x)&=c^{-1}\int_0^x p(y)\,\mathrm dy.&&\end{aligned}$$ This lies in $\mathcal H$. For domain vectors the two midpoint traces agree because $v(0)=0$. At the outer endpoints, $p(L)=-\eta v(L)$ gives $w(\tau)=qw(0)$, without division by $q$. Conversely those trace relations recover the physical boundaries and Sobolev regularity. Differentiation on each half proves $UG_\eta U^{-1}=A_q$.

In particular the dissipativity identity retains the physical constant: $$\mathop{\mathrm{Re}}\langle A_qw,w\rangle
 =\tfrac12(q^2-1)|w(0)|^2=-c\eta|v(L)|^2.$$

# The complete evolution and spectrum

For $t\geq0$, set $k=\lfloor(s+t)/\tau\rfloor$ for almost every $s\in(0,\tau)$. The strongly continuous semigroup and its exact norm are $$S_q(t)w(s)=q^kw(s+t-k\tau),\qquad
 \|S_q(t)\|=|q|^{\lfloor t/\tau\rfloor}.
 \label{eq:semigroup}$$ At $q=0$, the coefficient means one for $k=0$ and zero for $k\geq1$. If $q\ne0$, the entire spectrum is algebraically simple: $$\lambda_n=\frac{\log|q|+\mathrm i(\arg q+2\pi n)}{\tau},\qquad n\in\mathbb Z.
 \label{eq:spectrum}$$ The functions $\tau^{-1/2}\mathrm e^{\lambda_ns}$ form a complete Riesz basis. If $q=0$, the spectrum is empty and the sharp extinction time is $\tau$.

Characteristics give [\[eq:semigroup\]](#eq:semigroup){reference-type="eqref" reference="eq:semigroup"}. Floor addition proves the semigroup law; translation continuity on a dense set, followed by the contraction estimate, proves strong continuity. For $t=n\tau+a$ with $0\leq a<\tau$, the two translated input intervals have disjoint supports and weights $q^n,q^{n+1}$. The first has positive length $\tau-a$. Integration proves the norm bound, and data supported on that first input interval attain it. This includes the exact endpoints $t=n\tau$.

Solving $zw-w'=f$ gives the kernel $$R(z,A_q)(s,r)=\mathrm e^{z(s-r)}
 \left[\frac{\mathrm e^{z\tau}}{\mathrm e^{z\tau}-q}-{\bf1}_{r<s}\right],
 \qquad \mathrm e^{z\tau}\ne q.
 \label{eq:green}$$ It is a bounded kernel mapping into [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"}; direct substitution verifies both inverse identities. At each excluded point the exponential is an eigenvector, so no residual or continuous spectral points are omitted. For $\alpha=(\log|q|+\mathrm i\arg q)/\tau$, multiplication by $\mathrm e^{\alpha s}$ conjugates the periodic derivative plus $\alpha$ to $A_q$. The Fourier basis then proves the Riesz and algebraic-simplicity statements. At $q=0$, [\[eq:green\]](#eq:green){reference-type="eqref" reference="eq:green"} exists everywhere and reduces to $$R(z,A_0)f(s)=\int_s^\tau\mathrm e^{z(s-r)}f(r)\,\mathrm dr,
 \qquad z\in\mathbb C.
 \label{eq:volterra}$$ Its locally uniform exponential series is operator-norm entire. Equation [\[eq:semigroup\]](#eq:semigroup){reference-type="eqref" reference="eq:semigroup"} is norm one for $t<\tau$ and zero for $t\geq\tau$, proving sharp extinction independently of spectral language.

The condition number of the specified multiplication similarity is $1/|q|$, not an asserted optimal condition number among all possible bases. For $q=-1$ the group is unitary. Compact resolvent and empty spectrum are compatible for an unbounded non-self-adjoint generator; the nonempty-spectrum theorem for bounded complex operators does not apply to $A_0$.

   $\eta$    $q$     $\|S_q(n\tau)\|$, $n\geq1$   Imaginary spectral ladder
  -------- -------- ---------------------------- ---------------------------
    $0$      $-1$               $1$                   $(2n+1)\pi/\tau$
   $1/2$    $-1/3$            $3^{-n}$                $(2n+1)\pi/\tau$
    $1$      $0$                $0$                  No spectral points
    $2$     $1/3$             $3^{-n}$                  $2n\pi/\tau$

  : Exact parameter controls. Equal decay norms do not determine the spectral ladder. The ladder index ranges over all integers, independently of the positive time-step index in the norm column.

\>0

# Exact transparent pseudospectra

Write $z=x+\mathrm iy$. Multiplication by $\mathrm e^{\mathrm iys}$ is unitary and conjugates $R(x,A_0)$ to $R(z,A_0)$. Thus the resolvent norm is a function $\rho_\tau(x)$ of the real part alone. Empty spectrum does not make that function vanish or remain small.

For $x\tau>-1$, let $\theta\in(0,\pi)$ be the unique solution of $x\tau=-\theta\cot\theta$. For $x\tau<-1$, let $h>0$ be the unique solution of $x\tau=-h\coth h$. Then $$\rho_\tau(x)=
 \begin{cases}
 \tau\sin\theta/\theta,&x\tau>-1,\\
 \tau,&x\tau=-1,\\
 \tau\sinh h/h,&x\tau<-1.
 \end{cases}
 \label{eq:norm}$$ It is continuous and strictly decreasing from infinity to zero. With the strict convention $\|R\|>\varepsilon^{-1}$, every pseudospectrum is $$\sigma_\varepsilon(A_0)=\{z\in\mathbb C:\mathop{\mathrm{Re}}z<a_\varepsilon\},\qquad
 \rho_\tau(a_\varepsilon)=\varepsilon^{-1}.$$

The reciprocal squared norm is the infimum of $\|xu-u'\|^2/\|u\|^2$ over nonzero $u\in H^1$ with $u(\tau)=0$. Expansion of the numerator gives $$\int_0^\tau(|u'|^2+x^2|u|^2)\,\mathrm ds+x|u(0)|^2.$$ Compact interval embedding gives a minimizer, and variation gives $$-u''+x^2u=\mu u,\qquad u(\tau)=0,\quad u'(0)=xu(0).
 \label{eq:sl}$$ The positive functions $\sin(\theta(1-s/\tau))$, $\tau-s$ and $\sinh(h(1-s/\tau))$ solve the three regimes. Their eigenvalues are respectively $\theta^2/(\tau^2\sin^2\theta)$, $1/\tau^2$ and $h^2/(\tau^2\sinh^2h)$.

These are the lowest roots, not arbitrary solutions of the scalar boundary equation. A minimizing eigenfunction can be taken nonnegative. ODE uniqueness makes it strictly positive in the interior; orthogonality excludes a distinct eigenvalue with another positive eigenfunction. Uniqueness of the branch parameters follows from the positive derivatives of $-\theta\cot\theta$ and $h\coth h$. Finally, $\sin\theta/\theta$ strictly decreases and $\sinh h/h$ strictly increases. Their limits at zero are one. Together with the endpoint limits of the parameter equations, this proves strict monotonicity, continuity and the entire half-plane assertion.

In particular $\rho_\tau(0)=2\tau/\pi$. The critical branch point is $x=-1/\tau$, not zero; at that point the norm equals $\tau$. The theorem is restricted to the transparent face. It does not assert the same half-plane shape for a nonzero reflection coefficient.

\>1

# Operator ideals and the determinant boundary

For every $z\in\mathbb C$, the transparent resolvent is Hilbert--Schmidt but not trace class, is quasinilpotent, and satisfies $$\det{}_2(I-wR(z,A_0))=1,\qquad w\in\mathbb C.
 \label{eq:det2}$$ The semigroup is noncompact for $0\leq t<\tau$ and zero thereafter. For $q\ne0$ it is noncompact at every time.

At $x=0$ the complete separated problem [\[eq:sl\]](#eq:sl){reference-type="eqref" reference="eq:sl"} gives $$s_n(R(0,A_0))=\frac{\tau}{\pi(n+1/2)},\qquad n=0,1,2,\ldots.
 \label{eq:singular}$$ The associated half-integer Fourier bases are complete by reflection. The singular values are square summable and not summable. For general $z$, $R(z,A_0)=M_zR(0,A_0)M_z^{-1}$, where $M_z$ is bounded invertible multiplication by $\mathrm e^{zs}$. The two-sided ideal property preserves membership, not individual singular values. Direct integration gives $$\|R(x+\mathrm iy,A_0)\|_{\rm HS}^2=
 \begin{cases}
 \displaystyle\frac{\tau}{2x}-\frac{1-\mathrm e^{-2x\tau}}{4x^2},&x\ne0,\\
 \tau^2/2,&x=0.
 \end{cases}$$ The $n$th power of the Volterra inverse has kernel $\mathrm e^{z(s-r)}(r-s)^{n-1}/(n-1)!$ for $r>s$. Young's inequality implies $\|R(z,A_0)^n\|\leq\mathrm e^{|x|\tau}\tau^n/n!$, hence spectral radius zero. The order-two determinant is explicitly the canonical product $\prod_j(1-w\lambda_j)\mathrm e^{w\lambda_j}$ over nonzero compact-operator eigenvalues with algebraic multiplicity. There are no such eigenvalues here, so that product is one.

For $t<\tau$, the evolution is isometric on inputs supported on $(t,\tau)$. An orthonormal sequence on that infinite-dimensional subspace has no convergent image subsequence, proving noncompactness. For $q\ne0$, the wrapped translation has a bounded inverse at every fixed time; compactness would make the identity compact on an infinite-dimensional space.

Thus there is no ordinary trace of the semigroup before transparent extinction and no ordinary trace-class Fredholm determinant of its transparent resolvent. After extinction the semigroup is zero and has trace zero. The scalar characteristic $1-q\mathrm e^{-z\tau}$ records the nontransparent spectral equation but is not thereby an ordinary operator determinant. Equation [\[eq:det2\]](#eq:det2){reference-type="eqref" reference="eq:det2"} names its regularization; it does not forbid all other regularized constructions.

#### Parameter and reversal controls.

For positive impedance, $q(1/\eta)=-q(\eta)$. This preserves the norm and shifts the spectral ladder by $\mathrm i\pi/\tau$ modulo $2\pi\mathrm i/\tau$. As $\eta\to1$, the real parts of every nontransparent eigenvalue tend to minus infinity, while the similarity condition number diverges. Nevertheless the norm stays one at every fixed $t<\tau$. The physical reversal $(u,v)\mapsto(u,-v)$ maps the impedance domain for $\eta$ to that for $-\eta$, and therefore does not preserve positive damping. The conservative endpoint $\eta=0$ has the usual physical time reversal. These statements concern the physical involution, not arbitrary abstract antiunitaries.

# Executable evidence and scope

The canonical ledger uses seven impedances, three round-trip times and seven time ratios. Four spatial ratios give 588 exact transport rows; seven boundary rows check the reflection sign and dissipation. A separate checker uses repeated boundary crossings instead of the producer's floor formula. It checks 126 finite spectral rows by the exponential boundary equation, and 21 Green rows by direct kernel integration instead of the producer's polynomial inhomogeneous solution. \>0 The 27 transparent norm rows include all three regimes and the zero-real-part case. A separate 100-digit lane evaluates 27 Rayleigh quotients, 81 Volterra action checks and 81 complex-gauge action checks. Eleven symbolic identities check the characteristic, boundary and differential relations. Finite regression of 12 half-integer singular modes supports the normalization; the complete sequence follows from the Fourier argument. The stored decimal values have 60 significant digits from 100-digit arithmetic. They are not interval certificates. Canonical reproduction, two-directory replay and repaired-hash mutations test the artifact contract; they cannot establish the all-time and full-spectrum theorem by enumeration. Unknown fields and Boolean--integer substitutions are rejected by typed checks. The frozen evaluation is parsed strictly and locked before a release-write operation. Compiler logs, font checks and PDF hashes are separate engineering evidence, not mathematical novelty.

The conservative Route-A tuple is four failures followed by a formal operator hint; overall the candidate is rejected for the target route. The native generator supplies no rational-prime carrier, arithmetic primitive correspondence, target divisor, target functional equation or Hilbert--Pólya identification. No Euler factors, root number, automorphy or target local data are claimed. Route B remains disabled.

`NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Literature and review boundaries.

The author's website PDF initially failed to download. Retrieval from the same author's GitHub repository succeeded, and the relevant extracted text was read. The optional structural preflight was unavailable because its PDF-parser dependency was absent; no certified local-page-anchor claim is made. Equations (14)--(19), (25) and Theorem 1 of [@driscoll1996] support the ownership statement. The three-branch norm is established in the separate complete proof package; it is not attributed to a formula absent from the cited theorem. The precise three-branch norm is derived above rather than attributed to a formula not present in that theorem. An internal team agent independently checked the complete analytic proof. The authoring agent supplied the implementation and manuscript. This is AI-assisted internal review, not external peer review or venue acceptance. Variable coefficients, internal damping and infinite impedance are outside the frozen theorem. They would require new domains and proofs.

# Conclusion

**Round zero: the physical domain and complete spectrum.** The same exact unfolding determines all spectral points and all evolution times. At transparency the generator has no spectrum, yet the norm remains one until the sharp physical round-trip time. **Round one: transparent resolvent and exact pseudospectra.** The lowest separated eigenfunction selects three explicit resolvent-norm branches. Their strict monotonicity gives every transparent pseudospectrum, with no reliance on a finite matrix's apparent eigenvalues. **Round two: operator ideals and the determinant boundary.** Finite extinction, empty spectrum and an entire resolvent coexist in a single natural PDE source. Its resolvent is compact but not trace class, and its explicitly regularized determinant is trivial. These distinctions close the source theorem while leaving the target arithmetic route rejected.

1 T. A. Driscoll and L. N. Trefethen, Pseudospectra for the wave equation with an absorbing boundary, *Journal of Computational and Applied Mathematics* **69** (1996), 125--142. [doi:10.1016/0377-0427(95)00021-6](https://doi.org/10.1016/0377-0427(95)00021-6).
