---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-372-bounded-constraint-graph-transducer-certificates"
canonical_tex: "zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/main.pdf"
source_sha256: "059f8bee897d6b4b4cfdf0bbb9fb7908b1cb27b53691097b725f54fcd2724b90"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Bounded constraint-graph transducer certificates for arithmetic capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-372-bounded-constraint-graph-transducer-certificates/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate a finite, reusable theorem behind several arithmetic capacity experiments. A finite directed constraint graph with a bounded vertex observable admits an exact open-prefix max-plus dynamic program. A clocked finite-memory transducer is called universally safe when every possible pair of inputs produces a legal graph edge. If its observed label is a one-site factor of the current clock phase and the current Mobius value, then its Mobius correlation has an unconditional arithmetic-progression formula in terms of squarefree densities. Consequently every such certificate gives a rigorous lower bound on the graph capacity liminf, and all certificates with fixed clock and memory budgets form a finite enumerable class. We verify the contract on the RH-366 four-state graph, the distinct RH-368 three-cell factor, and a new period-three safe switch on the RH-366 graph. Labels that depend on memory are explicitly left open because they require higher-order Mobius correlations. This is a bounded classification result, not a classification of all subshifts and not a spectral or zeta construction.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: |
  Bounded constraint-graph transducer certificates\
  for arithmetic capacity
