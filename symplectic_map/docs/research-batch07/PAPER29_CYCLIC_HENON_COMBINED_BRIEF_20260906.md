# Paper29 candidate brief: optimal trace-differential jets near Hénon powers

Date: 2026-09-06. Candidate identifier:
`quadratic_symplectic_henon_power_locus_optimal_jets_v1`.
This is an author-side synthesis for two independent candidate reviews,
not a formal project, scientific/publication lock, manuscript or PASS.
The same complete package is to be assessed by both readers. Papers27–28
remain accepted; the batch count remains 2/5.

## 1. Question and one-sentence contribution

How many orders of the normalized periodic-trace coefficient differential
are necessarily lost near an equal-factor quadratic symplectic Hénon
power, can prescribed periods attain the least loss, and where does the
resulting fixed coordinate selection become critical again?

**Contribution:** For quadratic symplectic Hénon compositions, we determine
the universally unavoidable and explicitly attained trace-differential
jet order at the power locus, including the two second-order directions
when the factor count is divisible by six, and resolve the nearby critical
boundary of the fixed-point selection.

This is a single local spectral-parameter geometry question. It is not a
general Hénon reconstruction theorem and not an arithmetic-orbit claim.
`route_applicability: NOT_APPLICABLE` describes scope, not a Route verdict.

## 2. Exact inputs and their different roles

All paths in this section are relative to this directory.

| Input | Binding SHA-256 | Role |
| --- | --- | --- |
| [Main proof V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md) | `f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0` | Complete author proof of the general-factor, arbitrary-period theorem |
| [Boundary supplement](PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md) | `c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9` | Complete author proof for the same fixed-point selection, all resonant factor counts |
| [Literature comparison](PAPER29_CYCLIC_HENON_JET_LITERATURE_20260905.md) | `03ee822d74dc04059ddf89f6253a30708f357bae297241488f0c63f10086b197` | Verified nearest-source positioning, standard-tool deductions, finite-search limitations |
| [Main mathematical check](PAPER29_CYCLIC_HENON_JET_INDEPENDENT_CHECK_20260905.md) | `ff0144b1324cbdd25718ed017ea3a03611cd84882cd7c6d89abd3ce9b194d984` | Independent proof check, not a candidate value/page decision |

The boundary is receiving its own targeted independent mathematical check.
Its final report will be supplied identically to both candidate readers;
no conjectural strengthening is part of this package. The author source
snapshots retain their original pending-review language. The main proof
check is complete: PROVABLE AS STATED, with no remaining substantive gap.
V1 remains unchanged; V2 restores three omitted plus signs in two displays.

The older [portfolio audit](PAPER29_PORTFOLIO_AUDIT_20260905.md) supplies
the Papers1–28 comparison table only. Its recommendations concern a
different, stopped candidate and are not recommendations for this one.
Section 6 below gives the relevant current-candidate delta.

## 3. The exact mathematical package

Fix an integer $k\ge2$ and write, with phases indexed modulo $k$,
$$
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\qquad
c_j=\epsilon^{-2}(u_j-1).
$$
Every factor has determinant one. The point $u=0$ gives
$F_{\epsilon,0}=H_{-\epsilon^{-2}}^k$; the coefficient differential
still varies all $k$ factors independently. For a labeled simple exact
cycle of macro period $n_i$ define
$$
\rho_i=\operatorname{tr}DF^{n_i},\qquad
K_{ij}=\frac1{n_i\rho_i}\frac{\partial\rho_i}{\partial u_j}.
$$
Macro periods count iterates of $F$, not elementary factor steps.
In the following statements $\epsilon$ is held fixed during differentiation.

### A. Universal obstruction and exact attainment

For any $k$ periodic branches, of arbitrary positive periods,
$$
\det K(\epsilon,0)=O_k(\epsilon^{r_k}),\qquad
r_k=\begin{cases}k-1,&6\nmid k,\\k+1,&6\mid k.\end{cases}
$$
Every complex periodic point in the parameter region belongs to the
uniform two-symbol model. Thus the universal quantifier does not merely
range over a handpicked symbolic subset.

For every prescribed positive period vector $(n_1,\ldots,n_k)$, an
explicit disjoint tuple attains this order. In row $i$, use blocks with
a minus sign only in phase $i$. For $n_i=1$ use one such block; for
$n_i\ge2$ use $n_i-1$ such blocks and one all-plus marker. These are
primitive in macro time, including repeated values among the $n_i$.
Put $a_i=1$ if $n_i=1$, and $a_i=1-1/n_i$ otherwise. Then
$$
\det K(\epsilon,0)=-b_kP(a)\epsilon^{r_k}
 +O_k(\epsilon^{r_k+1}),\qquad
