# Paper30 candidate brief: finite-order polynomial Hamiltonian conjugacy

Date: 2026-09-06. Status: SAME_COMPLETE_INPUT_FOR_BLIND_CANDIDATE_REVIEWS.
This is a selection-stage brief, not a formal Paper30 project, manuscript,
capacity-measurement exception or accepted paper. Batch07 remains 3/5.
The action inverse, quantum, geometric detection and wild-cover packages
are separate problems and supply no claims or pages for this candidate.

## 1. Decision and unchanged gates

The final classification check has been received and fully read. Two fresh,
mutually blind candidate reviewers receive this same completed package.
Each must independently give novelty at least 7.5/10, research value at least
7.5/10, proof confidence at least 9/10, and credible support for **22–30
substantive body pages**. Both reports must pass all four gates. Do not
average reports, combine their strongest dimensions, infer candidate PASS
from a mathematical check, or reuse Paper29's one-time draft exception.

The capacity assumption is an anonymous English, single-column `article`,
11pt, letterpaper, one-inch margins, ordinary spacing and normal theorem
and display layout. References start on a separate page and are excluded.
The body must stand on the needed arguments and their interpretation.
Raw program listings, the long unreduced degree-four equation table,
review reports and repeated proofs of inherited tools do not supply pages.
No physical manuscript measurement is requested or authorized by this brief.

The proposed unifying question is precise: when does the prescribed
exponential perturbation of a polynomial Hénon map stay in its global
polynomial formal conjugacy class? The package joins a general obstruction
construction to an exact low-degree classification and a separate unbounded
orbit-linear rigidity theorem. Reviewers must assess whether those parts
form a substantive single article; cohesion and length are not assumed.

## 2. Complete inputs and actual evidence status

All files below are in this directory, unless a dependency path is given.
The author inputs are frozen and have been fully read by root.

| Author input | Lines | SHA256 |
| --- | ---: | --- |
| `PAPER30_FORMAL_GAUGE_FIRST_PROBE_20260906.md` | 777 | `c3d444b699dd09f2c7ab5334c0fe0e9cf71e219596de288553fc1c3e34708b33` |
| `PAPER30_ORBIT_LINEAR_GAUGE_PROOF_20260906.md` | 190 | `2f6e4e603fef5ca331e0f829c4493d426c0e57bf62e930c17e1ac3b965e7a183` |
| `PAPER30_ORBIT_LINEAR_GAUGE_TEXT_ERRATUM_20260906.md` | 24 | `b818cdfc8b31f12f703b34edfc40d137eac31d3bd273f3c65713dfc75581e57c` |
| `PAPER30_UNIFORM_FORMAL_GAUGE_PROOF_20260906.md` | 214 | `052366584730be71cd4426fae0e5d5470fc7ffa1fb8928b1f5c4005bf40ee3a0` |

Read those four inputs and this brief completely, together with:

- `PAPER30_GAUGE_STRUCTURAL_INDEPENDENT_CHECK_20260906.md`, 521 lines,
  SHA256 `ecbb49eaa5146a4e88f603f5a4a54c656a65b8fe3d94c9a8e8bb129aaffa4dba`;
- `PAPER30_CUBIC_GAUGE_INDEPENDENT_CHECK_20260906.md`, 607 lines,
  SHA256 `3f7dc12ea871dec91e049ed6e5b6204d19e5db86219a05ecb9f4da7de7cab946`;
- `PAPER30_GAUGE_ACTION_PRIOR_PREFLIGHT_20260906.md`, 305 lines,
  SHA256 `d5128f87fb9525e8827fcd4143b2c25b81d5a756adf23501a071ab58b2f432ce`.

The structural mathematical review and the dedicated prior report are
complete and fully read by root. Both structural theorems are independently
PROVABLE AS STATED. The only literal issue is the malformed second parameter
command in line 28 of the orbit-linear input; its separate erratum restores
the intended `\varepsilon^2` and has been independently closed. The original
input is not edited retrospectively. The cubic classification's final
independent report has completed and all 607 lines have been fully read
by root. Its actual conclusion is PROVABLE AS STATED, with no required
mathematical repair, coefficient correction or excluded parameter branch.
That report independently reconstructs all finite coefficients and supplies
the compact complete cubic nine-equation system, exhaustive branch proof
and full selected third-order contribution tables. Its statements about
general-degree questions being open are scoped to its sole cubic-author
input: F3 below is the separately authored and separately checked uniform
existence theorem, not a conclusion inferred from the cubic calculation.

The first probe's overall status records that its original degree-four
explicit-classification target was not completed. The present candidate
does not claim that target. Its explicit classification is for degree at
most three; the degree-four table is a checked implicit boundary calculation,
not a completed higher-degree classification or a substitute for one.

