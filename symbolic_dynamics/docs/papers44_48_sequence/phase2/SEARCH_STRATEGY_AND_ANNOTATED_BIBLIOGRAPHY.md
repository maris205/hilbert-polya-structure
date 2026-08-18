# Search Strategy and Annotated Primary-Source Bibliography — P44–P48

## Review question and freeze boundary

This Phase-2 review asks whether five distinct arithmetic symbolic-dynamics
objects can support five independent principal theorem packages after the
accepted P1–P43 baseline at Git commit
`6e5658649d2eab0fce077cbcdcc00070dd54095f`. It does not assume that five
survivors exist. The search cutoff for this freeze is 2026-08-18 UTC.

The review uses the Phase-1 object signature

```text
(phase space, dynamics, primitive type, repetition law, arithmetic source,
 clock, marker, operator owner, determinant owner, claim quantifiers)
```

and searches exact theorem signatures rather than title keywords. A broad
topic hit does not establish duplication; an exact object-and-quantifier hit
does. Conversely, failure to locate an exact hit is not a priority proof.

## Sources and search process

### Internal census

The internal corpus is a full-file census of the root README and Papers
1–43, including source locks, Route cards, proof files, experiment contracts,
result ledgers, manifests, and terminal audit reports. Searches used `rg`
over exact relation strings, operator kernels, named arithmetic predicates,
Schatten thresholds, fixed-point formulas, and determinant expressions.

### External retrieval

Primary retrieval used publisher/DOI landing pages, journal PDFs, arXiv
author manuscripts, institutional repositories, and primary monographs.
Backward and forward citation checks were applied around the closest exact
objects. Search families included:

- `multiplicative SFT finite prefix q-adic remainder accumulation boundary`;
- `radical squarefree kernel weighted composition Riesz projection Weyl`;
- `multiplicative Hankel perfect square product graph Schatten determinant`;
- `gcd k-free meet matrix Möbius factorization coprimality operator traces`;
- `powers of two sum Hankel Schatten lacunary cycle equation`;
- `integer reciprocal sum graph m+n divides mn weighted operator`;
- `binary carry-free graph bitwise disjoint weighted Schatten Kummer Lucas`;
- `finite B-admissible square-prime periodic points fixed count zeta`;
- `multiplication modulo N constrained coloring SFT fixed points zeta`;
- `algebraic Zd action simplex polynomial periodic points finite field`;
- `visible lattice admissible shift sublattice periodic point count`;
- rejected controls: beta `3/2`, finite carries, odometers, finite holonomy,
  square-sum Hankel, Rule 90, finite-prime B-free approximants, and periodic
  bouquets.

Metadata were checked against at least one first-party DOI, publisher, arXiv,
or institutional record. Technical ownership was checked from abstracts and,
where needed, the primary full text. Discovery-only search snippets were not
used as technical evidence.

### Screening flow

```text
internal census
  -> exact object signature
  -> primary-source theorem-signature search
  -> exact duplicate? STOP_DUPLICATE
  -> same proof skeleton only? MERGE/STOP_SALAMI audit
  -> new theorem delta + independent owner? proof audit
  -> two independent evaluator designs + adversarial controls
  -> provisional GO, still subject to Devil's Advocate checkpoint
```

## Annotated primary-source bibliography

### Multiplicative and gcd kernels

1. Perfekt, K.-M., & Pushnitski, A. (2018). On Helson matrices:
   Moment problems, non-negativity, boundedness, and finite rank.
   *Proceedings of the London Mathematical Society, 116*(1), 101–134.
   https://doi.org/10.1112/plms.12068

   This is the primary modern operator-theoretic framework for infinite
   multiplicative Hankel matrices `alpha(mn)`. It owns the generic Helson
   category, moment representation, boundedness questions, and finite-rank
   classification. It does not state the all-`k` perfect-power indicator,
   its residue-involution block spectrum, sharp Schatten ideals, or the
   parity-dependent trace/determinant products proposed here.

2. Brevig, O. F., & Perfekt, K.-M. (2015). Failure of Nehari's theorem for
   multiplicative Hankel forms in Schatten classes. *Studia Mathematica,
   228*(2), 101–119. Author manuscript: https://arxiv.org/abs/1409.3117

   This source establishes that Schatten questions for multiplicative Hankel
   forms are nontrivial and cannot be transferred naively from classical
   Hankel theory. Its examples and symbol problem differ from the exact
   perfect-power and power-free-gcd kernels.

