# Claims--Evidence Matrix

## Evidence classes

- **Exact internal derivation:** a symbolic proof is supplied in
  PROOF_PACKAGE.md and does not depend on computation.
- **Named theorem:** a standard result is invoked with its hypotheses
  checked; a source must be fixed before bibliography lock.
- **Frozen primary-source context:** a literature statement is bounded by
  the R1 search through 2026-08-26 UTC and is not mathematical evidence for
  the construction.
- **Local lineage record:** the scope is compared with closed Papers 20--24
  only to prevent portfolio duplication.

## Headline theorem claims

| ID | Exact claim | Assumptions | Dependency / evidence | Concrete falsifier | Design status |
|---|---|---|---|---|---|
| C-01 | If $r=\operatorname{rank}\binom{\mathsf Q}{\mathsf S}$, then $\chi_{BA}(t)=(t-1)^{n-r}Q_r(t)$ for an explicit monic degree-$r$ polynomial. | Compatible matrices over the stated characteristic-zero field; $A=-I+\mathsf P\mathsf Q$, $B=-I+\mathsf R\mathsf S$. | Exact row-basis factorization and rectangular Sylvester identity; Proof Step 1. | $C-I$ does not factor through the stacked row space, or determinant dimensions fail. | PROVABLE AS STATED |
| C-02 | Unit algebraic multiplicity is at least $n-r$, and nonunit characteristic degree is at most $r$. | C-01. | Exact factor plus common-kernel check; Proof Step 1. | The reduced factor is asserted not to contain $t-1$. | PROVABLE AS STATED with lower-bound-only wording |
| C-03 | For every $d\ge2$, parameters $p,c,a_i,b,R$ exist in the frozen order and satisfy all arithmetic and cone inequalities. | Dirichlet, cyclicity of $\mathbb F_p^\times$, finitely many fixed inequalities. | Exact existence proof plus named theorems; Proof Step 2. | The $b$ congruence is insoluble, or a required inequality grows in the wrong direction. | PROVABLE AS STATED |
| C-04 | $S_V$, $T_W$, and $F$ are polynomial symplectomorphisms, and their literal selected rows give $D$, $bJ-I_d$, and $C=b\mathbf1a^{\mathsf T}-D$. | Characteristic zero; frozen $V,W$. | Direct derivative and pullback calculation; Proof Step 3. | A Hessian block is not symmetric or a selected row has no gradient monomial. | PROVABLE AS STATED |
| C-05 | Pure spikes are strict throughout $\mathcal K_{\rm ratio}(R)$, and $C$ maps that cone strictly inside itself. | $a_1+1>4d$, $R^2<2$, parameter definitions. | Exact inequalities; Proof Steps 4--5. | A product competitor ties a spike or the image ratio reaches $R$. | PROVABLE AS STATED |
| C-06 | $\mathcal K_{\rm vis}(R)$ contains the seed and is invariant; after one step the first coordinate is strictly largest. | C-03 and the visibility inequalities. | Exact wall-by-wall proof; Proof Step 6. | The seed is excluded by an unintended strict wall, or a weighted order reverses. | PROVABLE AS STATED |
| C-07 | Every $V$-phase and $W$-phase carry is strict, and every new $q$ degree exceeds every current $p$ degree. | C-05, $b\ge2$, $a_i>1$. | Cross-phase estimate and iterate induction; Proof Step 7. | An old coordinate is not dominated at some phase. | PROVABLE AS STATED |
| C-08 | Selected top forms survive without cancellation. | Positive integer coefficients and characteristic zero. | Positive-semiring induction; Proof Step 7. | A negative coefficient or zero derivative coefficient enters the induction. | PROVABLE AS STATED |
| C-09 | $\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1$ for $n\ge0$, with unique $q_1$ visibility for $n\ge1$. | C-04 through C-08. | Exact coordinate-polynomial induction; Proof Step 7. | The equality is only a tropical bound or visibility changes coordinate. | PROVABLE AS STATED |
| C-10 | $\chi_C(t)=t^d+\sum_{k=1}^d(1-bk)e_k(a)t^{d-k}$. | Frozen $C$. | Matrix determinant lemma plus combinatorial coefficient count; Proof Step 8. | A sign or factor $k$ is wrong. | PROVABLE AS STATED |
| C-11 | $\chi_C(t)\equiv t^d-c\pmod p$ and is irreducible over $\mathbb Q$. | C-03, $c$ of order $p-1$. | Symmetric residues, exact binomial criterion, Gauss's lemma; Proof Step 9. | Any binomial condition, especially $4\mid d$, fails. | PROVABLE AS STATED |
| C-12 | $\lambda_1(F)=\rho(C)$, and this Perron algebraic integer has degree $d$. | C-09, C-11, strict positivity of $C$. | Perron--Frobenius and visible asymptotic; Proof Step 10. | The visible Perron coefficient is zero or $\chi_C$ is reducible. | PROVABLE AS STATED |
| C-13 | The scalar sequence $e_1^{\mathsf T}C^n\mathbf1$ has minimal rational constant-coefficient recurrence order $d$. | C-11 and nonzero seed/observation. | Cyclic reachability and observability, Hankel rank, and tail asymptotic; Proof Step 11. | Reachability or observability is singular, or a polynomial of degree $<d$ annihilates $\rho(C)$. | PROVABLE AS STATED |
| C-14 | The support-row bound is attained for every constructed rank $r=d\ge2$. | C-01, C-11, selected presentations. | Invertibility of $D+I_d$ and irreducible degree-$d$ quotient; Proof Step 12. | The stacked row rank is below $d$ or $\chi_C$ has a unit factor. | PROVABLE AS STATED |

