# Novelty Audit: Good-Reduction Hénon Rational-Modulus Certificate

**Search boundary:** literature and preprints checked through 2026-08-13  
**Candidate:** `integral_area_henon_multiplier_support_v1`  
**Lock:** v2, strengthened before candidate execution to exact rational modulus  
**Audit state:** completed before candidate execution

## Verdict

`PROCEED ONLY AS A NARROW CERTIFICATE NOTE / MERGE IF REVIEWERS REQUIRE A DEEPER THEOREM`

The exact frozen conclusion is clean: the area-preserving polynomial Hénon
map inherited at the algebraic-integer parameter $u$ has no multiplier of
exact rational-prime modulus at any complex periodic orbit, even if the
multiplier itself is nonrational.  The $S$-integral finite-composition
extension makes the obstruction reusable: prime factors of any exact
rational multiplier modulus must already lie in the map's finite bad-prime
support.

The underlying ingredients, however, are standard good-reduction ideas:
non-archimedean boundedness of periodic orbits, integrality of the derivative
matrix, determinant one, stability of units under complex conjugation, and
the definition of an $S$-unit.  The result must not be marketed as a new
general theory of Hénon multipliers.

Estimated novelty:

- periodic-coordinate integrality at good places: **2/10** (standard local
  filtration / good-reduction consequence);
- algebraic-unit multiplier consequence in determinant one: **2/10**
  (elementary once integrality is known);
- exact rational-modulus consequence via $\lambda\overline\lambda$:
  **3/10** mathematically, but materially stronger than rational-eigenvalue
  exclusion;
- all-period frozen prime-modulus clock obstruction: **5/10** as a
  precise design certificate in this research sequence;
- $S$-integral finite-composition rational-modulus support packaging with a
  sharp planted control: **5/10**;
- global Hénon symplecticity: **0/10** (classical).

I found no checked paper whose headline is the exact rational-modulus
prime-support corollary for periodic Hénon multipliers.  That negative search
does not establish priority: the proof is short enough to be folklore-level.

## Proposed contribution

For a finite composition of monic area-preserving generalized Hénon maps
over $\mathcal O_{K,S}$:

1. prove algebraicity of every complex periodic point and then use a cyclic
   non-archimedean maximum argument to make its coordinates integral outside
   $S$;
2. deduce that each periodic monodromy is in
   $\mathrm{SL}_2$ of the integral closure;
3. deduce that both multipliers are $S$-units;
4. pass to a conjugation-stable Galois closure and conclude that any exact
   rational multiplier modulus has support only at bad primes;
5. apply this to the inherited integral parameter $u$ and contrast it with
   the exact denominator control $a=-15/16$, whose fixed multipliers are
   $2$ and $1/2$.

The contribution is an **arithmetic design filter for exact
rational-modulus clocks**, not a classification of Hénon spectra.
The conjugation step is elementary and is not advertised as an application
or extension of Kronecker's theorem.

## Core claims and collision assessment

| Claim | Novelty | Closest boundary | Safe positioning |
|---|---:|---|---|
| Polynomial plane automorphisms reduce to generalized Hénon normal forms. | None | Friedland--Milnor (1989) | Background only. |
| At a good non-archimedean place, a periodic orbit of a monic generalized Hénon map stays in the unit polydisc. | Low | Ingram explicitly states the quadratic $\mathbb Z_p$ periodic-coordinate case; Kawaguchi's local Green functions and Allen--DeMark--Petsche's filtrations give broader context | Give the two-line maximum proof and acknowledge it as a standard good-reduction phenomenon. |
| Determinant-one integral monodromy has algebraic-unit multipliers. | Very low | Elementary characteristic-polynomial and $S$-unit arithmetic | Lemma/corollary, never the novelty headline. |
| Prime factors of an exact rational multiplier modulus lie in the bad-prime support $S$. | Low--medium as packaging | Unit stability under conjugation plus the preceding facts; no exact collision located | Call it a rational-modulus prime-support certificate in this specific research program. |
| The frozen $H_u$ excludes exact rational-prime modulus at every complex periodic orbit. | Medium as a case result | No parameter-specific statement found | Main certified case study, with no historical-first claim. |
| The denominator control realizes multipliers $2,1/2$. | None | Prescribed fixed-multiplier loci are classical and explicit in Hénon parameter space | Sharp control, not contribution. |
| Multiplier spectra determine Hénon maps up to finite ambiguity. | None and much deeper | Cantat--Dujardin (2026) | Cite as a strong adjacent frontier; do not imply our elementary value obstruction competes with it. |

