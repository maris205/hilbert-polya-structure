# Candidate Evaluation — Route A, Layers A0--A1

评估日期：2026-08-13。所有 verdict 使用 `skills/route-a-evaluator.md` 的枚举值。A2--A4 只作架构边界审计，不能越过 Stage 1 宣称已完成后续阶段。

## Obligation matrix

| Candidate | Frozen source lock | A0 | A1 | Later architecture (scoped) | Overall |
|---|---|---|---|---|---|
| `DEN-WITT-Z-FIN` | \(\operatorname{Spec}\mathbb Z\), finite-kernel admissibility \(\mathcal E_{\rm fin}\), \(\phi^t[P,u]=[P,e^tu]\) | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | `A1_WEAK` | packet-index Euler product is formal until a canonical packet trace/measure is proved; no natural quantization yet | `ROUTE_A_EXPLORATORY` |
| `MOD-GEO` | unit-speed flow on \(T^1(\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H)\) | `A0_WEAK_ARITHMETIC_RELATION`; rational-prime mechanism `REFUTED` | `A1_PASS_ANALYTIC` | `A2_ANALYTIC_DETERMINANT`, partial A3, natural Laplace/scattering A4, but all for the wrong arithmetic divisor/counting law | `ROUTE_A_REJECTED` as rational-prime HP candidate; exact benchmark retained |
| `COMPACT-GEO` | class-level compact curvature \(-1\) flow; no single \(\Gamma\) frozen | `A0_FAIL` | `A1_PASS_ANALYTIC` at theorem level | exact Selberg/Laplacian architecture | `PROVES_TOO_MUCH_CONTROL`; numerical candidate itself `NOT_TESTABLE` until \(\Gamma\) frozen |
| `CONTACT-ANOSOV` | smooth contact Anosov class only | `A0_FAIL` | `A1_PASS_ANALYTIC` at class level | Ruelle continuation/PR resonance architecture | class comparator, not a frozen candidate |
| `HENON-SUSP` | \(F_a(x,y)=(1-ax^2-y,x)\), geometry-only \(a=1.00561\), constant roof \(\tau=1\) | `A0_FAIL` | `A1_WEAK` | exact map action/monodromy exists; complete UPO ledger and natural flow quantization do not | `ROUTE_A_REJECTED` |
| `HYP-BILLIARD` | generic dispersing/hyperbolic billiard class | `A0_FAIL` | analytic primitive/monodromy framework, but no member frozen | natural Laplacian/scattering only after geometry and boundary condition are frozen | control only / `NOT_TESTABLE` |
| `BERRY-KEATING-XP` | unregularized \(H=xp\) on \(\mathbb R^2\), no cutoffs or boundary identifications | `A0_FAIL` | `A1_FAIL` | formal quantization clue only | `ROUTE_A_REJECTED` |

## Why Deninger is exactly `A1_WEAK`

Theorem 4.2 proves, for the frozen admissible system,

\[
\operatorname{Per}(X_{0,\mathcal E})=\coprod_{p}\Gamma_p,
\]

where each compact \(\Gamma_p\) consists of periodic orbits of least period \(\log p\), and every periodic orbit lies in one packet. Hence existence, period and completeness at packet level are `PROVED`.

But the source explicitly says a closed point corresponds **not to an individual orbit** but to a compact packet. There is no canonical representative, conventional isolated-orbit multiplicity, phase, smooth transverse monodromy, or trace weight. Therefore:

```text
packet decomposition                 PROVED
period log p                         PROVED
all periodic orbits accounted for   PROVED
unique individual orbit per p       REFUTED
canonical packet multiplicity        OPEN
smooth monodromy                     NOT_TESTABLE
packet trace weight and phase        OPEN
```

`A1_OPEN` is not a legal evaluator verdict; `OPEN` belongs in evidence status. `A1_FAIL` would erase the proved packet structure, while any `A1_PASS_*` would overclaim isolated-orbit data. `A1_WEAK` is the calibrated result.

## Why later exactness cannot rescue MOD-GEO

The modular candidate has nearly ideal A1--A4 architecture: primitive closed geodesics and repetitions are analytic; Selberg/Ruelle determinants exist; the Laplacian is fixed and self-adjoint on its proper domain. Nevertheless, with the frozen arc-length clock,

\[
e^{r\ell_\gamma}\notin\mathbb Q
\]

for every hyperbolic \(\gamma\) and \(r\ge1\). Thus the rational-prime power support is absent before any zeta or quantization question. The exact Selberg trace is a calibration benchmark, not an A0 bypass.

## Adversarial controls

1. **Generic compact hyperbolic surface.** It retains primitive/repetition, stability, Selberg zeta, Laplace quantization and \(e^T/T\) counting without rational-prime labels. Any criterion it passes cannot establish A0.
2. **Raw Deninger space without admissibility.** It has too many periodic orbits; arithmetic origin alone does not solve multiplicity.
3. **Constant-roof Hénon suspension.** It retains conservative map geometry and a closed-orbit ledger interface, but all periods lie in \(\tau\mathbb N\).
4. **Shuffled/random/composite labels.** Any after-the-fact rank assignment leaves the flow unchanged and is therefore non-intrinsic. The main modular ledger is frozen before the separately declared prime-proxy scan.
5. **Unregularized \(xp\).** It reproduces a desired smooth counting heuristic only after cutoff arguments, but has no nontrivial real periodic orbit.

## Decision

No Stage-1 candidate simultaneously has pass-level arithmetic origin and pass-level primitive isolated-orbit structure. Route B invocation is disallowed. The only justified survivor is an exploratory **interface problem** attached to `DEN-WITT-Z-FIN`: construct a functorial canonical measure/trace on each compact packet and derive its repetition weight without collapsing the packet by hand.
