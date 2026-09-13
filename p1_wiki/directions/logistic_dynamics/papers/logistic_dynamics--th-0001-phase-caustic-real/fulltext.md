---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--th-0001-phase-caustic-real"
canonical_tex: "logistic_dynamics/projects/th_0001_phase_caustic_real/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/th_0001_phase_caustic_real/paper/main.pdf"
source_sha256: "6381b247207d33c826888976960329b5e7aaa1c58ec1a2d80717adcfc56cf8b4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An On-Shell Real Caustic in a Frozen Three-Kick Fourier-Integral Model

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/th_0001_phase_caustic_real>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/th_0001_phase_caustic_real/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/th_0001_phase_caustic_real/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/th_0001_phase_caustic_real/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an exact, target-free follow-up to the TH-0001 audit of a frozen ordered three-kick Fourier-integral operator. For $$\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
   \qquad S_a(x,y)=xy-x+\frac{a}{3}x^3,$$ the internal Hessian has determinant $15q_1q_2-1$. Solving the stationary equations on this determinant-zero set gives the exact real parameterization $$q_1=t,\quad q_2=(15t)^{-1},\quad
   q_0=1-\tfrac32t^2-(15t)^{-1},\quad
   q_3=1-t-(90t^2)^{-1}$$ for every $t\in\mathbb{R}\setminus\{0\}$. Thus the caustic is a singular endpoint projection of the stationary canonical relation, rather than an off-shell integration artifact. At $t=1$, all six residuals of the three canonical kicks vanish exactly; the Hessian has rank one and the cubic derivative in a null direction equals $132$. The result strengthens the single-phase obstruction OBR-011 but does not supply a multi-chart Maslov ledger. No determinant, spectrum, prime or Riemann-zero data, Route-B inference, or RH claim is made.
