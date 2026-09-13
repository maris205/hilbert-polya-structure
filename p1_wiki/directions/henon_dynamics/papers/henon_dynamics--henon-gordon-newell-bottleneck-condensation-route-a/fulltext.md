---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-gordon-newell-bottleneck-condensation-route-a"
canonical_tex: "henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a/paper/main.pdf"
source_sha256: "c3420623bf2e9bd05bf288fd7e74fc6bd88a87673e5405cc8f1287a4ef96b271"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Canonical Flow and Bottleneck Condensation in Finite Gordon--Newell Networks

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_gordon_newell_bottleneck_condensation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite irreducible routing matrix, without assuming reversibility, we give a self-contained closure of the single-class Gordon--Newell network. The canonical partition function is the complete homogeneous polynomial $Z_N=h_N(w)$; its derivatives give every joint occupancy moment, while $Z_{N-1}/Z_N$ gives every station throughput and directed service-event flow. The stationary reverse routing is obtained exactly and yields a sharp reversibility criterion. \>0We further prove the complete thermodynamic limit: nonbottleneck occupancies become independent geometric variables, whereas tied bottleneck shares converge to an independent $\operatorname{Dirichlet}(1,\ldots,1)$ vector; a unique bottleneck is the degenerate case. \>1Zero population, one customer, one station, zero routing edges, self-routes, equal weights, traffic gauge, and singular zero-rate faces are separated, and an exact hostile executable certificate is closed. Gordon and Newell own the classical product-form and bottleneck lineage; no literature originality, arithmetic determinant, or quantization is claimed.
author:
- |
  Route-A source-local certificate HCS-C285\
  Revision round 2
date: 2 September 2026
title: |
  Canonical Flow and Bottleneck Condensation\
  in Finite Gordon--Newell Networks
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2852026090200000000000000000000\>\<C2852026090200000000000000000000\>\]

# Frozen owner and classical lineage

Fix $m\geq1$, $N\in\mathbb Z_{\geq 0}$, positive service rates $\mu_i$, and an irreducible row-stochastic matrix $P=(p_{ij})$. Zero entries and self-routes are allowed; $P$ need not satisfy detailed balance. On $$\mathcal S_N=\{n\in\mathbb Z_{\geq 0}^m:\ \textstyle\sum_i n_i=N\},$$ an occupied station $i$ completes service at total rate $\mu_i$ and sends the customer to $j$ with probability $p_{ij}$. Thus $$Lf(n)=\sum_{i:n_i>0}\mu_i\sum_jp_{ij}
       [f(n-e_i+e_j)-f(n)].                              \tag{1}$$ When $i=j$, a service event occurs but the state does not change. This distinction matters for physical edge flows below.

Let $e$ be the unique positive traffic vector with $e=eP$ and $\sum_i e_i=1$, and put $w_i=e_i/\mu_i$. Gordon and Newell's paper is the classical equilibrium and bottleneck owner [@GordonNewell1967]. Kelly supplies the standard reversal framework [@Kelly1979], and Kelly--Yudovina give a modern queueing-network account [@KellyYudovina2014]. Those sources are cited for classical ownership and standard context; no literature originality is claimed. The proofs below are included to freeze the exact conventions and boundaries used by the certificate.

# Canonical law and all occupancy derivatives

Define $$Z_N=h_N(w)=[z^N]\prod_{i=1}^m(1-w_i z)^{-1}
     =\sum_{n\in\mathcal S_N}\prod_iw_i^{n_i},\qquad Z_0=1. \tag{2}$$

