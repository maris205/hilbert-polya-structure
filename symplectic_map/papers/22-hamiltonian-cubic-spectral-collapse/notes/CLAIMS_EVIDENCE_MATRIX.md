# Paper 22 — Claims and Evidence Matrix

This is an author-side source-design ledger, not an independent acceptance
record. “Derived” means that a hand derivation is present in the proof package;
every row still requires fresh independent review.

## Formal theorem ledger

| ID | Exact claim | Assumptions and boundary | Evidence object | Author status |
|---|---|---|---|---|
| C01 | $S$ and $T$ are polynomial automorphisms with subtraction inverses. | fixed displayed potentials over a characteristic-zero field | gradients and inverse formulas | derived; review pending |
| C02 | $S$, $T$, and $F=T\circ S$ preserve $\omega=\sum_i dq_i\wedge dp_i$. | symmetric Hessians | pullback or block-Jacobian calculation | derived; review pending |
| C03 | The only competitive gradient rows are the first $V$ row and last $W$ row. | exact two-monomial potentials | full derivative support ledger | derived; review pending |
| C04 | The selected phase matrices are $A$ and $B$, and the complete-step matrix is $C=BA$. | strict selectors; phase order $S$ then $T$ | literal row derivation and multiplication | derived; review pending |
| C05 | $\mathcal K=\{u>0:x_i\ge1,\ \sum_{i=2}^r x_i<(h-1)/2\}$ is an explicit sufficient invariant selector cone. | $r\ge4$, $g\ge2r+1$ | two selector margins and all cone walls | derived; review pending |
| C06 | The seed $\mathbf1$ lies strictly in $\mathcal K$. | $m=r-2\ge2$, $h\ge2m+4$ | $m+1<(h-1)/2$ | derived; review pending |
| C07 | Every carried $p$- and $q$-coordinate is strictly dominated in its update phase. | seed, $C-I>0$, nonnegative nonzero rows of $A$ | phase-labelled induction | derived; review pending |
| C08 | Selected leading homogeneous forms do not cancel. | polynomial domain, strict degree gaps, characteristic zero | leading-form induction | derived; review pending |
| C09 | The same degree theorem holds for four arbitrary nonzero coefficients on the same two supports. | $\alpha\beta\gamma\delta\ne0$; no added supports | universal/domain argument and strict uniqueness | derived; review pending |
| C10 | The last $q$-coordinate strictly realizes total degree for $n\ge1$. | $u_n\in\mathcal K$, $C-A>0$ | $q_r-q_1$, $q_r-q_i$, and $q_i-p_i$ inequalities | derived; review pending |
| C11 | $\deg(F^n)=e_r^{\mathsf T}C^n\mathbf1$; the formula extends trivially to $n=0$, where all coordinates tie. | fixed ordinary-degree seed | phase recurrence and C10 | derived; review pending |
| C12 | $\lambda_1(F)=\rho(C)$. | exact degree identity and positive $C$ | Perron–Frobenius with positive seed and observable | derived; review pending |
| C13 | $U=\{z_1=z_r=0,\sum_{i=2}^{r-1}z_i=0\}$ has dimension $r-3$ and $C|_U=I$. | characteristic zero | $A|_U=B|_U=-I$ | derived; review pending |
| C14 | The complementary equal-middle space $E$ is invariant and carries the displayed $3\times3$ quotient. | coordinate convention $(a,b,c)\mapsto(a,b,\ldots,b,c)$ | direct row computation | derived; review pending |
| C15 | $\chi_C(t)=(t-1)^{r-3}P_{m,h}(t)$. | direct sum $K^r=U\oplus E$ | trace, principal minors, determinant | derived; review pending |
| C16 | $P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0$. | $m\ge2$, characteristic zero | direct substitution | derived; review pending |
| C17 | The eigenvalue $1$ has algebraic and geometric multiplicity exactly $r-3$. | C13–C16 | invariant direct sum and $P(1)\ne0$ | derived; review pending |
| C18 | The exact degree sequence has the displayed cubic annihilating recurrence. | seed $\mathbf1\in E$ | Cayley–Hamilton on $E$ | derived; review pending |
| C19 | $g=2r$ is a sharp boundary for the stated seed and strict selected face. | ordinary degree seed | first-step tie and cone-height equality | derived; review pending |
| C20 | The formal $m=1$ specialization matches Paper 21. | consistency check only | matrix and cubic substitution | derived; review pending |

## Exact evidence dependencies

$$
(C01,C02,C03)\longrightarrow C04\longrightarrow(C05,C06)
\longrightarrow(C07,C08)\longrightarrow(C10,C11,C12),
$$

$$
(C13,C14)\longrightarrow(C15,C16,C17)\longrightarrow C18,
$$

with C09, C19, and C20 as separately bounded corollary, boundary, and lineage
branches. Citation or novelty evidence cannot replace any formal arrow.

## Anti-claim ledger

Paper 22 does not claim:

1. that $\mathcal K$ is maximal, unique, necessary, or an exact
   classification of selector regions;
2. a result for arbitrary supports, arbitrary Hamiltonians, arbitrary shear
   words, or added monomials;
3. a classification of polynomial, symplectic, canonical, affine-triangular,
   or shift-like automorphisms;
4. first realization of any Perron or weak-Perron number;
5. that the Perron root has algebraic degree exactly three for every $(r,g)$;
6. that the cubic annihilator is always minimal or irreducible;
7. non-conjugacy to every product or lower-dimensional map;
8. equality with topological, metric, arithmetic, or measure-theoretic
   entropy;
9. genericity, integrability, periodic-point classification, or arithmetic
   orbit behavior;
10. positive-characteristic validity;
11. global optimality of $g\ge2r+1$ for every cone or degree description;
12. a new theorem for $r=3$ or a correction to Paper 21;
13. literature priority from a bounded source screen; or
14. authority to create a manuscript, build, release, submission, upload,
    identity disclosure, or other external effect.

## Counterexample and assumption-failure ledger

| Attack | Exact outcome |
|---|---|
| Include $x_1$ in $\sigma$ | the threshold seed test becomes false; the definition is prohibited |
| Set $g=2r$ | the first pure/mixed seed scores tie and the seed lies on the open height boundary |
| Ask for strict visibility at $n=0$ | false; all coordinate degrees equal one |
| Allow one of $\alpha,\beta,\gamma,\delta$ to vanish | the selected support can disappear; the coefficient corollary no longer applies |
| Add a monomial to either potential | a new selector face may occur; no theorem is inherited |
| Move to positive characteristic | derivative scalars or accumulated coefficients can vanish |
| Infer exact algebraic degree three from a cubic equation | invalid without irreducibility and minimality |
| Treat the $m=1$ row as new | collides exactly with Paper 21 |
| Call the cone exact or maximal | stronger than the proved sufficient invariance statement |

## Manuscript completeness gate

A later proof-first article must devote credible mass to every formal branch:
gradients and supports, two selectors, all cone walls, phase induction,
leading-form survival, visibility, Perron limit, invariant decomposition,
quotient algebra, sharp boundary, coefficient corollary, collision disclosure,
and limitations. The current plan supports 24–28 content pages and the
authorized range is 22–30. Page count alone is never evidence of completeness.

All rows remain pending independent source-design review.
