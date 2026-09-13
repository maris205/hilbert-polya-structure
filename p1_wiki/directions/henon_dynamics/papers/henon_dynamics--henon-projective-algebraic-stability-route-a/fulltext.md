---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-projective-algebraic-stability-route-a"
canonical_tex: "henon_dynamics/henon_projective_algebraic_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_projective_algebraic_stability_route_a/paper/main.pdf"
source_sha256: "799e2aa540fc028e8c826e4b0684fd44195dc3d4c6396a04207a9c0617cae201"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projective Algebraic Stability and Exact Degree Doubling for a Quadratic Hénon Automorphism

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_projective_algebraic_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_projective_algebraic_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_projective_algebraic_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_projective_algebraic_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the polynomial automorphism $H(x,y)=(x^2-4-y,x)$ and determine its exact projective degree growth. Its forward and inverse indeterminacy points are distinct, and the exceptional line maps to a forward-fixed point. A recurrence proves $\deg H^n=2^n$ for every $n\geq1$, hence algebraic dynamical degree two. We also certify two fixed points and a primitive real two-cycle with exact tangent monodromy; parameters $-3$ and $-5$ are exact negative controls for that cycle. These are exact structural data, but there is no complete orbit atlas, prime-like target correspondence, or determinant/analytic bridge.
author:
- 'Anonymous Route-A report'
title: |
  Projective Algebraic Stability and Exact Degree Doubling\
  for a Quadratic Hénon Automorphism
```

## Markdown 正文

# Birational projective geometry

Freeze $$H(x,y)=(x^2-4-y,x),\qquad H^{-1}(x,y)=(y,y^2-4-x).$$ Direct substitution verifies both inverse compositions. Homogenization gives $$\bar H[X:Y:Z]=[X^2-4Z^2-YZ:XZ:Z^2],$$ $$\bar H^{-1}[X:Y:Z]=[YZ:Y^2-4Z^2-XZ:Z^2].$$ The corresponding indeterminacy points are $I_+=[0:1:0]$ and $I_-=[1:0:0]$. On $Z=0$ away from $I_+$, the forward map has image $I_-$, and $\bar H(I_-)=I_-$. Since $\det DH=1$, the affine map has no exceptional curve; the line at infinity is the only projective exceptional curve. Its orbit is the fixed sequence $I_-,I_-,\ldots$ and therefore never reaches $I_+$.

# Degree recurrence

Put $p_{-1}=y$, $p_0=x$, and $$p_n=p_{n-1}^2-4-p_{n-2}.$$ Then $H^n=(p_n,p_{n-1})$. Induction shows that $p_n$ has degree $2^n$ and unique monic leading term $x^{2^n}$: squaring $p_{n-1}$ supplies that term, whereas the remaining terms have lower degree.

For completeness, set $P_k=Z^{2^k}p_k(X/Z,Y/Z)$ and $d=2^n$. The projective representative of $H^n$ is $$[P_n:P_{n-1}Z^{d/2}:Z^d].$$ Its first coordinate contains $X^d$ and is not divisible by $Z$, while every common factor would have to divide the third coordinate $Z^d$. The triple therefore has gcd one. Consequently $$\deg \bar H^n=2^n=(\deg\bar H)^n,\qquad
 \lambda_1(\bar H)=\lim_{n\to\infty}\deg(H^n)^{1/n}=2.$$ Thus $\bar H$ is algebraically stable at every order, independently of the finite replay cutoff. The exact replay prefix is shown in Table [1](#tab:degrees){reference-type="ref" reference="tab:degrees"}.

::: {#tab:degrees}
        $n$         1   2   3   4    5    6     7     8
  ---------------- --- --- --- ---- ---- ---- ----- -----
     $\deg p_n$     2   4   8   16   32   64   128   256
   $\deg p_{n-1}$   1   2   4   8    16   32   64    128

  : Nonexpanded recursive degree certificate.
:::

# Exact low-period witnesses

A fixed point has $x=y=q$ and $q^2-2q-4=0$, giving $$(q,q)=(1+\sqrt5,1+\sqrt5),\quad(1-\sqrt5,1-\sqrt5).$$ There is also the primitive real cycle $$(0,-2)\longmapsto(-2,0)\longmapsto(0,-2).$$ For $B(x)=\bigl(\begin{smallmatrix}2x&-1\\1&0\end{smallmatrix}\bigr)$, its monodromy based at $(0,-2)$ is $$B(-2)B(0)=\begin{pmatrix}-1&4\\0&-1\end{pmatrix},\quad
 \operatorname{tr}=-2,\quad\det=1,$$ and $\det(I-zB(-2)B(0))=(1+z)^2$.

The witness also fixes the parameter. For $H_c(x,y)=(x^2+c-y,x)$, each proposed transition has residual $(c+4,0)$. Thus $c=-3$ and $c=-5$ give nonzero residuals $(1,0)$ and $(-1,0)$, respectively, rather than preserving this cycle.

# Scope

The evidence stores an exact recurrence DAG, sparse leading certificates, and integer probes through $n=8$, avoiding full expansion at degree $256$. An independent checker reconstructs the complete ledger; a fresh SymPy program passes 97 identities, canonical replay fixes the bytes, and all sixteen hostile edits are rejected. Fixed-date isolated PDF builds agree bytewise and all fonts are embedded.

The all-order degree law, fixed points, and single primitive cycle support only A1 weak: no prime-like orbit-to-target correspondence or complete atlas is present. No weighted dynamical zeta, target divisor, or transfer owner exists, so A2 fails. No functional equation, Gamma-factor treatment, counting law, controlled continuation, or analytic bridge exists, so A3 fails; no natural lift is supplied, so A4 fails. In the repository evaluator vocabulary,

`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`, `ROUTE_A_EXPLORATORY`.

The algebraic dynamical degree is not promoted to entropy, and we make no claim about arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya, Riemann zeros, or Route B. The release scope is the literal

`NO_BAD_EULER_OR_ROOT_NUMBER`.
