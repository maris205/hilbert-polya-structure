---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-relative-lind-counterterm"
canonical_tex: "henon_dynamics/henon_relative_lind_counterterm/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_relative_lind_counterterm/paper/paper.pdf"
source_sha256: "681ad73e4e3057352857c33f032b00b298bdf56227ebd2b81944892014d02982"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Unique Local Counterterm between a Hénon Reflection Packet and the Full Lind Zeta

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_relative_lind_counterterm>)
- [规范 TeX](<../../../../../henon_dynamics/henon_relative_lind_counterterm/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_relative_lind_counterterm/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_relative_lind_counterterm/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_relative_lind_counterterm/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The orbit-resolved odd reflection-packet Euler product for the full Hénon horseshoe and the Lind zeta of the full two-shift reverse action share the same positive entropy boundary, but they do not have the same singular ledger. Starting from the primary-source formula $$\zeta_{\rm flip}(t)=(1-2t^2)^{-1/2}
   \exp\!\left(\frac{2t+3t^2}{1-2t^2}\right),$$ we set $u=1-\sqrt2t$ and compare it to the packet product. The packet accounts for exponential pole coefficient $1/\sqrt2$, whereas the full Lind zeta has coefficient $1/\sqrt2+3/4$ and a logarithmic branch of coefficient $-1/2$. We prove that $$u^{1/2}e^{-3/(4u)}
   \frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}$$ extends holomorphically and nonvanishingly across $u=0$ as a local branch germ. Among counterterms $u^\beta e^{-c/u}$, the pair $(c,\beta)=(3/4,1/2)$ is unique. Thus odd packet data admits an exact local reconciliation with the source zeta but does not by itself encode the full infinite-dihedral subgroup ledger. Global continuation, zeros, arithmetic semantics, and operator ownership remain open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  The Unique Local Counterterm between a Hénon\
  Reflection Packet and the Full Lind Zeta