For a concrete inherited dependency, inspect accepted Paper29 Sections 2–3:
`papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/`.
The orbit basis, ordinary-degree adaptation and coefficient-sum criterion
are deducted. Do not reopen its source review, build trees or accepted PDF.
The F section of the portfolio may be used for local noncollision; it does
not itself prove world novelty.

## 3. Objects and categorical distinctions

Let $A=\mathbb C[x,y]$, $p$ have exact degree $d\ge2$, and
$$
H_p(x,y)=(p(x)-y,x),\qquad \sigma=H_p^*,\qquad
\{f,g\}=f_xg_y-f_yg_x,\quad \operatorname{ad}_f(g)=\{f,g\}.
$$
Fix one polynomial $h$ and the entire prescribed curve
$$
U_h(\varepsilon)=\exp(\varepsilon\operatorname{ad}_{h-\sigma h})\sigma.
$$
The unknown conjugator fixes the parameter and is tangent to the identity:
$$
U_h=C_\varepsilon\sigma C_\varepsilon^{-1},\qquad
C_\varepsilon=\exp(\operatorname{ad}_{K_\varepsilon}),\qquad
K_\varepsilon=\varepsilon h+\sum_{n\ge2}\varepsilon^n h_n.
$$
Every $h_n$ is a global polynomial; their spatial degrees are not given a
common bound. Formal means completion in $\varepsilon$, not in $x,y$.
The initial $h$ does not depend on $\varepsilon$. Replacing the perturbation
by an arbitrarily completed conjugate curve would change the problem.

Every tangent-to-identity formal symplectic automorphism has a polynomial
Hamiltonian logarithm coefficient by coefficient. Constants are exactly
the kernel of $h\mapsto\operatorname{ad}_h$. Thus allowing all such
symplectic conjugators does not evade the Hamiltonian obstruction system;
the first Hamiltonian term is forced to equal $h$ modulo constants.

The accepted orbit coordinates obey $X_0=x$, $X_{-1}=y$ and
$X_{i-1}+X_{i+1}=p(X_i)$; $\sigma X_i=X_{i+1}$. Standard words have
finite support and exponents below $d$. In the quotient
$$
\overline{\mathcal H}=A/((1-\sigma)A+\mathbb C),
$$
the obstruction coordinates are sums of normal-form coefficients on
nonconstant translation orbits. A normal constant coefficient is not an
ordinary $x^0y^0$ coefficient. No periodic-point scheme or spectral-operator
claim enters this problem.

## 4. Stated mathematical package

### F1. Complete cubic classification and sharp third-order determination

For $p(x)=x^2+c$, every $c\in\mathbb C$, and every ordinary-degree
$\deg h\le3$, the following are equivalent:
$$
\begin{aligned}
&\text{the prescribed conjugacy holds modulo }\varepsilon^4;\\
&\text{it holds as a full global polynomial formal series};\\
&h=b+aX_i\quad\text{for some }i\in\{-2,-1,0,1\},\ a,b\in\mathbb C.
\end{aligned}
$$
For the surviving lines, $C_\varepsilon=\exp(\varepsilon\operatorname{ad}_h)$
is exact. Because $X_i$ is a polynomial coordinate,
$\operatorname{ad}_{X_i}=\sigma^i\partial_y\sigma^{-i}$ is locally
nilpotent; this conjugator and its inverse are polynomial also in
$\varepsilon$. That last observation is a direct property of the same
construction, not an additional independent mechanism.

The nontrivial part is the complete second-order zero set and its exclusion
at third order. Write the nine nonconstant cubic coefficients as
$$
\begin{aligned}
h={}&b+uX_{-2}+vX_{-1}+wX_0+zX_1\\
&+p_0X_{-2}X_{-1}+qX_{-2}X_0+sX_{-1}X_0
 +kX_{-1}X_1+lX_0X_1.
\end{aligned}
$$
Here $p_0$ is a Hamiltonian coefficient, not the map polynomial.
The first probe uses the letter $p$ for that coefficient.
The second-order class vanishes precisely on the four coordinate lines,
plus nonzero scalings and constant translates of the following families
and their images under $R f(x,y)=f(y,x)$:
$$
\begin{aligned}
h_A={}&tX_{-2}+
 \left(\frac{7r-12}{3}t^2-3r\right)X_{-1}+(4r-7)tX_0\\
 &+X_{-2}X_{-1}+rX_{-2}X_0-X_{-1}X_0,\qquad r^2=3,\\
