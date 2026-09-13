---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mobius-bergman-trace-route-a"
canonical_tex: "henon_dynamics/henon_mobius_bergman_trace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mobius_bergman_trace_route_a/paper/main.pdf"
source_sha256: "efd8d5fe72d1223525c17d934d0eae878e1d2c9d68b8c71fcb9bb6e12f8879c0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Trace-Class Bergman Fredholm Product for an Order-Sensitive Möbius Iterated System

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mobius_bergman_trace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mobius_bergman_trace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mobius_bergman_trace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mobius_bergman_trace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the nonlinear branches $\phi_a(z)=1/(a+z)$ for $a\in\{3,6\}$ on the unit disk. Their closed images are strictly separated, and the unweighted composition sum on normalized Bergman space is trace class with an explicit norm bound. Every word has a unique fixed point, a quadratic-algebraic multiplier read from an integer Möbius matrix, and an exact composition trace. These identities give an all-period trace formula and a primitive Fredholm product. Two non-cyclic same-count words have different multipliers and traces, repairing common-linear affine location blindness by intrinsic nonlinear order. The construction is dynamical and does not supply arithmetic Euler factors or a target spectral match.
author:
- 'Hénon Route-A Working Series, C132'
date: 24 August 2026
title: |
  A Trace-Class Bergman Fredholm Product\
  for an Order-Sensitive Möbius Iterated System
