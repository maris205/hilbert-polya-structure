---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--159-parallel-odd-vertex-pruning"
canonical_tex: "symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/main.tex"
canonical_pdf: "symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/main.pdf"
source_sha256: "f6ab9b4c0a2c5081d96597a5884fccd75058a5abfb4aab18e9ec4e57174e0738"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Rank-Transfer Atlas for Parallel Odd-Vertex Pruning

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/159-parallel-odd-vertex-pruning>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/159-parallel-odd-vertex-pruning/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix an ambient label set and iterate the deterministic rule that deletes all currently odd-degree vertices simultaneously. We count every inverse layer of this map. If a fixed target has $s$ vertices and a strict predecessor has $m=s+d$ vertices, then the predecessor fibre is empty for odd $d$ and, for positive even $d$, has size $$\binom{n-s}{d}
   2^{s(d-1)+\binom{d-1}{2}},$$ independently of the target edges. The proof is a rank--nullity calculation for one connected binary incidence system. Orienting this strict transfer with target rank as row and source rank as column makes its powers literal all-time fibres: a non-even target uses $B_n^t$, whereas an even target uses $I+B_n+\cdots+B_n^t$. This yields the exact time-$t$ image, the depth distribution, and all fixed-state counts. Every orbit stabilizes in at most $\lfloor n/2\rfloor$ rounds, sharply for a path. A paper-local exact audit checks $3{,}167{,}525$ assertions, including all states through ambient order six and independent incidence systems through total order nine. Classical parity, incidence, and parallel-peeling facts are used only as zero-credit inputs.
