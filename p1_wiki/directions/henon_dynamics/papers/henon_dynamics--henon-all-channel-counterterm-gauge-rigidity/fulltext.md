---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-all-channel-counterterm-gauge-rigidity"
canonical_tex: "henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/paper/paper.pdf"
source_sha256: "69584ec45f23043a3f99871584f3fdab77900ae7cb66881037536ecd370d305f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Channel Counterterm Rigidity and Holomorphic Gauge Freedom for the Relative Hénon--Lind Germ

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_all_channel_counterterm_gauge_rigidity>)
- [规范 TeX](<../../../../../henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_all_channel_counterterm_gauge_rigidity/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The reflection-packet Euler product of the full Hénon horseshoe has an exact scalar-channel logarithm, and its locally normalized ratio to the reverse-flip Lind zeta has one exponential essential singularity on each of infinitely many complex pole orbits. We classify all-channel counterterms in a normally convergent exponential channel class. With $\Phi(x)=2x/(1-2x^2)$ and $c_m=m^{-1}\prod_{p\mid m,\ p\text{ odd}}(1-p)$, the relative channel logarithm is $-\sum_{m\ge2}c_m\Phi(t^m)$. A multiplier $\exp(\sum_{m\ge2}d_m\Phi(t^m)+G(t))$ can make every channel singularity meromorphic only if $d_m=c_m$ coefficient by coefficient. At the remaining negative source boundary, nonzero holomorphic extension forces the unique power--exponential pair $(a,\beta)=(3/4,1/2)$. These singular coefficients are rigid, but the renormalization is not absolutely unique: the remaining counterterms form a torsor under the nowhere-zero holomorphic functions on the unit disk. Two normally convergent, pole-order-independent primary products make this freedom explicit. Genus $m-1$ annihilates the channel sector and, after the forced scalar normalization, trivializes the full relative object; genus $m$ preserves the first source monomial and leaves $\exp(-2\sum_{m\ge2}c_mt^m)$. Every finite Taylor-jet normalization still admits nonconstant gauges. The result is an analytic classification, not an operator determinant or an arithmetic trace formula.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: 'All-Channel Counterterm Rigidity and Holomorphic Gauge Freedom for the Relative Hénon--Lind Germ'
```

## Markdown 正文

# Introduction

The full Hénon horseshoe is conjugate to a two-shift in the classical horseshoe regime [@DevaneyNitecki1979]. Retaining marked reflection packets produces an Euler product different from the full infinite-dihedral Lind zeta. The reverse-flip source formula of @KimLeePark2003 is $$\label{eq:lind-source}
 \zeta_{\rm flip}(t)=(1-2t^2)^{-1/2}
 \exp\!\left(\frac{2t+3t^2}{1-2t^2}\right).$$ Earlier exact packet calculations give $$\label{eq:packet-source}
 \log\mathcal Z_{\rm orb}(t,1)=\sum_{m\ge1}c_m\Phi(t^m),\qquad
 \Phi(x)=\frac{2x}{1-2x^2},
 \quad
 c_m=\frac1m\prod_{\substack{p\mid m\\p\ \text{odd}}}(1-p).$$ The first positive boundary can be cancelled uniquely in the relative ratio, but all later channels survive. Their poles lie on distinct circles and accumulate at the unit circle.

The natural next instruction is "cancel every remaining singularity." It contains two logically separate questions. First, which singular coefficients are forced? Second, after they have been forced, which holomorphic part remains? Confusing these questions can turn a valid local rigidity theorem into an unjustified claim of a canonical determinant.

This paper answers both questions in a declared channel-log class. The singular coefficients are completely rigid. The regular part is a free nowhere-zero holomorphic gauge. We also construct two explicit primary products, both absolutely normally convergent and independent of the ordering of individual complex poles, that choose different gauges. One gives a normalized constant; the other leaves a nonconstant Möbius--cyclotomic residual. Thus all-channel renormalization exists analytically, but canonicity requires an additional source-native axiom.

The distinction matters for determinant language. A Fredholm determinant comes with an operator, a trace ideal, and a fixed normalization [@Simon1977]. A freely chosen holomorphic gauge supplies none of these. Our result neither constructs nor rules out an infinite-rank operator; it isolates what such an operator would still have to select.

# The relative continuation and its domains

Put $$\label{eq:u}
 u=1-\sqrt2t.$$ The uniquely normalized positive-boundary relative germ is $$\label{eq:Crel-def}
 C_{\rm rel}(t)=u^{1/2}\exp\!\left(-\frac{3}{4u}\right)
 \frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)},$$ with the power chosen on a local branch. The exact continuation ledger is $$\label{eq:relative-log}
 \log C_{\rm rel}(t)=H_{\rm rel}(1-\sqrt2t)
 -\sum_{m\ge2}c_m\Phi(t^m),$$ where $$\label{eq:H}
 H_{\rm rel}(u)=-\frac12\log(2-u)
 -\frac{3(2u-3)}{4(u-2)}.$$ The sign in [\[eq:relative-log\]](#eq:relative-log){reference-type="ref" reference="eq:relative-log"} is fundamental. Our counterterms are multipliers of $C_{\rm rel}$, so their channel coefficients must enter with the positive sign.

For $m\ge2$ and $0\le k<2m$, define $$\label{eq:poles}
 \rho_m=2^{-1/(2m)},\qquad
 \alpha_{m,k}=\rho_m e^{\pi i k/m}.$$ Let $$\label{eq:S2}
 S_2=\{\alpha_{m,k}:m\ge2,\ 0\le k<2m\},\qquad
 D_2=\mathbb D\setminus S_2.$$ The set $S_2$ is locally finite in $\mathbb D$, because $\rho_m\nearrow1$. The logarithmic source term in [\[eq:H\]](#eq:H){reference-type="ref" reference="eq:H"} is single-valued on the additional slit $$\label{eq:slit}
 \mathbb D_{\rm slit}=\mathbb D\setminus(-1,-2^{-1/2}],$$ using the principal branch in $w=1+\sqrt2t$. Channel statements live on $D_2$; statements involving $C_{\rm rel}$ live on $D_2\cap\mathbb D_{\rm slit}$. This separation prevents branch choices from being mistaken for channel monodromy.

[\[lem:channel-normal\]]{#lem:channel-normal label="lem:channel-normal"} Suppose a sequence $(d_m)_{m\ge2}$ satisfies $$\label{eq:d-growth}
 \sum_{m\ge2}|d_m|r^m<\infty\qquad(0<r<1).$$ Then $\sum_{m\ge2}d_m\Phi(t^m)$ converges normally on compact subsets of $D_2$.

Fix a compact $K\subset D_2$, and choose $r<1$ with $|t|\le r$ on $K$. For all sufficiently large $m$, $2r^{2m}\le1/2$, and hence $$|\Phi(t^m)|\le \frac{2r^m}{1-2r^{2m}}\le4r^m.$$ The corresponding tail is controlled by [\[eq:d-growth\]](#eq:d-growth){reference-type="ref" reference="eq:d-growth"}. Only finitely many earlier rational functions remain, and their denominators are bounded away from zero on $K$. The Weierstrass theorem then gives normal convergence and holomorphy [@Conway1978; @Remmert1991].

For the source sequence, $|c_m|\le1$: the absolute numerator is at most the odd radical of $m$, hence at most $m$. Thus [\[eq:d-growth\]](#eq:d-growth){reference-type="ref" reference="eq:d-growth"} holds for $d_m=c_m$.

# The exact complex principal parts

The positive P72 ladder is only one point from each complete pole orbit. We need the complete orbit to discuss order-independent pole products.

[\[lem:partial\]]{#lem:partial label="lem:partial"} Set $$\label{eq:bmk}
 b_{m,k}=\frac{c_m(-1)^k}{\sqrt2\,m}.$$ Then, as rational functions, $$\label{eq:partial}
 c_m\Phi(t^m)=\sum_{k=0}^{2m-1}
 \frac{b_{m,k}}{1-t/\alpha_{m,k}}.$$ In particular, the principal coefficient at $\alpha_{m,k}$ in the relative channel logarithm is $-b_{m,k}$.

Write $x=t/\rho_m$ and $\zeta=e^{\pi i/m}$. For $|x|<1$, expand the right side of [\[eq:partial\]](#eq:partial){reference-type="ref" reference="eq:partial"} into a geometric series. The coefficient at degree $j$ contains $$\label{eq:filter}
 \sum_{k=0}^{2m-1}(-1)^k\zeta^{-kj}
 =\sum_{k=0}^{2m-1}e^{\pi i k(m-j)/m}
 =\begin{cases}
 2m,&j\equiv m\pmod{2m},\\
 0,&\text{otherwise}.
 \end{cases}$$ Since $\rho_m^m=2^{-1/2}$, the surviving series is $$2c_mt^m+4c_mt^{3m}+8c_mt^{5m}+\cdots
 =\frac{2c_mt^m}{1-2t^{2m}}.$$ Equality in a neighborhood of zero proves the rational identity.

[\[lem:ownership\]]{#lem:ownership label="lem:ownership"} If $\alpha_{m,k}$ is a pole of channel $j$, then $j=m$.

The modulus of every pole in channel $j$ is $\rho_j$. The map $j\mapsto2^{-1/(2j)}$ is strictly increasing, so $\rho_j=\rho_m$ implies $j=m$.

This elementary radial separation is the source of coefficient rigidity. It also rules out a cancellation between arithmetically unrelated channel indices.

# Coefficientwise rigidity

Let $G\in\mathcal O(\mathbb D)$, and let $(d_m)$ satisfy [\[eq:d-growth\]](#eq:d-growth){reference-type="ref" reference="eq:d-growth"}. Define the multiplier $$\label{eq:W}
 W_{d,G}(t)=\exp\!\left(\sum_{m\ge2}d_m\Phi(t^m)+G(t)\right)
 \qquad(t\in D_2).$$

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Suppose $$\label{eq:combined-channel}
 W_{d,G}(t)\exp\!\left(-\sum_{m\ge2}c_m\Phi(t^m)\right)$$ extends meromorphically across every point of $S_2$. Then $$\label{eq:d=c}
 d_m=c_m\qquad(m\ge2).$$ Consequently [\[eq:combined-channel\]](#eq:combined-channel){reference-type="ref" reference="eq:combined-channel"} extends holomorphically and nowhere zero to $\mathbb D$, where it equals $e^{G(t)}$.

Fix $m\ge2$ and $0\le k<2m$. By [\[lem:channel-normal,lem:ownership\]](#lem:channel-normal,lem:ownership){reference-type="ref" reference="lem:channel-normal,lem:ownership"}, every channel with index different from $m$ is holomorphic near $\alpha_{m,k}$, including the normally convergent infinite tail. By [\[lem:partial\]](#lem:partial){reference-type="ref" reference="lem:partial"}, the logarithm of [\[eq:combined-channel\]](#eq:combined-channel){reference-type="ref" reference="eq:combined-channel"} has principal part $$\label{eq:rigidity-principal}
 \frac{(d_m-c_m)(-1)^k}
 {\sqrt2\,m(1-t/\alpha_{m,k})}.$$ If $d_m-c_m\ne0$, exponentiation produces an essential singularity. It cannot be meromorphic. Hence $d_m=c_m$. The pole orbit was arbitrary, so this holds for every $m\ge2$. Substitution leaves $e^G$, proving the last assertion.

The theorem does not assume a nonzero holomorphic extension in order to force [\[eq:d=c\]](#eq:d=c){reference-type="ref" reference="eq:d=c"}. A nonzero log pole exponentiates to an essential singularity, so even meromorphic continuation is impossible. The conclusion becomes nonzero holomorphic because the declared gauge is an exponential of a disk holomorphic function.

The theorem classifies the channel-log multipliers in [\[eq:W\]](#eq:W){reference-type="ref" reference="eq:W"}. One may write more exotic slit-dependent expressions, add algebraic zero factors, or allow counterterms without a global logarithm. Those are extra regularization data and are not silently included in the uniqueness claim.

# The negative source boundary

The positive source boundary was already removed in the definition of $C_{\rm rel}$. The negative point $t=-2^{-1/2}$ survives. Its exact ledger is particularly simple.

[\[prop:negative-ledger\]]{#prop:negative-ledger label="prop:negative-ledger"} Put $$\label{eq:w}
 w=1+\sqrt2t=2-u.$$ Then $$\label{eq:H-w}
 H_{\rm rel}(2-w)=\frac{3}{4w}-\frac12\log w-\frac32.$$

Substitute $u=2-w$ in [\[eq:H\]](#eq:H){reference-type="ref" reference="eq:H"}. Since $2-u=w$, $u-2=-w$, and $2u-3=1-2w$, one obtains $$-\frac12\log w-
 \frac{3(1-2w)}{-4w}
 =\frac{3}{4w}-\frac12\log w-\frac32.$$

[\[thm:source-rigidity\]]{#thm:source-rigidity label="thm:source-rigidity"} Choose a local slit at $w=0$. Let $a,\beta\in\mathbb C$. After the channel coefficients have been cancelled, the multiplier $$\label{eq:source-factor}
 w^\beta\exp(-a/w)$$ makes the relative object extend holomorphically and nonvanishingly across $w=0$ if and only if $$\label{eq:forced-source}
 (a,\beta)=\left(\frac34,\frac12\right).$$ For this pair the source contribution is $e^{-3/2}$. Including the holomorphic channel gauge, the exact total residual is $e^{-3/2}e^{G(t)}=e^{-3/2}A(t)$, where $A(t):=e^{G(t)}$. In the distinguished $G=0$ gauge this reduces to the constant $e^{-3/2}$.

After channel cancellation, the relevant logarithm is $$\label{eq:source-combined}
 \frac{3/4-a}{w}+(\beta-1/2)\log w-\frac32+G(t).$$ A nonzero coefficient of $1/w$ yields an exponential essential singularity, forcing $a=3/4$. The remaining factor $w^{\beta-1/2}$ has a nonzero holomorphic limit only when its exponent is zero, forcing $\beta=1/2$. Conversely these values reduce [\[eq:source-combined\]](#eq:source-combined){reference-type="ref" reference="eq:source-combined"} to $-3/2+G(t)$.

If the target were merely a meromorphic function allowed to vanish or have a pole at $w=0$, the conclusion would weaken to $a=3/4$ and $\beta-1/2\in\mathbb Z$. The exact pair [\[eq:forced-source\]](#eq:forced-source){reference-type="ref" reference="eq:forced-source"} belongs to the stated nonzero extension problem.

# The holomorphic gauge torsor

Write $$\label{eq:Rch}
 R_{\rm ch}(t)=\exp\!\left(-\sum_{m\ge2}c_m\Phi(t^m)\right).$$

[\[thm:gauge\]]{#thm:gauge label="thm:gauge"} The channel-log multipliers $W$ for which $WR_{\rm ch}$ extends holomorphically and nowhere zero to $\mathbb D$ form a torsor under $\mathcal O(\mathbb D)^\times$. More precisely, they are exactly $$\label{eq:gauge-form}
 W(t)=\exp\!\left(\sum_{m\ge2}c_m\Phi(t^m)\right)A(t),
 \qquad A\in\mathcal O(\mathbb D)^\times,$$ and $WR_{\rm ch}=A$.

Necessity of the singular series follows from [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}. Define $$A=W\exp\!\left(-\sum_{m\ge2}c_m\Phi(t^m)\right).$$ This is precisely the extended product $WR_{\rm ch}$, hence belongs to $\mathcal O(\mathbb D)^\times$. Conversely every such $A$ yields a valid multiplier. Since the disk is simply connected, every nowhere-zero holomorphic function on it has a holomorphic logarithm [@Conway1978]; therefore $A=e^G$ for some $G\in\mathcal O(\mathbb D)$, and the description agrees exactly with [\[eq:W\]](#eq:W){reference-type="ref" reference="eq:W"}. Multiplication by $A$ acts freely and transitively.

[\[cor:full-gauge\]]{#cor:full-gauge label="cor:full-gauge"} Insert the forced source factor $w^{1/2}e^{-3/(4w)}$. Every fully removable relative object in the class then has the form $$\label{eq:full-gauge}
 e^{-3/2}A(t),\qquad A\in\mathcal O(\mathbb D)^\times.$$

The singular data therefore determine a torsor, not a distinguished point of that torsor. An operator model could distinguish a point, but cancellation alone cannot.

# Two primary products and the residual sign

We now construct two explicit points of the torsor. Besides proving existence, they make the nonuniqueness visible without inserting an arbitrary function by hand.

For $z=t/\alpha_{m,k}$ and an integer $g\ge0$, define $$\label{eq:primary}
 \mathcal P_{m,k}^{[g]}(t)
 =\exp\!\left(
 b_{m,k}\left[\frac1{1-z}-\sum_{j=0}^{g}z^j\right]\right)
 =\exp\!\left(\frac{b_{m,k}z^{g+1}}{1-z}\right).$$ Its logarithm has principal part $b_{m,k}/(1-t/\alpha_{m,k})$, the positive sign needed to cancel the relative coefficient $-b_{m,k}$.

[\[lem:primary-normal\]]{#lem:primary-normal label="lem:primary-normal"} Both double products $$\label{eq:two-products}
 \prod_{m\ge2}\prod_{k=0}^{2m-1}\mathcal P_{m,k}^{[m-1]}(t),
 \qquad
 \prod_{m\ge2}\prod_{k=0}^{2m-1}\mathcal P_{m,k}^{[m]}(t)$$ converge through absolutely normally convergent logarithms on compact subsets of $D_2$. Their values are independent of every ordering of the individual pole factors.

Let $K\subset D_2$ be compact and choose $r<q<1$ with $|t|\le r$ on $K$. Since $\rho_m\to1$, for all sufficiently large $m$ and every $k$, $|t/\alpha_{m,k}|\le q$. Using $|c_m|\le1$, $$\begin{aligned}
 \sum_{k=0}^{2m-1}|\log\mathcal P_{m,k}^{[m-1]}(t)|
 &\le 2m\frac{1}{\sqrt2m}\frac{q^m}{1-q}
 =\frac{\sqrt2q^m}{1-q},\label{eq:majorant-minus}\\
 \sum_{k=0}^{2m-1}|\log\mathcal P_{m,k}^{[m]}(t)|
 &\le\frac{\sqrt2q^{m+1}}{1-q}.
 \label{eq:majorant-plus}\end{aligned}$$ Both majorants are summable in $m$. The finitely many earlier factors are holomorphic on $K$. Absolute normal convergence of the logarithms gives nonzero holomorphic products and unconditional, hence arbitrary-order, convergence [@Remmert1991].

[\[thm:genus-minus\]]{#thm:genus-minus label="thm:genus-minus"} The first product in [\[eq:two-products\]](#eq:two-products){reference-type="ref" reference="eq:two-products"} is $$\label{eq:Wminus}
 W_-(t)=\exp\!\left(\sum_{m\ge2}c_m\Phi(t^m)\right).$$ Hence $W_-R_{\rm ch}=1$. After the forced source factor, the result is $e^{-3/2}$; imposing final value one multiplies by the forced scalar $e^{3/2}$ and gives the identity function.

The compensating polynomial in [\[eq:primary\]](#eq:primary){reference-type="ref" reference="eq:primary"} contains degrees $0,\ldots,m-1$. Every corresponding weighted root sum in [\[eq:filter\]](#eq:filter){reference-type="ref" reference="eq:filter"} vanishes. Thus for each $m$, $$\sum_{k=0}^{2m-1}\log\mathcal P_{m,k}^{[m-1]}(t)
 =c_m\Phi(t^m).$$ Normal convergence permits summation over $m$, giving [\[eq:Wminus\]](#eq:Wminus){reference-type="ref" reference="eq:Wminus"}. The remaining assertions follow from [\[eq:Rch,eq:H-w\]](#eq:Rch,eq:H-w){reference-type="ref" reference="eq:Rch,eq:H-w"}.

[\[thm:genus-source\]]{#thm:genus-source label="thm:genus-source"} The second product in [\[eq:two-products\]](#eq:two-products){reference-type="ref" reference="eq:two-products"} is $$\label{eq:Wplus}
 W_+(t)=\exp\!\left(
 \sum_{m\ge2}c_m\Phi(t^m)-2\sum_{m\ge2}c_mt^m
 \right).$$ Consequently its channel residual is $$\label{eq:residual}
 W_+(t)R_{\rm ch}(t)
 =\exp\!\left(-2\sum_{m\ge2}c_mt^m\right).$$ The minus sign in [\[eq:residual\]](#eq:residual){reference-type="ref" reference="eq:residual"} is forced by treating $W_+$ as a multiplier of the negative relative channel logarithm.

The genus-$m$ compensating polynomial adds degree $m$ to the terms that were present in the preceding proof. By [\[eq:filter\]](#eq:filter){reference-type="ref" reference="eq:filter"}, $$\label{eq:first-retained}
 \sum_{k=0}^{2m-1}b_{m,k}
 \left(\frac{t}{\alpha_{m,k}}\right)^m=2c_mt^m.$$ It is subtracted in [\[eq:primary\]](#eq:primary){reference-type="ref" reference="eq:primary"}. Therefore $$\sum_{k=0}^{2m-1}\log\mathcal P_{m,k}^{[m]}(t)
 =c_m\Phi(t^m)-2c_mt^m.$$ Sum over $m$ and use [\[eq:Rch\]](#eq:Rch){reference-type="ref" reference="eq:Rch"}.

The residual has a useful Möbius product description.

[\[prop:mobius-product\]]{#prop:mobius-product label="prop:mobius-product"} For $|t|<1$, $$\label{eq:mobius-product}
 \exp\!\left(-2\sum_{m\ge2}c_mt^m\right)
 =e^{2t}\prod_{\substack{d\ge1\\d\ \text{odd}}}
 (1-t^d)^{2\mu(d)},$$ where the product is defined by its normally convergent logarithm.

Using $c_m=m^{-1}\sum_{d\mid m,\ d\ \text{odd}}d\mu(d)$, absolute convergence in $|t|<1$ permits the regrouping $$\begin{aligned}
 \sum_{m\ge1}c_mt^m
 &=\sum_{\substack{d\ge1\\d\ \text{odd}}}\mu(d)
   \sum_{r\ge1}\frac{t^{dr}}r\\
 &=-\sum_{\substack{d\ge1\\d\ \text{odd}}}\mu(d)\log(1-t^d).\end{aligned}$$ Since $c_1=1$, separating $m=1$, multiplying by $-2$, and exponentiating gives [\[eq:mobius-product\]](#eq:mobius-product){reference-type="ref" reference="eq:mobius-product"}.

The two products are equally successful at singularity cancellation and order independence, yet they differ by the nonconstant holomorphic gauge in [\[eq:residual\]](#eq:residual){reference-type="ref" reference="eq:residual"}. This is an explicit obstruction to claiming absolute canonicity from those two properties alone.

# Finite jets and monodromy

One might try to fix the gauge by prescribing the value and several derivatives at the origin. No finite number suffices.

[\[thm:finite-jet\]]{#thm:finite-jet label="thm:finite-jet"} Fix $N\ge0$, $t_0\in\mathbb D$, and an admissible multiplier $W$. For every $\lambda\in\mathbb C$, $$\label{eq:jet-gauge}
 W_\lambda(t)=W(t)\exp\!\left(\lambda(t-t_0)^{N+1}\right)$$ has the same cancellation data as $W$, and its residual agrees with that of $W$ through Taylor order $N$ at $t_0$. When $\lambda\ne0$, the gauge quotient is nonconstant.

The added exponential is entire and nowhere zero, so it changes no principal part or removability statement. Its Taylor expansion is $1+\lambda(t-t_0)^{N+1}+O((t-t_0)^{2N+2})$. Thus all derivatives through order $N$ agree, while the derivative at order $N+1$ changes when $\lambda\ne0$.

An infinite jet at one point would fix a holomorphic gauge by the identity theorem, but that is equivalent to prescribing the entire germ rather than deriving it from the singularities.

The primary factors in [\[eq:primary\]](#eq:primary){reference-type="ref" reference="eq:primary"} are exponentials of single-valued rational functions on $D_2$. They therefore have trivial monodromy. On a slit neighborhood of one puncture one can append $\lambda\log(1-t/\alpha_{m,k})$. Its exponential glues to the punctured disk only for integral $\lambda$; it then introduces a zero or pole unless $\lambda=0$. Hence nontrivial slit monodromy is additional data, and the requirement of a nowhere-zero globally exponential counterterm removes it.

# What the classification does not construct

The genus-$m-1$ convention gives a striking normalized identity, but it must be interpreted correctly. It says that a counterterm carrying the entire channel logarithm can cancel that logarithm. This is a valid analytic construction and an important order-independence theorem. It does not turn the identity function into a new spectral invariant.

The genus-$m$ convention keeps a nontrivial function, but its nontriviality does not by itself make it canonical. The torsor theorem supplies infinitely many other residuals, all with the same singular cancellation and any fixed finite jet. To promote one to a determinant requires independent data such as:

1.  a specified operator or complex;

2.  a trace ideal or a proved regularized-trace construction;

3.  a normalization functorial under the relevant dynamics; and

4.  a theorem identifying its determinant with the selected gauge.

None is supplied here. In particular, the integer channel label $m$ has not acquired rational-prime or von-Mangoldt semantics. The theorem does not produce a self-adjoint spectrum, a functional equation, or an explicit formula. It also does not rule out a future infinite-rank construction that selects one gauge for source-native reasons.

# Executable certificate

The accompanying exact-arithmetic package performs four independent types of finite verification.

1.  It replays $c_m=m^{-1}\sum_{d\mid m,\ d\ \text{odd}}d\mu(d)$ against the odd-radical Euler product.

2.  It checks the root filter [\[eq:filter\]](#eq:filter){reference-type="ref" reference="eq:filter"}, both primary residuals, and the product formula [\[eq:mobius-product\]](#eq:mobius-product){reference-type="ref" reference="eq:mobius-product"} through degree (96) using rational arithmetic.

3.  It constructs explicit finite-jet witnesses through order (12), and an independent program reconstructs all coefficient rows without importing the producer.

4.  It hash-locks the P72 and P73 proofs, certificates, and compiled papers. A mutation audit rejects sign reversals, a false source pair, and a false claim of finite-jet uniqueness, absolute canonicity, operator ownership, arithmetic advance, and Route-B authorization.

These computations certify the implementation and sign ledger. They do not replace the infinite normal-convergence or rigidity proofs.

# Conclusion

The P72 ladder admits all-channel exponential counterterms with strong analytic control. Within the declared channel-log class, every singular coefficient is forced; for a holomorphic nowhere-zero source extension, the negative source pair is uniquely $(3/4,1/2)$. Primary factors can be made absolutely normally convergent and independent of pole order. What is not forced is the holomorphic remainder. It is a full $\mathcal O(\mathbb D)^\times$-gauge torsor, and no finite Taylor jet selects a point.

The genus comparison gives the sharpest summary. One legitimate convention trivializes the normalized relative object; the next legitimate convention leaves an explicit nonconstant residual. Therefore singularity removal is not yet determinant ownership. A future operator theorem must select and explain a gauge rather than merely choose one.

# A general exponential-removability lemma

The channel proof used only a simple special case of the following local fact.

[\[lem:general-exp\]]{#lem:general-exp label="lem:general-exp"} Let $F$ be single-valued and holomorphic on a punctured disk. If $e^F$ extends meromorphically across the puncture, then its zero or pole order is zero. If the extension is finite there, then it is nonzero and $F$ extends holomorphically after addition of a constant in $2\pi i\mathbb Z$.

Write the meromorphic extension as $z^nU(z)$, where $n\in\mathbb Z$ and $U(0)\ne0$. On the punctured disk, $$F'(z)=\frac nz+\frac{U'(z)}{U(z)}.$$ The residue of the derivative of a single-valued Laurent series is zero, so $n=0$. A local holomorphic logarithm $L$ of $U$ then exists. Since $e^{F-L}=1$, the holomorphic function $F-L$ takes values in the discrete set $2\pi i\mathbb Z$, hence is constant. Thus (F) extends.

This lemma explains why globally exponential counterterms cannot create hidden zeros at the removed channel points. Algebraic zero factors require a counterterm without a single-valued global logarithm and hence lie outside the declared class.

# Exact sign table

For clarity, the complete sign ledger is

  object                          logarithmic channel        residual after multiplication
  ------------------------------- -------------------------- -------------------------------
  relative channel $R_{\rm ch}$   $-c_m\Phi(t^m)$            ---
  genus $m-1$ multiplier          $+c_m\Phi(t^m)$            $0$
  genus $m$ multiplier            $+c_m\Phi(t^m)-2c_mt^m$    $-2c_mt^m$
  negative source                 $3/(4w)-(1/2)\log w-3/2$   ---
  forced source multiplier        $-3/(4w)+(1/2)\log w$      $-3/2$.

This table is also encoded verbatim in the machine-readable certificate.
