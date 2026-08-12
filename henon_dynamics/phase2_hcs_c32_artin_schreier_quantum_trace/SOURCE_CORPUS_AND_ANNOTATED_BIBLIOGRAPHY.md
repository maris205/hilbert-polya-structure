# HCS-C32 source corpus and annotated bibliography

Date: 2026-08-11 UTC

## Corpus key

- **Core**: directly supports or defeats a C32 mathematical claim.
- **Boundary**: fixes terminology or shows why a stronger claim is not yet
  justified.
- **Context**: maps the nearby literature but does not prove a C32 theorem.
- **Excluded**: assessed and found not to address the proposed finite-field
  Hénon/Artin--Schreier bridge.

## A. Core theorem and obstruction sources

### 1. Deligne 1974 — Core, grade A

Deligne, P. (1974). La conjecture de Weil: I. *Publications
Mathématiques de l'IHÉS, 43*, 273–307.
https://doi.org/10.1007/BF02684373

Theorem 8.4 and Lemma 8.5 on journal pages 302–304 are the decisive
source. For a degree-\(d\) polynomial whose leading projective hypersurface is
smooth and with \(p\nmid d\), the nontrivial Artin--Schreier isotypic
cohomology is concentrated in degree \(n\) and has dimension \((d-1)^n\).
Lemma 8.5(ii) pairs a character with its inverse, not generally with itself.
Purity of weight \(n\) is a derived consequence of the injection on p. 304
into smooth-projective \(H^n\), together with Theorem 1.6; it is not a new
Hénon theorem.

### 2. Deligne 1977 — Core, grade A

Deligne, P. (1977). Applications de la formule des traces aux sommes
trigonométriques. In *Cohomologie étale (SGA 4 1/2)* (Lecture Notes in
Mathematics, Vol. 569, pp. 168–232). Springer.
https://doi.org/10.1007/BFb0091523

Section 1.1 gives the supertrace formula; §§1.4–1.7 construct the rank-one
character sheaf; and Scholium 1.9 gives extension-field sums as Frobenius-power
supertraces. For \(\mathbb G_a\), the group norm is the field trace, exactly
supporting \(\psi_r=\psi_0\circ\operatorname{Tr}_{\mathbb F_{p^r}/\mathbb F_p}\).

### 3. Katz and Laumon 1985 — Core, grade A, erratum required

Katz, N. M., & Laumon, G. (1985). Transformation de Fourier et majoration de
sommes exponentielles. *Publications Mathématiques de l'IHÉS, 62*, 145–202.
https://doi.org/10.1007/BF02698808

Definition 2.1.1 fixes the Fourier--Deligne transform and its essential
cohomological shift. Corollary 2.1.5(ii) sends \(\psi\) to \(\psi^{-1}\) under
duality, while Theorem 2.2.1 controls weights. This source is convention
sensitive and must always be read with the 1989 correction.

### 4. Katz and Laumon 1989 — Core, grade A

Katz, N. M., & Laumon, G. (1989). Corrections à: « Transformations de Fourier
et majoration de sommes exponentielles ». *Publications Mathématiques de
l'IHÉS, 69*, 233. https://doi.org/10.1007/BF02698847

The correction states that a missing shift \([r]\) caused missing
\((-1)^r\) signs. It is a direct historical warning against silently moving
between a raw kernel, a perverse shift, an ordinary trace, and a supertrace.

### 5. Laumon 1987 — Core, grade A

Laumon, G. (1987). Transformation de Fourier, constantes d'équations
fonctionnelles et conjecture de Weil. *Publications Mathématiques de l'IHÉS,
65*, 131–210. https://doi.org/10.1007/BF02698937

Formulas 1.1.1.2–1.1.1.3 give the exact sheaf--function rules: tensor product
becomes multiplication and \(Rf_!\) becomes summation over finite-field
fibers. These rules certify chronological intermediate-state summation for
the C32 raw kernel. Laumon's additive convolution uses a vector-bundle
addition map and should not be called literally identical to correspondence
composition on \(X\times X\).

### 6. Bolotin and Treschev 2010 — Core, grade A

Bolotin, S. V., & Treschev, D. V. (2010). Hill's formula. *Russian
Mathematical Surveys, 65*(2), 191–257.
https://doi.org/10.1070/RM2010v065n02ABEH004671

Theorem 2.1 gives the discrete-Lagrangian relation between the action Hessian
and \(\det(P-I)\) for symplectic twist maps. Thus the cyclic identity
\(\det D^2\Phi_n=(-1)^{n+1}\det(I-DH_6^n)\) is an important Hénon
specialization but not a first general Hill theorem.

### 7. Adolphson and Sperber 2004 — Core, grade A

Adolphson, A., & Sperber, S. (2004). Exponential sums on
\(\mathbb A^n\), II. *Transactions of the American Mathematical Society,
356*(1), 345–369. https://doi.org/10.1090/S0002-9947-03-03324-5

