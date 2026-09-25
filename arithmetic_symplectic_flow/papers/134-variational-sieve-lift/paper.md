# A finite causal-sieve potential gives canonical geometry and excess periodic multiplicity

**Paper ID:** `134-variational-sieve-lift`  
**Candidate ID:** `ASFS-20260914-VSL01`  
**Date:** 2026-09-14  
**Status:** `P0 GEOMETRY ESTABLISHED; A0 SCOPED FAIL — FINITE SOURCE EQUILIBRIUM; PERIOD-6 CONTINUUM CONTROL`  
**Evidence:** exact elementary derivation; no orbit search.  
**Route state:** scoped A0 admission failure; planned periodic/analytic
structural controls only; formal Route coordinates `NOT EVALUATED`;
Route B `NOT INVOKED`.

## 1. One frozen object

The [version-1 candidate card](candidate-card.md) fixes the real configuration
q=(q_2,q_3,q_4), G(q)=(1,1,1-q_2), and

\[
V(q)=\frac12\big[(q_2-1)^2+(q_3-1)^2+(q_4-1+q_2)^2\big],
\qquad F(x,y)=(y,2y-x-\nabla V(y)).
\]

| Item | Frozen definition and owner |
| --- | --- |
| Phase space | M=R^3_x times R^3_y, coordinates labelled 2,3,4 |
| Form | omega=sum_{i=2}^4 dx_i wedge dy_i |
| Base map | the exact F above; no adjustable coefficient |
| Arithmetic data | divisibility exclusion on the fixed window 2,3,4; no supplied prime vector |
| Roof | tau=1 on every point of M |
| Suspension | (M times [0,1]) with (z,1) identified with (Fz,0), translation flow |
| Measure | Liouville volume times unit time, without probability normalization |
| Primitive convention | least positive base period; cyclic phases identified; positive flow orientation |
| Analytic proposal | ordinary unweighted primitive product, one factor per full base cycle |
| Operator / later lift | none supplied; DEFERRED |

The unit roof supplies the same non-Zeno clock everywhere. The suspension is
seven-dimensional; the proved symplectic structure belongs to its
six-dimensional base. No Hamiltonian or contact owner is asserted for the
suspension itself.

## 2. Source, lineage, and question

The causal binary rule studied in [050](../050-causal-binary-sieve-fixed-point-screen/paper.md)
declares n active when no active candidate divisor m with 2<=m<=sqrt(n) divides
n. On indices 2 and 3 the test set is empty, giving the constant 1; on index 4
the only tested divisor is 2, giving 1-q_2. Thus the real polynomial G here
agrees exactly with that binary rule on this window. Its extension to real
coordinates and the squared residual potential are constructions of this
candidate, not claims attributed to the binary-sieve source. The defining rule
was rechecked in the author's [primary TeX source](https://zenodo.org/records/19894709/files/Fluctuation.tex?download=1),
under the definition titled Causal sieve operator.

The documented arrow from the [prior-work lineage](../../docs/prior_work/README.md)
is causal prime/composite admissibility to a real residual potential to a
reciprocal Henon-type canonical map. The precise preserved object will be the
finite source fixed-point equation. This does not provide a conjugacy of the
complete source evolution, an infinite-coordinate realization, or an all-prime
orbit mechanism.

The bounded questions are whether this explicit deformation is symplectic,
whether it preserves the source equilibrium without additional stationary
solutions, and whether its full primitive multiplicity permits the frozen
ordinary zeta proposal. The source window is fixed before the audit; it is not
increased or optimized after a failure.

## 3. Geometry and equilibrium: exact positive controls

### Proposition 1 — Global canonical map

F is a smooth symplectomorphism of the frozen M. Its inverse is

\[
F^{-1}(X,Y)=(2X-Y-\nabla V(X),X).
\]

**Proof.** Substitution verifies the inverse globally. Write H for the Hessian
of V. Then

\[
F^*\omega
=\sum_i dy_i\wedge\left(2dy_i-dx_i-\sum_jH_{ij}dy_j\right)
=\sum_i dx_i\wedge dy_i=\omega,
\]

because H is symmetric. There are no singularities or excluded points. QED.

### Proposition 2 — Unique source-derived equilibrium

The unique fixed point of F is x=y=q_*=(1,1,0).

**Proof.** Put E(q)=q-G(q). Its constant Jacobian in coordinate order 2,3,4 is

\[
A=DE=\begin{pmatrix}1&0&0\\0&1&0\\1&0&1\end{pmatrix},\qquad\det A=1.
\]

Since V=||E||^2/2, the equation grad V=A^T E=0 is equivalent to E=0.
Solving E(q)=0 gives q_2=1, q_3=1, q_4=0. A fixed point of F must satisfy
x=y and grad V(y)=0, proving the claim. QED.

This derivation produces the prime/composite values on the three frozen
indices from the rule; they were not inserted as a selected equilibrium.
The preservation is nevertheless only a finite stationary result. No
arithmetic statement for indices beyond 4 follows for this map.

## 4. Planned full-multiplicity precheck

### Proposition 3 — An invariant continuum of primitive six-cycles

The plane

\[
\Pi=\{x_2=y_2=1,\ x_4=y_4=0\}\subset M
\]

