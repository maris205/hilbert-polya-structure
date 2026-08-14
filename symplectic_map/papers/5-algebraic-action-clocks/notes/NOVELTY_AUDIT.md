# Novelty Audit: Algebraic Exact Actions Cannot Be Prime Logarithms

**Search boundary:** literature, publisher records, Crossref, and preprints
checked through 2026-08-13  
**Candidate:** `algebraic_exact_action_clock_obstruction_v1`  
**Audit state:** completed before candidate execution

## Verdict

`PROCEED ONLY AS A NARROW DESIGN-CERTIFICATE NOTE; MERGE IF STANDALONE DEPTH IS REQUIRED`

The source-locked statement is exact and useful within this research
sequence: a closed action obtained by evaluating a normalized algebraic
exact potential on an algebraic periodic orbit is algebraic, while every
logarithm of a nontrivial algebraic number is transcendental.  Consequently
that action, its repetition, its algebraically scaled version, its real or
imaginary part, and its modulus cannot be an exact $\log p$ clock.

The mechanism is not deep.  It combines:

1. the standard generating-function/action formalism for exact symplectic
   maps;
2. elementary closure properties of algebraic numbers; and
3. the classical Hermite--Lindemann theorem.

The normalization audit is essential but also standard: generating functions
are defined up to constants, and a period-$n$ action shifts by $nC$.  I found
no checked source whose stated result is the precise algebraic-action versus
prime-logarithm certificate, nor the same certificate for the algebraic
area-preserving Hénon map.  That negative search supports only narrow
candidate novelty.  It does not support a historical priority claim because
the proof is short enough to be folklore-level.

Estimated novelty:

- algebraic evaluation of a rational potential on an algebraic orbit:
  **1/10**;
- Hermite--Lindemann exclusion of $\log p$: **1/10**;
- gauge and additive-normalization ledger: **2/10**;
- Hénon formula and $S$-integral denominator-$3$ refinement: **3/10**;
- complete all-period design certificate in the present arithmetic-clock
  sequence: **4/10**;
- overall standalone mathematical novelty: **3/10**.

## Proposed contribution

The defensible contribution is one transparent certificate chain:

1. freeze an algebraic exact potential, including its algebraic additive
   normalization, before orbit evaluation;
2. prove that every algebraic periodic orbit has algebraic closed action;
3. invoke Hermite--Lindemann to exclude exact logarithms of primes and all
   nontrivial algebraic numbers;
4. prove exactly how a single-valued algebraic gauge telescopes and how an
   additive constant contributes $nC$;
5. exhibit the identity-map constant-potential counterexample showing why a
   transcendental normalization defeats the claim;
6. specialize to
   $H_a(q,p)=(q^2-a-p,q)$ with explicit type-1 generating function and
   exact potential;
7. add the $S$-integral statement $3\mathcal A\in\overline{\mathcal O}_{K,S}$;
8. state the surviving loopholes, especially $\log|\mathcal A|$, multiplier
   logarithms, return times, and transcendental scales.

This is a **provenance filter for an exact prime-logarithm action clock**, not
a new theory of symplectic action spectra, transcendental numbers, or Hénon
dynamics.

## Core claims and collision assessment

| Claim | Novelty | Closest boundary | Safe positioning |
|---|---:|---|---|
| Periodic actions are sums of one-step generating functions. | None | Kook--Meiss (1989), MacKay--Meiss--Percival (1984), Meiss (1992) | Background only. |
| Exact symplectic maps admit potentials through $F^*\theta-\theta=dG$, with additive constant ambiguity. | None | Delshams--Ramírez-Ros (1997), especially §2.1 | Cite directly; do not present exactness or the ambiguity as new. |
| Algebraic potential values on algebraic points sum to an algebraic action. | Very low | Elementary algebraic geometry/field closure | Self-contained evaluation lemma, explicitly labelled elementary. |
| Such an action cannot equal any branch of $\log p$. | Very low | Hermite--Lindemann; Baker's transcendence text | Classical corollary applied as a design test. |
| Algebraic exact gauges telescope, while an algebraic constant shifts by $nC$ without leaving $\overline{\mathbb Q}$. | Low as packaging | Standard gauge/normalization behavior in exact and Hamiltonian action spectra | Make the distinction between value invariance and algebraicity invariance the methodological point. |
| Every finite periodic orbit of algebraic $H_a$ has algebraic action for $G=2q^3/3-pq$. | Low--medium as a case certificate | Classical Hénon geometry plus the elementary no-points-at-infinity proof | Candidate-specific exact specialization; no priority claim. |
| If $a$ is $S$-integral, then $3\mathcal A$ is $S$-integral. | Low | Good-reduction Hénon maximum arguments and elementary denominator tracking | Supporting arithmetic-provenance refinement only. |
| This rules out every symplectic realization of prime logarithms. | False | Return times, multiplier logs, logarithmic observables, and transcendental normalizations remain open | State this as an explicit nonclaim. |

