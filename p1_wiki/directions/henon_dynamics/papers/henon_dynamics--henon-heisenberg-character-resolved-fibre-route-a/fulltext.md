---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-heisenberg-character-resolved-fibre-route-a"
canonical_tex: "henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a/paper/main.pdf"
source_sha256: "c7159a7c6a322e04d1be2f340359fc1b04a9aa79424c8f1d338e42f8628d10bc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Central-Rotation-Resolved Fixed Fibres for a Heisenberg Nilmanifold Automorphism

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_heisenberg_character_resolved_fibre_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a frozen Heisenberg lattice automorphism, we derive the central rotation over every horizontal fixed class. Its zero level counts clean fixed circles, and a finite root-of-unity average gives the component count at every iterate. Exact rational histograms through iterate twelve distinguish horizontal fixed classes from actual components. This is a source-side clean-family result, not an isolated-orbit or target construction.
author:
- 'Route-A structural certificate C151'
title: |
  Central-Rotation-Resolved Fixed Fibres for a\
  Heisenberg Nilmanifold Automorphism
```

## Markdown 正文

# Fixed-fibre equation

On $N=\mathbb Z^3\backslash H$, use $$(x,y,z)(X,Y,Z)=(x+X,y+Y,z+Z+xY),\quad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},$$ and $\Phi(v,z)=(Av,z+q(v))$, where $q(x,y)=x(x-1)+xy+y(y-1)/2$. Put $B=A^n$, $M=B-I$, and $q_n(v)=\sum_{j=0}^{n-1}q(A^jv)$. The horizontal fixed classes are $\mathbb Z^2/M\mathbb Z^2$. If $m=Mv$, the left-quotient equation is $$(Bv,z+q_n(v))=(m_1,m_2,k)(v,z)
              =(v+m,z+k+m_1v_2).$$ It follows that the fibre rotation is $$\rho_n(v)=q_n(v)-m_1v_2\pmod 1,                 \tag{1}$$ and the fibre is fixed exactly when $\rho_n(v)=0$. The condition is independent of $z$, so a zero produces the whole central circle.

For completeness, this is representative invariant. Replace $v$ by $v+r$ with $r\in\mathbb Z^2$, put $s=Mr$, and use the automorphism identity $$q_n(v+r)-q_n(v)-q_n(r)=(Bv)_1(Br)_2-v_1r_2.$$ The change in (1) reduces to $q_n(r)+\det(v,s)+m_1s_2-s_1r_2$. Since $B$ preserves area, $\det(v+m,r+s)=\det(v,r)$, and the change becomes $$q_n(r)-m_1r_2+m_2r_1+s_1m_2-s_1r_2\in\mathbb Z.$$ Thus (1) is well-defined on the horizontal class. Along a fixed fibre, the derivative is block lower triangular with diagonal blocks $B$ and $1$. Since $I-B$ is invertible, $\ker(I-D\Phi^n)$ is exactly the central tangent, so the component is clean.

# Finite root-of-unity projector

Let $D_n=|\det M|$. The adjugate formula puts the coordinates of $v$ in $D_n^{-1}\mathbb Z$, while $q_n$ is quadratic with half-integral coefficients. Thus $\rho_n\in Q_n^{-1}\mathbb Z/\mathbb Z$ for $Q_n=2D_n^2$. Root-of-unity orthogonality gives $$C_n=\frac{1}{Q_n}\sum_{a=0}^{Q_n-1}
 \sum_{[m]\in\mathbb Z^2/M\mathbb Z^2}
e^{2\pi i a\rho_n(m)}.                           \tag{2}$$ Here $\rho_n$ is generally quadratic and is not asserted to be a homomorphism of the horizontal quotient. Equation (2) is only a central cyclic root-of-unity filter: the average over $a$ is one at rotation zero and zero at every other $Q_n$-torsion rotation.

# Exact certificate and boundary

The exact pairs $(D_n,C_n)$ through $n=12$ are $$\begin{array}{c|rrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
D_n&1&5&16&45&121&320&841&2205&5776&15125&39601&103680\\
C_n&1&1&4&1&21&4&57&1&148&105&397&144
\end{array}$$ The checker reconstructs every rotation through $n=12$ by exact direct cocycle iteration; a separate SymPy path rebuilds the first eight full histograms. In particular, the values $C_{10}=105$ and $C_{12}=144$ refute the simple Lucas/parity/modulo-three extrapolation suggested by earlier rows; no all-iterate closed form for $C_n$ is claimed.

The tuple is $(\texttt{A1\_FAIL},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT})$. Haar Koopman evolution is only a formal unitary hint. We claim no isolated primitive-orbit determinant, target divisor, target functional equation or counting law, arithmetic/local factor, Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
