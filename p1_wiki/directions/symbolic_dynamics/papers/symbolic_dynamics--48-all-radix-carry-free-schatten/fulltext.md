---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--48-all-radix-carry-free-schatten"
canonical_tex: "symbolic_dynamics/papers/48-all-radix-carry-free-schatten/paper/main.tex"
canonical_pdf: "symbolic_dynamics/papers/48-all-radix-carry-free-schatten/paper/CarryFreeRadixOperators.pdf"
source_sha256: "ca139034537b3436acb0c1a5efac211518526b258312822fc2829edf58452539"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Carry-Free Radix Operators: Exact Schatten Surfaces, Binary Endpoint Pinching, and Weighted Cycle Traces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/48-all-radix-carry-free-schatten>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/48-all-radix-carry-free-schatten/paper/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/48-all-radix-carry-free-schatten/paper/CarryFreeRadixOperators.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/48-all-radix-carry-free-schatten/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/48-all-radix-carry-free-schatten/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For an integer radix $b\ge2$, we study the infinite matrix on the positive integers whose $(m,n)$ entry is $\mathbf 1_{\{m+n\text{ is carry-free in base }b\}}(mn)^{-s/2}$. Writing $\sigma=\Re s$, we prove for every $1\le q<\infty$ the exact classification $$B_{b,s}\in S_q
    \quad\Longleftrightarrow\quad
    \sigma>\max\{1,\log_b\|C_b\|_{S_q}\},$$ where $C_b=(\mathbf 1_{a+c<b})_{0\le a,c<b}$. Its singular values are $[2\sin((2j-1)\pi/(4b+2))]^{-1}$, so the critical surface is explicit. The proof separates a universal column wall from a digit-norm wall through exact radix-shell factorizations. At $b=2$, every same-shell block vanishes; paired adjacent-shell compressions recover the full nonmembership range, including equality. Consequently boundedness, compactness, and Hilbert--Schmidt membership are all equivalent to $\sigma>1$, whereas trace class begins at $\sigma>\alpha_b=\log_b\|C_b\|_{S_1}>1$. We also identify the legal domains of the trace, trace powers, the regularized determinant, and the least-period support of the associated countable graph shift. Independent finite lanes, interval checks, and hostile mutations provide consistency evidence for the exact identities; they are not used as proofs of the infinite statements.
author:
- Anonymous
bibliography:
- ../references.bib
title: |
  **Carry-Free Radix Operators:**\
  Exact Schatten Surfaces, Binary Endpoint Pinching,\
  and Weighted Cycle Traces
