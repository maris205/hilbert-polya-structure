---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--102-cyclic-group-algebra-involution-norm-dynamics"
canonical_tex: "symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/main.pdf"
source_sha256: "ade314e84deef4d4bf7b08baf23d93312dae8b64d7cf857f8bc4c5db16b5d500"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Involutive Norm Dynamics in Split Cyclic Group Algebras: Fixed Sequences, Sharp Depth, and Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/102-cyclic-group-algebra-involution-norm-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $n\mid(q-1)$ and let inversion on the cyclic group $C_n$ induce the canonical involution $*$ of the split group algebra $\mathcal A_{q,n}=\mathbb F_q[C_n]$. We determine the complete finite dynamics of the nonlinear norm map $T(a)=aa^*$. Character inversion partitions the Fourier coordinates into self-inverse blocks $z\mapsto z^2$ and paired blocks $(u,v)\mapsto(uv,uv)$. If $s=\gcd(n,2)$ and $o=(n+s)/2$, then $$\#\operatorname{Fix}(T^k)=\bigl(1+\gcd(2^k-1,q-1)\bigr)^o$$ for every $k\geq1$. Writing $q-1=2^\alpha m$ with $m$ odd, the recurrent core has size $(m+1)^o$, while the maximum transient depth is exactly $\alpha+\mathbf1_{\{n>s\}}$. Möbius inversion gives every cycle and a finite product for the Artin--Mazur zeta function. Finally, phase-space size, the fixed sequence, and maximum depth recover $(q,n)$, including the ambiguous two-orbit branch. Literal cyclic convolution over prime fields and explicit models of $\mathbb F_4$ and $\mathbb F_{16}$ independently check the formulas.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Involutive Norm Dynamics in Split Cyclic Group Algebras: Fixed Sequences, Sharp Depth, and Rigidity'
```

## Markdown 正文

# Introduction and ownership boundary

Let $q=p^h$ be a prime power, let $n\geq1$ divide $q-1$, and choose a generator $g$ of $C_n$. On $$\mathcal A_{q,n}=\mathbb F_q[C_n]
   =\left\{\sum_{r=0}^{n-1}a_rg^r:a_r\in\mathbb F_q\right\}$$ consider the canonical inversion involution $$\left(\sum_{r=0}^{n-1}a_rg^r\right)^*
   =\sum_{r=0}^{n-1}a_rg^{-r}$$ and the self-map $$\label{eq:T}
 T\colon\mathcal A_{q,n}\longrightarrow\mathcal A_{q,n},\qquad T(a)=aa^*.$$ The phase space has $q^n$ elements. The assumption $n\mid(q-1)$ is kept throughout: it makes the cyclic algebra split over the stated ground field and excludes modular nilpotents from $x^n-1$.

Group-algebra involutions and their symmetric and unitary units are classical; see, for example, @BovdiGrishkov2019. Finite Fourier decomposition is standard [@Terras1999], and scalar power-map functional graphs over finite fields have an established literature [@VasigaShallit2004; @QureshiReis2023]. We assign those ingredients no novelty credit. Our bounded target is their conjunction for the map [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} on the *whole* group algebra, including zero divisors: the paired-coordinate synchronization, all fixed and cycle counts, the sharp transient depth, and a recovery statement. A targeted source search completed on 29 August 2026 did not locate this exact package, but that database- and query-bounded observation is not a priority or novelty claim. External circulation remains on **HOLD** pending a specialist review.

There are two proof routes. A coefficient-free involution calculation first collapses every orbit to ordinary powering inside the symmetric algebra. Fourier idempotents then expose independent inversion-orbit blocks and make the census exact. The computational control reverses this order: it starts from literal coefficient convolution and cyclic reversal, then compares the result with the Fourier and arithmetic predictions.

# One-step collapse and Fourier blocks

Write $$\mathcal A_{q,n}^+=\{b\in\mathcal A_{q,n}:b^*=b\}.$$ The first route requires neither a primitive root nor a choice of coordinates.

[\[prop:collapse\]]{#prop:collapse label="prop:collapse"} For every $a\in\mathcal A_{q,n}$, $$T(a)\in\mathcal A_{q,n}^+,
 \qquad
 T^k(a)=(aa^*)^{2^{k-1}}\quad(k\geq1).$$ Moreover $T(b)=b^2$ for every $b\in\mathcal A_{q,n}^+$.

The cyclic group algebra is commutative, so $(aa^*)^*=a^*a=aa^*$. Thus $T(a)$ is symmetric. If $b=b^*$, then $T(b)=bb^*=b^2$. Starting with $b=aa^*$ and iterating squaring proves the displayed formula.

For the second route, choose a primitive $n$th root $\omega\in\mathbb F_q$. The Fourier transform $$\widehat{a}(j)=\sum_{r=0}^{n-1}a_r\omega^{jr},\qquad j\in\mathbb Z/n\mathbb Z,$$ is an algebra isomorphism from $\mathcal A_{q,n}$ to $\mathbb F_q^n$. Indeed, $p\nmid n$ and the usual Fourier matrix is invertible. Multiplication becomes coordinatewise, while $$\widehat{a^*}(j)=\widehat{a}(-j).$$ Let $$\label{eq:so}
 s=\gcd(n,2),\qquad o=\frac{n+s}{2}.$$ Here $s$ is the number of self-inverse characters and $o$ is the number of orbits of $j\mapsto-j$.

[\[thm:normal\]]{#thm:normal label="thm:normal"} Under the Fourier isomorphism, a self-inverse character carries the block $$z\longmapsto z^2,$$ whereas a two-element orbit $\{j,-j\}$ carries $$(u,v)\longmapsto(uv,uv).$$ In particular, for every $k\geq1$ and every $j$, $$\label{eq:iterate}
 \widehat{T^k(a)}(j)
 =\bigl(\widehat{a}(j)\widehat{a}(-j)\bigr)^{2^{k-1}}.$$ The fixed algebra $\mathcal A_{q,n}^+$ is isomorphic, as an algebra, to $\mathbb F_q^o$.

Coordinatewise multiplication gives $$\widehat{T(a)}(j)=\widehat{a}(j)\widehat{a}(-j).$$ If $j=-j$, this is $z^2$. Otherwise the two output coordinates coincide, giving the paired block. After the first step both kinds of blocks square, which proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}. Finally, $a=a^*$ is equivalent to $\widehat{a}(j)=\widehat{a}(-j)$ on every inversion orbit; choosing one common coordinate on each orbit identifies the fixed algebra with $\mathbb F_q^o$.

The paired block exhibits the first qualitative anomaly: two independent input coordinates synchronize in one step and never separate. This is the only source of an extra transient level beyond scalar squaring.

# Fixed points and the complete recurrent census

For $k\geq1$, put $$\label{eq:Lk}
 L_k=1+\gcd(2^k-1,q-1).$$

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} For every $k\geq1$, $$\label{eq:fixed}
 F_k:=\#\operatorname{Fix}(T^k)=L_k^o
 =\bigl(1+\gcd(2^k-1,q-1)\bigr)^o.$$ Equivalently, $T^k(a)=a$ precisely when $a\in\mathcal A_{q,n}^+$ and each of its $o$ symmetric Fourier coordinates satisfies $z^{2^k}=z$.

In a paired block, fixedness under the $k$th iterate and [\[eq:iterate\]](#eq:iterate){reference-type="ref" reference="eq:iterate"} force $$u=v=(uv)^{2^{k-1}}.$$ Writing the common value as $z$ reduces the condition to $z^{2^k}=z$. The same equation holds on a self-inverse block. It has the root $0$ and exactly $\gcd(2^k-1,q-1)$ roots in the cyclic group $\mathbb F_q^\times$. The $o$ inversion orbits are independent, proving [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. The equivalent description also follows directly from [\[prop:collapse\]](#prop:collapse){reference-type="ref" reference="prop:collapse"}: a fixed point of $T^k$ lies in the first image and hence is symmetric, where $T^k$ is $2^k$th powering.

Write $$\label{eq:decomp}
 q-1=2^\alpha m,\qquad m\ \text{odd},$$ and let $\mu_m\leq\mathbb F_q^\times$ be the subgroup of order $m$. Set $$R_q=\{0\}\cup\mu_m.$$ For a point $x$ in a finite dynamical system, define $\operatorname{depth}(x)=\min\{r\geq0:T^r(x)\text{ is periodic}\}$, and let $D$ be the maximum of this depth over the phase space.

[\[thm:depth\]]{#thm:depth label="thm:depth"} The recurrent set is, in symmetric Fourier coordinates, $$\label{eq:recset}
 \operatorname{Rec}(T)=R_q^o\subseteq\mathcal A_{q,n}^+.$$ Consequently $$\label{eq:recsize}
 \#\operatorname{Rec}(T)=(m+1)^o.$$ The maximum transient depth is $$\label{eq:depth}
 D=\alpha+\mathbf1_{\{n>s\}}.$$ Both bounds are attained, including the cases $n=1,2$ and characteristic two.

For $z\neq0$, write $\operatorname{ord}(z)=2^u d$ with $d$ odd. Repeated squaring removes one factor of $2$ from the order at each step until $u=0$. Thus $z$ is periodic under squaring if and only if $z\in\mu_m$; zero is fixed. Its scalar depth is $u$, whose maximum is $\alpha$, attained by a primitive element of $\mathbb F_q^\times$.

A periodic paired block must already be in the image of its update, hence must be diagonal. On the diagonal it is scalar squaring, so its recurrent points are exactly $(z,z)$ with $z\in R_q$. This proves [\[eq:recset\]](#eq:recset){reference-type="eqref" reference="eq:recset"} and [\[eq:recsize\]](#eq:recsize){reference-type="eqref" reference="eq:recsize"}.

Every self-inverse block reaches its recurrent part in at most $\alpha$ steps. Every paired block becomes diagonal after one step and then needs at most $\alpha$ further squarings. Hence the right side of [\[eq:depth\]](#eq:depth){reference-type="eqref" reference="eq:depth"} is an upper bound. More precisely, if $d_q(z)$ denotes scalar depth under $z\mapsto z^2$, then a self block $z$ has depth $d_q(z)$, while a paired block $(u,v)$ has depth $$\operatorname{depth}(u,v)=
 \begin{cases}
  d_q(u),&u=v,\\
  1+d_q(uv),&u\ne v.
 \end{cases}$$ Indeed, diagonal pairs already follow scalar squaring, whereas a nondiagonal pair cannot be periodic and first synchronizes to $(uv,uv)$. Thus the extra level belongs only to genuinely nondiagonal pairs. If no paired orbit exists, then $n=s$, equivalently $n\in\{1,2\}$, and a primitive scalar coordinate attains depth $\alpha$. If a pair exists, put $(1,\gamma)$ on that block for a primitive $\gamma\in\mathbb F_q^\times$ and put recurrent values on the other blocks. The first step gives $(\gamma,\gamma)$, which still has scalar depth $\alpha$; the total depth is $\alpha+1$. When $q$ has characteristic two, $\alpha=0$; a pair can occur only when $n\geq3$, and the same construction attains the remaining one synchronization step.

# Cycles and the Artin--Mazur zeta function

Let $P_k$ be the number of points of least period $k$ and $C_k=P_k/k$ the number of $k$-cycles. Let $\mu$ denote the Möbius function.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For every $k\geq1$, $$\begin{aligned}
 P_k&=\sum_{d\mid k}\mu(k/d)
       \bigl(1+\gcd(2^d-1,q-1)\bigr)^o,                         \label{eq:Pk}\\
 C_k&=\frac1k\sum_{d\mid k}\mu(k/d)
       \bigl(1+\gcd(2^d-1,q-1)\bigr)^o.                         \label{eq:Ck}\end{aligned}$$ If $\ell=\operatorname{ord}_m(2)$ for $m>1$ and $\ell=1$ for $m=1$, then $C_k=0$ unless $k\mid\ell$. The Artin--Mazur zeta function [@ArtinMazur1965] is the rational finite product $$\label{eq:zeta}
 \zeta_T(z)
 :=\exp\left(\sum_{k\geq1}\frac{F_k}{k}z^k\right)
 =\prod_{k\mid\ell}(1-z^k)^{-C_k}.$$ In particular, [\[eq:Ck\]](#eq:Ck){reference-type="eqref" reference="eq:Ck"} is a complete cycle inventory, not only an asymptotic count.

In any finite map, $F_k=\sum_{d\mid k}P_d$. Möbius inversion and [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} give [\[eq:Pk\]](#eq:Pk){reference-type="eqref" reference="eq:Pk"}; division by $k$ gives [\[eq:Ck\]](#eq:Ck){reference-type="eqref" reference="eq:Ck"}. On $R_q\setminus\{0\}=\mu_m$, squaring is an automorphism of order $\ell$. Coordinatewise squaring on $R_q^o$ also has order $\ell$, so every recurrent period divides $\ell$. Finally, a cycle of length $k$ contributes $$\exp\left(\sum_{r\geq1}\frac{z^{rk}}r\right)=(1-z^k)^{-1}$$ to the defining exponential. Multiplying over all cycles proves [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The small fixed sequences in [1](#tab:signals){reference-type="ref" reference="tab:signals"} show that the arithmetic is visible immediately. The contrast between $q=7$ and $q=16$ at time four, for example, detects different odd parts of $q-1$ although both begin $4,16,4$ when $n=3$.

::: {#tab:signals}
   $q$    $n$   $o$  first fixed counts
  ------ ----- ----- --------------------
   $7$    $3$   $2$  $4,16,4,16,4,16$
   $11$   $2$   $2$  $4,4,4,36,4,4$
   $5$    $4$   $3$  $8,8,8,8,8,8$
   $16$   $3$   $2$  $4,16,4,256,4,16$

  : Exact fixed-point signals; entries list $F_1,F_2,\ldots$.
:::

# Rigidity from temporal data

The exponent $o$ remembers only the number of inversion orbits, so by itself it leaves an odd/even ambiguity in $n$. Depth and phase size resolve it.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Within the family $n\mid(q-1)$, the data $$\label{eq:data}
 \left(q^n,\ (F_k)_{k\geq1},\ D\right)$$ determine the ordered pair $(q,n)$ uniquely. More explicitly:

1.  $o=\log_2F_1$;

2.  $m=\max_{k\geq1}F_k^{1/o}-1$;

3.  the only possible lengths are $n=2o-1$ and, when $o\geq2$, $n=2o-2$;

4.  for a candidate $n$, put $$\varepsilon_n=\mathbf1_{\{n>\gcd(n,2)\}},\qquad
     q_n=2^{D-\varepsilon_n}m+1.$$ The unique candidate satisfying the phase-size identity $q_n^n=q^n$ (and the family conditions) is the original pair.

Since $L_1=2$, [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} gives $F_1=2^o$. Because $2^k-1$ is odd, $$\gcd(2^k-1,q-1)=\gcd(2^k-1,m).$$ If $m>1$, some $k$ satisfies $2^k\equiv1\pmod m$; for $m=1$ the claim is immediate. Thus the maximum in item 2 is exactly $m$. Solving $2o=n+\gcd(n,2)$ gives precisely the candidates in item 3, and [\[thm:depth\]](#thm:depth){reference-type="ref" reference="thm:depth"} gives the formula for $q_n$.

It remains to show that the candidates cannot both survive. If $o=1$, only $n=1$ is positive. If $o\geq3$, both candidate lengths have paired characters, so both have $\varepsilon_n=1$ and hence the same candidate field size. Their distinct positive exponents cannot give the same phase size.

The only delicate branch is $o=2$, where the candidates are $n=2$ and $n=3$. Write their reconstructed field sizes as $q_2$ and $q_3$. Their different synchronization corrections give $$q_2-1=2(q_3-1).$$ If both also matched the phase size, then $q_2^2=q_3^3$, so coprimality of $2$ and $3$ would give integers $q_2=r^3$ and $q_3=r^2$ with $r\geq2$. Substitution yields $$r^3-1=2(r^2-1),\qquad
 (r-1)(r^2-r-1)=0,$$ which has no integer solution with $r\geq2$. Hence at most one candidate survives in every branch, while the true one necessarily does.

The phase-size datum in [\[eq:data\]](#eq:data){reference-type="eqref" reference="eq:data"} is the cardinality of the given finite phase space, not an invariant inferred from the zeta function. The theorem is therefore a qualified recovery statement inside the split cyclic family, not a claim that zeta functions classify arbitrary finite maps or group algebras.

# Exact controls and limitations

The accompanying verifier uses no computer-algebra package. For each stored small lane it enumerates all coefficient vectors, computes cyclic convolution and reversal literally, constructs the full functional graph, and checks: the Fourier product rule, [\[eq:iterate,eq:fixed,eq:recsize,eq:depth\]](#eq:iterate,eq:fixed,eq:recsize,eq:depth){reference-type="ref" reference="eq:iterate,eq:fixed,eq:recsize,eq:depth"}, the Möbius cycle ledger, and the zeta exponents. Prime-field lanes include $(q,n)=(3,1),(3,2),(5,2),(5,4),(7,3),(11,2),(13,3)$. Separate polynomial basis implementations of $$\mathbb F_4=\mathbb F_2[t]/(t^2+t+1),\qquad
 \mathbb F_{16}=\mathbb F_2[t]/(t^4+t+1)$$ exercise genuine extension-field arithmetic at $n=3$. A broader arithmetic lane checks the recovery algorithm for all divisors $n\mid(q-1)$ over a registered list of prime powers. The stored output is a deterministic exact certificate, not numerical evidence in place of the proofs.

The splitting hypothesis is essential to the present formulas. When $n\nmid(q-1)$, Frobenius acts nontrivially on character blocks; when $p\mid n$, the group algebra is not semisimple. Neither regime is covered here. Likewise, the cited unit literature focuses largely on units, whereas the transient maximum here is often attained using a whole-algebra block; this distinction motivates the calculation but does not establish priority.

There is also an internal firewall against P86. That paper studies the spatial two-block factor $Y_i=U_iU_{i+1}$ of an iid bi-infinite field process, with support entropy and prediction memory as its observables. Here a paired product is only one Fourier block of a finite self-map; after one update it synchronizes and enters scalar squaring, and the observables are temporal fixed counts, cycles, and depth. The shared multiplication primitive is therefore disclosed rather than counted as a separate contribution.

# Data and code availability {#data-and-code-availability .unnumbered}

The exact verifier, its stored output, claim-to-evidence ledger, and build instructions accompany this internal manuscript. No external data are used.
