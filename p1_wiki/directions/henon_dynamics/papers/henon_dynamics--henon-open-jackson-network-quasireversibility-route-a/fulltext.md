---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-jackson-network-quasireversibility-route-a"
canonical_tex: "henon_dynamics/henon_open_jackson_network_quasireversibility_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_jackson_network_quasireversibility_route_a/paper/main.pdf"
source_sha256: "9b2d7589e0a8200ed6a864d3843dcb46181829384d900641152d46e58c93d292"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Product Form, Time Reversal, and External Departure Flows in an Open Jackson Network

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_jackson_network_quasireversibility_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_jackson_network_quasireversibility_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_jackson_network_quasireversibility_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_jackson_network_quasireversibility_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a finite open network of single-server exponential queues, we prove the exact traffic solution, product-geometric invariant law, and stability criterion in one fixed row-vector convention. \>0 We compute every parameter of the stationary reversed Jackson network, including the routing-index reversal and nodes without direct exits. \>1 A truncated-drift argument closes the critical and overloaded faces. Time reversal then proves that the external departure streams are jointly independent Poisson processes whose past is independent of the present state. Finite rational receipts, source ownership, and the Route-A rejection are separated from the analytic proof.
author:
- 'Route-A source-local certificate HCS-C351'
date: 3 September 2026
title: |
  Product Form, Time Reversal, and External Departure Flows\
  in an Open Jackson Network
