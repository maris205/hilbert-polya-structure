# HCS-C31 validation report

The independent checker passes 6/6 gates:

1. exact envelope key sets and canonical payload hash;
2. byte locks for nine R058/R059/instability inputs, including the actual
   cutoff-20 root ledger, frozen protocol, summary, and independent audit;
3. type-strict W=13, chronology, interval, and rounding protocol;
4. independent reconstruction of 714 nodes, 1156 edges, and all direct
   cylinder Jacobian intervals;
5. independent rational log/exp weights and both strict Collatz signs;
6. claim-scope and Route-A firewall.

The checker does not import the producer and imports no NumPy, SciPy, or
mpmath. It accepts the producer's two integer vectors only after recomputing
the theorem-critical matrices and ratios. The verified machine record is
`c31_independent_check.json`.
