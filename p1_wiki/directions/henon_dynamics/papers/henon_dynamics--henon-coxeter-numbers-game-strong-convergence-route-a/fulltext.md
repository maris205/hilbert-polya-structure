---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-coxeter-numbers-game-strong-convergence-route-a"
canonical_tex: "henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/paper/main.pdf"
source_sha256: "b99d086f70685bdda2dc5ab485440137a3198732f64f767a89779e047ff0f7d3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Strong Convergence in the Finite Coxeter Numbers Game: Parabolic Length and the Complete Boundary Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_coxeter_numbers_game_strong_convergence_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We fix a finite reduced crystallographic root system and fire a simple node only when its coroot coordinate is strictly positive. In the strictly dominant chamber, every legal play is a reduced word for the longest Weyl element and has $|\Phi^+|$ moves. \>0For an arbitrary dominant wall position, with $J$ its zero-coordinate set, we prove that every play ends at the same anti-dominant point, accumulates to $w_0w_J$, and has the exact common length $|\Phi^+|-|\Phi_J^+|$. The element $w_0w_J$ is simultaneously the unique shortest representative of the terminal coset $w_0W_J$ and the maximum of the minimal right-coset representatives $W^J$. Zero, disconnected, and rank-one faces are included without perturbation. \>1A producer-independent reconstruction through positive roots, inversion lengths, longest elements, and quotient weak order checks all branches in small $A,B,C,D,G_2$ types. Classical ownership, finite-type stopping limits, collision controls, and the strict all-fail Route-A disposition are audited.
author:
- |
  Route-A source-local certificate HCS-C286\
  Revision round 2
date: 2 September 2026
title: |
  Strong Convergence in the Finite Coxeter Numbers Game:\
  Parabolic Length and the Complete Boundary Atlas
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2862026090200000000000000000000\>\<C2862026090200000000000000000000\>\]

# Finite owner and firing convention

Let $\Phi\subset V$ be a finite reduced crystallographic root system, with simple roots $\{\alpha_i:i\in I\}$, coroots $\alpha_i^\vee$, positive roots $\Phi^+$, and Weyl group $W=\langle s_i:i\in I\rangle$. We use $$A_{ij}=\langle\alpha_j,\alpha_i^\vee\rangle.             \tag{1}$$ For a dominant weight $\lambda$, write $$x_i=\langle\lambda,\alpha_i^\vee\rangle\geq0.           \tag{2}$$ Node $i$ is legal precisely when $x_i>0$. Firing it replaces $\lambda$ by $s_i\lambda$ and therefore $$x'_j=x_j-A_{ji}x_i.                                      \tag{3}$$ A firing word $(i_1,\ldots,i_m)$ accumulates on the left: $$w_m=s_{i_m}\cdots s_{i_1},\qquad \lambda_m=w_m\lambda.  \tag{4}$$ Equations (1)--(4) remove the sign, transpose, and word-order ambiguities that otherwise obscure comparisons between versions of the numbers game.

The game and its strong-convergence theory are classical. Mozes introduced reflection processes on graphs and Weyl groups [@Mozes1990]; Eriksson developed the Coxeter formulation and strong-convergence theorem [@Eriksson1995; @Eriksson1996]. We claim no priority. Our purpose is to give a convention-locked finite-type proof, close every dominant boundary, and make the reconstruction independently executable. Standard finite Coxeter and root-system facts are sourced to Humphreys and Bourbaki [@Humphreys1990; @Bourbaki2002].

# The reflection-sign mechanism

Let $\ell$ denote Coxeter length. The following observation is the local engine of the proof.

