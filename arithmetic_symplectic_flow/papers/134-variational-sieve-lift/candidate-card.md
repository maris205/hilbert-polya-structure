# Candidate card — ASFS-20260914-VSL01

**Version:** 1, frozen before audit, 2026-09-14.  
**Initial status:** P0 SPECIFICATION FROZEN — GEOMETRY/ARITHMETIC AUDIT OPEN.

This is a new reciprocal-force construction. No credit from 133 is transferred.

| Field | Frozen specification |
| --- | --- |
| Phase space and form | \(\mathbb R^3_x\times\mathbb R^3_y\), coordinates labelled 2,3,4; \(\omega=\sum_{i=2}^4 dx_i\wedge dy_i\) |
| Source | exactly \(G(q)=(1,1,1-q_2)\), the real divisor-polynomial restriction of 050 |
| Potential | \(V(q)=\tfrac12[(q_2-1)^2+(q_3-1)^2+(q_4-1+q_2)^2]\) |
| Map | \(F(x,y)=(y,2y-x-\nabla V(y))\), no free parameter |
| Data/provenance | fixed first nontrivial divisor window 2,3,4 selected for analytic geometry test; no supplied prime vector, weights, zero data, parameter fit |
| Lineage | causal prime/composite rule → squared residual potential → reciprocal Hénon-type canonical map; source-equilibrium preservation must be proved anew |
| Roof and suspension | \(\tau=1\); \((z,1)\sim(Fz,0)\) in \((M\times[0,1])/\sim\); translation flow; non-Zeno from unit roof |
| Measure | standard Liouville volume on M, not normalized to probability; product with unit time on suspension |
| Primitive/repetition convention | least positive base period, cyclic phases identified, one positively oriented flow orbit per base cycle; full multiplicity retained |
| Arithmetic question | whether source-derived equilibrium and any primitive packets provide an endogenous all-prime mechanism beyond this finite window; OPEN |
| Analytic convention | if admissible, ordinary unweighted primitive product \(Z(s)=\prod_\gamma(1-e^{-sT_\gamma})^{-1}\); existence/convergence OPEN, no operator supplied |
| Controls | full orbit ledger versus selected equilibrium/centre; scalar coordinate3 comparator; finite source-window limitation; same unit roof |
| Future lift | DEFERRED; no Route B |
| Planned decisive tests | symplecticity, unique source-equilibrium equation, full-multiplicity obstruction in decoupled coordinate3; stop on A0 or A1 failure |

The card defines one finite-dimensional candidate. An all-coordinate family,
different potential, different roof or selected invariant subset is a new
object. No global prime coverage is assumed.

## Version 1 audit outcome — 2026-09-14

**Current status:** `P0 GEOMETRY ESTABLISHED; A0 SCOPED FAIL — FINITE SOURCE EQUILIBRIUM; PERIOD-6 CONTINUUM CONTROL`.

The frozen F is a global canonical symplectomorphism, with its unique fixed
point at x=y=(1,1,0), derived from the residual equation q=G(q). This is exact
preservation of the finite source equilibrium, not a global prime mechanism.
The A0 admission test therefore fails in the finite/static scope.

The planned periodic-multiplicity precheck additionally exhibits a whole
invariant plane on which all nonzero centered states have primitive period 6.
Its uncountably many cyclic packets all have primitive flow length 6 under the
same unit roof. The precommitted unweighted primitive product diverges on every
real s>0. This is a structural control, not a formal A1 or A2 evaluation after
the A0 stop. The rest of the periodic set is not classified.

**Decision:** `stop`; portfolio `fork`. Formal Route coordinates are
`NOT EVALUATED`; Route B is `NOT INVOKED`. See [paper](paper.md) and
[claim ledger](claim-ledger.md). The original object and all its periodic
multiplicity are retained; no subset, roof, or parameter is substituted.
