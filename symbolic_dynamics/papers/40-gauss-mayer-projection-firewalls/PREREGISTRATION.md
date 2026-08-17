# Paper 40 authority-writer freeze — SD-C42

## 1. Status and chronology

This document freezes the authority writer's manuscript decisions after the
corrective Paper-40 research package was independently replayed and sealed,
and before the writer consumed any integrator-declared `FINAL` experiment
block. It is not a scientific preregistration and carries no novelty credit.
The corrected M1--M20 inputs were frozen before the single canonical
replacement run; provisional v1 results and multiple in-flight corrective
smoke tests were already known. The eleven immutable research renderings are
post-run files incorporating M21--M25 and the replacement literature audit.

`RESEARCH_LOCK.sha256` enumerates those eleven immutable research files.
This writer freeze, all manuscript files, figures, compilation outputs, and
the future integrator block are deliberately excluded from that acyclic lock.

## 2. Paper identity and claim boundary

- Candidate: `SD-C42`.
- Preferred title: **Trace, Order-Discriminant, and Norm Firewalls for the
  Two-Digit Gauss--Mayer Determinant**.
- Contribution: for one exactly typed two-digit/even-iterate Gauss--Mayer
  contract and exactly three declared scalar projections, prove that no
  projection satisfies the full rational-prime reciprocal-Euler-ledger
  conjunction, while retaining the intrinsic pair ledger and its same-object
  Fredholm determinant.

Paper 1 already owns the qualitative trace/discriminant/norm mismatch, a
large finite collision census, and the request for the next projection audit.
Paper 40 supplies theorem-grade exact closure of that pre-existing request.
It claims no new transfer operator, two-variable zeta mechanism, collision
priority, witness-size optimality, pair/geodesic bijection, or universal
Gauss-map no-go. The corrected M1--M25 cycle itself receives no novelty
credit.

The independent registry rule reads all six historical cards. A card survives
the first filter only when its hash-bound evidence anchor establishes a
nonempty intrinsic primitive/repetition ledger and its exact historical
verdict is `A2_ANALYTIC_DETERMINANT`; the survivors are SD-C01, SD-C02, and
SD-C04. SD-C04 then wins the frozen A3 followed by A4 comparison. P39 is used
only as terminal-clean provenance and neither ranks nor authorizes SD-C42.

## 3. Frozen object and type system

Let

$$
X=\mathbb N^{\mathbb N},\qquad
\sigma(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots)
$$

be the digit space and one-digit shift. Let

$$
X_2=(\mathbb N^2)^{\mathbb N},\qquad
\rho((a_1,a_2),(a_3,a_4),\ldots)
=((a_3,a_4),(a_5,a_6),\ldots)
$$

be the ordered-pair space and one-pair shift. The grouping bijection

$$
\iota(a_1,a_2,a_3,a_4,\ldots)
=((a_1,a_2),(a_3,a_4),\ldots)
$$

satisfies the typed identity

$$
\rho\circ\iota=\iota\circ\sigma^2.
$$

Thus $\sigma^2$ acts on $X$, while $\rho$ acts on $X_2$. One $\rho$ return
consumes two digits and carries marker $u^2$. For a cyclic pair word with
flattened digits $(a_1,\ldots,a_{2k})$,

$$
A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad
M(w)=A(a_1)\cdots A(a_{2k}).
$$

The manuscript keeps the following three types separate:

```text
RhoPrimitivePair
SigmaPrimitiveDigit
GeodesicPrimitiveClass
```

A least-period-$n$ $\sigma$ orbit yields $\gcd(n,2)$ cycles under
$\sigma^2$, each of length $n/\gcd(n,2)$: odd periods remain one cycle and
even periods split into two. Equivalently,

$$
N_{D^2}(k)=2N_D(2k)+\mathbf 1_{k\text{ odd}}N_D(k).
$$

No objectwise bridge among the three primitive types is inferred from the
$u=1$ determinant identity. Global raw-index reversal is only the bijective
bookkeeping needed to express $\mathcal L_s^{2k}$ in stored composition order;
it preserves cyclic pair classes and does not add a reversal quotient.
“Two-digit/even-iterate” never means the distinct even-continued-fraction
algorithm.

## 4. Frozen analytic boundary

On Mayer's disk algebra
$A_\infty(D)$, $D=\{z\in\mathbb C:|z-1|<3/2\}$,
$\mathcal L_s$ is nuclear of order zero for
$\operatorname{Re}s>1/2$. Mayer's Proposition 3 gives the holomorphic
Fredholm identity on that same half-plane:

$$
Z_{\mathrm{PSL}_2(\mathbb Z)}(s)
=\det(I-\mathcal L_s^2)
=\det(I-\mathcal L_s)\det(I+\mathcal L_s).
$$

The initial Selberg Euler product is absolutely convergent only for
$\operatorname{Re}s>1$, and Mayer's Corollary 3 supplies the separately
qualified meromorphic continuation to $\mathbb C$. These three domains may
not be collapsed.