## Dependency map

The mathematical dependency graph is:

$$
\begin{aligned}
&\text{C-01}\Rightarrow\text{C-02},\\
&\text{C-03}+\text{C-04}\Rightarrow
\text{C-05}+\text{C-06}+\text{C-07}+\text{C-08}
\Rightarrow\text{C-09},\\
&\text{C-03}+\text{C-10}\Rightarrow\text{C-11},\\
&\text{C-09}+\text{C-11}\Rightarrow\text{C-12}+\text{C-13},\\
&\text{C-01}+\text{C-04}+\text{C-11}\Rightarrow\text{C-14}.
\end{aligned}
$$

C-09 is the bridge from matrix selection to the ordinary polynomial degree.
C-13 is the bridge from a $d$-state realization to exact scalar complexity.
Neither bridge may be replaced by an example.

## Context and novelty claims

| ID | Bounded contextual statement | Evidence boundary | What it does not prove |
|---|---|---|---|
| N-01 | Paper 22 is the closest local rank-collapse ancestor, while Paper 23 occupies a fixed quartic full-profile family. | Local lineage records and candidate reviews. | External novelty or priority |
| N-02 | Blanc--van Santen give broad weak-Perron realization context for affine-triangular automorphisms. | Frozen R1 primary-source check. | The present Hamiltonian support-rank conjunction |
| N-03 | Shao--Sun study dimension-four affine-triangular dynamical degrees. | Frozen R1 primary-source check. | An arbitrary-$d$ Hamiltonian realization |
| N-04 | Dang--Favre supply broad spectral interpretations of dynamical degrees. | Frozen R1 primary-source check. | Exact selected-gradient visibility or rank sharpness |
| N-05 | Berger--Turaev and Koch--Lomelí provide Hamiltonian shear context. | Frozen R1 primary-source check. | The degree recurrence proved here |
| N-06 | Heyman--Shparlinski record the finite-field irreducible-binomial criterion. | Frozen R1 primary-source check. | Novelty of the arithmetic ingredient |
| N-07 | No direct collision with the complete conjunction was found in the bounded screen through 2026-08-26 UTC. | Search-bounded R1 record only. | Exhaustiveness, firstness, uniqueness, or absolute priority |

## Anti-claim matrix

| Forbidden expansion | Why unsupported |
|---|---|
| Arbitrary signs, coefficients, supports, exponents, or shear words | Positive-semiring survival and both cone proofs use the displayed family. |
| Every weak-Perron realization | The construction realizes one arithmetic family in each degree, not every Perron number. |
| Minimal ambient dimension or optimal sparsity | No lower bound or optimization theorem is proved. |
| Inverse or higher dynamical degrees | Only forward ordinary degree and $\lambda_1$ are analyzed. |
| Compactification, entropy equality, or integrability | No geometric or dynamical theorem of those kinds is present. |
| Periodic selectors or automata | The selected face is stationary on a strict invariant region. |
| Genericity, classification, or nonconjugacy | The result is existential and explicit. |
| Positive characteristic | Positive integer derivative coefficients and modular reduction are used only as characteristic-zero proof devices. |
| Exact unit multiplicity or exact rank profile | $Q_r(t)$ may contain further copies of $t-1$. |
| Isolated $d=5$ novelty | Fixed-dimensional extension is not the contribution. |
| First, only, unprecedented, or absolute priority | The literature screen is bounded and nonexhaustive. |

## Evidence sufficiency rule

A headline claim is ready for later manuscript planning only if every upstream
claim in the dependency map remains PROVABLE AS STATED after an independent
source-design rederivation. Context claims can shape exposition but cannot
raise a failed mathematical claim to PASS.
