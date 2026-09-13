---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-preferential-attachment-degree-martingale-route-a"
canonical_tex: "henon_dynamics/henon_preferential_attachment_degree_martingale_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_preferential_attachment_degree_martingale_route_a/paper/main.pdf"
source_sha256: "387a462bf5301e171cf4fa92d274416f4e55a09dd6e41c2833a4524da369361e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two Scales in a Convention-Locked Preferential-Attachment Tree: Fixed-Vertex Martingales and the Global Degree Profile

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_preferential_attachment_degree_martingale_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_preferential_attachment_degree_martingale_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_preferential_attachment_degree_martingale_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_preferential_attachment_degree_martingale_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the linear preferential-attachment tree started from one edge, with no self-loops, we join two scales in one boundary-complete theorem. Every fixed vertex has exact rising-factorial moments of all orders and a moment-determinate square-root limit, whereas every fixed degree population converges in $L^2$ to $4/[k(k+1)(k+2)]$. The proof keeps fixed-vertex degree and degree counts separate. An exact finite computation independently audits the recurrences but is not used to infer either asymptotic theorem.
author:
- 'HCS-C321 theorem-and-evidence package'
date: '3 September 2026 --- revision round 2'
title: |
  Two Scales in a Convention-Locked Preferential-Attachment Tree:\
  Fixed-Vertex Martingales and the Global Degree Profile
