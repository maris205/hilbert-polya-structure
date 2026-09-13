---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--178-state-selected-finite-differences"
canonical_tex: "symbolic_dynamics/papers/178-state-selected-finite-differences/main.tex"
canonical_pdf: "symbolic_dynamics/papers/178-state-selected-finite-differences/main.pdf"
source_sha256: "d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# State-Selected Finite Differences: Complete Fibres and Jordan Blocks

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/178-state-selected-finite-differences>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/178-state-selected-finite-differences/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/178-state-selected-finite-differences/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/178-state-selected-finite-differences/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/178-state-selected-finite-differences/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a prime $p$, consider all functions $f:\mathbb F_p\to\mathbb F_p$ and update $$f(x)\longmapsto f(x+f(0))-f(x).$$ The current value at zero selects a new translation direction at every epoch, so the map is nonlinear despite being assembled from linear differences. We prove a complete finite atlas. The $t$th image is the $t$th cyclic-difference layer and has size $p^{p-t}$ for $0\le t\le p$; each nonzero target in that layer has exactly $(p-1)^t$ time-$t$ preimages, while the zero fibre is obtained explicitly by mass balance. The functional graph is one rooted component of sharp height $p$, with closed depth shells. Its complex transition operator has one $J_1(1)$ block, $(p-1)^2p^{p-s-1}$ blocks $J_s(0)$ for $s<p$, and $p-1$ blocks $J_p(0)$. Fixed finite differences, augmentation-ideal nilpotence, and generic rank-to-Jordan conversion are assigned no contribution credit. The literal feedback conjunction remains owner-thin and externally held.
author:
- Anonymous
bibliography:
- references.bib
title: |
  State-Selected Finite Differences:\
  Complete Fibres and Jordan Blocks
