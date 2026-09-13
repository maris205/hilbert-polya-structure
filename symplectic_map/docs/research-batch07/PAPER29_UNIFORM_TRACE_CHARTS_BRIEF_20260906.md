# Candidate six: uniform optimal trace charts and selection-dependent criticality

Date: 2026-09-06. Candidate identifier:
`uniform_minimal_period_trace_charts_critical_geometry_v1`.
Author synthesis for two fresh independent candidate reviews. This is
not a formal Paper29, manuscript, scientific/publication lock or PASS.
The batch remains at 2/5 locally accepted papers.

## 1. The question and the genuinely changed package

Can exactly as many periodic traces as coefficient parameters provide
uniform local coordinates near quadratic symplectic Hénon powers, with
every period independently prescribed? Which conditioning losses are
unavoidable, and which nearby critical points are artifacts of the
selected observations?

The central new result gives a fixed, nonshrinking coefficient domain
for an explicit selection of exactly $k$ actual cycles, for every
prescribed period vector, while attaining the universal jet order.
Its support design and bounded occupation elimination are new actual
proofs. The previous single-phase selection supplies a comparison:
it attains the same order at the power locus yet has nearby corank-one
critical points for all periods and actual corank-two critical strata
for nonzero resonant occupation imbalance.

This is one local spectral-coordinate problem: unavoidable jet loss
versus avoidable selection-criticality. The fifth candidate's two
page-gate failures remain unchanged. That stopped package had no
fixed-domain resonant selection and its critical result assumed all
macro periods one. This package must be assessed anew, on all its
actual content, without borrowing old scores or merely adding page
estimates. The short $k+3$ redundant-frame preflight is not included.
Neither is the thermodynamic-metric corollary proposed in literature
discussion; it would add assumptions but no substantial new mechanism.

The scope is pure complex polynomial dynamics, not an arithmetic-orbit
or Riemann determinant proposal. `route_applicability: NOT_APPLICABLE`.

## 2. Exact immutable mathematical inputs

Paths below are relative to this directory. Historical pending-check
language in author snapshots remains historical: all listed actual
mathematical claims now have the separate completed checks below.

| Author input | SHA-256 | Use in a single integrated argument |
| --- | --- | --- |
| [Parent spectral jets V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md) | `f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0` | Uniform orbit/spectral estimates, universal obstruction, single-phase coefficient calculation |
| [Original boundary proof](PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md) | `c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9` | Actual moving-column correction and Hessian/Fourier calculation; its period-one theorem becomes a special case, not a second proof |
| [New minimal selection V1](PAPER29_MINIMAL_TRACE_SELECTION_PROOF_V1_20260906.md) | `e726963204552f5ac2b6afa8c05bdf3d224ece19a24337eed018f420cff4fb1c` | Main new fixed-domain, arbitrary-period selection theorem |
| [All-period boundary calculation](PAPER29_ALL_PERIOD_BOUNDARY_PREFLIGHT_20260906.md) | `f39d735da4ba02802e3baa570c043260f4424898e186f9d671696e81b345ffc9` | Oblique occupation projection, four-coordinate Schur block and uniform corank-one curves |
| [Actual corank-two proof](PAPER29_CORANK_TWO_TRACE_BOUNDARY_PROOF_20260906.md) | `f86ef7dd30e98f296abe7b1603dfd6a2e916e8d86382e9cb46dae0d6093b6e21` | Fixed-imbalance actual critical stratum and determinant hypersurface germ |

Completed mathematical checks, all PROVABLE AS STATED:

| Check | SHA-256 |
| --- | --- |
| [Parent jets](PAPER29_CYCLIC_HENON_JET_INDEPENDENT_CHECK_20260905.md) | `ff0144b1324cbdd25718ed017ea3a03611cd84882cd7c6d89abd3ce9b194d984` |
| [Original boundary](PAPER29_CYCLIC_HENON_BOUNDARY_INDEPENDENT_CHECK_20260906.md) | `9e1c22e0182d79398ce50ee840b56b62cb6823a69e5cdba3473af88645a8150c` |
| [Minimal selection, including explicit constant evaluation](PAPER29_MINIMAL_TRACE_SELECTION_INDEPENDENT_CHECK_20260906.md) | `fee2083f80307b07eaf8337016f458fbfa1278f2d3a5dc1d8f7f04934d0690df` |
| [All-period boundary and actual corank two](PAPER29_ALL_PERIOD_BOUNDARY_INDEPENDENT_CHECK_20260906.md) | `2f230867c7e78bf7d0fb3045f86c2b15bc8f29d95425f2be4eb20945bfbba767` |

