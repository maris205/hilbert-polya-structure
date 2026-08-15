# Novelty Audit

Audit date: 2026-08-14.

Search cutoff: 2026-08-14.  Scope: primary papers and official metadata;
exact-phrase and concept searches combined primitive divisors,
Lehmer--Pierce sequences, toral automorphisms, cat maps, prime-order torsion,
exact periods, and the exception set.  No research dataset, prime table, or
Riemann-zero data was accessed.

Verdict: `GO_SCOPED_TECHNICAL_NOTE_LOW_NOVELTY`.

## Closest-result map

1. Anthony Flatters, *Primitive Divisors of Some Lehmer--Pierce
   Sequences*, Journal of Number Theory 129 (2009), 209--219,
   DOI `10.1016/j.jnt.2008.05.008`, arXiv:`0708.2190`.  For a positive
   norm-one quadratic unit, Theorem 1.4 gives a primitive rational prime
   divisor in every term beyond twelve.  For
   \((3+\sqrt5)/2\), Theorem 3.1 and its proof table give the exact small
   terms and the nontrivial primitive-divisor exceptions
   \(\{6,10,12\}\); \(\Delta_1=-1\) trivially has none.  This is the direct
   arithmetic engine, not a new result of Paper 8.
2. Gregory Gaspari, *The Arnold Cat Map on Prime Lattices*, Physica D 73
   (1994), 352--372, DOI `10.1016/0167-2789(94)90105-8`.  For every prime
   lattice other than the ramified \(p=5\) case, it determines the common
   nonzero orbit period and orbit decomposition.  This is the closest
   collision: standard-cat dynamics over prime lattices is classical.
3. Ian C. Percival and Franco Vivaldi, *Arithmetical Properties of Strongly
   Chaotic Motions*, Physica D 25 (1987), 105--130,
   DOI `10.1016/0167-2789(87)90096-0`, classify generalized cat-map periodic
   orbits using modular arithmetic and ideal theory in quadratic fields.
4. Freeman J. Dyson and Harold Falk, *Period of a Discrete Cat Mapping*,
   American Mathematical Monthly 99 (1992), 603--614,
   DOI `10.2307/2324989`, and Peter Seibt, *A Period Formula for Torus
   Automorphisms*, DCDS 9 (2003), 1029--1048,
   DOI `10.3934/dcds.2003.9.1029`, study global matrix orders on rational
   lattices.  They occupy much of the finite-ring period background, but are
   not the cross-prime prescribed-period statement frozen here.
5. Michael Baake, John A. G. Roberts, and Alfred Weiss, *Periodic Orbits of
   Linear Endomorphisms on the 2-Torus and Its Lattices*, Nonlinearity 21
   (2008), 2427--2446, DOI `10.1088/0951-7715/21/10/012`,
   arXiv:`0808.3489`, develop global/local orbit counts, local zeta functions,
   and rational lattices.  The extension by Baake, Neumaerker, and Roberts,
   DCDS 33 (2013), 527--553, DOI `10.3934/dcds.2013.33.527`,
   arXiv:`1205.1003`, is also nearby.
6. V. Kannan, I. Subramania Pillai, K. Ali Akbar, and B. Sankararao,
   *The Set of Periods of Periodic Points of a Toral Automorphism*, Topology
   Proceedings 37 (2011), 219--232, prove that an ordinary hyperbolic
   two-torus period set is \(\mathbb N\) or \(\mathbb N\setminus\{2\}\).
   This concerns existence of periodic points without fixing their additive
   order.  Llibre and Neumaerker, Topology and its Applications 185--186
   (2015), 41--49, DOI `10.1016/j.topol.2015.02.003`, give broader period-set
   classifications.
7. Kai Tan and Chengqing Li, *The Graph Structure of a Class of Permutation
   Maps over Ring \(\mathbb Z_{p^k}\)*, arXiv:`2506.20118` (2025), develop
   exact cycle-length distributions and lifting for a class containing cat
   matrices.  This is a strong current collision for fixed-prime and
   prime-power cycle structure, but no cross-prime Flatters corollary was
   located.
8. Aryaman Chandra, *Arithmetic Landscape Functions of a Discrete Cat Map*,
   arXiv:`2607.24857` (2026), gives transparent Green-function, trace, and
   permutation-spectrum identities that record the orbit-length multiset.
   Thus a novelty claim for a spectral landscape whose value is merely the
   cat-map period is unavailable.  Paper 8 will not rely on the manuscript's
   separate displayed gap factorization, whose statement is inconsistent
   with its accompanying algebra.
9. Hannay and Berry, *Quantization of Linear Maps on a Torus*, Physica D 1
   (1980), 267--290, DOI `10.1016/0167-2789(80)90026-3`, and Kurlberg and
   Rudnick, *Hecke Theory and Equidistribution for the Quantization of Linear
   Maps of the Torus*, Duke Mathematical Journal 103 (2000), 47--77,
   DOI `10.1215/S0012-7094-00-10314-6`, arXiv:`chao-dyn/9901031`, establish
   the proper quantum-cat context.  They do not turn the classical
   torsion-order label into a new quantum operator theorem.

## Collision assessment

No primary source was located that explicitly states either of the following
packaged conclusions:

- every hyperbolic \(M\in\mathrm{SL}_2(\mathbb Z)\) has a prime-order
  exact-period torsion point for every \(n>12\); or
- the standard cat has a prime-order exact-period torsion point exactly for
  \(n\notin\{1,6,12\}\).

This bounded search result is not a proof of absence.  The positive-trace
half of the first statement is an immediate one-paragraph Flatters corollary;
negative trace adds a short but necessary three-case parity reduction through
\(-M\).  The second statement assembles Flatters' table, classical
prime-lattice dynamics, the ramified modulo-five Jordan repair at period ten,
and complete small-prime exclusions.

The torsion-order clock itself has almost no novelty: all torus torsion is
periodic, every additive order occurs, and the label is invariant but
unbounded and discontinuous on a dense set.  The useful contribution is the
explicit capacity-versus-specificity audit, not the definition of the clock.

## Novelty scores

| Component | Score | Reason |
|---|---:|---|
| Uniform \(n>12\) carrier theorem | 3/10 | Flatters plus elementary kernel and negative-trace parity lemmas. |
| Exact standard-cat classification | 4/10 | Exact packaging was not located, but all ingredients are classical or elementary. |
| Torsion-order clock | 1--2/10 | Natural global label; structurally non-specific and nonregular. |
| Combined technical note | 4/10 | A useful sharp audit, not a major new theorem. |

## Safe positioning

Frozen safe title:

**A Primitive-Divisor Audit of Prime-Order Torsion Periods for Hyperbolic
Toral Automorphisms**.

Use “derive,” “record,” “audit,” and “synthesis.”  Do not use “first,”
“discover,” “prime-generating cat map,” “prime-orbit correspondence,”
“Riemann dynamics,” or “natural quantization of the order clock.”  Present
the standard-cat exception set as an exact synthesis and the clock result as
an obstruction.  Any later bibliography must cite Flatters and the
prime-lattice literature prominently and keep classical torsion, aggregate
periodic-point counts, spectral landscape identities, and quantum cat maps
logically separate.
