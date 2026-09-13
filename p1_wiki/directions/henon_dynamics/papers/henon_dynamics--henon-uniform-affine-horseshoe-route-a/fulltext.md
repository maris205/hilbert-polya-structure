---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-uniform-affine-horseshoe-route-a"
canonical_tex: "henon_dynamics/henon_uniform_affine_horseshoe_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_uniform_affine_horseshoe_route_a/paper/main.pdf"
source_sha256: "f31b842751b50fa9e296b041f801116e2ef9383dd50e6af665955e0a8390d78c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Parameter-Uniform Affine Hénon Horseshoe: Exact Coding, Stability Traces, and a Trace-Class Owner

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_uniform_affine_horseshoe_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_uniform_affine_horseshoe_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_uniform_affine_horseshoe_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_uniform_affine_horseshoe_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We exhibit a two-parameter family of piecewise-affine Hénon horseshoes for which the hyperbolic geometry, full-shift coding, every-period fixed-point weights, and a trace-class operator identity are uniform on an explicit rectangle. For $(\lambda,\mu)\in[3,4]\times[1/5,1/3]$, every based binary word of length $n$ determines exactly one periodic point and the weighted fixed-point sum is $$\frac{2^n}{(\lambda^n-1)(1-\mu^n)}.$$ We realize this sum as the $n$th trace of a natural stability-mode operator, derive its Fredholm product, prove a uniform zero-free disk $|z|<3/2$, and give explicit trace-norm Lipschitz constants across the whole parameter rectangle. The result closes a structural uniform-parameter gate; it does not compare the determinant with an external spectral target.
author:
- 'Hénon Route-A Working Series, C127'
date: 24 August 2026
title: |
  A Parameter-Uniform Affine Hénon Horseshoe:\
  Exact Coding, Stability Traces, and a Trace-Class Owner