P_A={}&c(8+(4-2r)t)+(15r-26)t^3+(3r-6)t=0;
\end{aligned}
$$
$$
\begin{aligned}
h_B={}&tX_{-2}+
 \left(\frac25t^3+\frac{13}{9}t^2+\frac23ct-\frac{17}{5}\right)X_{-1}\\
 &+\left(-\frac{t^2}{3}-\frac{23t}{18}-\frac c3\right)X_0
 -\frac16X_1+X_{-2}X_0+\frac{2t}{9}X_{-1}X_0,\\
P_B={}&216t^5+528t^4+(576c-550)t^3+(80c+534)t^2\\
 &+(360c^2+420c+807)t-1080c^2+11034c=0.
\end{aligned}
$$
These are equations and a pointwise parametrization, not claims that every
fiber curve is smooth or irreducible. Nonzero complex divisions in the
classification are separated into exhaustive cases, including their zero
branches. No parameter $c$ is removed.

Let $B_h=\{h,\sigma h\}$ and choose the unique second-order primitive
modulo constants, $(1-\sigma)h_2=B_h/2\pmod\mathbb C$. The third-order
right-hand side is
$$
T=\frac12(\{h,\sigma h_2\}+\{h_2,\sigma h\})
 +\frac1{12}\{h+\sigma h,B_h\}.
$$
For the normalized A branch its $[X_0X_1X_2]$ coefficient is $30$;
for B its $[X_0X_4]$ coefficient is $14/9$. The proof separates cross and
nested terms into $45-15$ and $7/3-7/9$, proves that the remaining linear
terms in $h_2$ do not affect these coefficients, and handles the anti-Poisson
reversor with the parameter sign. Nonzero scaling multiplies each certificate
by its cube. All noncoordinate second-order zeros therefore fail at third
order regardless of any unrestricted polynomial choice for $h_3$.

For each fixed $c$, $P_A$ is a genuine cubic in $t$ because $15r-26\ne0$;
it has a complex root. Hence third order is necessary for every fixed map
in this family, not merely at one parameter. Degree at most two has no
such failure: its complete second-order zero set is already the axes.
The first possible ordinary degree for second-order success and third-order
failure is exactly three, for every $c$.

At $c=t=0$, B supplies a short rational example:
$$
h=xy^2-\frac76x^2-\frac{97}{30}y,\qquad Q_{04}(T)=\frac{14}{9}.
$$
Its explicit $h_2$ is in the first probe. The older rational quartic example
is retained in that input, but rational coefficients are not a reason to
treat it as a further breakthrough or a needed main-body section.

### F2. Rigidity on all finite orbit-linear spans

For arbitrary scalar $p$ of degree $d\ge2$ over a characteristic-zero field,
and any finite $h=b+\sum_i a_iX_i$, its second-order class vanishes if and
only if at most one $a_i$ is nonzero. This is unbounded in coordinate index
and ordinary degree but is explicitly restricted to this linear span.
It does not classify arbitrary high-degree polynomial Hamiltonians.

The proof uses the continuant for $\{X_i,X_j\}$ and the empty path matching.
If $L<R$ are the extreme nonzero indices and $a$ is the leading coefficient
of $p$, the unique highest formal-word-degree term of $\{h,\sigma h\}$ is
$$
-a_La_R(da)^{R-L}\prod_{j=L+1}^{R}X_j^{d-1}.
$$
It is already standard. Translation preserves formal word degree, so no
lower-degree term can cancel its orbit sum. This explains the rigidity
of coordinate combinations, while F1's mixed words exhibit the failure of
second-order sufficiency outside that subspace.

### F3. Universal polynomial obstruction recursion and finite-order locus

For each fixed exact map degree $d\ge2$ and initial Hamiltonian bound $D$,
all coefficients of $p$ and $h$ are allowed, with the leading coefficient
of $p$ inverted. There is a single existential $N(d,D)$ such that conjugacy
through order $N$ for the prescribed exponential curve is equivalent to
full formal conjugacy. The conjugator tangent to the identity is unique.
The locus in coefficient space is Zariski closed relative to the nonzero
leading-coefficient locus, and its equations are homogeneous in $h$.

The orbit basis over the universal localized ring survives every allowed
specialization. A fixed orbit representative gives linear maps $P,G$ with
$(1-\sigma)G=1-P$. The coefficient-$n$ BCH residual $E_n$ gives the canonical
choice $h_n=-G(E_n)$ and obstruction $\Theta_n=P_+(E_n)$. All are polynomials
over the localized parameter ring, defined even before imposing earlier
equations. The absence of nonconstant polynomial invariants proves that
arbitrary finite-order solutions must follow this same recursion.

Finally the ideal of all representative coefficients of all $\Theta_n$
is finitely generated by Noetherianity. This last step is a standard
principle, explicitly deducted. It does not calculate $N$, give a complexity
bound, certify that a currently observed plateau is final, or establish
finite determinacy under changes to the curve's higher perturbation terms.
F1 gives a sharp explicit order in its narrower family; it does not identify
the entire general obstruction ideal with its third-order ideal, including
over nonreduced parameter bases.

