---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--154-dihedral-normalizer-dynamics"
canonical_tex: "symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/main.pdf"
source_sha256: "5723fe0939afd3a390d03c48e8c2324841cc11063968e1b51827d8bbe9c048fa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Iterated subgroup-normalizer dynamics in finite dihedral groups

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/154-dihedral-normalizer-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/154-dihedral-normalizer-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle$, and iterate $H\mapsto N_{D_{2n}}(H)$ on the set of all subgroups. The subgroup coordinates and the one-step odd/even normalizer rule are classical and are used here with full credit to their sources. Writing $n=2^a m$ with $m$ odd, we show that the remaining dynamics consists of $\sigma(m)$ full binary inverse trees of height $a$, together with all $\tau(n)$ rotation subgroups feeding one distinguished fixed root. We derive every positive-time image and every target fibre. We then prove that the unlabelled functional graph is classified exactly by $(a,\sigma(m),\tau(n))$. In particular, the parameters $33$ and $35$ give conjugate graphs, and so do all common power-of-two lifts. Symbolic proofs are paired with deterministic literal-normalizer replay.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Iterated subgroup-normalizer dynamics\
  in finite dihedral groups
```

## Markdown 正文

# Scope, owned inputs, and theorem

The subgroup structure of finite dihedral groups is classical [@Cavior1975; @ConradDihedralII]. The normalizer of a reflection-containing dihedral subgroup is likewise governed by a direct odd/even rule; it appears in @Frenkel2003 and in complete subgroup cases in @ShelashEtAl2023. Those results settle the carrier and the one-step map. They receive no contribution credit below. Our subject is what repeated application does to *every* subgroup, including its full inverse forest, all-time fibres, and the information about $n$ retained by the resulting unlabelled graph.

Put $$G_n=D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,\qquad n\geq3.$$ For $d\mid n$ and $0\leq j<d$, write $$R_d=\langle r^d\rangle,\qquad
H_{d,j}=\langle r^d,r^j s\rangle.$$ The complete subgroup carrier is $$\operatorname{Sub}(G_n)=\{R_d:d\mid n\}\ \sqcup\
\{H_{d,j}:d\mid n,\ 0\leq j<d\},                       \tag{1}\label{eq:carrier}$$ of size $\tau(n)+\sigma(n)$. Let $\mathcal N_n(H)=N_{G_n}(H)$, and write $n=2^a m$ with $m$ odd.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq3$, the map $\mathcal N_n$ on $\operatorname{Sub}(G_n)$ has the following properties.

1.  The owned one-step rule and its iterates are $$\mathcal N_n(R_d)=H_{1,0},\qquad
    \mathcal N_n(H_{d,j})
    =H_{d/\gcd(d,2),\,j\bmod d/\gcd(d,2)},                 \tag{2}\label{eq:onestep}$$ $$\mathcal N_n^t(H_{2^k e,j})
    =H_{2^{\max(k-t,0)}e,\,
         j\bmod 2^{\max(k-t,0)}e},                         \tag{3}\label{eq:iterate}$$ for $t\geq0$, $0\leq k\leq a$, $e\mid m$, and $0\leq j<2^ke$.

2.  The dihedral states form $\sigma(m)$ full binary inverse trees of height $a$, rooted at the fixed states $H_{e,j}$ with $e\mid m$, $0\leq j<e$. Every $R_d$ is an extra source of depth one entering only $H_{1,0}=G_n$. Hence $$\operatorname{depth}(R_d)=1,\qquad \operatorname{depth}(H_{d,j})=v_2(d),$$ and the depth polynomial is $$\mathcal D_n(z)=\sigma(m)+\tau(n)z+
    \sigma(m)\sum_{k=1}^{a}2^kz^k.                         \tag{4}\label{eq:depth}$$ All cycles are fixed points, and $\#\operatorname{Fix}(\mathcal N_n^t)=\sigma(m)$ for $t\geq1$.

3.  For every $t\geq1$, $$|\operatorname{im}\mathcal N_n^t|
    =\sigma(m)\bigl(2^{\max(a-t,0)+1}-1\bigr).             \tag{5}\label{eq:image}$$ No rotation target has a positive-time preimage. For every $t\geq1$ and every positive-level carrier target $H_{2^ke,j}$ with $1\leq k\leq a$, $e\mid m$, and $0\leq j<2^ke$, $$\#(\mathcal N_n^t)^{-1}(H_{2^ke,j})
    =
    \begin{cases}
    2^t,&k+t\leq a,\\
    0,&k+t>a,
    \end{cases}                                            \tag{6}\label{eq:fibrelevel}$$ while a fixed root has fibre $$\#(\mathcal N_n^t)^{-1}(H_{e,j})
    =2^{\min(t,a)+1}-1+\tau(n)\,\mathbf1_{(e,j)=(1,0)}.    \tag{7}\label{eq:fibreroot}$$

4.  Two such unlabelled directed functional graphs are isomorphic exactly when $$\bigl(v_2(n),\sigma(\operatorname{odd}(n)),\tau(n)\bigr)
    =\bigl(v_2(q),\sigma(\operatorname{odd}(q)),\tau(q)\bigr). \tag{8}\label{eq:signature}$$ In particular, the graphs for $n=33$ and $n=35$ are conjugate, although $|G_{33}|\neq|G_{35}|$; the same holds for $(2^b33,2^b35)$ for every $b\geq0$.

#### Proof dependency graph.

The theorem is organized so the owner-covered bridge is visibly separated from the dynamical deductions: $$\begin{gathered}
\boxed{\text{subgroup coordinates + one-step parity rule}}\\[-1mm]
\Downarrow\\[-1mm]
\boxed{\text{\(t\)-fold halving \eqref{eq:iterate}}}\\[-1mm]
\Downarrow\\[-1mm]
\text{binary forest}\Longrightarrow
\{\mathcal D_n,\operatorname{im}\mathcal N_n^t,\text{ target fibres}\},\\
\text{forest observables}\Longrightarrow\{a,\sigma(m),\tau(n)\}
\Longrightarrow\text{iff signature and collisions}.
\end{gathered}                                         \tag{9}\label{eq:dependency}$$ Thus the signature theorem is not obtained merely from equal depth polynomials; it uses the full component structure and total vertex count.

# From the one-step rule to the entire forest

For completeness, we recall why [\[eq:carrier\]](#eq:carrier){reference-type="eqref" reference="eq:carrier"} and [\[eq:onestep\]](#eq:onestep){reference-type="eqref" reference="eq:onestep"} hold. A subgroup contained in $\langle r\rangle$ is a unique $R_d$. Otherwise its rotation part is $R_d$, and any reflection $r^js$ in it generates the unique nonrotation coset, giving $H_{d,j}$ with $j\bmod d$. This also proves the count $\tau(n)+\sigma(n)$.

Every $R_d$ is normal in $G_n$. Conjugation by $r^u$ sends $r^js$ to $r^{j+2u}s$, so it normalizes $H_{d,j}$ exactly when $d\mid2u$. A general normalizing reflection $r^us$ satisfies the corresponding condition $d\mid2(u-j)$. Therefore all normalizers together form $$\left\langle r^{d/\gcd(d,2)},r^js\right\rangle,$$ which is precisely [\[eq:onestep\]](#eq:onestep){reference-type="eqref" reference="eq:onestep"}. This derivation makes the coordinate convention explicit, but the result itself is part of the credited input.

Write $d=2^ke$ with $e$ odd. Iterating [\[eq:onestep\]](#eq:onestep){reference-type="eqref" reference="eq:onestep"} removes one factor of two per step until none remains, and reduces $j$ modulo the new step. This proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}. For a fixed pair $(e,j_0)$, $e\mid m$ and $0\leq j_0<e$, the states at level $k$ are $$H_{2^ke,j_0+\ell e},\qquad0\leq\ell<2^k.              \tag{10}\label{eq:lifts}$$ Each non-leaf state has exactly two lifts at the next level. Summing the number of roots over odd divisors gives $\sum_{e\mid m}e=\sigma(m)$, so these are $\sigma(m)$ full binary trees of height $a$. Separately, all $\tau(n)$ rotations map directly to $H_{1,0}$. The claimed depths and [\[eq:depth\]](#eq:depth){reference-type="eqref" reference="eq:depth"} follow. Every orbit reaches a root, hence every recurrent state is fixed.

# All-time images and target fibres

At time $t\geq1$, a level-$\ell$ dihedral state can be reached exactly when $0\leq\ell\leq\max(a-t,0)$. Each of the $\sigma(m)$ trees then contributes $$1+2+\cdots+2^{\max(a-t,0)}
=2^{\max(a-t,0)+1}-1$$ image vertices, proving [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. Rotations have no preimages because every normalizer contains the subgroup it normalizes, whereas a proper rotation target omits all reflections; this is also immediate from [\[eq:onestep\]](#eq:onestep){reference-type="eqref" reference="eq:onestep"}.

Let $H_{2^ke,j}$ be a carrier target with $1\leq k\leq a$, $e\mid m$, and $0\leq j<2^ke$. A time-$t$ source, for $t\geq1$, must occur at level $k+t$. When that level exists, the residue $j$ has exactly $2^t$ lifts modulo $2^{k+t}e$; otherwise there is no source. This proves [\[eq:fibrelevel\]](#eq:fibrelevel){reference-type="eqref" reference="eq:fibrelevel"}. For a root, all levels $0,\ldots,\min(t,a)$ have already arrived, giving the geometric sum $2^{\min(t,a)+1}-1$. In addition, every rotation has arrived at every positive time, but only at the distinguished root. This gives [\[eq:fibreroot\]](#eq:fibreroot){reference-type="eqref" reference="eq:fibreroot"}.

These formulas also close source mass without appeal to graph intuition. Indeed, summing all positive-level fibres, all root-tree fibres, and the $\tau(n)$ distinguished additions gives $$\sigma(n)+\tau(n)=|\operatorname{Sub}(G_n)|.$$ Targets absent from [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} have fibre zero. Thus [\[eq:fibrelevel\]](#eq:fibrelevel){reference-type="eqref" reference="eq:fibrelevel"}--[\[eq:fibreroot\]](#eq:fibreroot){reference-type="eqref" reference="eq:fibreroot"} are an every-target atlas rather than only a distribution of indegrees.

As a concrete ledger, take $n=12=2^2\cdot3$. Here $a=2$, $\sigma(m)=4$, $\tau(n)=6$, and

$$|\operatorname{Sub}(G_{12})|=\sigma(12)+\tau(12)=34,\qquad
\mathcal D_{12}(z)=4+14z+16z^2.                       \tag{11}\label{eq:n12depth}$$ At time one the image has $4(2^2-1)=12$ states. Each of the eight level-one targets has two sources; each ordinary root has three sources; and the distinguished root has $3+6=9$. Thus

$$8\cdot2+3\cdot3+9=34.$$ At time two only the four roots remain. The three ordinary roots have seven sources each and the distinguished root has $7+6=13$, giving $3\cdot7+13=34$. This box displays both mechanisms in [\[eq:fibreroot\]](#eq:fibreroot){reference-type="eqref" reference="eq:fibreroot"}: binary-tree mass grows geometrically, while the rotation contribution is already saturated at time one.

Because every cycle is a fixed root, the finite-map zeta function follows as $$\zeta_{\mathcal N_n}(z)
=\exp\left(\sum_{t\geq1}\frac{\sigma(m)}{t}z^t\right)
=(1-z)^{-\sigma(m)}.                                   \tag{12}\label{eq:zeta}$$ This is recorded for completeness; once the fixed-root census is known, it is generic cycle bookkeeping and receives no standalone credit.

# Exact inverse signature

Let $$S(n)=\bigl(a,\sigma(m),\tau(n)\bigr),\qquad n=2^am,\quad m\text{ odd}.$$ If $S(n)=S(q)$, match the distinguished roots, match all other roots arbitrarily, preserve the binary positions in [\[eq:lifts\]](#eq:lifts){reference-type="eqref" reference="eq:lifts"}, and match the $\tau(n)$ extra rotation leaves. This constructs a bijection commuting with the two maps, so equal signatures are sufficient.

Conversely, the unlabelled graph recovers $\sigma(m)$ as its number of fixed vertices. Let $L$ be its maximum tail. If $L\geq2$, then $a=L$. The only ambiguity is $L=1$, where $a\in\{0,1\}$. Because $n\geq3$, in either case the relevant odd part exceeds one and there is more than one fixed root. If $a=0$, only the distinguished root has nonfixed predecessors. If $a=1$, every root has two level-one dihedral predecessors. Hence the graph distinguishes the two cases and recovers $a$.

Now the complete population of dihedral vertices is $$\sigma(m)(1+2+\cdots+2^a)
=\sigma(m)(2^{a+1}-1).$$ The remaining vertices are exactly the rotations, so the graph recovers $$\tau(n)=|V|-\sigma(m)(2^{a+1}-1).                     \tag{13}\label{eq:taurecovery}$$ This total-vertex formula is essential: a shortcut comparing the distinguished root with other roots would not cover the one-root case $m=1$. Equation [\[eq:taurecovery\]](#eq:taurecovery){reference-type="eqref" reference="eq:taurecovery"} covers it without exception and completes necessity in [\[eq:signature\]](#eq:signature){reference-type="eqref" reference="eq:signature"}.

#### The $33/35$ collision.

Both parameters are odd and $$\sigma(33)=48=\sigma(35),\qquad \tau(33)=4=\tau(35).$$ All 48 dihedral vertices are fixed. Match $H_{1,0}$ with $H_{1,0}$, match the remaining $(d,j)$ pairs lexicographically, and match the four rotation leaves by $$R_1\mapsto R_1,\qquad R_3\mapsto R_5,\qquad
R_{11}\mapsto R_7,\qquad R_{33}\mapsto R_{35}.         \tag{14}\label{eq:collision}$$ Every rotation maps to the distinguished root, so this 52-state bijection commutes with the updates. Multiplication by $2^b$ preserves $a=b$, the odd-part divisor sum $48$, and $\tau(2^b33)=4(b+1)=\tau(2^b35)$; [\[eq:signature\]](#eq:signature){reference-type="eqref" reference="eq:signature"} gives every lifted collision.

#### Sharpness and boundary examples.

The third signature coordinate cannot be dropped. For example, $$v_2(15)=v_2(23)=0,\qquad \sigma(15)=\sigma(23)=24,$$ but $\tau(15)=4$ and $\tau(23)=2$; the graphs have 28 and 26 vertices. At the other extreme, [\[eq:collision\]](#eq:collision){reference-type="eqref" reference="eq:collision"} shows that even the complete graph does not identify the ambient group order. We use the literal subgroup set, not conjugacy classes of subgroups: quotienting by conjugacy merges residue positions and changes the binary fibres. Finally, the restriction $n\geq3$ keeps the standard nondegenerate dihedral convention; no statement here uses $n=1,2$ to resolve the $a=0/1$ case.

# Owner subtraction, collision firewall, and exact audit

L0.20L0.34L0.37 Source or neighbour & Material receiving no separation credit & Literal separation retained here\
@Cavior1975 [@ConradDihedralII] & Complete subgroup coordinates and counts & None until the coordinates are iterated as one global map\
@Frenkel2003 [@ShelashEtAl2023] & Odd/even one-step normalizer and halving & Full forest, all-time target fibres, iff signature, and order collisions\
P91 / P135 & Finite-group or centralizer vocabulary & No relation shift, spectrum, wreath product, or partition orbit; the carrier here is every subgroup and the arrow is its ambient normalizer\
P142 reserve & Divisors and two-adic halving & Literal subgroup normalizers and an unlabelled-graph inverse theorem, not a divisor-only gcd map\
P153 & Finite noninvertible branches & Binary forests into fixed roots, not factorial arms into a translating field cycle\

Related two-adic normalizer-length calculations, such as the Wielandt subgroup setting of @ShelashAshrafi2020, are also treated as structural adjacency, not as support for a contribution claim. Formula searches used dihedral-subgroup coordinates, normalizer towers, hypernormalizers, parity halving, functional graphs, and the $33/35$ arithmetic signature. The bounded search found the direct one-step owners above, but no source stating the entire iterated graph--fibre--signature conjunction. That bounded result is not an ownership certificate.

#### Deterministic replay.

The accompanying `verify.py` uses no randomness or external package. For 44 values of $n$, it materializes every displayed subgroup as an element set, computes every normalizer by conjugating every subgroup element with every ambient group element, and only then compares with [\[eq:onestep\]](#eq:onestep){reference-type="eqref" reference="eq:onestep"}. It next checks depths, fixed roots, images, and every target fibre through three steps beyond stabilization. Four equal-signature pairs, beginning with $33/35$, receive explicit commuting bijections. The frozen `CANONICAL.txt` ends with

    PROFILE_SHA256 6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782
    TOTAL boxes=44 iso_pairs=4 assertions=29590
    VERDICT PASS_EXACT_REPLAY

An independent pressure scan recorded no signature mismatch for $3\leq n\leq500$, but bounded enumeration is only a regression and falsification control. Subgroup completeness and both directions of [\[eq:signature\]](#eq:signature){reference-type="eqref" reference="eq:signature"} are supplied by the proofs above.

#### Reproducibility and release state.

The repository includes the exact script, canonical transcript, claim--evidence matrix, source-verification ledger, controls, and deterministic build instructions. The manuscript is anonymous and uses no human-subject data or randomized inference. External circulation remains `HOLD_EXTERNAL`.