```

## Markdown 正文

# Progress over the prior gate

The prior Hénon-track evidence included individual parameter witnesses and finite symbolic prefixes. Such evidence does not imply persistence on a region. Here the advance is a single theorem, with explicit constants, on a two-dimensional parameter rectangle. It simultaneously controls strip geometry, hyperbolicity, coding, all periods, a global Hilbert-space owner, and its determinant. No fitted target data enter the construction.

# The affine horseshoe

Let $\mathcal P=[3,4]\times[1/5,1/3]$. For $(\lambda,\mu)\in\mathcal P$, set $$R_0=[0,\lambda^{-1}]\times[0,1],\qquad
 R_1=[1-\lambda^{-1},1]\times[0,1]$$ and define, for $e\in\{0,1\}$, $$\label{eq:map}
 F_{\lambda,\mu}(x,y)=
 \bigl(\lambda x-(\lambda-1)e,\;\mu y+(1-\mu)e\bigr),
 \qquad (x,y)\in R_e.$$ Each vertical strip maps across the square into a horizontal strip. The domain gap is $1-2/\lambda\ge1/3$ and the image gap is $1-2\mu\ge1/3$. On either branch, $$DF_{\lambda,\mu}=\operatorname{diag}(\lambda,\mu),
 \qquad \lambda\ge3,\quad 0<\mu\le1/3.$$ Thus the coordinate cones are invariant with uniform expansion and contraction.

[\[thm:coding\]]{#thm:coding label="thm:coding"} The maximal two-sided invariant set of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is conjugate to the full two-shift. A based word $e_0\ldots e_{n-1}$ has exactly one periodic point, whose initial coordinates are $$\begin{aligned}
 x_0&=\frac{\lambda-1}{\lambda^n-1}
       \sum_{j=0}^{n-1}\lambda^{n-1-j}e_j,\label{eq:x}\\
 y_0&=\frac{1-\mu}{1-\mu^n}
       \sum_{j=0}^{n-1}\mu^{n-1-j}e_j.\label{eq:y}\end{aligned}$$ Consequently $\#\operatorname{Fix}(F^n)=2^n$, and the primitive-cycle count is $$p_n=\frac1n\sum_{d\mid n}\operatorname{mobius}(d)2^{n/d}.$$

Forward iteration of the first coordinate and backward determination of the stable coordinate give nested intervals whose diameters are bounded by $3^{-k}$. The strip gaps make distinct itineraries disjoint. Solving the two affine closure equations gives [\[eq:x\]](#eq:x){reference-type="eqref" reference="eq:x"}--[\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"}; these points remain in their prescribed strips by the same nested-interval construction. There are therefore $2^n$ based fixed points. Möbius inversion removes repetitions and cyclic rooting.

# A trace-class stability owner

At every $q\in\operatorname{Fix}(F^n)$, $$|\det(I-DF^n(q))|=(\lambda^n-1)(1-\mu^n).$$ We now obtain the resulting orbit sum as an actual operator trace. Let $$\mathcal H=\mathbb C^2\otimes
 \ell^2(\mathbb N_{\ge1}\times\mathbb N_0),\qquad
 J=\begin{pmatrix}1&1\\1&1\end{pmatrix},$$ and let $D_{\lambda,\mu}$ be diagonal with entry $\lambda^{-r}\mu^s$ at $(r,s)$. Define $K_{\lambda,\mu}=J\otimes D_{\lambda,\mu}$.

[\[thm:trace\]]{#thm:trace label="thm:trace"} The operator $K_{\lambda,\mu}$ is trace class, uniformly on $\mathcal P$, and $$\begin{aligned}
 \|K_{\lambda,\mu}\|_1
 &=\frac{2}{(\lambda-1)(1-\mu)}\le\frac32,\label{eq:norm}\\
 \operatorname{Tr}K_{\lambda,\mu}^n
 &=\frac{2^n}{(\lambda^n-1)(1-\mu^n)}
 =\sum_{q\in\operatorname{Fix}(F^n)}\frac1{|\det(I-DF^n(q))|}.
 \label{eq:trace}\end{aligned}$$

The nonzero eigenvalue of $J$ is $2$. Both geometric series in $$2\sum_{r\ge1}\lambda^{-r}\sum_{s\ge0}\mu^s$$ converge uniformly, proving [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}. Taking $n$th powers gives $\operatorname{Tr}J^n=2^n$ and $$\sum_{r\ge1}\lambda^{-nr}\sum_{s\ge0}\mu^{ns}
 =\frac1{(\lambda^n-1)(1-\mu^n)},$$ which is [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}.

# Uniform determinant control

Trace class makes the following product an ordinary Fredholm determinant: $$\label{eq:fredholm}
 \det(I-zK_{\lambda,\mu})
 =\prod_{r\ge1,\,s\ge0}
   \bigl(1-2z\lambda^{-r}\mu^s\bigr).$$ Its smallest-modulus zero is $z=\lambda/2$, so the determinant is zero-free for $|z|<\lambda/2$ and uniformly zero-free for $|z|<3/2$. The word "open" matters: at $\lambda=3$, the boundary point $z=3/2$ is a zero.

Differentiating the absolutely convergent diagonal series gives $$\|\partial_\lambda K\|_1\le\frac34,
 \qquad
 \|\partial_\mu K\|_1\le\frac94$$ on $\mathcal P$. Integration along a coordinate path yields $$\label{eq:lipschitz}
 \|K_{\lambda,\mu}-K_{\lambda',\mu'}\|_1
 \le\frac34|\lambda-\lambda'|+
      \frac94|\mu-\mu'|.$$ Equations [\[eq:fredholm\]](#eq:fredholm){reference-type="eqref" reference="eq:fredholm"}--[\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"} are global parameter statements, not neighboring-point numerical tests.

# Exact certificate and hostile controls

The release evidence uses rational arithmetic on a $3\times3$ parameter grid, checks periods through $12$, and replays representative words exactly. An independent implementation reconstructs every invariant. A separate SymPy program verifies the geometric-series and matrix identities, while sixteen semantic mutations test gaps, counts, traces, displayed periodic coordinates, scope flags, and route labels.

Three failure modes delimit the theorem. If $\lambda<2$, the domain strips can overlap; if $\mu>1/2$, the image strips can overlap. Replacing the stability denominator by $(\lambda\mu)^n$ is not a harmless convention: it breaks the trace identity. Finally, $2^n$ counts rooted words, not primitive cycles; the latter require Möbius inversion.

# Route-A assessment and limitations

The structural uniform-parameter subgate is certified. The strict canonical tuple is nevertheless $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ A2 and A3 remain failed because there is no frozen target-facing protocol, missing/extra-zero census, or target divisor comparison. The internal zeros of [\[eq:fredholm\]](#eq:fredholm){reference-type="eqref" reference="eq:fredholm"} must not be rebranded as arithmetic zeros. No natural quantization is constructed, and Route B is not authorized. The active scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Conclusion

This family supplies an explicit answer to a narrow but important Route-A question: exact orbit coding and a trace-class stability determinant can be made uniform on a genuine Hénon-style parameter region. The next separate task is target-facing validation under a future authorized protocol; it is not inferred from the present structural theorem.
