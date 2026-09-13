---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-physical-tail-galois-parity-obstruction"
canonical_tex: "henon_dynamics/henon_physical_tail_galois_parity_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_physical_tail_galois_parity_obstruction/paper/paper.pdf"
source_sha256: "8f1e43d170bd1d842b15bf9f66c814c91fc4a444c700150ce7fdecbf55396720"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Physical Stable Tails Do Not Control Hénon Galois Excess: Exact Period-Eight and Period-Nine Parity Falsifiers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_physical_tail_galois_parity_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_physical_tail_galois_parity_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_physical_tail_galois_parity_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_physical_tail_galois_parity_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_physical_tail_galois_parity_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove that stable linearization at one physical Hénon orbit does not control the all-conjugate Galois excess assigned to that orbit. The distinction matters because a natural continuation of a finite-memory obstruction ladder is to estimate its discrepancies from the negative fixed point approached by the physical reflection chains. We derive instead the complete reflection-reduced trace algebra at periods eight and nine. The period-eight vertex--vertex and edge--edge closures produce irreducible totally real trace fields of degrees $12$ and $6$; the period-nine vertex--edge closure produces one irreducible totally real degree-$28$ field whose extreme real embeddings are the two physical cycles. Rational root boxes, modular irreducibility and Sturm counts make these statements exact. Integer-product bounds then certify two consecutive incidence discrepancies, $$\Delta_6=-185.5524168765\ldots<0,
  \qquad
  \Delta_7=300.0665139420\ldots>0.$$ The selected physical tail is exponentially localized by a positive stable multiplier, but the Galois excess sums every nonphysical embedding. Hence a physical-tail theorem supplies no bound for the target without a separate, uniform reflection-ensemble count or pressure theorem. The result is an interface obstruction, not an eventual sign law or a Hilbert--Pólya construction.
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
  Physical Stable Tails Do Not Control Hénon Galois Excess:\
  Exact Period-Eight and Period-Nine Parity Falsifiers
