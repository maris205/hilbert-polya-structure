---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--exact-uc-polar-lower-growth"
canonical_tex: "logistic_dynamics/projects/exact_uc_polar_lower_growth/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/exact_uc_polar_lower_growth/paper/main.pdf"
source_sha256: "526554db6d6d569cba0357b4870c0ee94c58363ebc29986a9bd8d731c25fc79c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Cancellation-Safe Derivative Lower Bound for the Exact-$U_c$ Polar Fredholm Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/exact_uc_polar_lower_growth>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_lower_growth/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/exact_uc_polar_lower_growth/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/exact_uc_polar_lower_growth/README.md>)
- [BibTeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_lower_growth/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the unchanged canonical Fredholm determinant of the frozen exact-$U_c$ polar Logistic transfer family, we prove a cancellation-safe lower-growth statement at the real point $s=2$. The exact based-word trace logarithm is absolutely convergent there, and every signed denominator remains positive on the real axis. An absolute trace majorant bounds the determinant itself from below, while the pure-left length-one orbit gives a positive term in its logarithmic derivative. Writing $$\alpha_0=\frac{U_c^2}{4},\qquad
   \tau_*=-\log\alpha_0,\qquad
   B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},$$ we obtain $$D_{\mathrm{pol}}'(2)\ge
   \mathrm e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
   >0.0213.$$ Cauchy's estimate therefore yields $M_D(R)>0.0213(R-2)$ for $R>2$, and $M_D(R)>0.01065R$ for $R\ge4$. Moreover, $D_{\mathrm{pol}}(\sigma)\to1$ as $\sigma\to+\infty$; the nonzero derivative then proves that $D_{\mathrm{pol}}$ is transcendental entire, so its maximum modulus grows faster than every fixed power. These conclusions do not prove positive or exact order, an exponential lower bound, a zero-count lower bound, a $T\log T$ law, completed-xi structure, or the Riemann hypothesis.
author:
- Anonymous
date: August 2026
title: |
  A Cancellation-Safe Derivative Lower Bound\
  for the Exact-$U_c$ Polar Fredholm Determinant