[\[lem:sign\]]{#lem:sign label="lem:sign"} Suppose the current position is $w\lambda$. Then node $i$ is legal if and only if $w^{-1}\alpha_i$ is a positive root whose support is not contained in $J=\{j:\langle\lambda,\alpha_j^\vee\rangle=0\}$. Every legal firing obeys $$\ell(s_iw)=\ell(w)+1.                                  \tag{5}$$

The current coordinate is $$\langle w\lambda,\alpha_i^\vee\rangle
   =\langle\lambda,w^{-1}\alpha_i^\vee\rangle.           \tag{6}$$ A positive coroot is a nonnegative integral combination of simple coroots. Its pairing with $\lambda$ is zero exactly when the corresponding root lies in the subsystem $\Phi_J=\Phi\cap\operatorname{span}\{\alpha_j:j\in J\}$; outside that subsystem it is positive. A negative root gives a nonpositive pairing. This proves the legality criterion. The standard root criterion for Coxeter length says $w^{-1}\alpha_i>0$ exactly when (5) holds.

[\[thm:strict\]]{#thm:strict label="thm:strict"} If $x_i>0$ for every $i$, every complete legal firing sequence terminates at $w_0\lambda$, accumulates to the longest element $w_0$, and has exactly $|\Phi^+|$ moves.

Here $J=\varnothing$. Lemma [\[lem:sign\]](#lem:sign){reference-type="ref" reference="lem:sign"} makes every legal word reduced, so length strictly increases and termination follows from finiteness of $W$. At a terminal position every simple coordinate is nonpositive; hence the position is anti-dominant. A finite Weyl orbit meets the closed anti-dominant chamber in exactly one point, here $w_0\lambda$. Strict dominance makes the stabilizer trivial, so the accumulated element is $w_0$. Finally $\ell(w_0)=|\Phi^+|$.

\>0

# Walls as a parabolic quotient

Now retain all zero coordinates. Put $$J=\{i:x_i=0\},\qquad W_J=\langle s_j:j\in J\rangle,
 \qquad \Phi_J^+=\Phi^+\cap\operatorname{span}\{\alpha_j:j\in J\}. \tag{7}$$ The stabilizer of $\lambda$ is exactly $W_J$. Let $w_J$ be its longest element and define the minimal right-coset representatives $$W^J=\{w\in W:w\alpha_j\in\Phi^+\text{ for every }j\in J\}. \tag{8}$$

[\[lem:quotient\]]{#lem:quotient label="lem:quotient"} Starting at $e\in W^J$, legal firing edges are exactly the length-increasing left weak-order edges $$w\longmapsto s_iw\quad\text{that remain in }W^J.         \tag{9}$$ In particular every cumulative firing element is the unique minimum-length representative of its right coset modulo $W_J$.

The parabolic exchange lemma says that for $w\in W^J$ and $\ell(s_iw)=\ell(w)+1$, either $s_iw\in W^J$, or the reflection conjugate to $s_i$ by $w$ lies in $W_J$. In root language the exceptional alternative is precisely $w^{-1}\alpha_i\in\Phi_J^+$. Lemma [\[lem:sign\]](#lem:sign){reference-type="ref" reference="lem:sign"} excludes exactly that zero-coordinate alternative. It includes every other length-increasing edge, proving (9) inductively from the identity.

[\[thm:main\]]{#thm:main label="thm:main"} For every dominant $\lambda$ in every finite reduced crystallographic root system, every legal play terminates. Every complete play has the same:

1.  terminal position, namely the unique anti-dominant orbit point $w_0\lambda$;

2.  cumulative element $w_0w_J$;

3.  number of moves $$\ell(w_0w_J)=|\Phi^+|-|\Phi_J^+|.                       \tag{10}$$

Moreover $w_0w_J$ is the unique shortest representative of the terminal right coset $w_0W_J$, and equivalently the unique maximum-length element of $W^J$.

By Lemmas [\[lem:sign\]](#lem:sign){reference-type="ref" reference="lem:sign"} and [\[lem:quotient\]](#lem:quotient){reference-type="ref" reference="lem:quotient"}, each firing strictly raises length in the finite set $W^J$, so every play terminates. A terminal weight has all simple coordinates nonpositive and is therefore anti-dominant. Every finite Weyl orbit has one point in the closed anti-dominant chamber, so all plays end at $w_0\lambda$.

Since $W_J$ fixes $\lambda$, all elements taking $\lambda$ to this terminal point form the right coset $w_0W_J$. Lemma [\[lem:quotient\]](#lem:quotient){reference-type="ref" reference="lem:quotient"} says that the cumulative element is its unique minimum-length representative. The standard parabolic decomposition identifies that representative as $w_0w_J$; it is also the unique maximum of $W^J$. Thus the cumulative element is choice-independent.

Every firing word is reduced, so its move count is $\ell(w_0w_J)$. Inversion sets give $\ell(w_0)=|\Phi^+|$ and $\ell(w_J)=|\Phi_J^+|$. The length-additive parabolic factorization $w_0=(w_0w_J)w_J$ now proves (10). Finally $w_0w_J\lambda=w_0\lambda$ because $w_J$ fixes $\lambda$.

# Every degenerate face

The theorem specializes without limiting arguments:

  -----------------------------------------------------------------------------------------------------
  face                   exact conclusion
  ---------------------- ------------------------------------------------------------------------------
  strict dominance       $J=\varnothing$, cumulative element $w_0$, length $|\Phi^+|$

  arbitrary wall         retain $J$ exactly; the length loss is $|\Phi_J^+|$

  zero vector            $J=I$, $w_0w_J=e$, terminal zero, no legal moves

  disconnected $\Phi$    component games interleave; lengths add and terminals form the product point

  rank-one positive      $A_1$ sends $x>0$ to $-x$ in one firing

  rank-one zero          $A_1$ at $x=0$ has no legal firing

  zero-coordinate rule   legality is $x_i>0$, never $x_i\geq0$

  scope stop             affine and indefinite generalized Cartan systems are not covered
  -----------------------------------------------------------------------------------------------------

For a reducible system $\Phi=\bigsqcup_r\Phi^{(r)}$, one has $W=\prod_rW^{(r)}$, $\Phi^+=\bigsqcup_r(\Phi^{(r)})^+$ and $W_J=\prod_rW_{J_r}^{(r)}$. Firings in distinct components commute; hence complete component plays interleave freely and (10) adds componentwise. This proves the disconnected assertion rather than treating one sample as proof.

The finite hypothesis is structural: the proof uses longest elements, finite length ascent, and a finite parabolic quotient. We make no affine, indefinite, Kac--Moody, noncrystallographic, or arbitrary generalized-Cartan extension.

\>1

# Producer-independent executable reconstruction

The finite receipt tests conventions, not the all-system theorem. Its 23 cases cover $A_1$--$A_4$, $B_2$--$B_3$, $C_2$--$C_3$, $D_4$, $G_2$, and the disconnected product $A_2\sqcup A_1$, with strict, wall, positive rank-one, zero rank-one, and full-zero branches. The producer exhausts all 3332 complete legal words and records 143 depth levels plus eight boundary rows, for 3506 exact regression rows.

The checker imports no producer implementation. From each locked Cartan matrix it constructs the simple-reflection action on the root lattice, closes the complete root orbit, identifies $\Phi^+$, enumerates the Weyl group, computes inversion lengths, $w_0$, $\Phi_J^+$, $w_J$, $W^J$, and $w_0w_J$, and then constructs the quotient weak-order path DAG. It issues 19,056 assertions. SymPy independently checks 577 involution, determinant, characteristic-polynomial, braid-order, positive-root, length, and endpoint matrix identities. Two different fresh paths reproduce the 1,296,292-byte JSON receipt byte for byte. The checker rejects duplicate JSON keys at every depth and locks every contract value, row schema, scalar type, and complete unique grid. A hostile suite rejects 84/84 raw-duplicate, repaired-hash semantic/schema/type, drop-replace, and stale-hash attacks.

This separation matters: agreement cannot be obtained merely by invoking the same coordinate-update routine twice. Enumeration detects transpose and word-order mistakes; the proof remains the parabolic weak-order argument in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Source, collision, and Route-A boundaries

The primary papers and standard monographs cited above fix classical ownership. Publisher or author-institution metadata were checked for Mozes's DOI [10.1016/0097-3165(90)90024-Q](https://doi.org/10.1016/0097-3165(90)90024-Q), Eriksson's two DOIs [10.1016/0012-365X(94)00131-2](https://doi.org/10.1016/0012-365X(94)00131-2) and [10.1006/eujc.1996.0031](https://doi.org/10.1006/eujc.1996.0031), and Humphreys's book DOI [10.1017/CBO9780511623646](https://doi.org/10.1017/CBO9780511623646). This paper claims a checked synthesis, not originality of the theorem.

The internal collision scan distinguishes the mechanism from C185 Brockett matrix sorting, C230 open-Toda scattering, C176 recurrent sandpile translation, C181 rotor-router traversal, and C209 periodic Kreweras complementation. It is also disjoint from C279--C283. Shared words such as "reflection" or "sorting" do not identify a dynamical owner: here the state is a dominant Weyl-orbit point, the choices are legal simple reflections, and the invariant certificate is quotient weak-order ascent.

Route A is rejected on every axis. There is no rational-prime clock (A0), no nonconstant periodic or primitive recurrence (A1), no dynamical or Fredholm determinant (A2), no target analytic continuation or functional equation (A3), and no natural same-clock unitary/Hilbert--Polya lift of the terminating choice dynamics (A4). Thus $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)}
 \qquad \texttt{ROUTE\_A\_REJECTED}.                     \tag{11}$$ Route B is false. The frozen scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target zeros, Euler factors, or root numbers enter the proof or evidence.

# Conclusion {#conclusion .unnumbered}

Positive-coordinate firing on a finite crystallographic Weyl system is an exact parabolic quotient ascent. In the strict chamber this reaches $w_0$. \>0 On every wall it instead reaches the unique minimal representative $w_0w_J$ of the terminal coset, losing exactly the positive roots of the stabilizer subsystem and preserving choice-independent terminal state and length. Zero, reducible, and rank-one faces require no exception to the formula. \>1The independent root/Weyl reconstruction and hostile release controls certify the finite conventions while leaving the classical all-type proof, finite scope, and negative Route-A conclusion explicit.

9 N. Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, ISBN 978-3-540-42650-9.

K. Eriksson, The numbers game and Coxeter groups, *Discrete Mathematics* **139** (1995), 155--166. [doi:10.1016/0012-365X(94)00131-2](https://doi.org/10.1016/0012-365X(94)00131-2).

K. Eriksson, Strong convergence and a game of numbers, *European Journal of Combinatorics* **17** (1996), 379--390. [doi:10.1006/eujc.1996.0031](https://doi.org/10.1006/eujc.1996.0031).

J. E. Humphreys, *Reflection Groups and Coxeter Groups*, Cambridge Studies in Advanced Mathematics 29, Cambridge University Press, 1990. [doi:10.1017/CBO9780511623646](https://doi.org/10.1017/CBO9780511623646).

S. Mozes, Reflection processes on graphs and Weyl groups, *Journal of Combinatorial Theory, Series A* **53** (1990), 128--142. [doi:10.1016/0097-3165(90)90024-Q](https://doi.org/10.1016/0097-3165(90)90024-Q).