3. Trent, L. (2022). *Structure of number theoretic graphs* (Mathematical
   Sciences Technical Report 179, Rose-Hulman Institute of Technology).
   https://scholar.rose-hulman.edu/math_mstr/179/

   Trent explicitly studies the finite square-product graph and owns its
   decomposition by squarefree part. This caps novelty for the unweighted
   finite `k=2` graph. It does not cover the infinite weighted all-`k`
   operator, its complementary residue classes, Schatten transition,
   regularized determinant, or all power traces.  The later Hilberdink
   subtraction nevertheless stops this proposal as a standalone paper; the
   finite graph remains only a control.

4. Beslin, S., & Ligh, S. (1989). Greatest common divisor matrices. *Linear
   Algebra and Its Applications, 118*, 69–76.
   https://doi.org/10.1016/0024-3795(89)90572-7

   This is a primary source for finite gcd-matrix factorization and
   positivity. It places any finite coprimality or gcd indicator matrix near
   the classical meet-matrix literature.  The subsequently tested all-`h`
   power-free-gcd kernel reduced to this incidence mechanism plus routine
   Euler factors and was therefore stopped as a standalone proposal.

5. Haukkanen, P. (1996). On meet matrices on posets. *Linear Algebra and Its
   Applications, 249*, 111–123.
   https://doi.org/10.1016/0024-3795(95)00349-5

   Haukkanen systematically develops meet matrices using incidence
   convolution. This owns the generic Möbius-factorization method used in a
   finite control.  No active paper number is assigned to the withdrawn
   power-free-gcd kernel, and no novelty is claimed for meet-matrix
   factorization.

6. Mussardo, G., Giudici, G., & Viti, J. (2017). The coprime quantum chain.
   *Journal of Statistical Mechanics: Theory and Experiment, 2017*, 033104.
   https://doi.org/10.1088/1742-5468/aa5bb4

   This paper owns finite coprimality interactions and analyzes their graph
   and many-body consequences. It is a direct collision for any claim that
   coprimality adjacency itself is new.  Together with the meet-matrix
   sources it helps place the rejected power-free-gcd construction in the
   control ledger rather than the active five-paper sequence.

### Additive and Diophantine kernels

7. Peller, V. V. (1985). A description of Hankel operators of class
   `S_p` for `p>0`, an investigation of the rate of rational approximation,
   and other applications. *Mathematics of the USSR-Sbornik, 50*(2),
   465–494. https://doi.org/10.1070/SM1985v050n02ABEH002840

   Peller owns the classical Hankel–Besov characterization and therefore the
   general analytic machinery behind a lacunary Schatten calculation. The
   proposed dyadic-sum paper must own its exact arithmetic support,
   valuation direct sum, sharp elementary endpoint proofs, closed-cycle
   parity theorem, and regularized trace product—not generic Peller theory.

8. Peller, V. V. (2003). *Hankel operators and their applications*. Springer.
   https://doi.org/10.1007/978-0-387-21681-2

   The monograph is the primary general reference for weighted/generalized
   Hankel operators and Schatten ideals. It sets the novelty ceiling but does
   not contain the exact power-of-two sum graph claimed here.

9. Fournier, J. J. F., & Wagner, B. G. (2015). Paley's theorem for Hankel
   matrices via the Schur test. Author manuscript:
   https://arxiv.org/abs/1505.01760

   This supplies a direct primary treatment of lacunary Hankel boundedness.
   It is a method comparator, not an exact collision with the two-sided
   arithmetic weight, the `v_2` block decomposition, or cycle equations.

10. Alekseyev, M. A. (2026). Maximizing the number of integer pairs summing
    to powers of 2 via graph labeling and solving restricted systems of
    linear (in)equations. *Journal of Computer and System Sciences, 157*,
    103735. https://doi.org/10.1016/j.jcss.2025.103735

    Alekseyev owns finite distinct-label graph systems whose edge sums are
    powers of two and an algorithm for power-of-two linear constraints. The
    object is close to the proposed cycle-equation evaluator, but it does not
    study the canonical infinite weighted adjacency operator, Schatten
    thresholds, `det_2`, or its trace ledger.