For $K_s=\mathcal L_s^2$,
$D_{42}(s,u)=\det(I-u^2K_s)$ is a same-space Fredholm family in the nuclear
half-plane. Its logarithmic trace series and intrinsic primitive-pair product
are used coefficientwise/formally in $u^2$, or analytically for sufficiently
small $|u|$ with the local logarithm at $u=0$. The $u=1$ identity is invoked
only through Mayer's theorem; no arbitrary-$u$ Selberg semantics or global
logarithm across determinant zeros is claimed.

Complex operator weights use Mayer's fixed holomorphic logarithm branch.
Only at a positive real fixed point may the multiplier be written
$d_w=|\Phi_w'(x_w)|=\lambda(w)^{-2}$.

## 5. Frozen theorem and witnesses

For every `RhoPrimitivePair` word, the manuscript proves the exact
Gauss-branch/matrix bridge and the following universal statements for
$t=\operatorname{tr}M\ge3$:

1. $\Delta_{\mathbb Z[M]}=t^2-4=(t-2)(t+2)$ is prime exactly at
   $(t,\Delta)=(3,5)$;
2. $(t-1)^2<\Delta<t^2$, so $P_N=\lambda^2$ is irrational;
3. $T=2\log\lambda=\log\lambda^2>\log t$, and no constant rescales
   $\log t$ to $T$ on all realized traces;
4. $q_r=tq_{r-1}-q_{r-2}$ with $q_0=2$, $q_1=t$, so
   $q_2=t^2-2\ne t^2$.

The paper then gives three explicit in-domain collision classes, without
priority or size-optimality language:

1. trace $4$: `((1,2))` versus `((2,1))`, distinct reversal phases because
   only pair rotations are quotiented;
2. trace $6$: `((1,4))` versus `((2,2))`, a one-pair non-reversal collision;
3. trace $10$: `((2,4))` versus `((1,1),(1,2))`, a non-reversal,
   cross-pair-length collision.

The full ledger contains the composite trace species `((1,2))`, and none of
$P_t=t$, $P_\Delta=t^2-4$, or $P_N=\lambda^2$ has a declared reducing
projector or selected Fredholm owner in the frozen untwisted schema.

The intrinsic pair determinant is proved directly in the nuclear domain:

$$
-\log\det(I-u^2K_s)
=\sum_{n\ge1}\frac{u^{2n}}n\operatorname{Tr}(K_s^n)
=\sum_{[v]}\sum_{r\ge1}
 \frac{u^{2k(v)r}d_v^{rs}}{r(1-d_v^r)}
$$

in the local/formal sense above. Cyclic multiplicity $k(v)$ cancels the
$n=k(v)r$ denominator. This supplies same-object pair-ledger ownership and
does not import an objectwise geodesic bijection.

## 6. Frozen decision semantics

The complete projection predicate includes rational-prime support,
one-to-one target multiplicity, temporal powers, unchanged clock and marker,
weight/amplitude and sign, orientation and phase, operator ownership, and all
mandatory controls. In the exact truth matrix:

- $P_t$ and $P_\Delta$ are integer-valued but fail both the exact clock and
  temporal powers;
- $P_N$ preserves the exact clock and temporal powers but is irrational and
  retains the source stability denominator/Selberg tower;
- all three fail the complete rational-prime reciprocal-Euler-ledger
  conjunction and lack a declared scalar-selected owner.

The strict Route tuple is

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

and the terminal tuple is

```text
GO_MODULAR_PRIMITIVE_LEDGER
GO_SAME_OBJECT_MAYER_DETERMINANT
STOP_CANONICAL_INTEGER_PROJECTION
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

The second STOP is narrow: no integer-valued projection also preserves both
clock and powers. It does not say that $P_N$ fails those two tests. The two GO
codes refer only to the intrinsic pair ledger and its same-space determinant.

## 7. Manuscript and figure freeze

The modular A4 manuscript will contain seven numbered sections, two
appendices, and exactly three writer-owned vector TikZ figures:

1. the typed digit-to-pair return, object--marker--operator chain, and
   three-projection gate;
2. the universal algebraic firewalls plus all three explicit collision
   classes; and
3. the primitivity-splitting, analytic-domain, and selector-ownership
   firewalls.

No figure contains a provisional experiment count, raster image, or
integrator-owned artifact.

## 8. Integrator and writer QA gates

Only an explicit `FINAL / CLEAN` canonical block from the designated
integrator may be inserted, once and verbatim in substance, into mutable
narrative and manuscript artifacts. The writer will not create or modify
`code/**`, `results/**`, `experiments/**`, `evaluations/**`, `docs/**`, or
`EXPERIMENT_REPORT.md`.

Compilation will occur only after integration and in a fresh out-of-tree
directory. Two internal rounds are required:

1. mathematics, source domains, novelty, type, ownership, Route semantics,
   and canonical-result fidelity;
2. narrative, bibliography, figures, typography, page boundaries,
   stale-file and path hygiene, font embedding, and clean-tree checks.

No external review loop is authorized.