## Closest prior work and exact boundaries

### Exact symplectic maps, generating functions, and periodic action

1. **Kook and Meiss, “Periodic orbits for reversible, symplectic mappings,”
   Physica D 35 (1989), 65--86.**
   [DOI 10.1016/0167-2789(89)90096-1](https://doi.org/10.1016/0167-2789(89)90096-1).
   It constructs symplectic twist maps from Lagrangian generating functions
   and studies periodic action minimizers and minimax orbits.  This is direct
   precedent for summing a one-step generating function along a periodic
   sequence.  It contains no arithmetic-algebraic or prime-logarithm
   obstruction.

2. **MacKay, Meiss, and Percival, “Transport in Hamiltonian systems,”
   Physica D 13 (1984), 55--81.**
   [DOI 10.1016/0167-2789(84)90270-7](https://doi.org/10.1016/0167-2789(84)90270-7).
   It relates flux through cantori to differences in action.  It establishes
   the central dynamical role of action differences, not arithmetic of
   absolute action values.

3. **Meiss, “Symplectic maps, variational principles, and transport,”
   Reviews of Modern Physics 64 (1992), 795--848.**
   [DOI 10.1103/RevModPhys.64.795](https://doi.org/10.1103/RevModPhys.64.795).
   This is the standard review for the discrete Lagrangian formulation of
   twist maps and periodic minimizing orbits.  It also treats the
   area-preserving Hénon map as a standard symplectic example.  It does not
   impose number-field coefficients or study logarithms of primes.

4. **Delshams and Ramírez-Ros, “Melnikov Potential for Exact Symplectic
   Maps,” Communications in Mathematical Physics 190 (1997), 213--245.**
   [DOI 10.1007/s002200050239](https://doi.org/10.1007/s002200050239).
   Section 2.1 defines an exact map by $F^*\phi-\phi=dS$ and states that map
   and submanifold generating functions are determined only up to an
   additive constant.  It also normalizes homoclinic actions by fixing the
   potential at a reference fixed point.  This is the closest direct source
   for the normalization warning and must be cited rather than rediscovered.

5. **Ginzburg and Gürel, “Action and index spectra and periodic orbits in
   Hamiltonian dynamics,” Geometry & Topology 13 (2009), 2745--2805.**
   [DOI 10.2140/gt.2009.13.2745](https://doi.org/10.2140/gt.2009.13.2745).
   It studies iteration behavior of Hamiltonian action and index spectra.
   Its setting and conclusions are much deeper but different: it does not
   assert that action values of algebraically defined discrete maps are
   algebraic.

6. **Mazzucchelli, “Symplectically degenerate maxima via generating
   functions,” Mathematische Zeitschrift 275 (2013), 715--739.**
   [DOI 10.1007/s00209-013-1157-6](https://doi.org/10.1007/s00209-013-1157-6).
   It identifies critical values of a discrete symplectic action with action
   values of periodic Hamiltonian orbits and discusses average-action
   spectra.  This is close formal precedent, but not an arithmetic value
   theorem.

7. **Bialy and Tsodikovich, “Locally maximising orbits for the non-standard
   generating function of convex billiards and applications,” Nonlinearity
   36 (2023), 2001--2019.**
   [DOI 10.1088/1361-6544/acbb50](https://doi.org/10.1088/1361-6544/acbb50).
   It uses the action functional $\sum H(q_j,q_{j+1})$ for an exact
   symplectic map.  This recent example confirms that the action-sum
   formalism remains standard; it has no prime-logarithm or algebraic-number
   claim.

### Hénon and polynomial symplectic background

8. **Friedland and Milnor, “Dynamical properties of plane polynomial
   automorphisms,” Ergodic Theory and Dynamical Systems 9 (1989), 67--99.**
   [DOI 10.1017/S014338570000482X](https://doi.org/10.1017/S014338570000482X).
   This is foundational polynomial-automorphism and generalized-Hénon
   background.  It supplies no action arithmetic.

9. **Moser, “On quadratic symplectic mappings,” Mathematische Zeitschrift
   216 (1994), 417--430.**
   [DOI 10.1007/BF02572331](https://doi.org/10.1007/BF02572331).
   It places Hénon's quadratic area-preserving map in the normal-form theory
   of quadratic symplectic mappings.  The present type-1 formula is a simple
   specialization, not a new Hénon construction.

10. **Bäcker and Meiss, “Moser's Quadratic, Symplectic Map,” Regular and
    Chaotic Dynamics 23 (2018), 654--664.**
    [DOI 10.1134/S1560354718060023](https://doi.org/10.1134/S1560354718060023).
    It revisits the higher-dimensional quadratic symplectic normal form and
    explicitly locates the two-dimensional area-preserving Hénon case.  It
    is geometric context rather than an arithmetic collision.

11. **Berger et al., “Hénon Maps: A List of Open Problems,” Arnold
    Mathematical Journal 10 (2024), 585--620.**
    [DOI 10.1007/s40598-024-00252-x](https://doi.org/10.1007/s40598-024-00252-x).
    Its number-field section records good-reduction and $S$-integral Hénon
    language.  This is the nearest current community context for the
    $S$-integral refinement, but it does not state an algebraic action versus
    logarithm theorem.

12. **Kim, Krieger, Postolache, and Szeto, “Hénon maps with many rational
    periodic points” (2024 preprint).**
    [arXiv:2412.01668](https://arxiv.org/abs/2412.01668).
    It constructs Hénon maps over $\mathbb Q$ with many integral periodic
    points and long integer cycles.  It shows that arithmetic periodic-point
    structure is active, but it studies abundance of points rather than
    generating-function action values.  This source remains a preprint in
    the present audit.

### Transcendence and the prime-period target

13. **Baker, _Transcendental Number Theory_, Cambridge Mathematical Library
    edition (2022; original edition 1975).**
    [DOI 10.1017/9781009229937](https://doi.org/10.1017/9781009229937).
    This is an authoritative source for Hermite--Lindemann and linear forms
    in logarithms.  The specific corollary used here is classical:
    $e^\alpha$ is transcendental for nonzero algebraic $\alpha$, so a
    nonzero logarithm of an algebraic number is transcendental.

14. **Berry and Keating, “The Riemann Zeros and Eigenvalue Asymptotics,”
    SIAM Review 41 (1999), 236--266.**
    [DOI 10.1137/S0036144598347497](https://doi.org/10.1137/S0036144598347497).
    It states that the hypothetical Riemann dynamics should have periodic
    orbit periods that are multiples of logarithms of primes.  This is the
    motivation for testing $\log p$ as an intrinsic clock, not prior work on
    algebraic Hénon actions.

## Source verification matrix

| Source | Original/authoritative record checked | Peer reviewed / book | Relevance | Status |
|---|---|---|---|---|
| Kook--Meiss 1989 | Elsevier DOI metadata and abstract | Yes | Direct periodic generating action | VERIFIED |
| MacKay--Meiss--Percival 1984 | Elsevier DOI metadata and abstract | Yes | Action differences and transport | VERIFIED |
| Meiss 1992 | APS DOI record and review abstract | Yes | Standard symplectic variational formalism | VERIFIED |
| Delshams--Ramírez-Ros 1997 | Original full PDF, pp. 214 and 219--220; Crossref DOI metadata | Yes | Exact potential and additive constant | VERIFIED AGAINST ORIGINAL |
| Ginzburg--Gürel 2009 | Publisher DOI and arXiv metadata | Yes | Action spectrum under iteration | VERIFIED |
| Mazzucchelli 2013 | Springer/Crossref DOI metadata and arXiv abstract | Yes | Discrete symplectic action | VERIFIED |
| Bialy--Tsodikovich 2023 | IOP DOI metadata and arXiv abstract | Yes | Recent generating-action formalism | VERIFIED |
| Friedland--Milnor 1989 | Cambridge DOI page and original-paper metadata | Yes | Polynomial Hénon background | VERIFIED |
| Moser 1994 | Springer/Crossref and EuDML metadata | Yes | Quadratic symplectic normal form | VERIFIED |
| Bäcker--Meiss 2018 | Crossref and arXiv metadata | Yes | Modern Hénon symplectic context | VERIFIED |
| Berger et al. 2024 | Springer DOI record | Yes | Current Hénon arithmetic vocabulary | VERIFIED |
| Kim et al. 2024 | arXiv abstract and identifier | Preprint | Arithmetic periodic-point context | VERIFIED PREPRINT |
| Baker 2022 | Cambridge book/DOI record | Book | Hermite--Lindemann | VERIFIED |
| Berry--Keating 1999 | SIAM DOI record and abstract | Yes | Prime logarithm period target | VERIFIED |

No predatory venue or retraction signal was found for the included sources.
No source was used solely because a secondary summary repeated its claim.
The 2024 Kim et al. item is explicitly kept at preprint status.

## What survives as the paper's delta

The defensible delta is not any ingredient in isolation.  It is the
pre-execution obstruction workflow:

1. start from a globally algebraic exact-symplectic map and an algebraic
   periodic action, rather than inventing an external roof;
2. freeze the additive normalization, which the standard literature shows
   is otherwise ambiguous;
3. turn algebraicity into an all-period exact exclusion of the desired
   logarithmic clock;
4. give an explicit target-injection counterexample for a transcendental
   constant;
5. instantiate every step on the inherited polynomial Hénon family;
6. retain the logarithmic-observable and return-time routes as explicit
   surviving alternatives instead of claiming a universal no-go result.

## Explicit nonclaims

- No novelty claim for exact symplectic potentials, generating functions,
  discrete variational actions, or additive constant ambiguity.
- No novelty claim for Hermite--Lindemann or for algebraic-number closure.
- No claim that Hénon periodic points or actions are newly defined.
- No claim that algebraic actions cannot equal rational primes.
- No obstruction to $\log|\mathcal A|$, $\log|\lambda|$, return times,
  energy derivatives, or transcendental normalizations.
- No claim about approximate $\log p$ scaling.
- No prime-orbit correspondence, prime density, dynamical zeta identity,
  Riemann-zero comparison, trace formula, or quantization.
- No historical-first claim for the elementary combined observation.

## Search strategy and negative-search boundary

**Databases and records:** web search, arXiv metadata, publisher pages,
Crossref DOI metadata, author/institutional full-text copies, and the existing
project literature corpus.  Searches were performed on 2026-08-13.

**Inclusion criteria:** primary papers/books on exact symplectic generating
functions and periodic action; action normalization; algebraic or arithmetic
Hénon dynamics; Hermite--Lindemann; and the prime-logarithm periodic-orbit
target.  Secondary pages were used only to locate primary records.

**Exclusion criteria:** uses of “action” meaning group action or map
application; dissipative Hénon time-series applications without symplectic
action; non-mathematical prime analogies; and sources whose existence or
metadata could not be verified.

Query families included at least three variants in each core group:

- `exact symplectic map periodic orbit action generating function`
- `generating function defined up to additive constant symplectic map`
- `action spectrum additive constant Hamiltonian periodic orbits`
- `algebraic periodic action symplectic map`
- `algebraic number action spectrum symplectic`
- `polynomial symplectic map periodic action algebraic`
- `area-preserving Hénon map generating function`
- `Hénon periodic action symplectic`
- `quadratic symplectic map Hénon generating function`
- `Hermite Lindemann logarithm algebraic number transcendental`
- `Lindemann symplectic action spectrum`
- `2024 2025 2026 exact symplectic action arithmetic`
- `2024 2025 2026 Hénon generating function action`

No checked title, abstract, or searched full-text passage stated the exact
candidate theorem.  The search is necessarily recall-limited: an elementary
observation may appear as an unindexed remark, exercise, or implicit
corollary.  Therefore the safe novelty statement is “no direct collision
located,” not “first proof.”

### Distributional coverage advisory

The included corpus is intentionally concentrated in theoretical
mathematics and mathematical physics because the claim is a theorem-level
design certificate.  Most sources are foundational rather than from the last
five years.  This temporal skew is retained deliberately: the necessary
formalism and transcendence theorem are classical.  Recent 2023--2026
queries were nevertheless run, and the 2023 action paper plus 2024 Hénon
survey/preprint were included to test currency.

## Final recommendation

Proceed only if the write-up leads with the normalization/provenance lesson
and presents the Hénon computation as a complete exact case study.  Merge it
with a broader obstruction synthesis if a standalone venue expects a deeper
new theorem.  Abandon any framing that calls the algebraic evaluation lemma,
Hermite--Lindemann, or the exact symplectic gauge formula new.