**Additional direct control.** Guo, Y.-J. (2019). On the regularity of the
    Hankel determinant sequence of the characteristic sequence of powers of
    2. *Advances in Applied Mathematics, 104*, 100–116.
    https://doi.org/10.1016/j.aam.2018.12.001

    Guo owns exact finite Hankel-determinant regularity for the unweighted
    powers-of-two characteristic sequence.  This is a direct finite control,
    not the infinite Dirichlet-weighted operator, its ideal endpoints, or its
    `v_2` closed-walk decomposition.

11. Mordell, L. J. (1958). On the evaluation of some multiple series.
    *Journal of the London Mathematical Society, 33*, 368–371.
    https://doi.org/10.1112/jlms/s1-33.3.368

    This is a foundational primary source for the multiple Dirichlet series
    now called Mordell–Tornheim sums. It owns the analytic-series background
    for the proposed harmonic/Egyptian kernel's second trace. It does not
    own the graph relation `m+n | mn`, the coprime-scale edge
    parameterization, or the associated Schatten/determinant theorem.

### Higher-rank controls and rejected directions

12. Lind, D., Schmidt, K., & Ward, T. (1990). Mahler measure and entropy for
    commuting automorphisms of compact groups. *Inventiones Mathematicae,
    101*, 593–629. https://doi.org/10.1007/BF01231517

    This establishes the Laurent-module framework and entropy/periodic-point
    setting for algebraic `Z^d` actions. It strongly limits novelty of a
    finite-field simplex candidate even where a specialized root-count
    formula is not written verbatim.

13. Ward, T. (1992). Periodic points for expansive actions of `Z^d` on
    compact abelian groups. *Bulletin of the London Mathematical Society,
    24*(4), 317–324. https://doi.org/10.1112/blms/24.4.317

    Ward owns the fixed-finite-index-subgroup framework and the celebrated
    three-dot periodic-point collapse. This makes a two-sequence simplex
    calculation insufficient as a new paper; only a genuinely broader exact
    theorem could survive, and it remains outside the frozen sequence unless
    a later gate reverses that conclusion.

14. Baake, M., Bustos, Á., Huck, C., Lemańczyk, M., & Nickel, A. (2021).
    Number-theoretic positive entropy shifts with small centraliser and large
    normaliser. *Ergodic Theory and Dynamical Systems, 41*, 3201–3226.
    https://doi.org/10.1017/etds.2020.111

    This source owns the visible-lattice/admissible-subset correspondence,
    heredity, and entropy framework. A finite-prime higher-rank fixed-point
    formula may be a useful exact extension, but the object and CRT mechanism
    are too close to P43 to be counted automatically as another paper.

15. Hall, P. (1936). The Eulerian functions of a group. *Quarterly Journal of
    Mathematics, os-7*(1), 134–151.
    https://doi.org/10.1093/qmath/os-7.1.134

    Hall owns the subgroup-lattice Möbius function used to pass from fixed
    configurations to exact stabilizers. The inversion itself cannot carry a
    novelty claim for a visible-lattice census.

16. Flatto, L., Lagarias, J. C., & Poonen, B. (1994). The zeta function of
    the beta transformation. *Ergodic Theory and Dynamical Systems, 14*(2),
    237–266. https://doi.org/10.1017/S0143385700007860

    This paper owns the beta-transformation periodic/zeta framework. The
    exact least-period set of the `3/2` shift may be a short new corollary,
    but it is not a standalone paper and is retained only as a control.

17. Holte, J. M. (1997). Carries, combinatorics, and an amazing matrix.
    *American Mathematical Monthly, 104*(2), 138–149.
    https://doi.org/10.1080/00029890.1997.11990612

    Holte owns the finite carry matrix and its spectrum. Standard trace and
    Möbius conversion of that spectrum does not create a new arithmetic
    symbolic paper, so cyclic-carry proposals are stopped.

### Finite admissible shifts and carry-free kernels