```

## Markdown 正文

# Frozen data and claim boundary

RH-366 fixes a four-state survivor whose state order is $(--,-+,+-,++)$ and whose adjacency matrix is $$A_{366}=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix},
\qquad
\ell_{366}=(-1,-1,1,1).
\label{eq:rh366graph}$$ The graph path records a pair of consecutive signs, so this is the distance-two constraint used by RH-366 [@RH366]. RH-368 supplies a different three-cell graph $$A_{368}=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
\qquad
\ell_{368}=(1,-1,-1),
\label{eq:rh368graph}$$ with its parity factor and all-order capacity theorem [@RH368]. We use both only as frozen finite graph inputs; the two languages are not identified.

For a finite directed graph $G=(V,E)$ and an integer observable $\ell:V\to\mathbb Z$, write $$K_N(G,\ell)=
 \max_{\substack{v_1,\ldots,v_N\in V\\(v_n,v_{n+1})\in E}}
 \lvert\sum_{n=1}^N \mu(n)\ell(v_n)\rvert.
 \label{eq:capacity}$$ The optimizing open path may depend on the complete prefix. This definition is a finite scalar functional; it is not a trace or a determinant.

# Exact graph capacity

Assume every vertex has an incoming edge (as in the frozen graphs above). Put $$D_1^{\pm}(v)=\pm\mu(1)\ell(v),
\qquad
D_{n+1}^{\pm}(v)=\pm\mu(n+1)\ell(v)
 +\max_{(u,v)\in E}D_n^{\pm}(u).
\label{eq:dp}$$ Then $$K_N(G,\ell)=\max_{v\in V}\max\{D_N^+(v),D_N^-(v)\}.
\label{eq:dp-capacity}$$ The recurrence and a maximizing witness require $O(N\lvert E\rvert)$ integer operations.

Induct on $n$. The value $D_n^+(v)$ is the largest signed score among paths ending at $v$: appending $v$ contributes $\mu(n)\ell(v)$, and the predecessor must be an incoming neighbor. The same induction with the opposite sign gives $D_n^-(v)$, the largest negative of a path score. Taking the maximum over terminal vertices proves [\[eq:dp-capacity\]](#eq:dp-capacity){reference-type="eqref" reference="eq:dp-capacity"}. Each edge is inspected once per step; predecessor pointers give a witness.

For bounded $\ell$, $$\limsup_{N\to\infty}\frac{K_N(G,\ell)}N
\leq \frac{6}{\pi^2}\|\ell\|_\infty.
\label{eq:upper}$$

Every admissible path has absolute score at most $\|\ell\|_\infty\sum_{n\leq N}\mu(n)^2$. The squarefree density is $6/\pi^2$.

# Safe finite-memory transducers

Fix a clock $q\geq1$, a finite state set $S$, and input alphabet $\mathcal A=\{-1,0,1\}$. A transducer consists of maps $$\tau:S\times\mathbb Z/q\mathbb Z\times\mathcal A\to S,
 \qquad
 \omega:S\times\mathbb Z/q\mathbb Z\times\mathcal A\to V.$$ At time $n$, with $a_n=\mu(n)$ and $r_n=n\bmod q$, it outputs $v_n=\omega(s_n,r_n,a_n)$ and updates $s_{n+1}=\tau(s_n,r_n,a_n)$.

The table $(\tau,\omega)$ is universally safe on $G$ if, for every $s\in S$, $r\in\mathbb Z/q\mathbb Z$, and $a,b\in\mathcal A$, $$\bigl(\omega(s,r,a),
 \omega(\tau(s,r,a),r+1,b)\bigr)\in E.
\label{eq:safety}$$ It has a one-site observed factor if there are functions $g_r:\mathcal A\to\mathbb Z$ with $$\ell(\omega(s,r,a))=g_r(a)
 \quad\text{for every }s,r,a.
\label{eq:onesite}$$

The universal quantifier in [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"} is intentional. It is a finite table check and does not assume anything about future Mobius values. The one-site condition is the arithmetic firewall: the internal memory may choose a legal path, but it may not alter the observed label.

For $r\in\mathbb Z/q\mathbb Z$, $$\frac1N\#\{n\leq N:n\equiv r\pmod q,\mu(n)^2=1\}
 \longrightarrow
 \delta_{q,r}:=
 \sum_{\substack{d\geq1\\(q,d^2)\mid r}}
 \frac{\mu(d)}{\operatorname{lcm}(q,d^2)}.
\label{eq:delta}$$

Use $\mu(n)^2=\sum_{d^2\mid n}\mu(d)$. The simultaneous congruences $n\equiv r\pmod q$ and $d^2\mid n$ are soluble exactly when $(q,d^2)\mid r$, and then have density $1/\operatorname{lcm}(q,d^2)$. Truncating at $d\leq\sqrt N$ gives an $O(\sqrt N)$ counting error; the tail is $O(N/\sqrt N)$. Absolute convergence of the displayed series completes the limit.

Let a universally safe transducer satisfy [\[eq:onesite\]](#eq:onesite){reference-type="eqref" reference="eq:onesite"}. Then its explicit Mobius path obeys $$\lim_{N\to\infty}\frac1N\sum_{n\leq N}\mu(n)\ell(v_n)
 =L(T):=\frac12\sum_{r\bmod q}\delta_{q,r}
       \bigl(g_r(1)-g_r(-1)\bigr).
\label{eq:limit}$$ Consequently, $$|L(T)|\leq\liminf_{N\to\infty}\frac{K_N(G,\ell)}N
 \leq\limsup_{N\to\infty}\frac{K_N(G,\ell)}N
 \leq\frac6{\pi^2}\|\ell\|_\infty.
\label{eq:bracket}$$

For each residue $r$, let $Q_r(N)$ be the squarefree count in [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} and put $$M_r(N)=\sum_{\substack{n\leq N\\n\equiv r\pmod q}}\mu(n).$$ Davenport's fixed-frequency estimate, followed by finite Fourier inversion, gives $M_r(N)=o(N)$. Hence the positive and negative counts in that residue are $(Q_r\pm M_r)/2$. Since zero Mobius values contribute zero to the correlation, the residue-$r$ contribution divided by $N$ is $$\frac{Q_r}{2N}(g_r(1)-g_r(-1))
 +\frac{M_r}{2N}(g_r(1)+g_r(-1)).$$ Apply the lemma and sum over the finitely many residues. The explicit path is admissible by [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"}, so its absolute score is bounded by the capacity; the upper bound is [\[eq:upper\]](#eq:upper){reference-type="eqref" reference="eq:upper"}.

Fix $G,q$, and a memory budget $m=\lvert S\rvert$. The set of all transducer tables satisfying universal safety and the one-site condition is finite and can be exhaustively enumerated. If $$\Gamma_{q,m}(G,\ell)=\max_T\lvert L(T)\rvert,$$ where the maximum is over that finite set, then $$\Gamma_{q,m}(G,\ell)\leq\liminf_{N\to\infty}K_N(G,\ell)/N.$$

There are finitely many choices for the transition and output entries of the tables $S\times(\mathbb Z/q\mathbb Z)\times\mathcal A$, and finitely many initial states. Conditions [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"} and [\[eq:onesite\]](#eq:onesite){reference-type="eqref" reference="eq:onesite"} are finite Boolean tests. The inequality follows by maximizing the individual lower bounds in [\[eq:bracket\]](#eq:bracket){reference-type="eqref" reference="eq:bracket"}.

The proposition is not a classification of all mixing subshifts: $q$ and the memory budget are fixed before enumeration. If the observed label depends on $s_n$, the residue reduction is invalid and higher-order Mobius correlations enter. We do not replace those missing correlations by pair data or by a finite numerical fit.

# Three frozen certificates

## The RH-366 four-state label rule

Use the two-state universal safety completion supplied in the artifact. It has the same one-site labels as the RH-366 rule. Set $$e_n=+1\quad\Longleftrightarrow\quad
 \mu(n)=1\text{ and }n\bmod4\in\{1,2\},$$ and output a graph representative with that label. The state-1 rows at phases 2 and 3 are completion rows; they are not an additional arithmetic observable. The selected residues shift by two to $3,0\pmod4$, so two selected plus signs can never be two places apart. The completed state table is universally safe and its observed factor has $g_1(1)-g_1(-1)=g_2(1)-g_2(-1)=2$, with the other differences zero. Thus $$L(T)=\delta_{4,1}+\delta_{4,2}=\frac4{\pi^2}.$$ This recovers the RH-366 lower certificate, not its unresolved capacity limit.

## The RH-368 three-cell factor

For [\[eq:rh368graph\]](#eq:rh368graph){reference-type="eqref" reference="eq:rh368graph"}, at odd phases output vertex $0$ when $\mu(n)=1$ and vertex $1$ otherwise; at even phases output vertex 2. Every output edge is legal. Since $\ell=(1,-1,-1)$, this has $g_1(1)-g_1(-1)=2$ and gives $$L(T)=\delta_{2,1}=\frac4{\pi^2}.$$ RH-368 proves the separate parity-factor capacity limit; here it is used as an independent frozen graph audit of the general certificate contract.

## A new period-three safe switch

On the RH-366 graph, use the anchor state $0=(--)$. At a phase $n\equiv1\pmod3$, choose the loop $$0\to2\to1\to0$$ when $\mu(n)=1$, and choose $$0\to0\to0\to0$$ otherwise. The two paths have equal length and their observable labels $(-1,1,-1,-1)$ versus $(-1,-1,-1,-1)$ differ only at the first output position. The finite state table also defines safe outputs from every unreachable state, so the universal check is literal rather than trajectory-dependent. Therefore $$g_1(1)-g_1(-1)=2,
 \qquad L(T)=\delta_{3,1}=\frac9{4\pi^2}.$$ This is a new bounded certificate, not a claim about the RH-366 optimizer's limit.

::: {#tab:instances}
  Instance            graph vertices   clock   memory   certified limit
  ------------------- ---------------- ------- -------- -----------------
  RH-366 rule         4                4       2        $4/\pi^2$
  RH-368 factor       3                2       1        $4/\pi^2$
  RH-366 q=3 switch   4                3       2        $9/(4\pi^2)$

  : Finite safe transducer certificates. The constants are exact one-site limits; they are lower bounds for the corresponding open capacities.
:::

# Executable audit

The artifact uses a linear integer Mobius sieve, exact max-plus recurrences, literal universal table checks, and a small exhaustive table enumeration. It checks $N\leq128$ for all three transducer witnesses, an endpoint $N=2^{16}$, and all $3^6=729$ one-state output tables on the RH-368 graph at $q=2$. The source manifest locks nine files and five source commits. These are finite reproduction and provenance checks. The only asymptotic steps are the squarefree-density lemma and the cited Davenport estimate used in the proof.

# Route verdict and Gate ledger

Route A is `GO` narrowly: the max-plus theorem, the finite safety classification, the one-site arithmetic limit, and the three audited certificates form an independent theorem package. Route B is `STOP_SCOPED`. The transducer is an offline arithmetic selector, so the first mismatch occurs before Gate A: no canonical intrinsic operator, determinant, signed von-Mangoldt trace, or completed-zeta divisor is present. The RH-366 capacity limit remains open; memory-dependent labels remain outside the unconditional theorem.

The five project Gates remain false/open. This paper does not construct a Hilbert--Polya operator, identify Riemann zeros, prove a prime-power trace, or prove the Riemann Hypothesis.

# Conclusion

Finite constraint graphs admit a precise arithmetic certificate layer: exact finite optimization, a decidable bounded transducer contract, and an unconditional one-site Mobius limit. The bounded qualifier is the result's strength and its boundary. Increasing memory or allowing the observable to read that memory is a new higher-order arithmetic problem, not something a finite table or pair ledger can silently solve.