```

## Markdown 正文

# Progress over the prior gate

For a common-linear affine alphabet, determinant weights can collapse a word to symbol populations: rearranging positions while preserving counts then changes no weight. Here matrix multiplication is noncommutative and the branch images are geometrically separated. The source itself therefore retains cyclic order; no external phase label is appended.

# Frozen disk geometry and trace class

Let $\mathbb D=\{z:|z|<1\}$ and let $A^2(\mathbb D)$ use normalized area measure, so $e_n(z)=\sqrt{n+1}z^n$ is orthonormal. Define $$\phi_a(z)=\frac1{a+z}\quad(a=3,6),\qquad
 \mathcal L=C_{\phi_3}+C_{\phi_6},\qquad C_\phi f=f\circ\phi.$$ The image of the closed disk under $\phi_a$ is the disk $$\overline{\mathbb D}\!\left(\frac{a}{a^2-1},\frac1{a^2-1}\right).$$ Thus the respective centers and radii are $(3/8,1/8)$ and $(6/35,1/35)$; the largest image moduli are $1/2$ and $1/5$, and the closed-image gap is $$\frac38-\frac18-\frac6{35}-\frac1{35}=\frac1{20}.$$ Moreover $\sup_{\mathbb D}|\phi_a'|\le(a-1)^{-2}$, giving $1/4$ and $1/25$.

[\[thm:nuclear\]]{#thm:nuclear label="thm:nuclear"} The operator $\mathcal L$ is trace class on $A^2(\mathbb D)$ and $\|\mathcal L\|_1\le89/16$.

The Bergman expansion gives the rank-one representation $$C_{\phi_a}f=\sum_{n\ge0}\langle f,e_n\rangle
 \sqrt{n+1}\,\phi_a^n.$$ Each coefficient functional has norm one. If $\sup|\phi_a|\le r_a$, then $\|\sqrt{n+1}\phi_a^n\|_{A^2}\le\sqrt{n+1}r_a^n$. Hence the nuclear series converges; the deliberately coarse inequality $\sqrt{n+1}\le n+1$ gives $$\|\mathcal L\|_1\le\sum_{n\ge0}(n+1)2^{-n}
 +\sum_{n\ge0}(n+1)5^{-n}=4+\frac{25}{16}=\frac{89}{16}.$$

# All-word fixed points and traces

Put $M_a=\left(\begin{smallmatrix}0&1\\1&a\end{smallmatrix}\right)$. For $w=a_1\cdots a_n$, let $$\Phi_w=\phi_{a_1}\circ\cdots\circ\phi_{a_n},\qquad
 M_w=M_{a_1}\cdots M_{a_n}=
 \begin{pmatrix}A&B\\C&D\end{pmatrix}.$$ This matrix convention represents the displayed function composition. Composition operators reverse it: $C_{\phi_{a_1}}\cdots C_{\phi_{a_n}}
=C_{\phi_{a_n}\circ\cdots\circ\phi_{a_1}}$. Reversal is a bijection on all length-$n$ words and will be relabelled only when summing them. Each word is a strict contraction of the closed disk and therefore has one fixed point in $\mathbb D$.

[\[thm:word\]]{#thm:word label="thm:word"} Let $t=\operatorname{tr}M_w$, $\delta=\det M_w=(-1)^n$, and $\Delta=t^2-4\delta$. Then $$z_w=\frac{A-D+\sqrt\Delta}{2C},\qquad
 \lambda_w=\Phi_w'(z_w)=\frac{t-\sqrt\Delta}{t+\sqrt\Delta},$$ and $$\operatorname{Tr}C_{\Phi_w}=\frac1{1-\lambda_w}
 =\frac12+\frac{t}{2\sqrt\Delta}.$$

The fixed equation is $Cz^2+(D-A)z-B=0$, whose discriminant is $(D-A)^2+4BC=t^2-4\delta$. Contraction selects the displayed root in $\mathbb D$. Also $Cz_w+D=(t+\sqrt\Delta)/2$ and $\Phi_w'(z_w)=\delta/(Cz_w+D)^2$, which gives the multiplier.

Conjugate $z_w$ to zero by a disk automorphism. The induced composition operator is bounded and invertible on Bergman space. The conjugated symbol has form $\lambda_wz+O(z^2)$, so its monomial matrix is triangular with diagonal $1,\lambda_w,\lambda_w^2,\ldots$. The word operator is trace class: it is a product of a trace-class branch operator with bounded composition operators. Trace invariance under bounded similarity now gives the stated geometric sum.

# All periods and primitive product

Expanding $\mathcal L^n$ and applying Theorem [\[thm:word\]](#thm:word){reference-type="ref" reference="thm:word"} yields, for every $n\ge1$, $$\operatorname{Tr}\mathcal L^n=\sum_{|w|=n}\frac1{1-\lambda_w}. \tag{1}$$ Here equation (1) uses the reversal bijection just stated; it is not a termwise identification of the two order conventions. For primitive cyclic words $[p]$, regrouping the Fredholm logarithm gives $$\det(I-z\mathcal L)=\prod_{[p]}\prod_{k\ge0}
 (1-z^{|p|}\lambda_p^k). \tag{2}$$ The factor is well defined on $[p]$: cyclic rotation preserves the trace and determinant of the matrix product and therefore preserves $\lambda_p$. Indeed, a repetition $p^r$ has $|p|$ rooted rotations and multiplier $\lambda_p^r$, while $(1-\lambda_p^r)^{-1}=\sum_{k\ge0}\lambda_p^{rk}$. Thus its logarithmic contribution is $$-\sum_{r\ge1}\frac{z^{r|p|}}{r(1-\lambda_p^r)}
 =\sum_{k\ge0}\log(1-z^{|p|}\lambda_p^k).$$ Because there are at most $2^\ell/\ell$ primitive cycles of length $\ell$ and the chain-rule contraction bound gives $|\lambda_p|\le4^{-\ell}$, the sum of the absolute factor arguments is dominated by a constant times $\sum_{\ell\ge1}(2|z|)^\ell/\ell$. Hence the raw product is absolutely convergent for $|z|<1/2$. The logarithmic regrouping is initially valid near $z=0$; analyticity and the identity theorem extend the equality throughout that disk. The left side is entire by Theorem [\[thm:nuclear\]](#thm:nuclear){reference-type="ref" reference="thm:nuclear"}; this analytic continuation does not assert that the displayed raw factors converge outside their proved disk.

# Intrinsic order control and exact receipt

The words $33366$ and $33636$ have three digits $3$ and two digits $6$, but are not cyclic rotations: the rotations of the first are $33366,33663,36633,66333,63336$. Exact multiplication gives $$M_{33366}=\begin{pmatrix}63&388\\208&1281\end{pmatrix},\qquad
 M_{33636}=\begin{pmatrix}60&379\\199&1257\end{pmatrix}.$$ Both determinants are $-1$, whereas their traces are $1344$ and $1317$. For positive $t$, the trace weight is $1/2+t/(2\sqrt{t^2+4})$. Equality of two such weights, after squaring, would force $t_1^2(t_2^2+4)=t_2^2(t_1^2+4)$ and hence $t_1=t_2$. Thus these distinct positive traces force distinct composition traces and, because the weight is $(1-\lambda)^{-1}$, distinct multipliers.

The receipt enumerates every rooted word through period ten: $$\begin{array}{c|rrrrrrrrrr}
 n&1&2&3&4&5&6&7&8&9&10\\ \hline
 \text{rooted}&2&4&8&16&32&64&128&256&512&1024\\
 \text{primitive}&2&1&2&3&6&9&18&30&56&99
\end{array}$$ Thus 2,046 word cases and 226 primitive classes are represented. An independent checker reconstructs each integer matrix and ledger digest; 2,561 separate symbolic checks, byte replay, 36 repaired-hash semantic mutations, and one stale-hash mutation test the same claims.

# Strict Route-A boundary

The exact separated dynamics, trace-class owner, and all-period Fredholm identity justify $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL}).$$ There is no arithmetic Euler product, prime or zero table, root number, functional equation, target divisor match, automorphy, self-adjoint lift, or Hilbert--Pólya claim. Route B is unauthorized. The active scope is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$

# Conclusion

C132 replaces position-blind common-linear weights by an intrinsically order-sensitive nonlinear system and gives its trace-class determinant at all periods. Relating that dynamical determinant to any external target is a separate, currently unsupported problem.
