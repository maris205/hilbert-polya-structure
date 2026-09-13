---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-383-exact-euler-tail-partition-normal-form"
canonical_tex: "zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/main.pdf"
source_sha256: "b1030a1203685121ddc99504d0d8a5b389611b41e47a1009fea70a0215ab3bb3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Euler-Tail Partition Normal Form for the Square-Clock Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-383-exact-euler-tail-partition-normal-form/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Inside the fixed finite-clock, universally distance-two-safe phasewise lag-two class with $c_{11}(r)=0$ at every phase, we give an exact all-order normal form for the square-clock gap. With $$a_{j+1}=\frac1{p_{j+1}^{2}-1},\qquad
   P_r(y)=\sum_{j\ge y}a_{j+1}^{r},\qquad
   \Phi_c(y)=\sum_{r\ge1}\frac{c^rP_r(y)}r,$$ the finite Euler ratios and squarefree tail satisfy $$U_m^{(y)}=u_m e^{\Phi_{m-1}(y)},\qquad
   H_y=\frac4{\pi^2}e^{-\Phi_1(y)}.$$ Writing $$C(V)=1-2V_2+2V_3-\cdots-2V_8,
   \qquad W(V)=V_2-2V_3+\cdots+2V_8,$$ we prove $$\pi^2\bigl(B_\infty-G(q_y)\bigr)
   =2\bigl(C(u)-C(U^{(y)})\bigr)
    -4W(U^{(y)})\bigl(1-e^{-\Phi_1(y)}\bigr).$$ Every homogeneous coefficient is then compiled by a finite partition formula. The $m=2$ channel cancels at every nonempty partition, the first two layers recover RH-381 and RH-382 with the independent $P_2$ sign, and a new cubic block is displayed explicitly. If $\rho_y=7P_1(y)\le7/8$, then for every integer $D\ge1$ the remainder after total degree $D$ obeys $$|R_{D,y}|\le \frac{92}{3\pi^2}\rho_y^{D+1}
   <\frac{31}{\pi^2}\rho_y^{D+1}.$$ The proof is an absolutely convergent Euler-tail calculation, not a finite fit. It supplies no growing-clock theorem, active-$c_{11}$ cancellation, operator, prime-power trace, zero identification, or implication for the Riemann hypothesis.
author:
- RH research program
bibliography:
- references.bib
date: 'August 7, 2026'
title: |
  An Exact Euler-Tail Partition Normal Form\
  for the Square-Clock Gap
