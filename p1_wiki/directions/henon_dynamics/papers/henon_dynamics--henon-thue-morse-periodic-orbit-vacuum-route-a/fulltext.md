---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-thue-morse-periodic-orbit-vacuum-route-a"
canonical_tex: "henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a/paper/main.pdf"
source_sha256: "6b66f0c857d1ae516909cdb68d0654c4b29041b27a9b5926775e97162575b07c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Minimal Uniformly Recurrent Subshift with a Periodic-Orbit Vacuum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_thue_morse_periodic_orbit_vacuum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The two-sided Thue--Morse substitution subshift is nonempty, minimal, and uniformly recurrent, yet it has no shift-periodic point. We give a self-contained proof: for every proposed period $p$, an odd-popcount multiple $d=p(2^k-1)$ forces a mismatch inside every sufficiently long Thue--Morse window. Thus every positive Artin--Mazur fixed-point count and primitive-cycle count vanishes and the source zeta is $1$. Circulated finite substitution words are audited as periodic controls, with exact local and macroscopic defect ledgers; they are not points of the limiting subshift. This proves that rich recurrence alone need not supply a Route-A primitive-orbit layer.
author:
- 'Route-A structural certificate C144'
title: |
  A Minimal Uniformly Recurrent Subshift with a\
  Periodic-Orbit Vacuum
```

## Markdown 正文

# Frozen language subshift

Let $t_n\in\{0,1\}$ be the parity of the binary digit sum of $n\geq0$. Equivalently, $t=01101001\cdots$ is fixed by the substitution $0\mapsto01$, $1\mapsto10$. Write $w_q=t_0\cdots t_{2^q-1}$ and let $\overline w_q$ denote bitwise complement. Freeze $$X_{\rm TM}=\{x\in\{0,1\}^{\mathbb Z}:\text{every finite factor of $x$
occurs in $t$}\}$$ with one left-shift iterate as the clock. The Artin--Mazur convention is $$\zeta_{\rm TM}(z)=\exp\!\left(\sum_{n\geq1}
\#\operatorname{Fix}(\sigma^n|X_{\rm TM})\frac{z^n}{n}\right).       \tag{1}$$ The language definition makes $X_{\rm TM}$ closed and shift invariant.

Binary concatenation without carries gives, for $0\leq r<2^q$, $$t_{j2^q+r}=t_j\mathbin{\mathsf{xor}}t_r.                         \tag{2}$$ Hence each aligned $q$-block is $w_q$ or $\overline w_q$. Moreover $t_{2m}=t_m$ and $t_{2m+1}=1-t_m$, so every pair beginning at an even coordinate is complementary and neither $000$ nor $111$ occurs.

# Uniform recurrence and minimality

Fix a factor $u$ of $t$ and choose $q$ so that $u$ occurs in $w_q$. Every interval of length $4\cdot2^q$ contains three complete aligned $q$-blocks. Their types are three consecutive symbols of $t$, not all $1$, so one is $w_q$ and contains $u$. Thus every factor returns with bounded gaps.

For nonemptiness, extend $t$ arbitrarily on negative coordinates and take a product-topology limit of shifts whose origins tend to $+\infty$. Every fixed window of the shifted sequence eventually lies wholly in $t$, so every factor of the limit belongs to the language. If $x\in X_{\rm TM}$ and $u$ has recurrence bound $R$, every length-$R$ factor of $x$ is a factor of $t$ and therefore contains $u$. Consequently every orbit in $X_{\rm TM}$ meets every nonempty cylinder: $X_{\rm TM}$ is minimal.

# All-period aperiodicity theorem

Fix a proposed positive period $p$. Choose an odd integer $k$ strictly larger than the binary length of $p$ and set $$d=p(2^k-1)=(p-1)2^k+(2^k-p).                                    \tag{3}$$ The low $k$ bits of $2^k-p$ complement the $k$-bit expansion of $p-1$. The two summands in (3) occupy disjoint binary blocks, whence $$\operatorname{popcount}(d)=\operatorname{popcount}(p-1)
+k-\operatorname{popcount}(p-1)=k.                              \tag{4}$$ Therefore $d$ is a multiple of $p$ and $t_d=1\ne t_0$.

Let $b$ be the binary length of $d$, so $d<2^b$. Every interval of $t$ of length $2^{b+1}$ contains a complete $b$-aligned block. Equation (2) shows that its symbols at offsets $0$ and $d$ differ. Those offsets are congruent modulo $p$, so the interval is not $p$-periodic. If a $p$-periodic $x\in X_{\rm TM}$ existed, its window of that length would occur in $t$ and would be $p$-periodic, a contradiction. Hence $$\operatorname{Fix}(\sigma^n|X_{\rm TM})=\varnothing\quad(n\geq1),
\qquad \zeta_{\rm TM}(z)=1.                                    \tag{5}$$ There are likewise no primitive shift cycles. This is not an absence of recurrence or invariant measures; it is specifically a periodic-orbit vacuum.

# Periodic controls and validation

Circulate $w_k$ to obtain $c_k=w_k^{\infty}$. Its least period is $2^k$. Indeed, a least cyclic period divides $2^k$; any proper divisor also divides $2^{k-1}$ and would make the two halves equal, whereas the second half of $w_k$ complements the first. For a width-$m$ window with $m\leq2^k$, only the $m-1$ seam-crossing starts could be extrinsic, so the invalid rooted fraction is at most $(m-1)/2^k$.

The exact ledger gives a sharper scale contrast. For each width $m$, choose $2^q\geq m$. Equation (2) shows that every intrinsic $m$-factor lies in one of $w_qw_q,w_q\overline w_q,\overline w_qw_q,
\overline w_q\overline w_q$; the pairs $00,01,10,11$ all occur already in $01101001$. This makes the finite language membership tests exhaustive. At levels $2\leq k\leq12$, all 145 audited local cells through width $16$ have zero invalid rooted windows. At levels $2\leq k\leq9$, every rooted window of width $2^{k+1}+1$ is extrinsic. This latter statement is a finite checked control, not an all-$k$ theorem, and neither finite cutoff enters the proof of (5). Equation (5) already shows that no periodic $c_k$ belongs to $X_{\rm TM}$.

The independent checker passes 172,437 assertions, SymPy passes 83 exact checks, isolated production is byte-identical, and all 37 hostile cases (36 repaired-hash plus one stale-hash) are rejected. The strict verdict is $(\texttt{A1\_FAIL},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$, overall `ROUTE_A_REJECTED`. We claim no target divisor, target functional equation or counting law, arithmetic/local factor, root number, automorphy, natural operator lift, Hilbert--Pólya operator, or Route-B authorization. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
