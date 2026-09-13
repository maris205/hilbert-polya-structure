---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-free-group-kesten-random-walk-route-a"
canonical_tex: "henon_dynamics/henon_free_group_kesten_random_walk_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_free_group_kesten_random_walk_route_a/paper/main.pdf"
source_sha256: "aa31ff42697b5101923fe154f80af4eba527ab3f6db52ad955ff507101c7bb21"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Uniform Walk on a Free Group: Kesten Measure, Exact Excursions, and Radial Escape

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_free_group_kesten_random_walk_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_free_group_kesten_random_walk_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_free_group_kesten_random_walk_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_free_group_kesten_random_walk_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For simple random walk on the rank-$d$ free group, we give a single finite-to-infinite theorem joining operator spectrum, exact returns, and radial escape. With $D=2d$, the Markov operator has purely absolutely continuous spectrum $[-2\sqrt{D-1}/D,2\sqrt{D-1}/D]$ and root density $\sqrt{4(D-1)-D^2x^2}/[2\pi(1-x^2)]$. Weighted Dyck decomposition gives closed formulas for every even return and first return, including total return probability $1/(D-1)$. A pathwise boundary-flip coupling then proves speed $(D-2)/D$ and radial central-limit variance $4(D-1)/D^2$. The rank-one boundary becomes the recurrent walk on $\mathbb Z$, with arcsine spectrum and half-normal radial scaling. A 1,997-row exact certificate is a regression receipt, not a substitute for the all-time proofs. We claim neither priority nor an arithmetic-target interpretation.
author:
- 'HCS-C355 source-local reconstruction'
date: 3 September 2026
title: |
  The Uniform Walk on a Free Group:\
  Kesten Measure, Exact Excursions, and Radial Escape