Theorems 1.10 and 1.13 give a Dwork/p-adic cohomological framework, under the
paper's spectral-sequence hypotheses, in which the relevant degree is governed
by a sum of Milnor numbers.  This is prior art for a numerical
rank/critical-multiplicity equality.  It does not canonically decompose the
C32 \(\ell\)-adic group into critical-point summands, nor identify Hénon
critical values, multiplier data, or a Hilbert--Pólya structure.

### 8. Fornæss and Weickert 2000 — Core collision, grade A

Fornæss, J. E., & Weickert, B. (2000). A quantized Hénon map. *Discrete and
Continuous Dynamical Systems, 6*(3), 723–740.
https://doi.org/10.3934/dcds.2000.6.723

The authors quantize the classical Hénon map on \(\mathbb R^2\) and obtain a
unitary operator on \(L^2(\mathbb R)\). Therefore C32 cannot claim the first
quantization of a Hénon map. The paper does not supply the finite-field
Artin--Schreier/Frobenius construction proposed here.

### 9. Roberts and Vivaldi 2005 — Core finite-field control, grade A

Roberts, J. A. G., & Vivaldi, F. (2005). Signature of time-reversal symmetry
in polynomial automorphisms over finite fields. *Nonlinearity, 18*,
2171–2192. https://doi.org/10.1088/0951-7715/18/5/015

This paper studies finite-field reductions of polynomial automorphisms and
shows that reversibility strongly constrains cycle statistics. It is the
mandatory null/control literature for any apparent arithmetic signal from
finite Hénon orbit counts. It contains no Artin--Schreier quantization.

## B. Trace and categorical terminology boundaries

### 10. Gaitsgory and Varshavsky 2025 — Boundary, grade A

Gaitsgory, D., & Varshavsky, Y. (2025). Local terms for the categorical trace.
*Advances in Mathematics, 470*, 110223.
https://doi.org/10.1016/j.aim.2025.110223

Sections 0.1, 3, and 4.3–4.8 show that an actual categorical trace requires a
dualizable sheaf category, a specified endofunctor/correspondence, evaluation,
dualizing data, and the correct diagonal functor. This is why C32 uses the
more modest phrase “compactly supported diagonal kernel trace complex” for
\(R\Gamma_c(\Delta^*K^{\circ n})\).

### 11. Varshavsky 2007 — Boundary, grade A

Varshavsky, Y. (2007). Lefschetz–Verdier trace formula and a generalization of
a theorem of Fujiwara. *Geometric and Functional Analysis, 17*(1), 271–319.
https://doi.org/10.1007/s00039-007-0596-9

The paper develops trace maps for cohomological correspondences and a
Lefschetz–Verdier formula. It supports the statement that a genuine trace
formalism has hypotheses beyond a formal diagonal pullback. The elementary
finite-field identity needed by C32 already follows from Laumon's
sheaf--function rules.

### 12. Lu and Zheng 2022 — Boundary, grade A

Lu, Q., & Zheng, W. (2022). Categorical traces and a relative
Lefschetz–Verdier formula. *Forum of Mathematics, Sigma, 10*, e10.
https://doi.org/10.1017/fms.2022.2

This modern relative trace theorem works in a symmetric monoidal
2-category of cohomological correspondences and makes dualizability/local
acyclicity explicit. It is contextual support for the terminology firewall,
not a necessary ingredient in the finite-sum proof.

## C. Finite-field and arithmetic Hénon context

### 13. Roberts and Vivaldi 2009 — Context, grade A

Roberts, J. A. G., & Vivaldi, F. (2009). A combinatorial model for reversible
rational maps over finite fields. *Nonlinearity, 22*(8), 1965–1982.
https://doi.org/10.1088/0951-7715/22/8/011

The random-involution model explains the universal period statistics observed
for reversible finite maps. It strengthens the warning that raw finite-field
cycle statistics are not automatically arithmetic or spectral.

### 14. Gurevich and Hadani 2009 — Context, grade A

Gurevich, S., & Hadani, R. (2009). Quantization of symplectic vector spaces
over finite fields. *Journal of Symplectic Geometry, 7*(4), 475–502.
https://doi.org/10.4310/jsg.2009.v7.n4.a4

This constructs canonical finite-field quantization and the Weil
representation for linear symplectic spaces. It does not quantize a nonlinear
Hénon transformation, so it is context rather than a direct collision.

### 15. Gibbons, Hoffman, and Wootters 2004 — Context, grade A

Gibbons, K. S., Hoffman, M. J., & Wootters, W. K. (2004). Discrete phase space
based on finite fields. *Physical Review A, 70*, 062101.
https://doi.org/10.1103/PhysRevA.70.062101

The article constructs finite-field discrete phase spaces and Wigner
functions. It establishes that finite-field quantum phase-space language is
not new, but it does not provide the nonlinear Hénon kernel or its
Artin--Schreier cohomology.

### 16. Ingram 2014 — Context, grade A

Ingram, P. (2014). Canonical heights for Hénon maps. *Proceedings of the
London Mathematical Society, 108*(3), 780–808.
https://doi.org/10.1112/plms/pdt026

This is a central arithmetic-dynamics source for Hénon maps over number and
function fields. Its canonical-height results do not address finite-field
quantization or exponential-sum trace complexes.