18. Bartnicka, A., Kasjan, S., Kułaga-Przymus, J., & Lemańczyk, M. (2018).
    B-free sets and dynamics. *Transactions of the American Mathematical
    Society, 370*, 5425–5489. https://doi.org/10.1090/tran/7132

    This source owns the general B-admissible/B-free framework, the finite-B
    minimal-period background, entropy statements, and the all-prime
    zero-minimal-subsystem boundary. It does not state the finite-prime-square
    `gcd(n,p^2)` inclusion–exclusion formula, but after PFT subtraction that
    delta is too short for a standalone paper and is retained only as a
    rejected control.

19. Konieczny, J., Kupsa, M., & Kwietniak, D. (2023). On B-free and
    B-admissible systems. *Ergodic Theory and Dynamical Systems, 43*,
    943–970. https://doi.org/10.1017/etds.2021.167

    Proposition-level results in this paper own explicit finite-truncation
    sofic presentations and transitivity of hereditary periodic-orbit
    closures. Therefore finite-B soficity or rational-zeta machinery cannot
    be claimed as new. The specialized census did not survive the subsequent
    anti-salami gate.

20. Kummer, E. E. (1852). Über die Ergänzungssätze zu den allgemeinen
    Reciprocitätsgesetzen. *Journal für die reine und angewandte
    Mathematik, 44*, 93–146. https://doi.org/10.1515/crll.1852.44.93

    Kummer owns the valuation-of-binomial-coefficients carry theorem. In
    base two it gives `m & n = 0` exactly when `binom(m+n,m)` is odd. The
    digit theorem is prior art; the proposed contribution is the infinite
    Dirichlet-weighted operator's sharp nuclear threshold and its symbolic
    trace closure.

21. Lucas, É. (1878). Théorie des fonctions numériques simplement
    périodiques. *Bulletin de la Société Mathématique de France, 6*,
    49–54. https://doi.org/10.24033/bsmf.127

    Lucas owns the digitwise congruence theorem underlying finite
    zero-completed carry-free matrices. It does not contain the weighted
    countable operator, Schatten endpoint `log_2(sqrt(5))`, or `det_2`
    ledger.

22. Alman, J., Guan, S., & Padaki, A. (2023). Faster algorithms for
    structured matrices and disjointness matrices. In *Proceedings of
    SODA 2023*. https://doi.org/10.1137/1.9781611977554.ch160

    This is a close modern source for finite disjointness/Kronecker matrices.
    It owns fast finite-matrix structure, not the dyadic-shell trace-norm
    summation or the infinite arithmetic phase transition.

23. Chistikov, D., Iván, S., Lubiw, A., & Shallit, J. (2017).
    Fractional covers of the Kneser--Sierpiński matrix. In *STACS 2017*.
    https://doi.org/10.4230/LIPIcs.STACS.2017.23

    The Kneser--Sierpiński matrix is another finite disjointness comparator.
    It sets a clear novelty ceiling for the unweighted finite tensor. It does
    not address the Dirichlet weighting, exact Schatten thresholds, or the
    countable Markov shift.

24. Christopher, M. J., & Kennedy, J. W. (1997). Binomial graphs and their
    spectra. *Fibonacci Quarterly, 35*(1), 15–21.
    https://doi.org/10.1080/00150517.1997.12429027

    This paper already owns the finite binary bit-disjoint/binomial graph,
    its golden-ratio spectrum, and Lucas closed-walk counts. Consequently the
    zero-completed identity `C_2 tensor-power k` is only a diagnostic fixture
    here. Paper 48 must be the all-radix, Dirichlet-weighted infinite
    Schatten theorem; no finite Lucas census may be advertised as new.

25. Bacher, R., & Chapman, R. (2004). Symmetric Pascal matrices modulo p.
    *European Journal of Combinatorics, 25*, 459–473.
    https://doi.org/10.1016/j.ejc.2003.06.001

    This is a direct finite-base-`p` comparator. It owns modular Pascal
    matrix structure but not the countable Dirichlet-weighted no-carry
    adjacency, base-shell nuclear norms, or the critical exponents
    `alpha_p=log_p ||C_p||_1`.

26. Linial, N., & Shraibman, A. (2007). Lower bounds in communication
    complexity based on factorization norms. In *STOC 2007*.
    https://doi.org/10.1145/1250790.1250892

    This source already uses the binary disjointness tensor and its finite
    trace norm `5^(L/2)`. Thus neither `sqrt(5)` nor the finite tensor norm is
    new. The eligible delta remains the infinite Dirichlet weighting, sharp
    all-radix `S_q` shell threshold, determinant, and positive-vertex
    periodic ledger.

