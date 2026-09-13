---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-363-prime-return-entropy-tower"
canonical_tex: "zeta_mvp0/papers/RH-363-prime-return-entropy-tower/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-363-prime-return-entropy-tower/main.pdf"
source_sha256: "4e6bdede6775ff4e21fae928c40ce65aea1887e633684beabd5b4a75f8d7d5f3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime-return admissible entropy towers: zeta blindness, exact rank recovery, and sharp radius discontinuity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-363-prime-return-entropy-tower>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-363-prime-return-entropy-tower/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-363-prime-return-entropy-tower/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-363-prime-return-entropy-tower/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-363-prime-return-entropy-tower/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the integral Hénon automorphism $H(x,y)=(1-6x^2-y,x)$ and a nonperiodic integral point $P$, let $r_p(P)$ be the return period of $P\bmod p$. At every integer level $m\ge1$, we form the pairwise-coprime family $$\mathcal B_m(P)=\{p^{m r_p(P)}:p\text{ prime}\}$$ and its two-sided admissible shift $X_m(P)$. Every level has only the zero periodic point and hence the identical Artin--Mazur zeta function $(1-z)^{-1}$. Nevertheless its normalized topological entropy is $$E_m(P)=\frac{h_{\rm top}(X_m(P))}{\log2}
   =\prod_p(1-p^{-m r_p(P)})=Z_P(m)^{-1},$$ where $Z_P$ is the zero-free return Euler product of RH-362. The entropy tower is strictly increasing to one and is information-complete: if $\Lambda_m=-\log E_m$ and $M_m=\sum_p p^{-m r_p}$, then an absolutely convergent inversion over multiples gives $$M_m=\sum_{j\ge1}\frac{\mu(j)}j\Lambda_{mj}.$$ The moments recursively recover every distinct atom $p^{-r_p}$, and unique factorization recovers every labeled pair $(p,r_p)$.

  For the first $k$ primes, finite approximants agree with the limiting zeta through the degree before the primorial $W_k$. Their first defect occurs exactly at $W_k$ and is the universal prime-wheel defect, independent of $P$, $m$, and the return ranks. Their logarithmic and reduced-zeta radii are both $2^{-E_{m,k}}$, increase to $2^{-E_m}<1$, and their zeta germs converge uniformly on every smaller closed disk. This disk is sharp, while the coefficientwise limiting zeta has radius one. These are standalone structural theorems, not an operatorization of the Riemann zeta function. Gates A--E remain false/open; no Riemann-zero identification, Hilbert--Polya operator, completed divisor equality, or proof of RH is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Prime-return admissible entropy towers:\
  zeta blindness, exact rank recovery, and sharp radius discontinuity
