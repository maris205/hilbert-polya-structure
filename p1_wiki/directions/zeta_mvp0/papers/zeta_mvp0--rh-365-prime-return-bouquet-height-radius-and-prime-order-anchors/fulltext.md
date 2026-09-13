---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-365-prime-return-bouquet-height-radius-and-prime-order-anchors"
canonical_tex: "zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/main.pdf"
source_sha256: "cf70fb8a3bb2b9fb4158e75c91426ff07c4f501523cee02bbc7e1a13f1982e1f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime-return bouquet height and analytic radius: midpoint compression and prime-order anchors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-365-prime-return-bouquet-height-radius-and-prime-order-anchors/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the integral Hénon automorphism $H(x,y)=(1-6x^2-y,x)$ and the reversing-axis seed $P_0=(0,0)$, let $r_p$ be the return period of $P_0$ modulo a rational prime $p$. RH-362 attached one complete marked $r_p$-cycle to each prime and obtained a locally finite formal Artin--Mazur product. We prove that this formal object has a nontrivial analytic domain.

  Reversibility compresses every two-coordinate gcd term to one midpoint coordinate difference: $a_{2k}=|x_k-x_{k-1}|$ and $a_{2k+1}=|x_{k+1}-x_{k-1}|$. The escaping negative orbit then satisfies $5b_n^2\le b_{n+1}\le6b_n^2$, which yields explicit two-sided bounds and $\log a_n=\Theta(2^{n/2})$. For the bouquet fixed-point ledger $T_n=\sum_{p:r_p\mid n}r_p$, we obtain the all-order envelope $$T_n\le(\log_2 30)n\,2^{\lceil n/2\rceil-2}.$$ Consequently $\prod_p(1-z^{r_p})^{-1}$ converges normally and is holomorphic and zero-free on $|z|<2^{-1/2}$.

  At every odd prime order $\ell$, the term $a_\ell$ has a primitive prime divisor and $[z^\ell]\log\mathcal Z_0=\omega(a_\ell)\ge1$. This is an Euler-exponent and logarithmic-coefficient anchor, not a raw zeta coefficient: decomposable lower-order cycles already change the coefficient at order seven. Finally, the naive Hilbert direct sum $\bigoplus_p zU_p$ is noncompact and belongs to no finite Schatten class for $z\ne0$; therefore the analytic Euler product is not its ordinary Fredholm determinant.

  The bouquet remains a marked disjoint union across distinct finite fields, not a full finite-field zeta, Hasse--Weil factor, canonical global Hénon operator, or von-Mangoldt trace model. Gates A--E remain false/open, and no Hilbert--Pólya, Riemann-zero, completed-divisor, or RH conclusion is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Prime-return bouquet height and analytic radius:\
  midpoint compression and prime-order anchors
