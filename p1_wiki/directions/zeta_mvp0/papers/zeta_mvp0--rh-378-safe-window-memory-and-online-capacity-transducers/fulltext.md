---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-378-safe-window-memory-and-online-capacity-transducers"
canonical_tex: "zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/main.pdf"
source_sha256: "ebc5cb3eaf33ad2ecf1d65c3ab202a4ea6d23bbbbeeecc685ac65cbf1ea10ff0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Safe Window Memory and Online Capacity Transducers: Lag-Two Classification, Exact Greedy Machines, and a Chowla Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-378-safe-window-memory-and-online-capacity-transducers/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify two finite-memory layers of the distance-two Möbius capacity problem. A fixed periodic causal window table is universally safe exactly when a finite de Bruijn block test passes, and its current-zero score has a canonical ternary monomial expansion with unique coefficients. Among all $512$ lag-two tables, exactly $13$ are universally safe. Their six-term arithmetic ledger has rank five; seven tables have unconditional limiting correlations, whereas each of the other six has a limit exactly when the ordinary shift-two Chowla sum is $o(N)$. Separately, two fixed four-state causal machines produce the two endpoint extrema for every finite ternary word. Four states are necessary for either exact output stream, but no single deterministic universally safe causal policy can attain the absolute capacity at every prefix. A length-$15$ stateless table realizes each orientation on the run-at-most-eight class containing the Möbius word; that window length is minimal only in this narrow stateless model. Exact finite certificates accompany every enumeration. We prove neither shift-two Chowla cancellation nor convergence of the adaptive capacity. No operator, trace formula, zeta-zero identification, or implication for the Riemann hypothesis is claimed.
author:
- RH research program
bibliography:
- references.bib
date: 'August 7, 2026'
title: |
  Safe Window Memory and Online Capacity Transducers:\
  Lag-Two Classification, Exact Greedy Machines, and a Chowla Boundary
