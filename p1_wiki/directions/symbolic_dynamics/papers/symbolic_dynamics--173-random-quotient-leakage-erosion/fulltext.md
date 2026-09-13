---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--173-random-quotient-leakage-erosion"
canonical_tex: "symbolic_dynamics/papers/173-random-quotient-leakage-erosion/main.tex"
canonical_pdf: "symbolic_dynamics/papers/173-random-quotient-leakage-erosion/main.pdf"
source_sha256: "b28cfc0fa8b848cce50e48cbf12bb63dd7ac95d7fae7fb0b700ce34d7e0b35d4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Random Quotient-Leakage Erosion: Every-Target Fibres and a Complementary Jordan Ladder

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/173-random-quotient-leakage-erosion>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/173-random-quotient-leakage-erosion/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/173-random-quotient-leakage-erosion/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/173-random-quotient-leakage-erosion/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/173-random-quotient-leakage-erosion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $V=\mathbb F_q^n$. At every epoch, resample a uniform endomorphism $T$ of $V$ and replace the current subspace $U$ by $U\cap T^{-1}(U)$. Factoring $T|_U$ through $V/U$ identifies the update with the kernel of a uniform quotient map. This gives the exact fibre of every labelled target, an $(n+1)$-state dimension quotient, and every-time labelled transition probabilities. The full transition operator has algebraic eigenvalues $q^{-a(n-a)}$ with Gaussian multiplicities. In the dimension quotient, each equality between complementary dimensions $a$ and $n-a$ produces a forced $2$-by-$2$ Jordan block away from the endpoints. For $n\ge1$ the two endpoint occurrences of eigenvalue one are semisimple, whereas at $n=0$ they coincide and give one $J_1(1)$. Exact absorption formulas complete the finite atlas. Finite-field rank laws, Gaussian incidence, and generic triangular-chain algebra are treated as background; the external status is [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: 'Random Quotient-Leakage Erosion: Every-Target Fibres and a Complementary Jordan Ladder'
```

## Markdown 正文

# The quotient-kernel chain

Fix a prime power $q$ and an $n$-dimensional vector space $V$ over $\mathbb F_q$. Let $T_1,T_2,\ldots$ be independent uniform elements of $\operatorname{End}(V)$ and set $$\label{eq:update}
                 U_r=U_{r-1}\cap T_r^{-1}(U_{r-1}).$$ This is a Markov chain on the full labelled subspace lattice. The ordinary rank and nullity distributions of uniform finite-field matrices are well developed; the uniform rectangular ensemble is treated directly by @FulmanGoldstein2015. @Balakin1968 is broader nonuniform, sparse random-rank background rather than an owner of that uniform count, and Gaussian subspace enumeration is classical [@GoldmanRota1970]. Those rank laws, the Gaussian subspace census, the symmetry refinement to a fixed kernel, the elementary ambient-lift exponent, and generic finite-chain facts are assigned no contribution credit here. Evans's elementary-divisor filtration gives a dimension-chain precursor, and Van Peski's labelled refinement reduces a descending subspace transition to the kernel of a uniform square map and derives its fixed-target injection count [@Evans2002; @VanPeski2018]. That uniform-kernel architecture and ordinary Markov powering also receive zero credit. Our narrow object is the fixed- ambient rectangular codimension schedule in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} and the complementary spectral resonance it forces.

For $0\le b\le a\le n$, put $d=a-b$ and define $$\label{eq:C}
 C_{n,q}(a,b)=
 \begin{cases}
 \displaystyle\prod_{i=0}^{d-1}(q^{n-a}-q^i),&d\le n-a,\\[2mm]
 0,&d>n-a.
 \end{cases}$$ The empty product is one. Write $\genfrac{[}{]}{0pt}{}{a}{b}_{q}$ for a Gaussian coefficient and let $$\label{eq:Q}
 Q_{ab}=\genfrac{[}{]}{0pt}{}{a}{b}_{q}\frac{C_{n,q}(a,b)}{q^{a(n-a)}}
 \quad(0\le b\le a\le n),$$ with all other entries zero. Let $P$ be the full transition matrix indexed by labelled subspaces.

[\[thm:main\]]{#thm:main label="thm:main"} The chain [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} has the following exact description.

(i) Fix $B\le U\le V$ with $\dim U=a$ and $\dim B=b$. Then $$\label{eq:ambient-fibre}
     \#\{T\in\operatorname{End}(V):U\cap T^{-1}(U)=B\}
     =q^{n^2-a(n-a)}C_{n,q}(a,b).$$ A target not contained in $U$ has empty fibre. Consequently $$\label{eq:one-step}
     P(U,B)=\frac{C_{n,q}(a,b)}{q^{a(n-a)}}.$$

(ii) The matrix $Q$ in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} is the dimension transition matrix. For every $t\ge0$ and every fixed $B\le U$, $$\label{eq:alltime}
                  P^t(U,B)=\frac{(Q^t)_{ab}}{\genfrac{[}{]}{0pt}{}{a}{b}_{q}}.$$ The probability is zero when $B\nleq U$.

(iii) The complete algebraic eigenvalue multiset of $P$ is $$\label{eq:spectrum}
       \left\{q^{-a(n-a)}\text{ with multiplicity }\genfrac{[}{]}{0pt}{}{n}{a}_{q}:
                                            0\le a\le n\right\}.$$ The full Jordan form is not asserted. The Jordan form of the dimension quotient $Q$, however, is completely determined: the eigenvalue one has two $J_1$ blocks when $n\ge1$, while for $n=0$ the quotient is the single block $J_1(1)$; for every $1\le b<n/2$, the common eigenvalue $$\label{eq:paired-eigenvalue}
                       q^{-b(n-b)}=q^{-(n-b)b}$$ has one $J_2$ block; and when $n$ is positive and even, the middle eigenvalue $q^{-n^2/4}$ has one $J_1$ block.

(iv) The subspaces $0$ and $V$ are fixed. Every proper nonzero starting subspace is absorbed at $0$ almost surely. If $0<a<n$, then $$\begin{aligned}
      \mathbb P_a(\tau_0\le t)&=(Q^t)_{a0},                       \label{eq:cdf}\\
      E_0&=0,\qquad
      E_a=\frac{1+\sum_{b<a}Q_{ab}E_b}{1-Q_{aa}}=\mathbb E_a\tau_0.
                                                                    \label{eq:mean}\end{aligned}$$ For $n=2$ the sole transient row is $$\label{eq:n2}
      Q_{10}=\frac{q-1}{q},\qquad Q_{11}=\frac1q,
      \qquad E_1=\frac q{q-1},$$ while $0$ and $V$ remain fixed.

# Every-target fibres and labelled powers

Let $\pi_U:V\to V/U$ be the quotient projection. Only the map $$\label{eq:leak-map}
 L_T=\pi_U\circ T|_U:U\longrightarrow V/U$$ is visible to the update, and $$\label{eq:kernel}
                  U\cap T^{-1}(U)=\ker L_T.$$

The linear map $$\operatorname{End}(V)\longrightarrow\operatorname{Hom}(U,V/U),\qquad T\longmapsto L_T,$$ is surjective. Its codomain has dimension $a(n-a)$, so every quotient map has $q^{n^2-a(n-a)}$ lifts to an ambient endomorphism. Requiring $\ker L_T=B$ is equivalent to requiring the induced map $U/B\to V/U$ to be injective. There are exactly $$\prod_{i=0}^{a-b-1}(q^{n-a}-q^i)=C_{n,q}(a,b)$$ such maps, with none when $a-b>n-a$. Multiplying by the common number of lifts proves [\[eq:ambient-fibre\]](#eq:ambient-fibre){reference-type="eqref" reference="eq:ambient-fibre"}; dividing by $q^{n^2}$ proves [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"}.

Summing [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"} over the $\genfrac{[}{]}{0pt}{}{a}{b}_{q}$ subspaces $B\le U$ of dimension $b$ proves both the row-sum identity for [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} and the dimension quotient.

Every trajectory is nested. Moreover, the stabilizer of $U$ in $\operatorname{GL}(V)$ acts transitively on its $b$-subspaces and preserves the distribution of the freshly sampled endomorphisms. For two such targets $B,B'$, choose a stabilizer element $g$ with $gB=B'$. Conjugating every map in a complete history by $g$ is an unconditional probability-preserving bijection between the raw events $\{U_t=B\}$ and $\{U_t=B'\}$, including when both events have mass zero. Thus all $\genfrac{[}{]}{0pt}{}{a}{b}_{q}$ labelled endpoint probabilities are equal. Their total mass is $(Q^t)_{ab}$, giving [\[eq:alltime\]](#eq:alltime){reference-type="eqref" reference="eq:alltime"}, including $t=0$.

Thus the small quotient loses no labelled endpoint information: once $Q^t$ is known, one division recovers every reachable target.

# Complementary-dimension resonance

Order the labelled subspaces by nondecreasing dimension. The transition matrix is lower triangular because [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} only decreases the state. Remaining at an $a$-space is equivalent to $L_T=0$, hence $$\label{eq:diagonal}
                         P(U,U)=q^{-a(n-a)}.$$ There are $\genfrac{[}{]}{0pt}{}{n}{a}_{q}$ such subspaces, proving the algebraic multiset [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"}.

[\[lem:adjacent\]]{#lem:adjacent label="lem:adjacent"} For $1\le k\le n-1$, the adjacent entry $Q_{k,k-1}$ is positive.

Here the dimension loss is one and the codomain has dimension $n-k\ge1$. Thus $C_{n,q}(k,k-1)=q^{n-k}-1>0$ in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}.

The exponent $x(n-x)$ is strictly concave and symmetric around $n/2$. Consequently the only repetitions among the diagonal entries of $Q$ are the complementary pairs $b,n-b$, together with the endpoints $0,n$.

Fix $1\le b<n/2$, put $a=n-b$, and let $\lambda=q^{-b(n-b)}$. Consider the right-eigenvector recursion $(Q-\lambda I)x=0$ in increasing row order. Rows below $b$ force $x_0=\cdots=x_{b-1}=0$, while row $b$ leaves $x_b$ free. Scale a putative eigenvector born there so that $x_b=1$. For $b<k<a$, strict concavity gives $Q_{kk}<\lambda$, and the recursion reads $$x_k=\frac{\sum_{j<k}Q_{kj}x_j}{\lambda-Q_{kk}}>0.$$ The inequality follows inductively from Lemma [\[lem:adjacent\]](#lem:adjacent){reference-type="ref" reference="lem:adjacent"}. At row $a$, however, the diagonal again equals $\lambda$, while the compatibility sum is strictly positive because it contains $Q_{a,a-1}x_{a-1}>0$. Hence no eigenvector can be born at $b$.

The eigenvector born at $a$ remains, so this algebraically double eigenvalue has geometric multiplicity one and therefore one $J_2$ block. At eigenvalue one and $n\ge1$, the constant column vector is a right eigenvector because $Q$ is row stochastic, while the indicator column of the full-dimension state is a second right eigenvector because no lower-dimensional row reaches dimension $n$ and $Q_{nn}=1$. They are independent, so the algebraically double endpoint eigenvalue gives two $J_1$ blocks. If $n$ is positive and even, the midpoint occurs only once and gives one $J_1$. These blocks exhaust the $n+1$ quotient dimensions. When $n=0$, the endpoint states coincide, $Q=(1)$, and the inventory is instead one $J_1(1)$.

Functions depending only on subspace dimension form a $P$-invariant subspace represented by $Q$. Therefore every displayed $J_2$ is also a genuine obstruction to diagonalizability of the full operator. We do not infer the remaining full-operator Jordan multiplicities from this quotient.

# Absorption, boundaries, and claim boundary

The quotient in [\[eq:leak-map\]](#eq:leak-map){reference-type="eqref" reference="eq:leak-map"} is zero when $U=0$ or $U=V$, so those states are fixed. If $0<\dim U<n$, there is positive probability that $L_T$ is nonzero, and hence positive probability of strict dimension loss. The finite nested chain consequently reaches zero almost surely. Formula [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is [\[eq:alltime\]](#eq:alltime){reference-type="eqref" reference="eq:alltime"} with the unique zero-dimensional target. First-step conditioning gives [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}. Substitution in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} gives [\[eq:n2\]](#eq:n2){reference-type="eqref" reference="eq:n2"}. The cases $n=0$ and $n=1$ consist only of fixed boundary states.

The residual claim is intentionally narrower than random-matrix rank theory. The uniform finite-field nullity law studied by Fulman and Goldstein owns the dimension-level matrix count used in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"}; Balakin's sparse, nonuniform ensemble is only broader random-rank context [@Balakin1968; @FulmanGoldstein2015]. Gaussian incidence owns the number of labelled subspaces [@GoldmanRota1970]; fixed-kernel uniformity is its standard symmetry refinement; the ambient lift factor is elementary linear algebra; and triangular spectra, Jordan recursions, and hitting-time identities are standard. Evans's dimension precursor and Van Peski's labelled square-kernel chain own the descending-subspace architecture, fixed-target injection count, Gaussian lumping, and ordinary powers [@Evans2002; @VanPeski2018]. Their current $a$-space maps to an $a$-dimensional codomain inside a filtration of one Haar local-field matrix; P173 instead resamples in one fixed $n$-space and sees the rectangular map $U\to V/U$ of dimensions $a\to n-a$. The sources do not supply this complementary-codimension schedule or its Jordan ladder.

Internally, P109, P162, P165, and P168 own their subspace carriers, random-intersection language, and reusable proof devices. The same-batch P172 additionally owns fresh ambient maps, nested erosion, a small quotient, labelled recovery, triangular/Jordan tactics, and absorption formulas. Those shared shells earn zero separation credit. P172's inverse axis is specified-box set-image occupancy with one terminal $J_2$; it does not specialize to the present linear injection fibre. What remains under evaluation here is only the literal fixed-ambient leakage schedule $a\to n-a$, its every-target realization inside [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, and the forced complementary-dimension Jordan ladder.

The standalone verifier independently enumerates every binary subspace and every ambient endomorphism through $n=3$, checks labelled powers through four epochs, and tests exact rational Jordan nullities for $q\in\{2,3,4,5\}$ through $n=9$. These computations can falsify arithmetic or boundary errors but do not prove the uniform statements. The source search was bounded; a non-hit is not evidence of novelty, priority, or freedom to operate. The manuscript therefore remains anonymous and [hold\_external]{.smallcaps}.