```

## Markdown 正文

# Frozen foundation and source route

The RH corpus through RH-361 remains frozen in four disjoint volumes covering RH-1--RH-160, RH-161--RH-241, RH-242--RH-281, and RH-282--RH-361 [@WangRHCorpus2026]. Their outer archive replay still records four volumes, 361 numbered sources, 73 archive members, 1,548 dependency hashes, eight result hashes, and zero failures. Nothing in this paper renumbers, rewrites, or weakens that provenance base.

The active physical route coordinate also remains $$\texttt{actual\_same\_clock\_unnormalized\_head\_transport\_open}.$$ In particular, the first unproved physical leaf $$D_{4k}(R)=\sum_{2\le n<4k}
 \frac{|h_{\sigma,n}-s_{k,n}|R^n}{n}\longrightarrow0$$ is not estimated below.

The first locked input is RH-362 [@WangRH3622026]. For $$H(x,y)=(1-6x^2-y,x)$$ and a nonperiodic integral point $P$, it defines the modular return rank $$r_p(P)=\min\{n\ge1:H^n(P)\equiv P\pmod p\}$$ and proves two facts used here:

1.  for every fixed $K$, only finitely many primes have $r_p(P)<K$;

2.  the Euler product $$Z_P(s)=\prod_p(1-p^{-s r_p(P)})^{-1}
     \label{eq:return-euler}$$ converges normally and is holomorphic and zero-free on $\operatorname{Re}s>0$.

The finite return-distribution experiments in the upstream source are not used as asymptotic input.

The second locked input is the exact theory of pairwise-coprime admissible shifts in @WangPeriodicCollapse2026: infinite pairwise-coprime families have periodic-orbit collapse; summable reciprocal moduli retain an exact positive entropy; and finite approximants have gcd-stratified fixed-point counts and exact zeta radii. The contribution here is to bind those theorems to the complete return-rank sequence, then prove the entropy tower's exact inversion, its universal first defect, and its sharp local-uniform convergence domain.

# Return-power admissible shifts

For a family $\mathcal B$ of integers greater than one, define the two-sided $\mathcal B$-admissible shift $$A_{\mathcal B}
 =\left\{x\in\{0,1\}^{\mathbb Z}:
 |\operatorname{supp}(x)\bmod b|<b\ \text{for every }b\in\mathcal B\right\},
 \label{eq:B-admissible}$$ with the left shift $\sigma$. Thus the support must omit at least one residue class modulo every $b\in\mathcal B$.

[\[def:tower\]]{#def:tower label="def:tower"} Fix a nonperiodic $P\in\mathbb Z^2$. For $m\ge1$, put $$b_{m,p}=p^{m r_p(P)},
 \qquad
 \mathcal B_m(P)=\{b_{m,p}:p\text{ prime}\},
 \qquad
 X_m(P)=A_{\mathcal B_m(P)}.
 \label{eq:return-power-family}$$ Write $q_p=p^{-r_p(P)}$, so $b_{m,p}^{-1}=q_p^m$.

[\[lem:thin\]]{#lem:thin label="lem:thin"} For every $m\ge1$, the family $\mathcal B_m(P)$ is infinite and pairwise coprime, and $$\sum_p\frac1{b_{m,p}}
 =\sum_p p^{-m r_p(P)}<\infty.
 \label{eq:thin}$$

Distinct members are powers of distinct primes. To prove convergence, choose $K$ with $mK>1$. RH-362 leaves only finitely many primes with $r_p<K$, while the remaining terms are bounded by $p^{-mK}$. The latter prime sum converges.

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} For every $m,n\ge1$, $$\operatorname{Fix}(\sigma^n|_{X_m(P)})=\{0^\infty\}.$$ Consequently $$N_n(X_m(P))=1
 \quad(n\ge1),
 \qquad
 \zeta_{X_m(P)}(z)
 =\exp\!\left(\sum_{n\ge1}\frac{z^n}{n}\right)
 =\frac1{1-z}.
 \label{eq:collapsed-zeta}$$ In particular the Artin--Mazur zeta is independent of $m$, $P$, and all return ranks.

Fix a period $n$. Choose a prime $p\nmid n$. Then $\gcd(n,b_{m,p})=1$. If an $n$-periodic sequence has $x_s=1$, its support contains every $s+jn$, $j\in\mathbb Z$. Since $n$ is invertible modulo $b_{m,p}$, those positions cover every residue modulo $b_{m,p}$, contradicting [\[eq:B-admissible\]](#eq:B-admissible){reference-type="eqref" reference="eq:B-admissible"}. The zero sequence is admissible, so it is the unique fixed point at every order. The Artin--Mazur formula then gives [\[eq:collapsed-zeta\]](#eq:collapsed-zeta){reference-type="eqref" reference="eq:collapsed-zeta"} coefficientwise and analytically for $|z|<1$.

# The entropy tower

Define $$E_m(P)=\prod_p(1-q_p^m)
 =\prod_p(1-p^{-m r_p(P)}).
 \label{eq:entropy-density}$$ Lemma [\[lem:thin\]](#lem:thin){reference-type="ref" reference="lem:thin"} makes this a positive convergent product.

[\[thm:entropy\]]{#thm:entropy label="thm:entropy"} For every $m\ge1$, $$h_{\rm top}(X_m(P))=E_m(P)\log2,
 \qquad
 E_m(P)=Z_P(m)^{-1}.
 \label{eq:entropy-euler}$$ Moreover $$0<E_1(P)<E_2(P)<\cdots<1,
 \qquad
 \lim_{m\to\infty}E_m(P)=1.
 \label{eq:entropy-monotone}$$ Thus identical periodic zeta functions coexist with a nonconstant, information-bearing entropy tower.

For completeness, let $$F_m=\{j\in\mathbb Z:b_{m,p}\nmid j\text{ for every prime }p\}.$$ Finite Chinese-remainder counts and the tail bound from [\[eq:thin\]](#eq:thin){reference-type="eqref" reference="eq:thin"} show that $F_m$ has density $\prod_p(1-b_{m,p}^{-1})=E_m$. Every binary sequence supported on $F_m$ is admissible, giving the entropy lower bound $E_m\log2$. Conversely, $X_m$ is contained in the admissible shift for every finite prime prefix. A finite prefix is the union of finitely many periodic masks, each with free-coordinate density $\prod_{p\le p_k}(1-b_{m,p}^{-1})$. Its entropy is that density times $\log2$. Letting the prefix grow gives the matching upper bound. Equation [\[eq:return-euler\]](#eq:return-euler){reference-type="eqref" reference="eq:return-euler"} at $s=m$ gives the second identity in [\[eq:entropy-euler\]](#eq:entropy-euler){reference-type="eqref" reference="eq:entropy-euler"}.

Every factor $1-q_p^m$ strictly increases with $m$. More quantitatively, for every finite prefix containing $p=2$, $$\frac{E_{m+1,k}}{E_{m,k}}
 =\prod_{p\le p_k}\frac{1-q_p^{m+1}}{1-q_p^m}
 \ge\frac{1-q_2^{m+1}}{1-q_2^m}>1.$$ Taking the quotient of the positive limiting products proves $E_{m+1}>E_m$. Finally, $M_1:=\sum_p q_p<\infty$, $q_p\le1/2$, and $$0\le-\log E_m
 =\sum_p-\log(1-q_p^m)
 \le \frac{\sum_p q_p^m}{1-2^{-m}}
 \le \frac{2^{-(m-1)}M_1}{1-2^{-m}}\longrightarrow0.$$ Hence $E_m\to1$.

The equality $E_m=Z_P(m)^{-1}$ is only a sampling identity on the positive integers. It neither analytically continues $Z_P$ nor identifies a spectral divisor.

# Multiples--Möbius inversion and complete rank recovery

The collapse theorem shows that no individual Artin--Mazur zeta can recover even one rank. The full entropy tower has the opposite behavior.

Put $$\Lambda_m=-\log E_m=\log Z_P(m),
 \qquad
 M_m=\sum_p q_p^m=\sum_p p^{-m r_p(P)}.
 \label{eq:lambda-moment}$$

[\[thm:mobius\]]{#thm:mobius label="thm:mobius"} For every $m\ge1$, $$\begin{aligned}
 \Lambda_m
 &=\sum_{j\ge1}\frac{M_{mj}}j,
 \label{eq:lambert-transform}\\
 M_m
 &=\sum_{j\ge1}\frac{\mu(j)}j\Lambda_{mj}
 =-\sum_{j\ge1}\frac{\mu(j)}j\log E_{mj}.
 \label{eq:mobius-inversion}\end{aligned}$$ All displayed series and the rearranged double series in the proof converge absolutely.

Expanding the logarithm of the positive Euler product gives $$\Lambda_m
 =\sum_p\sum_{j\ge1}\frac{q_p^{mj}}j
 =\sum_{j\ge1}\frac{M_{mj}}j,$$ which proves [\[eq:lambert-transform\]](#eq:lambert-transform){reference-type="eqref" reference="eq:lambert-transform"}. Let $q_*=\max_p q_p$. This maximum exists, is at most $1/2$, and $M_1<\infty$. For $n\ge1$, $$M_n\le q_*^{n-1}M_1,
 \qquad
 \Lambda_n\le\frac{M_n}{1-q_*^n}.
 \label{eq:absolute-bounds}$$ These geometric bounds prove every required absolute convergence. Hence $$\begin{aligned}
 \sum_{j\ge1}\frac{\mu(j)}j\Lambda_{mj}
 &=\sum_{j,\ell\ge1}\frac{\mu(j)}{j\ell}M_{mj\ell}\\
 &=\sum_{t\ge1}\frac1t
   \left(\sum_{j\mid t}\mu(j)\right)M_{mt}
 =M_m,\end{aligned}$$ because the inner divisor sum is one for $t=1$ and zero otherwise.

The inversion is over multiples $mj$, rather than the more familiar finite divisor inversion at one index.

[\[thm:rank-recovery\]]{#thm:rank-recovery label="thm:rank-recovery"} Knowledge of the exact sequence $\{E_m(P):m\ge1\}$ uniquely determines the complete labeled return-rank sequence $\{(p,r_p(P)):p\text{ prime}\}$. More explicitly, theorem [\[thm:mobius\]](#thm:mobius){reference-type="ref" reference="thm:mobius"} first determines every moment $M_n$. Order the distinct atoms as $$q_{(1)}>q_{(2)}>\cdots>0.$$ After $q_{(1)},\ldots,q_{(a-1)}$ have been recovered, one has $$q_{(a)}
 =\lim_{n\to\infty}
 \left(M_n-\sum_{i<a}q_{(i)}^n\right)^{1/n}.
 \label{eq:moment-peeling}$$ Each reciprocal $q_{(a)}^{-1}$ is a unique prime power $p^{r_p}$, which recovers both the prime label and its rank.

Distinct primes give distinct atoms: an equality $p^{-r_p}=q^{-r_q}$ would imply $p^{r_p}=q^{r_q}$, so unique factorization gives $p=q$. Also $q_p\le p^{-1}$, hence only finitely many atoms exceed any fixed positive threshold and the atoms can be ordered strictly downward to zero.

Let $$R_{a,n}=M_n-\sum_{i<a}q_{(i)}^n
 =\sum_{i\ge a}q_{(i)}^n.$$ Since $\sum_iq_{(i)}=M_1<\infty$, $$q_{(a)}^n\le R_{a,n}
 \le q_{(a)}^{n-1}\sum_{i\ge a}q_{(i)}.$$ Taking $n$-th roots proves [\[eq:moment-peeling\]](#eq:moment-peeling){reference-type="eqref" reference="eq:moment-peeling"}. Finally, $q_{(a)}^{-1}=p^{r_p}$ by construction, and its prime-power factorization is unique.

Theorem [\[thm:rank-recovery\]](#thm:rank-recovery){reference-type="ref" reference="thm:rank-recovery"} is an injectivity theorem for the exact infinite entropy sequence. It does not say that a short, floating-point entropy table stably recovers large ranks. Quantitative finite-data conditioning is a separate open problem.

# Finite approximants and the universal primorial defect

List the primes increasingly as $p_1,p_2,\ldots$, and define $$\mathcal B_{m,k}(P)=\{p_i^{m r_{p_i}(P)}:1\le i\le k\},
 \qquad
 X_{m,k}(P)=A_{\mathcal B_{m,k}(P)},
 \qquad
 W_k=\prod_{i=1}^k p_i.
 \label{eq:finite-approximants}$$ Then $X_{m,k+1}\subset X_{m,k}$ and $X_m=\bigcap_kX_{m,k}$.

We recall the exact finite formula in the notation needed here. For pairwise-coprime $b_1,\ldots,b_k$, put $$d_i(n)=\gcd(n,b_i),
 \qquad
 D(n)=\prod_i d_i(n).$$ For a tuple $\boldsymbol d=(d_1,\ldots,d_k)$ with all $d_i>1$, let $$P_{\boldsymbol d}(u)
 =\sum_{1\le j_i\le d_i}
 \left[\prod_{i=1}^k(-1)^{j_i+1}\binom{d_i}{j_i}\right]
 u^{\prod_{i=1}^k(d_i-j_i)}.
 \label{eq:coprime-polynomial}$$ The gcd-reduction and inclusion--exclusion theorem of @WangPeriodicCollapse2026 gives $$N_n(A_{\{b_1,\ldots,b_k\}})
 =\begin{cases}
 1,&d_i(n)=1\text{ for some }i,\\
 P_{\boldsymbol d(n)}(2^{n/D(n)}),&d_i(n)>1\text{ for every }i.
 \end{cases}
 \label{eq:finite-fixed-count}$$

[\[thm:first-defect\]]{#thm:first-defect label="thm:first-defect"} For every nonperiodic $P$, every $m\ge1$, and every $k\ge1$, $$N_n(X_{m,k}(P))=1
 \quad\Longleftrightarrow\quad
 W_k\nmid n.
 \label{eq:exact-elimination}$$ If $W_k\mid n$, then in fact $N_n(X_{m,k}(P))\ge n+1$. In particular, $$N_n(X_{m,k}(P))=1
 \qquad(1\le n<W_k),
 \label{eq:no-early-defect}$$ whereas $$N_{W_k}(X_{m,k}(P))
 =P_{(p_1,\ldots,p_k)}(2)>1.
 \label{eq:universal-defect}$$ Thus the first defect is independent of $P$, $m$, and all return ranks. If $$C_k=\frac{P_{(p_1,\ldots,p_k)}(2)-1}{W_k},
 \label{eq:primitive-defect}$$ then $C_k$ is a positive integer and $$\zeta_{X_{m,k}}(z)
 =\frac1{1-z}\left(1+C_kz^{W_k}+O(z^{W_k+1})\right).
 \label{eq:zeta-first-defect}$$ Equivalently, the Taylor coefficients equal one through degree $W_k-1$, and the degree-$W_k$ coefficient is $1+C_k$.

If $W_k\nmid n$, not every $p_i$ divides $n$. For an index with $p_i\nmid n$, one has $\gcd(n,p_i^{m r_{p_i}})=1$, and the first line of [\[eq:finite-fixed-count\]](#eq:finite-fixed-count){reference-type="eqref" reference="eq:finite-fixed-count"} applies. Conversely, if $W_k\mid n$, every reduced modulus is greater than one. The zero support and each of the $n$ singleton supports in $\mathbb Z/n\mathbb Z$ omit a residue modulo every reduced modulus, so they give $n+1$ distinct admissible fixed points. This proves [\[eq:exact-elimination\]](#eq:exact-elimination){reference-type="eqref" reference="eq:exact-elimination"}. At $n=W_k$, the reduced moduli are exactly $$\gcd(W_k,p_i^{m r_{p_i}})=p_i,$$ and $D(W_k)=W_k$, proving [\[eq:universal-defect\]](#eq:universal-defect){reference-type="eqref" reference="eq:universal-defect"}.

Every nonzero point fixed by $\sigma^{W_k}$ has exact period $W_k$, because [\[eq:no-early-defect\]](#eq:no-early-defect){reference-type="eqref" reference="eq:no-early-defect"} excludes nonzero points at all proper divisors. Such points split into full shift orbits of size $W_k$; hence $C_k$ is a positive integer. Comparing $$\log\zeta_{X_{m,k}}(z)=\sum_{n\ge1}\frac{N_n(X_{m,k})}{n}z^n$$ with $-\log(1-z)$ proves [\[eq:zeta-first-defect\]](#eq:zeta-first-defect){reference-type="eqref" reference="eq:zeta-first-defect"}.

For $k=1,2,3$, the universal triples are $$(W_k,N_{W_k},C_k)=(2,3,1),\ (6,13,2),\ (30,4501,150).$$ These values are exact finite illustrations of the theorem, not evidence for a limiting rank distribution.

[\[cor:coefficientwise\]]{#cor:coefficientwise label="cor:coefficientwise"} For fixed $m$, both $\log\zeta_{X_{m,k}}$ and $\zeta_{X_{m,k}}$ converge coefficientwise, with eventual equality in every degree, to $$-\log(1-z)
 \quad\text{and}\quad
 \frac1{1-z}.$$

For each fixed $n$, choose an index $j$ with $p_j\nmid n$. Every $k\ge j$ then has a reduced modulus equal to one, so $N_n(X_{m,k})=1$. A zeta coefficient of degree $r$ depends only on the fixed counts through degree $r$.

# Exact radii and the sharp local-uniform disk

Put $$E_{m,k}=\prod_{i=1}^k(1-p_i^{-m r_{p_i}}).
 \label{eq:finite-density}$$ These finite densities decrease strictly to $E_m>0$.

For the finite approximant define $$\begin{aligned}
 \mathcal L_{m,k}(z)
 &=\sum_{n\ge1}\frac{N_n(X_{m,k})}{n}z^n,\\
 R_{m,k}^{\log}
 &=\text{the convergence radius of }\mathcal L_{m,k},\\
 R_{m,k}^{\zeta}
 &=\text{the origin Taylor radius of the reduced rational function }
   \zeta_{X_{m,k}}.\end{aligned}$$

[\[thm:radii\]]{#thm:radii label="thm:radii"} For every $m,k\ge1$, $$h_{\rm top}(X_{m,k})=E_{m,k}\log2,
 \qquad
 R_{m,k}^{\log}=R_{m,k}^{\zeta}
 =2^{-E_{m,k}}.
 \label{eq:finite-radii}$$ The positive point $2^{-E_{m,k}}$ is a nonremovable singularity of the reduced rational zeta function. Consequently $$R_{m,k}^{\log}=R_{m,k}^{\zeta}
 \nearrow R_m^*:=2^{-E_m}<1,
 \label{eq:radius-limit}$$ whereas the coefficientwise limit $(1-z)^{-1}$ has radius one.

Let $L_{m,k}=\prod_{i\le k}p_i^{m r_{p_i}}$. Choosing one omitted residue modulo each finite modulus produces a periodic mask with free-coordinate density $E_{m,k}$. The finite union over all joint phases gives the matching upper word-count bound, so the entropy is $E_{m,k}\log2$.

For periods divisible by $L_{m,k}$, one fixed phase supplies at least $2^{E_{m,k}n}$ admissible periodic points. Conversely the finite set of phases gives $N_n(X_{m,k})\le L_{m,k}2^{E_{m,k}n+O(L_{m,k})}$. Thus $$\limsup_{n\to\infty}N_n(X_{m,k})^{1/n}=2^{E_{m,k}},$$ and Cauchy--Hadamard gives the logarithmic radius. At $R=2^{-E_{m,k}}$, the subsequence $n=L_{m,k}\ell$ contributes at least $1/(L_{m,k}\ell)$ to $N_nR^n/n$. Hence $\mathcal L_{m,k}(r)\to+\infty$ as $r\uparrow R$, and $\zeta_{X_{m,k}}(r)=\exp(\mathcal L_{m,k}(r))\to+\infty$. The positive singularity cannot cancel in a reduced rational presentation, so the two radii agree. Finally $E_{m,k}\downarrow E_m>0$, proving [\[eq:radius-limit\]](#eq:radius-limit){reference-type="eqref" reference="eq:radius-limit"} and its strict inequality from one.

The number $R_m^*$ is the limit of finite-approximant radii and the sharp exhaustion radius in theorem [\[thm:sharp-disk\]](#thm:sharp-disk){reference-type="ref" reference="thm:sharp-disk"}. It is not the zeta radius of the infinite shift $X_m$, whose zeta function is $(1-z)^{-1}$ and whose origin radius is one.

Because the finite radii vary, we state local uniformity for origin germs.

Let $f_k$ be analytic at zero with origin radii $R_k\to R>0$. We say that $f_k\to f$ on the exhaustion disk $\mathbb D_R$ if, for every $0<\rho<R$, all sufficiently large origin series are analytic on $|z|\le\rho$ and converge there uniformly to $f$.

[\[thm:sharp-disk\]]{#thm:sharp-disk label="thm:sharp-disk"} For each fixed $m$, the germs $\zeta_{X_{m,k}}$ converge to $(1-z)^{-1}$ on the exhaustion disk $$\mathbb D_{R_m^*},
 \qquad R_m^*=2^{-E_m}.
 \label{eq:exhaustion-disk}$$ This disk is sharp among centered disks: no disk $\mathbb D_\rho$ with $\rho>R_m^*$ admits tailwise holomorphic convergence of the rational zeta functions. The finite positive poles converge to $R_m^*$, even though the limiting function is analytic there and throughout $|z|<1$.

Fix $\rho<R_m^*$. Choose $k_0$ with $\rho<R_{m,k_0}^{\log}$. The inclusions $X_{m,k+1}\subset X_{m,k}$ give $$1\le N_n(X_{m,k})\le N_n(X_{m,k_0})
 \qquad(k\ge k_0),$$ and corollary [\[cor:coefficientwise\]](#cor:coefficientwise){reference-type="ref" reference="cor:coefficientwise"} gives pointwise convergence of these counts to one. Since $\sum_n N_n(X_{m,k_0})\rho^n/n$ converges, dominated convergence yields $$\sup_{|z|\le\rho}
 \left|\mathcal L_{m,k}(z)+\log(1-z)\right|
 \le\sum_{n\ge1}\frac{(N_n(X_{m,k})-1)\rho^n}{n}
 \longrightarrow0.$$ Exponentiating proves uniform zeta convergence on the closed disk.

For sharpness, theorem [\[thm:radii\]](#thm:radii){reference-type="ref" reference="thm:radii"} supplies a nonremovable positive pole at $R_{m,k}<R_m^*$ for every $k$, with $R_{m,k}\to R_m^*$. Every centered disk of radius greater than $R_m^*$ contains all these poles, so no tail is holomorphic on that disk. The approaching poles also rule out an eventually pole-free neighborhood of the boundary point $R_m^*$.

# Route A discovery value and Route B boundary

The two-route audit is intentionally asymmetric.

  Route     Exact verdict
  --------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route A   **GO.** The return-power tower is well-defined and functorial once the marked integral orbit and its exact modular ranks are fixed, but it is engineered and is not a canonical global dynamics. Zeta blindness versus entropy completeness, the multiples--Möbius recovery theorem, the universal first defect, and the sharp exhaustion disk are all-order standalone conclusions.
  Route B   **STOP\_SCOPED.** The common Artin--Mazur zeta contains no rank data. Recovery uses the full sequence of topological entropies, not signed weighted traces of one canonical global operator. The first fatal mismatch is therefore data type: pressure/entropy samples are not a von-Mangoldt prime-power trace ledger.

Several further boundaries are exact.

1.  $X_m(P)$ is a symbolic admissible shift assembled from all prime labels. It is not the zeta function of any full finite-field Hénon map and not a Hasse--Weil zeta function.

2.  The family indexed by $m$ is not one autonomous flow with one clock. The identity $E_m=Z_P(m)^{-1}$ evaluates a previously defined scalar Euler product at positive integers; it does not construct its analytic continuation from entropy.

3.  The finite sofic zeta functions and their positive poles are not noisy $\det_2$ data, not scattering resonances, and not spectra of a self-adjoint generator.

4.  Neither exact moment recovery nor unique factorization supplies the von Mangoldt weights $\log p$ at every prime-power order. No signed trace formula is present.

Thus Gates A--E remain false/open:

  Gate   Status       Missing object
  ------ ------------ ---------------------------------------------------
  A      false/open   canonical intrinsic physical spectral determinant
  B      false/open   time-oriented scattering or unitary completion
  C      false/open   self-adjoint generator and intrinsic $T\log T$
  D      false/open   von-Mangoldt-weighted signed prime-power traces
  E      false/open   completed-zeta divisor equality

# Executable protocol and claim firewall

The executable artifact performs only finite exact reproduction:

1.  it hashes the RH-362 theorem artifact, the exact admissible-shift source, and the frozen four-volume seals;

2.  it recomputes modular return ranks for $P=(0,0)$ on a declared finite prime prefix;

3.  it constructs the finite return-power moduli and checks pairwise coprimality and exact entropy-density fractions;

4.  it verifies the universal first defects $(2,3,1)$, $(6,13,2)$, and $(30,4501,150)$;

5.  it checks finite high-precision truncations of [\[eq:mobius-inversion\]](#eq:mobius-inversion){reference-type="eqref" reference="eq:mobius-inversion"}, explicitly labeled as numerical reproductions;

6.  it requires the physical route coordinate to remain open and every Gate and forbidden macro claim to remain false.

No finite table proves an all-prime distribution or the asymptotic conditioning of moment recovery. The all-prime statements in theorems [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"}--[\[thm:sharp-disk\]](#thm:sharp-disk){reference-type="ref" reference="thm:sharp-disk"} are established by the displayed proofs and locked source theorems.

In particular, this paper constructs no Hilbert--Polya operator, identifies no Riemann zero as a spectrum, proves no completed-zeta divisor equality, does not close the RH-241 noisy trace-envelope frontier, and does not prove the Riemann Hypothesis.

# Conclusion

The return-power construction separates two notions of dynamical information as sharply as possible. Every periodic orbit count at every tower level is identical and yields the same elementary zeta function. Nevertheless the full entropy tower retains all modular return ranks, with an explicit absolutely convergent inversion and a deterministic recovery procedure. Finite approximants advertise the loss only at a universal primorial order, while their nearest singularities converge to a boundary strictly inside the analytic disk of the coefficientwise limit.

For Route A this is a viable new structure: periodic data, word complexity, and finite singularities can decouple while remaining exactly computable. For Route B the same theorem identifies the obstruction. The recovered information lives in a family of entropy samples, not in one canonical signed trace determinant. A future bridge must supply that missing object rather than relabel the entropy tower as a spectral solution.
