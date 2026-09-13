---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dimer-rsa-path-cycle-route-a"
canonical_tex: "henon_dynamics/henon_dimer_rsa_path_cycle_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dimer_rsa_path_cycle_route_a/paper/main.pdf"
source_sha256: "57f08794199cbe28a29ba37e96a8d57735518062ecfa33200e1901655ba5e126"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Finite Dimer Random Sequential Adsorption on Paths and Cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dimer_rsa_path_cycle_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dimer_rsa_path_cycle_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dimer_rsa_path_cycle_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dimer_rsa_path_cycle_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a finite-size solution of dimer random sequential adsorption on a path and a simple cycle, viewed as a uniformly random greedy edge order. =0 Conditioning on the first edge closes a convolution for the probability generating polynomials and a Riccati ordinary generating function. It gives an exact mean and the cycle identity $G_n(z)=zF_{n-2}(z)$. \>0 Arbitrary differentiation produces a triangular system for all factorial moments. Explicit first and second solutions give $\operatorname{Var}(M_n)=\mathrm e^{-4}n+2\mathrm e^{-4}+o(1)$. Binary gap words give the exact path and cycle supports, with every allowed cardinality attained. \>1 A producer-independent bitmask/order oracle, symbolic reconstruction, fresh-path replay, and repaired-hash mutation suite audit the theorem without replacing its all-size proof. The classical stochastic model has no arithmetic prime clock, target bridge, or source-native quantization, so all five Route-A gates fail.
author:
- 'Route-A source-local certificate HCS-C291'
date: 2 September 2026
title: |
  Exact Finite Dimer Random Sequential Adsorption\
  on Paths and Cycles