These are proof checks, not candidate novelty/value/page verdicts.
The minimal-selection check proves the author's determinant constant
$\Delta_k=-3/8$ explicitly; this evaluation is an included proved input.
Unchanged passed arguments need not be restarted as separate audits.
Concrete gaps discovered in the combined claims must still be reported.

Literature inputs:

- [Parent positioning](PAPER29_CYCLIC_HENON_JET_LITERATURE_20260905.md),
  SHA `03ee822d74dc04059ddf89f6253a30708f357bae297241488f0c63f10086b197`.
- [Actual minimal-selection positioning](PAPER29_MINIMAL_TRACE_SELECTION_LITERATURE_20260906.md),
  SHA `6c8cc7abdb284b3d94b1115c358e8331f6c5aa90c34c6b8a2e7ce0ad854b1ed0`.

The latter predates the all-period/corank-two supplements, so its
period-one-only boundary description is superseded by the actual
mathematical inputs above. No novelty claim for general singularity
theory is inferred from that report. The older
[portfolio audit](PAPER29_PORTFOLIO_AUDIT_20260905.md) is used only for
its Papers1–28 comparison table; its old candidate recommendation is
not current. Section 6 gives the relevant updated difference.

## 3. Main theorem: optimal prescribed-period charts on a fixed domain

Fix $k\ge2$, index phases modulo $k$, and set
$$
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\qquad
c_j=\epsilon^{-2}(u_j-1).
$$
All factors have Jacobian one and $F_{\epsilon,0}=H_{-\epsilon^{-2}}^k$.
For a marked exact macro-period-$n_p$ cycle write
$$
\rho_p=\operatorname{tr}DF^{n_p},\qquad
K_{pj}=\frac1{n_p\rho_p}\partial_{u_j}\rho_p.
$$
The parameter $\epsilon$ is held fixed in differentiation; a macro
iterate is one iterate of the composite $F$.

**Universal loss.** For every selection of $k$ periodic branches,
$$
\det K(\epsilon,0)=O_k(\epsilon^{r_k}),\qquad
r_k=\begin{cases}k-1,&6\nmid k,\\k+1,&6\mid k.\end{cases}
$$
The orbit construction exhausts all complex periodic points in the
domain, so this is not only a bound on a preferred symbolic subset.
The elementary Fourier resonance itself is not a novelty claim.

**Uniform selection.** For every independently prescribed vector of
$k$ positive macro periods, explicit pairwise-disjoint simple cycles
with nonzero traces can be chosen on a common product domain
$$
0<|\epsilon|<\epsilon_0(k),\qquad\|u\|_\infty<\eta(k)
$$
so that their normalized differential has singular values comparable to
$$
\begin{cases}
(1,|\epsilon|^{[k-1]}),&6\nmid k,\\
(1,|\epsilon|^{[k-3]},|\epsilon|^2,|\epsilon|^2),&6\mid k.
\end{cases}
$$
Square brackets denote multiplicities. All constants are independent
of the prescribed periods, though $k$ is fixed. Exactly $k$ raw traces
are observed. The bound is optimal in jet order at $u=0$; minimal
observation count is the separate elementary dimension bound.

For $6\nmid k$, use the parent single-negative-phase words. For
$6\mid k$, put $d=k-3$ and take the $k$ nonempty minus sets
$$
B_0=\{1,\ldots,d\},\quad B_i=\{i\}\ (1\le i\le d),\quad
B_\alpha=\{1,2\},\quad B_\beta=\{2,3\}.
$$
At period one use its base block; at period $n_p\ge2$ use $n_p-1$
base blocks and a unique all-plus marker. Three permanently positive
phases isolate all distance-one/two active correlations within a macro
block. Put $a_p=1$ or $1-1/n_p$ respectively and $w_p=1/a_p\in[1,2]$.
For the displayed row order the exact coefficient is
$$
\det K(\epsilon,0)=-\frac38\left(\prod_pa_p\right)
\Gamma(w)\epsilon^{k+1}+O_k(\epsilon^{k+2}),
$$
$$
\Gamma=w_0+w_\alpha+w_\beta-\sum_{i=1}^dw_i-w_1-2w_2-w_3
\le2-d\le-1.
$$
Uniform bounded row elimination cancels the first two coefficients in
two output combinations identically in $u$, not just at $u=0$.
This is the fixed-domain improvement; it is not a change to the
derivative normalization or a pointwise choice among redundant minors.