is invariant. Every point of Pi except (q_*,q_*) has exact primitive base
period 6. After cyclic identification, there are uncountably many distinct
primitive cycles in this plane.

**Proof.** Direct differentiation gives

\[
\nabla V(q)=(2q_2+q_4-2,\ q_3-1,\ q_4+q_2-1).
\]

The coordinates labelled 2 and 4 therefore remain at 1 and 0 on Pi.
For u=x_3-1 and v=y_3-1 the restriction is the linear map

\[
\binom uv\longmapsto C\binom uv,
\qquad C=\begin{pmatrix}0&1\\-1&1\end{pmatrix}.
\]

Its eigenvalues are the primitive sixth roots exp(plus/minus i*pi/3). Hence
C^6=Id, while C^k-Id is invertible for every 1<=k<6. Every nonzero vector
has least period 6. Each cycle has six points, so quotienting the uncountable
punctured plane by these finite cyclic classes still leaves uncountably many
cycles. One can see distinct packets explicitly from the invariant
Q(u,v)=u^2-u*v+v^2: the points (a,0) for a>0 have distinct Q-values and thus
belong to distinct cycles. QED.

Under the same unit roof each such base cycle gives one primitive suspension
orbit of length 6, whose r-th repetition has length 6r. The unique base fixed
point separately gives a length-one suspension orbit. The derivative of F^6
is the identity on tangent directions to Pi, so this family is degenerate and
non-isolated. We do not classify any remaining periodic points of M.

### Corollary — Frozen unweighted zeta cannot converge in a right half-plane

Take any real s>0 and any positive integer L. Select L distinct cycles from
the established six-cycle family, retaining their actual multiplicity. Their
partial product equals

\[
Z_L(s)=(1-e^{-6s})^{-L},\qquad
\log Z_L(s)=-L\log(1-e^{-6s})\longrightarrow+\infty.
\]

Thus even this subfamily precludes convergence of the precommitted ordinary
unweighted primitive product on every positive real s, hence in any right
half-plane. This is a direct obstruction to that frozen product, not an
assertion about every possible regularized trace or a different weighted
operator. Any such alternate object would require a new card.

The period and product calculations are the planned structural precheck. They
do not advance a failed A0 candidate into formal A1/A2 evaluation.

## 5. Adversarial controls and scope

| Control | Result and relevance |
| --- | --- |
| Finite source versus global claim | The input index window ends at 4. The equilibrium recovers that window only; no source action on further integers belongs to M. |
| Full periodic ledger versus selected equilibrium | Pi minus its centre contains uncountably many primitive six-cycles. Keeping only the centre discards the frozen map's intrinsic packets. |
| Scalar nonarithmetic comparator | The period-six formula uses only V's scalar term (q_3-1)^2/2. The same harmonic recurrence occurs without the divisor coupling and supplies no all-prime specificity. |
| Reciprocal versus causal update | grad V=A^T E is a reciprocal force. What is proved to survive from G is E=0, not its entire time evolution or periodic ledger. |
| Primitive phase quotient | Dividing each cycle into one cyclic class removes only six phases, not the continuum of distinct amplitudes. |
| Roof/normalization | Every established primitive six-cycle has actual length 6 under tau=1. No logarithmic roof, weights, or sample-dependent normalization is inserted. |
| Finite packet thickening | The geometric carrier does not retain the source's singleton periodic multiplicity. Its full period-six family cannot be erased by selecting a centre or section. |
| Cutoff/precision | All statements concern the exact frozen six-dimensional map. No numerical orbit cutoff or floating-point evidence is used; no parameter sweep is run. |

## 6. Gate assessment and stop decision

| Obligation | Exact evidence | Status |
| --- | --- | --- |
| P0 geometry | global symplectomorphism, fixed unit roof, defined suspension | ESTABLISHED for this frozen candidate |
| Finite source preservation | unique equilibrium solves the exact finite causal rule | ESTABLISHED local positive control |
| A0 admission | finite stationary window supplies no all-prime action/packet/clock mechanism | scoped FAIL |
| Full periodic multiplicity | uncountably many exact primitive six-cycles under the same map and roof | ESTABLISHED adverse structural precheck; formal A1 NOT EVALUATED |
| Frozen product | arbitrary finite subproducts already diverge as L grows for every real s>0 | scoped analytic obstruction; formal A2 NOT EVALUATED |
| Other periods and alternate analytic theories | not needed after stop | OPEN / NOT INVESTIGATED |
| Formal Route A | no tuple or target/divisor evaluation | NOT EVALUATED |
| Route B | no entry or evaluation | NOT INVOKED |

**Decision: stop**, portfolio `fork`. The exact geometric construction is a
useful control: the finite sieve equilibrium can survive a canonical
reciprocal lift, but neither global arithmetic coverage nor the source's finite
periodic multiplicity follows. This packet keeps the full map, roof, and orbit
ledger. No coefficients, domain, invariant subset, or dimension are altered
to continue the candidate.

## Evidence index

See the [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[source and verification record](evidence/README.md), and
[package overview](README.md). The explicit proofs are the evidence for the
mathematical results; document validation alone supplies no gate credit.