P(a)=\sum_i\prod_{j\ne i}a_j\ge k/2^{k-1},
$$
where $b_k=1-\cos(k\pi/3)$ in the nonresonant case, and
$b_k=3k^2/32$ in the resonant case. Bounds are uniform in all periods.

### B. Quantitative rank recovery on a common domain

For the same selection, singular values are uniformly comparable to
$$
\begin{cases}
(1,|\epsilon|,\ldots,|\epsilon|),&6\nmid k,\\
(1,\underbrace{|\epsilon|,\ldots,|\epsilon|}_{k-3},
|\epsilon|^2,|\epsilon|^2),&6\mid k.
\end{cases}
$$
The domain is a fixed small $u$-polydisc when $6\nmid k$ and the
shrinking region $u=\epsilon v$, $\|v\|_\infty<\eta$, when $6\mid k$.
Constants depend on $k$ but not on the prescribed period vector.
This gives $|\det K|\ge c_k|\epsilon|^{r_k}$ and a uniform normalized
conditioning profile, not a global inverse algorithm.

### C. The resonant critical boundary of the fixed-point selection

Now restrict to $6\mid k$ and $n_1=\cdots=n_k=1$, with the same
single-negative-phase words. Set
$$
\widehat v_\pm=\frac1k\sum_{j=0}^{k-1}v_j e^{\mp2\pi i j/3}.
$$
On bounded $v$-sets the holomorphic extension satisfies
$$
D_k(0,v):=\left.\epsilon^{-(k+1)}\det K_u(\epsilon,\epsilon v)
\right|_{\epsilon=0}
=-\frac{3k^3}{32}(1-4\widehat v_+\widehat v_-).
$$
The leading critical cylinder $\widehat v_+\widehat v_-=1/4$ is smooth;
near each of its points there is an actual holomorphic critical
hypersurface for small $\epsilon$. The line
$v_j=t\cos(2\pi j/3)$ gives actual zeros
$t_\pm(\epsilon)=\pm1+O(\epsilon)$, where the selected trace Jacobian
has rank exactly $k-1$ although the marked fixed points remain simple,
disjoint, and have nonzero traces.

Consequently no $\epsilon$-independent $u$-neighborhood makes this same
fixed tuple everywhere full rank for all small nonzero $\epsilon$.
This is a real limitation of that coordinate selection. It does not
exclude other selections, cover arbitrary periods, or classify every
critical component.

### D. Algebraic consequence, counted at its actual weight

For each period vector there is at least one component of the simple,
exact, disjoint cycle-marked coefficient incidence whose trace map is
dominant and generically étale. This follows by the standard incidence
Jacobian criterion and finite free cycle quotient after A–B. It is not
a fourth equally novel mechanism, an all-component theorem, or a global
reconstruction result.

## 4. What must be established beyond routine tools

| Module | Necessary technical content | Evidence location |
| --- | --- | --- |
| Uniform spectral rows | Two sup-norm contractions, exhaustion of all periodic roots, Riccati return line, normalized trace rather than multiplier, period-independent coefficient derivatives and remainders | Main §§3–4 |
| Universal first jet | Every phase-mean row has the same first operator; Fourier columns give a bound for every selection | Main §5 |
| Correct second jet | Both orbit displacement and Riccati correction; adjacent/distance-two correlations; coincident-index convention | Main §6 |
| Attaining periods | Marker exactness and disjointness; cross-macro-boundary occupation factors; matrix $D_a(\epsilon L_1+\epsilon^2L_2)$ | Main §7 |
| Exact determinant and conditioning | Nonconstant eigenvalue products, nonscalar $D_a$, Fourier column scaling to justify remainder order, compact occupation cube | Main §8 |
| Moving coefficient domain | Exact elimination of the moving common row by $Q(u)$; division by $\epsilon^2$ only after $u=\epsilon v$ | Main §9 |
| Actual critical boundary | Hessian coupling of the two resonant modes; retained nonresonant upper-right block; Schur argument valid even at singular resonant block; IFT and exact rank | Boundary §§2–8 |