```

## Markdown 正文

# Introduction

Local hyperbolic data often predicts how a chosen periodic orbit approaches a fixed point. It need not predict a height that sums the behavior of every algebraic conjugate of that orbit. This paper isolates that mismatch in a frozen area-preserving Hénon system.

The preceding incidence-ladder construction assigns to each primitive cycle $\gamma$ a Galois excess $\mathcal E(\gamma)$: the sum of the instability lengths over all nonphysical real embeddings of its trace field. Width-five block incidence already obstructs a locally constant realization of this assignment. The remaining natural idea is asymptotic. Two reflection families approach the negative fixed point, so one might try to estimate the ladder discrepancy from the stable eigenvalue there. The obstacle appears before any delicate asymptotics: the proposed estimate and the target use different sets of embeddings.

Our contributions are concrete.

1.  We derive the three parity-dependent reflection closures needed at periods eight and nine and eliminate them to trace fields of degrees $12,6,28$.

2.  We prove modular irreducibility and total reality, then identify four physical embeddings using rational coordinate boxes and trace monotonicity.

3.  We certify $\Delta_6<0<\Delta_7$ by integer products, independent of floating-point sign decisions.

4.  We prove an interface theorem: exponential localization of the selected physical tail does not compile an all-conjugate Galois-height estimate.

The theorem is deliberately narrower than a Hölder obstruction. A finite sequence of alternating signs proves no infinite sign law, and no prime or zero data enter the construction. The relevant background is the standard periodic-orbit and symbolic framework for hyperbolic dynamics [@Bowen1975; @ParryPollicott1990] and the cohomological role of periodic sums [@Livshits1972]; the exact trace fields below are new computations inside the frozen research programme.

Section 2 fixes the object and normalization. Sections 3--5 derive the trace fields, physical tail and exact signs. Section 6 states the interface obstruction and the next theorem obligation.

# Frozen system and Galois excess

We study the area-preserving map $$H_6(q,p)=(1-6q^2-p,q).
\label{eq:henon}$$ Its periodic coordinate chains satisfy $$q_{j+1}=1-6q_j^2-q_{j-1},
\qquad
D(q_j)=\begin{pmatrix}-12q_j&-1\\1&0\end{pmatrix}.
\label{eq:recurrence}$$ The symbolic survivor, chronological convention and primitive families are fixed by the predecessor packages; no parameters are refitted here.

For a physical primitive cycle $\gamma$, let $F_\gamma(T)$ denote its irreducible trace factor. Every real root $\tau$ with $|\tau|>2$ carries the instability length $$\ell(\tau)=\operatorname{arcosh}(|\tau|/2).$$ If $\tau_\gamma$ is the physical trace embedding, the frozen excess is $$\mathcal E(\gamma)
=\sum_{F_\gamma(\tau)=0}\ell(\tau)-\ell(\tau_\gamma).
\label{eq:excess}$$ Thus $\mathcal E$ is not the local Lyapunov exponent of $\gamma$. It is a field-wide sum with one physical term removed.

The two symbolic families are denoted $A_m$ and $B_m$. Their all-width incidence identity yields the discrepancy $$\Delta_m=\mathcal E(A_m)+\mathcal E(B_{m+2})
-\mathcal E(A_{m+1})-\mathcal E(B_{m+1}).
\label{eq:delta}$$ Earlier exact work proved $\Delta_5>0$. We compute $\Delta_6$ and $\Delta_7$ and ask whether fixed-point linearization explains them.

# Parity-dependent reflection trace fields

Reflection symmetry reduces each closure to one coordinate. For a vertex-axis chain put $$q_0=a,\qquad q_1=(1-6a^2)/2,$$ and iterate [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. For an edge-axis chain replace the second value by $q_1=1-6a^2-a$.

[\[thm:fields\]]{#thm:fields label="thm:fields"} The following primitive reflection closures have irreducible, totally real trace factors:

  cycle       boundary type    coordinate degree   trace degree   resultant mult.
  ----------- ---------------- ------------------- -------------- -----------------
  $A_8$       vertex--vertex   24                  12             2
  $B_8$       edge--edge       12                  6              2
  $A_9,B_9$   vertex--edge     28                  28             1

The period-nine physical cycles are two embeddings of the same degree-$28$ field.

The coordinate patterns are $$(a,b,c,d,e,d,c,b),\quad
(a,a,b,c,d,d,c,b),\quad
(a,b,c,d,e,e,d,c,b).$$ The closing equations are $$1-6e^2-2d=0,\quad
1-6d^2-c-d=0,\quad
1-6e^2-d-e=0.$$ Factoring selects unique primitive factors of degrees $24,12,28$. We multiply the matrices in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}, reduce the trace modulo each coordinate factor and eliminate $a$. The resulting trace factors are irreducible modulo $7,53,71$. Locked disjoint integer intervals each contain one root by Sturm's theorem and their counts equal the corresponding degrees. Hence every root is real and each trace factor is irreducible over $\mathbb Q$. The full coefficient and interval ledgers are machine readable in the certificate.

The physical roots are not selected by magnitude after the computation. Rational coordinate boxes certify the symbolic sign itinerary, contain one coordinate root and contain no critical point of the reduced trace map. They map into the trace intervals shown in Table [1](#tab:physical){reference-type="ref" reference="tab:physical"}.

::: {#tab:physical}
  cycle   coordinate box (denominator $10^{12}$)   trace interval
  ------- ---------------------------------------- -------------------------
  $A_8$   $(551939742238,551939742239)$            $(-2793061,-2793060)$
  $B_8$   $(-603835740359,-603835740358)$          $(1652592,1652593)$
  $A_9$   $(551940301478,551940301479)$            $(-19975348,-19975347)$
  $B_9$   $(-606695536138,-606695536137)$          $(11819577,11819578)$

  : Certified physical trace embeddings. The period-nine entries are the first and last roots of one common trace factor.
:::

# What the physical stable tail controls

The negative fixed point of [\[eq:henon\]](#eq:henon){reference-type="eqref" reference="eq:henon"} is $$q_-=-(1+\sqrt7)/6.$$ The derivative there has trace $2+2\sqrt7$. Its expanding and contracting eigenvalues are reciprocal, and the contracting eigenvalue is $$\lambda_s=
\left(1+\sqrt7+\sqrt{7+2\sqrt7}\right)^{-1}
=0.1398273783\ldots.$$ In particular, $$0<\lambda_s<\frac{2}{\sqrt{17}}<1.
\label{eq:contraction}$$ The signed inverse branches used by the reflection chains therefore localize the selected physical coordinates exponentially near $q_-$.

Equation [\[eq:contraction\]](#eq:contraction){reference-type="eqref" reference="eq:contraction"} is useful but has a strict scope. It follows one real branch and controls the local correction to its physical trace. By contrast, [\[eq:excess\]](#eq:excess){reference-type="eqref" reference="eq:excess"} requires every nonphysical root of a trace polynomial whose degree grows with the closure. A local stable eigenvalue does not bound either the number of those roots or their instability lengths. The degree split $12+6$ at period eight and the degree-$28$ merger at period nine make this missing input visible before taking any limit.

# Two exact parity falsifiers

The diagnostic Galois excesses come from high-precision real roots, but their signs do not. For $u>2$, $$\log(u-1)<\operatorname{arcosh}(u/2)<\log u.
\label{eq:logbound}$$ Every nonphysical absolute trace lies in a locked integer interval. Taking the lower factor $u-1$ for terms on one side of a discrepancy and the upper factor $u$ for the other converts each comparison into an integer product.

[\[thm:signs\]]{#thm:signs label="thm:signs"} For the frozen Galois excess [\[eq:excess\]](#eq:excess){reference-type="eqref" reference="eq:excess"}, $$\begin{aligned}
\Delta_6
&=\mathcal E(A_6)+\mathcal E(B_8)-\mathcal E(A_7)-\mathcal E(B_7)<0,\\
\Delta_7
&=\mathcal E(A_7)+\mathcal E(B_9)-\mathcal E(A_8)-\mathcal E(B_8)>0.\end{aligned}$$ Numerically, $$\Delta_6=-185.5524168765298761\ldots,
\qquad
\Delta_7=300.0665139419694939\ldots.$$

For $\Delta_6$, multiply the lower factors from the thirteen nonphysical roots of each period-seven extreme embedding. The product exceeds the upper product formed from the two nonphysical $A_6$ roots and five nonphysical $B_8$ roots. Taking logarithms and applying [\[eq:logbound\]](#eq:logbound){reference-type="eqref" reference="eq:logbound"} gives the negative sign. For $\Delta_7$, the lower product from the thirteen nonphysical $A_7$ roots and twenty-seven nonphysical $B_9$ roots exceeds the upper product from the eleven nonphysical $A_8$ roots and five nonphysical $B_8$ roots. The full integers and positive margins are retained in the primary and independent certificates.

The observed signs $\Delta_4,\ldots,\Delta_7$ alternate. We record this as a finite diagnostic only. Neither Theorem [\[thm:signs\]](#thm:signs){reference-type="ref" reference="thm:signs"} nor the fixed-point linearization proves eventual alternation.

# The physical/Galois interface obstruction

[\[thm:interface\]]{#thm:interface label="thm:interface"} The stable-tail estimate obtained from the negative fixed point controls the selected physical embedding of a reflection closure. It supplies no estimate for its Galois excess without an additional theorem controlling the complete nonphysical reflection ensemble. In particular, fixed-point linearization alone cannot imply an asymptotic bound for $\Delta_m$.

The input of the stable-tail estimate is a chosen inverse branch converging to $q_-$; its output is a correction to one physical coordinate and trace. The target $\mathcal E$ in [\[eq:excess\]](#eq:excess){reference-type="eqref" reference="eq:excess"} is the sum over all other roots of an irreducible trace polynomial. Theorem [\[thm:fields\]](#thm:fields){reference-type="ref" reference="thm:fields"} shows that the number and organization of these roots are not determined by the one physical branch: the two period-eight boundary types have different field degrees, while the two period-nine physical cycles occupy one shared field. No map from the one physical correction to the unobserved conjugate sum has been defined or proved. The missing map is therefore an independent hypothesis, not a consequence of local linearization.

The narrow replacement is a symmetry-resolved ensemble theorem. It must separate vertex--vertex, edge--edge and vertex--edge closures; subtract imprimitive factors; account for reflection-axis resultant multiplicity; and control the summed instability of the surviving trace embeddings uniformly in the period. Only after that theorem would pressure or Hölder estimates address the original asymptotic gate.

The result does not rule out an unrestricted Hölder potential. Nor does it construct a full Galois-weighted determinant. The inherited physical suspension zeta remains a valid subsystem object in the classical periodic-orbit framework [@ParryPollicott1990]; the obstruction concerns the attempted promotion from that subsystem to an all-conjugate amplitude.

# Reproducibility and hostile controls

The primary checker starts from the recurrence, selects primitive coordinate factors, recomputes resultants, verifies three modular irreducibility certificates and runs Sturm counts on every trace interval. It also checks four rational physical boxes, two exact integer products, six predecessor hashes and twenty-one claim mutations.

An independent program does not import the primary checker. It reconstructs the chains, factors, resultants, root counts and product inequalities, then compares a small common schema with the primary JSON certificate. Unit tests lock field degrees, total reality, physical indices, both signs and the Route A/B claim firewall. No target prime table, Riemann-zero table or fitted asymptotic law is used. The full command is

    bash code/run_c58.sh

The computations are exact except for decimal values printed as diagnostics.

# Conclusion

Periods eight and nine resolve the proposed stable-tail shortcut. Exact reflection algebra gives totally real trace fields of degrees $12$, $6$ and $28$, and integer comparisons certify two large discrepancies of opposite sign. Meanwhile the physical chain already contracts exponentially toward the negative fixed point. The coexistence of these facts identifies the missing data: local physical control is not all-conjugate height control.

The next useful problem is therefore combinatorial and thermodynamic rather than another isolated trace calculation. A parity-sensitive primitive reflection-ensemble theorem must first count the relevant factors and encode their summed instability. Eventual discrepancy bounds, unrestricted Hölder conclusions and any full dynamical determinant remain open. No arithmetic or Hilbert--Pólya claim follows from the present finite algebra.

# Exact certificate ledger

The trace coefficient-list SHA256 locks are

  ------- --------------------------------------------------------------------
  $A_8$   `c10a3536d0781bdbbfbb320d48441a97583af9cd18517991c76e71813936c8ab`
  $B_8$   `49e0a21377ff47f504fa00d85f8ed3cee17d70d0677085bdc52e4203f4ac77fd`
  $P_9$   `f52d222e2934061dc367950e3e98e56d4fb9e0e6bd95c7b383fec9061bd7ac3b`
  ------- --------------------------------------------------------------------

The $B_8$ trace polynomial, short enough to display, is $$\begin{aligned}
T^6&-2989740T^5+2576730072444T^4-637680391150733728T^3\\
&+52578572138849284508400T^2\\
&-1614475742627002932794479296T\\
&+16250878441395515982955290707008.\end{aligned}$$ The longer $A_8$ and $P_9$ coefficient lists, all $46$ isolating intervals, physical sign boxes, exact products and mutation trace are stored in `results/c58_certificate.json`. The independent certificate is `results/c58_independent_check.json`.