```

## Markdown 正文

# Introduction {#sec:introduction}

Digitwise constraints are local, but the operators they generate need not have local analytic behavior. A simple example is the rule that two nonnegative base-$b$ digits may be adjacent exactly when their sum is smaller than $b$. As a zero-completed fixed-length control, this rule gives a finite Kronecker power. On the positive integers, however, word length is unbounded, the all-zero word is absent, and the Dirichlet weight interacts with both the number and the length of the admissible words; the finite control is not a finite restriction of this positive-vertex source. The resulting infinite operator therefore has two different sources of divergence.

Write the base-$b$ expansions as $$m=\sum_{j\ge0}m_jb^j,\qquad
  n=\sum_{j\ge0}n_jb^j,
  \qquad 0\le m_j,n_j<b,$$ with only finitely many nonzero digits. We say that $m+n$ is *carry-free in base $b$*, and write $m\mathrel{\perp_b}n$, if $m_j+n_j<b$ for every $j$. For $s\in\mathbb C$, consider the formal matrix $$B_{b,s}(m,n)
  =\mathbf 1_{\{m\mathrel{\perp_b}n\}}(mn)^{-s/2},
  \qquad m,n\in\mathbb N=\{1,2,\ldots\},
  \label{eq:operator-intro}$$ where complex powers use the real logarithm. Whenever this matrix has a bounded completion, we use the same symbol for the resulting operator on $\ell^2(\mathbb N)$.

The finite digit matrix $$C_b=(\mathbf 1_{\{a+c<b\}})_{0\le a,c<b}$$ contains the local rule. Set $$\kappa_{b,q}=\|C_b\|_{S_q},
  \qquad
  \tau_b=\kappa_{b,1},
  \qquad
  \alpha_b=\log_b\tau_b.$$ Our central result is the following exact surface.

[\[thm:main-intro\]]{#thm:main-intro label="thm:main-intro"} For every integer $b\ge2$, every $1\le q<\infty$, and every $s\in\mathbb C$ with $\sigma=\Re s$, $$B_{b,s}\in S_q
  \quad\Longleftrightarrow\quad
  \sigma>\max\{1,\log_b\kappa_{b,q}\}.
  \label{eq:main-surface-intro}$$ Moreover, boundedness, compactness, and Hilbert--Schmidt membership are each equivalent to $\sigma>1$, while trace-class membership is equivalent to $\sigma>\alpha_b$, where $\alpha_b>1$.

The maximum in [\[eq:main-surface-intro\]](#eq:main-surface-intro){reference-type="ref" reference="eq:main-surface-intro"} is structural. The first wall, $\sigma=1$, is already visible in one positive-density column. The second comes from the exponential $S_q$-growth of the digit tensors. It is an active endpoint only when $\log_b\kappa_{b,q}>1$; otherwise the universal wall hides it. Equality at an active digit wall is nevertheless delicate. For $b\ge3$, diagonal radix shells provide a direct orthogonal pinching. For $b=2$, every such diagonal block is exactly zero, and equality must be recovered from disjoint pairs of adjacent shells.

The digit constants are explicit: $$s_j(C_b)
  =
  (
    2\sin\frac{(2j-1)\pi}{4b+2}
  )^{-1},
  \qquad 1\le j\le b.
  \label{eq:digit-spectrum-intro}$$ For example, $\tau_2=\sqrt5$ and $\alpha_2=\log_2\sqrt5$, whereas $\kappa_{b,2}^2=b(b+1)/2<b^2$. Thus the trace-class wall lies strictly to the right of $1$, but the Hilbert--Schmidt digit wall lies strictly to its left for every radix.

Beyond ideal membership, the same domain bookkeeping determines which cycle expressions are legal. In $\sigma>1$, all powers $B_{b,s}^r$, $r\ge2$, are trace class and their traces are absolutely convergent weighted closed-walk sums. Consequently $\det\nolimits_2(I-zB_{b,s})$ is entire in $z$, with its trace-power logarithm only asserted locally near $z=0$. The ordinary trace and Fredholm determinant require the smaller trace-class domain $\sigma>\alpha_b$. The positive-vertex convention is essential here: the all-zero digit word must be removed before traces or temporal support are interpreted.

The mechanism of the proof is summarized in [\[fig:mechanism\]](#fig:mechanism){reference-type="ref" reference="fig:mechanism"}. It also shows the evidence boundary used throughout the paper: finite tensors and computations check identities, but the infinite classification comes from analytic shell summation and endpoint pinching.

#### Contributions and scope.

The paper establishes three linked statements.

1.  It gives a self-contained classification of $B_{b,s}$ in every Banach Schatten ideal $S_q$, for every integer radix, including both strict walls.

2.  It separates the higher-radix same-shell endpoint mechanism from the binary paired-shell mechanism and derives the exact bounded, compact, Hilbert--Schmidt, and trace-class corollaries.

3.  It records the legal weighted trace and determinant domains and the least-period support of the countable carry-free graph shift, with the zero word deleted.

These statements do not assign new ownership to classical carry criteria, finite Pascal or Boolean matrices, finite disjointness tensors, or the general theory of trace ideals. Kummer's and Lucas's classical prime-modular results provide historical arithmetic context [@kummer1852ergaenzung; @lucas1878congruences]; standard ideal and regularized-determinant terminology follows Simon [@simon2005trace]. The all-radix relation used here is defined directly, so no composite-radix version of Kummer's theorem is invoked. A bounded directed search did not find the same-quantifier infinite weighted theorem, but that absence is not a priority or exhaustiveness claim.

#### Organization.

fixes the ownership boundary. derives the digit spectrum, and [4](#sec:shells){reference-type="ref" reference="sec:shells"} turns it into exact shell formulas. proves the sharp surface and both endpoint mechanisms. treats traces, determinants, and least periods. reports finite consistency controls without using them as proof. The appendices expand the digit recurrence, shell coordinates, endpoint limiting arguments, and reproducibility ledger.

# Related work and ownership boundary {#sec:related}

#### Carries and congruences.

For a prime radix, carry counts are classically tied to prime-adic valuations of binomial coefficients through Kummer's theorem [@kummer1852ergaenzung]; Lucas's congruence gives a complementary digitwise description modulo a prime [@lucas1878congruences]. Those results own the relevant arithmetic precedents. Our source relation, however, is simply the coordinatewise inequality $m_j+n_j<b$, defined for every integer $b\ge2$. We use the classical theorems only as prime-radix comparators and never as a definition or proof in composite radix.

#### Finite Pascal, Boolean, and disjointness matrices.

Finite graphs built from binomial parity and their spectra were studied by Christopher and Kennedy [@christopher1997binomial]; symmetric Pascal matrices modulo a prime have a substantial finite theory [@bacher2004pascal]. LaGrange treats eigenvalues of Boolean graphs and Pascal-type matrices [@lagrange2013eigenvalues]. Related disjointness matrices also occur in communication-complexity factorization norms [@linial2007factorization], rectifier-network coverings [@chistikov2017fractional], and algorithms for Kronecker powers [@alman2023kronecker]. These works establish ownership of the finite arithmetic, graph, tensor, spectral, covering, and algorithmic mechanisms that overlap our controls. Accordingly, we claim no novelty for finite digit Kronecker products, finite carry tests, finite singular values as objects, or finite Boolean/disjointness spectra.

#### Trace ideals and determinants.

We use the standard Schatten ideals and the usual Hilbert--Schmidt regularized determinant $\det\nolimits_2$; their general theory is described, for example, by Simon [@simon2005trace]. All estimates particular to the carry-free operator---the shell factorizations, the uniform transfer from unweighted to weighted blocks, the two endpoint pinchings, and the closed-walk limiting argument---are supplied below.

#### Positioning.

The distinction relevant to this paper is between a fixed finite digit tensor and an infinite positive-vertex operator with Dirichlet weights and unbounded digit length. The latter requires simultaneous control of shell separation, digit growth, endpoint equality, and deletion of the all-zero word. The bounded source search performed before writing did not locate the exact combination of quantifiers in [\[thm:main-intro\]](#thm:main-intro){reference-type="ref" reference="thm:main-intro"}; this statement reports the search outcome only and does not establish priority.

# The carry-free source and the digit operator {#sec:digit}

## Conventions and phase removal

For $d\ge1$, define $$C_d=(\mathbf 1_{\{a+c<d\}})_{0\le a,c<d},
  \qquad
  \kappa_{d,q}=\|C_d\|_{S_q},$$ and let $C_0$ denote the zero block, with $\kappa_{0,q}=0$. The positive-vertex alphabet is always $\mathbb N=\{1,2,\ldots\}$. When a length-$L$ tensor $C_b^{\otimes L}$ is used as a finite control, its all-zero word is therefore not a vertex of the infinite source.

The imaginary part of $s$ has no effect on singular values, but the relation is a two-sided unitary equivalence rather than a unitary conjugation. Indeed, for $s=\sigma+\mathrm it$, let $$U_te_n=n^{-\mathrm it/2}e_n.$$ Entrywise, $$B_{b,s}=U_t B_{b,\sigma}U_t.
  \label{eq:two-sided-unitary}$$ Both factors are unitary, so every singular-value assertion can be proved for the real symmetric matrix $B_{b,\sigma}$. We do not infer from [\[eq:two-sided-unitary\]](#eq:two-sided-unitary){reference-type="ref" reference="eq:two-sided-unitary"} that $B_{b,s}$ is positive or self-adjoint when $t\ne0$.

## Exact singular values

[\[prop:digit-spectrum\]]{#prop:digit-spectrum label="prop:digit-spectrum"} The singular values of $C_b$, in decreasing order, are $$s_j(C_b)=
  [
    2\sin\frac{(2j-1)\pi}{4b+2}
  ]^{-1},
  \qquad 1\le j\le b.
  \label{eq:digit-spectrum}$$ Consequently, $$\kappa_{b,q}
  =
  [
    \sum_{j=1}^{b}
    (
      2\sin\frac{(2j-1)\pi}{4b+2}
    )^{-q}
  ]^{1/q}.
  \label{eq:kappa-explicit}$$

The $(a,a')$ entry of $C_bC_b^*$ counts the digits $c$ satisfying $c<b-\max(a,a')$, and hence equals $b-\max(a,a')$. Reverse the row and column order and index the result by $1,\ldots,b$. The resulting matrix is $$K_b=(\min(i,j))_{1\le i,j\le b}.$$ Its inverse is the tridiagonal matrix $$L_b=K_b^{-1}
  =
  \begin{pmatrix}
    2&-1\\
    -1&2&-1\\
    &\ddots&\ddots&\ddots\\
    &&-1&2&-1\\
    &&&-1&1
  \end{pmatrix}.$$ For completeness, multiplying $K_b$ by this matrix subtracts consecutive columns twice in the interior and once at the terminal boundary, producing the identity.

The eigenvalue equation for $L_b$ has the interior solution $v_i=\sin(i\theta)$, with $\lambda=2-2\cos\theta=4\sin^2(\theta/2)$ and the left boundary $v_0=0$. The final row is equivalent to the ghost boundary $v_{b+1}=v_b$, so $$\sin((b+1)\theta)-\sin(b\theta)=0.$$ The $b$ roots in $(0,\pi)$ are $\theta_j=(2j-1)\pi/(2b+1)$. Thus the eigenvalues of $K_b$ are $[4\sin^2(\theta_j/2)]^{-1}$. Taking square roots proves [\[eq:digit-spectrum\]](#eq:digit-spectrum){reference-type="ref" reference="eq:digit-spectrum"}, and summing their $q$th powers proves [\[eq:kappa-explicit\]](#eq:kappa-explicit){reference-type="ref" reference="eq:kappa-explicit"}.

[\[cor:digit-comparisons\]]{#cor:digit-comparisons label="cor:digit-comparisons"} For every $b\ge2$, $$\kappa_{b,2}^2=\frac{b(b+1)}2<b^2,
  \qquad
  \tau_b:=\kappa_{b,1}>b.
  \label{eq:digit-comparisons}$$ In particular $\log_b\kappa_{b,2}<1$ and $\alpha_b:=\log_b\tau_b>1$.

The Hilbert--Schmidt norm squared counts the ones in $C_b$, giving $b+(b-1)+\cdots+1=b(b+1)/2$. Reversing the columns of $C_b$ makes it triangular with unit diagonal, so $\lvert\det C_b\rvert=1$. The product of its singular values is therefore one. Their arithmetic mean is at least their geometric mean, and the inequality is strict because their squared sum $b(b+1)/2$ exceeds $b$. Hence $\tau_b>b$.

::: {#tab:digit-thresholds}
    $b$   $\tau_b$   $\alpha_b$   $\kappa_{b,2}$   $\log_b\kappa_{b,2}$   $\sigma_c(q{=}2)$
  ----- ---------- ------------ ---------------- ---------------------- -------------------
      2   2.236068     1.160964         1.732051               0.792481            1.000000
      3   3.603875     1.166936         2.449490               0.815465            1.000000
      4   5.064178     1.170164         3.162278               0.830482            1.000000
      5   6.595934     1.172119         3.872983               0.841303            1.000000

  : Display evaluations of the exact formulas in [\[eq:kappa-explicit,eq:digit-comparisons\]](#eq:kappa-explicit,eq:digit-comparisons){reference-type="ref" reference="eq:kappa-explicit,eq:digit-comparisons"}. The last column is $\sigma_c(q=2)=\max\{1,\log_b\kappa_{b,2}\}$; the decimals are not empirical estimates and do not define the theorem.
:::

At $b=2$, [\[eq:digit-spectrum\]](#eq:digit-spectrum){reference-type="ref" reference="eq:digit-spectrum"} gives the golden-ratio pair $(1+\sqrt5)/2$ and $(\sqrt5-1)/2$. Their sum is $\sqrt5$, so $$\tau_2=\sqrt5,
  \qquad
  \alpha_2=\log_2\sqrt5.
  \label{eq:binary-alpha}$$ These identities will distinguish the binary trace-class wall from its Hilbert--Schmidt wall.

# Exact radix-shell calculus {#sec:shells}

Let $$I_k=[b^k,b^{k+1})\cap\mathbb N,\qquad k\ge0,$$ and let $P_k$ be the coordinate projection from $\ell^2(\mathbb N)$ onto $\ell^2(I_k)$. We write $A_{k\ell}$ for the unweighted carry-free matrix from $I_\ell$ to $I_k$, and $$B_{k\ell}=P_kB_{b,\sigma}P_\ell.$$ The notation $X\mathrel{\overset{\mathrm{sv}}{\simeq}}Y$ below means that $X$ and $Y$ have the same nonzero singular values, with multiplicity; zero rows and columns may have been deleted.

[\[prop:shell-blocks\]]{#prop:shell-blocks label="prop:shell-blocks"} For $k>\ell$, $$A_{k\ell}
  \mathrel{\overset{\mathrm{sv}}{\simeq}}
  \mathbf 1_{(b-1)b^{k-\ell-1}}
  \otimes C_{b-1}\otimes C_b^{\otimes\ell},
  \label{eq:cross-shell-factor}$$ and hence $$\|A_{k\ell}\|_{S_q}
  =
  ((b-1)b^{k-\ell-1})^{1/2}
  \kappa_{b-1,q}\kappa_{b,q}^{\ell}.
  \label{eq:cross-shell-norm}$$ For $k=\ell$, $$A_{kk}\mathrel{\overset{\mathrm{sv}}{\simeq}}C_{b-2}\otimes C_b^{\otimes k},
  \qquad
  \|A_{kk}\|_{S_q}
  =\kappa_{b-2,q}\kappa_{b,q}^{k}.
  \label{eq:same-shell-factor}$$ The case $k<\ell$ follows by transposition.

Take $m\in I_k$ and $n\in I_\ell$, with $k>\ell$. At each position $0,\ldots,\ell-1$, both digits range from $0$ to $b-1$, and the compatibility matrix is $C_b$. At position $\ell$, the leading digit of $n$ ranges from $1$ to $b-1$. The row indexed by the digit $m_\ell=b-1$ is zero; after deleting it and subtracting one from the column digit of $n$, the compatibility matrix is $C_{b-1}$.

All higher digits of $n$ vanish. The top digit $m_k$ has $b-1$ choices, and the intervening $k-\ell-1$ digits of $m$ have $b$ choices each. They repeat the same lower-digit block, producing the column vector of ones in [\[eq:cross-shell-factor\]](#eq:cross-shell-factor){reference-type="ref" reference="eq:cross-shell-factor"}. A permutation of digit coordinates now gives the displayed tensor product.

When $k=\ell$, both leading digits lie in $\{1,\ldots,b-1\}$. Subtracting one from each turns the condition $m_k+n_k<b$ into a $C_{b-2}$ block; the lower $k$ digit positions again give $C_b^{\otimes k}$. Tensor products multiply singular values, and the lone nonzero singular value of a length-$r$ ones vector is $\sqrt r$. This proves all norm identities.

[\[rem:binary-zero-block\]]{#rem:binary-zero-block label="rem:binary-zero-block"} For $b=2$, [\[eq:same-shell-factor\]](#eq:same-shell-factor){reference-type="ref" reference="eq:same-shell-factor"} contains $C_0$, so every $A_{kk}$ is exactly zero. On the adjacent shells, however, $\kappa_{1,q}=1$, and [\[eq:cross-shell-norm\]](#eq:cross-shell-norm){reference-type="ref" reference="eq:cross-shell-norm"} gives $$\|A_{2j+1,2j}\|_{S_q}=\kappa_{2,q}^{2j}.
  \label{eq:binary-adjacent-exact}$$ Thus the binary endpoint is not absent; it lives off the shell diagonal.

## Uniform transfer to weighted blocks

Let $D_k$ be diagonal on $\ell^2(I_k)$, with $(D_k)_{m,m}=m^{-\sigma/2}$. For real $\sigma>0$, $$B_{k\ell}=D_kA_{k\ell}D_\ell,
  \qquad
  b^{-(k+1)\sigma/2}I
  \le D_k\le
  b^{-k\sigma/2}I.$$

[\[lem:weighted-comparison\]]{#lem:weighted-comparison label="lem:weighted-comparison"} For $\sigma>0$, every $k,\ell\ge0$, and $1\le q<\infty$, $$b^{-\sigma}b^{-(k+\ell)\sigma/2}
  \|A_{k\ell}\|_{S_q}
  \le
  \|B_{k\ell}\|_{S_q}
  \le
  b^{-(k+\ell)\sigma/2}
  \|A_{k\ell}\|_{S_q}.
  \label{eq:weighted-comparison}$$

The upper bound is the ideal inequality $\|RXT\|_{S_q}\le\|R\|\|X\|_{S_q}\|T\|$. For the lower bound, write $A_{k\ell}=D_k^{-1}B_{k\ell}D_\ell^{-1}$ and use $\|D_k^{-1}\|\le b^{(k+1)\sigma/2}$ and the analogous estimate for $D_\ell^{-1}$. The resulting constants are independent of the shell indices, which is what preserves equality endpoints.

Combining [\[eq:cross-shell-norm,eq:weighted-comparison\]](#eq:cross-shell-norm,eq:weighted-comparison){reference-type="ref" reference="eq:cross-shell-norm,eq:weighted-comparison"} and putting $k=\ell+h$, $h\ge1$, yields $$\|B_{\ell+h,\ell}\|_{S_q}
  \le
  c_{b,q}\,
  b^{h(1-\sigma)/2}
  (\kappa_{b,q}b^{-\sigma})^\ell,
  \qquad
  c_{b,q}=\sqrt{\frac{b-1}{b}}\,\kappa_{b-1,q}.
  \label{eq:two-ratios}$$ The two ratios in [\[eq:two-ratios\]](#eq:two-ratios){reference-type="ref" reference="eq:two-ratios"} are the two walls of the theorem. The exact critical curves obtained from [\[eq:kappa-explicit\]](#eq:kappa-explicit){reference-type="ref" reference="eq:kappa-explicit"} are shown in [1](#fig:critical-surfaces){reference-type="ref" reference="fig:critical-surfaces"}.

![The exact critical abscissa $\sigma_c(q)=\max\{1,\log_b\kappa_{b,q}\}$, evaluated from [\[eq:kappa-explicit\]](#eq:kappa-explicit){reference-type="ref" reference="eq:kappa-explicit"} for four radices. The points at $q=1$ are the trace-class thresholds. Once the digit curve falls below $1$, the universal column wall is active and produces the plateau. Line styles and markers duplicate the color encoding.](../figures/generated/critical_surfaces.pdf){#fig:critical-surfaces width="\\textwidth"}

# Sharp ideal thresholds {#sec:thresholds}

## Sufficiency

[\[prop:sufficiency\]]{#prop:sufficiency label="prop:sufficiency"} If $$\sigma>1
  \quad\text{and}\quad
  \kappa_{b,q}b^{-\sigma}<1,
  \label{eq:sufficiency-conditions}$$ then $B_{b,s}\in S_q$.

By the two-sided unitary relation [\[eq:two-sided-unitary\]](#eq:two-sided-unitary){reference-type="ref" reference="eq:two-sided-unitary"}, it is enough to take $s=\sigma$. Sum the embedded shell blocks first over a finite square $0\le k,\ell\le K$. For the strict upper triangle, put $k=\ell+h$. gives $$\sum_{\ell\ge0}\sum_{h\ge1}
  \|B_{\ell+h,\ell}\|_{S_q}
  \le
  c_{b,q}
  \sum_{h\ge1}b^{h(1-\sigma)/2}
  \sum_{\ell\ge0}
  (\kappa_{b,q}b^{-\sigma})^\ell.$$ Both geometric series converge under [\[eq:sufficiency-conditions\]](#eq:sufficiency-conditions){reference-type="ref" reference="eq:sufficiency-conditions"}. The lower triangle has the same block norms. On the diagonal, [\[eq:same-shell-factor,eq:weighted-comparison\]](#eq:same-shell-factor,eq:weighted-comparison){reference-type="ref" reference="eq:same-shell-factor,eq:weighted-comparison"} gives $$\sum_{k\ge0}\|B_{kk}\|_{S_q}
  \le
  \kappa_{b-2,q}
  \sum_{k\ge0}
  (\kappa_{b,q}b^{-\sigma})^k.$$ Because $q\ge1$, $S_q$ is a Banach ideal. The finite block sums are therefore Cauchy in $S_q$, and their limit has the prescribed matrix entries. This constructs the completed operator and proves the claim.

## The universal wall

[\[prop:column-wall\]]{#prop:column-wall label="prop:column-wall"} If $\sigma\le1$, the formal matrix in [\[eq:operator-intro\]](#eq:operator-intro){reference-type="ref" reference="eq:operator-intro"} has no bounded completion on $\ell^2(\mathbb N)$.

The column indexed by $n=1$ contains every $m$ whose units digit lies in $\{0,\ldots,b-2\}$, because adding $1$ creates no carry exactly on that residue set. The squared norm of this column is therefore at least $$\sum_{\substack{m\ge1\\m\bmod b\in\{0,\ldots,b-2\}}}m^{-\sigma}.$$ For $0<\sigma\le1$, this is a finite union of arithmetic-progression subseries of the divergent $p$-series; for $\sigma\le0$, its summands do not tend to zero. Hence the column is not in $\ell^2$, which is incompatible with boundedness.

The universal obstruction has no digit-spectrum input. It remains the active wall whenever $\log_b\kappa_{b,q}\le1$; in that case the point $\sigma=\log_b\kappa_{b,q}$ is already on the unbounded side and is not a second analytic endpoint.

## The higher-radix digit wall

We use the standard orthogonal block pinching: if $(Q_j)$ are mutually orthogonal projections, then $$\Phi(T)=\bigoplus_j Q_jTQ_j$$ is contractive on $S_q$, $1\le q<\infty$, and $$\|\Phi(T)\|_{S_q}^q
  =\sum_j\|Q_jTQ_j\|_{S_q}^q.
  \label{eq:pinching-norm}$$ The statement follows first for finite families by averaging over diagonal unitaries and then for countable families by monotone truncation.

Suppose $\sigma>1$ and $$\rho_{b,q}(\sigma):=\kappa_{b,q}b^{-\sigma}\ge1.$$ For $b\ge3$, pinch $B_{b,\sigma}$ with the shell projections $P_k$. The lower half of [\[eq:weighted-comparison\]](#eq:weighted-comparison){reference-type="ref" reference="eq:weighted-comparison"} gives $$\|B_{kk}\|_{S_q}
  \ge
  b^{-\sigma}\kappa_{b-2,q}
  \rho_{b,q}(\sigma)^k.
  \label{eq:higher-radix-lower}$$ Because $\kappa_{b-2,q}>0$, the $q$th powers in [\[eq:higher-radix-lower\]](#eq:higher-radix-lower){reference-type="ref" reference="eq:higher-radix-lower"} are not summable. By [\[eq:pinching-norm\]](#eq:pinching-norm){reference-type="ref" reference="eq:pinching-norm"}, $B_{b,\sigma}\notin S_q$.

When $\log_b\kappa_{b,q}>1$, this argument treats the active digit-wall endpoint $\sigma=\log_b\kappa_{b,q}$ and the entire interval strictly below it but above the universal wall. When $\log_b\kappa_{b,q}\le1$, no $\sigma>1$ satisfies $\rho_{b,q}(\sigma)\ge1$, and [\[prop:column-wall\]](#prop:column-wall){reference-type="ref" reference="prop:column-wall"} already supplies necessity.

## Binary paired-shell repair {#sec:binary-pairing}

At $b=2$, the preceding pinch is illegal as a digit-wall witness because $B_{kk}=0$ for every $k$; see [\[rem:binary-zero-block\]](#rem:binary-zero-block){reference-type="ref" reference="rem:binary-zero-block"}. We first remove the phase by [\[eq:two-sided-unitary\]](#eq:two-sided-unitary){reference-type="ref" reference="eq:two-sided-unitary"} and work with the real matrix $B_{2,\sigma}$. Let $$\widehat P_j=P_{2j}+P_{2j+1},
  \qquad
  X_j:=B_{2j+1,2j}.$$ The spaces $I_{2j}\oplus I_{2j+1}$ are mutually orthogonal. Since the two diagonal-shell blocks vanish and $B_{2,\sigma}$ is real symmetric, $$\widehat P_jB_{2,\sigma}\widehat P_j
  =
  \begin{pmatrix}
    0&X_j^*\\
    X_j&0
  \end{pmatrix}.
  \label{eq:binary-pair-block}$$ Its nonzero singular values are those of $X_j$, each repeated twice, so $$\|\widehat P_jB_{2,\sigma}\widehat P_j\|_{S_q}^q
  =2\|X_j\|_{S_q}^q.
  \label{eq:binary-double-sv}$$

Using [\[eq:binary-adjacent-exact\]](#eq:binary-adjacent-exact){reference-type="ref" reference="eq:binary-adjacent-exact"} in the lower weighted comparison, $$\|X_j\|_{S_q}
  \ge
  2^{-3\sigma/2}
  (\kappa_{2,q}2^{-\sigma})^{2j}.
  \label{eq:binary-pair-lower}$$ Thus, throughout the full binary digit-norm nonmembership range $\kappa_{2,q}2^{-\sigma}\ge1$ with $\sigma>1$, the $q$th powers of the paired compressions are nonsummable. This includes both the strict-below case, where the lower bound grows, and equality, where it does not decay. Equality is the exceptional repaired endpoint only because same-shell pinching is unavailable. As before, if the digit wall is at or below $1$, the universal column wall is the active boundary.

## Classification and operator classes

[\[thm:sharp-classification\]]{#thm:sharp-classification label="thm:sharp-classification"} For every integer $b\ge2$, every $1\le q<\infty$, and every $s\in\mathbb C$, with $\sigma=\Re s$, $$B_{b,s}\in S_q
  \quad\Longleftrightarrow\quad
  \sigma>\max\{1,\log_b\kappa_{b,q}\}.$$

The forward implication fails at $\sigma\le1$ by [\[prop:column-wall\]](#prop:column-wall){reference-type="ref" reference="prop:column-wall"}. For $\sigma>1$ but $\kappa_{b,q}b^{-\sigma}\ge1$, it fails by [\[eq:higher-radix-lower\]](#eq:higher-radix-lower){reference-type="ref" reference="eq:higher-radix-lower"} when $b\ge3$ and by [\[eq:binary-pair-lower\]](#eq:binary-pair-lower){reference-type="ref" reference="eq:binary-pair-lower"} when $b=2$. Two-sided unitary equivalence transfers these conclusions from real $\sigma$ to complex $s$. The reverse implication is [\[prop:sufficiency\]](#prop:sufficiency){reference-type="ref" reference="prop:sufficiency"}.

[\[cor:operator-classes\]]{#cor:operator-classes label="cor:operator-classes"} The following are equivalent: $$B_{b,s}\text{ is bounded},\qquad
  B_{b,s}\text{ is compact},\qquad
  B_{b,s}\in S_2,\qquad
  \sigma>1.$$ Furthermore, $$B_{b,s}\in S_1
  \quad\Longleftrightarrow\quad
  \sigma>\alpha_b=\log_b\tau_b>1.$$

For $\sigma>1$, [\[cor:digit-comparisons\]](#cor:digit-comparisons){reference-type="ref" reference="cor:digit-comparisons"} gives $\log_b\kappa_{b,2}<1$, so [\[thm:sharp-classification\]](#thm:sharp-classification){reference-type="ref" reference="thm:sharp-classification"} yields Hilbert--Schmidt, hence compact and bounded, membership. For $\sigma\le1$, boundedness fails by [\[prop:column-wall\]](#prop:column-wall){reference-type="ref" reference="prop:column-wall"}. The trace-class statement is the case $q=1$, together with $\tau_b>b$.

# Traces, determinants, and temporal support {#sec:dynamics}

## The diagonal trace

A diagonal entry is present precisely when a positive integer is carry-free with itself. Define $$\mathcal D_b
  =
  \{
    m\ge1:
    \text{every base-\(b\) digit of \(m\) is at most }
    \lfloor\frac{b-1}{2}\rfloor
  \}.
  \label{eq:loop-digit-set}$$ The all-zero digit word would satisfy the digit restriction, but it is deleted because the source alphabet is $\mathbb N$.

[\[prop:diagonal-trace\]]{#prop:diagonal-trace label="prop:diagonal-trace"} If $\sigma>\alpha_b$, then $$\mathop{\mathrm{Tr}}(B_{b,s})
  =
  \sum_{m\in\mathcal D_b}m^{-s},
  \label{eq:trace-dirichlet}$$ and the series is absolutely convergent. In this trace-class domain, the trace is zero for $b=2$. For $b>2$, it is strictly positive on the real half-line $s=\sigma>\alpha_b$.

By [\[cor:operator-classes\]](#cor:operator-classes){reference-type="ref" reference="cor:operator-classes"}, $B_{b,s}$ is trace class in the stated domain, so its trace is the absolutely convergent sum of its diagonal entries in the standard basis. The condition $m\mathrel{\perp_b}m$ is exactly $2m_j<b$ at every digit, which is [\[eq:loop-digit-set\]](#eq:loop-digit-set){reference-type="ref" reference="eq:loop-digit-set"}; the diagonal weight is $m^{-s}$. For $b=2$, the only allowed digit is zero, so no positive vertex remains and $\mathcal D_2=\varnothing$. For $b>2$, the vertex $1$ is in $\mathcal D_b$, and every term is positive when $s=\sigma$ is real.

The statement that the binary trace is zero in [\[prop:diagonal-trace\]](#prop:diagonal-trace){reference-type="ref" reference="prop:diagonal-trace"} is an operator-trace statement only for $\sigma>\alpha_2$. Outside that domain, the diagonal or loop support is still empty, but we do not thereby define an operator trace. Likewise, positivity of the real Dirichlet series gives no zero-free statement for nonreal $s$.

## Trace powers as absolutely convergent walk sums

Let a *based closed $r$-walk* be a tuple $(n_1,\ldots,n_r)\in\mathbb N^r$ satisfying $$n_i\mathrel{\perp_b}n_{i+1},
  \qquad i\pmod r,$$ where $n_{r+1}=n_1$. The base point matters, so cyclic rotations are not identified.

[\[prop:trace-powers\]]{#prop:trace-powers label="prop:trace-powers"} If $\sigma>1$ and $r\ge2$, then $B_{b,s}^r\in S_1$ and $$\mathop{\mathrm{Tr}}(B_{b,s}^r)
  =
  \sum_{\substack{n_1,\ldots,n_r\ge1\\
                  n_i\mathrel{\perp_b}n_{i+1}\ (i\bmod r)}}
  \prod_{i=1}^{r}n_i^{-s}.
  \label{eq:closed-walk-trace}$$ The series on the right is absolutely convergent.

By [\[cor:operator-classes\]](#cor:operator-classes){reference-type="ref" reference="cor:operator-classes"}, $B_{b,s}\in S_2$ and is bounded. Hence $B_{b,s}^2\in S_1$, and multiplying by bounded powers shows $B_{b,s}^r\in S_1$ for every $r\ge2$.

Let $Q_K=\sum_{k=0}^{K}P_k$ and $T_K=Q_KB_{b,s}Q_K$. Because $B_{b,s}$ is Hilbert--Schmidt and $Q_K$ increases strongly to the identity, $$\|T_K-B_{b,s}\|_{S_2}\longrightarrow0.$$ For $r=2$, the ideal inequality gives $$\|T_K^2-B_{b,s}^2\|_{S_1}
  \le
  (\|T_K\|_{S_2}+\|B_{b,s}\|_{S_2})
  \|T_K-B_{b,s}\|_{S_2}.$$ For $r>2$, a telescoping expansion followed by bounded multiplication gives the same convergence in $S_1$: $$T_K^r\longrightarrow B_{b,s}^r
  \quad\text{in }S_1.
  \label{eq:power-trace-norm-limit}$$ Thus the finite traces converge to the operator trace.

For each $K$, direct finite matrix multiplication yields $$\mathop{\mathrm{Tr}}(T_K^r)
  =
  \sum_{\substack{n_1,\ldots,n_r<b^{K+1}\\
                  n_i\mathrel{\perp_b}n_{i+1}\ (i\bmod r)}}
  \prod_{i=1}^{r}n_i^{-s}.$$ To justify passage through the infinite sum, repeat the construction with the real matrix $B_{b,\sigma}$. Every term is nonnegative, the finite walk sums increase with $K$, and [\[eq:power-trace-norm-limit\]](#eq:power-trace-norm-limit){reference-type="ref" reference="eq:power-trace-norm-limit"} shows that their traces converge to the finite number $\mathop{\mathrm{Tr}}(B_{b,\sigma}^r)$. Monotone convergence therefore gives $$\sum_{\text{based closed \(r\)-walks}}
  \prod_{i=1}^{r}n_i^{-\sigma}<\infty.$$ This is exactly the sum of the absolute values of the complex-$s$ terms. The complex finite sums may consequently pass term by term to the absolutely convergent limit, and their trace-norm limit identifies that limit with $\mathop{\mathrm{Tr}}(B_{b,s}^r)$.

## Regularized and ordinary determinants

[\[cor:determinant-domains\]]{#cor:determinant-domains label="cor:determinant-domains"} For $\sigma>1$, the Hilbert--Schmidt regularized determinant $$\det\nolimits_2(I-zB_{b,s})$$ is an entire function of $z$. On a sufficiently small neighborhood of $z=0$, with the logarithm normalized to vanish at zero, $$\log\det\nolimits_2(I-zB_{b,s})
  =
  -\sum_{r=2}^{\infty}
  \frac{z^r}{r}\mathop{\mathrm{Tr}}(B_{b,s}^r),
  \label{eq:det2-local-log}$$ and each coefficient has the absolutely convergent walk expansion in [\[eq:closed-walk-trace\]](#eq:closed-walk-trace){reference-type="ref" reference="eq:closed-walk-trace"}. The ordinary trace and Fredholm determinant $\det(I-zB_{b,s})$ are asserted only for $\sigma>\alpha_b$.

For an $S_2$ operator, the regularized determinant $\det\nolimits_2(I-zB)=\det((I-zB)\exp(zB))$ is entire in $z$; this is the standard trace-ideal construction [@simon2005trace]. For, say, $|z|\|B_{b,s}\|<1$, the norm-convergent logarithm and [\[prop:trace-powers\]](#prop:trace-powers){reference-type="ref" reference="prop:trace-powers"} give [\[eq:det2-local-log\]](#eq:det2-local-log){reference-type="ref" reference="eq:det2-local-log"}. The ordinary Fredholm determinant requires $B_{b,s}\in S_1$, whose exact domain is $\sigma>\alpha_b$ by [\[cor:operator-classes\]](#cor:operator-classes){reference-type="ref" reference="cor:operator-classes"}.

We make no claim that [\[eq:det2-local-log\]](#eq:det2-local-log){reference-type="ref" reference="eq:det2-local-log"} converges for all $z$, even though the determinant itself is entire in $z$. Nor do we construct a completed function of $s$, a functional equation, or a prescribed divisor.

## Least periods of the graph shift

Let $$\Sigma_b
  =
  \{(x_j)_{j\in\mathbb N_0}\in\mathbb N^{\mathbb N_0}:
    x_j\mathrel{\perp_b}x_{j+1}\text{ for every }j\in\mathbb N_0\}$$ with the one-sided left shift. Repeating a cyclically admissible period-$r$ word to the right gives a periodic point, and every periodic point arises this way; its least period is its least shift period. We discuss support only, independently of the complex weights.

[\[prop:least-periods\]]{#prop:least-periods label="prop:least-periods"} The least-period sets are $$\operatorname{LPS}(\Sigma_2)=\{2,3,\ldots\},
  \qquad
  \operatorname{LPS}(\Sigma_b)=\{1,2,3,\ldots\}\quad(b>2).
  \label{eq:least-period-sets}$$ For every allowed length, there are infinitely many periodic points.

Distinct powers of $b$ are pairwise carry-free because their nonzero digits occupy distinct positions. At $b=2$, no positive vertex has a loop: any nonzero binary digit produces a carry when added to itself. Two distinct powers give a cyclic word of least period two. For each $r\ge3$, a word of $r$ distinct powers is cyclically admissible and cannot have a smaller period because all of its symbols are distinct.

For $b>2$, the vertex $1$ has a loop, providing least period one, and the same distinct-power construction gives every $r\ge2$. Finally, shifting every chosen digit position upward by an arbitrary common amount produces infinitely many distinct witnesses of the same least period.

It follows that the unweighted fixed-point count is infinite at every allowed length (for $b=2$, at every length at least two). Therefore the usual Artin--Mazur coefficients are not finite and no unweighted Artin--Mazur zeta function is claimed. The period statement is proved from support witnesses, not inferred from traces that could cancel for complex $s$.

# Independent finite controls and proof audit {#sec:validation}

This section reports finite consistency evidence, not a proof of [\[thm:sharp-classification\]](#thm:sharp-classification){reference-type="ref" reference="thm:sharp-classification"}. Every infinite statement above has an analytic proof independent of evaluator output, certificate status, or a finite cutoff.

Two separately constructed finite lanes were frozen. Lane A formed direct positive prefixes and checked carry-freeness by quotient and remainder. Lane B used digit automata and shell tensors. Each lane emitted $1{,}965$ rows. Across the common corpus, $8{,}010$ digit singular-value intervals overlapped, $420$ direct weighted shell norms lay inside independently constructed endpoint envelopes, and the exact fields had no mismatch, missing row, extra row, or duplicate row.

An independently implemented proof audit checked four dependency and domain claims: the universal wall, the digit wall, the determinant domain, and the trace/least-period ledger. These checks do not replace the arguments in [\[sec:thresholds,sec:dynamics\]](#sec:thresholds,sec:dynamics){reference-type="ref" reference="sec:thresholds,sec:dynamics"}.

The hostile suite contained $39$ atomic mutations. Across all consumers, it produced $68$ designated rejections and $322$ nondesignated acceptances, the latter checking that unrelated consumers did not reject an out-of-scope mutation. A further $76$ physical or adversarial instances had zero survivors. Independent replays of both finite states passed in normal and adversarial import-path environments. The census is summarized in [\[tab:validation-census\]](#tab:validation-census){reference-type="ref" reference="tab:validation-census"}.

The scope limitations are explicit. The source search was bounded; the validation set was finite; the Banach-ideal argument does not treat $0<q<1$; and the finite replay makes no archival, publication, or priority inference.

# Discussion and conclusion {#sec:conclusion}

The carry-free operator separates cleanly into a local and a global mechanism. The local digit matrix supplies the exact growth factor $\kappa_{b,q}$; the global shell geometry supplies a second ratio $b^{(1-\sigma)/2}$. Both must be strictly smaller than one. A positive-density column makes the first global obstruction visible before any tensor calculation, whereas orthogonal pinching makes the digit obstruction sharp. In radix two, zero same-shell blocks change the pinching geometry but not the final formula: adjacent paired shells recover the entire relevant bad range and, in particular, its active equality endpoint.

The same ideal surface prevents domain slippage in the dynamical consequences. Trace powers and $\det\nolimits_2$ begin at the Hilbert--Schmidt wall $\sigma>1$; the ordinary trace and Fredholm determinant begin only at the trace-class wall $\sigma>\alpha_b$. Deleting the all-zero word then determines the loop and least-period ledgers. These support statements cannot be replaced by complex trace values, just as finite numerical agreement cannot replace the endpoint proofs.

The reusable lesson is methodological: an endpoint classification for an infinite digit operator must keep shell summability, column boundedness, and zero-block geometry separate. The present proof uses the triangle inequality in a Banach Schatten ideal, so it does not settle $0<q<1$. Other natural questions include quasi-Schatten thresholds and digit automata whose shell blocks are not pure tensor powers. We make no priority claim for the present combination, and no completed $s$-plane object, rational-prime primitive ledger, or spectral-divisor interpretation is asserted.

# Digit covariance details {#app:digit}

We record the elementary inverse and boundary calculation behind [\[prop:digit-spectrum\]](#prop:digit-spectrum){reference-type="ref" reference="prop:digit-spectrum"}. Write $K_{ij}=\min(i,j)$ and let $L$ have diagonal $2,\ldots,2,1$ and first off-diagonals $-1$. For an interior column $2\le j\le b-1$, $$(KL)_{ij}
  =
  -K_{i,j-1}+2K_{ij}-K_{i,j+1}
  =
  \mathbf 1_{\{i=j\}}.$$ The same direct difference at $j=1$ uses $K_{i,0}=0$, and the terminal column gives $-K_{i,b-1}+K_{i,b}=\mathbf 1_{\{i=b\}}$. Thus $L=K^{-1}$.

For $Lv=\lambda v$, the interior recurrence and $v_0=0$ give $$v_i=\sin(i\theta),
  \qquad
  \lambda=2-2\cos\theta.$$ The final equation $-v_{b-1}+v_b=\lambda v_b$ agrees with the interior recurrence exactly when $v_{b+1}=v_b$. Therefore $$0=\sin((b+1)\theta)-\sin(b\theta)
   =2\cos(\frac{(2b+1)\theta}{2})
      \sin(\frac{\theta}{2}).$$ The nonzero modes are $\theta_j=(2j-1)\pi/(2b+1)$, $1\le j\le b$. Since the eigenvalues of $K$ are $[4\sin^2(\theta_j/2)]^{-1}$, their positive square roots give [\[eq:digit-spectrum\]](#eq:digit-spectrum){reference-type="ref" reference="eq:digit-spectrum"}.

Finally, column reversal changes $C_b$ into a triangular matrix with ones on its diagonal. Hence $$\prod_{j=1}^{b}s_j(C_b)=|\det C_b|=1.$$ The strict inequality $\sum_js_j(C_b)>b$ follows from strict arithmetic--geometric mean because $\sum_js_j(C_b)^2=b(b+1)/2>b$, so the singular values cannot all equal one.

# Shell-factor bookkeeping {#app:shells}

This appendix makes the coordinate deletion in [\[prop:shell-blocks\]](#prop:shell-blocks){reference-type="ref" reference="prop:shell-blocks"} explicit. Suppose $k>\ell$. Decompose the digits of $m\in I_k$ as $$(
    m_k,\ldots,m_{\ell+1};
    m_\ell;
    m_{\ell-1},\ldots,m_0
  )$$ and those of $n\in I_\ell$ as $$(
    n_\ell;
    n_{\ell-1},\ldots,n_0
  ).$$ The first group of digits of $m$ has $(b-1)b^{k-\ell-1}$ possibilities and is automatically compatible with the zero digits of $n$. It is therefore a row-repetition coordinate. At position $\ell$, the column digit $n_\ell$ is nonzero. The row $m_\ell=b-1$ has no compatible column and is deleted. The relabeling $$a=m_\ell\in\{0,\ldots,b-2\},
  \qquad
  c=n_\ell-1\in\{0,\ldots,b-2\}$$ turns $m_\ell+n_\ell<b$ into $a+c<b-1$, which is $C_{b-1}$. Each lower position contributes $C_b$. This proves [\[eq:cross-shell-factor\]](#eq:cross-shell-factor){reference-type="ref" reference="eq:cross-shell-factor"}; no all-zero positive vertex has been added.

If $k=\ell$, both leading digits are nonzero. Any compatible pair lies in $\{1,\ldots,b-2\}^2$, and subtracting one from both digits changes $$m_k+n_k<b
  \quad\text{to}\quad
  (m_k-1)+(n_k-1)<b-2.$$ This is $C_{b-2}$; the lower positions again contribute $C_b^{\otimes k}$. For $b=2$ the compatible leading-digit set is empty, giving the zero block $C_0$. The $k<\ell$ formula is the transpose of the $k>\ell$ formula because the carry-free relation is symmetric.

The weighted comparison is also insensitive to zero rows and columns. For the lower estimate, the exact identity $$A_{k\ell}=D_k^{-1}B_{k\ell}D_\ell^{-1}$$ and the shellwise bounds on the inverse diagonals lose only the fixed factor $b^\sigma$. This uniformity, rather than the exact value of the factor, is what allows the lower bounds to remain nondecaying at equality.

# Endpoint pinching and determinant convergence {#app:endpoint}

## Direct-sum accounting

For a finite family of mutually orthogonal projections $Q_1,\ldots,Q_N$, the block-diagonal map $$T\longmapsto\sum_{j=1}^{N}Q_jTQ_j$$ is an average over diagonal sign unitaries and is therefore contractive on every $S_q$, $1\le q<\infty$. Letting $N\to\infty$ gives the countable version used in [\[eq:pinching-norm\]](#eq:pinching-norm){reference-type="ref" reference="eq:pinching-norm"}. Because the image is a direct sum, $$\|\bigoplus_jQ_jTQ_j\|_{S_q}^q
  =\sum_j\|Q_jTQ_j\|_{S_q}^q.$$

For $b\ge3$, take $Q_j=P_j$ and use [\[eq:higher-radix-lower\]](#eq:higher-radix-lower){reference-type="ref" reference="eq:higher-radix-lower"}. For $b=2$, take $Q_j=\widehat P_j=P_{2j}+P_{2j+1}$. If $$H_j=
  \begin{pmatrix}0&X_j^*\\X_j&0\end{pmatrix},$$ then $$H_j^*H_j
  =
  \begin{pmatrix}X_j^*X_j&0\\0&X_jX_j^*\end{pmatrix}.$$ The nonzero eigenvalues of the two diagonal blocks agree, proving $\|H_j\|_{S_q}^q=2\|X_j\|_{S_q}^q$. Together with [\[eq:binary-pair-lower\]](#eq:binary-pair-lower){reference-type="ref" reference="eq:binary-pair-lower"}, this rejects both $\kappa_{2,q}2^{-\sigma}>1$ and equality whenever the digit wall is relevant above the universal wall.

## Finite-shell passage for trace powers

Let $T=B_{b,s}\in S_2$ and $T_K=Q_KTQ_K$. The elementary Hilbert--Schmidt approximation $$\|T-Q_KTQ_K\|_{S_2}
  \le
  \|(I-Q_K)T\|_{S_2}+\|Q_KT(I-Q_K)\|_{S_2}
  \longrightarrow0$$ justifies the first limit in the proof of [\[prop:trace-powers\]](#prop:trace-powers){reference-type="ref" reference="prop:trace-powers"}. The telescoping identity $$T_K^r-T^r
  =
  \sum_{j=0}^{r-1}T_K^j(T_K-T)T^{r-1-j}$$ is estimated in $S_1$ by placing the $S_2$ difference next to one $S_2$ factor and bounding the remaining factors in operator norm. For the endpoint terms one first uses the $r=2$ estimate and then bounded multiplication. Hence $T_K^r\to T^r$ in trace norm for every $r\ge2$.

For real $\sigma$, the finite closed-walk sums have nonnegative terms and increase with $K$. Their bounded trace limit supplies an integrable majorant for the complex-$s$ sums. This is the required exchange of the finite-shell limit with the walk expansion; trace-class membership alone is not being used as an unexplained termwise interchange.

Finally, for $|z|\|T\|<1$, the scalar identity $$\log(1-z\lambda)+z\lambda
  =-\sum_{r\ge2}\frac{z^r\lambda^r}{r}$$ may be summed over the eigenvalues using the $S_2$ bound. This proves the local series in [\[eq:det2-local-log\]](#eq:det2-local-log){reference-type="ref" reference="eq:det2-local-log"}. Analytic continuation defines the entire determinant, not a global choice of its logarithm or global convergence of that series.

# Reproducibility and evidence ledger {#app:reproducibility}

The data-driven assets are generated by from the content-addressed . The generator recomputes the critical curves from [\[eq:kappa-explicit\]](#eq:kappa-explicit){reference-type="ref" reference="eq:kappa-explicit"}, checks the summary's finite bindings and evidence ceiling, emits the tables, and records input/output SHA-256 values in . Thus the displayed decimals and census values do not depend on manual transcription.

Before asset generation, the canonical extraction checked the finite contract, two independently produced output trees, result ledgers, exact cross-lane fields, interval overlap, and mutation and adversarial counts. A separate replay then checked both finite states in normal and adversarial import environments. The figure and tables are deterministic evaluations of the exact digit formula or literal reports of that frozen census.

Evidence types remain disjoint:

-   the arguments in [\[sec:digit,sec:shells,sec:thresholds,sec:dynamics\]](#sec:digit,sec:shells,sec:thresholds,sec:dynamics){reference-type="ref" reference="sec:digit,sec:shells,sec:thresholds,sec:dynamics"} are the mathematical proof;

-   four independent audit checks examine proof dependencies and strict domains;

-   finite tensors, intervals, cutoffs, mutations, and adversarial replays are falsification and implementation controls only; and

-   the directed literature search is bounded and cannot establish priority.

No external archival or publication-attestation artifact is claimed in this manuscript.
