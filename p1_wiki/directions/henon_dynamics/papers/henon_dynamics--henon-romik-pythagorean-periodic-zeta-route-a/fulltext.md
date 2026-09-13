---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-romik-pythagorean-periodic-zeta-route-a"
canonical_tex: "henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a/paper/main.pdf"
source_sha256: "d7ae558eb41f348be2cb509833e35e12d7c46f17b18ac4ad46964de76e6582c0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Terminating Pythagorean Trees and the Periodic Zeta of the Romik Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_romik_pythagorean_periodic_zeta_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove a convention-complete split theorem for the Romik three-branch map. Reduced rational parameters with opposite parity terminate at $1/2$ and form the unique $(a\text{ odd},b\text{ even})$ Barning tree rooted at $(3,4,5)$; leg swap is a separate orientation terminating at $1/3$. On the invariant irrational set, every length-$n$ word except the pure $1$ and pure $3$ parabolic words has one quadratic-irrational fixed point. Hence $\#\operatorname{Fix}(T^n)=3^n-2$, Möbius inversion gives every primitive count, and the source Artin--Mazur zeta is $(1-z)^2/(1-3z)$. Word matrices also give exact orientation and multipliers. A 9,840-word finite ledger audits the formulas. The terminating arithmetic states and periodic states are disjoint, so no rational-prime orbit law or target-zeta claim follows.
author:
- Anonymous
date: 3 September 2026
title: Terminating Pythagorean Trees and the Periodic Zeta of the Romik Map
```

## Markdown 正文

#### Revision certificate.

Parity-oriented rational descent and the unique Pythagorean tree. Quadratic periodic atlas, primitive counts, and source zeta. Exact word evidence and the Route-A separation boundary.

# Frozen map and orientations

For $0<t<1$, put $$D(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),\qquad
 T(t)=\begin{cases}
 t/(1-2t),&0<t<1/3,\\
 1/t-2,&1/3<t<1/2,\\
 2-1/t,&1/2<t<1.
 \end{cases}$$ The branch images are open. We declare $1/2$ the primary terminal for the odd-first/even-second triple $(3,4,5)$, while $1/3$ is the terminal for the leg-swapped $(4,3,5)$ orientation. Neither endpoint belongs to the periodic space $X=\{t\in(0,1):t\notin\mathbb Q\}$. The inverse branches are $$F_1(t)=\frac{t}{1+2t},\qquad F_2(t)=\frac1{2+t},\qquad
 F_3(t)=\frac1{2-t},$$ with images $(0,1/3),(1/3,1/2),(1/2,1)$.

[\[thm:main\]]{#thm:main label="thm:main"} The three Barning matrices $$M_1=\begin{pmatrix}-1&2&2\\-2&1&2\\-2&2&3\end{pmatrix},\quad
M_2=\begin{pmatrix}1&2&2\\2&1&2\\2&2&3\end{pmatrix},\quad
M_3=\begin{pmatrix}1&-2&2\\2&-1&2\\2&-2&3\end{pmatrix}$$ give every primitive Pythagorean triple with first leg odd and second leg even exactly once as $M_{w_1}\cdots M_{w_n}(3,4,5)^t$ for a possibly empty finite word $w$; the empty word owns the root $(3,4,5)$. For every $n\ge1$, every word $w\in\{1,2,3\}^n$ except $1^n,3^n$ has one fixed point $t_w$ in its open inverse cylinder, and these are exactly $\operatorname{Fix}(T^n|X)$. They are quadratic irrational, and $$\#\operatorname{Fix}(T^n|X)=3^n-2,\qquad
 E_n=\sum_{d\mid n}\mu(d)(3^{n/d}-2),\qquad \pi_n=E_n/n,$$ where $E_n$ counts exact-period points and $\pi_n$ oriented cycles. Moreover $$\zeta_T(z)=\exp\!\left(\sum_{n\ge1}\frac{3^n-2}{n}z^n\right)
 =\frac{(1-z)^2}{1-3z}.$$ If $F_w(t)=(at+b)/(ct+d)$, then $t_w$ solves $ct^2+(d-a)t-b=0$, $\det F_w=(-1)^{\#_2(w)}$, and $$|(T^n)'(t_w)|=\rho(F_w)^2,\qquad
 \rho(F_w)=\frac{\operatorname{tr}F_w+
 \sqrt{(\operatorname{tr}F_w)^2-4\det F_w}}2.$$

# Rational descent and unique tree

Write $t=n/m$ in lowest terms. If $m>n>0$ have opposite parity, then $$(a,b,c)=(m^2-n^2,2mn,m^2+n^2)$$ is primitive with $a$ odd and $b$ even, and $D(t)=(a/c,b/c)$. Conversely, for such a primitive triple, $(c+a)/2$ and $(c-a)/2$ are coprime and have square product $(b/2)^2$; hence they are $m^2,n^2$, proving the unique Euclid parameters.

The inverse branches replace $(m,n)$ by $$(m+2n,n),\qquad(2m+n,m),\qquad(2m-n,m).$$ Substitution in the three quadratic formulas gives exactly multiplication by $M_1,M_2,M_3$. Coprimality and opposite parity persist. In the forward direction the three branches give $$\frac n{m-2n},\qquad\frac{m-2n}{n},\qquad\frac{2n-m}{n};$$ each new denominator is smaller than $m$. Opposite parity excludes the $1/3$ terminal, so descent ends at $1/2$. Disjoint branch intervals make each removed digit unique. This proves the primary tree; leg swap remains a separate mirror orientation.

\>0

# Periodic-word lemma and zeta

The words $1^n$ and $3^n$ have only the boundary fixed points $0$ and $1$. Every other $F_w$ is a strict contraction of $[0,1]$ into an interior subinterval and has one quadratic-irrational fixed point in its cylinder.

The derivative magnitudes of the inverse branches are $(1+2t)^{-2},(2+t)^{-2},(2-t)^{-2}$. Equality with one is possible only for $F_1$ at zero or $F_3$ at one; $|F_2'|\le1/4$. Thus a nonpure composition maps $[0,1]$ into $(0,1)$ and has derivative supremum below one. The contraction theorem gives one fixed point. The pure powers satisfy $F_{1^n}(t)=t/(1+2nt)$ and, by reflection, the analogous formula at one.

For $F_w=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})$, the fixed equation is $ct^2+(d-a)t-b=0$. Its derivative is $\det(F_w)/(ct+d)^2$. Every branch denominator is positive on $[0,1]$; the denominator cocycle therefore gives $ct_w+d>0$. At the attracting point this is an eigenvalue $\lambda>1$, while the other is $\det(F_w)/\lambda$. Thus the trace is $\lambda+\det(F_w)/\lambda>0$, the displayed positive square-root formula is exactly $\rho(F_w)=\lambda$, and the matrix discriminant is positive. If it were square, determinant $1$ would factor $\operatorname{tr}^2-r^2=4$ and force the parabolic trace two; determinant $-1$ would factor $r^2-\operatorname{tr}^2=4$ and force trace zero. Both contradict strict contraction. The fixed point is quadratic irrational.

Equal-length cylinders are disjoint, so their fixed points are distinct. Every point of $\operatorname{Fix}(T^n|X)$ has one itinerary and is fixed by its inverse word. Removing the two parabolic words gives $3^n-2$. Since fixed points partition by exact period, Möbius inversion gives $E_n$ and division by $n$ gives $\pi_n$. Finally $$\sum_{n\ge1}(3^n-2)z^n/n=-\log(1-3z)+2\log(1-z),$$ which proves the source zeta. The eigenvector identity $F_w(t_w,1)^t=(ct_w+d)(t_w,1)^t$ and the derivative formula give the stated multiplier. Matrix powers make logarithmic instability additive under word repetition. A word with an odd number of digit $2$ reverses orientation and is not silently treated as a $PSL_2$ element.

\>1

# Exact evidence, ownership, and Route A

The exact ledger contains all 9,840 nonempty words through depth eight: 9,824 hyperbolic rows and 16 pure parabolic boundary rows. For each it records the Pythagorean triple, Möbius matrix, cylinder, fixed quadratic, determinant, trace, discriminant, least word period, and multiplier. Independent reconstruction checks all triples for positivity, primitivity, parity, Pythagorean identity, global uniqueness, and strict rational descent. Count rows continue through $n=12$. This finite evidence audits the formulas; the proof owns the infinite theorem.

Romik's primary paper owns the map, Barning address, irrational coding, and its relation as a factor of a $\Gamma(2)$ geodesic-flow cross-section. This package makes a source-local reconstruction and no priority claim. Nearby local owners cover generic Möbius transfer operators, rational square billiards, Markoff descent, and the Lüroth map, not this parity-normalized split theorem.

The Pythagorean relation earns only A0 weak: rational arithmetic states terminate, whereas periodic states are quadratic irrational. The complete periodic atlas earns A1 analytic. The source Artin--Mazur zeta is not a target Euler factor, divisor, functional equation, zero match, or RH statement. The $\Gamma(2)$ factor supplies only an A4 formal hint here, not automorphy or a Hilbert--Pólya operator. Route B is not invoked.

#### Verified source.

D. Romik, "The dynamics of Pythagorean triples," *Trans. Amer. Math. Soc.* 360 (2008), 6045--6064; DOI [10.1090/S0002-9947-08-04467-X](https://doi.org/10.1090/S0002-9947-08-04467-X); [arXiv:math/0406512](https://arxiv.org/abs/math/0406512).
