---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hyperplane-chamber-walk-route-a"
canonical_tex: "henon_dynamics/henon_hyperplane_chamber_walk_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hyperplane_chamber_walk_route_a/paper/main.pdf"
source_sha256: "c1cd1167f49b4beab8c69bd32e0f0682dde2906e7f2ce9b560b0a06c5e5c4eb3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Spectra for Hyperplane Chamber Walks: A Route-A Stress Test

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hyperplane_chamber_walk_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hyperplane_chamber_walk_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hyperplane_chamber_walk_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hyperplane_chamber_walk_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite real hyperplane arrangement and every probability measure on its faces, the Brown--Diaconis theorem diagonalizes the induced chamber walk. We record the resulting characteristic polynomial, finite determinant, power traces, unique-stationarity criterion, exact sampler, and mixing bound. Exact rational coordinate and braid fixtures test the formulas but do not prove the all-family theorem. The complete operator structure still fails Route A: without target arithmetic semantics, its determinant is only a formal hint.
author:
- 'HCS-C192 theorem and evidence package'
date: 27 August 2026
title: |
  Exact Spectra for Hyperplane Chamber Walks:\
  A Route-A Stress Test
```

## Markdown 正文

# Face dynamics and the flat spectrum

Let $\mathcal A$ be a finite real hyperplane arrangement in $V$, with faces $\mathcal F$ and chambers $\mathcal C$. In sign coordinates the face product is $(FG)_H=F_H$ when $F_H\ne0$ and $(FG)_H=G_H$ otherwise. A face law $w$ defines $$K(C,C')=\sum_{F:FC=C'}w(F).$$ Write $L(\mathcal A)$ for the intersection poset and $\mu$ for its Möbius function. Brown and Diaconis [@BD98 Theorem 1] prove that $K$ is diagonalizable, with flat-indexed data $$\lambda_W=\sum_{F\subseteq W}w(F),\qquad
 m_W=|\mu(W,V)|.$$ Consequently, even when several flats yield the same numerical eigenvalue, $$\begin{aligned}
 \chi_K(x)&=\prod_{W\in L(\mathcal A)}(x-\lambda_W)^{m_W},\\
 \det(I-zK)&=\prod_{W\in L(\mathcal A)}(1-z\lambda_W)^{m_W},\\
 \operatorname{tr}(K^\ell)&=\sum_Wm_W\lambda_W^\ell.\end{aligned}$$ These are finite-dimensional deductions from the cited theorem, not a new diagonalization claim. In particular, diagonalizable does not mean reversible or self-adjoint.

# Stationarity and convergence

A face law is *separating* if each $H\in\mathcal A$ is avoided by some positive-weight face. Brown--Diaconis Theorem 2 proves that separation is equivalent to unique stationarity. Under separation, sample all positive-weight faces without replacement, choosing each next face proportionally to its remaining weight. Their product is a chamber with the stationary law $\pi$.

For every start $C$ and $\ell\ge0$, their coupling argument gives $$\lVert K_C^\ell-\pi\rVert_{\mathrm{TV}}
 \le -\sum_{W\ne V}\mu(W,V)\lambda_W^\ell
 \le \sum_{H\in\mathcal A}\lambda_H^\ell .$$ The middle term is exactly the probability that the product of $\ell$ i.i.d. sampled faces is not yet a chamber [@BD98 Section 4B].

#### Stopping terminology.

Sampling with replacement and stopping when the accumulated face product first becomes a chamber gives the same stationary marginal: earlier repeated factors may be deleted to recover weighted sampling without replacement. This is an exact stationary stopping sampler and the stopping event drives the displayed coupling bound. We do not call it a strict strong stationary time. That term would additionally require independence of the stopped chamber and the stopping time, a statement not supplied by the cited theorem and false for general unequal-weight coupon orders.

#### Nonseparating boundary.

Let $\mathcal A_0$ contain precisely the hyperplanes that contain every positive-weight face. Brown and Diaconis show that the $\mathcal A_0$-chambers index closed components of the walk. Each component has one stationary law, and the set of all stationary laws is exactly the simplex with one vertex per $\mathcal A_0$-chamber. Thus nonseparation has a complete component classification, not merely a failure of uniqueness. Their Section 6 carries Theorems 1 and 2 to oriented-matroid covector face semigroups; we import only that stated extension and no broader affine or realization claim.

# Finite exact regression

Two independent rational implementations and a separate SymPy oracle check eight coordinate/braid fixtures. The census contains 316 faces, 94 chambers, 75 flats, 1,604 transition cells, 62 stationary probabilities, 24 mixing rows, and 48 trace rows. The independent checker passes 20,609 assertions; SymPy passes 3,398 exact checks. These finite examples are regression oracles only.

The producer generates coordinate sign cubes and ordered-set-partition covectors, then enumerates weighted face orders. The checker imports no producer code: it reconstructs face closure and the support lattice from the serialized signs, recomputes Möbius values recursively, and obtains the stationary law by subset dynamic programming. SymPy separately recomputes the matrix polynomials, traces, and geometric multiplicities. Byte replay is exact, and 74 repaired-payload semantic attacks plus one stale-hash attack are rejected.

  --------------------------------------------------------------------------------------------------
  Statement                        Owner/evidence              Ceiling
  -------------------------------- --------------------------- -------------------------------------
  flat spectrum and multiplicity   Brown--Diaconis Theorem 1   no self-adjointness

  sampler, uniqueness, mixing      Theorem 2 and Section 4     no strict-SST independence

  nonseparating simplex            Section 4B remarks          no irreducibility across components

  oriented-matroid transfer        Section 6                   only the stated covector framework

  matrix identities                elementary deduction here   no target determinant

  finite census                    exact regression code       no proof by enumeration
  --------------------------------------------------------------------------------------------------

  : Claim ownership and release ceilings.

# Route-A verdict

The exact result has no intrinsic rational-prime or target-zero index, recovers no target arithmetic data, supplies no target functional equation, and yields no target counting law. Its finite determinant is a natural operator object but no target divisor is identified. Hence $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\_HINT}),$$ with overall rejection and no Route-B invocation. No local or Euler factors, root numbers, automorphy, Hilbert--Pólya operator, global novelty, or external review are claimed.

1 K. S. Brown and P. Diaconis, Random walk and hyperplane arrangements, *Ann. Probab.* 26 (1998), 1813--1854, [doi:10.1214/aop/1022855884](https://doi.org/10.1214/aop/1022855884).
