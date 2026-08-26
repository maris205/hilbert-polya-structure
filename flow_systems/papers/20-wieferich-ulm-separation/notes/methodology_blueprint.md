# Paper 20 methodology blueprint

Date: **2026-08-24**
Design: **theorem-first arithmetic investigation with bounded exact computation**

## Frozen inputs

- Paper 15's exact definition of `kappa_r(p)` and bare compact-group
  classification.
- Rational primes `p,q,r`; no marked or dynamical enhancement.
- A pre-registered finite search range used only for falsification and lemma
  discovery.

## Method

1. Expand one-coordinate equality into exact valuation and
   multiplicative-order statements, separately for exceptional coordinates.
2. Partition prime pairs into natural arithmetic classes suggested by
   reciprocity, congruence, or Kummer data.
3. Search for the weakest infinite-class separation lemma; do not begin with
   global injectivity as a proof obligation.
4. Use bounded computations to locate minimal separating coordinates,
   collisions, and counterexamples to candidate lemmas.
5. For a surviving lemma, freeze its extension/character/conjugacy-class
   owner and prove the required coordinate inequality.
6. If separation cannot be proved, test whether the obstruction itself gives
   a rigorous finite-collision or local-indistinguishability theorem.

## Controls

- `p=q` must give identical signatures;
- symmetry under swapping `p,q`;
- the known `p=2,q=3,r=11` separation from Paper 15;
- independent computation of local orders and valuations;
- increasing-range stability reports that explicitly remain non-theorems;
- adversarial pairs sharing many initial coordinates.

## Failure modes

- finite data is promoted to universal injectivity;
- a coordinate formula is evaluated outside its branch assumptions;
- Chebotarev supplies occurrence but not the desired inequality;
- a theorem merely restates `B_p ~= B_q iff kappa(p)=kappa(q)`;
- an arithmetic signature is mislabeled as packet or Route data.

## Validation

- independent implementations of the bounded arithmetic screen;
- exact integer/cyclotomic checks rather than floating point;
- proof review separating experimental, conditional, and unconditional lines;
- explicit failed-lemma ledger and counterexample retention;
- maximum-prior comparison with Wieferich and multiplicative-order literature.

## Expected output and effort

The Phase-2 arithmetic/source screen is complete.  It found an exact
fixed-finite-coordinate density corollary but no surviving standalone
infinite-class program.  Preserve the result for Paper 15, obtain the 2023
near-neighbor full text before novelty wording, and do not open an independent
Paper-20 proof or composition phase.