```

## Markdown 正文

**Keywords:** Möbius function; prime-square Euler tail; integer partitions; exact power-sum expansion; finite clocks; uniform remainder.

# Frozen class and predecessor identities

We retain exactly the class and order of limits fixed in RH-379--RH-382 [@RH379; @RH380; @RH381; @RH382]. Nothing in this paper enlarges that class.

Fix an integer $q\ge1$ before taking $N\to\infty$. At every phase $r\in\mathbb Z/q\mathbb Z$, choose $$f_r:\{-1,0,1\}^2\longrightarrow\{-1,+1\},\qquad
 \epsilon_n=f_{n\bmod q}\bigl(\mu(n-2),\mu(n)\bigr).$$ The table is universally distance-two-safe if no ternary input can produce $\epsilon_n=\epsilon_{n+2}=+1$. We further require the RH-379 interpolation coefficient $c_{11}(r)$ of $\mu(n-2)\mu(n)$ to vanish at every phase. The exact optimum after the fixed-$q$ prefix limit is denoted by $G(q)$.

An active $c_{11}(r)$ produces a phase-weighted shift-two Möbius correlation. No theorem in the frozen source set controls that term, so it is excluded rather than averaged away.

Let $3=p_1<p_2<\cdots$ be the odd primes and, for $1\le m\le9$, put $$E_m^{(y)}=\prod_{i\le y}\left(1-\frac m{p_i^2}\right),
 \qquad
 U_m^{(y)}=\frac{E_m^{(y)}}{E_1^{(y)}}\quad(1\le m\le8).
 \label{eq:finite-ratios}$$ The limiting ratios are $$e_m=\prod_{p\ \mathrm{odd}}\left(1-\frac m{p^2}\right),
 \qquad u_m=\frac{e_m}{e_1}.
 \label{eq:limit-ratios}$$ For $m\le8$ all factors used below are positive; $E_9^{(y)}=0$ is handled separately. RH-374 supplies $e_1=8/\pi^2$ and the finite run formula; RH-379 supplies the memory correction [@RH374; @RH379]. Put $A_y=\prod_{i\le y}(p_i^2-1)$, the positive-support count. If $O_y$ and $\mathcal E_y$ denote the odd-run and even-run counts, those formulas give $O_y/A_y=C(U^{(y)})$ and $\mathcal E_y/A_y=W(U^{(y)})$. In the notation $$\begin{aligned}
 C(V)&=1-2V_2+2V_3-2V_4+2V_5-2V_6+2V_7-2V_8,\\
 W(V)&=V_2-2V_3+2V_4-2V_5+2V_6-2V_7+2V_8,
 \label{eq:CW}\end{aligned}$$ their exact endpoint identities are $$B_y=\frac{4+2C(U^{(y)})}{\pi^2},\qquad
 B_\infty=\frac{4+2C(u)}{\pi^2},
 \label{eq:B-endpoints}$$ and $$G(q_y)=B_y+W(U^{(y)})\left(\frac4{\pi^2}-H_y\right),
 \qquad q_y=4\prod_{i\le y}p_i^2.
 \label{eq:G-endpoint}$$ These are frozen inputs, not conclusions inferred from the finite rows in Section [7](#sec:artifact){reference-type="ref" reference="sec:artifact"}.

The terminal run convention also remains frozen. Put $\mathcal P_y=\prod_{i\le y}p_i^2$. Second differences are used only for lengths $1\le\ell\le7$, $$R_\ell=\mathcal P_y(E_\ell-2E_{\ell+1}+E_{\ell+2}),$$ whereas $R_8=\mathcal P_yE_8$ is separate. The factor at $p=3$ gives $E_9=0$ in the licensed length-seven formula. No $E_{10}$ is defined or needed.

# Absolute Euler-tail coordinates

For $y\ge1$, set $$a_{j+1}=\frac1{p_{j+1}^2-1},\qquad
 P_r(y)=\sum_{j\ge y}a_{j+1}^r,\qquad
 T_y=P_1(y).
 \label{eq:power-sums}$$ Because the odd primes beyond $3$ form a subset of the odd integers at least $5$, $$0<T_y\le\sum_{k\ge2}\frac1{(2k+1)^2-1}
 =\frac14\sum_{k\ge2}\left(\frac1k-\frac1{k+1}\right)=\frac18.
 \label{eq:T-bound}$$ Also $a_{j+1}\le1/24$. For $0\le c\le7$, define $$\Phi_c(y)=\sum_{r\ge1}\frac{c^rP_r(y)}r.
 \label{eq:Phi}$$

[\[lem:absolute\]]{#lem:absolute label="lem:absolute"} For every $y\ge1$ and $0\le c\le7$, the series [\[eq:Phi\]](#eq:Phi){reference-type="eqref" reference="eq:Phi"} converges absolutely and $$\mathsf A_c(y):=e^{\Phi_c(y)}
 =\prod_{j\ge y}(1-ca_{j+1})^{-1},
 \qquad
 \mathsf F_c(y):=e^{\Phi_c(y)-\Phi_1(y)}
 =\prod_{j\ge y}\frac{1-a_{j+1}}{1-ca_{j+1}}.
 \label{eq:AF}$$ All rearrangements into homogeneous power-sum series used below are absolutely convergent.

Since $ca_{j+1}\le7/24<1$, $$\sum_{j\ge y}\sum_{r\ge1}\frac{(ca_{j+1})^r}{r}
 \le \frac{c}{1-7/24}\sum_{j\ge y}a_{j+1}<\infty.$$ Thus Tonelli's theorem applies to the nonnegative absolute majorant, and the logarithmic product identities give [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"}. The signed series for $e^{-\Phi_1}$ is absolutely dominated by $e^{\Phi_1}$; multiplying by the finitely many $m$-channels preserves absolute convergence.

[\[thm:endpoint\]]{#thm:endpoint label="thm:endpoint"} For every $y\ge1$ and $2\le m\le8$, $$U_m^{(y)}=u_m e^{\Phi_{m-1}(y)},
 \qquad H_y=\frac4{\pi^2}e^{-\Phi_1(y)}.
 \label{eq:ratio-H}$$ Consequently $$\boxed{\;
 \pi^2\bigl(B_\infty-G(q_y)\bigr)
 =2\bigl(C(u)-C(U^{(y)})\bigr)
  -4W(U^{(y)})\bigl(1-e^{-\Phi_1(y)}\bigr).\;}
 \label{eq:normal-form}$$

Factorwise division of [\[eq:limit-ratios\]](#eq:limit-ratios){reference-type="eqref" reference="eq:limit-ratios"} by [\[eq:finite-ratios\]](#eq:finite-ratios){reference-type="eqref" reference="eq:finite-ratios"} gives $$\frac{u_m}{U_m^{(y)}}
 =\prod_{j\ge y}\frac{p_{j+1}^2-m}{p_{j+1}^2-1}
 =\prod_{j\ge y}\bigl(1-(m-1)a_{j+1}\bigr).$$ Lemma [\[lem:absolute\]](#lem:absolute){reference-type="ref" reference="lem:absolute"} gives the first identity. The frozen squarefree tail product gives $$\frac{\pi^2H_y}{4}=\prod_{j\ge y}(1-a_{j+1})=e^{-\Phi_1(y)},$$ which is the second. Substitute these identities into [\[eq:B-endpoints\]](#eq:B-endpoints){reference-type="eqref" reference="eq:B-endpoints"}--[\[eq:G-endpoint\]](#eq:G-endpoint){reference-type="eqref" reference="eq:G-endpoint"} and subtract from $B_\infty$.

# The finite partition compiler

Let $\lambda=1^{k_1}\cdots d^{k_d}$ be a partition of total degree $|\lambda|=\sum_r rk_r=d$. Write $$\ell(\lambda)=\sum_r k_r,\qquad
 P_\lambda(y)=\prod_rP_r(y)^{k_r},\qquad
 z_\lambda=\prod_r r^{k_r}k_r!.
 \label{eq:partition-data}$$ The exponential formula and Lemma [\[lem:absolute\]](#lem:absolute){reference-type="ref" reference="lem:absolute"} give $$\mathsf A_c(y)=\sum_\lambda\frac{c^{|\lambda|}}{z_\lambda}P_\lambda(y),
 \qquad
 \mathsf F_c(y)=\sum_\lambda
 \frac{\prod_r(c^r-1)^{k_r}}{z_\lambda}P_\lambda(y),
 \label{eq:partition-AF}$$ where the empty partition contributes $1$.

Index the endpoint coefficient arrays by $m=2,\ldots,8$: $$(\alpha_m)=(-2,2,-2,2,-2,2,-2),\qquad
 (\beta_m)=(1,-2,2,-2,2,-2,2).
 \label{eq:alpha-beta}$$

[\[thm:partition\]]{#thm:partition label="thm:partition"} The absolutely convergent expansion $$\pi^2\bigl(B_\infty-G(q_y)\bigr)
 =\sum_{d\ge1}\ \sum_{\lambda\vdash d}
 \gamma_\lambda P_\lambda(y)
 \label{eq:partition-normal-form}$$ has the finite exact coefficient compiler $$\boxed{\begin{aligned}
 \gamma_\lambda={}&-\frac2{z_\lambda}
   \sum_{m=2}^8\alpha_m u_m(m-1)^d\\
 &-\frac4{z_\lambda}\sum_{m=2}^8\beta_m u_m
 \left((m-1)^d-\prod_r\bigl((m-1)^r-1\bigr)^{k_r}\right).
\end{aligned}}
 \label{eq:gamma}$$ For every nonempty partition, the $m=2$ summand in [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"} is exactly zero.

Write $c=m-1$. From [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"}, $$\begin{aligned}
 2(C(u)-C(U^{(y)}))
   &=-2\sum_{m=2}^8\alpha_mu_m(\mathsf A_c-1),\\
 -4W(U^{(y)})(1-e^{-\Phi_1})
   &=-4\sum_{m=2}^8\beta_mu_m(\mathsf A_c-\mathsf F_c).\end{aligned}$$ Insert [\[eq:partition-AF\]](#eq:partition-AF){reference-type="eqref" reference="eq:partition-AF"}; the coefficient of each nonempty $P_\lambda$ is [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}. Absolute convergence was proved in Lemma [\[lem:absolute\]](#lem:absolute){reference-type="ref" reference="lem:absolute"}, so coefficient collection and the finite $m$-sums are legitimate.

For $m=2$ one has $c=1$, $\alpha_2=-2$, and $\beta_2=1$. Because $\lambda$ is nonempty, $$\prod_r(1^r-1)^{k_r}=0.$$ The two terms are therefore $4u_2/z_\lambda$ and $-4u_2/z_\lambda$, proving exact cancellation at every order.

The coefficient of $P_\lambda$ in $e^{-\Phi_1}$ is $(-1)^{\ell(\lambda)}/z_\lambda$; in $1-e^{-\Phi_1}$ it is $(-1)^{\ell(\lambda)+1}/z_\lambda$. Total-degree parity is not a termwise substitute. For a finite set of tail variables, cancellation after summing all partitions of degree $n$ gives the different-basis identity $$\sum_{\lambda\vdash n}\frac{(-1)^{\ell(\lambda)}}{z_\lambda}P_\lambda
 =(-1)^ne_n.$$ The executable $Q$ oracle checks both sides independently; it does not replace the length sign in [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}.

# Independent increment and telescope compilers

The coefficient formula above comes from the endpoint $C/W$ form. We now recover it from the frozen increment law, both to expose the successor-tail index and to prepare the uniform remainder bound. Define the *increment* arrays $$(\xi_m)_{m=4}^8=(2,-4,6,-8,10),\qquad
 (\eta_m)_{m=3}^8=(2,-4,6,-8,10,-12).
 \label{eq:xi-eta}$$ They are not the endpoint arrays $\alpha,\beta$ in [\[eq:alpha-beta\]](#eq:alpha-beta){reference-type="eqref" reference="eq:alpha-beta"}.

RH-380--RH-382 give, after every fixed-clock limit has already been taken, $$\begin{aligned}
 \pi^2(B_\infty-G(q_y))
 =\sum_{j\ge y}\biggl[&2a_{j+1}X_j
 +4a_{j+1}\frac{M_j}{A_j}d_{j+1}\biggr],\\
 X_j&=\sum_{m=4}^8\xi_mU_m^{(j)},\qquad
 \frac{M_j}{A_j}=\sum_{m=3}^8\eta_mU_m^{(j)},\\
 d_{j+1}&=1-e^{-\Phi_1(j+1)}.
\end{aligned}
 \label{eq:increment}$$ The strict successor $j+1$ in $d_{j+1}$ is essential.

For a finite tail, let $h_r^{(j)}$ be the complete homogeneous polynomial of degree $r$ in the current suffix $\{a_{k+1}:k\ge j\}$, and let $e_s^{(j+1)}$ be the elementary polynomial in the strict successor suffix. After a common scale $t$ is inserted into all $a$'s, the degree-$n$ increment channels are $$\begin{aligned}
 \Gamma_{X,n}
 &=2\sum_{m=4}^8\xi_mu_m\sum_{j\ge y}
 a_{j+1}(m-1)^{n-1}h_{n-1}^{(j)},
 \label{eq:Gamma-X}\\
 \Gamma_{M,n}
 &=4\sum_{m=3}^8\eta_mu_m
 \sum_{\substack{r+s=n-1\\r\ge0,\ s\ge1}}
 \sum_{j\ge y}a_{j+1}(m-1)^rh_r^{(j)}
 (-1)^{s+1}e_s^{(j+1)}.
 \label{eq:Gamma-M}\end{aligned}$$ The infinite version follows by absolute convergence. Equations [\[eq:Gamma-X\]](#eq:Gamma-X){reference-type="eqref" reference="eq:Gamma-X"}--[\[eq:Gamma-M\]](#eq:Gamma-M){reference-type="eqref" reference="eq:Gamma-M"} are the independent $\Gamma/h/e/\Phi$ compiler.

There is also a direct telescope. For $c\ge2$, factorwise differences give $$\begin{aligned}
 \sum_{j\ge y}a_{j+1}\mathsf A_c(j)
 &=\frac{\mathsf A_c(y)-1}{c},
 \label{eq:A-telescope}\\
 \sum_{j\ge y}a_{j+1}\mathsf A_c(j)e^{-\Phi_1(j+1)}
 &=\frac{\mathsf F_c(y)-1}{c-1}.
 \label{eq:F-telescope}\end{aligned}$$ Indeed, the summands are respectively the successive differences of $\mathsf A_c/c$ and $\mathsf F_c/(c-1)$. Thus the two increment channels equal $$\begin{aligned}
 &2\sum_{m=4}^8\frac{\xi_m}{m-1}u_m(\mathsf A_{m-1}-1),
 \label{eq:X-AF}\\
 &4\sum_{m=3}^8\eta_mu_m\left(
 \frac{\mathsf A_{m-1}-1}{m-1}
 -\frac{\mathsf F_{m-1}-1}{m-2}\right).
 \label{eq:M-AF}\end{aligned}$$ Direct coefficient comparison shows that [\[eq:X-AF\]](#eq:X-AF){reference-type="eqref" reference="eq:X-AF"}--[\[eq:M-AF\]](#eq:M-AF){reference-type="eqref" reference="eq:M-AF"} sum to the $C/W$ compiler [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}. Explicitly, after extending $\xi_m$ and $\eta_m$ by zero outside their displayed ranges, $$\xi_m=-\alpha_m(m-1)-2\beta_m,
 \qquad \eta_m=-\beta_m(m-2)\qquad(2\le m\le8).$$ These two finite identities make the bridge coefficientwise. This is the third, $\mathsf A_c/\mathsf F_c$ telescope oracle. The $m=2$ endpoint cancellation is handled before these $c-1$ denominators appear.

# Low orders and the new cubic block

Set $$\begin{aligned}
 X_\infty&=2u_4-4u_5+6u_6-8u_7+10u_8,\\
 Y_\infty&=6u_4-16u_5+30u_6-48u_7+70u_8,\\
 m_\infty&=2u_3-4u_4+6u_5-8u_6+10u_7-12u_8.
 \label{eq:XYm}\end{aligned}$$ Applying [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"} to the partitions of degrees one and two gives $$\gamma_{(1)}=2X_\infty,\qquad
 \gamma_{(1,1)}=Y_\infty+2m_\infty,
 \qquad
 \gamma_{(2)}=Y_\infty-2m_\infty.
 \label{eq:low-orders}$$ Since $P_{(1,1)}=T_y^2$ and $P_{(2)}=P_2(y)$, these are exactly the RH-381 leading layer and RH-382 two-scale quadratic layer. In particular, $P_2(y)$ is not collapsed into a multiple of $T_y^2$, and its memory sign is opposite to the $T_y^2$ sign.

The first genuinely new homogeneous layer is cubic: $$\begin{aligned}
 \gamma_{(1,1,1)}={}&4u_3-\frac{22}{3}u_4+\frac{20}{3}u_5+2u_6
 -\frac{68}{3}u_7+\frac{178}{3}u_8,
 \label{eq:cubic111}\\
 \gamma_{(2,1)}={}&4u_3+10u_4-52u_5+134u_6-268u_7+466u_8,
 \label{eq:cubic21}\\
 \gamma_{(3)}={}&-8u_3+\frac{100}{3}u_4-\frac{248}{3}u_5+164u_6
 -\frac{856}{3}u_7+\frac{1364}{3}u_8.
 \label{eq:cubic3}\end{aligned}$$ Thus the cubic contribution is $$\gamma_{(1,1,1)}T_y^3
 +\gamma_{(2,1)}T_yP_2(y)
 +\gamma_{(3)}P_3(y).$$ These identities follow symbolically from [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}; no regression or numerical coefficient recognition is used.

# Uniform arbitrary-order remainder

Put $$\rho_y=7T_y\le\frac78.
 \label{eq:rho}$$ This analytic tail radius is not the square clock $q_y$. Let $R_{D,y}$ be the remainder in $B_\infty-G(q_y)$ after all partitions of total degree at most an integer $D\ge1$ have been retained.

[\[thm:remainder\]]{#thm:remainder label="thm:remainder"} For every $y\ge1$ and every integer $D\ge1$, $$\boxed{
 |R_{D,y}|\le\frac{92}{3\pi^2}\rho_y^{D+1}
 <\frac{31}{\pi^2}\rho_y^{D+1}.}
 \label{eq:remainder}$$

The $p=3$ factor in $u_m$ and positivity of all later factors give $$0<u_m\le\frac{9-m}{8}\qquad(2\le m\le8).$$ For the increment arrays in [\[eq:xi-eta\]](#eq:xi-eta){reference-type="eqref" reference="eq:xi-eta"}, this yields the distinct absolute ledgers $$\sum_{m=4}^8|\xi_m|u_m\le\frac{35}{4},
 \qquad
 \sum_{m=3}^8|\eta_m|u_m\le14.
 \label{eq:increment-ledgers}$$ The constants $35/4$ and $14$ belong to $\xi$ and $\eta$, not to the endpoint arrays $\alpha$ and $\beta$.

For nonnegative tail variables, $$h_r^{(j)}\le T_j^r,\qquad
 e_s^{(j+1)}\le\frac{T_{j+1}^s}{s!},
 \qquad \sum_{j\ge y}a_{j+1}=T_y.$$ The degree-$n$ numerator layer [\[eq:Gamma-X\]](#eq:Gamma-X){reference-type="eqref" reference="eq:Gamma-X"} therefore satisfies $$|\Gamma_{X,n}|
 \le2\frac{35}{4}\,7^{n-1}T_y^n
 =\frac52\rho_y^n.$$ For the memory layer, write $r+s=n-1$ with $s\ge1$. Each fixed $s$ contributes at most $$4\cdot14\,\frac{7^{n-s-1}T_y^n}{s!}
 =4\cdot14\,\frac{\rho_y^n}{7^{s+1}s!}.$$ Since $$\sum_{s\ge1}\frac1{7^{s+1}s!}
 \le\sum_{s\ge1}\frac1{7^{s+1}}=\frac1{42},$$ we obtain $|\Gamma_{M,n}|\le(4/3)\rho_y^n$; for $n=1$ this channel is zero. Consequently the $\pi^2$-scaled tail after degree $D$ is bounded by $$\left(\frac52+\frac43\right)
 \sum_{n>D}\rho_y^n
 \le\frac{23}{6}\cdot8\rho_y^{D+1}
 =\frac{92}{3}\rho_y^{D+1}.$$ Divide by $\pi^2$. Finally $92/3<31$.

Theorem [\[thm:remainder\]](#thm:remainder){reference-type="ref" reference="thm:remainder"} is uniform in arbitrary order. It does not replace, inherit, or claim to sharpen RH-381's quadratic constant $342$ or RH-382's cubic constant $3301/6$. Those papers use cancellations tailored to their fixed truncation orders.

# Executable protocol and adversarial checks {#sec:artifact}

The artifact uses only exact rational arithmetic. Its source contract locks $41$ immutable files: groups of sizes $7,8,8,8,8,2$ from RH-374, RH-379, RH-380, RH-381, RH-382, and the four-volume synthesis archive. Every live input is checked byte-for-byte against its declared Git release. Mutable root policy and handoff files are deliberately excluded.

Three independently organized oracles are compared:

1.  the canonical endpoint $C/W$ partition compiler [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"};

2.  the ordered-increment $\Gamma/h/e/\Phi$ compiler [\[eq:Gamma-X\]](#eq:Gamma-X){reference-type="eqref" reference="eq:Gamma-X"}--[\[eq:Gamma-M\]](#eq:Gamma-M){reference-type="eqref" reference="eq:Gamma-M"}, with the strict successor tail; and

3.  the direct $\mathsf A_c/\mathsf F_c$ telescope compiler [\[eq:A-telescope\]](#eq:A-telescope){reference-type="eqref" reference="eq:A-telescope"}--[\[eq:M-AF\]](#eq:M-AF){reference-type="eqref" reference="eq:M-AF"}.

The frozen exact grid is summarized in Table [1](#tab:protocol){reference-type="ref" reference="tab:protocol"}.

::: {#tab:protocol}
  --------------------------------------------------------------------------------------------------------------------------------------
  check                                     rows scope
  ------------------------------------ --------- ---------------------------------------------------------------------------------------
  endpoint normal form                        67 starts $1\le s<e$ at $e\in\{8,12,19,32\}$

  $\mathsf A/\mathsf F$ coefficients         864 six tails, $c=2,\ldots,7$, degrees $1,\ldots,12$, two functions

  $Q$ length-sign oracle                     432 72 tail/degree identities repeated under six inert $c$ labels

  partition gamma                           1084 271 unique partitions through degree 12, evaluated under four endpoint labels

  increment channels                         144 six tails, 12 degrees, numerator and memory

  low orders                                  33 endpoint-labeled bundles of the same three RH-381/RH-382 coefficient identities

  cubic block                            $67+12$ direct finite cubic rows plus three coefficients at four labels

  $m=2$ cancellation                        1151 $4\times271$ labeled symbolic rows plus 67 direct finite telescopes

  remainder                                  804 67 tails and every $1\le D\le12$

  terminal/successor                       $4+7$ $R_8,E_9,$ no $E_{10}$; strict $j+1$ telescope

  negative mutations                          20 wrong signs, denominators, factors, prefactors, channels, types, terminal, and $\rho$
  --------------------------------------------------------------------------------------------------------------------------------------

  : Exact reproduction and adversarial grid. Label repetitions are reported explicitly and are not counted as distinct mathematical theorems.
:::

The $20$ negative rows execute mutated compilers or complete formulas: degree parity in place of partition length, three wrong $z_\lambda$ denominators, current-tail memory, two endpoint normalizations, two broken $m=2$ coefficients, two cubic formula mutations, two increment coefficient mutations, Boolean/float/zero truncation orders, the forbidden $E_{10}$ terminal extension, and $\rho=T$ in place of $7T$. All are rejected. The closed Draft 2020--12 schema freezes every stored value and rejects numeric aliases, duplicate keys, nonfinite constants, extra members, and source-lock rebinding.

All finite rows in this section reproduce or attack identities already proved symbolically. They are not fits, asymptotic evidence, or evidence for a physical spectral model.

# Boundary and next theorem budget

The standalone discovery verdict is **Route A: GO**: the exact all-order coefficient compiler, absolute convergence, universal truncation bound, all-order $m=2$ cancellation, and cubic block are new theorem content inside the frozen class. The RH-compatibility verdict is **Route B: STOP\_SCOPED**. The normal form is an auxiliary arithmetic Euler-tail expansion, not a complex clock, intrinsic dynamical determinant, or Hilbert--Pólya operator.

The following claims are outside the theorem:

-   no nonzero phasewise $c_{11}(r)$ term is controlled;

-   no growing choice $q=q(N)$, exchange of limits, RH-377 adaptive envelope, or adaptive-capacity limit is proved;

-   no prime number theorem or rewrite in terms of $p_y$ is used;

-   no finite row is promoted to an all-$y$ theorem or physical signal;

-   no intrinsic operator, determinant, scattering completion, self-adjoint generator, von Mangoldt weighted prime-power trace, or completed-zeta divisor equality is constructed;

-   no Riemann zero is identified and the Riemann hypothesis is neither proved nor reduced to the present calculation.

Thus Gates A--E retain their frozen false/open status. Enlarging the active factor class requires a phase-weighted shift-two correlation theorem for nonzero $c_{11}$. Orthogonally, a within-class translation from the intrinsic tails $P_r(y)$ to a $p_y$ scale could be legitimate after independently source-locking a prime-counting theorem such as the RH-2 PNT input. A separate successor could then prove fixed-$r$ tail asymptotics and locate the independent $P_2$ scale relative to $T_y^3$. No such translation is used or proved here, and it would not promote an operator or RH Gate. Any different route must contribute its own source-backed theorem edge. The four-volume RH-1--RH-361 synthesis remains the preserved foundation rather than being replaced by this short paper [@RHMVP2].

# Declarations {#declarations .unnumbered}

#### Data and code availability.

All theorem inputs, exact source code, tests, closed result schema, source locks, and archive manifests are contained in the repository paper directory. No private dataset is used.

#### Author contributions.

The RH research program performed conceptualization, formal analysis, software construction, verification, artifact curation, adversarial review, and manuscript preparation.

#### Funding.

No external funding is declared.

#### Competing interests.

No competing interests are declared.

#### Ethics and human participants.

This mathematical and computational study uses no human participants, animals, or personal data; ethics approval and consent are not applicable.

#### AI assistance disclosure.

AI-assisted tools supported source triage, symbolic checking, deterministic artifact generation, drafting, and adversarial review. Every released claim is constrained by immutable repository sources and reproducible verification artifacts; responsibility for the scoped mathematical statements remains with the research program.
