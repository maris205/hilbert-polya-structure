# Final Proposal

## Frozen article identity

**Title:** Sharp Support-Rank Bounds and Unbounded Perron Degree in
Hamiltonian Product Shears

**Central question:** How much nonunit degree complexity can a selected
Hamiltonian product-shear profile carry, and can that support-rank bound be
attained in every unbounded nontrivial rank by maps whose ordinary iterate
degrees are proved exactly?

**Answer:** A stacked selected-support row rank $r$ bounds the nonunit
characteristic degree by $r$. For every $d\ge2$, an explicit positive
Hamiltonian product shear has rank $r=d$, attains degree $d$, and has an
exactly visible scalar degree sequence whose Perron algebraic degree and
minimal rational recurrence order are both $d$.

The article is a proof-first structural construction. It is not a
classification, a general realization theorem, or a computational study.

## Exact assumptions and construction

The base field $K$ has characteristic zero, and ordinary total degree is
used. Fix $d\ge2$. Choose parameters in the order

$$
d\longrightarrow p,c\longrightarrow
a_1<\cdots<a_d\longrightarrow b,R,
$$

where

$$
p\equiv1\pmod d,\quad
\operatorname{ord}_{\mathbb F_p^\times}(c)=p-1,
$$

the residues of the $a_i$ are all $d$-th roots of unity,
$a_1+1>4d$, and, writing $S_a=\sum_i a_i$ and $M=a_d$,

$$
bd\equiv1-(-1)^dc\pmod p,
\qquad
R=1+\frac{2M}{bS_a},
$$

$$
R^2<2,\qquad
b(a_i-a_1)S_a>a_i^2R-a_1^2\quad(i>1).
$$

Define

$$
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b,
$$

and

$$
F=T_W\circ S_V,\quad
S_V(q,p)=(q,p+\nabla V(q)),\quad
T_W(q,p)=(q+\nabla W(p),p).
$$

The selected matrices are

$$
D=\operatorname{diag}(a_1,\ldots,a_d),\quad
B=bJ-I_d,\quad
C=BD=b\mathbf1a^{\mathsf T}-D.
$$

## Frozen claims

### Claim A: support-rank bound

For

$$
A=-I_n+\mathsf P\mathsf Q,\qquad
B=-I_n+\mathsf R\mathsf S,\qquad C=BA,
$$

let

$$
r=\operatorname{rank}\binom{\mathsf Q}{\mathsf S}.
$$

There is an explicit monic degree-$r$ polynomial $Q_r(t)$ satisfying

$$
\chi_C(t)=(t-1)^{n-r}Q_r(t).
$$

Only unit multiplicity at least $n-r$ and nonunit degree at most $r$ are
claimed.

### Claim B: exact selected dynamics

The broad ratio cone gives strict spike selection, strict invariance, and
cross-phase domination. The nested visibility chamber gives a fixed visible
coordinate. Every temporal carry is strict, and all top forms survive in the
positive integer semiring. Therefore

$$
\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\quad(n\ge0),
\qquad
\lambda_1(F)=\rho(C).
$$

The coordinate $q_1$ is uniquely degree-maximal for $n\ge1$.

### Claim C: arbitrary Perron degree and scalar order

The characteristic polynomial is

$$
\chi_C(t)
=t^d+\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.
$$

Its reduction modulo $p$ is $t^d-c$, which is irreducible by the exact
finite-field binomial criterion. Thus $\chi_C$ is irreducible over
$\mathbb Q$, $\rho(C)$ has algebraic degree $d$, and the scalar degree
sequence has minimal rational constant-coefficient recurrence order $d$.

### Claim D: sharpness

The selected matrices admit

$$
A=-I_d+I_d(D+I_d),\qquad
B=-I_d+(b\mathbf1)\mathbf1^{\mathsf T}.
$$

The stacked row rank is $d$, and the irreducible nonunit factor has degree
$d$. Hence the support-row upper bound is attained for each rank
$r=d\ge2$.

## Lemma and dependency budget

