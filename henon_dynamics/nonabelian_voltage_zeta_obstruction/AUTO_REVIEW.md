# Adversarial review record

Date: 2026-08-07

## Release ruling

Two independent reviewers audited the proof chain, representation theory,
code certificates, novelty boundary, Route-A record, and compiled paper.
Round one found no false main theorem but required a focused major revision.
After revision:

- proof audit: FINAL ACCEPT;
- hostile senior review: 8.7/10;
- remaining mathematical, novelty, citation, proof, and reproducibility
  issues: none;
- remaining release action at review time: append a new Route-A evaluation
  with real Git provenance while preserving the original record.

The provenance action is completed in the append-only Route-A record
evaluations/route_a/hcs_c15/20260807T032927Z.yaml, which cites frozen
source/code commit f519609e32362a4113d84a8e55772c38c53c84da.

## Changes made between rounds

The revision:

1. defined the full Schrödinger representation
   \(\rho_m(a,b,c)=\omega_m^cV_m^bU_m^a\);
2. verified the Heisenberg group law, unitarity, scalar commutant,
   irreducibility, exact conductor, bouquet-cover Artin block, and
   level-new cancellation statement;
3. proved \(\lambda_{\max}(H_m)<4\) at every finite level;
4. added the closest finite-ring Heisenberg/Harper sources and narrowed the
   novelty claim to the conductor-resolved Rayleigh certificate and its
   frozen new-sector-gap use;
5. narrowed the tower conclusion so it does not exclude every renormalized
   infinite determinant or subtraction scheme;
6. completed the nine mandatory A2 metric fields in the revised Route-A
   record;
7. extended the independent word checker and added a direct modulus-nine
   Weyl/group-law/scalar-commutant test;
8. added an exact Fraction certificate at \(q=243\);
9. clarified the common orbit weight, left/right regular convention, Jensen
   boundary radii, complex affine spectral maps, and the positive-height
   Riemann--von Mangoldt normalization;
10. pinned Python 3.12.3 and SymPy 1.14.0.

## Round-one proof audit: raw response

~~~text
Verdict: all six core mathematical claims are correct; I found no counterexample or false theorem. The six regression tests pass. The needed corrections are mostly proof-completeness and certificate-scope issues.

- Schrödinger irreducibility is omitted from the paper. paper/sections/5_tower.tex defines the Weyl pair and proves only non-descent via the central character. To justify “primitive nonabelian sector,” add the argument already present in DERIVATION_PACKAGE.md: V_m has q_m distinct eigenspaces and U_m permutes them transitively, so any U_m,V_m-invariant subspace is 0 or the whole space. Also explicitly state the map x maps to U_m, y maps to V_m, z maps to exp(-2 pi i/q_m) I.

- Strictness at finite level is asserted but not proved. Add: equality in <f,H_m f> <= 4||f||^2 forces U_m f=f=V_m f, impossible under U_m V_m=zeta V_m U_m with zeta not equal to 1. Equivalently, connectedness/Perron--Frobenius makes eigenvalue 4 occur only in the trivial representation.

- The claimed “independent” certification of the full H7 proposition is overstated. independent_check.py independently checks bigrams, holonomies/conjugacy classes, and regular-cycle lengths, but not cyclic reduction, primitivity, non-dihedrality, or noninverse holonomy. Either extend the independent checker or narrow the introduction’s claim.

- One code comment is literally false: voltage_zeta.py says the two holonomies act by “opposite” roots of unity. Their exponents are -3k and -2k, which are distinct, not opposite. The generated phase ledger is correct; replace “opposite” by “distinct.”

- The rational q=243 certificate is mathematically correct but not machine-certified. Explicitly,
  60/31 + 2 - 1000/6561 = 769442/203391,
  and its excess over 7/2 is 115147/406782 > 0.
  Consider an exact Fraction assertion. Likewise, result-field bass_roots belongs to the abelian branch, not the Schrödinger lambda_max.

- Minor regular-representation convention issue: paper/sections/3_aggregation.tex writes the usual left-regular irrep decomposition but then invokes right multiplication. The determinant formula remains correct because either multiplication has |G|/o cycles and dual irreps merely reindex the product. Say “left multiplication,” or explicitly mention the dual/reindexing convention.

- Minor Jensen hygiene: paper/sections/4_zero_density.tex is correct, including finite meromorphic quotients, provided every entry uses finitely many positive real exponents with s-independent coefficients. State that explicitly in the generalized-entry clause, handle possible zeros on the Jensen outer circle by a limiting radius, and define quotient divisor count after cancellation. Also clarify that the displayed Riemann--von Mangoldt normalization counts positive-height zeros; the manuscript’s symmetric strip count is twice this up to O(1), which does not affect the Theta(T log T) contradiction.