```

## Markdown 正文

trailerid \[\<C3512026090300000000000000000000\>\<C3512026090300000000000000000000\>\]

# Convention and theorem

Let $V=\{1,\ldots,d\}$. Independent external Poisson streams have rates $\alpha_i>0$, and node $i$ has one exponential server of rate $\mu_i>0$. After service at $i$, a customer is routed to $j$ with probability $p_{ij}$, or exits with $$p_{i0}=1-\sum_jp_{ij}\ge0.$$ Assume the substochastic routing matrix $P=(p_{ij})$ satisfies $\operatorname{spr}(P)<1$. Self-routing is allowed, but it is a phantom service mark for the queue-length vector $X\in\mathbb Z_+^d$. The visible transitions are $$\label{eq:generator}
\begin{aligned}
x&\longrightarrow x+e_i &&\text{at rate }\alpha_i,\\
x&\longrightarrow x-e_i &&\text{at rate }\mu_ip_{i0}\mathbf 1_{\{x_i>0\}},\\
x&\longrightarrow x-e_i+e_j &&\text{at rate }
 \mu_ip_{ij}\mathbf 1_{\{x_i>0\}},\quad i\ne j .
\end{aligned}$$ Vectors are rows. Thus $$\label{eq:traffic}
 \lambda=\alpha+\lambda P=\alpha(I-P)^{-1},\qquad
 \rho_i=\lambda_i/\mu_i .$$

[\[thm:main\]]{#thm:main label="thm:main"} The chain is nonexplosive and irreducible. It is positive recurrent if and only if $\rho_i<1$ for every $i$. In that case its unique invariant law is $$\label{eq:product}
 \pi(x)=\prod_{i=1}^d(1-\rho_i)\rho_i^{x_i}.$$ \>0 Its stationary reversal is a Jackson network, in the natural extension allowing zero exogenous rates, with service rates $\mu_i$, traffic vector $\lambda$, and $$\label{eq:reverse}
 \widehat\alpha_i=\lambda_ip_{i0},\qquad
 \widehat p_{ji}=\frac{\lambda_ip_{ij}}{\lambda_j},\qquad
 \widehat p_{i0}=\frac{\alpha_i}{\lambda_i}.$$ \>1 In a two-sided stationary realization, the external departure point processes $D_i$ are jointly independent Poisson processes of rates $\lambda_ip_{i0}$. For every $t$, the vector $(D_i\cap(-\infty,t])_i$ is independent of $X(t)$. This does not assert joint independence of all internal routed arc flows. If some $\lambda_i\ge\mu_i$, the chain is not positive recurrent.

The inverse in [\[eq:traffic\]](#eq:traffic){reference-type="eqref" reference="eq:traffic"} is $\sum_{m\ge0}P^m$, so $\lambda$ exists uniquely and $\lambda_i\ge\alpha_i>0$. The total visible jump rate is bounded by $\sum_i(\alpha_i+\mu_i)$. Also $\operatorname{spr}(P)<1$ makes the routing chain eventually exit from every node. A prescribed finite sequence of services, with no intervening arrivals, reaches zero with positive probability; positive external rates then reach any state. This proves nonexplosion and irreducibility.

# Global balance and the product law

Assume $\rho_i<1$, let $E(x)=\{i:x_i>0\}$, and put $w(x)=\prod_i\rho_i^{x_i}$. The visible rate out of $x$ is $$\label{eq:outgoing}
 q_{\rm out}(x)=\sum_i\alpha_i+
 \sum_{j\in E(x)}\mu_j(1-p_{jj}).$$ After division by $w(x)$, incoming external departures from $x+e_i$ contribute $$\label{eq:outsideflow}
 \sum_i\rho_i\mu_ip_{i0}
 =\sum_i\lambda_ip_{i0}=\sum_i\alpha_i,$$ where the last equality follows by summing [\[eq:traffic\]](#eq:traffic){reference-type="eqref" reference="eq:traffic"}. For an occupied destination $j$, its incoming external arrival and all routed arrivals from $i\ne j$ contribute $$\label{eq:occupied}
 \frac{\alpha_j}{\rho_j}
 +\frac1{\rho_j}\sum_{i\ne j}\lambda_ip_{ij}
 =\frac{\lambda_j(1-p_{jj})}{\rho_j}
 =\mu_j(1-p_{jj}).$$ Equations [\[eq:outsideflow\]](#eq:outsideflow){reference-type="eqref" reference="eq:outsideflow"}--[\[eq:occupied\]](#eq:occupied){reference-type="eqref" reference="eq:occupied"} reproduce [\[eq:outgoing\]](#eq:outgoing){reference-type="eqref" reference="eq:outgoing"}, hence $wQ=0$ at every state. Normalizing each geometric factor proves [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}; irreducibility gives uniqueness and positive recurrence.

This is the *round zero product form closure*: the continuum theorem is proved by global balance, not by truncating the state space.

\>0

# The reversed network

For a stationary forward jump $x\to y$, $\widehat q(y,x)=\pi(x)q(x,y)/\pi(y)$. The three visible pairs give $$\label{eq:jumpreverse}
\begin{array}{rcl}
x\to x+e_i&:&\widehat q(x+e_i,x)=\alpha_i/\rho_i
 =\mu_i\widehat p_{i0},\\
x\to x-e_i&:&\widehat q(x-e_i,x)=\rho_i\mu_ip_{i0}
 =\widehat\alpha_i,\\
x\to x-e_i+e_j&:&\widehat q(x-e_i+e_j,x)
 =\mu_ip_{ij}\rho_i/\rho_j=\mu_j\widehat p_{ji}.
\end{array}$$ Thus the index order in [\[eq:reverse\]](#eq:reverse){reference-type="eqref" reference="eq:reverse"} is forced: forward $i\to j$ becomes reverse $j\to i$. For reverse source $j$, $$\widehat p_{j0}+\sum_i\widehat p_{ji}
 =\frac{\alpha_j+\sum_i\lambda_ip_{ij}}{\lambda_j}=1.$$ The reversed traffic check is equally explicit: $$\widehat\alpha_i+\sum_j\lambda_j\widehat p_{ji}
 =\lambda_ip_{i0}+\lambda_i\sum_jp_{ij}=\lambda_i .$$ Since $\widehat p_{j0}=\alpha_j/\lambda_j>0$, the reversed routing matrix has every row sum below one. The forward model retains $\alpha_i>0$, whereas formula [\[eq:reverse\]](#eq:reverse){reference-type="eqref" reference="eq:reverse"} may have $\widehat\alpha_i=0$ when $p_{i0}=0$; the natural zero-input extension is the convention used for the reversed network, and openness and the traffic equations remain valid.

This is the *round one reversal closure*.

\>1

# Necessity and the external Burke law

Suppose an invariant probability $\nu$ exists. An irreducible conservative countable-state continuous-time Markov chain with an invariant probability is positive recurrent, that probability is unique, and it gives every state positive mass. This standard lemma applies because the chain is irreducible and its rates are bounded. Set $\beta_i=\mu_i\nu\{x_i>0\}$. Apply stationarity to the bounded coordinate truncation $f_M(x)=\min\{x_i,M\}$. Its generator is uniformly bounded by the total event rate; pointwise, $Qf_M$ converges to the ordinary coordinate drift. Dominated convergence yields $$0=\alpha_i+\sum_j\beta_jp_{ji}-\beta_i.$$ Hence $\beta=\alpha+\beta P$, so uniqueness in [\[eq:traffic\]](#eq:traffic){reference-type="eqref" reference="eq:traffic"} gives $\beta=\lambda$. Thus $\lambda_i\le\mu_i$. Equality would imply $\nu\{x_i>0\}=1$, contradicting the lemma's positive mass at the zero state. All inequalities are strict, proving necessity, including the critical face.

Construct the reversed stationary network in the natural extension allowing zero exogenous rates, using independent external Poisson streams of rates $\widehat\alpha_i=\lambda_ip_{i0}$. Equation [\[eq:jumpreverse\]](#eq:jumpreverse){reference-type="eqref" reference="eq:jumpreverse"} identifies its visible marked-jump law with the time reversal of the forward visible marked-jump law. Phantom self-routing completions are state-preserving marks; they can be restored with the same conditional rates and do not enter the external-departure assertion. A forward external departure at $s\le t$ becomes a reversed external arrival at $-s\ge-t$. Future increments of all reversed exogenous streams after $-t$ are jointly independent of the state at $-t$. Reversing time proves both the joint Poisson law and the independence of the forward past-departure history from $X(t)$. Internal routed completions are outside this statement.

# Boundaries, receipts, and Route A

For one node with $p_{11}=0$, the theorem is the $M/M/1$ product law and Burke theorem. Feedback gives $\lambda=\alpha/(1-p_{11})$. When $P=0$, the queues are independent; nilpotent $P$ includes tandems. A node may have $p_{i0}=0$: the spectral-radius assumption still gives a finite positive route to an exit, while that node's external departure process is the zero-rate Poisson process. Critical and overloaded systems fail positive recurrence by the drift argument, not merely by a formal normalizer.

The exact evidence contains 12 rational networks, 1,020 global-balance states, 12 reverse parameter systems, 84 visible reverse-jump identities, and 6 boundary rows. Producer and checker use Gauss--Jordan and Cramer's rule, respectively. These finite receipts test conventions only; they do not prove the infinite-state or point-process theorem.

The closest workspace owner C285 is closed and fixed-population; C233 is infinite-server; C342 is a reinforced walk in a Dirichlet environment. No collision owns the present open single-server departure-history theorem. The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),$$ overall $\mathrm{ROUTE\_A\_REJECTED}$, and Route B is false. There is no prime carrier, deterministic primitive-orbit product, target Euler factor, root number, automorphy, target functional equation or divisor, target-zero match, or Hilbert--Pólya operator.

This is the *round two necessity and external flow closure*.

# Source boundary {#source-boundary .unnumbered}

This is a source-local reconstruction, not a priority claim. Jackson owns the open-network product-form lineage; Burke owns the classical output theorem; Kelly supplies the time-reversal and quasi-reversibility lineage. The exact software receipts are local implementation checks, not attributions to those sources.

9 J. R. Jackson, "Networks of Waiting Lines," *Operations Research* 5(4) (1957), 518--521, DOI [10.1287/opre.5.4.518](https://doi.org/10.1287/opre.5.4.518). P. J. Burke, "The Output of a Queuing System," *Operations Research* 4(6) (1956), 699--704, DOI [10.1287/opre.4.6.699](https://doi.org/10.1287/opre.4.6.699). F. P. Kelly, "Networks of Queues with Customers of Different Types," *Journal of Applied Probability* 12(3) (1975), 542--554, DOI [10.2307/3212869](https://doi.org/10.2307/3212869). F. P. Kelly, *Reversibility and Stochastic Networks*, Wiley, 1979; author-hosted edition at <https://www.statslab.cam.ac.uk/~fpk1/BOOKS/kelly_book.html>.

\>1

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

All finite receipts and release checks are contained in the accompanying package. No human or animal subjects, private data, or external datasets are used. The source-local certificate author performed conceptualization, formal analysis, software, validation, and writing with AI assistance. There is no external funding and no declared conflict of interest.
