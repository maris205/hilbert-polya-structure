# Citation Verification

## 1. Citation-lock verdict

The primary-source chain needed for the source proof is identifiable and
claim-safe, subject to one explicit reviewer checkpoint:

> The all-\(d\) scalar full-centralizer/wreath statement is cited to Morton
> (1998), Theorem D/Theorem 10. Fakhruddin (2014), Theorem 3.2, states the
> same formula over every characteristic-zero constant field and therefore
> supplies the geometric form needed here.

Gao–Ou verify the scalar curve geometry. Morton (1998) is the exact primary
all-degree Galois-group source; Fakhruddin is the exact arbitrary
characteristic-zero-field restatement. Gao's 2016 article, p. 39, gives a
useful later comparison-table cross-check. Morton (1996), Corollaries 1 and
3 and pp. 335--336, is direct scalar primitive-generator prior art:
\(\rho|_{a=0}\) generates the scalar cycle field for every \(d,n\), and
\(\tau|_{a=0}\) does so when \(d=2\). It is not asked to carry the
full-wreath theorem input.

Cantat--Dujardin (2026), Section 3.2 and Theorems A/3.7, is locked as exact
trace-spectrum adjacency: it reconstructs map parameters up to uniformly
finite ambiguity from formal-period trace multisets over finitely many
periods. It does not prove primitivity in one fixed actual-period cycle field.

Current lifecycle: `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE /
NO_RESULTS`.

Literature cutoff: **2026-08-16**.

## 2. Evidence classes

- **T — theorem input:** directly used in PC1 or PC2.
- **B — boundary/background:** defines the ambient category or a mandatory
  caveat.
- **D — direct or strong collision:** removes novelty credit from a component.
- **A — adjacent frontier:** close topic, different theorem.
- **M — mature method source:** standard algebraic machinery.

No source below is used as evidence for historical priority or universal
absence.

## 3. Verified dynamical sources

### 3.1 Gao–Ou (2014) — T/D: scalar dynatomic geometry

