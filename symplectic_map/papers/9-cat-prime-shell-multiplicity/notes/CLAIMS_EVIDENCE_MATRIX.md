# Claims--Evidence Matrix

## Scope key

- Candidate: `cat_prime_shell_multiplicity_obstruction_v1`.
- Status vocabulary:
  - `PROVED`: established in `PROOF_PACKAGE.md`;
  - `CLASSICAL_REDERIVATION`: proved locally but strongly covered by prior
    literature;
  - `FORMAL_IDENTITY`: exact algebra, not an empirical finding;
  - `AUDIT_CONTROL_ONLY`: a later fixed exact reproduction can falsify an
    implementation but cannot prove the general statement;
  - `OUTSIDE_SCOPE`: a live escape or adjacent theory not closed by Paper 9.

## Claim ledger

| ID | Frozen claim | Proof or evidence required | Closest primary literature | Later exact control | Status and permitted wording |
|---|---|---|---|---|---|
| C1 | For odd $p\ne5$, all nonzero $p$-torsion points have one common exact period; split shells have $m_p=(p+1)h_p$, inert shells have $m_p=(p-1)h_p$ | diagonalization over $\mathbb F_p$ or multiplication by the norm-one root in $\mathbb F_{p^2}$ | Gaspari (1994) is a direct collision; Baake--Neumärker--Roberts (2013), Appendix A.1, gives prime/prime-power cycle-generating formulas | fixed profiles at $p=3,7,11$ | `CLASSICAL_REDERIVATION`; say “record” or “re-derive,” not “discover” |
| C2 | $p=2$ has one three-cycle; $p=5$ has two two-cycles and two ten-cycles; hence $p=2$ is the unique $m_p=1$ shell and $m_p\ge p-1$ for every odd prime | Cayley--Hamilton modulo two; $A=-I+N$, $N^2=0$, $\operatorname{rank}N=1$ modulo five; combine with C1 | Baake--Neumärker--Roberts (2013), Appendix A.1, directly covers these cycle boundaries; Gaspari (1994) is near-direct prior art | fixed profiles at $p=2,5$ | `CLASSICAL_REDERIVATION`; the uniform lower-bound packaging is safe but low novelty |
| C3 | The point-potential/raw-return factor is $\prod_\gamma(1-p^{-s|\gamma|})^{-1}$, with a mixed length-two/length-ten factor at $p=5$ | fixed-point exponential grouped by primitive orbit and repeat | Artin--Mazur (1965); Ruelle (1976); Parry--Pollicott (1990); Baake--Roberts--Weiss (2008) for finite/rational-lattice Euler products; Chandra (2026) for a finite-permutation determinant/cycle product | reproduce all five frozen raw factors symbolically | `FORMAL_IDENTITY`; never call this construction a new zeta function |
| C4 | The distinct orbit-label factor is $(1-p^{-s})^{-m_p}$ and its logarithmic coefficient at repeat $r$ is $m_p/r$ | direct logarithmic expansion after assigning the label once per primitive orbit | standard primitive-orbit Euler-product ledger; finite-permutation cycle products are classical | fixed $m_p$ and symbolic repeats $r=1,2,3$ as controls | `FORMAL_IDENTITY`; its distinction from C3 is the scoped audit's main semantic contribution |
| C5 | For odd $p$, fixed nonzero scalar coefficients independent of $z$ cannot turn $\prod_\gamma(1-w_\gamma z)^{-1}$ into $(1-z)^{-1}$; allowing zeros leaves exactly $\{1,0,\ldots,0\}$ | clear denominators and compare polynomial degree; optionally cross-check all power sums | standard weighted-zeta formalism in Ruelle (1976) and Parry--Pollicott (1990); the finite degree argument itself is elementary | symbolic denominator-degree and $w=1/m_p$ repeat controls | `PROVED`, but only for pure scalar denominator factors; no matrix/Fredholm/cohomological extrapolation |
| C6 | Equal weight $w_\gamma=1/m_p$ fixes only the first coefficient and gives $m_p^{1-r}$ at repeat $r$ | power-sum calculation | elementary | frozen $p=3,5,7,11$ and formal $r=2,3$ | `FORMAL_IDENTITY`; do not call it a failed Hölder-potential theorem beyond the frozen scalar product |
| C7 | Fractional exponent $|\gamma|/(p^2-1)$ gives exactly one factor, but this is shell-global normalized counting and works for composite exact-order shells with denominator $J_2(q)$ | cycles partition a finite shell; exact-order shell cardinality is the Jordan totient | finite-permutation orbit counting; Baake--Roberts--Weiss (2008) and Baake--Neumärker--Roberts (2013) are close structural context | frozen prime weights, plus one symbolic composite-shell identity only; no composite scan | `FORMAL_IDENTITY`; required conclusion is `A0_FAIL_GLOBAL_NORMALIZATION_ONLY`, not impossibility of normalization |
| C8 | The global label logarithm diverges for real $1<s\le2$, is not absolutely convergent for complex $1<\Re s\le2$, and is absolutely convergent for $\Re s>3$ | lower bound $m_p\ge p-1$, upper bound $m_p\le p^2-1$, and Euler's divergence of $\sum_p1/p$ | classical Euler-product analysis | none; no numerical evaluation of $s$ or logarithms is permitted | `PROVED_SAFE_BOUNDS`; no claim for $2<\Re s\le3$, exact abscissa, continuation, or zeros |
| C9 | Choosing one orbit per shell makes one factor but adds a selector and discards all other cycles; Paper 9 supplies no canonical selector | definition and orbit count | symmetry and centralizer analysis in Baake--Neumärker--Roberts (2013) | record selector cardinality only | `PROVED_CONSTRUCTION_COST`; not a proof that an enriched selector is impossible |
| X1 | A centralizer quotient might compress shell multiplicity | not investigated here; inert, split, and ramified shells have nontrivial centralizer strata/actions | Baake--Neumärker--Roberts (2013) | none | `OUTSIDE_SCOPE`; a real Paper-10 escape, not a Paper-9 negative claim |
| X2 | Matrix-valued, numerator-bearing, alternating, transfer/Fredholm, or cohomological products might cancel multiplicity | requires a different theorem and construction | Ruelle (1976); Parry--Pollicott (1990); Chandra (2026) | none | `OUTSIDE_SCOPE`; explicitly not excluded by C5 |