Here $L_1=I-S-S^{-1}$, while
$L_2=-\frac32I+\frac54(S+S^{-1})-(S^2+S^{-2})$.
The eigenvalue of $L_2$ on each missing first-order mode is $3/4$.
For $k=2$, $S=S^{-1}$ and the repeated neighbor is counted twice;
the second-order correlation formula is not needed there.
The arithmetic fact that $1-2\cos(2\pi\ell/k)=0$ occurs twice iff
$6\mid k$ is elementary and is not itself the innovation.

The boundary's effective block is
$$
R(v)=\begin{pmatrix}3/4&-(3/2)\widehat v_+\\
-(3/2)\widehat v_-&3/4\end{pmatrix}.
$$
It is obtained after accounting for $Q(u)$ and the other directions,
not by assuming all Fourier blocks remain diagonal away from $u=0$.

## 5. External positioning and obligatory deductions

Use the bound literature report for exact versions and checked locations.
The important comparisons, not a bibliography quota, are:

- Gorbovickis: prescribed-period multipliers as coordinates for scalar
  polynomials, even using a common monomial base point. These concepts
  alone are already known; the present full coefficient differential
  is on a special invertible multi-factor family.
- Cantat–Dujardin: complete multiplier/trace spectrum rigidity in fixed
  multidegree and multi-Jacobian families, with finite determination.
  The present result is not the first spectral rigidity statement for
  this family. Its delta is the universal optimal local jet order and
  explicit minimal-size selection with prescribed periods.
- Sterling–Meiss and later anti-integrable work: all-word uniform
  continuation is established. The trace-parameter rank calculation
  is additional, not a new invention of symbolic continuation.
- Hill/orbit-Jacobian and Fourier lattice methods: established state
  stability analysis. Here $K$ differentiates different cycle traces
  with respect to external coefficients; it is not that state Jacobian.
- Bianchi–He: thermodynamic multiplier geometry is pertinent background;
  this finite selected jet calculation is not a global positive-metric
  theorem.

The secondary tools—Cauchy estimates, finite-dimensional perturbation,
Chebyshev products, determinant lemma and IFT—must be credited and
deducted. The critical boundary uses the same jet mechanism as A–B;
its derived geometry is a meaningful limitation, not a second paper.
Finite search found no precise covering theorem but is not a proof of
worldwide novelty. No score in the literature preflight binds reviewers.

## 6. Portfolio non-collision: current-candidate delta

| Nearest local work | Occupied contribution | Difference and deduction here |
| --- | --- | --- |
| P4: integral/$S$-integral Hénon factors | Arithmetic multiplier-unit obstruction, including finite compositions | Same family language does not supply coefficient spectral jets; no arithmetic claim is repeated |
| P12/P15: formal trace fibers | Specific single-factor formal trace moments and finite spectral truncation/fiber results | Present traces are individually marked actual cycles of a factorized map; no claim of improved global reconstruction |
| P13: primitive Hénon cycle covers | Exact-period marking, normalization, monodromy in its scalar boundary family | Marking and exact-period incidence are background here, not a new cover/monodromy theorem |
| P18: marked scalar boundary | Specified-period trace independence near a polynomial boundary, generic Jacobian slice and Fitting base change | Incidence consequence D overlaps methodologically; nonzero symplectic factor composition, universal jet obstruction, attained order, conditioning and fixed-tuple critical cylinder are not supplied by P18 |
| P20–P28 | Hamiltonian weighted/ordinary degree selectors, support rank, matrix visibility and selector monodromy | Present matrices are differentials of actual state-periodic spectra, not degree propagation matrices; no degree theorem is recycled |
| Stopped single-factor Paper29 candidate | Fixed-Jacobian uniform trace coordinates via separated roots | Its method/background is deducted; the current equal-factor power locus has a universal first-order rank loss and two-mode second-order recovery absent from that result |

The comparison uses the existing portfolio table and targeted readings
of P4/P13/P15/P18 problem statements already completed in discovery.
The older common-ray, cancellation and centralizer results are not
included to increase volume. No Paper30/31 question is bundled here.

## 7. Author-side substantive-body feasibility, not a page certificate

The project requires 22–30 main-body pages, with the complete mathematical
argument in the body and references excluded. There is no manuscript
yet and no observed page count. A previous independent check estimated
16–20 natural body pages for the main theorem alone; that estimate did
not include the subsequently completed critical-boundary argument.
Neither raw source length nor the addition of a theorem label proves
that the combined package reaches the floor.