### 17. de Hénon 2024 — Context, grade A

de Hénon, J. X. (2024). Hénon maps: A list of open problems. *Arnold
Mathematical Journal, 10*(4), 585–620.
https://doi.org/10.1007/s40598-024-00252-x

The survey maps current real, complex, algebraic, and arithmetic Hénon
questions. The searched text did not reveal the proposed Artin--Schreier
quantum-trace construction. This is search evidence, not proof of novelty.

### 18. Allen, DeMark, and Petsche 2018 — Context, grade A

Allen, K., DeMark, D., & Petsche, C. (2018). Non-Archimedean Hénon maps,
attractors, and horseshoes. *Research in Number Theory, 4*(1), Article 5.
https://doi.org/10.1007/s40993-018-0105-2

The work studies Hénon dynamics over complete locally compact
non-Archimedean fields and proves horseshoe/attractor results in parameter
regions. It confirms substantial arithmetic Hénon activity but does not
supply the finite-field sheaf-theoretic bridge.

## D. Assessed exclusions and near misses

### 19. Shudo, Ishii, and Ikeda 2002 — Excluded after assessment

Shudo, A., Ishii, Y., & Ikeda, K. S. (2002). Julia set describes quantum
tunnelling in the presence of chaos. *Journal of Physics A, 35*(17),
L225–L231. https://doi.org/10.1088/0305-4470/35/17/101

This is genuine quantum-Hénon context, but its subject is continuous
semiclassical tunnelling and complex Julia-set dynamics. It does not use
finite fields, Artin--Schreier sheaves, or Frobenius.

### 20. Shudo and Ikeda 2008 — Excluded after assessment

Shudo, A., & Ikeda, K. S. (2008). Stokes geometry for the quantum Hénon map.
*Nonlinearity, 21*, 1831–1880.
https://doi.org/10.1088/0951-7715/21/8/007

This extends exact-WKB/Stokes analysis for the quantum Hénon map. It raises
the collision level for any continuous semiclassical claim, but it does not
touch the finite-field arithmetic construction.

### 21. Endler and Gallas 2002 — Excluded as a semantic false friend

Endler, A., & Gallas, J. A. C. (2002). Arithmetical signatures of the dynamics
of the Hénon map. *Physical Review E, 65*, 036231.
https://doi.org/10.1103/PhysRevE.65.036231

Despite “arithmetical” in the title, the paper studies polynomial
parametrization and discontinuities in symbolic coding. It is important Hénon
periodic-orbit prior work, but not Artin--Schreier or number-theoretic
quantization.

### 22. Entin and Pirani 2023 — Excluded from the technical bridge

Entin, A., & Pirani, N. (2023). Local statistics for zeros of Artin--Schreier
\(L\)-functions. *Transactions of the American Mathematical Society, 376*(9),
6141–6175. https://doi.org/10.1090/tran/8850

The paper studies zero statistics for established families of
Artin--Schreier curves and finds random-matrix behavior. It was screened
because the conclusion can resemble a Hilbert--Pólya signal, but it does not
identify the Hénon action, chronological kernel powers, or Hill multipliers.
It is not evidence for the C32 bridge.

## E. Partial bridge sources found in the final expansion

### 23. Fu 2014 — Bridge, grade A

Fu, L. (2014). A Thom–Sebastiani theorem in characteristic \(p\).
*Mathematical Research Letters, 21*(1), 101–119.
https://doi.org/10.4310/MRL.2014.v21.n1.a8

Fu uses the \(\ell\)-adic Fourier transform and Laumon's stationary-phase
principle to identify the vanishing-cycle complex of a sum of two functions
with a local convolution of the individual vanishing-cycle complexes. This
confirms that positive-characteristic local convolution is the correct
language for a critical-point decomposition. It does not by itself give the
global decomposition, Frobenius indexing, or Hénon multiplier formula needed
by the remaining candidate gate.

### 24. Illusie 2017 — Bridge, grade A

Illusie, L. (2017). Around the Thom–Sebastiani theorem, with an appendix by
Weizhe Zheng. *Manuscripta Mathematica, 152*(1–2), 61–125.
https://doi.org/10.1007/s00229-016-0852-0

Illusie proves broad étale-cohomological Thom--Sebastiani variants over
fields of arbitrary characteristic, with local convolution replacing the
naive tensor product. This makes the proposed vanishing-cycle lane
mathematically plausible. It also raises the proof burden: the Hénon phase is
not a separated sum of independent germs, so a direct specialization and all
tameness/critical-value hypotheses must still be proved.

## Corpus-level novelty ruling

No direct prior source was found that simultaneously contains:

\[
\text{Hénon discrete action}
\;\longrightarrow\;
\text{finite-field raw kernel}
\;\longrightarrow\;
\text{extension-degree Frobenius traces}
\;\longrightarrow\;
\text{Hill-controlled local factors}.
\]

However, the first three arrows separately belong to established theories,
and the generic rank/purity result is fully prior art. The only potentially
new mathematical content is therefore a precise critical-value or
vanishing-cycle factorization whose local data is controlled by the Hénon
monodromy.
