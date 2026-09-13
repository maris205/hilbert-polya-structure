---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-affine-impact-bouncing-ball-route-a"
canonical_tex: "henon_dynamics/henon_affine_impact_bouncing_ball_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_affine_impact_bouncing_ball_route_a/paper/main.pdf"
source_sha256: "a95abc120694944fa33631258dfef34da9f0e219e60a08a0e1f3f0f677b2e43e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Event-Time Atlas for an Affine-Impact Bouncing Ball

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_affine_impact_bouncing_ball_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_affine_impact_bouncing_ball_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_affine_impact_bouncing_ball_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_affine_impact_bouncing_ball_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We analyse a gravity-driven ball on a half-line with restitution and a constant impact impulse. The physical flow is $\dot q=v$, $\dot v=-g$, the guard is $q=0,v^-<0$, and the reset is $v^+=r(-v^-)+J$. On the positive outgoing section the event map is the affine map $P(u)=ru+J$, but each iterate carries the physical roof $2u/g$. This gives exact geometric and arithmetic event sequences, a sharp Zeno boundary, a unique positive forced flight for $J>0,r<1$, and separate elastic, sticking, and accelerating boundaries. We adjoin $(0,0)$ as rest and exclude it from the regular section, so a zero-duration fixed event is not counted as a physical cycle. The certificate checks 96 exact event-time cells and 36 interior impact reconstructions. Any fixed-point series is explicitly an event-map object, not a physical-flow zeta or a target arithmetic construction.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'An Exact Event-Time Atlas for an Affine-Impact Bouncing Ball'
```

## Markdown 正文

suppressoptionalinfo 611

# Hybrid model and reduction

For $g>0$, $0\le r\le1$, and $J\ge0$, let $$\dot q=v,\qquad \dot v=-g\quad(q>0),\qquad
 v^+=r(-v^-)+J\quad(q=0,v^-<0).$$ The point $(q,v)=(0,0)$ is a separate absorbing rest state. For an interior state, solving $q_0+v_0t-gt^2/2=0$ gives $$\tau_0=\frac{v_0+\sqrt{v_0^2+2gq_0}}{g},\qquad
 w_0=\sqrt{v_0^2+2gq_0},\qquad u_0=rw_0+J.$$ Starting just after an impact with positive outgoing speed $u$, symmetry of constant acceleration gives one physical flight of duration $2u/g$ and returns the incoming speed $-u$. Thus the outgoing section map is $$P(u)=ru+J,\qquad \tau(u)=\frac{2u}{g},\qquad u\in\mathcal S_+=(0,\infty).$$

[\[thm:impact\]]{#thm:impact label="thm:impact"} For $r\ne1$, put $u_*=J/(1-r)$. Then $$u_n=u_*+r^n(u_0-u_*),\qquad
 t_n=\frac2g\left[n u_*+(u_0-u_*)\frac{1-r^n}{1-r}\right].$$ For $r=1$, $u_n=u_0+nJ$ and $t_n=\frac2g[n u_0+Jn(n-1)/2]$. If $J=0$ and $0<r<1$, positive speeds form a Zeno sequence with accumulation time $2u_0/[g(1-r)]$. The edge $r=0,J=0$ has one positive-duration flight at most and then sticks at rest. If $J>0$ and $r<1$, $u_*$ is the unique positive forced cycle, with physical period $2u_*/g$ and event multiplier $P'(u)=r$; every positive speed converges to it. At $r=1,J=0$ there is a continuum of elastic periods $2u/g$, while $r=1,J>0$ is nonperiodic with quadratic event times.

The first equation is the quadratic flight root. The reset gives $P$, and induction followed by a finite geometric or arithmetic sum gives the displayed iterates and times. The geometric sum is finite precisely for $J=0,0<r<1$; $r=0$ reaches zero after one flight and the rest convention stops the execution. Solving $u=P(u)$ and using contraction proves the forced cycle and its multiplier. Identity and translation follow directly.

\>0

# Section domains and formal series

The regular section is $\mathcal S_+=(0,\infty)$ (the literal label `S_+`): it parametrizes positive-duration flights only. Consequently, for $J>0,r<1$ the physical event-map fixed-point series is $\zeta_{\rm phys}(z)=1/(1-z)$, whereas for $J=0,r<1$ it is the empty series $1$ on $\mathcal S_+$. If the section is artificially closed to $[0,\infty)$, the affine boundary point $u=0$ contributes the separate formal series $\zeta_{\rm aff}(z)=1/(1-z)$ when $J=0,r<1$; that point is rest, not a physical orbit. For $r=1,J=0$ the fixed set is a continuum and a cardinality series is undefined. For $r=1,J>0$ translation has no fixed point, so its finite-count series is $1$. None of these event-map series is a physical-flow zeta.

\>1

# Exact audit and scope boundary

Twelve rational controls cover contraction, strict Zeno, the $r=0$ sticking edge, elastic identity, and translation. The ledger contains 96 exact roof and cumulative-time cells and 36 first-impact reconstructions. An independent checker passes 368 exact assertions; SymPy passes 11 identities, byte replay is exact, and 14 repaired/stale hash mutations are rejected. In particular, an attack that relabels $r=0,J=0$ as Zeno is caught before release.

The Route-A tuple is

(A0\_FAIL, A1\_WEAK, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The package makes no target prime, zero, local factor, root number, automorphy, target functional equation, or Hilbert--Polya operator claim.

# Source note {#source-note .unnumbered}

Hybrid modeling context is given by Leine--Nijmeijer [@leine2004] and Goebel--Sanfelice--Teel [@goebel2012]; no priority claim is made.

9 R. I. Leine and H. Nijmeijer, *Dynamics and Bifurcations of Non-Smooth Mechanical Systems*, Springer (2004), DOI:[10.1007/978-3-540-44398-8](https://doi.org/10.1007/978-3-540-44398-8). R. Goebel, R. G. Sanfelice, and A. R. Teel, *Hybrid Dynamical Systems: Modeling, Stability, and Robustness*, Princeton University Press (2012), DOI:[10.1515/9781400842636](https://doi.org/10.1515/9781400842636).

# Declarations {#declarations .unnumbered}

**Scope.** The exact registered literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. **Data and code.** The theorem, exact ledger, independent checks, and build recipe are released with HCS-C212. **Competing interests.** None declared. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked formulas, metadata, and scope boundaries. This is not external peer review.