## 4. Comparison theorem: criticality of the single-phase selection

For $6\mid k$, retain the old selection with minus phase $j$ in its
base block for row $j$, with independently prescribed periods. It
attains the universal power-locus order too, but does not stay full
rank on a fixed $u$ neighborhood. Put $a_j,w_j$ as above,
$W=\sum_jw_j$, $P(a)=(\prod_ja_j)W$, and use
$$
V_\pm=\frac1k\sum_jv_je^{\mp i\pi j/3},\quad
Z_\pm=\frac1k\sum_jv_je^{\mp2\pi i j/3},\quad
\omega_\pm=\frac1W\sum_jw_je^{\mp i\pi j/3}.
$$
The complex $v$ coordinates are independent; only the real occupation
weights imply $\omega_-=\overline{\omega_+}$.

On every fixed bounded $v$ domain, the normalized determinant
$D_{\boldsymbol n}(\epsilon,v)=\epsilon^{-(k+1)}
\det K_u(\epsilon,\epsilon v)$ extends holomorphically, and
$$
D_{\boldsymbol n}(0,v)=-\frac{3k^2}{32}P(a)\mathcal P_a(v),
$$
$$
\mathcal P_a(v)=1-4Z_+Z_-+2(\omega_+V_-+\omega_-V_+)
+4(Z_+\omega_-V_-+Z_-\omega_+V_+).
$$
Here remainders are period-uniform on compact domains. The actual
rescaled matrix has a holomorphic Schur complement whose limit is
$$
R_a(v)=\frac34\begin{pmatrix}
1+2\omega_+V_-&-2Z_++2\omega_+V_+\\
-2Z_-+2\omega_-V_-&1+2\omega_-V_+
\end{pmatrix}.
$$
Both the moving common-row column correction and the occupation
oblique projection are necessary for this coefficient. The other
Fourier blocks need not remain diagonal.

Along $v_j=t\cos(2\pi j/3)$ the leading polynomial is $1-t^2$
for every period vector. Actual critical curves
$t_{\boldsymbol n,\pm}(\epsilon)=\pm1+O_k(\epsilon)$ exist with
uniform estimates, and the selected differential has rank exactly
$k-1$ there. The underlying state cycles remain simple and disjoint.

For a fixed period vector with $\omega_+\omega_-\ne0$, the four
Fourier coordinates control all four entries of $R_a$ independently.
Its zero matrix is at
$$
V_+^*=-\frac1{2\omega_-},\quad V_-^*=-\frac1{2\omega_+},\quad
Z_+^*=-\frac{\omega_+}{2\omega_-},\quad
Z_-^*=-\frac{\omega_-}{2\omega_+}.
$$
The actual Schur complement, not just its leading determinant, gives
a nearby smooth codimension-four family of rank-$k-2$ points. For
each fixed small nonzero $\epsilon$, the actual determinant
hypersurface germ is a nonvanishing analytic unit times
$$x_{11}x_{22}-x_{12}x_{21}=0,$$
with the remaining $k-4$ coordinates free. Across $\epsilon=0$ this
unit statement applies to the normalized determinant, not raw
$\det K$ with its factor $\epsilon^{k+1}$.

This is a short classical inverse/implicit-function consequence of
the actual four-coordinate Schur block, not a new classification of
singularities or a normal form for the full trace map. Its constants
may depend on the fixed nonzero imbalance. In the balanced case
$\omega_\pm=0$, the actual Schur trace is $3/2+O(\epsilon)$ on
bounded $v$ sets, excluding corank two there. The unbalanced centers
escape as imbalance vanishes; no uniform transition theorem is claimed.

