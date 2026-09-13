---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quadratic-newton-cayley-global-dynamics-route-a"
canonical_tex: "henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a/paper/main.pdf"
source_sha256: "1af08064f105d5f96808d7a9241a392b9acc3171554801fabea071f0edd16926"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Global Quadratic Newton Dynamics through the Cayley Coordinate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quadratic_newton_cayley_global_dynamics_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For Newton iteration of $p_a(z)=z^2-a^2$, $a\ne0$, we take an all-state step: a Cayley coordinate conjugates the rational map on the Riemann sphere exactly to squaring. This yields both root basins, their Julia boundary, double-exponential error identities, and a complete periodic/preperiodic classification. A root of unity of order $2^e q$, $q$ odd, has exact tail $e$ and eventual period $\operatorname{ord}_q(2)$. We also derive all multipliers, $\#\operatorname{Fix}(N_a^n)=2^n+1$, $\zeta_{\mathrm{AM}}(t)=((1-t)(1-2t))^{-1}$, and the invariant Cauchy law on the Julia line. Exact independent checks cover 16 periods, 128 root orders, and 41 hostile mutations. The result is source-local complex dynamics, with no arithmetic, target-determinant, or Hilbert--Pólya claim.
author:
- HCS Research Program
date: 31 August 2026(revision 2)
title: Global Quadratic Newton Dynamics through the Cayley Coordinate
```

## Markdown 正文

suppressoptionalinfo 611 trailerid \[\<C2572026083100000000000000000000\>\<C2572026083100000000000000000000\>\]

# Frozen Newton family and global coordinate

For $a\in\mathbb C^*$, let $$p_a(z)=z^2-a^2,\qquad
 N_a(z)=z-\frac{p_a(z)}{p_a'(z)}=\frac{z^2+a^2}{2z}
 \label{eq:newton}$$ act on $\mathbb P^1(\mathbb C)$. The clock is the Newton iterate $n\ge0$. Introduce $$C_a(z)=\frac{z-a}{z+a},\qquad
 C_a^{-1}(w)=a\frac{1+w}{1-w}.
 \label{eq:cayley}$$ Direct cancellation gives the decisive identity $$C_a\!\left(N_a(z)\right)=C_a(z)^2,
 \qquad C_a\!\left(N_a^n(z)\right)=C_a(z)^{2^n}.
 \label{eq:conjugacy}$$ Thus the statement below is global on the sphere; it is not a local convergence estimate inferred from samples.

The basins of $+a$ and $-a$ are $$\begin{aligned}
 \mathcal B(+a)&=\{z:|C_a(z)|<1\}=\{z:\Re(z/a)>0\},\\
 \mathcal B(-a)&=\{z:|C_a(z)|>1\}=\{z:\Re(z/a)<0\}.\end{aligned}$$ Their common boundary $J(N_a)=\{\Re(z/a)=0\}\cup\{\infty\}$ is the Julia set. If $w=C_a(z)$, then in the plus basin $$N_a^n(z)-a=\frac{2a w^{2^n}}{1-w^{2^n}}.
 \label{eq:pluserror}$$ If $v=w^{-1}$, then in the minus basin $$N_a^n(z)+a=-\frac{2a v^{2^n}}{1-v^{2^n}}.
 \label{eq:minuserror}$$

#### Proof.

The inequalities are $|z-a|<|z+a|$ and its reverse, which are equivalent to the sign of $\Re(z/a)$. The unit circle is the Julia set of $w^2$, so its inverse Cayley image is the displayed generalized line. Substituting $w^{2^n}$ into $C_a^{-1}$ proves ([\[eq:pluserror\]](#eq:pluserror){reference-type="ref" reference="eq:pluserror"})--([\[eq:minuserror\]](#eq:minuserror){reference-type="ref" reference="eq:minuserror"}).

# Every periodic orbit and the dynamical zeta

Write $D(w)=w^2$. The equation $D^n(w)=w$ contains $0$, $\infty$, and the $2^n-1$ roots of $w^{2^n-1}=1$. Hence $$F_n=\#\operatorname{Fix}(N_a^n)=2^n+1,
 \quad P_n=\sum_{d\mid n}\mu(n/d)(2^d+1),
 \quad O_n=P_n/n.
 \label{eq:counts}$$ Here $P_n$ and $O_n$ count exact-period points and primitive cycles. The two root fixed points are superattracting. At any Julia point of exact period $n$, $(D^n)'(w)=2^n w^{2^n-1}=2^n$, so every such cycle is repelling and its multiplier is exactly $2^n$. Therefore $$\zeta_{\mathrm{AM}}(t)=\exp\!\left(\sum_{n\ge1}\frac{F_n}{n}t^n\right)
 =\frac{1}{(1-t)(1-2t)}.
 \label{eq:zeta}$$

\>0

# Exact tails and the invariant failure-line law

The count formula does not by itself classify strictly preperiodic points. Equation ([\[eq:conjugacy\]](#eq:conjugacy){reference-type="ref" reference="eq:conjugacy"}) supplies the missing global statement.

Apart from $w=0,\infty$, a point is preperiodic if and only if $w$ is a root of unity. If its order is $m=2^e q$ with $q$ odd, then the exact tail is $e=v_2(m)$, the landing order is $q$, and the eventual exact period is $\operatorname{ord}_q(2)$, with $\operatorname{ord}_1(2)=1$. It is periodic precisely when $e=0$.

Indeed, each squaring removes exactly one factor $2$ from the order until the odd order $q$ remains. Thereafter squaring acts by multiplication by $2$ in $(\mathbb Z/q\mathbb Z)^*$. Conversely, equality between two distinct powers $w^{2^r}=w^{2^s}$ forces $w$ to be a root of unity.

On the Julia set write $w=e^{i\theta}$ and $$z=ia s,\qquad s=\cot(\theta/2).$$ Normalized Haar measure becomes $$d\nu(s)=\frac{ds}{\pi(1+s^2)},
 \label{eq:cauchy}$$ and angle doubling becomes the rational map $$s\longmapsto\frac{s^2-1}{2s}.
 \label{eq:boundary}$$ Thus $\nu$ is invariant and mixing, and the Lyapunov exponent in the Cayley angle is $\log2$. In Newton language, the basin-separating line carries an exact Cauchy statistical law rather than convergence to a root.

#### Parameter boundaries.

Scale covariance is $N_a(au)=aN_1(u)$, and replacing $a$ by $-a$ exchanges the root labels. At $a=0$, however, $N_0(z)=z/2$ for finite $z$: the rational degree drops from two to one. The degree-two theorem is not extended silently across this face.

=1

#### Exact receipt.

The canonical JSON records periods $1$ through $16$, root-of-unity orders $1$ through $128$, ten exact real basin rows, and eight rational Cauchy rows. The producer-independent checker reconstructs all integer formulas; SymPy separately verifies the rational conjugacy, error identities, multipliers, boundary map, and zeta coefficients. These finite rows are regression probes for the analytic theorem, not its proof.

\>1

# Independent gates, collision control, and route boundary

The checker passes 1317 assertions. A separate SymPy program passes 88 identities, clean-process evidence replay is byte-identical, and all 41 repaired-hash hostile mutations are rejected. Three revision PDFs are built twice under a fixed epoch and checked for embedded subset fonts, clean logs, extractable text, and visual integrity.

The ownership boundary is explicit. C141 concerns the Hardy-space inverse-branch Ruelle operator for $z^2-6$, not Newton root basins. C177 concerns Wold and Sobolev mixing for every expanding circle degree, not the Newton sphere, root errors, or exact even-order tail. C257 does not claim either neighboring operator theorem; this is workspace bookkeeping, not a literature-priority claim.

The locked scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. Formula ([\[eq:zeta\]](#eq:zeta){reference-type="ref" reference="eq:zeta"}) is the generic degree-two source dynamical zeta, not an arithmetic Euler product. There is no prime carrier, logarithmic prime clock, arithmetic local datum, root number, automorphy statement, target divisor or functional equation, target determinant, or Hilbert--Pólya operator. The strict tuple is `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, the overall verdict is `ROUTE_A_REJECTED`, and Route B is false.

# Conclusion

One Möbius conjugacy closes an unusually broad dynamical ledger: global root selection, exact quadratic error at every iterate, all periodic and preperiodic points and multipliers, primitive counts, zeta, and the invariant law on the failure line. The same completeness sharpens the obstruction: the formulas are universal for quadratic Newton maps with two simple roots and do not single out arithmetic primes or a target spectrum. No statement for cubic or higher-degree Newton maps is inferred.

9 A. Cayley, "Desiderata and Suggestions: No. 3. The Newton--Fourier Imaginary Problem," *American Journal of Mathematics* 2 (1879), 97, DOI [10.2307/2369201](https://doi.org/10.2307/2369201). M. Artin and B. Mazur, "On Periodic Points," *Annals of Mathematics* 81 (1965), 82--99, [JSTOR 1970384](https://www.jstor.org/stable/1970384).
