---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-bulgarian-solitaire-recurrent-necklace-route-a"
canonical_tex: "henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/paper/main.pdf"
source_sha256: "13a3e573b93660191901d103341e81864055cc7e3efb70fa5aa4b933a9d0c1e1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Bulgarian Solitaire: Recurrent Necklaces, Every Fixed Iterate, and the Full Finite Koopman Spectrum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_bulgarian_solitaire_recurrent_necklace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For Bulgarian solitaire on every integer-partition set $\mathcal P(N)$, we turn Brandt's attributed recurrent classification into a complete periodic ledger. The unique decomposition $N=\binom{k}{2}+r$, $0\le r<k$, identifies recurrent partitions with length-$k$, weight-$r$ binary words, and one solitaire move becomes rotation. We derive a closed formula for every positive-iterate fixed count, then recover all least periods, primitive cycles, and the finite Artin--Mazur zeta by Möbius inversion. The finite cycle factors also give the full Koopman algebraic spectrum, including the transient zero multiplicity. The finite census is a regression oracle, not the proof of the all-$N$ theorem.
author:
- 'Anonymous structural certificate HCS-C190'
title: |
  Bulgarian Solitaire: Recurrent Necklaces, Every Fixed Iterate,\
  and the Full Finite Koopman Spectrum
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Bulgarian solitaire; integer partitions; binary necklaces; primitive cycles; dynamical zeta; Koopman spectrum.

chinese-simplified

中文摘要

本文研究任意整数分拆集合上的保加利亚单人纸牌动力学。利用归属于 [Brandt]{lang="en"}的循环分拆分类，将循环状态与长度为$k$、重量为$r$ 的二进制词对应，其中$N=\binom{k}{2}+r$且$0\le r<k$；一次动力学迭代正好对应循环旋转。 由此得到所有正迭代固定点数的闭式公式，再用[Möbius]{lang="en"}反演恢复 全部最小周期、原始循环、有限动力学$\zeta$函数与包含瞬态零重数的完整有限 [Koopman]{lang="en"}代数谱。有限枚举仅用于回归检验，不替代全参数定理。

关键词：保加利亚单人纸牌；整数分拆；二进制项链；原始循环；动力学$\zeta$函数； [Koopman]{lang="en"}谱。

# The noninvertible map and Brandt coordinates

Write a partition of $N$ as $\lambda=(\lambda_1\ge\cdots\ge\lambda_m>0)$. The Bulgarian move is $$T_N(\lambda)=\operatorname{sort}\bigl(m,\lambda_1-1,\ldots,
 \lambda_m-1\bigr),$$ after zero parts are deleted. This map is generally noninjective. Every $N\ge1$ has a unique representation $$N=\binom{k}{2}+r,\qquad k\ge2,\quad 0\le r<k.$$ Brandt's cyclic-partition theorem [@Brandt82], treated also by Akin and Davis [@AkinDavis85], says that the recurrent set consists exactly of $$\phi(w)=\text{positive parts of }(k-1,k-2,\ldots,0)+w,
 \qquad w\in\{0,1\}^k,\quad |w|=r.$$ For the right rotation $(\rho w)_i=w_{i-1\bmod k}$, direct subtraction of the first column gives $T_N\phi=\phi\rho$. States correspond to words; dynamical cycles correspond to binary necklaces.

# Every fixed iterate and every primitive cycle

