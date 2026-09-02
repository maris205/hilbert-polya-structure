# Owner-search log — root cross-class lane

**Search date:** 2026-09-02. **External state:** HOLD_EXTERNAL.

The search is claim-subtractive, not novelty-certifying. A source gets full
credit for every literal rule, standard lemma, algorithmic interpretation,
or generic proof engine that it controls. Search non-hits only bound this
intake pass.

## NHI — Newton--Hensel idempotent lift modulo powers of two

### Literal queries

    Newton iteration idempotents x^2(3-2x) modulo 2^n dynamics
    polynomial 3x^2-2x^3 iteration modulo powers of 2 fixed points
    "3x^2-2x^3" Newton idempotent ring
    "x^2(3-2x)" idempotent lifting
    idempotent lifting Newton polynomial 3x^2 - 2x^3
    iterate polynomial smoothstep modulo 2^n dynamics
    site:doi.org idempotents lifting polynomial 3x^2-2x^3 nil ideal
    site:ams.org "3x^2-2x^3" idempotent
    "Newton's method" lifting idempotents rings polynomial
    "G_1(x)=3x^2-2x^3"

### Direct owners and deductions

- Burban and Drozd, *Derived categories of nodal algebras*, J. Algebra 272
  (2004), Appendix A, gives the polynomial
  $G_1(x)=3x^2-2x^3$ as an idempotent-lifting polynomial and states its
  improvement of an approximate idempotent modulo successive ideal powers:
  <https://doi.org/10.1016/j.jalgebra.2003.07.025>.
- The general Newton/Hensel interpretation and quadratic improvement are
  therefore owned input. Generic idempotent lifting, convergence in a
  nilpotent ideal, and the bare logarithmic number of lifting rounds receive
  zero contribution credit.
- The same cubic is the classical first smoothstep polynomial; that name and
  its real-variable interpolation properties are irrelevant to the residual
  arithmetic claims and receive zero credit.

### Residual after subtraction

The bounded search found no source treating this cubic as the complete
self-map of every residue class modulo $2^n$, nor the conjunction of:

1. the parity-resolved pointwise entry law and exact temporal polynomial;
2. the complete one-step image as valuation strata with normalized unit
   congruent to $7\pmod8$ on the first stratum and $3\pmod8$ thereafter;
3. every-target fibre sizes, including the boundary truncations near zero
   and their reflected copies near one.

Those are the only proposed contribution axes. The literal polynomial and
its convergence principle are explicitly not proposed as new.

## ASD — Artin--Schreier difference

### Literal queries

    Artin-Schreier map x^q - x iteration finite field normal basis nilpotent
    functional graph x^p-x finite fields iteration Artin Schreier
    "(Frobenius - 1)" nilpotent finite field extension degree p power
    kernel iterates Artin Schreier operator finite fields (sigma-1)^k
    Jordan form Frobenius automorphism finite fields normal basis characteristic p
    modular normal basis Frobenius Jordan block cyclic p extension

### Owners and internal subtraction

- Standard Artin--Schreier theory owns $\wp(x)=x^p-x$, its
  $\mathbb F_p$-linearity, kernel, and one-step trace-zero image; see the
  Stacks Project, Tag 09I7: <https://stacks.math.columbia.edu/tag/09I7>.
- The normal basis theorem owns the conjugacy of $q$-Frobenius to a cyclic
  coordinate shift. Standard modular representation/rational-canonical
  theory owns the Jordan/Fitting analysis of shift minus identity.
- Internally, P115 already packages a finite-field linear operator into
  exact core, depth layers, uniform fibres, fixed iterates, cycles, and zeta.
  The ASD formulas are clean, but their main theorem conjunction and proof
  engine transfer almost verbatim from that occupied silhouette.

**Verdict:** DOWNRANK_INTERNAL_COLLISION. Retain as a verified reserve; do
not assign one of P157--P161 without a genuinely nonlinear second axis.

## CMD — simultaneous center deletion on paths

### Queries and owners

    parallel centroid decomposition path graph delete centroids rounds
    centroid decomposition path synchronous center deletion graph
    site:arxiv.org centroid decomposition tree algorithm path graph
    Jordan tree centroid decomposition 1869 centroid tree graph
    recursive centroid decomposition path graph depth

Jordan's centroid theorem and the standard recursive centroid-decomposition
algorithm own the centroid-removal primitive and the generic logarithmic
depth bound. A modern nearby primary paper on centroid trees is Berendsohn,
Golinsky, Kaplan, and Kozma, *Fast approximation of search trees on trees
with centroid trees*: <https://arxiv.org/abs/2209.08024>.

The exact path formulas in the pilot — equal descendants, survivor profile,
and bounded-composition census for starting linear forests — were not
located literally. Nevertheless the binary split engine is too close to
P126 balanced composition refinement and the deletion clock too close to
P114 forest peeling. It remains RESERVE_COLLISION, not a frozen paper.

## DGD — derivative--gcd multiplicity descent

### Queries and subtraction

    polynomial squarefree decomposition repeated gcd f derivative multiplicities
    Yun square-free factorization gcd f f' repeated

Yun's square-free factorization and later polynomial-factorization accounts
own the fact that $\gcd(f,f')$ lowers each positive irreducible multiplicity
by one in characteristic zero (or characteristic exceeding the degree), as
well as the repeated-gcd extraction of multiplicity layers. See Musser's
survey, *Factorization of polynomials*:
<https://users.cs.duke.edu/~elk27/bibliography/82/Ka82_survey.pdf>, and the
formal verification account of Berthomieu et al.:
<https://pmc.ncbi.nlm.nih.gov/articles/PMC7115093/>.

The proposed clock is consequently algorithmic repackaging, while the
enumeration would reuse P128's irreducible-orbit Euler-product machinery.
Verdict: KILL_DIRECT_OWNER_AND_INTERNAL_ENGINE.

## Search ceiling

The NHI query family was pursued through exact-polynomial, idempotent-lift,
Newton/Hensel, modular-iteration, and smoothstep terminology. ASD was
searched through Artin--Schreier, Frobenius-minus-identity, normal-basis, and
Jordan terminology. CMD was searched through centroid, center removal,
parallel recursion, and paths. DGD was stopped once the repeated-gcd
square-free algorithm controlled its literal multiplicity evolution. No
claim beyond this bounded ceiling is licensed.
