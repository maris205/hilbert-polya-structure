---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--10-entropy-paired-relative-determinant"
canonical_tex: "symbolic_dynamics/papers/10-entropy-paired-relative-determinant/main.tex"
canonical_pdf: "symbolic_dynamics/papers/10-entropy-paired-relative-determinant/main.pdf"
source_sha256: "80d13ea272996e4a4f07fd7b8153246918a33c0db254197c7e2e7fbb73d3f5c2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Entropy-Paired Relative Determinants for Tensor-Prime Symbolic Atoms: A Common Critical Strip and the Positive-Orientation Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/10-entropy-paired-relative-determinant>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/10-entropy-paired-relative-determinant/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/10-entropy-paired-relative-determinant/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/10-entropy-paired-relative-determinant/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/10-entropy-paired-relative-determinant/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct an exact relative Fredholm determinant from entropy-ordered tensor-prime symbolic atoms. Pair consecutive atoms by a frozen $1|1$ graded block and set $$D_s^+=\operatorname{diag}(p_1^{-s},p_3^{-s},\ldots),\qquad
   D_s^-=\operatorname{diag}(p_2^{-s},p_4^{-s},\ldots).$$ Although neither sector is trace class near the critical line, their paired difference is trace class throughout $\operatorname{Re}s>0$. The proof is the exact identity $a^{-s}-b^{-s}=s\int_a^b x^{-s-1}\,\mathrm dx$ summed over disjoint entropy intervals. It yields $$R(s,z)=\det_{\!F}\!\left[(I-zD_s^+)(I-zD_s^-)^{-1}\right]
   =\prod_{n\ge1}\frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}},$$ with every relative repetition trace retained. The reflected completion $H(s,z)=R(s,z)R(1-s,z)$ is holomorphic and exactly invariant under $s\mapsto1-s$ on $0<\operatorname{Re}s<1$. At $z=1$ it is zero-free but not vertically constant: the second derivative of $\log H(1/2+it,1)$ at $t=0$ is a strictly positive convergent series. The gain has a sharp cost. The prime sign is fixed by entropy-rank parity and does not exponentiate with repetition, so the logarithmic derivative carries an alternating-rank rather than positive von Mangoldt ledger. A finite-block rigidity theorem proves that any fixed local cancellation rule extending to all $\operatorname{Re}s>0$ must have zero block sum and therefore cannot assign $+1$ to every prime. SD-C12 supplies a common-strip relative determinant and a scoped obstruction, not a Riemann divisor or Hilbert--Pólya operator.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Entropy-Paired Relative Determinants for Tensor-Prime Symbolic Atoms:\
  A Common Critical Strip and the Positive-Orientation Obstruction