```

## Markdown 正文

trailerid \[\<C2912026090200000000000000000000\>\<C2912026090200000000000000000000\>\]

# Model, ownership, and claim boundary

Let $P_n$ have vertices $1,\ldots,n$ and edges $e_i=\{i,i+1\}$, with $P_0$ empty. Assign iid continuous priorities to the edges and inspect them in increasing order. An edge is accepted exactly when both endpoints are currently unmatched. Equivalently, scan a uniformly random permutation of the labeled edges. Let $M_n$ be the number accepted and write $$F_n(z)=\mathbb Ez^{M_n}.$$ For the simple labeled cycle $C_n$, $n\ge3$, write the corresponding count and PGF as $K_n$ and $G_n(z)$.

The terminal edge set is a jammed *maximal* matching: no further edge can be added. It need not be a *maximum* matching. This distinction is part of every statement below. Continuous priorities merely generate a uniform order; a discrete-priority model needs a separate tie-breaking convention.

One-dimensional blocking goes back at least to Flory's polymer calculation [@Flory1939]; Evans reviews random and cooperative sequential adsorption [@Evans1993]. Penrose gives rigorous general jamming-limit context [@Penrose2001], while Dyer and Frieze place randomized greedy matching in its algorithmic lineage [@DyerFrieze1991]. We reconstruct an exact finite theorem and integrity chain. We do not claim invention or literature priority for the model, the limiting density, or random greedy matching.

# The finite theorem

[\[thm:main\]]{#thm:main label="thm:main"} Set $F_0=F_1=1$. For every $n\ge2$, $$\label{eq:convolution}
 (n-1)F_n(z)=z\sum_{a+b=n-2}F_a(z)F_b(z).$$ Thus the formal OGF $F(x,z)=\sum_{n\ge0}F_n(z)x^n$ is the unique formal solution with $[x^0]F=[x^1]F=1$ of $$\label{eq:riccati}
 F_x=\frac{F-1}{x}+zxF^2,
 \qquad xF_x-F+1=zx^2F^2.$$

Put $H_r(x)=\left.\partial_z^rF(x,z)\right|_{z=1}$. Then $H_0=(1-x)^{-1}$, and for every $r\ge1$, $H_r(0)=0$ and $$\begin{aligned}
 H_r'-\left(\frac1x+\frac{2x}{1-x}\right)H_r
  ={}&x\sum_{j=1}^{r-1}\binom{r}{j}H_jH_{r-j} \notag\\
   &+rx\sum_{j=0}^{r-1}\binom{r-1}{j}H_jH_{r-1-j}.
\label{eq:triangle}\end{aligned}$$ This triangular system determines every factorial moment. In particular, for $n\ge2$, $$\label{eq:meanexact}
 \mathbb EM_n=\sum_{j=1}^{n-1}
 (n-j)\frac{(-1)^{j+1}2^{j-1}}{j!}.$$ If $a=\mathrm e^{-2}$ and $\alpha=(1-a)/2$, then $$\label{eq:pathasym}
 \mathbb EM_n=\alpha n-a+o(1),\qquad
 \operatorname{Var}(M_n)=a^2n+2a^2+o(1).$$

The support is $\{0\}$ for $n=0,1$. For $n\ge2$, $$\label{eq:pathsupport}
 \operatorname{supp}(M_n)=
 \left\{\left\lceil\frac{n-1}{3}\right\rceil,
 \ldots,\left\lfloor\frac n2\right\rfloor\right\}.$$ For every simple cycle $n\ge3$, $$\label{eq:cycleidentity}
 G_n(z)=zF_{n-2}(z),
 \qquad
 \operatorname{supp}(K_n)=
 \left\{\left\lceil\frac n3\right\rceil,
 \ldots,\left\lfloor\frac n2\right\rfloor\right\}.$$ Consequently $$\begin{aligned}
 \mathbb EK_n&=1+\mathbb EM_{n-2}=\alpha n+o(1),\label{eq:cyclemean}\\
 \mathbb EK_n-\mathbb EM_n&=\mathrm e^{-2}+o(1),\label{eq:boundarymean}\\
 \operatorname{Var}(K_n)&=\operatorname{Var}(M_{n-2})=\mathrm e^{-4}n+o(1).
 \label{eq:cyclevariance}\end{aligned}$$ Both expected occupied-vertex fractions tend to $1-\mathrm e^{-2}$.

# First-edge decomposition and the Riccati OGF

The first edge in any order is accepted. Conditional on $e_i$ being first, its endpoints $i,i+1$ are blocked and the eligible residual vertices split into $P_{i-1}$ and $P_{n-i-1}$. Given this event, the relative orders induced on those two disjoint edge sets are independent and uniform. Their interleaving has no effect because the vertex sets are disjoint. Therefore $$M_n\ \stackrel{d}{=}\ 1+M_{i-1}^{(L)}+M_{n-i-1}^{(R)}
 \quad\hbox{given }e_i\hbox{ first},$$ where the two variables on the right are independent. Averaging over the $n-1$ equally likely choices proves [\[eq:convolution\]](#eq:convolution){reference-type="eqref" reference="eq:convolution"}. Multiplication by $x^{n-1}$ and summation over $n\ge2$ gives $$F_x-\frac{F-1}{x}=zxF^2,$$ which is [\[eq:riccati\]](#eq:riccati){reference-type="eqref" reference="eq:riccati"}. This is a formal-power-series derivation, so it does not presume analytic convergence in two variables.

At $z=1$, normalization gives $F_n(1)=1$, hence $F(x,1)=(1-x)^{-1}$. Differentiate $zF^2$ exactly $r$ times: $$\begin{aligned}
 \left.\partial_z^r(zF^2)\right|_{z=1}
 ={}&\sum_{j=0}^r\binom{r}{j}H_jH_{r-j}
 +r\sum_{j=0}^{r-1}\binom{r-1}{j}H_jH_{r-1-j}.\end{aligned}$$ The $j=0,r$ terms in the first sum are $2H_0H_r$. Moving them to the left proves the all-$r$ equation [\[eq:triangle\]](#eq:triangle){reference-type="eqref" reference="eq:triangle"}; all other indices are strictly below $r$.

For $r=1$, the equation is $$H_1'-\left(\frac1x+\frac{2x}{1-x}\right)H_1
 =\frac{x}{(1-x)^2},$$ and its formal solution regular at zero is $$\label{eq:H1}
 H_1(x)=\frac{x(1-\mathrm e^{-2x})}{2(1-x)^2}.$$ Expanding the exponential and extracting $[x^n]$ proves [\[eq:meanexact\]](#eq:meanexact){reference-type="eqref" reference="eq:meanexact"}.

\>0

# Second factorial moment and variance

For $r=2$, the triangular equation becomes $$\label{eq:H2ode}
 H_2'-\left(\frac1x+\frac{2x}{1-x}\right)H_2
 =4xH_0H_1+2xH_1^2.$$ The unique formal solution regular at zero is $$\label{eq:H2}
 H_2(x)=
 \frac{x\mathrm e^{-4x}
 (4x^2\mathrm e^{2x}-3x\mathrm e^{4x}-x+\mathrm e^{4x}-1)}{4(x-1)^3}.$$ Direct differentiation verifies [\[eq:H2ode\]](#eq:H2ode){reference-type="eqref" reference="eq:H2ode"}. The formula also follows by multiplying by the integrating factor $\mathrm e^{2x}(1-x)^2/x$ and integrating from zero.

To extract the variance without fitting finite data, set $s=1-x$, $a=\mathrm e^{-2}$, and $\alpha=(1-a)/2$. Equations [\[eq:H1\]](#eq:H1){reference-type="eqref" reference="eq:H1"} and [\[eq:H2\]](#eq:H2){reference-type="eqref" reference="eq:H2"} have pole parts $$\begin{aligned}
 H_1&=\frac{\alpha}{s^2}-\frac{1+a}{2s}+R_1(x),\label{eq:H1pole}\\
 H_2&=\frac{c_3}{s^3}+\frac{c_2}{s^2}+\frac{c_1}{s}+R_2(x),\label{eq:H2pole}\end{aligned}$$ where $$\label{eq:cs}
 c_3=\frac{(1-a)^2}{2},\quad
 c_2=-\frac54+a+\frac54a^2,\quad
 c_1=\frac34+a+\frac54a^2.$$ After these pole parts are removed, $R_1,R_2$ are entire combinations of exponentials and polynomials divided by removable powers of $1-x$. Their Taylor coefficients are therefore $o(1)$ (indeed factorially small up to a polynomial factor). It follows that $$\begin{aligned}
 \mathbb EM_n&=\alpha(n+1)-\frac{1+a}{2}+o(1)
       =\alpha n-a+o(1),\\
 \mathbb E(M_n)_2&=c_3\binom{n+2}{2}+c_2(n+1)+c_1+o(1).\end{aligned}$$ Since $c_3/2=\alpha^2$, substituting these expressions into $\operatorname{Var}(M_n)=\mathbb E(M_n)_2+\mathbb EM_n-(\mathbb EM_n)^2$ cancels the quadratic term. The linear coefficient simplifies to $a^2$ and the constant to $2a^2$, proving [\[eq:pathasym\]](#eq:pathasym){reference-type="eqref" reference="eq:pathasym"}. Thus the requested leading law is $\operatorname{Var}(M_n)=\mathrm e^{-4}n+O(1)$, with its boundary constant also identified.

# Exact support: binary gap words

[\[lem:pathsupport\]]{#lem:pathsupport label="lem:pathsupport"} A cardinality $k$ occurs as a maximal matching of $P_n$ exactly when $2k\le n\le3k+1$, with the separate empty cases $n=0,1$.

List the $k$ selected dimers from left to right. There are $k+1$ gaps of unmatched vertices: two end gaps and $k-1$ internal gaps. Maximality is equivalent to every gap having size at most one, since two adjacent unmatched vertices would support another edge. Hence $$n=2k+g_0+\cdots+g_k,\qquad g_j\in\{0,1\},$$ which is possible exactly for $0\le n-2k\le k+1$. Conversely, choosing any $n-2k$ of these gaps to have size one explicitly constructs a maximal matching. This proves the equivalence.

Every such maximal matching occurs with positive probability under RSA: place all of its mutually disjoint edges first in the scan. They are accepted, and every remaining edge meets one of them by maximality, so it is rejected. Lemma [\[lem:pathsupport\]](#lem:pathsupport){reference-type="ref" reference="lem:pathsupport"} therefore proves [\[eq:pathsupport\]](#eq:pathsupport){reference-type="eqref" reference="eq:pathsupport"}, not merely a bound on possible sizes.

For a cycle with $k$ selected dimers there are $k$ cyclic gaps, each again zero or one. Thus $n=2k+g_1+\cdots+g_k$, so $2k\le n\le3k$, and the same ordering argument realizes every constructed matching. This proves the support in [\[eq:cycleidentity\]](#eq:cycleidentity){reference-type="eqref" reference="eq:cycleidentity"}. Notice that smaller support values are maximal but not maximum; for example, the middle edge alone is a maximal matching of $P_4$, while a maximum matching has size two.

# Cycle identity and the boundary correction

The first edge of $C_n$ is accepted. Removing its two endpoints from further competition leaves exactly a path on $n-2$ vertices; conditional on the first edge, the residual relative order is uniform. The identity $K_n\stackrel d=1+M_{n-2}$ follows for every $n\ge3$, including $C_3$ and $C_4$, and proves [\[eq:cycleidentity\]](#eq:cycleidentity){reference-type="eqref" reference="eq:cycleidentity"}. Taking moments gives [\[eq:cyclemean\]](#eq:cyclemean){reference-type="eqref" reference="eq:cyclemean"} and $\operatorname{Var}(K_n)=\operatorname{Var}(M_{n-2})$. Finally, $$1+\alpha(n-2)-a=\alpha n,
 \qquad 1-2\alpha-a=0,$$ which explains the exact cancellation of the path mean's constant boundary term. Comparison with the same-size path leaves the positive correction $a=\mathrm e^{-2}$ in [\[eq:boundarymean\]](#eq:boundarymean){reference-type="eqref" reference="eq:boundarymean"}. The cycle variance has no constant term at this precision because $a^2(n-2)+2a^2=a^2n$.

# Boundary atlas and theorem limits

  Face             Exact treatment         Not silently identified with
  ---------------- ----------------------- --------------------------------
  $P_0,P_1$        $M_n=0$, $F_n=1$        the $n\ge2$ recurrence
  $P_2$            $M_2=1$, $F_2=z$        a limiting-density statement
  $C_n$            simple cycle, $n\ge3$   loops or parallel-edge cycles
  priority ties    null under continuity   unspecified discrete tie rules
  terminal state   maximal matching        guaranteed maximum matching
  finite tables    regression evidence     proof for arbitrary $n$

The theorem concerns the final count. It does not classify adsorption times under an additional physical-time embedding, general graphs, weighted edge orders, correlated priorities, or discrete ties. Such changes destroy at least one symmetry used in the first-edge convolution.

\>1

# Executable reconstruction and adversarial controls

The evidence producer implements [\[eq:convolution\]](#eq:convolution){reference-type="eqref" reference="eq:convolution"} in exact rational arithmetic through $P_{20}$, stores orders zero through five of the factorial triangle, and independently propagates the first two moments through $n=200$. It records full path distributions through $P_{10}$, cycle distributions through $C_9$, and asymptotic cells at $n=20,50,100,200$.

The checker imports no producer module and never trusts a floating Monte Carlo sample. Its state is a pair of bitmasks: the set of processed labeled edges and the set of matched vertices. Extending every state by every unprocessed edge aggregates all $818{,}225$ labeled orders in the declared window and recovers their exact integer multiplicities. A separate implementation of the falling-factorial conditional identity reconstructs every stored high-order moment. In the frozen release it executes $19{,}371$ assertions.

A SymPy lane checks the Riccati specialization, the $H_1,H_2$ differential equations, pole algebra, finite coefficient controls, and path-to-cycle support shift in 132 symbolic checks. Two unrelated temporary paths reproduce the evidence byte for byte. Strict JSON and recursive safe-YAML loaders reject duplicate keys, nonstandard constants, unknown or missing keys, bool-as-integer confusion, row-order or uniqueness loss, and any semantic drift; exact top/nested YAML schemas, types, values, and a semantic hash are release-blocking. All 105/105 repaired-hash, drop-replace, stale-hash, raw-duplicate, nonstandard-constant, and YAML attacks are rejected.

These finite calculations are falsification tools. The all-$n$ claims rest on the first-edge decomposition, formal differentiation, pole extraction, and binary-gap proof above. No finite cutoff is promoted to an induction proof.

# Route-A assessment and nonclaims

   Gate  Verdict   Strongest obstruction
  ------ --------- -------------------------------------------------------------
    A0   FAIL      no rational-prime carrier or arithmetic weight
    A1   FAIL      terminating random scans are not primitive periodic orbits
    A2   FAIL      a PGF is source probability data, not a target determinant
    A3   FAIL      no divisor, functional equation, or explicit-formula bridge
    A4   FAIL      no source-native same-clock self-adjoint quantization

The tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$, so the overall verdict is `ROUTE_A_REJECTED`. Route B is not authorized. In particular, we do not reinterpret random histories as an unweighted orbit product, attach prime labels to graph edges, call a PGF an Euler factor, or introduce a formal quantum operator. The governing obstruction is HEN-O275, within the literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Data, code, and research declarations

#### Data and code availability.

All data are generated deterministically in the package. The canonical evidence JSON, producer, independent checker, SymPy reconstruction, fresh-path replay, hostile mutation suite, manuscript source, three revision PDFs, and self-excluded release ledger are included. No external dataset or training data are used.

#### Ethics.

This is a theoretical and computational study of a finite stochastic model. It uses no human participants, animals, personal data, or clinical decisions; institutional ethics approval is not applicable.

#### Conflicts of interest.

No conflicts of interest are declared.

#### Funding.

No external funding is declared for this reconstruction.

#### CRediT authorship.

The package records one accountable computational authorship role covering conceptualization, formal analysis, software, validation, visualization audit, and writing. Classical ownership is assigned through the cited literature.

#### AI-use disclosure.

AI assistance was used to organize exposition and executable checks. Every mathematical claim is supported by the displayed derivation and deterministic reconstruction; responsibility for verification remains with the package author. AI assistance is not listed as an author and no claim of autonomous literature originality is made.

9 P. J. Flory, Intramolecular reaction between neighboring substituents of vinyl polymers, *J. Amer. Chem. Soc.* **61**(6), 1518--1521 (1939), [doi:10.1021/ja01875a053](https://doi.org/10.1021/ja01875a053).

J. W. Evans, Random and cooperative sequential adsorption, *Rev. Mod. Phys.* **65**(4), 1281--1329 (1993), [doi:10.1103/RevModPhys.65.1281](https://doi.org/10.1103/RevModPhys.65.1281).

M. D. Penrose, Random parking, sequential adsorption, and the jamming limit, *Commun. Math. Phys.* **218**(1), 153--176 (2001), [doi:10.1007/s002200100387](https://doi.org/10.1007/s002200100387).

M. Dyer and A. Frieze, Randomized greedy matching, *Random Structures Algorithms* **2**(1), 29--45 (1991), [doi:10.1002/rsa.3240020104](https://doi.org/10.1002/rsa.3240020104).