```

## Markdown 正文

# Frozen foundation and exact object

The RH-1--RH-361 foundation remains frozen in four provenance-preserving volumes [@WangRHCorpus2026]. RH-362 opened an independent arithmetic-dynamical branch by assigning one marked modular return cycle to each prime [@WangRH3622026]; RH-364 is the immediate numbered baseline and leaves the original physical route coordinate $$\texttt{actual\_same\_clock\_unnormalized\_head\_transport\_open}
 \label{eq:physical-coordinate}$$ unchanged [@WangRH3642026]. Nothing below estimates that physical same-clock defect, supplies a typed $q/E_{\rm off}$ theorem, or closes the RH-241 moving noisy envelope.

Fix the integral polynomial automorphism $$H(x,y)=(1-6x^2-y,x),
 \qquad
 H^{-1}(u,v)=(v,1-6v^2-u).
 \label{eq:henon-map}$$ Let $$R(x,y)=(y,x).
 \label{eq:reversor}$$ Direct substitution gives $$R^2=\operatorname{id},
 \qquad
 RHR=H^{-1}.
 \label{eq:reversibility}$$ These identities hold over every commutative ring and hence after reduction modulo every positive integer [@WangPrimeReturns2026].

For $P\in\mathbb Z^2$, let $$r_M(P)=\min\{n\ge1:H^n(P)\equiv P\pmod M\},
 \qquad r_1(P)=1,
 \label{eq:return-rank}$$ and, writing $H^n(P)=(x_n,y_n)$, define $$a_n(P)=\gcd(|x_n-x_0|,|y_n-y_0|).
 \label{eq:gcd-sequence-general}$$ The locked source theorem is $$M\mid a_n(P)
 \quad\Longleftrightarrow\quad
 r_M(P)\mid n.
 \label{eq:return-divisibility}$$ It also proves strong divisibility for every nonperiodic integral orbit [@Silverman2007; @WangPrimeReturns2026].

This paper uses only $$P_0=(0,0).
 \label{eq:seed}$$ Set $x_{-1}=x_0=0$ and define $$x_{n+1}=1-6x_n^2-x_{n-1}.
 \label{eq:scalar-recurrence}$$ Then $$H^n(P_0)=(x_n,x_{n-1}),
 \qquad
 a_n:=a_n(P_0)=\gcd(|x_n|,|x_{n-1}|).
 \label{eq:orbit-indexing}$$

# Exact reversibility midpoint compression

The seed lies on the reversing axis: $RP_0=P_0$. Thus $$H^{-k}P_0=RH^kP_0
 \qquad(k\ge0).
 \label{eq:reversed-orbit}$$ This turns a long return into equality of two midpoint states.

[\[thm:midpoint\]]{#thm:midpoint label="thm:midpoint"} For every $k\ge1$, $$a_{2k}=|x_k-x_{k-1}|,
 \label{eq:even-midpoint}$$ and for every $k\ge0$, $$a_{2k+1}=|x_{k+1}-x_{k-1}|.
 \label{eq:odd-midpoint}$$

Fix a positive modulus $M$. Because $H$ is invertible modulo $M$, $$\begin{aligned}
 H^{2k}P_0\equiv P_0\pmod M
 &\Longleftrightarrow
 H^kP_0\equiv H^{-k}P_0\pmod M\\
 &\Longleftrightarrow
 (x_k,x_{k-1})\equiv(x_{k-1},x_k)\pmod M\\
 &\Longleftrightarrow
 M\mid x_k-x_{k-1}.\end{aligned}$$ Together with [\[eq:return-divisibility\]](#eq:return-divisibility){reference-type="eqref" reference="eq:return-divisibility"}, this says that the two nonnegative integers in [\[eq:even-midpoint\]](#eq:even-midpoint){reference-type="eqref" reference="eq:even-midpoint"} have exactly the same positive divisors, hence are equal.

Likewise, $$\begin{aligned}
 H^{2k+1}P_0\equiv P_0\pmod M
 &\Longleftrightarrow
 H^{k+1}P_0\equiv H^{-k}P_0\pmod M\\
 &\Longleftrightarrow
 (x_{k+1},x_k)\equiv(x_{k-1},x_k)\pmod M\\
 &\Longleftrightarrow
 M\mid x_{k+1}-x_{k-1},\end{aligned}$$ which proves [\[eq:odd-midpoint\]](#eq:odd-midpoint){reference-type="eqref" reference="eq:odd-midpoint"}. The convention $x_{-1}=0$ includes $k=0$.

The theorem is specific to the reversing-axis seed $P_0$. It is not a height theorem for every integral point and is not inferred from the finite return-rank tables.

# Quadratic escape and the two-sided height scale

The first scalar values are $$x_0=0,\qquad x_1=1,\qquad x_2=-5,\qquad x_3=-150.
 \label{eq:first-x-values}$$ For $n\ge2$, put $$b_n=-x_n.
 \label{eq:b-definition}$$

[\[thm:height\]]{#thm:height label="thm:height"} The sequence $b_n$ is positive and strictly increasing. It satisfies $$b_2=5,\qquad b_3=150=6b_2^2,
 \label{eq:b-bases}$$ and, for $n\ge3$, $$b_{n+1}=6b_n^2-b_{n-1}-1.
 \label{eq:b-exact}$$ For every $n\ge2$, $$5b_n^2\le b_{n+1}\le6b_n^2.
 \label{eq:b-quadratic}$$ Consequently, $$5^{\,2^{n-1}-1}
 \le b_n\le
 \frac{30^{\,2^{n-2}}}{6}.
 \label{eq:b-closed}$$

The bases follow from [\[eq:scalar-recurrence\]](#eq:scalar-recurrence){reference-type="eqref" reference="eq:scalar-recurrence"}. Suppose $b_n>b_{n-1}\ge5$. Because the variables are integral, $b_{n-1}+1\le b_n$. Equation [\[eq:scalar-recurrence\]](#eq:scalar-recurrence){reference-type="eqref" reference="eq:scalar-recurrence"} gives [\[eq:b-exact\]](#eq:b-exact){reference-type="eqref" reference="eq:b-exact"}, and hence $$b_{n+1}
 \ge6b_n^2-b_n
 >b_n.$$ This proves positivity and strict increase by induction from $(b_2,b_3)=(5,150)$. The upper inequality in [\[eq:b-quadratic\]](#eq:b-quadratic){reference-type="eqref" reference="eq:b-quadratic"} is immediate from [\[eq:b-exact\]](#eq:b-exact){reference-type="eqref" reference="eq:b-exact"}; for the lower inequality, $$b_{n-1}+1\le b_n\le b_n^2$$ gives $b_{n+1}\ge5b_n^2$. The case $n=2$ follows directly from [\[eq:b-bases\]](#eq:b-bases){reference-type="eqref" reference="eq:b-bases"}.

Multiplying the lower recurrence by five gives $5b_{n+1}\ge(5b_n)^2$, and multiplying the upper recurrence by six gives $6b_{n+1}\le(6b_n)^2$. Iterating from $5b_2=25$ and $6b_2=30$ yields [\[eq:b-closed\]](#eq:b-closed){reference-type="eqref" reference="eq:b-closed"}.

Strict increase proves again that the integral orbit of $P_0$ is nonperiodic. In particular every $a_n$ is positive.

[\[thm:gcd-height\]]{#thm:gcd-height label="thm:gcd-height"} The first values are $$a_1=a_2=1,\qquad
 a_3=5,\quad a_4=6,\quad a_5=151.
 \label{eq:a-bases}$$ Let $n\ge6$ and $m=\lceil n/2\rceil$. Then $$\frac{24}{25}b_m\le a_n<b_m.
 \label{eq:a-sharp-comparison}$$ Uniformly for every $n\ge3$, $$4\,5^{\,2^{m-1}-2}
 \le a_n\le
 \frac{30^{\,2^{m-2}}}{5},
 \qquad m=\left\lceil\frac n2\right\rceil.
 \label{eq:a-closed}$$ Thus $$\log a_n=\Theta(2^{n/2}).
 \label{eq:log-height}$$

The bases follow from theorem [\[thm:midpoint\]](#thm:midpoint){reference-type="ref" reference="thm:midpoint"}. If $n=2m\ge6$, then $$a_n=b_m-b_{m-1}.$$ If $n=2m-1\ge7$, then $$a_n=b_m-b_{m-2}.$$ In either case the subtracted term is at most $b_{m-1}$. Since $$b_m\ge5b_{m-1}^2\ge25b_{m-1},$$ equation [\[eq:a-sharp-comparison\]](#eq:a-sharp-comparison){reference-type="eqref" reference="eq:a-sharp-comparison"} follows.

The three special values in [\[eq:a-bases\]](#eq:a-bases){reference-type="eqref" reference="eq:a-bases"}, together with [\[eq:a-sharp-comparison\]](#eq:a-sharp-comparison){reference-type="eqref" reference="eq:a-sharp-comparison"}, give the uniform comparison $$\frac45b_m\le a_n\le\frac65b_m
 \qquad(n\ge3).
 \label{eq:a-uniform-comparison}$$ Combining this with [\[eq:b-closed\]](#eq:b-closed){reference-type="eqref" reference="eq:b-closed"} proves [\[eq:a-closed\]](#eq:a-closed){reference-type="eqref" reference="eq:a-closed"}. Finally $2^{m-1}$ is comparable to $2^{n/2}$, proving [\[eq:log-height\]](#eq:log-height){reference-type="eqref" reference="eq:log-height"}.

# The all-order bouquet trace envelope

For a rational prime $p$, write $r_p=r_p(P_0)$, and let $$\mathcal O_p=\{P_0,H_pP_0,\ldots,H_p^{r_p-1}P_0\}
 \label{eq:marked-cycle}$$ be the complete marked cycle in $\mathbb F_p^2$. Let $U_p$ be its cyclic permutation matrix. Then $$\operatorname{Tr}(U_p^n)=r_p\mathbf 1_{r_p\mid n},
 \qquad
 \det(I-zU_p)=1-z^{r_p}.
 \label{eq:local-cycle}$$

Define the countable marked disjoint union $$\mathcal X_0=\bigsqcup_p\mathcal O_p
 \label{eq:bouquet}$$ and let $F_0$ act on each component as the cyclic restriction of $H_p$: $$F_0|_{\mathcal O_p}=H_p|_{\mathcal O_p}.
 \label{eq:bouquet-map}$$ Define also the rank multiplicities $$c_d=\#\{p:r_p=d\}.
 \label{eq:rank-multiplicity}$$ The return-divisibility theorem implies that $c_d$ is finite for every $d$: every such prime divides the fixed positive integer $a_d$.

[\[thm:trace-envelope\]]{#thm:trace-envelope label="thm:trace-envelope"} For every $n\ge1$, the fixed-point set of the $n$-th bouquet iterate is finite and $$T_n:=\#\operatorname{Fix}(F_0^n)
 =\sum_{p:r_p\mid n}r_p
 =\sum_{d\mid n}d\,c_d
 =\sum_{p\mid a_n}r_p.
 \label{eq:trace-ledger}$$ Moreover $T_1=T_2=0$, and for every $n\ge1$, $$T_n\le
 (\log_2 30)n\,2^{\lceil n/2\rceil-2}.
 \label{eq:trace-envelope}$$

Equation [\[eq:local-cycle\]](#eq:local-cycle){reference-type="eqref" reference="eq:local-cycle"} and finiteness of the set $r_p\le n$ give the first three expressions in [\[eq:trace-ledger\]](#eq:trace-ledger){reference-type="eqref" reference="eq:trace-ledger"}. Equation [\[eq:return-divisibility\]](#eq:return-divisibility){reference-type="eqref" reference="eq:return-divisibility"} gives the last.

If $p\mid a_n$, then $r_p\mid n$, hence $r_p\le n$. Therefore $$T_n\le n\,\omega(a_n),
 \label{eq:T-omega}$$ where $\omega$ counts distinct prime factors. Since $2^{\omega(a_n)}\le\operatorname{rad}(a_n)\le a_n$, $$\omega(a_n)\le\log_2a_n.
 \label{eq:omega-log}$$ For $n\ge3$, theorem [\[thm:gcd-height\]](#thm:gcd-height){reference-type="ref" reference="thm:gcd-height"} gives $$\log_2a_n
 \le2^{\lceil n/2\rceil-2}\log_2 30-\log_2 5,$$ which proves [\[eq:trace-envelope\]](#eq:trace-envelope){reference-type="eqref" reference="eq:trace-envelope"}. The terms $a_1=a_2=1$ give $T_1=T_2=0$, so the same displayed envelope holds at the two base orders.

[\[rem:trace-data-type\]]{#rem:trace-data-type label="rem:trace-data-type"} The term *trace ledger* refers to the finite sum of local cycle traces, or equivalently the bouquet fixed-point count. It is not yet the Hilbert-space trace of a trace-class global operator. Section [7](#sec:naive-operator){reference-type="ref" reference="sec:naive-operator"} proves the precise obstruction.

# A strict zero-free disk

The RH-362 formal Artin--Mazur product is $$\mathcal Z_0(z)
 =\exp\left(\sum_{n\ge1}\frac{T_n}{n}z^n\right)
 =\prod_p(1-z^{r_p})^{-1}.
 \label{eq:formal-zeta}$$ RH-362 asserted this coefficientwise, without a positive analytic radius.

[\[thm:analytic-disk\]]{#thm:analytic-disk label="thm:analytic-disk"} For every $$0\le r<2^{-1/2},
 \label{eq:strict-radius}$$ one has $$\sum_{n\ge1}\frac{T_n}{n}r^n
 \le
 (\log_2 30)\frac{r^3+r^4}{1-2r^2}.
 \label{eq:log-majorant}$$ Consequently the logarithmic series and Euler product in [\[eq:formal-zeta\]](#eq:formal-zeta){reference-type="eqref" reference="eq:formal-zeta"} converge locally normally on $$|z|<2^{-1/2}.
 \label{eq:analytic-disk}$$ They define a holomorphic zero-free function $\mathcal Z_0$ there, and $\mathcal Z_0^{-1}$ is also holomorphic and zero-free.

The base traces vanish. The odd and even parts of [\[eq:trace-envelope\]](#eq:trace-envelope){reference-type="eqref" reference="eq:trace-envelope"} give $$\begin{aligned}
 \sum_{n\ge1}\frac{T_n}{n}r^n
 &\le(\log_2 30)
 \left(
  \sum_{j\ge0}2^jr^{2j+3}
  +\sum_{j\ge0}2^jr^{2j+4}
 \right),\end{aligned}$$ which is [\[eq:log-majorant\]](#eq:log-majorant){reference-type="eqref" reference="eq:log-majorant"}.

For $|z|\le r<2^{-1/2}$, Tonelli's theorem and [\[eq:trace-ledger\]](#eq:trace-ledger){reference-type="eqref" reference="eq:trace-ledger"} give $$\sum_p\sum_{j\ge1}\frac{|z|^{jr_p}}j
 =\sum_{n\ge1}\frac{T_n}{n}|z|^n<\infty.
 \label{eq:tonelli-log}$$ Thus the analytic logarithms $\sum_{j\ge1}z^{jr_p}/j$ sum absolutely and uniformly on compact subdisks. Exponentiating their sum and its negative proves normal convergence and the two zero-free claims.

The inequality is strict at the boundary: the denominator in [\[eq:log-majorant\]](#eq:log-majorant){reference-type="eqref" reference="eq:log-majorant"} vanishes when $r=2^{-1/2}$. No assertion is made there.

[\[cor:radius-bracket\]]{#cor:radius-bracket label="cor:radius-bracket"} Let $R_{\log}$ and $R_{\mathcal Z}$ be the origin Taylor radii of $\log\mathcal Z_0$ and $\mathcal Z_0$, respectively. Then $$2^{-1/2}\le R_{\log}\le1,
 \qquad
 2^{-1/2}\le R_{\mathcal Z}\le1.
 \label{eq:radius-bracket}$$

The lower bounds are theorem [\[thm:analytic-disk\]](#thm:analytic-disk){reference-type="ref" reference="thm:analytic-disk"}. The upper bounds follow from the prime-order anchors in theorem [\[thm:prime-anchors\]](#thm:prime-anchors){reference-type="ref" reference="thm:prime-anchors"}: the logarithmic coefficient is at least one at infinitely many orders, and the coefficients of the Euler product are nonnegative with the raw coefficient at least the primitive contribution.

This is a bracket for the origin power-series radii. It is not an exact radius, a meromorphic-continuation theorem, or a natural-boundary theorem.

# Odd-prime primitive anchors and the raw-coefficient firewall

A prime $p$ is a primitive prime divisor of $a_n$ when $p\mid a_n$ and $p\nmid a_m$ for every $1\le m<n$.

[\[thm:prime-anchors\]]{#thm:prime-anchors label="thm:prime-anchors"} Let $\ell$ be an odd rational prime. Then $a_\ell>1$, and $$\{p:p\mid a_\ell\}
 =\{p:r_p=\ell\}.
 \label{eq:prime-anchor-set}$$ Every distinct prime divisor of $a_\ell$ is primitive. In particular, $$c_\ell=\omega(a_\ell)\ge1,
 \qquad
 T_\ell=\ell c_\ell,
 \qquad
 [z^\ell]\log\mathcal Z_0(z)=c_\ell.
 \label{eq:prime-anchor-ledger}$$ The number of primitive bouquet cycles of length $\ell$ is exactly $c_\ell$.

The lower bound in theorem [\[thm:gcd-height\]](#thm:gcd-height){reference-type="ref" reference="thm:gcd-height"} gives $a_\ell\ge4$, so $a_\ell$ has a prime divisor. Equation [\[eq:return-divisibility\]](#eq:return-divisibility){reference-type="eqref" reference="eq:return-divisibility"} gives $$p\mid a_\ell
 \quad\Longleftrightarrow\quad
 r_p\mid\ell.$$ No prime has $r_p=1$, because that would imply $p\mid a_1=1$. Since $\ell$ is prime, the only remaining divisor is $r_p=\ell$, proving [\[eq:prime-anchor-set\]](#eq:prime-anchor-set){reference-type="eqref" reference="eq:prime-anchor-set"}. If such a $p$ divided $a_m$ for some $m<\ell$, then $\ell=r_p\mid m$, a contradiction. The first two identities in [\[eq:prime-anchor-ledger\]](#eq:prime-anchor-ledger){reference-type="eqref" reference="eq:prime-anchor-ledger"} follow.

Finally, $$[z^\ell]\log\mathcal Z_0=\frac{T_\ell}{\ell}=c_\ell.$$ Equivalently, Möbius inversion of the fixed-point ledger gives primitive cycle count $(T_\ell-T_1)/\ell=c_\ell$.

The theorem does not assert that $a_\ell$ is squarefree. The symbol $\omega$ counts distinct factors, not factors with multiplicity. It also does not imply a primitive divisor at any composite order.

[\[prop:raw-firewall\]]{#prop:raw-firewall label="prop:raw-firewall"} Write $$\mathcal Z_0(z)=\sum_{n\ge0}q_nz^n.
 \label{eq:raw-coefficients}$$ Then $$nq_n=\sum_{k=1}^nT_kq_{n-k},
 \qquad q_0=1.
 \label{eq:zeta-recurrence}$$ The exact finite ledger begins $$(q_0,\ldots,q_7)=(1,0,0,1,2,1,2,3).
 \label{eq:first-zeta-coefficients}$$ At the prime order seven, $$c_7=1,
 \qquad
 [z^7]\log\mathcal Z_0=1,
 \qquad
 [z^7]\mathcal Z_0=3.
 \label{eq:order-seven-firewall}$$

Differentiating [\[eq:formal-zeta\]](#eq:formal-zeta){reference-type="eqref" reference="eq:formal-zeta"} and comparing coefficients gives [\[eq:zeta-recurrence\]](#eq:zeta-recurrence){reference-type="eqref" reference="eq:zeta-recurrence"}. The midpoint identities give $$a_3=5,\qquad a_4=6,\qquad a_7=134989.$$ Direct exact factorization gives rank multiplicities $c_3=1,c_4=2,c_7=1$; the artifact independently checks the return ranks and the primality of $134989$. Thus $$(T_1,\ldots,T_7)=(0,0,3,8,5,9,7).$$ Substitution in [\[eq:zeta-recurrence\]](#eq:zeta-recurrence){reference-type="eqref" reference="eq:zeta-recurrence"} proves [\[eq:first-zeta-coefficients\]](#eq:first-zeta-coefficients){reference-type="eqref" reference="eq:first-zeta-coefficients"} and [\[eq:order-seven-firewall\]](#eq:order-seven-firewall){reference-type="eqref" reference="eq:order-seven-firewall"}. The two extra order-seven contributions are decomposable products of one length-three and one of the two length-four cycles.

# Naive direct-sum obstruction {#sec:naive-operator}

Let $$\mathcal H_0=\bigoplus_p\mathbb C^{r_p},
 \qquad
 U=\bigoplus_pU_p,
 \qquad
 B_z=zU.
 \label{eq:naive-operator}$$ The operator $U$ is unitary. Formally, its finite blocks have the local determinants used in [\[eq:formal-zeta\]](#eq:formal-zeta){reference-type="eqref" reference="eq:formal-zeta"}. Ordinary Fredholm determinants, however, require trace-ideal hypotheses [@Simon2005].

[\[thm:noncompact\]]{#thm:noncompact label="thm:noncompact"} For every $z\ne0$, the operator $B_z$ is noncompact and belongs to no finite Schatten class $S_q$. For every $n\ge1$, $U^n$ is not trace class, so $T_n$ is not its Hilbert-space trace. Consequently $\mathcal Z_0^{-1}$ is not the ordinary Fredholm determinant $\det_F(I-B_z)$ of this naive direct sum.

For $|z|<1$, the operator $I-B_z$ is nevertheless invertible. Noncompactness is not a non-Fredholmness statement.

Choose one unit vector $e_p$ in each prime block. The vectors $B_ze_p$ are mutually orthogonal and all have norm $|z|$. They therefore have no convergent subsequence when $z\ne0$, proving noncompactness.

Every singular value of $U_p$ is one. Hence the partial $S_q$ burden of $B_z$ over any finite prime set $S$ is $$|z|^q\sum_{p\in S}r_p.
 \label{eq:partial-schatten}$$ This diverges as $S$ exhausts the primes, so no finite $S_q$ membership holds. The same observation with $z=1$ shows that every $U^n$ has infinitely many singular values equal to one and is not trace class. Thus the finite block sum in [\[eq:trace-ledger\]](#eq:trace-ledger){reference-type="eqref" reference="eq:trace-ledger"} is a fixed-point ledger, not a global operator trace.

Finally, if $|z|<1$, then $\|B_z\|=|z|<1$, so the Neumann series $\sum_{j\ge0}B_z^j$ inverts $I-B_z$.

This theorem excludes only the naive constant-weight cycle direct sum. It is not a nonexistence theorem for every compact realization of the same scalar germ.

# Route verdicts and Gate ledger

  Route     Exact verdict
  --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route A   **GO.** Reversibility supplies exact midpoint compression; escape gives the two-sided height scale; the resulting all-order fixed-point envelope produces a strict zero-free disk and infinitely many prime-order primitive anchors. The direct-sum theorem supplies a rigorous scoped operator negative.
  Route B   **STOP\_SCOPED.** The first fatal mismatch is Gate A data type: one marked cycle is selected from each of distinct finite-field maps, so the bouquet is not a canonical intrinsic global Hénon operator. Its fixed-point counts are also not signed von-Mangoldt traces of one trace-class operator.

The following boundaries are mandatory.

1.  The bouquet is not the zeta function of the full map $H_p:\mathbb F_p^2\to\mathbb F_p^2$, and is not a Hasse--Weil local factor.

2.  The certified disk is a lower bound for the origin analytic radius. No exact radius, continuation across its boundary, or natural boundary is proved.

3.  The odd-prime theorem gives primitive divisors only at odd prime orders. It does not give an eventual composite-order Zsigmondy theorem or squarefreeness.

4.  The exact anchor is $c_\ell$ in the Euler exponent, primitive-cycle ledger, and logarithmic coefficient. The raw coefficient $q_\ell$ can be larger.

5.  The global operator $U$ is noncompact; the locally finite block trace ledger is not a Hilbert-space trace.

Thus:

  Gate   Status       First missing object
  ------ ------------ -------------------------------------------------
  A      false/open   canonical intrinsic global physical determinant
  B      false/open   time-oriented scattering or unitary completion
  C      false/open   self-adjoint generator and intrinsic $T\log T$
  D      false/open   signed von-Mangoldt prime-power operator trace
  E      false/open   completed-zeta divisor equality

No Hilbert--Pólya operator, self-adjoint generator, Riemann-zero spectral identification, completed-zeta divisor equality, or proof of the Riemann Hypothesis follows.

# Executable protocol

The publication artifact performs finite exact reproduction and provenance checks only:

1.  it hashes the locked reversibility, divisibility, finite diagnostic, RH-362, RH-364, and four-volume inputs;

2.  it checks the exact midpoint identities through order twelve and an extended test through order sixteen;

3.  it checks the quadratic height step and both closed bounds;

4.  it factors $a_1,\ldots,a_{12}$, verifies each factor's first modular return, and reconstructs $c_n$, $T_n$, and $q_n$;

5.  it checks the prime-order anchors at orders $3,5,7,11$, including the raw-coefficient mismatch at orders seven and eleven;

6.  it validates the strict analytic-majorant domain, result schema, fixed-member archive, five Gate values, and fifteen forbidden macro claims.

The finite factor rows are not evidence for an all-large-order primitive divisor law. The all-order conclusions are the analytic theorems proved in sections 2--6.

# Conclusion

The marked return bouquet has more structure than its original formal definition suggested. Reversibility halves the orbit depth of the gcd problem, and the escaping midpoint height pays an explicit all-order fixed-point budget. This produces a genuine zero-free analytic germ without inserting prime weights or changing local clocks.

The same argument also exposes the boundary. Prime order forces new divisors because the only possible earlier rank is one, but composite order does not. The scalar Euler product converges even though the most immediate global cycle operator is noncompact. The shortest new arithmetic problem is therefore a genuine composite-order primitive-divisor theorem; the shortest operator problem is an intrinsic compact globalization rather than another marked direct sum. The original physical same-clock route remains open and unchanged.