```

## Markdown 正文

# Problem and claim boundary

Let $a=(a_n)_{n\ge1}$ be a word in $\{-1,0,1\}$. A sign word $\epsilon=(\epsilon_n)_{n\ge1}\in\{-1,+1\}^{\mathbb N}$ is *distance-two safe* when $$\epsilon_n=\epsilon_{n+2}=+1\quad\text{never occurs}.
       \label{eq:safety}$$ For a finite prefix put $$S_N(a,\epsilon)=\sum_{n\le N}a_n\epsilon_n,
 \quad S_N^{\max}(a)=\max_{\epsilon\ \mathrm{safe}}S_N(a,\epsilon),
 \quad S_N^{\min}(a)=\min_{\epsilon\ \mathrm{safe}}S_N(a,\epsilon),$$ and $$K_N(a)=\max\{|S_N^{\max}(a)|,|S_N^{\min}(a)|\}.
                 \label{eq:capacity}$$ For $a_n=\mu(n)$ these are the frozen RH-366/RH-371 objects [@RH366; @RH371]. The optimization is adaptive in the finite input word; it is not an intrinsic dynamical trace.

This paper has two logically separate outputs. First, it gives exact finite classifications of fixed-memory safe factors. Second, it gives exact online realizations of the two extrema. Arithmetic limits enter only in the lag-two classification. The unproved object is $$D_2(N)=\sum_{m\le N-2}\mu(m)\mu(m+2)=o(N).
                   \label{eq:chowla}$$ We never infer [\[eq:chowla\]](#eq:chowla){reference-type="eqref" reference="eq:chowla"} from finite data.

# Periodic causal windows

Fix integers $q,\ell\ge1$. A $q$-periodic causal $\ell$-window table is a family $$F_r:\{-1,0,1\}^\ell\longrightarrow\{-1,+1\},\qquad r\in\mathbb Z/q\mathbb Z,$$ with output $$\epsilon_n=F_{n\bmod q}(a_{n-\ell+1},\ldots,a_n).$$ At the beginning of a finite word we pad by zeros. Universal safety means that [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"} holds for every ternary input, not merely for the Möbius word.

[\[thm:block-test\]]{#thm:block-test label="thm:block-test"} A fixed $q$-periodic $\ell$-window table is universally safe if and only if, for every phase $r$ and every block $(x_0,\ldots,x_{\ell+1})\in\{-1,0,1\}^{\ell+2}$, $$F_r(x_0,\ldots,x_{\ell-1})\quad\text{and}\quad
 F_{r+2}(x_2,\ldots,x_{\ell+1})
 \label{eq:block-check}$$ are not both $+1$. Thus the exact test has $q3^{\ell+2}$ compatible-block checks.

The two displayed windows are precisely the overlapping windows at times $n$ and $n+2$. Universal safety therefore implies every check. Conversely, every possible distance-two output pair occurs inside such a compatible block, so the checks imply safety. This argument also covers $\ell=1$ and $\ell=2$: overlap is then empty or confined to the appropriate symbols, but the same length-$\ell+2$ block still records both windows. Any phase can be realized by placing the block sufficiently far into a finite input.

The score function of one phase is $$h_r(x_1,\ldots,x_\ell)=x_\ell F_r(x_1,\ldots,x_\ell).$$ It vanishes when the current symbol $x_\ell$ is zero.

[\[prop:basis\]]{#prop:basis label="prop:basis"} The displayed monomials $$\prod_{j<\ell}x_j^{\alpha_j}x_\ell^e,\qquad
 \alpha_j\in\{0,1,2\},\quad e\in\{1,2\}.
 \label{eq:basis}$$ form a basis for current-zero functions, and every $h_r$ has a unique expansion in this basis. Across $q$ phases the formal dimension is $2q3^{\ell-1}$.

On $\{-1,0,1\}$, the three functions $1,x,x^2$ are linearly independent and hence form an interpolation basis for all scalar functions. Tensoring gives the $3^\ell$ monomials with exponents in $\{0,1,2\}$. Setting $x_\ell=0$ kills exactly the monomials with current exponent one or two; the vanishing condition forces all coefficients with current exponent zero to vanish. This leaves $2\cdot3^{\ell-1}$ basis functions per phase.

This is a formal function-space dimension. It is not a minimal number of Möbius correlations and does not use any arithmetic identities among their averages.

# Complete lag-two classification

Consider a stateless lag-two rule $$\epsilon_n=f(a_{n-2},a_n),\qquad f:\{-1,0,1\}^2\to\{-1,+1\},
       \label{eq:lag-rule}$$ with $a_j=0$ for $j\le0$. Write $P=\{(x,z):f(x,z)=+1\}$ for its plus-edge relation. This is an $\ell=3$ table that ignores the middle coordinate.

[\[thm:thirteen\]]{#thm:thirteen label="thm:thirteen"} The rule [\[eq:lag-rule\]](#eq:lag-rule){reference-type="eqref" reference="eq:lag-rule"} is universally safe if and only if $P$ contains no composable pair: $$(x,z),(z,w)\in P\quad\text{for no }x,z,w\in\{-1,0,1\}.
       \label{eq:no-compose}$$ Among all $2^9=512$ tables, exactly $13$ are safe: the empty relation, the six single off-diagonal edges, and six two-edge relations, consisting of three in-stars and three out-stars.

Outputs two sites apart are $f(x,z)$ and $f(z,w)$, proving the equivalence. Condition [\[eq:no-compose\]](#eq:no-compose){reference-type="eqref" reference="eq:no-compose"} makes every loop illegal. More generally, the source set of $P$ is disjoint from its target set. On three vertices this bounds $|P|$ by two. There are six allowed one-edge relations. A two-edge relation must share its source or share its target, giving three out-stars and three in-stars. These relations all satisfy [\[eq:no-compose\]](#eq:no-compose){reference-type="eqref" reference="eq:no-compose"}.

Every score $h(x,z)=zf(x,z)$ has the exact interpolation $$h(x,z)=c_{01}z+c_{02}z^2+c_{11}xz+c_{12}xz^2
             +c_{21}x^2z+c_{22}x^2z^2.
 \label{eq:six-basis}$$ For $N\ge1$ define, always with the common endpoint $m\le N-2$, $$\begin{aligned}
 M(N)&=\sum_{n\le N}\mu(n),& Q_1(N)&=\sum_{n\le N}\mu(n)^2,\\
 D_2(N)&=\sum_{m\le N-2}\mu(m)\mu(m+2),&
 Q_2(N)&=\sum_{m\le N-2}\mu(m)^2\mu(m+2)^2,\\
 U_2(N)&=\sum_{m\le N-2}\mu(m)\mu(m+2)^2,&
 V_2(N)&=\sum_{m\le N-2}\mu(m)^2\mu(m+2).\end{aligned}$$ Zero padding in [\[eq:lag-rule\]](#eq:lag-rule){reference-type="eqref" reference="eq:lag-rule"} makes the following identity exact, including the first two sites: $$L_f(N):=\sum_{n\le N}\mu(n)f(\mu(n-2),\mu(n))
 =c_{01}M+c_{02}Q_1+c_{11}D_2+c_{12}U_2+c_{21}V_2+c_{22}Q_2.
 \label{eq:ledger}$$

[\[prop:rank-five\]]{#prop:rank-five label="prop:rank-five"} For the thirteen safe tables, the coefficient matrix in the order appearing in [\[eq:six-basis\]](#eq:six-basis){reference-type="eqref" reference="eq:six-basis"} has rank five. Its unique column relation is $$c_{22}=-c_{02}-c_{11}.
                         \label{eq:relation}$$ The multiplicities of $(A,B)=(c_{02},c_{11})$ are

   $A$     $B$    count   $A$     $B$     count
  ------ ------- ------- ------ -------- -------
   $0$     $0$      5     $0$    $-1/2$     2
   $0$    $1/2$     2     $-1$    $0$       1
   $1$     $0$      1     $1$    $-1/2$     1
   $-1$   $1/2$     1

In particular, seven tables have $c_{11}=0$ and six have $c_{11}\ne0$.

Ternary interpolation in [\[eq:six-basis\]](#eq:six-basis){reference-type="eqref" reference="eq:six-basis"}, applied to the thirteen relations in Theorem [\[thm:thirteen\]](#thm:thirteen){reference-type="ref" reference="thm:thirteen"}, gives the displayed multiplicities. Exact rational row reduction gives rank five and [\[eq:relation\]](#eq:relation){reference-type="eqref" reference="eq:relation"}. The accompanying artifact performs both calculations with `fractions.Fraction`; the theorem does not depend on floating-point rank detection.

Put $$\rho=\frac6{\pi^2},\qquad
 \kappa_2=\prod_p\left(1-\frac2{p^2}\right).
 \label{eq:constants}$$ Davenport gives $M=o(N)$ [@Davenport1937]. The squarefree density and two-site squarefree density give $Q_1/N\to\rho$ and $Q_2/N\to\kappa_2$ [@Mirsky1948]. RH-376 proves, with this fixed endpoint, $$U_2=o(N),\qquad V_2=o(N),\qquad
        D_2(N)/N\text{ converges }\Longleftrightarrow D_2(N)=o(N).
        \label{eq:rh376-input}$$ The final equivalence uses the frozen logarithmic Chowla input only to show that any ordinary limit would have to be zero; it does not prove that the ordinary limit exists [@RH376].

[\[thm:lag-limits\]]{#thm:lag-limits label="thm:lag-limits"} For every safe lag-two table, $$\frac{L_f(N)}N
 =c_{02}(\rho-\kappa_2)
  +c_{11}\left(\frac{D_2(N)}N-\kappa_2\right)+o(1).
 \label{eq:limit-formula}$$ Consequently:

1.  all seven tables with $c_{11}=0$ have unconditional limits; the largest absolute limit within this subclass is $\rho-\kappa_2$, attained for example by $P=\{(0,+1)\}$;

2.  each of the six tables with $c_{11}\ne0$ has a limit if and only if $D_2=o(N)$; under that condition the largest absolute limit within this subclass is $\rho-\kappa_2/2$, attained for example by $P=\{(-1,+1),(0,+1)\}$.

Insert the four established asymptotics into [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"}, then use [\[eq:relation\]](#eq:relation){reference-type="eqref" reference="eq:relation"}; this gives [\[eq:limit-formula\]](#eq:limit-formula){reference-type="eqref" reference="eq:limit-formula"}. The thirteen $(c_{02},c_{11})$ pairs in Proposition [\[prop:rank-five\]](#prop:rank-five){reference-type="ref" reference="prop:rank-five"} give both optimizations by exact finite comparison, using $0<\kappa_2<\rho$. When $c_{11}\ne0$, convergence of the left side is equivalent to convergence of $D_2/N$, which is equivalent to [\[eq:chowla\]](#eq:chowla){reference-type="eqref" reference="eq:chowla"} by [\[eq:rh376-input\]](#eq:rh376-input){reference-type="eqref" reference="eq:rh376-input"}.

The two constants are optima only inside the thirteen-table lag-two class. In particular, $\rho-\kappa_2/2$ is conditional, not an unconditional capacity floor.

## Exact comparison with the one-site supremum

The conditional lag-two value is strictly larger than the all-clock one-site supremum $B_\infty$ of RH-374/RH-375 [@RH374; @RH375]. This comparison is analytic rather than a finite decimal observation. Let $$e_m=\prod_{p\ \mathrm{odd}}(1-m/p^2),\qquad e_9=0,$$ and let $C$ be the normalized odd-run density in the frozen square-clock limit, so that $e_1=8/\pi^2$ and $B_\infty=(4+2C)/\pi^2$. Since $\kappa_2=e_2/2$, $$\rho-\frac{\kappa_2}{2}-B_\infty
        =\frac{e_1-e_2-e_1C}{4}.
 \label{eq:strict-comparison}$$ Here $e_1-e_2$ is the positive-run-boundary density on the odd lattice and, by shift invariance, also the positive-run-start density, whereas $e_1C$ is the density of odd-run starts. Their difference is the even-run-start density. Exact length-eight runs alone have density $e_8$: the adjacent sites are forced to be zero modulo $9$. Therefore $$\rho-\frac{\kappa_2}{2}-B_\infty
       \ge \frac{e_8}{4}>0.
       \label{eq:positive-gap}$$ This strict gap becomes available only if [\[eq:chowla\]](#eq:chowla){reference-type="eqref" reference="eq:chowla"} is supplied.

# Two exact online extrema machines

For $\sigma\in\{-1,+1\}$, define a Mealy transducer $T_\sigma$ with state $$s_n=(\epsilon_{n-1},\epsilon_{n-2}),\qquad s_1=(-1,-1),
             \label{eq:state}$$ output and update $$\epsilon_n=+1\Longleftrightarrow
        (a_n=\sigma\ \text{and}\ \epsilon_{n-2}=-1),
 \qquad s_{n+1}=(\epsilon_n,\epsilon_{n-1}).
 \label{eq:greedy}$$

[\[thm:greedy\]]{#thm:greedy label="thm:greedy"} For every finite ternary word, $$S_N(a,T_{+})=S_N^{\max}(a),\qquad
 S_N(a,T_{-})=S_N^{\min}(a).
 \label{eq:two-extrema}$$ Hence $$K_N(a)=\max\{|S_N(a,T_+)|,|S_N(a,T_-)|\}.
 \label{eq:two-machine-K}$$ Each $T_\sigma$ is universally safe.

Split the integer sites into the two parity paths. Relative to the all-minus output, changing a site to plus changes the score by $2a_n$. For the maximum only sites with $a_n=+1$ can help, and one needs a largest independent subset of those marked vertices on each path. Left-greedy selection is maximum cardinality on a path: choosing the first available marked vertex never reduces the attainable number to its right. This is exactly $T_+$. Applying the same argument to minimization selects the $a_n=-1$ vertices and gives $T_-$. Rule [\[eq:greedy\]](#eq:greedy){reference-type="eqref" reference="eq:greedy"} can emit plus only when the output two sites earlier was minus, proving universal safety.

Equation [\[eq:two-machine-K\]](#eq:two-machine-K){reference-type="eqref" reference="eq:two-machine-K"} takes a maximum of two endpoint registers. It must not be described as one transducer directly outputting $K_N$.

[\[prop:four-state\]]{#prop:four-state label="prop:four-state"} For either fixed orientation $\sigma$, all four states in [\[eq:state\]](#eq:state){reference-type="eqref" reference="eq:state"} are reachable, and every exact deterministic Mealy realization of the same input-output map has at least four states.

Starting from $(-1,-1)$, suitable symbols reach $(+1,-1)$, $(+1,+1)$, and $(-1,+1)$, so all states are reachable. Take two states. If their second coordinates differ, the next input $a=\sigma$ immediately distinguishes their outputs. If their second coordinates agree but their first coordinates differ, first feed $a\ne\sigma$, which emits minus in both states, and then feed $\sigma$; the second output distinguishes them. Thus the four residual input-output behaviors are pairwise distinct.

This is a lower bound only for exact realization of the frozen orientation stream. It is not a lower bound for all capacity algorithms, offline encodings, or machines that return only a final scalar.

[\[thm:no-single\]]{#thm:no-single label="thm:no-single"} There is no single deterministic causal universally safe policy which, for every ternary input and at every prefix, satisfies $$|S_N(a,\epsilon)|=K_N(a).
                  \label{eq:online-demand}$$

Begin with $a_1=+1$. If the policy emits $\epsilon_1=+1$, extend by $(a_2,a_3)=(-1,+1)$. Prefix optimality at time two forces $\epsilon_2=-1$ and gives score $2$. Reaching $K_3=3$ would then force $\epsilon_3=+1$, contradicting safety with $\epsilon_1=+1$.

If instead $\epsilon_1=-1$, extend by $(a_2,a_3,a_4)=(-1,-1,-1)$. Prefix optimality successively forces $\epsilon_2=\epsilon_3=+1$ and scores $-2,-3$. Reaching $K_4=4$ would force $\epsilon_4=+1$, contradicting safety with $\epsilon_2=+1$. Thus either first output has a finite adversarial continuation.

The obstruction is to one deterministic policy required to be optimal on every branch and every prefix. It does not exclude a policy designed offline for one known endpoint. The artifact independently counts the admissible deterministic causal policy trees: the counts at horizons $1,2,3,4$ are respectively $8,256,65536,0$.

# A length-fifteen stateless realization

Fix $\sigma\in\{-1,+1\}$. Define the contiguous $15$-window table $$\begin{aligned}
 b_n&=\sum_{k=1}^{8}(-1)^{k+1}
       \prod_{j=0}^{k-1}{\bf1}_{\{a_{n-2j}=\sigma\}},
       \label{eq:b-table}\\
 \widehat\epsilon_n&=2b_n-1,
       \label{eq:window-output}\end{aligned}$$ again padding the past by zeros.

[\[thm:ell15\]]{#thm:ell15 label="thm:ell15"} The table [\[eq:b-table\]](#eq:b-table){reference-type="eqref" reference="eq:b-table"} is universally safe for every ternary input. If every step-two $\sigma$-run has length at most eight, then its entire output stream equals $T_\sigma$. The Möbius input belongs to this class. For an unrestricted ternary input the statement is false: the shortest divergence is a run of nine same-parity $\sigma$ sites, spanning a length-$17$ integer prefix.

Let $r$ be the length of the current same-parity $\sigma$-run, with $r=0$ when $a_n\ne\sigma$. The first $\min(r,8)$ product indicators in [\[eq:b-table\]](#eq:b-table){reference-type="eqref" reference="eq:b-table"} equal one and the rest vanish. Hence $b_n=1$ precisely for $r\in\{1,3,5,7\}$, and $b_n=0$ for $r=0$, for even $r$, and for $r\ge8$. A plus output is therefore followed two sites later by a minus output whether the run continues or breaks. This proves universal safety.

Along a $\sigma$-run, recursion [\[eq:greedy\]](#eq:greedy){reference-type="eqref" reference="eq:greedy"} alternates plus and minus, starting with plus. It agrees with the displayed rule through run length eight. At run length nine the recursion emits plus while [\[eq:b-table\]](#eq:b-table){reference-type="eqref" reference="eq:b-table"} emits minus, giving the claimed $17$-site example.

For odd Möbius sites, any nine consecutive step-two positions contain a multiple of $9$, whose Möbius value is zero. For even sites, two consecutive step-two positions include a multiple of $4$. Thus neither orientation has a step-two run longer than eight.

[\[prop:ell15-minimal\]]{#prop:ell15-minimal label="prop:ell15-minimal"} On the class in Theorem [\[thm:ell15\]](#thm:ell15){reference-type="ref" reference="thm:ell15"}, among $q=1$ causal contiguous stateless windows that reproduce the complete $T_\sigma$ output stream, the minimum window length is exactly $15$.

Theorem [\[thm:ell15\]](#thm:ell15){reference-type="ref" reference="thm:ell15"} supplies the upper bound. At $n=15$, construct two words identical on the last fourteen sites $a_2,\ldots,a_{15}$ and zero on the other parity. Set $a_3,a_5,\ldots,a_{15}=\sigma$. In the first word take $a_1=0$; in the second take $a_1=\sigma$, with a break before the prefix. The current same-parity run lengths are seven and eight, so $T_\sigma$ emits respectively plus and minus. No contiguous window of length at most fourteen can distinguish the two inputs.

The proposition excludes stateful realizations, sparse or noncontiguous access, noncausal models, and algorithms that compute only a score or $K_N$. It is not a global memory lower bound.

# Reproducible finite protocol

The standard-library artifact uses exact integers and `fractions.Fraction`. It performs:

-   the $512$-table census, rational rank, relation, and multiplicities;

-   two independent $243$-block graph-lift safety tests for the witnesses $P=\{(0,+1)\}$ and $P=\{(-1,+1),(0,+1)\}$;

-   all $72=2\cdot4\cdot3^2$ two-step Mealy safety cases and pairwise state distinguishability;

-   both extrema on all $\sum_{n=1}^{10}3^n=88572$ ternary words, checked against an independent four-state dynamic program;

-   the deterministic causal-policy tree counts through horizon four, including direct replay of both adversarial branches in Theorem [\[thm:no-single\]](#thm:no-single){reference-type="ref" reference="thm:no-single"};

-   all $2^9=512$ binary assignments to the union of two adjacent depth-eight same-parity windows, the $17$-site counterexample, and the narrow length-$15$ witness;

-   every Möbius prefix through $2^{20}$: $2097152$ orientation-extremum equalities, $1048576$ six-term ledger identities, and $2097152$ recursive versus stateless-window equalities.

The frozen endpoint rows are:

          $N$     $M$      $Q_1$    $D_2$   $U_2$   $V_2$      $Q_2$      $S_0$      $S_h$   $S^{\max}$   $S^{\min}$        $K$
  ----------- ------- ---------- -------- ------- ------- ---------- ---------- ---------- ------------ ------------ ----------
       $1024$    $-4$      $624$    $-34$   $-18$   $-14$      $330$      $308$      $492$        $530$       $-504$      $530$
      $65536$    $14$    $39844$     $33$   $-51$    $35$    $21155$    $18654$    $29258$      $32320$     $-32222$    $32320$
    $1048576$   $257$   $637461$   $-382$   $130$   $438$   $338334$   $298689$   $468201$     $515983$    $-516163$   $516163$

Here $S_0$ is the unconditional witness and $S_h$ the conditional witness. At every checked prefix the exact specializations of [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"} are $$S_0=Q_1-V_2-Q_2,
 \qquad
 2S_h=2Q_1-D_2-U_2-V_2-Q_2.$$ These rows are finite reproductions only. They neither estimate an asymptotic rate nor test convergence.

# Frontier and gates

Route A is `GO`: finite-window safety, the thirteen-table census, the rank-five arithmetic interface, exact online extrema, two narrow minimality results, and the single-policy obstruction are proved. Route B is `STOP_SCOPED`: the six hard lag tables stop exactly at ordinary shift-two Chowla cancellation, and the full adaptive capacity still stops at the RH-371/RH-377 envelope rather than at a proved limit [@RH371; @RH377]. RH-372's bounded-transducer framework does not remove these higher-order arithmetic requirements [@RH372].

All Gates A--E remain false/open. We have no canonical dynamical spectral determinant, scattering or unitary completion, self-adjoint generator, von-Mangoldt prime-power trace law, or completed-zeta divisor identity. Nothing here constructs a Hilbert--Pólya operator, identifies Riemann zeros, or proves RH. A genuine next step requires either a theorem implying $D_2=o(N)$ or a new exact reduction of the adaptive capacity envelope; a larger finite fit alone is not a reopen trigger.
