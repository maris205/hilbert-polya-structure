---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--109-nilpotent-image-subspace-dynamics"
canonical_tex: "symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/main.pdf"
source_sha256: "65561cbeb51c67a41e18c5bfcb4d0df7242baadc81e3ace8117264a866632eae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Nilpotent Image Dynamics on Finite Subspace Lattices: Exact Fibres, Absorption, and Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/109-nilpotent-image-subspace-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $V=\mathbb F_q^d$ and let $N$ be a regular nilpotent endomorphism. We study the finite self-map $T(U)=N(U)$ on the full subspace lattice of $V$. For $0\leq t\leq d$, an $s$-subspace $W\leq\operatorname{im}N^t$, and an integer $r$, the complete fibre formula is $$\#\{U\in\operatorname{Gr}(r,V):N^tU=W\}
   =\genfrac{[}{]}{0pt}{}{t}{r-s}_{q}q^{s(t-r+s)}.$$ It yields every joint transition count for $(\dim U,\dim N^tU)$ and a uniform one-step indegree law. If $G_j(q)=\sum_a\genfrac{[}{]}{0pt}{}{j}{a}_{q}$, then the number of points absorbed by time $t$ is $G_{\min(t,d)}(q)$; hence the exact depth-$t$ layer has size $G_t(q)-G_{t-1}(q)$ for $1\leq t\leq d$. Zero is the unique periodic point, the sharp maximum depth is $d$, and the Artin--Mazur zeta function is $(1-z)^{-1}$. The depth census determines $(q,d)$ whenever $d\geq2$; all one-dimensional fields give the same two-state map. Quotient-fibre geometry and an independent hyperplane recurrence prove the main count. Exhaustive RREF controls over prime and extension fields register $515{,}379$ exact assertions.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Nilpotent Image Dynamics on Finite Subspace Lattices: Exact Fibres, Absorption, and Rigidity'
