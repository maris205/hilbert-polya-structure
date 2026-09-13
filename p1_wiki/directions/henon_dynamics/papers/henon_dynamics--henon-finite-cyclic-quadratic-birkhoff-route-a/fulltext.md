---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-finite-cyclic-quadratic-birkhoff-route-a"
canonical_tex: "henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a/paper/main.pdf"
source_sha256: "6838610efd55903c044d105b23b612f75ccbfac7a3ff6f727660bb97ce933b2a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Every-Iterate Quadratic Amplitudes for Finite Cyclic Rotations

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_finite_cyclic_quadratic_birkhoff_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the odd cyclic rotation $R_q(x)=x+1$ with quadratic observable $ax^2+bx$, we evaluate the complete Birkhoff amplitude at every iterate and for every source parameter. If $d=(an,q)$, the sum vanishes exactly when $d\nmid an(n-1)+bn$; otherwise its nonconstant branch has magnitude $d\sqrt{q/d}$ and an explicit Jacobi sign and completed-square phase. Over a prime source ring the zero level is $1+(\Delta/p)$ in the quadratic branch; for $p\ge5$ and $a=1,b=0$, $\Delta=n^2(1-n^2)/3$. This all-parameter theorem replaces a Heisenberg candidate that failed its quotient-coordinate and local-equivalence proof gate. Exhaustive checks through odd $q\le31$ are regression sentinels, not the proof. A same-clock finite unitary realizes the amplitude as $\operatorname{Tr}(U^nK^{-n})$. No target trace law, arithmetic Euler data, or Hilbert--Pólya operator is claimed.
author:
- 'Route-A structural certificate C161'
title: 'Every-Iterate Quadratic Amplitudes for Finite Cyclic Rotations'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** cyclic dynamics; Birkhoff sum; quadratic Gauss sum; exact vanishing; discriminant; finite Koopman unitary.

# All-iterate evaluation

Let $q$ be odd, let $n\ge1$, let $R_q(x)=x+1$ on $\mathbb Z/q\mathbb Z$, and $\phi_{a,b}(x)=ax^2+bx$. Summing $1,j,j^2$ gives $$\begin{aligned}
S_n\phi(x)&=A_nx^2+B_nx+C_n\pmod q,\tag{1}\\
A_n&=an,\quad B_n=an(n-1)+bn,\nonumber\\
C_n&=\frac{an(n-1)(2n-1)}6+\frac{bn(n-1)}2.\nonumber\end{aligned}$$ The quotients in $C_n$ are integers before reduction. Define $$G_{q,n}(a,b)=\sum_{x\bmod q}\exp(2\pi iS_n\phi(x)/q).$$ Put $d=(A_n,q)$ and $Q=q/d$. Translation $x\mapsto x+Q$ multiplies the sum by $\exp(2\pi iB_n/d)$. Hence $G_{q,n}=0$ exactly when $d\nmid B_n$. If $d\mid B_n$ and $Q>1$, write $A'=A_n/d$, $B'=B_n/d$, and $$h\equiv-(4A')^{-1}(B')^2\pmod Q,\qquad r\equiv C_n+dh\pmod q.$$ Reduction gives $d$ copies of a primitive odd quadratic sum, and completing the square gives $$G_{q,n}(a,b)=d\left(\frac{A'}Q\right)\epsilon_Q\sqrt Q\,
e^{2\pi ir/q},\qquad
\epsilon_Q=\begin{cases}1,&Q\equiv1\pmod4,\\ i,&Q\equiv3\pmod4.
\end{cases}                                                    \tag{2}$$ Here $(A'/Q)$ is the source-ring Jacobi symbol. For $\Gamma_k(A)=\sum_{x\bmod p^k}e^{2\pi iAx^2/p^k}$, split $x=y+p^{k-1}z$. The $z$-sum vanishes unless $p\mid y$ and gives $$\Gamma_k(A)=p\,\Gamma_{k-2}(A)\quad(k\ge2).$$ Together with $\Gamma_1(A)=(A/p)\epsilon_p\sqrt p$ and $\Gamma_0=1$, this proves every odd prime-power case. CRT combines the prime-power sums, and quadratic reciprocity reduces the accumulated signs to $(A'/Q)\epsilon_Q$. Thus (2) is an exact finite-sum identity. If $Q=1$, the separate constant branch is $G_{q,n}=q e^{2\pi iC_n/q}$. Thus (2), including its vanishing gate, holds for every $q,a,b,n$ in the frozen family; finite sweeps are only regressions.

# Zero levels and a concrete specialization

For an odd prime $p$, reduce $(A_n,B_n,C_n)$ modulo $p$. If $A_n\ne0$, completion of the square yields $$\#\{x:S_n\phi(x)=0\}=1+\left(\frac{\Delta}{p}\right),\qquad
\Delta=B_n^2-4A_nC_n.                                        \tag{3}$$ If $A_n=0\ne B_n$ the count is one; if $A_n=B_n=0$, it is $p$ or zero according as $C_n=0$ or not. In the pure quadratic case $a=1,b=0$, $p\ge5$, and $n\ne0\pmod p$, $$\Delta=\frac{n^2(1-n^2)}3,
\qquad \#\{x:S_nx^2=0\}=1+\left(\frac{\Delta}{p}\right).     \tag{4}$$ Thus $n\equiv\pm1\pmod p$ gives the single double root, whereas $n\equiv0\pmod p$ gives all $p$ roots.

# Same-clock unitary and boundary

On $\mathcal H_q=\ell^2(\mathbb Z/q\mathbb Z)$ let $(K_qf)(x)=f(x+1)$, let $M_\phi$ multiply by $e^{2\pi i\phi(x)/q}$, and put $U_\phi=M_\phi K_q$. Direct iteration gives the exact same-clock identity $$G_{q,n}(a,b)=\operatorname{Tr}(U_\phi^nK_q^{-n}).              \tag{5}$$ The compensating shift is essential; (5) is not replaced by $\operatorname{Tr}(U_\phi^n)$. Let $P f(x)=f(-x)$, let $J$ be complex conjugation, set $g(x)=(a-b)x^2$, and let $D_g$ multiply by $e^{2\pi ig(x)/q}$. The antiunitary $\Theta=D_gPJ$ obeys $$\Theta^2=I,\qquad \Theta U_\phi\Theta^{-1}=U_\phi^{-1}.         \tag{6}$$ Indeed $g$ is even and $g(x)-g(x-1)=\phi(-x)-\phi(x-1)=(a-b)(2x-1)$, exactly the multiplier identity obtained when $P$ reverses the shift. More explicitly, $$(\Theta U_\phi\Theta f)(x)
=e^{2\pi i\{g(x)-\phi(-x)-g(1-x)\}/q}f(x-1)
=e^{-2\pi i\phi(x-1)/q}f(x-1)=U_\phi^{-1}f(x).$$

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION})$. We claim no target trace/divisor/counting law, isolated stability determinant, arithmetic local/Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing data and programs are packaged with this certificate; no external dataset is used. **Ethics.** No human participants, animals, or sensitive personal data are involved. **Author contributions/CRediT.** Anonymous technical certificate; Conceptualization, Formal analysis, Software, Validation, and Writing are recorded at package level. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported derivation planning, drafting, and code review. Packaged independent checks validate quantitative claims; the assistant was not treated as an external peer reviewer.