### Mordell--Tornheim and rejected cyclic controls

27. Bradley, D. M., & Zhou, X. (2013). On Mordell--Tornheim sums and
    multiple zeta values. Author manuscript: https://arxiv.org/abs/1205.0037

    This source owns identities for the classical multiple series appearing
    in the harmonic kernel's second trace. It does not own the edge relation,
    coprime-scale parametrization, operator ideals, or regularized
    determinant.

28. Kenyon, R., Peres, Y., & Solomyak, B. (2012). Hausdorff dimension for
    fractals invariant under the multiplicative integers. *Ergodic Theory
    and Dynamical Systems, 32*, 1567–1584.
    https://doi.org/10.1017/S0143385711000538

    This paper owns the infinite multiplicative golden-mean/multiplicative
    SFT direction, its leading entropy, and its leading dimensions.  The
    revised Paper 44 assigns all of that ownership here and claims only the
    exact order-one `q`-adic boundary spectrum. Together with standard finite
    multiplication-cycle and Bowen--Lanford trace formulas, it also makes the
    rejected finite cyclic multiplicative SFT a classical-component assembly.

29. Laohakosol, V., Pintoptang, S., & Tadee, R. (2014). The concept of
    q-cycle and applications. *Journal of Discrete Mathematics*, 2014,
    823567. https://doi.org/10.1155/2014/823567

    This source explicitly owns multiplication-by-`q` cycle arithmetic
    modulo `N`. The exact constrained-coloring product formula was not found
    verbatim, but its combination with standard SFT traces is too direct to
    carry a separate paper here.

### Late nearest-owner corrections

30. Hilberdink, T. (2017). Matrices with multiplicative entries are tensor
    products. *Linear Algebra and its Applications, 532*, 179–197.
    https://doi.org/10.1016/j.laa.2017.06.037

    This is the nearest general owner for the withdrawn perfect-power
    proposal. It proves that infinite
    matrices whose two-variable entries are multiplicative decompose as
    infinite tensor products over primes, and treats general boundedness,
    norm, spectrum, and multiplicative Toeplitz/Hankel questions. Therefore
    tensor-product decomposition and generic norm criteria are not new. After
    subtracting this theorem, the residue-complement specialization is too
    short and is `STOP_SALAMI`, not Paper 45.

31. Manada, A., & Kashyap, N. (2013). On the zeta function of a
    periodic-finite-type shift. *IEICE Transactions on Fundamentals of
    Electronics, Communications and Computer Sciences, E96.A*(6),
    1024–1031. https://doi.org/10.1587/transfun.E96.A.1024
    Extended manuscript: https://arxiv.org/abs/0904.2375

    This is the nearest general owner for the withdrawn finite-B proposal. It
    gives matrix/word-graph
    formulas for periodic points and zeta functions of periodic-finite-type
    shifts. Paper 44 therefore cannot claim general PFT/sofic rational-zeta
    ownership. The residual specialized CRT formula, exact-period criterion,
    and standard inversion do not meet the standalone size gate.

32. LaGrange, J. D. (2013). Eigenvalues of Boolean graphs and Pascal-type
    matrices. *International Electronic Journal of Algebra, 13*, 109–119.
    Journal full text:
    https://www.ieja.net/files/papers/volume-13/Volume-13-2013/11-V13-2013.pdf

    This paper determines spectra and multiplicities for finite Boolean-ring
    zero-divisor graphs using Pascal-type quotient matrices. It is a nearer
    finite control for Paper 48 than generic carry literature, so finite
    Boolean/disjointness spectra and their Pascal reduction are explicitly
    subtracted. It does not treat the Dirichlet-weighted infinite operator,
    sharp all-radix Schatten endpoints, or the associated `det_2` ledger.

### Revised-sequence nearest owners

33. Fan, A.-H., Liao, L., & Ma, J.-H. (2012). Level sets of multiple
    ergodic averages. *Monatshefte für Mathematik, 168*(1), 17–26.
    https://doi.org/10.1007/s00605-011-0358-5

    This source already contains the multiplicative golden-mean setting,
    Fibonacci chain counts, and leading dimension calculation. Revised Paper
    44 does not claim any of those items; it starts at the exact bounded
    finite-size remainder.

