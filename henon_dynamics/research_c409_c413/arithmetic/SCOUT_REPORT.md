# Arithmetic/native-orbit scout: five distinct questions

2026-09-06. Scoped to the C409–C413 selection stage. This report assigns
no C-number, does not admit a manuscript, and does not certify worldwide
priority. Only the first question currently has a complete proposed
post-classical proof. The other four are recorded as eliminations or
unproved reserves, not padded deliverables.

## Outcome after classical deduction

| Question | Native observable | Decisive screen | Present disposition |
|---|---|---|---|
| A. Wild multiple-phase FAD boundary | Ordinary fixed-count series and Artin–Mazur zeta | Exact phase aggregation and dense nonzero atoms; BHN removes the no-wild novelty claim | Complete author proof; independent admission still required |
| B. Inverse finite-adelic orbit data | Reconstruction from the full ordinary fixed-count sequence | BCH uniqueness already owns the FAD parameters | Eliminate as a standalone theorem |
| C. Joint power/Frobenius returns | Two-clock common fixed-point counts | Exact gcd reduction and the classical diagonal gcd estimate | Exact formula classical; no effective new theorem established |
| D. Integral polynomial orbit decomposition | Periodic points, clopen minimal components, basins on $\mathbb Z_p$ | Fan–Liao and the internal C394 direction | Eliminate the proposed general/classical formulation |
| E. Infinite-place arithmetic distortion | Ordinary fixed counts on an infinite-$S$ solenoid | Existing sparse-complement theorem; finite Fourier proof does not extend automatically | Reserve only; no complete proof |

These are different inverse, joint-return, topological-decomposition,
and analytic-continuation questions, not parameter specializations of
the first theorem. Their failures are useful selection evidence but
do not constitute new mathematical contributions.

## A. Phase-safe wild natural boundaries

**Object, domain, parameters and clock.** A confined FAD self-map,
with native integer time $n\geq1$, finite prime set $S$, integral matrix
$A$, positive periodic $r_n$, and periodic nonnegative distortion data:
$$
 f_n=\#\operatorname{Fix}(f^n)
 =|\det(A^n-I)|c^n r_n
   \prod_{p\in S}p^{-s_{p,n}v_p(n)-t_{p,n}p^{v_p(n)}}.
$$
The system has positive counting entropy $\log\Lambda>0$. The target
is continuation of $\sum f_nz^n$ and
$\zeta_f(z)=\exp(\sum f_nz^n/n)$ at $|z|=\Lambda^{-1}$.
No recoding of the observable or claim about the Riemann zeta function
is introduced.

**Proposed theorem.** The genuinely distorted branch has a natural
boundary, including multiple archimedean dominant phases and wild
distortion. The underlying analytic theorem permits complex periodic
coefficients, arbitrary unit-modulus phases and real nonnegative local
exponents; after grouping phases whose ratios are roots of unity, a
finite active-fibre condition exactly distinguishes rationality from
a natural boundary.

**Classical inputs fully deducted.** BCH supplies the FAD framework,
fixed counts, dominant expansion and positivity, root-rational branch,
and the hyperbolic boundary theorem. Dense atoms of a finite Cauchy
measure give boundary singularities by an elementary radial limit;
that general analytic mechanism is also not claimed as new. The
2026 Cornelissen–Park paper already uses Fourier analysis of the FAD
coefficients for a different asymptotic objective.