The new selection in Section 3 is full rank at these old-selection
critical points once $\epsilon$ is sufficiently small. Thus neither
corank-one nor these corank-two criticalities imply a common
infinitesimal kernel of the whole marked periodic spectrum. This is
the direct conceptual comparison, not a separate global rigidity theorem.

## 5. Integrated proof load and required deductions

The orbit and spectral input is proved once: uniform sign-disc
continuation, exhaustion, return-line Riccati contraction, conversion
from multiplier to the actual normalized trace, and period-uniform
holomorphic Taylor remainders. The universal first jet is then one
Fourier calculation. The second jet is derived once with both the
orbit displacement and Riccati correction, giving phase, adjacent-pair
and distance-two terms.

The main new selection proof uses this common input but has additional
obligations: macro-boundary-safe supports, binary polarization with
$a_p$ rather than $a_p^2$, uniformly invertible weighted elimination,
the complementary Fourier minor, resonant restrictions, and the
strict sign certificate for $\Gamma$. It yields a bounded inverse
after scaling output rows by $1,\epsilon^{[k-3]},\epsilon^2,\epsilon^2$.
The original normalized rows retain the stated conditioning loss.

The critical section uses the single-phase occupation matrix and
its exact coefficient, eliminates the moving zeroth row, and computes
the Hessian coupling followed by the oblique projection. Only the
nonresonant block is inverted, including at critical points. The
period-one cylinder is a special case of the all-period calculation;
it is not written out as a repeated theorem and proof. Corank two
then costs the actual short Schur/IFT argument, not a chapter of
general singularity theory.

Deduct the following completely as independent mechanisms: symbolic
anti-integrable continuation as a concept; Fourier eigenvalues and
Vandermonde products; Cauchy and finite-dimensional perturbation
tools; implicit/inverse function theorems; the dimension lower bound;
the component-level incidence Jacobian criterion. State/prove their
specialized uses only at the length required for this argument.
Omit the redundant $k+3$ frame, the old resonant thin-wedge sufficiency
proof now superseded by fixed-domain coordinates, and metric claims.

## 6. External and portfolio separation

The bound literature reports identify checked primary sources and
finite-search limitations. Particularly important are:

- Gorbovickis: prescribed-period multipliers and a common monomial
  witness for one-variable polynomials are known. Minimal-size
  prescribed-period coordinates as an abstract concept are not new.
- Cantat–Dujardin: complete spectra in fixed multidegree/multi-Jacobian
  families determine only finitely many conjugacy classes, with finite
  determination and even a period-subsequence version. This does not
  yield a fixed list of $k$ prescribed-period observations, uniform
  conditioning, or a pointwise full-rank chart on this product domain.
- Sterling–Meiss and anti-integrable work supply the established
  all-word continuation setting. Hill/orbit-Jacobian methods concern
  state derivatives, not this coefficient-to-selected-traces Jacobian.
- Bianchi–He supply relevant full-spectrum/thermodynamic context.
  Neither quantitative metric lower bounds nor their assumptions
  are added as theorems here.

The local portfolio differences are specific:

| Nearest work | Occupied contribution and deduction | New package difference |
| --- | --- | --- |
| P4 | Arithmetic multiplier-unit obstruction for Hénon factors/compositions | No arithmetic conclusion here; the coefficient spectral geometry is different |
| P12/P15 | Formal trace moments, finite truncations and special trace fibers | Actual individually marked cycles of a multi-factor map; no repeated global reconstruction claim |
| P13 | Primitive cycle marking and scalar-family cover/monodromy structure | Marking is background; no new cover irreducibility or monodromy theorem |
| P18 | Scalar boundary marked traces and generic Jacobian slice/Fitting arguments | Incidence consequences are discounted; no safe-support occupation elimination, universal resonant jet or fixed-domain selection supplied there |
| P20–P28 | Degree/support selectors, propagation matrices and selector monodromy | Current matrices differentiate actual state-periodic traces, not degree propagation |
| Earlier stopped P29 scalar candidate | Uniform separated-root trace coordinates for one factor | Its continuation idea is discounted; the resonant multi-factor coefficient defect and its explicit selection resolution are different |
| Stopped fifth candidate | Universal jets and one attained selection, with period-one critical cylinder | Necessary jets are reused once; fixed-domain resonant selection and all-period actual critical geometry genuinely change the present claims |