```

## Markdown 正文

# Two objects at one boundary

For the full $n$-shift with reverse flip, @KimLeePark2003 [Example 4.3] prove $$\label{eq:source-n}
 \zeta_{\sigma,\rho}(t)=
 \frac1{\sqrt{1-nt^2}}
 \exp\!\left(
 \frac{nt+(n+n^2)t^2/2}{1-nt^2}
 \right).$$ This is the Lind zeta of the full infinite-dihedral action; its definition sums fixed points over all finite-index subgroups. Finite-order reversal and matrix extensions are developed in @Ryu2019.

We specialize [\[eq:source-n\]](#eq:source-n){reference-type="eqref" reference="eq:source-n"} to $n=2$: $$\label{eq:lind}
 \zeta_{\rm flip}(t)=(1-2t^2)^{-1/2}
 \exp\!\left(\frac{2t+3t^2}{1-2t^2}\right).$$ The Hénon/full-shift conjugacy [@DevaneyNitecki1979] also yields a different object: the product $\mathcal Z_{\rm orb}(t,1)$ over primitive odd marked reflection words. Its exact local theorem is $$\label{eq:packet}
 \log\mathcal Z_{\rm orb}(t,1)=
 \frac{1}{\sqrt2(1-\sqrt2t)}+G_{\rm orb}(t),$$ with $G_{\rm orb}$ analytic near $t=1/\sqrt2$. Equation [\[eq:packet\]](#eq:packet){reference-type="eqref" reference="eq:packet"} does not assert equality with [\[eq:lind\]](#eq:lind){reference-type="eqref" reference="eq:lind"}.

# The source Lind boundary ledger

Put $$\label{eq:u}
 u=1-\sqrt2t,\qquad t=\frac{1-u}{\sqrt2}.$$ Then $$\begin{aligned}
 1-2t^2&=u(2-u),\label{eq:denominator}\\
 2t+3t^2
 &=\sqrt2(1-u)+\frac32(1-2u+u^2).\label{eq:numerator}\end{aligned}$$

[\[prop:lind-local\]]{#prop:lind-local label="prop:lind-local"} There is a function $G_{\rm L}$, analytic at $u=0$, such that $$\label{eq:lind-local}
 \log\zeta_{\rm flip}(t)=
 \frac{1/\sqrt2+3/4}{u}-\frac12\log u+G_{\rm L}(u).$$

The exponential term in [\[eq:lind\]](#eq:lind){reference-type="eqref" reference="eq:lind"} is the quotient of [\[eq:numerator\]](#eq:numerator){reference-type="eqref" reference="eq:numerator"} by [\[eq:denominator\]](#eq:denominator){reference-type="eqref" reference="eq:denominator"}. Its residue in the coordinate $u$ is $$\frac{\sqrt2+3/2}{2}=\frac1{\sqrt2}+\frac34.$$ Subtracting this multiple of $u^{-1}$ leaves a rational function analytic at zero. The prefactor contributes $-\frac12\log u-\frac12\log(2-u)$, and the latter term is analytic at zero.

The coefficient $1/\sqrt2$ in [\[eq:lind-local\]](#eq:lind-local){reference-type="eqref" reference="eq:lind-local"} agrees exactly with the odd packet coefficient in [\[eq:packet\]](#eq:packet){reference-type="eqref" reference="eq:packet"}. The remaining $3/4$ and the square-root branch cannot be absorbed into an analytic nonzero factor.

# Relative counterterm and uniqueness

Subtracting [\[eq:packet\]](#eq:packet){reference-type="eqref" reference="eq:packet"} from [\[eq:lind-local\]](#eq:lind-local){reference-type="eqref" reference="eq:lind-local"} gives $$\label{eq:relative-log}
 \log\frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}
 =\frac{3}{4u}-\frac12\log u+G_{\rm rel}(u),$$ where $G_{\rm rel}$ is analytic.

[\[thm:counterterm\]]{#thm:counterterm label="thm:counterterm"} On any fixed local branch of $u^{1/2}$, $$\label{eq:Crel}
 C_{\rm rel}(t):=
 u^{1/2}e^{-3/(4u)}
 \frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}$$ extends holomorphically and nonvanishingly across $u=0$. Moreover, among all counterterms $u^\beta e^{-c/u}$, a nonzero holomorphic extension is possible only for $$\label{eq:unique}
 c=\frac34,\qquad\beta=\frac12.$$

Taking a logarithm in [\[eq:Crel\]](#eq:Crel){reference-type="eqref" reference="eq:Crel"} cancels the two singular terms in [\[eq:relative-log\]](#eq:relative-log){reference-type="eqref" reference="eq:relative-log"}, leaving $G_{\rm rel}$. Exponentiation gives the nonzero extension. For a general pair $(c,\beta)$, the logarithm contains $(3/4-c)u^{-1}+(\beta-1/2)\log u+G_{\rm rel}$. A nonzero holomorphic germ has neither an essential exponential nor a nonintegral/logarithmic branch, forcing [\[eq:unique\]](#eq:unique){reference-type="eqref" reference="eq:unique"}.

The theorem is local: the square-root branch is fixed only in a neighborhood, and no claim is made that [\[eq:Crel\]](#eq:Crel){reference-type="eqref" reference="eq:Crel"} is a globally single-valued determinant.

# Exact audit and route boundary

The accompanying certificate performs the expansion in $\mathbb Q(\sqrt2)$, verifies the normalized algebraic factor $u^{1/2}/\sqrt{u(2-u)}=(2-u)^{-1/2}$, and records the analytic exponent through order six. An independent rational audit recovers $3/4$ and $1/2$. Eight tests pass in normal and optimized modes, four dependencies are locked, and 23 claim mutations are rejected.

P71 supplies a source-native local bridge: the restricted Hénon packet can be reconciled with the full Lind germ only after adding precisely the missing subgroup and branch ledgers. It does not prove global continuation, a Fredholm realization, rational-prime weights, a trace formula, or a self-adjoint operator. Route A remains exploratory and Route B is not authorized. The next test is whether the normalized relative Taylor coefficients satisfy a finite-state recurrence or carry a new obstruction.