```

## Markdown 正文

# Introduction {#sec:introduction}

The tensor-prime symbolic program has an exact arithmetic clock but a stubborn analytic threshold. A loop at the tensor atom $F_p$ carries the intrinsic entropy weight $e^{-s h(F_p)}=p^{-s}$, so its repetitions recover $p^{-rs}$. The corresponding diagonal transfer is trace class only for $\operatorname{Re}s>1$. Moving that boundary past the critical line by separate estimates is impossible because it would require summing the prime harmonic series.

SD-C12 changes the data type. Rather than regularizing a single positive transfer, it compares two transfers whose atoms are paired by strict entropy rank. The odd-rank and even-rank sectors are individually large, but their relative difference consists of adjacent increments of $x^{-s}$. Those increments integrate over disjoint intervals and are trace class on the full half-plane $\operatorname{Re}s>0$. The cancellation is local, determinate once the least atom and grading orientation are fixed, and independent of any target zero. These choices are a relative modeling convention, not an invariant forced by the tensor-atom monoid.

The relative construction produces more than a formal alternating product. On the safe two-variable domain it is the ordinary Fredholm determinant of an $I+\mathcal S_1$ quotient. At the primary normalization $z=1$, it is holomorphic and zero-free on $\operatorname{Re}s>0$. Multiplication by the same determinant at $1-s$ gives exact reflection on the entire open critical strip. Unlike the balanced holomorphic double of SD-C11, this reflected product still moves with height. Its center curvature can be written as a strictly positive convergent series.

Analytic improvement does not imply arithmetic correctness. The relative trace is $$\mathcal S_r(s)=\sum_{n\ge1}
 \left(p_{2n-1}^{-rs}-p_{2n}^{-rs}\right).       \tag{1.1}$$ Thus odd-rank atoms enter with $+1$ and even-rank atoms with $-1$ for every repetition $r$. This is a super-parity sign attached to an atom sector. It is not a unitary orbit phase: a holonomy $u_p$ would contribute $u_p^r$ at repetition $r$, whereas the grading contributes the same sign at every $r$. Consequently the logarithmic derivative has the wrong von Mangoldt orientation even though the primitive/repetition ledger remains exact.

The paper establishes five concrete claims.

1.  The entropy-paired difference and every power difference are trace class and trace-norm holomorphic for $\operatorname{Re}s>0$.

2.  Their relative Fredholm determinant has an exact product and an all-order trace expansion beginning at $r=1$.

3.  The reflected product is holomorphic, zero-free, and symmetric on $0<\operatorname{Re}s<1$, while its restriction to the critical line is nonconstant.

4.  Fixed super-parity is distinguished exactly from a multiplicative cocycle phase, exposing the incorrect prime-power signs.

5.  A local finite-block theorem shows that zero-order cancellation on the full half-plane forces zero block sum. All-positive Euler orientation is therefore excluded in this class.

The result is deliberately scoped. It proves no analytic continuation beyond the stated domains, no Gamma completion, no Riemann--von Mangoldt counting law, and no spectral realization. Shifted pairings, larger balanced blocks, and non-prime inventories obey the same analytic mechanism. These controls make the common-strip theorem reusable but prevent it from certifying an RH-like divisor.

locates the construction among symbolic and relative determinants. freezes SD-C12. The determinant and reflection theorems appear in [\[sec:relative,sec:reflection\]](#sec:relative,sec:reflection){reference-type="ref" reference="sec:relative,sec:reflection"}; [6](#sec:orientation){reference-type="ref" reference="sec:orientation"} proves the orientation obstruction. Exact controls and the Route-A boundary close the main text.

# Related work and claim boundary {#sec:related}

#### Symbolic zeta functions and transfer determinants.

Periodic-point zeta functions for shifts of finite type admit finite determinant formulas, and transfer operators organize primitive cycles and their repetitions [@bowenlanford1970; @ruelle1976]. SD-C12 retains that periodic-word logic after reducing each tensor-prime full shift to its atom loop. Its new object is not another finite-state zeta formula. It is a relative determinant for a countable entropy-ordered atom inventory in a domain where the two sector determinants do not separately exist.

#### Signed and graded symbolic constructions.

Alternating determinants arise from exterior automata in sofic dynamics [@beal1995]. Signed Lefschetz and zeta structures also occur in the homological treatment of symbolic systems [@deeley2018], while flip systems provide zeta functions adapted to a symbolic involution [@kimleepark2003]. These works establish that signs and gradings are natural symbolic data. They do not imply that a sector sign behaves as an orbit holonomy. The distinction between a fixed supertrace sign and a phase raised to the repetition number is central here.

#### Relative Fredholm determinants.

For operators differing by trace class, an $I+\mathcal S_1$ quotient has an ordinary Fredholm determinant with a trace expansion; infinite determinant theory provides the analytic framework [@simon1977]. The novelty claimed here is narrower than that general theory. The entropy-adjacent symbolic pairing supplies an exact trace-class difference on $\operatorname{Re}s>0$, and its arithmetic meaning can be audited orbit by orbit. No new theorem about arbitrary Fredholm pairs is asserted.

#### Direct collision audit.

Bayart and Kouroupis prove strong universality on $2/3<\operatorname{Re}s<1$ for the alternating prime Dirichlet series $\sum_{k\ge1}(-1)^kp_k^{-s}$ [@bayartkouroupis2024]. A 2014 MathOverflow question also writes an Euler product whose prime values are chosen by even/odd prime index [@agno2014mathoverflow]. The latter is cited only as evidence that the rank-parity product has appeared in public discussion, not as a refereed theorem. These collisions rule out any novelty claim for alternating prime-rank coefficients themselves. SD-C12 instead proves a tensor-atom source theorem, an $I+\mathcal S_1$ relative quotient, a reflected zero-free completion with strict center curvature, and the scoped finite-block rigidity result. No claim is made that this combination is the first in the literature.

#### Claim boundary.

The paper proves a source-specific relative determinant theorem and a general finite-block cancellation criterion under explicit locality hypotheses. It does not claim priority for graded traces, signed symbolic zeta functions, or relative determinants. Nor does it identify the resulting product with the Riemann zeta function. The prime factors with even entropy rank occur in the denominator, the reflected product is zero-free in its proved strip, and no operator lift is supplied. Those failures are part of the theorem package, not qualifications deferred to future work.

# SD-C12: entropy-paired tensor atoms {#sec:source}

For an integer $m\ge2$, let $F_m=(\{1,\ldots,m\}^{\mathbb Z},\sigma_m)$ be the full two-sided shift. Cartesian product satisfies $F_m\times F_n\cong F_{mn}$ and topological entropy satisfies $h(F_m)=\log m$. The tensor-indecomposable objects are therefore $F_p$ with $p$ rational prime. Write $$p_1=2<p_2=3<p_3=5<\cdots                       \tag{3.1}$$ for the order induced by entropy. At the atom-reduced level, each $F_p$ has one primitive loop of roof $\log p$; its $r$th traversal has weight $p^{-rs}$.

Pair consecutive entropy ranks as $$\mathcal B_n=(F_{p_{2n-1}}\mid F_{p_{2n}}),           \tag{3.2}$$ where the left entry has super-degree zero and the right entry has super-degree one. Let $\mathcal H_+=\ell^2(\mathbb N)$ with basis $(e_n^+)$ and $\mathcal H_-=\ell^2(\mathbb N)$ with basis $(e_n^-)$. The canonical rank-pairing unitary $U:\mathcal H_+\to\mathcal H_-$ is $Ue_n^+=e_n^-$. Define $$\begin{aligned}
 D_s^+e_n^+&=p_{2n-1}^{-s}e_n^+,&
 D_s^-e_n^-&=p_{2n}^{-s}e_n^-,                 \tag{3.3}\\
 B_s&=U^*D_s^-U
   =\operatorname{diag}(p_2^{-s},p_4^{-s},\ldots)
   &&\text{on }\mathcal H_+.                          \tag{3.4}\end{aligned}$$ Both operators are bounded and holomorphic in operator norm for $\operatorname{Re}s>0$. Neither is trace class throughout that half-plane.

For $$\Omega_+=\{(s,z)\in\mathbb C^2:\operatorname{Re}s>0,
                    \ |z|2^{-\operatorname{Re}s}<1\},   \tag{3.5}$$ set $$Q(s,z)=(I-zD_s^+)(I-zB_s)^{-1},
 \qquad R(s,z)=\det_{F}Q(s,z).                 \tag{3.6}
 \label{eq:relative-definition}$$ The primary normalization is $z=1$. The auxiliary variable $z$ marks word length and is not fitted.

The definition is legitimate only after proving $Q-I\in\mathcal S_1$; this is the first theorem below. The grading also permits the formal notation $$R(s,z)=\operatorname{Ber}(I-z(D_s^+\oplus D_s^-)),          \tag{3.7}$$ but [\[eq:relative-definition\]](#eq:relative-definition){reference-type="ref" reference="eq:relative-definition"} is the determinant convention: a relative Fredholm determinant on one Hilbert space, not a quotient of two independently defined infinite determinants.

All ingredients are frozen before evaluation: tensor atoms, entropy order, adjacent pairing, grading orientation, roof, function spaces, unitary, and determinant. The pairing is a modeling rule canonical only relative to the ordered list, the choice of its first atom, and the $+|-$ orientation. It is not an unqualified invariant of the tensor-atom monoid. Reversing the grading is an explicit control and replaces $R$ by $R^{-1}$. Riemann zeros, fitted scales, target phases, and inserted von Mangoldt weights are forbidden.

For reference, the Route-A object tuple is

0.96L0.21X Field & Frozen value\
Candidate & SD-C12 entropy-paired relative determinant\
Primitive/repetition & atom loop $F_p$ and its $r$th traversal\
Clock & $h(F_p)=\log p$ from the full shift\
Potential & $-s h(F_p)$\
Grading & $(-1)^{\operatorname{rank}(p)+1}$, fixed by sector\
Function space & $\ell^2(\mathbb N)_+\oplus\ell^2(\mathbb N)_-$\
Determinant & $\det_F[(I-zD_s^+)(I-zB_s)^{-1}]$\
Forbidden data & zero tables, root fitting, external-family mechanisms\

# The relative half-plane theorem {#sec:relative}

The analytic gain comes from estimating each entropy pair before summing over the inventory. For $a<b$ and $\operatorname{Re}s>0$, $$a^{-s}-b^{-s}=s\int_a^b x^{-s-1}\,\mathrm dx.        \tag{4.1}$$ The prime intervals $[p_{2n-1},p_{2n}]$ are disjoint. No estimate of the odd or even sector alone has this property.

[\[thm:trace-class\]]{#thm:trace-class label="thm:trace-class"} Let $\sigma=\operatorname{Re}s>0$. The map $s\mapsto K_s=D_s^+-B_s$ is holomorphic from the right half-plane to the trace class $\mathcal S_1(\mathcal H_+)$. More precisely, $$\|K_s\|_1
 \le \frac{|s|}{\sigma}2^{-\sigma}.           \tag{4.2}$$ For every integer $r\ge1$, $$K_{r,s}=(D_s^+)^r-B_s^r\in\mathcal S_1,
 \qquad
 \|K_{r,s}\|_1
 \le \frac{|s|}{\sigma}2^{-r\sigma}.          \tag{4.3}
 \label{eq:power-bound}$$ Consequently the relative trace $$\mathcal S_r(s)=\operatorname{Tr}K_{r,s}
 =\sum_{n\ge1}\left(p_{2n-1}^{-rs}-p_{2n}^{-rs}\right)             \tag{4.4}$$ exists for every repetition $r$, including $r=1$.

Apply [\[eq:pair-integral\]](#eq:pair-integral){reference-type="ref" reference="eq:pair-integral"} entrywise and sum absolute values: $$\begin{aligned}
 \|K_s\|_1
 &\le |s|\sum_{n\ge1}\int_{p_{2n-1}}^{p_{2n}}
                       x^{-\sigma-1}\,\mathrm dx \notag\\
 &\le |s|\int_2^\infty x^{-\sigma-1}\,\mathrm dx
  =\frac{|s|}{\sigma}2^{-\sigma}.             \tag{4.5}
 \label{eq:pair-integral}\end{aligned}$$ The bound is locally uniform in $s$. Uniform limits in $\mathcal S_1$ of the finite diagonal analytic sums prove trace-norm holomorphy. Since $(D_s^+)^r=D_{rs}^+$ and $B_s^r=B_{rs}$, applying the same calculation to $rs$ yields [\[eq:power-bound\]](#eq:power-bound){reference-type="ref" reference="eq:power-bound"}; the factor $r$ cancels in the integral. The trace formula follows from the diagonal entries and trace-norm convergence.

Equation [\[eq:pair-integral\]](#eq:pair-integral){reference-type="eqref" reference="eq:pair-integral"} also shows why the cancellation is local. The proof uses the gaps inside the selected pairs but ignores every gap between pairs. Primality is not needed for the estimate once an increasing inventory has been supplied.

[\[thm:relative-determinant\]]{#thm:relative-determinant label="thm:relative-determinant"} On $\Omega_+$, $Q(s,z)-I$ is trace class and $R$ is holomorphic and nonzero. It has the locally convergent product $$R(s,z)=\prod_{n\ge1}
 \frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}},       \tag{4.6}
 \label{eq:relative-product}$$ and the all-order trace expansion $$\log R(s,z)=-\sum_{r\ge1}\frac{z^r}{r}\mathcal S_r(s).                  \tag{4.7}
 \label{eq:relative-log}$$ At $z=1$, these statements hold for every $\operatorname{Re}s>0$.

The domain condition gives $\|zB_s\|<1$. Algebraically, $$Q(s,z)-I=-z(D_s^+-B_s)(I-zB_s)^{-1}.           \tag{4.8}$$ The first factor is trace class by [\[thm:trace-class\]](#thm:trace-class){reference-type="ref" reference="thm:trace-class"}, and the second is bounded and holomorphic. Hence $Q-I\in\mathcal S_1$. Both $I-zD_s^+$ and $I-zB_s$ are invertible on $\Omega_+$, so $Q$ and its Fredholm determinant are nonzero. Finite diagonal truncations give the product; the trace-norm limit passes their determinants to [\[eq:relative-product\]](#eq:relative-product){reference-type="eqref" reference="eq:relative-product"}.

For the logarithm, [\[eq:power-bound\]](#eq:power-bound){reference-type="ref" reference="eq:power-bound"} gives $$\sum_{r\ge1}\frac{|z|^r}{r}|\mathcal S_r(s)|
 \le \frac{|s|}{\sigma}
       \sum_{r\ge1}\frac{(|z|2^{-\sigma})^r}{r}<\infty.           \tag{4.9}$$ The scalar logarithm series may therefore be summed in trace norm, producing [\[eq:relative-log\]](#eq:relative-log){reference-type="eqref" reference="eq:relative-log"}. Since $2^{-\sigma}<1$, $z=1$ is safe throughout the right half-plane.

The logarithmic derivative displays the arithmetic ledger without changing clocks: $$\partial_s\log R(s,1)
 =\sum_{p}\varepsilon_p\sum_{r\ge1}(\log p)p^{-rs},
 \qquad
 \varepsilon_{p_k}=(-1)^{k+1}.                         \tag{4.10}$$ This series is understood through the entropy pairs in the proved half-plane. It contains the correct primitive lengths and repetitions, but its orientation already differs from the positive prime-power side.

# Reflection without vertical sterility {#sec:reflection}

Define the reflected determinant on $$\Omega_{\mathrm{ref}}=
 \{(s,z):0<\operatorname{Re}s<1,\
 |z|2^{-\min(\operatorname{Re}s,1-\operatorname{Re}s)}<1\}       \tag{5.1}$$ by $$H(s,z)=R(s,z)R(1-s,z).                         \tag{5.2}$$ The primary slice $z=1$ lies in this domain for every $0<\operatorname{Re}s<1$.

[\[thm:reflection\]]{#thm:reflection label="thm:reflection"} The function $H$ is holomorphic and nonzero on $\Omega_{\mathrm{ref}}$ and satisfies $$H(s,z)=H(1-s,z).                               \tag{5.3}$$ For real $z$, it also obeys $H(\bar s,z)=\overline{H(s,z)}$. In particular, $$H(\tfrac12+it,1)=|R(\tfrac12+it,1)|^2>0.      \tag{5.4}
 \label{eq:critical-modulus}$$

The two factors are holomorphic and nonzero where $\operatorname{Re}s>0$ and $\operatorname{Re}(1-s)>0$, respectively. Their common domain is the open critical strip with the stated $z$ bound. Swapping $s$ and $1-s$ exchanges the two factors. Conjugation follows from the real entropy inventory and fixed real grading. On the critical line $1-s=\bar s$, which gives [\[eq:critical-modulus\]](#eq:critical-modulus){reference-type="eqref" reference="eq:critical-modulus"}.

Zero-freeness rules out the desired divisor, but it does not mean that the reflection completion is constant. The next theorem separates those two properties exactly.

[\[thm:motion\]]{#thm:motion label="thm:motion"} Let $$\Phi(t)=\log H(\tfrac12+it,1).$$ Then $\Phi$ is real analytic, even, and $$\Phi''(0)=2\sum_{n\ge1}
 \bigl[g(p_{2n-1})-g(p_{2n})\bigr]>0,           \tag{5.5}
 \label{eq:curvature}$$ where $$g(x)=\frac{x^{-1/2}(\log x)^2}{(1-x^{-1/2})^2}.                    \tag{5.6}$$ Therefore $H(1/2+it,1)$, and hence the modulus of $R$ on the critical line, has nontrivial vertical motion.

The locally uniform relative product permits termwise differentiation near $t=0$. For $q=x^{-1/2}$, $$\frac{\,\mathrm d^2}{\,\mathrm dt^2}
 \log|1-qe^{-it\log x}|\bigg|_{t=0}
 =\frac{q(\log x)^2}{(1-q)^2}=g(x).             \tag{5.7}$$ The modulus square in [\[eq:critical-modulus\]](#eq:critical-modulus){reference-type="ref" reference="eq:critical-modulus"} supplies the factor two and the entropy grading supplies the adjacent difference.

It remains to determine the sign. Put $y=\sqrt{x}>1$. Then $$g(x)=\frac{4y(\log y)^2}{(y-1)^2}.$$ Its logarithmic derivative is negative precisely when $$\log y>\frac{2(y-1)}{y+1}.                     \tag{5.8}$$ The difference between the two sides vanishes at $y=1$ and has derivative $(y-1)^2/[y(y+1)^2]>0$. Thus $g$ is strictly decreasing. Every summand in [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"} is positive, and the series converges by the alternating series criterion applied to the decreasing sequence $g(p_k)\to0$. Its sum is strictly positive.

This theorem marks genuine progress over a balanced two-layer double: the reflection operation no longer cancels every vertical frequency. Yet the motion is carried by a relative signed inventory, not by a positive Euler determinant, and the same theorem proves that no zero occurs in the strip.

# The positive-orientation obstruction {#sec:orientation}

The grading sign must be classified before it is interpreted as a periodic orbit phase. On $\mathcal H_+\oplus\mathcal H_-$, let $\Gamma=I_{\mathcal H_+}\oplus(-I_{\mathcal H_-})$. For the block-diagonal transfer $D_s=D_s^+\oplus D_s^-$, $$\operatorname{Str}(D_s^r)=\operatorname{Tr}(\Gamma D_s^r)
 =\sum_p\varepsilon_p p^{-rs},\qquad
 \varepsilon_{p_k}=(-1)^{k+1}.                         \tag{6.1}$$ The operator $\Gamma$ is inserted once by the trace. It is not part of $D_s^r$, so $\varepsilon_p$ is independent of $r$.

By contrast, a scalar unitary cocycle with primitive holonomy $u_p\in\mathbb T$ changes the transfer eigenvalue to $u_pp^{-s}$ and contributes $$(u_pp^{-s})^r=u_p^r p^{-rs}.                   \tag{6.2}$$ For $u_p=-1$, repetitions alternate with $r$. Replacing the fixed sector sign by $(-1)^r$ would therefore change the candidate, the transfer, and the determinant. The two sign mechanisms cannot be exchanged after the trace is computed.

The obstruction extends beyond $1|1$ pairs. The appropriate generality is a fixed local coefficient pattern, not arbitrary rank-dependent cancellation.

[\[thm:block-rigidity\]]{#thm:block-rigidity label="thm:block-rigidity"} Let $m\ge2$, let $c_1,\ldots,c_m\in\mathbb C$ be fixed, and let $1<x_1<x_2<\cdots$ be an inventory satisfying $$\begin{aligned}
 \frac{x_{mn+j}}{x_{mn+1}}&\longrightarrow1
       &&(j=1,\ldots,m),                       \tag{6.3}\label{eq:locality}\\
 \sum_{n\ge0}x_{mn+1}^{-1}&=\infty.            \tag{6.4}\label{eq:reciprocal-divergence}\end{aligned}$$ Set $$A_n(s)=\sum_{j=1}^m c_jx_{mn+j}^{-s},
 \qquad n\ge0.                                \tag{6.5}$$ Then $\sum_n|A_n(s)|$ converges locally uniformly on $\operatorname{Re}s>0$ if and only if $$\sum_{j=1}^m c_j=0.                           \tag{6.6}$$ The entropy-ordered prime inventory satisfies [\[eq:locality\]](#eq:locality){reference-type="eqref" reference="eq:locality"}--[\[eq:reciprocal-divergence\]](#eq:reciprocal-divergence){reference-type="eqref" reference="eq:reciprocal-divergence"}. Consequently no fixed finite-block local cancellation extending to the full right half-plane can assign coefficient $+1$ to every prime.

Assume first that the block sum vanishes and write $C_j=\sum_{k=1}^j c_k$. Discrete Abel summation gives $$A_n(s)=\sum_{j=1}^{m-1}C_j
 \left(x_{mn+j}^{-s}-x_{mn+j+1}^{-s}\right).   \tag{6.7}$$ The adjacent intervals within all blocks are disjoint. On a compact subset of $\operatorname{Re}s>0$, the integral identity [\[eq:pair-integral\]](#eq:pair-integral){reference-type="eqref" reference="eq:pair-integral"} bounds the sum of absolute values by a constant times $\int_{x_1}^{\infty}x^{-\sigma-1}\,\mathrm dx$. This proves local uniform convergence.

Conversely, let $C=\sum_jc_j\ne0$ and take $s=1$. Asymptotic locality gives $$A_n(1)=x_{mn+1}^{-1}(C+o(1)).                  \tag{6.8}$$ Thus $|A_n(1)|\ge |C|/(2x_{mn+1})$ for all sufficiently large $n$, contrary to [\[eq:reciprocal-divergence\]](#eq:reciprocal-divergence){reference-type="eqref" reference="eq:reciprocal-divergence"}. The prime inventory has asymptotically local fixed-size blocks, and Euler's divergence of $\sum_p1/p$ implies the required fixed-rank-subsequence divergence. The criterion follows.

The theorem is sharp for SD-C12: $(c_1,c_2)=(1,-1)$ has zero sum and opens the entire right half-plane. The positive Euler pattern $(1,1,\ldots,1)$ has sum $m$ and cannot do so. The theorem does not exclude rank-dependent phases, growing block size, sparse exceptional blocks, or nonlocal potentials. Those mechanisms require new source locks and new convergence proofs.

# Exact controls and proves-too-much boundary {#sec:controls}

The main statements are analytic identities, so their decisive controls can be proved without a root-fitting experiment. Let $1<x_1<x_2<\cdots$ be any increasing inventory and replace $(p_k)$ by $(x_k)$. Adjacent pairing still gives $$\sum_n|x_{2n-1}^{-s}-x_{2n}^{-s}|
 \le |s|\int_{x_1}^{\infty}x^{-\operatorname{Re}s-1}\,\mathrm dx.                  \tag{7.1}$$ Thus the half-plane theorem, relative product, and zero-free reflected strip hold for sorted composites, random integers, perturbed entropies, and matched non-prime inventories. Only the interpretation of the labels changes.

0.98L0.24L0.24X Control & Analytic result & Arithmetic diagnosis\
Reverse $+|-$ orientation & $R\mapsto R^{-1}$; same half-plane & no intrinsic choice of positive Euler orientation\
Shift pairing by one rank & same trace-class estimate, up to finite factors & most signs change although the inventory does not\
Balanced $m$-blocks & full half-plane iff block sum is zero & every admissible fixed pattern contains cancellation\
Sorted composites & identical interval proof & no prime-specific discrimination\
Random matched inventory & identical interval proof after sorting & mechanism proves too much\
All-positive blocks & fails at zero order & correct orientation loses the common strip\
Unitary phase $u_p$ & repetition sign becomes $u_p^r$ & different candidate and determinant\

The two-atom prefix already displays every structural effect. For $a<b$, $$R_{a,b}(s,z)=\frac{1-za^{-s}}{1-zb^{-s}},
 \qquad
 H_{a,b}(s,z)=R_{a,b}(s,z)R_{a,b}(1-s,z).       \tag{7.2}$$ At $z=1$ and $0<\operatorname{Re}s<1$, all four scalar factors are nonzero. On the critical line the modulus generally moves, but there is no zero. Adding more adjacent pairs preserves these properties through a locally uniform relative product.

Shifted pairing is particularly adversarial. Pairing $(p_2,p_3),(p_4,p_5),\ldots$ obeys the same proof, while the unpaired factor at $p_1$ is only a finite-rank correction. The parity of almost every prime is reversed. Hence the analytic continuation mechanism cannot decide which prime factors belong in the numerator. Entropy ordering chooses a reproducible pattern, but the trace-class theorem does not certify its arithmetic sign.

Larger blocks reach the same conclusion with more freedom. Coefficients such as $(1,1,-1,-1)$ or $(1,\omega,\omega^2)$, with $\omega^3=1$, satisfy zero block sum and therefore inherit the right-half-plane estimate. Their prime-power ledgers are mutually incompatible. Constant phases can change the block pattern, but they cannot turn a zero-sum vector into the all-positive vector.

These controls trigger the Route-A adversarial verdict $$\boxed{\texttt{STOP\_SCOPED / PROVES\_TOO\_MUCH}}.               \tag{7.3}$$ The proved theorem remains useful as a symbolic regularization principle. It cannot, by itself, distinguish the rational primes or infer a critical-line divisor.

# Route-A outcome and Route-B lock {#sec:route}

SD-C12 is fully testable at the symbolic determinant level. Its object, arithmetic source, clock, normalization, primitive loops, repetition rule, grading, function spaces, relative operator, and forbidden data are fixed.

0.99L0.08L0.27X Layer & Verdict & Evidence and strongest failure\
A0 & analytic arithmetic origin & tensor-indecomposable full shifts supply primes and the entropy clock; rank parity is source-derived but not the positive arithmetic orientation\
A1 & target fail & primitive atom loops and all repetitions are enumerated exactly, but even entropy ranks have the wrong fixed sign, so the target prime-power ledger fails\
A2 & exact auxiliary determinant & $R$ is a relative Fredholm determinant on $\operatorname{Re}s>0$ and $H$ is holomorphic on the critical strip; exactness does not repair the signed ledger, and $H$ is zero-free there\
A3 & fail & conjugation is real-coefficient symmetry and reflection is imposed tautologically by multiplying $R(s,z)R(1-s,z)$; no Gamma factor, continuation, counting law, Weil compression, or divisor\
A4 & fail & no natural unitary scattering object, fixed self-adjoint generator, Hilbert-space domain problem, or spectral parameter map\

The Route-A tuple is

  --------------------------------------------
   `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL,`
      `A2_ANALYTIC_DETERMINANT, A3_FAIL,`
                  `A4_FAIL).`
  --------------------------------------------

Here `A1_FAIL` is specifically a target-ledger failure, whereas `A2_ANALYTIC_DETERMINANT` certifies only the exact auxiliary relative determinant. That determinant solves an analytic domain problem but fails the target orientation and divisor gates. The overall status is therefore $$\boxed{\texttt{ROUTE\_A\_REJECTED}.}                             \tag{8.1}$$

The Route-B entry gate is closed. The relative pencil depends holomorphically on $s$ and is not a fixed self-adjoint operator. No dense domain, boundary condition, compact-resolvent mechanism, intrinsic $T\log T$ counting law, von-Mangoldt trace formula, Weil form, or completed determinant identity is defined by SD-C12. In particular, $$\mathtt{route\_b\_invocation\_allowed=false}.                   \tag{8.2}$$ Route B is not invoked to repair the wrong signs.

The next smallest same-family branch is an entropy-rank Bloch unitary twist. It should replace a fixed finite grading vector by a character of rank translation and then distinguish two questions: whether Fourier averaging preserves zero-order local cancellation, and whether the phase attached to a primitive atom is raised correctly at repetition $r$. Before any zero test, the branch must prove a trace-ideal domain and an exact signed/phase ledger.

# Conclusion {#sec:conclusion}

Entropy-adjacent pairing turns a divergent positive symbolic transfer into a rigorous relative determinant. The construction keeps the intrinsic $\log p$ clock, preserves every primitive repetition, reaches the whole right half-plane, and supports an exact reflected completion on the critical strip. Its critical-line modulus has strictly positive center curvature, so analytic reflection does not force vertical sterility.

The same mechanism fixes the failure boundary. Relative trace-class cancellation assigns opposite sector orientations inside each entropy block. Because super-parity is applied by the trace rather than transported around an orbit, its sign remains fixed under repetition. The resulting prime-power ledger is not the positive Euler ledger, and the reflected determinant has no zeros in its proved strip. The finite-block theorem shows that this tradeoff persists for every fixed local coefficient pattern: extension to $\operatorname{Re}s>0$ requires zero block sum.

SD-C12 should therefore be retained as a positive analytic prior and a negative arithmetic theorem. It demonstrates that relative symbolic cancellation can open the critical strip without an adjoint, but it cannot simultaneously keep all prime orientations positive. Entropy-rank Bloch twists provide the next minimal Symbolic-Dynamics-only test because they can separate sector parity from repetition phase. Any geometric interpretation of such a phase remains a Round-2 clue and is not developed here.

# Proof details and scope audit {#app:proofs}

## Holomorphy in trace norm

Fix a compact set $K\Subset\{\operatorname{Re}s>0\}$ and write $\delta=\min_{s\in K}\operatorname{Re}s>0$ and $M=\max_{s\in K}|s|$. The tail of the paired diagonal series satisfies $$\sup_{s\in K}\sum_{n>N}|p_{2n-1}^{-s}-p_{2n}^{-s}|
 \le M\sum_{n>N}\int_{p_{2n-1}}^{p_{2n}}x^{-\delta-1}\,\mathrm dx.       \tag{A.1}$$ The right-hand side tends to zero. Finite diagonal sums are entire $\mathcal S_1$-valued functions, so their locally uniform limit is holomorphic in trace norm. Applying the same argument to $rs$ proves the all-power statement.

## Product convergence and nonvanishing

On a compact subset of $\Omega_+$, $(I-zB_s)^{-1}$ is uniformly bounded and $Q(s,z)-I$ is locally uniformly trace class. Continuity of the Fredholm determinant in trace norm passes the finite diagonal determinants to the product in [\[eq:relative-product\]](#eq:relative-product){reference-type="ref" reference="eq:relative-product"}. Nonvanishing follows from invertibility: $Q$ is a product of two bounded invertible diagonal operators. Equivalently, the logarithm series [\[eq:relative-log\]](#eq:relative-log){reference-type="ref" reference="eq:relative-log"} converges absolutely and represents $R$ as the exponential of a holomorphic function.

For $z=1$, no local factor vanishes because $|p^{-s}|=p^{-\operatorname{Re}s}<1$. This observation applies to both $s$ and $1-s$ on the open critical strip, proving that $H(s,1)$ has neither zeros nor poles there.

## Fixed-rank reciprocal divergence

Let $(a_k)$ be a positive decreasing sequence with $\sum_ka_k=\infty$. For every fixed $m$, each residue subsequence $\sum_na_{mn+j}$ diverges. Indeed, convergence of the last subsequence would bound each following block of $m$ terms by $m$ times its preceding last term, forcing convergence of the full tail; the other residue subsequences dominate a shift of the last one. Applying this fact to $a_k=1/p_k$ and Euler's divergence proves [\[eq:reciprocal-divergence\]](#eq:reciprocal-divergence){reference-type="ref" reference="eq:reciprocal-divergence"} for consecutive prime blocks. Asymptotic locality [\[eq:locality\]](#eq:locality){reference-type="ref" reference="eq:locality"} is the fixed-block consequence of the standard asymptotic law for $p_k$.

## Controls outside the theorem

The finite-block necessity direction requires a fixed coefficient vector, bounded block size, asymptotic locality, and a nonsummable reciprocal block inventory. It does not cover:

-   coefficients that decay with rank;

-   nonzero-sum blocks occurring only on a sufficiently sparse subsequence;

-   block size increasing with entropy;

-   a nonlocal or infinite-memory potential;

-   a Bloch/Fourier integral whose character parameter is part of the symbolic extension.

These exclusions are theorem boundaries, not proposed solutions. Each would need a new frozen candidate and a proof that its prime-power ledger remains intrinsic.

## Route-B boundary

The unitary $U$ in SD-C12 merely identifies two copies of $\ell^2(\mathbb N)$ for a relative determinant. It is not a time-evolution operator, scattering matrix, or quantization map. Likewise, $H(s,1)$ is a holomorphic scalar family rather than the spectral determinant of one fixed self-adjoint generator. No Route-B conclusion follows from its reflection symmetry, real critical-line values, or zero-free strip.