**Record.** Yan Gao and Ya Fei Ou, “The dynatomic periodic curves for
polynomial \(z\mapsto z^d+c\) are smooth and irreducible,” *Science China
Mathematics* **57**(6) (2014), 1175–1192.
DOI: [10.1007/s11425-014-4807-1](https://doi.org/10.1007/s11425-014-4807-1).
Preprint: [arXiv:1304.4751](https://arxiv.org/abs/1304.4751).

**Verified content.** For every \(d\ge2\) and \(n\ge1\), the affine periodic
dynatomic curve for \(z^d+c\) is smooth and irreducible over \(\mathbb C\).
The article's Theorems 1.1 and 1.2 are the relevant statements.

**Allowed use.**

- \(D_n\) is a normal geometrically integral domain in characteristic zero.
- \(D_n\otimes_{\mathbb Q[c]}\mathbb Q(c)\) is a field.
- the scalar exact-period factor is a connected input for Henselian lifting.

**Forbidden use.**

- no relative Hénon normalization, flatness, cyclic quotient, or
  two-parameter monodromy is attributed to Gao–Ou;
- the paper does not erase the formal-versus-actual distinction at special
  parabolic parameters.

### 3.2 Morton (1998) — T: exact all-degree periodic Galois group

**Record.** Patrick Morton, “Galois Groups of Periodic Points,” *Journal of
Algebra* **201**(2) (1998), 401–428.
DOI: [10.1006/jabr.1997.7304](https://doi.org/10.1006/jabr.1997.7304).

**Verified content.** Theorem D/Theorem 10 states that for
\(f(z)=z^d+t\), every \(d\ge2\), and every \(b\ge1\), the Galois group of
\(f^b(z)-z\) over \(\mathbb Q(t)\) is

\[
\prod_{e\mid b}\bigl(C_e\wr S_{r_e}\bigr),
\]

where \(e r_e\) is the number of exact-period-\(e\) points. Consequently the
exact-period-\(n\) factor has group \(C_n\wr S_r\).

**Allowed use.** The exact primary source for maximal scalar marked-point
monodromy and its \(S_r\) cycle quotient for all \(d,n\).

**Scope guard.** The theorem is scalar. The restriction map and global
time-shift centralizer bound are still required to transfer it to the Hénon
parameter plane.

### 3.3 Fakhruddin (2014) — T: characteristic-zero/geometric restatement

**Record.** Najmuddin Fakhruddin, “The algebraic dynamics of generic
endomorphisms of \(\mathbb P^n\),” *Algebra & Number Theory* **8**(3)
(2014), 587–608.
DOI: [10.2140/ant.2014.8.587](https://doi.org/10.2140/ant.2014.8.587).

**Verified content.** Theorem 3.2 explicitly identifies its statement with
Morton (1998), Theorem 10, except that \(\mathbb Q\) is replaced by an
arbitrary characteristic-zero field \(k\): for \(f(z)=z^d+t\),

\[
\operatorname{Gal}(f^b(z)-z/k(t))
=\prod_{e\mid b}(C_e\wr S_{r_e}).
\]

Taking \(k=\overline{\mathbb Q}\) verifies that the full group is geometric,
not merely an arithmetic group enlarged by constants.

**Allowed use.** The geometric scalar point group and its exact-period
factor, with the characteristic-zero hypothesis stated.

### 3.4 Gao (2016) — T: general-degree Galois-group cross-check

**Record.** Yan Gao, “Preperiodic dynatomic curves for
\(z\mapsto z^d+c\),” *Fundamenta Mathematicae* **233**(1) (2016), 37–69.
DOI: [10.4064/fm91-12-2015](https://doi.org/10.4064/fm91-12-2015).
Publisher record:
[IMPAN](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/233/1/91299/preperiodic-dynatomic-curves-for-z-mapsto-z-d-c).
Preprint: [arXiv:1304.4849](https://arxiv.org/abs/1304.4849).

**Verified content.** The introduction and comparison table on p. 39 record,
for the periodic curve and every \(d\ge2\), the Galois group

\[
S_{\nu_d(n)/n}\ltimes(\mathbb Z/n\mathbb Z)^{\nu_d(n)/n},
\]

i.e. \(C_n\wr S_r\), and identify it with the permutations commuting with
the scalar dynamics. The paper attributes periodic curve irreducibility and
Galois groups to the established Bousch/Morton/Lau–Schleicher/Schleicher
line, while its own main theorem treats preperiodic curves.

**Allowed use.** Precise general-degree corroboration for the scalar wreath
input and its source chain.

**Forbidden use.** Gao's preperiodic theorem is not called a proof of the
two-parameter Hénon theorem.

### 3.5 Morton (1996), with corrigendum (2011) — T/D

**Record.** Patrick Morton, “On certain algebraic curves related to polynomial
maps,” *Compositio Mathematica* **103**(3) (1996), 319–350.
[NUMDAM stable record and PDF](https://www.numdam.org/item/CM_1996__103_3_319_0/).
MR 1414593.

**Corrigendum.** Patrick Morton, “Corrigendum: ‘On certain algebraic curves
related to polynomial maps, Compositio Math. 103 (1996), 319–350’,”
*Compositio Mathematica* **147**(1) (2011), 332–334.
DOI:
[10.1112/S0010437X1000480X](https://doi.org/10.1112/S0010437X1000480X).

**Verified content.**

- Morton's Theorem B/Corollary 1 and the discussion on pp. 322--323 give the
  relevant dynatomic and multiplier-polynomial irreducibility for
  \(f(z)=z^d+c\), every \(d\ge2\), at the fixed arbitrary period \(n\).
- On p. 322, the introduction records Bousch's quadratic group as
  \(C_n\wr S_r\).
- On p. 323, the discussion following Corollary 1 records the
  general-degree Lau–Schleicher/Bousch development, its Galois-group
  calculation, and that it implies Morton--Patel Conjecture 2(b).
- Corollary 3 on p. 335 proves irreducibility of the quadratic orbit-sum
  polynomial whose roots are
  \(t=z+f(z)+\cdots+f^{n-1}(z)\).
- On p. 336 Morton sets \(K_0=\mathbb Q(c,z)\), with
  \(\Phi_{d,n}(z,c)=0\), and proves directly that the orbit-shift fixed field
  is
  \[
  K_0^{\langle\sigma\rangle}=\mathbb Q(c,w),\qquad
  w=\prod_{i=0}^{n-1}f'(f^i(z)).
  \]
  On the Paper 13 scalar fiber,
  \(w=d^n\prod_i z_i^{d-1}=\rho|_{a=0}\). Hence Morton directly gives
  scalar fixed-field generation by \(\rho\) for every \(d,n\).
- The same p. 336 passage states that the fixed field can be generated by the
  orbit sum \(t\) whenever its trace polynomial is irreducible. Together with
  Corollary 3, this gives
  \(K_0^{\langle\sigma\rangle}=\mathbb Q(c,\tau|_{a=0})\) for \(d=2\).
- The 2011 corrigendum repairs a finite-characteristic lifting gap in later
  Theorem 15. It does not retract these characteristic-zero fixed-field
  statements; it must accompany citations that touch the corrected argument.

**Claim and novelty effect.** Morton is a direct theorem input available for
the scalar non-base step (indeed a stronger scalar field-generation result)
for \(\rho\) in all degrees and \(\tau\) in degree two. The package's
infinity-word proof remains a uniform internal route, especially for
\(\tau\) when \(d\ge3\). PC2's residual delta is the two-parameter lift,
uniform all-degree \(\tau\) result, and monic integral basis-free
characteristic polynomial in \(A[T]\), not invention of scalar generators.

**Attribution guard.** The displayed “Theorem D” in Morton's **1996** article
is a finiteness theorem, not the all-\(d\) wreath theorem. The relevant
“Theorem D/Theorem 10” is in Morton's **1998** *Journal of Algebra* article.
Always give the year and title so the two labels cannot be conflated.

### 3.6 Schleicher (2017) — T/B: quadratic Galois/monodromy source

**Record.** Dierk Schleicher, “Internal Addresses of the Mandelbrot Set and
Galois Groups of Polynomials,” *Arnold Mathematical Journal* **3** (2017),
1–35. DOI:
[10.1007/s40598-016-0042-x](https://doi.org/10.1007/s40598-016-0042-x).
Preprint history:
[arXiv:math/9411238](https://arxiv.org/abs/math/9411238).

**Allowed use.** The analytic-continuation/Galois calculation in the
quadratic Mandelbrot setting and the historical Lau–Schleicher source chain.

**Scope guard.** This citation by itself is not the all-\(d\) theorem. The
general-\(d\) source statement is cross-checked by Gao (2016) and Morton's
discussion of the Lau–Schleicher generalization.

### 3.7 Doyle–Poonen (2020) — D/B: scalar modular-curve geometry

**Record.** John R. Doyle and Bjorn Poonen, “Gonality of dynatomic curves and
strong uniform boundedness of preperiodic points,” *Compositio Mathematica*
**156**(4) (2020), 733–743.
DOI:
[10.1112/S0010437X20007022](https://doi.org/10.1112/S0010437X20007022).
Preprint: [arXiv:1711.04233](https://arxiv.org/abs/1711.04233).

**Verified content.** The paper uses the scalar dynatomic curves
\(X_1(n)\), \(X_0(n)\), proves geometric irreducibility results for relevant
components, and proves gonality growth in the unicritical setting.

**Allowed use.** Scalar modular-curve notation, quotient context, and adjacent
geometry.

**Forbidden use.** No Hénon normalization, exact special-fiber theorem, or
primitive derivative-trace coordinate is inferred.

### 3.8 Hutz (2010) — B/D: formal dynatomic cycles

**Record.** Benjamin Hutz, “Dynatomic cycles for morphisms of projective
varieties,” *New York Journal of Mathematics* **16** (2010), 125–159.
[Journal record](https://nyjm.albany.edu/j/2010/16-8.html).
Preprint: [arXiv:0801.3643](https://arxiv.org/abs/0801.3643).

**Verified content.** Hutz proves effectivity of formal dynatomic zero-cycles,
analyzes their degrees and multiplicities, and records conditions relating
formal period to minimal period.

**Allowed use.** Mandatory warning that dynatomic/formal period need not be
actual minimal period on every special fiber.

**Forbidden use.** No everywhere actual-period Hénon subscheme is attributed
to Hutz.

### 3.9 Friedland–Milnor (1989) — B: Hénon category

**Record.** Shmuel Friedland and John Milnor, “Dynamical properties of plane
polynomial automorphisms,” *Ergodic Theory and Dynamical Systems* **9**(1)
(1989), 67–99.
DOI:
[10.1017/S014338570000482X](https://doi.org/10.1017/S014338570000482X).

**Verified content.** Foundational structure and dynamics for plane
polynomial automorphisms and generalized Hénon maps.

**Allowed use.** Ambient category and a reason to keep the claimed family
narrow.

**Forbidden use.** PC1/PC2 are not promoted to arbitrary polynomial
automorphisms.

### 3.10 Cantat–Dujardin (2026) — A/D: formal-period trace-spectrum rigidity

**Record.** Serge Cantat and Romain Dujardin, “Multiplier rigidity for complex
Hénon maps,” preprint (2026).
[arXiv:2603.09445](https://arxiv.org/abs/2603.09445).

**Verified content.** Section 3.1 defines the formal-period-\(n\) multiset
\(\operatorname{Per}^{*}_n(f)\), with multiplicities. Section 3.2 defines

\[
 \operatorname{Trace}_n(f)=
 \{\operatorname{tr}(D_zf^n):z\in\operatorname{Per}^{*}_n(f)\}
\]

as a multiset of fixed length \(p_n\), and defines the trace spectrum as the
sequence of these multisets over all \(n\). The use of formal rather than
exact period is explicit and is chosen for good algebraic and analytic
behavior.

Theorem A says that a complex Hénon map of fixed degree is determined up to
finitely many choices by its trace spectrum (or by its unstable-multiplier
spectrum). Theorem 3.7 gives a uniform finite-period version: there exist
\(P,N\), depending only on the degree or multidegree, such that equality of
\(\operatorname{Trace}_n\) for every \(n\le P\) leaves at most \(N\) maps.
It also states the result over every algebraically closed field of
characteristic zero. In the composition parameter space, the multi-Jacobian
is fixed as part of the theorem's setup.

**Allowed use.** Exact current context for pointwise derivative traces as
formal-period multisets and the strongest recent trace-spectrum adjacency
located.

**Noncollision boundary.** Cantat--Dujardin reconstruct map parameters from
whole trace multisets across finitely many formal periods. PC2 fixes one
actual period and asks whether the trace value at one generic cycle generates
the degree-\(r\) cycle function field over the parameter base. These are
different source/target problems, and neither statement implies the other.
The paper is not said to contain, imply, or disprove the exact relative
normalization and one-cycle-field theorem.

### 3.11 Arai (2016) — A: different Hénon monodromy

**Record.** Zin Arai, “On loops in the hyperbolic locus of the complex Hénon
map and their monodromies,” *Physica D* **334** (2016), 133–140.
DOI:
[10.1016/j.physd.2016.02.006](https://doi.org/10.1016/j.physd.2016.02.006).
Preprint: [arXiv:0704.2978](https://arxiv.org/abs/0704.2978).

**Boundary.** Arai studies symbolic/horseshoe monodromy on a hyperbolic
parameter locus. The present \(S_r\) is finite algebraic-cover monodromy on
primitive cycles. Shared terminology is not a direct theorem collision.

### 3.12 Ji–Xie (2026) — A: current dynatomic geometry

**Record.** Zhuchao Ji and Junyi Xie, “Genus and Gonality of Small Curves,
Dynamical Uniform Boundedness, and Bifurcation,” preprint (2026).
[arXiv:2607.12561](https://arxiv.org/abs/2607.12561).

**Boundary.** Their theorems concern genus/gonality growth for dynatomic and
small horizontal curves in one-parameter endomorphism families, with
higher-dimensional analogues under hypotheses. They do not state the
two-parameter affine normalization, special fiber, finite cycle monodromy, or
two primitive coordinates here.

### 3.13 Endler--Gallas (2002) — D: period-four orbit-sum carrier

**Record.** Antônio Endler and Jason A. C. Gallas, “Arithmetical signatures
of the dynamics of the Hénon map,” *Physical Review E* **65** (2002),
036231.
DOI: [10.1103/PhysRevE.65.036231](https://doi.org/10.1103/PhysRevE.65.036231).

**Verified content.** For the quadratic Hénon map, the paper sets the carrier
\(s=x_1+x_2+x_3+x_4\), expresses the period-four orbital polynomial in terms
of \(s\), and gives a cubic equation whose three roots parameterize the three
period-four orbits.

**Novelty effect.** Directly blocks any claim that a Hénon orbit sum, an
orbit-sum carrier polynomial, or its low-period algebraic use is introduced
here. It does not prove an all-\(d,n\) normalized cover, full cycle monodromy,
or generic irreducibility of the multiplication polynomial.

### 3.14 Endler--Gallas (2004) — D: period-six carrier and stability

**Record.** Antônio Endler and Jason A. C. Gallas, “Existence and
characterization of stable ghost orbits in the Hénon map,” *Physica A*
**344**(3) (2004), 491–497.
DOI: [10.1016/j.physa.2004.06.019](https://doi.org/10.1016/j.physa.2004.06.019).
Preprint: [arXiv:nlin/0407004](https://arxiv.org/abs/nlin/0407004).

**Verified content.** The paper writes the period-six orbital polynomial
using \(\sigma=x_1+\cdots+x_6\), a degree-nine equation for the possible
\(\sigma\)-values, and a secular equation for stability. It applies these
equations to stable complex or “ghost” orbits.

**Novelty effect.** Direct prior art for \(\tau\)-type Hénon carriers and
low-period stability information. It does not identify \(\sigma\) or a
derivative trace as a primitive generator of the arbitrary-period generic
cycle field.

### 3.15 Zhang (2014) — D: bounded-period cyclic polynomials

**Record.** Cheng Zhang, “Cycles of the Logistic Map,” *International
Journal of Bifurcation and Chaos* **24**(1) (2014), 1450005.
DOI:
[10.1142/S0218127414500059](https://doi.org/10.1142/S0218127414500059).
Preprint: [arXiv:1204.0546](https://arxiv.org/abs/1204.0546).

**Verified content.** Cyclic polynomials are used to derive onset and
bifurcation parameter equations for polynomial maps; the published abstract
reports Hénon computations through period \(n=9\).

**Novelty effect.** Direct bounded-period computational precedent for cyclic
Hénon polynomial elimination. It does not prove the relative normalization,
special-fiber identity, all-period monodromy, or primitive-coordinate theorem
in PC1/PC2.

## 4. Exact commutative-algebra source ledger

The following Stacks Project tags are the locked references. The proof package
also supplies the local arguments, so these tags are not used as opaque
citations.

| Tag | Exact statement used | Proof-package role |
|---|---|---|
| [07QW](https://stacks.math.columbia.edu/tag/07QW) | finite-type algebras over a field are excellent | \(A\) is excellent |
| [07QV](https://stacks.math.columbia.edu/tag/07QV) | quasi-excellent rings are Nagata | normalization finiteness chain |
| [035S](https://stacks.math.columbia.edu/tag/035S) | normalization of a Nagata scheme is finite | \(S/A\) finite |
| [033P](https://stacks.math.columbia.edu/tag/033P) | normal is \(R_1+S_2\); normal schemes of dimension at most two are CM; \(R_0+S_1\) is reduced | CM surface and special-fiber reducedness |
| [00R4](https://stacks.math.columbia.edu/tag/00R4) | miracle flatness | \(S/A\) flat |
| [0D49](https://stacks.math.columbia.edu/tag/0D49) | finite étale algebras over a henselian pair are equivalent to those over the quotient; idempotents lift uniquely | exact scalar block lifts |
| [09E4](https://stacks.math.columbia.edu/tag/09E4) | ramification index and residue degree for DVR extensions | \(e=1\) terminology |
| [09E8](https://stacks.math.columbia.edu/tag/09E8) | for a finite separable field extension, \([L:K]=\sum e_if_i\), with one prime over a henselian DVR | unique-prime degree ledger |
| [0309](https://stacks.math.columbia.edu/tag/0309) | a normal domain is integrally closed in its fraction field | finite birational normal-overring equality |
| [037P](https://stacks.math.columbia.edu/tag/037P) | if \(k\) is algebraically closed in \(K\), then \(K/k\) is geometrically irreducible | constants step |
| [0322](https://stacks.math.columbia.edu/tag/0322) | a characteristic-zero field extension is geometrically reduced | constants plus characteristic zero |
| [0FWF](https://stacks.math.columbia.edu/tag/0FWF) | geometric integrality may be checked after algebraic closure | final geometric-integrality criterion |

### Reynolds/base-change note

No external theorem is needed beyond elementary idempotent algebra. Because
\(n\) is invertible in \(A\),

\[
\mathcal R=n^{-1}\sum_{j=0}^{n-1}\sigma^j
\]

is an idempotent with image \(S^{C_n}\). Images of a direct-sum idempotent on
a finite projective module commute with arbitrary tensor base change. This is
stronger and more precise than citing a vague “invariants commute with base
change” slogan.

## 5. Claim-to-citation map

| Claim | Required source | What remains internal |
|---|---|---|
| Scalar \(D_n\) smooth/geometrically integral/normal | Gao–Ou 2014 | descent and finite birational comparison |
| Scalar exact generic block one field | Gao–Ou 2014; Morton 1996 | henselian identification with \(E_n\) |
| Scalar point monodromy \(C_n\wr S_r\) | Morton 1998, Theorem D/Theorem 10; Fakhruddin 2014, Theorem 3.2; Gao 2016, p. 39 cross-check | correct special-to-global restriction and centralizer bound |
| Formal versus actual caveat | Hutz 2010; scalar dynatomic literature | generic idempotent construction |
| \(S\) finite locally free | Stacks 07QW, 07QV, 035S, 033P, 00R4 | local dimension verification |
| exact special fiber | Stacks 0D49, 09E4, 09E8, 033P; Gao–Ou | unique-prime descent and map \(D_n\to S/aS\) |
| geometric integrality | Stacks 037P, 0322, 0FWF; Gao–Ou | injection of constants into scalar residue |
| \(\rho\) primitive | Morton 1996, Corollary 1 and p. 336, directly gives scalar fixed-field generation for every \(d,n\); scalar \(S_r\) monodromy | two-parameter lift, retained infinity-word route, maximal stabilizer, and integral basis-free \(\chi_\rho\) |
| \(\tau\) primitive | Morton 1996, Corollary 3 (p. 335) and p. 336, directly gives scalar fixed-field generation for \(d=2\); scalar \(S_r\) monodromy | two-parameter lift, uniform infinity-word proof including \(d\ge3\), maximal stabilizer, and integral basis-free \(\chi_\tau\) |
| Hénon trace-spectrum adjacency | Cantat--Dujardin 2026, Section 3.2 and Theorems A/3.7 | distinguish finite-period formal-multiset parameter reconstruction from one fixed actual-period cycle-field primitivity |

## 6. Direct-collision and novelty boundaries

### Directly occupied

- scalar dynatomic smoothness/irreducibility;
- scalar orbit quotients and \(X_0(n)\) geometry;
- scalar wreath monodromy;
- formal dynatomic cycles;
- multiplier and trace-polynomial machinery;
- scalar cycle-field generation by the multiplier
  \(\rho|_{a=0}\) for every \(d,n\), and by the quadratic orbit sum
  \(\tau|_{a=0}\), from Morton (1996);
- quadratic Hénon period-four and period-six orbit-sum carriers and their
  stability equations;
- bounded-period Hénon cyclic-polynomial computations;
- Hénon parameter reconstruction from formal-period trace-spectrum multisets
  over finitely many periods, from Cantat--Dujardin (2026);
- Hénon symbolic monodromy as a neighboring topic.

### Bounded residual conjunction

No located source states the entire conjunction of:

\[
\begin{gathered}
\text{two-parameter normalized actual block}\\
+\text{finite locally free normalization across }a=0\\
+\text{exact reduced scalar fiber}\\
+\text{affine cyclic quotient}\\
+S_r\text{ global cycle monodromy}\\
+\text{two-parameter lifts of }\tau,\rho\text{ separately primitive}\\
+\text{uniform all-}d\text{ treatment of }\tau\\
+\text{integral basis-free characteristic polynomials}.
\end{gathered}
\]

This is a bounded no-hit result, not proof of priority.

## 7. Search log

Searches were run through 2026-08-16 using combinations of:

- “Hénon dynatomic curve primitive cycle cover monodromy normalization”;
- “Hénon exact periodic point cover algebraic monodromy”;
- “primitive cycle Hénon derivative trace field”;
- “Morton fixed field multiplier orbit trace dynatomic”;
- “Hénon formal period trace spectrum finite determination”;
- “dynatomic \(x^d+c\) Galois group wreath product”;
- “all permutations commuting with \(f_c\) dynatomic”;
- “Morton Theorem D dynatomic Galois group”;
- “Gao Ou dynatomic smooth irreducible DOI”;
- “Doyle Poonen \(X_0(n)\) gonality”;
- “2026 Hénon multiplier rigidity”;
- “2026 dynatomic genus gonality”;
- “Hénon period 4 orbit sum carrier cubic Endler Gallas”;
- “Hénon period 6 orbit sum stability Endler Gallas”;
- “Hénon cyclic polynomials period 9 Zhang”;
- exact Stacks terms for excellence, normalization, miracle flatness,
  henselian idempotents, DVR ramification, and geometric constants.

The “Morton Theorem D” query was important: it exposed that a later shorthand
can be misleading because the displayed Theorem D in Morton's 1996 paper is a
finiteness result, whereas Morton 1998, Theorem D/Theorem 10, is the periodic
Galois-group result. The source lock therefore always cites year, title, and
theorem content. The Round-1 direct-page audit then exposed the stronger
1996 fixed-field collision on pp. 335--336; generic descriptions such as
“trace-related constructions” are no longer accepted.

## 8. Bibliography recommendations

### Mandatory theorem/context bibliography

1. Gao–Ou 2014.
2. Morton 1998.
3. Fakhruddin 2014.
4. Gao 2016.
5. Morton 1996 and Morton corrigendum 2011.
6. Schleicher 2017, with Lau–Schleicher historical attribution where needed.
7. Doyle–Poonen 2020.
8. Hutz 2010.
9. Friedland–Milnor 1989.
10. Cantat–Dujardin 2026.
11. Endler--Gallas 2002.
12. Endler--Gallas 2004.
13. Zhang 2014.
14. the Stacks Project tags in Section 4.

### Include if the corresponding discussion remains

- Arai 2016 for the distinction from symbolic Hénon monodromy.
- Ji–Xie 2026 for the current dynatomic genus/gonality frontier.

## 9. Submission-time recheck list

Before any manuscript is authorized, the independent Round-2 reviewer must:

- [ ] open the published Gao–Ou theorem, not only the abstract;
- [ ] verify Morton 1998, Theorem D/Theorem 10, and Fakhruddin 2014,
      Theorem 3.2, including extraction of the exact-period factor;
- [ ] use Gao 2016, p. 39 only as a later all-degree cross-check;
- [ ] inspect Morton 1996, Corollaries 1/3 and pp. 335--336, together with
      the 2011 corrigendum; verify direct scalar fixed-field generation by
      \(\rho\) for all \(d,n\) and by \(\tau\) for \(d=2\);
- [ ] distinguish Morton 1996, Theorem D, from Morton 1998, Theorem D/Theorem
      10;
- [ ] inspect Endler--Gallas 2002/2004 and Zhang 2014 when assessing the
      observable novelty boundary;
- [ ] distinguish affine \(Y_0(n)\)/\(X_0^{\rm aff}(n)\) from projective
      \(X_0(n)\) conventions;
- [ ] update the 2026 frontier search from the literature cutoff to the actual
      submission date;
- [ ] verify Cantat–Dujardin Section 3.2 and Theorems A/3.7, including formal
      period, multiset multiplicities, finitely many periods, uniform finite
      ambiguity, and the characteristic-zero field scope;
- [ ] distinguish that parameter-reconstruction theorem from fixed-\(n\),
      one-cycle-field primitivity;
- [ ] recheck Cantat–Dujardin and Ji–Xie version/publication status;
- [ ] preserve the bounded-absence wording;
- [ ] retain the novelty STOP/GO disagreement and the corrected author-side
      novelty \(4.8\)--\(5.5\), size \(4.5\)--\(5.5\) ranges without averaging;
- [ ] verify the immutable Round-1 review, v1 lock SHA, all corrected planner
      hashes, and the v2 lifecycle before issuing any pass;
- [ ] verify every DOI, page range, author name, and citation key against the
      final bibliography.

## 10. Mandatory nonclaims

The citations do not support:

- an everywhere embedded actual-period Hénon subscheme;
- free cyclic action or smoothness on every fiber;
- automatic commutation of normalization with base change;
- arbitrary generalized Hénon maps;
- novelty of dynatomic, trace, monodromy, normalization, or invariant methods;
- invention of scalar fixed-field generation by the multiplier or quadratic
  orbit sum;
- invention of Hénon orbit-sum carriers, low-period stability carriers, or
  cyclic-polynomial elimination;
- Hénon parameter reconstruction from formal-period trace spectra;
- historical priority;
- fiberwise irreducibility of \(\chi_\tau\) or \(\chi_\rho\);
- replacement of pointwise derivative trace by a field trace or determinant.