```

## Markdown 正文

**Revision certificate.** =0 Kesten resolvent, root spectral law, radial chain, and exact even-return closure. =1 Round-one full-space Haar--Jacobi pure-AC proof and first-return closure. Round-two escape laws, rank-one boundary, evidence, and Route-A closure.

# Frozen walk and complete theorem

Let $F_d=\langle a_1,\ldots,a_d\rangle$, $d\ge2$, and put $D=2d$. Starting from the identity $o$, multiply on the right at each step by one element of $\{a_i,a_i^{-1}:1\le i\le d\}$, uniformly. Its Cayley graph is the $D$-regular tree $T_D$. On $\ell^2(T_D)$ the transition operator is the bounded self-adjoint operator $$(Pf)(v)=D^{-1}\sum_{w\sim v}f(w).$$ Write $R_n=|X_n|$ for reduced-word length, and let $u_n=\mathbb P_o(X_n=o)$. Set $\rho=2\sqrt{D-1}/D$ and $C_m=(m+1)^{-1}\binom{2m}{m}$.

[\[thm:main\]]{#thm:main label="thm:main"} For the frozen walk:

1.  $P$ is purely absolutely continuous and $\operatorname{spec}(P)=[-\rho,\rho]$. The spectral measure at $o$ has density $$k_D(x)=\frac{\sqrt{4(D-1)-D^2x^2}}{2\pi(1-x^2)}
     \mathsf{1}_{\{|x|<\rho\}}.                                      \label{eq:density}$$ Equivalently, for $z\notin[-\rho,\rho]$ and the branch $\sqrt{z^2-\rho^2}\sim z$ at infinity, $$\langle\delta_o,(z-P)^{-1}\delta_o\rangle
     =\frac{D\sqrt{z^2-\rho^2}-(D-2)z}{2(z^2-1)}.             \label{eq:resolvent}$$

2.  $R_0=0$, $R_{n+1}=1$ from $R_n=0$, while for $r\ge1$, $$\mathbb P(R_{n+1}=r+1\mid R_n=r)=p=\frac{D-1}{D},\qquad
     \mathbb P(R_{n+1}=r-1\mid R_n=r)=q=\frac1D.                   \label{eq:radial}$$ All odd returns vanish and, for $n\ge1$, $$u_{2n}=D^{-2n}\sum_{k=1}^{n}
     \frac{k}{2n-k}\binom{2n-k}{n}D^k(D-1)^{n-k}.             \label{eq:returns}$$

3.  If $\tau_o^+=\inf\{n\ge1:X_n=o\}$, then $$\mathbb P_o(\tau_o^+=2k)=\frac{C_{k-1}(D-1)^{k-1}}{D^{2k-1}},
     \qquad \mathbb P_o(\tau_o^+<\infty)=\frac1{D-1}.               \label{eq:firstreturn}$$

4.  With $v=(D-2)/D$ and $\sigma^2=4(D-1)/D^2$, $$\frac{R_n}{n}\longrightarrow v\quad\text{a.s.},\qquad
     \frac{R_n-vn}{\sqrt n}\Longrightarrow N(0,\sigma^2).     \label{eq:escape}$$

5.  At the excluded rank-one boundary $d=1$, $F_1\cong\mathbb Z$: $P$ is purely absolutely continuous on $[-1,1]$ with arcsine density, $u_{2n}=4^{-n}\binom{2n}{n}$, return is recurrent, $R_n/n\to0$ a.s., and $R_n/\sqrt n\Rightarrow |N(0,1)|$.

# Cavity resolvent and the root measure

Delete the edge from a vertex to its parent and let $h(z)$ be the diagonal resolvent of the resulting rooted forward tree. Schur complementation at the root of that tree and then at $o$ gives $$h=\frac1{z-(D-1)h/D^2},\qquad
 G_o(z)=\frac1{z-h/D}.                                    \label{eq:cavity}$$ The solution satisfying $h(z)\sim z^{-1}$ is $$h(z)=\frac{D^2}{2(D-1)}\bigl(z-\sqrt{z^2-\rho^2}\bigr).$$ Substitution and rationalization prove [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"}. For $|x|<\rho$, the upper boundary value has $$-\pi^{-1}\operatorname{Im}G_o(x+i0)
 =\frac{D\sqrt{\rho^2-x^2}}{2\pi(1-x^2)}=k_D(x).$$ The apparent singularities at $z=\pm1$ in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} are removable: the numerator vanishes there with the branch fixed above. There are therefore no exterior atoms. Stieltjes inversion gives [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} on the open band. Its integral is one (substitute $x=\rho\cos\theta$ and evaluate the resulting rational sine integral), while the square-root endpoints have no poles. Thus no singular-continuous or endpoint mass remains. The independent asymptotic check $zG_o(z)\to1$ confirms the total normalization. Hence [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} is the full probability measure of the cyclic root vector in the radial subspace.

# Weighted Dyck paths and exact returns

Distance from $o$ changes by one. From a positive radius, precisely one letter cancels the last reduced letter and $D-1$ extend it; at radius zero all $D$ letters lead to radius one. This proves [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}. A return of length $2n$ is thus a Dyck path with $n$ rises and $n$ falls. Suppose it has exactly $k$ irreducible excursions from zero. Its $k$ rises from zero have $D$ choices each; the remaining $n-k$ rises have $D-1$ choices, and every fall is forced.

It remains to count the paths. If $C(t)=1+tC(t)^2$ is the Catalan series, the required number is $[t^{n-k}]C(t)^k$. Lagrange inversion gives $$C(t)^k=\frac{k}{2n-k}\binom{2n-k}{n}.            \label{eq:lagrange}$$ Multiplying [\[eq:lagrange\]](#eq:lagrange){reference-type="eqref" reference="eq:lagrange"} by $D^k(D-1)^{n-k}$, summing over $k$, and dividing by $D^{2n}$ proves [\[eq:returns\]](#eq:returns){reference-type="eqref" reference="eq:returns"}. This also proves the renewal identity $u_{2n}=\sum_{k=1}^n\mathbb P(\tau_o^+=2k)u_{2n-2k}$ directly at word-count level.

\>0

# Why the whole operator is purely absolutely continuous

The root measure alone controls only radial functions, so we record the complete orthogonal decomposition. Let $S_m$ be the sphere of radius $m$ and let $\phi_m=|S_m|^{-1/2}\mathsf{1}_{S_m}$. The radial subspace generated by $\phi_0$ reduces $P$ and has Jacobi matrix $$J_0=J(0;a_0,a,a,\ldots),\qquad
 a_0=D^{-1/2},\quad a=\frac{\sqrt{D-1}}D.                 \label{eq:radialjacobi}$$ It is cyclic at its first coordinate, so [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"}--[\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"}, including the absence of singular mass, show that $J_0$ is purely absolutely continuous on $[-2a,2a]$.

For every vertex $v$, let ${\rm Ch}(v)$ be its children relative to $o$, and choose an orthonormal basis of the zero-sum space $$E_v=\{\eta\in\ell^2({\rm Ch}(v)):\sum_{w\in{\rm Ch}(v)}\eta(w)=0\}.$$ Its dimension is $D-1$ when $v=o$ and $D-2$ otherwise. Given $\eta\in E_v$, let $e_j^{v,\eta}$, $j\ge0$, assign to every descendant at depth $j$ below ${\rm Ch}(v)$ the value of its first child divided by $(D-1)^{j/2}$, and vanish elsewhere. These vectors are orthonormal, the zero-sum condition cancels the edge back to $v$, and direct substitution gives $$Pe_0^{v,\eta}=ae_1^{v,\eta},\qquad
 Pe_j^{v,\eta}=a(e_{j-1}^{v,\eta}+e_{j+1}^{v,\eta})\quad(j\ge1).
                                                               \label{eq:freejacobi}$$ For clarity, $e_0^{v,\eta}=\eta$ and the displayed normalization at depth $j$ uses $(D-1)^{-j/2}$.

These half-line spaces and the radial space are mutually orthogonal. They are complete: on every finite rooted truncation, recursively split the values on each sibling set into its mean and zero-sum parts; induction on the outermost occupied level exhausts every finitely supported vector. Density then exhausts $\ell^2(T_D)$. Thus $P$ is an orthogonal direct sum of $J_0$ and copies of the free half-line Jacobi matrix $J(0;a,a,\ldots)$. The latter is carried by the sine transform to multiplication by $2a\cos\theta$ on $L^2(0,\pi)$, hence is purely absolutely continuous with spectrum $[-2a,2a]$. This proves the full-space assertion in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(i), without extrapolating from one spectral measure.

# First return and transience

A first return at time $2k$ is one irreducible Dyck excursion. Removing its first rise and last fall leaves one of $C_{k-1}$ Dyck paths. The first rise has $D$ choices, the other $k-1$ rises have $D-1$ choices, and falls are forced. Hence the word count is $DC_{k-1}(D-1)^{k-1}$, proving the first formula in [\[eq:firstreturn\]](#eq:firstreturn){reference-type="eqref" reference="eq:firstreturn"}. With $p=(D-1)/D$ and $q=1/D$, the Catalan generating function yields $$\sum_{k\ge1}C_{k-1}p^{k-1}q^k
 =\frac{1-\sqrt{1-4pq}}{2p}=\frac qp=\frac1{D-1},$$ because $p>q$. The missing mass is escape, not an uncounted finite return.

\>1

# Escape strong law and central limit theorem

The boundary at zero requires an explicit coupling. Let $\xi_1,\xi_2,\ldots$ be i.i.d. with $\mathbb P(\xi_i=1)=p$ and $\mathbb P(\xi_i=-1)=q$, and recursively set $$\widehat R_{n+1}=\widehat R_n+\xi_{n+1}
 +2\mathsf{1}_{\{\widehat R_n=0,\,\xi_{n+1}=-1\}},\qquad \widehat R_0=0.
                                                               \label{eq:coupling}$$ This chain has exactly [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}, so it has the law of $R$. From radius one the probability of hitting zero is $q/p$: solve the bounded gambler's-ruin recurrence $h_r=ph_{r+1}+qh_{r-1}$ with $h_0=1$ and $h_r\to0$. After every departure from zero, the strong Markov property therefore gives fixed escape probability $1-q/p>0$. The number of returns, and hence the number $$B_\infty=\sum_{n\ge0}\mathsf{1}_{\{\widehat R_n=0,\,\xi_{n+1}=-1\}},$$ is finite almost surely. Iterating [\[eq:coupling\]](#eq:coupling){reference-type="eqref" reference="eq:coupling"} gives $$\widehat R_n=\sum_{i=1}^n\xi_i+2B_n,\qquad B_n\uparrow B_\infty<\infty.
                                                               \label{eq:correction}$$ The i.i.d. strong law and central limit theorem now apply to the first term; the finite correction divided by $n$ or $\sqrt n$ vanishes. Since $\mathbb E\xi_i=p-q=(D-2)/D$ and $\operatorname{Var}\xi_i=4pq=4(D-1)/D^2$, [\[eq:escape\]](#eq:escape){reference-type="eqref" reference="eq:escape"} follows. Equation [\[eq:correction\]](#eq:correction){reference-type="eqref" reference="eq:correction"} is also why no conditioning-on-the-last-return gap is hidden in the CLT.

# Rank-one boundary, exact receipt, and scope

When $d=1$ and $D=2$, the Cayley graph is $\mathbb Z$. Fourier transform takes $P$ to multiplication by $\cos\theta$, giving the arcsine density $[\pi\sqrt{1-x^2}]^{-1}$ on $[-1,1]$. Direct word counting gives $u_{2n}=4^{-n}\binom{2n}{n}$; its divergence criterion or the symmetric gambler's-ruin limit gives recurrence. Here $R_n$ has the law of the absolute value of symmetric walk, so the strong law and invariance principle give $R_n/n\to0$ a.s. and $R_n/\sqrt n\Rightarrow|N(0,1)|$. Thus [\[eq:escape\]](#eq:escape){reference-type="eqref" reference="eq:escape"} is not silently continued through the critical boundary.

The exact receipt uses $D\in\{4,6,8,10\}$: 1,156 radial-DP rows through time 32, 260 return rows, 256 first-return rows, 256 renewal rows, four parameter rows, and 65 rank-one rows, totaling 1,997 rows and 9,483 scalar cells. An independent implementation checks every row; 237 symbolic identities, two isolated byte replays, and 74 hostile mutations form separate gates. Finite computation proves none of the pure-AC, infinite-sum, strong-law, or CLT statements; the preceding arguments do.

Kesten's original article establishes the symmetric group-walk and free-group spectral-radius lineage [@kesten]; the AMS DOI and JSTOR DOI listed below identify that same article, not two independent sources. Woess provides an authoritative graph-and-group random-walk monograph lineage [@woess]. We make no priority claim; the contribution here is a source-local, normalization-locked reconstruction joining the results and their boundaries.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ The last entry records only that $P$ is a natural self-adjoint operator. The rank and clock have no structural arithmetic origin, closed random words are not primitive arithmetic orbits, and [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} is not a target determinant. There is no target Euler product, divisor, functional equation, counting law, zero match, or Hilbert--Pólya claim. Route A is rejected and Route B is not invoked.

9 H. Kesten, "Symmetric random walks on groups," *Trans. Amer. Math. Soc.* 92 (1959), 336--354. [doi:10.1090/S0002-9947-1959-0109367-6](https://doi.org/10.1090/S0002-9947-1959-0109367-6); same record at [doi:10.2307/1993160](https://doi.org/10.2307/1993160).

W. Woess, *Random Walks on Infinite Graphs and Groups*, Cambridge Tracts in Mathematics 138, Cambridge University Press, 2000. [doi:10.1017/CBO9780511470967](https://doi.org/10.1017/CBO9780511470967).
