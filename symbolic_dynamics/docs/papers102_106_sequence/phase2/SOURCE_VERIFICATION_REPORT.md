# Source verification report

Date of bounded audit: 2026-08-29 UTC.  Frozen status:
**INTERNAL AUDIT COMPLETE / EXTERNAL HOLD**.

This report reconciles the owner language in the current P102--P106
manuscripts, claims ledgers, and available cross-hostile reviews.  It records
search scope and known owners; it is not a novelty, priority, or freedom-to-
operate certificate.  `BOUNDED_NO_EXACT_PACKAGE_FOUND` means only that the
named conjunction was not located in the queries already run.

## P102 -- cyclic group-algebra involution norm

Known ownership explicitly subtracted:

- finite-group Fourier decomposition (Terras);
- canonical group-algebra involutions and the symmetric/unitary-unit setting,
  including Bovdi--Grishkov, DOI `10.1017/S0013091518000500`;
- scalar quadratic and power-map functional graphs, including
  Vasiga--Shallit, DOI `10.1016/S0012-365X(03)00158-4`, and
  Qureshi--Reis, DOI `10.1016/j.disc.2023.113393`; and
- Artin--Mazur periodic-point zeta bookkeeping.

The residual claim is restricted to the whole split group algebra, including
zero divisors, under `a -> a a*`: paired-character synchronization, the full
fixed/cycle census, sharp transient depth, and within-family recovery.  P86
shares an elementary adjacent-product primitive but studies a spatial
stochastic factor rather than this finite temporal map.  P97/P99/P87 are
lower-level squaring/depth, algebraic-census, or ring-multiplication motif
neighbors, not update-rule duplicates.  Status:
`BOUNDED_NO_EXACT_PACKAGE_FOUND`; specialist direct-owner review remains a
medium-high release gate because `a -> a a*` is canonical.

## P103 -- double adjugation

Known ownership explicitly subtracted: Jacobi/complementary-minor identities
and Lawrence's hyperadjugate extension, DOI `10.4153/CMB-1964-045-0`;
projective adjugation as a classical Cremona map (Dolgachev); standard
finite-field structure (Lidl--Niederreiter); and scalar power-map functional
graphs (Qureshi--Reis, DOI `10.1016/j.disc.2023.113393`).  The current
manuscript does not cite the previously scouted Kahle--Kubjas--Kummer--Rosen
paper, so that record is not represented as a manuscript owner here.

The residual claim is only the full-matrix temporal conjunction: singular
one-step collapse, iterate/fixed/image formulas, valuation stabilization,
cycles, and zeta.  P99 shares a valuation-staircase motif and P97 shares a
power/squaring primitive, but neither uses the full matrix phase space or
double-adjugate action.  Status: `BOUNDED_NO_EXACT_PACKAGE_FOUND`; the
classical identity receives zero novelty credit.

## P104 -- monomial-toggle contraction cocycle

Known ownership explicitly subtracted: Furstenberg--Kesten random-product
limit theory, DOI `10.1214/aoms/1177705909`; generalized-Lyapunov and tilted
transfer methods, including Texier, DOI `10.1007/s10955-020-02617-w`; and
Brown's martingale CLT, DOI `10.1214/aoms/1177693494`.

The residual claim is the exact specialization to the two atoms
`D=diag(a,1)` and `R=SD`: its finite-word normal form, folded singular-value
fluctuation, endpoint split, and closed annealed exponent.  P91 is the
declared medium internal motif risk; P93 and P101 have stochastic/two-state
motifs but different phase spaces, update rules, and observables.  Status:
`BOUNDED_NO_EXACT_PACKAGE_FOUND`; exact-atom direct-owner review remains a
release gate.

## P105 -- cycle-minimum pruning

Known ownership explicitly subtracted: labelled-cycle and exponential-formula
enumeration (Flajolet--Sedgewick and Stanley); the Shepp--Lloyd longest-cycle
law, DOI `10.1090/S0002-9947-1966-0195117-8`; adjacent deletion-consistent
combinatorial structures (Pitman); and Artin--Mazur zeta bookkeeping.

The residual claim is the deterministic simultaneous labelled surgery, its
complete transient census, and especially the threshold-matching one-step
fibre formula.  P100 is an absorbing finite system but uses arithmetic digit
erasure, not label-preserving parallel cycle surgery.  Status:
`BOUNDED_NO_EXACT_PACKAGE_FOUND`; no longest-cycle asymptotic is claimed.

## P106 -- synchronous MIS polarity

This paper has a **direct-system owner boundary**, not merely an analogous
graph-model boundary.  The current source correctly subtracts:

- Aracena--Demongeot--Goles, *Fixed Points and Maximal Independent Sets in
  AND--OR Networks* (2004), DOI
  `10.1016/S0166-218X(03)00461-X`;
- Aracena--Richard--Salinas, *Fixed Points in Conjunctive Networks and
  Maximal Independent Sets in Graph Contractions*, *Journal of Computer and
  System Sciences* 88 (2017), 145--163, DOI
  `10.1016/j.jcss.2017.03.016`;
- Gadouleau--Kutner, *Generalising the Maximum Independent Set Algorithm via
  Boolean Networks*, *Information and Computation* 303 (2025), 105266, DOI
  `10.1016/j.ic.2025.105266`, for the same MIS Boolean local rule and its
  fixed-point/sequential-schedule setting;
- Ganter--Wille for the antitone formal-concept/Galois-closure machinery; and
- Euler--Oleksik--Skupień, *Counting Maximal Distance-Independent Sets in
  Grid Graphs* (2013), DOI `10.7151/dmgt.1707`, Remark 2.2, for the classical
  maximal-independent-set recurrence on paths.

The draft-stage DOI `10.1016/j.jcss.2018.01.003` is rejected from the owner
record: it resolves to the unrelated Gutin--Reidl--Wahlström paper
*k-distinct in- and out-branchings in digraphs*.  The corrected 2017
Aracena--Richard--Salinas record and the direct Euler--Oleksik--Skupień path
owner are now the only identities carried forward.

The residual claim is narrowly the synchronous temporal conjunction
`F^3=F`, its one/two-cycle census and zeta, and the bipartite square law.
The checked sources did not contain that entire displayed conjunction, but
the underlying network is directly owned and the polarity mechanism is
classical.  Status:
`DIRECT_SYSTEM_COLLISION / BOUNDED_NO_EXACT_TEMPORAL_PACKAGE_FOUND`;
direct-owner risk is **high** and external release remains **HOLD**.

## Internal collision reconciliation

The ten within-batch pairs remain distinct in phase space, action, headline
invariant, and proof engine; the certificates are maintained in
[`../phase1/SYSTEM_COLLISION_FIREWALL.md`](../phase1/SYSTEM_COLLISION_FIREWALL.md).
The nearest historical neighbors currently disclosed by the papers/reviews
are P86 (primary) plus P97/P99/P87 for P102; P99/P97 for P103;
P91/P93/P101 for P104; P100 for P105; and P68/P75/P80 for P106.  These are
motif or background overlaps.  P106's
external direct-system collision is recorded separately and is not converted
into a claim of internal duplication.

## Release boundary

The audit is database- and query-bounded.  It cannot certify novelty or
priority, and a direct local-rule owner is already known for P106.  Every
manuscript and batch report must keep public circulation, submission, author
contact, and priority language on **HOLD** until an authorized specialist
review closes the owner gates.  The two internal hostile-review passes and
the batch integrity pass are complete; neither closes those external owner
gates.