The following is an author working allocation totaling **22.25 pages**.
It is explicitly challengeable; reviewers should replace it with their
own compact complete estimate. Standard inputs should be stated at the
length needed for these specific uniform estimates, not expanded into
a survey or repeated as purported novelty.

| Section | Working pages | Specific content and source |
| --- | ---: | --- |
| 1. Introduction and precise related-work positioning | 3.00 | Specific question, A–C previews, normalization, closest-source distinctions; no general dynamical-systems survey |
| 2. Setup and main statements | 2.00 | Macro time, marking, coefficient/trace normalization, full quantifiers and common-domain theorems |
| 3. Uniform branches and actual spectral differentials | 3.00 | Main §§3–4, exhaustion and exact normalized log derivative with uniform remainder proof |
| 4. The universal first-order obstruction | 2.50 | Main §5, all-word operator and Fourier-column valuation; repeated neighbor case |
| 5. Second-order correlation and resonant recovery | 3.00 | Main §6 and exact $L_2$ derivation; no duplicated contraction setup |
| 6. Arbitrary-period attainment and exact coefficient | 3.00 | Main §§7–8, marker argument, occupation prefactor, product identities and correctly scaled determinant remainder |
| 7. Conditioning and common coefficient regions | 2.50 | Main §§8–9, bounded inverse and moving-row elimination; distinguish derivative coordinates |
| 8. Fixed-selection critical boundary | 2.50 | New supplement compressed to Hessian/Fourier projection, Schur block, critical cylinder and actual rank-loss curves; reuse earlier analytic setup |
| 9. Incidence consequence and conclusion | 0.75 | Main §10, standard component-level consequence and exact limitations |
| Total main body | 22.25 | References start afterward; no appendices, administrative prose or redundant examples count toward this figure |

Some section allocations could be optimistic. In particular the first
jet is short once its actual spectral input is in place, and the
boundary reuses that input. A complete but naturally shorter treatment
does not become eligible by spreading displays, enlarging type/margins,
repeating proof statements, adding unrelated examples or expanding
classical background. If a compact full treatment cannot credibly reach
22 substantive pages, the correct candidate outcome is FAIL / WRITE
NOTHING for this project's long-paper selection.

No decorative figure is required. A compact theorem-comparison table
may materially distinguish full spectra, selected traces and state
Jacobians. Any mathematical examples must explain a real convention or
phenomenon, such as $k=2$ repeated neighbors or the $k=6$ determinant
$-81\epsilon^7/4+O(\epsilon^8)$; they are not new contributions.

## 8. Strict claim guards

- $K$ is the normalized $u$ differential. On $u=\epsilon v$, replacing
  it by the $v$ differential adds $k$ powers of $\epsilon$ to its
  determinant; replacing it by the $c$ differential adds $2k$.
- $k$ is fixed in each theorem. Uniformity is over arbitrary periods,
  not over unbounded factor counts.
- Cycles are disjoint for the composite $F$. Distinct $F$-fixed points
  can be phases of one elementary Hénon orbit at the power locus.
- The universal order statement is at $u=0$, not every parameter point.
- The critical-boundary statement is only for the same selected tuple
  with all macro periods one. It does not negate other choices.
- No all-component irreducibility, global injectivity, entire critical
  scheme classification, optimal anisotropic neighborhood shape,
  entropy, arithmetic determinant or Riemann-zero conclusion is made.
- A proof check, novelty assessment, candidate gate and physical PDF
  acceptance are four separate records. None substitutes for another.

## 9. Identical questions for two fresh independent readers

Read the exact complete main and boundary proofs, this brief, the
literature comparison and the relevant portfolio distinctions. Use the
finished proof checks as existing evidence; do not demand a repeat audit
of unchanged mathematics merely because this is a new workflow stage.
If a concrete missed gap is found while assessing the claims, report it.
Reviewers must not read each other's scores or conclusions.

The unchanged conjunctive gate requires, **in each independent review**:
novelty at least 7.5/10, research value at least 7.5/10, proof confidence
at least 9/10, and credible 22–30 substantive main-body pages after all
classical/portfolio deductions. Report every score and an independent
section-level page estimate, confidence and concrete grounds. Do not
combine the best gate from different reviewers or treat this author
allocation as measured evidence.

The verdict is PASS only if all four conditions hold for this same
package; otherwise FAIL / WRITE NOTHING, with precise failure grounds.
An explanation of the minimum genuinely missing scientific content is
useful, but reviewers should not invent an additional project or invite
padding. No answer is requested on Route evaluation, external submission,
or authorization to create cloud resources.