[\[thm:ledger\]]{#thm:ledger label="thm:ledger"} Let $t\ge1$ and $g=\gcd(k,t)$. Then $$F_t:=\#\operatorname{Fix}(T_N^t)=
 \begin{cases}
 \displaystyle\binom{g}{rg/k},&(k/g)\mid r,\\[2pt]
 0,&\text{otherwise}.
 \end{cases}$$ For each $d\mid k$, the number $P_d$ of points of least period $d$ and the number $C_d$ of $d$-cycles are $$P_d=\sum_{e\mid d}\mu(d/e)F_e,\qquad C_d=P_d/d.$$ Consequently the zeta function of the full noninvertible finite map is $$\label{eq:zeta}
 \zeta_{T_N}(z)=\exp\!\left(\sum_{t\ge1}\frac{F_t}{t}z^t\right)
 =\prod_{d\mid k}(1-z^d)^{-C_d}.$$

#### Proof.

The index rotation $\rho^t$ has $g$ cycles, each of length $k/g$. A fixed binary word is constant on each index cycle, so its weight is a multiple of $k/g$; choosing the $rg/k$ one-cycles gives the displayed binomial. A point fixed by $T_N^t$ is periodic and hence recurrent, so no transient partition adds to this count. Divisor Möbius inversion gives $P_d$, and division by $d$ gives $C_d$. Substituting $F_t=\sum_{d\mid t}dC_d$ into the exponential definition proves [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. $\square$

# The full finite Koopman algebraic spectrum

Let $p(N)=|\mathcal P(N)|$ and let $(U_Nf)(\lambda)=f(T_N\lambda)$ on all complex functions on $\mathcal P(N)$. Ordering each functional-graph component from its transient trees toward its cycle gives $$\label{eq:char}
 \det(\xi I-U_N)=\xi^{p(N)-\binom{k}{r}}
 \prod_{d\mid k}(\xi^d-1)^{C_d},\qquad
 \det(I-zU_N)=\prod_{d\mid k}(1-z^d)^{C_d}=\zeta_{T_N}(z)^{-1}.$$ Thus zero has algebraic multiplicity $p(N)-\binom{k}{r}$. If $\omega_k=e^{2\pi i/k}$, the nonzero multiplicities are $$\operatorname{mult}(\omega_k^j)
 =\sum_{\substack{d\mid k\\k\mid jd}}C_d,\qquad
 \operatorname{Tr}(U_N^t)=F_t.$$ Indeed, transient vertices contribute only a zero diagonal block to the characteristic polynomial, whereas a $d$-cycle contributes $\xi^d-1$ and every $d$th root once. Formula [\[eq:char\]](#eq:char){reference-type="eqref" reference="eq:char"} determines eigenvalues with algebraic multiplicities, not the nilpotent Jordan block sizes in the transient sector.

For $N=8=\binom42+2$, the six recurrent words form one $2$-cycle and one $4$-cycle. Hence $(F_1,F_2,F_3,F_4)=(0,2,0,6)$, $\zeta_{T_8}(z)=((1-z^2)(1-z^4))^{-1}$, zero has multiplicity $22-6=16$, and the four fourth-root multiplicities are $(2,1,2,1)$. The sentinel is obtained both from all $22$ partitions of $8$ and from the word model.

# Reflection reversal on the recurrent core

Use indices in $\mathbb Z/k\mathbb Z$ and define $(Qw)_i=w_{-i}$. Then $Q^2=1$ and a direct index calculation gives $$Q\rho Q=\rho^{-1}.$$ Transporting $Q$ through $\phi$ produces an involutory reversor of the recurrent partition permutation. More generally, each $\rho^aQ$ is an involutory reversor, giving $k$ phase-labelled reflection formulas; these formulas need not act distinctly when the weight layer is nonfaithful. The corresponding recurrent Koopman permutation is unitary; reflection followed by coefficientwise conjugation is an antiunitary reversor. No such inverse relation is claimed on all of $\mathcal P(N)$ because $T_N$ is generally noninjective.

# Triangular boundary and evidence scope

If $r=0$, the sole word is $0^k$ and the sole recurrent partition is the staircase $(k-1,k-2,\ldots,1)$. It is fixed, so $F_t=1$ and $\zeta_{T_N}(z)=(1-z)^{-1}$; the recurrent Koopman spectrum is $\{1\}$, while the full operator has zero algebraic multiplicity $p(N)-1$. The conclusion concerns the recurrent core; triangular deck size does not erase the transient basin in general.

The executable census covers every $1\le N\le40$. A producer enumerates 757 recurrent words and their 114 cycles. A separate checker constructs all 215,307 integer partitions, follows the actual noninvertible map, and recovers exactly the same recurrent states and cycles. This finite agreement tests implementations and conventions; it does not establish Brandt's all-$N$ classification or classify complete transient trees and hitting times.

The independent checker passes 658,664 assertions. A separate SymPy path passes 2,210 checks, producer replay is byte exact, and the hostile suite rejects 118 semantic mutations after their payload hashes are repaired plus one stale-hash attack. These are implementation checks, not an independent mathematical review.

# Route-A stop and limitations

Periodic cycles and their finite determinant are exact, but partition and necklace data contain no intrinsic rational-prime carrier, prime-power weight, or logarithmic prime clock. No target divisor, functional equation, continuation, counting law, or Weil compression follows. The finite unitary on the recurrent core is therefore a formal operator hint only: $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{WEAK},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}).$$ The overall verdict is `ROUTE_A_REJECTED`; Route B is false. We do not claim a complete transient tree, an exact hitting-time distribution, nilpotent Jordan block sizes, a global reversor, or priority for the Brandt and Akin--Davis inputs.

#### Scope.

No target zero or prime table, arithmetic local datum, Euler factor, root number, automorphy input, target divisor, or Hilbert--Polya operator is used. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data and code availability.** Package-local exact evidence and deterministic code accompany this manuscript. **Ethics.** No human, animal, clinical, personal, or sensitive data are used; approval is not applicable. **Author contributions (CRediT).** This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, and Writing; AI systems are not authors. **Funding and conflicts.** No external funding is reported; no conflict is known. **AI-use disclosure.** An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

2 J. Brandt, "Cycles of partitions," *Proc. Amer. Math. Soc.* 85(3) (1982), 483--486. <https://doi.org/10.1090/S0002-9939-1982-0656129-5>.

E. Akin and M. Davis, "Bulgarian Solitaire," *Amer. Math. Monthly* 92(4) (1985), 237--250. <https://doi.org/10.1080/00029890.1985.11971590>.
