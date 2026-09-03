# C351: Open Jackson networks and external quasi-reversibility

This package proves one complete theorem for a finite open single-class
Jackson network of \(M/M/1\) nodes:

- the unique traffic solution and the exact stability criterion;
- the unique product-geometric invariant probability;
- the complete stationary time-reversed Jackson parameters, with zero reverse
  exogenous rates admitted when a forward node has no direct exit;
- jointly independent external Poisson departure streams and the correct
  past-departure/current-state independence direction;
- critical, overloaded, singleton, independent, tandem, and no-direct-exit
  boundaries.

The 12 exact rational networks and their 1,134 evidence rows are regression
receipts. The infinite-state and process-level assertions are proved in
THEOREM_PACKAGE.md and the paper. Those proofs explicitly invoke the
irreducible conservative CTMC invariant-probability lemma and identify only the
visible marked-jump reversal; phantom self-routing marks are state preserving
and do not affect the external-output theorem.

Run from this directory:

    python -B code/c351_jackson_producer.py
    python -B code/c351_jackson_checker.py
    python -B code/c351_jackson_sympy_crosscheck.py
    python -B code/c351_jackson_replay.py
    python -B code/c351_jackson_mutation.py
    python -B code/c351_release_manifest.py

Route-A result:
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL), overall
ROUTE_A_REJECTED; Route B is false. No target arithmetic local data,
Euler factor, root number, automorphy, target divisor, target zero match, or
Hilbert--Pólya operator is claimed.