```

## Markdown 正文

# Introduction and ownership boundary

Fix a prime power $q$, an integer $d\geq1$, and a regular nilpotent endomorphism $N$ of $V=\mathbb F_q^d$. Thus $N^d=0$ and $N^{d-1}\neq0$. The full subspace lattice $\mathcal L(V)$ carries the finite dynamical system $$\label{eq:T}
 T=T_{q,d,N}\colon\mathcal L(V)\longrightarrow\mathcal L(V),
 \qquad T(U)=N(U).$$ The update loses both dimension and position relative to the kernel flag. The resulting functional graph is nevertheless exactly enumerable.

Gaussian coefficients and their interpretation as finite-subspace counts are classical [@GoldmanRota1970; @Prasad2010]. Lattices of subspaces *fixed* by a linear operator, including finite-field enumeration, form another established subject [@BrickmanFillmore1967; @Fripertinger2011]. More directly, Bender, Coley, Robbins, and Rumsey enumerate subspaces by their dimension sequence relative to a linear endomorphism and obtain a regular-nilpotent product formula [@BenderEtAl1992]; Ram gives a recent general solution of the finite-field subspace-profile problem [@Ram2026]. We assign no novelty credit to Gaussian/intersection counts, invariant-subspace lattices, subspace-profile enumeration, or the regular-nilpotent specialization of that theory. Our bounded object is different: the phase contains every subspace, usually non-invariant, and the question is the pointed temporal map $U\mapsto N(U)$. We isolate fibres with a prescribed target $N^tU=W$, then record its absorption tree, local indegrees, and isomorphism rigidity. A targeted search did not locate this exact conjunction, but that query-bounded observation is not a priority or novelty claim. External circulation remains on **HOLD** pending a specialist owner review.

The note proves four concrete statements. First, every $t$-step fibre is uniform once the target dimension is fixed. Second, the kernel flag gives the complete absorption distribution. Third, the functional graph has one periodic vertex and an explicit local indegree. Fourth, its depth census recovers the field size and dimension except for the unavoidable one-dimensional collapse. Two proof routes are kept separate: the first uses exact sequences and graphs of linear maps; the second slices the Grassmannian by a hyperplane and solves the resulting recurrence.

Internally, [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} is neither the rejected saturation map $U\mapsto U+N(U)$ nor Jordan-block substitution discrepancy, invertible shear on integer sublattices, or adjugate dynamics on a full matrix phase. Here the states are all finite-field subspaces and the headline invariant is the full transient fibre census.

# Setup and exact iterates

For $0\leq a\leq b$, write $$\genfrac{[}{]}{0pt}{}{b}{a}_{q}
 =\prod_{i=0}^{a-1}\frac{q^{b-i}-1}{q^{a-i}-1},
 \qquad
 G_b(q)=\sum_{a=0}^{b}\genfrac{[}{]}{0pt}{}{b}{a}_{q}.$$ We set $\genfrac{[}{]}{0pt}{}{b}{a}_{q}=0$ when $a<0$ or $a>b$. Thus $G_b(q)$ is the number of all subspaces of $\mathbb F_q^b$.

Choose a Jordan basis $e_1,\ldots,e_d$ with $$Ne_1=0,\qquad Ne_i=e_{i-1}\quad(2\leq i\leq d).$$ For $t\geq0$, put $$K_t=\ker N^t,\qquad I_t=\operatorname{im}N^t.$$ When $0\leq t\leq d$, one has $\dim K_t=t$ and $\dim I_t=d-t$.

[\[prop:iterate\]]{#prop:iterate label="prop:iterate"} For every $U\leq V$ and $t\geq0$, $$\label{eq:iterate}
 T^t(U)=N^t(U).$$ If $0\leq t\leq d$, then $$\label{eq:ranknullity}
 \dim T^t(U)=\dim U-\dim(U\cap K_t).$$

The image of a subspace under a composition of linear maps is the iterated image, so induction gives [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}. The kernel of the restricted map $N^t|_U$ is $U\cap K_t$. Applying rank--nullity to this restriction gives [\[eq:ranknullity\]](#eq:ranknullity){reference-type="eqref" reference="eq:ranknullity"}.

# Exact fibres and dimension transitions

The first main result refines the absorption census down to each target subspace.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Let $0\leq t\leq d$, let $W\leq I_t$ have dimension $s$, and let $0\leq r\leq d$. Then $$\label{eq:fibre}
 \#\{U\in\operatorname{Gr}(r,V):N^t(U)=W\}
 =\genfrac{[}{]}{0pt}{}{t}{r-s}_{q}q^{s(t-r+s)}.$$ If $W\nleq I_t$, the fibre is empty.

The last assertion follows from $N^t(U)\leq I_t$. Assume $W\leq I_t$ and let $K=K_t$. For any subspace in the displayed fibre, rank--nullity gives $$k:=\dim(U\cap K)=r-s.$$ If $k<0$ or $k>t$, the fibre is empty and the Gaussian coefficient on the right of [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is zero. Hence assume $0\leq k\leq t$. There are $\genfrac{[}{]}{0pt}{}{t}{k}_{q}$ choices for $R=U\cap K$. Fix one such $R$. The restriction of $N^t$ to $E=(N^t)^{-1}(W)$ gives an exact sequence $$0\longrightarrow K\longrightarrow E\xrightarrow{N^t}W\longrightarrow0.$$ Choose a linear section $\sigma\colon W\to E$ and a complement of $R$ in $K$. Every $U$ with $U\cap K=R$ and $N^tU=W$ is then uniquely of the form $$U=R\oplus\{\sigma(w)+\widetilde f(w):w\in W\},$$ where $f\colon W\to K/R$ is linear and $\widetilde f$ is its representative in the chosen complement. Conversely, each such graph has the required intersection and image. Since $\dim(K/R)=t-k$, the number of graphs is $q^{s(t-k)}$. Substituting $k=r-s$ proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

[\[cor:transition\]]{#cor:transition label="cor:transition"} For $0\leq t\leq d$ and $0\leq r,s\leq d$, $$\label{eq:transition}
 \#\{U\in\operatorname{Gr}(r,V):\dim N^t(U)=s\}
 =\genfrac{[}{]}{0pt}{}{t}{r-s}_{q}\genfrac{[}{]}{0pt}{}{d-t}{s}_{q}q^{(t-r+s)s}.$$

There are $\genfrac{[}{]}{0pt}{}{d-t}{s}_{q}$ possible $s$-subspaces $W\leq I_t$. Multiplying this number by [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} gives the result.

Summing [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} over the possible input dimensions also gives every iterated indegree.

[\[cor:indegree\]]{#cor:indegree label="cor:indegree"} If $W\leq I_t$ has dimension $s$, then $$\label{eq:tindegree}
 \#(T^t)^{-1}(W)
 =\sum_{k=0}^{t}\genfrac{[}{]}{0pt}{}{t}{k}_{q}q^{s(t-k)}.$$ In particular, $$\label{eq:indegree}
 \#T^{-1}(W)=q^s+1\quad(W\leq I_1),$$ whereas a subspace outside $I_t$ has no $t$-step predecessor.

In [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, put $k=r-s$ and sum over $0\leq k\leq t$. For $t=1$, the two terms are $q^s$ and $1$.

# Absorption, periodic points, and zeta

Define the absorption depth $$\operatorname{depth}(U)=\min\{t\geq0:T^t(U)=0\},$$ so that $\operatorname{depth}(0)=0$. Let $B_t$ denote the number of subspaces absorbed by time $t$.

[\[thm:depth\]]{#thm:depth label="thm:depth"} For every $t\geq0$, $$\label{eq:cdf}
 B_t=G_{\min(t,d)}(q).$$ Consequently the number $A_t$ of points of exact depth $t$ is $$\label{eq:layers}
 A_0=1,
 \qquad
 A_t=G_t(q)-G_{t-1}(q)\quad(1\leq t\leq d),$$ and $A_t=0$ for $t>d$. The maximum depth is exactly $d$.

By [\[prop:iterate\]](#prop:iterate){reference-type="ref" reference="prop:iterate"}, a subspace is absorbed by time $t$ precisely when it is contained in $K_t$. The kernel has dimension $\min(t,d)$, so the number of its subspaces is [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. Taking successive differences gives [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}. Finally, $A_d>0$ because $K_{d-1}$ is a proper subspace of $V$; equivalently, a line generated by a vector $v$ with $N^{d-1}v\neq0$ has depth $d$.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} Zero is the unique periodic point. Hence, for every $n\geq1$, $$\#\operatorname{Fix}(T^n)=1,$$ and the Artin--Mazur zeta function is $$\label{eq:zeta}
 \zeta_T(z)
 =\exp\!\left(\sum_{n\geq1}\frac{\#\operatorname{Fix}(T^n)}{n}z^n\right)
 =\frac{1}{1-z}.$$

Suppose $T^n(U)=U$ for some $n\geq1$. Iterating this equality gives $N^{mn}U=U$ for every $m\geq1$. Choose $m$ with $mn\geq d$. Then $N^{mn}=0$, so $U=0$. The fixed counts follow, and substituting them into the definition of the Artin--Mazur zeta function [@ArtinMazur1965] yields [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

Thus the functional graph is one rooted in-tree with a loop at zero. Its global depth profile is [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}, while [\[eq:indegree\]](#eq:indegree){reference-type="eqref" reference="eq:indegree"} records the local branching at every vertex that lies in the first image.

# Rigidity and the one-dimensional collapse

The temporal census distinguishes the family except at a genuine boundary.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Let $q,q'$ be prime powers and $d,d'\geq1$. The finite maps $T_{q,d,N}$ and $T_{q',d',N'}$, for regular nilpotent $N,N'$, are conjugate if and only if either

1.  $q=q'$ and $d=d'$, or

2.  $d=d'=1$.

In particular, for $d\geq2$ the depth census recovers $$\label{eq:recovery}
 d=\max_U\operatorname{depth}(U),
 \qquad
 q=B_2-3.$$

All regular nilpotent endomorphisms of a fixed $d$-dimensional vector space are similar, and similarity induces a conjugacy of their subspace maps. Thus the first condition is sufficient.

Conversely, a dynamical conjugacy sends the unique fixed point to the unique fixed point and preserves every absorption layer. By [\[thm:depth\]](#thm:depth){reference-type="ref" reference="thm:depth"}, the largest nonempty layer recovers $d$. If $d\geq2$, then $$B_2=G_2(q)=1+(q+1)+1=q+3,$$ so the same census recovers $q$. If $d=1$, the lattice consists only of $0$ and $V$, with both vertices mapped to $0$, independently of $q$. Hence all and only the one-dimensional systems form the exceptional conjugacy class.

The exception is necessary rather than technical: neither phase size nor any temporal statistic can distinguish the ground fields in dimension one.

# A second proof route

We give a hyperplane recurrence for [\[cor:transition\]](#cor:transition){reference-type="ref" reference="cor:transition"}. Besides providing an independent proof, it is the algebraic pattern used by the RREF control. Fix a $t$-subspace $K\leq\mathbb F_q^d$ and define $$C_{d,t}(r,k)
 =\#\{U\in\operatorname{Gr}(r,\mathbb F_q^d):\dim(U\cap K)=k\}.$$

[\[prop:recurrence\]]{#prop:recurrence label="prop:recurrence"} For $d>t$, $$\label{eq:recurrence}
 C_{d,t}(r,k)
 =C_{d-1,t}(r,k)+q^{d-r}C_{d-1,t}(r-1,k),$$ with boundary $C_{t,t}(r,k)=\genfrac{[}{]}{0pt}{}{t}{r}_{q}$ when $k=r$ and zero otherwise. Its solution is $$\label{eq:intersection}
 C_{d,t}(r,k)
 =\genfrac{[}{]}{0pt}{}{t}{k}_{q}\genfrac{[}{]}{0pt}{}{d-t}{r-k}_{q}q^{(t-k)(r-k)}.$$

Choose a hyperplane $H$ that contains $K$. The $r$-subspaces contained in $H$ contribute the first term of [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. If $U\nleq H$, then $U_0=U\cap H$ has dimension $r-1$ and satisfies $U_0\cap K=U\cap K$. For a fixed $U_0$, the possible $U$ correspond to lines in $\mathbb F_q^d/U_0$ that do not lie in $H/U_0$. Their number is $$\genfrac{[}{]}{0pt}{}{d-r+1}{1}_{q}-\genfrac{[}{]}{0pt}{}{d-r}{1}_{q}=q^{d-r},$$ which proves the recurrence and its boundary.

It remains to check the solution. The Gaussian Pascal identity $$\genfrac{[}{]}{0pt}{}{n}{j}_{q}
 =\genfrac{[}{]}{0pt}{}{n-1}{j}_{q}+q^{n-j}\genfrac{[}{]}{0pt}{}{n-1}{j-1}_{q}$$ shows by substitution that [\[eq:intersection\]](#eq:intersection){reference-type="eqref" reference="eq:intersection"} satisfies [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}; it also matches the boundary at $d=t$. Induction on $d-t$ therefore proves [\[eq:intersection\]](#eq:intersection){reference-type="eqref" reference="eq:intersection"}.

For $K=K_t$, [\[eq:ranknullity\]](#eq:ranknullity){reference-type="eqref" reference="eq:ranknullity"} gives $k=r-s$. Substituting this value in [\[eq:intersection\]](#eq:intersection){reference-type="eqref" reference="eq:intersection"} reproduces [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"}, without using the quotient-fibre parametrization in the first proof.

# Exact control and limitations

The control script constructs each finite field from a polynomial basis, enumerates every subspace from its unique reduced-row-echelon basis, materializes its vectors, and applies the Jordan shift literally. It then checks every fibre indexed by $(t,W,r)$, every rank transition indexed by $(t,r,s)$, all depth layers, all tested periods, the one-step indegree, and the rigidity signature. The tested lanes are $$\begin{array}{c|c}
 q&\text{dimensions}\\ \hline
 2&1\text{--}6\\
 3&1\text{--}5\\
 5&1\text{--}4\\
 4&1\text{--}4\\
 8,9,16&1\text{--}3.
 \end{array}$$ The polynomial-basis extension fields are $\mathbb F_4$, $\mathbb F_8$, $\mathbb F_9$, and $\mathbb F_{16}$. A fresh run registers $515{,}379$ exact assertions, and the stored output is reproduced byte for byte.

The paper treats a single regular nilpotent block. For a general nilpotent operator, [\[thm:fibre\]](#thm:fibre){reference-type="ref" reference="thm:fibre"} still applies to each fixed $t$ after replacing $t$ by $\dim\ker N^t$ and $d-t$ by $\dim\operatorname{im}N^t$, but the depth census then encodes the whole Jordan partition rather than the single staircase. That extension is not claimed here. Nor do the results concern the lattice of $N$-invariant subspaces, whose enumeration belongs to the owner literature cited above. These boundaries, together with the unresolved specialist owner gate, keep external status on **HOLD**.