```

## Markdown 正文

# Frozen process and exact local law

Let $T_2$ consist of the single edge $\{1,2\}$. Given $T_n$, add vertex $n+1$ and connect it to exactly one old vertex $v$, chosen with probability $$\Pr(v\mid T_n)=\frac{d_v(n)}{2(n-1)}.$$ Thus there are no loops or multiple edges, $n$ is the vertex-count clock, and $\sum_{v\leq n}d_v(n)=2(n-1)$. Write $D_i(n)=d_i(n)$ for one fixed vertex, $N_k(n)=\#\{v\leq n:d_v(n)=k\}$ for a population, and $$s_i=\begin{cases}2,&i=1,2,\\i,&i\geq3.\end{cases}$$ This precise convention matters: several standard formulations use a self-loop or a linearized-chord-diagram seed [@ba; @bollobas]. Fixed-vertex limit lineage is discussed by Backhausz [@backhausz]; the constants below are nevertheless derived for the declared one-edge process.

For $x^{\overline r}=x(x+1)\cdots(x+r-1)$, the identity $(d+1)^{\overline r}-d^{\overline r}=r d^{\overline r}/d$ gives $$\label{eq:factor-step}
 \mathbb E[D_i(n+1)^{\overline r}\mid T_n]
 =\left(1+\frac{r}{2(n-1)}\right)D_i(n)^{\overline r}.$$

[\[thm:moments\]]{#thm:moments label="thm:moments"} For every integer $r\geq1$ and $n\geq s_i$, $$\label{eq:moments}
 \mathbb ED_i(n)^{\overline r}
 =r!\frac{\Gamma(n-1+r/2)}{\Gamma(n-1)}
 \frac{\Gamma(s_i-1)}{\Gamma(s_i-1+r/2)}.$$

Every vertex has degree one at its birth time, so its initial rising factorial is $r!$. Iterating [\[eq:factor-step\]](#eq:factor-step){reference-type="eqref" reference="eq:factor-step"} and converting the finite product to a gamma quotient proves [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}.

\>0

# The fixed-vertex limit

Put $$a_{s,n}=\prod_{t=s}^{n-1}\left(1+\frac1{2(t-1)}\right).$$ Equation [\[eq:factor-step\]](#eq:factor-step){reference-type="eqref" reference="eq:factor-step"} at $r=1$ makes $M_i(n)=D_i(n)/a_{s_i,n}$ a nonnegative martingale.

[\[thm:local-limit\]]{#thm:local-limit label="thm:local-limit"} For every fixed $i$, there is a nonnegative $Z_i$ such that $D_i(n)/\sqrt n\to Z_i$ almost surely and in $L^p$ for every finite $p$. For each integer $r\geq1$, $$\label{eq:limit-moments}
 \mathbb EZ_i^r=\frac{r!\,\Gamma(s_i-1)}{\Gamma(s_i-1+r/2)}.$$ These moments determine the law of $Z_i$.

For every integer $q$, $D^q\leq D^{\overline q}$ and Theorem [\[thm:moments\]](#thm:moments){reference-type="ref" reference="thm:moments"} gives $\mathbb ED_i(n)^q=O(n^{q/2})$. Since $a_{s_i,n}\asymp\sqrt n$, $(M_i(n))$ is bounded in every $L^q$. Martingale convergence and uniform integrability, choosing an integer $q>p$, give almost-sure and every-finite-$L^p$ convergence. Moreover $$\frac{a_{s,n}}{\sqrt n}\longrightarrow
 \frac{\Gamma(s-1)}{\Gamma(s-1/2)},$$ which transfers the convergence to $D_i(n)/\sqrt n$.

The difference $D^{\overline r}-D^r$ has degree at most $r-1$ in $D$. Divide its expectation by $n^{r/2}$ and use the lower-order moment bounds; then apply gamma asymptotics to [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}. Uniform integrability at order $r$ follows from the order-$r+1$ bound, proving [\[eq:limit-moments\]](#eq:limit-moments){reference-type="eqref" reference="eq:limit-moments"}. Finally, for $m_{2r}=\mathbb EZ_i^{2r}$, Stirling's formula gives $$m_{2r}^{-1/(2r)}=
 \left(\frac{(2r)!\Gamma(s_i-1)}{\Gamma(s_i-1+r)}\right)^{-1/(2r)}
 \geq c_i r^{-1/2}$$ for all sufficiently large $r$. Carleman's sum diverges, proving moment determinacy.

# The global population scale

Set $N_0(n)=0$. The newborn contributes to class one, and selection of an old degree-$k-1$ or degree-$k$ vertex moves one vertex into or out of class $k$. Hence $$\label{eq:drift}
 \mathbb E[\Delta N_k\mid T_n]=\mathbf 1_{\{k=1\}}+
 \frac{(k-1)N_{k-1}(n)-kN_k(n)}{2(n-1)},\qquad |\Delta N_k|\leq1.$$

[\[thm:profile\]]{#thm:profile label="thm:profile"} For every fixed $k\geq1$, $$\frac{N_k(n)}n\longrightarrow p_k=\frac4{k(k+1)(k+2)}
 \quad\hbox{in }L^2.$$ Furthermore $\sum_{k\geq1}p_k=1$ and $\sum_{k\geq1}kp_k=2$.

The equilibrium equation from [\[eq:drift\]](#eq:drift){reference-type="eqref" reference="eq:drift"} is $p_k=\mathbf 1_{\{k=1\}}+[(k-1)p_{k-1}-kp_k]/2$. It gives $p_1=2/3$ and $p_k=(k-1)p_{k-1}/(k+2)$, hence the displayed formula.

For the $L^2$ assertion, define $\xi_{k,n+1}=\Delta N_k-\mathbb E[\Delta N_k\mid T_n]$ and $U_{k,n}=N_k(n)-np_k$. Then $\mathbb E(\xi_{k,n+1}\mid T_n)=0$, $|\xi_{k,n+1}|\leq2$, and $$\label{eq:U}
 U_{k,n+1}=a_nU_{k,n}+b_nU_{k-1,n}+r_n+\xi_{k,n+1},$$ where $a_n=1-k/[2(n-1)]$, $b_n=(k-1)/[2(n-1)]$, and $r_n=(p_k-\mathbf 1_{\{k=1\}})/(n-1)$.

We prove $\mathbb EU_{k,n}^2=O_k(n)$ by induction on $k$, beginning at a finite $n_0(k)$; earlier times enter the constant. After conditioning and squaring [\[eq:U\]](#eq:U){reference-type="eqref" reference="eq:U"}, all cross terms with $\xi$ vanish and its variance is at most four. Fix $0<\eta<k/2$. Young's inequality gives $$2|a_nU_{k,n}(b_nU_{k-1,n}+r_n)|
 \leq \frac{\eta}{n}U_{k,n}^2+\frac{n}{\eta}
       (b_nU_{k-1,n}+r_n)^2.$$ For $k=1$ the $b_n$ term is absent. At the induction step, $\mathbb EU_{k-1,n}^2\leq C_{k-1}n$ implies $$\mathbb E(b_nU_{k-1,n}+r_n)^2
 \leq2b_n^2C_{k-1}n+2r_n^2=O_k(n^{-1}).$$ Because $a_n^2=1-k/n+O_k(n^{-2})$, enlarge $n_0(k)$ so that $a_n^2+\eta/n\leq1-c_k/n$ for some $c_k>0$. Thus $\mathbb EU_{k,n+1}^2\leq(1-c_k/n)\mathbb EU_{k,n}^2+C_k$. An induction on $n$ yields $\mathbb EU_{k,n}^2\leq C'_kn$, and division by $n^2$ proves the claim. Finally the two sums follow from the telescoping identities $$\sum_{k=1}^Kp_k=1-\frac2{(K+1)(K+2)},\qquad
 \sum_{k=1}^Kkp_k=2-\frac4{K+2}.$$

Theorems [\[thm:local-limit\]](#thm:local-limit){reference-type="ref" reference="thm:local-limit"} and [\[thm:profile\]](#thm:profile){reference-type="ref" reference="thm:profile"} expose two distinct scales: each fixed old vertex is a square-root hub, while the empirical degree population has a normalized cubic-tail profile. This paper makes no claim about the maximum degree, joint hub laws, $m>1$, or uniformity as $k$ grows with $n$.

\>1

# Exact evidence and Route-A boundary

Exact rational dynamic programming records every labeled degree-vector law for $2\leq n\leq9$, 352 fixed-vertex factorial cells, 36 degree-population moment cells, and the terminal distribution. A producer-independent program enumerates all $8!=40{,}320$ weighted parent histories and reconstructs every receipt. Separate symbolic, replay, strict-parser, repaired-hash mutation, and optimized-mode gates close the audit. This finite computation is regression evidence, not a proof of the limits above.

The nearest repository models are a Pólya urn, a fixed-size uniform random mapping, and independent-edge Erdős--Rényi connectivity. None owns this sequential degree-biased labeled-tree process. No literature-priority claim is made.

The Route-A tuple is $(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
\mathrm{FAIL},\mathrm{FAIL})$: there is no rational-prime carrier, deterministic primitive-orbit ledger, zeta/divisor bridge, target functional equation, or natural unitary/scattering/Hamiltonian lift. The verdict is `ROUTE_A_REJECTED`, and Route B is locked. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, we assert no target arithmetic local data, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Pólya operator.

# Revision certificate: convention and exact factorial law {#revision-certificate-convention-and-exact-factorial-law .unnumbered}

This original round freezes the one-edge model and proves every finite-time rising-factorial identity.

# Revision certificate: both microscopic and macroscopic limits {#revision-certificate-both-microscopic-and-macroscopic-limits .unnumbered}

This round adds the square-root martingale limit, Carleman determinacy, and the global $L^2$ degree profile with its explicit second-moment induction.

# Revision certificate: independent evidence and scope closure {#revision-certificate-independent-evidence-and-scope-closure .unnumbered}

This final round adds weighted-history reconstruction, source and collision audits, hostile gates, and the complete Route-A firewall.

9 A.-L. Barabási and R. Albert, "Emergence of scaling in random networks," *Science* 286 (1999), DOI: 10.1126/science.286.5439.509. B. Bollobás, O. Riordan, J. Spencer, and G. Tusnády, "The degree sequence of a scale-free random graph process," *Random Structures Algorithms* 18 (2001), DOI: 10.1002/rsa.1009. Á. Backhausz, "Limit distribution of degrees in random family trees," *Electron. Commun. Probab.* 16 (2011), DOI: 10.1214/ECP.v16-1598.