## Source-to-claim metadata lock

| Key | Primary record | Exact use in Paper 9 | Not used to claim |
|---|---|---|---|
| Gaspari1994 | Gregory Gaspari, “The Arnold cat map on prime lattices,” *Physica D* 73(4), 352--372, DOI `10.1016/0167-2789(94)90105-8` | direct novelty collision for common prime-lattice period and orbit decomposition | historical priority for Paper 9 |
| PercivalVivaldi1987 | Ian Percival and Franco Vivaldi, “Arithmetical properties of strongly chaotic motions,” *Physica D* 25, 105--130, DOI `10.1016/0167-2789(87)90096-0` | arithmetic cat-map context | the Paper-9 product formulas |
| DysonFalk1992 | Freeman J. Dyson and Harold Falk, “Period of a Discrete Cat Mapping,” *American Mathematical Monthly* 99(7), 603--614, DOI `10.1080/00029890.1992.11995900` | discrete-period context | scalar-weight obstruction |
| BaakeRobertsWeiss2008 | Michael Baake, John A. G. Roberts, and Alfred Weiss, “Periodic orbits of linear endomorphisms on the 2-torus and its lattices,” *Nonlinearity* 21, 2427--2446, DOI `10.1088/0951-7715/21/10/012` | rational-lattice cycle counts and finite-lattice Euler-product collision | a new global/local toral zeta theory |
| BaakeNeumaerkerRoberts2013 | Michael Baake, Natascha Neumärker, and John A. G. Roberts, “Orbit structure and (reversing) symmetries of toral endomorphisms on rational lattices,” *DCDS* 33(2), 527--553, DOI `10.3934/dcds.2013.33.527` | Appendix A.1 cycle-generating-polynomial collision; centralizer/symmetry context | absence of quotient escapes |
| ArtinMazur1965 | Michael Artin and Barry Mazur, “On periodic points,” *Annals of Mathematics* 81(1), 82--99, DOI `10.2307/1970384` | classical fixed-point exponential | novelty of C3 |
| Ruelle1976 | David Ruelle, “Zeta-functions for expanding maps and Anosov flows,” *Inventiones Mathematicae* 34, 231--242, DOI `10.1007/BF01403069` | weighted product and operator-theoretic boundary | a new transfer theorem |
| ParryPollicott1990 | William Parry and Mark Pollicott, *Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics*, Astérisque 187--188, DOI `10.24033/ast.28` | primitive/repetition and Hölder-weight formalism | excluding Fredholm/cohomological cancellation |
| BaakeLauPaskunas2010 | Michael Baake, Eike Lau, and Vytautas Paskunas, “A note on the dynamical zeta function of general toral endomorphisms,” *Monatshefte für Mathematik* 161, 33--42, DOI `10.1007/s00605-009-0118-y` | ordinary toral zeta boundary | identifying $Z_{\mathrm{lab}}$ with the cat map's ordinary zeta function |
| TanLi2025 | Kai Tan and Chengqing Li, “The Graph Structure of a Class of Permutation Maps over Ring $\mathbb Z_{p^k}$,” arXiv:2506.20118 | contemporary exact prime-power cycle context | new finite-ring cycle analysis |
| Chandra2026 | Aryaman Chandra, “Arithmetic Landscape Functions of a Discrete Cat Map,” arXiv:2607.24857 | contemporary finite-permutation identity $\det(I-\alpha P)$ as a product over cycles | new determinant/Green-function packaging |

## Evidence hierarchy and stop conditions

1. The proof package is the only evidence for the all-prime and global
   statements.
2. Primary literature fixes attribution and lowers novelty; it is not a
   target dataset.
3. The inherited five-prime ledger is an implementation control and is
   development-seen.
4. A later registered audit must stop on any disagreement.  It may not add
   primes, alter the matrix or product semantics, evaluate numerical $s$ or
   logarithms, or repair a theorem after seeing output.
5. A passing audit cannot open Route B, a prime/zero study, a centralizer
   quotient, or any transfer/quantization claim.

## Terminal evidence decision

If and only if the source-lock proof passes independent review and a later
separately authorized fixed audit reproduces its controls, the permitted
terminal wording is:

`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

The research-level positioning remains
`GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY` regardless of a passing audit.
