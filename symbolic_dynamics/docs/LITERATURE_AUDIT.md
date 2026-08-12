# Literature Audit: Symbolic Dynamics and Arithmetic Determinants

Search date: 2026-08-12  
Primary family: symbolic dynamics only

The search was organized around four obligations: a natural arithmetic
grammar, a primitive/repetition ledger, an analytic determinant, and a
non-post-hoc phase mechanism.  The table records what each source actually
supports; proximity to zeta notation is not treated as evidence for the
Riemann divisor.

## Source-to-claim map

| Topic | Primary source | Claim supported here |
|---|---|---|
| Periodic-point zeta | Artin–Mazur, 1965, [DOI](https://doi.org/10.2307/1970384) | Definition and analytic questions for dynamical zeta functions |
| Finite shifts | Bowen–Lanford, 1970, [paper](https://people.math.harvard.edu/~knill/history/lanford/papers/BowenLanford.pdf) | Finite-state determinant/Euler-product identity |
| Sofic shifts | Béal, [Numdam record](https://www.numdam.org/item/ITA_1993__27_4_321_0/) | Rationality of the unweighted sofic zeta |
| Transfer determinants | Ruelle, 1976, [DOI](https://doi.org/10.1007/BF01403069) | Zeta/transfer-operator framework beyond finite matrices |
| Hölder boundary | Pollicott, 1986, [DOI](https://doi.org/10.1007/BF01388795) | Finite alphabet does not imply a finite-dimensional determinant for general Hölder data |
| Suspensions and twists | Parry–Pollicott, 1990, [Numdam book](https://www.numdam.org/item/AST_1990__187-188__1_0/) | Weighted zeta functions, suspensions, and group extensions |
| Countable shifts | Gurevich, 1969, [MathNet](https://www.mathnet.ru/eng/dan34469) | Entropy framework for countable Markov chains |
| Countable zeta | Gurevich–Savchenko, 1998, [DOI](https://doi.org/10.1070/RM1998v053n02ABEH000017) | Zeta questions for symbolic systems of infinite type |
| Countable thermodynamics | Sarig, 1999, [DOI](https://doi.org/10.1017/S0143385799146820) | Thermodynamic formalism with countable Markov partitions |
| Renewal flexibility | Sarig, [official manuscript](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/zetarenewal.pdf) | A fixed renewal graph with complex weights can realize a broad class of analytic reciprocal zeta germs |
| Circular codes | Hong, 2011, [DOI](https://doi.org/10.1017/S0143385710000015) | Code-zeta bookkeeping and hypotheses needed for unique factorization |
| Countable coding | Amroun, 2004, [DOI](https://doi.org/10.1016/j.bulsci.2004.02.003) | Symbolic codings and zeta functions in a countable setting |
| Gauss operator | Mayer, 1990, [DOI](https://doi.org/10.1007/BF02473355) | Nuclear transfer operator for the Gauss map |
| Modular determinant | Mayer, 1991, [DOI](https://doi.org/10.1090/S0273-0979-1991-16023-4) | Signed Fredholm determinants and the modular Selberg zeta |
| Farey arithmetic model | Knauf, 1998, [DOI](https://doi.org/10.1007/s002200050441) and [official preprint](https://www.mis.mpg.de/publications/preprint-repository/article/1997/issue-15) | Binary recursion with unsigned limit \(\zeta(s-1)/\zeta(s)\); proposed Liouville refinement remains conditional |
| Knauf correction | Knauf, erratum, [DOI](https://doi.org/10.1007/s002200050715) | A correction exists and must accompany use of the 1998 article |
| Squarefree flow | Cellarosi–Sinai, 2013, [journal page](https://ems.press/journals/jems/articles/11437) | Natural squarefree symbolic system and its spectral structure |
| \(\mathscr B\)-free systems | El Abdalaoui–Lemańczyk–de la Rue, 2015, [DOI](https://doi.org/10.1093/imrn/rnu164) | Dynamical properties of \(\mathscr B\)-free subshifts |
| Graph Artin twists | Stark–Terras, 2000, [DOI](https://doi.org/10.1006/aima.2000.1917) | Finite graph coverings and Artin \(L\)-functions |
| Finite-group SFTs | Boyle–Schmieding, 2017, [DOI](https://doi.org/10.1017/etds.2015.87) | Group-ring and periodic-data formalism for finite group extensions |
| Farey/Gauss relation | Isola, 2002, [DOI](https://doi.org/10.1088/0951-7715/15/5/310) | Transfer-operator relation between Farey and Gauss maps |
| Unary context-free languages | Esparza–Ganty–Kiefer–Luttenberger, 2011, [DOI](https://doi.org/10.1016/j.ipl.2011.03.019) | Parikh images are semilinear; the unary specialization is ultimately periodic |

## Conclusions used in candidate design

### 1. Finite memory gives a clean ledger but the wrong divisor scale

For a finite graph with locally constant roofs, weights, and a
finite-dimensional twist, the determinant is a finite exponential polynomial.
The primitive/repetition expansion is exact, but the number of zeros in a
large disk is \(O(R)\).  This is incompatible with the
Riemann–von Mangoldt \(T\log T\) count for the completed Riemann function.

The scope qualifier is essential: a finite-alphabet shift with a genuinely
infinite-memory Hölder potential can have an infinite-dimensional transfer
operator.  It is not covered by the finite-memory theorem merely because its
alphabet is finite.

### 2. Countable renewal systems are flexible enough to prove too much

Renewal shifts escape finite-matrix rationality.  Sarig's construction also
shows that, once sufficiently free complex weights are admitted, a fixed
renewal graph can encode a very broad analytic target.  Exact target
reconstruction is therefore a non-identifiability warning, not arithmetic
evidence.  The same pipeline must reconstruct preregistered off-target
controls.

### 3. Gauss/Farey is the strongest natural analytic benchmark found

The continued-fraction grammar, derivative roof, and Mayer operator are
natural and mathematically rigid.  Its primitive periodic words correspond to
quadratic irrationals or hyperbolic modular conjugacy classes.  They are not
indexed by rational primes, and their repetitions do not supply the
\(\Lambda(p^r)\) ledger.  The signed determinants have a natural modular
meaning, but importing that geometry would leave this session's primary
family.

### 4. Knauf is the closest prior-art collision, not a solved candidate

Knauf's low-complexity binary recursion gives, in its proved half-plane, the
unsigned limit

\[
Z(s)=\frac{\zeta(s-1)}{\zeta(s)}.
\]

This is an exact arithmetic identity and therefore a stronger benchmark than a
finite zero fit.  However, its \(\zeta\)-zeros occur as poles of a quotient,
not as the divisor of a demonstrated periodic-orbit Fredholm determinant for
the same symbolic object.  The Liouville sign in the proposed refinement is an
extra number-theoretic observable.  The paper's convergence problem in the
critical half-plane is not closed; numerical convergence cannot substitute
for it.

### 5. Finite-group phases solve only a local positivity problem

A nontrivial character sector can cancel a Perron–Frobenius contribution.
The full skew product still contains the trivial representation, and every
finite-dimensional block remains a finite exponential polynomial.  Thus a
finite-group cocycle can provide an endogenous sign only when the symmetry is
pre-existing; it cannot raise the divisor count from \(O(T)\) to \(T\log T\).

## Literature gap

No source located in this audit supplies all of the following on one fixed,
low-description-complexity symbolic construction:

1. endogenous rational primes and the exact prime-power repetition ledger;
2. an intrinsic \(\log p\)-scale clock rather than a prime-labelled roof;
3. a canonical sign or unitary sector fixed before target inspection;
4. a nuclear determinant whose global divisor is the completed Riemann
   divisor;
5. a non-post-hoc interface to a self-adjoint realization.

That negative search result is an **OPEN literature gap**, not a theorem of
nonexistence.
