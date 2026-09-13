---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--177-random-projective-hyperplane-toggling"
canonical_tex: "symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/main.tex"
canonical_pdf: "symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/main.pdf"
source_sha256: "fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Random Projective-Hyperplane Toggling Is a Disjoint Union of Crown Walks

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/177-random-projective-hyperplane-toggling>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/177-random-projective-hyperplane-toggling/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $E=\mathbb F_2^d\setminus\{0\}$, and repeatedly toggle the points in the kernel of a uniformly sampled nonzero linear form. We determine this chain on the full $2^{2^d-1}$-state subset carrier. Its communicating classes are $2^{2^d-d-2}$ equal cosets, and every class is simple random walk on the crown graph $K_{2^d,2^d}$ with one perfect matching removed. Fourier inversion gives the exact number of ordered histories between every pair of states at every time. The resulting law converges within its parity-compatible half at exact total-variation distance $1/(2^d(2^d-1)^{t-1})$; it does not mix in ordinary total variation because the chain has period two. On the whole carrier the only eigenvalues are $1,-1,\pm(2^d-1)^{-1}$, with all multiplicities explicit and no Jordan blocks. Simplex-code, incidence-design, Cayley/Fourier, and crown-graph facts are treated as background. The residual claim remains [owner\_amber]{.smallcaps}; external circulation is [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Random Projective-Hyperplane Toggling Is a\
  Disjoint Union of Crown Walks
```

## Markdown 正文

# Model, background boundary, and theorem

Fix $d\ge2$, put $V=\mathbb F_2^d$, $E=V\setminus\{0\}$, and write $$\label{eq:parameters}
             q=2^d,\qquad N=q-1,\qquad m=|E|=N.$$ We identify a subset of $E$ with its incidence word in $\mathbb F_2^E$; addition of words is symmetric difference. At each epoch choose, independently and uniformly, a nonzero form $\ell\in V^*\setminus\{0\}$ and update $$\label{eq:update}
 A\longmapsto A+ h_\ell,
 \qquad h_\ell=\mathbf 1_{H_\ell},\qquad
 H_\ell=\{x\in E:\ell(x)=0\}.$$ Over $\mathbb F_2$, the nonzero forms index the projective hyperplanes without a scalar ambiguity. The zero form is not sampled. In particular, $|H_\ell|=2^{d-1}-1$ is odd.

Projective systems and simplex codes are standard coding-theoretic objects [@KwiatkowskiPankovPasini2018]; binary codes, symmetric-difference designs, and projective hyperplane sections also have a direct established connection [@Tonchev1993]. Walks involving generating sets of Abelian groups provide broader Markov-chain context [@DiaconisSaloffCoste1996]. Brown's hyperplane-chamber walks [@Brown2000] are a useful terminology control but have a different state space and update from [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. We assign simplex-code and incidence language, symmetric difference, Cayley-graph reduction, finite-abelian character calculus, the named crown graph, and its elementary spectrum no contribution credit. The calculations below are included to make the literal conjunction self-contained.

For $a\in V^*$ define the evaluation word $$\label{eq:code}
 c_a=(a(x))_{x\in E},\qquad
 \mathcal C=\{c_a:a\in V^*\},\qquad
 \mathcal W=\langle\mathbf 1,\mathcal C\rangle\le \mathbb F_2^E,$$ where $\mathbf 1$ is the all-one word. Let $P$ be the transition operator of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} and set $$\label{eq:K}
                  K=2^{m-d-1}.$$

[\[thm:main\]]{#thm:main label="thm:main"} The following statements hold for every $d\ge2$.

(i) The closed communicating classes are precisely the $K$ cosets of $\mathcal W$. Each has $2q$ states, all states are recurrent, and the support on each class is the crown graph $K_{q,q}$ with one perfect matching deleted. The chain is simple random walk on that graph and has period two.

(ii) For $t\ge0$ and $A,B\subseteq E$, the endpoint lies in the parity-compatible phase exactly when there is a unique $L\in V^*$ such that $$\label{eq:endpoint-condition}
                  A+B=(t\bmod2)\mathbf 1+c_L.$$ When this condition holds, the number of ordered form histories is $$\label{eq:history-count}
      a_t(L)=\begin{cases}
      q^{-1}\bigl(N^t+N(-1)^t\bigr),&L=0,\\
      q^{-1}\bigl(N^t-(-1)^t\bigr),&L\ne0,
      \end{cases}
      \qquad P^t(A,B)=\dfrac{a_t(L)}{N^t}.$$ A history exists exactly when [\[eq:endpoint-condition\]](#eq:endpoint-condition){reference-type="eqref" reference="eq:endpoint-condition"} holds and $a_t(L)>0$: this requires $L=0$ at $t=0$, $L\ne0$ at $t=1$, and permits every $L$ at $t\ge2$. Outside [\[eq:endpoint-condition\]](#eq:endpoint-condition){reference-type="eqref" reference="eq:endpoint-condition"}, $P^t(A,B)=0$.

(iii) Put $$\label{eq:phase}
       \Phi_t(A)=A+(t\bmod2)\mathbf 1+\mathcal C$$ and let $U_{\Phi_t(A)}$ be uniform on these $q$ states. For $t\ge1$, $$\label{eq:phase-tv}
       \left\|P^t(A,\cdot)-U_{\Phi_t(A)}\right\|_{\mathrm{TV}}
             =\frac{1}{qN^{t-1}}.$$ If $\pi_{A+\mathcal W}$ is uniform on the full communicating class, then $$\label{eq:ordinary-tv}
       \left\|P^t(A,\cdot)-\pi_{A+\mathcal W}\right\|_{\mathrm{TV}}
       =\begin{cases}
       \frac12+\frac{1}{2q},&t=1,\\[1mm]
       \frac12,&t\ge2.
       \end{cases}$$ Thus [\[eq:phase-tv\]](#eq:phase-tv){reference-type="eqref" reference="eq:phase-tv"} is parity-phase convergence, not ordinary mixing.

(iv) On the entire $2^m$-state carrier, the eigenvalues and algebraic multiplicities are $$\label{eq:spectrum-table}
     \begin{array}{c|cccc}
     \lambda&1&-1&1/N&-1/N\\ \hline
     \operatorname{mult}(\lambda)&K&K&NK&NK.
     \end{array}$$ Boolean characters give a complete eigenbasis. Hence there are no other eigenvalues and no nontrivial Jordan blocks.

(v) Within this family, the degree $N$ of one unlabelled component recovers $d=\log_2(N+1)$. If the total state count is also supplied, then it recovers $K$ as the number of components. This is not a characterization among arbitrary regular bipartite graphs.

For reference, the theorem's quantitative spine is

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  object                exact value
  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  class decomposition   $K=2^{m-d-1}$ cosets, each of size $2q$

  component support     $K_{q,q}$ minus a matching; degree $N$; period $2$

  endpoint kernel       [\[eq:endpoint-condition\]](#eq:endpoint-condition){reference-type="eqref" reference="eq:endpoint-condition"}--[\[eq:history-count\]](#eq:history-count){reference-type="eqref" reference="eq:history-count"}

  phase convergence     $1/(qN^{t-1})$ in total variation

  global spectrum       $1,-1,1/N,-1/N$ with multiplicities $K,K,NK,NK$
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Code coordinates and crown components

[\[lem:code\]]{#lem:code label="lem:code"} The map $a\mapsto c_a$ is injective and linear, $\mathbf 1\notin\mathcal C$, and $\dim\mathcal W=d+1$. Moreover, the masks $h_\ell$, $\ell\ne0$, generate $\mathcal W$.

Linearity is coordinatewise. If $a\ne0$, some nonzero $x$ satisfies $a(x)=1$, so $c_a\ne0$ and the evaluation map is injective. A nonzero form has a kernel of dimension $d-1\ge1$; hence it cannot equal one on every nonzero vector. Thus $\mathbf 1\notin\mathcal C$, proving $\dim\mathcal W=d+1$.

For every nonzero $\ell$ and $x\in E$, $$\label{eq:mask-code}
          h_\ell(x)=1+\ell(x),\qquad h_\ell=\mathbf 1+c_\ell.$$ Given $u\ne0$, choose $a\notin\{0,u\}$, which is possible because $d\ge2$, and put $b=a+u$. Then $a,b$ are nonzero and $h_a+h_b=c_{a+b}=c_u$. Finally $\mathbf 1=h_u+c_u$, so the masks generate both $\mathcal C$ and $\mathbf 1$.

A walk on an additive group remains in the coset of the subgroup generated by its increments. Lemma [\[lem:code\]](#lem:code){reference-type="ref" reference="lem:code"} identifies that subgroup as $\mathcal W$, so its cosets are exactly the closed irreducible classes. Their size is $2^{d+1}=2q$, and [\[eq:K\]](#eq:K){reference-type="eqref" reference="eq:K"} gives their number. Finite closed irreducible classes contain only recurrent states.

Fix a coset representative $R$. The unique code coordinates give a bijection $$\label{eq:crown-coordinates}
 R+\epsilon\mathbf 1+c_a\longleftrightarrow(\epsilon,a),
 \qquad (\epsilon,a)\in\mathbb F_2\times V^*.$$ By [\[eq:mask-code\]](#eq:mask-code){reference-type="eqref" reference="eq:mask-code"}, a step indexed by $\ell\ne0$ sends $(\epsilon,a)$ to $(\epsilon+1,a+\ell)$. It therefore joins $(0,a)$ to every $(1,b)$ except $b=a$, exactly the crown graph $K_{q,q}$ minus its diagonal matching. Every edge changes subset parity because every mask has odd weight. Thus all returns have even length, while repeating any mask gives a two-step return. The period is exactly two.

# Ordered histories and the two TV comparisons

After the ordered choices $\ell_1,\ldots,\ell_t$, linearity in [\[eq:mask-code\]](#eq:mask-code){reference-type="eqref" reference="eq:mask-code"} gives the total increment $$\label{eq:increment}
 \sum_{r=1}^t h_{\ell_r}=(t\bmod2)\mathbf 1+c_L,
 \qquad L=\sum_{r=1}^t\ell_r.$$ Injectivity of $a\mapsto c_a$ proves the endpoint condition and uniqueness in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(ii).

The additive characters of $V^*$ give the exact number of ordered nonzero summands with sum $L$: $$\label{eq:fourier-count}
 a_t(L)=\frac1q\sum_{y\in V^{**}}(-1)^{y(L)}
       \left(\sum_{\ell\ne0}(-1)^{y(\ell)}\right)^t.$$ The inner sum is $N$ for the trivial character and $-1$ otherwise. The sum of all nontrivial characters at $L$ is $N$ when $L=0$ and $-1$ otherwise. This proves [\[eq:history-count\]](#eq:history-count){reference-type="eqref" reference="eq:history-count"}, including $t=0$. Division by the $N^t$ equiprobable histories proves the transition formula. Directly in [\[eq:history-count\]](#eq:history-count){reference-type="eqref" reference="eq:history-count"}, $a_0(L)$ is positive only for $L=0$, $a_1(L)$ is positive only for $L\ne0$, and both displayed values are positive for every $L$ when $t\ge2$. These are precisely the asserted support cases.

On the $q$-point set [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"}, the probability deviations from $1/q$ are $$\label{eq:deviations}
 p_t(0)-\frac1q=\frac{(-1)^t}{qN^{t-1}},\qquad
 p_t(L)-\frac1q=-\frac{(-1)^t}{qN^t}\quad(L\ne0).$$ Half the sum of their absolute values is $1/(qN^{t-1})$, proving [\[eq:phase-tv\]](#eq:phase-tv){reference-type="eqref" reference="eq:phase-tv"}.

The connected regular crown walk has the uniform stationary law on all $2q$ component vertices. At $t=1$, one point in the occupied parity half has mass zero and the other $N$ points have mass $1/N$; direct subtraction from $1/(2q)$ gives the first line of [\[eq:ordinary-tv\]](#eq:ordinary-tv){reference-type="eqref" reference="eq:ordinary-tv"}. For $t\ge2$, [\[eq:deviations\]](#eq:deviations){reference-type="eqref" reference="eq:deviations"} and $N\ge3$ show that every probability in the occupied half exceeds $1/(2q)$. That half contributes total absolute deviation $1/2$, and the empty half contributes another $1/2$. Dividing by two proves the second line. In particular, the phase limit must not be reported as ordinary mixing.

# Full-carrier spectrum and reconstruction

For $S\subseteq E$, define the Boolean character $$\label{eq:boolean-character}
 \chi_S(A)=(-1)^{|S\cap A|},\qquad
 \sigma(S)=\sum_{x\in S}x\in V.$$ These $2^m$ characters form an orthogonal basis on $\mathbb F_2^E$.

Convolution by the uniform mask measure makes $\chi_S$ an eigenvector with eigenvalue $$\label{eq:eigen-character}
 \lambda_S=\frac1N\sum_{\ell\ne0}(-1)^{|S\cap H_\ell|}.$$ Modulo two, $|S\cap H_\ell|=|S|+\ell(\sigma(S))$. Character orthogonality therefore gives $$\label{eq:eigen-cases}
 \lambda_S=\begin{cases}
 (-1)^{|S|},&\sigma(S)=0,\\
 (-1)^{|S|+1}/N,&\sigma(S)\ne0.
 \end{cases}$$

It remains to count the four cases without hiding a rank assumption. The linear map $$\label{eq:parity-sum-map}
 \mathbb F_2^E\longrightarrow\mathbb F_2\oplus V,\qquad
 S\longmapsto (|S|\bmod2,\sigma(S))$$ has columns $(1,x)$ for $x\in E$. For any $u\ne0$, choose $x\notin\{0,u\}$; then $(1,x)+(1,x+u)=(0,u)$. These vectors span $\{0\}\oplus V$, and $(1,x)+(0,x)=(1,0)$ supplies the remaining direction. The map is surjective, so every fibre has size $2^{m-d-1}=K$. Sorting [\[eq:eigen-cases\]](#eq:eigen-cases){reference-type="eqref" reference="eq:eigen-cases"} by parity and by whether $\sigma(S)$ vanishes proves [\[eq:spectrum-table\]](#eq:spectrum-table){reference-type="eqref" reference="eq:spectrum-table"}. The full character basis also proves diagonalizability, so no Jordan block is concealed by the repeated multiplicities.

The crown support has degree $N$ because the $N$ nonzero forms give distinct masks. Hence $N+1=2^d$ recovers $d$. A component has $2(N+1)=2q$ states; dividing the supplied total state count by this number recovers $K$. The argument uses the promised family and makes no inverse claim for an arbitrary graph with the same degree and order.

# Exact controls, exclusions, and status

The paper-local author-side verifier uses only integer and rational arithmetic and imports no scouting or prior-paper code. It checks $1{,}095{,}999$ exact assertions: literal carriers, cosets, neighborhoods, and Boolean characters through $d=4$; ordered histories through five steps in those boxes; and the algebraic formulas through $d=8$ and sixteen steps. This is falsification pressure, not a proof or an owner-search instrument.

At $d=1$, the sole projective hyperplane is empty, so the chain is the identity rather than a crown walk. Sampling the zero form for $d\ge2$ would add an empty mask; toggling hyperplane complements would replace the generators $\mathbf 1+c_\ell$ by $c_\ell$. Neither variant is covered. No claim is made for nonbinary spaces.

The remaining claim is deliberately owner-thin: the literal process plus the disjoint-crown conjugacy, exact labelled history kernel, parity-phase TV, and full-carrier multiplicity lift. Generic Fourier and the finite-group proof shell already appear in the internal P145 line and receive zero separation credit. A bounded literature non-hit is not a novelty result. The author-side gate is [owner\_amber]{.smallcaps}, and the external lifecycle is [hold\_external]{.smallcaps}.