Most importantly, Baril Boudreau–Holmes–Nguyen (BHN),
*Adelic perturbation of rational functions and applications*,
[arXiv:2307.07910v1](https://arxiv.org/pdf/2307.07910v1),
published in *Math. Ann.* 392 (2025), 2253–2275,
[DOI 10.1007/s00208-025-03155-0](https://doi.org/10.1007/s00208-025-03155-0),
already owns the no-wild FAD conclusion by the explicit deduction in
`POSTCLASSICAL_DELTA.md`. Their abelian-variety and finite-place
solenoid results are not new conclusions of this project.

**What remains after subtraction.** The proof constructs the actual
atomic coefficient measure after all finite torsion collisions,
establishes unbounded local conductors on an active fibre, and uses
local unit symmetries to obtain arbitrarily fine grids of equal,
nonzero atoms. This controls cancellation between multiple dominant
phases. The genuinely wild example has perturbation
$g(n)=p^{-p^{v_p(n)}}$ with $h(g(p^a))=p^a\log p$, so it fails BHN's
sublinear-height assumption. It is not simply another application of
their theorem.

**Cheap decisive checks actually completed.**

- A necessary cancellation control is
  $u_n=1-(-1)^n$, $H(n)=|n|_2$. Its apparent distortion gives the
  rational series $2z/(1-z^2)$; the exact active-fibre condition
  correctly fails. Thus an unsupported rule that a finite sum of
  natural-boundary series still has a natural boundary is not used.
- A genuine nonhyperbolic wild product is built from the Salem toral
  automorphism with polynomial $x^4-x^3-x^2-x+1$ and the additive
  self-map $x\mapsto x^p+x$ on $\overline{\mathbb F}_p$, for odd $p$.
  `REALIZED_EXAMPLE.md` proves its count and all required properties.
  Its factor counts and the Salem construction are classical inputs;
  the example does not become a second contribution.
- The abstract proof does not call C407's covering or perfectness
  theorem. C407 concerns the topology of orbit-count limit images,
  whereas this candidate concerns analytic continuation of the
  original fixed-count series. Shared elementary radial expansions
  are acknowledged rather than repackaged as new lemmas.

**Files and admission boundary.** `PROOF_PACKAGE.md` contains the full
argument, `POSTCLASSICAL_DELTA.md` the BHN deduction,
`REALIZED_EXAMPLE.md` the genuine test, and `SOURCE_AUDIT.md` the exact
primary-source reading scope. The coordinator has separately checked
the mathematical core; neither that check nor this author report
settles final-version ownership. The full BHN publisher text and the
forthcoming EMS final book were not obtained. Any novelty statement
must preserve those version limitations.

## B. Recover the finite-adelic system from its native orbit counts

**Object and question.** For scalar finite-$S$ solenoids, or more
generally genuine FAD data, does equality of $f_n$ for every native
integer time determine the exponential multiplier and active local
distortion? Parameters include the multiplier, finite primes and
periodic local exponents; the observable is the unweighted fixed-count
sequence, not a decorated spectrum.

**Classical owner and failure gate.** BCH
[arXiv:2209.00085v2](https://arxiv.org/pdf/2209.00085v2),
Proposition 11.2.1 gives uniqueness of the FAD representation in its
specified sense, including the active distortion data. Its statement
and proof were inspected. Matrix realization itself need not be
unique; cyclic-resultant and conjugacy ambiguities must not be
confused with a new uniqueness theorem for the count representation.

An elementary progression argument for scalar multipliers therefore
only re-proves a specialization. The broader inverse-conjugacy problem
is not solved by such an argument. This candidate is eliminated;
there is no separate proof package or proposed manuscript.

## C. Two-clock common power/Frobenius returns

**Object, domain and observable.** On
$X=\overline{\mathbb F}_p^{\times}$, take the commuting maps
$P_d(x)=x^d$ and $\operatorname{Fr}_p(x)=x^p$, with $d\geq2$.
At genuine two-clock time $(n,m)\in\mathbb N^2$, ask about
$$
 C_{d,p}(n,m)
 =\#\bigl(\operatorname{Fix}(P_d^n)\cap
             \operatorname{Fix}(\operatorname{Fr}_p^m)\bigr).
$$
These are actual common returns, not arbitrary weights on old orbits.

**Exact classical reduction.** The second fixed set is the cyclic
group $\mathbb F_{p^m}^{\times}$ of order $p^m-1$. Its elements whose
$(d^n-1)$-st power is one number exactly
$$C_{d,p}(n,m)=\gcd(d^n-1,p^m-1).$$
This group-theoretic identity is not a proposed research result.

**Potential question and decisive obstruction.** When $d$ and $p$ are
multiplicatively independent, one could seek a uniform effective
bound on diagonal common returns. However, the qualitative estimate
$\log\gcd(d^n-1,p^n-1)=o(n)$ is already the classical
Bugeaud–Corvaja–Zannier theorem. Its standard subspace-theorem proof
does not provide the desired effective bound merely from the count
identity. No new effective Diophantine input or complete strengthened
theorem was found, so the candidate is not admitted.

**Sources actually inspected.** The original BCZ publisher paper was
not obtained and is not falsely listed as fully read. The theorem and
its ineffectivity are recorded in Joseph Silverman's original research
article, *Common divisors of $a^n-1$ and $b^n-1$ over function fields*,
[*New York J. Math.* 10 (2004), 37–43](https://nyjm.albany.edu/j/2004/10-2.pdf),
introduction and equation (1); its different function-field conclusion
was also checked. Barroero–Capuano–Turchet,
*Greatest common divisor results on semiabelian varieties and a
conjecture of Silverman*, *Research in Number Theory* 10 (2024), Article 17,
[DOI 10.1007/s40993-023-00494-2](https://doi.org/10.1007/s40993-023-00494-2),
introduction and equation (1.1), independently state the classical
owner while studying a broader geometric setting. These are primary
research sources, but not substitutes for claiming a full read of BCZ.

## D. Polynomial minimal components over the $p$-adic integers

**Object and question.** For a degree-at-least-two polynomial
$f\in\mathbb Z_p[x]$, use the actual integer iterates on
$\mathbb Z_p$ and the compatible finite quotients
$\mathbb Z/p^k\mathbb Z$. Ask for all periodic cycles, minimal clopen
components, their odometer type and attracting basins. The most
tempting explicit test was $f(x)=x^2+x$ on $\mathbb Z_2$.

**Primary owner.** Fan–Liao,
*On minimal decomposition of $p$-adic polynomial dynamical systems*,
[original arXiv:1010.5583v2](https://arxiv.org/pdf/1010.5583v2),
29 October 2010, 27 pages;
*Advances in Mathematics* 228(4) (2011), 2116–2144,
[publisher record](https://www.sciencedirect.com/science/article/pii/S0001870811002234),
DOI 10.1016/j.aim.2011.06.032.

The original introduction, Theorems A–F, and the cycle-lifting setup
through the first recurrence propositions were actually read.
Theorems A and C already give the general decomposition and odometer
form; Theorem E gives the explicit $x^2+x$ decomposition. Therefore
that test and the general structural formulation cannot be presented
as new. This is a statement-level ownership exclusion, not a claim to
have independently reproved all 27 pages of the source.

**Internal collision.** The C394–C398 batch report already covers the
analytic $p$-adic interpolation direction, with C394's classical
Poonen input. Replacing scalar dynamics by a near-identity polynomial
or repeating the usual lift analysis does not by itself clear that
collision. A future higher-dimensional/nonclassical problem would
need genuinely new data and a different full theorem. No such theorem
is asserted here.

## E. Infinite-$S$ arithmetic solenoids with sparse activation orders

**Object and question.** Let $S$ be an infinite set of odd primes and
let $T$ be the endomorphism dual to multiplication by $2$ on
$\mathbb Z[S^{-1}]$. Its ordinary fixed-count sequence is
$$
 f_n=(2^n-1)\prod_{p\in S}|2^n-1|_p,
$$
where each product at a fixed $n$ is finite. Unlike candidate A, this
is not finite adelic distortion. One possible sparsity hypothesis is
$\sum_{p\in S}1/\operatorname{ord}_p(2)<\infty$; the question would be
whether an appropriate rationality/natural-boundary classification
holds for the native zeta function throughout that class.

**Classical owner and limit of the comparison.** Bell–Miles–Ward,
*Towards a Pólya–Carlson dichotomy for algebraic dynamics*,
[*Indag. Math.* 25 (2014), 652–668, original manuscript](https://shura.shu.ac.uk/17223/1/Miles-TowardsaPoly-CarlsonDichotomy%28AM%29.pdf),
Theorem 13 gives a thin-*complement* result for one-solenoids, with a
specific growth condition on the omitted primes. It is not the same
as sparsity of $S$ by activation order. The count formula and existing
theorem are deducted; no assertion that all infinite-place boundary
questions remain open is made.

**Cheap feasibility check.** The finite-$S$ Wiener estimate used in
candidate A grows with the number of primes. A newly added individual
factor is not uniformly close to one merely because its activation
order is large: at a multiple of that order it can differ by at least
$1-1/p$. Thus the order-summability hypothesis does not justify the
required uniform or Fourier-norm product convergence. This statement
is about the factor, not an unproved lower bound for the difference
of the full products. A different argument is needed to pass to
infinitely many primes and prevent cancellation.

No complete proof or counterexample for this proposed full class was
obtained. The question is a reserve, not an admitted result and not a
second natural-boundary manuscript carved out of candidate A.

## Local collision scope and handoff

The local screen inspected the relevant C389–C398 reports, the C404–C408
scouting material and the C14 $S$-integer chronology report, together
with targeted registry/file searches. This is a bounded collision
screen, not a claim that every repository file was read. In particular:

- C14's chronology/Parikh-fibre obstruction is not the full wild FAD
  boundary theorem, but its single-system classical boundary inputs
  must be deducted.
- C397 already uses Salem/nonexpansive dynamics and studies its native
  orbit statistics. The Salem factor in the new wild product is a
  classical test, not a claim to a new Salem construction.
- C407 owns the previous orbit-limit-image topological theorem. Its
  measure, covering, perfectness or small-parameter consequences are
  not proposed as separate candidates here.

All changes for this scout are confined to `arithmetic/`. No frozen
round2/round3 file, C-paper, TeX/PDF, formal evaluation, shared registry,
Git state, or external collaboration channel was changed by this
scout. The next decision is nonauthor theorem/source admission of A,
plus exploration of a genuinely independent question if the batch
still lacks five qualified contracts.

## Follow-up: complete two-clock classification

After the initial five-way screen, a different common-return question
was developed for all circle multiplication maps $T_a,T_b$, with
$a,b\geq2$ and two independent clocks. This does not rehabilitate the
discarded one-clock/diagonal candidate above. The full ordinary
two-variable function is classified by its exact open convergence
domain, dependent-branch polar divisor and joint meromorphic
natural boundary. The dependent and independent branches form one
theorem, not two contracts.

The complete proof, bounded nearest-owner audit and small exact
checks are now in:

- `RECTANGULAR_RETURN_PROOF.md`;
- `RECTANGULAR_SOURCE_AUDIT.md`;
- `rectangular_exact_checks.py` and `RECTANGULAR_EXACT_CHECK_REPORT.md`.

The source audit explicitly deducts Ward's original rectangular
return example and earlier volume-weighted rectangular zeta,
Miles's Lind/synchronization generating functions, the general
Corvaja–Zannier input, the 2026 diagonal recurrence result, and
classical Hartogs tools. It does not claim source completeness.
In particular, $a=b=2$ has a rational diagonal but genuine infinitely
many two-variable polar components, so diagonal nonrationality is
not the proposed theorem.

The nonauthor coordinator's `../REVIEW_RECTANGULAR_ROOT.md` records
its independent mathematical and substantive decision: retain one
research-ready candidate, with no C-number or manuscript/PDF yet.
This author-side file does not replace that admission decision.
The exact script passed 784 explicit circle-kernel intersections and
24,624 dependent-ray coefficient checks; no infinite analytic claim
is certified by those samples.