The article should expose, rather than compress, the following proof units.

1. Row-basis factorization and Sylvester determinant lemma.
2. Common-kernel unit-eigenspace corollary and exact-multiplicity warning.
3. Ordered residue-lift and large-$b$ parameter-existence lemma.
4. Hamiltonian shear and literal gradient-support lemma.
5. Broad ratio-cone spike-selection lemma.
6. Strict broad-cone invariance lemma.
7. Fine visibility-chamber invariance lemma.
8. Cross-phase domination and all temporal-carry lemma.
9. Positive-semiring leading-form survival lemma.
10. Exact fixed-coordinate degree formula.
11. Characteristic-polynomial coefficient lemma.
12. Modular irreducibility lemma with $d=2$ and $4\mid d$ audit.
13. Perron degree and dynamical-degree lemma.
14. Reachability-observability and Hankel-minimality lemma.
15. Rank-$d$ sharpness corollary.

Claims 5--10 form one induction chain and must retain phase labels. Claims
11--14 form the arithmetic-spectral chain. Claim 15 joins both chains to the
abstract bound.

## Article narrative and page budget

The target is 22--30 article pages before references, with a working total
of about 26 pages.

| Section | Purpose | Target pages |
|---|---|---:|
| 1. Introduction and theorem map | Problem anchor, result statement, local and public positioning, anti-claims | 2.5--3.0 |
| 2. Degree profiles for Hamiltonian product shears | Definitions, phase notation, literal support matrices | 2.0--2.5 |
| 3. Support-row factorization | Sylvester proof, kernel interpretation, failure of exact unit multiplicity | 2.5--3.0 |
| 4. Uniform parameter construction | Quantifier order, ordered lifts, large-$b$ existence, boundary setup | 2.5--3.0 |
| 5. Two-level cones and exact degree induction | Selection, both cone invariances, carries, no cancellation, visibility | 5.0--6.0 |
| 6. Characteristic polynomial and irreducibility | Coefficient formula, modular reduction, binomial criterion, $d=2$ and $4\mid d$ | 3.0--3.5 |
| 7. Perron degree and minimal scalar recurrence | Perron limit, cyclicity, reachability, observability, Hankel rank | 2.5--3.0 |
| 8. Sharpness, limitations, and comparison | Rank attainment, predecessor subtraction, external neighbors, open directions outside scope | 2.0--2.5 |
| Appendix A | Fully expanded inequality and carry audit if needed | 1.5--2.0 |

If the main text reaches 30 pages, the first compression target is repeated
inequality algebra, not assumptions, phase labels, boundary cases, or
anti-claims.

## Evidence and exposition policy

- Headline claims require complete symbolic derivations in the article.
- Named standard results must be stated with their hypotheses and cited
  accurately.
- Public-source claims are limited to the bounded R1 landscape and must not
  be turned into an exhaustive novelty conclusion.
- Papers 22--24 are disclosed as local lineage; Paper 22 is the closest
  structural ancestor and Paper 23 occupies the quartic case.
- No example, table, or symbolic check may substitute for the all-$d$ proof.
- No CAS, numerical run, parameter sweep, or empirical certificate is part of
  the evidence.

## Mandatory exclusions

The article does not claim arbitrary signs, supports, coefficients, or
exponents; realization of all weak Perron numbers; minimal dimension or
sparsity; inverse or higher-degree results; compactification; entropy or
integrability conclusions; periodic selector or automaton theory;
genericity; classification; nonconjugacy; positive characteristic; exact
unit multiplicity; or an exact rank profile for arbitrary matrices. It does
not advertise isolated $d=5$ novelty and uses no first, only, unprecedented,
or absolute-priority wording.

## Source-design acceptance criteria

The design passes only if an independent reviewer can rederive all fifteen
proof units, verify the two-level cone formulation, confirm the exact
inventory and scope controls, and find no hidden computational dependency.
Until such a review exists, no source lock, manuscript, bibliography, build,
PDF, release, registry edit, or external effect is authorized.
