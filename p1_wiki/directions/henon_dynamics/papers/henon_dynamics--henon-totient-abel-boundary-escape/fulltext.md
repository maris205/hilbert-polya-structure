---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-totient-abel-boundary-escape"
canonical_tex: "henon_dynamics/henon_totient_abel_boundary_escape/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_totient_abel_boundary_escape/paper/paper.pdf"
source_sha256: "4c732b6e1bbbba4626baf37db1633a350b61736c17a6adc3cd5f8c71203c6ab1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Totient Abel Laws and Tagged-Mass Escape at a Hénon Packet Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_totient_abel_boundary_escape>)
- [规范 TeX](<../../../../../henon_dynamics/henon_totient_abel_boundary_escape/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_totient_abel_boundary_escape/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_totient_abel_boundary_escape/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_totient_abel_boundary_escape/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An Abel variable regularizes the all-orbit prime-ideal packet germ attached to a certified area-preserving Hénon survivor, but the ungraded boundary is already divergent on one exact primitive period-four orbit. We determine the first canonical boundary law on that orbit. Its positive multiplier is $L=289+24\sqrt{145}$ and its inversion-fixed cyclotomic packet has mass $b_n=\log\!\left(L^{-\varphi(n)/2}\Phi_n(L)\right)$. We prove the uniform formula $$b_n=\tfrac12\varphi(n)\log L+O_L(1),$$ with an explicit error below $0.001735$. Consequently $$\lim_{u\uparrow1}(1-u)^2\sum_{n\ge3}b_nu^n
  =\frac{3\log L}{\pi^2}.$$ After placing the normalized $n$th packet mass at $(-\log u)n$, the resulting probability measures converge to the $\Gamma(2,1)$ law. This positive scalar boundary has a sharp topological limit: the corresponding renormalized positive divisor vectors have no norm- or weakly-convergent subnet in the original source-tagged weighted $\ell^1$ space. Thus mass escapes along the cyclotomic grading, and the Gamma law is a blow-up compactification rather than a lossless divisor boundary. The result advances the analytic packet structure at one orbit; all-orbit pressure interchange, a von-Mangoldt trace, a Fredholm determinant and a Hilbert--Pólya operator remain open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Totient Abel Laws and Tagged-Mass Escape\
  at a Hénon Packet Boundary
```

## Markdown 正文

# Introduction

Periodic-orbit constructions motivated by the Hilbert--Pólya programme face two different analytic problems. The first is to assemble infinitely many source-native orbit packets without erasing their chronology or arithmetic provenance. The second is to understand what, if anything, survives on the boundary of the regularizing variables. The second problem cannot be solved by substituting a boundary value into a power series whose coefficients do not tend to zero.

The preceding HCS-P51 construction [@wangp51] addresses the first problem for a certified four-state survivor of the area-preserving Hénon map $$H_6(q,p)=(1-6q^2-p,q).$$ It defines an all-primitive-orbit, source-tagged, Banach-valued germ in an Abel grading $u$, and proves holomorphy for $|u|<1$ in an explicit pressure half-plane. On an exact primitive period-four orbit, however, the $u$-radius is exactly one and the raw value at $u=1$ diverges. The primitive-divisor context for the underlying Lehmer--Pierce sequence is consistent with Flatters' theorem [@flatters2009], but no primitive-divisor input is needed for the asymptotic boundary law proved here.

We keep the orbit, cyclotomic clock and reciprocal normalization frozen. If $D_n$ denotes the $n$th effective tagged packet divisor, its source-native mass is $$b_n=\|D_n\|_{\rm tag}.$$ Our first result identifies the precise average size of these masses. The reciprocal cyclotomic normalization turns $b_n$ into one half of $\varphi(n)\log L$, up to a uniformly bounded correction. The elementary summatory law for Euler's totient function---proved below rather than used as a hidden Tauberian assumption; see also [@apostol1976 Chapter 3] for background on arithmetic functions---then forces a second-order Abel boundary.

The second contribution resolves the topology of that boundary. A scalar mass functional has a nonzero limit, and the escaping grading has a canonical $\Gamma(2,1)$ blow-up profile. In contrast, the tagged divisor vectors themselves have no norm or weak limit. Each fixed source coordinate vanishes while total mass remains positive. This gives an exact example where an Abel scalarization is canonical but cannot be promoted to a lossless vector boundary or a determinant.

#### Main results.

For the exact multiplier $L=289+24\sqrt{145}$ we prove:

1.  the uniform packet formula $b_n=\varphi(n)\log L/2+\varepsilon_n$ with $|\varepsilon_n|\le C_L<0.001735$;

2.  the Abel law $(1-u)^2\sum_{n\ge3}b_nu^n\to3\log L/\pi^2$;

3.  weak convergence of the normalized mass at scale $(-\log u)n$ to the density $xe^{-x}\,\mathrm dx$;

4.  nonexistence of a norm- or weakly-convergent subnet for the renormalized positive vectors in the original tagged space.

#### Claim boundary.

Every theorem is fixed-orbit. We do not interchange the Abel limit with the all-orbit pressure sum of HCS-P51, identify rational primes with primitive orbits, construct a trace-class operator, count zeros, derive a functional equation, or claim a Hilbert--Pólya realization.

# The period-four packet and its totient main term

The source orbit has positive unstable multiplier $$L=289+24\sqrt{145}>1,
\qquad L+L^{-1}=578,
\qquad N_{\mathbb Q(\sqrt{145})/\mathbb Q}(L)=1.
\label{eq:L}$$ For $n\ge3$ define the inversion-fixed packet $$\beta_n=L^{-\varphi(n)/2}\Phi_n(L).
\label{eq:beta}$$ Cyclotomic reciprocity expresses [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"} as a polynomial in $T=L+L^{-1}=578$. In particular the orbit trace field is $\mathbb Q(T)=\mathbb Q$, so $\beta_n$ is an ordinary rational integer and the divisor below is genuinely a divisor over $\mathbb Q$. Pairing conjugate roots of $\Phi_n$ makes it positive. We use the effective source-tagged divisor $$D_n=\operatorname{Div}_{\mathbb Q}(\beta_n)
=\sum_p v_p(\beta_n)[\gamma_4,n,p].
\label{eq:Dn}$$ The weighted tagged space inherited from HCS-P51 assigns weight $\log p$ to the displayed basis atom. Hence $$b_n:=\|D_n\|_{\rm tag}=\log\beta_n.
\label{eq:mass}$$ The index $n$ is part of the tag, so different packets have disjoint support even when the same rational prime divides several packets.

For every $n\ge3$, $$b_n=\frac{\varphi(n)}2\log L+\varepsilon_n,
\qquad
\varepsilon_n=\sum_{d\mid n}\mu(n/d)\log(1-L^{-d}).
\label{eq:totientformula}$$ Moreover $$|\varepsilon_n|\le C_L:=\sum_{d\ge1}-\log(1-L^{-d})<0.001735.
\label{eq:CL}$$

Cyclotomic Möbius inversion gives $$\Phi_n(L)=\prod_{d\mid n}(L^d-1)^{\mu(n/d)}.$$ Writing $L^d-1=L^d(1-L^{-d})$ and using $\sum_{d\mid n}\mu(n/d)d=\varphi(n)$ proves [\[eq:totientformula\]](#eq:totientformula){reference-type="eqref" reference="eq:totientformula"}. Since $0<L^{-d}<1$, $$|\varepsilon_n|
\le\sum_{d\mid n}|\log(1-L^{-d})|
\le C_L.$$ The inequality $-\log(1-x)\le x/(1-x)$ bounds the tail geometrically. Evaluating the first 32 terms and this explicit tail gives [\[eq:CL\]](#eq:CL){reference-type="eqref" reference="eq:CL"}; the calculation is independently reproduced by the project checker.

In particular $b_n>0$ for all $n\ge3$. The correction is not merely lower order on average: it is uniformly bounded while the main term records the exact cyclotomic degree.

# The scalar Abel boundary

We first recall the required average in a form that fixes the error budget.

As $x\to\infty$, $$\sum_{n\le x}\varphi(n)
=\frac{3}{\pi^2}x^2+O(x\log(2x)).
\label{eq:phisum}$$

From $\varphi(n)=n\sum_{d\mid n}\mu(d)/d$, $$\sum_{n\le x}\varphi(n)
=\frac12\sum_{d\le x}\mu(d)
\left(\lfloor x/d\rfloor^2+\lfloor x/d\rfloor\right).$$ Replacing the floors costs $O(x\sum_{d\le x}d^{-1})$. Extending $\sum_{d\le x}\mu(d)d^{-2}$ to infinity costs $O(x)$ after multiplication by $x^2$, and the infinite sum is $1/\zeta(2)=6/\pi^2$.

Put $$Z(\tau)=\sum_{n\ge3}b_ne^{-\tau n},\qquad \tau>0.
\label{eq:Ztau}$$

As $\tau\downarrow0$, $$Z(\tau)=\frac{3\log L}{\pi^2\tau^2}
+O_L\!\left(\frac{\log(2/\tau)}{\tau}\right).
\label{eq:Zasymptotic}$$ Equivalently, $$\lim_{u\uparrow1}(1-u)^2\sum_{n\ge3}b_nu^n
=A_L:=\frac{3\log L}{\pi^2}
=1.9330777456585248\ldots .
\label{eq:Abel}$$

Stieltjes summation applied to [\[eq:phisum\]](#eq:phisum){reference-type="eqref" reference="eq:phisum"} yields $$\sum_{n\ge1}\varphi(n)e^{-\tau n}
=\frac{6}{\pi^2\tau^2}
+O\!\left(\frac{\log(2/\tau)}{\tau}\right).$$ Insert [\[eq:totientformula\]](#eq:totientformula){reference-type="eqref" reference="eq:totientformula"}. The bounded correction contributes at most $C_L\sum_{n\ge3}e^{-\tau n}=O_L(\tau^{-1})$, proving [\[eq:Zasymptotic\]](#eq:Zasymptotic){reference-type="eqref" reference="eq:Zasymptotic"}. Set $u=e^{-\tau}$ and use $(1-e^{-\tau})/\tau\to1$ for [\[eq:Abel\]](#eq:Abel){reference-type="eqref" reference="eq:Abel"}.

The normalization is rigid. The reciprocal packet contributes $\varphi(n)\log L/2$, so omitting the factor $1/2$ doubles the false target. The average order of $\varphi(n)$ is linear, so the boundary pole has order two rather than one.

# Blowing up the escaping grading

The scalar asymptotic determines where the mass lives. Define a probability measure on $[0,\infty)$ by $$\mu_\tau=\frac1{Z(\tau)}
\sum_{n\ge3}b_ne^{-\tau n}\delta_{\tau n}.
\label{eq:mutau}$$

As $\tau\downarrow0$, $$\mu_\tau\Longrightarrow \Gamma(2,1),
\label{eq:gamma}$$ where the limiting probability measure has density $xe^{-x}\mathbf1_{x\ge0}\,\mathrm dx$.

For $s\ge0$, the Laplace transform of [\[eq:mutau\]](#eq:mutau){reference-type="eqref" reference="eq:mutau"} is exactly $$\int_0^\infty e^{-sx}\,\mathrm d\mu_\tau(x)
=\frac{Z((1+s)\tau)}{Z(\tau)}.
\label{eq:laplace}$$ Theorem 3.2 makes [\[eq:laplace\]](#eq:laplace){reference-type="eqref" reference="eq:laplace"} tend to $(1+s)^{-2}$, the Laplace transform of the stated Gamma distribution.

For completeness, tightness follows directly from the packet bound. There is a constant $C$ with $b_n\le C(n+1)$. Therefore the mass of $\{x\ge R\}$ in [\[eq:mutau\]](#eq:mutau){reference-type="eqref" reference="eq:mutau"} is, uniformly for sufficiently small $\tau$, at most a constant multiple of $$\tau^2\sum_{n\ge R/\tau}(n+1)e^{-\tau n}
\ll(R+1)e^{-R}.$$ Every subsequential limit has the transform $(1+s)^{-2}$; uniqueness of Laplace transforms completes the proof.

The profile is a boundary compactification of the cyclotomic index. It does not identify the rational-prime factors inside each packet. Its shape two is the probabilistic image of the totient's linear average order: replacing it by an exponential, whose transform is $(1+s)^{-1}$, fails the exact ratio [\[eq:laplace\]](#eq:laplace){reference-type="eqref" reference="eq:laplace"}.

# Why the tagged divisor vector has no boundary

The positive scalar law might suggest that the renormalized divisor series converges in the original HCS-P51 Banach space. The source tags rule this out. Define $$E_\tau=\tau^2\sum_{n\ge3}e^{-\tau n}D_n\in\mathcal B_{\mathrm{tag}}.
\label{eq:Etau}$$ Because all coefficients are positive and different $n$-packets have disjoint support, $$\|E_\tau\|_{\rm tag}=\tau^2Z(\tau)\longrightarrow A_L>0.
\label{eq:Enorm}$$

The family $(E_\tau)_{\tau>0}$ has neither a norm-convergent subnet nor a weakly convergent subnet in $\mathcal B_{\mathrm{tag}}$ as $\tau\downarrow0$.

Fix a source coordinate $(\gamma_4,n,p)$. Its coefficient in [\[eq:Etau\]](#eq:Etau){reference-type="eqref" reference="eq:Etau"} is $$\tau^2e^{-\tau n}v_p(\beta_n)\longrightarrow0.$$ Thus every coordinate of any norm limit would vanish. The only possible norm limit is zero, contradicting [\[eq:Enorm\]](#eq:Enorm){reference-type="eqref" reference="eq:Enorm"}.

The same coordinate functionals force any weak limit to be zero. However, the positive mass functional $$\mathfrak m\!\left(\sum c_{n,p}[\gamma_4,n,p]\right)
=\sum c_{n,p}\log p$$ is bounded with norm one and satisfies $\mathfrak m(E_\tau)=\|E_\tau\|_{\rm tag}\to A_L$. Hence weak convergence is also impossible. Both contradictions apply to arbitrary subnets.

This theorem separates three data types:

  Object                         Boundary behaviour             Status
  ------------------------------ ------------------------------ ---------
  total packet mass              finite nonzero Abel constant   proved
  scaled index distribution      $\Gamma(2,1)$ weak limit       proved
  source-tagged divisor vector   no norm or weak subnet limit   refuted

The first two rows cannot be promoted to the third. Any boundary retaining the full prime-ideal ledger must use a different topology or an additional distributional construction.

# Executable certificate and adversarial controls

The project includes a producer, an implementation-independent checker and a unit/adversarial suite. The producer constructs reciprocal trace polynomials and evaluates them at $T=578$. Seventy exact rows, $3\le n\le72$, satisfy [\[eq:totientformula\]](#eq:totientformula){reference-type="eqref" reference="eq:totientformula"} to more than 70 decimal digits. Eighteen rows are cross-checked against the frozen HCS-P51 certificate.

Table [1](#tab:abel){reference-type="ref" reference="tab:abel"} records finite Abel sums. The cutoff is $\lceil40/\tau\rceil$; an explicit geometric bound controls the omitted tail. The table is a reproducibility diagnostic, not the proof of Theorems 3.2--4.1.

::: {#tab:abel}
    $\tau$   $\tau^2Z(\tau)$   ratio to $A_L$   prefix mass
  -------- ----------------- ---------------- -------------
    0.2000      1.7634673091         0.912259      0.908028
    0.1000      1.8834717456         0.974338      0.597776
    0.0500      1.9196452327         0.993051      0.268687
    0.0250      1.9295814347         0.998191      0.092475
    0.0125      1.9321857649         0.999539      0.027304

  : Finite convergence to $A_L=1.9330777456585248\ldots$ and escape of the fixed prefix $3\le n\le20$.
:::

At the smallest recorded scale, the normalized Laplace transforms at $s=1/2,1,2$ are respectively $0.4441926$, $0.2496630$ and $0.1107191$, approaching the exact Gamma targets $4/9$, $1/4$ and $1/9$.

The checker recomputes all dependency hashes and uses independent routines for prime factorization, $\varphi$, $\mu$, divisors and finite Abel sums. The suite rejects: deletion of the reciprocal factor $1/2$; first-order instead of second-order boundary scaling; a shape-one exponential profile; norm convergence of the tagged vectors; and promotion to an all-orbit theorem, von-Mangoldt trace, Fredholm determinant or Hilbert--Pólya operator.

# Route evaluation and conclusion

HCS-P52 closes the boundary problem named at the end of HCS-P51, but only on one exact orbit and only after distinguishing scalar, rescaled-distributional and tagged-vector topologies. The strongest positive statement is an exact source-native Abel/Tauberian law with a canonical Gamma blow-up. The strongest obstruction is equally exact: the original positive tagged vectors have no boundary even weakly.

Under the Session Route-A evaluator, the result is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\mathrm{A4\_FORMAL\_HINT}),$$ with overall status `ROUTE_A_EXPLORATORY`. A1 remains weak because one packet orbit is not an intrinsic all-prime orbit family. A2 fails because there is no zeta or Fredholm determinant. A3 receives genuine partial credit from the proved boundary law and profile, but no continuation, functional equation or zero theorem follows. A4 remains formal because no quantum lift or operator domain is supplied. Route B is therefore not authorized.

The next non-micro theorem is pressure-uniform boundary interchange. One must determine whether the P51 all-orbit weights make $$\tau^2\sum_{\gamma\ \mathrm{primitive}}
e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}e^{-\tau n}\|D_{\gamma,n}\|_{\rm tag}$$ converge to a finite orbit-height sum, and whether the scaled index keeps the same Gamma profile. That problem couples orbit growth to the cyclotomic boundary and cannot be settled by adding more finite period-four factors.

The present theorem thus moves the route across the first Abel boundary while marking exactly where the next bridge begins.

# Elementary bounds used by the certificate

For $0<x<1$, $$-\log(1-x)=\sum_{k\ge1}\frac{x^k}{k}\le\frac{x}{1-x}.$$ Consequently, if $K\ge1$, $$\sum_{d>K}-\log(1-L^{-d})
\le
\frac{L^{-(K+1)}}{(1-L^{-(K+1)})(1-L^{-1})}.$$ The certificate takes $K=32$.

For a finite Abel cutoff $N$ and $q=e^{-\tau}$, Theorem 2.1 gives $b_n\le n\log L/2+C_L$. The tail is therefore bounded by $$\sum_{n>N}b_nq^n
\le\frac{\log L}{2}
\frac{q^{N+1}((N+1)-Nq)}{(1-q)^2}
+C_L\frac{q^{N+1}}{1-q}.$$ This is the stored truncation bound for every row in the compact JSON certificate.

Finally, the Gamma transform values used as adversarial sentinels are $$\mathcal L_{\Gamma(2,1)}(s)=(1+s)^{-2},
\quad
\mathcal L(1/2)=\frac49,
\quad
\mathcal L(1)=\frac14,
\quad
\mathcal L(2)=\frac19.$$