34. Ban, J.-C., Hu, W.-G., & Lai, G.-Y. (2023). Boundary complexity and
    surface entropy of 2-multiplicative integer systems on `N^d`.
    *Journal of Mathematical Physics, 64*, 062704.
    https://doi.org/10.1063/5.0118652
    Author manuscript: https://arxiv.org/abs/2210.09115

    This is the closest title and conceptual boundary for revised Paper 44.
    It owns speed-dependent boundary complexity and surface entropy, but its
    full text does not give the exact order-one `q`-adic remainder, complete
    accumulation image, or golden boundary Cantor dimension.

35. Ban, J.-C., Hu, W.-G., Lai, G.-Y., & Liao, L. (2025). Hausdorff
    dimensions of affine multiplicative shifts. *Advances in Mathematics,
    471*, 110266. https://doi.org/10.1016/j.aim.2025.110266

    This recent primary source extends leading fractal-dimension ownership.
    It does not state the subleading `q`-adic theorem proposed here.

36. Luan, D. M., & Khoi, L. H. (2015). Weighted composition operators on
    weighted sequence spaces. *Contemporary Mathematics, 645*, 199–215.
    https://doi.org/10.1090/conm/645/12907

    This source owns generic boundedness and compactness questions for
    weighted composition on sequence spaces. It fixes the framework ceiling
    for Paper 45; rank-one fibers or compactness alone cannot be new.

37. Carlson, J. W. (1990). The spectra and commutants of some weighted
    composition operators. *Transactions of the American Mathematical
    Society, 317*(2), 631–654.
    https://doi.org/10.1090/S0002-9947-1990-0979958-6

    Carlson studies discrete weighted composition spectra and commutants,
    primarily under finite-branch/near-injectivity hypotheses. The paper does
    not contain the arithmetic saturated/modulo retraction pair, its Weyl
    constants, primorial projection growth, or commutator ideal wall.

38. Nordin, A., & Noorani, M. S. M. (2020). Orbit growth of periodic-finite-
    type shifts via Artin--Mazur zeta function. *Mathematics, 8*(5), 685.
    https://doi.org/10.3390/math8050685

    This source owns the simple Perron root-of-unity pole necklace for an
    irreducible PFT presentation. It removes finite-stage pole novelty from
    the backup admissible-tower candidate; only a genuinely cross-stage
    convergence theorem could remain.

39. de Weger, B. M. M., & van de Woestijne, C. E. (1999). On the power-free
    parts of consecutive integers. *Acta Arithmetica, 90*(4), 387–395.
    https://doi.org/10.4064/aa-90-4-387-395

    This is a primary arithmetic source for power-free-part terminology and
    nearby Diophantine uses.  The standard map and terminology receive zero
    novelty credit in Paper 45; its eligible delta is the paired operator
    geometry, exact Weyl/maximal-order laws, and commutator comparison.

## Evidence quality and source-distribution audit

- Evidence grade for generic frameworks and exact collisions: **A** when a
  DOI/publisher primary text states the relevant object or theorem.
- Evidence grade for absence of an exact package: **B-** at best; it is a
  reproducible negative search, not a priority proof.
- Primary sources span operator theory, number-theoretic graph theory,
  symbolic/algebraic dynamics, and arithmetic combinatorics.
- No candidate author is part of this review team; no financial or personal
  conflict was identified.
- Currency is mixed by design: foundational ownership sources are old, while
  exact-object searches include 2024–2026 records.

## Current screening status

The revised audit supports five exact positions after the independent
Paper 45 and final five-way seals: q-adic multiplicative-SFT boundary
spectrum; paired all-`h` arithmetic retractions; dyadic-sum Hankel;
harmonic/Egyptian adjacency; and all-radix carry-free adjacency. The former
finite-prime-square and perfect-power positions are explicitly stopped, not
silently counted. The nested PFT pole wall remains a backup HOLD. All other
listed beta, odometer, finite-holonomy, power-free-gcd, visible-lattice,
finite-field, and cyclic-SFT proposals remain stopped or merged. The revised
Devil's Advocate gate is sealed at the scientific level; no authority write
is implied by that seal.
