# Experiment Plan

## Evidentiary hierarchy

The all-period claims are proofs.  The registered computation is a
development-seen reproduction, code falsification, and finite ledger only.
It cannot establish the all-period equality residue.

## Stage P0: immutable preflight

- Validate the exact source-lock JSON and its SHA-256.
- Recompute every upstream binding.
- Verify the cubic relation, 2-Eisenstein criterion, unique real root,
  critical portrait, and \(2=u^3/(u^2-u+1)\).
- Scan all runnable code for forbidden network, prime/zero target, floating
  matching, and dynamic-import paths.

Any failure stops execution.

## Stage P1: proof-contract audit

The implementation must encode, test, and report the exact identities used by
Theorems A--B and Lemmas C--E.  A static proof contract is not itself a proof;
it prevents the code and manuscript from silently changing the equations or
scope after review.

Required symbolic checks include:

- multiplier factorization \(\Lambda=2^nB_n\);
- the PCF orbit and fixed point;
- the cycle-polynomial functional identity;
- Frobenius reduction \(g^n-X\equiv X^{2^n}-X\pmod u\) and squarefreeness;
- the mod-2 lift \(z_\alpha\equiv\alpha+u+u^2\);
- enumeration of exact degree-two and degree-three finite-field obstructions;
- an exact degree-four witness showing the two-coefficient filter is not
  sufficient.

## Stage P2: controls-only

Run all four source-locked dynamical controls plus the upstream regression
before the frozen candidate.  The control
runner and candidate runner must share the exact-period, cycle-product, gcd,
and resultant engines.  Controls are required to exercise both equality
signs, a no-hit target, and formal-period pollution.

## Stage P3: independent deployment review

An independent reviewer binds its verdict to the source-lock and code-tree
hashes.  It must attack exact-period saturation, repeated roots, target
specialization, resultant/norm semantics, JSON parsers, forbidden-data scan,
and result-manifest closure.  Only `DEPLOYMENT_PASS` unlocks P4.

## Stage P4: registered exact reproduction

For each \(n=2,\ldots,7\):

1. Compute \(F_n=g^n-X\) and the formal dynatomic polynomial by exact Mobius
   division.
2. Define the set-theoretic exact-period component by the frozen formula
   \[
   \Psi_n^{\rm set}=
   \frac{\operatorname{rad}(F_n)}
   {\gcd\!\left(\operatorname{rad}(F_n),
   \prod_{d\mid n,\ d<n}\operatorname{rad}(F_d)\right)},
   \]
   normalized to be monic.  Formal dynatomic and scheme multiplicities are
   recorded separately and never replace this least-period root set.
3. Verify squarefreeness (or retain scheme multiplicity),
   \(n\mid\deg\Psi_n^{\rm set}\), and
   \(B_n\circ g\equiv B_n\pmod{\Psi_n^{\rm set}}\).
4. For \(\varepsilon=\pm1\), compute
   \(\gcd(\Psi_n^{\rm set},B_n-\varepsilon)\).
5. Independently compute the target resultant, reduce it in
   \(\mathbb Q(u)\), and certify its exact nonzero rational field norm.  A
   reduction modulo the predeclared prime \(q=3\) may be reported only as an
   optional diagnostic and is never chosen after seeing the result.
6. Stop immediately on any hit or disagreement.

Periods 2--7 were observed before the lock.  Their output is labeled
`DEVELOPMENT_SEEN_REPRODUCTION`, never validation or test.

## Stage P5: analysis and closure

Generate strict JSON records, a human result report, validation report,
experiment tracker update, JUnit output, and a hash manifest.  Required final
labels are:

- `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`;
- `BASE2_EQUALITY_ABSENT_N2_N3_BY_LOCAL_THEOREM`;
- either finite equality hit with exact certificate, or
  `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`;
- `BASE2_EQUALITY_ALL_PERIODS_OPEN_N_GE_4`;
- `ROUTE_A_NOT_ADVANCED / ROUTE_B_NOT_OPENED`.

## Resource and failure policy

No GPU or network is used.  Resource failure is reported as
`NOT_EXECUTED_RESOURCE_LIMIT`; the period cutoff may not be reduced after
inspection.  No result author may independently approve their own deployment
or manuscript.