[\[thm:finite\]]{#thm:finite label="thm:finite"} The unique stationary probability is $$\pi_N(n)=Z_N^{-1}\prod_iw_i^{n_i}.                       \tag{3}$$ For $D_i=w_i\partial_{w_i}$, $$\mathbb En_i=D_i\log Z_N,
 \qquad \operatorname{Cov}(n_i,n_j)=D_iD_j\log Z_N.                   \tag{4}$$ For every multi-index $\alpha\in\mathbb Z_{\geq 0}^m$, $$\mathbb E\prod_i(n_i)_{\alpha_i}
 =\frac{w^\alpha\partial_w^\alpha Z_N}{Z_N}.            \tag{5}$$ Thus (5), followed by Stirling conversion, gives all joint ordinary moments.

For a fixed $n$, the outgoing nonself rate is $\sum_{j:n_j>0}\mu_j(1-p_{jj})$. An incoming jump with destination $j$ starts from $n-e_j+e_i$ and has weight ratio $w_i/w_j$. Its total stationary mass for this $j$ equals $$\pi_N(n)\sum_{i\ne j}\frac{w_i}{w_j}\mu_ip_{ij}
 =\pi_N(n)\frac{\mu_j}{e_j}\sum_{i\ne j}e_ip_{ij}
 =\pi_N(n)\mu_j(1-p_{jj}),$$ where $e=eP$ was used in the last equality. Summing over occupied $j$ proves global balance without reversibility. Strong connectivity makes the composition chain irreducible when $N>0$; $N=0$ is a singleton. Differentiating the finite sum (2) proves (4)--(5).

Equation (2) also gives two independent recurrences useful for exact reconstruction. If $p_k=\sum_iw_i^k$, then $$Nh_N=\sum_{k=1}^Np_kh_{N-k},\qquad h_0=1,                \tag{6}$$ while multiplying the $m$ truncated geometric series gives a convolution recurrence. Neither recurrence divides by $w_i-w_j$, so equal weights are regular.

# Throughput, directed currents, and time reversal

Put $R_N=Z_{N-1}/Z_N$ for $N\geq1$ and $R_0=0$. Decrementing coordinate $i$ in (2) gives $$\mathbb P(n_i>0)=w_iR_N,\quad
 T_i=\mu_i\mathbb P(n_i>0)=e_iR_N,\quad
 J_{ij}=e_ip_{ij}R_N.                                    \tag{7}$$ Here $J_{ij}$ counts service events, including $i=j$. Traffic balance gives $\sum_jJ_{ij}=\sum_jJ_{ji}=T_i$; hence $C_{ij}=J_{ij}-J_{ji}$ is an antisymmetric divergence-free current.

Define $$p^*_{ij}=\frac{e_jp_{ji}}{e_i}.                          \tag{8}$$

[\[thm:reverse\]]{#thm:reverse label="thm:reverse"} $P^*$ is irreducible and row-stochastic, has traffic vector $e$, and is the routing matrix of the stationary time-reversed occupancy process with the same service rates. Reversal is involutive. For $N\geq1$, the state process is reversible if and only if $$e_ip_{ij}=e_jp_{ji}\quad\hbox{for every }i,j,             \tag{9}$$ equivalently $P^*=P$. At $N=0$ the singleton chain is trivially reversible for every routing matrix and therefore cannot identify (9).

If $n'=n-e_i+e_j$, stationary rate reversal and (3) give $$q^{\rm rev}(n',n)=\frac{\pi_N(n)\mu_ip_{ij}}{\pi_N(n')}
 =\mu_j\frac{e_ip_{ij}}{e_j}=\mu_jp^*_{ji}.$$ The traffic equations imply the row sums and stationary vector of $P^*$; the same formula applied twice returns $P$. Positive population supplies a state transition along every routing edge, so detailed balance of the state chain is equivalent to (9). Reversed event flow is $J^*_{ij}=J_{ji}$.

\>0

# The complete bottleneck limit

Let $$w_*=\max_iw_i,\quad B=\{i:w_i=w_*\},\quad r=|B|,
 \quad C=B^c,\quad q_j=w_j/w_*\ (j\in C).                \tag{10}$$

[\[thm:condensation\]]{#thm:condensation label="thm:condensation"} For fixed $(m,P,\mu)$ and $N\to\infty$, $$Z_N\sim w_*^N\frac{N^{r-1}}{(r-1)!}
       \prod_{j\in C}(1-q_j)^{-1}.                       \tag{11}$$ Jointly, $$(n_C,n_B/N)\ \Longrightarrow\ (G,Y),                   \tag{12}$$ where $G_j$ are independent with $\mathbb P(G_j=k)=(1-q_j)q_j^k$, $Y\sim\operatorname{Dirichlet}(1,\ldots,1)$, and $G$ and $Y$ are independent. Convergence of $n_C$ is in total variation. For $r=1$, $N-n_b\Rightarrow\sum_{j\in C}G_j$, so the unique bottleneck contains $N-O_{\mathbb P}(1)$ customers. For $r>1$, the bottleneck total is $N-O_{\mathbb P}(1)$ but its station shares remain macroscopically random.

After scaling by $w_*^N$, write $$H_N=[z^N](1-z)^{-r}A(z),\qquad
 A(z)=\prod_{j\in C}(1-q_jz)^{-1}=\sum_{k\geq0}a_kz^k.$$ All $a_k$ are nonnegative and $\sum_ka_k=A(1)<\infty$. Hence $$H_N=\sum_{k=0}^Na_k\binom{N-k+r-1}{r-1}.                 \tag{13}$$ Divide by $\binom{N+r-1}{r-1}$. Each binomial ratio is at most one and tends to one for fixed $k$, so dominated convergence gives (11).

For fixed $k=(k_j)_{j\in C}$ with $|k|\leq N$, exact cancellation gives $$\mathbb P(n_C=k)=
 \frac{q^k\binom{N-|k|+r-1}{r-1}}{H_N}.                  \tag{14}$$ The limit of (14) is $\prod_{j\in C}(1-q_j)q_j^{k_j}$. Since these pointwise limiting masses sum to one, the convergence is total variation on the countable space.

Conditionally on $n_C=k$, let $M=N-|k|$. Every weak composition of $M$ over $B$ has identical weight and is therefore exactly uniform. For a multi-index $\beta$ on $B$, $$\mathbb E\!\left[\prod_{i\in B}(n_i)_{\beta_i}\mid M\right]
 =(M)_{|\beta|}\frac{(r-1)!\prod_i\beta_i!}
 {(r+|\beta|-1)!}.                                       \tag{15}$$ After division by $M^{|\beta|}$, (15) converges to the moments of the uniform Dirichlet distribution. Compactness of the simplex makes these moments determining. Total-variation tightness of $n_C$ yields $M/N\to1$ and, by conditioning first on each fixed $k$, independence in (12).

If all $m$ weights equal $w_*$, then $Z_N=\binom{N+m-1}{m-1}w_*^N$, the finite law is uniform on ${\cal S}_N$, and $n/N\Rightarrow\operatorname{Dirichlet}(1,\ldots,1)$. At $m=1$ this is the degenerate one-point Dirichlet law and $n_1=N$ exactly.

\>1

# Boundary atlas and executable closure

The admissible and singular faces are deliberately not merged:

  ---------------------------------------------------------------------------------------------------------
  face                   exact semantics
  ---------------------- ----------------------------------------------------------------------------------
  $N=0$                  singleton, $Z_0=1$, zero moments and event flows; routing criterion not inferred

  $N=1$                  categorical law $\mathbb P(n=e_i)=w_i/\sum_jw_j$

  $m=1$                  one state, $P=[1]$, $Z_N=w_1^N$; completions are self-events

  $p_{ij}=0$             allowed whenever the routing digraph stays strongly connected

  $p_{ii}>0$             included in $J_{ii}$, absent from off-diagonal generator rates

  tied/all-equal $w$     all maximizers retained; no singular weight difference

  $e\mapsto ce$          $w\mapsto cw$, $Z_N\mapsto c^NZ_N$; laws, reversal and flows invariant

  $\mu_i=0$ or $w_i=0$   excluded singular face; positivity is not replaced by formal infinity or zero

  reducible $P$          excluded; positive traffic and irreducible composition owners may fail
  ---------------------------------------------------------------------------------------------------------

Periodic embedded routing requires no aperiodicity assumption for this continuous-time theorem. Negative or nonintegral populations lie outside the state-space definition.

The canonical receipt contains 9 exact network cases and all 177 of their states, 165 joint factorial-moment cells through degree three, 9 flow and 9 reversal ledgers, 28 finite condensation rows, and 12 boundary rows. The producer-independent checker performs 11,628 assertions: before reconstructing Fraction traffic vectors, each complete generator and the full left nullspace of its transpose, three routes to $Z_N$, every stored moment and flow, and every asymptotic cell, it enforces exact JSON types and canonical rational text. SymPy checks 28 identities; two fresh paths reproduce all 158,346 evidence bytes; 64/64 hostile attacks are rejected. Finite cells are regression oracles and do not prove the all-parameter or $N\to\infty$ theorem.

# Collision audit, limitations, and Route-A verdict

The registry scan through C1--C283 found no closed routed Gordon--Newell canonical/condensation owner. C225 is a single finite M/M/1/K spectral chain; C263 is a reinforced Pólya urn; C220 is open TASEP; C246 is an AIMD perpetuity; C282 is a killed risk process; C181 is deterministic rotor routing. None owns the conjunction of (2)--(15).

This paper does not cover multiclass or multiserver networks, state-dependent service, open networks, zero service rates, or reducible routing. It does not claim to originate the classical product form, reversal theory, or bottleneck principle.

Ordinary station and service parameters provide no rational-prime carrier or logarithmic-prime clock. Stochastic jump paths provide no source-canonical isolated deterministic primitive-orbit ledger; $Z_N$ is a fixed-population normalizer, not a dynamical zeta or target determinant. No target divisor, functional equation, Weil form, or same-clock unitary Hilbert--Pólya lift is defined. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the exact tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},$$ overall `ROUTE_A_REJECTED`; Route B is false. No Euler factor, root number, target zero, or formal quantization is claimed.

9 William J. Gordon and Gordon F. Newell, *Closed Queuing Systems with Exponential Servers*, Operations Research 15(2) (1967), 254--265, [doi:10.1287/opre.15.2.254](https://doi.org/10.1287/opre.15.2.254). F. P. Kelly, *Reversibility and Stochastic Networks*, Wiley, Chichester, 1979; Cambridge University Press reissue, 2011, ISBN 978-1-107-40115-0, [authorized author-hosted edition](https://www.statslab.cam.ac.uk/~fpk1/BOOKS/kelly_book.html). Frank Kelly and Elena Yudovina, *Stochastic Networks*, Cambridge University Press, 2014, [doi:10.1017/CBO9781139565363](https://doi.org/10.1017/CBO9781139565363).