```

## Markdown 正文

# Frozen determinant and main result

Let $u=U_c$ be the real root of $$u^3-2u^2+2u-2=0,
 \qquad \rho=u-1.
 \tag{1}$$ The inherited real system is the exact two-full-branch polar map on $I_L=[-\pi/2,0]$ and $I_R=[0,\pi/2]$. Its inverse branches $\phi_L,\phi_R$ extend to the fixed complex stadiums and share a holomorphic logarithmic weight $\ell=\operatorname{Log}a$, where $\phi_L'=a$ and $\phi_R'=-a$.

On the matching space $$X=A(U_L)\oplus A(U_R),
 \qquad
 B=\{(v_L,v_R):v_L(0)=v_R(0)\},$$ the transfer family is $$(\mathcal L_s v)_j(z)=\mathrm e^{s\ell(z)}
 \bigl[v_L(\phi_L(z))+v_R(\phi_R(z))\bigr].
 \tag{2}$$ The preceding analytic stages establish that $\mathcal L_{s,B}:=\mathcal L_s|_B$ is nuclear of order zero and that $$D_{\mathrm{pol}}(s):=\operatorname{det}_{\mathrm{Fr}}(I-\mathcal L_{s,B})
 \tag{3}$$ is entire. Equation (3), the roof clock, and the signed trace convention are fixed throughout this paper.

Define $$\alpha_0=\frac{U_c^2}{4},\qquad
 \tau_*=-\log\alpha_0,
 \qquad
 B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},
 \tag{4}$$ and let $$M_D(R)=\max_{|s|\le R}|D_{\mathrm{pol}}(s)|.
 \tag{5}$$

For the same determinant *(3)*, $$D_{\mathrm{pol}}'(2)\ge
 \mathrm e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
 >0.0213.
 \tag{6}$$ Consequently, $$M_D(R)>0.0213(R-2)\qquad(R>2),
 \tag{7}$$ and $$M_D(R)>0.01065R\qquad(R\ge4).
 \tag{8}$$ The function $D_{\mathrm{pol}}$ is transcendental entire. In particular, for every fixed $A>0$, $$\lim_{R\to\infty}\frac{M_D(R)}{R^A}=+\infty.
 \tag{9}$$

The explicit inequality in (7) is only linear. The qualitative statement (9) does not supply an effective coefficient sequence, an exponential rate, or a positive entire-function order.

# Signed trace logarithm on the safe real axis

For a based word $\omega\in\{L,R\}^n$, let $T_\omega>0$ denote its roof time and retain the exact orientation sign $$\varepsilon_\omega=(-1)^{\#R(\omega)}.
 \tag{10}$$ The inherited trace identity is $$\operatorname{Tr}\mathcal L_s^n
 =\sum_{\omega\in\{L,R\}^n}
 \frac{\mathrm e^{-sT_\omega}}
 {1-\varepsilon_\omega\mathrm e^{-T_\omega}}.
 \tag{11}$$ No denominator in (11) is replaced by an unsigned expression.

The real roof bound gives $$T_\omega\ge n\tau_*,
 \qquad
 \mathrm e^{-T_\omega}\le\alpha_0^n.
 \tag{12}$$ For $\sigma=\Re s\ge0$, equations (11)--(12) imply the absolute majorant $$|\operatorname{Tr}\mathcal L_s^n|
 \le \frac{(2\alpha_0^\sigma)^n}{1-\alpha_0^n}.
 \tag{13}$$ Thus, when $$\sigma>\sigma_*:=\frac{\log2}{-\log\alpha_0},
 \qquad q_\sigma:=2\alpha_0^\sigma<1,$$ the series converges normally and $$\sum_{n\ge1}\frac{|\operatorname{Tr}\mathcal L_s^n|}{n}
 \le
 \frac{-\log(1-q_\sigma)}{1-\alpha_0}
 =:B(\sigma).
 \tag{14}$$ Keeping the auxiliary Fredholm variable distinct from $s$, analytic continuation from its convergence disk gives $$D_{\mathrm{pol}}(s)=\exp\!\left(
 -\sum_{n\ge1}\frac{\operatorname{Tr}\mathcal L_s^n}{n}
 \right)
 \qquad(\Re s>\sigma_*).
 \tag{15}$$

For real $\sigma>\sigma_*$, both possible denominators in (11) are strictly positive. If $S(\sigma)$ denotes the complete positive trace sum in the exponent of (15), then $$S(\sigma)>0,
 \qquad
 \log D_{\mathrm{pol}}(\sigma)=-S(\sigma)<0.$$ Consequently, $$0<\exp[-B(\sigma)]\le D_{\mathrm{pol}}(\sigma)\le1.
 \tag{16}$$ At $\sigma=2$, equation (14) is exactly the constant $B_2$ in (4).

# The pure-left derivative lower bound

Normal convergence of the trace logarithm on closed sub-half-planes permits termwise differentiation. For real $\sigma>\sigma_*$, equation (15) gives $$\frac{d}{d\sigma}\log D_{\mathrm{pol}}(\sigma)
 =\sum_{n\ge1}\frac1n
 \sum_{\omega\in\{L,R\}^n}
 \frac{T_\omega\mathrm e^{-\sigma T_\omega}}
 {1-\varepsilon_\omega\mathrm e^{-T_\omega}}.
 \tag{17}$$ Every summand in (17) is positive. This use of positivity is cancellation-safe: it occurs only after the exact signed denominator has been fixed, and no complex or signed sum is split into incompatible absolute bounds.

The boundary periodic point $P=-\pi/2$ has one left label. For the length-one pure-left word, $$T_L=\tau_*,\qquad
 \mathrm e^{-T_L}=\alpha_0,\qquad
 \varepsilon_L=1.
 \tag{18}$$ Retaining this single positive term in (17) at $\sigma=2$ yields $$\left.\frac{d}{d\sigma}\log D_{\mathrm{pol}}(\sigma)\right|_{\sigma=2}
 \ge \frac{\tau_*\alpha_0^2}{1-\alpha_0}.
 \tag{19}$$ Meanwhile, (16) gives $D_{\mathrm{pol}}(2)\ge\mathrm e^{-B_2}$. Since $D_{\mathrm{pol}}'(2)=D_{\mathrm{pol}}(2)(\log D_{\mathrm{pol}})'(2)$, multiplying the two positive lower bounds proves $$D_{\mathrm{pol}}'(2)\ge
 \mathrm e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}.
 \tag{20}$$

This mechanism avoids the usual lower-bound obstruction from cancellation. It works at a real point where the exact orbit ledger is termwise positive; it does not assert positivity for complex $s$, nor does it transfer a single coefficient through an uncontrolled signed determinant expansion.

# Maximum modulus and transcendence

Fix $R>2$. The closed disk centered at $2$ with radius $R-2$ is contained in $\{|s|\le R\}$. Cauchy's derivative estimate on that disk therefore gives $$|D_{\mathrm{pol}}'(2)|\le\frac{M_D(R)}{R-2}.
 \tag{21}$$ Combining (20) with its certified decimal lower bound proves (7). If $R\ge4$, then $R-2\ge R/2$, which proves (8).

The trace logarithm supplies a separate qualitative conclusion. Since $q_\sigma=2\alpha_0^\sigma\to0$, equation (14) gives $B(\sigma)\to0$. Equations (15)--(16) therefore imply $$D_{\mathrm{pol}}(\sigma)\longrightarrow1
 \qquad(\sigma\to+\infty).
 \tag{22}$$ The derivative bound (20) proves that $D_{\mathrm{pol}}$ is nonconstant. A nonconstant polynomial diverges in modulus along the positive real ray, so (22) rules out every polynomial. Because $D_{\mathrm{pol}}$ is entire, it is transcendental entire.

Finally, write $D_{\mathrm{pol}}(s)=\sum_{m\ge0}a_ms^m$. Transcendence means that nonzero coefficients occur at arbitrarily high degrees. For any fixed $A>0$, choose an integer $m>A$ with $a_m\ne0$. Cauchy's coefficient estimate gives $$M_D(R)\ge |a_m|R^m,$$ and hence $$\frac{M_D(R)}{R^A}
 \ge |a_m|R^{m-A}\longrightarrow\infty.$$ This proves (9), but it gives no useful numerical value for $|a_m|$ as $m$ varies.

# Outward interval certificate and reproducibility

The companion scalar audit evaluates (1) and (4) with 1024-bit outward Arb balls. Table [1](#tab:lower-constants){reference-type="ref" reference="tab:lower-constants"} displays central decimal values; the machine-readable artifact retains the interval radii and the strict comparison gates.

::: {#tab:lower-constants}
  Quantity                          Certified displayed value
  --------------------------------- -----------------------------------------
  $U_c$                             $1.54368901269207636157085597180\ldots$
  $\alpha_0$                        $0.59574394197655937353067713411\ldots$
  $\tau_*$                          $0.51794433178925625819844058117\ldots$
  $2\alpha_0^2$                     $0.70982168880354028313796314116\ldots$
  $B_2$                             $3.06058413770995492489591306195\ldots$
  $\mathrm e^{-B_2}$                $0.04686031434695642308253249628\ldots$
  $\tau_*\alpha_0^2/(1-\alpha_0)$   $0.45472184398972339295137217650\ldots$
  Lower-bound product               $0.02130840854978611545501449300\ldots$

  : Target-free scalar evaluation. The final outward interval lies strictly above $0.0213$; no Fredholm determinant value is evaluated.
:::

The certificate checks that the algebraic root lies in its sealed bracket, $0<\alpha_0<1$, $2\alpha_0^2<1$, $2>\sigma_*$, every logarithm has a positive argument, and the final outward lower endpoint exceeds $0.0213$. Its data firewall forbids prime tables, primality predicates, Riemann-zero tables, zeta or xi evaluation, USTC data, parameter fitting, Fredholm evaluation, and root searches.

The source, regression, and artifact are synchronized as one provenance unit under , , and . The scalar program certifies only the numerical inequalities used after the analytic trace argument; it cannot certify termwise positivity or the Cauchy step by sampling.

# Limitations and conclusion

The safe real axis supplies a narrow way around signed cancellation. At $s=2$, the unchanged trace logarithm converges absolutely, all exact real denominators are positive, and the pure-left orbit gives a retained positive term. This proves $D_{\mathrm{pol}}'(2)>0.0213$ without evaluating the determinant. Cauchy's estimate transfers the local derivative certificate to an explicit linear lower bound for the global maximum modulus.

The limiting value $D_{\mathrm{pol}}(\sigma)\to1$ and the nonzero derivative also prove that the determinant is transcendental entire. The resulting super-polynomial maximum-modulus statement is qualitative. It does not control any high Taylor coefficient uniformly and therefore cannot be promoted to an exponential lower bound or a positive-order theorem.

The claim boundary is strict. This stage does not prove positive order, exact order, finite nonzero type, an exponential lower bound, a zero-count lower bound, a sharp divisor asymptotic, or a $T\log T$ law. It does not identify determinant zeros, relate primitive roof periods to logarithms of primes, produce von-Mangoldt weights, establish a completed-xi determinant, or construct a self-adjoint operator. Route B remains unauthorized, and no statement about Hilbert--Polya or the Riemann hypothesis follows.

The reusable conclusion is structural: a same-object trace logarithm can produce a certified determinant lower statement when one finds a real zero-free point where its exact signed terms become positive. Beyond that pointwise mechanism, quantitative lower growth still requires new information about high coefficients, boundary values, or the determinant divisor.

# Proof details

## Normal convergence and differentiation

Fix a compact set $K\subset\{s:\Re s>\sigma_*\}$, and let $\sigma_0=\min_{s\in K}\Re s$. Equation (13) gives $$\sum_{n\ge1}\sup_{s\in K}
 \frac{|\operatorname{Tr}\mathcal L_s^n|}{n}
 \le
 \sum_{n\ge1}
 \frac{(2\alpha_0^{\sigma_0})^n}
 {n(1-\alpha_0^n)}<\infty.$$ Thus the trace logarithm is a normally convergent series of holomorphic functions. Cauchy's integral formula on a slightly larger compact neighborhood permits termwise differentiation, which proves (17). For real $\sigma$, $0<\mathrm e^{-T_\omega}<1$ and $\varepsilon_\omega\in\{-1,1\}$, so every denominator and every numerator in (17) is positive.

## The determinant lower anchor

For real $\sigma>\sigma_*$, put $$S(\sigma)=\sum_{n\ge1}\frac1n
 \sum_{\omega\in\{L,R\}^n}
 \frac{\mathrm e^{-\sigma T_\omega}}
 {1-\varepsilon_\omega\mathrm e^{-T_\omega}}.$$ Termwise positivity and (14) give $0<S(\sigma)\le B(\sigma)$. Equation (15) becomes $D_{\mathrm{pol}}(\sigma)=\mathrm e^{-S(\sigma)}$, hence $$\mathrm e^{-B(\sigma)}\le D_{\mathrm{pol}}(\sigma)<1.$$ At $\sigma=2$, $q_2=2\alpha_0^2$, so $B(2)=B_2$. Combining this anchor with the pure-left term in (17) proves (20).

## Cauchy transfer

For $0<r<R-2$, Cauchy's estimate on $|s-2|\le r$ gives $$|D_{\mathrm{pol}}'(2)|\le
 \frac{\max_{|s-2|\le r}|D_{\mathrm{pol}}(s)|}{r}
 \le\frac{M_D(R)}{r}.$$ Letting $r\uparrow R-2$ proves (21). This centered-disk argument avoids the extraneous factor that would arise from estimating the derivative directly on the circle $|s|=R$.

## Super-polynomial maximum modulus

If an entire function $f(s)=\sum_{m\ge0}a_ms^m$ is not a polynomial, then for every $A>0$ there is an integer $m>A$ with $a_m\ne0$. Cauchy's coefficient estimate on $|s|=R$ gives $|a_m|\le M_f(R)R^{-m}$. Therefore $M_f(R)/R^A\ge|a_m|R^{m-A}\to\infty$. Applying this observation to $f=D_{\mathrm{pol}}$ completes the proof of (9).

# References {#references .unnumbered}

No external references are cited in this self-contained stage report. The argument uses the frozen determinant and trace ledger established in the preceding project stages and standard facts from complex analysis.