author:
- Anonymous
bibliography:
- references.bib
title: 'A Rank-Transfer Atlas for Parallel Odd-Vertex Pruning'
```

## Markdown 正文

# The labelled map and its complete transfer statement {#sec:setup}

Put $[n]=\{1,\ldots,n\}$, with $[0]=\varnothing$. Let $\mathcal X_n$ be the set of all simple graphs whose vertex set is an arbitrary subset of $[n]$, including the empty graph. For $G\in\mathcal X_n$, write $$D(G)=\{v\in V(G):\deg_G(v)\text{ is odd}\},\qquad
 F(G)=G[V(G)\setminus D(G)].                         \tag{1.1}\label{eq:update}$$ Thus the vertices in $D(G)$ are evaluated in the same current graph and then deleted simultaneously. Set $\rho(G)=|V(G)|$. A graph is called *even* when all its degrees are even; connectivity is not required. The entrance time is $$\tau(G)=\min\{t\geq0:F^t(G)\text{ is even}\}.$$

For $0\leq s,m\leq n$, define the strict rank-transfer matrix $B_n$ by $$\label{eq:B}
 B_n(s,m)=
 \begin{cases}
 \displaystyle \binom{n-s}{d}
 2^{s(d-1)+\binom{d-1}{2}},
     & d=m-s>0\text{ is even},\\[4pt]
 0,  & \text{otherwise}.
 \end{cases}$$ Rows are target ranks and columns are source ranks. In particular, $B_n$ is strictly upper triangular; its zero diagonal does not encode fixed self-predecessors. Let $$C_{n,t}=I+B_n+\cdots+B_n^t,
 \qquad
 e_0=e_1=1,\qquad e_s=2^{\binom{s-1}{2}}\ (s\geq2).$$

Parity-restricted vertex deletion has been studied as a sequential combinatorial game [@NowakowskiOttaway2005; @Kruger2014]. Eulerian and prescribed-parity deletion instead choose edits to meet an optimization or decision constraint [@CyganEtAl2014; @DabrowskiEtAl2016]. Parallel peeling usually refers to simultaneous threshold deletion, for example in random hypergraph core processes [@JiangMitzenmacherThaler2014]. These sources own the neighbouring language and mechanisms, not the claims assigned here. The standard handshaking, incidence-rank, and cycle-space facts used below also receive no contribution credit; see, for example, [@Diestel2017].

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq0$, the map $F$ has the following properties.

(i) Its recurrent states are exactly the even graphs, all fixed. Every orbit satisfies $\tau(G)\leq\lfloor n/2\rfloor$, and the labelled path on $[n]$ attains equality.

(ii) Fix a graph $H$ on a particular $s$-set. For every $m>s$, the number of rank-$m$ graphs sent to $H$ in one step is $B_n(s,m)$, independently of the edges of $H$. At $m=s$ the full one-step fibre has size one if $H$ is even and zero otherwise. For a fixed deleted pair over the empty target there is one source, $K_2$; hence $B_n(0,2)=\binom n2$.

(iii) For every $t\geq0$ and $0\leq m\leq n$, $$\label{eq:iterate-fibre}
       \#\{G\in\mathcal X_n:\rho(G)=m,\ F^t(G)=H\}
       =\begin{cases}
       (B_n^t)(s,m),&H\text{ is not even},\\
       C_{n,t}(s,m),&H\text{ is even}.
       \end{cases}$$

(iv) At time $t=0$, every state occurs. For $t\geq1$, a rank-$s$ graph $H$ lies in $\operatorname{im}(F^t)$ if and only if $$\label{eq:image}
      H\text{ is even}\qquad\text{or}\qquad n-s\geq2t.$$

(v) The phase size, fixed count, depth CDF, and image size are $$\begin{aligned}
     |\mathcal X_n|&=\sum_{s=0}^n\binom ns2^{\binom s2},
                                                            \label{eq:phase}\\
     |\operatorname{Fix}F|&=\sum_{s=0}^n\binom ns e_s,
                                                            \label{eq:fixed}\\
     \#\{G:\tau(G)\leq t\}
     &=\sum_{s=0}^n\binom ns e_s\sum_{m=0}^n C_{n,t}(s,m),
                                                            \label{eq:cdf}\\
     |\operatorname{im}(F^t)|
     &=\sum_{s=0}^n\binom ns
     \left[e_s+\mathbf1_{\{n-s\geq2t\}}
     \left(2^{\binom s2}-e_s\right)\right],\quad t\geq1.
                                                            \label{eq:image-count}\end{aligned}$$ Exact depth shells are successive differences of [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. For $t=0$, the image size is instead [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"}.

The theorem is boundary-complete. For $n=0$ there is one fixed empty state; for $n=1$ the empty and singleton states are both fixed. These carriers have clock zero, as does the formula $\lfloor n/2\rfloor$.

# Forward loss and the sharp clock {#sec:forward}

The handshaking lemma gives $|D(G)|\equiv0\pmod2$. If $G$ is not even, then $D(G)$ is nonempty and has at least two elements, so an active update lowers $\rho(G)$ by at least two. If $G$ is even, then $D(G)=\varnothing$ and $F(G)=G$. Strict rank loss at every other state rules out nontrivial cycles and proves the upper bound $\tau(G)\leq\lfloor\rho(G)/2\rfloor$.

For the path $P_n$, the two endpoints are the only odd-degree vertices. Deleting them leaves $P_{n-2}$ until the empty graph or a singleton remains. Thus $\tau(P_n)=\lfloor n/2\rfloor$, including the $n=0,1$ boundaries.

This clock is a supporting invariant only. The same argument is common to many pruning processes and does not explain the inverse fibres.

# The parity-extension space {#sec:inverse}

Fix a target $H$ on a labelled set $S$, $|S|=s$, and a prospective deleted set $D\subseteq[n]\setminus S$, $|D|=d>0$. A predecessor must agree with $H$ on $\binom S2$. Its free variables $x_{uv}\in\mathbb F_2$ correspond to the $$sd+\binom d2$$ edges having at least one endpoint in $D$. Exact deletion of $D$ and survival of $S$ are equivalent to $$\begin{aligned}
 \sum_{v\in D}x_{uv}&=\deg_H(u)\pmod2,
        &&u\in S,                                      \label{eq:S-equations}\\
 \sum_{w\in(S\cup D)\setminus\{v\}}x_{vw}&=1\pmod2,
        &&v\in D.                                      \label{eq:D-equations}\end{aligned}$$

Let $Q_{S,D}$ be the graph on $S\cup D$ containing precisely the possible variable edges. It is connected when $d>0$, including the one-vertex boundary. The coefficient matrix of [\[eq:S-equations\]](#eq:S-equations){reference-type="eqref" reference="eq:S-equations"}--[\[eq:D-equations\]](#eq:D-equations){reference-type="eqref" reference="eq:D-equations"} is its unoriented incidence matrix over $\mathbb F_2$. Its rank is $s+d-1$: a row vector lies in the left kernel exactly when its endpoint values agree along every edge, hence exactly when it is constant on the connected graph.

Every incidence column has even weight, and the rank calculation shows that the column space is the full even-weight subspace of $\mathbb F_2^{s+d}$. The sum of the right-hand sides is $$\sum_{u\in S}\deg_H(u)+d\equiv d\pmod2.$$ Consequently the system is consistent exactly for even $d$. For positive even $d$, rank--nullity gives $$\begin{aligned}
 &2^{sd+\binom d2-(s+d-1)}
   =2^{s(d-1)+\binom{d-1}{2}}\end{aligned}$$ solutions for the fixed set $D$. Choosing $D$ among the $n-s$ unused labels proves [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}. The count depends on $H$ only through the parity-vector sum, which is automatically zero, proving target independence.

When $d=0$, a same-rank preimage deletes nothing. It must therefore be even and fixed, so it equals $H$; this gives exactly the separate diagonal rule in the theorem. When $s=0,d=2$ and $D$ is fixed, the two odd-degree equations force the sole possible edge, so the unique source is $K_2$.

# Powers, images, and censuses {#sec:atlas}

The orientation of $B_n$ is load-bearing. With target ranks as rows and source ranks as columns, $$\label{eq:composition}
 (B_n^2)(s,m)=\sum_{k=0}^n B_n(s,k)B_n(k,m).$$ For example, $$B_4(0,2)=6,\qquad B_4(2,0)=0,\qquad (B_4^2)(0,4)=24.$$ The reversed convention fails already at the middle value.

A strict predecessor contains the nonempty set of odd vertices deleted by its next update, so it is not even and cannot wait. For a fixed target and an intermediate source rank $k$, Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(ii) supplies $B_n(s,k)$ choices; every such intermediate graph has $B_n(k,m)$ strict rank-$m$ predecessors. Target independence makes this second factor uniform, and the deterministic forward orbit gives each inverse chain a unique intermediate graph. Equation [\[eq:composition\]](#eq:composition){reference-type="eqref" reference="eq:composition"} therefore counts literal two-step chains. Induction gives $B_n^t$ for $t$ strict steps.

If $H$ is not even, every one of the $t$ forward steps ending at $H$ must be strict: an earlier fixed state could never leave itself. If $H$ is even, a source may first reach it after any $j\in\{0,\ldots,t\}$ strict steps and then wait. These first-arrival cases are disjoint and sum to $C_{n,t}$. This proves [\[eq:iterate-fibre\]](#eq:iterate-fibre){reference-type="eqref" reference="eq:iterate-fibre"}, including $t=0$ through $B_n^0=I$.

A reverse strict step adds a positive even number of labels. Hence a non-even rank-$s$ target can have a $t$-step predecessor only if $n-s\geq2t$. Conversely, under this inequality use $t$ rank increments of two; every corresponding transfer entry in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} is positive. Even targets lie in every image through their fixed self-predecessor. This proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}; the identity map supplies the separate $t=0$ case.

Equation [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"} follows by choosing a vertex set and then its edge set. On a fixed $s$-set, even graphs form the kernel of the incidence map of $K_s$. Its dimension is $\binom s2-(s-1)=\binom{s-1}{2}$ for $s\geq1$, with the empty case separate, giving $e_s$ and [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. A graph has $\tau(G)\leq t$ exactly when $F^t(G)$ is one of these even targets. Summing their rank-refined fibres proves [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. Finally, [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} admits all even rank-$s$ targets and, precisely when $n-s\geq2t$, all remaining rank-$s$ targets. This gives [\[eq:image-count\]](#eq:image-count){reference-type="eqref" reference="eq:image-count"} and completes the proof.

Since every nonzero entry of $B_n$ advances rank by at least two, $B_n^{\lfloor n/2\rfloor+1}=0$. Nilpotence here records finite rank loss; it is not an additional contribution axis.

# Exact pressure, collision firewall, and limits {#sec:audit}

The paper-local verifier constructs every graph state through ambient order six using immutable labelled vertex and edge tuples. Independently, it row-reduces every parity system of total order at most nine and every attainable target degree-parity vector. It compares literal strict and full one-step fibres, all iterates through stabilization and beyond, images, image counts, temporal CDFs and shells, fixed counts, path clocks, matrix orientation, and nilpotence.

::: {#tab:audit}
  Lane                                                Exact assertions
  ------------------------------------------------- ------------------
  Binary incidence rank, consistency, and nullity                  726
  Literal one-step fibres and boundary cases                   869,751
  Clock and fixed-state census                                 112,319
  All-time fibres, images, CDFs, and shells                  2,184,715
  Matrix orientation and nilpotence                                 14
  Total                                                      3,167,525

  : Deterministic exact falsification. These checks do not replace the all-parameter proofs.
:::

The enumeration covers $41{,}658$ states, including all $40{,}069$ states at $n=6$, and 511 independently formed parity systems. It uses exact integer and $\mathbb F_2$ arithmetic, no randomness, network access, or third-party package. Finite agreement is counterexample pressure, not proof, owner clearance, novelty evidence, or release authorization.

The internal collision firewall is proof-engine based. Rooted-forest leaf peeling (P114) uses height, Cayley enumeration, and attachment inclusion--exclusion; odd-component complementation (P123) preserves vertices and uses a component/co-component split tree; weighted threshold MIS (P141) uses a random exponential race; random ear deletion (P146) uses dual-tree hook orders; even-level plane-tree contraction (P148) uses depth divisibility and an ordered tree grammar. None mechanically yields the connected binary incidence extension or its rank-only powers. The common silhouette "clock--fibre--image" and all generic pruning language receive zero credit.

# Limitations {#limitations .unnumbered}

The results concern finite, simple, labelled graphs on all subsets of one fixed ambient set. They do not treat asynchronous or random odd-vertex deletion, directed graphs, multigraphs, relabelling or isomorphism classes, weighted edges, asymptotic random-graph laws, or optimization over a chosen deletion set. The bounded source audit does not establish novelty or priority; any direct owner of the simultaneous transfer atlas would require renewed subtraction. The clock, fixed locus, standard parity algebra, and generic matrix multiplication are not claimed contributions.

# Data Availability {#data-availability .unnumbered}

No external data were used. The paper-local verifier and frozen transcript contain the complete deterministic exact control.

# Ethics Statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, animals, personal data, or field intervention.

# Author Contributions {#author-contributions .unnumbered}

The anonymous author performed the derivations, exact checks, source-boundary audit, and manuscript preparation.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The author declares no conflict of interest.

# Funding {#funding .unnumbered}

No external funding is declared.

# Tool-Use Statement {#tool-use-statement .unnumbered}

Automated language and code-generation tools assisted with drafting and verifier implementation. The anonymous author checked the derivations, source metadata, executable controls, and final text and remains responsible for all claims.

# External Status {#external-status .unnumbered}

This artifact remains `HOLD_EXTERNAL`; it is not cleared for posting, submission, circulation, or author contact.