## Closest prior work and exact boundaries

### Structural and arithmetic Hénon foundations

1. **Friedland and Milnor, “Dynamical properties of plane polynomial
   automorphisms,” Ergodic Theory and Dynamical Systems 9(1) (1989),
   67--99.**
   [DOI 10.1017/S014338570000482X](https://doi.org/10.1017/S014338570000482X).
   This is the foundational classification/normal-form source for polynomial
   automorphisms of the plane.  It establishes the generalized Hénon setting;
   it is not a source of novelty for the map family.

2. **Silverman, “Geometric and arithmetic properties of the Hénon map,”
   Mathematische Zeitschrift 215(2) (1994), 237--250.**
   [DOI 10.1007/BF02571713](https://doi.org/10.1007/BF02571713).
   This early arithmetic study develops height and periodic-point structure
   for Hénon maps over global fields.  It is a core predecessor for any
   arithmetic claim about algebraic Hénon periodic points; the present
   prime-support statement should be presented as a later elementary
   good-reduction corollary rather than as the start of that subject.

3. **Marcello, “Sur la dynamique arithmétique des automorphismes de
   l'espace affine,” Bulletin de la Société Mathématique de France 131(2)
   (2003), 229--257.**
   [DOI 10.24033/bsmf.2441](https://doi.org/10.24033/bsmf.2441).
   This studies arithmetic properties and periodic points of regular and
   triangular affine polynomial automorphisms, completing parts of the
   dimension-two arithmetic picture.  It is broad arithmetic-automorphism
   prior art, not an exact collision with return-multiplier modulus support.

4. **Kawaguchi, “Canonical height functions for affine plane
   automorphisms,” Mathematische Annalen 335(2) (2006), 285--310.**
   [DOI 10.1007/s00208-006-0750-y](https://doi.org/10.1007/s00208-006-0750-y),
   [arXiv:math/0405007](https://arxiv.org/abs/math/0405007).
   It constructs canonical heights for plane polynomial automorphisms of
   dynamical degree at least two and characterizes periodic algebraic points
   by height zero.  This places periodic-point arithmetic well before the
   present note.

5. **Kawaguchi, “Local and global canonical height functions for affine
   space regular automorphisms,” Algebra & Number Theory 7(5) (2013),
   1225--1252.**
   [DOI 10.2140/ant.2013.7.1225](https://doi.org/10.2140/ant.2013.7.1225).
   It defines good reduction for regular polynomial automorphisms, constructs
   non-archimedean Green functions, and shows that outside a finite bad set
   the local correction constants vanish.  This is the closest general
   conceptual precedent for the local integrality step.

6. **Ingram, “Canonical heights for Hénon maps,” Proceedings of the London
   Mathematical Society 108(3) (2014), 780--808.**
   [DOI 10.1112/plms/pdt026](https://doi.org/10.1112/plms/pdt026),
   [arXiv:1111.3609](https://arxiv.org/abs/1111.3609).
   It studies arithmetic of Hénon maps over number and function fields,
   variation in families, periodic parameters, and lower bounds controlled by
   bad reduction.  Before its good-reduction period computation, it states
   explicitly that for $b\in\mathbb Z_p$, every $\mathbb Q_p$-periodic point
   of $(x,y)\mapsto(y,x+y^2+b)$ has $p$-adic-integral coordinates.  Thus even
   the candidate's basic quadratic-coordinate integrality mechanism has a
   direct precedent; our additional step is the return-multiplier modulus
   support package.

7. **Dujardin and Favre, “The dynamical Manin--Mumford problem for plane
   polynomial automorphisms,” Journal of the European Mathematical Society
   19(11) (2017), 3421--3465.**
   [DOI 10.4171/JEMS/743](https://doi.org/10.4171/JEMS/743),
   [arXiv:1405.1377](https://arxiv.org/abs/1405.1377).
   Under a dense-periodic-curve hypothesis it proves that the global
   Jacobian and all its Galois conjugates have modulus one, with a
   root-of-unity consequence under integrality.  It concerns the map's
   constant Jacobian rather than eigenvalues of individual periodic return
   derivatives, but it is an important warning that algebraic integrality,
   Galois conjugation, and archimedean modulus are established tools in plane
   polynomial dynamics.

8. **Hsia and Kawaguchi, “Heights and periodic points for one-parameter
   families of Hénon maps” (2018 preprint).**
   [arXiv:1810.03841](https://arxiv.org/abs/1810.03841).
   It studies adelic height functions and periodic parameter values in Hénon
   families.  It is relevant family-arithmetic context, not an exact
   rational-modulus multiplier collision.

9. **Allen, DeMark, and Petsche, “Non-Archimedean Hénon maps, attractors,
   and horseshoes,” Research in Number Theory 4 (2018), Article 5, 30 pp.**
   [DOI 10.1007/s40993-018-0105-2](https://doi.org/10.1007/s40993-018-0105-2).
   This gives explicit non-archimedean Hénon filtrations and describes when
   filled Julia sets equal a unit ball, are attracting, or are horseshoes.
   It strongly cautions against calling the maximum-norm mechanism new.

10. **Berger, Bedford, Bianchi, Buff, Crovisier, Dinh, Dujardin, Favre,
   Firsova, Ingram, Ishii, Palmisano, Pujals, Raissy, Štimac, and Vigny,
   “Hénon maps: a list of open problems,” Arnold Mathematical Journal 10
   (2024), 585--620.**
   [DOI 10.1007/s40598-024-00252-x](https://doi.org/10.1007/s40598-024-00252-x).
   Its number-field section explicitly formulates generalized Hénon maps
   with good reduction away from $S$ as having $S$-integral coefficients and
   unit leading/Jacobian data.  This is the current community vocabulary for
   the proposed extension.

11. **Kim, Krieger, Postolache, and Szeto, “Hénon maps with many rational
   periodic points” (2024 preprint).**
   [arXiv:2412.01668](https://arxiv.org/abs/2412.01668).
   It constructs Hénon maps over $\mathbb Q$ with many integral periodic
   points and long integer cycles.  It shows that coordinate integrality is
   an active construction theme; our issue is the arithmetic of return
   eigenvalues, not abundance of rational points.

### Multiplier frontier

12. **Cantat and Dujardin, “Some rigidity results for polynomial
   automorphisms of $\mathbb C^2$,” Cambridge Journal of Mathematics 14(3)
   (2026), 539--601.**
   [DOI 10.4310/CJM.260722225236](https://doi.org/10.4310/CJM.260722225236),
   [arXiv:2411.10339](https://arxiv.org/abs/2411.10339).
   It studies fields of definition of saddle-periodic multipliers along with
   strong analytic rigidity.  This is directly adjacent arithmetic-multiplier
   context and is much deeper than a unit-support corollary.

13. **Cantat and Dujardin, “Multiplier rigidity for complex Hénon maps”
    (2026 preprint).**
    [arXiv:2603.09445](https://arxiv.org/abs/2603.09445).
    It proves that a complex Hénon map of fixed degree is determined up to
    finitely many choices by its trace spectrum or unstable multiplier
    spectrum; for compositions, multidegree and multi-Jacobian are fixed.
    It concerns recovery from the whole spectrum, while our note excludes a
    thin set of exact rational modulus values under good-reduction
    hypotheses.

## Why standalone novelty remains fragile

A referee can compress the argument to:

> good reduction bounds periodic points; the derivative is integral; the
> determinant is one; hence eigenvalues are units; multiplying by the complex
> conjugate controls any rational modulus.

That compression is mathematically fair.  Neither using a finite composition
nor specializing to the inherited $u$ adds deep machinery.  The proposed note
is viable only if its stated purpose is a transparent obstruction certificate
within a sequence of arithmetic-clock designs, supported by exact controls
and careful nonclaims.

## What survives as the paper's delta

The defensible delta is the complete certificate chain:

1. a frozen algebraic-integer parameter inherited before any multiplier
   inspection;
2. a global nonlinear polynomial symplectic map rather than a singular
   branch lift;
3. an all-period, place-by-place obstruction to exact rational-prime return
   moduli without assuming rational eigenvalues;
4. a finite-bad-prime extension for compositions;
5. a sharp exact control showing how prime $2$ reappears once it is inserted
   into the denominator support;
6. a reproducible low-period algebra audit used only to test implementation,
   never to infer the theorem.

## Explicit nonclaims

- No priority claim for good-reduction boundedness, canonical heights, or
  algebraic-unit eigenvalues.
- No claim that $H_u$ has no large or unstable multipliers.
- No classification of irrational complex moduli or spectral radii, and no
  obstruction for singular values or Lyapunov exponents.  Exact rational
  moduli (and therefore exact rational spectral radii in this determinant-one
  two-dimensional setting) are part of the theorem.
- No claim that all periodic points are defined over $K$.
- No claim that $+1$ or $-1$ occurs or does not occur.
- No prime-orbit correspondence, prime density, Riemann determinant, target
  zero comparison, or natural quantization.
- No use of external prime or zero data in candidate choice or evaluation.

## Query log and negative-search boundary

Searches included recent 2024--2026 variants of:

- `Henon map periodic points algebraic integers good reduction multiplier`
- `generalized Henon map good reduction S-integral periodic points`
- `polynomial automorphism periodic multiplier algebraic unit`
- `S-integral Henon periodic monodromy S-unit`
- `Henon multiplier rational modulus algebraic unit`
- `periodic multiplier absolute value rational S-unit`
- `non-Archimedean Henon maps periodic unit ball`
- `canonical heights Henon maps Kawaguchi Ingram Hsia`
- `Henon multiplier field number field Cantat Dujardin`
- `multiplier rigidity complex Henon maps 2026`
- `area preserving Henon prescribed fixed multiplier`
- `Henon maps rational integral periodic points 2024`

No checked title or abstract states the same finite-bad-prime
rational-modulus multiplier certificate.  The rational-modulus-specific
queries were rerun after strengthening the theorem and likewise found no
headline collision.  Because the result is a direct synthesis of standard
facts, the absence of an exact phrase match is not evidence of high novelty.

## Independent audit outcome

An independent proof-and-novelty audit confirmed the cyclic recurrence,
projective algebraicity proof, non-archimedean maximum lemma, integral
$\mathrm{SL}_2$ monodromy, and algebraic-unit conclusion.  It also confirmed
the strengthened exact rational-modulus statement after one mandatory
repair: for a general non-Galois $(K,S)$ one must not assume that complex
conjugation preserves the original place set.  `PROOF_PACKAGE.md` now passes
to a finite Galois extension over $\mathbb Q$ and uses all places above
$S_{\mathbb Q}$, which is conjugation-stable without changing rational-prime
support.

The independent novelty estimate was approximately **4/10** for a standalone
theorem and **5/10** for the frozen all-period obstruction certificate.  Its
recommendation agrees with this audit: retain the result as a short exact
good-reduction certificate or merge it into a broader negative-results paper;
do not position it as multiplier or spectral rigidity.

## Final recommendation

Proceed through exact implementation and later manuscript review if the
intended output is a concise arithmetic-dynamics certificate note.  If a reviewer
requires a standalone conceptual advance comparable to current multiplier
rigidity work, merge this result into a broader obstruction paper rather
than inflating its novelty.