```

## Markdown 正文

# The feedback map and theorem

Fix a prime $p$ and put $$\mathcal V=\mathbb F_p^{\mathbb F_p}=\{f:\mathbb F_p\to\mathbb F_p\}.$$ For $a\in\mathbb F_p$, let $(\tau_a f)(x)=f(x+a)$ and $D_a=\tau_a-I$. Our literal self-map is $$\label{eq:T}
                  T(f)=D_{f(0)}f.$$ Thus $T(f)=0$ immediately when $f(0)=0$; otherwise the direction used at the next epoch depends on the new state. Write $\tau=\tau_1$, $N=\tau-I$, and $$J^t=N^t\mathcal V\qquad(0\le t\le p).$$

Difference operators and their augmentation-ideal formulation are standard [@AichingerMoosbauer2021]. The nilpotent/bijective decomposition and functional graphs of fixed linear maps over finite fields are likewise classical [@HernandezToledo2005]. We assign the filtration $J^\bullet$, fixed-difference nilpotence, affine kernel counts, and rank-to-Jordan conversion no contribution credit. The object isolated here is the state-selected direction in [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}, especially its anchored inverse system.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every prime $p$, the map [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} has the following properties.

(i) For $0\le t\le p$, $$\label{eq:image}
           \operatorname{im}T^t=J^t,\qquad \dim_{\mathbb F_p}J^t=p-t,\qquad
           |\operatorname{im}T^t|=p^{p-t}.$$ In particular $T^p=0$, and this exponent is sharp.

(ii) If $1\le t\le p$ and $g\in\mathcal V$, then $$\label{eq:fibres}
      |(T^t)^{-1}(g)|=
      \begin{cases}
      p^p-\bigl(p^{p-t}-1\bigr)(p-1)^t,&g=0,\\
      (p-1)^t,&0\ne g\in J^t,\\
      0,&g\notin J^t.
      \end{cases}$$ At $t=0$ every fibre is a singleton. For $t\ge p$, the only nonempty fibre is the zero fibre, of size $p^p$.

(iii) Zero is the unique recurrent state, and the functional graph is one rooted component with its root loop retained. If $\delta(f)$ is the least $t$ with $T^t(f)=0$, then the number $A_d$ of states of exact depth $d$ is $$\label{eq:depth}
       A_0=1,\qquad
       A_d=(p-1)^{d-1}\bigl(p^{p-d}+p-2\bigr)
       \quad(1\le d\le p).$$ Every nonzero target in $J^1$ has $p-1$ immediate predecessors, every target outside $J^1$ has none, and zero has $$\label{eq:rootdegree}
                   p^p-\bigl(p^{p-1}-1\bigr)(p-1)$$ immediate predecessors, including its loop.

(iv) On the complex vector space with basis $\{e_f:f\in\mathcal V\}$, define the deterministic transition operator $P e_f=e_{T(f)}$. Then $$\label{eq:charpoly}
                        \chi_P(\lambda)=(\lambda-1)\lambda^{p^p-1}.$$ Besides one $J_1(1)$ block, the number $m_s$ of zero-Jordan blocks of size $s$ is $$\label{eq:jordan}
      m_s=(p-1)^2p^{p-s-1}\quad(1\le s<p),
      \qquad m_p=p-1.$$

# The difference flag and anchored lifting

For $0\le j<p$, regard $$e_j(x)=\binom{x}{j}=\frac{x(x-1)\cdots(x-j+1)}{j!}$$ as a function on $\mathbb F_p$, with $e_0=1$. Their evaluation matrix on $0,1,\ldots,p-1$ is lower triangular with diagonal one, so $e_0,\ldots,e_{p-1}$ form a basis of $\mathcal V$. Pascal's identity gives $$\label{eq:pascal}
             Ne_0=0,\qquad Ne_j=e_{j-1}\quad(1\le j<p).$$ Consequently $$\label{eq:flag}
        J^i=\operatorname{span}_{\mathbb F_p}\{e_0,\ldots,e_{p-1-i}\},
        \qquad \dim J^i=p-i.$$ This is the familiar one-block cyclic-difference flag.

[\[lem:anchor\]]{#lem:anchor label="lem:anchor"} Let $a\in\mathbb F_p^\times$ and $0\le i<p$. The restriction $$D_a:J^i\longrightarrow J^{i+1}$$ is onto and has kernel $\mathbb F_p e_0$. For each $h\in J^{i+1}$ and each $b\in\mathbb F_p$, exactly one solution $f\in J^i$ of $D_af=h$ satisfies $f(0)=b$.

Choose the integer representative $r\in\{1,\ldots,p-1\}$ of $a$. Since $\tau_a=\tau^r=(I+N)^r$, $$D_a=N U_a(N),\qquad
 U_a(z)=\sum_{k=1}^{r}\binom rk z^{k-1},\qquad U_a(0)=a.$$ The polynomial $U_a(N)$ is invertible because $N$ is nilpotent and its constant coefficient is nonzero. It preserves every $J^i$, commutes with $N$, and acts on $\ker N=\mathbb F_p e_0$ as multiplication by $a$. Equations [\[eq:pascal\]](#eq:pascal){reference-type="eqref" reference="eq:pascal"}--[\[eq:flag\]](#eq:flag){reference-type="eqref" reference="eq:flag"} now show that $D_a$ maps $J^i$ onto $J^{i+1}$ with kernel $\mathbb F_p e_0$. A nonempty solution set is therefore an affine line $f_0+\mathbb F_p e_0$. Since $e_0(0)=1$, evaluation at zero is a bijection from this line to $\mathbb F_p$, proving the anchored assertion.

Suppose a trajectory has not yet reached zero and record its direction word $$(a_0,\ldots,a_{t-1})
          =\bigl(f_0(0),\ldots,f_{t-1}(0)\bigr)
          \in(\mathbb F_p^\times)^t.$$ Each nonzero difference raises the flag index by one, while a zero direction sends the state to zero. Hence $T^t(\mathcal V)\subseteq J^t$ and $T^p=0$.

Conversely, fix $0\ne g\in J^t$ and a word $(a_0,\ldots,a_{t-1})\in(\mathbb F_p^\times)^t$. Set $f_t=g$ and solve backward, for $i=t-1,\ldots,0$, $$\label{eq:backward}
             D_{a_i}f_i=f_{i+1},\qquad f_i(0)=a_i,
             \qquad f_i\in J^i.$$ Lemma [\[lem:anchor\]](#lem:anchor){reference-type="ref" reference="lem:anchor"} gives exactly one $f_i$ at every step. Distinct words give distinct sources because a forward orbit recovers each $a_i$. Thus every nonzero $g\in J^t$ has exactly $(p-1)^t$ sources, proving the second line of [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} and the reverse inclusion in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. A target outside $J^t$ is unreachable. Subtracting the mass of the $p^{p-t}-1$ nonzero targets from the $p^p$ sources yields the zero line of [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"}.

For sharpness, let $f_\star=\sum_{j=0}^{p-1}e_j$. Repeated use of [\[eq:pascal\]](#eq:pascal){reference-type="eqref" reference="eq:pascal"} gives $$N^k f_\star=\sum_{j=0}^{p-1-k}e_j,\qquad
        (N^k f_\star)(0)=1\quad(0\le k<p).$$ The selected direction therefore remains one until the last step: $T^{p-1}f_\star=e_0\ne0$ and $T^pf_\star=0$.

# The rooted graph and transition operator

The relation $T^p=0$ makes zero the sole recurrent state. Formula [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} at $t=1$ gives every immediate indegree and [\[eq:rootdegree\]](#eq:rootdegree){reference-type="eqref" reference="eq:rootdegree"}. Thus the graph is a single rooted component; the stated indegrees describe all of its branching.

Let $Z_t=|(T^t)^{-1}(0)|$. Exact depth $d$ means membership in the $d$th zero fibre but not the $(d-1)$st, so $A_d=Z_d-Z_{d-1}$. Using [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"}, with $Z_0=1$ and $Z_p=p^p$, gives $$Z_d-Z_{d-1}
 =(p-1)^{d-1}\bigl(p^{p-d}+p-2\bigr)$$ for every $1\le d\le p$, including the two endpoints.

Put $E=P^p$. Since $T^p(f)=0$ for every state, $Ee_f=e_0$; hence $E$ is a rank-one idempotent commuting with $P$. This gives the invariant decomposition $$\mathbb C^{\mathcal V}=\operatorname{im}E\oplus\ker E.$$ The restriction of $P$ to $\operatorname{im}E=\mathbb C e_0$ is the identity, whereas $Q=P|_{\ker E}$ is nilpotent of exponent at most $p$. This proves [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}.

For $0\le t\le p$, the image of $P^t$ is spanned by $\{e_g:g\in J^t\}$ and therefore has dimension $p^{p-t}$. Moreover $$P^t(\ker E)=\operatorname{im}P^t\cap\ker E.$$ Indeed, only the reverse inclusion needs comment: if $y=P^tx$ and $Ey=0$, then $P^t(x-Ex)=y$. Since $E$ has rank one on $\operatorname{im}P^t$, it follows that $$\label{eq:ranks}
                \operatorname{rank}Q^t=p^{p-t}-1=:r_t.$$ For a nilpotent operator, the number of blocks of exact size $s<p$ is the second rank difference $$m_s=r_{s-1}-2r_s+r_{s+1},$$ while $m_p=r_{p-1}$. Substitution into [\[eq:ranks\]](#eq:ranks){reference-type="eqref" reference="eq:ranks"} gives [\[eq:jordan\]](#eq:jordan){reference-type="eqref" reference="eq:jordan"}. This rank-to-block conversion is generic linear algebra and is not part of the claimed mechanism.

[\[rem:p2\]]{#rem:p2 label="rem:p2"} At $p=2$, the image sizes are $4,2,1$, the depth layers are $1,2,1$, and the transition operator has $J_1(1)\oplus J_1(0)\oplus J_2(0)$. Thus the sharp clock and the top zero block already occur in the first admissible prime.

# Exact controls, ownership, and limits

The paper-local verifier represents functions directly as value tuples and starts from the literal update [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}. It exhausts every state, every target, and every time through $p=5$, including the direction-word lift behind [\[eq:backward\]](#eq:backward){reference-type="eqref" reference="eq:backward"}. A separate modular-matrix certificate checks the binomial flag, all ranks, and anchor injectivity for $p=2,3,5,7,11,13,17,19$. The settled run makes $44{,}689$ exact assertions over $3{,}156$ literal arrows. These computations pressure-test arithmetic and boundary cases; they do not prove the theorem.

The ownership subtraction is intentionally severe. The operators $D_a=\tau_a-I$, augmentation powers, and their nilpotency belong to the finite-difference background represented by [@AichingerMoosbauer2021]. Fixed linear finite dynamical systems and their nilpotent flags are also established territory [@HernandezToledo2005]. Internally, the A05 scout already discarded iteration of one fixed cyclic difference, and P164 already used a nonlinear first step followed by a fixed cyclic-difference tail. Their image flags, kernel cosets, clocks, and Jordan conversions all receive zero separation credit here.

What remains is narrower: [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} selects its direction at every epoch, the nonzero direction word is observable along the orbit, and the same observed values anchor each reverse integration uniquely. That feedback mechanism yields the simultaneous nonuniform zero/nonzero fibre atlas [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} and the $p-1$ top Jordan blocks. A bounded exact-literal search found no direct owner of this conjunction, but a search nonhit does not establish novelty, priority, or freedom to operate. The note therefore remains [owner\_thin]{.smallcaps} and [hold\_external]{.smallcaps}.