Finite search found no source stating the exact new result. That is
not a proof of worldwide novelty. Reviewers should score the actual
delta after every deduction, not the breadth of neighboring literature.

## 7. Natural body estimate: a challengeable plan, not certification

The locked project target remains 22–30 substantive English main-body
pages, proofs in the body and references excluded. No manuscript has
been made, so no observed count exists. The fifth package failed its
own natural-body gate. This package must have its own deduplicated
estimate; neither summing old estimates nor stretching layout suffices.

An author working allocation is **23.25 pages**:

| Integrated section | Working pages | Mathematical content |
| --- | ---: | --- |
| Introduction and exact positioning | 2.50 | One question, main contrast and closest-source distinctions |
| Setup and main statements | 2.00 | Macro periods, actual traces, both selections, full quantifiers and normalization |
| Uniform branches and spectral derivatives | 3.25 | Necessary specialized analytic proof once, including exhaustion and trace correction |
| Universal first and second jets | 3.50 | All-word obstruction, second-order correlations and resonant recovery; no repeated Fourier preliminaries |
| Optimal charts on a fixed coefficient domain | 5.25 | Nonresonant case briefly; safe support, independent occupations, weighted elimination, complementary minor, exact coefficient and uniform singular values |
| Critical geometry of the single-phase selection | 6.00 | Its occupation prefactor, moving-row Hessian calculation, oblique Schur block, all-period curves, actual corank-two stratum and balanced comparison |
| Short consequences and conclusion | 0.75 | Component-level generic étaleness, full-spectrum no-common-kernel comparison, precise limits |
| Total | 23.25 | No administrative prose, appendix, bibliography or decorative material counted |

The 6-page critical allocation includes the essential inherited
boundary calculation plus the new all-period and actual-rank steps;
it does not count three independent boundary proofs. The new selection
alone was independently estimated at 3–5 net pages; the all-period
increment at 2–4 and the subsequent corank-two step at 1–2. Those
incremental comments are not certificates for this integrated total.
Reviewers must replace this working allocation with an independent,
compact yet complete plan. Under 22 natural substantive pages is
FAIL for this task even when the mathematics is valid and useful.

## 8. Claim guards and identical independent-review request

- Derivatives are in $u$. $K_c=\epsilon^2K_u$; on $u=\epsilon v$
  one has $K_v=\epsilon K_u$. Determinants change accordingly.
- Uniformity is in all prescribed periods for each fixed $k$.
  Corank-two neighborhoods explicitly depend on nonzero imbalance.
- Universal optimality is at the power locus, not all parameters.
  Observation-count minimality is merely dimension, not uniqueness.
- Simplicity and disjointness are for actual macro cycles of $F$;
  criticality here is not a state-space bifurcation.
- No global inverse map, all-component incidence theorem, generic
  selection classification, full trace-map germ classification,
  arbitrary factor degrees/Jacobians or arithmetic conclusion is made.
- The intrinsic full-spectrum comparison and algebraic consequence
  are short deductions, not additional headline mechanisms.

Two fresh mutually blind readers receive exactly this package. Read
the full author inputs, completed mathematical checks, positioning
reports and current portfolio difference. Do not read the other fresh
reader's report. Reuse passed proof evidence without a ritual re-audit,
but report concrete newly found errors or overclaims. Primary-source
checks may be bounded to an actual possible collision.

In **each** independent assessment all of the following are required:
novelty $\ge7.5/10$, research value $\ge7.5/10$, proof confidence
$\ge9/10$, and credible 22–30 substantive body pages after deductions.
Give separate scores, an independent section-level page estimate,
confidence, claim limits and a clear overall verdict. No combining
the best dimensions of different reports. No favorable score can
compensate for an inadequate body estimate. No artificial expansion
or unrelated theorem can be prescribed to force a PASS.

The outcome is PASS only if every condition holds for this same
actual changed package; otherwise FAIL / WRITE NOTHING for formal
Paper29. Accepted old papers and stopped candidate files stay intact.
The review uses the research-review discipline with xhigh independent
local agents because the named Codex MCP review channel is not
configured; exact underlying model identity is not asserted.