Confirmed without correction: the regular-minus-trivial factor, both H7 holonomies and complete bigram ledger, non-dihedral/primitivity claims, the Jensen O(T) conclusion for finite products/quotients, the q=243 Rayleigh inequality, and Bass-root convergence to 1/3 and 1.
~~~

## Round-one hostile senior review: raw response

~~~text
Verdict: ALMOST — reject in the present form, invite a focused major revision.
Score: 6.8/10.

I found no false main theorem. The obstruction package is mathematically sound in outline, the chronology certificate is correct, the Jensen argument works, and the Bass-root calculation is correct. However, the manuscript is not yet ready to present as a completed paper because its most “new” theorem skips a necessary representation-theoretic step and the novelty audit omits the closest prior work.

Critical issues

1. The primitive exact-conductor Schrödinger sector is asserted, not established.

Section 5 jumps from a Weyl pair U_m,V_m to “the corresponding primitive central-character adjacency block.” For the theorem to concern a genuine nonabelian Artin/Fourier sector, the paper must explicitly:

- put omega_m=exp(-2 pi i/q_m);
- define rho_m(a,b,c)=omega_m^c V_m^b U_m^a;
- verify the Heisenberg group law using U_m V_m=omega_m V_m U_m;
- prove irreducibility;
- prove exact conductor using rho_m(z^(q_m/3))=exp(-2 pi i/3)I not equal to I;
- explain why this full-group Fourier block is an Artin sector for the cover of the two-loop bouquet, and why non-factor-through blocks remain in the level-new quotient after the old blocks cancel.

2. The novelty audit misses the closest prior source.

The exact irreducible representations of H(Z/p^n Z), their p^n-dimensional blocks, and the associated Harper matrices are already written down in DeDeo et al., “Spectra of Heisenberg graphs over finite rings,” especially its representation proposition and Hofstadter-block discussion.

It should also acknowledge Béguin--Valette--Żuk, “On the spectrum of a random walk on the discrete Heisenberg group and the norm of Harper’s operator.”

The defensible novelty claim is therefore an explicit conductor-resolved Rayleigh certificate and its use as a frozen Hilbert--Pólya/new-sector-gap obstruction, not a new discovery of the primitive Schrödinger block or of its near-zero-flux spectral-edge behavior.

3. “Closing the Heisenberg tower” is too strong.

The theorem proves failure of the uniform Ramanujan/new-sector-gap rescue under the registered normalization. It does not prove that no renormalized infinite determinant, subtraction scheme, or other tower limit can exist.

Major process issue

The Route-A verdict is substantively correct:
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT).

But the YAML omits all nine mandatory A2 metric names: zero_error_train, zero_error_validation, zero_error_test, extra_zero_count, missing_zero_count, root_count_discrepancy, cutoff_drift, precision_drift, control_margin. They may be recorded as NOT_APPLICABLE_ANALYTIC_REJECTION, but the exact schema names should be present. source_commit and code_commit must also be replaced with real commit hashes when synchronized.

Minor mathematical and exposition fixes

- Avoid Jensen boundary zeros by an admissible outer radius or limiting form.
- State the scope of affine spectral identification.
- Prove lambda_max(H_m)<4 at finite level.
- Identify x as the common unit-roof weight u^10, or a weight depending only on the matched ledger.
- Distinguish the bouquet cover from X_m to X_(m-1).
- Pin Python 3.12.3 and SymPy 1.14.0.
- Add a direct small-q Weyl/group-relation/scalar-commutant test.

Checks that passed

- The regular-minus-trivial local formula is correct.
- The two length-ten words have the stated bigram ledgers, are primitive and non-dihedrally equivalent, and have holonomies z^3,z^2.
- The Jensen zero-density argument gives O(T) as claimed.
- The q=243,L=15 rational bound is valid and exceeds 7/2>2 sqrt(3).
- The Bass roots converge to 1/3 and 1.
- All six original tests pass.
- Regenerated JSON/CSV artifacts are byte-for-byte identical.
- The original 12-page paper compiles cleanly.
~~~

## Round-two proof audit: raw response

~~~text
FINAL ACCEPT
~~~

## Round-two hostile senior review: raw response

~~~text
Score: 8.7/10
Verdict: ALMOST — mathematically ready; repository release still conditional.

Remaining critical issues: None.

Remaining major issue: Route-A provenance is still incomplete: source_commit and code_commit remain NOT_A_GIT_WORKTREE. Also, the revised evidence appears to have overwritten the original timestamped YAML instead of creating a new evaluation version, contrary to the Route-A accumulation protocol. Create a newly timestamped evaluation after committing, record the real commit hash, and preserve the previous evaluation if recoverable.

No remaining major mathematical, novelty, citation, proof, or reproducibility defects were found. All nine tests pass, generated artifacts reproduce exactly, and the 13-page paper compiles cleanly.
~~~