### Validated boundary computation, not a further classification

The full first probe also gives 17 exact homogeneous quadratic equations
for second-order solvability of all degree-four $h$, and its original quartic
third-order counterexample. Those finite calculations remain part of the
scientific input and must not be hidden. They do not provide an explicit
decomposition of the degree-four locus or its third-/all-order solutions.
The raw equation table and reproducibility code are not independent main-body
contributions or capacity. A concise boundary discussion may be appropriate;
the candidate must not rely on printing the whole list to reach 22 pages.

## 5. Strongest prior deductions and local noncollision

The dedicated report separates read primary theorems, public indexed text,
abstract-only items and failed access. Its A branch is unrelated background
and supplies no result here. Relevant F deductions are:

- **Bousch and accepted Paper29:** the orbit-basis/shift mechanism, coefficient
  obstructions and ordinary-degree-adapted normal forms are inherited tools.
  The first-order equation is not a new contribution. Give only the setup
  needed to state and use these tools, including the constant convention.
- **BCH and polynomial Hamiltonian calculus:** the second-order class,
  third-order formula, formal logarithm, constant-center quotient and exact
  commuting-derivation construction are standard ingredients. A single low
  obstruction example is not by itself the claimed classification.
- **de la Llave–Saprykina (2022 preprint), Theorem 3 and Remark 4:** analytic
  cocycles over an integrable torus shear admit equivalences among whole
  periodic data, parameter-formal solvability and existence of an analytic
  solution. Their formal solution need not itself converge. This is strong
  prior for the noncommutative cohomological theme, not a theorem about
  changing global polynomial Hénon coordinates or classifying every cubic
  Hamiltonian. [Primary text](https://arxiv.org/html/2205.12356v1).
- **Fiorenza–Manetti (2007):** mapping-cone higher brackets and MC/gauge
  deformation theory are mature. No new general higher-bracket theory is
  asserted. In particular $1-\sigma$ is not generally a Lie morphism, so
  their mapping-cone theorem is not invoked by plugging it in without
  constructing a valid model. [Primary text](https://arxiv.org/html/math/0601312v3).
- **Mardešić–Novikov–Ortiz-Bobadilla–Pontigo-Herrera (2026), §2.1:** a finite
  parameter family has a uniform finite first-obstruction index by a simple
  Noetherian argument in their adjacent Melnikov setting. This strongly
  deducts the general principle in F3. Their main unbounded-deformation
  orbit-length theorem is different and is not applied here.
  [Published primary text](https://link.springer.com/article/10.1007/s00574-026-00521-7).
- **Arcet–Giné–Romanovski (2022):** the public publisher index contains a
  related Noetherian ideal-stabilization step in local Hamiltonian
  linearizability. Direct full-text access failed; the report does not claim
  to have read or independently established the full theorem.
  [Publisher record](https://www.sciencedirect.com/science/article/pii/S1468121821001346).

The possible new substance is the exact all-parameter second-order locus,
its complete third-order exclusion and sharp cutoff, together with the
specific global polynomial obstruction construction and orbit-linear
extremal rigidity after the above deductions. The bounded current search
located no direct covering theorem, but does not justify a broad priority
claim. Reviewers should assess that delta, not merely new notation or the
fact that the objects differ from previous papers.

## 6. Review obligations and limits

Give a self-contained claim assessment, the strongest prior overlap, and an
independent natural low/central/high body estimate by substantive section.
A possible dependency order is: problem and distinctions; compact inherited
orbit splitting; general formal recursion and finite-order locus; unbounded
orbit-linear rigidity; explicit cubic second-order classification; third-order
certificates and sharpness; limitations. This is neither a mandatory section
count nor a page allocation. Compress anything genuinely short or repetitive.

Assess all three core parts, their mutual dependence and standalone value.
Do not disregard the substantial complete classification merely because its
proof has finite calculations; equally, do not treat a long computational
report or many displayed coefficients as automatic long-article substance.
Do not count unproved higher-degree classification, an effective general
index, a new convergence theorem, geometric/quantum/action material, or future
experiments as present capacity. There are no numerical experiments to run.

Report the four separate gates and your own conjunction. The required final
selection rule is the conjunction of two independently passing reports.
Reviewer provenance must describe the actual fresh secondary agent with
xhigh reasoning, not an unavailable specified GPT-5.4/Codex-MCP endpoint,
an independently verified cross-model setting or a human referee.
All effects are local. Accepted Papers27–29 remain untouched; no manuscript,
upload, submission, external message or paid resource is authorized here.
