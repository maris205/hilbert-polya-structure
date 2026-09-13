---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lozi-nonsmooth-route-a"
canonical_tex: "henon_dynamics/henon_lozi_nonsmooth_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lozi_nonsmooth_route_a/paper/main.pdf"
source_sha256: "f742d36ad6ef84eba7cf96867626f35e82e366990f6549d42a767d902cc4483d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Sign-Itinerary Pruning in a Rational Lozi Pilot

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lozi_nonsmooth_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lozi_nonsmooth_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lozi_nonsmooth_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lozi_nonsmooth_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a finite exact pilot for a nonsmooth Lozi map. Every binary branch word through length eight is converted to an affine return, solved over the rationals, and checked against strict sign domains. The resulting ledger has 37 primitive cyclic classes. This is a certified finite orbit atlas, not a claim of a global Markov partition or analytic transfer operator.
author:
- 'Anonymous Route-A report'
title: 'Exact Sign-Itinerary Pruning in a Rational Lozi Pilot'
```

## Markdown 正文

# Frozen nonsmooth map

We freeze $$L(x,y)=\left(1-2|x|+\frac12y,x\right)$$ and assign symbol $0$ to $x<0$ and symbol $1$ to $x>0$. The switching line $x=0$ is excluded before enumeration. On the two open half-planes the map is affine with matrices $$B_0=\begin{pmatrix}2&1/2\\1&0\end{pmatrix},\qquad
 B_1=\begin{pmatrix}-2&1/2\\1&0\end{pmatrix},
 \qquad d=\binom10.$$ Both determinants are $-1/2$, but their chronology is retained in every return matrix.

# Exact return test

For a word $w=s_0\cdots s_{n-1}$, composition gives $L_w(q)=M_wq+t_w$. Exact Gaussian elimination produces the unique candidate $$q_w=(I-M_w)^{-1}t_w$$ whenever the return is nonsingular. We then iterate $q_w$ and require the $k$th coordinate to lie strictly in the half-plane declared by $s_k$. Algebraic solvability alone is therefore not counted as admissibility.

The rooted strict counts for periods one through eight are $$(2,4,2,8,22,40,58,128).$$ After restricting to primitive words and quotienting only by cyclic rotation, the primitive counts are $$(2,1,0,1,4,6,8,15),$$ for a total of 37 certified classes. No return is singular and no candidate hits the switching line in this prefix; all rejected words fail a sign test.

   $n$    binary   strict   sign fail   primitive   primitive pruned
  ----- -------- -------- ----------- ----------- ------------------
    1          2        2           0           2                  0
    2          4        4           0           1                  0
    3          8        2           6           0                  2
    4         16        8           8           1                  2
    5         32       22          10           4                  2
    6         64       40          24           6                  3
    7        128       58          70           8                 10
    8        256      128         128          15                 15

The table is an exact strict-sign classification of all 510 words in the frozen prefix. Its rooted and primitive columns obey $t_n=\sum_{d\mid n}d p_d$ for every $n\leq8$.

The return solver uses rational matrix arithmetic. For each nonsingular candidate, direct branch iteration checks every strict inequality and closure. Primitive words are identified before taking the lexicographically minimal cyclic rotation. Substituting the eight displayed values verifies the finite necklace identity.

# A finite cycle-atlas operator

Freeze the diagnostic phase weights $\rho_0=1/2$ and $\rho_1=2/3$. For a certified primitive word $c=s_0\cdots s_{n-1}$, let $C_c$ be the weighted cyclic block $$C_c e_k=\rho_{s_k}e_{k+1\bmod n},\qquad
 \rho(c)=\prod_{k=0}^{n-1}\rho_{s_k}.$$ Taking one block for each of the 37 canonical classes gives $A_8=\bigoplus_c C_c$ with 240 states and 240 nonzero edges. Direct block algebra yields the exact finite identities $$\det(I-zA_8)=\prod_c\bigl(1-\rho(c)z^{|c|}\bigr),\qquad
 \operatorname{tr}(A_8^k)=
 \sum_{n\mid k}n\!\sum_{|c|=n}\rho(c)^{k/n}.$$ For $k=1,\ldots,8$, the weighted traces are $$\frac76,\ \frac{49}{36},\ \frac{91}{216},\ \frac{1393}{1296},\
 \frac{13027}{7776},\ \frac{82873}{46656},\
 \frac{430171}{279936},\ \frac{3258913}{1679616}.$$ Setting every edge weight to one recovers the rooted strict column of the table. At powers above eight, $A_8$ repeats its known cycles but omits unknown longer primitive cycles; it is therefore a prefix device, not a global transition matrix.

# Validation and limitations

An independent checker, which imports no producer code, reconstructs all 510 returns, sign decisions, canonical cycles, dimensions, and traces. A SymPy implementation separately verifies each affine fixed point, monodromy polynomial, cyclic-block factor, and trace. Canonical-byte replay protects the receipt, while twelve hostile mutations target source parameters, domains, counts, margins, traces, dimensions, scope, and verdict fields.

The prefix contains no singular return or switching-line hit; this observation is limited to $n\leq8$. It does not establish completeness of the sampled invariant set, exclude border orbits at later periods, or supply the geometric rectangles needed for a Markov theorem.

# Route-A boundary

The strict finite ledger earns the partial-certified A1 label. A finite cycle-atlas construction earns only the certified-prefix A2 label. A global invariant set, global Markov partition, analytic Fredholm determinant, arithmetic data, and Route B are not claimed. In full, the ledger records $$\begin{gathered}
\texttt{A1\_PARTIAL\_CERTIFIED},\quad
\texttt{A2\_CERTIFIED\_PREFIX},\\
\texttt{A3\_NOT\_ADDRESSED},\quad \texttt{A4\_FAIL}.
\end{gathered}$$ The `NO_BAD_EULER_OR_ROOT_NUMBER` scope firewall remains active.