author:
- 'HP-Dynamics Research Archive'
date: August 2026
title: 'An On-Shell Real Caustic in a Frozen Three-Kick Fourier-Integral Model'
```

## Markdown 正文

# Introduction

Oscillatory kernels for composed canonical maps are often written as products of elementary Fourier-integral factors. It is tempting to integrate out all intermediate coordinates and treat the result as one global phase. That step is only legitimate while the stationary projection is nondegenerate. A zero of the internal Hessian can instead signal a caustic, where the phase chart must be changed or retained as an iterated oscillatory integral.

The TH-0001 object is a deliberately frozen three-kick model. Its factors, clock, Fourier normalization, and phase sign are fixed before any calculation; no prime table, zero table, spectrum, or fitted parameter is admissible. A previous symbolic audit found an internal Hessian determinant $15q_1q_2-1$. The smallest unresolved question was whether this set is actually reached by the stationary canonical relation. If it were merely off-shell, the obstruction would be weaker. If it were on-shell, a global single-phase reduction would fail for geometric rather than coordinate-level reasons.

This paper answers that narrow question exactly. We solve the two stationary equations together with the caustic equation, identify the endpoint projection Jacobian, and certify one rational trajectory. The computation uses symbolic rational arithmetic only and is reproduced by a short SymPy program.

Our contributions are therefore limited and falsifiable:

1.  We parameterize every real nonzero-$t$ point of the internal caustic on the stationary relation.

2.  We prove that the endpoint projection Jacobian is exactly the negative of the internal Hessian, so the same set is the projection singular locus.

3.  We give an exact rational rank-one witness with vanishing canonical residuals and nonzero null-direction cubic derivative.

These facts refine OBR-011, but they do not open a spectral determinant or a Hilbert--Pólya construction. The rest of the paper defines the frozen object, proves the incidence identities, reports the rational witness, and closes with the Route-A boundary and reproduction protocol.

# Frozen ordered Fourier-integral object

For a real parameter $a$, fix the generating function $$S_a(x,y)=xy-x+\frac{a}{3}x^3.$$ The associated canonical kick is $$F_a(q,p)=\bigl(1-aq^2-p,\ q\bigr).$$ The clock is one ordered superstep $$G=F_{5/2}\circ F_{3/2}\circ F_{1/2},$$ with exactly three factors. In the iterated kernel, $q_0$ and $q_3$ are endpoints and $(q_1,q_2)$ are the internal variables. The frozen phase is $$\Phi(q_0,q_1,q_2,q_3)
 =S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3).$$

Differentiation in the internal coordinates gives $$E_1=\partial_{q_1}\Phi
 =q_0+\frac32q_1^2+q_2-1,
 \qquad
 E_2=\partial_{q_2}\Phi
 =q_1+\frac52q_2^2+q_3-1.$$ The internal Hessian is $$H_{\mathrm{int}}
 =\operatorname{Hess}_{(q_1,q_2)}\Phi
 =\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
 \qquad
 \det H_{\mathrm{int}}=15q_1q_2-1.$$

The source lock fixes $\hbar=1$, phase convention $\exp(+iS_a)$, positive-real factor amplitude $(2\pi)^{-1/2}$, and global phase $1$. The factorized operator acts on $L^2(\mathbb{R},\,\mathrm{d}q)$; its global Maslov index is intentionally not assigned. This stage has no determinant convention: neither a zeta function nor a spectral zero ledger is defined.

The factorization is the object. Replacing it by a single reduced phase would require a nondegenerate internal stationary projection on the region being used. The next section tests that requirement on-shell.

# Exact on-shell incidence

The internal caustic is the algebraic set $$15q_1q_2-1=0.$$ Let $t=q_1\in\mathbb{R}\setminus\{0\}$. The caustic equation gives $$q_2=\frac{1}{15t}.$$ Substitution into $E_1=E_2=0$ then gives $$q_0=1-\frac32t^2-\frac{1}{15t},
 \qquad
 q_3=1-t-\frac{1}{90t^2}.$$

Every real nonzero-$t$ point of the internal caustic is the endpoint data of a stationary point of the frozen phase. Conversely, the displayed formulas solve the stationary equations and the caustic equation identically in $t$.

The first formula follows by solving $15q_1q_2=1$ for $q_2$. The two stationary equations are affine in $q_0$ and $q_3$, respectively, so their substitution gives the displayed expressions. Direct expansion makes both $E_1$ and $E_2$ vanish and leaves $15q_1q_2-1=0$.

The stationary Lagrangian can be parameterized by $(q_1,q_2)$ through its endpoint map $$\pi(q_1,q_2)=\left(1-\frac32q_1^2-q_2,
                       1-q_1-\frac52q_2^2\right).$$ Its Jacobian is $$D\pi
 =\begin{pmatrix}-3q_1&-1\\-1&-5q_2\end{pmatrix}
 =-H_{\mathrm{int}}.$$ Hence $\det D\pi=0$ precisely on $15q_1q_2=1$. The caustic is therefore an actual singular projection of the stationary relation, not an artifact of allowing arbitrary internal integration coordinates.

# Rational rank-one witness

Choose $t=1$ in the exact parameterization. The endpoint and internal coordinates are $$(q_0,q_1,q_2,q_3)=\left(-\frac{17}{30},1,\frac1{15},-\frac1{90}\right).$$ Using $p_{j+1}=q_j$ and the first component of $F_a$, the corresponding momenta are $$(p_0,p_1,p_2,p_3)=\left(-\frac{289}{1800},-\frac{17}{30},1,\frac1{15}\right).$$ For the three parameters in their frozen order, direct substitution gives $$F_{1/2}(q_0,p_0)=(q_1,p_1),\qquad
 F_{3/2}(q_1,p_1)=(q_2,p_2),\qquad
 F_{5/2}(q_2,p_2)=(q_3,p_3),$$ with all six coordinate residuals equal to zero in exact arithmetic.

At this point $$H_{\mathrm{int}}=\begin{pmatrix}3&1\\1&1/3\end{pmatrix},
 \qquad \operatorname{rank} H_{\mathrm{int}}=1.$$ The vector $v=(-1,3)^T$ spans its nullspace. Since the only nonzero pure third derivatives of the phase in the internal variables are $\partial_{q_1}^3\Phi=3$ and $\partial_{q_2}^3\Phi=5$, $$D_v^3\Phi=3(-1)^3+5(3)^3=132\ne0.$$ The witness is thus a regular rank-one caustic in the frozen chart. This is an exact algebraic certificate, not a floating-point near-singularity.

::: {#tab:witness}
  Check                             Exact value
  --------------------------------- ----------------
  Caustic equation                  $15q_1q_2-1=0$
  Kick residuals                    six zeros
  Hessian rank                      $1$
  Null direction                    $(-1,3)$
  Null-direction cubic derivative   $132$

  : Exact checks at $t=1$.
:::

# Route-A interpretation and claim boundary

The exact incidence result strengthens obstruction OBR-011. The obstruction is not that the factorized operator fails to exist: each elementary factor keeps its declared positive-real normalization and factorized Plancherel unitarity. The obstruction is narrower. A single globally nondegenerate type-I phase, obtained by eliminating $(q_1,q_2)$ in one chart, cannot represent the whole stationary relation. A later phase analysis must introduce explicit charts, transition amplitudes, and a signed Maslov ledger.

The Route-A evaluation is $$\text{analytic tuple}=(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}),$$ while the Riemann-target tuple remains $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ The scoped verdict is `GO_WITH_LIMITATIONS`, with the audit then stopped.

No determinant, spectrum, periodic-orbit census, arithmetic weight law, completed-$\xi$ divisor, self-adjoint realization, or zero computation follows from this certificate. In particular, a real classical multiplier is not a Maslov assignment, and the local cubic witness is not evidence for a spectral zero. Route B is therefore not authorized.

# Reproducibility

All identities in this stage use exact SymPy rational polynomial arithmetic. The generator is copied byte-for-byte under 'experiments/' and 'src/'; the test suite checks the source-lock and parent-evaluation hashes, rebuilds the certificate in a temporary directory, and compares it byte-for-byte with the canonical JSON artifact. No training, validation, or test target data exist.

From the project root, the complete check is:

    PYTHONPATH=. python3 experiments/th_0001_phase_caustic_real.py --quiet \
      --output artifacts/th_0001/phase_caustic_real_audit.json
    PYTHONPATH=. python3 -m unittest -v tests/test_th_0001_phase_caustic_real.py
    sha256sum -c results/ARTIFACT_HASHES.sha256

The paper itself is built by two 'pdflatex' passes from 'paper/'. The hash manifest records the source lock, Route-A evaluation, generator, formal result, test, artifact, and manuscript source/PDF. Rebuildable auxiliary LaTeX files are ignored by the mirror repository.

The next smallest verifiable task is not another computation on this object. Reopening would require a new source lock for a multi-chart phase/Maslov transition ledger; otherwise the breadth-first search should pivot to a new candidate.

# Algebraic proof details

Expanding the phase gives $$\Phi=\frac{q_0^3}{6}+q_0q_1-q_0
      +\frac{q_1^3}{2}+q_1q_2-q_1
      +\frac{5q_2^3}{6}+q_2q_3-q_2.$$ Therefore $$\partial_{q_1}\Phi=q_0+\frac32q_1^2+q_2-1,
 \qquad
 \partial_{q_2}\Phi=q_1+\frac52q_2^2+q_3-1,$$ and $$\operatorname{Hess}_{(q_1,q_2)}\Phi
 =\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix}.$$ Imposing its determinant to vanish and writing $q_1=t\ne0$ yields $q_2=(15t)^{-1}$. The stationary equations are affine in the endpoints, which proves the formulas in Section 3.

For the witness, substitution of $$q_0=-17/30,\quad q_1=1,\quad q_2=1/15,\quad q_3=-1/90$$ and $$p_0=-289/1800,\quad p_1=-17/30,\quad p_2=1,\quad p_3=1/15$$ into $F_a(q,p)=(1-aq^2-p,q)$ at $a=1/2,3/2,5/2$ gives the three displayed equalities. At $(q_1=1,q_2=1/15)$, the Hessian annihilates $v=(-1,3)^T$, and the cubic directional derivative is $$\partial_{q_1}^3\Phi\,v_1^3+
 \partial_{q_2}^3\Phi\,v_2^3=3(-1)^3+5(3)^3=132.$$
